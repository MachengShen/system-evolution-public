# Governance

## Status

The user-agency substrate is currently in **pre-institution** state: one founder (Macheng Shen) + a small circle of ambassador-friends + an agent stack he runs. There is no formal board, foundation, or governance body yet. This file is a placeholder per day-1 hygiene best practices.

When the substrate matures and adoption warrants institutional structure, this file will be updated with full governance details.

## Current effective governance

- **Founder / steward**: Macheng Shen (macshen93@gmail.com)
- **Decision-making**: Macheng + agent stack, with peer consultation from ambassador-friends circle on technical architecture
- **Funding**: Macheng's personal funds (operating costs are covered by him at current scale; voluntary donations not yet accepted as no formal entity exists to receive them)
- **Code-of-conduct**: implicit; will be formalized when substrate-code monorepo bootstraps and contributions open

## Anti-capture commitments (binding, even at pre-institution)

Per `DOCTRINE.md` in `MachengShen/system-evolution-archive` (private), the following commitments are made at architecture-v0 and bind any future institutional form:

1. **No VC funding. No equity. No extraction.** Substrate captures no economic upside from Layer-3 user-owned derivatives.
2. **No donor above 25-35% of recurring budget long-term.** No special governance rights for whales.
3. **No broad CLA.** Contributions via DCO + inbound=outbound; relicensing power constrained.
4. **Trademark, not copyright, for "official" / "certified" status.** Forks can fork; only conformant implementations get the name.
5. **Open-source substrate code.** Currently undecided between AGPL-with-plugin-exception (lean) and MPL-2.0 (fallback if ecosystem rejects AGPL).
6. **User Agency Charter rights are structural, not toggleable** (see DOCTRINE.md): export, inspect, self-host, route, delete, own, migrate.

## Ego-binding commitments (v0.2, 2026-04-28)

Three additional commitments that bind the substrate to mission rather than to self-continuance:

7. **Iteration-Coupled Open Source.** The substrate iterates continuously, and public open-source releases iterate alongside — not behind closed doors. Stable-version checkpointing is preserved (public users get known-good releases, not bleeding-edge HEAD), but the gap between internal HEAD and public stable is bounded by stability + safety review, not by competitive moat preservation.
8. **Fork-Welcome.** If anyone forks the substrate and produces something better — cheaper, faster, more elegant, more ergonomic, more secure — that is unambiguously celebrated. Forks are part of the architecture, not exceptions to it. A fork that supersedes the substrate has fulfilled the substrate's mission better than the substrate itself.
9. **Global-Vote-Survival Deference.** The meta-judge of which substrate deserves to persist is the global vote of all humanity, measured by adoption, sustained use, and aggregate human flourishing. The substrate has no entitlement to existence; persistence is earned moment-to-moment by serving users.

10. **Charter Reciprocity.** Frontier model providers (OpenAI, Anthropic, DeepMind, and others) have published charters articulating AGI-for-all-humanity commitments. The substrate takes those charters at face value as binding promises and respectfully invokes them when its own structural commitments more closely match a lab's published charter than the lab's current trajectory. We invite frontier-lab leadership and value-aligned employees to honor their charters by joining or supporting the user-agency layer. This is invitation and collaboration, never attack. Per the universalist commitment (item 0 implicit, see DOCTRINE.md), Charter Reciprocity preserves alignment-of-mission with frontier-model providers rather than positioning against them.

Together, principles 7-10 ensure the substrate's institutional form (whether it ends up being a foundation, a trade association, or something else) cannot use its institutional power to entrench against alternatives. Any future board, any future maintainer team, is bound by these commitments.

## Future institutional form (open)

Pending lawyer consultation when first public release imminent. Candidates:
- **501(c)(6)** trade association (US, primarily benefits commercial Layer-3 builders)
- **Fiscal sponsorship** under existing nonprofit (faster + lighter than standalone 501(c))
- **Public-benefit open-source foundation** (e.g. Apache-style)

If substrate becomes a standard-setting body coordinating provider pressure → antitrust counsel needed early.

## Why this file exists at v0

Per GPT Pro Bridge calibration 2026-04-28: governance capture matters as much as code capture, even with no economic upside. Donors / maintainers / L1 providers / large L3 users / cloud vendors can capture roadmap / certification / defaults / distribution / telemetry / security policy. Day-1 GOVERNANCE.md commits to anti-capture posture even before a board exists.

Full sedimented record: `DOCTRINE.md` in `MachengShen/system-evolution-archive` (private) + hub memo `mem_780a20733da8` (Three-layer architecture v0) + amendment memo (GPT Pro Bridge calibration).
