# DRUNKEN GLASS — DEVELOPER HANDOVER
### Everything needed to quote, scope and build this website

**Version:** 1.0 · **Owners:** Amit Gupta & Rahul Gupta · **Contact:** [your email / phone]

---

## 0.1 Read this first

This single document contains **the complete brief and the complete technical specification** for the Drunken Glass website. Nothing else is required to quote the job.

A companion folder, `design-reference/`, contains **14 working HTML pages**. They are a *visual and behavioural prototype* — every page, layout, interaction and piece of copy is already decided and demonstrated. **They are not production code.** Every price and rule in them is a hard-coded placeholder that must be re-implemented server-side.

**Document map**
| Part | Contents |
|---|---|
| **0 — Handover** (this part) | Scope, what's supplied, what's needed, phases, questions to ask, acceptance |
| **1 — The business** | Brand, audiences, positioning |
| **2 — Design system** | Colours, type, components, responsive rules |
| **3 — Global elements** | Nav, footer, badges, SEO |
| **4 — Commercial rules** | Every price, discount, minimum, tax rule |
| **5 — Page specs** | All 14 pages, section by section |
| **6 — Backend** | Data model, pricing engine, API, auth, admin |
| **7 — Integrations** | GoKwik, Razorpay, GSTIN, shipping, email |
| **8 — Delivery** | Phases, placeholders, compliance, definition of done |

---

## 0.2 What is being built, in one paragraph

A hybrid **D2C + B2B glassware e-commerce website** for the Indian market. Consumers browse and buy at public prices with COD or prepaid (prepaid earns 5% off). Businesses apply for a trade account, get GSTIN-verified, and only then see wholesale pricing — with quantity tiers up to 70% off, a 50-piece-per-design minimum, a ₹10,000 minimum order, and **100% prepaid payment**. A third flow handles corporate gifting by quotation. All three share one brand, one design system, and one catalogue.

---

## 0.3 What is already done (do not re-do this)

- **All visual design** — colours, typography, components, layout, responsive behaviour. See Part 2 and the prototype.
- **All copy** — every headline, description, policy and FAQ answer is written. Use it verbatim.
- **All commercial logic** — every discount, minimum, tier and tax rule is decided. See Part 4.
- **All 14 page structures** — sections, order, features and interactions. See Part 5.
- **Prototype of every page**, including working sliders, calculators, tier pricing, order drawer, proforma generation and the GST split.

**The developer's job is to make it real and safe**, not to redesign it. Raise anything that looks wrong — but changes to design or commercial rules are the founders' call, not assumptions to make.

---

## 0.4 Scope of work

**In scope**
1. Build the production site from this spec (framework of your recommendation — Next.js suggested).
2. Database, authentication, and an admin panel.
3. **Server-side pricing engine** enforcing every rule in Part 4.
4. Trade account application → GSTIN verification → approval → gated catalogue.
5. Consumer checkout via **GoKwik**, settling through a licensed payment aggregator.
6. Proforma invoice generation with the correct GST split, plus sequential tax invoices on dispatch.
7. Order management, tracking integration, and all transactional emails.
8. Deployment, environment configuration, and handover documentation.

**Explicitly out of scope unless quoted separately**
- Product photography and content entry
- Logo/brand asset design (the wordmark is type-set, not a drawn logo)
- Legal review of policies (a lawyer's job)
- GST/HSN confirmation (a CA's job)
- Ongoing maintenance, unless separately agreed
- Marketing, SEO content, ads

---

## 0.5 What the founders will supply

Have these ready before the build starts — a developer will stall without them.

| Item | Needed for |
|---|---|
| Legal entity name, registered address, **GSTIN**, state code | Invoices, policies, contact, gateway onboarding |
| Bank account details + UPI ID | Proforma, payouts |
| Real phone number and email addresses (support / trade / gifting) | Contact page, gateway verification |
| Grievance officer name and contact | Privacy policy (legally required) |
| **Final product list** — 100+ designs with names, category, material, MRP, capacity, height, stock | Catalogue |
| **Product photography** (including mixed-colour shots) | Every page |
| Real dispatch and delivery day ranges | Shipping policy |
| Lawyer-reviewed policy text | Policies page |
| CA confirmation of HSN 7013 / 18% GST | Invoicing |
| Accounts + API keys: hosting, database, **Razorpay** (or equivalent), **GoKwik**, GSTIN verification API, email provider, courier (e.g. Shiprocket) | Everything |
| Domain and DNS access | Deployment |
| Founding year, hometown, export countries, one true anecdote | About page personalisation |
| Real customer reviews (when available) | Product pages — **never publish invented reviews** |

---

## 0.6 Suggested phasing

Quote these separately so the founders can stage the spend.

**Phase 1 — Launchable store**
Catalogue · consumer browse → product → cart → GoKwik checkout · prepaid 5% and free shipping · trade application → GSTIN verify → approval → gated catalogue with tier pricing, MOQ and MOV · proforma with correct GST split · gifting and contact forms · policies, contact, track order, 404 · config table · minimal admin.

**Phase 2 — B2B depth**
Reorder · replenishment schedules · trade order history and invoice downloads · preorder automation · multi-address gifting fulfilment · prepaid-vs-COD analytics.

**Phase 3 — Scale**
Multiple users per company with approval thresholds · multi-outlet split shipping · WhatsApp ordering · annual volume rebates · CSV bulk upload · case-pack ordering · spec sheets · back-in-stock alerts · venue-branded glassware · net terms.

---

## 0.7 Questions a developer should ask before quoting

1. Custom build (Next.js + database) or Shopify with B2B apps? *(Trade-offs in Part 8.2. The tier logic, MOQ/MOV, proforma and replenishment are the awkward parts on Shopify.)*
2. Who owns hosting and the ongoing maintenance relationship after launch?
3. Is GoKwik confirmed, and which payment aggregator sits behind it?
4. How many SKUs at launch, and who enters the catalogue data?
5. Is there an existing accounting system that tax invoices must reconcile with?
6. What are the real dispatch and delivery SLAs?
7. Single admin user, or multiple staff with roles?
8. Does the founder need a staging environment for review?

---

## 0.8 Non-negotiables

These are not preferences. Getting them wrong creates financial, legal or security exposure.

1. **The browser is never trusted.** Every price, discount, minimum, stock check, tax split and access decision is computed and enforced server-side, and re-verified before any payment is taken.
2. **Wholesale prices must be unreachable without an approved trade account** — verified by calling the API directly with no session.
3. **MOQ 50/design and MOV ₹10,000 cannot be bypassed from the client.**
4. **Trade and gifting orders accept 100% prepaid only.** No COD, no part-payment.
5. **GST split is derived from the buyer's GSTIN state code**, server-side: same state → CGST 9% + SGST 9%; other state → IGST 18%. Rate is always 18%, HSN 7013.
6. **Tax invoice numbering must be sequential and GST-compliant**, in its own series separate from proformas.
7. **Payment status comes from webhooks**, never from a browser redirect. Order creation and payment capture must be idempotent.
8. **No card data is ever stored.**
9. **Contact and policy pages must be live** before payment-provider onboarding — providers verify them.
10. **Mobile is the primary case.** ~70% of traffic. Every page must be fully navigable on a phone.

---

## 0.9 Acceptance criteria

The build is done when all of the following are true:

- [ ] No dead links on any page, desktop or mobile; the mobile menu reaches every page.
- [ ] All pricing, discounts, minimums and tax computed server-side and re-verified before payment.
- [ ] Wholesale pricing returns nothing for an unapproved or unauthenticated caller (tested via direct API call).
- [ ] MOQ and MOV cannot be bypassed by manipulating the client.
- [ ] Trade checkout rejects anything other than 100% prepaid.
- [ ] GST split correct for both intra-state and inter-state orders; place of supply recorded.
- [ ] Proforma and tax invoice numbering sequential and compliant.
- [ ] Every form submission is persisted **and** emailed to the right address.
- [ ] Consumer checkout completes end-to-end with a real payment, prepaid and COD.
- [ ] Trade flow completes end-to-end: apply → verify → approve → sign in → order → proforma → pay.
- [ ] Admin can approve accounts, edit catalogue and stock, and change every value in the config table without a deploy.
- [ ] Lighthouse passes performance, accessibility and SEO on mobile.
- [ ] Handover includes source code, deployment docs, environment variable list, and admin instructions.

---

## 0.10 How to use the prototype

`design-reference/` — open `index.html` and click through the whole site.

| Try this | Where |
|---|---|
| Trade sign-in | Trade page → email + code **DG-DEMO** |
| Tier pricing, MOQ/MOV, next-tier nudges | Wholesale catalogue → enter quantities |
| Order summary drawer | Wholesale catalogue → "View order" |
| GST split switching | Proforma → destination state dropdown |
| Set discounts and prepaid pricing | Product page → quantity slider |
| Prepaid vs COD | Cart → payment toggle |
| Order-size calculator | My orders → "How many do I need?" |
| Order tracking | Track page → any ID starting **DG-** |

**Every number in the prototype is a placeholder.** Full list of what to replace in Part 8.3.

---

---

# THE SPECIFICATION

*Everything below is the complete technical specification. Parts 1–8 follow.*

---

### Full build specification for developers

**What this is:** everything needed to build the Drunken Glass website, in one document. Every page, every feature, every commercial rule, every integration, and every acceptance criterion. A developer should be able to build the entire site from this file alone.

**Companion files (optional reference):** a working static prototype of all 14 pages exists as HTML. It is a *visual and behavioural reference*, not production code — all prices and rules in it are hard-coded placeholders that must move server-side.

---

# PART 1 — THE BUSINESS

## 1.1 What the company is

**Drunken Glass** — a designer glassware brand selling in India, in ₹.

Founded by two brothers, **Amit Gupta and Rahul Gupta**. Fifteen years running their own glass furnace, producing **borosilicate** glassware exported worldwide under other companies' labels. They now sell direct, under their own name.

**Core positioning:** factory-direct. *We make it — we don't resell it. No middleman.*

**Two materials:**
- **Hand-cut lead-free crystal** — the designer line. Aspirational, consumer-facing.
- **Borosilicate** — the workhorse. Heat-resistant, dishwasher-proof, durable. Everyday + trade.

**Seven product categories:** Wine & Champagne · Cocktail · Whisky · Coffee & Tea · Tumblers · Decanters · Candle jars & stands.

**Scale:** 100+ designs. Products ship in **mixed colours**. **Themes** run across categories — one design theme appears as a wine glass, whisky glass, tumbler, decanter and candle.

## 1.2 Three audiences, three journeys

| | Consumer (D2C) | Wholesale (B2B) | Corporate gifting |
|---|---|---|---|
| Who | Individuals | Restaurants, cafés, bars, hotels, resellers | Companies buying gifts |
| Prices | Public | **Hidden until verified login** | Quoted |
| Action | Add to cart → checkout | Build order → proforma → pay | Request a quote |
| Payment | COD or prepaid | **100% prepaid only** | **100% prepaid only** |
| Friction | Near zero | Application + GSTIN verification | Quote conversation |

**Design principle:** one brand, three front doors. Shared story, shared visual system, different pricing, friction and calls-to-action.

---

# PART 2 — DESIGN SYSTEM

## 2.1 Brand kit (from sister brand "Comet")

**Colours**
| Token | Hex | Use |
|---|---|---|
| Blue (primary) | `#2765fa` | Links, prices, CTAs, accents, icons |
| Berry | `#ef426f` | Savings/discount badges, errors, one hero word |
| Yellow | `#eaef29` | Bestseller/preorder flags, "themed drops", warnings |
| Light Grey (ground) | `#f2f1f0` | Page background |
| White | `#ffffff` | Cards, alternating sections |
| Black (ink) | `#000000` | Type, 2px borders, dark sections |

**Colour discipline:** blue does the work. Berry and yellow appear sparingly — roughly once or twice per page. Do not scatter all three.

**Typography**
- Headings: **Space Grotesk** (400/500/700). Uppercase, tight letter-spacing (−0.01 to −0.02em).
- Body: **Montserrat** (400/500/600/700).
- Both free on Google Fonts.

**Signature motifs**
1. **The fill line** — a dashed line drawn across each glass illustration marking the correct pour level. Used as both product spec and brand device.
2. **The shooting star** — a small blue dot with two trailing dots after the wordmark.

**Component conventions**
- 2px solid black borders on cards, buttons, inputs.
- 2–4px border radius (nearly square).
- Hover on cards: `translateY(-3px)` + `6px 6px 0` black hard shadow.
- Buttons: black fill → blue on hover; ghost variant is transparent with black text.
- Focus states: `outline: 3px solid var(--blue)`.
- Section rhythm: alternate grey/white backgrounds, separated by 2px black rules.

## 2.2 Responsive

- Breakpoints used: 1000px, 900px, 820px, 760px, 680px, 620px, 560px, 520px, 460px.
- **Mobile nav appears below 820px** — hamburger toggling a full menu list.
- ~70% of Indian traffic is mobile. Mobile is the primary case, not the fallback.
- Respect `prefers-reduced-motion`.

---

# PART 3 — GLOBAL ELEMENTS

Present on every page.

## 3.1 Announcement bar (top of page)
Black bar, blue ✦ separators, yellow highlights.
- **Consumer pages:** "Free shipping on **all orders**" · "Pay online — skip COD charges & take **5% extra off**"
- **Trade pages:** "100% prepaid orders only — **no COD**" · "delivered across India"
- **Gifting:** "Corporate gifting · logo engraving & custom packaging" · "Bulk quotes · 100% prepaid · delivered across India"

## 3.2 Navigation
Sticky, blurred background, 2px black bottom border.
- Logo (links home) with shooting-star mark.
- **Consumer nav:** Shop · Gifting · About · **Trade Login** (blue button)
- **Trade (signed in) nav:** Catalogue · My orders · Policies · FAQ · "Signed in · Trade" · Sign out
- **Mobile (<820px):** hamburger → Home · Shop · Corporate Gifting · Trade/Wholesale · Our Story · Cart · Track Order · Contact · Policies

**Requirement:** every page must be reachable from every page on mobile. No page may be a dead end.

## 3.3 Footer
Dark, multi-column:
1. Wordmark + "Made at our furnace ✦ sold direct" + "Amit & Rahul Gupta"
2. Shop · Corporate gifting · Wholesale/trade · Our story
3. Contact us · Track your order · Shipping policy · Returns & replacement
4. Privacy policy · Terms & conditions · Your bag

## 3.4 Trust badge band
Six badges with line icons: Free shipping · **Prepaid · 5% extra off** (highlighted blue) · Breakage replaced free · Lead-free crystal · Factory-direct · Secure checkout.

**Rule:** this band is the single home for trust messaging. Do not repeat these claims in separate blocks elsewhere on the same page.

## 3.5 Brand story band
Reusable dark section, identical wording site-wide:

> **The world drank from our glass. It never knew our name.**
>
> For fifteen years, two brothers — **Amit and Rahul Gupta** — have shaped glass at one furnace and shipped it to tables the world over. Every cut was ours. The label was always someone else's.
>
> *Amit & Rahul Gupta ✦ finally poured at home*

## 3.6 SEO / meta (required on every page)
`<meta name="description">`, `og:type`, `og:site_name`, `og:title`, `og:description`, `twitter:card`, `theme-color=#2765fa`. Add per-page OG images. WhatsApp sharing is a primary channel in India — link previews must render.

Also required: favicon, `sitemap.xml`, `robots.txt`, analytics, and Product structured data (schema.org) on product pages.

---

# PART 4 — COMMERCIAL RULES ENGINE

**These are the authoritative numbers. All must be enforced server-side.**

## 4.1 Consumer pricing

**Set-size volume discount** (applies to quantity of a single design):

| Quantity | Discount |
|---|---|
| 1 | 0% |
| 2–3 | 5% |
| 4–5 | 10% |
| 6–7 | 15% |
| 8–11 | 20% |
| 12 | 25% |

**Mix & match:** on the "build your own set" tool, the discount applies to the **total count across designs**, not per design.

**Prepaid discount:** **5% off the order subtotal** when paying online. Not applied to COD orders. Applied at order level after item pricing.

**Shipping:** **free on all consumer orders**, no minimum. Pan-India.

**Payment:** COD **or** prepaid. Business objective is to shift volume to prepaid — hence the 5% incentive, prominently displayed at every stage (announcement bar, product page, cart, badges).

## 4.2 Wholesale pricing

**Quantity tiers, discount off MRP, applied PER DESIGN:**

| Quantity of one design | Discount off MRP |
|---|---|
| 50–99 | **55%** |
| 100–199 | **60%** |
| 200–499 | **65%** |
| 500+ | **70%** |

**Hard constraints:**
- **MOQ: 50 pieces per design.** Any line below 50 is invalid and blocks checkout.
- **MOV: ₹10,000 minimum order value.** May be reached by mixing designs and categories.
- **Payment: 100% prepaid only.** No COD. No part-advance. Order enters production only when payment clears.
- **Delivery: pan-India**, all states. Freight on large consignments quoted separately.
- **Access:** approved trade account with verified, active GSTIN. Prices are never shown to unapproved users.

**Preorder:** out-of-stock designs may be ordered, paid in full upfront, delivered in **15–20 working days**.

**Custom quote:** for very large volumes or bespoke designs, bypass tiers → personalised quotation.

## 4.3 Corporate gifting
- Minimum **50 pieces**.
- Options: logo engraving, custom packaging, gift notes, curated sets.
- **100% prepaid**, no COD.
- Lead time **15–20 working days after sample approval**.
- Delivery to single or multiple addresses, pan-India.
- Quote-based — no checkout.

## 4.4 Returns & replacement
- **Free replacement** for items that arrive broken, cracked, chipped, defective, or wrong.
- **Requires an unboxing video** — one continuous recording from sealed parcel to glass in hand.
- **Claim window: 48 hours** from delivery.
- **Replacement only. No refunds.** No returns on correctly delivered, intact goods (no change-of-mind returns).
- Nothing in this policy limits statutory rights under the Consumer Protection Act, 2019.
- Hand-cut variation in colour, cut, weight and size is expected and is not a defect.

## 4.5 Tax
- **GST 18% on all products. HSN 7013.** Nationwide.
- **Rate never changes; only the split does**, determined by comparing the buyer's GSTIN state code with the seller's:
  - **Same state** → CGST 9% + SGST 9%
  - **Different state** → **IGST 18%**
- Computed **server-side from the stored GSTIN**, never from user input.
- Record **place of supply** on every document.
- **Proforma invoice ≠ tax invoice.** A sequential, GST-compliant tax invoice is issued on dispatch, with its own numbering series.

## 4.6 Lead times
| | Time |
|---|---|
| Consumer dispatch | 2–3 working days |
| Consumer delivery | +3–7 working days (confirm) |
| Preorder / made-to-order | 15–20 working days |
| Branded gifting | 15–20 working days after sample approval |

---

# PART 5 — PAGE-BY-PAGE SPECIFICATION

14 pages.

## 5.1 Homepage

**Purpose:** establish the brand, route the three audiences.

**Sections in order:**
1. **Announcement bar** + scrolling ticker ("Made at our furnace ✦ Sold direct ✦ 15 years of borosilicate ✦ Never watered down ✦ Home & trade")
2. **Hero** — "We make the glass. You skip the **middleman**." (berry on "middleman"). Subcopy covers 15 years of borosilicate, the crystal line, factory-direct, home *and* trade. Two CTAs: *Shop the collection* → shop page; *Open a trade account* → trade page.
3. **Trust strip** (blue band, 4 cells): 15 YRS at our own furnace · 100+ designs hand-cut · 7 categories one factory · 2 brothers, Amit & Rahul. *(Each stat must be distinct — do not repeat "factory-direct" here, it's covered elsewhere.)*
4. **The furnace** (black section) — "We don't buy glass. We make it." Three paragraphs on borosilicate mastery, the crystal line, and what direct means to a home vs a restaurant. Side panel: 3.3×10⁻⁶/K expansion · lead-free by nature · furnace → you, no reseller markup.
5. **Categories** — 7 tiles + a yellow "Themed Drops" tile. **Every tile must link** to the shop page (ideally to that category).
6. **Materials** — two cards: "The crystal you show off" / "The borosilicate you rely on", each stating who it's for and how it's bought.
7. **Trust badges band**
8. **Trade** — "Wholesale sits behind the login." Apply CTA + a compact gated sign-in panel.
9. **Brand story band**
10. **Footer**

**Acceptance:** every category tile navigates. Hero CTAs navigate. No dead links. Mobile menu reaches all pages.

## 5.2 Shop / category listing

**Purpose:** browse by category, reach product pages.

**Features:**
- Sticky **category pills** (7 categories). Selecting one updates the page title, blurb, and grid.
- **Sort:** Featured · Price low→high · Price high→low.
- Live **design count**.
- **Product cards:** glass illustration with fill line · colour dots (mixed-colour range) · name · category + material · retail price · **"Pay online ₹X" (5% less)** · Bestseller/New tags · Add to bag.
- Card body links to the product page; Add to bag increments the bag counter without navigating.
- Trust badges + brand story + footer.

**To add for production:** search box, price filter, pagination or infinite scroll (100+ designs), material filter (crystal/borosilicate), in-stock filter.

## 5.3 Product page (PDP)

**Purpose:** convert. The most important page on the site.

**Layout:** sticky gallery left, buy panel right (stacks on mobile).

**Gallery**
- Product image. *(Currently SVG illustration — replace with real photography. This is the single biggest content gap.)*
- Fill-line animation: liquid rises to the marked line on load.
- Thumbnails: empty / filled-to-the-line.

**Buy panel, in order**
1. Category kicker · product title · **star rating + review count** (links to reviews)
2. Short description
3. **Design picker** — 5 swatches + "100+ / All cuts" tile linking to the full wall. Selecting a design updates the title, breadcrumb, price, illustration and theme section live.
4. **Colour picker** — 5 colour dots + note: "Sets arrive in a mix of colours and designs."
5. **Price** — per glass, with a berry **savings badge** when a discount applies.
6. **Set box** — quantity slider 1–12, live label ("Set of 6"), live total, tier legend, and a **live prepaid price** ("Pay online ₹X — 5% off, no COD fee").
7. **Two buttons:** Add to bag (ghost) · Buy now (solid). Both route to the cart.
8. **Reassurance block** (2 lines only): dispatch time + free shipping; breakage replaced free with link.
9. **Trade one-liner:** "Buying for a business? Verified trade accounts get wholesale from 55% off → See wholesale". *(Must be a link, not an embedded login form.)*

**Sections below**
1. Trust badges band
2. **The details** — spec strip (350ml capacity · 150ml fill line · 22cm height · stemware, lead-free crystal), use-chips ("more than wine": reds & whites, water & juice, iced tea, spritzers, mocktails), and two short notes: *Made by us* and *Care* (with a link to the stemless Tumbler range).
3. **More ways to cut it** — tabbed: **All cuts** (grid of every design; selecting loads it into the buyer) / **Build a set** (steppers per design; **volume discount applies to total count across designs**; running total).
4. **Shop the theme** — the selected design rendered across all other categories (whisky, tumbler, coffee, decanter, candle) + "Complete the theme · save 15%" bundle bar. Reprices live when the design changes.
5. **Reviews** — rating summary + review cards.
6. **FAQ** — 4 questions only, each adding information not already on the page: what if it arrives broken · delivery time · mixing designs and colours · dishwasher safety.
7. Brand story band · footer.

**Sticky mobile buy bar:** appears once the buy button scrolls out of view; shows design name, set size, live total, and Add. Hidden on desktop.

**Accessibility:** design swatches, colour dots and thumbnails must be real `<button>`s with `aria-pressed` and labels.

**Rules:**
- Do not repeat a trust claim more than twice on the page.
- Product information must appear **before** upsell sections.

## 5.4 Cart

**Purpose:** review, adjust, and hand off to checkout.

**Features:**
- Line items: thumbnail, name, category, unit price after set discount, **discount label**, stepper, line total, remove.
- Empty state with a CTA to the shop.
- **Order summary (sticky):** subtotal at MRP · set discount · **Shipping: Free** · prepaid discount (5%) or COD handling · **Total**.
- **Payment toggle:** *Pay online* / *Cash on delivery*. Switching recalculates instantly — the 5% saving visibly disappears on COD. This is the primary prepaid conversion device.
- **Next-tier nudge:** "Add 2 more glasses for 15% off the set."
- **Checkout button → GoKwik** (see 7.1).
- Assurances: free shipping · dispatch 2–3 working days · broken on arrival replaced free.
- Cross-sell row ("Completes the table") with Add to bag.

## 5.5 Track order

- Inputs: **Order ID** (must start `DG-`) + email or phone. Validated.
- Result: order ID, status pill, and a 5-step timeline — Order confirmed → Packed at our furnace → In transit (with courier AWB) → Out for delivery → Delivered. Steps marked done / current / pending.
- Expected delivery date range, courier tracking ID.
- Help box: "Something arrived broken?" → link to replacement policy; "Need help with this order" → contact.

**Production:** queries the order system + courier tracking API (e.g. Shiprocket).

## 5.6 Trade / wholesale login

**Purpose:** application, verification, and entry to the gated catalogue.

**Sections:**
1. Announcement: 100% prepaid, no COD, delivered across India.
2. Hero: "Wholesale sits behind the **login**."
3. **Two panels:**
   - **Application form** — Legal business name*, **GSTIN*** (live 15-character format validation), Business type* (Restaurant / Café / Coffee shop / Bar / Hotel / Cloud kitchen / Retail chain / Distributor / Corporate), Monthly volume, Address*, City*, PIN*, Contact person*, Phone*, Work email*, Website/Instagram. → Submits to a pending state with a reference number `DG-TRADE-######`.
   - **Sign in** — work email + access code → **redirects to the wholesale catalogue**.
4. **Payment terms** — "100% prepaid. No COD." card + "Pan-India" delivery card + a line stating part-advance and COD are not available.
5. Trust badges.
6. **Wholesale & corporate gifting policies** — 6 cards: Ordering (GSTIN, MOQ, MOV) · Pricing (tiers) · Payment (100% prepaid) · Delivery & preorder (pan-India, 15–20 days) · Corporate gifting (engraving, packaging) · Breakage & returns.
7. **FAQ** — 6 questions that add *new* information beyond the policy cards: approval time and GSTIN failure handling · mixing designs to hit minimums · whether tiers are per-design or per-order · reordering and price stability · pan-India freight · samples before a large run.
8. Brand story · footer.

**GSTIN format regex:** `^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}Z[0-9A-Z]{1}$`

## 5.7 Wholesale catalogue (gated)

**Purpose:** the B2B ordering surface. Only reachable by approved, signed-in trade accounts.

**Header:** four tier cards (50+ 55% · 100+ 60% · 200+ 65% · 500+ 70%) and rule chips: Min 50 pcs/design · Min order ₹10,000 · Available in mixed colours as shown · 100% prepaid, no COD · Delivered across India.

**Toolbar:**
- **Search** across *all* categories (essential at 100+ designs).
- **Sort:** Featured · Unit price low→high · high→low · In stock first.
- Live result count with scope.

**Category pills** for the 7 categories.

**Product cards:** stock badge (In stock / **Preorder** in yellow) · glass illustration · colour dots · name · MRP · **all four tier unit prices** · quantity input · line total · **next-tier nudge** ("Add 40 more for 60% off" → at 500+, "★ Best tier — 70% off applied") · preorder note (advance booking, 15–20 working days).

**Validation:** quantity below 50 turns the field red with "min 50" and blocks the order.

**Sticky order bar:** total pieces · total value · status message · **View order** · **Proforma** · **Request order**. Buttons enable only when MOQ and MOV are both satisfied; otherwise the message states exactly what's missing ("Add ₹3,240 more to reach the ₹10,000 minimum order").

**Order summary drawer:** every line across every category, with per-line quantity adjust and remove, running totals, MOV gap message, clear-all, Proforma, and Request order.

**Custom quote block:** "Ordering really big?" → personalised quotation.

**Quantities persist** across category switches.

## 5.8 Proforma invoice

**Purpose:** unblocks the prepaid model. An Indian business cannot release funds without a proforma carrying both GSTINs.

**Contents:**
- Seller block: legal entity, address, GSTIN, state code, contact.
- Document block: "Proforma Invoice", number (`DG-PI-######`), date, valid-until, status pill.
- **Bill to** and **Ship to** blocks with buyer GSTIN and **place of supply** + state code.
- **Line table:** Design · **HSN 7013** · Qty · MRP · Trade rate (with tier % badge) · Taxable value.
- **Totals:** Gross at MRP → Trade discount → Taxable value → **GST split** → Freight → **Total payable**.
  - **GST split is automatic:** same state → CGST 9% + SGST 9%; other state → **IGST 18%**.
- **Amount in words**, Indian numbering (lakh/crore).
- **Bank details** + UPI ID.
- **Terms:** 100% prepaid · proforma is not a tax invoice · production starts on payment · lead times · MOQ/MOV · mixed colours · breakage replacement · GST 18% HSN 7013 · trade pricing confidential.
- **Print stylesheet** — hides nav, pay button and notices; prints clean to PDF.
- **"Pay ₹X now"** action → payment link.

## 5.9 Trade account dashboard ("My orders")

Three tabs.

**A. Order history**
- Cards per order: order ID, date, **status pill** (Delivered / In transit / In production / **Awaiting payment**), line items, total incl. GST.
- Actions: **Reorder** (one tap — rebuilds the cart at today's prices and stock, routes to catalogue) · **Invoice** (or **Pay now** for awaiting-payment orders) · **Set schedule**.

**B. Replenishment** *(the repeat-revenue engine — restaurants break glasses continuously)*
- Active schedules: name, interval, next date, items, and **Pause / Resume · Skip next · Edit**.
- Create new: base it on a past order · repeat every 30/60/90/120 days · quantity (same / 50% / manual).
- Messaging: we prepare the order and send a proforma; nothing ships until paid; adjust, skip or pause any time; **schedules preserve your quantity tier**.

**C. "How many do I need?" calculator**
- Inputs: covers (seats) · table turns/day · glasses of this type per cover · wash-cycle buffer (2× / 2.5× / 3×) · monthly breakage rate (5% / 10% / 15%).
- Formula: `daily = covers × turns × perCover` → `inService = ceil(daily × washBuffer)` → `quarterBreakage = ceil(inService × breakRate × 3)` → **total = inService + quarterBreakage**.
- Output: headline number, breakdown, and **which discount tier it lands in** plus how many more for the next tier.
- Framed as planning guidance, not a guarantee.

## 5.10 Corporate gifting

1. Hero: "Gift something they'll actually **keep**."
2. **Why glass** — 4 cards: actually kept · your brand cut in · factory-direct value · delivered at scale.
3. **Occasions** — client gifting · employee/onboarding · **Diwali & festive** (yellow) · conferences · milestones · wedding/hospitality.
4. **Personalisation** — logo engraving · custom packaging · gift notes & sets.
5. **How it works** — 4 steps: share your brief → we quote & sample → brand & produce → we deliver.
6. **Gifting policies** — 6 cards: minimums (50) · payment (**100% prepaid**) · lead time (15–20 working days after sample approval) · delivery (pan-India, single or multiple addresses) · breakage (replaced free) · custom designs.
7. **Quote form:** Company*, Contact*, Work email*, Phone*, Approx. quantity* (50–100 / 100–250 / 250–500 / 500–1000 / 1000+), Occasion, **Branding checkboxes** (logo engraving / custom packaging / gift note), Deadline, Delivery (single/multiple), Free-text brief. → Confirmation with reference `DG-GIFT-######`.
8. **FAQ** — 5 additive questions: sample process · artwork formats for engraving · different glasses for different recipients · realistic festive deadlines · GST invoicing.
9. Footer.

**No cart. The deliverable is a conversation.**

## 5.11 About / our story

Editorial page, the emotional centre.

1. Hero: "We made the glass the world raised — and no one knew our **name**."
2. **Chapter one: It began with heat** — learning borosilicate, exporting worldwide, every piece wearing someone else's name.
3. **Pull quote** (full-bleed black): *"For fifteen years, our best work wore a stranger's label."* — Amit & Rahul Gupta
4. **Chapter two: Why we finally signed our name** — the decision, the fill line, selling direct at home.
5. **"15"** — full-bleed yellow moment: "15 — Years at the furnace, and only getting started."
6. **Four promises:** Made by us · Sold direct · Replaced if it breaks · Fair by design.
7. **Signature block** — Amit & Rahul Gupta, brothers, makers, founders + a note on the brand name (glasses that get *raised*).
8. CTA: Shop the collection / For the trade.

**To personalise:** hometown, furnace location, the actual founding year, one true anecdote, real number of export countries.

## 5.12 Contact

- **Reach us:** phone/WhatsApp with hours · customer support email · **trade email** · **gifting email** · registered address · GSTIN.
- **Quick routes:** wholesale enquiry → trade · corporate gifting → gifting · where's my order → track.
- **Form:** name*, phone, email*, subject* (order / damaged item / product question / wholesale / gifting / other), order ID, message* → confirmation with reference `DG-MSG-######`.

**Critical:** payment providers verify these details during onboarding. They must be real.

## 5.13 Policies

Four sections with sticky sub-navigation and deep anchors — `#shipping`, `#returns`, `#privacy`, `#terms`. Provide these as distinct URLs if a payment provider requires it.

- **Shipping** — free on all orders; dispatch and delivery times; preorder and gifting lead times; tracking; packaging; payment methods; pan-India; undelivered/refused parcel handling.
- **Returns & replacement** — what's covered; the 3-step claim (film unboxing → contact within 48h → we ship a replacement); replacement-only resolution; what isn't covered; statutory rights; refunds where applicable; cancellation.
- **Privacy** — who we are; what we collect (order, payment, business/GSTIN, usage); why; who we share with; retention; **DPDP Act 2023 rights**; cookies; **grievance officer**.
- **Terms** — eligibility and jurisdiction; hand-cut variation; pricing and GST; order acceptance; wholesale terms; gifting/custom terms and artwork indemnity; IP; liability; changes.

**Requires legal review** against the Consumer Protection (E-Commerce) Rules, 2020 and the DPDP Act, 2023.

## 5.14 404

On-brand: "This one slipped." Broken-glass illustration. CTAs to shop and home, plus links to track / wholesale / gifting / contact.

---

# PART 6 — BACKEND

**The governing rule: the browser is never trusted.** Every price, discount, minimum, stock check, tax split and access decision is computed and enforced on the server. If a rule lives only in the front end, it does not exist.

## 6.1 Recommended stack
- **Frontend:** Next.js/React (or the existing static pages progressively wired to the API).
- **Database:** PostgreSQL (Supabase gives DB + auth + storage together).
- **Auth:** passwordless magic-link email.
- **Payments:** Razorpay (licensed aggregator) + **GoKwik** as the consumer checkout layer.
- **GST verification:** third-party GSTIN API.
- **Email:** Resend / Postmark / SES.
- **Shipping:** Shiprocket or equivalent.

**Alternative:** Shopify + B2B apps (see 8.2).

## 6.2 Data model

**categories** — id, key, label, blurb, sort_order

**products** — id, category_id, theme_id, name, material (`crystal`|`borosilicate`|`glass`), mrp, retail_price, capacity_ml, fill_ml, stemware (bool), in_stock, stock_qty, is_active, tags[], images[], hsn (default `7013`)

**themes** — id, name *(links one design across categories)*

**colours** + **product_colours** — id, name, hex

**users** — id, email, role (`consumer`|`trade`|`admin`), trade_account_id

**trade_accounts** — id, legal_name, gstin, **gstin_verified (jsonb — full API response, audit trail)**, business_type, address, city, pincode, state_code, contact_name, phone, email, website, est_monthly_volume, status (`pending`|`approved`|`rejected`), pricing_tier, reviewed_by, reviewed_at, created_at

**orders** — id, user_id, channel (`consumer`|`trade`), status (`pending`|`confirmed`|`in_production`|`shipped`|`delivered`|`cancelled`), subtotal, discount_total, taxable_value, cgst, sgst, igst, place_of_supply, shipping, grand_total, payment_method (`prepaid`|`cod`), payment_status, prepaid_discount_applied, has_preorder_items, addresses (jsonb), created_at

**order_items** — id, order_id, product_id, qty, unit_price, tier_applied, is_preorder, hsn, taxable_value

**replenishment_schedules** — id, trade_account_id, name, source_order_id, interval_days, next_run_date, quantity_mode, status (`active`|`paused`), items (jsonb)

**proformas** — id, order_id, number (sequential series), issued_at, valid_until, status, pdf_url

**trade_applications** · **gifting_requests** (company, contact, email, phone, quantity_band, occasion, branding[], deadline, delivery, brief, ref, status) · **contact_messages**

**config** — every tunable value (see 6.6)

## 6.3 Pricing engine (single source of truth)

```
function priceFor({ product, qty, customerType }) {
  if (customerType === 'trade') {
    const d = qty >= 500 ? 0.70
            : qty >= 200 ? 0.65
            : qty >= 100 ? 0.60
            : qty >= 50  ? 0.55
            : null;
    if (d === null) throw MOQError(product, 50);   // MOQ 50/design
    return round(product.mrp * (1 - d));
  }
  // consumer
  const d = qty >= 12 ? 0.25 : qty >= 8 ? 0.20
          : qty >= 6 ? 0.15 : qty >= 4 ? 0.10
          : qty >= 2 ? 0.05 : 0;
  return round(product.retail_price * (1 - d));
}
```

**Order-level rules:**
- Consumer prepaid → subtract 5% from subtotal. COD → no discount.
- Consumer shipping → always 0.
- Trade → reject if subtotal < ₹10,000; reject any line < 50; reject `payment_method != 'prepaid'`.
- Any out-of-stock line → `has_preorder_items = true`, expected delivery 15–20 working days, still paid in full upfront.

**Tax:**
```
taxRate = 0.18
interState = (buyer.state_code !== seller.state_code)
interState ? igst = taxable * 0.18
           : cgst = sgst = taxable * 0.09
```

## 6.4 Authentication & gating
- Roles: `consumer`, `trade`, `admin`.
- Trade role granted only when `trade_account.status = 'approved'`.
- **Wholesale prices and the catalogue endpoint must check `role === 'trade' && status === 'approved'` server-side.** The redirect after sign-in is convenience — authorization is the actual gate.
- Re-check authorization on every priced endpoint.

## 6.5 API surface

**Catalogue (public):** `GET /categories` · `GET /categories/:key/products` · `GET /products/:id` · `GET /themes/:id/products`

**Consumer:** `POST /cart/price` · `POST /orders` · `POST /orders/:id/pay` · `POST /webhooks/gokwik` · `POST /webhooks/razorpay` · `GET /orders/:id/track`

**Auth:** `POST /auth/magic-link` · `POST /auth/verify` · `GET /me`

**Trade (🔒 approved only):** `POST /trade/applications` (public) · `GET /trade/catalogue` · `POST /trade/price` (enforces MOQ/MOV) · `POST /trade/orders` (prepaid only) · `GET /trade/orders` · `POST /trade/orders/:id/reorder` · `POST /trade/proformas` · `GET /trade/proformas/:id.pdf` · `GET|POST|PATCH /trade/schedules` · `POST /trade/quote`

**Gifting (public):** `POST /gifting/requests`

**Contact (public):** `POST /contact`

**Admin (👤):** trade application queue · `POST /admin/trade-applications/:id/verify` (GSTIN API) · approve/reject · products & stock CRUD · orders · gifting requests · schedules · `PUT /admin/config`

## 6.6 Config table — every tunable value

| Key | Default |
|---|---|
| consumer_prepaid_discount | 0.05 |
| consumer_free_shipping | true |
| consumer_set_tiers | 2:0.05, 4:0.10, 6:0.15, 8:0.20, 12:0.25 |
| wholesale_tiers | 50:0.55, 100:0.60, 200:0.65, 500:0.70 |
| trade_moq_per_design | 50 |
| trade_min_order_value | 10000 |
| trade_payment_methods | [prepaid] |
| gifting_min_qty | 50 |
| gst_rate | 0.18 |
| hsn_code | 7013 |
| seller_state_code | *(set this)* |
| dispatch_days | 2–3 working days |
| preorder_lead_days | 15–20 working days |
| replacement_claim_window_hours | 48 |
| theme_bundle_discount | 0.15 |

Front end should read these from the API so there is exactly one source of truth.

## 6.7 Admin panel (minimum)
- **Trade approval queue** — application detail, one-click GSTIN verify (shows legal name, status, address from the API), approve/reject with reason + email.
- **Catalogue & stock** — products, MRP, stock, images, theme, colours.
- **Orders** — consumer and trade, payment status, preorder flags, status transitions.
- **Proformas & invoices** — issue, track payment, convert to tax invoice on dispatch.
- **Replenishment schedules** — view, edit, trigger.
- **Gifting requests & contact messages** — inbox with references.
- **Config** — edit every value in 6.6 without a deploy.

---

# PART 7 — INTEGRATIONS

## 7.1 Checkout — GoKwik
- GoKwik is a **checkout and conversion layer, not a payment aggregator**. Payments settle through a licensed aggregator (e.g. Razorpay) connected behind it. **You need both.**
- Useful for this business: one-click checkout, COD verification and RTO reduction, **COD fees and prepaid-only perks** — which directly serve the objective of shifting orders to prepaid.
- Build the GoKwik cart payload from **server-computed** prices. Never from the page.
- Consumer only. Trade orders use proforma + payment link, not GoKwik.

## 7.2 Payments — Razorpay (or licensed equivalent)
- Consumer prepaid: create the payment for the server-computed 5%-discounted total.
- Consumer COD: no gateway; mark accordingly.
- **Trade: full amount only.** Order moves to `in_production` only when payment is captured. No part-payment path.
- **Webhooks are the source of truth** for payment status, not browser redirects.
- Make order-create and payment-capture idempotent.
- Never store card data.

## 7.3 GSTIN verification
- Called at admin review of a trade application.
- Returns legal name, trade name, registration status, taxpayer type, principal address. Costs a few paise per call.
- Store the full response as an audit trail.
- Block approval if status ≠ active; flag legal-name mismatches for manual review.
- Free format pre-check client- and server-side using the regex in 5.6.

## 7.4 Shipping
- Courier integration (Shiprocket or similar) for label generation, AWB, and tracking feed into the Track Order page.
- Free shipping for consumers; freight quoted separately on large trade consignments.

## 7.5 Email
Magic-link sign-in · trade application received (applicant + admin) · trade approval/rejection · proforma issued · payment received · order confirmation and status · gifting request received · contact message received.

---

# PART 8 — DELIVERY

## 8.1 Build phases

**Phase 1 — MVP (launch):**
1. Catalogue: categories, products, stock, images.
2. Consumer browse → PDP → cart → GoKwik/Razorpay checkout with prepaid 5%, free shipping, COD.
3. Trade application → admin queue → GSTIN verify → approve → magic-link login.
4. Gated wholesale catalogue + pricing engine with MOQ/MOV + prepaid-only checkout.
5. Proforma generation with correct GST split.
6. Gifting and contact forms → email routing.
7. Policies, contact, track order, 404.
8. Config table + minimal admin.

**Phase 2:**
- Reorder + replenishment schedules.
- Trade order history and downloadable invoices.
- Preorder automation and lead-time tracking.
- Multi-address gifting fulfilment.
- Analytics on **prepaid vs COD share** (the stated business objective), tier uptake, quote conversion.

**Phase 3 (B2B depth):**
- Multiple users per company account with an approval threshold.
- Multi-outlet split shipping for chains.
- WhatsApp ordering and support.
- Annual volume rebate scheme.
- CSV bulk order upload.
- Case-pack ordering, spec sheets per design, back-in-stock alerts.
- Branded glassware for venues (etching a restaurant's own logo).
- Net terms / credit for established accounts.

## 8.2 Alternative: Shopify route
Faster for a solo founder, less flexible:
- Shopify Basic (~₹1,499/mo + 18% GST). Shopify Payments is unavailable in India → connect Razorpay; Shopify adds ~2% transaction fee on Basic on top of gateway fees.
- Theme "Dawn", restyled with the tokens in Part 2.
- Apps: a **B2B wholesale app** (registration + approval workflow, gated price lists, tiered discounts, MOQ/order limits) · **Request-a-Quote app** for gifting · **COD fee / prepaid discount app** · GoKwik app for checkout.
- GSTIN verified manually on the government portal at approval.
- **Caveat:** the exact tier/MOQ/MOV logic, the proforma, replenishment and the calculator will need app configuration or custom work.

## 8.3 Placeholders that MUST be replaced before launch

| Item | Where |
|---|---|
| All prices and MRPs | Everywhere |
| Real product photography | PDP, shop, cart, catalogue |
| Sample reviews — **never publish invented reviews** | PDP |
| Phone, emails, address, GSTIN, legal entity, state code | Contact, Policies, Proforma |
| Bank details, UPI ID, invoice number series | Proforma |
| Grievance officer name and contact | Privacy policy |
| Dispatch and delivery day ranges | Shipping policy, PDP, cart |
| "Last updated" date | Policies |
| Design names, count behind "100+", stock status | Catalogue, PDP |
| Founding year, hometown, export countries, an anecdote | About |
| Favicon, OG images, analytics ID | All pages |

## 8.4 Compliance checklist
- [ ] Policies reviewed by a lawyer (Consumer Protection E-Commerce Rules 2020; DPDP Act 2023).
- [ ] Replacement-only / no-refund wording checked against statutory rights for defective goods.
- [ ] HSN 7013 and 18% GST confirmed with a CA.
- [ ] GST split derived from the buyer's GSTIN state code, server-side.
- [ ] Sequential, GST-compliant tax invoice numbering.
- [ ] Contact and policy URLs live before payment-provider onboarding.
- [ ] Grievance officer published.
- [ ] Cookie consent if analytics/marketing cookies are used.

## 8.5 Definition of done
- No dead links on any page, on desktop or mobile.
- Mobile menu reaches every page.
- All prices, discounts, minimums and tax computed server-side and re-verified before payment.
- Wholesale prices unreachable without an approved account — verified by calling the API directly without a session.
- MOQ 50/design and MOV ₹10,000 cannot be bypassed from the client.
- Trade checkout rejects anything other than 100% prepaid.
- GST split correct for both intra-state and inter-state orders.
- Every form submission is persisted and emailed.
- Lighthouse: performance, accessibility and SEO all pass on mobile.

---

*One brand, three doors, fourteen pages. Everything above is the specification; anything not stated here is a decision for the founders — Amit and Rahul Gupta — not an assumption for the developer to make.*
