#!/usr/bin/env python3
import argparse
import datetime as dt
import html
import json
import re
import urllib.request
from pathlib import Path
from typing import Any
from urllib.parse import urljoin


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = REPO_ROOT / "sources/comets/aerith_current_comets_v1.json"
DEFAULT_CURRENT_URL = "http://www.aerith.net/comet/weekly/current.html"
USER_AGENT = "AstroGuide metadata audit/1.0 (permission request in progress)"

MONTHS = {
    "Jan.": 1,
    "Feb.": 2,
    "Mar.": 3,
    "Apr.": 4,
    "May": 5,
    "Jun.": 6,
    "Jul.": 7,
    "Aug.": 8,
    "Sep.": 9,
    "Oct.": 10,
    "Nov.": 11,
    "Dec.": 12,
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a normalized Aerith weekly comet source snapshot for AstroGuide review."
    )
    parser.add_argument("--current-url", default=DEFAULT_CURRENT_URL)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--fetched-at")
    parser.add_argument(
        "--single-page",
        action="store_true",
        help="Only parse --current-url instead of also following the linked opposite hemisphere page.",
    )
    return parser.parse_args()


def utc_now() -> str:
    return dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def read_url(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8", errors="replace")


def write_json(path: Path, payload: dict[str, Any]) -> bytes:
    data = (json.dumps(payload, indent=2, ensure_ascii=True) + "\n").encode("utf-8")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return data


def strip_tags(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def normalize_comet_key(value: str) -> str:
    text = html.unescape(value or "").strip().upper()
    text = re.sub(r"\s+", " ", text)

    numbered = re.match(r"^0*(\d+P)\b", text)
    if numbered:
        return numbered.group(1)

    modern = re.match(r"^([ACPDI]/\d{4})\s+([A-Z]\d+)", text)
    if modern:
        return f"{modern.group(1)}{modern.group(2)}"

    parenthesized = re.match(r"^\((\d+)\)", text)
    if parenthesized:
        return parenthesized.group(1)

    first_token = re.split(r"[\s(]", text, maxsplit=1)[0]
    return re.sub(r"[^A-Z0-9/]", "", first_token)


def parse_page_context(document: str) -> dict[str, Any]:
    title = strip_tags(re.search(r"<TITLE>(.*?)</TITLE>", document, re.I | re.S).group(1))
    updated_match = re.search(r"Updated on\s+([^<]+)", document, re.I)
    page_date_match = re.search(
        r"\((\d{4})\s+([A-Z][a-z]{2}\.?)\s+(\d+):\s+(North|South)\)",
        title,
    )
    if not page_date_match:
        raise RuntimeError(f"Could not parse Aerith page date from title: {title}")

    month_label = page_date_match.group(2)
    if month_label == "May.":
        month_label = "May"

    return {
        "title": title,
        "pageDate": dt.date(
            int(page_date_match.group(1)),
            MONTHS[month_label],
            int(page_date_match.group(3)),
        ),
        "hemisphere": page_date_match.group(4).lower(),
        "updatedText": strip_tags(updated_match.group(1)) if updated_match else None,
    }


def discover_link(document: str, base_url: str, link_text: str) -> str | None:
    pattern = re.compile(
        rf"<A\s+HREF=\"([^\"]+)\">\s*{re.escape(link_text)}\s*</A>",
        re.I,
    )
    match = pattern.search(document)
    if not match:
        return None
    return urljoin(base_url, html.unescape(match.group(1)))


def row_date(page_date: dt.date, month_label: str, day: int) -> str:
    month = MONTHS[month_label]
    year = page_date.year
    delta = month - page_date.month
    if delta < -6:
        year += 1
    elif delta > 6:
        year -= 1
    return dt.date(year, month, day).isoformat()


def parse_pre_rows(pre_text: str, page_date: dt.date) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    row_pattern = re.compile(
        r"^(?P<month>[A-Z][a-z]{2}\.?)\s+"
        r"(?P<day>\d+)\s+"
        r"(?P<rah>\d+)\s+(?P<ram>\d+(?:\.\d+)?)\s+"
        r"(?P<decd>-?\d+)\s+(?P<decm>\d+(?:\.\d+)?)\s+"
        r"(?P<delta>\d+(?:\.\d+)?)\s+"
        r"(?P<r>\d+(?:\.\d+)?)\s+"
        r"(?P<elong>-?\d+(?:\.\d+)?)\s+"
        r"(?P<m1>-?\d+(?:\.\d+)?)\s+"
        r"(?P<best>\d+:\d+)\s+"
        r"\(\s*(?P<az>-?\d+(?:\.\d+)?),\s*(?P<alt>-?\d+(?:\.\d+)?)\s*\)",
    )
    for line in html.unescape(pre_text).splitlines():
        match = row_pattern.match(line.strip())
        if not match:
            continue
        month_label = match.group("month")
        if month_label == "May.":
            month_label = "May"
        declination_degrees = float(match.group("decd"))
        declination_minutes = float(match.group("decm"))
        declination_sign = -1.0 if declination_degrees < 0 else 1.0
        rows.append(
            {
                "date": row_date(page_date, month_label, int(match.group("day"))),
                "rightAscensionHours": round(
                    float(match.group("rah")) + float(match.group("ram")) / 60.0,
                    8,
                ),
                "declinationDegrees": round(
                    declination_degrees + declination_sign * declination_minutes / 60.0,
                    8,
                ),
                "geocentricDistanceAU": float(match.group("delta")),
                "heliocentricDistanceAU": float(match.group("r")),
                "elongationDegrees": float(match.group("elong")),
                "magnitude": float(match.group("m1")),
                "bestTimeLocal": match.group("best"),
                "bestAzimuthDegreesFromSouth": float(match.group("az")),
                "bestAltitudeDegrees": float(match.group("alt")),
            }
        )
    return rows


def parse_reported_magnitudes(text: str) -> list[dict[str, Any]]:
    reports: list[dict[str, Any]] = []
    for match in re.finditer(r"(\d+(?:\.\d+)?)\s+mag\s+\(([^)]+)\)", text):
        context = match.group(2).strip()
        parts = [part.strip() for part in context.split(",", maxsplit=1)]
        reports.append(
            {
                "magnitude": float(match.group(1)),
                "reportedDateText": parts[0] if parts else context,
                "observer": parts[1] if len(parts) > 1 else None,
            }
        )
    return reports


def parse_entries(document: str, page_url: str) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    context = parse_page_context(document)
    blocks = re.split(r"<H2\b", document, flags=re.I)[1:]
    entries: list[dict[str, Any]] = []
    for rank, block in enumerate(blocks, start=1):
        h2_fragment = "<H2" + block
        heading_match = re.search(r"<A\s+HREF=\"([^\"]+)\">(.*?)</A>\s*</H2>", h2_fragment, re.I | re.S)
        pre_match = re.search(r"<PRE>(.*?)</PRE>", h2_fragment, re.I | re.S)
        if not heading_match or not pre_match:
            continue

        name = strip_tags(heading_match.group(2))
        detail_url = urljoin(page_url, html.unescape(heading_match.group(1)))
        image_sources = [
            html.unescape(source)
            for source in re.findall(r"<IMG\s+SRC=\"([^\"]+)\"", h2_fragment, re.I)
        ]
        comet_image_source = next(
            (source for source in image_sources if "/pictures/" in source or "pictures/" in source),
            image_sources[0] if image_sources else None,
        )
        image_url = urljoin(page_url, comet_image_source) if comet_image_source else None
        paragraphs = " ".join(
            strip_tags(match)
            for match in re.findall(r"<P>(.*?)</P>", h2_fragment, re.I | re.S)
        )
        weekly_rows = parse_pre_rows(pre_match.group(1), context["pageDate"])
        reports = parse_reported_magnitudes(paragraphs)

        entries.append(
            {
                "aerithName": name,
                "normalizedDesignation": normalize_comet_key(name),
                "hemisphere": context["hemisphere"],
                "pageRank": rank,
                "sourcePageURL": page_url,
                "detailURL": detail_url,
                "thumbnailImageURL": image_url,
                "reportedMagnitudes": reports,
                "weeklyRows": weekly_rows,
                "currentMagnitude": weekly_rows[0]["magnitude"] if weekly_rows else None,
                "nextWeekMagnitude": weekly_rows[1]["magnitude"] if len(weekly_rows) > 1 else None,
            }
        )
    context["entryCount"] = len(entries)
    return context, entries


def merge_entries(entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    merged: dict[str, dict[str, Any]] = {}
    for entry in entries:
        key = entry["normalizedDesignation"]
        existing = merged.setdefault(
            key,
            {
                "aerithName": entry["aerithName"],
                "normalizedDesignation": key,
                "hemispheres": [],
                "pageRanks": {},
                "sourcePageURLs": {},
                "detailURL": entry.get("detailURL"),
                "thumbnailImageURL": entry.get("thumbnailImageURL"),
                "imagePermissionStatus": "permission-requested",
                "imageAttribution": (
                    "Candidate image from Aerith weekly comet page; do not publish "
                    "or promote to app hero imagery until permission is granted."
                ),
                "reportedMagnitudes": [],
                "weeklyRowsByHemisphere": {},
                "currentMagnitude": None,
                "nextWeekMagnitude": None,
            },
        )
        hemisphere = entry["hemisphere"]
        if hemisphere not in existing["hemispheres"]:
            existing["hemispheres"].append(hemisphere)
        existing["pageRanks"][hemisphere] = entry["pageRank"]
        existing["sourcePageURLs"][hemisphere] = entry["sourcePageURL"]
        existing["weeklyRowsByHemisphere"][hemisphere] = entry["weeklyRows"]
        existing["reportedMagnitudes"].extend(entry.get("reportedMagnitudes") or [])
        existing["detailURL"] = existing.get("detailURL") or entry.get("detailURL")
        existing["thumbnailImageURL"] = existing.get("thumbnailImageURL") or entry.get("thumbnailImageURL")
        if existing["currentMagnitude"] is None:
            existing["currentMagnitude"] = entry.get("currentMagnitude")
        if existing["nextWeekMagnitude"] is None:
            existing["nextWeekMagnitude"] = entry.get("nextWeekMagnitude")

    return sorted(
        merged.values(),
        key=lambda row: min(row["pageRanks"].values()) if row["pageRanks"] else 9999,
    )


def build_source(current_url: str, *, fetched_at: str, single_page: bool = False) -> dict[str, Any]:
    pages: list[dict[str, Any]] = []
    all_entries: list[dict[str, Any]] = []
    documents = [(current_url, read_url(current_url))]
    if not single_page:
        south_url = discover_link(documents[0][1], current_url, "South")
        if south_url and south_url != current_url:
            documents.append((south_url, read_url(south_url)))

    for page_url, document in documents:
        context, entries = parse_entries(document, page_url)
        context["url"] = page_url
        serializable_context = dict(context)
        serializable_context["pageDate"] = context["pageDate"].isoformat()
        pages.append(serializable_context)
        all_entries.extend(entries)

    return {
        "schemaVersion": 1,
        "generatedAt": fetched_at,
        "source": {
            "name": "Aerith Weekly Information about Bright Comets",
            "sourceURL": current_url,
            "owner": "Seiichi Yoshida",
            "contact": "comet@aerith.net",
            "permissionStatus": "permission-requested",
            "notes": (
                "Normalized source snapshot for AstroGuide comet metadata review. "
                "Brightness estimates may be used to patch hosted comet magnitudes. "
                "Image URLs are retained as candidates only until publication permission is granted."
            ),
        },
        "pages": pages,
        "comets": merge_entries(all_entries),
    }


def main() -> int:
    args = parse_args()
    payload = build_source(
        args.current_url,
        fetched_at=args.fetched_at or utc_now(),
        single_page=args.single_page,
    )
    data = write_json(args.output, payload)
    print(f"Aerith comet source: {len(payload['comets'])} comets {len(data)} bytes -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
