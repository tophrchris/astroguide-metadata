import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts.reconcile_metadata_manifest import HOST, PACKAGE_PATHS, reconcile, validate


TNS = "transientEventFeed"
AERITH = "cometDetailMetadata"


def manifest(tns=1, aerith=1, time="2026-11-07T00:00:00Z"):
    return {
        "schemaVersion": 1,
        "channel": "stable",
        "generatedAt": time,
        "publishedAt": time,
        "packages": [
            {"family": TNS, "packageVersion": tns},
            {"family": AERITH, "packageVersion": aerith},
        ],
    }


class ReconcileManifestTests(unittest.TestCase):
    def test_both_merge_orders_keep_both_updates(self):
        newer = "2026-11-09T00:00:00Z"
        for live, staged, family in [
            (manifest(aerith=2, time=newer), manifest(tns=2), TNS),
            (manifest(tns=2), manifest(aerith=2, time=newer), AERITH),
        ]:
            with self.subTest(family=family):
                self.assertEqual(reconcile(manifest(), live, staged, family), manifest(2, 2, newer))

    def test_refuses_competing_changes_to_same_family(self):
        with self.assertRaisesRegex(ValueError, "disagree"):
            reconcile(manifest(), manifest(tns=2), manifest(tns=3), TNS)

    def test_refuses_staged_edits_to_unowned_family(self):
        with self.assertRaisesRegex(ValueError, "outside"):
            reconcile(manifest(), manifest(), manifest(2, 2), TNS)

    def test_preserves_main_package_variants(self):
        live = manifest()
        variants = [
            {"family": "anotherPackage", "packageURL": "north.json"},
            {"family": "anotherPackage", "packageURL": "south.json"},
        ]
        live["packages"].extend(variants)
        self.assertEqual(reconcile(manifest(), live, manifest(tns=2), TNS)["packages"][-2:], variants)

    def test_checks_staged_payload_bytes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            path = PACKAGE_PATHS[TNS]
            file = root / path
            file.parent.mkdir(parents=True)
            data = b'{"opportunities":[]}'
            file.write_bytes(data)
            entry = {
                "family": TNS, "packageURL": HOST + path, "byteSize": len(data),
                "checksum": {"algorithm": "sha256", "value": hashlib.sha256(data).hexdigest()},
            }
            validate(root, entry)
            file.write_bytes(data.replace(b"[]", b"{}"))
            with self.assertRaisesRegex(ValueError, "checksum"):
                validate(root, entry)

    def test_checks_aerith_shards_as_well_as_index(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            path = PACKAGE_PATHS[AERITH]
            name = "COMET_10P_v1.json"
            shard = Path(path).parent / "shards" / name
            (root / shard).parent.mkdir(parents=True)
            (root / shard).write_bytes(b"{}")
            data = json.dumps({"comets": [{
                "fileName": name, "path": shard.as_posix(), "byteSize": 2,
                "checksum": hashlib.sha256(b"{}").hexdigest(),
            }]}).encode()
            (root / path).write_bytes(data)
            entry = {
                "family": AERITH, "packageURL": HOST + path, "byteSize": len(data),
                "checksum": {"algorithm": "sha256", "value": hashlib.sha256(data).hexdigest()},
            }
            validate(root, entry)
            (root / shard).write_bytes(b"[]")
            with self.assertRaisesRegex(ValueError, "checksum"):
                validate(root, entry)


if __name__ == "__main__":
    unittest.main()
