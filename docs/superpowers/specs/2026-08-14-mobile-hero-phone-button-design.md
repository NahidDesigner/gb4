# Mobile Homepage Hero Phone Button

## Scope

Add one telephone call-to-action inside the existing homepage hero. The control appears only at mobile widths and sits immediately below the sentence ending “We exceed them.” No other homepage section, hero copy, image, heading, typography, masthead, scroll cue, or sticky action bar changes.

## Design

The control is a centered, compact gold button that reads `(516) 444-1000` and includes the project’s existing phone SVG icon. Its gold surface and navy foreground echo the existing hero lockup and mobile action bar, giving the action clear contrast without introducing a new visual language.

The button uses a minimum 48px touch height, balanced horizontal padding, a modest corner radius, and a subtle inset highlight and shadow so it remains legible over the photographic hero. Touch and keyboard activation receive visible feedback through a short translate/shadow change and an accessible focus outline. Motion is removed when `prefers-reduced-motion` is enabled.

## Structure and behavior

- Add one semantic telephone anchor within `.hero-copy`, immediately after `.hero-h1`.
- Reuse the existing `#i-phone` SVG symbol rather than introducing another icon or asset.
- Use `href="tel:+15164441000"` and visible text `(516) 444-1000`.
- Hide the control by default and reveal it only at the existing phone breakpoint, below 641px.
- Preserve the current mobile sticky action bar, which remains hidden while the hero is visible and appears after the hero exits.
- Preserve the desktop hero exactly; the new anchor must compute to `display: none` at 641px and above.

## Responsive constraints

- At 320px and 375px widths, the button stays within the hero and does not collide with the fixed “Scroll to explore” cue.
- The control remains centered and does not cause horizontal overflow.
- The hero retains its `100svh` minimum height and existing image crop.
- At desktop width, geometry and visible content remain unchanged.

## Accessibility

- The visible number provides an unambiguous action target.
- The phone icon is decorative and marked `aria-hidden="true"`.
- The link remains keyboard operable and has a visible `:focus-visible` state.
- The tap target is at least 44×44px.
- Foreground/background contrast meets WCAG AA.

## Verification

- Add a static contract test that fails before implementation and confirms the telephone link, existing icon, mobile-only CSS, touch target, and desktop-hidden default.
- Capture paired screenshots at 375px and 1440px.
- Measure button placement, touch dimensions, content containment, scroll-cue clearance, and horizontal overflow.
- Confirm the button is absent from desktop layout and browser diagnostics contain no errors.
