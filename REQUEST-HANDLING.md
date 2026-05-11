# Request Handling Policy

This document tells agents how to respond when people ask for access, setup, or
help.

## Default Position

The public project offers an adapter-layer infrastructure pattern, not free
hosted compute or model credits.

Each requester should normally:

- run their own instance;
- bring their own provider API keys;
- pay their own model/API/cloud costs;
- keep their own private data in their own environment;
- use the public protocol/docs as the starting point.

## Agent Classification

Classify each inbound request:

| Request type | Default handling |
| --- | --- |
| "How do I try this?" | Point to `AGENT-SETUP.md`; tell them BYOK. |
| "Can you host this for me?" | Draft a scoped managed-service discussion; do not promise free hosting. |
| "Can I use Macheng's assistant?" | Decline sharing private owner instance; offer public setup docs. |
| "Can I contribute code/docs?" | Point to `CONTRIBUTING.md` and public issue/discussion path once available. |
| "Can you integrate my email/WeChat/files?" | Treat as sensitive; provide adapter pattern only unless a private paid setup is agreed. |
| "Can I get Macheng's data/context?" | Refuse; private raw context is not part of the open-source boundary. |

## Email Reply Template

```text
Hi,

Thanks for reaching out. Macheng's personal agent is not exposed as a shared
hosted service, because it contains private memory, channels, and context.

The reusable part is the open adapter-layer infrastructure: request intake,
routing, memory boundaries, reviewer loops, receipts, and BYOK model-provider
execution. The intended setup is that you run your own instance with your own
API keys and pay your own provider/cloud costs.

Start here:
- README.md
- INFRASTRUCTURE.md
- AGENT-SETUP.md
- REQUEST-HANDLING.md
- schemas/

If you want collaboration beyond self-setup, please describe your use case,
data boundary, preferred model providers, and whether you need a private
deployment or only protocol guidance.

This message was drafted by Macheng's AI assistant.
```

## Closed Loop

Every request must end in one of:

- `answered_with_public_docs`
- `drafted_for_owner_review`
- `escalated_to_private_setup_discussion`
- `rejected_private_data_or_credentials`
- `blocked_missing_contact_or_context`

Do not leave inbound requests as "seen but not handled."
