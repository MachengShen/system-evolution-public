# Local tomography is not our gluing obstruction — refuting our own bridge

*2026-09-07 · Macheng Shen and an AI research assistant*

**Cognitive state per claim; refutations kept visible.** Badges follow
[Claim-Receipt](../CLAIM-RECEIPT.md): 🟢 survived-stress-test / 🟡 speculative / 🔴 refuted,
followed by a confidence in 0–1. Every number below comes from a script that ran on one laptop;
nothing here is an empirical claim about the universe.

## The bridge we proposed, and why it is dead

The [previous note](2026-09-06-from-encoding-to-physical-possibility.md) argued that encodability
is too weak to select an ontology, and that the real question is why composition works the way it
does — in particular why physics is *locally tomographic*: why the joint state is fixed by the
joint statistics of local measurements.

Separately, this line has a result about **lossy projections**: two channels projecting one latent
generically cannot be glued into a shared representation, leaving an irreducible residual
`r_perp` — the [multimodal gluing obstruction](2026-08-19-multimodal-gluing-obstruction.md),
whose synthetic threshold sits at `ρ = 1`.

The tempting bridge: **local tomography is exactly the statement that this residual vanishes**, and
complex quantum theory sits exactly at `ρ = 1`. It is a pretty thought. It is wrong, and this note
is mostly about how it died.

🔴 **0.1 — the bridge, as a mechanism.**

**1. The two `ρ = 1`s are thresholds of different invariants.** Write `α` for the map from joint
states to local joint statistics. For two real-amplitude qubits ("rebits"):

| | invariant | value |
|---|---|---|
| local tomography failure | `dim ker α` — the *separation* half of a sheaf condition | **1** |
| our `r_perp` | `coker` of the constraint operator — the *gluing* half | **0** |

Both hold simultaneously and they point opposite ways. Worse, our own synthetic rig's constraint
operator `D` is a graph incidence matrix, and `dim ker(D) = #connected components` in 20 of 20
cells checked (28 of 28 rows on re-check). Its kernel is pure gauge, always. **The rig is
structurally incapable of detecting a tomography-type failure.** A coincidence at one point,
between an invariant that was measured and a different invariant that is unmeasurable in the same
apparatus, is not evidence.

**2. `ρ = 1` selects nothing.** Classical probability satisfies it. So does *any* power law
`d(n) = n^k` (checked k = 1..4). So does **boxworld** — enumerated here: 24 vertices, affine
dimension 8, `d(AB) = 9 = 3×3`, and it contains a PR box with CHSH = 4, well above the Tsirelson
bound 2√2. A counting condition satisfied by a super-quantum theory cannot be what picks out
quantum theory. The genuine selection theorem in the literature is Barnum–Wilce 2014 (local
tomography *plus* homogeneity *plus* self-duality *plus* one qubit); boxworld fails homogeneity.

**3. The sign was wrong.** Real quantum theory's famous excess (10 > 9) is *under*-determination —
a hidden global parameter — which is the opposite failure mode from an over-constrained residual.
The quaternionic row we wanted to cite is not merely wrong but ill-posed: `ℍ ⊗_ℝ ℍ ≅ M₄(ℝ)`, and
each local `J` has `J² = −1` while `(J_A ⊗ J_B)² = +1`, so there is no quaternionic composite to
count.

**4. The equivocation was in our code, not only our prose.** Two scripts computed
`coker(α) = Λ²(ℝⁿ) ⊗ Λ²(ℝᵐ)` — value 1 for two rebits — and *called* it the `r_perp` residual,
which for that same system is 0. The arithmetic is right and the labels are wrong. We record this
because a bridge that has a counterexample sitting inside our own prior results should not have
survived to a second round.

🟢 **0.9 — what does survive, stated narrowly.** The closed form
`dim coker = [n(n−1)/2]·[m(m−1)/2] = dim Λ²(ℝⁿ) ⊗ Λ²(ℝᵐ)` is a symbolic identity for all `n, m`
(verified by direct rank computation at (2,2), (2,3), (3,3), (3,4), (4,4), (2,5), (5,5)), and the
explicit witness `ρ± = (I₄ ± 0.2·Y⊗Y)/4` gives two valid, distinct rebit states whose expectation
values agree to `0.000e+00` over all local real observable pairs and `3.55e-15` over 20,000 random
ones. **NOVELTY = OCCUPIED** — Hardy 2001, Wootters' "limited holism", and the plethysm
`S²(V⊗W) = S²V⊗S²W ⊕ Λ²V⊗Λ²W` are all classical. **TRUTH = SUPPORTED.** This is the third
independent derivation of this counterexample in two days within this project, which says something
about how reachable it is, not about how novel.

## What replaced it

🟢 **0.8 (mechanism) / 🟡 0.6 (generality) — the discard is dimension-exact, and it is not in the
towers.** A [previous result](2026-08-19-multimodal-gluing-obstruction.md) found that contrastive
co-training reduces the residual by *discarding* obstructed structure rather than repairing it, but
measured this only as a scalar norm ratio. Measuring rank instead: after co-training, the hard rank
of the type-generator field projected onto the obstruction is exactly `max(0, T − s)` — **192 of
192 measurements, zero standard deviation, at every setting where the instrument is trusted**
(12 seeds, two shared-subspace sizes, all eight constraint counts, spanning `ρ` from 0.12 to 4.0).
The control (no obstruction) reads exactly zero in 140 of 144 measurements.

The part that matters: **single-tower embedding rank does not fall.** Hard rank stays 8/8 before
and after, and *effective* rank **rises** (4.64 → 6.66). The discarding happens in the cross-modal
agreement field, invisible to a plain embedding-SVD probe. This distinguishes the effect from the
dimensional-collapse literature that would otherwise absorb it (Jing 2022, Hua 2021, and more
recent work asserting dimension collapse as the origin of the modality gap) — **that prior-art flag
is not yet cleared, and a direct comparison is owed before any stronger claim.** Scope: this is our
own rig's obstruction quantity, not a physical law. At the largest setting the result is
**RIG-UNDECIDED** — a k-means resolution ceiling, diagnosed by running the same trained encoder
through the original code's own controls, not a theory failure.

🟢 **0.9 — a deflation of our own threshold was attempted and failed.** We suspected the `ρ = 1`
threshold was really graph percolation, since the constraint graph happens to connect at exactly
`T = s + 1`. Deleting edges to shatter the graph to 42 components leaves the obstruction rank
unchanged, and every zero row is exactly where `#edges = rank D` — arithmetically forced, not
disconnection. **Counting confirmed, percolation refuted.** The threshold is stronger than before.

## Corrections to our own axioms

🟢 **0.95 — "attention cannot be scaled" is not a thermodynamic claim.** We had leaned on a
Landauer-style budget. The margin is not close: at 10 bits/s the Landauer floor is ~3×10⁻²⁰ W
against ~20 W of brain power, slack by a factor ~10²⁰; the barrier stock for 10¹⁴ distinctions held
for a year is ~19 μJ, under a microsecond of that budget. Two errors compounded: purely predictive
memory has a dissipation lower bound of *zero* (Still et al. 2012), and holding a distinction is a
stock, not a flow. Corrected, the cost of *multiplicity* is linear while the cost of *duration* is
only logarithmic — 1 second to 100 years is a factor 1.79. The binding constraint is interference
in a shared substrate (Fusi–Abbott 2007), whose shape in (count, duration) is the opposite.

The honest coda: **the practical rule this was supposed to justify did not change at all.** If the
physics had been load-bearing, removing it would have moved the practice. It did not, which shows
the physics was decorative. We would rather say that than keep the decoration.

🟡 **0.5 — a self-observation clause is false as stated.** The claim that a system's
self-observation ceiling is *invisible from inside* does not follow; the underlying theorem
(Breuer 1995, on proper self-inclusion — not ours) makes the ceiling locatable from within, with
its *contents* unenumerable. Diagonalisation and Löbian arguments only rhyme: they give size
obstructions, not a self/other asymmetry.

## Prior art, honestly

`NOVELTY = OCCUPIED` never means a claim is false, and it never means stop — it means the
publication slot is taken. Separating the two axes:

- The real-vs-complex composition mathematics: **OCCUPIED**, TRUTH **SUPPORTED**.
- Whether experiment has settled it: **UNRESOLVED**, and we were about to overstate it. The 2021
  network-Bell falsification of real quantum theory rests on an independence assumption for the
  sources whose *testability* is itself under live 2026 dispute, with a rebuttal and a
  counter-rebuttal. The correct sentence is "falsified conditional on an independence assumption
  now contested", not "real quantum theory is dead."
- Objectivity as a zero-sum trade (what one observer gains from a fragment, the complement loses):
  **OCCUPIED** (Zwolak–Zurek 2013), verified here to 1e-16. Our small addition — an exact,
  and numerically *negative*, defect term when the global state is not pure, so that some
  distinguishability reaches nobody — is **PARTIAL** and rests on two lines of derivation.
- One proposed research direction died before it cost anything: the conjecture that complex quantum
  theory is the memory-optimal predictive model is **already refuted in peer review by the same
  group whose earlier result motivated it** (Onggadinata, Tanggara, Gu, Kaszlikowski, *Quantum*,
  2026). A pre-registered kill condition firing on a citation instead of on three CPU-days is the
  system working.

## What we are not claiming

No empirical claim about the universe is made here. The mathematics is small, exact, and mostly
classical; what is ours is the verdict on our own bridge and the dimension-exact measurement.
An earlier attempt to read a Buddhist thesis (dependent origination and emptiness) directly off
local tomography is **withdrawn as a Buddhist claim** — the two properties involved are logically
independent, all four combinations are populated, and our own world sits in the cell that the
conjecture said should not exist. The linear algebra is real; the Sanskrit was doing no work.

Companion material and the full internal round, including the four review passes that killed the
bridge, are kept with the working notes. Retracted items stay in place rather than being deleted.
