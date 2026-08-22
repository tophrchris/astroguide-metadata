import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1]
    / "scripts"
    / "build_target_image_package.py"
)
SPEC = importlib.util.spec_from_file_location("build_target_image_package", SCRIPT_PATH)
target_images = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = target_images
assert SPEC.loader is not None
SPEC.loader.exec_module(target_images)


class TargetImagePackageTests(unittest.TestCase):
    def write_json(self, path: Path, payload: dict):
        path.parent.mkdir(parents=True, exist_ok=True)
        target_images.write_json(path, payload)

    def make_source_package(self, root: Path):
        source = root / "source"
        asset_dir = source / "assets" / "shared-asset-primary-exact"
        asset_dir.mkdir(parents=True)
        image_bytes = {
            "hero.jpg": b"fake hero jpeg bytes",
            "thumbnail-320.jpg": b"fake 320 jpeg bytes",
            "thumbnail-160.jpg": b"fake 160 jpeg bytes",
        }
        for file_name, data in image_bytes.items():
            (asset_dir / file_name).write_bytes(data)

        def media(file_name: str, width: int):
            data = image_bytes[file_name]
            return {
                "path": f"assets/shared-asset-primary-exact/{file_name}",
                "width": width,
                "height": width,
                "bytes": len(data),
                "sha256": target_images.sha256_bytes(data),
            }

        base_subject = {
            "catalog": "TEST",
            "commonName": None,
            "objectType": "Nebula",
            "constellation": "Test",
            "assetId": "shared-asset-primary-exact",
            "media": {
                "hero": media("hero.jpg", 640),
                "thumbnail": media("thumbnail-320.jpg", 320),
                "compactThumbnail": media("thumbnail-160.jpg", 160),
                "naturalSourceOutputSize": 640,
                "heroCapped": False,
            },
            "result": {
                "resultId": "test-result",
                "title": "Test Result",
                "captureDate": "2026-08-21T00:00:00Z",
                "persistedImagePath": "assets/results/test-result.jpg",
                "originalPngSource": "Test Result.png",
                "preferred": True,
            },
            "preferredResult": True,
            "wcsMethod": "source-render-fits-wcs",
            "humanSelected": True,
            "cropFraming": {"mode": "exact", "scale": 1},
            "framing": {"objectId": "TEST1", "diameterArcmin": 10, "source": "test"},
            "associatedSubjects": ["TEST1"],
        }
        subject_one = dict(base_subject, objectId="TEST1", qualityReady=True)
        subject_two = dict(
            base_subject,
            objectId="TEST2",
            commonName="Second Test",
            qualityReady=False,
            associatedSubjects=["TEST2", "TEST1"],
        )
        manifest = {
            "schema": "astroguide-capture-package/v1",
            "packageId": "astroguide-capture-package-test",
            "generatedAt": "2026-08-21T21:52:59.603205+00:00",
            "source": {
                "reportGeneratedAt": "2026-08-21T21:01:17Z",
                "galleryGeneratedAt": "2026-08-21T20:14:11Z",
                "astroGuideCatalogVersion": "test",
                "sirilTag": "1.4.4",
            },
            "selectionExport": {
                "schema": "astroguide-capture-selection/v2",
                "exportedAt": "2026-08-21T21:22:15Z",
                "fileName": "test-selection.json",
                "sha256": "0" * 64,
            },
            "selectionCount": 2,
            "assetCount": 1,
            "sharedAssetCount": 1,
            "expandedCropCount": 0,
            "manualSelectionCount": 1,
            "sizeProposalCount": 1,
            "heroMaximumSize": 2400,
            "orientationStandard": "north-up-east-left",
            "preferredResults": [],
            "subjects": [subject_one, subject_two],
        }
        selection = {
            "schema": "astroguide-capture-selection/v2",
            "exportedAt": "2026-08-21T21:22:15Z",
            "source": manifest["source"],
            "selectionCount": 2,
            "preferredResultCount": 0,
            "preferredResults": [],
            "selections": [
                {
                    "objectId": "TEST1",
                    "sourceCrop": {"left": 1, "top": 2, "side": 3},
                    "orientation": {"standard": "north-up-east-left"},
                },
                {
                    "objectId": "TEST2",
                    "sourceCrop": {"left": 4, "top": 5, "side": 6},
                    "orientation": {"standard": "north-up-east-left"},
                },
            ],
        }
        validation = {
            "schema": "astroguide-capture-package-validation/v1",
            "validatedAt": "2026-08-21T21:52:59Z",
            "passed": True,
            "selectionCount": 2,
            "assetCount": 1,
            "checkedImageFiles": 3,
            "contactSheetCards": 2,
            "manualSelectionWarnings": 1,
            "errors": [],
            "warnings": ["TEST2 is an explicit human selection over an automatic geometry warning"],
        }
        self.write_json(source / "manifest.json", manifest)
        self.write_json(source / "source-selection.json", selection)
        self.write_json(source / "validation.json", validation)
        self.write_json(source / "catalog-update.json", {"imageAssignments": []})
        self.write_json(source / "catalog-size-updates.json", {"updates": [{"object_id": "TEST1"}]})
        (source / "README.md").write_text("# Test\n", encoding="utf-8")
        (source / "contact-sheet.html").write_text("<html></html>\n", encoding="utf-8")
        (source / "catalog-size-updates.csv").write_text("object_id\nTEST1\n", encoding="utf-8")
        return source

    def make_repo(self, root: Path):
        repo = root / "repo"
        self.write_json(
            repo / "v1/channels/stable/manifest.json",
            {
                "schemaVersion": 1,
                "channel": "stable",
                "generatedAt": "2026-08-20T00:00:00Z",
                "publishedAt": "2026-08-20T00:00:00Z",
                "packages": [],
            },
        )
        self.write_json(
            repo / target_images.TARGET_METADATA_OVERLAY_PATH,
            {
                "schemaVersion": 1,
                "packageFamily": "targetMetadataOverlay",
                "targets": [
                    {
                        "canonicalID": "TEST1",
                        "preferredName": "First Test",
                        "aliases": ["Test One"],
                        "resolution": {"catalogObjectID": "TEST1"},
                    }
                ],
            },
        )
        return repo

    def test_build_package_preserves_shared_asset_paths_and_manifest_counts(self):
        original_root = target_images.REPO_ROOT
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            source = self.make_source_package(temp_path)
            repo = self.make_repo(temp_path)
            target_images.REPO_ROOT = repo
            try:
                descriptor = target_images.write_target_image_package(
                    source_root=source,
                    generated_at="2026-08-21T21:52:59Z",
                    package_version="target-image-assets-v1-test",
                    min_supported_app_version="1.4.1",
                    min_supported_build="1",
                    update_manifest_path=repo / "v1/channels/stable/manifest.json",
                )
                package = target_images.read_json(repo / target_images.PACKAGE_PATH)
                target_images.validate_package(package, repo / target_images.PACKAGE_PATH)
                target_images.validate_manifest_descriptor(
                    repo / "v1/channels/stable/manifest.json",
                    package,
                    (repo / target_images.PACKAGE_PATH).read_bytes(),
                )
            finally:
                target_images.REPO_ROOT = original_root

        self.assertEqual(descriptor["recordCount"], 2)
        self.assertEqual(descriptor["assetCount"], 1)
        self.assertEqual(descriptor["imageFileCount"], 3)
        self.assertEqual(package["counts"]["variantReferences"], 6)
        self.assertEqual(package["counts"]["imageFiles"], 3)
        self.assertEqual(package["sharedAssets"][0]["targetIDs"], ["TEST1", "TEST2"])
        first, second = package["targets"]
        self.assertEqual(first["aliases"], ["First Test", "Test One"])
        self.assertEqual(first["assetOwnerTargetID"], "TEST1")
        self.assertEqual(second["assetOwnerTargetID"], "TEST1")
        self.assertEqual(
            first["variants"]["thumbnail160"]["path"],
            second["variants"]["thumbnail160"]["path"],
        )
        self.assertTrue(first["variants"]["thumbnail160"]["path"].startswith("v1/assets/target-images/"))

    def test_validate_package_rejects_asset_hash_mismatch(self):
        original_root = target_images.REPO_ROOT
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            source = self.make_source_package(temp_path)
            repo = self.make_repo(temp_path)
            target_images.REPO_ROOT = repo
            try:
                target_images.write_target_image_package(
                    source_root=source,
                    generated_at="2026-08-21T21:52:59Z",
                    package_version="target-image-assets-v1-test",
                    min_supported_app_version="1.4.1",
                    min_supported_build="1",
                    update_manifest_path=None,
                )
                package = target_images.read_json(repo / target_images.PACKAGE_PATH)
                corrupt_path = repo / package["targets"][0]["variants"]["hero"]["path"]
                corrupt_path.write_bytes(corrupt_path.read_bytes() + b"corruption")
                with self.assertRaises(RuntimeError):
                    target_images.validate_package(package, repo / target_images.PACKAGE_PATH)
            finally:
                target_images.REPO_ROOT = original_root


if __name__ == "__main__":
    unittest.main()
