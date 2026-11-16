# Drunken Glass US store: Shopify build spec

Version 1.0, 16 November 2026
Market: United States only, prices in USD
Reference build: `02-prototype/drunken-glass-us-prototype.html` (open in Chrome, every button works)
Live prototype link: https://claude.ai/artifact/4RegCau13KeqMkuNBaoL7i

If this spec and the prototype disagree, follow this spec. If Shopify works differently from the prototype, use the Shopify-native way and tell the owner what changed.

---

## 1. What we're building

A D2C store for designer borosilicate glassware: tumblers, coffee cups, teacups, cocktail glasses, sets and small add-ons. The brand is design-led and Gen Z in tone (all lowercase copy, bold colors, ink outlines). The store has two jobs:

1. **Make people want the glass**: big visuals, collections that feel like fashion drops, a quiz and gifting.
2. **Raise order value**: pack sizes, add-ons, "complete the set" bundles, build-a-set, a free-shipping goal and gift cards.

Everything visible in the prototype is in scope unless section 12 lists it as open.

---

## 2. Store setup (Shopify admin)

| Area | Setting |
|---|---|
| Markets | United States only. Currency USD. |
| Payments | Shopify Payments with Shop Pay, Apple Pay, Google Pay and PayPal. Turn on **Shop Pay Installments**: this is the "4 interest-free payments" line in the prototype (confirm eligibility). |
| Taxes | Shopify Tax. Prices exclude sales tax ("sales tax calculated at checkout"). |
| Shipping | US profile: flat **$6.95** standard rate under $75 and **free at $75+** (price-based condition). Gift cards don't require shipping. Check that gift card value does not count toward the $75 threshold. The theme meter already excludes it. |
| Customer accounts | **New customer accounts** (email plus one-time code, no passwords). This matches the prototype sign-in. |
| Checkout | One-page checkout, express buttons on, brand colors and fonts in the checkout editor. |
| Policies | Refund, privacy, terms of service, shipping and contact info from `05-content/policies.md`, after legal review. |
| Customer privacy | Turn on the US state privacy settings so the "do not sell or share my personal information" link works (it's in the footer). |
| Discount codes | `SIPSIP10`: 10% off, first order only, once per customer. See section 7 for combining rules. |
| Notifications | Brand the order, shipping and **gift card** emails (logo, colors, lowercase voice). |
| Chat | Shopify Inbox (or the chosen tool) replaces the prototype's chat card. |

---

## 3. Theme approach

- Build an **Online Store 2.0 theme** with JSON templates and sections. Start from a current Shopify free theme (for example Dawn or Horizon) for the cart, product form, gift card and accessibility plumbing, then add the custom sections in section 4.
- Don't build core templates with page-builder apps; speed matters for ads traffic.
- **Fonts** (all on Google Fonts, SIL Open Font License): Shrikhand (display), Space Grotesk 500/700 (headings and UI), Montserrat 400–700 (body), Space Mono 400/700 (prices and numbers). Self-host them in `assets/` and preload Shrikhand and Space Grotesk 700.
- **Design tokens and rules**: `06-design/tokens.css` and `06-design/design-system.md`.
- **Illustrations**: the SVGs in `07-assets` are placeholders until product photography is ready. Use the PNG renders as temporary product images so every variant has media from day one.
- Breakpoints from the prototype: 1180px (hamburger menu below this), 960px (columns stack), 760px (mobile sticky add-to-bag bar), 420px.

---

## 4. Templates and sections

Screens for each are in `03-screens/desktop`, `03-screens/mobile` and `03-screens/states`.

| Page | Template | Sections, in order (★ = custom section) |
|---|---|---|
| Home | `index.json` | announcement bar (static) · header with ★mega menu · ★hero with refraction glass · ★vibe chips · ★marquee · ★category tiles · ★product rail with tabs (new in / hero designs / under $30) · ★collection bento ("pick your era") · ★quiz · ★build-a-set teaser · ★story rows · ★gifting tiles · ★sip club sign-up · footer |
| Collection / shop | `collection.json` | ★page head (title and line change with the active collection) · ★type tabs · filters (Search & Discovery) · sort · product grid · ★empty state |
| Product: glass | `product.json` | ★gallery (4 views) · ★buy box (section 6.6) · ★complete the set · ★more from the collection · reviews (app block, hidden at 0 reviews) · ★recently viewed · ★mobile sticky bar |
| Product: accessory | `product.accessory.json` | gallery (2 views) · buy box without pack selector, add-ons or bundle · ★"glasses it goes with" rail |
| Product: set | `product.set.json` | buy box with quantity stepper (no pack selector, no bundle) |
| Gift card | `product.gift-card.json` | ★live card preview · amount buttons (variants) · native gift card recipient form · add to bag |
| Build a set | `page.build-a-set.json` | ★builder (grid plus 4-slot tray) |
| Quiz | `page.quiz.json` | ★quiz |
| Gifting | `page.gifting.json` | ★recipient tabs and product grid · gift box info cards · ★bulk/corporate form (office tab) · link to gift cards |
| Our story | `page.story.json` | ★story rows · ★process steps (6) · CTA band |
| Help | `page.help.json` | contact cards · FAQ accordion (with FAQ JSON-LD) |
| Track order | `page.track.json` | order lookup (section 6.15) |
| Wishlist | `page.wishlist.json` | ★saved products grid |
| Policies | Shopify policy pages | styled to match, with tabs for shipping / returns / privacy / terms / accessibility |
| Search | `search.json` + overlay | ★predictive search overlay (section 6.3) |
| Cart | drawer, plus `cart.json` fallback | ★bag drawer · ★"added to your bag" drawer |
| 404 | `404.json` | ★wobbling glass, "this page had one too many" |

---

## 5. Data model

**Import order:** metafield definitions → products CSV → collections → images → metaobjects.

1. **Metafield definitions**: create all of them from `04-data/metafield-definitions.csv` **before** importing products, or the metafield columns will be skipped.
2. **Products**: import `04-data/products.csv`. That's 25 products and 50 variants: 19 glasses and sets, 4 accessories, the gift box and the gift card. Everything imports as **draft**.
   - Variant option is **Color**. Swatch colors and card backgrounds per color are in `04-data/colorways-and-swatches.csv`. Use Shopify's native color swatches (or a metaobject) to show them.
   - **Variant Grams is blank on purpose.** Fill in real weights before shipping rates or a 3PL go live.
   - SKUs are suggestions (`DG-…`). Replace them if the warehouse has its own.
3. **Tags** drive collections, filters and logic:

| Tag | Meaning |
|---|---|
| `collection:<handle>` | drop collection (fruit-club, heart-eyes, golden-hour, wobble, chai-club, after-hours, y2k-bloom) |
| `vibe:<id>` | shop-by-vibe chips (chai, wfh, date, party, gift) |
| `shape:<shape>` | glass shape (can, tumbler, strawberry, heart, mug, chai, coupe, wavy, bubble, rocks), used to match add-ons |
| `addon` | shows in "finish it off" rows |
| `fits:<shape>` / `fits:all` | which glass shapes an add-on fits |
| `build-a-set` | eligible for "any 4 for $99" (glasses priced $26–$38) |
| `new` | "new in" rail and badge |
| `bundle` | pre-made set (pour decisions, date night duo) |
| `hidden` | keep out of search and collections (gift box) |

4. **Collections**: create them from `04-data/collections.json` as automated collections: drop collections, type collections, vibe collections and utility collections (build-a-set, new, extras).
5. **Metaobjects** (or section blocks, if that's easier for the client to edit):
   - quiz: `04-data/quiz.json`
   - gifting tabs: `04-data/gifting-tabs.json`
   - FAQ entries: `05-content/faq.md`
   - story rows and process steps: `05-content/copy-deck.md`
6. **Images**: upload the PNGs from `07-assets/png/products/` (named `handle--color.png`) and attach each one to its variant.
7. **Navigation**: `04-data/navigation.json`.

---

## 6. Features and acceptance criteria

### 6.1 Announcement bar
Static text, no rotation: "free US shipping on orders over $75 ✦ first order? use SIPSIP10 for 10% off". Editable in theme settings.

### 6.2 Header and mega menu
- Desktop (≥1181px): nav on the left, centered wordmark with sparkle, search / account / wishlist / bag on the right. Below 1181px: hamburger, wordmark, search and bag.
- The bag button shows a 2-digit item count and bounces when something is added.
- The **mega menu** opens on hover (desktop) and on click/tap. It has a tile for each drop collection with a product image and a tinted background, a "shop by type" list and a quiz promo tile. It closes on Esc, on an outside click and on route change.
- The account icon shows the customer's initial when signed in.

### 6.3 Predictive search overlay
- Opens as a top sheet. Use the Predictive Search API (`/search/suggest.json`) for products.
- Empty state: trending terms (theme setting list: strawberry, heart mug, chai, can glass, gift set, coupe), recent searches (localStorage, last 5) and 4 "popular right now" products.
- Pressing Enter with exactly one result goes straight to that product.

### 6.4 Product card
- Sticker badge from `custom.badge` (new / hero design / staff pick / gift pick), slightly rotated.
- Wishlist heart (top right), toggles on and off.
- Color swatch dots: tapping one swaps the card image to that variant's image and the "in {color}" line, with no page load.
- "add to bag" adds the selected variant with `/cart/add.js`, then opens the **added-to-bag drawer** (6.8).
- Sets show "save $X" against buying the pieces separately (value in `pricing-and-bundles.csv`).
- Hover (desktop): the card lifts with a 6px hard ink shadow.

### 6.5 Collection filters
- Search & Discovery filters: type, drop collection, color, price (under $30 / $30–39 / $40+), vibe (tags).
- Sort: featured, price low to high, price high to low, newest.
- Active filters show as removable pills. A "clear all filters" link is always there.
- Mobile: a filters drawer with a "show N glasses" button.
- Empty state: wobbly glass, "no glass matches that combo" and a clear button.

### 6.6 Product page buy box (the most important part)
In this order:

a. **Care at a glance pills**
   - "hot + cold safe" when `custom.hot_cold_safe` is true.
   - Dishwasher: true → "dishwasher safe", false → "hand wash only", blank → dashed "dishwasher: test pending".
   - Microwave: true → "microwave safe", false → "not for the microwave", blank → dashed "microwave: test pending".
   - The blank state must not show at launch; fill the metafields from test results.

b. **Price**: big mono price. When the pack is bigger than one, show "$X per glass" and a "you save $Y" pill. "sales tax calculated at checkout" goes underneath.

c. **Color swatches**: they select the variant. When "one of each" is selected, show the swatches as static and the label as "all N colors".

d. **Pack selector** (glasses only; hidden for accessories, sets and the gift card). A 2×2 grid of radio cards:

| Card | Adds to cart | Tag |
|---|---|---|
| single | qty 1 of the selected color | |
| pair | qty 2 of the selected color | "save $X" pill |
| set of 4 | qty 4 of the selected color | "save $X" pill, "made for hosting" tag |
| one of each (N) | qty 1 of every color variant ("mixed pair" when there are 2 colors) | "save $X" pill, mini swatch dots |

   Prices come from the discount tiers in section 7. The selected card gets an ink border, lime tint, check mark and hard shadow. Use `role="radiogroup"` / `role="radio"` with `aria-checked`.

e. **"finish it off" add-ons**: products tagged `addon` plus `fits:<this shape>` or `fits:all`, excluding `hidden`. Each is a row with a 48px image, name, one-line note (`custom.addon_note`), price and a round toggle (+ / ✓, `aria-pressed`).
   - The last row is always the **gift box + handwritten note** ($9, one per order). If it's already in the cart, the row reads "already in your bag" and the toggle is disabled.

f. **Add-to-bag button** shows the live total: pack + add-ons + gift box. One click adds everything in **one** `/cart/add.js` call (`items[]`), then opens the added-to-bag drawer and resets the add-on toggles.

g. **Express checkout**: replace the prototype's "buy with shop pay / buy with apple pay" placeholders with Shopify's dynamic checkout buttons (`{{ form | payment_button }}`). Keep a "more payment options" link.

h. **Pay-in-4 line**: replace the placeholder with the Shop Pay Installments banner (`{{ form | payment_terms }}`).

i. **Free-shipping meter**: progress to $75 = (cart merchandise subtotal, excluding gift cards, minus discounts) + the current selection. Message: "add $X more for free US shipping" / "free US shipping unlocked". The threshold is a theme setting.

j. **ZIP delivery estimate**: 5-digit validation. Show "estimated delivery to {zip}: {date} to {date}. free returns within 30 days." using business days from theme settings (now 5–8, skipping weekends). Replace with real carrier or 3PL data once fulfilment is decided.

k. **Trust row**: free breakage replacement · 30-day returns · secure checkout.

l. **Accordions**:
   - about this glass
   - specs: capacity as `fl oz (ml)` where fl oz = ml ÷ 29.574 to 1 decimal; height in inches = cm ÷ 2.54 to 1 decimal; in the box; material; works with; dishwasher; microwave; country of origin; US importer
   - how do i take care of my glass?
   - shipping, returns and breakage

m. **"bought this one? write a review"** link: opens the review app's form.

n. **Mobile sticky bar** (≤760px): product name, live total, "add to bag".

### 6.7 Complete the set (below the buy box)
- Shows this glass plus up to 2 partner pieces. Source: the Search & Discovery **complementary products** (`/recommendations/products.json?intent=complementary`), seeded from the "complete-the-set partners" column in `pricing-and-bundles.csv`.
- Each partner has a toggle. The summary shows the crossed-out total, the bundle price, "you save $X" and "add N to bag" (disabled until at least 2 pieces are on).
- Lines are added with the property `_bundle` = `fbt-<uuid>`. 10% off applies through the discount logic (section 7).
- Hidden for accessories, sets and multi-packs.

### 6.8 "Added to your bag" drawer
Opens after **every** add (card, product page, quiz, bundle, build-a-set, gift card). It shows:
- the lines just added
- the free-shipping meter (only if the cart has merchandise)
- 3 "goes well with" tiles: fitting add-ons not in the cart → same-collection glasses → other add-ons
- "view bag" and "checkout" buttons

### 6.9 Bag drawer
- Free-shipping meter.
- Lines with quantity stepper and remove. Gift cards have no stepper.
- One upsell row: the first item not already in the cart from coaster set → glass straws → street chai glasses → brush.
- Gift box + note checkbox. It adds or removes the gift box product and shows a note field (max 160 characters, saved as cart attribute "Gift note").
- Discount code field. Apply in the cart if the theme supports it, otherwise send the code to checkout. Error copy is in the copy deck.
- Totals: subtotal, discount, shipping (free / $6.95), gift box, "sales tax: at checkout", estimated total.
- "checkout securely" button and the pay-in-4 line.
- Refresh with the Section Rendering API (no full page reloads).

### 6.10 Build a set ($99 for any 4)
- The grid lists the `build-a-set` collection. Tapping a card fills the next empty slot. A count bubble shows how many of that glass are picked. Slots have an ✕ to remove.
- The tray shows the crossed-out sum, the $99 set price and "you save $X". "add set to bag" stays disabled until 4 are picked.
- The 4 lines are added with `_bundle` = `set-<uuid>`. The discount makes those 4 lines total exactly $99.
- Mobile: the tray sticks to the bottom.

### 6.11 Quiz
- 3 questions, 4 options each, with a progress bar and a "go back" link. Scoring follows `04-data/quiz.json` (add points per product handle; highest total wins).
- The result card shows the product image, name, line, price, "add to bag", "see details", "retake quiz" and a collection link.
- No data is collected.

### 6.12 Gifting page
- Tabs (from `gifting-tabs.json`): for the host / bestie / couple / mom and dad / office, plus a link chip to gift cards.
- Info cards: gift box + note, ships straight to them, take the quiz.
- The **office tab** adds a bulk/corporate form (Shopify contact form): name, company, work email, quantity band, message. It's tagged `bulk-inquiry` and sent to the sales inbox.

### 6.13 Digital gift cards
- A native Shopify gift card product (`digital-gift-card`) with variants $25 / $50 / $75 / $100 / $150 as amount buttons.
- Use Shopify's **gift card recipient** fields: recipient name, email, message and send date (today or later).
- The card preview (`07-assets/svg/brand/gift-card-*.svg`) updates live with the amount and "for {name}, from {name}".
- Gift cards are excluded from discounts and from the free-shipping meter.
- Linked from home gifting tiles, the gifting page, the mobile menu and the footer.

### 6.14 Wishlist
- The heart on cards and the product page saves the product. The header shows a count.
- The prototype saves to the device only (localStorage). Use a wishlist app if you want it to sync with customer accounts across devices.

### 6.15 Track order
- Order number + email → the Shopify order status page (order lookup app or custom page).
- The prototype timeline is a demo.
- Validation copy is in the copy deck.

### 6.16 Sip club sign-up
- Email field → Shopify customer with email marketing consent (or Klaviyo). A valid submit reveals the `SIPSIP10` code with a copy button.
- Consent line under the form.
- Corner pop-up after 16 seconds on a first visit. Dismissal is remembered. Never shown in the cart, at checkout or on mobile product pages.
- Optional: SMS sign-up, with US consent wording (see section 12).

### 6.17 Other pages
- Story rows and the 6-step process ("from furnace to your shelf").
- Help with FAQ (add FAQ JSON-LD).
- Policies with tabs, including accessibility.
- 404 page.
- Footer: 5 columns, payment chips, giant two-color wordmark, legal line.

### 6.18 Hero refraction glass (home)
- An SVG can glass of soda on blue/yellow stripes. Inside the drink, the stripes are flipped and magnified and the straw looks "broken", like real refraction.
- Desktop: the glass tilts slightly and the refraction shifts with the cursor. Touch devices: it sways on its own.
- Only animate while the hero is on screen. With `prefers-reduced-motion`, show it static.
- Source: `07-assets/svg/brand/hero-refraction-glass.svg` and the `lensSVG` / `initLens` functions in the prototype.

### 6.19 Motion rules
Only these move: the hero words wobble once on load, one lime marquee scrolls, the hero glass refracts, cards lift on hover, drawers slide and the bag bounces. Nothing else rotates or loops. Everything respects reduced motion.

---

## 7. Pricing and discount logic

The recommended approach is **one custom Discount Function** (in a small custom app) that handles all product-level rules, so they never fight each other.

| Rule | Which lines | Discount |
|---|---|---|
| **Pack tiers** | glasses (tag `shape:*`, not `bundle`, not accessories or gift cards) **without** a `_bundle` property, grouped by product (all colors together) | total qty 2 → **8%** · qty 3 → **12%** · qty 4+ → **15%** |
| **Build a set** | lines with `_bundle` = `set-<uuid>`, in groups of exactly 4 | fixed: those 4 lines total **$99** |
| **Complete the set** | lines sharing `_bundle` = `fbt-<uuid>`, when there are 2 or more | **10%** off those lines |
| **SIPSIP10** | order | 10% off, first order only |

- A line gets only **one** product discount: a bundle rule beats a pack tier.
- **Decide (owner):** can SIPSIP10 combine with the product discounts above? The prototype allows it.
- **Rounding:** the prototype rounds pack and bundle prices to whole dollars (pair $66, set of 4 $122). Exact percentages give cents (pair $66.24). `pricing-and-bundles.csv` shows both. Either accept cents or store whole-dollar prices in the optional `custom.price_pair` / `custom.price_set4` metafields and discount to reach them.
- **Gift cards:** never discounted, never counted toward free shipping.
- **Pre-made sets** (pour decisions party set, date night duo): consider Shopify Bundles (fixed bundle), so stock is deducted from the component glasses.
- **Alternative:** a quantity-breaks or bundle app. Only pick one that supports per-product tiers, line-property bundles, correct price display in the theme, and runs on Shopify Functions.

### Test cases (expected results from the prototype)
| Cart | Expected |
|---|---|
| the wobble tumbler, set of 4 ($36 × 4) + glass straws ($12) + gift box ($9) | button shows **$143** (122 + 12 + 9); free shipping unlocked |
| checkmate tumbler ($34) + $100 gift card | subtotal $134, shipping **$6.95** (gift card doesn't count), total $140.95 + tax |
| any 4 build-a-set glasses | 4 lines totalling **$99** |
| wobble tumbler + wobble mug + heart eyes mug (complete the set) | $102 → **$92** (prototype, rounded) / $91.80 (exact 10%) |
| strawberry fields, pair | **$66** (rounded) / $66.24 (exact 8%) |
| $34 order with SIPSIP10 | $3.40 off, shipping $6.95 |

---

## 8. Apps (evaluate before installing; keep the count low)

| Job | Shopify-native first | Options if you need more |
|---|---|---|
| Filters, search, complementary products | Search & Discovery | n/a |
| Reviews with photos and star ratings on cards | n/a | Judge.me, Okendo or Yotpo (pick one) |
| Email pop-up and flows (welcome, abandoned cart, post-purchase "complete your set") | Shopify Email + Shopify Forms | Klaviyo (also does SMS) |
| Chat | Shopify Inbox | n/a |
| Fixed bundles (pre-made sets) | Shopify Bundles | n/a |
| Pack tiers, build-a-set, complete-the-set pricing | custom Discount Function (section 7) | a Functions-based quantity-breaks/bundle app |
| Wishlist across devices | theme localStorage | a wishlist app |
| Order lookup page | theme page + order status | an order-tracking app |

Every app adds scripts. Check Lighthouse before and after each install.

---

## 9. Tracking

- GA4 and Meta (pixel + Conversions API) through Shopify's customer events / Meta sales channel.
- Standard events: `view_item`, `view_item_list`, `add_to_cart` (with every item, including add-ons), `begin_checkout`, `purchase`.
- Custom events (fire to the data layer):

| Event | Parameters |
|---|---|
| `pack_selected` | product, pack (single / pair / set4 / every) |
| `addon_toggled` | product, addon, on/off |
| `bundle_added` | type (fbt / build-a-set), items, value |
| `quiz_completed` | result product |
| `gift_card_added` | amount |
| `express_click` | method |
| `zip_checked` | zip prefix only (first 3 digits) |
| `filter_used` | filter, value |

---

## 10. Performance and accessibility

- **Targets:** Lighthouse mobile performance ≥ 85, accessibility ≥ 95; LCP under 2.5s on 4G.
- Inline small SVGs. Lazy-load everything below the fold. Use `srcset` product images once photography arrives.
- **WCAG 2.1 AA:**
  - visible keyboard focus (3px blue outline)
  - radiogroup semantics for packs and gift card amounts
  - `aria-pressed` on toggles
  - drawers and modals trap focus, close on Esc and return focus to the trigger
  - text colors from the tokens (muted grey #57534e on white passes AA)
- Respect `prefers-reduced-motion` everywhere.

---

## 11. Content

- `05-content/copy-deck.md`: every page's copy, microcopy, empty states and error messages.
- `05-content/faq.md` and `05-content/policies.md`.
- Voice: all lowercase (brand names in product copy too), US spelling, short sentences, dry and clever. No fake reviews, testimonials or follower counts anywhere.

---

## 12. Open items before launch

**Decisions (Drunken Glass):**
1. **Fulfilment:** ship from a US warehouse/3PL or from India. This affects delivery estimates, duties and the "ships from the US" badge plus holiday cut-off banner, which aren't built yet.
2. Final USD prices, the pack discount %s, the $75 threshold, accessory SKUs and sourcing.
3. Whether SIPSIP10 combines with pack and bundle discounts.
4. Review app, email/SMS tool and wishlist approach.
5. Personalisation (initials on glass): left out until production confirms it's possible.

**Content and data:**
6. Dishwasher and microwave test results for every design (fill the metafields; the "test pending" pills must be gone at launch).
7. Lead and cadmium testing of printed and colored designs (lip-and-rim area), and a California Prop 65 warning if results require it.
8. Variant weights (grams).
9. US importer of record, legal entity name, US contact address, support email and hours, social handles.
10. Real product photography and video (5 shots per hero design). Replace the placeholder PNGs.
11. Legal review of the policies, and the accessibility statement.

---

## 13. QA checklist

- [ ] Every page in `03-screens` matches at 1440px and 390px.
- [ ] All the cart math test cases in section 7 pass.
- [ ] Pack selector, add-ons, gift box, express buttons and pay-in-4 banner work on iOS Safari and Android Chrome.
- [ ] The added-to-bag drawer opens after every kind of add.
- [ ] Gift card: recipient email arrives on the chosen date; the card can't be discounted; it doesn't count toward free shipping.
- [ ] Build-a-set: exactly $99 for 4; removing one line removes the set discount.
- [ ] Complete-the-set: 10% only when 2 or more pieces from the same bundle are in the cart.
- [ ] Filters, sort and the empty state work; the mobile filter drawer shows the right count.
- [ ] Keyboard-only run through product page → bag → checkout.
- [ ] Reduced motion: hero static, marquee stopped.
- [ ] Footer privacy link and policies pages are live.
- [ ] No "test pending", dashed placeholder or "to be added" text left anywhere.
