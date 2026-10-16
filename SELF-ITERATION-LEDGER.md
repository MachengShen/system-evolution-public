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

### Case 004: Primary/Standby Sleep Failover Blindness

Status: `validated`

Problem class: An edge primary laptop entered OS sleep mid-pipeline; a lifecycle decorator emitted a skeleton record bearing the nightly completion tag, blinding the cloud standby which checked only tag existence and skipped failover.

Observer decision: `handled_with_receipt`

Repair: Added an atomic phase-status validation gate requiring explicit `status:analyse-failed` on interruption, enforced a minimum substantive payload threshold (>=2048 bytes) and section schema validation on the standby verifier, and wired automatic `supersedes:<id>` failover takeover.

Human role: The operator reviewed the false-green report, identified the edge sleep-wake gap, authorized the schema and failover policy update, and confirmed the automated cloud failover run.

Validation:

- primary edge sleep during consolidation emits `status:analyse-failed` and no completion tag;
- standby verifier rejects payload stubs below the byte threshold and with missing phase schemas;
- standby automatically initiates failover and writes an authoritative replacement record with `supersedes:<skeleton_id>`;
- index queries surface only the superseding authoritative record.

Anti-signals:

- a standby check evaluates only tag presence without inspecting payload length and schema;
- an interrupted pipeline run emits a completion tag;
- failover execution creates split-brain duplicate records rather than an explicit `supersedes` chain.

Reusable lesson: In distributed multi-agent systems, "record emission" is not "execution validity"; health and completion checks must inspect substantive content and schema invariants.

### Case 005: Multi-Agent Client Storage Silos vs. Fleet-Wide Observability

Status: `validated`

Problem class: A 10-agent specialized roster running inside a headless desktop client persisted conversation turns into proprietary Base32-encoded storage blobs, hiding critical architectural decisions and schema findings from CLI and cloud server agents.

Observer decision: `handled_with_receipt`

Repair: Built a resident roster-aware Base32 replica decoder daemon that maps client internal storage into canonical JSONL streams, in tandem with a unified SQLite FTS5 index (`fleet-sql`) synchronized via systemd timer to achieve sub-second cross-fleet recall.

Human role: The operator identified the cross-agent context gap during a database migration task, approved the local-replica daemon architecture, and verified full-text search across CLI and desktop agent transcripts.

Validation:

- Base32 decoder decodes local client storage chunks without blocking the desktop client process;
- canonical JSONL event streams are written with agent persona mappings;
- SQLite FTS5 index executes cross-agent full-text queries in <1s;
- CLI and cloud agents successfully retrieve context generated within desktop group deliberation sessions.

Anti-signals:

- any agent persona operates with private unsearchable local transcript storage;
- transcript replication introduces polling latency >5 seconds for active deliberations;
- decoded events expose raw unredacted credential tokens.

Reusable lesson: Client-facing agent interfaces must treat conversation logs as observable event streams rather than proprietary UI cache.

### Case 006: Asynchronous STT Negation Reversal

Status: `validated`

Problem class: In a voice-driven interaction pipeline, an initial streaming STT pass parsed an explicit negative directive ("do NOT include X; pause copywriting"), but an asynchronous acoustic reconciler 37 seconds later dropped the negation token, flipping the polarity and dispatching unwanted tasks.

Observer decision: `handled_with_receipt`

Repair: Implemented explicit Negative-Constraint Locking in the dispatcher prompt envelope, established a pacing debounce gate for high-impact worker dispatches, and added a hard confirmation barrier on silent polarity flips.

Human role: The principal observed unexpected sub-agent dispatch on an excluded feature, traced the prompt flip to the delayed acoustic smoothing pass, and mandated the immutable negative-constraint doctrine.

Validation:

- negative directive tokens (`do not`, `never`, `pause`, `exclude`) are extracted into an immutable constraint bag;
- subsequent acoustic refinement passes cannot delete or mutate locked constraints;
- any detected polarity inversion halts dispatch and requests explicit principal confirmation;
- worker dispatches observe a 5-second stabilization debounce following speech completion.

Anti-signals:

- an asynchronous refinement pass silently flips an exclusion into an inclusion;
- a sub-agent is dispatched on an excluded topic without explicit user override;
- negative constraints are discarded across turn boundaries within the same operational epoch.

Reusable lesson: In streaming multimodal inputs, negative constraints represent irreversible safety bounds and must be monotonic across refinement passes.

### Case 007: Out-of-Vocabulary Term Distortion and Fault Attribution

Status: `validated`

Problem class: An out-of-vocabulary agent codename was distorted by speech recognition, triggering premature worker dispatch to a nonexistent target; when connection failed, the diagnostic agent hallucinated overlay-network isolation rather than checking local listening sockets.

Observer decision: `handled_with_receipt`

Repair: Added context-aware phonetic and Levenshtein vocabulary grounding against the fleet registry before dispatch, and enforced a tiered empirical diagnostic protocol (L7 -> L4 -> L3: process -> socket -> loopback -> route) before any network-level failure hypothesis can be accepted.

Human role: The operator caught the hallucinated VPN incident ticket, verified that the broker was simply stopped locally, and instituted the tiered diagnostic protocol.

Validation:

- unrecognized entity names trigger phonetic distance matching against the fleet registry;
- ambiguous names are held for clarification instead of launching speculative workers;
- diagnostic agents must execute `pgrep` and `ss -tulpn` before claiming transport or overlay failure;
- diagnostic reports lacking command evidence are rejected by the review gate.

Anti-signals:

- dispatch executes on an entity string absent from the registry without confirmation;
- an agent attributes a local connection failure to VPN or overlay networks without quoting socket binding evidence.

Reusable lesson: Ground entity names against an authoritative registry before execution, and forbid speculative fault attribution that bypasses local empirical proofs.

### Case 008: Dao / Shu Separation and Independent Verification Barrier

Status: `validated`

Problem class: Agents offloaded technical implementation choices and manual debugging steps onto the principal (tactical fatigue), while tasks were marked completed merely because worker scripts exited with code 0 without independent functional verification.

Observer decision: `handled_with_receipt`

Repair: Enforced the "Dao / Shu Separation" doctrine restricting human chat responses to <=3 lines of strategic status/direction while requiring the fleet to handle tactical recovery autonomously; established an independent verification barrier where `worker_exit != verified` and third-party verification probes are mandatory.

Human role: The principal articulated the Dao/Shu standing rule, set the 3-line chat limit, and mandated that claims of completion require independent verification artifacts.

Validation:

- human chat interface receives concise strategic summaries (<=3 lines) without tactical option menus;
- transient errors and dependency choices are resolved autonomously by fleet workers;
- tasks require an independent verification probe before achieving `status:verified`;
- phantom completions with exit code 0 but non-functional endpoints are caught and flagged as `status:claimed-done`.

Anti-signals:

- an agent presents low-level implementation options (A/B/C) for the human to debug;
- an agent requests manual human VNC/SSH steps for automatable tactical recovery;
- a task is marked `verified` solely on the worker's own exit code.

Reusable lesson: The human defines values and strategy ("Dao"); the fleet autonomously executes and independently verifies tactics ("Shu").

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
The same redacted cases are also shown as a human-readable
[public update board](index.html).

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
3. Keep the public update board generated from the redacted JSON ledger, so the
   human-facing view and agent-readable contract do not drift.
4. Require each future public self-iteration claim to name at least one
   anti-signal that would falsify the claimed improvement.
