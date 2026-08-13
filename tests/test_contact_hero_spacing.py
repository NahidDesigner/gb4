import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INNER_CSS = (ROOT / "inner-atlas.css").read_text(encoding="utf-8")


def rule(marker: str) -> str:
    start = INNER_CSS.index(marker)
    opening = INNER_CSS.index("{", start)
    closing = INNER_CSS.index("}", opening)
    return INNER_CSS[opening + 1 : closing]


class ContactHeroSpacingTests(unittest.TestCase):
    def test_contact_hero_label_is_inset_from_the_left_border(self):
        label = rule("main:has(#reach) .page-head::before")
        self.assertIn("left: clamp(1.15rem, 2vw, 1.55rem)", label)

    def test_contact_hero_rule_sits_below_the_subtitle(self):
        divider = rule("main:has(#reach) .sec--tight::after")
        self.assertIn("bottom: clamp(1.75rem, 2.6vw, 2.4rem)", divider)


if __name__ == "__main__":
    unittest.main()
