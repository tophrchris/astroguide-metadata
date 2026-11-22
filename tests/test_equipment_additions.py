import copy
import tempfile
import unittest
from pathlib import Path

from test_equipment_catalog_package import equipment


class EquipmentAdditionsTests(unittest.TestCase):
    def test_sv580_survives_rebuild_and_sanitization(self):
        catalog = {"opticalComponents": [], "cameraComponents": []}
        equipment.apply_metadata_additions(catalog)
        row = catalog["opticalComponents"][0]
        self.assertEqual(row["component_id"], "optical-tube-svbony-sv580-official")
        self.assertEqual((row["aperture_mm"], row["native_focal_length_mm"], row["native_focal_ratio"]), (80, 360, 4.5))
        self.assertTrue(equipment.is_selectable_optical_component(row, None))
        self.assertEqual(equipment.sanitized_optical_component(row, None)["model"], "SV580")
        before = copy.deepcopy(catalog)
        self.assertEqual(equipment.apply_metadata_additions(catalog), before)
        self.assertEqual(catalog["counts"]["optical_tubes"], 1)

    def test_conflicting_bundle_fails(self):
        catalog = equipment.apply_metadata_additions({"opticalComponents": [], "cameraComponents": []})
        catalog["opticalComponents"][0]["aperture_mm"] = 1
        with self.assertRaisesRegex(ValueError, "conflicts"):
            equipment.apply_metadata_additions(catalog)

    def test_no_additions_leaves_catalog_untouched(self):
        with tempfile.TemporaryDirectory() as directory:
            catalog = {"opticalComponents": [], "cameraComponents": []}
            before = copy.deepcopy(catalog)
            self.assertEqual(equipment.apply_metadata_additions(catalog, Path(directory) / "absent.json"), before)
