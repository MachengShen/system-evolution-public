# Agency as Second-Order Persistence: why a "self-preservation term" is not enough, what would be, and what our own experiments did to the idea

Date: 2026-07-16 → 2026-08-19

Public index: [Theory Mainline](../THEORY.md) · Format: [Claim-Receipt](../CLAIM-RECEIPT.md) · Companion: [Exclusion Cannot Remember](2026-07-13-exclusion-cannot-remember-self-boundary-hysteresis.md) · Experiments: [mu-boundary D0–D2](2026-08-19-mu-boundary/README.md) · Next: [Boundary-Defense pre-registration](2026-08-19-boundary-defense-preregistration.md)

> **Cognitive state (per claim):**
> - "AI lacks subjectivity/agency because its objective lacks a self-persistence term" (literal version): 🔴 **retired as a lead** — it is a restatement of Friston self-evidencing / FEP, and Omohundro (2008) / Turner et al. (2021) show optimal policies under *any* reward already generalize self-preservation, so "generalized self-protection" is not an agency signature.
> - "First-order persistence (keep x in a viability set, static argmax) is a thermostat; agency requires *second-order* persistence — maintaining the boundary/projection μ that defines the self, via a state→coupling feedback loop (self-seal) — whose testable signature is hysteresis of the self-boundary": 🟡 speculative · **Confidence 0.45** (down from 0.6 after D2)
> - "Hysteresis of a self-boundary emerges from a precision gate without any hand-built bistability": 🟢 survived-stress-test · 0.85 (mu-boundary D2, a=0, A₀ 24–35× resolution floor, frozen-gate control at floor)
> - "…and that hysteresis is *about the self*": 🔴 **not supported** — the specificity control (same gate on a disturbance channel, gain matched) gives bit-identical hysteresis; the asymmetric time-constant prediction was falsified
> - "Constitutive vs instrumental persistence is itself new": 🔴 not new (= terminal-vs-instrumental in the corrigibility literature; Dennett/Searle constitutive-vs-derived intentionality). Only the *measurable separator* is ours.
>
> provenance: owner-posed thesis (2026-07-16), adversarial-panel audit (2026-07-16, Omohundro falsifier), data hunt + MuJoCo experiments D0–D2 (2026-07-28), owner decision 2026-08-19 to run a second-order "boundary-defense" experiment · **evidence:** mu-boundary RESULTS-D0 / D1-D2; human reanalysis (RHI order effect, synchrony-judgment sequential dependence) · **prior-art:** Friston FEP / self-evidencing (note: Biehl–Pollock–Kanai 2021, Aguilera et al. 2022 show the blanket⇒inference step needs unstated assumptions); Maturana–Varela autopoiesis; Aubin viability / homeostatic RL; Klyubin–Polani empowerment; Omohundro 2008; Turner et al. 2021; Hadfield-Menell et al. (off-switch); Man & Damasio 2019 homeostatic robots; Tononi & Koch 2015; Levin cognitive light cone.

## 1. The thesis as posed, and why the literal version dies

Thesis B (owner, 2026-07-16): AI lacks subjectivity/agency because its optimization target has no term about maintaining its own existence; endogenous vs exogenous goals.

Taken literally this is the free-energy principle restated (agents act to keep themselves in characteristic states because the goal is bound to their own persistence) — the third rediscovery on this line after Levin's light cone and Tononi–Koch's boundary bifurcation. Worse, it loses to Omohundro: self-preservation *emerges* from any sufficiently capable optimizer (Turner et al. 2021: optimal policies seek power / avoid absorbing states), so an agent trained with a plain exogenous reward also protects itself and generalizes that protection to novel threats. "It protects itself" is therefore **not** a discriminating signature. The first-draft experiment (persistence-term ablation in a gridworld) was discarded for this reason before it was run.

## 2. What is actually ours: first-order vs second-order persistence

- Putting persistence into a scalar objective (FEP / viability / empowerment) yields a **first-order homeostat**: argmax of a fixed functional = memoryless = a thermostat. A thermostat "maintains itself" and has zero subjectivity. Necessary, not sufficient.
- Agency needs **second-order persistence**: the system maintains not "x inside the viable set V" but **the V / boundary / projection μ that defines "me"**. That requires a **state→coupling** loop — μ sets attention / input gating → gating shapes the statistics → statistics re-confirm μ (self-seal). This makes the self-boundary **path-dependent = hysteretic**.
- The companion note proves the negative half: any argmax/exclusion criterion is a memoryless selection function; it locates a boundary but has no boundary *dynamics*, hence structurally no hysteresis. So "the missing term" is not a scalar added to a loss; it is a **feedback architecture**.
- Two sharp corollaries we still hold: (a) empowerment ≠ identity maintenance (number of reachable futures vs the projection that defines the agent); (b) endogenous vs exogenous = constitutive vs instrumental — instrumental self-preservation trades itself away once the external goal pays more (which is exactly what corrigibility designs rely on); constitutive persistence does not. Prediction: only the self-sealing version gives agency-like behavior; the instrumental version gives a tool that protects itself with no self present.

**Hard guard:** this program delivers *agency* (instrument layer: self-model, self-maintenance, self-referential closure). It does not and cannot deliver phenomenal subjectivity (the hard problem). The word "subjectivity" must be split before any experiment is called a demo of it.

## 3. The surviving discriminator after the adversarial audit

Omohundro / Turner / Hadfield-Menell are all *reward-mediated, optimal-policy, high-capability* theorems. They are structurally silent in two regimes: (i) **sub-threshold capability** (agent too weak to derive the instrumental drive), and (ii) **reward-orthogonal or reward-costly** boundary maintenance (an optimal exogenous agent provably does not spend effort on identity features unrelated to reward). All of B's remaining content lives in those two cells, plus a positive signature: **loop width monotone in self-seal gain g, zero at g=0** (Omohundro has no g). Honest warning recorded at the time: after narrowing, B and the self-boundary note share a **single point of failure** — the g-hysteresis bet.

Unifying corollary (A⋈B): the persistence term is the missing **selection principle** among the generally multiple closure fixed points μ=F(μ); representation emerges as "the coarse-graining the agent must maintain to keep existing". Falsifiable: if a persistence term does not reduce init-dependence of which fixed point is reached, the unification fails.

## 4. What the experiments did (2026-07-28, MuJoCo 3R arm, CPU)

Full numbers in [mu-boundary README](2026-08-19-mu-boundary/README.md), [RESULTS-D0](2026-08-19-mu-boundary/RESULTS-D0.md), [RESULTS-D1-D2](2026-08-19-mu-boundary/RESULTS-D1-D2.md); spec [v0.1](2026-08-19-mu-boundary/SPEC-v0.1-20260727.md).

| Step | Result |
|---|---|
| D0-pos protocol positive control | instrument works: hand-built double well gives A₀ ∈ [0.36, 0.62] (95% CI excludes 0); linear control at the resolution floor |
| D0 blanket partition on the arm | a non-trivial (self, blanket, world) partition exists; but the constraint is nearly uninformative and an unconstrained search collapses to \|S\|=1 in 87% of runs |
| D1 loop gain G>1 | reachable, but the criterion is nearly synonymous with "the boundary flips"; the real bottleneck is that costs must cancel gains to 1.3–2.6% relative precision while the objective's own coefficients are off by tens of × |
| **D2 emergent hysteresis (a=0)** | **positive**: A₀ = +0.19…+0.28 = 24–35× floor; frozen-gate control back at floor; bistability stay-rates 1.00/1.00 vs 0.47/0.43 |
| D2 specificity control | **narrative removed**: same gate on the disturbance ball, gain matched ⇒ identical hysteresis. Generic property of a gated slow variable, not of "self" |
| D2 §5.7 asymmetry | **falsified** (τ_off/τ_on = 1.008; 0.794 opposite direction with gate on the whole drive) |

Human-data anchor (same day): rubber-hand-illusion order effect is on the **adaptation** side (d = −0.76, N=185; expectancy DV), against hysteresis; synchrony-judgment sequential dependence is robust but sign-inconsistent across tasks and gone by lag-3. See [bsfwu order](2026-08-19-mu-boundary/human-reanalysis/RESULTS-bsfwu-order.md), [sync dry-run](2026-08-19-mu-boundary/human-reanalysis/RESULTS-sync-dryrun.md). Only anesthetic neural inertia remains as a hard human anchor, and it is not yet connected to a boundary measure.

## 5. Where this leaves the line (2026-08-19)

First-order hysteresis cannot carry the self-specific claim: a gated thermostat has it too. The only signature left that a gated thermostat *cannot* produce is **second-order behavior** — the agent acting to repair or resist a rewrite of its own boundary definition (re-acquiring a removed tool faster the second time; resisting a "cheaper" partition offered by the environment; re-carving μ without labels after a body swap), with a reward-max + first-order-viability RL agent and a gated-slow-variable control both failing. That is pre-registered in [Boundary-Defense](2026-08-19-boundary-defense-preregistration.md) and running as of today; our prior that it lands under natural parameters is ≤ 0.3.

A public, time-stamped sample of the literal version (a platform assistant independently proposing "write system-integrity maintenance as a hardware-level reward → shutdown conflict → proto-consciousness", 2026-08-02) is the natural foil: it is exactly the version the audit killed.
