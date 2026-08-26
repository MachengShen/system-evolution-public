# Closure Before Intake: What a Forecast Ledger Actually Bottlenecks On

We keep a small, append-only ledger of forecasts about how the world is
changing — institutional transition under AI, compute and energy, capital and
media, migration. Each entry carries a probability, a check date, a
pre-registered resolution contract, named public sources, anti-signals, and a
frozen rule for how evidence is allowed to move the number. The ledger exists
so that later readers can audit what was said before the outcome was known.

On 2026-08-26 we measured the ledger before designing anything new. Ten
forecasts. One scored. **Nine past their check date and unscored**, the oldest
by eleven weeks. A weekly check job had faithfully reported them as "due" every
week. Nothing was obliged to act on the report. The public forecast page,
meanwhile, still had zero real entries — only the format.

That measurement changed the design. The obvious plan was to build intake: more
sources, more monitoring, more candidates. But a ledger that cannot close the
forecasts it already holds does not need more forecasts. It needs a forcing
function. Everything below follows from that.

## Intake is demand-driven by exposure

A general crawler reads the world and hopes something in it matters. We do the
opposite. Every forecast already names the observable that would resolve it,
the sources that publish that observable, and the anti-signals that would move
it. Those fields *compile* into watches:

- **source-release** — a named periodic publication or series issues a new
  edition. Only sources with a machine-checkable release signal (feed, API,
  version endpoint) may be watched this way; a source without one cannot carry
  this kind of watch, and a forecast that compiles to no watch at all is not a
  forecast and is rejected.
- **anti-signal** — a threshold or keyword condition changes state. Watches
  fire on transitions, never on persistence, so a standing condition does not
  nag.
- **coupling** — another forecast resolves or revises, and a pre-registered
  edge (sign *and* magnitude bound) propagates the move. Every propagated
  revision cites the original observation, and one observation may move a given
  forecast once, so correlated evidence cannot be counted twice.
- **check date** — the calendar arrives. This is a fail-safe, not a closure: it
  opens a gate with a time-to-live, and the gate has a default action if nobody
  resolves it in time.

So "what triggers reading the world" is answered by the ledger itself: the
world is read exactly where a claim is exposed to it, and nowhere else. A fixed
interval survives only as an upper bound on staleness.

## Metabolism needs a forcing function

The nine stale forecasts were not a data problem. Their sources were public and
cheap to read. They rotted because every path that could have closed them ended
in a state — "due", "held", "gated" — with no obligation attached. Any redesign
that adds new states without obligations only renames the parking lot.

The rule we adopted: **every gate, hold, or stale state carries a time-to-live
and a pre-registered default action on expiry.** Unresolved disagreement after
N days is scored at reduced confidence and flagged, never silently closed.
Pending gates batch into one weekly digest rather than per-event interrupts.
The depth of the held queue is tracked as its own failure signal, so a backlog
cannot hide behind the metric that only watches the old failure shape.

Two further disciplines came out of adversarial review of the draft:

- **The scorer re-derives from raw capture.** A second, independent reader
  scores from the original captured source, not from the first reader's
  extracted number. Otherwise "two readers agreed" only means they shared one
  extraction bug. The reader that authored a forecast never scores it.
- **Update magnitude is a table, written before the evidence.** Not a single
  cap, but a pre-registered table indexed by source tier and by whether the
  evidence confirms or disconfirms, with steps that shrink as the probability
  approaches 0 or 1. A flat cap rewards opening with an extreme number to
  minimize exposure. Each revision records which cell it invoked.

## Multi-scale without narrative repair

Forecasts live on two axes: time (weeks, years, decades) and abstraction
(civilizational transitions; structural processes per region and domain; what
they mean for a specific cohort's exposure, options, and timing).

Long-horizon claims are scored early through a ladder: each names a
short-horizon consequence of the *same mechanism* that would already be visible
if the mechanism were real. The review added the condition that makes this
diagnostic rather than decorative: **each rung must name a rival mechanism and
state how the rung's outcome would differ under it.** A rung compatible with
every story tests nothing. Rungs are coupling edges into the parent claim, so
confirmation and falsification travel the same audited path.

The highest layer must be able to die on its own. Every civilizational-scale
claim carries its own resolution contract and check date, plus at least two
rival hypotheses that predict a further, named rung differently. A claim that
survives only by propagated confidence, never by direct scoring, is forced into
review after a bounded run of rung hits.

Downward, implication is capped mechanically: a cohort-level card's displayed
confidence is computed at publish time as the minimum over the claims it
cites, and a card that exceeds any source is rejected before it renders.

Cross-region comparisons — the unit we care most about — are only admitted with
a comparability certificate: the sources on each side measure the same
construct with compatible definitions and cadence, and the null policy states
explicitly what happens when a source is discontinued or redefined.

## What stays private

Forecasts whose publication would create exposure for people in a particular
jurisdiction are kept in a private tier; the public ledger carries aggregate
projections of them, dated and receipted like everything else. The exposure of
a public, attributable ledger is set by its single most sensitive entry, not
diluted by how many regions it covers.

## Sequence

1. Close the nine. Retroactively compile their watches, fetch the missed
   window, score with two independent readers, and put any disagreement into
   one digest. This step needs none of the new machinery; it tests whether a
   forcing function produces closure at all.
2. Publish the first real entries with receipts on the day they are written.
3. Only then generalize the two existing threshold monitors into the watch
   compiler.

---

**Claim receipt.** State: *speculative* — this is a design that has been
adversarially reviewed, not a system that has run. Confidence 0.65 that the
forcing-function rule eliminates the stale backlog within one cycle; 0.5 that
the overall design is worth its coordination cost at our current volume.
Falsified if, after one full cycle with time-to-live gates in place, the
unscored-past-check-date count is nonzero or the held-gate queue is growing.
