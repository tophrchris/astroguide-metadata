"""Evaluate a local queue and registry to stdout, never publish or fetch sources."""
import argparse
import json
from pathlib import Path

from apply_tns_transient_review_decisions import sync_decisions
from transient_early_policy import date


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("queue", type=Path)
    parser.add_argument("--registry", type=Path, required=True)
    parser.add_argument("--generated-at", required=True)
    args = parser.parse_args()
    if date(args.generated_at) is None:
        parser.error("--generated-at requires a timezone-aware ISO-8601 timestamp")
    queue = json.loads(args.queue.read_text())
    registry = json.loads(args.registry.read_text())
    candidates = {item["id"]: item for item in queue["opportunities"]}
    provenance = {key: {"sourceReviewQueue": str(args.queue),
                        "reviewSetID": queue["reviewSetID"], "asOfDate": queue["asOfDate"]}
                  for key in candidates}
    evaluated = sync_decisions(registry, None, candidates, provenance,
                               generated_at=args.generated_at, early_opportunities=True)
    print(json.dumps({"localPreviewOnly": True, "registry": evaluated,
                      "candidates": list(candidates.values())}, indent=2))


if __name__ == "__main__":
    main()
