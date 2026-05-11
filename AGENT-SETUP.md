# Agent Setup

This document is for an AI agent helping a new user set up their own
user-agency substrate.

Do not ask the user to pay Macheng or use Macheng's API keys. The default setup
is bring-your-own-key.

## Bootstrap Order

1. Read `INFRASTRUCTURE.md`.
2. Confirm that the user understands BYOK: they pay their own model/provider
   bills.
3. Create a private working directory for that user.
4. Create a local `.env` file that is never committed.
5. Add provider keys owned by that user.
6. Start with request intake and response drafting before any autonomous
   external actions.
7. Add memory only after the raw/private boundary is explicit.
8. Add outbound channels only after receipts, audit logs, and disable paths
   exist.

## Required Secrets

Use names like these, but do not require a specific provider:

```text
OPENAI_API_KEY=
ANTHROPIC_API_KEY=
GOOGLE_API_KEY=
OPENROUTER_API_KEY=
SMTP_HOST=
SMTP_USER=
SMTP_PASS=
```

Only set the keys the user actually chooses. Do not commit `.env`.

## Minimum Local Files

```text
substrate/
  .env                 # private, never committed
  requests.jsonl        # append-only intake events
  replies.jsonl         # drafted/sent reply receipts
  memories.jsonl        # derived memories, not raw transcript dumps
  policy.md             # what the agent is allowed to do
  audit/                # command receipts and failures
```

## First Working Loop

The first loop should be narrow:

```text
incoming request
  -> classify with schemas/request-intake.schema.json
  -> decide: handle / draft / escalate / reject
  -> produce schemas/agent-reply.schema.json
  -> write receipt
```

Do not begin with always-on audio, WeChat automation, personal file indexing, or
public posting. Those are higher-risk adapters and need explicit local policy.

## Default Reply To New Requesters

If someone asks for access to Macheng's system, answer with the open-source
boundary:

> This is not a hosted free service. The public substrate is an adapter layer
> you can run for yourself. You use your own model/API accounts, your own data,
> and your own operating budget. The public docs explain the protocol; private
> owner data and credentials are not shared.

## Anti-Signals

Stop and ask for review if:

- an agent tries to copy private transcripts into public docs;
- a requester asks for Macheng's keys, credits, WeChat, email, contacts, or
  private Memory Hub;
- a component can send messages, spend money, book services, or expose private
  data without receipts and a disable path;
- the user cannot tell which costs they will pay;
- docs are written mainly for humans while agents still cannot execute them.
