import unittest
from pathlib import Path


CSS = (Path(__file__).resolve().parents[1] / "homepage-atlas.css").read_text(
    encoding="utf-8"
)
HTML = (Path(__file__).resolve().parents[1] / "index.html").read_text(encoding="utf-8")


class HomepageMobileCtaTests(unittest.TestCase):
    def test_mobile_footer_has_three_items_then_centered_credit(self):
        self.assertIn('<span class="foot-copy-main">', HTML)
        self.assertIn('<span class="foot-copy-credit">', HTML)
        mobile_footer = CSS.split("QUICK FIX 3 — Mobile footer colophon", 1)[1]
        self.assertIn(".atlas-home .foot-copy-main", mobile_footer)
        self.assertIn("white-space: nowrap", mobile_footer)
        self.assertIn(".atlas-home .foot-copy-credit", mobile_footer)
        self.assertIn("text-align: center", mobile_footer)
        self.assertIn(".atlas-home .foot-sep--credit", mobile_footer)
        self.assertIn("display: none", mobile_footer)

    def test_long_mobile_section_titles_have_authored_two_line_breaks(self):
        self.assertIn(
            'What to Do After a<br class="mobile-heading-break" /> Crash on '
            "<span>Long Island</span>",
            HTML,
        )
        self.assertIn(
            'What to Expect When<br class="mobile-heading-break" /> You Contact '
            "<span>Our Office</span>",
            HTML,
        )

    def test_long_mobile_section_titles_use_full_width_without_extra_wraps(self):
        final_mobile = CSS.rsplit("@media (max-width: 760px)", 1)[1]
        first48 = final_mobile.split(
            ".atlas-home #first48.ds-sequence-section .ds-sequence-section__heading {",
            1,
        )[1].split("}", 1)[0]
        process = final_mobile.split(".atlas-home #process.sec .h2 {", 1)[1].split(
            "}", 1
        )[0]
        self.assertIn("max-width: none", first48)
        self.assertIn("white-space: nowrap", first48)
        self.assertIn("max-width: none", process)
        self.assertIn("white-space: nowrap", process)

    def test_no_fee_heading_stays_on_one_line_on_mobile(self):
        final_rule = CSS.rsplit(".atlas-home .cta-wrap .cta-h {", 1)[1].split("}", 1)[0]
        self.assertIn("max-width: none", final_rule)
        self.assertIn("white-space: nowrap", final_rule)


if __name__ == "__main__":
    unittest.main()
