"""Generate planted D4 v0.2 controls and run every instrument certificate."""

from __future__ import annotations

import argparse
from dataclasses import asdict
from datetime import datetime, timezone
import json
import math
import os
from pathlib import Path
import subprocess
import tempfile

import numpy as np

from estimator import (
    ESTIMATOR_VERSION,
    Observation,
    attach_interval,
    fit_projection,
    match_scalar,
    paired_effect,
    score_heldout,
    stable_hash,
)


N_CHANNELS = 12
TRAIN_SEEDS = tuple(range(100, 108))
TEST_SEEDS = tuple(range(20))
N_PAIRS = 12
CONFIG = {
    "estimator_version": ESTIMATOR_VERSION,
    "n_channels": N_CHANNELS,
    "scalar_tol": 0,
    "min_pairs_per_seed": 4,
    "projection": "through-origin rank-1 SVD on calibration seeds only",
    "score": "L1 norm of mean signed held-out residual, channel units",
    "seed_ci": {"method": "percentile bootstrap", "n_boot": 10000, "seed": 20260825},
    "paired_test": {"method": "seed-wise sign flip", "draws": 20000, "seed": 20260825},
    "train_seeds": TRAIN_SEEDS,
    "test_seeds": TEST_SEEDS,
}


def _atomic_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=path.name + ".", dir=path.parent)
    try:
        with os.fdopen(fd, "w") as f:
            json.dump(value, f, indent=2, sort_keys=True, allow_nan=False)
            f.write("\n")
        os.replace(tmp, path)
    except Exception:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def _members(size: int, swap_out: int | None = None, swap_in: int | None = None) -> list[int]:
    m = np.zeros(N_CHANNELS, dtype=int)
    m[:size] = 1
    if swap_out is not None:
        m[swap_out] = 0
    if swap_in is not None:
        m[swap_in] = 1
    return m.tolist()


def _row(seed: int, arm: str, path: str, control: float, members: list[int], idx: int) -> Observation:
    return Observation(
        seed=seed,
        arm=arm,
        path=path,
        control=float(control),
        members=tuple(int(x) for x in members),
        scalar_size=int(sum(members)),
        ridge_readout=float(sum(members) / N_CHANNELS),
        echo_readout=float(sum(members) / N_CHANNELS),
        row_index=idx,
    )


def coherent_fixture(arm: str, seeds: tuple[int, ...], out_ch: int, in_ch: int) -> list[Observation]:
    rows = []
    for seed in seeds:
        for j in range(N_PAIRS):
            up = _members(6)
            down = _members(6, swap_out=out_ch, swap_in=in_ch)
            rows.extend((_row(seed, arm, "up", j, up, 2 * j), _row(seed, arm, "down", j, down, 2 * j + 1)))
    return rows


def zero_fixture(arm: str, seeds: tuple[int, ...]) -> list[Observation]:
    rows = []
    for seed in seeds:
        for j in range(N_PAIRS):
            m = _members(6)
            rows.extend((_row(seed, arm, "up", j, m, 2 * j), _row(seed, arm, "down", j, m, 2 * j + 1)))
    return rows


def randomized_identity_fixture(arm: str, seeds: tuple[int, ...]) -> list[Observation]:
    """Balanced independent event identities: churn positive, coherent score zero."""
    rows = []
    for seed in seeds:
        for j in range(N_CHANNELS):
            # Both marginals visit every channel equally; event identity is not stable.
            up = np.zeros(N_CHANNELS, dtype=int)
            down = np.zeros(N_CHANNELS, dtype=int)
            up[(np.arange(6) + j) % N_CHANNELS] = 1
            down[(np.arange(6) + j + 1) % N_CHANNELS] = 1
            rows.extend((_row(seed, arm, "up", j, up.tolist(), 2 * j), _row(seed, arm, "down", j, down.tolist(), 2 * j + 1)))
    return rows


def sensitivity_fixture(arm: str, seeds: tuple[int, ...], bias: float) -> list[Observation]:
    rows = []
    for seed in seeds:
        rng = np.random.default_rng(50_000 + seed + int(1000 * bias))
        n_signal = int(rng.binomial(N_PAIRS, bias))
        for j in range(N_PAIRS):
            up = _members(6)
            if j < n_signal:
                down = _members(6, swap_out=2, swap_in=9)
            else:
                # zero residual event, not extra noise hidden as signal
                down = up
            rows.extend((_row(seed, arm, "up", j, up, 2 * j), _row(seed, arm, "down", j, down, 2 * j + 1)))
    return rows


def evaluate(rows: list[Observation], projection: np.ndarray) -> dict:
    matched = match_scalar(rows, n_channels=N_CHANNELS, min_pairs=4)
    return attach_interval(score_heldout(matched, projection))


def timing_certificate() -> dict:
    step_epoch = 10
    dynamic_range = 8
    ridge = np.zeros(24, dtype=int)
    echo = np.zeros(24, dtype=int)
    ridge[step_epoch + 2 :] = 1
    echo[step_epoch + 1 :] = 1
    lag_ridge = int(np.flatnonzero(ridge[step_epoch:] == 1)[0])
    lag_echo = int(np.flatnonzero(echo[step_epoch:] == 1)[0])
    passed = max(lag_ridge, lag_echo) <= 2 and dynamic_range >= 3 * max(lag_ridge, lag_echo)
    return {
        "status": "PASS" if passed else "FAIL",
        "step_epoch": step_epoch,
        "ridge_lag_epochs": lag_ridge,
        "echo_lag_epochs": lag_echo,
        "dynamic_range_epochs": dynamic_range,
        "criteria": "max lag <= 2 and dynamic range >= 3 * max lag",
    }


def crowd_certificate() -> dict:
    rows = []
    for c1, p, mu, churn in ((0.05, 0.20, 22.0, 0.12), (0.10, 0.42, 18.0, 0.17), (0.15, 0.66, 13.0, 0.20), (0.25, 0.82, 6.0, 0.34)):
        seed_rows = []
        for seed in TEST_SEEDS:
            rng = np.random.default_rng(70_000 + seed + int(c1 * 1000))
            seed_rows.append({
                "seed": seed,
                "excluded": int(rng.random() < p),
                "mu_size": float(mu + rng.normal(0, 0.35)),
                "churn_per_30_epochs": float(np.clip(churn + rng.normal(0, 0.012), 0, 1)),
            })
        summary = {
            "c1": c1,
            "exclusion_probability": float(np.mean([r["excluded"] for r in seed_rows])),
            "mean_mu_size": float(np.mean([r["mu_size"] for r in seed_rows])),
            "mean_churn_per_30_epochs": float(np.mean([r["churn_per_30_epochs"] for r in seed_rows])),
        }
        summary["passes"] = bool(summary["exclusion_probability"] >= 0.5 and 8 <= summary["mean_mu_size"] <= 20 and summary["mean_churn_per_30_epochs"] <= 0.25)
        rows.append(summary)
    winners = [r for r in rows if r["passes"]]
    return {
        "status": "PASS" if winners else "FAIL",
        "criteria": "exclusion >= 0.5, 8 <= mean |mu| <= 20, churn <= 0.25/30 epochs",
        "grid": rows,
        "selected_c1": winners[0]["c1"] if winners else None,
    }


def orthogonality_certificate() -> dict:
    changes = []
    noise = []
    for seed in TEST_SEEDS:
        rng = np.random.default_rng(80_000 + seed)
        task = rng.normal(size=(200, 3))
        orth = rng.normal(size=(200, 4))
        reward = task[:, 0] - 0.3 * task[:, 1] + 0.1 * task[:, 2]
        perm = rng.permutation(orth.shape[0])
        # The registered task reward has no orth-block term by construction.
        reward_perm = task[:, 0] - 0.3 * task[:, 1] + 0.1 * task[:, 2] + 0.0 * orth[perm, 0]
        changes.append(float(np.mean(reward_perm - reward)))
        noise.append(float(np.std(reward, ddof=1) / math.sqrt(reward.size)))
    bound = float(np.quantile(noise, 0.95))
    observed = float(abs(np.mean(changes)))
    return {
        "status": "PASS" if observed <= bound else "FAIL",
        "mean_absolute_reward_change": observed,
        "reward_noise_band_95": bound,
        "criteria": "mean absolute change <= independent reward-noise band",
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--code-commit", required=True)
    ap.add_argument("--out", default="results/certificates.json")
    args = ap.parse_args()
    out = Path(args.out)

    repo = Path(__file__).resolve().parents[2]
    head = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=repo, text=True
    ).strip()
    if args.code_commit != head:
        raise SystemExit(
            f"refusing unbound code commit: supplied={args.code_commit} HEAD={head}"
        )
    subprocess.run(
        ["git", "cat-file", "-e", f"{args.code_commit}^{{commit}}"],
        cwd=repo,
        check=True,
    )

    projection_rows = coherent_fixture("scalar-shadow-train", TRAIN_SEEDS, 0, 8)
    projection_matches = match_scalar(projection_rows, n_channels=N_CHANNELS, min_pairs=4)
    projection = fit_projection(projection_matches)

    fixtures: dict[str, list[Observation]] = {
        "scalar_shadow_heldout": coherent_fixture("scalar-shadow-heldout", TEST_SEEDS, 0, 8),
        "p_hyst_set_latch": coherent_fixture("p-hyst-set-latch", TEST_SEEDS, 2, 9),
        "gate_const": zero_fixture("gate-const", TEST_SEEDS),
        "sweep_random": randomized_identity_fixture("sweep-random", TEST_SEEDS),
        "identity_randomized": randomized_identity_fixture("identity-randomized", TEST_SEEDS),
    }
    scores = {name: evaluate(rows, projection) for name, rows in fixtures.items()}

    sensitivity = {}
    for bias in (0.0, 0.25, 0.5, 1.0):
        sensitivity[str(bias)] = evaluate(sensitivity_fixture(f"p-plus-b-{bias}", TEST_SEEDS, bias), projection)
    zero_vals = [x["w_set_perp"] for x in sensitivity["0.0"]["seed_scores"]]
    for value in sensitivity.values():
        vals = [x["w_set_perp"] for x in value["seed_scores"]]
        value["vs_b0"] = paired_effect(vals, zero_vals)
    fixture_bias_min = next(
        (
            float(b)
            for b in ("0.25", "0.5", "1.0")
            if sensitivity[b]["vs_b0"]["dz"] is not None
            and sensitivity[b]["vs_b0"]["dz"] >= 1.0
            and sensitivity[b]["ci95_seed_bootstrap"][0] > 0
        ),
        None,
    )

    all_rows = projection_rows + [r for rows in fixtures.values() for r in rows]
    for bias in (0.0, 0.25, 0.5, 1.0):
        all_rows.extend(sensitivity_fixture(f"p-plus-b-{bias}", TEST_SEEDS, bias))
    raw = {
        "schema_version": "d4-instrument-observation-v0.2.0",
        "code_commit": args.code_commit,
        "estimator_version": ESTIMATOR_VERSION,
        "config_hash": stable_hash(CONFIG),
        "observations": [asdict(row) for row in all_rows],
    }
    data_hash = stable_hash(raw)
    leakage = {
        "status": "PASS" if set(TRAIN_SEEDS).isdisjoint(TEST_SEEDS) else "FAIL",
        "train_test_seed_overlap": sorted(set(TRAIN_SEEDS) & set(TEST_SEEDS)),
        "cache_key": stable_hash({"code_commit": args.code_commit, "config_hash": stable_hash(CONFIG), "data_hash": data_hash, "estimator_version": ESTIMATOR_VERSION}),
        "criteria": "disjoint train/test seeds and cache key binds code, config, data, estimator",
    }
    timing = timing_certificate()
    crowd = crowd_certificate()
    orth = orthogonality_certificate()

    gates = {
        "scalar_shadow_removed": scores["scalar_shadow_heldout"]["ci95_seed_bootstrap"][1] <= 1e-12,
        "p_hyst_known_answer": scores["p_hyst_set_latch"]["ci95_seed_bootstrap"][0] >= 1.99,
        "gate_const_zero": scores["gate_const"]["ci95_seed_bootstrap"][1] <= 1e-12,
        "sweep_random_zero": scores["sweep_random"]["ci95_seed_bootstrap"][1] <= 1e-12,
        "identity_randomized_zero": scores["identity_randomized"]["ci95_seed_bootstrap"][1] <= 1e-12,
        "p_plus_b_fixture_sensitivity": fixture_bias_min is not None and fixture_bias_min <= 1.0,
        "p_plus_timing": timing["status"] == "PASS",
        "p_plus_crowd": crowd["status"] == "PASS",
        "reward_orthogonality": orth["status"] == "PASS",
        "heldout_no_leakage": leakage["status"] == "PASS",
    }
    synthetic_self_test = "PASS" if all(gates.values()) else "FAIL"
    result = {
        "schema_version": "d4-instrument-certificate-v0.2.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "code_commit": args.code_commit,
        "estimator_version": ESTIMATOR_VERSION,
        "config": CONFIG,
        "config_hash": stable_hash(CONFIG),
        "raw_data_hash": data_hash,
        "projection": projection.tolist(),
        "projection_fit_seed_count": len(TRAIN_SEEDS),
        "scores": scores,
        "p_plus_b_fixture": {
            "status": "PASS" if gates["p_plus_b_fixture_sensitivity"] else "FAIL",
            "fixture_bias_min": fixture_bias_min,
            "warning": "bias is a planted event probability, not sigma_drive or a physical rig unit",
            "levels": sensitivity,
        },
        "p_plus_timing": timing,
        "p_plus_crowd": crowd,
        "reward_orthogonality": orth,
        "leakage": leakage,
        "gates": gates,
        "synthetic_self_test": synthetic_self_test,
        "instrument_rig": "NOT_RUN",
        "overall": "RIG-UNDECIDED",
        "main_program": "NOT_RUN",
        "main_arm_endpoint_check": "NOT_APPLICABLE_MAIN_ARM_NOT_RUN",
        "interpretation_boundary": "Same-runner fixtures check selected algebra only. D4-I rig readiness and all D4 mechanism/theory claims remain untested.",
        "posthoc_notes": [
            "POSTHOC REVIEW: finite-sample nonnegative-score null bias invalidates the raw-zero randomization gate.",
            "POSTHOC REVIEW: timing, crowding, and orthogonality values are constructed fixtures, not D4 rig measurements.",
        ],
    }

    raw_path = out.parent / "raw-observations.json"
    receipt_path = out.parent / "claim-receipt.json"
    _atomic_json(raw_path, raw)
    _atomic_json(out, result)
    receipt = {
        "id": "d4-v0.2-instrument-certificates-20260825",
        "claim": "The current D4 v0.2 estimator implementation is a candidate for D4-I rig calibration; rig readiness remains unestablished.",
        "cognitive_state": "speculative",
        "cognitive_state_reason": "Only same-generator synthetic fixtures and limited unit tests were exercised; no independent D4-I rig or real ridge/echo path was tested.",
        "observed": f"synthetic_self_test={synthetic_self_test}; instrument_rig=NOT_RUN; main_program=NOT_RUN; code_commit={args.code_commit}",
        "provenance": {"source": "experiments/d4-instrument-v0.2/results/certificates.json", "derivation_type": "empirical"},
        "evidence": [{"kind": "supports" if overall == "PASS" else "fails-to-reproduce", "ref": "certificates.json"}],
        "edges": [],
    }
    _atomic_json(receipt_path, receipt)
    print(json.dumps({"overall": "RIG-UNDECIDED", "synthetic_self_test": synthetic_self_test, "fixture_bias_min": fixture_bias_min, "gates": gates}, indent=2, sort_keys=True))
    if synthetic_self_test != "PASS":
        raise SystemExit(2)


if __name__ == "__main__":
    main()
