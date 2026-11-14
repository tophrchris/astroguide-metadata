"""Reconcile a staged automation manifest against main without rebuilding data."""

import argparse
import hashlib
import json
from pathlib import Path
import subprocess


MANIFEST = "v1/channels/stable/manifest.json"
HOST = "https://metadata.astroguide.space/"
PACKAGE_PATHS = {
    "cometDetailMetadata": "v1/packages/comet-details/comet_detail_metadata_v1.json",
    "transientEventFeed": "v1/packages/transients/transient_opportunities_v1.json",
}
GENERATED_FIELDS = {"packages", "generatedAt", "publishedAt"}


def packages(manifest):
    indexed = {}
    for entry in manifest["packages"]:
        indexed.setdefault(entry["family"], []).append(entry)
    return indexed


def reconcile(base, main, pending, family):
    def header(manifest):
        return {key: value for key, value in manifest.items() if key not in GENERATED_FIELDS}

    if header(base) != header(pending) or header(base) != header(main):
        raise ValueError("Manifest header changed; curator review required")
    old, live, staged = map(packages, (base, main, pending))
    if any(old.get(key) != staged.get(key) for key in (old.keys() | staged.keys()) - {family}):
        raise ValueError("Pending branch changed a package outside its owned family")
    if any(len(entries.get(family, [])) != 1 for entries in (old, live, staged)):
        raise ValueError("Owned family must have exactly one package; curator review required")
    if live[family] != old.get(family) and live[family] != staged[family]:
        raise ValueError("Main and pending branch disagree on the owned package")
    return {
        **main,
        "generatedAt": max(main["generatedAt"], pending["generatedAt"]),
        "publishedAt": max(main["publishedAt"], pending["publishedAt"]),
        "packages": [staged[family][0] if entry["family"] == family else entry for entry in main["packages"]],
    }


def checked_json(root, path, digest, size):
    file = root / path
    if not file.resolve().is_relative_to(root) or not file.is_file():
        raise ValueError(f"Invalid package path: {path}")
    data = file.read_bytes()
    if len(data) != size or hashlib.sha256(data).hexdigest() != digest:
        raise ValueError(f"Package size or checksum mismatch: {path}")
    return json.loads(data)


def validate(root, entry):
    path = PACKAGE_PATHS[entry["family"]]
    if entry["packageURL"] != HOST + path or entry["checksum"]["algorithm"] != "sha256":
        raise ValueError("Unexpected package URL or checksum algorithm")
    payload = checked_json(root, path, entry["checksum"]["value"], entry["byteSize"])
    if entry["family"] == "cometDetailMetadata":
        for shard in payload["comets"]:
            path = shard["path"]
            if path != f"v1/packages/comet-details/shards/{shard['fileName']}" or Path(path).parent.as_posix() != "v1/packages/comet-details/shards":
                raise ValueError(f"Unexpected comet shard path: {path}")
            checked_json(root, path, shard["checksum"], shard["byteSize"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("worktree", type=Path)
    parser.add_argument("family", choices=PACKAGE_PATHS)
    args = parser.parse_args()
    root = args.worktree.resolve()

    def git(*argv):
        return subprocess.check_output(["git", "-C", str(root), *argv], text=True).strip()

    try:
        base = git("merge-base", "HEAD", "MERGE_HEAD")
        merged = reconcile(
            *(json.loads(git("show", f"{ref}:{MANIFEST}")) for ref in (base, "MERGE_HEAD", "HEAD")),
            args.family,
        )
        validate(root, packages(merged)[args.family][0])
        (root / MANIFEST).write_text(json.dumps(merged, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    except (ValueError, KeyError, TypeError, OSError, subprocess.CalledProcessError) as exc:
        parser.exit(1, f"Manifest refresh refused: {exc}\n")


if __name__ == "__main__":
    main()
