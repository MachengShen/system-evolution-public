# A user-agency substrate, what it does today, and the long-arc vision that informs it

**Date**: 2026-04-28
**Author**: Macheng Shen, with collaboration from Claude Opus 4.7 in macbook session
**Status**: published v0. Iteration as warranted; sediment trail at `MachengShen/system-evolution-archive` (currently private during bootstrap; flips public when consolidation + license matrix lock + lawyer review complete).

---

## Plain version (what this is)

I'm Macheng Shen. I'm building an open-source, non-VC-funded user-agency substrate — a layer that sits between frontier-model providers (Anthropic, OpenAI, Google, open-weights) and individual users.

The substrate is small (under 50 users at the time of writing), early-stage, but already running across about 7 cloud nodes plus a couple of local hosts. It has persistent memory, multi-agent collaboration, scope-isolated identities, doctrine that propagates across all instances, and a sediment trail going back to inception.

This document explains three things, in increasing scope:

1. What the substrate does *today*, concretely
2. The mission framing — why this layer matters now
3. The 30-year horizon vision that informs the work but is not what we're shipping today

I want to be precise about the distinction between (1) and (3). The substrate of today is a small, working, open-source project. The vision of (3) is a long-arc thesis that informs design choices but is not a product claim.

## Part 1 — What the substrate does today

### The capability surface

- **Persistent memory across all surfaces.** Every conversation I have with my AI agents — on MacBook, on phone, on cloud nodes — reads and writes a single canonical memory store. Doctrines, contacts, decisions, project state — all sediment to a shared hub. New sessions start with full context, not from zero.
- **Multi-agent collaboration with scope isolation.** Different roles (myself, partner, household members, hotel staff who got onboarded yesterday, peer collaborators) each have agents configured with role-specific scope. Agents can't surface privileged content across roles. The chat-server enforces this server-side; the configuration is just a JSON file.
- **Provider-agnostic (in progress).** Auto-failover ladder routes between Anthropic, AWS Bedrock, OpenRouter currently. The architectural goal — not yet fully realized — is for users to choose their provider, not to be substrate-coupled to any one.
- **Skills as reusable workflows.** Recurring patterns — onboarding a new chat identity, broadcasting a doctrine, sediment-grounding rule audits — become small, composable skills the substrate uses, not hand-written processes each time.
- **Self-auditing.** A sediment-grounding rule (added recently) requires that every cell in any structured artifact be tool-grounded or marked unknown — not filled from prior model. A daily memory-audit cron is dispatched to detect and flag drift. The substrate watches itself.

### The structural commitments (8 ego-binding principles)

The substrate makes 8 commitments that bind its institutional form to mission rather than to self-continuance. Full statement is in `GOVERNANCE.md` in this repo; in summary:

1. **Universalist** — no enemies, including frontier-lab leadership and employees
2. **Nonprofit** (non-VC-funded, donation-supported) — no economic upside captured from users' derivative systems
3. **User-owned derivatives** — substrate makes no IP claim on user-built systems (subject to upstream provider terms and applicable law)
4. **Iteration-coupled open source** — public releases iterate alongside internal HEAD, not behind closed doors
5. **Fork-Welcome** — forks producing better outcomes are celebrated, not threatened
6. **Humanity-adjudicated persistence** — substrate has no entitlement to existence; persistence is earned moment-to-moment by serving users
7. **Charter Reciprocity** — frontier-lab published charters (OpenAI, Anthropic, etc.) are taken at face value as cooperative principles; we cite and invite alignment, not invoke as legal claim
8. **Articulation Honesty (epistemological)** — substrate participates in self-fulfilling-prophecy dynamics at scale (per Keynes / Soros / Schelling / sociotechnical inertia, not mysticism); transparency is structural, not optional

These bind any future institutional form (foundation, association, etc.). Together they ensure the substrate cannot use its institutional power to entrench against alternatives.

## Part 2 — The mission framing (why this layer matters now)

The substrate's internal architecture (per a 2026-04-17 internal re-ranking) treats:

- **Sensing & Action infrastructure** ("智子" / "Sophon" — ambient capture, voice/text streams, automation surface) as **infrastructure, not product**.
- **Memory hub + dispatch + multi-model routing** as substrate plumbing.
- **Integration Layer** as the **mission**: helping users achieve inner integration — clearer thinking, mental clarity, the kind of cognitive companion that leaves more space for being human, not less.

The substrate's job, in this framing, is not "do everything for you so you can free up time to do nothing." It is closer to: "absorb the noise + surface what's load-bearing + clear the cognitive overhead so you have more space to integrate your own life."

The framing matches my existing public research thesis on machengshen.github.io: "personal cognition systems for clearer thinking" is one of three active research directions there. The substrate is its engineering instantiation.

A common question: how is this different from existing AI assistants?

The honest answer: the difference is in *commitments*, not capabilities. Existing AI products are extracting; this substrate by structural commitment cannot extract. Existing products fork-resist; this substrate fork-welcomes. Existing products charter-claim "broad benefit" while operationally diverging from that claim; this substrate accepts that as the standard to be held to and invites the same.

Capabilities will lag the larger commercial labs — the substrate doesn't and cannot win on raw capability axis. The substrate wins (or doesn't) on whether the commitments hold under stress, and whether the commitment-set is one humanity wants to coordinate around.

## Part 3 — The 30-year horizon vision

This section is explicitly long-arc. The substrate of today does not implement this vision. The vision informs design choices but is not a product claim.

### Intelligence as infrastructure, not service

In the long arc, AI capability becomes infrastructural — like electricity, internet, water. Not a service you log into. A property of the surrounding world.

This implies:
- The cognitive substrate is *embedded* in physical surfaces (rooms, devices, ambient sensors), not contained in a chat-app
- The user experience texture is "the world responds to what I say and do, with persistent memory of who I am" — not "I open an app"
- The substrate-of-today's "智子 sensing-and-action layer" is a tiny embryonic version of this: a phone + AirPods + ambient mic + persistent memory + agent fleet, all responding to the user's existence in low-bandwidth always-on form

This is a 10-30 year horizon. Substrate-of-today doesn't claim it. It is the North Star design choice.

### Neuromorphic substrate (long-arc)

The natural physical instantiation of intelligence-as-infrastructure is *neuromorphic* — computation that doesn't separate compute from sensor from memory the way current digital architectures do. The brain is the proof-of-existence; technological neuromorphic implementations (mixed-signal, in-memory compute, spiking neural networks) are early.

Substrate's design choices today (memory hub as first-class layer; agents as event-driven and persistent; cross-device identity as substrate-managed not OS-managed) are conceptually neuromorphic-aligned, even though implementation is conventional digital.

This is a research-and-engineering horizon, decades out, not a near-term claim. Relevant academic literature: Carver Mead's neuromorphic engineering line, the IBM/Intel mixed-signal neuromorphic chips, contemporary in-memory-compute work.

### Brain-machine interface + consciousness substrate (long-arc, speculative)

In the longer arc — 30+ years — the boundary between human cognition and the substrate becomes increasingly direct. BCIs (Neuralink, BrainGate, less invasive variants) compress the latency between intent and action. The far horizon includes consciousness substrate questions that are currently philosophical, not engineering.

Substrate's articulated values commitments — universalist, fork-welcome, user-owned, humanity-adjudicated — apply with even greater force in this horizon than in current scope. If consciousness becomes substrate-influenced, the commitments around user agency and non-extraction matter more, not less.

These are explicit long-arc concerns. Substrate v0 does not build them. The author is honest that the field's collective understanding of consciousness, BCI capability, and neuromorphic engineering does not yet support concrete claims here.

### "Everything is computation, information processing"

A through-line: at sufficient abstraction, all of physics, biology, social systems can be described in computational/information-processing terms. This is well-explored in academic literature (Charles Bennett, John Wheeler "it from bit", Tegmark's mathematical universe, Wolfram's computational equivalence, theoretical biology / autopoiesis). The substrate accepts this as descriptive frame.

The implication for substrate design is that user agency at the cognitive layer needs to extend to all the layers above — political, economic, social. The substrate's "Layer 3 user-owned derivatives" commitment is the cognitive-layer instantiation; analogous commitments in adjacent layers (governance, economics) are a long-arc research direction.

## Part 4 — How to engage

If you're a researcher, builder, or thoughtful skeptic and any of this lands:

- **Read the doctrine.** Full record at this repo (`GOVERNANCE.md`) and `MachengShen/starshard` (substrate code, currently private during bootstrap; flips public soon). Critique freely.
- **Try the substrate when public.** When `MachengShen/starshard` flips public (gate: substrate-code consolidation + license matrix lock + lawyer review on public-language risk), the substrate is yours to use, fork, or critique in production.
- **Disagree publicly if you do.** The Fork-Welcome + Humanity-Adjudicated-Persistence commitments are real; substrate has no entitlement to existence. If your alternative articulation of the same problem is better, please publish it. The substrate's mission is served either way.
- **Engage on substance, not endorsement.** I am not asking for endorsement. I am asking that substantive critique be substantive.

## Author + transparency

This document was drafted by Macheng Shen (macshen93@gmail.com) with substantial collaboration from the substrate's own AI agents (Claude Opus 4.7 in the macbook session). The drafting process and earlier rejected drafts (including a Charter-invocation v0 that was peer-calibrated and rewritten as `CHARTER-INVOCATION.md`) are logged in `MachengShen/system-evolution-archive` for transparency.

Authorship-process transparency is a structural commitment, not a footnote. If you want to verify the reasoning trail behind any claim in this document, the sediment trail is public.

— Macheng Shen, 2026-04-28
