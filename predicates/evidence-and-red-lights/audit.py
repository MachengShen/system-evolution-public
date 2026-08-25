#!/usr/bin/env python3
"""Audit a structured evidence manifest against six mechanical predicates."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import sys
from pathlib import Path
from typing import Any


PREDICATE_IDS = {f"ER-{number:03d}" for number in range(1, 7)}


def nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def parse_time(value: Any) -> dt.datetime | None:
    if not nonempty(value):
        return None
    text = value.strip()
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    try:
        parsed = dt.datetime.fromisoformat(text)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=dt.timezone.utc)
    return parsed.astimezone(dt.timezone.utc)


def finding(predicate_id: str, record_id: str, message: str) -> dict[str, str]:
    return {"predicate_id": predicate_id, "record_id": record_id, "message": message}


def record_id(record: Any, fallback: str) -> str:
    if isinstance(record, dict) and nonempty(record.get("id")):
        return record["id"].strip()
    return fallback


def audit_monitors(data: dict[str, Any]) -> list[dict[str, str]]:
    results: list[dict[str, str]] = []
    for index, monitor in enumerate(data.get("monitors", [])):
        rid = record_id(monitor, f"monitors[{index}]")
        if not isinstance(monitor, dict):
            results.append(finding("ER-001", rid, "monitor record is not an object"))
            continue
        missing = []
        if not nonempty(monitor.get("named_reader")):
            missing.append("named_reader")
        repeat = monitor.get("repeat_report")
        if not isinstance(repeat, dict) or repeat.get("enabled") is not True:
            missing.append("repeat_report.enabled=true")
        if monitor.get("reader_independent") is not True:
            missing.append("reader_independent=true")
        if missing:
            clue = ""
            if monitor.get("last_exit_code") == 0 and monitor.get("last_stderr") == "":
                clue = "; exit 0 plus empty stderr is not evidence of an independent reader"
            results.append(finding("ER-001", rid, "missing " + ", ".join(missing) + clue))
    return results


def audit_blockers(data: dict[str, Any]) -> list[dict[str, str]]:
    results: list[dict[str, str]] = []
    waiting_states = {"waiting", "pending", "blocked"}
    for index, blocker in enumerate(data.get("blockers", [])):
        rid = record_id(blocker, f"blockers[{index}]")
        if not isinstance(blocker, dict):
            results.append(finding("ER-002", rid, "blocker record is not an object"))
            continue
        if blocker.get("state") not in waiting_states:
            continue
        verification = blocker.get("verification")
        missing = []
        if not isinstance(verification, dict):
            missing = ["verification.check", "verification.output_summary", "verification.checked_at"]
        else:
            if not nonempty(verification.get("check")):
                missing.append("verification.check")
            if not nonempty(verification.get("output_summary")):
                missing.append("verification.output_summary")
            if parse_time(verification.get("checked_at")) is None:
                missing.append("verification.checked_at (ISO-8601)")
        if missing:
            results.append(finding("ER-002", rid, "waiting-like blocker is unverified: missing " + ", ".join(missing)))
    return results


def audit_receipts(data: dict[str, Any]) -> list[dict[str, str]]:
    results: list[dict[str, str]] = []
    for index, receipt in enumerate(data.get("receipts", [])):
        rid = record_id(receipt, f"receipts[{index}]")
        if not isinstance(receipt, dict):
            results.append(finding("ER-003", rid, "receipt record is not an object"))
            continue
        observed = receipt.get("observed")
        interpretation = receipt.get("interpretation")
        problems = []
        if not nonempty(observed):
            problems.append("observed is empty")
        if not nonempty(interpretation):
            problems.append("interpretation is empty")
        if nonempty(observed) and nonempty(interpretation) and observed.strip() == interpretation.strip():
            problems.append("observed and interpretation are identical")
        if receipt.get("source_kind") == "external":
            verification = receipt.get("verification")
            verified = isinstance(verification, dict) and verification.get("status") == "verified"
            if receipt.get("claim_status") != "unverified" and not verified:
                problems.append("external receipt was promoted without verification")
        if problems:
            results.append(finding("ER-003", rid, "; ".join(problems)))
    return results


def audit_gates(data: dict[str, Any]) -> list[dict[str, str]]:
    results: list[dict[str, str]] = []
    for index, gate in enumerate(data.get("engineering_gates", [])):
        rid = record_id(gate, f"engineering_gates[{index}]")
        if not isinstance(gate, dict):
            results.append(finding("ER-004", rid, "engineering gate record is not an object"))
            continue
        threshold = gate.get("threshold")
        comparison = gate.get("comparison")
        reachability = gate.get("reachability")
        if not isinstance(threshold, (int, float)) or isinstance(threshold, bool):
            results.append(finding("ER-004", rid, "threshold must be numeric"))
            continue
        if comparison not in {"gte", "lte"}:
            results.append(finding("ER-004", rid, "comparison must be gte or lte"))
            continue
        if not isinstance(reachability, dict):
            results.append(finding("ER-004", rid, "missing reachability certificate"))
            continue
        witness_id = reachability.get("witness_id")
        witness_value = reachability.get("witness_value")
        if not nonempty(witness_id) or not isinstance(witness_value, (int, float)) or isinstance(witness_value, bool):
            results.append(finding("ER-004", rid, "reachability requires witness_id and numeric witness_value"))
            continue
        reachable = witness_value >= threshold if comparison == "gte" else witness_value <= threshold
        if not reachable:
            results.append(finding("ER-004", rid, f"witness value {witness_value} cannot satisfy {comparison} threshold {threshold}"))
    return results


def audit_estimators(data: dict[str, Any]) -> list[dict[str, str]]:
    results: list[dict[str, str]] = []
    for index, estimator in enumerate(data.get("estimators", [])):
        rid = record_id(estimator, f"estimators[{index}]")
        if not isinstance(estimator, dict):
            results.append(finding("ER-005", rid, "estimator record is not an object"))
            continue
        problems = []
        if estimator.get("validated") is not True and estimator.get("decision") != "invalid":
            problems.append("unvalidated estimator produced a non-invalid decision")
        value = estimator.get("value")
        upper = estimator.get("trivial_upper_bound")
        if (
            isinstance(value, (int, float))
            and not isinstance(value, bool)
            and isinstance(upper, (int, float))
            and not isinstance(upper, bool)
            and math.isclose(float(value), float(upper), rel_tol=0.0, abs_tol=0.0)
        ):
            problems.append("value exactly equals the trivial upper bound")
        if problems:
            results.append(finding("ER-005", rid, "; ".join(problems)))
    return results


def audit_experiments(data: dict[str, Any]) -> list[dict[str, str]]:
    results: list[dict[str, str]] = []
    for index, experiment in enumerate(data.get("experiments", [])):
        rid = record_id(experiment, f"experiments[{index}]")
        if not isinstance(experiment, dict):
            results.append(finding("ER-006", rid, "experiment record is not an object"))
            continue
        observed_at = parse_time(experiment.get("numbers_observed_at"))
        if observed_at is None:
            results.append(finding("ER-006", rid, "numbers_observed_at must be ISO-8601"))
            continue
        alternatives = experiment.get("alternatives")
        if not isinstance(alternatives, list) or not alternatives:
            results.append(finding("ER-006", rid, "no alternatives were recorded"))
            continue
        preregistered = 0
        problems = []
        for alt_index, alternative in enumerate(alternatives):
            if not isinstance(alternative, dict):
                problems.append(f"alternatives[{alt_index}] is not an object")
                continue
            written_at = parse_time(alternative.get("written_at"))
            status = alternative.get("status")
            if written_at is None:
                problems.append(f"alternatives[{alt_index}].written_at is not ISO-8601")
            elif written_at < observed_at and status == "PREREGISTERED":
                preregistered += 1
            elif written_at >= observed_at and status != "POSTHOC":
                problems.append(f"alternatives[{alt_index}] was written after numbers but is not POSTHOC")
        if preregistered == 0:
            problems.append("no PREREGISTERED alternative predates the numbers")
        if problems:
            results.append(finding("ER-006", rid, "; ".join(problems)))
    return results


def audit(data: dict[str, Any]) -> list[dict[str, str]]:
    if data.get("schema_version") != "1.0":
        raise ValueError("schema_version must be '1.0'")
    section_names = (
        "monitors",
        "blockers",
        "receipts",
        "engineering_gates",
        "estimators",
        "experiments",
    )
    for name in section_names:
        if name not in data or not isinstance(data[name], list):
            raise ValueError(f"top-level {name!r} must be an array")
    results: list[dict[str, str]] = []
    for check in (
        audit_monitors,
        audit_blockers,
        audit_receipts,
        audit_gates,
        audit_estimators,
        audit_experiments,
    ):
        results.extend(check(data))
    unknown = {item["predicate_id"] for item in results} - PREDICATE_IDS
    if unknown:
        raise AssertionError(f"unknown predicate ids: {sorted(unknown)}")
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args()
    try:
        raw = json.loads(args.manifest.read_text(encoding="utf-8"))
        if not isinstance(raw, dict):
            raise ValueError("manifest root must be an object")
        results = audit(raw)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"audit error: {exc}", file=sys.stderr)
        return 2

    report = {
        "manifest": str(args.manifest),
        "finding_count": len(results),
        "predicate_ids_fired": sorted({item["predicate_id"] for item in results}),
        "findings": results,
    }
    if args.format == "json":
        print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
    elif results:
        for item in results:
            print(f"{item['predicate_id']} {item['record_id']}: {item['message']}")
        print(f"FAIL: {len(results)} finding(s) across {len(report['predicate_ids_fired'])} predicate(s)")
    else:
        print("PASS: no predicate findings")
    return 1 if results else 0


if __name__ == "__main__":
    raise SystemExit(main())
