import unittest
from pathlib import Path


CSS = (
    Path(__file__).resolve().parents[1]
    / "practice-areas"
    / "practice-atlas.css"
).read_text(encoding="utf-8")


class PracticeClaimMobileTests(unittest.TestCase):
    def test_shared_mobile_claim_heading_stays_on_one_line(self):
        quick_fix = CSS.split("QUICK FIX 5 — One-line mobile claim heading", 1)[1]
        self.assertIn(
            "main #protect.claim-stage .claim-stage__title",
            quick_fix,
        )
        self.assertIn("max-width: none", quick_fix)
        self.assertIn("flex-wrap: nowrap", quick_fix)
        self.assertIn("white-space: nowrap", quick_fix)


if __name__ == "__main__":
    unittest.main()
