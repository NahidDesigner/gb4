import unittest
from pathlib import Path


CSS = (
    Path(__file__).resolve().parents[1]
    / "practice-areas"
    / "practice-atlas.css"
).read_text(encoding="utf-8")


class PracticeTermsMobileTests(unittest.TestCase):
    def test_shared_mobile_terms_heading_keeps_each_span_on_one_line(self):
        quick_fix = CSS.split("QUICK FIX 4 — Two-line mobile terms heading", 1)[1]
        self.assertIn(
            "main #terms.terms-stage .index-head .h2",
            quick_fix,
        )
        self.assertIn("max-width: none", quick_fix)
        self.assertIn("white-space: nowrap", quick_fix)


if __name__ == "__main__":
    unittest.main()
