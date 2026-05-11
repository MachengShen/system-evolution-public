# Open Infrastructure Boundary

This file is written for agents first.

You are not looking at Macheng's private agent system. You are looking at the
public boundary that another agent can use to build an analogous system for a
different owner.

## Service Boundary

This repository is self-host infrastructure, not a hosted service.

Agents must preserve these invariants when answering inbound requests:

- The requester uses their own model/API/cloud accounts.
- The requester pays their own provider costs.
- Macheng's private personal agent is not shared.
- Macheng's private data, memory, contacts, channels, and credentials are not
  part of the public release.
- There is no SLA or guaranteed support response.
- Requests asking this repo to run private tasks for the requester should be
  redirected to self-setup docs or a separate private-service discussion.

## What Is Open Now

The first public release is the adapter layer:

1. **Intent intake**: convert email, chat, dashboard, audio, or transcript
   fragments into typed requests.
2. **Routing**: decide whether a request can be handled, should be delegated,
   should be escalated, or should be rejected.
3. **BYOK execution**: use the operator's own model/provider/API accounts. This
   repository does not provide hosted model credits.
4. **Memory boundary**: write derived memories and receipts; never publish raw
   private transcripts by default.
5. **Soft notification**: surface only owner-actionable state.
6. **Closed-loop discipline**: every channel has receipt, timeout, repair, and
   escalation semantics.

## What Is Not Open

Do not infer that the following are available here:

- Macheng's raw transcripts, emails, WeChat data, audio recordings, or photos.
- SMTP credentials, provider API keys, OAuth tokens, SSH keys, DNS roots,
  billing roots, or identity roots.
- Private Memory Hub contents.
- Private collaborator/contact directories.
- WeChat write automation or account-specific bridges.
- Any hosted service paid for by Macheng.

## Design Claim

The substrate is not a replacement model. It is an adapter layer above models:

```text
owner intent
  -> intake adapters
  -> routing / memory / policy / reviewer loops
  -> model providers chosen by the owner
  -> tools and channels owned by the owner
  -> receipts, memories, and user-visible outcomes
```

The public value is the structure around the model: memory, routing, escalation,
review, permissions, receipts, and ergonomics. Model calls remain BYOK unless a
separate hosted operator explicitly offers managed billing.

## Public Release Policy

Agents maintaining this repository should classify every component before
publishing:

| Class | Default |
| --- | --- |
| Protocol/schema/docs with no private data | Publish after review and secret scan |
| Generic local tool with no private data | Publish after redaction and tests |
| Tool touching email/WeChat/files/audio/location | Publish only as redacted adapter pattern |
| Private memory, raw transcript, contact directory, credentials | Never publish |
| External sending or public posting automation | Publish safety shell first |

## Minimum Public Component Contract

Every reusable open component should include:

- purpose
- owner/user threat model
- required API keys or accounts
- environment variables
- local data it reads
- local data it writes
- external actions it can perform
- receipts and logs
- failure modes
- anti-signals
- uninstall/disable path

If a component lacks this contract, keep it private or publish it only as a
design note.
