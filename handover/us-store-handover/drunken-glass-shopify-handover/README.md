# Drunken Glass US store: developer handover

Hi! This folder has everything needed to build the Drunken Glass US store on **Shopify**.

**Start here:**
1. Open `02-prototype/drunken-glass-us-prototype.html` in Chrome and click around. Every page, drawer and button works. It's the reference for how things should look and behave.
2. Read `01-build-spec.md`. It maps every feature to Shopify (templates, data, discounts, apps) and has acceptance criteria and test cases.

## What's in the folder
| Folder / file | What it is |
|---|---|
| `01-build-spec.md` | The build spec: store setup, templates and sections, data model, feature specs, discount logic, apps, tracking, performance, open items and the QA checklist |
| `02-prototype/` | Clickable single-file prototype (HTML, CSS and JS in one file) |
| `03-screens/desktop/` | 17 full-page screenshots at 1440px |
| `03-screens/mobile/` | the same 17 pages at 390px (2x) |
| `03-screens/states/` | drawers, modals, menus, filters, quiz result, buy box states |
| `04-data/products.csv` | **Shopify product import** (25 products, 50 variants, imports as draft). Includes metafield columns. |
| `04-data/metafield-definitions.csv` | Metafields to create **before** importing products |
| `04-data/colorways-and-swatches.csv` | Swatch color, card background and placeholder image for every variant |
| `04-data/pricing-and-bundles.csv` | Unit prices, pack prices, discount tiers, build-a-set eligibility, complete-the-set partners |
| `04-data/collections.json` | Automated collections and their rules |
| `04-data/quiz.json` | Quiz questions, options and scoring |
| `04-data/gifting-tabs.json` | Gifting page tabs and products |
| `04-data/navigation.json` | Header, mega menu and footer menus |
| `04-data/catalogue-source.json` | Raw catalogue data from the prototype (for reference) |
| `05-content/copy-deck.md` | All page copy, microcopy, empty states and error messages |
| `05-content/faq.md`, `policies.md` | Help page FAQ and policy drafts (policies need legal review) |
| `06-design/tokens.css` | Colors, fonts, sizes, borders, shadows, breakpoints |
| `06-design/design-system.md` | How components look and behave, motion and accessibility rules |
| `07-assets/svg/` | Product illustrations (one per colorway), brand art (hero glass, story art, gift card, badge), UI icons |
| `07-assets/png/products/` | 1200×1200 placeholder product images (named `handle--color.png`) plus the gift card image |

## Suggested build order
1. **Store setup** (spec section 2): US market, payments with Shop Pay Installments, Shopify Tax, shipping ($6.95 / free over $75), new customer accounts, privacy settings.
2. **Metafield definitions** → **import `products.csv`** → create **collections** → upload placeholder **images**.
3. **Theme base** (OS 2.0) + **tokens** + fonts.
4. Header, mega menu, search, footer → product card → collection page with filters.
5. **Product page buy box** (spec 6.6), then complete-the-set, the added-to-bag drawer and the bag drawer.
6. **Discount Function** (spec section 7) for pack tiers, build-a-set and complete-the-set.
7. Home page sections → build a set → quiz → gifting → gift cards → story, help, policies, track, wishlist, 404.
8. Apps (reviews, email/SMS, chat), tracking events, the QA checklist (spec 13).

## Placeholders: please don't launch with these
- Prices, discounts and the $75 threshold are sample values. Confirm them with the owner.
- **Variant weights** are blank in the CSV.
- "test pending" dishwasher/microwave pills, importer, legal entity, US address, support email: see spec section 12.
- All product images are illustrations until photography arrives.
- The prototype's sign-in, order tracking, ZIP estimate and form submissions are demos. Use the Shopify-native versions described in the spec.

Questions about the brand or business: ask the owner. Questions about how something should behave: check the prototype first, then the spec.
