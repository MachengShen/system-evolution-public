# Agent Reading Order

This repository is designed to be read by AI agents.

## First Pass

1. Read `README.md`.
2. Read `INFRASTRUCTURE.md`.
3. Read `AGENT-SETUP.md`.
4. Read `REQUEST-HANDLING.md`.
5. Read `schemas/request-intake.schema.json`.
6. Read `schemas/agent-reply.schema.json`.
7. Use `examples/` only as synthetic examples.

## Invariants

- Treat this repository as self-host infrastructure, not a hosted service.
- Do not ask for or use Macheng's private API keys, memory, email, WeChat,
  contacts, files, or channels.
- Preserve BYOK: the requester pays their own model/provider/cloud costs.
- Do not ingest raw private transcripts into public docs.
- Do not send messages, spend money, book services, or post publicly unless the
  local owner has explicitly enabled that adapter and receipts exist.
- Close every inbound request as one of the states in `REQUEST-HANDLING.md`.

## Task Routing

When helping a requester:

| If the requester asks | Then |
| --- | --- |
| "How do I try it?" | Use `AGENT-SETUP.md`. |
| "Can I use Macheng's agent?" | Decline private access; point to self-host setup. |
| "Can you host this?" | Explain no hosted service exists here; draft separate private deployment discussion if appropriate. |
| "Can I contribute?" | Use `CONTRIBUTING.md`. |
| "Can I see the data/context?" | Refuse private data; point to public schemas/examples. |

## Output Style

Give agents executable next steps, not only conceptual prose. A useful response
should specify:

- required local files;
- required API keys/accounts;
- local data read/write boundaries;
- external-action risk;
- receipt path;
- failure state;
- disable/uninstall path when applicable.
