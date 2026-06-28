#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
DEFAULT_APP_REPO="$(cd "${REPO_ROOT}/.." && pwd)/DSOPlanneriOS"

BASE_BRANCH="main"
BRANCH_NAME=""
APP_REPO="${DEFAULT_APP_REPO}"
TITLE="Update seasonal recommendation metadata"
COMMIT_MESSAGE="Update seasonal recommendation metadata"
DRY_RUN=0
SKIP_BUILD=0
OPEN_DRAFT=1

usage() {
  cat <<'USAGE'
Usage:
  scripts/propose_seasonal_recommendation_update.sh [options]

Creates or switches to a metadata branch, rebuilds seasonal recommendation
packages from the app repo, validates package/manifest integrity, commits the
scoped metadata changes, pushes the branch, and opens a descriptive GitHub PR.

Options:
  --app-repo PATH        App repository to read catalog/target metadata from.
                         Defaults to sibling ../DSOPlanneriOS.
  --base BRANCH         PR base branch. Defaults to main.
  --branch NAME         Branch to create/use. Defaults to
                         codex/seasonal-recommendations-YYYYMMDD-HHMMSS.
  --title TITLE         PR title. Defaults to "Update seasonal recommendation metadata".
  --commit-message MSG  Commit message. Defaults to the PR title.
  --ready               Open a ready-for-review PR instead of a draft PR.
  --skip-build          Do not run the package generator; commit existing scoped changes.
  --dry-run             Validate and show pending changes, but do not commit/push/PR.
  -h, --help            Show this help.
USAGE
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --app-repo)
      APP_REPO="$2"
      shift 2
      ;;
    --base)
      BASE_BRANCH="$2"
      shift 2
      ;;
    --branch)
      BRANCH_NAME="$2"
      shift 2
      ;;
    --title)
      TITLE="$2"
      shift 2
      ;;
    --commit-message)
      COMMIT_MESSAGE="$2"
      shift 2
      ;;
    --ready)
      OPEN_DRAFT=0
      shift
      ;;
    --skip-build)
      SKIP_BUILD=1
      shift
      ;;
    --dry-run)
      DRY_RUN=1
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

if [[ -z "${BRANCH_NAME}" ]]; then
  BRANCH_NAME="codex/seasonal-recommendations-$(date -u +%Y%m%d-%H%M%S)"
fi

cd "${REPO_ROOT}"

for command_name in git gh python3; do
  if ! command -v "${command_name}" >/dev/null 2>&1; then
    echo "Missing required command: ${command_name}" >&2
    exit 1
  fi
done

if [[ ! -d "${APP_REPO}/App/Resources" ]]; then
  echo "App repo does not look valid: ${APP_REPO}" >&2
  exit 1
fi

if [[ ! -f "${APP_REPO}/App/Resources/Catalog/catalog.sqlite" ]]; then
  echo "App catalog.sqlite not found under: ${APP_REPO}" >&2
  exit 1
fi

if ! gh auth status >/dev/null 2>&1; then
  echo "GitHub CLI is not authenticated. Run gh auth login first." >&2
  exit 1
fi

echo "Fetching origin/${BASE_BRANCH}..."
git fetch origin "${BASE_BRANCH}" --quiet

current_branch="$(git branch --show-current || true)"
if [[ "${current_branch}" != "${BRANCH_NAME}" ]]; then
  if git show-ref --verify --quiet "refs/heads/${BRANCH_NAME}"; then
    echo "Switching to existing branch ${BRANCH_NAME}..."
    git switch "${BRANCH_NAME}"
  else
    if git diff --quiet && git diff --cached --quiet && [[ -z "$(git ls-files --others --exclude-standard)" ]]; then
      echo "Creating ${BRANCH_NAME} from origin/${BASE_BRANCH}..."
      git switch --create "${BRANCH_NAME}" "origin/${BASE_BRANCH}"
    else
      echo "Creating ${BRANCH_NAME} from current HEAD and carrying existing worktree changes..."
      git switch --create "${BRANCH_NAME}"
    fi
  fi
fi

if [[ "${SKIP_BUILD}" -eq 0 ]]; then
  echo "Rebuilding seasonal recommendation packages from ${APP_REPO}..."
  python3 scripts/build_seasonal_recommendation_packages.py --app-repo "${APP_REPO}"
else
  echo "Skipping rebuild; using existing scoped changes."
fi

echo "Validating seasonal package integrity..."
python3 - <<'PY'
import hashlib
import json
from pathlib import Path
from urllib.parse import urlparse

root = Path.cwd()
package_dir = root / "v1/packages/seasonal-recommendations"
manifest_path = root / "v1/channels/stable/manifest.json"
expected_bands = {
    "north_high_60_90n",
    "north_mid_30_60n",
    "north_low_0_30n",
    "south_low_0_30s",
    "south_mid_30_60s",
    "south_high_60_90s",
}

manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
descriptors = [
    package for package in manifest.get("packages", [])
    if package.get("family") == "seasonalRecommendationCandidates"
]
descriptor_by_band = {}
for descriptor in descriptors:
    parsed = urlparse(descriptor.get("packageURL", ""))
    package_name = Path(parsed.path).name
    for band in expected_bands:
        if band in package_name:
            descriptor_by_band[band] = descriptor
            break

missing_descriptors = expected_bands - set(descriptor_by_band)
if missing_descriptors:
    raise SystemExit(f"Missing seasonal manifest descriptors: {sorted(missing_descriptors)}")

for band in sorted(expected_bands):
    path = package_dir / f"seasonal_recommendation_candidates_{band}_v1.json"
    if not path.exists():
        raise SystemExit(f"Missing seasonal package: {path}")
    data = path.read_bytes()
    payload = json.loads(data)
    if payload.get("packageFamily") != "seasonalRecommendationCandidates":
        raise SystemExit(f"Unexpected package family in {path}")
    if payload.get("latitudeBand") != band:
        raise SystemExit(f"Unexpected latitude band in {path}: {payload.get('latitudeBand')}")
    rows = payload.get("rows") or []
    if not rows:
        raise SystemExit(f"No recommendation rows in {path}")
    bad_missing_magnitude = [
        row for row in rows
        if row.get("magnitude") is None and row.get("challengeRating") in {"easy", "moderate"}
    ]
    if bad_missing_magnitude:
        first = bad_missing_magnitude[0]
        raise SystemExit(
            f"Missing-magnitude row published as easy/moderate in {path}: "
            f"{first.get('canonicalID')} {first.get('displayName')}"
        )

    descriptor = descriptor_by_band[band]
    checksum = hashlib.sha256(data).hexdigest()
    if descriptor.get("byteSize") != len(data):
        raise SystemExit(f"Manifest byteSize mismatch for {band}")
    if (descriptor.get("checksum") or {}).get("value") != checksum:
        raise SystemExit(f"Manifest checksum mismatch for {band}")

print("Seasonal package validation passed.")
PY

echo "Checking generated diff..."
git diff --check -- \
  scripts/build_seasonal_recommendation_packages.py \
  scripts/propose_seasonal_recommendation_update.sh \
  v1/channels/stable/manifest.json \
  v1/packages/seasonal-recommendations

git add \
  scripts/build_seasonal_recommendation_packages.py \
  scripts/propose_seasonal_recommendation_update.sh \
  v1/channels/stable/manifest.json \
  v1/packages/seasonal-recommendations

if git diff --cached --quiet; then
  echo "No scoped seasonal metadata changes to commit."
  exit 0
fi

echo "Staged changes:"
git diff --cached --stat

if [[ "${DRY_RUN}" -eq 1 ]]; then
  echo "Dry run requested; leaving changes staged and skipping commit/push/PR."
  exit 0
fi

git commit -m "${COMMIT_MESSAGE}"
git push --set-upstream origin "${BRANCH_NAME}"

app_revision="$(git -C "${APP_REPO}" rev-parse --short HEAD 2>/dev/null || echo "unknown")"
metadata_revision="$(git rev-parse --short HEAD)"
body_file="$(mktemp)"
cat >"${body_file}" <<EOF
## Summary
- Rebuilds all six seasonal recommendation dynamic metadata packages from the app catalog and target metadata.
- Updates the stable channel manifest descriptors, byte sizes, and SHA-256 checksums.
- Keeps missing-magnitude recommendation rows conservative by preventing Easy/Moderate challenge publication for unknown magnitude.

## Validation
- Ran \`scripts/build_seasonal_recommendation_packages.py --app-repo ${APP_REPO}\`.
- Validated every seasonal package has rows, matches its latitude band, and matches the stable manifest checksum/byte size.
- Validated missing-magnitude rows are not published as Easy or Moderate.
- Ran \`git diff --check\` on the scoped metadata files.

## Source
- App repo: \`${APP_REPO}\` at \`${app_revision}\`
- Metadata commit: \`${metadata_revision}\`
EOF

pr_flags=(--base "${BASE_BRANCH}" --head "${BRANCH_NAME}" --title "${TITLE}" --body-file "${body_file}")
if [[ "${OPEN_DRAFT}" -eq 1 ]]; then
  pr_flags+=(--draft)
fi

gh pr create "${pr_flags[@]}"
rm -f "${body_file}"
