import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CSS = (ROOT / "inner-atlas.css").read_text(encoding="utf-8")
HTML = (ROOT / "service-areas" / "index.html").read_text(encoding="utf-8")


class ServiceAreasHeroSpacingTests(unittest.TestCase):
    def test_hero_label_uses_the_same_left_inset_as_the_title(self):
        fix = CSS.split("QUICK FIX 9 — Service Areas hero padding", 1)[1]
        self.assertIn("main:has(#counties) > .sec--tight .page-head::before", fix)
        self.assertIn("left: clamp(1.15rem, 2vw, 1.55rem)", fix)

    def test_service_areas_page_requests_current_inner_styles(self):
        self.assertIn("inner-atlas.css?v=service-areas-fixes-2", HTML)


if __name__ == "__main__":
    unittest.main()
