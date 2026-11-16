# Design system: Drunken Glass US store

The look is **a sticker board for glassware**: ink-outlined blocks, hard offset shadows, slightly tipsy rotations, bold brand colors, and one big "wow" moment (the refraction glass in the hero). The ink outlines and flat colors do the work, so no gradients behind UI, no soft blurry shadows and no glassmorphism.

All values are in `tokens.css`. The prototype's full stylesheet is inside `02-prototype/drunken-glass-us-prototype.html` (the `<style>` block) if you want exact numbers.

---

## Color roles
| Token | Hex | Use | Don't |
|---|---|---|---|
| blue | #2765fa | primary buttons (add to bag, checkout), links, focus ring, meter fill, hero background | body text |
| berry | #ef426f | "save $X" pills, badges, sale accents, error-adjacent highlights | large backgrounds behind long text |
| lime | #eaef29 | marquee, quick-add buttons, selected pack tint (#f8fac4), sign-up button on berry | text on white |
| ink | #0a0a0a | all text, 2px outlines, hard shadows, dark buttons | n/a |
| cloud | #f2f1f0 | alternating section backgrounds, panels, field prefixes | n/a |
| tints | #ffe1e8 / #dfe8ff / #f8fac4 | product card and tile backgrounds (each colorway has its own, see `colorways-and-swatches.csv`) | n/a |

## Type
| Role | Font | Size / weight |
|---|---|---|
| Hero headline | Shrikhand | 46–104px, words rotated -3° to +3° |
| Section titles (h2) | Shrikhand | 34–62px |
| Product title | Space Grotesk 700 | 32–50px, tight tracking |
| Product names on cards, buttons, labels, nav | Space Grotesk 700 | 13–19px |
| Body | Montserrat 500 | 16px / 1.55 |
| Prices, counts, codes, SKUs | Space Mono 700 | 13–32px |

- Copy is **all lowercase**, except discount codes (SIPSIP10) and payment brand chips.
- Don't add uppercase eyebrow labels.

## Shape and depth
- **Outline:** 2px solid ink on cards, buttons, inputs, drawers and panels.
- **Radius:** 6px on cards, buttons and inputs; 10px on big panels; pills on chips, badges and icon buttons.
- **Shadow:** none at rest. On hover, a **hard 6px ink offset** and the element moves up-left 3–4px. Selected pack cards keep a 4px shadow. Big panels (hero lens, quiz, build-a-set band, bundle box) carry a permanent 10px shadow.
- **Stickers:** badges are pills rotated -5°. The hero pill and lens tags rotate ±2–3°.

## Components
| Component | Spec |
|---|---|
| Button | 50px tall (56px for the main add-to-bag), 2px ink border, Space Grotesk 700 16px. Variants: blue/white, lime/ink, ink/white, white/ink. Hover: lift + hard shadow. |
| Add-to-bag (product page) | Blue button, label left, live total right (Space Mono) behind a thin white divider. |
| Express buttons | 2-up grid: Shop Pay (#5a31f4) and Apple Pay (black), 50px tall. Replace with Shopify's dynamic checkout buttons. |
| Chip | 40px pill, 2px ink border. Hover: lime. Active: ink with white text. |
| Product card | White, 2px ink border. Media area is 4:4.4 on the colorway tint with a 2px ink line under it. Badge top-left, heart top-right (38px circle). Name in Space Grotesk 17px, "in [color]" muted, price in mono, swatch dots (22px), lime "add to bag" pill. |
| Swatch | 22px circle (36px on the product page), 2px ink border. Selected: white gap ring + ink ring. |
| Pack card | Radio card, 2px #d6d2cc border; selected = ink border, lime tint, check circle, 4px shadow, nudged up-left. Berry "save $X" pill sits on the top edge. |
| Add-on row | 48px image tile, name (Space Grotesk 14px), one-line note (12px muted), mono price, 34px round toggle (+ / ✓; on = ink with lime check). Rows divided by 1.5px hairlines inside a 2px ink box with a cloud header row. |
| Free-shipping meter | Lime-tint box, 2px ink border, message in Space Grotesk 700 14px, 12px bar with ink outline and blue fill. |
| Care pill | 2px ink pill on cloud with an icon. "Test pending" is a dashed outline on white in muted text (remove before launch). |
| Drawer | Slides in from the right (bag) or left (menu), max 440px wide, 2px ink edge. Header in Shrikhand 28px. Footer area on cloud. |
| Modal | Centered, 2px ink border, 10px radius, 10px hard shadow. |
| Toast | Ink pill at the bottom center with lime text, pops up with a springy ease. |
| Accordion | 2px ink rules between rows, Space Grotesk 17px summary, "+" rotates to "×" when open. |
| Inputs | 46–52px tall, 2px ink border, 6px radius. Focus: 3px lime glow. Prefix boxes (like "+1") sit on cloud. |

## Illustration style
- Flat glass drawings with 4px ink outlines, translucent color fills, white highlight strips and a soft ground shadow. Patterns (cherries, lemons, daisies, hearts, checks, stars, clouds, waves, polka dots, seeds) are printed inside the glass.
- Source files: `07-assets/svg/products` (each glass and colorway), `07-assets/svg/brand` (hero refraction glass, story art, gift card, badge) and `07-assets/svg/icons` (UI icons, 24px grid, 2.2–2.6 stroke).
- These are **placeholders** until photography. When photos arrive, shoot on the same tint backgrounds so the cards keep the sticker-board look.

## Motion (keep it calm)
Allowed:
- the hero headline words wobble once on load
- one lime marquee scrolls
- the hero glass tilts and refracts (cursor on desktop, gentle sway on touch, only while visible)
- hover lifts
- drawers slide (300ms)
- the bag button bounces when an item is added
- toasts pop

Everything else stays still. Respect `prefers-reduced-motion`.

## Accessibility
- Focus ring: 3px blue outline, 3px offset, on everything interactive.
- Contrast: text is ink or #57534e. White text only on blue, berry and ink. Never put lime text on white.
- Pack cards and gift card amounts are radio groups; toggles use `aria-pressed`. Drawers trap focus, close on Esc and return focus to the trigger.
