# system-evolution-public

Public record and first open infrastructure boundary for the user-agency
substrate.

## What This Is

Self-hostable infrastructure for agent request intake, routing, BYOK model
execution, reply contracts, memory boundaries, and closed-loop receipts.

This repository is for builders and agents who want to set up their own
user-agency substrate using their own data, tools, and model-provider accounts.

## What This Is Not

- Not a hosted service.
- Not a shared endpoint for Macheng's private personal agent.
- Not backed by Macheng's API budget. BYOK means you pay your own model,
  cloud, and provider bills.
- Not under an SLA.
- Not a stable v1 API yet. Schemas may change before v1.
- Issues or emails asking maintainers to run requests on your behalf may be
  closed with a pointer to `AGENT-SETUP.md`.

This repo is the future home of the public-facing record of a user-agency substrate's evolution — the journey from "vanilla Claude Code in a terminal" to a multi-layer agent architecture, in roughly two months.

The unfiltered raw archive is private. Public files here are derived, redacted,
and written for reuse. The goal is not to publish Macheng's private system; it
is to publish the adapter layer and protocols that let other people build their
own systems on top of frontier models with their own accounts and API keys.

## Start Here

- [INFRASTRUCTURE.md](INFRASTRUCTURE.md) — what is open-sourced now and what
  remains private.
- [AGENTS.md](AGENTS.md) — machine-readable reading order and invariants for
  AI agents.
- [AGENT-SETUP.md](AGENT-SETUP.md) — agent-facing bootstrap instructions for
  setting up your own adapter layer.
- [REQUEST-HANDLING.md](REQUEST-HANDLING.md) — how agents should answer people
  asking for access, help, or hosting.
- [schemas/](schemas/) — public JSON contracts for request intake and agent
  replies.
- [essays/2026-05-07-black-box-io-adapter.md](essays/2026-05-07-black-box-io-adapter.md)
  — the black-box I/O adapter principle.

## Three-layer architecture (preview)

```
Layer 3 — Users own their derivative systems entirely.
Layer 2 — User-Agency Substrate (this stack). Nonprofit, open-source, provider-agnostic.
          Captures NO economic upside. Charges users only for direct operating costs.
Layer 1 — { Anthropic, OpenAI, Google, open-weights, ... } competitive frontier-model market.
```

Universalist commitment: "all humanity to be freed" explicitly includes Anthropic employees, the Anthropic CEO, and every other person working at Layer-1 providers. This is not adversarial framing. The substrate is a structural amplifier of the alignment-of-mission already shared with frontier-model providers, not a counter-faction.

## Status

- **Today**: first public infrastructure boundary is live. It contains the
  adapter-layer doctrine, bootstrap contract, request-handling policy, and
  schemas. It does not contain private transcripts, credentials, WeChat data,
  Memory Hub contents, or personal collaborator directories.
- **Next**: gradually lift reusable components into clean public packages after
  redaction, license, secret-scan, and reviewer checks.

## Public Essays

- [The Black-Box I/O Adapter Principle](essays/2026-05-07-black-box-io-adapter.md) — how to wrap closed-source tools at their input/output boundaries instead of treating them as cognitive authorities.

## License

Unless otherwise noted, the public docs, schemas, examples, and protocol notes
in this repository are released under Apache-2.0. Future substrate code may use
a different explicit license at the file or package boundary. User data and
user-created derivative systems are not licensed to this substrate by default.

## Sediment trail

Private archive: `MachengShen/system-evolution-archive` (private, this stub's twin).
Adjacent public artifact: `MachengShen/starshard-public` (existing evidence stream of work executed by the substrate).
