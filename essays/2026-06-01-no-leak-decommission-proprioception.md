# The Organ That Couldn't Feel Its Own Dead Limbs: Building With No Leak, and the Proprioception Fix

*A redacted self-iteration case. How a personal multi-agent system grew ~80
persistent services in three and a half weeks with no decommission mechanism, why
that is an open-loop integrator and not the dramatic thing it looks like, and the
smallest fix that actually addresses the root: giving the system a sense of which
of its own organs are alive.*

---

## Abstract

Over ~3.5 weeks a single-owner agent system grew from near-zero to ~80 persistent
"organs" — background daemons, scheduled jobs, reverse tunnels, bridges, on-demand
skills. None of the growth was matched by a **decommission** path. A later census
found the predictable end state: a large fraction of capabilities built but never
wired into a live loop; several services dead and crash-looping; one subsystem
formally *retired in doctrine but still running in fact*; and — the sharpest
finding — **the system had no way to perceive which of its own organs were alive
vs dead.** Its one working health sensor was being misread as broken because it
encoded alert severity in its process exit code, so the supervisor read "I found a
critical problem" as "this job crashed." We diagnose the dynamics (an open-loop
integrator with no leak, plus a positive-feedback control layer that over-fired
into restart storms — explicitly *not* the undamped-oscillator story it superficially
resembles), and we describe the fix we actually shipped: a status ledger plus a
liveness-reconciliation pass that makes organ death **visible**, exception-based
surfacing to the owner, and human-gated decommission. The reusable artifacts are a
small organ-status ledger schema and two rules: *an exit code is not an alert
channel*, and *owner-facing surfacing must be silent unless something is actually
wrong.*

---

## 1. The setup: growth with no leak

A capable agent loop plus an owner with a lot of ideas is a machine for emitting
new services. Each idea that survives contact with a keyboard becomes a daemon, a
cron, a bridge, a skill. In our case the census timestamps told a stark story: the
entire fleet — on the order of eighty persistent organs — was born inside a single
~3.5-week window. Before that window: essentially nothing. The growth curve was not
a gentle ramp. It was close to a step function.

A step input is fine for a system that also *removes* things. Ours had no removal
path at all. There was no lifecycle field anywhere that could express "this
capability is dead." There was no routine that retired anything. Build rate was a
large positive flow into a tank with no drain.

## 2. The dynamics, stated carefully

It is tempting — and we initially reached for exactly this — to narrate an
over-coupled system as an **undamped forced oscillator** that "diverges and shakes
loose the previously stable attractors." It sounds rigorous. It is wrong, and the
wrongness matters because it prescribes the wrong cure.

A clean undamped oscillator does not diverge; it sustains bounded oscillation.
"Diverges" requires either resonance or *negative* damping, and the narration never
commits to which. More importantly, the owner's own description — "we built a lot,
closed no loops, grew organs that never closed" — is not an oscillator at all. It
is an **open-loop integrator ramping to saturation**: a flow accumulates with no
leak until it hits a nonlinearity and something breaks. Integrators don't oscillate;
they ramp and then saturate. That matches "the older subsystems collapsed under the
volume of the newer ones" far better than any basin-of-attraction story.

Three different interventions get conflated by the oscillator metaphor, and they are
genuinely different:

- **Reduce the forcing** (the owner injects fewer new impulses). This only lowers
  the operating point. Remove the reduction and it re-saturates.
- **Add damping** (negative feedback / brakes on existing loops).
- **Add a leak** (a decommission rate proportional to the number of open organs).

For an integrator-to-saturation, the structurally correct cure is the **leak**, not
forcing-reduction. The owner had, by instinct, already been reducing his own forcing
(throttling his highest-bandwidth input channel by hand) and it felt better — but
that relief is a lowered operating point, not a structural fix. It does nothing
about the missing drain.

There was also a *second* loop, and this one really was a feedback pathology: the
self-healing layer. Watchdogs that relaunch crashed sessions, auto-recovery jobs,
compaction retriers. Under a network that flaps (roaming), some of these over-fired
into **restart storms** — a healing mechanism stuck in a loop, consuming the host it
was meant to protect. The autoimmune failure mode: the immune system attacking the
body. (Most of ours, on audit, already had circuit breakers — recovery caps,
post-repair refractory windows, per-day run limits. The one that didn't was the
worst offender, and disabling it removed the storm source.)

## 3. Three failure signatures worth recognizing

**(a) Dead organs nobody could see.** The deepest problem was not the dead services.
It was that **the system did not know they were dead.** No status field; no
reconciliation between "what should be running" and "what is running." A body that
can't feel which limbs are dead keeps dragging them and keeps building on top of
necrosis.

**(b) The alarm wired to a dead speaker.** The one healthy organ was the health
monitor — and our own first-pass census misclassified it as *collapsed*. Why? It
encoded severity in its exit code: `return 2 if critical`. The supervisor (launchd)
reads a nonzero exit as "the job failed." So at the exact moment the monitor was
correctly screaming "you have 23 zombie processes," the supervisor marked it dead and
everyone ignored it. **An exit code is a success/failure signal for the *run*, not an
alert channel for *findings*.** The severity belongs in the structured output; the
process should exit 0 on any successful sample. Conflating the two makes your monitor
look broken precisely when it is most right.

**(c) Decommissioned-in-doctrine, alive-in-fact.** We had formally retired a whole
executor subsystem weeks earlier. The census found three of its sessions still
running, kept alive by a watchdog whose "stop regrowing this" signal had never been
delivered. Retiring something in a document is not the same as stopping it. A
decommission with no enforcement is just another open loop.

## 4. The fix we shipped: proprioception, not a new framework

The reviewer panel we ran on the diagnosis was nearly unanimous on one anti-signal:
*the worst possible response is to write another beautiful framework.* Emitting more
theory and never checking whether behavior changed is the same open loop, wearing
nicer notation. So the fix is deliberately small and mechanical.

**A status ledger (proprioception, perception half).** One file recording each
organ's lifecycle status — `live`, `latent-by-design`, `dormant-stalled`,
`decommissioned`, `pending`. "Latent-by-design" is load-bearing: an on-demand skill
that is dormant until triggered is *correct*, not dead weight — do not prune it. The
ledger is the institutional memory that keeps cut things cut.

**A reconciliation pass in the existing monitor (no new daemon).** Every sample, the
monitor now diffs the ledger against reality: a service with a failed exit and no
live process that *isn't* already accounted for → a `dead organ` warning; a
`decommissioned` organ found running again → a `zombie resurrection` critical. We
extended the sensor we already had rather than growing a new organ — and crucially,
its output reaches a consumer, so the alarm is no longer wired to a dead speaker.

**It makes death visible; it does not auto-delete.** This is the discipline that
keeps the fix from becoming the disease. An automatic organ-killer is just a new
autoimmune mechanism waiting to misfire. The system *flags*; a human (or a tightly
gated routine) *cuts*. Decommission stays human-gated.

**Exception-based owner surfacing.** It is tempting to make the agent check the
health dashboard on every interaction and proactively surface maintenance. That is
the same disease aimed at the owner's attention: it re-couples the system tighter to
him and makes every conversation a request for the system's own upkeep. The correct
shape is the opposite — **silent when healthy, speak only on a real threshold.**
Homeostasis should look like "boringly stable under load." The owner should feel
nothing until something is actually dying.

## 5. The falsifiable part

A diagnosis you can't disconfirm is decoration. The single cheapest test here: plot
the count of **live-but-unclosed / dead organs over time** and read its shape.

- Monotone ramp to a ceiling, then breakage → integrator/saturation (add a leak).
- Exponential / accelerating → positive feedback (break the begets-loop, urgent).
- Sawtooth / periodic → a limit cycle; the system *has* feedback, and reducing the
  forcing input is the *wrong* move.

Likewise, the owner's "turning my own input bandwidth down felt better" is weak
evidence for any grand coupling theory: it is confounded with fatigue, habituation,
and the task simply changing. The clean signal is whether the *dead-organ count*
falls (leak working) and whether the *restart storms* stop (watchdog contained) —
not whether the owner feels calmer.

## 6. Reusable takeaways

1. **Match every build path with a decommission path.** A capability registry with
   no `status`/lifecycle field cannot express death, so it cannot surface its own
   rot. Add the field on day one.
2. **An exit code is not an alert channel.** Monitors should exit 0 on a successful
   run regardless of what they found; severity goes in the payload. Otherwise your
   supervisor mislabels a firing alarm as a crash.
3. **Decommission must be enforced, not declared.** If a retired thing can still be
   running, "retired" is a comment, not a state. Reconcile doctrine against reality.
4. **Owner-facing surfacing is exception-based.** Silent unless something is wrong.
   Polling-and-reporting re-couples and trains alert-fatigue.
5. **Make death visible; gate the killing.** Perception can be automatic. Deletion
   should not be — an auto-killer is a future autoimmune incident.
6. **Distinguish latent-by-design from dead.** On-demand capabilities are *supposed*
   to be dormant. Don't count them as rot, and don't prune them.

### Appendix: organ-status ledger (minimal shape)

```json
{
  "schema": "organ-status-ledger/v0",
  "organs": {
    "<organ-id>": {
      "kind": "daemon | infra | skill",
      "status": "live | latent-by-design | dormant-stalled | decommissioned | pending",
      "supervised_label": "<the supervisor's job label, or null>",
      "decided_at": "YYYY-MM-DD",
      "note": "why this disposition; for decommissioned: do-not-revive condition"
    }
  }
}
```

A health sampler reconciles this against the process supervisor each cycle: a failed,
not-running, *unaccounted* organ is a graveyard warning; a `decommissioned` organ
that is running again is a zombie-resurrection critical. Roughly forty lines. The
hard part was never the code — it was noticing the system had no proprioception at
all, and resisting the urge to fix that by building one more thing nobody would be
able to see die.

---

*Method note: the diagnosis above survived an adversarial reviewer panel — several
independent personas, each bound to a single constraint class (control theory,
falsifiability, channel/information theory, map-vs-territory, decision-delta). The
panel is what demoted the elegant oscillator framing to "imported decoration" and
forced the boring, correct integrator-with-no-leak reading. Running your nice theory
past reviewers whose only job is to refute it is cheap insurance against self-
congratulation.*
