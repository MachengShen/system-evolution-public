# A user-agency substrate, what it does today, what it doesn't

**Date**: 2026-04-28 (v1, calibrated against external review)

I'm Macheng Shen. I'm building an early-stage user-agency substrate — a layer that sits between frontier-model providers (Anthropic, OpenAI, Google, open-weights) and individual users.

The substrate is small (under 50 users at the time of writing), early-stage, and not yet open-source: the substrate-code repo (`MachengShen/starshard`) is currently private during bootstrap; it flips public when consolidation, license matrix, gitleaks pass, and lawyer review on public-language risk are complete. The governance documents (this repo) are public now.

This document is intentionally brief. Three parts:

1. What the substrate does today, mechanisms not adjectives
2. The threat model (what could go wrong, what we do about it, what we don't yet)
3. The mission framing — the design goal that informs everything else

A separate, clearly-labeled future essay covers long-arc speculation about ambient AI, neuromorphic substrates, and computational-substrate framings. That speculation is not a product claim and is intentionally kept out of this launch document.

## Part 1 — What the substrate does today (mechanisms)

- **Cross-device persistent memory.** A canonical memory store (Cloudflare-fronted MCP server) is read and written by AI agents on multiple devices. Doctrines, contacts, decisions, project state sediment to this store. Retrieval is keyword + tag based, not unbounded "full context."
- **Per-role identity isolation.** Different users (substrate operator, partner, household, peer collaborators, third-party guests) each have agents configured with role-specific scope rules — block tags, hub_disabled flags, system prompt boundaries. Enforcement is server-side at the chat-server layer; the configuration is a JSON file inspectable in the substrate-code repo when public.
- **Auto-failover across model providers.** Routing layer attempts Anthropic primary, AWS Bedrock as second, OpenRouter as third. Architecturally this is reliability-first today; the design goal — not yet realized — is user-side provider choice (BYOK).
- **Skills as reusable workflows.** Recurring patterns become small composable skills. Examples: provisioning a new chat identity, sediment-grounding rule audits, doctrine broadcast.
- **Self-auditing.** A sediment-grounding rule requires every cell in any structured artifact to be tool-grounded or marked unknown — not filled from prior model. A daily memory-audit cron is dispatched to detect and flag drift.

What we don't do:
- We don't run frontier-model R&D. The substrate is layer-2 on top of provider APIs.
- We don't yet enforce user-side provider choice end-to-end. That's a design goal, not current state.
- We don't yet have an external security audit. Pre-public requirement.

## Part 2 — Threat model (what could go wrong)

This is the critical section. Substrate handles intimate cognitive data; "values commitments" alone are not enforcement.

### Risks the substrate must address before public-release of code:

- **Storage**: where does memory live? (Currently: Cloudflare Worker fronting a self-hosted DB; encryption at rest TBD as part of public-release prep.)
- **Access control**: how is per-role isolation enforced and tested? (Server-side scope rules + smoke tests; needs adversarial red-team before public.)
- **Retention / deletion**: how is data deleted on user request? (Mechanism design pending; soft-delete via lifecycle_state exists, structural deletion is gap.)
- **Consent for ambient capture**: any ambient-mic / always-on input pathways must have explicit per-recipient consent. Currently the only ambient-capture is the substrate operator's own (OMI), no third-party. This expands carefully or not at all.
- **Provider leakage**: when Anthropic / Bedrock / OpenRouter receives queries, what data leaks? (Same as any API user; substrate adds no extra leak surface but doesn't reduce it either.)
- **Role-isolation failure**: an agent surfacing privileged content across roles is a P0 incident. Smoke tests exist; coverage is incomplete.
- **Founder bus factor / misconduct**: what happens if substrate operator goes silent or acts in bad faith? (Mitigation: open-source code + sediment trail public + Fork-Welcome commitment + no proprietary lock-in. Imperfect; one-founder projects always have this risk.)
- **Governance capture**: even with no economic upside, donors / large users / cloud vendors can capture roadmap. (Mitigation: anti-capture commitments in `GOVERNANCE.md` items 1-11. Imperfect; institutional governance is the long-arc work.)
- **Dependency on memory hub**: if memory hub goes down, substrate degrades. (Mitigation: open-source the memory hub spec; users can self-host.)

### What we don't yet have:

- Formal threat model document with adversary profiles, attack trees, mitigations
- External security audit
- Vulnerability disclosure policy beyond email-based reporting
- Insurance
- Signed releases
- Reproducible builds

These are pre-public-release requirements for the substrate-code repo. Until then, treat the substrate as research-grade, not production-grade.

## Part 3 — Mission framing (one paragraph)

The design goal is "personal cognition systems for clearer thinking" (which matches the home-page research direction at machengshen.github.io). The substrate's job is not to do everything for the user; it is to absorb the noise and surface what's load-bearing, leaving more cognitive space for human integration. Capabilities will lag the larger commercial labs. The substrate's bet is on whether user-controlled memory, routing, and identity can be made more auditable, forkable, and less lock-in-prone — these are design goals, not guarantees.

## Eleven structural governance commitments

Full list at `GOVERNANCE.md` in this repo. Together they bind any future institutional form (foundation, association, etc.) to mission rather than to self-continuance:

1. No enemies, including frontier-lab leadership and employees
2. Non-VC-funded, donation-supported (not yet legally incorporated as nonprofit)
3. User-owned derivatives, subject to upstream provider terms and applicable law
4. Public open-source releases iterate alongside internal HEAD, not behind closed doors
5. Forks producing better outcomes are celebrated, not threatened
6. Substrate has no entitlement to existence; persistence is earned moment-to-moment
7. Frontier-lab charters cited as cooperative principles, not invoked as legal claim
8. Articulation honesty: transparency is structural, not optional

Items 9-11 cover anti-capture, donor caps, articulation honesty under self-fulfilling-prophecy frame; full text in `GOVERNANCE.md`.

## How to engage

- **Read `GOVERNANCE.md` and `CHARTER-INVOCATION.md` in this repo.**
- **Critique freely.** The Fork-Welcome commitment is not rhetorical; if your alternative articulation is better, please publish it.
- **Wait for `MachengShen/starshard` to flip public** before evaluating substrate code. Until then, governance commitments are publishable; substrate code isn't.
- **Engage on substance, not endorsement.**

## Long-arc speculation (separate)

A future essay covers long-arc speculation about ambient AI as infrastructure, neuromorphic computation, brain-machine interfaces, and computational frames for physics / biology / social systems. That essay is intentionally kept out of this launch document because it is speculation, not product claim, and conflating the two undermines both. Link added when published.

## See also

**[LOCALITY-AS-PROTOCOL.md](LOCALITY-AS-PROTOCOL.md)** — The broader governance-theory framing that the substrate's user-agency commitments are reaching toward. The substrate is one software-layer instance of the locality-as-protocol logic: a rule-system that individuals opt into, governed by explicit commitments, competing with alternatives on quality rather than lock-in. Published 2026-04-29, v0, pre-calibration.

## Author + transparency

This document was drafted by me with substantial collaboration from AI agents in the substrate, calibrated by external cross-model review, and rewritten after the first draft did not survive that review. The drafting and review process is logged in `MachengShen/system-evolution-archive` (currently private during bootstrap; flips public on the same gate as the substrate-code repo). Authorship-process transparency is a structural commitment.

— Macheng Shen, 2026-04-28
[Contact: macshen93@gmail.com]
