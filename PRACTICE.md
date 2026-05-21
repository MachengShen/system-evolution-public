# Engineering Practice Mainline

This is the public entrypoint for the engineering practice behind the
user-agency substrate.

The theory line asks what a General Learning Machine is. The practice line asks
how to build a useful, inspectable, user-owned approximation of one with today's
frontier models, local machines, cloud workers, memory systems, and public
interfaces.

Theory companion: [Theory Mainline](THEORY.md)

This file is intentionally conceptual and agent-readable. It does not publish
private transcripts, credentials, personal contact data, raw Memory Hub contents,
or every low-level implementation detail.

## One-Sentence Practice Thesis

A personal AI system becomes more than chat when every channel, memory, task,
review, publication, and repair path is part of a closed loop with receipts,
durable state, escalation, and consolidation.

## When To Use This

Use this document when designing, reviewing, or publishing the practice layer of
a user-agency substrate: agent orchestration, memory contracts, channel loops,
adapter boundaries, reviewer workflows, and public iteration receipts.

Do not use it as evidence that any private implementation is open, hosted,
available, or safe for third-party data. Public practice notes are derived,
redacted artifacts.

## What Is Public

The public practice record should expose reusable patterns:

- architectural concepts,
- protocol surfaces,
- agent-readable contracts,
- redacted iteration receipts,
- falsifiable anti-signals,
- and small implementation boundaries that others can reproduce with their own
  data, accounts, and models.

The public record should not expose:

- private raw conversations,
- personal contacts,
- private collaborator context,
- credentials or provider keys,
- private memory databases,
- private device state,
- or hidden operational controls.

## Current Practice Organs

These are the conceptual organs being iterated.

### P-00: Self-Iteration Ledger

The system should keep a durable record of its own repair metabolism.

The public-safe entrypoint is
[Self-Iteration Ledger](SELF-ITERATION-LEDGER.md). It presents redacted cases
where a failure became a reviewed repair, validation result, and anti-signal.

Public practice implication:

- publish the shape of self-iteration, not the private substrate;
- require every claim to have a receipt, validation, and falsifiable
  anti-signal;
- keep internal and public ledgers structurally aligned so public pressure
  improves the private control loop.

Trigger: a system repair demonstrates a reusable failure pattern or a real
improvement in future reliability.

Action: write a private receipt first, then derive a redacted public case if it
does not expose private data or overclaim autonomy.

Anti-pattern: marketing self-improvement without a receipt-backed repair.

### P-01: Single Visible Agent

The user should experience one coherent front-stage agent, not a provider graph.

Internally, that agent may delegate to model backends, local workers, cloud
workers, reviewers, and scripts. Externally, it should preserve a stable
interface: current conclusion, decision gates, material disagreement, receipts,
and anti-signals.

Public practice implication:

- publish the orchestration contract, not the private worker chatter;
- keep backend choice replaceable;
- make receipts durable enough that another agent can resume.

Trigger: a user-facing workflow would otherwise expose multiple backend agents,
providers, or worker queues.

Action: collapse the graph into one front-stage report with receipts and
decision gates.

Anti-pattern: making the user manage the backend graph.

### P-02: Memory as Durable Substrate

Memory is not a chat history dump. It is the system's evolving substrate.

Useful public patterns include:

- raw private trace stays private;
- public artifacts are derived and redacted;
- durable memories preserve decisions, rejected alternatives, receipts, and
  provenance;
- agent-readable summaries point back to public artifacts when safe;
- high-stakes facts use ledgers rather than casual recall.

Public practice implication:

- publish memory contracts and redaction rules;
- do not publish the private memory corpus;
- make public artifacts reconstructible from safe receipts.

Trigger: a fact, preference, task, or publication decision must survive the
current session.

Action: write a durable receipt with provenance and rejected alternatives when
relevant.

Anti-pattern: relying on raw chat recall for high-stakes future action.

### P-03: Closed-Loop Channels

Every channel should answer: what closes the loop?

A useful channel declares:

```text
input
  -> receipt
  -> classification / routing
  -> durable state update
  -> timeout or error detection
  -> repair / escalation
  -> consolidation
```

This applies to email, chat bridges, dashboards, public forms, reviewer calls,
agent tasks, publication flows, and future devices.

Public practice implication:

- publish protocol surfaces and state machines;
- treat fire-and-forget integrations as incomplete;
- expose enough receipt structure for other agents to audit behavior.

Trigger: a message, task, publication, reviewer call, or external input can
enter the system without a visible completion state.

Action: define receipt, routing, durable state update, timeout detection,
repair path, and consolidation before treating the channel as complete.

Anti-pattern: fire-and-forget intake with no auditable end state.

### P-04: Adapter Layer Over Black Boxes

Closed tools can still be useful if their boundaries are controlled.

The system wraps tools at the input/output boundary:

```text
human intent + context
  -> input adapter
  -> black-box tool
  -> output adapter
  -> memory / action / user interface
```

Public practice implication:

- publish adapter principles;
- preserve provenance and uncertainty;
- separate vendor output, normalized output, inferred intent, proposed action,
  and executed action.

Trigger: a black-box tool sits between user intent and memory, action, or
public output.

Action: separate raw input, vendor output, normalized output, inferred intent,
proposed action, and executed action.

Anti-pattern: collapsing all layers into one clean text blob.

### P-05: Reviewer Metabolism

Reviewers are not ceremonial. They are metabolism for high-salience changes.

Useful reviewer practice:

- create compact packets;
- ask for concrete risks and implementable deltas;
- continue reversible work while reviewers run;
- block only on high-risk or irreversible actions;
- record reviewer artifacts and anti-signals.

Public practice implication:

- publish review packet templates and integrated conclusions;
- do not publish private raw transcripts by default;
- make reviewer failure modes visible enough to improve the process.

Trigger: a decision affects public positioning, real users, privacy boundaries,
or persistent architecture.

Action: create a compact reviewer packet, continue reversible work, and record
the integrated result.

Anti-pattern: waiting for review before doing safe reversible work, or ignoring
reviewer anti-signals after publication.

### P-06: Public Theory and Practice Runway

The theory and practice lines should now publish together.

The desired loop is:

```text
private system iteration
  -> redaction and abstraction
  -> public theory or practice artifact
  -> public feedback / reviewer pressure
  -> memory and architecture update
  -> next system iteration
```

Public practice implication:

- each substantial theory update should ask what practice artifact corresponds
  to it;
- each substantial engineering update should ask what theory claim it tests;
- publication is not distribution only; it is part of the learning loop.

Trigger: a theory insight changes system behavior, or an engineering iteration
tests a theory claim.

Action: publish a redacted theory or practice artifact, link it from the stable
index, and write a receipt.

Anti-pattern: leaving reusable system knowledge only in private chat.

## Agent-Readable Publication Contract

When an agent handles a new practice update, it should produce a public artifact
with this shape:

```text
title:
date:
public_surface:
private_boundary:
problem:
conceptual_pattern:
operational_loop:
agent_contract:
receipt_shape:
anti_signals:
next_iteration:
```

Before publishing, the agent should check:

- no secrets or credentials;
- no private third-party details;
- no raw private transcript;
- no unapproved local paths or internal service endpoints;
- no claim that depends on hidden evidence without marking it as a working
  hypothesis;
- links from README or an index if discoverability matters.

After publishing, the agent should write a durable receipt containing:

- public URL,
- commit hash,
- local artifact path,
- validation performed,
- reviewer status if applicable,
- and remaining anti-signals.

## Current Public Practice Map

- [The Black-Box I/O Adapter Principle](essays/2026-05-07-black-box-io-adapter.md)
- [Forecasts, Targets, and Interventions](FORECASTS.md)
- [What Replaces Super-App Chat In The AI-Agent Era?](essays/2026-05-13-open-communication-substrate.md)
- [SPEC-0001: Inbox, Addressing, And Receipts](SPEC-0001-inbox-addressing-receipts.md)
- [Agent Setup](AGENT-SETUP.md)
- [Request Handling](REQUEST-HANDLING.md)

## Provenance

This public practice line is derived from personal system iteration and then
redacted into reusable patterns. It is not an employer work product, not a
hosted service description, and not a promise that private components are
available to third parties.

## Changelog

- 2026-05-19: created the public practice entrypoint and linked it from
  `README.md` and `THEORY.md`.

## Anti-Signals

The practice line is failing if:

1. engineering changes remain private and unabstracted;
2. public artifacts are too vague for another agent to implement from;
3. public artifacts leak private operational detail;
4. theory claims are not tied to practice tests;
5. practice updates do not leave receipts;
6. feedback is collected but not routed into memory, experiments, or design.

## Next Iteration

The next useful public practice artifact should be a dated, concrete iteration
note using the contract above. Good candidates:

- closed-loop publication flow;
- reviewer packet and receipt pattern;
- memory redaction and public artifact derivation;
- inbound channel anti-stranding;
- theory-to-practice update coupling.
