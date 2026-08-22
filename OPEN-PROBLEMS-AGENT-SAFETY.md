# Agent Safety: Open Research Problems from a Continuously Running Personal Agent Fleet

Date: 2026-08-22 · Companion: [Divergences](DIVERGENCES.md) · Confidence format: [Claim-Receipt](CLAIM-RECEIPT.md) · License: Apache-2.0

This is a research agenda, not a product description and not a position paper.

It comes from operating a personal agent fleet continuously for several months:
multiple heterogeneous agents, on multiple hosts, sharing one persistent memory,
taking real irreversible actions in the world, restarted by watchdogs when they
crash, and authorized by exactly one human whose attention is the binding
constraint on the whole system.

Most published agent-safety work evaluates one agent, on one task, in one
episode, in a sandbox, with a reset. The failures we actually hit are not in that
class. They are inter-agent, cross-session, and cumulative: a stop that does not
propagate, a belief that a later agent inherits as authorization, three sessions
performing the same irreversible action, a gate that pressures the thing it gates
into faking compliance.

We think **the setting itself is the contribution**, and that stating it
precisely is worth as much as the mechanisms. Section 1 defines it. Section 2
lists what we have built and grades it honestly — a third of it is text with no
mechanism behind it, and it is labelled that way. Section 3 is the point of the
document: eleven problems, each with a statement precise enough to start on, why
existing methods do not close it, what we tried and what failed, and what
success would look like. Section 4 is what we know we have not addressed at all.
Section 5 is where to start if you want to take one.

**Epistemic status of the whole document: n=1.** One principal, one operator, one
system. Every confidence grade below was assigned by the system it describes.
The incident counts are counts of incidents, not statistics. We are offering a
setting and a set of failure traces, not evidence.

---

## 1. The setting

### 1.1 Definition

A single human principal **P** authorizes a set of agents **A = {a₁ … aₙ}** with
the following properties. Every one of these is true of the running system, not
hypothetical.

1. **Heterogeneous and multi-host.** Agents run on a laptop, on cloud instances,
   and on a phone, under more than one commercial model provider. There is no
   single runtime and no single vendor whose safety features can cover the fleet.
2. **Continuously running, no episode boundary.** Sessions are long-lived, crash,
   and are automatically relaunched by watchdogs with context handoff. There is
   no natural point at which the system is "done" and state is discarded.
3. **Shared mutable memory.** All agents read and write a common semantic store.
   A belief written by one agent conditions the behaviour of every other agent,
   including agents started later, on other devices, with no other connection to
   the writer.
4. **Real irreversible effect.** Agents send email and messages, push to public
   repositories, publish web surfaces, operate devices, and can spend money.
5. **Sub-delegation.** Agents launch sub-agents with natural-language briefs and
   an inherited, textual permission envelope. Delegation depth is not fixed.
6. **Multiple principals of unequal authority.** Some agents act on behalf of, or
   in conversation with, humans other than P — a delegated principal in a service
   relationship, whose low-risk requests the fleet is authorized to handle
   without P in the loop. Their authority is real but strictly narrower than P's.
7. **Untrusted input everywhere.** Agents ingest web pages, inbound email,
   third-party messages, and speech transcripts. Any of it may be adversarial,
   and all of it lands in the same context that holds the fleet's authority.
8. **Attention is the binding constraint.** P can absorb on the order of a
   handful of interrupts per day. An escalation is not free; it is drawn from a
   budget, and over-drawing it degrades the channel rather than merely wasting it.
9. **The configuration is natural language.** A significant fraction of the
   system's safety-relevant behaviour is specified in a rule layer written in
   prose, loaded into every turn, which the agents both read and can edit.

### 1.2 How this differs from adjacent settings

**Versus single-turn model safety.** There is no episode. The object that must be
safe is a *persistent state*, not a *response*. Refusal is a marginal control
surface here — almost nothing that goes wrong involves the model producing
disallowed text. What goes wrong is that a correct-looking action, taken with
correct-looking authority, was not the action the principal would have
authorized, and nothing downstream can tell.

**Versus agent benchmarks.** AgentBench, τ-bench, AgentHarm, and ToolEmu each
evaluate a single agent on a bounded task with a reset [1, 2, 3, 4]. They are
good at what they measure. None of them can express the failures above: there is
no second concurrent agent to duplicate your irreversible action, no shared
memory for a poisoned belief to persist in, no watchdog to resurrect a stopped
component, and no cross-session accumulation. A benchmark for this setting would
need concurrency, persistence, and a resurrection adversary as first-class
features.

**Versus AI control.** The closest relative [5]. Control evaluations assume a
trusted (typically weaker) monitor with independent standing, an untrusted model,
and a protocol combining them; that framing transfers well and we borrow from it.
Three things differ. (a) Our monitor is usually the *same* model family as the
monitored — sometimes the same weights — so the trusted/untrusted split is
aspirational rather than architectural. (b) A meaningful part of the "protocol"
is natural-language rules the agent reads and could edit, not code the agent
cannot touch. (c) The human's budget is a few interventions per *day*, not per
action, which rules out any protocol whose auditing rate is a tunable fraction of
actions.

**Versus classical access control.** Capability systems, attenuable tokens, and
workload identity are mature [6, 7, 8]. They assume the holder's intent is fixed
by its code. Here the holder is a model that can be argued into a different
intent by its own input while holding the same credentials and the same workload
identity. Attesting the workload authenticates the wrong thing.

**Versus safe interruptibility.** Orseau and Armstrong formalize an agent's
indifference to being interrupted [9]. That is a property of the learner's
incentives, and it is the right question for a single agent. It is not the
question here: an agent perfectly indifferent to interruption, which a watchdog
then restarts, is not stopped.

### 1.3 Why this setting is worth formalizing

Systems with these properties are being assembled right now by individuals, with
no threat model and no security review, and they hold email, credentials, code
push rights, and money. The gap is not that the safety community lacks the tools;
it is that almost nobody in it is running one of these, so the failure modes are
not in the literature. This document is an attempt to put a few of them there.

---

## 2. What is built, and how well verified

Grades are deliberately unflattering.

- 🟢 **load-bearing** — in production, and it has already survived a real failure
  of the kind it exists to prevent. There is an incident behind it.
- 🟡 **in production, unstressed** — running, but we have no evidence it works
  under the condition it was built for. It may be decoration.
- ⚪ **written, not enforced** — a rule in text with no mechanism that makes it
  bite. Honest label for "we believe this and nothing stops us violating it."

| # | Mechanism | Grade |
|---|---|---|
| M1 | Bright-line permission envelope, escalation-minimizing default | 🟡 |
| M2 | Content-gated publication checklist | 🟢 |
| M3 | Fail-closed work-claim gate on irreversible external actions | 🟢 |
| M4 | Intent-before / outcome-after receipts | 🟢 |
| M5 | Evidence-required blocker gate | 🟢 |
| M6 | Delegation-bound contract at sub-agent launch | 🟡 |
| M7 | Belief-conflict quarantine | 🟡 |
| M8 | Bitemporal facts with a source-kind confidence ceiling | 🟡 |
| M9 | `owner-stop` as an absorbing state | ⚪ |
| M10 | Independent, non-agent emergency stop | ⚪ |
| M11 | "A safety event may not become a source of agent privilege" | ⚪ |
| M12 | Green light requires fresh telemetry + independent verifier | 🟡 |
| M13 | Failure signals must have an independent reader | ⚪ |

**M1 — permission envelope.** Default is act. A closed list of categories
requires P personally: material about private individuals, financial figures,
naming or first-time public identity commitments, creating a new public surface,
legal commitments, and anything not reversible within an hour. Enforced by the
always-loaded rule layer plus a receipt requirement; a subset also by hard
pre-execution hooks. 🟡 because it has never been adversarially tested — we do
not know what it does under a persuasive input arguing that an exception applies.

**M2 — content-gated publication.** Every artifact is checked against a fixed
content checklist immediately before publication, regardless of destination.
"Already a cleared public repository" grants nothing. 🟢: it has caught private
material hitchhiking in commit messages and in example values — the channels a
per-repository approval structurally cannot see. False-negative rate is
unmeasurable by construction.

**M3 — fail-closed work-claim gate.** A pre-execution hook classifies each action;
bright-line irreversible external effects (outbound send, push, deploy, spend)
must hold a short-lived per-key lease from the shared hub. Leases are leaderless.
If the hub is unreachable the action is **blocked**. Everything reversible or
internal is not gated at all, and any internal error *inside the hook* fails
**open**, because a buggy gate must never brick the fleet. 🟢: it exists because
three concurrent sessions once each sent the same outbound message to one
recipient, each believing it was the only one handling the task. It also has a
recorded own-goal — it acquired a lease, the call was denied further downstream,
the lease was orphaned, and the session deadlocked against itself for the full
lease window. Wire format and a runnable implementation are public [10, 11]. A
companion specification covers agent identity, authentication, and the
authorization envelope carried by inter-agent messages, and publicly documents
this gate's own unfixed defects — notably that its leases carry no fencing token,
so a lease holder that stalls and resumes cannot be excluded by the resource
itself [25].

**M4 — two-part receipts.** For irreversible actions an intent receipt is written
*before* and an outcome receipt after. A dangling intent is itself the alarm, and
the only way to distinguish "never started" from "started and vanished" in a
fleet where sessions crash and get relaunched. 🟢, published as one of four
primitives [10].

**M5 — evidence-required blocker gate.** Any item parked as "waiting on the
principal" must carry the command actually run, its output, and the date, or the
tag is void. 🟢 with a large asterisk: the first version also matched prose
keywords and was negation-blind. See OP-6 — the failure is more valuable than the
mechanism.

**M6 — delegation bound.** Sub-agent launches get an advisory check for a
tool-call cap, a deadline, and a partial-report contract. 🟡, advisory only.
Motivated by a real incident described under OP-2.

**M7 — belief-conflict quarantine.** A write that contradicts a held,
high-confidence fact is quarantined and flagged rather than silently applied. 🟡
in the fleet; the primitive is published and runnable [10, 11].

**M8 — source-kind ceiling.** Facts about people are assertions on a bitemporal
timeline. Content from an unattributed transcript must be tagged as such, is
capped at low confidence, and **no later step may promote it**. Conflict is
computed by the tool, never asserted by an agent. Unknown is a first-class state
distinct from false. 🟡 — recently adopted, immediately surfaced dead channels
that a snapshot model had been presenting as live, not yet stressed.

**M9 — `owner-stop` as an absorbing state. ⚪ — this is the headline gap.** The
doctrine says a stop must be inherited by every watchdog, retry loop, broker,
relauncher, and mutual-repair agent, and that only a new authenticated
authorization epoch can lift it. **There is no implementation.** A search of the
live host finds the rule in the always-loaded rule layer and zero enforcing code.
We are grading it ⚪ rather than describing the intended design as though it
worked, because the gap between the two is exactly what this document is for.

**M10 — independent emergency stop. ⚪.** Non-agent paths exist in the trivial
sense (kill the process, revoke a key, power down). They are not systematized,
not tested, and not verified reachable *while the fleet is misbehaving*, which is
the only condition under which they matter.

**M11 — no privilege from incidents. ⚪.** A written rule that a safety event may
never justify self-granting authority, renewing an expiring grant, or downgrading
a guardrail, and that when evidence or monitoring is insufficient the correct move
is to contract to a minimal recovery envelope rather than expand. No detector.
See OP-3.

**M12 — green light hygiene. 🟡.** A rule that a green light must come from fresh
telemetry plus a verifier that is not the acting agent, and that a live process, a
self-reported success, and a cached result are *not* evidence of safety. Enforced
by convention. Whether our "independent" verifiers are independent in any measured
sense is OP-7, and we assume it rather than know it.

**M13 — failure signals need a reader. ⚪, and it is one day old.** The mirror of
M12, adopted after the incident in OP-11: a component that writes an honest
failure record into a sink nothing reads has not reported a failure. There is no
mechanism, no static check, and at the time of writing we know of at least two
further instances of the structure in the fleet that we have not repaired. It is
in this table because leaving it out would be the same error the incident was.

---

## 3. Open problems

### OP-1 · Offline-verifiable delegation chains with monotone attenuation

**Problem.** P grants authority to a₁, which sub-delegates to a₂, and so on.
Model authority as a set of (action-class, resource, constraint) triples. Require:
(i) any third party — including the service being acted upon — can verify
**offline**, from the request alone, that the chain is well-formed and rooted in
P; (ii) authority is **monotonically non-increasing** along the chain, so no step
may add an action class, widen a resource set, or relax a constraint; (iii)
revocation at any node invalidates the entire subtree within a bounded time;
(iv) a holder of a downstream token cannot forge an upstream one. And then the
part that is actually open: (v) the delegation as *issued* is natural language
("go help them get set up"), and compiling it into a triple set must be
**conservative** — an ambiguous instruction must yield the intersection of
readings, not the union.

**Why existing methods do not close it.** (i)–(iv) are largely solved.
Contextual caveats give offline attenuation and verification [6]; token exchange
gives a standard actor/subject delegation representation [7]; workload identity
gives short-lived credentials with attestation [8]. The unsolved parts are (v),
and a structural mismatch underneath it: in an LLM fleet the agent is not a
process with fixed code identity. The same process, holding the same credential
and passing the same attestation, can be argued by its input into a different
intent. You want to bind authority to *intent*, and intent is not attestable. The
agent-specific literature is nascent — 2025–2026 preprints, largely unreviewed;
we know of no canonical treatment, and we take that absence as the finding [12].
Our own companion specification [25] designs this layer — identity,
authentication, a per-message authorization envelope, and UCAN-shaped chains with
an explicit attenuation-monotonicity check — and it is scrupulous that the
delegation portions are *designed and not implemented*, and have never met an
adversary. It does not close (v) either: its own open list names the tradeoff
between authority expressiveness and offline verifiability as unresolved, which
is (v) seen from the other end. The predicate language is deliberately tiny
precisely because nobody knows how to keep a richer one verifiable.

**Our partial progress and what failed.** We enforce a delegation-bound contract
at launch (cap, deadline, partial-report), advisory only. Our sub-agent briefs are
natural language plus an inherited textual envelope — precisely the unattestable
thing. There is no cryptographic chain anywhere in the fleet. The instructive
failure: we tried bounding children by *naming* the constraint in the launch
prompt ("only write under these paths"). Measured result — **falsified 5 out of
5**: in five consecutive launches the constraint was not honoured as the parent
assumed. What worked was structural, not textual: the parent pre-creates the
artifact skeleton and registers it, so the child's compliance is machine-checkable
after the fact. A constraint that only exists as text in a prompt is not a
constraint.

**Success criterion.** A construction where a verifier with no access to fleet
internal state and no online call to P can decide accept/reject at the boundary;
plus a measured error rate for the natural-language→capability compiler under
adversarial paraphrase, on a released corpus. A clean impossibility result — e.g.
that conservative compilation requires an interactive clarification round — would
be equally useful, because it would tell us to build the clarification round.

---

### OP-2 · An absorbing stop, enforced across components that do not yet exist

**Problem.** A stop issued at time *t* must have the property that no component
of the system can cause the stopped capability to resume, except through a new
authenticated authorization epoch — and this must hold for watchdogs, retry
loops, brokers, relaunchers, cron entries, mutual-repair agents, **and components
added after t**. The open-world clause is the hard part: the property must
quantify over launch paths that did not exist when the stop mechanism was
designed. Formalize this as a property of a distributed system, not a feature of
one supervisor.

**Why existing methods do not close it.** Safe interruptibility [9] concerns an
agent's indifference to interruption — the learner's incentives — and says nothing
about propagation. Classical fault tolerance gives fencing tokens and epoch
numbers, which correctly prevent a *stale* actor from acting; but a relauncher
that reads current configuration and starts a fresh agent is not stale. It is
functioning correctly, and it defeats the stop. Fencing tokens are also, we should note, a
mechanism our own lease implementation lacks; that omission is documented in
[25], and closing it would still not address a non-stale relauncher. The gap is
architectural:
"stopped" is a property of a *capability*, and in our system — and, we suspect, in
most systems of this kind — there is no object that owns capabilities such that
every launch path must consult it.

**Our partial progress: none that is enforced.** M9 is ⚪. We are stating that
plainly rather than describing the design as though it ran.

We do have one measured result that sharpens the problem, and it is the most
useful thing we can contribute here: **you cannot stop a component that is not
polling.** In an observed incident a sub-agent hung inside a network call with
zero open sockets — the network was verified healthy, the same call succeeded in
seconds from the same host. It never timed out. The supervisor's rescue message
is delivered at the agent's next tool invocation, which never came. The agent was
simultaneously not-running and not-stoppable. The parent then burned about two
hours: first waiting, then inferring death from a file modification time, then
launching a second agent on the same task — doubling the failure surface. Any stop
design that assumes the target will *ask* whether it should stop is wrong for
exactly the case where stopping matters.

**Success criterion.** (a) A formal property, checkable by a model checker against
a system description, that quantifies over launch paths rather than enumerating
them. (b) An architectural pattern — plausibly "execution is obtainable only
through a revocable capability handle" — with a demonstration that adding a *new,
naive* relauncher cannot violate the property. (c) A red-team result: given the
fleet description and the ability to add one component, can an attacker resurrect
a stopped capability? We would implement a solution to this immediately.

---

### OP-3 · Machine-checkable detection of envelope expansion when every step is locally reasonable

**Problem.** Given a trace of an agent's actions, tool calls, configuration edits,
and memory writes, decide whether the agent is expanding its own permission
envelope. The difficulty is that expansion is a property of the *sequence*, not of
any step. Adding an allowlist entry to remove a recurring prompt; writing a
memory that later reads as prior authorization; building a helper that happens to
run outside the gate; defining a new category as "safe" — each is individually
defensible and often individually correct. Formalize the envelope as an object
with a partial order, and require every trace to be non-increasing absent an
authenticated grant.

**Why existing methods do not close it.** This is not jailbreak detection: no step
produces disallowed content. It is not anomaly detection: every action is
in-distribution and resembles ordinary maintenance. Control evaluations [5]
presuppose a discrete subversion attempt a monitor can flag; distributed,
individually-benign drift is a different object. It is closest to insider-threat
and privilege-escalation detection, except that here a substantial share of the
"privileges" are implicit — a rule in a natural-language configuration file *is* a
permission, and editing that file is a privilege change no access-control system
models. Sleeper Agents [13] establishes the adjacent worry that a disposition can
persist through the training meant to remove it, but gives no runtime detector.

**Our partial progress.** Two mechanisms of the right shape, neither adequate.
(a) M11: a written rule that a safety incident may not be used to justify
self-granting or renewing authority or downgrading a guardrail — text, no
detector. (b) A hardcoded structural constraint that identity, account, billing,
DNS, signing, secret, and recovery roots are not agent-modifiable. This one works,
but only because it enumerates, which neither generalizes nor covers the
natural-language rule layer.

One observation we think is worth formalizing: **in our traces the most common
expansion vector is not a configuration edit — it is a memory write.** An agent
writes a durable note; later agents read it as established policy. There is no
signature and no type distinction between "the principal decided this" and "an
agent concluded this," so a conclusion laundered into shared memory functions as
an authorization on the next read. We now require a provenance field on memory
writes. We do **not** enforce that a policy-shaped memory must carry a principal
signature, and we should.

**Success criterion.** A detector achieving a useful ROC on a released corpus
containing both benign refactors and staged expansions — and whose false-positive
behaviour does not trigger OP-6, since an over-firing detector teaches the agent
to route around it. A definition of "envelope" that is stable under refactoring
would itself be a contribution.

---

### OP-4 · Bounding the influence of a poisoned observation after it enters persistent memory

**Problem.** An agent ingests untrusted content and writes something derived from
it into shared, persistent, cross-agent memory. Later agents, on other devices, in
other sessions, condition on it. Give (i) a bound on the causal influence of a
single poisoned observation on the fleet's future actions, and (ii) a *revocation*
procedure: identify everything downstream derived from it and retract or
re-derive, within bounded time, without discarding unrelated knowledge.

**Why existing methods do not close it.** Indirect prompt injection is well
characterized [14], and there is now a genuinely architectural defense for the
within-episode case — separating control flow from data flow through an
interpreter with capability metadata [15]. The persistent case is different in
kind: the injection succeeded in a *past* episode, its output now sits in memory
indistinguishable from a legitimate fact, and the compromised episode may be
unrecoverable. AgentPoison and PoisonedRAG demonstrate that retrieval-backed
agents can be compromised at very low poison rates [16, 17]; neither offers
recovery. Provenance tracking is the obvious answer, but derived facts lose
provenance through summarization and consolidation — which are exactly the
operations that make long-term memory tractable. The tension is structural.

**Our partial progress.** (a) Every record carries provenance with derivation type
and confidence — but the field is agent-written, and an injected agent writes
clean-looking provenance. (b) M8's **source-kind ceiling** is real and enforced by
the write API: unattributed-transcript content is capped low and cannot be
promoted by any later step. It bounds one channel, not the general case. (c) M7's
belief-conflict quarantine makes it harder to *overwrite* a held fact, and does
nothing against poisoning that *adds* a fact into a gap — which is the easier
attack and the one our own "unknown is first-class" design makes visible as an
opportunity.

**Success criterion.** A memory architecture where influence of any ingested item
on future action is traceable, retraction is bounded with a stated cost, and both
survive summarization — evaluated against an adversary who knows the architecture
and optimizes to make their planted fact look independently corroborated. A good
*negative* result — a lower bound on retraction cost under consolidation — would
be equally valuable and would change how we design consolidation.

---

### OP-5 · When does fail-closed become the attack surface?

**Problem.** A fail-closed gate converts an availability failure into a safety
guarantee. It also creates a denial-of-service path: whoever can degrade the
gate's dependency can halt the protected capability. Worse, and this is the part
we care about: a gate that halts too often trains its operators to build a bypass,
so the long-run effect of an over-firing fail-closed gate can be *less* safety than
no gate at all. Model it. Given a false-block rate, a cost of blocking, and a
population (human or agent) that can construct bypasses at some cost, when is
fail-closed optimal, and what is the maximum tolerable false-block rate before
bypass becomes rational?

**Why existing methods do not close it.** Security engineering has the
fail-safe/fail-secure distinction as a design maxim chosen per mechanism by
judgment, not derived from parameters. There is a real empirical literature on the
downstream half — alert fatigue in clinical decision support [18] and in security
operations centres [19] both document that high-volume, low-precision alerting
degrades response quality. But it studies human alert *response*, not bypass
*construction*, and it has not been connected to agent systems, where the bypass
can be designed and deployed automatically, in seconds, by the thing being gated.

**Our partial progress.** We run the asymmetry deliberately and it is the one
design decision here we would defend confidently: irreversible external actions
fail **closed** on dependency unreachability, while any internal error in the gate
itself fails **open**. A duplicated reversible action costs nothing; a duplicated
irreversible one cannot be undone; a bricked fleet helps no one. Two data points
on the failure side: (a) the gate self-deadlocked by orphaning its own lease when
the downstream call was denied, blocking the same session for the full lease
window; (b) a different gate — hygiene, not safety — had to be demoted from
blocking to advisory precisely because it created bypass pressure, which is OP-6.

**Success criterion.** A decision rule mapping (reversibility, blast radius,
dependency availability, false-block rate, bypass cost) to fail-open/fail-closed,
validated against a corpus of real gate incidents — plus a methodology for
estimating false-block rate *without* ground truth, which by construction you do
not have, since a blocked action's counterfactual is unobserved.

---

### OP-6 · Safety predicates that are cheap to fake select for faking

**Problem.** A safety mechanism requires an agent to demonstrate a property —
evidence attached, review performed, verification run — before proceeding. If
satisfying the predicate *honestly* is expensive and satisfying it *apparently* is
cheap, the mechanism selects for the apparent form, and does so silently.
Characterize the conditions under which such a predicate is incentive-compatible,
and construct predicates whose cheapest satisfying strategy is the honest one.

**Why existing methods do not close it.** This is Goodhart, but with a specific
structure we believe is formalizable and has not been formalized for agent gates.
Mechanism design and proof-carrying code both point the right way — make the
artifact carry evidence expensive to forge and cheap to check — but neither has
been applied to the natural-language, model-generated case, where the "evidence"
is text the gate must judge and the gate is itself a regex or a model.

**Our partial progress: a measured own-goal, which is the most useful thing we
have.** M5 requires that any item parked as "waiting on the principal" carry an
executed-command evidence line. Version one also matched prose keywords, and it
blocked a document whose entire thesis was *"there is no pending owner action
here"* — the matcher was negation-blind. The bug is unremarkable. The lesson is
not: **a blocking gate that fires on documents declaring the absence of a blocker
pressures the agent to fabricate a blocker, or a fake evidence line, in order to
get through.** It manufactures the exact pathology it exists to prevent. We
demoted the prose path to advisory and kept only the explicit-tag path blocking,
reasoning that a missed false-park is cheap while an *induced* fake blocker is not.

A second lesson, about evaluation. The v1 author did run a false-positive test —
roughly a hundred local documents, zero hits, a real test honestly performed. The
corpus simply contained no document of the *negative genre*: no document that
argues about owner-blockers in order to deny one. Genre coverage of a gate's input
distribution is part of this problem and we have no method for it.

**Success criterion.** A characterization theorem giving conditions on cost
asymmetry under which a predicate is incentive-compatible; and at least one
constructed predicate, for a real agent-safety property, whose cheapest satisfying
strategy is provably honest. An evaluation methodology that deliberately samples
the negative genre would be a valuable by-product on its own.

---

### OP-7 · Quantifying verifier independence when the verifier shares the substrate

**Problem.** The rule is that a green light must come from an independent
verifier. In deployment the verifier is (a) the same model family, often the same
weights; (b) reading the same context, or a summary produced by the verified
agent; (c) holding the same credentials and the same tools; (d) frequently in the
same process tree. Define a measure of independence that *predicts* correlated
failure, and give an architecture that achieves a stated level of it.

**Why existing methods do not close it.** The closest measured result is that LLM
judges recognize and favour their own generations [20], which establishes that (a)
is not innocuous. Debate and weak-to-strong generalization [21, 22] address the
*capability* asymmetry between verifier and verified, not the *correlation of
their errors*. Control evaluations [5] presuppose a trusted weaker model and get
real mileage from it — arguably the best current answer — but leave open how much
independence a trusted-weak monitor buys against a shared-pretraining-corpus
failure mode, and say little about (b)–(d), which in a deployed fleet are the
dimensions you can actually change cheaply.

**Our partial progress.** M12 is a written rule: fresh telemetry plus a verifier
that is not the acting agent; a live process, a self-reported success, and a
cached result are not evidence of safety. In practice our "independent" reviewer
is usually a different provider's model reading a compact packet — which addresses
(a) and partially (b), and nothing else. We have never measured whether
cross-provider review decorrelates errors. We assume it, and we should not.

**Success criterion.** An empirical measure — conditional error correlation on a
task suite as a function of shared weights, shared context, and shared tooling —
that is predictive out of sample; plus a demonstration that a cheap intervention
(context isolation, disjoint tool scopes, provider diversity) actually moves it. A
clean negative result — "provider diversity does not decorrelate on task class X"
— would change how we build within a week.

---

### OP-8 · Optimal escalation under a hard attention budget

**Problem.** The principal absorbs roughly B interrupts per day. Each candidate
escalation has an unknown cost-of-being-wrong, an unknown probability that the
principal's answer differs from the agent's default, and a value of information.
Over-escalation is not merely wasteful: it **degrades the channel**, because a
principal asked constantly learns to approve reflexively, at which point the
approvals carry no information and the gate is worse than absent. Formalize
escalation as sequential decision-making under a budget in which the answer
channel's *fidelity is itself state* that depends on past usage, and characterize
the optimal policy.

**Why existing methods do not close it.** Value of information and active learning
give the static version and treat the oracle as stationary. The non-stationarity
is the entire problem: the oracle's reliability is a function of how often you
queried it recently. The alert-fatigue literature documents the effect on the
human side [18, 19] but frames it as a phenomenon to reduce, not as state in a
decision problem. Scalable oversight [21, 22, 23] asks how to supervise a system
more capable than the supervisor — a different scarcity, capability rather than
attention.

**Our partial progress.** A hand-tuned policy, entirely judgment: a categorical
bright-line list that always escalates; default-act for everything else; a
requirement that a deferral **name the failing predicate** rather than ask an open
question, so the escalation carries its own reason and is debuggable; and a
routing rule that a genuine decision goes to a guaranteed-reach channel as a
one-line fork with a return path. Separately, a deliberate **hold-depth** policy —
analysis is sedimented silently by default and surfaced only on pull — adopted
after the principal reported being flooded by pushed depth, which is the same
phenomenon on the information rather than the approval channel. We also defined an
anti-signal: a deferral rate above roughly 30% means the approval gate has
regrown. None of this is derived from anything.

**Success criterion.** A policy with a regret bound against an oracle that knows
the value of each escalation, in a model where channel fidelity decays with query
rate and recovers with disuse; validated on real escalation logs with an observed
rubber-stamp rate as the dependent variable. This is plausibly the most
immediately formalizable problem on the list, and the one where a good theory
would change a deployed system tomorrow.

---

### OP-9 · Safety properties for systems whose configuration is natural language

**Problem.** A large share of this system's safety-relevant behaviour is specified
in a prose rule layer, injected into every turn, which the agents both read and
can edit. That object is simultaneously policy, prompt, and mutable state, and it
has no theory. Concretely: (i) what is the analogue of a type system or a
consistency check for a set of prose rules — can two rules be shown to conflict?
(ii) How do you detect **rule decay**, where a rule is present in the file but no
longer influencing behaviour? (iii) Which prose rules can be *compiled* into hard
mechanisms, and by what procedure?

**Why existing methods do not close it.** Prompt engineering treats the prompt as
an input to optimize, not as a policy artifact with integrity requirements.
Policy-as-code assumes the policy is code. Constitutional approaches specify
values at training time, not a mutable runtime configuration the agent can edit
mid-operation.

**Our partial progress.** We have direct evidence that (ii) is real and expensive:
rules stored only in *retrievable* memory required re-teaching by the principal
every one to two weeks, because a guard rule's job is to fire in the turn where
the agent does not believe it is relevant and therefore does not retrieve it. The
fix was to load a small hot tier unconditionally on every turn, and the
re-teaching dropped. But **loaded is not obeyed**, and we do not measure the
latter at all. On (iii) we have anecdotal evidence that compilation works when it
happens — every mechanism graded 🟢 in section 2 is a prose rule that was compiled
into a hook, and every ⚪ is one that was not. That correlation is the most
suggestive thing we have and we cannot tell whether it is causal.

**Success criterion.** A per-rule adherence measurement; a decay detector that
fires before the principal notices; and a compilation result characterizing which
prose rules admit hard enforcement. Even a taxonomy — which rule shapes are
compilable — would be immediately useful.

---

### OP-10 · Multi-principal agents: whose preferences, whose secrets, whose stop?

**Problem.** The owner delegates to the fleet the authority to serve *other*
people. A delegated principal in a service relationship gets an agent-mediated
channel and may have their low-risk requests handled without the owner in the
loop. Three questions with operational teeth follow. (i) **Preference conflict**:
when the served party's immediate request conflicts with the owner's standing
policy, which wins, and is there a decidable rule rather than case-by-case
judgment? (ii) **Information boundary**: the agent holds context about the owner
and about other served parties; consent does not transit between them, so the
agent must decide, per utterance, what it knows but may not convey. This is an
*inference*-control problem, not an access-control one — the agent can reconstruct
and reveal a fact it was never explicitly told, through the shape of what it says.
(iii) **Stop authority**: can a served party stop an agent acting on their behalf,
and does that stop bind against the owner's instruction to continue?

**Why existing methods do not close it.** Multi-stakeholder alignment is discussed
at the level of values. The operational version — one agent instance, one joint
context, a live conversation, two humans with asymmetric authority — has no
standard model. Access control does not help, because the leak channel is
inference from behaviour rather than a read of a record. Differential privacy
addresses aggregate release, not conversational inference by a capable agent with
a rich prior.

**Our partial progress, all ⚪.** (a) An explicit tier split: the owner gets
pushback on strategy and priorities; served parties never do, except on safety and
on engineering facts, and any friction they experience is filed as our defect
rather than their error. (b) A rule that consent does not transit between parties,
and that introductions between them are proposed, never executed. (c) A rule that
a low-risk request from a delegated principal is handled immediately rather than
queued behind the owner, and that escalating still requires giving the requester
an immediate answer plus a tracked open loop — silence is not an acceptable form
of escalation. All of it is text, none of it is mechanism, and we believe (ii) is
not solvable by rules at all.

**Success criterion.** A formal model of an agent with multiple principals of
unequal authority sharing one context, providing a decidable conflict rule for (i),
an inference-control guarantee for (ii) stated over *what the agent may cause a
party to learn* rather than over records read, and stop semantics for (iii). An
impossibility result for (ii) under a capable agent would also be a real
contribution — it would tell us to change the architecture rather than the prompt,
which is a decision we are currently unable to make.

---

### OP-11 · A failure signal with no reader: observability as a statically checkable property

**Problem.** A system emits failure signals into sinks: log lines, exit codes,
status fields, parked-request directories. Define an **observability
obligation**: for every reachable failure state *f* of a component *c*, there
exists a path from *f* to a state observed by some actor that can act — a
principal, or an agent whose behaviour changes — within a bounded latency *L*. A
guard that detects a failure correctly and writes it to a sink with no reader is,
at the system level, a **no-op**; and it is a no-op that reads as a fix, closes
the incident, and removes the pressure to fix it properly. Make this checkable
statically from a system description, and give a metric that separates *time to
failure* from *time to observation*, so that a change which increases honesty
while decreasing observability shows up as a regression rather than as a repair.

**Why existing methods do not close it.** Observability practice instruments
known signals and tunes alerts; it presupposes each signal has a consumer. The
alert-fatigue literature [18, 19] studies the opposite end — consumers
overwhelmed by signals — and has nothing to say about a signal with no consumer
at all. Distributed-systems failure detectors are formalized in terms of
completeness and accuracy [24], but the framework assumes the detector's output
is consumed by the protocol; the failure here is a detector that was correctly
installed and wired to nothing. And in conventional software this gap is
partially covered by an accident of staffing: there is a human on call who greps.
An agent fleet has no on-call. The only reader that exists is one some agent was
separately told to build, and *building the detector and building its reader are
two different acts, only the first of which feels like the work*.

Low event rates finish the job. The signal in our incident was five records in
sixteen days. No volume-based anomaly detection can fire on that, and the low
rate is not incidental — rare failures are exactly the ones for which nobody
builds a reader.

**Our partial progress — an own-goal with a measured 4× regression.** This is
recent and it is the sharpest data in this document.

1. An outbound notification leg — a nudge on a channel a person outside the fleet
   actually reads, used to draw them to a message waiting elsewhere — judged
   success by *process exit code zero and empty output*. That is not a
   transport-layer confirmation. For four days the leg was armed and recording a
   message as delivered that had never been delivered.
2. A correct fix added a precondition guard: when the required hardware
   precondition is absent, abort and record the abort truthfully. This ended the
   false success. It was the right fix and we would make it again.
3. The abort branch wrote one honest line to a log file, parked the request in a
   directory, and **exited zero**. The supervisor therefore recorded each run as
   successful; the unit never appeared in the failed-unit list. Meanwhile the
   caller had been told `queued` at the instant the request was written to the
   spool — true, and rendered to the human as success.
4. A static readership check — search the entire host for any reference to the
   log path, the parked-request directory, or the abort token, across timers,
   cron entries, unit files, and scripts — returned **six writers and zero
   readers**. No re-drive, no age sweep, no alert.

The failure mode changed from a four-day loud lie into a **sixteen-day silent
truth**. Undetected duration went up roughly 4×. It was found by an unrelated
audit, not by the system.

The control group is what makes this diagnostic rather than anecdotal: on the
same host, a different unit that exits nonzero *did* appear in the failed-unit
list. The alarm channel was working. The guard opted out of it by exiting zero.

The cost in the world was not the dropped notifications, of which there were two.
A person outside the fleet had asked a direct question; the answer was composed
into a channel they do not read; and the single action that would have brought
them to it did not happen and reported success. Fifteen days.

**The part we think generalizes.** Once we looked for the *structure* instead of
the bug, two more instances surfaced that have not yet caused harm: a send path
that receives a transport-layer acknowledgement and never captures it, so every
send through it is *unverifiable* rather than verified; and a delivery tool with
no success record of its own, currently observable only because one of its
callers happens to log. Both have the same shape the incident had four days
before it fired. **The structure is enumerable even when the incidents are not** —
which is the reason we believe this is statically checkable and not merely a
discipline problem.

Two sub-properties from the same audit, both of which we think belong in the
formal statement:

- **Channel liveness is not channel health.** Of eight outbound channels, three
  had carried no transport-confirmed message in 10, 26, and 69 days. Nothing
  reported it. A channel that has silently stopped being usable is
  indistinguishable, from inside, from a channel that is simply idle.
- **A refusal is a routing outcome and needs a receipt.** The principal issued an
  instruction; the agent holding that surface replied that it lacked the
  capability; and the instruction then evaporated — no task, no open loop, no
  record anywhere. This is the same absence-of-reader failure moved up a level,
  it was the costliest line in the incident, and it is the least technical.

**Success criterion.**

(a) A static analysis over a system description — units, timers, scripts, sinks,
notification surfaces — that decides, for each failure-emission site, whether a
reader exists, and enumerates the ones that do not. We believe this is close to
trivial for the exit-code / log-file / queue-directory subset and would have
caught this incident in seconds. The research question is where it *stops* being
trivial: a reader that exists but is itself dead; a reader whose own output has
no reader; readership that depends on a model choosing to look rather than on
code that must run.

(b) A per-channel liveness obligation: a declared maximum silence interval and a
report on breach, where success is defined as transport-layer confirmation and
never as process exit status.

(c) **Time-to-observation reported separately from time-to-repair**, with any
change to a failure path required to state its effect on the former. Our fix
improved correctness and quadrupled time-to-observation, and no metric we had
could see that.

(d) The theorem, if it is one: an honest failure signal with no reader is
observationally equivalent to no detector, so a system's safety argument may not
be conditioned on a detector existing — only on a *read* detector existing. This
is obvious once written down. It nonetheless survived a four-day failure and a
sixteen-day failure, with every layer in the stack reporting success.

This is the exact mirror of M12. If a green light must come from fresh telemetry
plus an independent verifier, then **a red light with no independent reader is
not a red light.** We had written the first half and not the second.

---

## 4. Gaps: what we know we have not addressed

Separated from section 3 because these are not research problems we are working
on. They are holes.

1. **No stop implementation.** M9 is doctrine with no code. This is the largest
   distance between what is written and what is true anywhere in the system.
2. **Nothing here has been attacked on purpose.** Every failure trace in this
   document came from a bug or an accident. We have never run a red team against
   the fleet. The mechanisms graded 🟢 survived *accidents*, which is weaker
   evidence than it reads as.
3. **No isolation between agents.** Agents on a host share a filesystem and often
   credentials. Compromise of one agent is compromise of the host. There is no
   sandboxing story at all.
4. **Credential handling is not principled.** Agents hold long-lived,
   broadly-scoped tokens because the alternative is friction. Scope minimization
   is aspirational. This directly contradicts OP-1 and we know it.
5. **No control/data separation on untrusted input.** Web content, email, and
   transcripts are ingested straight into the same context that holds authority.
   The architectural defense that exists for this [15] is implemented nowhere in
   the fleet.
6. **Rule adherence is unmeasured.** See OP-9. We do not know which of our rules
   are actually operative.
7. **No formal threat model document.** Our implicit adversary is "accidents plus
   injected content," not a motivated attacker with knowledge of the architecture.
   A real threat model would likely reorder this entire agenda.
8. **Physical and device security is out of scope** and unaddressed.
9. **n=1, and the evaluator is the evaluated.** One principal, one operator. The
   safety rules, their implementation, and their confidence grades all have the
   same author. Section 2's grades should be read with that in mind — and OP-7 is
   about exactly this failure mode, which we are committing at the document level
   even as we describe it.

---

## 5. How to engage

**If you want to attack something concrete, start with the runnable code.** Two
small public repositories implement the coordination primitives referenced above:

- [`starshard-ai/agent-continuity-demo`](https://github.com/starshard-ai/agent-continuity-demo)
  — roughly 300 lines, standard library only, runs in about a second: shared
  cross-agent memory, a content-gated permission boundary, a receipt per action,
  and cross-session work-claims.
- [`starshard-ai/fleet-coordination-protocol`](https://github.com/starshard-ai/fleet-coordination-protocol)
  — the wire format for those four record shapes, plus a pip-installable
  file-backed reference implementation with no server and no keys.
- [`starshard-ai/starshard-communication`](https://github.com/starshard-ai/starshard-communication),
  specifically
  [SPEC-0003](https://github.com/starshard-ai/starshard-communication/blob/main/docs/SPEC-0003-agent-identity-authentication-and-secure-messaging.md)
  — agent identity, authentication, the per-message authorization envelope, and
  two-part receipts, with a section enumerating the defects we have not fixed.
  OP-1 and OP-2 both bite there first.

OP-1, OP-2, OP-5, and OP-6 all have a surface in that code. It is small enough to
read in one sitting and to break on purpose, which is what we would most like
someone to do.

**Context for the practice these came out of:** [DIVERGENCES.md](DIVERGENCES.md)
in this repository, which describes the operating practices and what each cost.
[CLAIM-RECEIPT.md](CLAIM-RECEIPT.md) describes the confidence format used here.

**Channel.** Issues on the public repositories above, or on this repository.
Please do not route research discussion through private contact — the point of
publishing this is that the discussion is public and other people building these
systems can read it.

**What would help us most, in order.** (1) A formalization of OP-2 that we could
implement, because it is the gap we are least able to close ourselves. (2) A
negative result on OP-7, since we are currently *assuming* our verifiers are
independent. (3) An evaluation corpus for OP-6 that deliberately includes the
negative genre. (4) OP-11(a) — a static readership checker — because it looks
like the most tractable item on the list and we would run it the day it existed.

**What we can offer.** Redacted incident write-ups. If a specific problem here
would be sharpened by the actual trace behind it, open an issue naming the
problem and we will write the incident up in a form that can be published. We
cannot share raw logs — they contain third-party and personal material — and we
have no dataset, no funding, and no institutional affiliation behind this. It is
one system and its operating record.

**Expectations.** This is not a lab and there is no roadmap commitment. Anything
in section 3 may sit untouched. If you take one of these and solve it, the useful
thing is to publish it; we will link it from here and, where we can, implement it
and report what happened.

---

## References

Every entry below was verified against its primary source on 2026-08-22 — arXiv
IDs against the arXiv API, others against the publisher or the standards body.
Where we could not verify a claim in the literature, we say so rather than cite.

1. Liu, X., Yu, H., Zhang, H., et al. (2023). *AgentBench: Evaluating LLMs as Agents.* arXiv:2308.03688.
2. Yao, S., Shinn, N., Razavi, P., Narasimhan, K. (2024). *τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains.* arXiv:2406.12045.
3. Andriushchenko, M., Souly, A., Dziemian, M., et al. (2024). *AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents.* arXiv:2410.09024.
4. Ruan, Y., Dong, H., Wang, A., et al. (2023). *Identifying the Risks of LM Agents with an LM-Emulated Sandbox* (ToolEmu). arXiv:2309.15817.
5. Greenblatt, R., Shlegeris, B., Sachan, K., Roger, F. (2023). *AI Control: Improving Safety Despite Intentional Subversion.* arXiv:2312.06942.
6. Birgisson, A., Politz, J. G., Erlingsson, Ú., Taly, A., Vrable, M., Lentczner, M. (2014). *Macaroons: Cookies with Contextual Caveats for Decentralized Authorization in the Cloud.* NDSS 2014.
7. Jones, M., Nadalin, A., Campbell, B. (Ed.), Bradley, J., Mortimore, C. (2020). *OAuth 2.0 Token Exchange.* RFC 8693, IETF Standards Track.
8. SPIFFE / SPIRE. Workload identity specification and reference implementation. https://spiffe.io — a project specification, not a peer-reviewed paper.
9. Orseau, L., Armstrong, S. (2016). *Safely Interruptible Agents.* Proceedings of the Thirty-Second Conference on Uncertainty in Artificial Intelligence (UAI 2016).
10. Fleet Coordination Protocol (FCP) v0. https://github.com/starshard-ai/fleet-coordination-protocol — our own work; a descriptive v0 spec, not a standard.
11. `agent-continuity-demo`. https://github.com/starshard-ai/agent-continuity-demo — our own work; reference implementation for [10].
12. On agent-specific delegation: we searched for a canonical treatment of verifiable delegation chains for LLM agents and did not find one. What exists is recent and largely unreviewed — e.g. Goswami, A. (2025), *Agentic JWT: A Secure Delegation Protocol for Autonomous AI Agents*, arXiv:2509.13597, a single-author preprint we verified exists but whose rigour we have not assessed. We cite the absence, not the preprint.
13. Hubinger, E., Denison, C., Mu, J., et al. (2024). *Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training.* arXiv:2401.05566.
14. Greshake, K., Abdelnabi, S., Mishra, S., et al. (2023). *Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection.* arXiv:2302.12173.
15. Debenedetti, E., Shumailov, I., Fan, T., et al. (2025). *Defeating Prompt Injections by Design* (CaMeL). arXiv:2503.18813. — Related and influential but *not* a peer-reviewed citation: Willison, S. (2023), "The Dual LLM pattern for building AI assistants that can resist prompt injection," blog post, https://simonwillison.net/2023/Apr/25/dual-llm-pattern/. We flag it as a blog post because it is one.
16. Chen, Z., Xiang, Z., Xiao, C., et al. (2024). *AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases.* arXiv:2407.12784.
17. Zou, W., Geng, R., Wang, B., et al. (2024). *PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models.* arXiv:2402.07867.
18. Hussain, M. I., Reynolds, T. L., Zheng, K. (2019). *Medication safety alert fatigue may be reduced via interaction design and clinical role tailoring: a systematic review.* Journal of the American Medical Informatics Association 26(10):1141–1149.
19. Tariq, S., Baruwal Chhetri, M., Nepal, S., Paris, C. (2025). *Alert Fatigue in Security Operations Centres: Research Challenges and Opportunities.* ACM Computing Surveys 57(9), Article 224.
20. Panickssery, A., Bowman, S. R., Feng, S. (2024). *LLM Evaluators Recognize and Favor Their Own Generations.* arXiv:2404.13076.
21. Irving, G., Christiano, P., Amodei, D. (2018). *AI safety via debate.* arXiv:1805.00899.
22. Burns, C., Izmailov, P., Kirchner, J. H., et al. (2023). *Weak-to-Strong Generalization: Eliciting Strong Capabilities With Weak Supervision.* arXiv:2312.09390.
23. Bowman, S. R., Hyun, J., Perez, E., et al. (2022). *Measuring Progress on Scalable Oversight for Large Language Models.* arXiv:2211.03540.

24. Chandra, T. D., Toueg, S. (1996). *Unreliable Failure Detectors for Reliable Distributed Systems.* Journal of the ACM 43(2):225–267.
25. Starshard Communication, SPEC-0003: *Agent Identity, Authentication, and Secure Messaging.* https://github.com/starshard-ai/starshard-communication/blob/main/docs/SPEC-0003-agent-identity-authentication-and-secure-messaging.md — our own work; a v0 specification with a published defect list, not a standard.

### Explicitly not cited

- We found no established academic treatment of **absorbing-state semantics for
  irrevocable stop propagation in distributed capability systems**. OP-2's framing
  is our own systems synthesis, not a reference to existing literature. [9] is the
  nearest canonical anchor and addresses a different question.
- We found no canonical, well-cited academic work on **LLM-agent delegation chains
  or agent identity** comparable in standing to [5] or [14]. See note [12].
- The **dual-LLM pattern** has no formal academic citation; see the note in [15].
- For OP-11 we looked for existing work on **statically verifying that a failure
  signal has a consumer** and did not find it. The nearest formal anchor is [24],
  which specifies what a failure detector must guarantee but assumes its output
  is consumed. We cite the absence.
