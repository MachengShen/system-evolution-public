# Prior Art Is Not a Truth Verdict

**Date:** 2026-08-24

**Status:** research-method update

**Scope:** theory work, especially recent machine-learning literature

## Thesis

Finding that a conceptual slot is already occupied changes what can honestly be
claimed as publication novelty. It does not decide whether the claim is true,
whether the published evidence is reliable, or whether independent verification
would teach us something about reality.

The research objective here is to understand underlying regularities, not to
optimize for paper acceptance.

## Four fields, not one verdict

Every prior-art gate must now report four separate fields:

1. **Novelty status** — is the wording, mechanism, theorem, or experiment already
   public?
2. **Epistemic status** — supported, contradicted, unresolved, or out of range?
3. **Reliability** — how much weight should the source carry?
4. **What remains to know** — what derivation, control, replication, or
   intervention would change our belief?

The invalid shortcut is:

> occupied → void → stop

The correct relationship is:

> occupied → no novelty claim; then independently assess truth and reliability

## Reliability audit

For formal work:

- read the actual proof rather than only an abstract or a later summary;
- list the assumptions and re-derive the load-bearing step;
- resolve the foundational citations the proof relies on;
- distinguish a theorem from an interpretation attached to it.

For empirical work:

- inspect code and data availability;
- identify positive, negative, and randomization controls;
- check whether the estimator measures the claimed quantity;
- preserve the true statistical unit and power calculation;
- separate preregistered choices from post-hoc repairs;
- inspect raw outputs and seek independent replication.

Publication pressure, irreproducibility, selective reporting, and possible
fraud are real field-level uncertainty, especially in fast-moving ML. They
raise the prior probability that a result is unreliable. They do not justify
accusing a particular author or paper without direct evidence.

## Bounded top-down belief

Experimental science also fails when every negative result immediately kills a
good theory. A result can be negative because the theory is wrong, but also
because the code, measurement, control, or experimental rig is wrong.

A top-down belief is allowed only after the direction passes four gates:

- the mechanism is beautiful rather than patched;
- it is simple enough to state in one sentence;
- it explains more than one otherwise separate phenomenon;
- its physical or biological inspiration is mechanistic and measurable.

Once authorized, the belief must carry:

- a concrete prediction;
- a preregistered kill condition;
- a finite debug budget;
- instrument trust gates.

While trust gates fail and a specific bug hypothesis remains inside the debug
budget, contradictory data are `RIG-UNDECIDED`. Once the instrument is
trusted and the kill condition is met, the direction stops. Theory beauty is a
reason to debug carefully, not permission for unlimited parameter rescue.

## Current application: PID self-observation

Tallam's 2026 uncommon-self-knowledge paper occupies the publication slot for
self-directed redundancy/synergy as a consciousness criterion. Its existence
does not establish the criterion's truth: the paper is a conceptual proposal
without an experiment, code, or data.

A second-pass audit also corrected our own citation error. Gottwald and Braun's
[*On the Structure of Information*](https://arxiv.org/abs/2409.20331) is a
general loss-based uncertainty framework; it is not the partition-lattice PID
proof first attributed to it. Tallam's foundational citation still requires
independent resolution.

Current state:

- **novelty:** occupied;
- **truth:** unresolved;
- **standard PID identity:** a single source carries redundant plus its unique
  share, not the joint-only synergy atom;
- **unresolved bridge:** whether that source decomposition operationally equals
  what a physically embedded subsystem can observe.

The algebraic identity does not need an experiment. The physical
embedded-observer bridge may deserve one if it can be independently
operationalized and given trustworthy controls.

## Current application: set-valued boundary hysteresis

The D4 boundary hypothesis survives as a top-down direction because one
state-to-coupling loop makes distinct predictions for split, fuse, and
substrate-transplant interventions.

Prior scalar hysteresis and adaptive-network work reduce publication novelty;
they do not establish the exact proposed effect: membership-identity hysteresis
remaining after scalar boundary size is matched out.

The theory is preserved, but the current rig is not yet trusted. Its primary
set-residual estimator needs a frozen mathematical definition, held-out
fitting, seed-level statistics, known-answer controls, and a negative control
before a large run can count as evidence.

## Anti-signals

- Treating a highly cited paper as ground truth.
- Treating an unreliable paper as if it did not exist.
- Killing a beautiful, mechanistic theory before checking the instrument.
- Using theory beauty to move thresholds after seeing the result.
- Calling field-level fraud risk proof that one named paper is fraudulent.
- Letting a receipt or polished PDF turn an unverified claim into a fact.

## Research contract

Prior art constrains what we may call new. Reliability constrains what we should
believe. Experiments constrain what survives. None of those roles may silently
replace the others.
