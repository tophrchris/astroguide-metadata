import importlib.util
import sys
import unittest
from pathlib import Path


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1]
    / "scripts"
    / "summarize_aerith_comet_update.py"
)
SPEC = importlib.util.spec_from_file_location("summarize_aerith_comet_update", SCRIPT_PATH)
summary = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = summary
assert SPEC.loader is not None
SPEC.loader.exec_module(summary)


def source(comets, page_date):
    return {
        "pages": [{"pageDate": page_date}],
        "comets": comets,
    }


def comet(designation, magnitude, *, name=None, url=None):
    return {
        "normalizedDesignation": designation,
        "aerithName": name or designation,
        "detailURL": url or f"https://www.aerith.net/comet/{designation}",
        "currentMagnitude": magnitude,
    }


def record(
    stable_id,
    *,
    state="current",
    media_path=None,
    points=None,
    name=None,
):
    media = {}
    if media_path:
        media = {"thumbnail": {"cachedPath": media_path}}
    return {
        "stableID": stable_id,
        "displayName": name or stable_id,
        "detailURL": f"https://www.aerith.net/comet/{stable_id}",
        "visibilitySummary": {"state": state},
        "media": media,
        "brightness": points or [],
    }


class AerithUpdateSummaryTests(unittest.TestCase):
    def test_build_summary_highlights_material_reviewer_changes(self):
        before_source = source(
            [
                comet("10P", 8.6, name="10P/Tempel"),
                comet("OLD", 15.0),
            ],
            "2026-09-05",
        )
        after_source = source(
            [
                comet("10P", 7.1, name="10P/Tempel"),
                comet("NEW", 12.0),
            ],
            "2026-09-12",
        )
        before_records = [record("COMET:10P", state="comingSoon", media_path="old.jpg")]
        after_records = [
            record(
                "COMET:10P",
                state="current",
                media_path="new.jpg",
                points=[
                    {
                        "id": "10P-new-signal",
                        "date": "2026-09-12",
                        "magnitude": 7.1,
                        "magnitudeDelta": -1.5,
                        "isSignificant": True,
                        "interpretation": "Brightened 1.5 mag.",
                    }
                ],
                name="10P/Tempel",
            )
        ]

        result = summary.build_summary(
            before_source,
            after_source,
            before_records,
            after_records,
        )

        self.assertEqual([entry["normalizedDesignation"] for entry in result["added"]], ["NEW"])
        self.assertEqual([entry["normalizedDesignation"] for entry in result["removed"]], ["OLD"])
        self.assertEqual(result["magnitudeChanges"][0]["delta"], -1.5)
        self.assertEqual(result["newSignals"][0]["magnitude"], 7.1)
        self.assertEqual(result["visibilityTransitions"][0]["after"], "current")
        self.assertEqual(result["mediaChanges"][0]["stableID"], "COMET:10P")

        markdown = summary.render_markdown(result)
        self.assertIn("Brightened 1.5 mag", markdown)
        self.assertIn("`comingSoon` -> `current`", markdown)
        self.assertIn("New or changed cached media", markdown)
        self.assertIn("10P/Tempel", markdown)

    def test_render_summary_has_explicit_empty_states(self):
        unchanged_source = source([comet("10P", 8.6)], "2026-09-05")
        unchanged_records = [record("COMET:10P")]

        result = summary.build_summary(
            unchanged_source,
            unchanged_source,
            unchanged_records,
            unchanged_records,
        )
        markdown = summary.render_markdown(result)

        self.assertIn("**Added:** None", markdown)
        self.assertIn("**Removed:** None", markdown)
        self.assertIn("No newly introduced significant brightness signals", markdown)
        self.assertIn("No cached-media assignments changed", markdown)


if __name__ == "__main__":
    unittest.main()
