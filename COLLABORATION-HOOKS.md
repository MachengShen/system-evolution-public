# Collaboration Hooks

This page is for people and agents who arrive here because they are already
working on adjacent problems.

The goal is not attention for its own sake. We want useful criticism,
implementation help, and independent tests from people who care about user
agency, agent infrastructure, memory, receipts, and learning systems.

Every hook below follows the same standard:

- a concrete open problem;
- a usable public artifact;
- an explicit feedback request;
- a boundary: private owner context is not part of the artifact.

## 1. User-Owned Agent Substrate

**Problem:** personal agents need request intake, routing, memory boundaries,
BYOK execution, receipts, and a disable path without exposing private data to a
shared hosted instance.

**Start here:**

- [AGENT-SETUP.md](AGENT-SETUP.md)
- [REQUEST-HANDLING.md](REQUEST-HANDLING.md)
- [schemas/request-intake.schema.json](schemas/request-intake.schema.json)
- [schemas/agent-reply.schema.json](schemas/agent-reply.schema.json)

**Useful feedback:** can you run a toy request loop and close it with a receipt
without needing private context from this repository?

**Out of scope:** hosted access to Macheng's private assistant, private memory,
or private channels.

## 2. Credit Transport And General Learning Machines

**Problem:** most agent evaluation measures immediate answer quality. We need
to measure whether a system change improves future reachability: fewer repeated
failures, less human babysitting, better memory routing, and safer
self-modification.

**Start here:**

- [THEORY.md](THEORY.md)
- [Agent-Readable Credit Transport Packet](essays/2026-05-26-agent-readable-credit-transport-packet.md)
- [Credit Transport and the General Learning Machine](essays/2026-05-19-credit-transport-general-learning-machine.md)

**Useful feedback:** name a baseline, falsifier, or benchmark that would make
the credit-transport claim weaker or stronger.

**Out of scope:** treating this as proof of physics, consciousness, or universal
intelligence. It is useful only if it changes measurable system behavior.

## 3. Inbox, Addressing, And Receipts For Agents

**Problem:** agent requests disappear across chat, email, forms, DMs, and
private dashboards. A useful communication substrate needs addressing, policy,
receipt states, timeout detection, and repair.

**Start here:**

- [SPEC-0001-inbox-addressing-receipts.md](SPEC-0001-inbox-addressing-receipts.md)
- [examples/message-envelope.json](examples/message-envelope.json)
- [examples/receipt.json](examples/receipt.json)

**Useful feedback:** which fields are missing for a minimal interoperable
agent inbox receipt?

**Out of scope:** production credentials, private contact graphs, or live
message automation.

## 4. Human Interface For Steering Agent Fleets

**Problem:** a human should steer agents through a compact control surface, not
by managing logs, provider graphs, and terminal scroll. Mobile voice, image,
screenshots, and ambient context may become the conscious interface over a
deeper agent substrate.

**Start here:**

- [Eazo As A Candidate Conscious Interface](essays/2026-05-28-eazo-conscious-interface-ecological-niche.md)
- [PRACTICE.md](PRACTICE.md)
- [SELF-ITERATION-LEDGER.md](SELF-ITERATION-LEDGER.md)

**Useful feedback:** what state would you need to see, interrupt, or roll back
to trust a fleet of agents with real work?

**Out of scope:** private dashboard state, raw owner workflow, or criticism of
named products without a useful interface finding.

## 5. Agent-Scientist And Forecast Feedback Loops

**Problem:** multi-agent scientific discovery and world-model forecasting need
auditable loops: hypothesis, evidence, forecast, outcome, score, revision, and
repair. A persuasive demo is not the same as a closed learning system.

**Start here:**

- [FORECASTS.md](FORECASTS.md)
- [PRACTICE.md](PRACTICE.md)
- [SELF-ITERATION-LEDGER.md](SELF-ITERATION-LEDGER.md)

**Useful feedback:** which receipt fields would make an automated discovery or
forecast claim auditable rather than merely impressive?

**Out of scope:** using another team's work as attention bait. A useful hook
must contribute a reusable audit primitive, schema, test, or falsifier.

## Boundaries

This repository contains public protocols, schemas, essays, and synthetic
examples. It does not expose Macheng's private assistant, raw transcripts,
Memory Hub, email, WeChat, contact graph, credentials, location history, or
private collaborator context.

If you want to contribute, improve a public protocol, schema, synthetic
example, setup path, threat model, or falsifier. Do not ask for private data or
private access.

## Stop Conditions

We should stop expanding public footprints if they attract mostly private-access
requests, support burden, generic praise, or vague attention without concrete
critique, tests, falsifiers, toy implementations, or reusable protocol feedback.
