import datetime as dt
import importlib.util
import sys
import unittest
from pathlib import Path


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1]
    / "scripts"
    / "build_aerith_comet_source.py"
)
SPEC = importlib.util.spec_from_file_location("build_aerith_comet_source", SCRIPT_PATH)
aerith = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = aerith
assert SPEC.loader is not None
SPEC.loader.exec_module(aerith)


SAMPLE_PAGE = """
<HTML>
<HEAD><TITLE>Weekly Information about Bright Comets (2026 Aug. 8: North)</TITLE></HEAD>
<BODY>
<EM>Updated on August 9, 2026</EM>
<H2><IMG SRC="../../icon/pr_star.gif" ALT="*">
<A HREF="../catalog/0220P/2026.html">220P/McNaught</A></H2>
<TABLE><TR><TD>
<A HREF="../catalog/0220P/2026.html"><IMG SRC="../../pictures/fichtl/s/220P.jpg"></A>
</TD><TD>
<P>Another major outburst occured on Aug. 5 and it brightened up to 7 mag (Aug. 5, Giuseppe Pappa).</P>
<PRE>
Date(TT)  R.A. (2000) Decl.   Delta     r    Elong.  m1   Best Time(A, h)
Aug.  8   2 42.66    9 31.0   1.231   1.647    93    7.3   3:39 (306, 53)
Aug. 15   2 54.90    9 32.9   1.199   1.669    97    8.0   3:47 (313, 56)
</PRE>
</TD></TR></TABLE>

<H2><IMG SRC="../../icon/pr_star.gif" ALT="*">
<A HREF="../catalog/2024T5/2024T5.html">C/2024 T5 ( ATLAS )</A></H2>
<TABLE><TR><TD>
<A HREF="../catalog/2024T5/2024T5.html"><IMG SRC="../../pictures/jager/s/2024T5.png"></A>
</TD><TD>
<P>Now it is 13.9 mag (July 24, Andrew Pearce).</P>
<PRE>
Date(TT)  R.A. (2000) Decl.   Delta     r    Elong.  m1   Best Time(A, h)
Aug.  8   5 14.96  -12 58.2   4.834   4.502    65   13.0   3:39 (294, 10)
Aug. 15   5 20.42  -12 54.6   4.733   4.471    69   12.9   3:47 (298, 15)
</PRE>
</TD></TR></TABLE>
</BODY>
</HTML>
"""


class AerithCometSourceTests(unittest.TestCase):
    def test_parse_entries_extracts_designation_images_and_weekly_magnitudes(self):
        context, entries = aerith.parse_entries(
            SAMPLE_PAGE,
            "http://www.aerith.net/comet/weekly/current.html",
        )

        self.assertEqual(context["hemisphere"], "north")
        self.assertEqual(context["pageDate"], dt.date(2026, 8, 8))
        self.assertEqual(context["entryCount"], 2)
        self.assertEqual(entries[0]["normalizedDesignation"], "220P")
        self.assertEqual(
            entries[0]["thumbnailImageURL"],
            "http://www.aerith.net/pictures/fichtl/s/220P.jpg",
        )
        self.assertEqual(entries[0]["currentMagnitude"], 7.3)
        self.assertEqual(entries[0]["nextWeekMagnitude"], 8.0)
        self.assertIn("major outburst", entries[0]["sourceCommentary"].lower())
        self.assertAlmostEqual(entries[0]["weeklyRows"][0]["rightAscensionHours"], 2.711)
        self.assertAlmostEqual(entries[1]["weeklyRows"][0]["declinationDegrees"], -12.97)

    def test_normalize_comet_key_handles_periodic_and_modern_names(self):
        self.assertEqual(aerith.normalize_comet_key("220P/McNaught"), "220P")
        self.assertEqual(aerith.normalize_comet_key("0220P/McNaught"), "220P")
        self.assertEqual(aerith.normalize_comet_key("C/2024 T5 ( ATLAS )"), "C/2024T5")
        self.assertEqual(aerith.normalize_comet_key("P/2010 H2 (Vales)"), "P/2010H2")

    def test_merge_entries_records_granted_source_media_permission(self):
        _, entries = aerith.parse_entries(
            SAMPLE_PAGE,
            "http://www.aerith.net/comet/weekly/current.html",
        )

        merged = aerith.merge_entries(entries)

        self.assertEqual(len(merged), 2)
        self.assertEqual(merged[0]["imagePermissionStatus"], "permission-granted")
        self.assertIn("Seiichi Yoshida", merged[0]["imageAttribution"])
        self.assertIn("major outburst", merged[0]["sourceCommentaries"][0].lower())
        self.assertEqual(merged[0]["weeklyRowsByHemisphere"]["north"][0]["magnitude"], 7.3)


if __name__ == "__main__":
    unittest.main()
