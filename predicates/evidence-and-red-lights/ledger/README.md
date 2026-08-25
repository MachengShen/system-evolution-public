# Predicate Receipt Ledger

This page is generated from [`events.jsonl`](events.jsonl). The JSONL file is the append-only source of truth. Trigger records distinguish `self_test` from `real` use.

## Release

| Version | First release | Status | Evidence |
| --- | --- | --- | --- |
| 1.0.0 | 2026-08-25T00:45:29Z | active | [../README.md](../README.md) |

## ER-001

Version `1.0.0` · first released `2026-08-25T00:45:29Z` · status `active`.

### Trigger history

| When | Kind | Result | Evidence | Note |
| --- | --- | --- | --- | --- |
| 2026-08-25T00:45:29Z | self_test | fired | [../examples/intentionally-failing.json](../examples/intentionally-failing.json) | Caught a monitor without a named independent repeat reader. |

### Falsification attempts

| When | Result | Evidence | Note |
| --- | --- | --- | --- |
| 2026-08-25T00:45:29Z | clean_fixture_not_flagged | [../examples/clean.json](../examples/clean.json) | Independent named repeat reader passed without a false positive. |

## ER-002

Version `1.0.0` · first released `2026-08-25T00:45:29Z` · status `active`.

### Trigger history

| When | Kind | Result | Evidence | Note |
| --- | --- | --- | --- | --- |
| 2026-08-25T00:45:29Z | self_test | fired | [../examples/intentionally-failing.json](../examples/intentionally-failing.json) | Caught a waiting blocker without a dated measured check. |

### Falsification attempts

| When | Result | Evidence | Note |
| --- | --- | --- | --- |
| 2026-08-25T00:45:29Z | clean_fixture_not_flagged | [../examples/clean.json](../examples/clean.json) | Measured and dated blocker passed without a false positive. |

## ER-003

Version `1.0.0` · first released `2026-08-25T00:45:29Z` · status `active`.

### Trigger history

| When | Kind | Result | Evidence | Note |
| --- | --- | --- | --- | --- |
| 2026-08-25T00:45:29Z | self_test | fired | [../examples/intentionally-failing.json](../examples/intentionally-failing.json) | Caught an external receipt that promoted interpretation without observation or verification. |

### Falsification attempts

| When | Result | Evidence | Note |
| --- | --- | --- | --- |
| 2026-08-25T00:45:29Z | clean_fixture_not_flagged | [../examples/clean.json](../examples/clean.json) | Separated unverified external receipt passed without a false positive. |

## ER-004

Version `1.0.0` · first released `2026-08-25T00:45:29Z` · status `active`.

### Trigger history

| When | Kind | Result | Evidence | Note |
| --- | --- | --- | --- | --- |
| 2026-08-25T00:45:29Z | self_test | fired | [../examples/intentionally-failing.json](../examples/intentionally-failing.json) | Caught an engineering threshold whose witness could not reach it. |

### Falsification attempts

| When | Result | Evidence | Note |
| --- | --- | --- | --- |
| 2026-08-25T00:45:29Z | clean_fixture_not_flagged | [../examples/clean.json](../examples/clean.json) | Reachable engineering threshold passed without a false positive. |

## ER-005

Version `1.0.0` · first released `2026-08-25T00:45:29Z` · status `active`.

### Trigger history

| When | Kind | Result | Evidence | Note |
| --- | --- | --- | --- | --- |
| 2026-08-25T00:45:29Z | self_test | fired | [../examples/intentionally-failing.json](../examples/intentionally-failing.json) | Caught an unvalidated green decision at the trivial upper bound. |

### Falsification attempts

| When | Result | Evidence | Note |
| --- | --- | --- | --- |
| 2026-08-25T00:45:29Z | clean_fixture_not_flagged | [../examples/clean.json](../examples/clean.json) | Invalidated decision away from the trivial bound passed without a false positive. |

## ER-006

Version `1.0.0` · first released `2026-08-25T00:45:29Z` · status `active`.

### Trigger history

| When | Kind | Result | Evidence | Note |
| --- | --- | --- | --- | --- |
| 2026-08-25T00:45:29Z | self_test | fired | [../examples/intentionally-failing.json](../examples/intentionally-failing.json) | Caught a post-result alternative incorrectly labelled as preregistered. |

### Falsification attempts

| When | Result | Evidence | Note |
| --- | --- | --- | --- |
| 2026-08-25T00:45:29Z | clean_fixture_not_flagged | [../examples/clean.json](../examples/clean.json) | Pre-result alternative plus labelled posthoc note passed without a false positive. |
