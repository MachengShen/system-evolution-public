# Capacity is not the lever either: a pre-registered 91-cell sweep returns its KILL branch, and the same run shows the assay could only ever have seen a very large effect

Date: 2026-08-24

Public index: [Theory Mainline](../THEORY.md) · Format: [Claim-Receipt](../CLAIM-RECEIPT.md) · Direct parent: [A permutation control cannot separate "which coordinate" from "consistently which coordinate"](2026-08-24-permutation-controls-cannot-separate-structure-from-routing.md) · Machine-readable: [`results/s1_cells.json`](2026-08-24-capacity-is-not-the-lever/results/s1_cells.json)

> **Cognitive state (per claim):**
> - "The registered sweep ran to completion at its registered budget (91 cells, 32 paired seeds each, 960 batches) and its pre-registered terminal is `KILL_ESCALATE`: no capacity or feature rung cleared +0.10 min-source with the bootstrap CI lower bound at or above +0.10, anywhere on the width ladder, the depth ladder, or the learned-feature/pretrained arm": 🟢 survived-stress-test · **Confidence 0.97** — deterministic bookkeeping over the run record. All nine decision-authority flags true, all three B4 invariants true, all three clearing lists empty.
> - "On this registered harness, capacity and features are not the rescuable lever": 🟢 survived-stress-test · **Confidence 0.90 (mechanism)** / 🟡 **0.45 (that this transfers anywhere useful)** — the highest capacity-delta CI lower bound anywhere on the ladder is **+0.0123** against a required +0.1000, and the upper rungs mostly point the wrong way (10/13 x16-width cells, 9/13 x16-depth cells and 13/13 frozen-pretrained cells have a *negative* capacity delta). The practice number is low for the reason in the next bullet.
> - "**This assay had almost no headroom.** Every one of the 91 cells sits in 0.4309–0.5447 against a chance level of 0.5000, and not one of the 13 mechanism-by-channel families comes within 0.0788 of its own +0.10 threshold": 🟢 survived-stress-test · **Confidence 0.95** — direct measurement, in the same file as the verdict. This is a cap on the result, published in the same breath as it, not a later excuse.
> - "Because the program's own rule says +0.10 is a **hypothesis** threshold and not an engineering gate, 'nothing reached it' means the hypothesis is false rather than the ruler being broken — and that reading is kept side by side with the headroom fact rather than resolved in the rig's favour": 🟡 speculative · **Confidence 0.6** — this is a methodological commitment, not a measurement. It is the honest position and it is also unsatisfying, which is why it is stated rather than smoothed.
> - "The frozen text's by-elimination clause therefore fires: the credit-transport line is refuted at small scale": 🟡 speculative · **Confidence 0.75 (the clause fires as written)** / **0.35 (that it is a good guide to what happens at scale)** — the clause is frozen and its antecedent holds. The de-rating is about the elimination chain it rests on, several links of which were measured on harnesses with the same headroom problem.
> - "Structure attribution": 🔴 **WITHHELD.** See §5. Nothing here licenses any structured-vs-scalar or 'more bits vs structure' claim.
>
> provenance: agent-executed registered experiment against a frozen pre-registration written before any run · **evidence:** the full run record (91 cells x 32 paired seeds, paired bootstrap, 2000 resamples) plus five named pre-run probe artefacts · **not evidence:** no scaled run was executed and none is licensed by this; the gated-working-point comparison in §4 is a different model family and no experiment here discriminates the two. **prior-art (reasoned, NOT read for this note):** direct feedback alignment (Nokland 2016), feedback alignment (Lillicrap et al. 2016), predictive coding / equilibrium propagation (Whittington & Bogacz; Scellier & Bengio), forward-forward (Hinton 2022), and the continual-learning capacity/plasticity literature — the "wider net does not fix the worst task" observation is very likely known there and should be checked first.

## 0. The claim in one sentence

A prior arc of negative results had concluded that credit-side levers do not move worst-source continual learning, and an adversarial review reframed the bottleneck as **representational capacity** rather than credit. That reframe was pre-registered as a cheap, decisive precondition before any larger bet. It ran. **Nothing on the capacity ladder moved the metric**, so by the frozen rule the reframe fails and the larger bet's premise is contradicted by its own precondition — and the same run shows the test could only ever have distinguished "no effect" from "very large effect," which is a fact about the test that has to travel with the verdict.

## 1. What was registered, and what ran

Two axes crossed: credit mechanism (plain backprop, direct feedback alignment, forward-forward, a predictive-coding nudge) against representational capacity (a width ladder, a depth ladder, and a raw-input / learned-feature / frozen-pretrained feature arm), on a non-stationary source-switching task with a deceptive worst source. Primary metric: **min-source accuracy**, the worst source's held-out accuracy. Decision rule, fixed in advance: a rung clears only if the gain is >= +0.10 **and** the bootstrap CI lower bound is >= +0.10. Plain backprop is re-run inside every cell as the matched-capacity reference.

Executed: **91 cells**, **32 paired seeds** each, 960 batches, learning rate 0.006, 2000 bootstrap resamples, local CPU, no accelerator. All nine registered decision-authority conditions true (seeds, batch count, both ladders exact, mechanisms complete, channels complete, paired-seed convention, trust gates green, mechanism known-answers green).

## 2. The result

```
KILL_ESCALATE
No capacity/feature rung clears +0.10 with CI lower bound >= +0.10.
```

The pre-registered exhaustive truth table:

| predicate | meaning | value |
|---|---|:--:|
| `A` | any capacity/feature rung clears +0.10 with CI lower bound >= +0.10 | **FALSE** |
| `P` | any **plain backprop** rung clears it (the "decoration on scaling" trap) | **FALSE** |
| `D` | any non-BP cell clears while its matched-capacity BP does not | **FALSE** |
| `U` | any unquantised (`full_precision`) arm beats its matched-capacity BP | **TRUE** (diagnostic only) |

All three invariants (`P->A`, `D->A`, `A and not D -> P`) hold, and the table is exhaustive: `A=P=D=0` is the single reachable row whose terminal is the KILL branch. `U` was added in the construction pre-registration as a conjunct that can only ever **narrow** the anti-signal terminal; it never enters `A`, `P`, or `D`, and the KILL branch is deliberately not conditioned on it, because when nothing clears anywhere — including *unquantised* plain backprop, which is not throttled at all — bandwidth starvation cannot be the explanation.

Mechanism-versus-matched-BP deltas, over the 84 cells that have a paired BP reference:

| mechanism | cells | mean delta vs matched BP | range | cells above BP |
|---|---:|---:|---|---:|
| `dfa` | 28 | -0.0062 | -0.0751 .. +0.0342 | 18 |
| `predictive_coding` | 28 | -0.0146 | -0.0738 .. +0.0337 | 14 |
| `forward_forward` | 28 | -0.0694 | -0.0932 .. -0.0103 | 0 |

Forward-forward is below its matched-capacity backprop in **every** cell. Direct feedback alignment and the predictive-coding nudge straddle zero at effect sizes an order of magnitude below the registered bar.

Full per-cell numbers: [`results/s1_cells.json`](2026-08-24-capacity-is-not-the-lever/results/s1_cells.json).

## 3. What the frozen rule licenses (quoted, not paraphrased)

> - representation is **not** the rescuable lever at this scale, **and**
> - by elimination — meta-control already failed, credit-richness already destabilized, and now capacity/features also fail — **the credit-transport line is refuted at small scale.**
> - **Escalate before any larger / GPU-scale spend; do not silently proceed to a scaled bet** whose premise this small-scale precondition just contradicted.

That is the frozen §3a text, written before any run, and `A = false` is exactly its antecedent. The anti-signal clause §3b does not fire, because `P = false`: there is no capacity-scaling win to record as decoration on standard scaling. The escalation is an owner-level decision and is open at the time of writing; nothing scaled has been started.

## 4. The caps, published with the result rather than after it

**4.1 The working point has almost no headroom.** Every cell lands in **0.4309–0.5447** against chance at **0.5000**; the best arm in the whole sweep is only **+0.0447** above chance. The +0.10 is a *within-family* delta against the same mechanism and channel at the bottom rung, so the level a cell must actually reach is its own baseline plus 0.10 — roughly 0.62 for the backprop and DFA families. **Not one of the 13 families comes within 0.0788 of its own threshold** (best shortfall -0.0788, worst -0.0939).

This is not a power problem. Computed from the run's own per-seed values, the minimum detectable effect at 80% power for the 78 capacity contrasts (paired, two-sided, alpha 0.05, 32 seeds) is **0.0080–0.0303** — three to thirteen times *smaller* than the bar. The design would have seen a real +0.05. It saw nothing because there is no room above chance for a +0.10 to occupy. The unquantised upper-bound arm agrees from the other side: at the registered budget its best cell reached **0.5443**, against a clearing level of **0.6382**, and a pre-written oracle criterion ("oracle (full_precision) min_source >= 0.62") failed at every learning rate tried.

**So this assay could only ever distinguish "no effect" from "very large effect."** A real +0.05 lever would have been invisible to it.

**4.2 And a hypothesis threshold is not a broken ruler.** The program's own rule separates two kinds of bar. The +0.10 is a **hypothesis threshold** inherited deliberately from the prior arc (where a +0.075 effect correctly fell below it) precisely to foreclose post-hoc threshold-shopping; nothing reaching it means **the hypothesis is false**. An *engineering gate* that nothing can reach is a different animal — that one means the ruler is broken. Declaring the first kind unreachable *after* watching it go unreached is the exact move the pre-registration was written to forbid.

So both statements stand, side by side, and this note does not resolve them in the rig's favour: the KILL is not withdrawn on account of 4.1, and 4.1 is not suppressed on account of the KILL. What is honestly missing is that nobody produced a satisfiability certificate for +0.10 on this harness *before* the run; when one was produced afterwards, it failed.

**4.3 The no-headroom excuse was partly pre-empted, on purpose, before the run.** The alternative explanation — "`A` is false only because this harness has no signal at its working point" — was written down as a pre-registered ALT *before any result existed*, together with the split that had already been run against it. On a **gated** historical working point that does carry signal (known-answer anchor 0.5800, reproduced 0.5799 at 16 seeds and 0.5802 at 4 seeds), capacity was **monotonically harmful**: -0.0578 at x4 width (95% CI [-0.0794, -0.0341]) and -0.0768 at x16 (95% CI [-0.1047, -0.0466]), both CIs entirely below zero. That is the *opposite sign* from the capacity hypothesis, on the axis the ALT would have rescued.

It does **not** eliminate the ALT. The gated protocol is a gated/modular model family; the registered sweep uses a plain MLP. No experiment here discriminates the two families, and saying otherwise would be exactly the kind of tidy-up this note is trying not to do.

## 5. Structure attribution: withheld

**§2 attribution = WITHHELD - P0 red (c5 = -0.3576)**

The pre-registration's confound control — scalar versus structured credit at matched bandwidth — is reported by this run as withholding its attribution entirely, on a red positive-control gate. The [direct parent note](2026-08-24-permutation-controls-cannot-separate-structure-from-routing.md) explains why: the permutation twin built to make "structure" hard to claim is degenerate in both directions, and the gate that was supposed to police it was itself a collision counter. Neither the twin, nor the entropy tolerance, nor the estimator appears anywhere in the frozen text; all three were implementer inventions layered on top of a frozen paragraph that asked only for a recording rule. **Nothing in this run supports any structured-versus-scalar or "more bits versus structure" claim.** The bit-matched control is retired to diagnostic status and gates no terminal.

One consequence deserves to be stated against interest. The failing criterion (`structured >= 2x twin`, measured **-0.3576**) is *probably an unsatisfiable gate*: at cold start a fixed-bijection twin retains 90–121% of the un-permuted arm's credit-attributable learning across the measured bijection families, so the criterion cannot be met wherever the twin is a symmetry of the model. **It was deliberately not acted on.** Declaring a gate broken at the moment it blocks you is motivated reading, and the ruling was to leave it red and hand over what it protects rather than to unlock it. It is carried forward as an open item for the next pre-registration.

## 6. Named implementer choices

The frozen text is silent on all of these. They were chosen by the implementer, and naming them is part of the result:

1. **Twin attribution disabled** — the structure-attribution label is hard-coded to withheld and the corresponding flag is permanently false.
2. **"Matched" bandwidth discharged as *frame* bandwidth, not empirical entropy** — within each geometry the three local channels carry identical fixed frame bits by construction; empirical entropy is reported as a diagnostic and gates nothing.
3. **The twin is retained as a recording arm only** — its data is archived and may not support any structure claim anywhere.
4. **A narrow reading of the construction pre-registration's stop rule** — a red positive control seals the attribution axis it protects, leaving the capacity and mechanism decision paths in force — was ruled and written down **before** the run started, not after seeing the result. It changed no frozen file.

## 7. The transferable lesson

The prior note in this series ended on *an ablation applied where the thing it ablates is a symmetry of the model will report "no effect" for reasons that have nothing to do with the hypothesis.* This one adds its sibling:

> **Before freezing a threshold, produce a satisfiability certificate for it on the actual apparatus: name something in the rig that could reach the bar.** A threshold nobody can reach on your harness turns every run into a foregone conclusion — and you will not notice, because the run's output will look exactly like a clean negative result.

And the sharp edge on that lesson, which is why it is stated here rather than used: **the certificate has to be produced *before* the run.** Produced afterwards, by whoever is unhappy with the outcome, it is indistinguishable from threshold-shopping — and the fact that this one is, on the numbers, probably *correct* does not fix that. That is the honest, uncomfortable shape of this result, and it is published in that shape.

## 8. What would change the verdict

- Run the same registered ladder at a working point with demonstrated headroom — an arm at or above the gated protocol's 0.5799 — and see whether capacity moves min-source by >= +0.05. If it does, the confidence on "capacity is not the lever" drops sharply; if it does not, it rises.
- Re-derive the clearing flags and both delta CIs from the per-seed arrays with an independent bootstrap. If they reproduce, section 2 is not in doubt and the argument moves entirely to 4.1 versus 4.2, which is where it belongs.
- Show that two or more links in the by-elimination chain were themselves measured on harnesses with this headroom defect. That would take "refuted at small scale" down to roughly a coin flip.

No scaled or accelerator-backed run has been started, and none is licensed by this note.
