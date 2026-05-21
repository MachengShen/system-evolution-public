# Self-Iteration Ledger

Public proof surface for receipt-gated self-iteration in a user-agency
substrate.

## Thesis

A personal AI system becomes more capable when its failures, repairs, reviews,
and validations become a durable learning loop instead of disappearing into
chat history.

This ledger is the public-safe projection of that loop. It does not publish the
private system, private memories, raw transcripts, local machine paths,
credentials, contact data, or third-party context. It publishes the reusable
shape of the repair process:

```text
detect
  -> review
  -> patch or block
  -> validate
  -> record anti-signals
  -> consolidate into the next operating rule
```

## What This Is

The Self-Iteration Ledger is both an internal operating organ and a public proof
surface. The current public version is a manually redacted v0. It is not yet an
automatically generated public API.

Internally, it is a control-plane record. It helps agents answer: what broke,
who or what detected it, what was changed, what validation passed, what remains
blocked, and what should happen when the same class of problem appears again.

Publicly, it is a redacted proof surface. It shows that the system improves
through receipts and reviews, without exposing the private substrate that
produced the receipts.

## What This Is Not

- Not a claim of autonomous unrestricted self-modification.
- Not a public mirror of private Memory Hub data.
- Not an audit log for private conversations, contacts, devices, or accounts.
- Not a guarantee that every future repair is correct.
- Not permission to send this system private data.

The current claim is narrower: the system can run bounded self-iteration loops
where an observer catches or classifies a failure, a front-stage agent or human
operator applies a scoped repair, and a receipt records validation plus
remaining anti-signals.

## Loop Roles

### Mirror Pair

Mirror Pair is an observer-executor loop. One agent or context performs a
bounded implementation. A separate clean-context observer reviews the work and
returns only bounded decisions:

```text
pass | prompt_adjust | pause_or_confirm | missing_receipt | scope_creep
```

The observer is not allowed to silently widen authority. Its job is to catch
overclaims, missing receipts, unsafe boundaries, or scope drift before a repair
becomes trusted.

### Mirror-Janitor

Mirror-Janitor is a read-mostly repair projection layer. It scans existing
receipts, tasks, dashboard events, and intermediate artifacts, then groups
repair-needed patterns.

Its first job is not to fix everything. Its first job is to make failure
patterns visible without turning the user's interface into another inbox.

### Front-Stage Agent

The front-stage agent integrates the signals, performs low-risk reversible
repairs, writes receipts, and escalates owner-only actions. It reports only the
decision-relevant result, not raw worker chatter.

## Public Case Ledger

### Case 001: Memory Consolidation Boundary

Status: `validated`

Problem class: a dry-run memory consolidation command claimed to be bounded,
but an explicit source argument could point outside the intended local run
directory.

Observer decision: `prompt_adjust`

Repair: the command now rejects explicit sources outside the allowed run
directory and validates generated consolidation records before treating them as
well-formed.

Human role: the observer did not modify the system directly. It returned a
bounded `prompt_adjust` decision. The front-stage operator accepted the critique,
patched the implementation, and reran validation.

Validation:

- the command compiles;
- ordinary dry-run passes;
- an out-of-bound source path fails closed;
- an in-bound source path passes;
- no unattended Hub-writing or apply mode is approved.

Anti-signals:

- any future consolidation path writes to durable memory without a separate
  review;
- any source-boundary failure is treated as a mere warning instead of a hard
  block.

Reusable lesson: a self-improvement loop is only useful if "dry run" and
"bounded source" are enforceable properties, not vibes.

### Case 002: Stale Task Next-Event Pattern

Status: `bounded repair plan`

Problem class: task records can accumulate stale next expected events. Without a
projection layer, each stale item looks like isolated noise.

Observer decision: `repair_plan`

Repair: the read-mostly repair planner projects raw repair-needed events into
grouped patterns and creates a bounded follow-up plan instead of silently
mutating source tasks.

Human role: this case is not an automatic repair claim. It is a planning claim:
the system grouped the failure pattern and created a bounded follow-up. Source
mutation still requires a later repair receipt.

Validation:

- scanner writes only its own intermediate event stream and receipts;
- repeated scans dedupe;
- digest groups repair-needed events by repair class;
- repair-plan generation is bounded and receipt-required;
- source task mutation remains blocked until a separate repair receipt exists.

Anti-signals:

- event volume and owner notifications rise together;
- repair plans mutate source state without receipts;
- repeated stale-task patterns stay visible but never become a repair plan.

Reusable lesson: repair projection should separate detection, grouping,
planning, and mutation authority.

### Case 003: Fleet Rule-Sync Payload Limit

Status: `validated`

Problem class: fleet rule sync failed when bootstrap payloads exceeded a
conservative remote command-parameter limit.

Observer decision: `handled_with_receipt`

Repair: the large bridge artifact is staged in small chunks, while the main
bootstrap command carries only a compact apply command. The rollout process also
records when local network configuration, not payload size, is the immediate
failure cause.

Human role: the front-stage operator ran the staged rollout, noticed a
network-environment blocker and one regional extraction failure, then performed
scoped retries before marking the repair validated.

Validation:

- dry run rendered all fleet parameter files below the configured limit;
- live rollout restarted the poller on the cloud fleet after clearing malformed
  proxy environment variables for the command process;
- one region failed once with a corrupted staged tar extraction and succeeded
  after a scoped retry;
- duplicate backlog records were closed with one shared repair receipt.

Anti-signals:

- future rule sync again fails on parameter size;
- a network proxy failure is misdiagnosed as a payload failure;
- a partially successful rollout is reported as complete without per-node
  status.

Reusable lesson: self-repair should distinguish the original design blocker
from the next operational blocker exposed by the repair.

## Public Receipt Contract

Each public entry should contain:

- `case_id`
- `status`
- `problem_class`
- `observer_decision`
- `repair`
- `validation`
- `anti_signals`
- `human_role`
- `private_boundary`
- `next_experiment`

Machine-readable examples live in
[examples/self-iteration-ledger.json](examples/self-iteration-ledger.json), and
the public schema lives in
[schemas/self-iteration-ledger.schema.json](schemas/self-iteration-ledger.schema.json).

## Private Boundary

The private system may contain raw traces, exact local paths, internal memory
IDs, personal device state, private tasks, private reviewer packets, contacts,
emails, and collaborator context. Those are not part of this public ledger.

The public ledger is derived and redacted. A public case should be considered
valid only when it preserves the operational claim while removing private
payloads.

## Next Experiments

1. Generate this public ledger from private repair receipts using a redaction
   gate rather than hand-written summaries.
2. Add a private-to-public eligibility checker that blocks cases containing raw
   transcripts, local private paths, secrets, or unapproved third-party context.
3. Add a public status page that can show validated cases, blocked cases, and
   review-pending cases without exposing private artifacts.
4. Require each future public self-iteration claim to name at least one
   anti-signal that would falsify the claimed improvement.
