# Does Vector-Valued Meta-Control Help Continual Learning? A Negative Result and a Diagnosis

*A pre-registered, smoke-scale continual-learning study. Public research log,
negative + diagnostic finding.*

---

## Abstract

Many continual-learning and meta-learning systems modulate their own learning
process with a control signal — a "meta-control" or valence variable that tunes
learning rate, exploration temperature, and replay. A natural question is
whether that signal should be a single **scalar** (a global neuromodulator-style
valence) or a **k-dimensional vector** carrying distinct axes such as prediction
error, anticipated information gain, learning progress, and hazard value; and if
a vector helps, what minimum dimensionality `k*` is needed. We pre-registered a
falsification of this question on a delayed-credit, multi-source continual-
learning benchmark with engineered inter-source interference. Across the study
we found: (1) an early null result was an artifact of under-training, not of
dimensionality; (2) a foundational bug — the meta-controller was an
**untrained, fixed-random network**, so all prior comparisons were measuring a
random readout rather than learned meta-control; (3) with a hand-coded **ideal**
controller on an environment engineered to require multi-axis reading, vector
meta-control did **not** significantly beat scalar on scheduling actions
(learning rate / replay / plasticity), and the scheduling action channel had
almost no leverage on accuracy (an ideal gate barely beat no gate at all); (4)
reframing meta-control to act on **structure** (module allocation / isolation)
gave only a small, sub-threshold improvement on the worst source (+0.075,
below our +0.10 precondition bar), and the dangerous source it was designed to
isolate barely moved (+0.009). We conclude that **meta-control — whether
scheduling or structural, whether scalar or vector — is not the lever for
worst-source continual learning in this benchmark.** The dimensionality question
is therefore moot here: extra control dimensions cannot help when the control
lever itself is weak. The binding constraint is the worst source's
**representation / capacity**, which neither a learning schedule nor parameter
isolation repairs — even a perfect oracle controller with perfect structural
isolation cannot rescue a representationally bottlenecked source. We report this
as a clean negative-plus-diagnosis, with the methodological caveat that the
study is smoke-scale (4–8 seeds), pre-registered, and run on a single benchmark.

---

## 1. The question

Self-modulating learners use a control signal to decide *how* to learn, not just
*what* to learn. Theory suggests this signal is multi-axis — prediction error,
anticipated information gain, learning progress (in the intrinsic-motivation
sense), and a pragmatic/hazard term are conceptually distinct and arguably
should not be collapsed. The competing intuition is that a single global scalar
valence is simpler and may be sufficient, as in coarse neuromodulatory schemes.

We turned this tension into a measurable quantity: the minimum dimensionality
`k*` of the meta-control signal.

**Pre-registered falsification.** In a delayed-credit, multi-source continual-
learning environment with interference, does expanding the meta-control signal
from scalar to a k-dimensional vector significantly improve mean and worst-source
(min-source) accuracy under compute-matched conditions? If so, where does the
accuracy-vs-k curve inflect (k\*)?

- *Falsify multi-dim:* if the scalar (k=1) bootstrap confidence interval
  overlaps the best k, a single scalar suffices.
- *Confirm + emit k\*:* if the curve flattens after some k* near a full-credit
  upper bound, k* is the minimum useful meta-control dimensionality.

The six candidate dimensions, accumulated in a fixed pre-registered order:
prediction error, anticipated information gain, learning progress,
pragmatic/hazard value, source novelty, and recurrence interval. The gate acts
on global learning rate, exploration temperature, and replay weighting.

**Pre-registration discipline.** All meta-control signals are estimated online
from environment observables. Three confound-controlling ablations were required
and any positive result missing one was to be discarded: a compute-matched
control (so improvement cannot come from added capacity), a random-vector
control (so improvement must come from signal content, not free parameters), and
a frozen-signal control (so online estimation must be doing work). We committed
in advance not to add seeds to chase significance, not to prune seeds, and not
to over-claim a marginal effect across the threshold.

---

## 2. What we found, stage by stage

### Stage 1 — An early null was just under-training
An initial pilot showed no significant benefit from vectorization (both
confidence intervals overlapped zero), which reads on the surface as "scalar
suffices." We rejected it as untrustworthy: the full-credit upper bound
*underperformed* every meta-learner and all absolute accuracies sat near chance.
The regime was simply under-trained — the meta-control signal was not yet biting
— so the accuracy-vs-k curve could not locate anything. Raising the training
budget roughly 6× fixed this. **Lesson:** a mechanical "run the codebook" process
would have shipped this null as a real "scalar suffices" finding.

### Stage 2 — Instrument validation
At an adequate budget the base learner became competent (well above chance on all
difficulty cells), the gate wiring transmitted (actuators moved with the signal),
and injecting correct oracle credit significantly lifted the worst source. But a
fidelity gradient was absent — degrading the oracle signal with noise did not
monotonically degrade accuracy, and on *mean* accuracy a correct oracle was
indistinguishable from a shuffled one. The environment rewarded credit-richness
only weakly, motivating a richer, engineered **dimension-conflict** regime in
which the meta-control axes genuinely disagree (e.g. a deceptive-stable source
that looks calm but is hazardous, and a novel-but-noise source that looks
informative but is not).

### Stage 3 — A foundational bug: the controller was never trained
On inspection, the meta-controller was a **fixed random network**: its weights
were initialized randomly and never updated. Every earlier comparison had been
measuring "does a *random* fixed readout of a k-dimensional signal help?" — not
"does meta-control dimensionality help when the controller has learned to use
it?" The original question was effectively unanswerable as run. We fixed this in
two stages: first a hand-coded **analytic ideal controller** as a ceiling (the
optimal gate for the engineered conflict sources), then a trained gate to see if
a learner approaches that ceiling. The ideal ceiling cleanly separates "the
signal/regime is insufficient" from "the controller cannot learn." **This bug
was caught only because each result was actively reflected on; a fixed pipeline
would have shipped the random-gate numbers as a finding.**

### Stage 4 — Ideal controller, scheduling actions: no significant vector benefit
With the bug fixed, the analytic ideal controller on the dimension-conflict
regime (8 seeds) produced no significant gain from vectorization: best-k vs
scalar on worst-source accuracy was +0.028 with a confidence interval just
touching zero, and slightly negative on mean. The controller demonstrably fired
its conflict-aware branches (actuator variance rose with k), so the mechanism
was active. **Critical caveat:** the scheduling action channel was weak — even
the ideal gate barely beat no gate at all (the scalar gate was actually *below*
no-gate on the worst source). So this is "no detectable vector benefit," not
"proven none": the study was under-powered in the *action* dimension, not the
signal dimension. We set a precondition — strengthen the action channel until an
ideal gate clearly beats no-gate — before drawing any scalar-vs-vector
conclusion.

### Stage 5 — Strengthening the scheduling channel failed the precondition
We strengthened the scheduling levers (elastic protection, replay source-
weighting, a wider learning-rate range). This made worst-source accuracy
*worse*, not better. An ablation identified the cause: the protection/freeze
lever is destructive on a **shared-weight** learner — freezing weights to protect
one source freezes *all* sources, because there is no per-source parameter
isolation. Replay weighting and learning-rate range were leverage-neutral. A
best-case oracle (rehearse the dangerous source heavily, never inject noise)
yielded **zero** worst-source leverage. This pointed away from scheduling
entirely: worst-source failure is data/representation-bound, not schedule-bound.

### Stage 6 — Reframing to structural actions: marginal and sub-threshold
We moved meta-control to act on **structure** — allocating, growing, and
isolating dedicated modules per source, using a modular substrate that does
provide genuine per-module parameter isolation. With an ideal structural
controller on the conflict regime (4 seeds), worst-source accuracy improved by
+0.075 (CI [+0.017, +0.146]) — statistically positive but **below the
pre-registered +0.10 precondition bar**, so we stopped (no k-sweep). The mean
improved more (+0.093) — i.e. most of the benefit was on the *average* source.
Crucially, the **deceptive source we explicitly force-grew, pinned, and isolated
barely improved (+0.009)**, even though isolation was verified real (the
deceptive sources received dedicated, pinned modules). Structural meta-control
helped the average a little and the actual hard case essentially not at all.

---

## 3. Conclusion

**Meta-control is not the lever for worst-source continual learning in this
benchmark.**

- *Scheduling actions* (learning rate / replay / plasticity on a shared-weight
  learner): zero worst-source leverage, even with an ideal controller and a
  best-case oracle.
- *Structural actions* (module allocation / isolation): marginal (+0.075,
  sub-threshold) and essentially no effect on the source it was designed to
  isolate (+0.009).
- Therefore the **scalar-vs-vector dimensionality question is moot here.** Adding
  control dimensions cannot help when the control lever itself has little
  leverage. The scalar intuition "wins" only in the trivial sense that nothing
  meta-control-shaped helps much — this is *not* a positive vindication of scalar
  valence.
- The binding constraint is the worst source's **representation / capacity.**
  Neither a learning schedule nor parameter isolation fixes it. Even perfect
  oracle knowledge plus perfect structural isolation cannot rescue a
  representationally bottlenecked source.

---

## 4. Methodological note

The most valuable output of this arc was procedural. A reflect-driven process —
treating every intermediate result as something to interrogate rather than
record — surfaced two failures that a mechanical pipeline would have shipped as
genuine findings: the under-training behind the early null (Stage 1) and the
untrained fixed-random controller (Stage 3). Either alone would have produced a
publishable-looking but false "a scalar meta-control signal suffices." The
analytic-ideal-controller ceiling was the key instrument: by establishing what a
*perfect* controller could achieve, it cleanly separated "the environment or
signal cannot support this" from "the controller failed to learn it," and made
the eventual negative result interpretable rather than ambiguous.

We also held pre-registration discipline: we did not add seeds to push a marginal
effect across the +0.10 bar, did not prune seeds, and explicitly declined a
post-hoc tweak (pinning earlier, raising interference) that would likely have
nudged the structural effect over threshold — that would have been p-hacking a
marginal effect across a pre-registered line.

---

## 5. Limitations (do not over-claim)

- **Smoke-scale.** 4–8 seeds throughout. We deliberately did not run a large
  (e.g. 32-seed) confirmation, because a large run on a regime where the lever is
  weak only buys tight confidence intervals around a near-zero effect.
- **Single benchmark.** One delayed-credit, multi-source continual-learning
  environment with engineered interference. The representation-bottleneck
  conclusion is specific to this benchmark family; we do not claim it generalizes
  to all continual-learning settings.
- **Negative result, narrow scope.** We show meta-control dimensionality does not
  drive worst-source performance *here*. We do not claim meta-control is useless
  in general, nor that vector valence is never beneficial — only that, with ideal
  controllers and adequate budget, it was not the operative lever in this regime.
- **Ideal-controller framing.** Much of the evidence uses a hand-coded optimal
  controller as a ceiling. A learned controller can at best approach this ceiling,
  so a weak ceiling is genuinely informative; but the absolute numbers reflect an
  idealized upper bound, not a deployed learner.

---

## 6. Next directions

- **Accept the negative result** as the honest answer to the pre-registered
  question (this log).
- **Pivot to the representational lever** the evidence points at: more capacity,
  better features, or a different mechanism for the hard (deceptive-stable)
  source — the constraint the study located.
- We explicitly *reject* the option of tuning the setup until the marginal
  structural effect crosses the pre-registered threshold.
