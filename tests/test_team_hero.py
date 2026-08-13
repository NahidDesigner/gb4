from html.parser import HTMLParser
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "our-team" / "index.html").read_text(encoding="utf-8")
CSS = (ROOT / "inner-atlas.css").read_text(encoding="utf-8")
TEAM_CSS = CSS.split("Team index hero — supplied 2026-08-12 reference", 1)[1].split(
    "main > .sec--tight:has(> .wrap > .bio)", 1
)[0]
MOBILE_CSS = TEAM_CSS.rsplit("@media (max-width: 720px)", 1)[1]


class HeroParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.team_hero_depth = 0
        self.h1_count = 0
        self.hero_images = []

    def handle_starttag(self, tag, attrs):
        attr_map = dict(attrs)
        classes = attr_map.get("class", "").split()
        if self.team_hero_depth:
            self.team_hero_depth += 1
        elif tag == "section" and "team-hero" in classes:
            self.team_hero_depth = 1

        if self.team_hero_depth and tag == "h1":
            self.h1_count += 1
        if self.team_hero_depth and tag == "img":
            self.hero_images.append(attr_map)

    def handle_endtag(self, tag):
        if self.team_hero_depth:
            self.team_hero_depth -= 1


class TeamHeroContractTests(unittest.TestCase):
    def setUp(self):
        self.parser = HeroParser()
        self.parser.feed(HTML)

    def test_semantic_hero_uses_one_h1_and_requested_photo(self):
        self.assertIn('class="team-hero"', HTML)
        self.assertEqual(self.parser.h1_count, 1)
        self.assertEqual(len(self.parser.hero_images), 1)
        image = self.parser.hero_images[0]
        self.assertEqual(image.get("src"), "../assets/imgi_40_GW-Law_about_main_img.webp")
        self.assertTrue(image.get("alt"))

    def test_reference_copy_is_present_verbatim(self):
        for phrase in (
            "Personal Injury Law",
            "Our Legal Team",
            "Dedicated advocates. Proven results.",
            "We work together to protect your rights and get you the compensation you deserve.",
            "Our Promise",
            "Personal attention.",
            "Powerful representation.",
            "Results that matter.",
        ):
            self.assertIn(phrase, re.sub(r"<[^>]+>", "", HTML))

    def test_css_has_scoped_desktop_and_mobile_compositions(self):
        self.assertIn("main:has(.team-roster) > .team-hero", CSS)
        self.assertIn("clip-path:", CSS)
        mobile = re.search(
            r"@media\s*\(max-width:\s*720px\).*?main:has\(\.team-roster\)\s*>\s*\.team-hero",
            CSS,
            flags=re.S,
        )
        self.assertIsNotNone(mobile)

    def test_desktop_uses_requested_height_and_site_fonts(self):
        self.assertIn("height: 600px", TEAM_CSS)
        self.assertIn("min-height: 600px", TEAM_CSS)
        self.assertIn("max-height: 600px", TEAM_CSS)
        self.assertRegex(
            TEAM_CSS,
            r"\.team-hero__title\s*\{[^}]*font-family:\s*\"Atlas Display\"",
        )
        self.assertRegex(
            TEAM_CSS,
            r"\.team-hero__content\s*\{[^}]*font-family:\s*\"Atlas Text\"",
        )
        self.assertRegex(
            TEAM_CSS,
            r"\.team-hero__content\s*\{[^}]*padding-block:\s*0",
        )

    def test_desktop_uses_one_full_bleed_image_under_a_shared_seam_overlay(self):
        self.assertIn("--team-seam-top: 55.25%", TEAM_CSS)
        self.assertIn("--team-seam-bottom: 48.75%", TEAM_CSS)
        self.assertRegex(
            TEAM_CSS,
            r"\.team-hero__media\s*\{[^}]*inset:\s*0[^}]*clip-path:\s*none",
        )
        self.assertRegex(
            TEAM_CSS,
            r"\.team-hero::before\s*\{[^}]*var\(--team-seam-top\)[^}]*var\(--team-seam-bottom\)",
        )
        self.assertRegex(
            TEAM_CSS,
            r"\.team-hero::after\s*\{[^}]*var\(--team-seam-top\)[^}]*var\(--team-seam-bottom\)",
        )

    def test_desktop_moves_both_attorneys_clear_of_overlay_without_changing_mobile_crop(self):
        self.assertIn("--team-photo-shift: 22vw", TEAM_CSS)
        self.assertIn("--team-photo-scale: 1.44", TEAM_CSS)
        self.assertRegex(
            TEAM_CSS,
            r"\.team-hero__media img\s*\{[^}]*transform:\s*translateX\(var\(--team-photo-shift\)\) scale\(var\(--team-photo-scale\)\)",
        )
        self.assertRegex(
            TEAM_CSS,
            r"\.team-hero__media img\s*\{[^}]*transform-origin:\s*center top",
        )
        self.assertRegex(
            MOBILE_CSS,
            r"\.team-hero__media img\s*\{[^}]*transform:\s*none",
        )

    def test_desktop_spreads_supporting_content_across_two_columns(self):
        self.assertRegex(
            TEAM_CSS,
            r"\.team-hero__content\s*\{[^}]*display:\s*grid[^}]*grid-template-columns:",
        )
        self.assertRegex(
            MOBILE_CSS,
            r"\.team-hero__content\s*\{[^}]*display:\s*block",
        )

    def test_hero_css_does_not_load_a_second_image(self):
        self.assertNotIn("url(", TEAM_CSS)

    def test_team_title_stays_on_one_line_at_all_widths(self):
        self.assertRegex(
            TEAM_CSS,
            r"\.team-hero__title\s*\{[^}]*display:\s*flex[^}]*flex-wrap:\s*nowrap[^}]*white-space:\s*nowrap",
        )

    def test_mobile_places_content_over_the_photo(self):
        self.assertRegex(
            MOBILE_CSS,
            r"\.team-hero__media\s*\{[^}]*position:\s*absolute",
        )
        self.assertRegex(
            MOBILE_CSS,
            r"\.team-hero__media::after\s*\{[^}]*rgba\(",
        )


if __name__ == "__main__":
    unittest.main()
