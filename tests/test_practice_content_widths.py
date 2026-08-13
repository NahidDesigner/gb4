import unittest
from pathlib import Path


CSS = (
    Path(__file__).resolve().parents[1]
    / "practice-areas"
    / "practice-atlas.css"
).read_text(encoding="utf-8")


class PracticeContentWidthTests(unittest.TestCase):
    def test_terms_intro_and_related_card_copy_use_available_width(self):
        quick_fix = CSS.split(
            "QUICK FIX 7 — Wider shared practice content", 1
        )[1]
        self.assertIn("main #terms.terms-stage .index-head", quick_fix)
        self.assertIn("main #terms.terms-stage .index-head > .lede", quick_fix)
        self.assertIn("main #related .tile-t", quick_fix)
        self.assertIn("main #related .tile-p", quick_fix)
        self.assertGreaterEqual(quick_fix.count("max-width: none"), 2)
        self.assertIn("width: 100%", quick_fix)


if __name__ == "__main__":
    unittest.main()
