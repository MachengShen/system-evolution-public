# Information Dynamics — THEORY v3: the discounted cokernel obstruction (and what v1/v2 got wrong)

Date: 2026-08-04 (published 2026-08-19)

Public index: [Theory Mainline](../THEORY.md) · Format: [Claim-Receipt](../CLAIM-RECEIPT.md)

> **Cognitive state:** 🟢 survived-stress-test · **Confidence:** 0.9 (finite-graph algebra + exact rational enumeration + 3,000-trial reproduction, fixed seeds) · provenance: authoritative correction of the private v1/v2 "discounted holonomy" claims; the correction was found by our own re-derivation, not by an external reviewer · **evidence:** `exp_discounted_cokernel.py` (3,000 trials, γ=0.9): 3-edge graphs 0% non-exact, 5-/6-edge graphs 100% non-exact, overall 93.63%; exact enumeration 42/45 = 14/15 · **prior-art:** ordinary graph cycle-space / circulation at γ=1 (standard); potential-based reward shaping (Ng, Harada, Russell 1999); the γ<1 residual is a least-squares/cokernel object, NOT de Rham cohomology — we withdraw that language.

**Why this file exists in public.** v1 of this line claimed a "gauge-invariant discounted holonomy" `M(L)=4.095` as evidence that partial observability forces a topological obstruction. That claim was wrong: for `0 ≤ γ < 1` the discounted incidence operator on a cycle is invertible, so every edge field has a discounted potential and the reported number measured fit against an arbitrary candidate potential. What survives is narrower and cleaner — a **cokernel / shaping-irreducible residual `r_perp`** on the complete observation-edge graph, forced by **overdetermined edge consistency after coarse-graining**. This object is the upstream of the two 2026-08 experimental lines published alongside it (multimodal gluing obstruction; self-boundary / boundary-defense). Refutations stay visible per Claim-Receipt.

Downstream (2026-08): [Multimodal gluing obstruction (E1/E2)](2026-08-19-multimodal-gluing-obstruction.md) ports `r_perp` to cross-modal consistency graphs.

Code: `information-dynamics/exp_discounted_cokernel.py`, `results_discounted_cokernel.json` — available on request (not yet mirrored into this repo).

---

# Information Dynamics — THEORY v3

*Authoritative correction · 2026-08-04 · supersedes the discounted-holonomy claims in v1/v2*

## 0. Verdict

The v1 object called the discounted `gamma`-monodromy defect is **not** a
gauge-invariant holonomy.  On a simple deterministic cycle and `0 <= gamma < 1`,
the discounted incidence operator is invertible, so every edge-reward field has
a discounted scalar potential.  The reported `M = 4.095` therefore measured
failure relative to a chosen candidate potential; it did not certify a
representation-independent obstruction.

The partial-observability result survives in a narrower and cleaner form when
tested on the **complete observation-edge graph**.  The correct object is the
weighted residual of the reward field modulo the image of the discounted
incidence operator: a quotient/cokernel obstruction, not generally de-Rham
cohomology or loop holonomy.

The historical 1,484-instance filter still gives **93.0593% nonzero corrected
residuals**.  Across all 3,000 aliasings the fraction is **93.6333%**.  Every
three-edge/three-observation graph is exact; every five- or six-edge graph in
this ensemble is non-exact.  What forces the obstruction is **overdetermined
edge consistency after coarse-graining**, not the existence of a discounted
cycle by itself.

## 1. The error in v1

For directed edges `e = (u -> v)`, define the discounted incidence operator

```text
(D_gamma phi)_e = phi(u) - gamma phi(v).
```

Potential-based shaping uses the negative of the same image,
`gamma Phi(v) - Phi(u)`; the sign does not change exactness.

For a deterministic `n`-cycle, `D_gamma = I - gamma P`, where `P` is a cyclic
permutation.  Its determinant is

```text
det(I - gamma P) = 1 - gamma^n.
```

Thus for `0 <= gamma < 1`, `D_gamma` is invertible.  Given **any** edge reward
`r`, there is a unique `phi = D_gamma^{-1} r`.  No nonzero quotient remains.
Subtracting the loop prediction of some externally selected `phi_0` can be
nonzero, but that quantity changes when `phi_0` changes.  It is a model-fit
residual, not a gauge-invariant holonomy.

At `gamma = 1`, the determinant vanishes.  The ordinary incidence matrix has a
cycle-space cokernel, and circulation around a closed loop is the familiar
obstruction.  That undiscounted statement remains valid.

## 2. Correct finite-graph object

Let `E` be the set of observed directed transition types, `V` the observed
states, `r in R^E` their expected rewards, and `W` a positive diagonal matrix of
edge visitation weights.  Define the best discounted potential by

```text
phi* = argmin_phi ||r - D_gamma phi||_W^2.
```

The corrected obstruction is

```text
r_perp = r - D_gamma phi*
       = [I - D_gamma (D_gamma^T W D_gamma)^+ D_gamma^T W] r.
```

It has four exact properties:

1. `r_perp = 0` iff one scalar discounted potential fits every observed edge.
2. `D_gamma^T W r_perp = 0`: it is `W`-orthogonal to all potential fields.
3. Adding any potential-based shaping term leaves it unchanged:
   `(r + D_gamma psi)_perp = r_perp`.
4. Dual certificates live in the left nullspace: if `z in ker(D_gamma^T)`, then
   `z^T r` vanishes for every exact field.

For `gamma = 1`, this recovers ordinary graph circulation/cycle-space
decomposition.  For `gamma < 1`, it is safer to call it the **discounted
potential residual**, **shaping-irreducible residual**, or **cokernel
obstruction**.  Calling it de-Rham cohomology would require an actual differential
or local-system construction not supplied here.

## 3. Corrected reproduction of the aliasing result

Protocol retained from v1:

1. draw a potential on a six-state latent deterministic ring;
2. construct a latent reward exactly as `r = D_gamma phi`;
3. randomly alias the six states into three pairs;
4. aggregate rewards for every distinct observed transition type;
5. fit one scalar potential per observation against **all** observed edges;
6. measure `||r_perp||_W`.

Results (`gamma = 0.9`, 3,000 fixed-seed trials):

| observed edges | trials | nonzero residual |
|---:|---:|---:|
| 3 | 191 | 0% |
| 5 | 1,230 | 100% |
| 6 | 1,579 | 100% |
| all | 3,000 | 93.6333% |

Applying the historical filter that required the particular observed cycle
`0 -> 1 -> 2 -> 0` leaves 1,484 trials and gives **93.0593%**, reproducing the old
headline for a different reason.  In that filtered set, the 103 three-edge
graphs are exact and every five-/six-edge graph is non-exact.

An exact rational enumeration removes Monte Carlo ambiguity. There are 90
balanced alias maps; 45 satisfy the historical cycle filter. Of those, 3 have
three observed edges and are generically exact, while all 18 five-edge and all
24 six-edge maps are generically non-exact. The structural proportion is thus
`42/45 = 14/15 = 93.333...%`; the 93.0593% number is one finite sample around it,
not a universal POMDP constant.

The surviving claim is therefore:

> Lossy state aggregation can turn a latent discounted-potential reward into an
> overconstrained observation-level reward field for which no single scalar
> potential fits all transition types.

This is a representation-consistency diagnostic.  It is not yet a useful
algorithm, a topological invariant, or evidence about consciousness.

## 4. What survives, what is withdrawn

### Survives

- Partial observation/coarse-graining can force a nonzero global discounted
  potential residual.
- The corrected residual is invariant to potential-based shaping and has a
  precise least-squares/dual-certificate meaning.
- Representation inconsistency and strategic game cycling are distinct
  obstructions and should be measured separately.
- At `gamma = 1`, ordinary cycle circulation remains a legitimate graph
  cohomology/cycle-space object.

### Withdrawn or reset

- `M(L) = 4.095` as a gauge-invariant discounted holonomy: **withdrawn**.
- “Every nonzero discounted loop defect is a nontrivial de-Rham class”:
  **withdrawn**.
- v2's monodromy-based bound and localization comparison: **formally
  superseded**; its conservative no-go posture may be retained, but the numbers
  must not be cited as results about `r_perp` until recomputed.
- RL implications, Abel-style pivot claims, and any public draft built on the
  v1 `M(L)` definition: **review required before reuse**.

## 5. Two-axis dissociation rig

The next minimal check separates:

1. **representation obstruction** — `||r_perp||_W` on the transition graph;
2. **strategic obstruction** — the antisymmetric/harmonic component of a game
   gradient field.

The 2x2 smoke test crosses full vs aliased observation with potential vs
antisymmetric game dynamics.  It passes only if state refinement removes the
first residual without changing strategic harmonicity, while potential/game
shaping removes the second without repairing the representation.

This is a definition-level dissociation, not empirical validation of a
bicomplex.  Its falsifier is simple: if either repair changes the wrong axis in
the coupled version, the proposed separation is incomplete.

## 6. Artifacts and status

- `exp_discounted_cokernel.py` — corrected operator and 3,000-trial reproduction.
- `results_discounted_cokernel.json` — machine-readable corrected numbers.
- `exp_representation_game_dissociation.py` — executable 2x2 smoke test.
- `results_representation_game_dissociation.json` — four cells and orthogonal repairs.
- `THEORY-v1.md`, `THEORY-v2.md`, `exp_credit_holonomy.py`, and downstream pivot
  notes remain as historical research records, but their discounted-holonomy
  conclusions are superseded by this file.

Next bar: compare the corrected residual with TD residual, bisimulation,
predictive-state splitting, and game harmonicity on a genuinely coupled task.
If it adds no out-of-sample or interventional value, keep it as a precise but
redundant representation certificate.
