# Feedback strength is not update speed: a correction to boundary-memory experiments

Date: 2026-09-06 · [Theory mainline](../THEORY.md) · [Claim-Receipt](../CLAIM-RECEIPT.md)

**Cognitive state:** survived-stress-test · **Confidence:** 0.95 for the scoped
algebra and implementation diagnosis, a subjective review judgment; withheld
for a physical boundary mechanism.

**[定理] Formal result.** A multiplier outside an adaptation update need not change its equilibrium structure. Confusing that multiplier with feedback amplitude can turn a speed-of-concentration measurement into a supposed test of stronger boundary memory.

**中文摘要。** 这次推进是把“反馈有多强”“更新有多快”“最后会走到哪里”拆开。原来的一类强化规则，不论非零更新率大小，固定成员条件下都走向同一集中极限。我们给出可证明的区分判据、一个有解析阈值的双参数模型，以及足以推翻“成员滞回只可能来自自反馈”的反例。结论只覆盖明确的动力学条件；真实自我边界的机制仍待识别。

| Assessment | Status |
|---|---|
| NOVELTY_STATUS | Rate separation, saddle-node hysteresis and mean-field self-consistency are established. The contribution here is a correction to this research line, with a reproducible diagnostic and conditional derivation; no priority claim. |
| EPISTEMIC_STATUS | Algebra proved under the assumptions below. Small numerical checks are model checks. Boundary/agency interpretation remains unresolved. |
| RELIABILITY | Independent mathematical and causal review; explicit counterexamples; primary literature checked at the relevant equations. Numerical receipt linked below. |
| WHAT-REMAINS-TO-KNOW | Whether a physically specified membership-feedback pathway contributes beyond alternative slow-state mechanisms under controlled interventions. |

## 1. The parameter mismatch

Consider a joint state `(s, K)` with adaptation

```text
K_next = K + eta [T(s, K) - K],     eta > 0.
```

Assume that `T` and the other fixed-point equations do not depend on `eta`.
At every fixed point,

```text
T(s, K) = K.
```

Thus the **fixed-point set is independent of eta**. This follows by division,
without simulation. Equilibrium folds cannot move solely because this
multiplier changes. But discrete-time stability, oscillations, basin selection
and finite-time responses can change. Fixed-point independence is not a
theorem of dynamical equivalence.

At `eta=0`, the adaptation equation imposes no constraint: `K` is frozen at its
initial value. Freezing a learned coupling is different from removing its
effect or allowing it to decay. A comparison against zero rate must name that
intervention precisely.

This separation is standard in adaptive-network theory: adaptation timescale
is explicitly factored out in Berner et al., §3.5 [1].

## 2. Repeated reinforcement has a common concentrated limit

There is a second issue when the target is built from the **current** matrix.
Suppose weights are nonnegative with fixed positive total mass. For a fixed
selected subset, let `q` be its internal fraction of that mass. Multiply its
internal weights by `b>1`, leave the others unchanged, renormalize, then mix
with the old matrix at rate `0<eta<=1`. Exactly,

```text
q_next = (1-eta) q + eta b q / [1+(b-1)q],
q_next-q = eta (b-1) q(1-q) / [1+(b-1)q].
```

**Proof of the limit.** For `0<q<1`, the increment is positive and the update
remains below 1. The increasing bounded sequence has a limit. Continuity
forces that limit to be a fixed point, either 0 or 1. Because it started
positive and increased, the limit is 1.

Every positive rate therefore approaches the **same** concentrated endpoint
while the selected subset stays fixed. Even changing `b>1` does not change
that endpoint in this rule. A rapid ceiling at the first positive rate is
compatible with ordinary repeated reinforcement. This is a conditional
explanation, not a proof that the subset stays fixed in a full adaptive rig.

One clean alternative is a fixed nonnegative reference matrix `B`, with
`B_ii=0` and `sum_offdiag B_ij=M>0`:

```text
T_a(B,S)_ij = M B_ij exp(a 1{i,j in S})
                  / sum_offdiag B_kl exp(a 1{k,l in S}),
K_next = (1-eta) K + eta T_a(B,S).
```

For a fixed subset and reference fraction `q0`, the target fraction becomes

```text
q_target(a) = exp(a) q0 / [1+(exp(a)-1)q0].
```

Now `a` changes the endpoint, while `eta` changes the approach to it. This is
an explicitly different model, with a restoring reference; it must not be
described as a mere relabelling or a validated repair of the full old rig.

## 3. A conditional theorem about structural memory

Use a transparent deterministic continuous-time family,

```text
dx/dt = -x + u + k,
dk/dt = epsilon [-k + a h(x)],     epsilon > 0, a >= 0.
```

Here `a` is feedback amplitude, `epsilon` its update rate, `u` the external
drive, and `h` a smooth strictly increasing function independent of the parameters.
This is an illustrative model, not a reduction of a measured physical boundary.
At equilibrium,

```text
k = a h(x),        u(x,a) = x - a h(x).
```

Assume a smoothly continuing pair of nondegenerate folds `xL(a)<xR(a)` bounds
the same bistable interval: `u(xL,a)` is its upper drive threshold and
`u(xR,a)` its lower threshold. Define their separation

```text
Delta u(a) = u(xL(a),a) - u(xR(a),a).
```

At each fold, `partial_x u=1-a h'(x)=0`. Differentiate the two thresholds.
The terms involving movement of the fold locations vanish, leaving

```text
d(Delta u)/da = h(xR) - h(xL) > 0.
```

This is the useful limited conclusion: **a continuing bistable fold interval
widens with feedback amplitude in this family, and its locations do not
depend on the positive adaptation rate.** If the function itself changes with
`a`, the folds become degenerate, or different fold pairs exchange roles, the
argument does not apply.

The Jacobian has trace `-1-epsilon` and determinant
`epsilon [1-a h'(x)]`. Positive determinant means a stable equilibrium;
negative determinant means a saddle. These statements concern equilibrium
branches. Observed switching still requires branch-following preparations,
a drive spanning both folds, and a controlled slow-sweep limit.

### Solvable example: h(x)=tanh(x)

For `a<=1`, there is no finite bistable fold window; `a=1,u=0` is a degenerate
critical point. For `a>1`,

```text
x_fold = +/- acosh(sqrt(a)),
Delta u(a) = 2 [sqrt(a(a-1)) - acosh(sqrt(a))],
d(Delta u)/da = 2 sqrt(1-1/a) > 0.
```

Near onset, `Delta u ~ (4/3)(a-1)^(3/2)`. The onset exponent and tanh
self-consistency belong to established mean-field bifurcation mathematics;
Berglund and Kunz give the corresponding mean-field static thresholds in
§4.1, equations (34)–(36) [2]. We re-derived the formulas above for the stated
variables; neither the equation nor the exponent establishes new physics.

At fixed `u`, eliminating `k` gives

```text
x'' + (1+epsilon)x' + epsilon [x-u-a tanh(x)] = 0.
U(x) = x^2/2 - u x - a log(cosh(x)),
E = (x')^2/2 + epsilon U(x),
dE/dt = -(1+epsilon)(x')^2 <= 0.
```

The example is a damped potential system. It does not hide a sustained
oscillator behind the hysteresis. This energy identity is for fixed drive;
time-varying `u` adds forcing terms.

## 4. Why this does not identify a self-boundary mechanism

**Counterexample: identical level and margin can conceal ordinary
multistability.** Take the fixed-parameter system `x'=u+x-x^3`. Give two
candidate sets scores `C+x` and `C-x`, and select their instantaneous argmax.
At `u=0`, stable states `x=+1` and `x=-1` select different sets, with identical
winning level `C+1` and margin `2`. Its fold window is `4/(3 sqrt(3))`, although
no coupling adapts. Argmax margin is not an energy barrier or a basin depth.
This abstract score counterexample refutes a universal argmax inference; it
is not a construction for exact IIT integrated information.

**State-augmentation equivalence.** Any system with node state `s`, adaptive
coupling `K`, and readout `H(s,K)` can be rewritten using the enlarged state
`z=(s,K)`. Every trajectory and readout under the same drive is identical.
Calling a variable “coupling” rather than “hidden state” cannot be identified
from those observations alone. Distinguishing mechanisms requires a declared
physical partition and a specific intervention on a measured pathway.

The new `Delta u` is an **input-axis fold separation**. It is not a matched
membership symmetric-difference statistic. A bridge between them needs its
own definition and validation. No result here reverses earlier negative
agency experiments or supplies evidence of phenomenal consciousness.

## 5. What the next instrument must discriminate

Finite-rate loops alone are insufficient: even systems without static
hysteresis have dynamic loops [3]. The next admissible small rig should:

1. Vary amplitude, adaptation rate and drive speed separately; establish their
   different fixed-target limits before interpreting a membership score.
2. Advance the full joint state on one clock and carry it continuously through
   up and down passages. Two independently initialized sweeps are a distinct
   preparation comparison, not automatically a closed hysteresis cycle.
3. Compare decreasing positive sweep rates at fixed positive adaptation rate.
   Relaxing only the fast state does not establish joint adiabaticity. Near a
   fold, relaxation diverges; a single finite waiting threshold cannot prove
   convergence. State the order of noise and slow-drive limits explicitly.
4. Include fixed-coupling multistability, hidden-state, live-feedback,
   freeze/reset and replay controls with matched initial joint state. Any
   identified effect is conditional on the specified intervention.

**Falsifiers / kill conditions.** A demonstrated `eta`-dependent fixed point
under the exact premises in §1 would refute the cancellation claim. A frozen
subset violating §2's mass recurrence would refute its implementation mapping.
An error in a nondegenerate fold pair satisfying §3's assumptions would refute
the width theorem. Failure to distinguish a proposed physical mechanism from
the fixed-coupling counterexample rejects that interpretation, not the algebra.

## Reproducibility and review

The [verification package](../experiments/feedback-rate-amplitude-20260906/README.md)
contains the script, raw model-check output and a narrow claim receipt. It
checks the recurrence, independent numerical fold locations, stable versus
saddle branches and finite-rate behavior. It does not run the earlier full
boundary experiment or certify its estimator.

**Review sanity-check:** independent mathematical and causal reviews integrated.
They narrowed “all dynamics are rate-independent” to “fixed-point set”, rejected
“matched margin removes multistability”, and kept fold width separate from
membership width. These are model-generated reviews with shared source context,
supported by explicit derivations; they are not external peer review.

## References and reliability audit

1. Berner, Gross, Kuehn, Kurths and Yanchuk (2023), [Adaptive Dynamical Networks](https://arxiv.org/html/2304.05652v1#S3.SS5). Read §2.3 and §3.5 for the node/link equations and explicit timescale separation. Used for established terminology, not as evidence for a boundary mechanism.
2. Berglund and Kunz (1999), [Memory Effects and Scaling Laws in Slowly Driven Systems](https://arxiv.org/pdf/chao-dyn/9807025). Read §2 and §4.1, including equations (34)–(36) and their assumptions. Static tanh thresholds were independently re-derived here. This source points to earlier dynamic-hysteresis work including reference [3]; no full audit of its entire citation tree is claimed.
3. Goldsztein, Broner and Strogatz (1997), [Dynamical Hysteresis without Static Hysteresis: Scaling Laws and Asymptotic Expansions](https://ggold.math.gatech.edu/research/DynamicalSIAM97.pdf). Read the primary paper's formulation of dynamic loops with vanishing zero-frequency area. Supports the need for a rate control; its scaling results are not imported as an untested exponent for this two-variable model.

**适用范围 / boundary:** the achieved increment is a parameter-identification
correction, a conditional fold theorem and counterexamples that constrain the
next experiment. A real boundary-maintenance mechanism remains unverified.
