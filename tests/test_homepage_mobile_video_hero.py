from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
CSS = (ROOT / "homepage-atlas.css").read_text(encoding="utf-8")
JS = (ROOT / "homepage-atlas.js").read_text(encoding="utf-8")
HERO_JS = (ROOT / "hero-video.js").read_text(encoding="utf-8")


class HomepageMobileVideoHeroTests(unittest.TestCase):
    def test_mobile_vimeo_background_is_progressively_loaded(self):
        self.assertIn(
            'data-mobile-src="https://player.vimeo.com/video/1224408820?background=1&amp;autoplay=1&amp;loop=1&amp;muted=1&amp;autopause=0&amp;controls=0&amp;playsinline=1&amp;dnt=1"',
            HTML,
        )
        self.assertIn(
            'data-desktop-src="https://player.vimeo.com/video/1224409606?background=1&amp;autoplay=1&amp;loop=1&amp;muted=1&amp;autopause=0&amp;controls=0&amp;playsinline=1&amp;dnt=1"',
            HTML,
        )
        self.assertRegex(
            HTML,
            r'<iframe class="hero-video__frame"[^>]*title=""[^>]*aria-hidden="true"[^>]*tabindex="-1"[^>]*allow="autoplay; fullscreen; picture-in-picture"',
        )
        self.assertNotRegex(HTML, r'<iframe class="hero-video__frame"[^>]*\ssrc=')
        self.assertIn("dataset.mobileSrc", HERO_JS)
        self.assertIn("dataset.desktopSrc", HERO_JS)
        self.assertIn('(prefers-reduced-motion: reduce)', HERO_JS)
        self.assertIn('removeAttribute("src")', HERO_JS)

    def test_desktop_vimeo_loops_its_first_six_seconds(self):
        self.assertIn('"addEventListener","timeupdate"', HERO_JS)
        self.assertRegex(HERO_JS, r"Number\([a-z]\.data\?\.seconds\)")
        self.assertIn(">=6", HERO_JS)
        self.assertIn('"setCurrentTime",0', HERO_JS)
        self.assertIn('(max-width: 640px)', HERO_JS)

    def test_homepage_motion_javascript_stays_within_budget(self):
        total_bytes = len(JS.encode("utf-8")) + len(HERO_JS.encode("utf-8"))
        self.assertLessEqual(total_bytes, 8192)

    def test_mobile_copy_uses_the_approved_order_and_existing_claim(self):
        hero_copy = re.search(r'<div class="hero-copy">(.*?)</div>', HTML, re.S)
        self.assertIsNotNone(hero_copy)
        fragment = hero_copy.group(1)
        ordered = re.compile(
            r'hero-proof__injured">Injured\?</span>[\s\S]*?'
            r'hero-proof__over">Over</span>[\s\S]*?'
            r'\$100 Million\+[\s\S]*?Recovered for clients[\s\S]*?'
            r'Your expectations should be met\.[\s\S]*?We exceed them\.',
            re.I,
        )
        self.assertRegex(fragment, ordered)
        self.assertEqual(1, fragment.lower().count("$100 million+"))

    def test_desktop_copy_matches_the_client_reference_hierarchy(self):
        hero_copy = re.search(r'<div class="hero-copy">(.*?)</div>', HTML, re.S)
        self.assertIsNotNone(hero_copy)
        fragment = hero_copy.group(1)
        self.assertIn(
            '<span class="hero-proof__label-desktop">Recovered for clients</span>',
            fragment,
        )
        self.assertNotIn("in Settlements", fragment)

        marker = "DESKTOP HERO PROOF — client reference composition"
        self.assertIn(marker, CSS)
        desktop = CSS.split(marker, 1)[1].split(
            "Keep the approved mobile hero authoritative", 1
        )[0]
        self.assertRegex(desktop, r'@media\s*\(min-width:\s*641px\)')
        self.assertRegex(
            desktop,
            r'\.atlas-home \.hero-proof__injured\s*\{[^}]*display:\s*block',
        )
        self.assertRegex(
            desktop,
            r'\.atlas-home \.hero-h1__injured\s*\{[^}]*display:\s*none',
        )
        self.assertRegex(
            desktop,
            r'\.atlas-home \.hero-proof__main\s*\{[^}]*white-space:\s*nowrap',
        )
        self.assertRegex(
            desktop,
            r'\.atlas-home \.hero-proof__main > span::before,\s*'
            r'\.atlas-home \.hero-proof__main > span::after\s*\{[^}]*content:\s*""',
        )

    def test_mobile_logo_and_menu_are_scoped_from_desktop(self):
        block = CSS.split("RESPONSIVE HERO VIDEO — client-supplied Vimeo compositions", 1)[1]
        self.assertRegex(block, r'\.atlas-home \.hero-video\s*\{[^}]*display:\s*block')
        self.assertRegex(
            block,
            r'\.atlas-home \.lockup\s*\{[^}]*top:\s*max\(2rem,\s*calc\(env\(safe-area-inset-top\)\s*\+\s*1rem\)\)',
        )
        self.assertRegex(
            block,
            r'\.atlas-home \.lockup-mark img\s*\{[^}]*width:\s*clamp\(8rem,\s*40vw,\s*10\.5rem\)',
        )
        self.assertRegex(
            block,
            r'\.atlas-home \.lockup-mark\s*\{[^}]*transform:\s*translateY\(3\.5rem\)',
        )
        self.assertRegex(block, r'\.atlas-home \.lockup-menu\s*\{[^}]*min-width:\s*64px[^}]*min-height:\s*64px')
        self.assertRegex(block, r'\.atlas-home \.lockup-search\s*\{[^}]*display:\s*none')
        desktop = re.search(r'@media\s*\(min-width:\s*641px\)(.*)', block, re.S)
        self.assertIsNotNone(desktop)
        desktop_video = desktop.group(1).split(
            "@media (prefers-reduced-motion: reduce)", 1
        )[0]
        self.assertNotRegex(desktop_video, r'\.atlas-home \.hero-video\s*\{[^}]*display:\s*none')
        self.assertRegex(
            desktop_video,
            r'\.atlas-home \.hero-video__frame\s*\{[^}]*width:\s*max\(100vw,\s*177\.78svh\)[^}]*height:\s*max\(100svh,\s*56\.25vw\)',
        )

    def test_narrow_mobile_metric_reserves_a_readable_side_gutter(self):
        mobile = re.search(r'@media\s*\(max-width:\s*640px\)(.*)', CSS, re.S)
        self.assertIsNotNone(mobile)
        self.assertRegex(
            mobile.group(1),
            r'\.atlas-home \.hero-proof__main\s*\{[^}]*font-size:\s*clamp\(2\.8rem,\s*13vw,\s*3\.55rem\)',
        )

    def test_reduced_motion_keeps_the_static_poster(self):
        reduced = re.search(
            r'@media\s*\(prefers-reduced-motion:\s*reduce\)(.*)', CSS, re.S
        )
        self.assertIsNotNone(reduced)
        self.assertRegex(reduced.group(1), r'\.atlas-home \.hero-video\s*\{[^}]*display:\s*none')

    def test_client_fallback_posters_are_used_at_the_matching_breakpoints(self):
        self.assertTrue((ROOT / "assets" / "hero-video-fallback-mobile.png").is_file())
        self.assertTrue((ROOT / "assets" / "hero-video-fallback-desktop.png").is_file())
        self.assertIn(
            '<link rel="preload" as="image" href="assets/hero-video-fallback-mobile.png" media="(max-width: 640px)" />',
            HTML,
        )
        self.assertIn(
            '<link rel="preload" as="image" href="assets/hero-video-fallback-desktop.png" media="(min-width: 641px)" />',
            HTML,
        )

        marker = "RESPONSIVE HERO POSTERS — client-supplied video fallbacks"
        self.assertIn(marker, CSS)
        posters = CSS.split(marker, 1)[1]
        self.assertRegex(
            posters,
            r'\.atlas-home \.hero-bg\s*\{[^}]*background-image:\s*url\("assets/hero-video-fallback-mobile\.png"\)',
        )
        self.assertRegex(
            posters,
            r'@media\s*\(min-width:\s*641px\)\s*\{[^}]*'
            r'\.atlas-home \.hero-bg\s*\{[^}]*background-image:\s*url\("assets/hero-video-fallback-desktop\.png"\)',
        )

    def test_homepage_requests_the_mobile_video_hero_assets(self):
        self.assertIn(
            'homepage-atlas.css?v=responsive-video-hero-2',
            HTML,
        )
        self.assertIn(
            'homepage-atlas.js?v=responsive-video-hero-2',
            HTML,
        )
        self.assertIn(
            'hero-video.js?v=desktop-six-second-loop-1',
            HTML,
        )


if __name__ == "__main__":
    unittest.main()
