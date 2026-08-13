import unittest
from pathlib import Path


CSS = (
    Path(__file__).resolve().parents[1]
    / "practice-areas"
    / "practice-atlas.css"
).read_text(encoding="utf-8")


class PracticeSharedHeadingTests(unittest.TestCase):
    def test_why_and_related_headings_are_one_line_at_all_widths(self):
        quick_fix = CSS.split(
            "QUICK FIX 6 — One-line shared practice headings", 1
        )[1]
        self.assertIn("main #why.dark .h2", quick_fix)
        self.assertIn("main #related .h2", quick_fix)
        self.assertGreaterEqual(quick_fix.count("white-space: nowrap"), 2)
        self.assertIn("main #related .h2 span", quick_fix)
        self.assertIn("display: inline", quick_fix)


if __name__ == "__main__":
    unittest.main()
