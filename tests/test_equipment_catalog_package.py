import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1]
    / "scripts"
    / "build_equipment_catalog_package.py"
)
SPEC = importlib.util.spec_from_file_location("build_equipment_catalog_package", SCRIPT_PATH)
equipment = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = equipment
assert SPEC.loader is not None
SPEC.loader.exec_module(equipment)


class EquipmentCatalogPackageTests(unittest.TestCase):
    def make_app_repo(self) -> tempfile.TemporaryDirectory:
        tempdir = tempfile.TemporaryDirectory()
        root = Path(tempdir.name)
        resources = root / "App" / "Resources" / "Equipment"
        resources.mkdir(parents=True)

        catalog = {
            "schemaVersion": 1,
            "generatedAt": "2026-08-19T00:00:00Z",
            "source": {"name": "Unit Test"},
            "counts": {},
            "normalizationNotes": [],
            "manufacturers": [],
            "opticalComponents": [
                {
                    "curation_status": "candidate",
                    "include_in_app": True,
                    "component_type": "optical_tube",
                    "component_id": "optic-keep",
                    "manufacturer": "William Optics",
                    "manufacturer_raw": "William Optics",
                    "model": "Ultra Cat 76",
                    "aperture_mm": 76.0,
                    "native_focal_length_mm": 342.0,
                    "native_focal_ratio": 4.5,
                    "source_value": "raw-source-value",
                    "source_id": "123",
                    "source_label": "William Optics - Ultra Cat 76",
                    "source_url": "https://example.test/optic-keep",
                    "source_attribution": "Unit source",
                    "source_confidence": "unit",
                    "curator_notes": "Should not leak.",
                },
                {
                    "curation_status": "candidate",
                    "include_in_app": True,
                    "component_type": "optical_tube",
                    "component_id": "optic-excluded",
                    "manufacturer": "William Optics",
                    "model": "Seestar-adjacent widget",
                    "aperture_mm": 50.0,
                    "native_focal_length_mm": 250.0,
                },
            ],
            "cameraComponents": [
                {
                    "curation_status": "candidate",
                    "include_in_app": True,
                    "component_type": "camera",
                    "component_id": "camera-keep",
                    "manufacturer": "ZWO",
                    "manufacturer_raw": "ZWO",
                    "model": "ASI533MC Pro",
                    "pixel_size_width_um": 3.76,
                    "pixel_size_height_um": 3.76,
                    "horizontal_resolution_px": 3008,
                    "vertical_resolution_px": 3008,
                    "source_value": "raw-camera-source-value",
                    "source_id": "456",
                    "source_label": "ZWO - ASI533MC Pro",
                    "source_url": "https://example.test/camera-keep",
                    "source_attribution": "Unit source",
                    "source_confidence": "unit",
                    "curator_notes": "Should not leak.",
                },
                {
                    "curation_status": "candidate",
                    "include_in_app": True,
                    "component_type": "camera",
                    "component_id": "camera-missing-geometry",
                    "manufacturer": "ZWO",
                    "model": "Incomplete Camera",
                },
            ],
        }
        curation = {
            "schemaVersion": 1,
            "generatedAt": "2026-08-19T00:00:00Z",
            "source": {"name": "Unit Test"},
            "opticalBrandAllowlist": ["William Optics"],
            "cameraBrandAllowlist": ["ZWO"],
            "excludedModelPhrases": [],
            "excludedSmartTelescopeTerms": ["seestar"],
            "normalizationNotes": [],
            "opticalProductLines": [
                {"manufacturer": "William Optics", "productLine": "Ultra Cat"}
            ],
        }
        (resources / "astrophotography_equipment.json").write_text(
            json.dumps(catalog), encoding="utf-8"
        )
        (resources / "astrophotography_equipment_curation.json").write_text(
            json.dumps(curation), encoding="utf-8"
        )
        return tempdir

    def test_raw_astrophotography_package_still_preserves_source_and_curation(self):
        with self.make_app_repo() as app_repo:
            package = equipment.build_astrophotography_package(
                Path(app_repo),
                "2026-08-19T00:00:00Z",
            )

        self.assertEqual(package["packageFamily"], "astrophotographyEquipmentCatalog")
        self.assertEqual(package["catalog"]["opticalComponents"][0]["curation_status"], "candidate")
        self.assertEqual(package["catalog"]["opticalComponents"][0]["source_value"], "raw-source-value")
        self.assertIn("curation", package)

    def test_sanitized_package_matches_app_rendered_selectable_projection(self):
        with self.make_app_repo() as app_repo:
            package = equipment.build_sanitized_astrophotography_package(
                Path(app_repo),
                "2026-08-19T00:00:00Z",
            )

        catalog = package["catalog"]
        self.assertEqual(package["packageFamily"], "astrophotographyEquipmentSanitizedCatalog")
        self.assertEqual(catalog["counts"], {
            "opticalComponents": 1,
            "cameraComponents": 1,
            "totalComponents": 2,
        })

        optic = catalog["opticalComponents"][0]
        self.assertEqual(optic["component_id"], "optic-keep")
        self.assertEqual(optic["product_line"], "Ultra Cat")
        self.assertEqual(optic["display_name"], "William Optics Ultra Cat 76")
        self.assertNotIn("curation_status", optic)
        self.assertNotIn("include_in_app", optic)
        self.assertNotIn("curator_notes", optic)
        self.assertNotIn("manufacturer_raw", optic)
        self.assertNotIn("source_value", optic)

        camera = catalog["cameraComponents"][0]
        self.assertEqual(camera["component_id"], "camera-keep")
        self.assertEqual(camera["pixel_size_um"], 3.76)
        self.assertNotIn("curation_status", camera)
        self.assertNotIn("source_value", camera)


if __name__ == "__main__":
    unittest.main()
