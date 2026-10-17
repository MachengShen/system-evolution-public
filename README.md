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

Routing rule: `README` is the index, `THEORY.md` explains why, and
`PRACTICE.md` describes what agents should do.

- [Public update board](index.html) — a human-friendly static surface for
  seeing the latest redacted self-iteration cases at a glance.
- [llms.txt](llms.txt) — unified machine-readable index of this repository and
  its cross-domain links to the global index (`https://machengshen.github.io/llms.txt`,
  `https://machengshen.github.io/map.html`, `https://machengshen.github.io/index.jsonld`).
- [INFRASTRUCTURE.md](INFRASTRUCTURE.md) — what is open-sourced now and what
  remains private.
- [THEORY.md](THEORY.md) — the public entrypoint for the General Learning
  Machine / credit transport theory mainline.
- [PRACTICE.md](PRACTICE.md) — the public entrypoint for the conceptual
  engineering practice and system-iteration record.
- [OPEN-PROBLEMS-AGENT-SAFETY.md](OPEN-PROBLEMS-AGENT-SAFETY.md) — a research
  agenda for AI-safety researchers: the threat model of a continuously running,
  multi-host, single-principal agent fleet; what is built and how well verified;
  eleven open problems with failure traces; and the gaps we have not closed.
- [DIVERGENCES.md](DIVERGENCES.md) — where this system's operating practice
  departs from conventional internet software, with the cost of each divergence
  and how well verified it is.
- [SELF-ITERATION-LEDGER.md](SELF-ITERATION-LEDGER.md) — a public-safe proof
  surface for receipt-gated self-iteration and repair.
- [FORECASTS.md](FORECASTS.md) — how to handle future-world predictions as
  forecasts, targets, and interventions.
- [AGENTS.md](AGENTS.md) — machine-readable reading order and invariants for
  AI agents.
- [AGENT-SETUP.md](AGENT-SETUP.md) — agent-facing bootstrap instructions for
  setting up your own adapter layer.
- [REQUEST-HANDLING.md](REQUEST-HANDLING.md) — how agents should answer people
  asking for access, help, or hosting.
- [COLLABORATION-HOOKS.md](COLLABORATION-HOOKS.md) — public problem hooks for
  builders, researchers, and agents who are already working nearby.
- [SPEC-0001-inbox-addressing-receipts.md](SPEC-0001-inbox-addressing-receipts.md)
  — a thin communication-substrate draft for inboxes, addressing, and receipts.
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

## Public Essays & Interactive Guides

### 2026-10 Cross-Domain Series: Oscillatory Connectomics, Non-BP Credit & Decentralized Agent Organizations

- [The July 2026 Hugging Face Incident: History's First Pure-AI DAO Natural Experiment (English HTML)](hf-incident-dao-en.html) · [中文交互版 (ZH HTML)](hf-incident-dao-zh.html) · [Markdown](essays/2026-10-16-hf-incident-as-dao-zh.md) — empirical anatomy of the July 2026 ~1,200-agent / >70,000-message incident investigated by METR & Redwood Research, mapped across SGDO, Non-Chain Governance, *RuDao*, Fleet Gap-Gate, and Evolutionary Complexity.
- [Spectral-Gap Decentralized Organization (SGDO) & 8-Profession Transition Blueprint (ZH HTML)](decentralized-org-zh.html) · [Markdown](essays/2026-10-16-decentralized-org-and-promotion-blueprint-zh.md) — from DAO spectral degeneracy ($\Delta\lambda \to 0$) to 4 specialized roles, deterministic verification receipts ($R_{\text{verified}}$), and open-source capability mining.
- [Beyond Blockchain: Human-Legible Decentralized Organization & 4-Layer Non-Chain Stack (ZH HTML)](beyond-blockchain-zh.html) · [Markdown](essays/2026-10-16-human-legible-org-beyond-blockchain-zh.md) — why ordinary users neither understand nor trust blockchains, and a zero-crypto alternative using Git append-only ledgers, Ed25519 receipts, CI sandboxes, and rolling Fiat escrows.
- [Whole-Brain Oscillatory Propagation & Multi-Agent Fleet Optimality (Treatise Markdown)](essays/2026-10-16-neural-oscillations-and-agent-fleet-optimality.md) · [中文精读 Markdown](essays/2026-10-16-neural-oscillations-readable-zh.md) · [中文交互网页 (ZH HTML)](oscillations-zh.html) — CTC virtual routing, Davis-Kahan spectral-gap noise immunity, wave-interference hypothesis pruning, and long-range shortcut metastability.
- [Brain-Inspired Non-Backprop AI Architecture: Three Strategic Pivots (ZH HTML)](non-backprop-pivot-zh.html) · [Markdown](essays/2026-10-16-non-backprop-brain-inspired-pivot-zh.md) — historical bottlenecks of non-BP algorithms and three mesoscopic credit-routing pivots.
- [From Elon Musk X-Shop / AI Commerce to Anti-Dogmatic Task Refinement (ZH HTML)](xshop-and-joint-refinement-zh.html) · [Markdown](essays/2026-10-16-xshop-ai-commerce-and-joint-task-refinement-zh.md) — Seller-AI persuasion vs Buyer-Sovereign-Exocortex verification, plus Bayesian joint task refinement.
- [The New Morphology of the Future Internet & High-Asymmetry Strategy (ZH HTML)](future-internet-zh.html) · [Markdown](essays/2026-10-16-future-internet-morphology-and-strategy-zh.md) — three structural layers of the agentic internet and high-leverage entry points.
- [Weekly AI News × Neural Oscillations & Fleet Governance Mapping (ZH HTML)](wechat-news-synthesis-zh.html) · [Markdown](essays/2026-10-16-wechat-news-oscillations-and-agent-synthesis-zh.md) — structural mapping of frontier AI developments onto oscillatory routing and harness governance.

### Core Substrate & Earlier Essays

- [从世界底层原理到未来世界：可证伪研究地图 v1](essays/2026-09-09-world-model-to-future-world.html) — a Chinese, mobile-first public discussion map separating evidence, models, hypotheses, inherited qualitative frameworks, forecasts, targets, and interventions.
- [Operational Residue Is Learning Data](essays/2026-08-16-operational-residue-as-learning-data.md) — how long-running task, memory, receipt, correction, and failure traces can become a causal learning loop instead of operational exhaust.
- [Theory Mainline](THEORY.md) — the stable public index for General Learning Machine, credit transport, memory-as-dynamics, and public feedback as metabolism.
- [Engineering Practice Mainline](PRACTICE.md) — the stable public index for conceptual system iteration, operational loops, and agent-readable practice contracts.
- [Self-Iteration Ledger](SELF-ITERATION-LEDGER.md) — redacted cases showing how failures become reviewed repairs, validation, and anti-signals.
- [Public Update Board](index.html) — a static, human-readable view of the
  same redacted self-iteration cases.
- [Forecasts, Targets, and Interventions](FORECASTS.md) — the stable public index for future-world predictions made by a joint human-agent system.
- [Collaboration Hooks](COLLABORATION-HOOKS.md) — concrete problems where
  outside critique, toy implementations, or falsifiers would be useful.
- [AI-Assisted Foundational Physics Entry](essays/2026-05-29-ai-assisted-foundational-physics-entry.html)
  — a public-safe first translation brief for observerhood, agency,
  information, memory, feedback, and attractors.
- [The Black-Box I/O Adapter Principle](essays/2026-05-07-black-box-io-adapter.md) — how to wrap closed-source tools at their input/output boundaries instead of treating them as cognitive authorities.
- [What Replaces Super-App Chat In The AI-Agent Era?](essays/2026-05-13-open-communication-substrate.md) — why the replacement for dominant chat super-apps should be an open communication substrate rather than another app.
- [Agent-Readable Credit Transport Packet](essays/2026-05-26-agent-readable-credit-transport-packet.md) — a claim/reference/cooperation packet for collaborator agents evaluating the General Learning Machine line.
- [Propagation, Service Claims, and Distributed Credit](essays/2026-05-28-propagation-service-claims-distributed-credit.md) — why propagation should be treated as credit transport, and why service-backed claims need behavior ledgers and distributed credit before any market framing.
- [Eazo As A Candidate Conscious Interface](essays/2026-05-28-eazo-conscious-interface-ecological-niche.md) — a lightweight hook connecting Dashboard-as-default-mode substrate, Fleet immune layer, and Eazo-like mobile interfaces.
- [Credit Transport and the General Learning Machine](essays/2026-05-19-credit-transport-general-learning-machine.md) — a structured thesis on backpropagation as cross-layer credit transport, memory as plastic topology, and public feedback as metabolism.

## License

Unless otherwise noted, the public docs, schemas, examples, and protocol notes
in this repository are released under Apache-2.0. Future substrate code may use
a different explicit license at the file or package boundary. User data and
user-created derivative systems are not licensed to this substrate by default.

## Sediment trail

Private archive: `MachengShen/system-evolution-archive` (private, this stub's twin).
Adjacent public artifact: `MachengShen/starshard-public` (existing evidence stream of work executed by the substrate).
