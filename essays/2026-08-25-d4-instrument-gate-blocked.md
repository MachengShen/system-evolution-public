# D4 v0.2 instrument gate: pre-rig self-test passed, estimator not certified

**Date:** 2026-08-25

**Claim-Receipt:** 🟡 `speculative` · D4 rig readiness **RIG-UNDECIDED** ·
confidence withheld

**Scope:** estimator/instrument stage only. The D4 main program was not run.

## Verdict

The software returns its registered values on its own planted fixtures, but the
actual D4-I instrument rig has not been run and the proposed `W_set^perp`
definition failed adversarial measurement review. Neither a positive nor a
negative D4 theory result is available.

Gate 1 of the associated release packet was completed separately: public commit
`e90e09428b960792d6cbcc0dfb1e6cbe6412cbe0` was independently read, privacy /
secret checked, and pushed to `main`. This note concerns Gate 2 only.

## What actually ran

- six estimator unit tests;
- same-runner synthetic scalar-shadow, set-latch, `gate_const`, randomized-
  identity, sensitivity, timing, crowding, and reward-orthogonality fixtures;
- strict JSON generation and a code-commit binding check;
- three independent constraint reviews: measurement/falsifiability,
  reproducibility/invariants, and public claim boundary.

The recorded state is:

```text
synthetic_self_test = PASS
instrument_rig      = NOT_RUN
main_program        = NOT_RUN
overall             = RIG-UNDECIDED
```

Machine-readable artifacts:

- [candidate estimator and frozen pre-number alternatives](../experiments/d4-instrument-v0.2/README.md)
- [self-test output](../experiments/d4-instrument-v0.2/results/certificates.json)
- [raw planted observations](../experiments/d4-instrument-v0.2/results/raw-observations.json)
- [narrow Claim-Receipt](../experiments/d4-instrument-v0.2/results/claim-receipt.json)

## Why the green self-test is not an instrument certificate

The primary candidate score is a nonnegative norm of a finite-sample mean. A
genuine randomized null therefore has positive finite-sample bias; bootstrapping
the raw scores cannot be expected to produce an interval containing zero. The
shipped cyclic randomization fixture cancelled exactly by construction and hid
that defect.

There is a second identification problem. Exact matching on integer `|mu|`
already removes the all-ones scalar-size direction. The additional fitted
rank-1 direction is an arbitrary membership-identity orientation: it can erase
a coherent effect aligned with the calibration orientation while leaving an
equally plausible orthogonal nuisance unchanged.

Finally, the timing, crowding, and reward-orthogonality rows in this version are
planted satisfiability fixtures. They do not pass through the real `MuObserver`,
ridge/echo readouts, `c1` scan, or task-reward path. Calling them measured rig
certificates would launder construction into evidence.

## Release condition for D4-I

Before any main arm can start, a replacement estimator must:

1. compare against a predeclared finite randomized-null distribution rather
   than use a raw-score interval against zero;
2. survive channel relabelling, multiple nuisance orientations, constant-zero,
   constant-upper-bound, missing-seed, and leakage mutations;
3. record expected seeds and common control support, not silently accept absent
   seeds or arbitrarily separated matched controls;
4. use distinct dynamical runs for randomized sweep and identity randomization;
5. run the actual set-valued bistable/`gate_const`, ridge+echo timing, crowding,
   and reward-orthogonality paths with independent held-out seeds.

Until then, instrument failure means `RIG-UNDECIDED`, not theory killed. The
630-run SPLIT/FUSE/TRANSPLANT program remains prohibited.

## Confidence boundary

- **0.97** that the current artifacts are synthetic self-tests rather than D4-I
  rig measurements; this follows directly from code-path inspection.
- **withheld** for estimator validity and D4 rig readiness.
- **no update** to the D4 mechanism/theory probability because no valid D4
  observation was produced.

**Review sanity-check:** failed constructively; all three reviews converged on
the same release blocker, and their concrete anti-signals are incorporated
above.
