import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
CSS = (ROOT / "homepage-atlas.css").read_text(encoding="utf-8")


class HomepageHeaderLogoCallNowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.header = HTML.split(
            '<header class="ds-site-header ds-on-dark" id="dsHeader">', 1
        )[1].split("</header>", 1)[0]
        cls.refinement = CSS.split("/* EDIT 50 — Homepage-only", 1)[1].split(
            ".atlas-home .cta-wrap .btn", 1
        )[0]
        cls.mobile = cls.refinement.split("@media (max-width: 760px)", 1)[1]

    def test_header_uses_one_phone_link_with_responsive_labels(self):
        self.assertEqual(self.header.count('href="tel:+15164441000"'), 1)
        self.assertIn('class="ds-button-call__desktop"', self.header)
        self.assertIn('class="ds-button-call__mobile"', self.header)
        self.assertIn("(516) 444-1000", self.header)
        self.assertIn("Call Now", self.header)

    def test_mobile_replaces_search_with_a_44px_call_target(self):
        self.assertIn("#searchOpen2", self.mobile)
        self.assertIn("display: none", self.mobile)
        self.assertIn(".ds-site-header .ds-button-call", self.mobile)
        self.assertIn("display: inline-flex", self.mobile)
        self.assertIn("min-height: 44px", self.mobile)
        self.assertIn(".ds-button-call__desktop", self.mobile)
        self.assertIn(".ds-button-call__mobile", self.mobile)

    def test_header_is_translucent_without_a_glass_filter(self):
        self.assertIn("rgba(242, 240, 234, 0.94)", self.refinement)
        self.assertNotIn("backdrop-filter", self.refinement)

    def test_logo_is_larger_and_stylesheet_cache_is_busted(self):
        self.assertIn("height: 104px", self.refinement)
        self.assertIn("height: 78px", self.mobile)
        self.assertIn(
            'homepage-atlas.css?v=header-logo-call-now-1',
            HTML,
        )

    def test_locked_hero_and_mobile_actionbar_remain_present(self):
        self.assertIn('<!-- ================= HERO (locked) ================= -->', HTML)
        self.assertIn('<header class="hero">', HTML)
        self.assertIn('<div class="actionbar" id="actionbar">', HTML)
        self.assertIn(
            '<a class="ab ab--call" href="tel:+15164441000">',
            HTML,
        )


if __name__ == "__main__":
    unittest.main()
