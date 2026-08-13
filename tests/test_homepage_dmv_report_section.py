import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
CSS = (ROOT / "homepage-atlas.css").read_text(encoding="utf-8")
JS = (ROOT / "homepage-atlas.js").read_text(encoding="utf-8")


def section(section_id: str) -> str:
    match = re.search(
        rf'<section\b[^>]*\bid="{re.escape(section_id)}"[^>]*>[\s\S]*?</section>',
        HTML,
    )
    return match.group(0) if match else ""


def declarations(selector: str) -> list[str]:
    return re.findall(re.escape(selector) + r"\s*\{([^}]*)\}", CSS, re.S)


class HomepageDmvReportSectionTests(unittest.TestCase):
    def test_section_is_unique_and_sits_between_first48_and_premises(self):
        self.assertEqual(HTML.count('id="dmv-report"'), 1)
        self.assertRegex(
            HTML,
            r'id="first48"[\s\S]*?</section>\s*'
            r'(?:<!--[\s\S]*?-->\s*)?'
            r'<section\b[^>]*\bid="dmv-report"[\s\S]*?</section>\s*'
            r'(?:<!--[\s\S]*?-->\s*)?'
            r'<section\b[^>]*\bid="premises"',
        )

    def test_section_replaces_the_old_first48_resource_row(self):
        first48 = section("first48")
        self.assertNotIn("mynyaccident.com", first48.lower())
        self.assertNotIn("ds-sequence-section__foot", first48)

    def test_section_keeps_primary_link_and_omits_disclosure_card(self):
        report = section("dmv-report")
        self.assertRegex(
            report,
            r'<a[^>]+href="https://mynyaccident\.com/"[^>]+'
            r'target="_blank"[^>]+rel="[^"]*noopener[^"]*"',
        )
        self.assertNotIn("dmv-report__disclosure", report)
        self.assertNotIn("Independent website", report)
        self.assertNotIn("Not affiliated with the NYS DMV", report)
        self.assertNotIn("dmv.ny.gov/records/", report)
        self.assertNotIn(".dmv-report__disclosure", CSS)

    def test_section_uses_separate_background_and_phone_layers(self):
        report = section("dmv-report")
        self.assertRegex(
            report,
            r'<div class="dmv-report__visual"[^>]*>[\s\S]*?'
            r'<img class="dmv-report__scene" src="assets/report-onlybg\.webp"'
            r'[^>]+width="1774" height="887"[\s\S]*?'
            r'<img class="dmv-report__phone" src="assets/report-phone\.webp"'
            r'[^>]+width="1024" height="1536"[\s\S]*?</div>\s*'
            r'<div class="dmv-report__inner',
        )
        self.assertNotIn("dmv-report__phone-ui", report)
        self.assertNotIn(".dmv-report__phone-ui", CSS)
        self.assertNotIn('src="assets/report.webp"', report)

    def test_phone_layer_is_contained_and_mobile_media_comes_before_content(self):
        phone_rules = declarations(".atlas-home #dmv-report .dmv-report__phone")
        self.assertTrue(any("object-fit: contain" in rule for rule in phone_rules))

        marker = "EDIT 25 — MyNYAccident report resource section"
        edit = CSS.split(marker, 1)[1]
        mobile = edit.split("@media (max-width: 760px)", 1)[1]
        self.assertRegex(
            mobile,
            r"\.atlas-home #dmv-report \.dmv-report__visual\s*\{[^}]*"
            r"position:\s*relative[^}]*order:\s*1",
        )
        self.assertRegex(
            mobile,
            r"\.atlas-home #dmv-report \.dmv-report__inner\s*\{[^}]*"
            r"order:\s*2",
        )
        self.assertRegex(
            mobile,
            r"\.atlas-home #dmv-report \.dmv-report__close\s*\{[^}]*"
            r"order:\s*3",
        )

    def test_phone_uses_one_shot_perspective_settle_with_safe_fallbacks(self):
        self.assertIn("document.getElementById('dmv-report')", JS)
        self.assertIn("querySelector('.dmv-report__phone')", JS)
        self.assertIn("typeof dmvPhone.animate !== 'function'", JS)
        self.assertIn("window.matchMedia('(max-width: 760px)')", JS)
        self.assertIn("translate3d(72px, 24px, 0)", JS)
        self.assertIn("translate3d(-50%, -36px, 0)", JS)
        self.assertIn("duration: 700", JS)
        self.assertIn("easing: 'cubic-bezier(0.16, 1, 0.3, 1)'", JS)
        self.assertRegex(
            JS,
            r"entry\.target\.classList\.add\('atlas-visible'\);\s*"
            r"if \(entry\.target === dmvReport\) animateDmvPhone\(\);\s*"
            r"observer\.unobserve\(entry\.target\)",
        )
        self.assertRegex(
            JS,
            r"if \(!\('IntersectionObserver' in window\) \|\| reduceMotion\.matches\)",
        )

    def test_section_owns_the_approved_atlas_fonts(self):
        section_rules = declarations(".atlas-home #dmv-report")
        heading_rules = declarations(".atlas-home #dmv-report .dmv-report__heading")
        self.assertTrue(
            any('font-family: "Atlas Text", sans-serif' in rule for rule in section_rules)
        )
        self.assertTrue(
            any('font-family: "Atlas Display", sans-serif' in rule for rule in heading_rules)
        )

    def test_desktop_grid_reserves_the_right_side_for_the_baked_phone(self):
        grid_rules = declarations(".atlas-home #dmv-report .dmv-report__inner")
        self.assertTrue(
            any(
                "grid-template-columns: minmax(0, 0.48fr) minmax(0, 0.52fr)"
                in rule
                for rule in grid_rules
            )
        )

    def test_phone_layout_has_an_authored_single_column_composition(self):
        marker = "EDIT 25 — MyNYAccident report resource section"
        self.assertIn(marker, CSS)
        edit = CSS.split(marker, 1)[1]
        phone = edit.split("@media (max-width: 760px)", 1)[1]
        self.assertRegex(
            phone,
            r"\.atlas-home #dmv-report \.dmv-report__grid\s*\{[^}]*"
            r"grid-template-columns:\s*1fr",
        )
        self.assertRegex(
            phone,
            r"\.atlas-home #dmv-report \.dmv-report__action\s*\{[^}]*"
            r"min-height:\s*44px",
        )


if __name__ == "__main__":
    unittest.main()
