# D4 v0.2 — estimator and instrument-certificate stage

Status: **instrument only / no D4 main-arm run**

This directory freezes and runs the estimator/certificate stage for the D4
membership-identity hysteresis proposal. It deliberately does not implement or
launch the 630-run SPLIT/FUSE/TRANSPLANT program.

## Exact estimator contract

An observation is one row from one seed and one sweep path:

```text
(seed, arm, path, control, members[0:N], scalar_size,
 ridge_readout, echo_readout)
```

`members` is binary and `scalar_size == sum(members)`. For each seed and arm:

1. Split rows into `up` and `down` paths.
2. Match only rows with exactly equal integer `scalar_size` (`scalar_tol = 0`).
   Within each scalar stratum, sort both paths by `(control, row_index)` and
   pair equal ranks. Unequal stratum counts are refused rather than silently
   dropping the inconvenient tail. Each seed must retain at least four pairs.
3. On calibration seeds only, form signed membership differences
   `d = m_up - m_down`. Fit one rank-1, through-origin projection by the first
   right singular vector of the pooled calibration `d` matrix. Canonicalize its
   sign by making its largest-magnitude coordinate positive.
4. Freeze that one projection for every certificate and later confirmatory arm.
   For each held-out seed, compute `r = d - (d·v)v`, then

   ```text
   W_set_perp(seed) = || mean_over_matched_pairs(r) ||_1
   W_set_perp_normalized(seed) = W_set_perp(seed) / N
   ```

   The signed mean is load-bearing: raw mean pairwise Hamming distance is also
   reported as churn, but is not the confirmatory statistic because it cannot
   distinguish coherent path dependence from identity-randomized churn.
5. The independent unit is the seed. The 95% interval bootstraps seed scores;
   paired comparisons use seed-wise sign-flip permutation. Epochs and matched
   rows never inflate `n`.

If matching or held-out evaluation fails, the result is `RIG-UNDECIDED`. A
main-arm result exactly at a trivial endpoint (0 or N) is an estimator red flag;
known-answer controls may be constructed at an endpoint and are labelled as
such.

## Frozen alternatives (written before certificate numbers)

- **ALT-EST-1 — scalar shadow:** apparent set hysteresis is a single coherent
  displacement caused by scalar `|mu|` dynamics. The frozen rank-1 subtraction
  must remove the planted scalar-shadow fixture.
- **ALT-EST-2 — projection leakage:** fitting the projection on evaluation rows
  manufactures a small residual. Training and evaluation seed sets must be
  disjoint, and all cache keys include code/config/data hashes.
- **ALT-EST-3 — unordered churn:** mean Hamming distance stays positive even
  when membership identities or sweep order are randomized. Therefore raw
  Hamming is diagnostic only; the registered score is the held-out coherent
  signed residual above.
- **ALT-EST-4 — latency artifact:** a slow readout can create apparent path
  asymmetry. The planted step certificate must recover lag <= 2 epochs and at
  least three times that lag in dynamic range.
- **ALT-EST-5 — crowding empty test:** a crowding threshold is meaningless if
  no planted working point jointly has exclusion probability >= 0.5,
  `8 <= |mu| <= 20`, and churn <= 25% per 30 epochs.
- **ALT-EST-6 — non-orthogonal control:** a supposedly reward-orthogonal block
  may change task reward. The permutation certificate must keep the change
  inside the independently measured reward-noise band.
- **ALT-EST-7 — symmetry-preserving ablation:** a common channel relabelling
  leaves Hamming geometry invariant and is not a valid identity ablation. The
  certificate instead randomizes identity assignments independently across
  matched events, after balancing channel marginals.

Any explanation added after numbers must be labelled `POSTHOC` in the result
note.

## Certificates

The runner executes all instrument-stage gates:

- known-answer scalar-shadow subtraction;
- `P+(b)` set-latch sensitivity and physical-unit `b_min`;
- `P+hyst` coherent set latch plus `gate_const` negative control;
- randomized sweep and balanced membership-identity randomization;
- `P+timing` latency/dynamic-range certificate;
- `P+crowd` satisfiable working-window certificate;
- reward-block orthogonality certificate;
- seed-unit, held-out leakage, schema, and cache-key checks.

These are planted instrument controls. Passing them certifies the estimator and
certificate machinery, not the D4 mechanism, agency, life, or consciousness.

## Reproduce

Requires Python 3.10+ and NumPy. No API keys, accounts, network, GPU, external
messages, spending, or private data are used.

```bash
cd experiments/d4-instrument-v0.2
python3 -m unittest -v test_estimator.py
python3 run_certificates.py --code-commit <commit> --out results/certificates.json
```

The runner writes `results/certificates.json`,
`results/raw-observations.json`, and `results/claim-receipt.json` atomically.
Delete this directory to disable/remove the instrument package. A failed gate
closes as `RIG-UNDECIDED`; it never kills or supports the theory.
