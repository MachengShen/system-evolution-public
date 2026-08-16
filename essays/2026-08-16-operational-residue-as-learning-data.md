# Operational Residue Is Learning Data

Date: 2026-08-16  
Type: engineering practice update  
Status: public-safe proposal

## One-Sentence Thesis

A long-running personal agent system should learn from the difference between what it accepted, dispatched, claimed, verified, corrected, and retired—not from the volume of memories, tasks, logs, or model calls it produced.

## Public Surface

This note describes a reusable pattern for self-hosted, provider-neutral agent systems. It concerns the contracts between memory, tasks, receipts, owner decisions, workers, and learning updates.

It does not describe a hosted service or grant access to any private owner instance.

## Private Boundary

Excluded by design:

- raw memories and conversations;
- personal or collaborator data;
- credentials, endpoints, machine paths, and device state;
- private task payloads and worker transcripts;
- internal operational counts that could fingerprint a deployment.

The public claim is about structure, not a private corpus.

## Problem

Agent systems often accumulate several successful local mechanisms:

- an intake writes a receipt;
- a memory process creates a task;
- a dispatcher writes another receipt;
- a worker starts or fails;
- a dashboard records a status;
- a recovery process preserves unresolved intent.

Each mechanism can be locally correct while the end-to-end system remains unable to answer:

1. What is the single current truth?
2. Did a worker actually claim the work?
3. Was the result independently verified?
4. Did the owner receive or correct it?
5. Which rule, memory, route, or tool should change next?

The residue of these partial loops is not merely clutter. It is a naturally occurring learning dataset containing false completion, stale state, duplicate promotion, owner-gate friction, infrastructure incidents, recovery failures, and successful repair chains.

## Conceptual Pattern

### Separate three data classes

```text
telemetry/state
  current health + short history + state transitions

event/receipt
  append-only causal events + retention + compaction

semantic memory
  durable owner-relevant claims + provenance + validity + supersession
```

High-frequency telemetry should not automatically become infinitely versioned semantic memory. An operational event should enter durable memory only when it changes future judgment or action.

### Require a causal envelope

Every task-producing surface should preserve a common identity:

```text
task_id
run_id
transaction_id
lease_id + lease_epoch
causation_chain_id
source_event_id
idempotency_key
owner_gate_state
expected_receipt
```

A dispatch without an observed claim is not execution. A completion without causal identity and verification is not a trusted terminal result.

### Learn from verified behavior change

Memory metabolism should optimize for:

- proposal-to-claim conversion;
- claim-to-verified-terminal conversion;
- owner correction followed by reduced repeat failure;
- a live behavior, routing, retrieval, or policy delta;
- obsolete work being explicitly superseded or retired;
- owner attention consumed per verified outcome.

Task creation is traffic, not learning.

### Compile owner correction into prediction error

Corrections such as “that was already finished,” “this is not the current decision,” or “the task did not actually complete” should become typed learning events. The first update target is often a route, tool reliability estimate, retrieval policy, playbook, suppression lease, or truth projection—not another free-form memory.

### Turn permission boundaries into interaction

An owner gate should be a first-class, expiring decision object:

```text
question
recommended_default
scope
target
expiry
safe_on_expiry
consequence
revocation
causal_id
```

Safety that only blocks is incomplete. A useful boundary blocks the action and gives the owner one bounded decision that can close, expire, or be revoked.

## Operational Loop

```text
owner intent or world event
  -> authenticated intake
  -> causal envelope
  -> canonical event ledger
  -> read-only truth projection
  -> claimant
  -> independent verification
  -> result, recoverable failure, or owner decision
  -> owner-visible receipt
  -> learning event
  -> bounded policy / retrieval / routing update
```

The truth projector should begin as a read-only join over existing records. It reports conflicts and orphans instead of rewriting history. Only after shadow replay and canary validation should new tasks adopt the canonical state machine.

## Agent Contract

An agent implementing this pattern must:

1. preserve old ledgers during the shadow phase;
2. distinguish observation, inference, and hypothesis;
3. refuse a trusted closing state when required causal identity is missing;
4. keep owner-gated authority separate from ordinary task text;
5. record one original incident and aggregate repeated symptoms;
6. give stable no-op decisions a TTL instead of recomputing them continuously;
7. emit observable summaries, not hidden reasoning;
8. define a rollback and stop condition before live promotion.

## Receipt Shape

```json
{
  "task_id": "opaque",
  "run_id": "opaque",
  "causation_chain_id": "opaque",
  "source_event_id": "opaque",
  "claim": {
    "worker": "named-role",
    "lease_epoch": 1
  },
  "terminal": {
    "state": "verified | recoverable_failure | owner_decision | superseded",
    "evidence_refs": ["opaque-ref"]
  },
  "learning_event": {
    "target": "routing | retrieval | playbook | tool-reliability | suppression",
    "proposed_delta": "bounded summary",
    "validation": "shadow | canary | accepted | rejected"
  }
}
```

This shape is illustrative, not a stable API.

## First Experiments

### 1. Read-only causal projection

Replay a bounded set of recent tasks across intake, dispatch, claim, result, owner gate, and terminal receipts.

Success:

- nearly every canary reaches one truthful terminal or explicit owner decision;
- current state matches event replay;
- each owner intent has one current projection.

Stop if the projector hides a conflict, overwrites evidence, or needs destructive migration.

### 2. Owner decision cards

Render every new owner gate as an expiring, scoped decision with a safe default.

Success:

- gates become visible quickly;
- old unresolved gates decline;
- no privileged action occurs without a valid grant.

Stop on any bypass, scope merger, or increase in owner burden without improved decision closure.

### 3. Infrastructure incident coalescing

Check worker health before admission and group repeated network, authentication, or transport failures under one incident.

Success:

- task completion rises;
- repeated failure noise falls;
- retries recover under the original causal identity.

Stop on retry storms or when a healthy worker is incorrectly suppressed.

### 4. Current-truth memory retrieval

Evaluate a frozen multilingual query set containing current/old conflicts, supersession, owner preferences, and abstention cases.

Success:

- current verified state outranks stale candidates;
- historical chains remain expandable on demand;
- privacy and abstention do not regress.

Stop if freshness heuristics suppress older but still load-bearing doctrine.

## Anti-Signals

The pattern is failing if:

- a new task protocol is added without retiring or projecting older truth planes;
- task count or memory count is treated as learning progress;
- telemetry dominates semantic retrieval or durable version history;
- an action can start before its durable receipt exists;
- a process launch is treated as proof of worker claim;
- a completion lacks causal identity or independent verification;
- owner gates remain invisible indefinitely;
- owner correction creates another note but does not change future behavior;
- the public artifact exposes private traces in order to appear empirical.

## Next Iteration

Use a mobile conscious interface as the first end-to-end truth probe:

```text
owner turn
  -> authenticated gateway
  -> causal task
  -> one claimant
  -> one verifier
  -> durable receipt
  -> app restart and state recovery
  -> optional owner correction
  -> learning event
```

Do not expand private memory access, device control, or external action authority until this chain can be replayed completely and truthfully.

## Implementation Receipt: Causal Truth P0

Status: `validated-canary`

The first bounded implementation now connects a mobile-first owner surface to a durable, low-permission receipt lane. It does not yet claim general autonomy or private-memory integration.

Implemented:

- an additive causal receipt store that records owner intent before dispatch;
- a deterministic projector that refuses orphaned, conflicting, action-before-receipt, missing-claim, and false-completion chains;
- an expiring owner gate with one-use grants, deny, revoke, and safe expiry, while rejecting permanent authorization;
- worker-health admission, incident coalescing, stable deduplication, and capped retry backoff;
- a frontend that renders only persisted receipts and explicit safe boundaries instead of sample tasks or simulated permissions;
- an authenticated owner scope that exposes a display name but not the raw owner identity to the client;
- a low-permission backend handoff that can capture intent and return a receipt without private memory access, external messaging, or device control.

Validation:

- the source builds and passes static checks;
- twenty-two contract and integration tests pass;
- a local end-to-end canary produced both a durable client receipt and a backend receipt;
- the health gate correctly stopped a bad route, preserved the original receipt, and recovered under the same idempotency key after the route was corrected;
- the owner surface was published under owner-only access.

Truth boundary:

- “received” is not “completed”;
- browser or transport failure is rendered as failure or recoverable waiting, never replaced by demo data;
- memory submissions remain proposals until a separate confirmed memory-write path exists;
- no device or external-action capability is implied by the presence of an owner gate.

Next experiment:

Replay production receipts through the causal projector, bind any backend-generated owner request to the gate state machine, and add a verified result receipt before allowing the interface to show a terminal `done` state.
