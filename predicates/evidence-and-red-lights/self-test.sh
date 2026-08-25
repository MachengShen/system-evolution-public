#!/usr/bin/env bash
set -euo pipefail

pack_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
temporary_dir="$(mktemp -d)"
trap 'rm -rf "$temporary_dir"' EXIT

failing_report="$temporary_dir/failing-report.json"
clean_report="$temporary_dir/clean-report.json"

set +e
python3 "$pack_dir/audit.py" "$pack_dir/examples/intentionally-failing.json" --format json >"$failing_report"
failing_rc=$?
set -e
if [[ "$failing_rc" -ne 1 ]]; then
  echo "self-test failed: intentionally failing fixture returned $failing_rc, expected 1" >&2
  exit 1
fi

python3 - "$failing_report" <<'PY'
import json
import sys

report = json.load(open(sys.argv[1], encoding="utf-8"))
expected = {f"ER-{number:03d}" for number in range(1, 7)}
actual = set(report["predicate_ids_fired"])
if actual != expected:
    raise SystemExit(f"self-test failed: expected {sorted(expected)}, got {sorted(actual)}")
print("failing fixture: all six predicates fired")
PY

python3 "$pack_dir/audit.py" "$pack_dir/examples/clean.json" --format json >"$clean_report"
python3 - "$clean_report" <<'PY'
import json
import sys

report = json.load(open(sys.argv[1], encoding="utf-8"))
if report["finding_count"] != 0:
    raise SystemExit(f"self-test failed: clean fixture had {report['finding_count']} finding(s)")
print("clean fixture: no predicates fired")
PY

python3 "$pack_dir/ledger/render.py" --check
echo "SELF-TEST PASS"
