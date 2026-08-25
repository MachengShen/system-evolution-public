# Evidence and Red-Light Predicates

This directory is an executable policy pack for six recurring evidence
failures. It is intentionally descriptive rather than branded. The rules are
small enough to run in a local check or CI job, and every rule includes a way
to detect its own decay.

The pack consumes a JSON audit manifest. See
[`schema.json`](schema.json) and the two files under [`examples/`](examples/).
It uses only the Python standard library.

## Five-minute self-test

From this directory, run:

```sh
./self-test.sh
```

The test makes the auditor inspect an intentionally failing manifest and
requires all six predicate ids to fire. It then checks a clean manifest and
requires no findings. The failing example stays in the repository so a new
checkout has something real to catch on day one.

To inspect a project's own evidence manifest:

```sh
python3 audit.py path/to/evidence-audit.json
```

Exit codes are stable: `0` means no findings, `1` means one or more predicates
fired, and `2` means the input could not be audited. A machine-readable report
is available with `--format json`.

## Manifest sections

The top-level arrays map directly to the six predicates:

| Section | Predicate |
| --- | --- |
| `monitors` | `ER-001` |
| `blockers` | `ER-002` |
| `receipts` | `ER-003` |
| `engineering_gates` | `ER-004` |
| `estimators` | `ER-005` |
| `experiments` | `ER-006` |

An empty section means “nothing declared,” not “verified.” The pack only
judges declared records; it does not claim to discover every undeclared
monitor, blocker, receipt, gate, estimator, or experiment in a repository.

## ER-001 — A red light needs an independent repeat reader

**When it triggers:** A declared monitor lacks any of: a named reader, an
enabled repeat-report policy, or a reader independent of the monitored object.
The combination `last_exit_code: 0` and empty `last_stderr` is reported as a
structural-blindness clue when those three properties are incomplete.

**Failure class it prevents:** A check appears green because a process exited,
while nobody independent can observe, remember, and repeat its red condition.

**Mechanical test:** For every entry in `monitors`, require non-empty
`named_reader`, `repeat_report.enabled: true`, and
`reader_independent: true`. The auditor lists the exact missing properties.

**Anti-signal — how to tell the rule has decayed:** Monitor definitions begin
passing with generic readers such as “the service itself,” repeat reporting is
disabled after noise complaints, or incidents are found only by manual
inspection despite green monitor receipts. A growing count of `exit 0` plus
empty-error records without an independent reader is a direct decay signal.

## ER-002 — A blocker must be measured

**When it triggers:** A blocker is in `waiting`, `pending`, or `blocked` state
without a verification record containing an actual command/check, an output
summary, and a dated `checked_at` value.

**Failure class it prevents:** Work is stranded behind an assumed human action
such as “someone must click, install, connect, or confirm,” even though the
assumption was never tested or has already become stale.

**Mechanical test:** For every waiting-like blocker, require non-empty
`verification.check`, `verification.output_summary`, and an ISO-8601
`verification.checked_at`. Otherwise the auditor emits `ER-002` and the item
must be treated as unverified rather than entering a waiting queue.

**Anti-signal — how to tell the rule has decayed:** Waiting queues contain
records with prose-only evidence, verification dates stop moving while the
environment changes, or completed prerequisites remain labelled as owner or
operator blockers. The measurable indicator is the fraction of waiting-like
items with missing or stale verification fields.

## ER-003 — A receipt must not launder an explanation into a fact

**When it triggers:** A receipt does not separate `observed` from
`interpretation`, or a receipt from another source is promoted above
`unverified` without an explicit verified status.

**Failure class it prevents:** A plausible explanation is copied into a receipt
and later consumed as if it were a direct measurement. Repetition then raises
confidence without adding evidence.

**Mechanical test:** Require both a non-empty `observed` field and a distinct
non-empty `interpretation` field. When `source_kind` is `external`, require
either `claim_status: unverified` or `verification.status: verified`.

**Anti-signal — how to tell the rule has decayed:** Receipts increasingly use
causal language inside `observed`, external receipts arrive pre-labelled as
facts, or downstream summaries cannot quote the measurement independently of
the explanation. A rising count of receipts with identical observation and
interpretation text is a direct decay signal.

## ER-004 — An engineering threshold needs a reachability certificate

**When it triggers:** An engineering gate lacks a reachability witness, or its
recorded witness value cannot meet the declared threshold in the declared
comparison direction.

**Failure class it prevents:** A hypothesis is rejected because nothing can
reach the gate, while the team mistakenly blames the candidate rather than an
unsatisfiable measuring rule.

**Mechanical test:** Require `reachability.witness_id` and
`reachability.witness_value`. For `comparison: gte`, the witness must be at
least the threshold; for `comparison: lte`, it must be at most the threshold.
This predicate applies only to engineering gates.

**Anti-signal — how to tell the rule has decayed:** Thresholds change without
new witnesses, all candidates fail at nearly the same ceiling, or a witness is
copied across environments without rerunning calibration. The measurable
indicator is any gate version whose threshold changed after the timestamp of
its current witness.

## ER-005 — A broken estimator invalidates both red and green

**When it triggers:** An unvalidated estimator emits any decision other than
`invalid`, or its value equals a declared trivial upper bound.

**Failure class it prevents:** A bad instrument produces apparently decisive
positive or negative results. A fully green dashboard can therefore certify an
instrument bug instead of readiness.

**Mechanical test:** If `validated` is not true, require `decision: invalid`.
Independently, compare `value` to `trivial_upper_bound` and emit a red flag on
exact equality. The check uses exact JSON numeric equality because the point is
to catch suspicious boundary saturation for investigation, not to prove a bug.

**Anti-signal — how to tell the rule has decayed:** Unvalidated estimators
reappear in release decisions, exact-boundary values are routinely waived, or
“all green” becomes sufficient despite missing instrument-validation records.
Track the number of decisions produced before the corresponding estimator
validation timestamp.

## ER-006 — Alternatives must predate the numbers

**When it triggers:** An experiment declares no alternatives before results,
or an alternative written after `numbers_observed_at` is not explicitly marked
`POSTHOC`.

**Failure class it prevents:** A result is explained only after it is known,
while hindsight is presented as prospective discrimination among hypotheses.

**Mechanical test:** Parse `numbers_observed_at` and every alternative's
`written_at`. At least one alternative must be dated earlier and marked
`PREREGISTERED`. Any later alternative must be marked `POSTHOC`.

**Anti-signal — how to tell the rule has decayed:** Alternative files share a
timestamp with result generation, version history shows alternatives first
appearing after outputs, or `POSTHOC` labels disappear during summarization.
The measurable indicator is the share of experiments lacking a pre-result
alternative commit or immutable record.

## Receipt ledger

[`ledger/events.jsonl`](ledger/events.jsonl) is the machine-readable,
append-only history. Its first event is this release. It distinguishes
`self_test` triggers from `real` triggers and records attempts to falsify each
predicate. [`ledger/README.md`](ledger/README.md) is rendered from that file:

```sh
python3 ledger/render.py --check
```

Append events; do not rewrite earlier history to make a rule look healthier.
A status change should be a new event with the reason and evidence reference.
