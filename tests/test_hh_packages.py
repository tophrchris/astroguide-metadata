import copy
import contextlib
import csv
import importlib.util
import json
import io
import math
import os
import tempfile
import unittest
from unittest import mock
from types import SimpleNamespace
from pathlib import Path

import numpy as np
from astropy.coordinates import SkyCoord
import astropy.units as u
from jsonschema.exceptions import ValidationError

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("hh_builder", ROOT / "scripts/build_hh_packages.py")
hh = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hh)


def source_rights():
    return {"sources": {"synthetic": {"status": "cleared", "license": "test-only",
                            "evidenceURL": "https://example.invalid/rights",
                            "allowedFields": ["core", "prose", "distance", "media"]}}}


def record(number=1, component=False, located=True):
    parent = f"hh:{number}"
    return {"id": parent + ":component:synthetic-1" if component else parent,
            "group": parent, "parentID": parent if component else None,
            "name": f"HH {number}" + ("A" if component else ""), "aliases": [],
            "kind": "component" if component else "parent",
            "classification": {"source": "synthetic", "mainType": "HH", "status": "candidate",
                               "conflict": False, "confirmation": "synthetic test only"},
            "position": hh.position(0, 0, "component_center" if component else "parent_center") if located else None,
            "provenance": [{"source": "synthetic", "sourceID": "1", "retrievedAt": "2026-10-04",
                            "inputSHA256": "0" * 64, "sourceURL": "https://example.invalid/test"}]}


def fixture_packages():
    records, links, _ = hh.eligibility(hh.assemble([record(), record(component=True)]),
                                      {"NGC1": ["NGC1", "M1"], "NGC2": ["NGC2"]},
                                      {"NGC1": hh.position(0, 0), "M1": hh.position(.1, 0), "NGC2": None})
    return {"core": {"schemaVersion": 1, "packageVersion": "fixture-only",
                     "catalog": {"version": "fixture", "sha256": "0" * 64, "fingerprint": "0" * 64,
                                 "identityMapSHA256": "0" * 64, "identityPolicy": "fixture-only", "rowCount": 3},
                     "footprint": hh.FOOTPRINT, "records": records, "dsoLinks": links},
            "enrichment": {"schemaVersion": 1, "packageVersion": "fixture-enrichment", "records": []},
            "media": {"schemaVersion": 1, "packageVersion": "fixture-media", "records": []}}


class GeometryTests(unittest.TestCase):
    def test_wrap_pole_and_back_hemisphere(self):
        self.assertTrue(hh.contained((359.9, 0), [(0.1, 0)])[0])
        self.assertTrue(hh.contained((0, 89), [(90, 89)])[0])
        self.assertFalse(hh.contained((0, 0), [(180, 0)])[0])
        self.assertFalse(hh.contained((0, 0), [(1.13, 0)])[0])

    def test_rectangle_edges_and_corners(self):
        corner = (math.degrees(math.atan(math.tan(math.radians(1.12)))),
                  math.degrees(math.atan(math.tan(math.radians(1.995)) * math.cos(math.radians(1.12)))))
        self.assertTrue(hh.contained((0, 0), [corner])[0])
        self.assertTrue(hh.contained((0, 0), [(0, 1.995)])[0])
        self.assertFalse(hh.contained((0, 0), [(0, 1.99501)])[0])

    def test_independent_astropy_projection(self):
        rng = np.random.default_rng(84)
        for ra, dec in [(359.5, 0), (32, 89), (93, -89), (44, 31)]:
            points = [(float(a % 360), float(np.clip(d, -90, 90)))
                      for a, d in zip(rng.uniform(ra - 100, ra + 100, 200), rng.uniform(dec - 3, dec + 3, 200))]
            origin = SkyCoord(ra * u.deg, dec * u.deg)
            off = SkyCoord(np.array(points)[:, 0] * u.deg, np.array(points)[:, 1] * u.deg).transform_to(origin.skyoffset_frame())
            x = np.tan(off.lon.radian)
            y = np.tan(off.lat.radian) / np.cos(off.lon.radian)
            expected = ((np.cos(off.lon.radian) * np.cos(off.lat.radian) > 0)
                        & (abs(x) <= math.tan(math.radians(1.12)) + 1e-12)
                        & (abs(y) <= math.tan(math.radians(1.995)) + 1e-12))
            np.testing.assert_array_equal(expected, hh.contained((ra, dec), points))

    def test_invalid_positions(self):
        for ra, dec in [(float("nan"), 0), (0, 91), (360, 0), (None, None)]:
            self.assertIsNone(hh.position(ra, dec))


class IdentityTests(unittest.TestCase):
    def test_components_count_once_and_unknown_is_null(self):
        packages = fixture_packages()
        links = {r["targetID"]: r for r in packages["core"]["dsoLinks"]}
        self.assertEqual(links["NGC1"]["hhIDs"], ["hh:1"])
        self.assertEqual(links["M1"]["hhIDs"], ["hh:1"])
        self.assertIsNone(links["NGC2"]["hhIDs"])
        hh.validate_packages(packages, source_rights())

    def test_proxy_and_ids_stable_after_coordinate_change(self):
        component = record(component=True)
        one = hh.assemble([component])
        component["position"] = hh.position(1, 1)
        two = hh.assemble([component])
        self.assertEqual([r["id"] for r in one], [r["id"] for r in two])
        self.assertEqual(one[0]["position"]["role"], "representative_component_proxy")

    def test_order_does_not_change_output(self):
        records = [record(), record(component=True), record(2)]
        self.assertEqual(hh.encoded(hh.assemble(records)), hh.encoded(hh.assemble(list(reversed(records)))))

    def test_unlocated_hh_is_reported_not_eligible(self):
        eligible, _, counts = hh.eligibility(hh.assemble([record(located=False)]), {"M1": ["M1"]}, {"M1": hh.position(0, 0)})
        self.assertEqual(eligible, [])
        self.assertEqual(counts["unlocatedGroups"], 1)
        self.assertEqual(counts["histogram"], {"0": 1})

    def test_primary_classification_and_ambiguous_parent_quarantine(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "simbad.csv"
            with path.open("w", newline="") as stream:
                writer = csv.DictWriter(stream, fieldnames=["oid", "main_id", "ra", "dec", "otype", "ids"])
                writer.writeheader()
                writer.writerows([
                    dict(oid=1, main_id="HH 1A", ra=0, dec=0, otype="HH", ids="HH 1A"),
                    dict(oid=2, main_id="HH 2", ra=0, dec=0, otype="Y*O", ids="HH 2"),
                    dict(oid=3, main_id="HH 3", ra=0, dec=0, otype="HH", ids="HH 3|HH 4")])
            records, conflicts = hh.read_simbad(path, "2026-10-04")
            self.assertEqual(len(records), 1)
            self.assertEqual(records[0]["id"], "hh:1:component:simbad-1")
            self.assertEqual(len(conflicts), 2)
            historical = record(2)
            self.assertTrue(hh.assemble([historical], conflicts)[0]["classification"]["conflict"])


class ValidationTests(unittest.TestCase):
    def test_core_only_and_empty_optional_are_valid(self):
        hh.validate_packages(fixture_packages(), source_rights())

    def test_unknown_join_and_orphan_component(self):
        packages = fixture_packages()
        packages["core"]["records"][1]["parentID"] = "hh:999"
        with self.assertRaisesRegex(ValueError, "orphan"):
            hh.validate_packages(packages, source_rights())

    def test_unknown_is_not_zero(self):
        packages = fixture_packages()
        packages["core"]["dsoLinks"][-1]["hhIDs"] = []
        with self.assertRaisesRegex(ValueError, "unknown"):
            hh.validate_packages(packages, source_rights())

    def test_uncleared_source_rejected(self):
        with self.assertRaisesRegex(ValueError, "uncleared"):
            hh.validate_packages(fixture_packages(), {"sources": {}})

    def test_hidden_uncleared_position_alternative_rejected(self):
        packages = fixture_packages()
        packages["core"]["records"][0]["positionAlternatives"][0] = copy.deepcopy(
            packages["core"]["records"][0]["positionAlternatives"][0])
        packages["core"]["records"][0]["positionAlternatives"][0]["provenance"][0]["source"] = "Chen2026"
        with self.assertRaisesRegex(ValueError, "uncleared position alternative"):
            hh.validate_packages(packages, source_rights())

    def test_withdrawal_and_field_rights(self):
        rights = source_rights()
        self.assertFalse(hh.source_allowed(rights, "synthetic", "core", {"synthetic"}))
        self.assertFalse(hh.source_allowed(rights, "synthetic", "excitingSources"))
        rights["sources"]["synthetic"]["status"] = "unresolved"
        self.assertFalse(hh.source_allowed(rights, "synthetic", "core"))

    def test_optional_enrichment_independent_version(self):
        packages = fixture_packages()
        field = {"value": "Synthetic prose only", "source": "synthetic", "sourceURL": "https://example.invalid/test",
                 "credit": "Synthetic", "license": "test-only", "basis": "test only"}
        packages["enrichment"]["records"] = [{"id": "hh:1", "fields": {"prose": field}}]
        hh.validate_packages(packages, source_rights())
        packages["enrichment"]["records"][0]["id"] = "hh:999"
        with self.assertRaisesRegex(ValueError, "join"):
            hh.validate_packages(packages, source_rights())

    def test_optional_field_exclusion_does_not_remove_core(self):
        record_input = [{"id": "hh:1", "fields": {"prose": {"source": "synthetic"}}}]
        self.assertEqual(hh.optional_records(record_input, "enrichment", {"hh:1"}, source_rights(), {"synthetic"}), [])
        self.assertEqual(len(fixture_packages()["core"]["records"]), 2)

    def test_invalid_coordinate_and_unexpected_field(self):
        for field, value in [("position", hh.position(0, 0)), ("extra", "oops")]:
            packages = fixture_packages()
            packages["core"]["records"][0][field] = value
            if field == "position":
                packages["core"]["records"][0][field]["decDeg"] = 91
            with self.assertRaises(ValidationError):
                hh.validate_packages(packages, source_rights())

    def test_manifest_hash_and_path_validation(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp)
            hh.write_packages(path, fixture_packages(), source_rights())
            before = (path / "manifest.json").read_bytes()
            hh.write_packages(path, fixture_packages(), source_rights())
            self.assertEqual(before, (path / "manifest.json").read_bytes())
            (path / "hh-core-v1.json").write_bytes(b"{}")
            with self.assertRaisesRegex(ValueError, "size"):
                hh.validate_directory(path, source_rights())

    def test_checksum_same_size_corruption(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp)
            hh.write_packages(path, fixture_packages(), source_rights())
            payload = path / "hh-core-v1.json"
            payload.write_bytes(payload.read_bytes().replace(b"NGC1", b"NGC9"))
            with self.assertRaisesRegex(ValueError, "checksum"):
                hh.validate_directory(path, source_rights())

    def test_limit_is_enforced(self):
        with mock.patch.dict(hh.LIMITS, core=1):
            with self.assertRaisesRegex(ValueError, "size limit"):
                hh.validate_packages(fixture_packages(), source_rights())

    def test_alias_inconsistency_rejected(self):
        packages = fixture_packages()
        packages["core"]["dsoLinks"][0]["hhIDs"] = []
        with self.assertRaisesRegex(ValueError, "alias count"):
            hh.validate_packages(packages, source_rights())

    def test_image_found_not_reusable_and_dedup(self):
        assets = [{"id": "hh:1", "assetID": "a", "role": "dedicated", "reuseVerified": False,
                   "identityVerified": True, "source": "synthetic"}]
        result = hh.image_audit({"hh:1", "hh:2"}, assets, source_rights(), [])
        self.assertEqual(result["foundHHs"], 1)
        self.assertEqual(result["reusableHHs"], 0)
        self.assertEqual(result["noVerifiedReusableImage"], 2)

    def test_checked_in_schemas_are_valid(self):
        for family in hh.LIMITS:
            hh.Draft202012Validator.check_schema(hh.load(hh.SOURCE / f"hh-{family}-v1.schema.json"))

    def test_hosted_output_forbidden(self):
        with self.assertRaisesRegex(ValueError, "hosted"):
            hh.write_packages(ROOT / "v1/never-write-hh", fixture_packages(), source_rights())


@unittest.skipUnless(os.environ.get("HH_RESEARCH"), "set HH_RESEARCH for pinned local-input integration tests")
class LocalResearchTests(unittest.TestCase):
    def build_args(self, temporary, excluded):
        return SimpleNamespace(research=Path(os.environ["HH_RESEARCH"]), catalog=Path(os.environ["HH_CATALOG"]),
                               rights=hh.SOURCE / "rights.json", pins=hh.SOURCE / "input-pins.json",
                               enrichment=hh.SOURCE / "enrichment.json", media=hh.SOURCE / "media-candidates.json",
                               exclude_source=excluded, version="local-test", enrichment_version=None, media_version=None,
                               output=Path(temporary) / "review", audit_output=Path(temporary) / "audit.json")

    def test_core_rebuild_without_historical_reader(self):
        with tempfile.TemporaryDirectory() as temporary:
            args = self.build_args(temporary, ["V104"])
            with mock.patch.object(hh, "read_v104", side_effect=AssertionError("withdrawn source read")):
                with contextlib.redirect_stdout(io.StringIO()):
                    hh.build(args)
            packages = hh.validate_directory(args.output, hh.load(args.rights), args.exclude_source)
            self.assertEqual(len(packages["core"]["records"]), 2889)
            self.assertEqual(len(packages["enrichment"]["records"]), 2)
            self.assertEqual(len(packages["media"]["records"]), 3)

    def test_all_core_sources_withdrawn(self):
        with tempfile.TemporaryDirectory() as temporary:
            args = self.build_args(temporary, ["SIMBAD", "V104"])
            with mock.patch.object(hh, "read_simbad", side_effect=AssertionError("withdrawn source read")):
                with mock.patch.object(hh, "read_v104", side_effect=AssertionError("withdrawn source read")):
                    with contextlib.redirect_stdout(io.StringIO()):
                        hh.build(args)
            packages = hh.validate_directory(args.output, hh.load(args.rights), args.exclude_source)
            self.assertTrue(all(not package["records"] for package in packages.values()))
            self.assertEqual(len(packages["core"]["dsoLinks"]), 7622)
            unknown = [link for link in packages["core"]["dsoLinks"] if link["status"] == "unknown"]
            self.assertEqual(len({link["identityID"] for link in unknown}), 105)

    def test_independent_census_and_fk4_transform(self):
        research = Path(os.environ["HH_RESEARCH"])
        provenance = hh.load(research / "provenance.json")
        simbad, conflicts = hh.read_simbad(research / "private_sources/simbad_full.csv", "2026-10-04")
        _, named_conflicts = hh.read_simbad(research / "private_sources/simbad_hh_named.csv", "2026-10-04")
        conflicts.extend(named_conflicts)
        historical = hh.read_v104(research / "private_sources/V104_catalog.dat", "2026-10-04")
        self.assertEqual(len(historical), 454)
        self.assertEqual(historical[0]["position"]["inputFrame"], "FK4/B1950")
        pin = next(v["sha256"] for k, v in provenance["files"].items() if k.endswith("catalog.sqlite"))
        catalog = os.environ["HH_CATALOG"]
        groups, dsos, _, _ = hh.read_catalog(catalog, research / "dso_identity_groups.csv", pin)
        _, _, counts = hh.eligibility(hh.assemble(simbad + historical, conflicts), groups, dsos)
        self.assertEqual(counts["dsoIdentities"], 6410)
        self.assertEqual(counts["locatedDSOIdentities"], 6305)
        self.assertEqual(counts["unknownDSOIdentities"], 105)
        self.assertEqual(counts["coveredGroups"], 1249)
        self.assertEqual(counts["pairs"], 17739)
        self.assertEqual(counts["hitDSOIdentities"], 1325)
        self.assertEqual(counts["samples"]["NGC281"], 0)
        self.assertEqual(counts["samples"]["M8"], counts["samples"]["M20"])
        self.assertEqual(sum(counts["histogram"].values()), 6305)
        self.assertEqual(sum(int(k) * v for k, v in counts["histogram"].items()), counts["pairs"])
        reference = {r["name"]: r for r in hh.rows(research / "private_sources/parsed_hh_centers.csv") if r["source"] == "V104"}
        for row in historical:
            self.assertAlmostEqual(row["position"]["raDeg"], float(reference[row["name"]]["ra"]), places=10)
            self.assertAlmostEqual(row["position"]["decDeg"], float(reference[row["name"]]["dec"]), places=10)


if __name__ == "__main__":
    unittest.main()
