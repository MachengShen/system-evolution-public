#!/usr/bin/env python3
"""Deterministic numerical checks for the gain-separation theory note.

These are model checks only. They are not evidence about physical integration,
agency, boundaries, or real-world systems.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


OUT = Path(__file__).with_name("results.json")


def assert_close(actual: float, expected: float, tol: float, label: str) -> None:
    if not math.isfinite(actual) or abs(actual - expected) > tol:
        raise AssertionError(
            f"{label}: actual={actual:.17g}, expected={expected:.17g}, tol={tol:g}"
        )


def normalized_reboost() -> dict:
    b = 3.0
    q0 = 0.2
    gains = (0.05, 0.2, 0.8)
    checkpoints = {20, 100, 1000}
    runs = {}
    max_identity_error = 0.0

    for g in gains:
        q = q0
        samples = {}
        previous = q
        for step in range(1, max(checkpoints) + 1):
            selected_after_boost = b * q / (1.0 + (b - 1.0) * q)
            q_next = (1.0 - g) * q + g * selected_after_boost
            observed_delta = q_next - q
            identity_delta = (
                g * (b - 1.0) * q * (1.0 - q)
                / (1.0 + (b - 1.0) * q)
            )
            error = abs(observed_delta - identity_delta)
            max_identity_error = max(max_identity_error, error)
            assert_close(observed_delta, identity_delta, 3e-16, "reboost delta identity")
            if q_next + 1e-15 < previous or q_next < 0.0 or q_next > 1.0 + 1e-15:
                raise AssertionError("reboost path must stay in [0,1] and be monotone")
            q = min(1.0, q_next)
            previous = q
            if step in checkpoints:
                samples[str(step)] = q

        if q < 1.0 - 1e-12:
            raise AssertionError(f"reboost failed convergence check for g={g}: q={q}")
        runs[str(g)] = {
            "q_by_step": samples,
            "q_1000_distance_to_one": 1.0 - q,
        }

    return {
        "model": "q_next=(1-g)q+g*b*q/(1+(b-1)q)",
        "parameters": {"b": b, "q0": q0, "gains": list(gains)},
        "identity": "delta=g*(b-1)*q*(1-q)/(1+(b-1)*q)",
        "max_abs_identity_error": max_identity_error,
        "runs": runs,
        "interpretation": (
            "For fixed b>1, every tested positive gain has the same attracting "
            "fixed point q=1; gain changes the approach rate."
        ),
    }


def anchored_target() -> dict:
    q0 = 0.2
    boosts = (1.5, 3.0, 6.0)
    etas = (0.05, 0.2, 0.8)
    checkpoints = (20, 100, 1000)
    rows = []
    max_closed_form_error = 0.0

    for b in boosts:
        target = b * q0 / (1.0 + (b - 1.0) * q0)
        final_values = []
        for eta in etas:
            q = q0
            samples = {}
            for step in range(1, max(checkpoints) + 1):
                q = (1.0 - eta) * q + eta * target
                expected = target + (1.0 - eta) ** step * (q0 - target)
                error = abs(q - expected)
                max_closed_form_error = max(max_closed_form_error, error)
                assert_close(q, expected, 2e-15, "anchored-target closed form")
                if step in checkpoints:
                    samples[str(step)] = q
            final_values.append(q)
            rows.append(
                {
                    "b": b,
                    "eta": eta,
                    "q_target": target,
                    "q_by_step": samples,
                    "q_1000_error_to_target": q - target,
                }
            )
        if max(abs(value - target) for value in final_values) > 1e-12:
            raise AssertionError(f"eta-dependent anchored fixed point for b={b}")

    targets = [row["q_target"] for row in rows if row["eta"] == etas[0]]
    if not all(left < right for left, right in zip(targets, targets[1:])):
        raise AssertionError("larger b should increase the anchored target for q0 in (0,1)")

    return {
        "model": "q_next=(1-eta)q+eta*q_target",
        "q0": q0,
        "boosts": list(boosts),
        "etas": list(etas),
        "target_formula": "q_target=b*q0/(1+(b-1)*q0)",
        "max_abs_closed_form_error": max_closed_form_error,
        "runs": rows,
        "interpretation": (
            "eta changes only the geometric relaxation rate (1-eta); b changes "
            "the fixed target."
        ),
    }


def bisect_root(function, left: float, right: float, iterations: int = 100) -> float:
    f_left = function(left)
    f_right = function(right)
    if f_left == 0.0:
        return left
    if f_right == 0.0:
        return right
    if f_left * f_right > 0.0:
        raise ValueError("bisection interval does not bracket a root")
    for _ in range(iterations):
        middle = 0.5 * (left + right)
        f_middle = function(middle)
        if f_left * f_middle <= 0.0:
            right = middle
            f_right = f_middle
        else:
            left = middle
            f_left = f_middle
    return 0.5 * (left + right)


def sech_squared(x: float) -> float:
    c = math.cosh(x)
    return 1.0 / (c * c)


def jacobian_eigenvalues(a: float, eps: float, x: float) -> tuple[float, float]:
    trace = -(1.0 + eps)
    determinant = eps * (1.0 - a * sech_squared(x))
    discriminant = trace * trace - 4.0 * determinant
    root = math.sqrt(max(0.0, discriminant))
    return (0.5 * (trace - root), 0.5 * (trace + root))


def adaptive_fold_checks() -> dict:
    a_values = (1.05, 1.2, 1.5, 2.0)
    eps_values = (0.2, 1.0, 5.0)
    rows = []
    max_fold_x_error = 0.0
    max_width_error = 0.0

    for a in a_values:
        derivative = lambda x: 1.0 - a * sech_squared(x)
        positive_fold_numeric = bisect_root(derivative, 0.0, 10.0)
        positive_fold_exact = math.acosh(math.sqrt(a))
        negative_fold_numeric = -positive_fold_numeric
        width_numeric = 2.0 * (
            a * math.tanh(positive_fold_numeric) - positive_fold_numeric
        )
        width_exact = 2.0 * (
            math.sqrt(a * (a - 1.0)) - math.acosh(math.sqrt(a))
        )
        x_error = abs(positive_fold_numeric - positive_fold_exact)
        width_error = abs(width_numeric - width_exact)
        max_fold_x_error = max(max_fold_x_error, x_error)
        max_width_error = max(max_width_error, width_error)
        assert_close(positive_fold_numeric, positive_fold_exact, 2e-14, "fold x")
        assert_close(width_numeric, width_exact, 2e-14, "fold width")

        stability = []
        for eps in eps_values:
            middle_eigs = jacobian_eigenvalues(a, eps, 0.0)
            outer_x = positive_fold_numeric + 0.5
            outer_eigs = jacobian_eigenvalues(a, eps, outer_x)
            if not (middle_eigs[0] < 0.0 < middle_eigs[1]):
                raise AssertionError("middle equilibrium must be a saddle for a>1")
            if not (outer_eigs[0] < 0.0 and outer_eigs[1] < 0.0):
                raise AssertionError("outer equilibrium sample must be stable")
            stability.append(
                {
                    "eps": eps,
                    "middle_x": 0.0,
                    "middle_eigenvalues": list(middle_eigs),
                    "middle_class": "saddle",
                    "outer_abs_x": outer_x,
                    "outer_eigenvalues": list(outer_eigs),
                    "outer_class": "stable",
                }
            )

        rows.append(
            {
                "a": a,
                "fold_x_numeric": [negative_fold_numeric, positive_fold_numeric],
                "fold_x_exact": [-positive_fold_exact, positive_fold_exact],
                "static_drive_width_numeric": width_numeric,
                "static_drive_width_exact": width_exact,
                "stability_by_eps": stability,
            }
        )

    return {
        "model": "xdot=-x+u+k; kdot=eps*(-k+a*tanh(x))",
        "equilibrium_curve": "u=x-a*tanh(x)",
        "fold_condition": "1-a*sech(x)^2=0",
        "fold_formula": "x_fold=+/-acosh(sqrt(a))",
        "width_formula": "2*(sqrt(a*(a-1))-acosh(sqrt(a)))",
        "eps_values": list(eps_values),
        "max_abs_fold_x_error": max_fold_x_error,
        "max_abs_width_error": max_width_error,
        "rows": rows,
        "interpretation": (
            "eps does not move equilibria or folds in this model, but it does "
            "enter the Jacobian and finite-rate dynamics; no universal claim of "
            "rate-independent dynamical stability follows."
        ),
    }


def equilibrium_at_drive(a: float, u: float) -> tuple[float, float]:
    residual = lambda x: x - a * math.tanh(x) - u
    if u < 0.0:
        x = bisect_root(residual, -20.0, 0.0)
    elif u > 0.0:
        x = bisect_root(residual, 0.0, 20.0)
    else:
        x = 0.0
    return x, a * math.tanh(x)


def derivatives(x: float, k: float, u: float, a: float, eps: float) -> tuple[float, float]:
    return -x + u + k, eps * (-k + a * math.tanh(x))


def rk4_step(
    x: float,
    k: float,
    u: float,
    du_dt: float,
    dt: float,
    a: float,
    eps: float,
) -> tuple[float, float]:
    x1, k1 = derivatives(x, k, u, a, eps)
    x2, k2 = derivatives(
        x + 0.5 * dt * x1,
        k + 0.5 * dt * k1,
        u + 0.5 * dt * du_dt,
        a,
        eps,
    )
    x3, k3 = derivatives(
        x + 0.5 * dt * x2,
        k + 0.5 * dt * k2,
        u + 0.5 * dt * du_dt,
        a,
        eps,
    )
    x4, k4 = derivatives(
        x + dt * x3,
        k + dt * k3,
        u + dt * du_dt,
        a,
        eps,
    )
    return (
        x + dt * (x1 + 2.0 * x2 + 2.0 * x3 + x4) / 6.0,
        k + dt * (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0,
    )


def settle_at_fixed_drive(
    x: float,
    k: float,
    u: float,
    a: float,
    eps: float,
    dt: float,
    tolerance: float = 1e-11,
    max_time: float = 500.0,
) -> tuple[float, float, float, float]:
    steps = int(math.ceil(max_time / dt))
    for step in range(steps + 1):
        dx, dk = derivatives(x, k, u, a, eps)
        residual = max(abs(dx), abs(dk))
        if residual <= tolerance:
            return x, k, step * dt, residual
        x, k = rk4_step(x, k, u, 0.0, dt, a, eps)
    raise AssertionError(f"endpoint did not equilibrate: a={a}, eps={eps}, u={u}")


def ramp_leg(
    x: float,
    k: float,
    u_start: float,
    u_end: float,
    rate: float,
    dt_max: float,
    a: float,
    eps: float,
) -> tuple[float, float, float]:
    direction = 1.0 if u_end > u_start else -1.0
    duration = abs(u_end - u_start) / rate
    steps = int(math.ceil(duration / dt_max))
    dt = duration / steps
    du_dt = direction * rate
    u = u_start
    crossing = None

    for _ in range(steps):
        previous_x = x
        previous_u = u
        x, k = rk4_step(x, k, u, du_dt, dt, a, eps)
        u += du_dt * dt
        crossed_up = direction > 0.0 and previous_x <= 0.0 < x
        crossed_down = direction < 0.0 and previous_x >= 0.0 > x
        if crossing is None and (crossed_up or crossed_down):
            fraction = -previous_x / (x - previous_x)
            crossing = previous_u + fraction * (u - previous_u)

    if crossing is None:
        raise AssertionError(f"no x=0 crossing: a={a}, eps={eps}, rate={rate}")
    return x, k, crossing


def sweep_once(a: float, eps: float, rate: float, dt: float) -> dict:
    u_min, u_max = -3.0, 3.0
    x, k = equilibrium_at_drive(a, u_min)
    start_residual = max(abs(v) for v in derivatives(x, k, u_min, a, eps))
    if start_residual > 1e-12:
        raise AssertionError("analytic/bisection initial endpoint is not equilibrated")

    x, k, up_crossing = ramp_leg(x, k, u_min, u_max, rate, dt, a, eps)
    x, k, top_hold_time, top_residual = settle_at_fixed_drive(
        x, k, u_max, a, eps, dt
    )
    x, k, down_crossing = ramp_leg(x, k, u_max, u_min, rate, dt, a, eps)
    x, k, bottom_hold_time, bottom_residual = settle_at_fixed_drive(
        x, k, u_min, a, eps, dt
    )
    return {
        "a": a,
        "eps": eps,
        "sweep_rate": rate,
        "dt_max": dt,
        "up_x_zero_drive": up_crossing,
        "down_x_zero_drive": down_crossing,
        "drive_gap": up_crossing - down_crossing,
        "top_hold_time_to_residual_1e-11": top_hold_time,
        "bottom_hold_time_to_residual_1e-11": bottom_hold_time,
        "top_final_residual": top_residual,
        "bottom_final_residual": bottom_residual,
    }


def finite_rate_sweeps() -> dict:
    a_values = (0.5, 1.5)
    eps_values = (0.5, 2.0)
    rates = (0.02, 0.005, 0.00125)
    dt = 0.05
    rows = []

    for a in a_values:
        for eps in eps_values:
            group = []
            for rate in rates:
                run = sweep_once(a, eps, rate, dt)
                rows.append(run)
                group.append(run)
            static_width = (
                0.0
                if a <= 1.0
                else 2.0 * (math.sqrt(a * (a - 1.0)) - math.acosh(math.sqrt(a)))
            )
            slow_errors = [abs(run["drive_gap"] - static_width) for run in group]
            if not (slow_errors[2] < slow_errors[1] < slow_errors[0]):
                raise AssertionError(
                    f"sweep gap did not approach static width: a={a}, eps={eps}, "
                    f"errors={slow_errors}"
                )

    selected = {"a": 1.5, "eps": 0.5, "sweep_rate": 0.005}
    coarse = next(
        run
        for run in rows
        if run["a"] == selected["a"]
        and run["eps"] == selected["eps"]
        and run["sweep_rate"] == selected["sweep_rate"]
    )
    fine = sweep_once(selected["a"], selected["eps"], selected["sweep_rate"], dt / 2.0)
    convergence = {
        "selected": selected,
        "coarse_dt": dt,
        "fine_dt": dt / 2.0,
        "abs_up_crossing_difference": abs(coarse["up_x_zero_drive"] - fine["up_x_zero_drive"]),
        "abs_down_crossing_difference": abs(coarse["down_x_zero_drive"] - fine["down_x_zero_drive"]),
        "abs_gap_difference": abs(coarse["drive_gap"] - fine["drive_gap"]),
    }
    if convergence["abs_gap_difference"] > 2e-6:
        raise AssertionError(f"selected RK4 step-size check failed: {convergence}")

    return {
        "method": (
            "RK4; start at the exact stable equilibrium at u=-3, ramp to +3, "
            "hold to max(|xdot|,|kdot|)<=1e-11, carry (x,k) into the down-ramp, "
            "then hold at -3 to the same tolerance"
        ),
        "drive_range": [-3.0, 3.0],
        "rates": list(rates),
        "rows": rows,
        "step_size_convergence": convergence,
        "interpretation": (
            "For a=0.5 the loop gap tends toward zero. For a=1.5 it tends "
            "toward the analytic static fold width. eps affects finite-rate lag "
            "and Jacobian dynamics even though it does not move static folds."
        ),
    }


def fixed_double_well_negative_control() -> dict:
    fold_abs_x = 1.0 / math.sqrt(3.0)
    fold_abs_u = 2.0 / (3.0 * math.sqrt(3.0))
    static_width = 2.0 * fold_abs_u
    assert_close(static_width, 4.0 / (3.0 * math.sqrt(3.0)), 1e-15, "double-well width")
    return {
        "model": "xdot=x-x^3+u",
        "equilibrium_curve": "u=x^3-x",
        "fold_x": [-fold_abs_x, fold_abs_x],
        "fold_u": [fold_abs_u, -fold_abs_u],
        "static_drive_width": static_width,
        "same_magnitude_stable_states_at_u0": [-1.0, 1.0],
        "stability": "stable when |x|>1/sqrt(3); unstable when |x|<1/sqrt(3)",
        "negative_control_claim": (
            "Arbitrary sign-readout labels A/B distinguish x=-1 and x=+1 at "
            "the same |x|, and the fixed-coupling system has static hysteresis. "
            "Thus hysteresis or a binary membership-style readout is not "
            "specific to an adaptive membership loop. These labels are not a "
            "genuine physical integration subset."
        ),
    }


def main() -> None:
    results = {
        "scope": (
            "Deterministic checks of the stated toy equations only; no evidence "
            "about boundaries, agency, physical integration, or real-world systems."
        ),
        "normalized_current_matrix_reboost": normalized_reboost(),
        "anchored_target": anchored_target(),
        "adaptive_continuous_toy": adaptive_fold_checks(),
        "illustrative_finite_rate_rk4": finite_rate_sweeps(),
        "fixed_coupling_double_well_negative_control": fixed_double_well_negative_control(),
        "status": "all assertions passed",
    }
    OUT.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"all assertions passed; wrote {OUT}")


if __name__ == "__main__":
    main()
