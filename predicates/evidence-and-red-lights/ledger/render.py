#!/usr/bin/env python3
"""Render and validate the human-readable predicate ledger."""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path


HERE = Path(__file__).resolve().parent
EVENTS_PATH = HERE / "events.jsonl"
OUTPUT_PATH = HERE / "README.md"
PREDICATE_IDS = [f"ER-{number:03d}" for number in range(1, 7)]


def load_events() -> list[dict[str, object]]:
    events = []
    seen = set()
    for line_number, line in enumerate(EVENTS_PATH.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        event = json.loads(line)
        event_id = event.get("event_id")
        if not isinstance(event_id, str) or not event_id:
            raise ValueError(f"line {line_number}: missing event_id")
        if event_id in seen:
            raise ValueError(f"line {line_number}: duplicate event_id {event_id}")
        seen.add(event_id)
        events.append(event)
    if not events or events[0].get("event_type") != "release" or events[0].get("predicate_id") != "PACK":
        raise ValueError("first ledger event must be the pack release")
    return events


def render(events: list[dict[str, object]]) -> str:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for event in events:
        predicate_id = event.get("predicate_id")
        if isinstance(predicate_id, str):
            grouped[predicate_id].append(event)

    lines = [
        "# Predicate Receipt Ledger",
        "",
        "This page is generated from [`events.jsonl`](events.jsonl). The JSONL file is the append-only source of truth. Trigger records distinguish `self_test` from `real` use.",
        "",
        "## Release",
        "",
        "| Version | First release | Status | Evidence |",
        "| --- | --- | --- | --- |",
    ]
    pack = grouped["PACK"][0]
    lines.append(
        f"| {pack.get('version')} | {pack.get('occurred_at')} | {pack.get('current_status')} | [{pack.get('evidence_ref')}]({pack.get('evidence_ref')}) |"
    )

    for predicate_id in PREDICATE_IDS:
        predicate_events = grouped.get(predicate_id, [])
        releases = [event for event in predicate_events if event.get("event_type") == "release"]
        triggers = [event for event in predicate_events if event.get("event_type") == "trigger"]
        attempts = [event for event in predicate_events if event.get("event_type") == "falsification_attempt"]
        if len(releases) != 1:
            raise ValueError(f"{predicate_id}: expected exactly one release event")
        release = releases[0]
        lines.extend(
            [
                "",
                f"## {predicate_id}",
                "",
                f"Version `{release.get('version')}` · first released `{release.get('occurred_at')}` · status `{release.get('current_status')}`.",
                "",
                "### Trigger history",
                "",
                "| When | Kind | Result | Evidence | Note |",
                "| --- | --- | --- | --- | --- |",
            ]
        )
        for event in triggers:
            ref = event.get("evidence_ref")
            lines.append(
                f"| {event.get('occurred_at')} | {event.get('trigger_kind')} | {event.get('result')} | [{ref}]({ref}) | {event.get('note')} |"
            )
        lines.extend(
            [
                "",
                "### Falsification attempts",
                "",
                "| When | Result | Evidence | Note |",
                "| --- | --- | --- | --- |",
            ]
        )
        for event in attempts:
            ref = event.get("evidence_ref")
            lines.append(
                f"| {event.get('occurred_at')} | {event.get('result')} | [{ref}]({ref}) | {event.get('note')} |"
            )
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if README.md is not the current render")
    args = parser.parse_args()
    try:
        output = render(load_events())
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"ledger error: {exc}", file=sys.stderr)
        return 2
    if args.check:
        current = OUTPUT_PATH.read_text(encoding="utf-8") if OUTPUT_PATH.exists() else ""
        if current != output:
            print("ledger error: README.md is stale; run ledger/render.py", file=sys.stderr)
            return 1
        print("ledger render: current")
        return 0
    OUTPUT_PATH.write_text(output, encoding="utf-8")
    print(f"wrote {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
