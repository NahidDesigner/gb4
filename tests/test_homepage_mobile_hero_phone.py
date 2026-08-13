from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
CSS = (ROOT / "styles.css").read_text(encoding="utf-8")


class HomepageMobileHeroPhoneTests(unittest.TestCase):
    def test_phone_link_is_inside_hero_copy_after_headline(self):
        hero_copy = re.search(r'<div class="hero-copy">(.*?)</div>', HTML, re.S)
        self.assertIsNotNone(hero_copy)
        fragment = hero_copy.group(1)
        self.assertRegex(
            fragment,
            r'class="hero-h1"[\s\S]*?class="hero-phone" href="tel:\+15164441000"',
        )
        self.assertIn('(516) 444-1000', fragment)
        self.assertIn('<use href="#i-phone"', fragment)

    def test_phone_button_is_hidden_by_default_and_mobile_only(self):
        self.assertRegex(CSS, r'\.hero-phone\s*\{[^}]*display:\s*none')
        mobile = re.search(r'@media\s*\(max-width:\s*640px\)(.*)', CSS, re.S)
        self.assertIsNotNone(mobile)
        self.assertRegex(
            mobile.group(1),
            r'\.hero-phone\s*\{[^}]*display:\s*inline-flex[^}]*min-height:\s*48px',
        )

    def test_phone_button_has_focus_and_reduced_motion_rules(self):
        self.assertIn('.hero-phone:focus-visible', CSS)
        reduced = re.search(
            r'@media\s*\(prefers-reduced-motion:\s*reduce\)(.*)', CSS, re.S
        )
        self.assertIsNotNone(reduced)
        self.assertIn('.hero-phone', reduced.group(1))


if __name__ == "__main__":
    unittest.main()
