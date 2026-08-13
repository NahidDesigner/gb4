import unittest
from pathlib import Path


CSS = (
    Path(__file__).resolve().parents[1]
    / "practice-areas"
    / "practice-atlas.css"
).read_text(encoding="utf-8")
PRACTICE_ROOT = Path(__file__).resolve().parents[1] / "practice-areas"
PAGES = tuple(
    path
    for path in PRACTICE_ROOT.glob("*/index.html")
    if "practice-atlas.css" in path.read_text(encoding="utf-8")
)


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

    def test_all_practice_pages_request_the_current_shared_css(self):
        self.assertGreaterEqual(len(PAGES), 5)
        for page in PAGES:
            with self.subTest(page=page.parent.name):
                self.assertIn(
                    "practice-atlas.css?v=quick-fixes-8",
                    page.read_text(encoding="utf-8"),
                )


if __name__ == "__main__":
    unittest.main()
