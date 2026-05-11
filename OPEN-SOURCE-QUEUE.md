# Open Source Queue

This is the public-facing queue of reusable wheels that should be lifted out of
Macheng's private system when safe.

## Ready As Public Docs

| Component | Public form | Why |
| --- | --- | --- |
| Black-box I/O adapter | Essay + protocol notes | General pattern; no private data required. |
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
