#!/usr/bin/env python3
"""Fetch Aerith comet data and regenerate detail metadata when it changes."""

from __future__ import annotations

import argparse
import copy
import datetime as dt
import json
import shutil
from pathlib import Path
from typing import Any

import build_aerith_comet_source as aerith
import build_comet_detail_metadata_package as details


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = REPO_ROOT / "sources/comets/aerith_current_comets_v1.json"
DEFAULT_COMET_SNAPSHOT = REPO_ROOT / "v1/packages/comets/comet_snapshot_v1.json"
DEFAULT_MANIFEST = REPO_ROOT / "v1/channels/stable/manifest.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Refresh Aerith comet source data and rebuild cometDetailMetadata only "
            "when the fetched source content materially changes."
        )
    )
    parser.add_argument("--current-url", default=aerith.DEFAULT_CURRENT_URL)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--comet-snapshot", type=Path, default=DEFAULT_COMET_SNAPSHOT)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--generated-at")
    parser.add_argument("--package-version")
    parser.add_argument("--min-supported-app-version", default="1.4.1")
    parser.add_argument("--min-supported-build", default="1")
    parser.add_argument("--image-limit", type=int, default=50)
    parser.add_argument("--max-image-bytes", type=int, default=500_000)
    parser.add_argument("--fetch-delay-seconds", type=float, default=0.5)
    parser.add_argument("--skip-images", action="store_true")
    parser.add_argument("--single-page", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def utc_now() -> str:
    return dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def read_json(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def material_source(payload: dict[str, Any] | None) -> dict[str, Any] | None:
    if payload is None:
        return None
    normalized = copy.deepcopy(payload)
    normalized.pop("generatedAt", None)
    return normalized


def clean_generated_outputs(remove_assets: bool) -> None:
    shard_dir = REPO_ROOT / details.SHARD_DIR
    asset_dir = REPO_ROOT / details.ASSET_DIR
    if shard_dir.exists():
        shutil.rmtree(shard_dir)
    if remove_assets and asset_dir.exists():
        shutil.rmtree(asset_dir)


def main() -> int:
    args = parse_args()
    generated_at = args.generated_at or utc_now()
    source_path = args.source.resolve()
    comet_snapshot_path = args.comet_snapshot.resolve()
    manifest_path = args.manifest.resolve()

    fetched = aerith.build_source(
        args.current_url,
        fetched_at=generated_at,
        single_page=args.single_page,
    )
    existing = read_json(source_path)
    if material_source(existing) == material_source(fetched):
        print("Aerith comet source has no material changes; skipping package rebuild.")
        return 0

    print(
        "Aerith comet source changed: "
        f"{len((existing or {}).get('comets') or [])} -> {len(fetched.get('comets') or [])} comets."
    )
    if args.dry_run:
        print("Dry run requested; no files written.")
        return 0

    aerith.write_json(source_path, fetched)
    package_version = (
        args.package_version
        or f"comet-detail-metadata-v1-{details.date_token(generated_at)}-aerith"
    )

    clean_generated_outputs(remove_assets=not args.skip_images)
    records = details.build_records(
        details.read_json(comet_snapshot_path),
        fetched,
        generated_at=generated_at,
        cache_images=not args.skip_images,
        image_limit=max(0, args.image_limit),
        max_image_bytes=args.max_image_bytes,
        fetch_delay_seconds=max(0, args.fetch_delay_seconds),
    )
    if not records:
        raise RuntimeError("No comet detail records were generated from the refreshed Aerith source.")

    descriptor = details.write_detail_package(
        records,
        package_version=package_version,
        generated_at=generated_at,
        min_supported_app_version=args.min_supported_app_version,
        min_supported_build=args.min_supported_build,
        update_manifest_path=manifest_path,
    )
    print(
        f"{details.PACKAGE_FAMILY}: {descriptor['packageVersion']} "
        f"{descriptor['recordCount']} comets {descriptor['byteSize']} bytes"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
