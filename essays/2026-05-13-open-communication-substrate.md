# What Replaces Super-App Chat In The AI-Agent Era?

Date: 2026-05-13

The replacement for super-app chat is probably not another chat app.

It is an open communication substrate: a user-owned layer where inboxes,
addresses, receipts, policies, and channel adapters are part of the same closed
loop. Memory and task systems can plug into that layer, but they do not need to
be part of the first spec.

The practical goal is not to win a slogan contest against any one platform. It
is to make closed super-app chat less necessary by giving people a working path
out: open addresses, local policy, portable receipts, and adapters that can
start with channels people already use.

## The Problem

Messaging apps from the IT era treat communication as a stream of messages
between human accounts. That model made sense when the primary action was
"read this and reply."

AI-agent systems change the shape of communication.

A message may need to trigger:

- a receipt,
- an escalation,
- a task,
- a durable memory,
- or a reply that the user's own agent can help complete.

If the platform owns the inbox, contact graph, message history, notification
policy, and integration surface, the user does not really own their social
operating system.

## Direct Messages Still Matter

The strongest objection to AI-mediated communication is correct: intimate
people still need direct messages.

But directness is not the same thing as being trapped inside one app.

Directness means preserving agency, trust, latency, privacy, emotional
bandwidth, and the ability to reach the person who matters. An AI-native
communication substrate should therefore support trust tiers instead of forcing
all relationships through one undifferentiated inbox.

One possible minimum:

- **Direct**: intimate or high-trust contacts can reach the user with low
  latency.
- **Priority**: messages are classified by the user's agent but surfaced
  quickly.
- **Standard**: messages enter a digest or task queue.
- **Public**: strangers interact with a public ambassador or limited-scope
  agent, not the user's private system.

This keeps intimacy intact while removing platform captivity.

## A Minimal Protocol Surface

The first useful artifact does not need to be a complete app. It can be a small
protocol and reference implementation.

Candidate primitives:

```text
ContactIdentity
EndpointAddress
TrustTier
MessageEnvelope
AgentPolicy
Receipt
AuditEvent
```

The important shift is that a message is no longer only a blob of text. It is an
event in a user-owned agent system.

The first reference implementation should be deliberately boring: receive an
email-like or webhook message, map the sender to a local trust tier, apply a
static policy, write a receipt, and leave an audit trail. That is enough to make
the idea concrete without asking anyone to trust a new social network.

## Existing Channels Become Adapters

Email, web chat, Matrix, SimpleX, ActivityPub, MCP endpoints, local inboxes,
HTTP webhooks, and legacy messaging systems can all be adapters.

The user-owned substrate should be the place where state becomes durable and
auditable. Individual channels should not own the user's memory, contact graph,
or agency.

This also avoids a common trap: trying to replace a closed platform by building
one more closed platform. The goal is not to make a prettier silo. The goal is
to make the silo less important.

## Open Questions

1. What is the smallest useful `MessageEnvelope`?
2. How should `TrustTier` be represented without encoding one person's social
   assumptions into everyone else's system?
3. What should a receipt prove: delivery, attention, handling, task creation, or
   final resolution?
4. Which adapters are most useful first: email, Matrix, SimpleX, MCP, webhooks,
   browser chat, local-first inboxes, or something else?
5. How can memory and task systems attach without becoming mandatory for the
   thin protocol layer?

## What This Is Not

This is not a proposal to scrape private databases from existing chat apps.

This is not a hosted service.

This is not an argument that every intimate message should be read by an AI.

This is not a new cryptographic protocol. Transport security should reuse
existing, reviewed protocols and libraries.

This is an argument that users should own the communication substrate around
their agents: identity, policy, memory, receipt, and portability.

## Invitation

If this framing is right, the next step is not a grand product launch. It is a
small open RFC and a few working adapters.

The useful question is:

> What is the minimal open communication substrate that lets AI-agent users
> leave closed super-app chat behind?

See also: [SPEC-0001: Inbox, Addressing, And Receipts](../SPEC-0001-inbox-addressing-receipts.md).
