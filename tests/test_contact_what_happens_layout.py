import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CSS = (ROOT / "inner-atlas.css").read_text(encoding="utf-8")
HTML = (ROOT / "contact" / "index.html").read_text(encoding="utf-8")


class ContactWhatHappensLayoutTests(unittest.TestCase):
    def test_heading_is_wider_and_left_column_cards_share_one_edge(self):
        fix = CSS.split("QUICK FIX 8 — Contact follow-up layout", 1)[1]
        self.assertIn("#what-happens .h2", fix)
        self.assertIn("max-width: 18ch", fix)
        self.assertIn("text-wrap: wrap", fix)
        self.assertIn("font-size: clamp(2.35rem, 11.5vw, 3.5rem)", fix)
        self.assertIn("padding-inline: 1rem", fix)
        self.assertIn(".acard:nth-child(2n + 1)", fix)
        self.assertIn("padding-left: 24px", fix)
        self.assertIn("border-left: 0", fix)

    def test_contact_page_requests_current_inner_styles(self):
        self.assertIn("inner-atlas.css?v=contact-layout-13", HTML)


if __name__ == "__main__":
    unittest.main()
