# Task-Orthogonal Minimal Leakage: When Can You Safely Delegate to an Untrusted Model?

Date: 2026-06-12

Public index: [Theory Mainline](../THEORY.md) · Format: [Claim-Receipt](../CLAIM-RECEIPT.md)

> **Cognitive state:** 🟡 speculative · **Confidence:** 0.55 · provenance: reasoned synthesis over an established formal object (Privacy Funnel) plus an open frontier; presented as a research direction. **Evidence/prior-art:** Privacy Funnel (Makhdoumi, Calmon, Médard 2014) as the dual of the Information Bottleneck (Tishby, Pereira, Bialek 1999); adversarial / censoring representation learning (controllable invariance). **Aligns-with / extends:** Information Bottleneck; rate–distortion; minimal-sufficient-statistic. A speculative tag means the *frontier* claim (the bounded-adversary middle and the per-task-class test) is an idea worth testing, not an established result.

---

## The wrong goal, and the right one

Suppose an agent wants to delegate a sub-computation to a compute provider it does
not fully trust — a cheaper model, a third-party endpoint, any box that will see
the input in plaintext because it must read it to do semantic work. The instinct
is to frame this as **confidentiality**: "make it so they cannot read the data."
Against a model that must read plaintext to be useful, that framing is close to
hopeless. Homomorphic encryption and secure multi-party computation need the
provider's cooperation and are impractically slow for large models; trusted
execution needs the provider to offer confidential inference at all. You usually
cannot stop a useful reader from reading.

The better-posed goal is **adversary-utility minimization**, not confidentiality.
Whatever you leak should be **orthogonal to the adversary's objective** — readable,
but of no practical applied value *to them*.

## The formal object

Release a representation `X'` of input `X` such that:

- `I(X'; Y_task)` is **high** — the untrusted model can still do the intended task;
- `I(X'; Y_adv) → 0` — `X'` is useless with respect to the adversary's target.

This is exactly the **Privacy Funnel** (Makhdoumi, Calmon, Médard 2014), the
information-theoretic **dual of the Information Bottleneck**. "Orthogonal" means
`X'` lives in the task-relevant subspace and is approximately null in the
adversary's target subspace. It has gradient-based operationalizations:
adversarial representation learning, censoring representations, controllable
invariance — train an encoder so a discriminator cannot recover `Y_adv` while the
task head still works.

## Why it is genuinely open

The tractable, interesting part is not the textbook version. Two things sharpen it:

**1. Orthogonality is defined relative to *whose* objective.** Against one concrete
adversary target — re-identify the user, extract a strategy, harvest a trainable
corpus — the privacy funnel is solvable. But a general foundation-model provider's
effective "objective" is the **supremum over all future uses**. Minimizing leakage
against that universal adversary collapses to compressing everything except the
task channel — i.e. to a near-minimal sufficient statistic — at which point you
might as well have run the task locally. So the interesting middle is to defend a
**bounded class** of adversary objectives, not the universal one. The shape of the
utility–leakage frontier (the privacy-funnel curve) over that bounded class is the
research object.

**2. There is an economic frontier.** The cheap model is useful *because* it eats
natural language at maximum bandwidth. Pre-compressing the input into a
task-minimal code requires a task-specific encoder — and a good-enough encoder can
cost about as much as the task itself. So there is a hard constraint: **encoder
cost ≪ task cost**, or the scheme saves nothing. This single inequality filters out
most naive "just encrypt it" proposals.

## The decidable deliverable: a per-task-class orthogonality test

The theory pays rent by sharpening a routing decision. Today the common rule is a
binary "is this sensitive or not." A sharper test asks whether the **task-output
axis is orthogonal to or parallel to the sensitive axis**:

- **Orthogonal** — e.g. classify a ticket's urgency, where urgency is independent
  of *who* or *what secret* is in the ticket. Here a privacy-funnel encoding *can*
  in principle make untrusted-model use safe.
- **Parallel** — e.g. summarize a private conversation, where the wanted output
  *is* the sensitive content. Here no encoding helps; the work must stay on a
  trusted model.

This is stronger than sensitive-vs-not: it tells you which task classes are *even
in principle* safe to route to cheap untrusted compute, before you try.

## The general primitive

This is not only about untrusted external models. It is an agent-OS primitive:
**need-to-know representation transport** — when an agent delegates a sub-task to
any compute it does not fully trust, transport only the minimal sufficient
representation *for that sub-task*. It generalizes to any untrusted delegation, and
it sits in the same family as the broader information-dynamics line: transport only
the information that should be transported, and no more.

## Candidate techniques

Privacy-funnel / IB encoders; adversarial representation learning (a discriminator
cannot recover `Y_adv` while the task head still works); split compute (do the
sensitive-axis-bearing part locally, send only the orthogonal residual);
structure-preserving substitution (e.g. in code review, replace identifiers and
business semantics with isomorphic dummies that preserve the bug structure).

## Open sub-questions (the falsifiable surface)

- How broad an adversary-objective class is defensible while keeping the untrusted
  model useful? (the frontier shape)
- What are cheap, measurable proxies for `I(X'; Y_adv)` per bounded adversary class?
- Where exactly does the `encoder-cost ≪ task-cost` line fall for real task classes?

**Anti-signal / falsifier:** if, across realistic task classes, every encoder cheap
enough to be worth running leaks as much applied adversary-utility as sending the
raw input — i.e. the privacy-funnel curve is flat in the affordable region — then
the "task-orthogonal minimal leakage" framing buys nothing over plain trusted/
untrusted routing, and should be dropped.

## Prior art and where this sits

- **Information Bottleneck** — Tishby, Pereira, Bialek (1999). The object this is the
  dual of.
- **Privacy Funnel** — Makhdoumi, Calmon, Médard (2014). The direct formal home.
- **Adversarial / censoring representation learning, controllable invariance** — the
  gradient-based operationalizations.

The contribution claimed here is not the formal object (it exists) but the framing
that the *tractable* problem is the bounded-adversary middle, plus the per-task-class
orthogonality test as a sharper routing primitive than sensitive-vs-not. That
framing is the speculative part, and the open sub-questions above are how it gets
tested.
