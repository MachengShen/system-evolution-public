# SPEC-0001: Inbox, Addressing, And Receipts

Status: draft
Date: 2026-05-13

This spec defines the thinnest useful layer of a personal-agent-native
communication substrate: inbox, addressing, policy, and receipts.

It is deliberately not a full messaging app, not a crypto protocol, and not a
memory-hub protocol. It defines the minimum event shape needed for a user's
agent to receive, route, acknowledge, and audit communication.

## Non-Goals

- No custom encryption protocol. Transport encryption should use existing
  protocols and libraries such as Matrix/MLS, Signal Protocol, TLS, or
  established mail/webhook security patterns.
- No platform-specific scraping.
- No claim that the recipient's agent should read every intimate message.
- No hosted service requirement.
- No dependency on a specific model provider.

## Core Objects

```text
ContactIdentity
EndpointAddress
TrustTier
MessageEnvelope
AgentPolicy
Receipt
AuditEvent
```

## ContactIdentity

```json
{
  "contact_id": "contact_123",
  "display_name": "Example Person",
  "known_endpoints": [
    {
      "scheme": "email",
      "address": "person@example.com",
      "verified_at": "2026-05-13T00:00:00Z"
    }
  ],
  "trust_tier": "priority"
}
```

## TrustTier

Trust tiers are local to the recipient. They do not claim global truth about a
relationship.

```text
direct
priority
standard
public
blocked
```

Implementations may map these to different behaviors. A minimal default:

- `direct`: low-latency delivery, no digest delay.
- `priority`: agent classification plus quick surface.
- `standard`: digest or task queue.
- `public`: limited-scope public agent or contact form.
- `blocked`: no delivery except audit.

## MessageEnvelope

```json
{
  "message_id": "msg_20260513_0001",
  "created_at": "2026-05-13T00:00:00Z",
  "from": {
    "scheme": "email",
    "address": "person@example.com"
  },
  "to": {
    "scheme": "agent-endpoint",
    "address": "owner@example.net"
  },
  "channel": "email",
  "subject": "hello",
  "body": "Can you take a look at this?",
  "attachments": [],
  "declared_urgency": "normal",
  "metadata": {}
}
```

## AgentPolicy

```json
{
  "policy_id": "policy_default_v0",
  "recipient_user_id": "user_local",
  "default_tier": "standard",
  "tier_actions": {
    "direct": ["deliver_now", "write_receipt"],
    "priority": ["classify", "surface_soon", "write_receipt"],
    "standard": ["classify", "digest", "write_receipt"],
    "public": ["route_public_agent", "write_receipt"],
    "blocked": ["audit_only"]
  }
}
```

## Receipt

A receipt is not only "delivered." The useful unit is lifecycle state.

```json
{
  "receipt_id": "rcpt_20260513_0001",
  "message_id": "msg_20260513_0001",
  "created_at": "2026-05-13T00:00:05Z",
  "state": "handled",
  "state_detail": "surfaced_to_priority_inbox",
  "actor": "recipient_agent",
  "next_expected_event": null
}
```

Initial receipt states:

```text
received
routed
surfaced
digested
task_created
replied
delegated
blocked
handled
failed
```

## AuditEvent

```json
{
  "audit_id": "audit_20260513_0001",
  "created_at": "2026-05-13T00:00:05Z",
  "event_type": "receipt_written",
  "message_id": "msg_20260513_0001",
  "receipt_id": "rcpt_20260513_0001",
  "actor": "recipient_agent",
  "summary": "Message received and surfaced to priority inbox."
}
```

## Extension Points

This thin spec intentionally leaves larger systems as extensions:

- Memory persistence
- Task ledgers
- Public/friends/private ambassador agents
- Contact graph synchronization
- Cross-device notification surfaces
- Provider routing

The thin layer should still work if none of those exist.

## Success Criterion

A reference implementation should demonstrate:

1. Receive an email or HTTP webhook.
2. Map sender to a local `ContactIdentity`.
3. Apply `TrustTier` and `AgentPolicy`.
4. Write a `Receipt`.
5. Produce an auditable local log.

That is enough for the first protocol spike.

## Six-Month Metric

The first serious success metric is not stars or manifesto agreement.

Within six months, at least 30 of the owner's top 50 active contacts should be
reachable through a non-super-app path with a receipt loop:

```text
message received -> routed -> surfaced/digested/delegated/blocked -> receipt
```

That metric keeps the project grounded in communication reality: network
effects are defeated by working migration paths, not by a better slogan.

## Reference Demo Target

The first demo should stay smaller than the full system:

1. Accept an HTTP webhook or email-like JSON message.
2. Map the sender to a local `ContactIdentity`.
3. Apply a static `AgentPolicy`.
4. Write `Receipt` and `AuditEvent` JSONL files.
5. Print the next action: surface now, digest, task, public-agent route, or
   audit-only.

No memory hub, model provider, or private contact graph is required for the
first demo.
