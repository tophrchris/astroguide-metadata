import importlib.util
import sys
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "build_lunar_event_package.py"
SPEC = importlib.util.spec_from_file_location("build_lunar_event_package", SCRIPT_PATH)
lunar = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = lunar
assert SPEC.loader is not None
SPEC.loader.exec_module(lunar)


def target(
    object_id,
    primary_name,
    catalog_name,
    ra_hours,
    dec_degrees,
    *,
    aliases=(),
    magnitude=None,
):
    return lunar.TargetRecord(
        object_id=object_id,
        primary_name=primary_name,
        catalog_name=catalog_name,
        object_type="Galaxy",
        constellation=None,
        magnitude=magnitude,
        angular_size_arcmin=None,
        angular_size_major_arcmin=None,
        angular_size_minor_arcmin=None,
        ra_hours=ra_hours,
        dec_degrees=dec_degrees,
        aliases=tuple(aliases),
    )


def identity_context(targets, tolerance_arcmin=6.0):
    groups = lunar.build_target_groups(targets, tolerance_arcmin)
    context = lunar.build_target_identity_context(groups, tolerance_arcmin)
    return groups, context


def reference(
    *,
    primary=(),
    alternate=(),
    common=(),
    ra_degrees=None,
    dec_degrees=None,
    allow_coordinate_common_name=False,
    owns_common_names=False,
    reason="curatedRecommendation",
):
    return lunar.SelectionReference(
        reason=reason,
        source="test",
        label="test-reference",
        primary_exact_tokens=tuple(primary),
        alternate_exact_tokens=tuple(alternate),
        common_name_tokens=tuple(common),
        ra_degrees=ra_degrees,
        dec_degrees=dec_degrees,
        allow_coordinate_common_name=allow_coordinate_common_name,
        owns_common_names=owns_common_names,
    )


class LunarEventIdentityTests(unittest.TestCase):
    def test_alias_sorting_is_deterministic_for_case_variants(self):
        groups, context = identity_context(
            [
                target(
                    "M104",
                    "Sombrero Galaxy",
                    "M M104",
                    12.6667,
                    -11.6231,
                    aliases=["Sombrero galaxy"],
                )
            ]
        )

        aliases = lunar.target_group_aliases(groups[0], context)

        self.assertLess(aliases.index("Sombrero Galaxy"), aliases.index("Sombrero galaxy"))

    def test_exact_designation_precedes_contaminated_alias_and_coordinates(self):
        groups, context = identity_context(
            [
                target("M33", "Triangulum Galaxy", "M M33", 1.565, 30.65, aliases=["NGC 598"]),
                target("IC 4209", "Triangulum Galaxy", "IC IC 4209", 13.1729, -7.1707),
            ]
        )
        ref = reference(
            primary=(lunar.exact_identifier_token("M33"),),
            alternate=(lunar.catalog_designation_token("IC 4209"),),
            common=(lunar.common_name_token("Triangulum Galaxy"),),
            ra_degrees=13.1729 * 15.0,
            dec_degrees=-7.1707,
            allow_coordinate_common_name=True,
        )

        self.assertEqual(lunar.resolve_selection_reference(ref, context), {"M33"})
        self.assertEqual([group.canonical.object_id for group in groups if group.group_id == "M33"], ["M33"])

    def test_preferred_catalog_order_selects_messier_ngc_ic_caldwell(self):
        groups, _ = identity_context(
            [
                target("NGC598", "Triangulum galaxy", "NGC NGC598", 1.5639, 30.6602, aliases=["M 33"]),
                target("M33", "Triangulum Galaxy", "M M33", 1.565, 30.65, aliases=["NGC 598"]),
                target("C5", "Caldwell 5", "C C5", 3.78, 68.0964, aliases=["IC 342"]),
                target("IC342", "IC342", "IC IC342", 3.78, 68.0964, aliases=["C 5"]),
            ]
        )

        canonicals = {group.group_id: group.canonical.object_id for group in groups}
        self.assertEqual(canonicals["M33"], "M33")
        self.assertEqual(canonicals["IC342"], "IC342")

    def test_ambiguous_common_names_need_one_coordinate_consistent_cluster(self):
        _, context = identity_context(
            [
                target("M33", "Triangulum Galaxy", "M M33", 1.565, 30.65),
                target("IC 4209", "Triangulum Galaxy", "IC IC 4209", 13.1729, -7.1707),
            ]
        )
        common = lunar.common_name_token("Triangulum Galaxy")
        no_coordinate_ref = reference(common=(common,))
        coordinate_ref = reference(
            common=(common,),
            ra_degrees=1.565 * 15.0,
            dec_degrees=30.65,
            allow_coordinate_common_name=True,
        )

        self.assertIn(common, context.ambiguous_common_tokens)
        self.assertEqual(lunar.resolve_selection_reference(no_coordinate_ref, context), set())
        self.assertEqual(lunar.resolve_selection_reference(coordinate_ref, context), {"M33"})

    def test_alias_identity_is_rejected_when_candidate_coordinates_disagree(self):
        _, context = identity_context(
            [
                target("Foo1", "Foo 1", "Foo Foo1", 1.0, 1.0, aliases=["NGC 999"]),
                target("Foo2", "Foo 2", "Foo Foo2", 12.0, -20.0, aliases=["NGC 999"]),
            ]
        )
        token = lunar.catalog_designation_token("NGC 999")
        ref = reference(alternate=(token,))

        self.assertIn(token, context.ambiguous_exact_tokens)
        self.assertEqual(lunar.resolve_selection_reference(ref, context), set())

    def test_concrete_contaminated_ic_rows_do_not_select_or_emit_wrong_names(self):
        targets = [
            target("M33", "Triangulum Galaxy", "M M33", 1.565, 30.65, aliases=["NGC 598"]),
            target("NGC598", "Triangulum galaxy", "NGC NGC598", 1.5639, 30.6602, aliases=["M 33"]),
            target("IC 4209", "Triangulum Galaxy", "IC IC 4209", 13.1729, -7.1707),
            target("IC10", "IC10", "IC IC10", 0.3381, 59.3038, aliases=["IC 10"]),
            target("IC 770", "IC 10", "IC IC 770", 12.2173, -4.5534, aliases=["IC 10"]),
            target("IC342", "IC342", "IC IC342", 3.78, 68.0964, aliases=["IC 342"]),
            target("C5", "Caldwell 5", "C C5", 3.78, 68.0964, aliases=["IC 342"]),
            target("IC 924", "IC 342", "IC IC 924", 13.7604, -12.4551, aliases=["IC 342"]),
            target("IC 1341", "IC 342", "IC IC 1341", 21.0046, -13.9763, aliases=["IC 342"]),
        ]
        groups, context = identity_context(targets)
        refs = [
            reference(
                primary=(lunar.exact_identifier_token("M33"),),
                alternate=(lunar.catalog_designation_token("NGC 598"),),
                common=(lunar.common_name_token("Triangulum Galaxy"),),
                ra_degrees=1.565 * 15.0,
                dec_degrees=30.65,
                owns_common_names=True,
            ),
            reference(primary=(lunar.exact_identifier_token("IC10"),)),
            reference(primary=(lunar.exact_identifier_token("IC342"),)),
        ]
        lunar.populate_common_name_owners(context, refs)
        selected, _ = lunar.select_dso_target_groups(
            groups,
            identity_context=context,
            curated_references=refs,
            named_showcase_references=[],
            bright_ngc_ic_mag_limit=10.0,
        )
        selected_ids = {group.group_id for group in selected}

        self.assertTrue({"M33", "IC10", "IC342"}.issubset(selected_ids))
        self.assertFalse({"IC 4209", "IC 770", "IC 924", "IC 1341"}.intersection(selected_ids))

        group_by_id = {group.group_id: group for group in groups}
        self.assertIn("NGC 598", lunar.target_group_aliases(group_by_id["M33"], context))
        self.assertEqual(lunar.target_group_display_name(group_by_id["IC 4209"], context), "IC 4209")
        self.assertNotIn("Triangulum Galaxy", lunar.target_group_aliases(group_by_id["IC 4209"], context))
        self.assertEqual(lunar.target_group_display_name(group_by_id["IC 770"], context), "IC 770")
        self.assertNotIn("IC 10", lunar.target_group_aliases(group_by_id["IC 770"], context))
        self.assertEqual(lunar.target_group_display_name(group_by_id["IC 924"], context), "IC 924")
        self.assertNotIn("IC 342", lunar.target_group_aliases(group_by_id["IC 924"], context))
        self.assertEqual(lunar.target_group_display_name(group_by_id["IC 1341"], context), "IC 1341")
        self.assertNotIn("IC 342", lunar.target_group_aliases(group_by_id["IC 1341"], context))


if __name__ == "__main__":
    unittest.main()
