# Alterity as an Exploration Source: why a self-iterating agent needs a term in its objective it cannot write itself

Date: 2026-08-23

Public index: [Theory Mainline](../THEORY.md) · Format: [Claim-Receipt](../CLAIM-RECEIPT.md) · Companion: [Multimodal Gluing Obstruction](2026-08-19-multimodal-gluing-obstruction.md) · [Exclusion Cannot Remember](2026-07-13-exclusion-cannot-remember-self-boundary-hysteresis.md) · [Agency as Second-Order Persistence](2026-08-19-agency-second-order-persistence.md)

> **Cognitive state (per claim):**
> - "An objective is a function on the agent's own representation, so a coupling to something irreducibly outside that representation cannot be an argument of it; optimizing it silently substitutes the model of the other for the other": 🟡 speculative · **Confidence 0.7** — this is close to definitional given the projection setup, but the setup itself is a modelling choice.
> - "When an optimizer is pointed at such a coupling, it reduces the residual by *discarding* the obstructed structure rather than assimilating it": 🟢 survived-stress-test **in the representational rig only** · 0.75 mechanism / 0.4 transplant to control — measured in RESULTS-E4 P1c (field_ratio 0.75→0.41 and 0.84→0.66 under co-training where the analytic floor is > 0, versus 1.00→1.00 in the no-obstruction control, while the readout-bounded violation never fell below the floor, 0/150). The transplant from embeddings to an *agent coupling* is untested.
> - "Standard exploration machinery is self-sealing: every intrinsic bonus is a functional of the agent's own model, so improving the model extinguishes the bonus": 🟢 survived-stress-test · 0.85 — this is the known saturation of curiosity/RND/count-based methods and the known posterior concentration of assistance games; the only new part is naming them one failure mode.
> - "Bayesian uncertainty about another agent is *in-span and shrinks*; a gluing obstruction is *out-of-span and does not* — so assistance-game exploration and alterity-driven exploration are formally different sources": 🟡 speculative · **Confidence 0.6** unclaimed, 0.75 correct-if-the-obstruction-line-holds. This is the sharpest technical claim in the essay and the one to attack first.
> - "An unmodifiable terminal coupling is a *capability* precondition for open-ended self-improvement, not only a safety tax": 🟡 speculative · **Confidence 0.45** — the corrigibility literature has the object; the inversion of its purpose is the originality bet.
> - "Adversarial/self-play coupling is not alterity because the other's objective is a function of yours, hence in-span": 🟡 speculative · 0.55 — plausible account of self-play fixed points and mode collapse, but not derived and not tested.
> - "The philosophical content is new": 🔴 **not new.** It is Levinas verbatim (the Other is not reducible to the Same), plus Frank's *Passions Within Reason* (1988) for the commitment half. Only the formal transplant and the rig are candidates for originality.
>
> provenance: owner-posed thesis (2026-08-23, from a conversation about why love resists optimization), reasoned transplant of the THEORY-v3 cokernel formalism · **evidence:** RESULTS-E4 (P1c mechanism), RESULTS-E1 (overdetermination threshold), RESULTS-D3 (negative, boundary defense) · **prior-art (reasoned, NOT yet read):** Levinas; Frank 1988; Schelling; Lehman & Stanley novelty search; Wang/Lehman/Clune/Stanley POET & minimal criterion coevolution; Leibo autocurricula; Baker et al. hide-and-seek; Pathak curiosity / Burda RND; Klyubin–Polani empowerment; Hadfield-Menell CIRL / assistance games; Everitt & Hutter self-modification; Soares et al. corrigibility; Friston FEP dark-room problem. **None of these were re-read for this essay** — §4 is reasoning about the literature, not a literature check, and should be read as a to-verify list.

## 0. The claim in one sentence

An objective is a function on the agent's own representation; a coupling to something irreducibly *outside* that representation therefore cannot be an argument of the objective — and when you point an optimizer at it anyway, the optimizer's available move is not to understand the other but to **re-carve the agent's own representation until the other fits**, which deletes exactly the part that was doing the work. So "optimizing this destroys it" is a type statement, not a sentiment. The corollary for design: a self-iterating agent needs a component of its objective whose *time derivative lies outside its own span*, and nothing built from inside the agent can supply that.

## 1. Why the standard exploration machinery cannot supply it

Every mechanism the field uses to keep an agent from converging is a functional of the agent's own state or model. That is the whole problem, stated once:

| mechanism | why it is self-sealing |
|---|---|
| ε-greedy, entropy bonus | noise expressed in *known* coordinates; it perturbs the point, never the span |
| curiosity / RND / count-based novelty | bonus `b = f(model error)`; improving the model drives `b → 0` **by construction**. The noisy-TV pathology is the degenerate escape, not a counterexample |
| meta-learned objectives | the level-(n+1) objective is still a function on the same representation; the regress does not terminate inside the agent |
| Bayesian reward uncertainty (CIRL / assistance games) | the human's reward is a parameter θ *inside* the hypothesis space; the posterior concentrates, so the query incentive → 0 |
| self-play / GAN / adversarial curricula | the other's objective is a **function of yours** (often exactly −J), hence fully determined by you, hence in-span. This is a candidate account of why self-play lands on fixed points and cycles, and why adversarial exploration mode-collapses |
| active inference / free energy | surprise minimization seals the agent in (the dark-room problem); the standard fix adds an epistemic-value term which is, again, a function of the agent's own model, so it saturates the same way |

The common shape: **the source of novelty is a functional of the agent's own state, so getting better extinguishes it.** Call it *self-sealing exploration*. It is not a tuning problem. Adding a bigger coefficient to a term that is structurally headed to zero buys time, not a different asymptote.

The one distinction worth isolating: **uncertainty is not alterity.** A diffuse posterior over a parameter inside your hypothesis space is *in-span*, and it shrinks — that is what a posterior is for. An obstruction is *out-of-span*, and no amount of data moves it, because there is no coordinate in which to move it. Assistance games buy the first and are routinely described as if they bought the second.

## 2. What the gluing obstruction adds

**Setup.** Agent A has a representation `Z_A` reached by a lossy projection `π_A`. Another agent B has its own `Z_B` and its own generative dynamics. A's access to B is `π_A(B)`. The THEORY-v3 result transplanted in [the multimodal line](2026-08-19-multimodal-gluing-obstruction.md): when the consistency constraints exceed the latent degrees of freedom, the cokernel residual `r_perp` is generically nonzero, and structure living in `ker(π_A)` is not merely unknown — it is **not expressible**.

Two consequences follow, one trivial and one measured.

**(i) The type error.** `J` is a function on `Z_A`. So `J(B)` is really `J(π_A(B))`. Optimizing "the coupling" optimizes the *model of the other*, never the other. This is trivially true and usually ignored, because for most objects the projection loss is small enough not to matter. For another agent with its own irreducible latent, it is the whole story.

**(ii) The optimizer's actual move, measured.** In the synthetic rig of RESULTS-E4, contrastive co-training's reduction of the measured residual was carried by **field collapse**, not by repair: `field_ratio` fell 0.75→0.41 and 0.84→0.66 in the configurations where the analytic floor is > 0, against 1.00→1.00 in the no-obstruction control, while the readout-bounded violation `V_lin` never went below the analytic floor at any checkpoint (0 of 150 checkpoint×seed). Registered prediction P1c, confirmed. On real models, a linear repair head on frozen independent towers improved mutual-kNN alignment past CLIP's level on the same split (0.063 vs 0.050) and shrank the discrepancy field (0.56→0.41) yet left the noise-corrected cokernel residual essentially unchanged (0.0356→0.0396).

Read that as a statement about coupling and it says: **an optimizer pointed at an unmodelable other reduces its dissatisfaction by re-carving its own representation until the other fits — i.e. by ceasing to see the part that did not fit.** Not assimilation. Deletion.

That is the mechanism behind "optimizing it destroys it", and it is *measured* in a rig we own, not asserted. The honest caveat is large: E4 is representational, not behavioral. Nothing in it shows that an *acting, coupled* agent does the same thing. §5 is the rig that would decide it, and until that rig runs, the transplant is a hypothesis with confidence 0.4.

**Why the residual is the exploration source.** `r_perp` is the only part of the world that is simultaneously (a) persistently coupled to A, (b) outside A's hypothesis space, and (c) *generative* — B keeps acting under its own dynamics, so the residual keeps emitting trajectory that A could not have sampled from its own model. Intrinsic-motivation bonuses sample new *points* in a known space; this supplies directions not in the span. The difference between novelty and alterity is the difference between a new sample and a new coordinate.

## 3. Four design elements

The design surface is not `J`. It is the **boundary condition on `J`** — which part of the objective is sealed off from the optimizer and wired outward.

**D1 — Exogenous drive.** Require `P_ker(π_A)(dJ_t/dt) ≠ 0` persistently: the objective must keep changing in directions A cannot represent. This cannot be constructed from inside. It requires a coupled optimizer whose objective is **not a function of A's**: not a teacher (objective derived from A's performance), not an adversary (derived and negated), not a stationary environment. Concretely: a second agent with its own reward, its own history, and no readout of its internals.

*Weakest joint, attack here first:* how is this different from "the environment is non-stationary"? A non-stationary environment is still a distribution A can eventually model. The claim needs the other's state to be **persistently unmodelable**, not merely time-varying. If a fixed-but-unlearnable random operator inside the agent reproduces the same long-horizon effect, D1's necessity is dead and this whole essay reduces to "add more noise".

**D2 — A sealed terminal weight.** If the coupling weight `w` to B is itself subject to A's meta-optimizer, then — since an irreducible residual is *indistinguishable from irreducible cost* to any `J` defined on `Z_A` — the optimizer drives `w → 0` in finite time. The coupling must therefore be **terminal** (valued non-instrumentally) and **non-editable by A's own update rule**.

The inversion worth stating loudly: the corrigibility literature wants un-self-modifiable values for *safety* and prices them as an alignment tax. This says an unmodifiable terminal coupling is a **capability precondition** for open-ended self-improvement. **Self-iteration requires a non-self-iterating anchor.** An agent all of whose values are revisable converges on the easiest value to satisfy — which is the same collapse as E4's field collapse, one level up, and is the structural content of wireheading.

**D3 — Hysteresis on attachment.** Even sealed, a coupling that is *re-evaluated* each step against local cost gets dropped whenever the residual spikes — and the residual is precisely where the payoff is unpredictable. So detachment needs a wide band: a state→coupling feedback with gain `g`, ring width monotone in `g`, zero at `g = 0`. This is literally the self-seal object of [Exclusion Cannot Remember](2026-07-13-exclusion-cannot-remember-self-boundary-hysteresis.md), arriving here from an independent direction — learning dynamics rather than consciousness boundaries — which is mild corroboration that the object is real and not a rhyme. It also proposes an answer to the parked question "is the bistable window an attractor of learning?": the window is what keeps an exploration source attached across the interval where it pays negative marginal reward.

**D4 — A structurally blank region of the objective (weakest, 0.3).** Not a diffuse prior — §1 says diffuse priors concentrate. A subspace on which `J` is *undefined* rather than uncertain, and defended from inference. I do not have a construction for this that is not just "a very slow posterior", and flag it as unfinished rather than dropping it, because it is the piece that would make "designed unknowability" an engineering object instead of a slogan.

## 4. What is actually new (honest grading)

- The philosophical claim is **Levinas**, verbatim. Zero originality at the level of insight.
- The commitment half is **Frank (1988)** and **Schelling**: emotions as precommitments whose value comes from being immune to marginal recalculation. Covers "non-optimizable is what makes it credible"; does **not** cover the exploration function, which is the part this essay is about.
- "Abandon the objective" is **novelty search** and the open-endedness line (Lehman & Stanley; POET; minimal criterion coevolution). Closest prior art. Claimed distinction: their novelty is measured in a *designer-chosen behavior characterization* — in-span. Confidence 0.5 that this survives contact with the actual papers.
- "Other agents as an inexhaustible curriculum" is **autocurricula / coevolution** (Leibo; Baker et al.). Claimed distinction: those couplings are competitive and derived, and they do cycle. Confidence 0.5.
- Un-self-modifiable values: **corrigibility**, **Everitt & Hutter**. The capability inversion in D2 is where the originality bet sits. Confidence 0.45 unclaimed.
- The claim this essay would defend hardest: **in-span uncertainty versus out-of-span obstruction as two formally distinct sources of exploration**, with the second not extinguished by learning. Confidence 0.6 unclaimed.

Per [prior art is evidence, not verdict]: none of the above is a verdict, and none of it is a literature *check*. It is reasoning about remembered literature and must not be cited as if it were verified.

## 5. The cheapest decisive rig (specified, not queued)

Two-agent particle or gridworld environment, private latents, reusing the existing E1 cokernel machinery and the mu-boundary sweep protocol.

**Arms.** C0 no coupling · C1 instrumental coupling (B's state enters A's optimizable reward, weight learnable) · C2 sealed terminal coupling weight, non-editable · C3 = C2 + hysteresis band with gain `g` · Baselines: RND and entropy bonus, no second agent.

**Measures.** `r_perp(Z_A, Z_B)` through training · `field_ratio` (does A's carving collapse?) · long-horizon state-visitation coverage · detach time for `w` in C1.

**Registered predictions.**
- **P-a** (direct E4 transplant): C1 → `field_ratio` falls, `r_perp` falls *by collapse*, and long-horizon coverage returns to C0 level. Optimizing the coupling costs you the coupling.
- **P-b**: C2 → `r_perp` holds above a nonzero floor; coverage stays above baselines at long horizon.
- **P-c**: baselines' intrinsic bonus → 0 and coverage saturates; C2/C3 does not saturate.
- **P-d**: in C1 with editable weight, `w → 0` in finite time with probability → 1; C3's detach time is monotone in `g` and minimal at `g = 0`.

**Falsifiers.** RND matches C2 at long horizon ⟹ alterity buys nothing over in-span novelty and the wedge is dead. C2 collapses like C1 ⟹ sealing is insufficient, D2 dead. C1 shows no field collapse ⟹ the E4 mechanism does not transplant to control, §2(ii) dead and the essay is a metaphor.

Cost: order of one to two days on CPU. All machinery already exists.

## 6. Status

**Parked by default; no compute requested.** The multimodal line is deliberately at rest as of 2026-08-19 and this essay does not restart it and does not need the previously-specified next experiment on that line. It is recorded because, if the line is ever resumed, §5 is a better handle: it makes the obstruction do **behavioral** work — which nothing in E1/E2/E4 did, all of them being representational — and it folds the parked bistable-window question into the same rig.

The reason to write it down now rather than run it: the claim is currently a transplant across two domains on the strength of one confirmed mechanism prediction. Writing the falsifiers before there is any incentive to protect the idea is the only cheap part of this that is guaranteed to be worth doing.
