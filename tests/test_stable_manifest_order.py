import ast
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
MANIFEST = ROOT / "v1/channels/stable/manifest.json"

FAMILY_ORDER = [
    "targetMetadataOverlay",
    "targetNeighborhoodDefinitions",
    "targetImageAssets",
    "equipmentCatalog",
    "astrophotographyEquipmentCatalog",
    "astrophotographyEquipmentSanitizedCatalog",
    "telescopeReferencePrices",
    "telescopeOfficialProductLinks",
    "darkSkyPlaces",
    "cometSnapshot",
    "cometOrbitGeometry",
    "cometDetailMetadata",
    "planetCatalog",
    "lunarEvents",
    "fullMoonNameAliases",
    "planetTargetCloseEncounters",
    "cometCloseEncounters",
    "seasonalRecommendationCandidates",
    "transientEventFeed",
]

LATITUDE_BAND_ORDER = [
    "north_high_60_90n",
    "north_mid_30_60n",
    "north_low_0_30n",
    "south_low_0_30s",
    "south_mid_30_60s",
    "south_high_60_90s",
]


def assigned_list(path: Path, name: str):
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if any(isinstance(target, ast.Name) and target.id == name for target in node.targets):
            return ast.literal_eval(node.value)
    return None


def manifest_sort_key(package):
    family = package.get("family") or package.get("packageFamily") or ""
    family_index = FAMILY_ORDER.index(family) if family in FAMILY_ORDER else len(FAMILY_ORDER)
    band = str(package.get("latitudeBand") or "")
    band_index = (
        LATITUDE_BAND_ORDER.index(band)
        if band in LATITUDE_BAND_ORDER
        else len(LATITUDE_BAND_ORDER)
    )
    return family_index, band_index, family, str(package.get("packageVersion") or "")


class StableManifestOrderTests(unittest.TestCase):
    def test_every_manifest_builder_uses_the_canonical_family_order(self):
        builders = []
        for path in sorted(SCRIPTS.glob("*.py")):
            order = assigned_list(path, "FAMILY_ORDER")
            if order is None:
                continue
            builders.append(path.name)
            self.assertEqual(order, FAMILY_ORDER, path.name)
        self.assertGreater(len(builders), 0)

    def test_stable_manifest_is_canonically_ordered(self):
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        packages = manifest["packages"]
        self.assertEqual(packages, sorted(packages, key=manifest_sort_key))


if __name__ == "__main__":
    unittest.main()
