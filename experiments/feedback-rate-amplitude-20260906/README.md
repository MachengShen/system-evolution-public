# Feedback rate versus amplitude: deterministic verification

Date: 2026-09-06.

Companion to [Feedback strength is not update speed](../../essays/2026-09-06-feedback-strength-is-not-update-speed.md).

Run with Python 3.10 or later, standard library only:

```sh
python3 verify.py
```

This writes `results.json` alongside the script and fails if a numerical
assertion fails. There is no network access, training, stochastic seed, private
data, external model call or background process.

- [verify.py](verify.py): frozen recurrence, independent fold-root bisection,
  Jacobian stability, RK4 finite-rate sweeps and one step-size refinement.
- [results.json](results.json): complete deterministic model-check output.
- [verification-report.md](verification-report.md): readable results and limits.
- [claim-receipt.json](claim-receipt.json): schema-conforming narrow claim.

The script is independently implemented from the written equations. It checks
a scalar reduction of normalized reboosting; it does not execute the original
network code or certify a set-valued measurement. The full mathematical proof
and implementation mapping are in the companion note and its reviewed source
analysis. No existing agency or consciousness experiment is restarted here.

Finite-rate runs approach the analytic static limit but remain measurably away
from it, especially near the bistable folds. They demonstrate why a finite
sweep is not by itself an adiabatic certificate. They are not a numerical
extrapolation to zero rate or observations of a physical self-boundary.
