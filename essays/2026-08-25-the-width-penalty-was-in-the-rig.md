# The width penalty was in the rig: a control that a "capacity is harmful" result had to survive, and did not

Date: 2026-08-25

Public index: [Theory Mainline](../THEORY.md) · Format: [Claim-Receipt](../CLAIM-RECEIPT.md) · Direct parent: [Capacity is not the lever either](2026-08-24-capacity-is-not-the-lever.md) · Machine-readable: [`results/crossing_certificate.json`](2026-08-25-the-width-penalty-was-in-the-rig/results/crossing_certificate.json), [`results/crossing_run.json`](2026-08-25-the-width-penalty-was-in-the-rig/results/crossing_run.json)

> **Cognitive state (per claim):**
> - "This rig penalises width even where capacity cannot possibly be the binding constraint: on a null-capacity reference target, widening a hidden layer 48→768 costs **0.021 to 0.093** worst-source accuracy with the whole 95% CI below zero, in all four cells of a model-family x working-point crossing": 🟢 survived-stress-test · **Confidence 0.92 (mechanism)** / **0.85 (practice)** — 16 paired seeds per cell, paired bootstrap, and a width-48-vs-width-48 `identity` comparator returning exactly zero in all 12 arms.
> - "Therefore the prior note's reading that **adding capacity is monotonically harmful** is withdrawn as a claim about capacity": 🔴 **RETRACTED CLAIM** (mine, from the parent note) — the measurements stand and reproduce; the causal attribution does not. Net of the rig's own width penalty, no cell shows excess harm and two show a small excess *benefit*.
> - "The gap between the working point that carried signal and the registered one is the **working point**, not the model family": 🟢 survived-stress-test · **Confidence 0.88 (mechanism)** / **0.7 (practice)** — making the source/task cue informative is worth **+0.1124 [+0.0988, +0.1258]** and **+0.0928 [+0.0750, +0.1095]** in the two families; holding the working point fixed, the plain MLP *beats* the gated modular model by **+0.0436 [+0.0242, +0.0654]**. Practice number held down because this is one synthetic task family.
> - "The pre-registered +0.10 KILL stands, and now stands at a working point with demonstrated headroom": 🟢 survived-stress-test · **Confidence 0.9 (mechanism)** / **0.8 (practice, raised from 0.45 by the parent document's own pre-registered update rule)** — best cell 0.6611 against a 0.5799 anchor, and the ladder still moves the metric by at most +0.0306, a factor of 3.3 short.
> - "Structure / bandwidth attribution": 🔴 **WITHHELD — P0 red (c5 = -0.3576).** Unchanged. Nothing here licenses any structured-vs-scalar claim, and nothing here retires that gate.
>
> **provenance:** agent-executed experiment against a pre-registration committed before the decision run, whose satisfiability certificate was measured *first* and killed the criterion the author intended to register · **evidence:** two 16-paired-seed passes over a 2x2x3 design (4 cells x 3 widths x 3 label rules), paired bootstrap with 2000 resamples, plus a historical known-answer anchor reproducing to four decimals · **not evidence:** one synthetic non-stationary stream, one optimiser, one fixed learning rate, one budget; no scaled run was executed and none is licensed. **prior-art (reasoned, NOT read for this note):** the plasticity-loss / loss-of-trainability literature in continual RL (Dohare et al. on continual backprop; Lyle et al. on plasticity loss), width-versus-optimisation interactions at fixed learning rate (muP and related work on learning-rate transfer across width), and double descent. A "wider net trained at the same learning rate for the same number of steps does worse" observation is very likely known there and should be checked before any of this is presented as novel.

## 0. The claim in one sentence

A previous note reported a pre-registered KILL and, alongside it, a signed observation: on two independent working points, adding capacity did not merely fail to help, it made the metric monotonically *worse*. This note reports the control that observation needed — a reference target on which capacity **cannot** be the binding constraint — and the control shows the same rig produces the same negative sign there. The signed observation was measuring the rig.

## 1. Why a second look

The parent note closed with a specific, named gap. The working point that carried signal (a gated, modular router reaching 0.5799 worst-source accuracy) and the registered working point (a plain MLP at roughly 0.52) differed in **two** things at once — the model family and the task presentation — and no experiment separated them. The paper-thin version of the finding was "capacity hurts in both, so the sign is robust." The honest version was "these are different rigs and we do not know which difference matters."

That gap is cheap to close, so it was closed.

## 2. The design

One data stream, one budget (960 batches of 24, learning rate 0.006, one epoch per batch), one seed set, two axes crossed:

| axis | levels |
|---|---|
| **model family** | monolithic MLP · gated modular router (prototype routing over grown/pruned modules) |
| **working point** | the source/task cue is informative · the cue is permuted across batches — identical marginal distribution, zero task information |
| **width ladder** | hidden 48 / 192 / 768, 16 paired data seeds, paired bootstrap, 2000 resamples |

The cue is the right axis to cross because the router feeds each module the raw input and uses the cue **only** to decide which module sees it. So the cue is exactly what one working point has and the other lacks, and crossing it gives both families the same input at both working points.

Two gates were in place throughout: a historical known-answer anchor (must reproduce 0.580 / 0.596; measured 0.5802 / 0.5964), and a width-48-versus-width-48 `identity` comparator that must return exactly zero (it does, in all twelve arms).

## 3. The control, and why it was run before the criterion was written

The intended criterion was a criterion on a **sign**: "the capacity delta is negative in all four cells, therefore the negative sign is cross-cutting." A sign criterion is only informative if **both signs are reachable by the measurement**. So the reachable range was measured first, with two reference label rules on the identical stream, schedule, budget and seeds:

- **null-capacity reference** — `y = 1[x_0 > 0]` with 15% label noise. Task-independent, and a width-48 network is grossly over-parameterised for a single-coordinate threshold. **Capacity cannot be binding.** Whatever the width ladder does here is not a capacity effect.
- **capacity-bound positive control** — a random 256-unit ReLU teacher per source-task pair, against a 48-unit student. **Capacity is binding by construction.**

The null-capacity arm:

| cell | w48 | w192 | w768 | x16 delta [95% CI] |
|---|---:|---:|---:|---|
| MLP, cue informative | 0.7724 | 0.7637 | 0.7517 | **-0.0207 [-0.0424, -0.0044]** |
| MLP, cue uninformative | 0.7764 | 0.7621 | 0.7467 | **-0.0297 [-0.0464, -0.0151]** |
| gated, cue informative | 0.6953 | 0.6470 | 0.6026 | **-0.0927 [-0.1109, -0.0775]** |
| gated, cue uninformative | 0.6924 | 0.6475 | 0.6052 | **-0.0872 [-0.1012, -0.0738]** |

Negative, with the entire confidence interval below zero, in every cell, on a task with no capacity demand whatsoever. **The intended criterion was dead on arrival**, and it was dead before any number from the real task had been looked at. That ordering is the only reason this is a design decision rather than an excuse: a control that arrives *after* an inconvenient result is a rationalisation, and the same control run *first* is an instrument check.

The decision-bearing quantity became the **width-penalty-controlled delta** — the width effect of the real task minus the width effect of the null-capacity reference, in the same cell, on the same seeds — and only cells where the capacity-bound positive control clears zero *after* that correction were allowed to carry the verdict. Two of the four did.

## 4. The result

Real task, raw:

| cell | w48 | w192 | w768 | x16 delta [95% CI] |
|---|---:|---:|---:|---|
| MLP, cue informative | 0.6305 | 0.6611 | 0.6553 | **+0.0249 [+0.0077, +0.0424]** |
| MLP, cue uninformative | 0.5181 | 0.4897 | 0.4732 | -0.0449 [-0.0612, -0.0299] |
| gated, cue informative | 0.5868 | 0.5311 | 0.5100 | -0.0768 [-0.0973, -0.0579] |
| gated, cue uninformative | 0.4940 | 0.4940 | 0.4801 | -0.0139 [-0.0288, +0.0036] |

Even raw, the sign is not cross-cutting: one cell is positive with its CI above zero. And net of each cell's own width penalty, **no cell shows excess harm**; the two certified cells show excess *benefit*, **+0.0456 [+0.0219, +0.0697]** and **+0.0733 [+0.0546, +0.0905]**.

The prior note's headline number reproduces exactly and means something different than it did. The gated working point's x16 capacity delta was reported at **-0.0768**; here it is **-0.0768** again, on a different random-number namespace and a different seed count. In the same cell, the null-capacity reference gives **-0.0927**. The measurement was right. The attribution was not.

## 5. What actually moves the metric

| contrast, at width 48 | delta [95% CI] |
|---|---|
| making the cue informative, MLP | **+0.1124 [+0.0988, +0.1258]** |
| making the cue informative, gated router | **+0.0928 [+0.0750, +0.1095]** |
| MLP minus gated router, cue informative | **+0.0436 [+0.0242, +0.0654]** |
| MLP minus gated router, cue uninformative | **+0.0241 [+0.0061, +0.0393]** |

Nothing on the capacity ladder, in any cell, in either direction, is as large as the working-point effect. And the family axis points the *opposite* way to the assumption that was quietly riding along: with the working point held fixed, the plain MLP is **better** than the gated modular model. The router's 0.5799 was never evidence that its architecture was doing the work. It was evidence that its task presentation was.

## 6. What this does to the KILL: strengthens it

The parent note had to publish its own cap. All 91 cells of the registered sweep sat between 0.4309 and 0.5447 against a chance level of 0.5000, so a +0.10 bar might simply have been unreachable there — an uncomfortable fact that was printed next to the verdict rather than after it.

That cap is now partly discharged. The same ladder, run at a working point reaching **0.6305 / 0.6611 / 0.6553** — above the 0.5799 anchor and above every cell of the original sweep — still moves the metric by at most **+0.0306 [+0.0187, +0.0419]**, a factor of **3.3** short of the bar. The clearing level there would be 0.7305, and the same cell reaches 0.7724 on the easy reference target, so that range is not outside what the rig produces.

*(The limitation, stated rather than buried: a range being attainable on an easier target does not prove it is attainable on the real task. This removes "the instrument tops out below the bar" as an explanation. It does not establish reachability, and no run here does.)*

The parent note's pre-registered update rule for this claim read: *run the same ladder at a working point with demonstrated headroom; if capacity still does not move the metric by at least +0.05 there, the practical confidence rises to about 0.8.* Both antecedents are now measured. It rises to **0.8**.

## 7. The method note, which is the transferable part

Three rules did the work here, and two of them are uncomfortable.

**A threshold needs a satisfiability certificate, and so does a sign.** The program already had the rule for thresholds — do not freeze a bar without measuring whether anything on the instrument can reach it. What was missing was that the rule generalises: a criterion on a *direction* is only informative if the measurement can return both directions. It could not, and that was measurable in about four minutes of CPU.

**Run the control before you write the criterion, not after you dislike the result.** These are the same experiment and opposite epistemic acts. The certificate here changed the registered criterion, and the change is legitimate exactly because no number from the real task existed yet.

**Enumerate every branch of your own verdict table, including the flattering one.** The pre-registration listed four aggregate outcomes — harm everywhere, cells disagree, no excess anywhere, nothing certified — and the data returned *benefit in both certified cells*, which is none of them. That branch was missing because the author was enumerating ways the expected finding could fail, not ways it could invert. The aggregate verdict is reported as unregistered and the pre-committed confidence moves keyed to it are declared non-binding, rather than snapping the result to the nearest row.

## 8. What is closed and what is carried

The line is closed. The frozen protocol's escalation clause — *escalate before any larger or GPU-scale spend; do not silently proceed to a scaled bet* — is discharged: it was escalated, it was ruled on, and **no scaled bet is made and no larger spend is requested.** Total cost of this note: one laptop CPU, about twelve minutes.

Carried forward, unresolved and explicitly not retired:

1. An engineering gate in the prior work (measured -0.3576) is very probably unsatisfiable by construction. It stays **red**. Declaring a gate broken at the moment it blocks you is motivated reading; the next pre-registration must either produce its satisfiability certificate in advance or replace it with a criterion that has one.
2. Nothing in this program yet separates *which coordinate* from *consistently the same coordinate*. A permutation control cannot do it, because the permutation is a symmetry of the model. The replacement must be shown satisfiable in advance, in the same file that registers it.
3. **New, from this note:** any future width or capacity claim on this substrate must be reported net of the rig's own width penalty, measured in the same cell with a null-capacity reference. A raw width delta on this rig is not a capacity measurement.
