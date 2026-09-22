#!/usr/bin/env python3
"""Render a reviewer-focused summary of an Aerith metadata refresh."""

from __future__ import annotations

import argparse
import json
import subprocess
from collections import Counter
from pathlib import Path
from typing import Any, Callable


REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = Path("sources/comets/aerith_current_comets_v1.json")
INDEX_PATH = Path("v1/packages/comet-details/comet_detail_metadata_v1.json")
MAX_TABLE_ROWS = 12


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Summarize an Aerith refresh against a checked-in git revision."
    )
    parser.add_argument("--before-ref", default="HEAD")
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def read_json(path: Path) -> dict[str, Any]:
    with (REPO_ROOT / path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def read_json_at_ref(ref: str, path: Path) -> dict[str, Any]:
    result = subprocess.run(
        ["git", "show", f"{ref}:{path.as_posix()}"],
        cwd=REPO_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(result.stdout)


def load_records(
    index: dict[str, Any],
    reader: Callable[[Path], dict[str, Any]],
) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for descriptor in index.get("comets") or []:
        path_text = str(descriptor.get("path") or "").strip()
        if not path_text:
            continue
        payload = reader(Path(path_text))
        record = payload.get("record")
        if isinstance(record, dict):
            records.append(record)
    return records


def designation(entry: dict[str, Any]) -> str:
    return str(entry.get("normalizedDesignation") or entry.get("designation") or "").strip()


def display_name(entry: dict[str, Any]) -> str:
    return str(
        entry.get("displayName")
        or entry.get("aerithName")
        or entry.get("designation")
        or entry.get("normalizedDesignation")
        or entry.get("stableID")
        or "Unknown comet"
    ).strip()


def number(value: Any) -> float | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    return None


def page_dates(source: dict[str, Any]) -> list[str]:
    return sorted(
        {
            str(page.get("pageDate"))
            for page in source.get("pages") or []
            if page.get("pageDate")
        }
    )


def source_entries(source: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        designation(entry): entry
        for entry in source.get("comets") or []
        if designation(entry)
    }


def record_entries(records: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {
        str(record.get("stableID") or ""): record
        for record in records
        if record.get("stableID")
    }


def current_magnitude(entry: dict[str, Any]) -> float | None:
    return number(entry.get("currentMagnitude"))


def cached_media_paths(record: dict[str, Any]) -> tuple[str, ...]:
    media = record.get("media") or {}
    paths = {
        str(asset.get("cachedPath"))
        for asset in media.values()
        if isinstance(asset, dict) and asset.get("cachedPath")
    }
    return tuple(sorted(paths))


def significant_points(record: dict[str, Any]) -> dict[tuple[str, str], dict[str, Any]]:
    stable_id = str(record.get("stableID") or "")
    return {
        (stable_id, str(point.get("id") or "")): point
        for point in record.get("brightness") or []
        if point.get("isSignificant") and point.get("id")
    }


def build_summary(
    before_source: dict[str, Any],
    after_source: dict[str, Any],
    before_records: list[dict[str, Any]],
    after_records: list[dict[str, Any]],
) -> dict[str, Any]:
    before_by_designation = source_entries(before_source)
    after_by_designation = source_entries(after_source)
    before_keys = set(before_by_designation)
    after_keys = set(after_by_designation)

    magnitude_changes: list[dict[str, Any]] = []
    for key in sorted(before_keys & after_keys):
        previous = current_magnitude(before_by_designation[key])
        current = current_magnitude(after_by_designation[key])
        if previous is None or current is None or abs(current - previous) < 0.05:
            continue
        magnitude_changes.append(
            {
                "designation": key,
                "name": display_name(after_by_designation[key]),
                "url": after_by_designation[key].get("detailURL"),
                "previous": previous,
                "current": current,
                "delta": current - previous,
            }
        )
    magnitude_changes.sort(key=lambda row: (-abs(row["delta"]), row["designation"]))

    before_by_id = record_entries(before_records)
    after_by_id = record_entries(after_records)
    before_signals = {
        key
        for record in before_records
        for key in significant_points(record)
    }
    new_signals: list[dict[str, Any]] = []
    for record in after_records:
        for key, point in significant_points(record).items():
            if key in before_signals:
                continue
            new_signals.append(
                {
                    "stableID": record.get("stableID"),
                    "name": display_name(record),
                    "url": record.get("detailURL"),
                    "date": point.get("date"),
                    "magnitude": point.get("magnitude"),
                    "delta": point.get("magnitudeDelta"),
                    "interpretation": point.get("interpretation") or point.get("commentary"),
                }
            )
    new_signals.sort(
        key=lambda row: (
            -abs(number(row.get("delta")) or 0.0),
            str(row.get("stableID") or ""),
        )
    )

    visibility_transitions: list[dict[str, Any]] = []
    media_changes: list[dict[str, Any]] = []
    for stable_id in sorted(set(before_by_id) & set(after_by_id)):
        before_record = before_by_id[stable_id]
        after_record = after_by_id[stable_id]
        before_state = str((before_record.get("visibilitySummary") or {}).get("state") or "unknown")
        after_state = str((after_record.get("visibilitySummary") or {}).get("state") or "unknown")
        if before_state != after_state:
            visibility_transitions.append(
                {
                    "stableID": stable_id,
                    "name": display_name(after_record),
                    "url": after_record.get("detailURL"),
                    "before": before_state,
                    "after": after_state,
                }
            )
        if cached_media_paths(before_record) != cached_media_paths(after_record):
            media_changes.append(
                {
                    "stableID": stable_id,
                    "name": display_name(after_record),
                    "url": after_record.get("detailURL"),
                }
            )

    for stable_id in sorted(set(after_by_id) - set(before_by_id)):
        after_record = after_by_id[stable_id]
        if cached_media_paths(after_record):
            media_changes.append(
                {
                    "stableID": stable_id,
                    "name": display_name(after_record),
                    "url": after_record.get("detailURL"),
                }
            )

    brightest = [
        {
            "designation": key,
            "name": display_name(entry),
            "url": entry.get("detailURL"),
            "magnitude": current_magnitude(entry),
        }
        for key, entry in after_by_designation.items()
        if current_magnitude(entry) is not None
    ]
    brightest.sort(key=lambda row: (row["magnitude"], row["designation"]))

    def package_metrics(records: list[dict[str, Any]]) -> dict[str, Any]:
        visibility = Counter(
            str((record.get("visibilitySummary") or {}).get("state") or "unknown")
            for record in records
        )
        return {
            "records": len(records),
            "withMedia": sum(1 for record in records if cached_media_paths(record)),
            "visibility": dict(sorted(visibility.items())),
        }

    return {
        "beforePageDates": page_dates(before_source),
        "afterPageDates": page_dates(after_source),
        "beforeSourceCount": len(before_by_designation),
        "afterSourceCount": len(after_by_designation),
        "added": [after_by_designation[key] for key in sorted(after_keys - before_keys)],
        "removed": [before_by_designation[key] for key in sorted(before_keys - after_keys)],
        "magnitudeChanges": magnitude_changes,
        "newSignals": new_signals,
        "visibilityTransitions": visibility_transitions,
        "mediaChanges": media_changes,
        "brightest": brightest,
        "beforePackage": package_metrics(before_records),
        "afterPackage": package_metrics(after_records),
    }


def escape_markdown(value: Any) -> str:
    return str(value or "").replace("|", "\\|").replace("\n", " ").strip()


def linked_name(name: str, url: Any) -> str:
    safe_name = escape_markdown(name)
    safe_url = str(url or "").strip()
    if safe_url.startswith(("http://www.aerith.net/", "https://www.aerith.net/")):
        return f"[{safe_name}]({safe_url})"
    return safe_name


def format_dates(values: list[str]) -> str:
    return ", ".join(values) if values else "Unavailable"


def format_magnitude(value: Any) -> str:
    parsed = number(value)
    return f"{parsed:.1f}" if parsed is not None else "Unavailable"


def format_visibility(metrics: dict[str, Any]) -> str:
    visibility = metrics.get("visibility") or {}
    return ", ".join(f"{key}: {value}" for key, value in visibility.items()) or "none"


def bounded_rows(rows: list[Any]) -> tuple[list[Any], int]:
    return rows[:MAX_TABLE_ROWS], max(0, len(rows) - MAX_TABLE_ROWS)


def render_markdown(summary: dict[str, Any]) -> str:
    before_package = summary["beforePackage"]
    after_package = summary["afterPackage"]
    lines = [
        "## Refresh summary",
        "",
        "| Metric | Previous | Refreshed |",
        "| --- | ---: | ---: |",
        f"| Aerith page date | {format_dates(summary['beforePageDates'])} | {format_dates(summary['afterPageDates'])} |",
        f"| Weekly comet entries | {summary['beforeSourceCount']} | {summary['afterSourceCount']} |",
        f"| Packaged AstroGuide records | {before_package['records']} | {after_package['records']} |",
        f"| Records with cached imagery | {before_package['withMedia']} | {after_package['withMedia']} |",
        f"| Visibility states | {escape_markdown(format_visibility(before_package))} | {escape_markdown(format_visibility(after_package))} |",
        "",
        "### Weekly-list movement",
        "",
    ]

    if summary["added"]:
        added = ", ".join(
            linked_name(display_name(entry), entry.get("detailURL"))
            for entry in summary["added"]
        )
        lines.append(f"- **Added:** {added}")
    else:
        lines.append("- **Added:** None")
    if summary["removed"]:
        removed = ", ".join(
            linked_name(display_name(entry), entry.get("detailURL"))
            for entry in summary["removed"]
        )
        lines.append(f"- **Removed:** {removed}")
    else:
        lines.append("- **Removed:** None")

    lines.extend(["", "### Largest current-magnitude movements", ""])
    movements, movement_overflow = bounded_rows(summary["magnitudeChanges"])
    if movements:
        lines.extend(
            [
                "| Comet | Previous | Refreshed | Interpretation |",
                "| --- | ---: | ---: | --- |",
            ]
        )
        for row in movements:
            delta = row["delta"]
            interpretation = (
                f"Faded {delta:.1f} mag" if delta > 0 else f"Brightened {abs(delta):.1f} mag"
            )
            lines.append(
                f"| {linked_name(row['name'], row.get('url'))} | {row['previous']:.1f} | "
                f"{row['current']:.1f} | {interpretation} |"
            )
        if movement_overflow:
            lines.append(f"\n_{movement_overflow} additional smaller movement(s) omitted._")
    else:
        lines.append("No current-magnitude movements of at least 0.05 mag were detected.")

    lines.extend(["", "### Newly introduced review signals", ""])
    signals, signal_overflow = bounded_rows(summary["newSignals"])
    if signals:
        lines.extend(
            [
                "| Comet | Date | Magnitude | Signal |",
                "| --- | --- | ---: | --- |",
            ]
        )
        for row in signals:
            lines.append(
                f"| {linked_name(row['name'], row.get('url'))} | {escape_markdown(row.get('date'))} | "
                f"{format_magnitude(row.get('magnitude'))} | {escape_markdown(row.get('interpretation'))} |"
            )
        if signal_overflow:
            lines.append(f"\n_{signal_overflow} additional signal(s) omitted._")
    else:
        lines.append("No newly introduced significant brightness signals were detected.")

    transitions, transition_overflow = bounded_rows(summary["visibilityTransitions"])
    if transitions:
        lines.extend(["", "### Visibility-state transitions", ""])
        for row in transitions:
            lines.append(
                f"- {linked_name(row['name'], row.get('url'))}: "
                f"`{escape_markdown(row['before'])}` -> `{escape_markdown(row['after'])}`"
            )
        if transition_overflow:
            lines.append(f"- _{transition_overflow} additional transition(s) omitted._")

    media, media_overflow = bounded_rows(summary["mediaChanges"])
    lines.extend(["", "### Cached imagery", ""])
    if media:
        lines.append(
            "New or changed cached media: "
            + ", ".join(linked_name(row["name"], row.get("url")) for row in media)
            + "."
        )
        if media_overflow:
            lines.append(f"\n_{media_overflow} additional media change(s) omitted._")
    else:
        lines.append("No cached-media assignments changed.")

    brightest, brightest_overflow = bounded_rows(summary["brightest"])
    lines.extend(["", "### Brightest current Aerith entries", ""])
    if brightest:
        lines.extend(["| Comet | Current magnitude |", "| --- | ---: |"])
        for row in brightest:
            lines.append(
                f"| {linked_name(row['name'], row.get('url'))} | {format_magnitude(row['magnitude'])} |"
            )
        if brightest_overflow:
            lines.append(f"\n_{brightest_overflow} additional entry or entries omitted._")
    else:
        lines.append("No current magnitude estimates were available.")

    lines.extend(
        [
            "",
            "> Magnitude comparisons use the weekly table's `currentMagnitude`; positive deltas mean fading because larger astronomical magnitudes are fainter. Significant-signal rows describe newly introduced package data, not an independent AstroGuide scientific classification.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    before_source = read_json_at_ref(args.before_ref, SOURCE_PATH)
    after_source = read_json(SOURCE_PATH)
    before_index = read_json_at_ref(args.before_ref, INDEX_PATH)
    after_index = read_json(INDEX_PATH)
    before_records = load_records(
        before_index,
        lambda path: read_json_at_ref(args.before_ref, path),
    )
    after_records = load_records(after_index, read_json)
    summary = build_summary(before_source, after_source, before_records, after_records)
    output = args.output if args.output.is_absolute() else REPO_ROOT / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_markdown(summary), encoding="utf-8")
    print(f"Wrote Aerith PR summary: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
