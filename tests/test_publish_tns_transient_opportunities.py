import importlib.util
import sys
import unittest
from pathlib import Path


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1]
    / "scripts"
    / "publish_tns_transient_opportunities.py"
)
SPEC = importlib.util.spec_from_file_location("publish_tns_transient_opportunities", SCRIPT_PATH)
publish = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = publish
assert SPEC.loader is not None
SPEC.loader.exec_module(publish)


class PublishTNSTransientOpportunitiesTests(unittest.TestCase):
    def test_empty_approved_feed_is_valid(self):
        package = publish.normalize_package(
            {
                "schemaVersion": 1,
                "family": "transientOpportunities",
                "reviewOnly": False,
                "asOfDate": "2026-09-20",
                "counts": {"approved": 0},
                "opportunities": [],
            }
        )

        self.assertEqual(package["opportunities"], [])
        self.assertEqual(package["packageFamily"], "transientEventFeed")

    def test_opportunities_must_be_a_list(self):
        with self.assertRaises(publish.ValidationError):
            publish.normalize_package(
                {
                    "schemaVersion": 1,
                    "family": "transientOpportunities",
                    "reviewOnly": False,
                    "opportunities": None,
                }
            )


if __name__ == "__main__":
    unittest.main()
