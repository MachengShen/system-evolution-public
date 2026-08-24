"""Frozen D4 v0.2 W_set^perp estimator.

NumPy only. The independent statistical unit is always a seed.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
import hashlib
import json
from typing import Iterable

import numpy as np


ESTIMATOR_VERSION = "d4-wsetperp-v0.2.0"


class EstimatorError(ValueError):
    """A contract violation that makes the result RIG-UNDECIDED."""


@dataclass(frozen=True)
class Observation:
    seed: int
    arm: str
    path: str
    control: float
    members: tuple[int, ...]
    scalar_size: int
    ridge_readout: float
    echo_readout: float
    row_index: int

    def validate(self, n_channels: int) -> None:
        if self.path not in {"up", "down"}:
            raise EstimatorError(f"invalid path {self.path!r}")
        if len(self.members) != n_channels:
            raise EstimatorError("member vector has wrong length")
        if any(v not in (0, 1) for v in self.members):
            raise EstimatorError("members must be binary")
        if sum(self.members) != self.scalar_size:
            raise EstimatorError("scalar_size must equal sum(members)")


def stable_hash(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def match_scalar(
    observations: Iterable[Observation],
    *,
    n_channels: int,
    min_pairs: int = 4,
) -> dict[int, list[tuple[Observation, Observation]]]:
    """Exact integer-|mu| matching with deterministic rank pairing.

    Counts must agree within every retained scalar stratum. Refusal is safer
    than selecting a favorable subset after observing membership identities.
    """
    grouped: dict[tuple[int, int, str], list[Observation]] = defaultdict(list)
    seen_arm: str | None = None
    for row in observations:
        row.validate(n_channels)
        if seen_arm is None:
            seen_arm = row.arm
        elif row.arm != seen_arm:
            raise EstimatorError("match_scalar accepts exactly one arm")
        grouped[(row.seed, row.scalar_size, row.path)].append(row)

    seeds = sorted({key[0] for key in grouped})
    matched: dict[int, list[tuple[Observation, Observation]]] = {}
    for seed in seeds:
        pairs: list[tuple[Observation, Observation]] = []
        sizes = sorted({key[1] for key in grouped if key[0] == seed})
        for scalar_size in sizes:
            up = sorted(
                grouped.get((seed, scalar_size, "up"), []),
                key=lambda x: (x.control, x.row_index),
            )
            down = sorted(
                grouped.get((seed, scalar_size, "down"), []),
                key=lambda x: (x.control, x.row_index),
            )
            if len(up) != len(down):
                raise EstimatorError(
                    f"seed {seed} scalar {scalar_size}: unequal up/down counts"
                )
            pairs.extend(zip(up, down))
        if len(pairs) < min_pairs:
            raise EstimatorError(
                f"seed {seed}: retained {len(pairs)} pairs, need {min_pairs}"
            )
        matched[seed] = pairs
    if not matched:
        raise EstimatorError("no matched seeds")
    return matched


def difference_matrix(
    matched: dict[int, list[tuple[Observation, Observation]]],
) -> np.ndarray:
    rows = []
    for seed in sorted(matched):
        for up, down in matched[seed]:
            rows.append(np.asarray(up.members, float) - np.asarray(down.members, float))
    return np.asarray(rows, dtype=float)


def fit_projection(
    matched_train: dict[int, list[tuple[Observation, Observation]]],
) -> np.ndarray:
    """Fit the through-origin rank-1 L2-optimal projection on train seeds."""
    d = difference_matrix(matched_train)
    if not np.any(d):
        raise EstimatorError("projection training matrix is all zero")
    _, _, vt = np.linalg.svd(d, full_matrices=False)
    v = np.asarray(vt[0], dtype=float)
    pivot = int(np.argmax(np.abs(v)))
    if v[pivot] < 0:
        v = -v
    norm = np.linalg.norm(v)
    if not np.isfinite(norm) or norm <= 0:
        raise EstimatorError("invalid projection direction")
    return v / norm


def score_heldout(
    matched_test: dict[int, list[tuple[Observation, Observation]]],
    projection: np.ndarray,
) -> dict:
    """Score coherent held-out residual; preserve raw Hamming as diagnostics."""
    n_channels = int(projection.size)
    seed_rows = []
    for seed in sorted(matched_test):
        d = np.asarray(
            [
                np.asarray(up.members, float) - np.asarray(down.members, float)
                for up, down in matched_test[seed]
            ]
        )
        residual = d - np.outer(d @ projection, projection)
        coherent = residual.mean(axis=0)
        score = float(np.abs(coherent).sum())
        raw_hamming = float(np.abs(d).sum(axis=1).mean())
        seed_rows.append(
            {
                "seed": int(seed),
                "n_pairs": int(d.shape[0]),
                "w_set_perp": score,
                "w_set_perp_normalized": score / n_channels,
                "raw_mean_hamming": raw_hamming,
            }
        )
    vals = np.asarray([r["w_set_perp"] for r in seed_rows], float)
    return {
        "n_seeds": int(vals.size),
        "n_channels": n_channels,
        "seed_scores": seed_rows,
        "mean": float(vals.mean()),
        "sd": float(vals.std(ddof=1)) if vals.size > 1 else None,
        "normalized_mean": float(vals.mean() / n_channels),
    }


def bootstrap_ci(
    values: Iterable[float], *, n_boot: int = 10_000, seed: int = 20260825
) -> list[float]:
    vals = np.asarray(list(values), dtype=float)
    if vals.size < 2:
        raise EstimatorError("seed bootstrap needs at least two seeds")
    rng = np.random.default_rng(seed)
    ix = rng.integers(0, vals.size, size=(n_boot, vals.size))
    means = vals[ix].mean(axis=1)
    lo, hi = np.quantile(means, [0.025, 0.975])
    return [float(lo), float(hi)]


def paired_effect(a: Iterable[float], b: Iterable[float]) -> dict:
    va = np.asarray(list(a), dtype=float)
    vb = np.asarray(list(b), dtype=float)
    if va.shape != vb.shape or va.size < 2:
        raise EstimatorError("paired effect needs equal arrays with n >= 2")
    d = va - vb
    sd = float(d.std(ddof=1))
    mean = float(d.mean())
    dz = float(mean / sd) if sd > 0 else (float("inf") if mean > 0 else 0.0)
    rng = np.random.default_rng(20260825)
    signs = rng.choice((-1.0, 1.0), size=(20_000, d.size))
    null = np.abs((signs * d).mean(axis=1))
    p = float((1 + np.count_nonzero(null >= abs(mean) - 1e-15)) / (null.size + 1))
    return {"mean_difference": mean, "dz": dz, "p_sign_flip": p, "n": int(d.size)}


def attach_interval(score: dict) -> dict:
    vals = [row["w_set_perp"] for row in score["seed_scores"]]
    return {**score, "ci95_seed_bootstrap": bootstrap_ci(vals)}
