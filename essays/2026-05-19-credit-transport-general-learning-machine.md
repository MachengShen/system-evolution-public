# Credit Transport and the General Learning Machine

Date: 2026-05-19

Public index: [Theory Mainline](../THEORY.md)

> **Cognitive state:** 🟡 speculative · **Confidence:** 0.50 · provenance: reasoned reframing, presented as a research direction with no empirical test attached.
> Format: [Claim-Receipt](../CLAIM-RECEIPT.md) · Cognition Track node: [General Learning Machine as Dynamical System](https://github.com/MachengShen/cognition-track/blob/main/nodes/mem_ccacc817ccd8.md) `mem_ccacc817ccd8` (per-sub-claim breakdown there). A speculative tag means this is an idea, not an established result.

The next useful abstraction for personal AI systems is not "an agent with long
memory."

It is a general learning machine: a finite, situated system that continuously
changes its own information structure in order to preserve, recover, and extend
its reachable futures.

The claim is not that today's agent scaffolds already solve this. They do not.
The claim is that the right research object is larger than a model, a prompt, a
workflow, or a database.

## The Core Unit

A learning system should be described by its evolving state:

```text
S_t = {
  model policy,
  memory topology,
  credit ledger,
  tools and actuators,
  reviewer graph,
  rules / genes / immune constraints,
  experiments and artifacts,
  objective priors,
  substrate constraints
}
```

Learning is the transition from `S_t` to `S_t+1`.

The important question is not only whether the next answer is better. It is what
information exists after the interaction, where that information is stored, how
it flows, how it is trusted, and which future actions become reachable.

## Backpropagation as Credit Transport

Backpropagation should not be understood only as a neural-network training
algorithm.

It is the first widely successful engineered example of a deeper principle:
credit transport.

A system observes an outcome. Some structures inside the system helped produce
that outcome. Credit transport is the process by which error, surprise, value,
friction, or viability pressure moves backward through the structures that
caused the result and changes them.

In a neural network, this happens through differentiable layers and parameter
updates.

In an open-world agent system, the causal structures are broader:

- human signals and taste,
- agent policies,
- memory schemas,
- retrieval paths,
- tool choices,
- reviewer topology,
- rules and safety gates,
- experiments,
- model weights,
- organizational routines,
- hardware workload,
- and physical substrate constraints.

The research target is therefore not to discard backpropagation. It is to
generalize the credit-transport question beyond the narrow case where all
plasticity lives inside one differentiable model.

## Memory Is Not Storage

Long-term memory is often treated as a retrieval problem: store facts, search
facts, cite facts.

That is too weak.

Memory in a learning machine is a plastic topology. It carries:

- raw experience,
- compiled schemas,
- provenance,
- eligibility traces,
- trust and uncertainty,
- routing priors,
- recovery paths,
- and rollback state.

The failure mode is not only forgetting. A system can carry information and
still fail to locate it, route it, trust it, or apply it at the right moment.

Useful memory must therefore learn addresses, not just contents. It must learn
which substrate, path, person, artifact, or prior context is likely to contain
the needed structure.

## Sleep, Spiral, and Self-Shedding

A continual learning system cannot only accumulate.

If every interaction adds another memory, rule, module, exception, and routing
path, the system becomes sedimented drag. Growth without shedding is not
learning. It is sprawl.

A general learning machine needs phase separation:

- wake: couple to the world, act, ingest, route, and preserve uncertain traces;
- sleep: replay, compare, consolidate, downscale, hibernate, merge, prune, and
  repair;
- reawakening: return to the world with a changed reachable future.

This is why a spiral is a better image than a line. The system returns to old
anchors, but not from the same state. Revisit plus transformation is different
from repetition.

In operational terms, the system needs a mechanism like:

```text
detect stale self-part
  -> propose preserve / hibernate / merge / prune / quarantine / grow
  -> validate against identity, competence, safety, and rollback tests
  -> commit the change
  -> monitor for regression
```

## Information as Reachability Change

Information should not be reduced to message content.

A more useful operational definition is:

> Information is a perturbation of the transition structure of a system that
> changes its future reachability.

Memory, attention, trust, routing, semantics, and action are projections of
that deeper transition structure.

This framing makes familiar mathematical languages useful without turning them
into metaphysics:

- Euler-style dynamics give a grammar for growth / decay plus phase / return.
  A system can gain or lose usable structure while also moving through modes:
  wake, explore, act, contradiction, sleep, replay, consolidate, prune, and
  reawaken.
- Field-boundary dynamics give a grammar for source, propagation, coupling,
  boundary integrity, permeability, localization, and constraint.

These are engineering metaphors unless they produce measurements. The useful
test is whether they help us predict and change future reachability.

## Public Feedback as Metabolism

Public interaction is often treated as distribution: publish, get attention,
measure traffic.

For a learning machine, public feedback is a metabolic input.

External researchers, users, critics, collaborators, and edge cases are source
currents. They perturb the system. The system must then decide what to absorb,
what to reject, what to quarantine, what to route to experiments, and what to
turn into durable structure.

This requires an immune system. Without one, openness becomes drift. With too
rigid an immune system, openness becomes theater.

The closed loop is:

```text
world source
  -> intake
  -> receipt
  -> memory / experiment / reviewer routing
  -> credit assignment
  -> consolidation or rejection
  -> changed future action
  -> new world feedback
```

If a public channel does not close this loop, it is not yet part of the
learning machine. It is only an output surface.

## Hardware Implication

If learning is only dense inference, the hardware roadmap is mostly about
faster matrix multiplication, memory bandwidth, and deployment cost.

If learning becomes continuous information-structure evolution, the workload
changes.

The important traces include:

- memory locality,
- working-set drift,
- sparse activation,
- event-triggered updates,
- credit-path latency,
- provenance overhead,
- rollback cost,
- mutation validation cost,
- cross-node synchronization,
- and energy per useful state transition.

This points toward memory-centric, event-driven, online-learning,
near-memory, neuromorphic, analog, mixed-signal, and verification-heavy
architectures. Not as a slogan, but as a workload consequence.

The hardware question becomes:

> What substrate best supports delegated, persistent, auditable, physically
> situated adaptation?

## What Would Falsify This Direction?

This thesis should not be protected by impressive language.

Useful anti-signals include:

1. The system produces better summaries but does not reduce human babysitting.
2. Memory grows, but future retrieval and action do not improve.
3. Public feedback increases attention without improving experiments,
   routing, or judgment.
4. Self-modification creates drift, hidden fragility, or unreviewable behavior.
5. Sleep and consolidation sound elegant but fail to improve later performance.
6. Hardware traces do not differ meaningfully from ordinary inference serving.
7. The system cannot preserve trust, identity, and safety while adapting.

If these anti-signals persist, the framing is too broad or the architecture is
wrong.

## A Minimal Research Program

The next step is not to claim a final theory of intelligence.

The next step is to build small systems where credit transport is observable
across more than one layer.

Candidate experiments:

1. Compare scalar reward with structured credit ledgers in agent trajectories.
2. Test whether memory-topology updates reduce repeated failures and human
   burden.
3. Measure whether sleep / replay / consolidation changes future reachability,
   not only replay accuracy.
4. Add self-shedding: preserve, hibernate, merge, prune, quarantine, or grow
   system parts under rollback tests.
5. Track hardware-facing workload traces for continuous agent learning.
6. Treat public feedback as source current and test whether it becomes durable
   structure rather than traffic.

The practical criterion is simple:

> Does the system become more capable of doing the right thing later, with less
> human babysitting, while remaining inspectable and corrigible?

## One-Sentence Thesis

True learning is not a model updating parameters. It is a situated system
transporting future error and value signals backward into every structure that
helped cause them, then changing those structures without losing identity,
trust, or control.
