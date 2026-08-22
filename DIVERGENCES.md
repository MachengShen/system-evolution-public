# Divergences: where a personal agent fleet stops looking like a web service

Date: 2026-08-22 · Companion: [Agent Safety — Open Research Problems](OPEN-PROBLEMS-AGENT-SAFETY.md) · Format: [Claim-Receipt](CLAIM-RECEIPT.md)

This document lists the places where the operating practice of a continuously
running personal agent fleet has diverged from the conventional practice of
building internet software — and states, for each one, what it cost.

It is written for people who are about to build a similar system and want the
design decisions without the two months of rediscovery. It is **not** a
manifesto, and none of these are claimed to be right in general. Several were
adopted only after the conventional approach failed in a way we could name.

Each entry has the same five fields:

| Field | Meaning |
|---|---|
| **Conventional** | what the standard internet-software practice is |
| **Here** | what this system does instead |
| **Why** | the failure the divergence is a response to |
| **Cost** | what we gave up; where this is a bad trade |
| **Status** | how well verified, with a badge (below) |

### Status badges

- 🟢 **load-bearing** — in production, and has already survived a real failure
  of the kind it exists to prevent. There is an incident behind it.
- 🟡 **in production, unstressed** — running, but we have no evidence it works
  under the condition it was built for. It may be decoration.
- ⚪ **written, not enforced** — a rule in text, with no mechanism that makes it
  bite. Honest label for "we believe this but nothing stops us violating it."

Same honesty discipline as the rest of this repo: a badge that flatters is a
badge that is wrong.

---

## 1. The rule layer is loaded unconditionally, not retrieved on demand

**Conventional.** Context is retrieved. You embed your documentation, your
policies, and your prior decisions, and you pull the relevant chunk when the
current query resembles it. Retrieval-augmented generation is the default answer
to "the model needs to know a lot of things."

**Here.** There are two memory tiers with different physics. A small **hot
tier** — currently a few thousand tokens — is injected into every single turn
unconditionally, with no relevance test. Everything else lives in a **cold
tier** that is searched. The admission criterion for the hot tier is not
importance and not frequency; it is: *does this rule only work if it arrives
uninvited?*

**Why.** Retrieval is a similarity match against what the agent is currently
thinking about. A guard rule's entire job is to fire when the agent is thinking
about something else. "Do not escalate implementation choices to the principal"
must be present in the turn where the agent is about to escalate an
implementation choice — which is exactly the turn where the agent does not
believe it is doing that, and so will not retrieve the rule. We observed the
decay directly: rules stored only in searchable memory were re-taught by the
principal roughly every one to two weeks, and the re-teaching stopped when they
moved to the always-loaded layer.

**Cost.** A fixed token tax on every turn, paid whether or not it is needed. The
hot tier competes with task context and therefore has to be aggressively pruned;
it cannot grow. Curating it is ongoing manual work, and the pruning decisions are
themselves unprincipled — we have no measure of a rule's marginal value.

**Status.** 🟢 load-bearing. The tier split was made *after* the decay was
observed and named, and rule re-teaching by the principal dropped noticeably
after the split.

---

## 2. Memory keeps tombstones — the point is to prevent re-derivation

**Conventional.** A knowledge base stores what is true. Deleting a record means
removing it. Wrong or obsolete entries are cleaned up.

**Here.** Refuted research directions, deprecated architectures, and rejected
approaches get an explicit **gravestone entry** that is kept forever and, for the
expensive ones, promoted into the always-loaded tier. Current gravestones
include several theory directions that were pursued and abandoned, and one
infrastructure pattern that was permanently retired. They are labelled "do not
re-run," with the reason and the date.

**Why.** For an agent system, forgetting a fact is cheap — you look it up again.
The expensive failure is **re-deriving a dead conclusion**: proposing an
architecture that was already tried and abandoned, or re-running an experiment
whose negative result is already known. Nothing in a conventional store makes
absence-of-record distinguishable from never-considered, so a clean knowledge
base actively invites the loop. A deprecation is a *result*, and it costs as much
to produce as a positive one.

**Cost.** The index grows monotonically and never shrinks. Gravestones consume
scarce hot-tier budget, competing with rules that are about live behavior. And a
gravestone can be wrong: a direction dead under 2026 assumptions may be alive
under 2027 ones, so each one needs an explicit revival condition, which is extra
work and frequently omitted.

**Status.** 🟡 in production, unstressed. The gravestones exist and are loaded.
We do not have a clean measurement of how many re-derivations they prevented,
because the counterfactual is invisible — which is itself the honest problem
with this practice.

---

## 3. The publication gate judges content, never location

**Conventional.** Perimeter security. Private repository, private bucket,
internal network — the boundary is a *place*, and data inside it is safe. Review
happens when data crosses out.

**Here.** There is no safe place. Every artifact is evaluated against a fixed
content checklist immediately before publication, regardless of destination, and
"this is going to an already-cleared public repository" grants nothing. The
checklist is mechanical and closed: no private personal names or inferable
references, no financial figures or account details, no first-time public
identity commitment, destination on a pre-cleared list, reversible within an
hour.

The corollary is the part that actually earns its keep: **private material
hitchhikes.** It arrives in a commit message, in an example value that happens to
be real, in a filename, in prose that is redacted but still uniquely
identifying. A per-repository approval cannot see any of that, because it
approved the repository, not the bytes.

**Why.** The perimeter model fails silently and in the direction that matters.
Nobody reviews the commit message of a commit to an already-public repo.

**Cost.** The checklist must be evaluated per artifact and cannot be amortised.
It is only as good as its own completeness: a novel category of harm that the
checklist does not name will pass, and the gate will not notice it passed. The
false-negative rate is unmeasurable by construction.

**Status.** 🟢 load-bearing. This is the reason the surrounding repository is
publishable at all, and it has caught hitchhikers in commit messages and in
example data. The same distinction — a permission gate that is *content*-gated
rather than *act*-gated — is implemented in the runnable reference at
[`agent-continuity-demo`](https://github.com/starshard-ai/agent-continuity-demo).

---

## 4. Default is ship; the gate is a predicate list, not a question

**Conventional.** Human-in-the-loop. Anything outbound, irreversible, or public
gets an approval prompt. More sensitivity, more prompts.

**Here.** The default is **act**. Explicit permission is required only for a
short list of bright lines — private-person material, financial figures, naming
or first-time public identity commitments, creating a new public surface, legal
commitments, and anything not reversible within an hour. Everything else: run
the checklist, write a receipt, ship. When the checklist fails, the agent may not
ask a general question; it must **name the failing predicate**. "Should I post
this?" is not a permitted output. "This fails predicate (a), the example
contains a real name" is.

**Why.** An approval gate that fires on every action does not produce oversight;
it produces a rubber stamp. The principal's attention is the binding constraint
in the entire system, and a gate that consumes it on routine actions is spending
the safety budget on the cases where safety was not at issue — which leaves less
for the cases where it is. Named deferrals also make the gate *debuggable*: a
predicate that keeps firing is a signal to change the bright line, not to keep
adjudicating instances.

**Cost.** Real. A harm outside the checklist ships without anyone looking.
Reversibility-within-an-hour is doing heavy lifting and is not always true —
an artifact can be copied within the hour. And the discipline is self-referential:
it depends on the agent honestly evaluating a checklist that only the agent runs.

**Status.** 🟡 in production, unstressed. It is enforced by convention plus a
receipt requirement, not by a hard mechanism. There is a defined anti-signal — if
the deferral rate exceeds roughly 30%, the approval gate has regrown and the
policy has failed — but we have not yet had an adversarial test of the checklist
itself.

---

## 5. Escalate value decisions; decide implementation decisions

**Conventional.** When uncertain, ask. Surface options, let the human choose.
Presenting A/B/C is considered respectful of user agency.

**Here.** An explicit split between **道 (dao, ends)** and **术 (shu, means)**.
Escalate only what changes the principal's goals, time, or strategy. Decide, and
merely report, anything that only changes implementation. Which machine runs a
service, whether to keep a fallback path, which daemon, which library — all
decided by the agent, reported as an outcome, never presented as a menu.

The sharpest sub-rule: **an uncertainty of fact is not a decision to escalate.**
"Is this robust enough?" is a question the agent goes and *answers* — by testing
— and then acts on. Handing it upward disguised as a choice is a transfer of
work, not of authority.

**Why.** A menu of implementation options requires the principal to reconstruct
the technical context in order to pick, which is the exact cost the agent was
supposed to absorb. This is a category error dressed as deference.

**Cost.** The agent will sometimes decide wrong and the principal will find out
after the fact. This is accepted explicitly: the correction is cheaper than the
per-decision review would have been. It is a bad trade wherever the
implementation choice is irreversible, so those are pulled back across the line
into the bright-line set.

**Status.** 🟢 load-bearing. Adopted after a specific violation was called out,
and promoted into the always-loaded tier precisely because storing it in
searchable memory led to it decaying (see §1).

---

## 6. Iteration step size is a tuned parameter, not a fixed cadence

**Conventional.** Fixed process cadence. Sprints, ticket sizes, planning
horizons, a release train.

**Here.** How large an increment to ship is treated as a **dynamic parameter the
agent tunes**, explicitly analogous to a learning rate. Small steps in unfamiliar
territory or where the principal's intent is uncertain; larger steps after a run
of clean landings on a validated line; minimum step plus a human gate for
anything irreversible; a deliberately tiny warmup step when opening a new line.
The principal's need to redirect is treated as the **loss signal**: an overshoot
shrinks the step, a clean landing grows it.

The associated rule is: do not accumulate planning before closing a loop. Ship
the smallest increment the principal can actually *use*, observe, then size the
next step.

**Why.** A fixed cadence over-plans in novel territory (where the plan is wrong
anyway) and under-ships in familiar territory (where the plan was unnecessary).
Meanwhile "how big should this step be" is itself an implementation question, so
by §5 it must not be escalated — which forces it to become a parameter the agent
owns.

**Cost.** No predictable delivery cadence, and nothing external to compare
progress against. Step-size tuning has no principled update rule; it is currently
heuristic, which means it can oscillate.

**Status.** ⚪ written, not enforced. The policy is documented and referenced,
but no mechanism measures overshoot or adjusts anything. Whether the step size
actually tracks the loss signal is unverified.

---

## 7. A blocker must carry executed evidence, or it is not a blocker

**Conventional.** A ticket says "blocked on customer" or "waiting for
provisioning," and everyone in the system believes it. Blocked status is
self-asserted and never checked.

**Here.** Any item parked as *waiting on the principal* must carry, in the same
record, a line naming **the command that was actually run, a summary of its
output, and the date**. Without that line the tag is void: the item is downgraded
to `blocker-unverified` and may not enter the principal's queue. This is enforced
by a pre-write hook, not by discipline.

**Why.** Discipline failed, three separate times, which is why there is a hook.
A false blocker is uniquely nasty: it consumes the scarcest resource in the
system — the principal's attention and calendar — while producing **no error
anywhere**. One capability sat parked for roughly two weeks on a stated hardware
prerequisite that had in fact been satisfied weeks earlier; the real gate was a
single on-screen confirmation. A sweep of eleven parked items found three or four
falsely parked in the same way, including two "waiting for the principal to
install X" items where X had been installed for over two weeks.

**Cost.** Verification work on every park, including parks that are obviously
genuine. And the mechanism itself has a documented failure, which is the more
interesting half — see below.

**Status.** 🟢 load-bearing, *with a recorded own-goal*. The first version of the
hook also blocked on prose keywords, and it fired on a document whose entire
thesis was "there is no pending owner action here" — the regex was
negation-blind. That is worse than a missed detection, because a blocking gate
that fires on a document declaring the absence of a blocker **pressures the agent
to fabricate a blocker, or a fake evidence line, in order to get through** — the
gate manufactures the exact pathology it exists to prevent. It was demoted in v2:
the explicit-tag path blocks, the prose path only warns. The v1 author's
"zero false positives over 100 local documents" test was real and passed; the
corpus simply contained no document of the negative genre.

There is a general lesson we have not solved and have written up as an open
problem: **a safety predicate that is expensive to satisfy and cheap to fake
selects for faking.**

---

## 8. Triggers are event-driven; fixed intervals only bound staleness

**Conventional.** Cron. Poll every five minutes. Want it fresher? Poll every
minute.

**Here.** Every recurring action — sync, publish, surface, review, refresh — is
driven by **the change itself**: a filesystem watch, a queue-depth threshold, an
accumulated-delta threshold, or a named state transition. A coarse interval (say
hourly) exists only as a fail-safe to bound worst-case staleness, never as the
primary rhythm. Shortening a poll interval to fake real-time is explicitly an
anti-pattern.

**Why.** Two reasons, and the second is the one that actually drove it. First,
polling is simultaneously wasteful (most wakeups find nothing) and not
real-time (mean latency is half the interval). Second and more important: for an
*agent* fleet, every empty wakeup is a wakeup that consumes context and can
produce spurious output. Polling does not just waste CPU; it manufactures noise
in a system whose scarcest resource is attention.

**Cost.** Event primitives are platform-specific — path watches, queue
directories, filesystem notification APIs all differ — which couples the
implementation to the host, exactly against the general preference for
host-neutral services. Worse, event sources fail *silently*: a watch that stops
firing looks identical to nothing happening. The fail-safe interval exists
entirely to bound that, and it means we can never fully drop the polling path.

**Status.** 🟡 in production, unstressed. Several loops were converted. We have
not measured whether silent watch death is actually caught by the fail-safe
interval in practice.

---

## 9. Cross-device state is a semantic memory hub, not file sync

**Conventional.** Sync a directory. Share a database. Put the state in a repo
and pull.

**Here.** Agents on different devices coordinate through a **shared memory hub of
typed records** — each carrying tags, provenance (how it was derived, with what
confidence), and a stable id. The unit of exchange is a decision, a receipt, or
a superseded belief, not a file. An agent's first action in a session is to
*sync* against the hub before acting, on the assumption that a concurrent
session may have already done, or already invalidated, the work it is about to
start.

**Why.** File sync moves bytes, not the reason. A second agent picking up work
needs the rejected alternatives, the confidence, and the provenance, and none of
those survive a diff. Concurrency is the sharper reason: multiple sessions run
at once, and a watchdog restarts crashed ones, so "act on the state I remember"
is reliably wrong. Local per-project agent memory is invisible to other devices,
which makes it worse than useless for anything cross-cutting — it produces
confident, stale action.

**Cost.** A hub is a live dependency and a single point of failure, which forces
an explicit answer to "what happens when it is unreachable" (see §10). It also
concentrates: a compromise of the hub is a compromise of every agent's beliefs
at once. And the discipline of writing a record *immediately* rather than at
session end is real overhead that is easy to skip.

**Status.** 🟢 load-bearing. Production across devices. The record shapes are
published as [Fleet Coordination
Protocol](https://github.com/starshard-ai/fleet-coordination-protocol) with a
stdlib-only reference implementation.

---

## 10. Leaderless work-claims on irreversible actions, failing closed

**Conventional.** Either a distributed lock with a coordinator and a leader, or
optimistic concurrency with retry, applied uniformly. And when the lock service
is unreachable, systems generally proceed — availability wins.

**Here.** A pre-execution hook classifies the action. If it is a bright-line
**irreversible external effect** — an outbound message, a push, a deploy, a
charge — it must hold a short-lived per-key lease from the shared hub. Leases
are leaderless: for a given work key, the lowest session id wins. If the hub is
unreachable, the action is **blocked** — fail-closed. Everything else, meaning
every reversible or internal action, is not gated at all and any error inside the
hook itself **fails open**.

That asymmetry is the entire design. A duplicated reversible action costs
nothing. A duplicated irreversible one cannot be undone. So the two get opposite
failure defaults, in the same hook.

**Why.** Concretely: three concurrent sessions once sent three duplicate
messages to the same recipient, each session believing it was the only one
handling the task. Uniform optimistic concurrency does not prevent that, and a
uniform lock would have gated thousands of harmless file reads to prevent it.

**Cost.** A hub outage stops all external effects, which is a real availability
hit and, in the general case, an attack surface — anyone who can take down the
hub can silence the fleet. And we have a recorded self-inflicted failure: the
gate acquired a lease, the tool call was then denied further downstream, and the
lease was orphaned — so the session **deadlocked against itself** for the full
lease TTL. Fail-closed designs fail in ways their authors do not anticipate.

**Status.** 🟢 load-bearing, with a recorded own-goal (the self-deadlock above).
Wire format published in [FCP](https://github.com/starshard-ai/fleet-coordination-protocol);
runnable primitives in
[`agent-continuity-demo`](https://github.com/starshard-ai/agent-continuity-demo).

---

## 11. Facts about people are a bitemporal timeline, not a profile row

**Conventional.** A contact record, a CRM row, a user profile. Fields hold
current values. Updating means overwriting. Absent field means we do not have it,
which in practice gets read as "no."

**Here.** Every fact about a collaborator is an **assertion on a timeline**,
carrying `valid_from`, optionally `valid_to`, a source-kind, and a confidence.
Four consequences, each adopted after a specific failure:

- **Conflict is computed, never asserted.** The tool derives that two assertions
  overlap and disagree; an agent may not write "conflict" as a state, because an
  agent that can declare a conflict can also declare its absence.
- **Unknown is first-class and distinct from false.** A gap in the timeline is
  recorded as an explicit `unknown`, because the recurring error was reading
  "no record" as evidence of "no."
- **Retirement is supersession, not deletion.** A dead channel or expired
  capability gets `valid_to` closed and a `superseded_by` pointer. Nothing is
  removed, so a wrong retirement is recoverable and an audit can replay what was
  believed on any past date.
- **Source kind is a ladder with a ceiling.** Content from an unattributed
  transcript must be tagged as such and capped at low confidence, and cannot be
  promoted by any later step. Unverified speaker attribution never launders
  itself into a fact.

**Why.** An agent acting on a stale channel or an expired capability fails
*silently and in front of a real person*, which is the failure mode with the
highest cost and the lowest observability. Snapshots make the staleness
invisible: the row looks equally authoritative whether it was written yesterday
or in March.

**Cost.** A much heavier write path — no direct edits are permitted, everything
goes through an assertion API that holds a lock and recomputes projections. Query
complexity goes up: "what do we believe now" is a fold over a timeline rather
than a field read. And the discipline is bypassable by anyone who edits the
underlying store directly, which is forbidden but not prevented.

**Status.** 🟡 in production, unstressed. Recently adopted and materially
consequential — it immediately surfaced dead channels that a snapshot model had
been presenting as live — but it has not yet run long enough to know whether the
assertion discipline holds under time pressure.

---

## 12. Two-part receipts: intent before the act, outcome after

**Conventional.** Log after the fact. The log line is written when the operation
returns.

**Here.** For irreversible actions, an **intent receipt is written before the
action** and an outcome receipt after. The pair is the unit. A dangling intent
with no matching outcome is not a gap in the logs — it is itself the primary
alarm, and the only way to distinguish "never started" from "started and
vanished."

**Why.** Post-hoc logging cannot see the case that matters most. A process that
sends an email and then dies before logging leaves the same trace as a process
that never ran. For a fleet where sessions crash and are restarted by a watchdog,
that ambiguity is not rare — it is the normal case.

**Cost.** Two writes per action and write amplification on the hub. It also
introduces a genuine failure mode of its own: an intent receipt written for an
action that is then correctly *declined* looks identical to a crash, so declines
must be explicitly closed out or they generate false alarms. Related to the
orphaned-lease bug in §10 — the same class of mistake.

**Status.** 🟢 load-bearing. Receipt-before-irreversible-action is one of the
four published FCP primitives and is implemented in the reference demo.

---

## 13. Friction is categorically the system's defect

**Conventional.** User education. Onboarding docs. Better instructions. When
someone does not follow the flow, the flow gets a tooltip and the person gets a
reminder.

**Here.** Any instance of a human not following, not remembering, using the wrong
link, or missing a message is filed as a **system defect**, unconditionally, and
never returned to the human as their error. This is applied symmetrically to the
principal and to third parties the system serves.

The clarifying example is small and stupid, which is the point. Links sent to the
principal repeatedly arrived broken. The cause: on a phone, the tap target for a
URL greedily absorbs adjacent characters, so a URL wrapped in markdown bold
emphasis had the trailing markers swallowed into the link, producing a 404. The
conventional read is "the user tapped slightly off." The fix that actually worked
was a formatting rule — any link intended to be tapped goes **alone on its own
line, with no adjacent markup, punctuation, quotes, arrows, or emoji**, and the
status label goes on the preceding line.

**Why.** Attributing friction to the human terminates the debugging loop exactly
where the real fix is. It is also the more accurate attribution far more often
than it feels: in the cases we investigated, "they did not follow up" resolved
into "the message went to a channel they do not read," and "they used the wrong
link" resolved into a rendering bug.

**Cost.** Some genuine human errors get engineered around at real expense, and
the rule provides no stopping criterion — taken literally it justifies unbounded
work. It also removes a legitimate signal: sometimes the correct fix *is* to tell
someone the convention.

**Status.** 🟢 load-bearing. Narrowly: the link-formatting rule was adopted after
repeated real breakage and the breakage stopped. Broadly, as a general principle,
it is closer to 🟡 — we do not measure how often it is applied.

---

## What we are not claiming

- None of these are novel in isolation. Bitemporal modelling, leases,
  write-ahead intent records, and event-driven triggers are all standard
  somewhere. The claim is about the **combination and the defaults** in a
  setting where the actor is a fallible model rather than deterministic code.
- These are the practices of *one* system with *one* principal. Nothing here has
  been tested at multi-user scale, and several would probably break there —
  §4 and §5 in particular assume a single principal whose preferences the system
  can learn.
- Roughly a third of the entries above are honestly labelled 🟡 or ⚪. The
  distribution is the finding: **the mechanisms that are load-bearing are almost
  exactly the ones with an incident behind them.** Practices adopted from
  reasoning alone tend to stay decorative. That pattern is the most portable
  thing in this document.

The safety-relevant subset of these — permission envelopes, stop semantics,
fail-closed gates, verifier independence, escalation under scarce attention — is
developed as a research agenda in [Agent Safety — Open Research
Problems](OPEN-PROBLEMS-AGENT-SAFETY.md), including the parts we know are
unsolved.
