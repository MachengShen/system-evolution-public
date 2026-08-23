# A permutation control cannot separate "which coordinate" from "consistently which coordinate": a bit-matched credit channel measures routing consistency, not structure

Date: 2026-08-24

Public index: [Theory Mainline](../THEORY.md) · Format: [Claim-Receipt](../CLAIM-RECEIPT.md) · Companion: [Alterity as an Exploration Source](2026-08-23-alterity-as-exploration-source.md)

> **Cognitive state (per claim):**
> - "With `C` classes, `softmax − onehot` has rows in the `(C−1)`-dimensional zero-sum subspace, so any credit signal of the form `err @ M` for fixed `M` has rank at most `C−1`; at `C=2` it is rank exactly 1, and the arg-max coordinate is therefore *constant across every sample and every update*": 🟢 survived-stress-test · **Confidence 0.95** — one-line derivation, plus measured singular spectra `[σ, 0, 0, 0]` and measured distinct-arg-max-coordinate counts on the production training paths. This is arithmetic, not interpretation.
> - "Raising `C` restores the channel: measured spectral-gap rank is *exactly* `C−1` (1 → 2 → 9 at `C` = 2, 3, 10) and the number of distinct coordinates used over a whole run rises 1 → 3 → 14/15": 🟢 survived-stress-test · **Confidence 0.95** — direct measurement on the same production paths, value-for-value against the prediction.
> - "But discriminability does **not** recover. A twin that relabels the coordinate axis by one *fixed* bijection retains 103% / 108% / 121% of the un-permuted arm's credit-attributable learning at `C` = 2, 3, 10 — monotonically increasing": 🟡 speculative · **Confidence 0.6** — measured, but in an 8-seed two-layer toy, not at the scale the claim wants. Direction is stable across all three `C` values; magnitude is not to be trusted.
> - "Therefore permutation-class controls generically cannot separate *coordinate identity* from *input-dependent routing consistency*, because a permutation of a consistent routing rule is itself a consistent routing rule": 🟡 speculative · **Confidence 0.55** — this is an argument with a supporting measurement, not a theorem. I have not enumerated the space of non-permutation controls, and a single counterexample control would refute it.
> - "The fixed-permutation twin *outperforms* the un-permuted arm, increasingly with `C`": 🔴 **observed, unexplained.** Both arms were constructed with identical amplitude codes and matched delivery paths, so this is not under-delivery. I have a guess (credit repeatedly reinforcing already-dominant units versus spreading specialisation) and **no experiment discriminating it.** Recorded rather than explained.
> - "This invalidates the specific pre-registered contrast that motivated the work": 🟢 survived-stress-test · **Confidence 0.85** — the contrast's stated purpose was to make a "structure" attribution *hard* to earn; as specified with a fresh permutation per update it makes the attribution nearly automatic, and as repaired with a fixed permutation it makes the attribution nearly impossible. Both are degenerate, in opposite directions.
>
> provenance: agent-executed diagnostics against a frozen pre-registration, plus analytic derivation · **evidence:** production-path instrumentation (monkeypatched dimensions only, training code unmodified) and an 8-seed synthetic toy · **not evidence:** no decision-bearing run of the parent experiment was executed; no result here licenses one. **prior-art (reasoned, NOT read for this note):** direct feedback alignment (Nøkland 2016), feedback alignment (Lillicrap et al. 2016), predictive coding / equilibrium propagation (Whittington & Bogacz; Scellier & Bengio), lottery-ticket and permutation-symmetry work on loss landscapes (Entezari et al.; Ainsworth et al. "Git Re-Basin"). The permutation-symmetry literature is the most likely place this is already known and should be checked first.

## 0. The claim in one sentence

If you throttle a learning rule's credit signal into a fixed-width code and ask whether its advantage comes from *structure* (which coordinate receives credit) or from *bandwidth* (how many bits), the natural control — permute the coordinate the credit lands on — **cannot answer the question**, because permuting a consistent input→coordinate map yields another consistent input→coordinate map. What such a control actually measures is whether the routing is *temporally consistent at all*, which is a different and much weaker property.

## 1. The setup that produced this

A pre-registered sweep crosses representational capacity against credit mechanism (backprop versus direct feedback alignment, forward-forward, and a predictive-coding nudge). It contains a confound control stated roughly as: *also compare scalar versus structured credit at matched entropy per update; a structured-credit win that disappears once the channel bandwidth is matched is "more bits", not "structure."*

The structured channel transmits one coordinate index plus one quantised signed amplitude, and decodes to a single non-zero coordinate. The scalar channel transmits one amplitude and broadcasts it. Equal frame width, different meaning. The control's whole job is to make "structure" **hard** to claim.

Two things went wrong, and the second is the interesting one.

## 2. The first failure: a gate whose statistic was never checked against a known answer

The matched-entropy requirement was implemented as a plug-in empirical entropy over the transmitted codewords, with a tolerance of 0.25 bits per symbol. It compared 24 samples drawn from an alphabet of `2^18 = 262,144`.

At that sampling ratio the plug-in estimator is pinned near its ceiling `log2(n)`. Reverse-solving each recorded value against the integer partitions of 24 shows what the statistic actually was: **a collision count.** Every broadcast-channel arm sat exactly at `log2(24) = 4.584962500721156`; every structured arm sat at the value corresponding to some specific number of colliding pairs. The value that halted the run, `0.5573934896284056`, is `log2(24) − 4.027569…`.

Three consequences, and the middle one is the one people miss:

1. The red light was not evidence that the contrast was unbuildable.
2. **A green light would not have been evidence either.**
3. The gate was one-sided by construction: with one arm pinned at the ceiling, it was structurally impossible to observe the inequality in the other direction.

Meanwhile six trust gates, three production known-answers, and nine mutation-detection checks were all green. They all ask *"did the apparatus compute this correctly?"* None asks *"is this quantity the thing we think it is?"* The repair is a gate that sits **before** the others:

> **No statistic may gate a decision until it has been checked against a construction whose true value is known analytically — at the sample size and alphabet size the experiment actually uses.**

The replacement was a *construction identity* rather than a tolerance: relabel the coordinate axis by a bijection `(i, a) ↦ (π(i), a)`. A bijection preserves the multiset of symbol counts, hence preserves the plug-in entropy **exactly**. Measured difference: `0.0`, no tolerance. That part worked.

## 3. The second failure: two classes make the coordinate a constant

The cross-entropy error `err = softmax(logits) − onehot(y)` has rows summing to zero. With `C` classes those rows live in a `(C−1)`-dimensional subspace. Any credit of the form `full = err @ M` for a fixed matrix `M` therefore has rank at most `C−1`.

At `C = 2` that is **rank exactly 1**: every row of `full` is a scalar multiple of the same vector `M[0] − M[1]`. So `argmax |full|` is *the same coordinate for every sample and every update, for the entire run.*

Measured on the production training paths (dimensions monkeypatched, training code unmodified), counting distinct arg-max coordinates over a whole run:

| classes | direct feedback alignment | predictive coding | forward-forward |
|---|---|---|---|
| `C = 2` | rank 1, **1 coordinate** | rank 1, **1 coordinate** | rank 24 (full), 33 coordinates |
| `C = 3` | rank 2, 3 coordinates | rank 2, 3 coordinates | — |
| `C = 10` | rank 9, 14 coordinates | rank 9–10, 15 coordinates | — |

Rank lands on `C−1` value-for-value. Forward-forward escapes at every `C` because its credit is a row-wise rescaling of the hidden activations, not a product of `err` with a fixed matrix — so it never had the degeneracy and cannot be used to test the fix.

**What this means for the original contrast.** For two of the three non-backprop mechanisms at `C = 2`, the structured channel's coordinate field is a *constant*. There is no coordinate information to destroy. "Is the win structure or bandwidth?" is not measured badly there — it is **ill-posed**. And this contaminates the pre-registered contrast itself, not merely one implementation of it.

This is a property of the binary task, not of the learning rules. That is worth stating plainly because it is easy to mistake for a fact about direct feedback alignment.

## 4. The result that does not go away

The obvious repair: use more classes, restore the coordinate information, re-run the control. Section 3 shows the channel does recover.

The control does not.

Compare three arms against a no-credit baseline, reporting *credit-attributable* learning (arm minus the baseline that trains the readout but delivers no credit to the hidden layer — without this subtraction roughly nine-tenths of the measured quantity is a shared offset and the comparison is noise):

| classes | un-permuted | **fixed-permutation twin** | fresh-permutation-per-update twin |
|---|---|---|---|
| `C = 2` | 100% | **103.0%** | 6.3% |
| `C = 3` | 100% | **107.7%** | −16.8% |
| `C = 10` | 100% | **121.0%** | 19.7% |

The fixed-permutation twin does not lose. It matches, then beats, and the gap grows with `C`. The fresh-permutation twin collapses to the noise floor — a uniformly random router scores 1–2% on the same scale.

The reading: **what the structured channel supplies is not the identity of the arg-max coordinate; it is the consistency of the input→coordinate map.** `π ∘ argmax` is exactly as serviceable a consistent map as `argmax`. Hidden units are exchangeable at initialisation; the network does not need credit to arrive at the arg-max unit, only at *some* stable unit per input pattern.

So a permutation control changes **one** variable if you believe the thing under test is coordinate identity, and **the** variable if the thing under test is routing consistency. Drawing a fresh permutation every update changes *both* — which is why the as-specified control let "structure" light up almost automatically, and why the fixed-permutation repair makes "structure" almost impossible to claim. Same design, opposite degeneracies.

Neither is a bug in the code. Both are the contrast asking a question the apparatus does not distinguish.

## 5. What I am not claiming

- I have **not** shown that no control can separate these. I have shown that permutation-class controls do not, given a stated reason that generalises within that class, and I have not enumerated non-permutation alternatives. One working counterexample refutes §4's generalisation and I would rather have it than keep the claim.
- The 103/108/121% numbers come from an 8-seed two-layer toy. The *direction* is stable across three values of `C` and two credit regimes; the magnitudes are not load-bearing.
- **The fixed-permutation twin outperforming the un-permuted arm is unexplained.** Amplitude codes and delivery paths were matched by construction, so it is not under-delivery. Guessing is cheap here and I am not going to spend the reader's attention on one.
- No decision-bearing run of the parent sweep has been executed. Nothing here licenses one. The failing negative-control numbers that halted it are still failing and are not withdrawn.

## 6. The transferable part

Three habits, in decreasing order of how sure I am:

1. **Check the estimator, not just the apparatus.** Every "known answer" gate in §2 verified that the code computed its statistic correctly. The statistic was still measuring collisions. Add the analytic-known-answer check on the *quantity*, at the experiment's real `n` and alphabet size, before it is allowed to gate anything.
2. **Prefer a construction identity to a tolerance.** "These two differ by ≤ ε" invites an estimator to be wrong quietly. "These two are related by a bijection, therefore this functional is identical" cannot be. Where a control can be expressed as an exact invariant, express it that way.
3. **Ask what your ablation holds fixed, not only what it removes.** A control that removes a property by randomising it usually removes *consistency* as well. If the hypothesis is about identity and the ablation destroys identity **and** stability, the ablation tests the weaker of the two — and will report whichever answer its noise floor prefers.

The last one is the reason this note exists. The contrast was designed specifically to be hard to pass, by people who had already been careful. It still ended up unable to distinguish its own two hypotheses, and the failure was invisible until the ablation was itself decomposed.

---

## 7. Addendum, same day: §4's generalisation is refuted, by the counterexample §5 asked for

§5 said one working counterexample would refute the generalisation and that I would rather have it than keep the claim. It arrived within the hour.

**The named alternative I had not tested.** Every measurement above applies the fixed relabeling from step 0, to a network at random initialisation. At random initialisation the hidden units are **exchangeable** — no unit means anything yet. Applying a fixed bijection to an exchangeable set is a **symmetry of the problem**, so of course it costs nothing. The 103/108/121% figures may therefore measure exchangeability, not information preservation.

**The split.** Warm-start with exact (unquantised) credit for 100 steps so units acquire roles, *then* apply the same fixed permutation for the remaining 100. Eight seeds; credit-attributable measured as the no-credit arm's final loss minus the arm's final loss:

| | fixed-permutation twin, as share of un-permuted |
|---|---|
| `C = 2`, cold start | 1.030 |
| **`C = 2`, warm-started** | **0.437** |
| `C = 10`, cold start | 1.210 |
| **`C = 10`, warm-started** | **−0.107** (worse than delivering no credit at all) |

**So permutation controls do separate identity from routing consistency — but only against a network whose units already carry roles.** The earlier null was an artifact of testing the ablation exactly where a symmetry makes it vacuous.

**What survives, what dies:**

- 🔴 **Dies:** "permutation-class controls generically cannot separate coordinate identity from routing consistency" (§4, §0, and the title's implied generality). **Withdrawn.** It holds only in the cold-start regime, where it is a symmetry statement rather than a finding.
- 🟢 **Survives unchanged:** everything in §2 and §3 — the collision-counter estimator, the rank-`C−1` derivation, the measured constancy of the coordinate field at `C = 2`. Those are arithmetic and are untouched.
- 🟡 **Sharpened:** the transferable lesson in §6.3 is now stronger and more specific. *An ablation applied where the thing it ablates is a symmetry of the model will report "no effect" for reasons that have nothing to do with the hypothesis.* Check whether your ablation is acting on a degree of freedom the model has actually broken yet.
- 🔴 **Still unexplained:** the cold-start twin *out*-performing the un-permuted arm (up to 121%). The exchangeability account explains why it does not lose; it does not explain why it wins. Still no experiment discriminating it, still no story offered.

**Confidence on the addendum:** 0.6. Eight seeds, one two-layer toy, one credit family (direct-feedback-alignment style), and the warm-started effects are small in absolute terms (0.0043 and 0.0228) even though the `C = 10` sign flip is not subtle. It refutes a 0.55-confidence generalisation; it does not establish its converse at any strength worth quoting.

**Method note, since this essay is partly about method.** The refuted claim was published with an explicit falsifier attached, at a confidence that said "argument, not theorem." That is the only reason this correction is a one-hour edit rather than an embarrassment. Publishing the falsifier alongside the claim is what makes a claim cheap to withdraw.
