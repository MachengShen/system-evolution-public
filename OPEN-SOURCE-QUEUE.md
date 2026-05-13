# Open Source Queue

This is the public-facing queue of reusable wheels that should be lifted out of
Macheng's private system when safe.

## Ready As Public Docs

| Component | Public form | Why |
| --- | --- | --- |
| Black-box I/O adapter | Essay + protocol notes | General pattern; no private data required. |
| Open communication substrate | `starshard-communication` repo + SPEC-0001 | Thin protocol and synthetic examples; no private contact graph. |
| Request handling / BYOK reply policy | `REQUEST-HANDLING.md` | Useful immediately for inbound traffic. |
| Agent-facing setup order | `AGENT-SETUP.md` | Lets other agents bootstrap without human-heavy docs. |
| Intake/reply schemas | `schemas/` | Low-risk protocol boundary. |

## Next To Lift

| Component | Public form | Required gate |
| --- | --- | --- |
| Shared Memory Hub pattern library | Docs/examples only first | Remove any private memory references; add license. |
| Owner Dashboard/Console contract | Screenshots + schema + local-only mock | Remove private status lanes and raw owner data. |
| Task ledger / hierarchical queue | Schema + toy implementation | Strip private worker names, tokens, and paths. |
| Reviewer bridge contract | Protocol + fallback policy | No provider keys, no private prompts. |
| WeChat bridge | Redacted health/repair contract only | No raw messages, no account-specific automation. |

## Public Repos

| Repo | Role | Status |
| --- | --- | --- |
| `MachengShen/system-evolution-public` | Public doctrine, specs, essays, queue | Live. |
| `MachengShen/starshard-communication` | Open inbox/addressing/policy/receipt substrate | Live; needs minimal adapter demo and community critique. |
| `MachengShen/wechaty` fork | Upstream contribution staging | Draft PR only; not a product repo. |

## Extraction Order

1. `starshard-communication`: make the minimal email/webhook adapter runnable
   in under five minutes.
2. `task-ledger`: extract schemas plus a toy implementation, not private task
   data.
3. `frontstage-wakeup`: publish the wakeup packet schema and bounded runner
   pattern with synthetic fixtures.
4. `public-access-boundary`: publish trust-tier / public-agent boundary docs
   and schemas.
5. `reviewer-bridge-contract`: publish reviewer quorum/fallback protocol with
   dummy providers.
6. `owner-state-brake`: publish as a general skill/design note only after
   removing personal health context and private triggers.

## Not For Public Release

- raw transcripts
- private Memory Hub
- private contact/collaborator directory
- email/WeChat credentials
- billing and provider keys
- active owner Dashboard data
- private hotel/medical/family/life logistics

## Rule

Public release should favor protocols, schemas, safety shells, synthetic
examples, and small toy implementations before production adapters.
