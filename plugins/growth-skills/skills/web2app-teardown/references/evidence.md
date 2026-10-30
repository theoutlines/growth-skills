# Web2app evidence: published tests, benchmarks and gaps

Collected 2026-10-30. Every number was read on the page it comes from. Cite tests as **#W1, #W2 …** and benchmarks by their row (e.g. "FunnelFox State of Web2App 2026, funnel steps"). The `W` prefix keeps this list apart from the onboarding (#1–#77), upsell (#U1–#U50) and cancel-flow (#C1–#C28) libraries; rows that already exist there keep their original number in a "Same as" note.

Scope: paid-ad landing → web quiz → web paywall → web checkout → post-purchase upsells → account → app download and login, plus the US iOS link-out ("buy on the web" inside the app) and Android external offers.

Part 1 is published tests and case studies. Part 2 is benchmarks from public reports. Never merge two rows into one number, and keep metric definitions apart (Part 2, section 0).

# Part 1. Published tests and case studies

**Tiers in the two parts.** Part 1 tiers grade a row as evidence that a *change* works; a vendor aggregate there is "directional". Part 2 tiers grade a benchmark as a *description* of what apps see; the same dataset can be a "strong benchmark". For priority, a benchmark is Medium at most.

**Rows used from other libraries** (number kept): onboarding #1 Blinkist, a day-by-day trial timeline with a reminder, +23% trial sign-ups, −55% complaints (strong, in-app), https://uxplanet.org/how-solving-our-biggest-customer-complaint-at-blinkist-led-to-a-23-increase-in-conversion-b60ad514134b

## Tiers

- **Strong**: controlled A/B, holdback or randomized experiment, with numbers on the page.
- **Directional**: numbers, but no stated method, a before/after or year-over-year comparison, bundled changes, a matched observational comparison, or a vendor aggregate.
- **Anecdotal**: no numbers, or a claim without a source.
- **Observed**: what apps do (screen counts, field counts), no outcome.

## Conventions

- Lifts are **relative** unless marked **pp** or given as two absolute rates (a% → b%).
- The denominator is named when the page names it (per ad click, per session, per landing visitor, per paywall view, per CTA tap, per checkout session, per install, per customer in arm, per failed payment). "Denominator not stated" means the page doesn't say.
- Bucket = RevenueCat SOSA bucket (Health & Fitness, Education, Productivity, Utilities, Photo & Video, Media & Entertainment, Social & Lifestyle, Business). "AI" is a tag. Games, e-commerce, SaaS and cross-business datasets are **n/a**. "(inferred)" = from the app's description, not a checked store listing.
- Surface: **web** (pre-install web funnel or web checkout), **iOS link-out** (button in the iOS app that opens web checkout), **Android**, **in-app** (store billing, for comparison).
- Bundled changes are flagged. Two tests are never merged into one number. Where one experiment is reported twice, both reports get their own row and a note.
- Vendor caveat: FunnelFox, Paddle, Stripe, Solidgate, Superwall, Adapty, RevenueCat, Shopify and SamCart sell the thing they report on. RevenueCat's own test (#W39) is the only one where the vendor's result cut against the product it sells.

---

## A. Landing and ad-to-funnel match

| ID | App/company | Category | Bucket | AI tag | Surface | Change | Metric | Result | Date | URL | Tier |
|---|---|---|---|---|---|---|---|---|---|---|---|
| W1 | Campaign Monitor (agency ConversionLab) | Email marketing SaaS | Business | no | web | Landing-page headline and CTA verb swapped to match the verb in the visitor's Google search (dynamic text replacement); default "Create" | Trial sign-ups on the next page, per landing visitor | +31.4%, "100% statistical significance"; 1,274 visitors in total, 100+ conversions per variant | Ran 2017-10-31 → 2018-01-16; pub. 2018-04-03 | https://unbounce.com/?p=70889 | Strong (A/B) |
| W2 | Seamwork (Conversion Rate Experts) | Sewing patterns and classes, membership | n/a (web membership) | no | web | Homepage hero replaced: benefits + social proof → a 5-question personal quiz as the first thing new visitors see | Memberships; revenue per visitor | Memberships +34%; revenue per visitor (memberships + pattern sales) +56%. Sample not disclosed | Pub. 2025-02-04 | https://conversion-rate-experts.com/seamwork-quiz-win-report/ | Strong (A/B), sample not given |
| W3 | Google, 55 and Deloitte, "Milliseconds make millions" | 37 retail, travel, luxury and lead-gen brand sites | n/a | no | mobile web | 0.1 s faster mobile load (four speed metrics), 30M+ sessions over 30 days, end of 2019 | Funnel progression and conversion, per session | Retail conversion +8.4%, spend +9.2%; travel conversion +10.1%; lead-gen form step 1 → submission +21.6% | Last updated 2020-06-24 | https://web.dev/case-studies/milliseconds-make-millions | Directional (observational, commissioned by Google) |
| W4 | FunnelFox, State of Web2App 2026 (platform data) | Cross-category web2app funnels | All | mixed | web vs store | Web funnel vs app-store funnel from the same ad click (not a test). Web funnel steps per session | Purchase per ad click; step reach per session | Web 3% vs app-store 1.5% of ad clicks ("2×"); store funnel: install 30.0% of clicks. Web steps: second screen 47.5% → paywall 13% → purchase 3% of sessions. Sample size, means vs medians not stated | Pub. 2026-01 (data 2025) | https://funnelfox.com/state-of-web2app-2026 | Directional (vendor aggregate) |
| W5 | AIR Music (ExploreApps) | AI song generator | Media & Entertainment (inferred) | yes | web vs store | Web2app funnel (8-screen quiz) vs direct App Store campaigns for the same app | Cost per subscription | 1.5× lower on web (page URL says "by half"; body says 1.5×). No absolute CPS, spend or sample | Not dated (© 2026) | https://funnelfox.com/case-studies/exploreapps-cuts-cps-by-half-with-funnelfox/ | Directional ("side-by-side A/B tests", vendor, no figures behind them) |
| W6 | Unnamed content subscription web app (FunnelFox) | Personalised content | Not stated | unknown | web | Funnels built around whichever ad creative gained traction | Conversion to purchase; second screen → checkout click-through | Top funnel "roughly 5%" / "up to 5%"; average across funnels ~2.5%; second screen → checkout "as high as 75%"; acquisition cost 30% lower than earlier flows. Denominators not stated | Not dated (© 2026) | https://funnelfox.com/case-studies/web-funnels-for-content-web-app/ | Directional |
| W7 | Houzz | Home design | Social & Lifestyle | no | web | **Same as onboarding #39.** Dedicated landing page for paid traffic (3D floor plans only) | Trial starts | +5% | Not dated | https://abtest.design/tests/customized-landing-page-for-paid-traffic | Directional |
| W8 | YNAB | Budgeting | Utilities | no | web | **Same as onboarding #38.** Product-tour page with large screenshots, captions, testimonial | Free-trial downloads | +85%, 97% confidence | About 2019 | https://wingify.com/success-stories/ynab/ | Strong (split URL) |

## B. Quiz length and question design

| ID | App/company | Category | Bucket | AI tag | Surface | Change | Metric | Result | Date | URL | Tier |
|---|---|---|---|---|---|---|---|---|---|---|---|
| W9 | Lasting (Talkspace) | Couples therapy / relationship health | Health & Fitness (inferred) | no | web | Animation timing in the web sign-up quiz shortened (less waiting between questions) | Conversions across landing-page conversion and sign-up completion | "60% increase in conversions". No sample, no date, denominator not stated | Not dated | https://taplytics.com/blog/how-talkspace-increased-conversions-by-60-with-web-a-b-testing | Strong (A/B per vendor), thin details |
| W10 | Villar, Callegaro & Yang, meta-analysis | Web surveys | n/a | no | web | Progress indicators: constant vs fast-to-slow vs slow-to-fast | Drop-off (breakoff) rate | 32 randomized experiments. Constant indicator: no significant reduction in drop-off. Fast-to-slow: fewer drop-offs. Slow-to-fast: more drop-offs. No effect sizes in the abstract | Social Science Computer Review 31, 2013 | https://research.google/pubs/where-am-i-a-meta-analysis-of-experiments-on-the-effects-of-progress-indicators-for-web-surveys/ | Strong (meta-analysis of randomized experiments), direction only |
| W11 | Rino (FunnelFox) | Men's health | Health & Fitness | no | web | 4 funnel variants compared; the 51-step one won and was scaled. One clarifying quiz question added, then creatives and content tailored to the segment it found | Share of user base in the new segment | Segment 35% → 80% of users. No conversion figure for the 51-step win | Not dated (© 2026) | https://funnelfox.com/case-studies/doubled-checkout-cr-with-funnelfox/ | Directional (before/after; win is anecdotal) |
| W12 | GEM SLEEP | Sleep-apnea diagnostics | Health & Fitness | no | web | **Same as onboarding #37.** Screening quiz reordered ("None of the below" first) + results screen reframed with next step and price comparison | Conversion to test sign-up | 35% → 52% (+50% relative) | Not dated | https://irrationallabs.com/case-studies/gem-sleep-increasing-diagnostic-test-conversion/ | Directional |
| W13 | Noom (teardown by Daphne Tideman, RevenueCat blog) | Weight loss | Health & Fitness | no | web | Web-to-app onboarding walked manually, ~20 paths | Funnel length | Up to 113 screens; 10–15 min to complete; a 10-question behavioural quiz; email asked about one-third through, before the results graph | Pub. 2026-04-09 | https://www.revenuecat.com/blog/growth/web-to-app-onboarding-funnel | Observed |

## C. Web paywall, plan and price

| ID | App/company | Category | Bucket | AI tag | Surface | Change | Metric | Result | Date | URL | Tier |
|---|---|---|---|---|---|---|---|---|---|---|---|
| W14 | Reading.com (FunnelFox) | Kids' phonics | Education | no | web | Funnel rebuilt: screens reordered, paywall reworked to make the monthly plan more visible, Apple Pay made the primary payment option (was a Stripe-hosted checkout) | Conversion; revenue; ARPPU | First test on one ad set: conversion +50%, blended revenue +40% despite an ARPPU drop. At scale (before/after): conversion +40%, revenue +30%. Denominator not stated | Not dated (© 2026; FunnelFox since May 2024) | https://funnelfox.com/case-studies/revenue-and-cr-uplift-after-funnel-redesign/ | Directional (A/B on one ad set, but paywall, order and checkout changed together) |
| W15 | Prehab (FunnelFox) | Physio / rehab | Health & Fitness | no | web | Black Friday: free trial replaced by direct $149 annual purchase; scratch-to-reveal discount screen; auto-applied discount, countdown, money-back guarantee; monthly de-emphasised | Conversion (denominator not stated) | Peak 4.5%, average ~3%; said to match the historical trial funnel (no baseline number) | Not dated (BFCM, © 2026) | https://funnelfox.com/case-studies/prehab-from-free-trial-to-annual-plan/ | Directional (before/after, bundled, seasonal) |
| W16 | FunnelFox, State of Web2App 2026 | Cross-category | All | mixed | web | Revenue by trial type and plan (not a test) | Share of web2app revenue | No trial 56.9%, paid trial 28.9%, free trial 14.3%. Plans: 1-month 48.8%, 1-week 30.5%, 1-year 12.2%, 3-month 8.4% | Pub. 2026-01 | https://funnelfox.com/state-of-web2app-2026 | Directional (vendor aggregate) |
| W17 | Stripe Adaptive Pricing (Stripe Sessions 2024 talk) | Cross-business | n/a | no | web | Prices shown in the buyer's local currency vs control without Adaptive Pricing | International revenue | +17.8% relative | Sessions 2024 | https://stripe.com/sessions/2024/a-look-under-stripes-hood-using-data-to-demystify-payments | Strong (holdback), sample not on page |
| W18 | Flashbook (FunnelFox) | Book summaries | Education | no | web | Quiz funnel rebuilt and A/B tested; localised funnels per market (language, price, currency, trial type); full-funnel event tracking; upsells moved to one-click after checkout | Monthly web revenue; CPA; revenue share | Web revenue +70% (July → September); CPA −30% after full-funnel tracking; localised funnels 57% of web revenue; upsells a "double-digit %" of web revenue (no figure) | Migration Apr 2026; not dated | https://funnelfox.com/case-studies/flashbook-grew-web-revenue-70-percent/ | Directional (before/after, bundled; the funnel A/B result has no number) |

## D. Checkout: payment methods, wallets, fields, trust, failures

| ID | App/company | Category | Bucket | AI tag | Surface | Change | Metric | Result | Date | URL | Tier |
|---|---|---|---|---|---|---|---|---|---|---|---|
| W19 | Stripe, "50+ global payment methods" | Cross-business (Optimized Checkout Suite) | n/a | no | web | Holdback experiment: relevant payment methods shown vs not shown | Conversion and revenue (unit not defined; reads as relative) | Any extra method beyond cards: conversion +7.4%, revenue +12%. **Apple Pay: conversion +22.3%, revenue +22.5%** (eligible checkouts). PayPal in Germany (digital books, music, film) +47%; Konbini in Japan (digital apps) +27%; Cash App in the US (digital games) +5%; SEPA Debit +12%; ACH/pre-authorised debit neutral | Pub. 2025-04-10 | https://stripe.com/blog/testing-the-conversion-impact-of-50-plus-global-payment-methods | Strong ("statistically significant holdback"; number of businesses and period not stated) |
| W20 | Stripe (Sessions 2024 talk) | Cross-business | n/a | no | web | Apple Pay offered vs not offered | Checkout conversion | +10%, statistically significant. Wallets (Apple Pay, Google Pay, Link): 3× faster median checkout (comparison, not a test) | Sessions 2024 | https://stripe.com/sessions/2024/a-look-under-stripes-hood-using-data-to-demystify-payments | Strong (A/B); a different, earlier test from #W19, do not average |
| W21 | Stripe Link | Cross-business, high returning-customer base | n/a | no | web | Link (saved payment details) shown vs not | Conversion | +14% average for businesses with many returning customers. Reported in the 2024 talk and in the 2023 newsroom post; likely the same test, kept as one row with two sources, not added twice | 2023-04-28; Sessions 2024 | https://stripe.com/newsroom/news/payments-revenue-uplift ; https://stripe.com/sessions/2024/a-look-under-stripes-hood-using-data-to-demystify-payments | Strong (A/B) |
| W22 | Stripe Payment Element migration | 10,000 businesses (5,000 migrated vs 5,000 matched) | n/a | no | web | Card-only form → Payment Element (dynamic wallets, BNPL, bank redirects) | Revenue | +10.5% average vs matched non-migrators; Stripe says it may include other changes made at the same time | Pub. 2023-04-28 | https://stripe.com/newsroom/news/payments-revenue-uplift | Directional (matched observational) |
| W23 | Rino (FunnelFox) | Men's health | Health & Fitness | no | web | Payment provider switched and checkout simplified (ZIP code and full name removed) | "Checkout conversion" (conclusion calls it "paid conversion") | 2.5× (title "doubled", body "2–2.5×"). Baseline and denominator not stated | Not dated (© 2026) | https://funnelfox.com/case-studies/doubled-checkout-cr-with-funnelfox/ | Directional (before/after; provider and fields changed together) |
| W24 | Shmoody (FunnelFox) | Mental health / habit tracker | Health & Fitness | no | web | "Payment failed" screen when a prepaid card is declined, explaining the failure and offering a retry with a supported method (e.g. debit card) | Failed transactions recovered (per failed transaction) | ~20% in the first week; base count not disclosed | Not dated (© 2026) | https://funnelfox.com/case-studies/how-shmoody-recovers-20-of-failed-payments-with-funnelfox/ | Directional (vendor, first week) |
| W25 | Unnamed wellbeing app (FunnelFox) | Wellbeing | Health & Fitness (inferred) | no | web | Second payment provider (Airwallex) as instant fallback to Stripe, region-based routing, retry schedule, checkout localised to USD/EUR/GBP and ~10 languages | Revenue recovered; recovery rate; acceptance rate | 18% of otherwise-lost revenue recovered; recovery 31% of failed renewals, 24% of failed first payments; acceptance GBP 83%, EUR 78%, USD 71% (denominators not defined); ~$200K recovered in month one | Not dated (© 2026) | https://funnelfox.com/case-studies/wellbeing-app-grew-payments-8x/ | Directional (vendor) |
| W26 | FunnelFox, State of Web2App 2026 | Cross-category | All | mixed | web | Payment mix and failures (not a test) | Share of web transactions; share of initiated payments; renewals | Apple Pay ~60%, cards 20%, PayPal 18% (~90% in Germany), Google Pay 2%. 30–50% of initiated payments fail. Renewals: 60% succeed first try, 17.5% fail then recover, 22.5% lost; retry success attempts 1–3: 19.3%, 12.5%, 9.3% | Pub. 2026-01 | https://funnelfox.com/state-of-web2app-2026 | Directional (vendor aggregate) |
| W27 | Baymard Institute | E-commerce (US shoppers; 50 abandonment studies 2006–2025) | n/a | no | web | Checkout abandonment reasons (survey; "just browsing" excluded) and usability audit (not a test) | Share of abandoners; potential conversion gain | Average cart abandonment 70.22%. Reasons: extra costs 40%, trust with card details 19%, **forced account creation 18%**, checkout too long/complicated 17%, not enough payment methods 9%. Fixing solvable checkout issues: up to +35.26% conversion for a large site (estimate) | Updated 2025-09-22 | https://baymard.com/lists/cart-abandonment-rate | Directional (survey + benchmark estimate) |
| W28 | Baymard Institute | E-commerce checkout benchmark | n/a | no | web | Form fields in top sites (not a test) | Field count | Average 11.3 fields (2024; 12.7 in 2019); "most sites need only 8"; 5.1 steps on average; 84% of sites don't delay account creation to the confirmation step | Pub. 2024-06-26 | https://baymard.com/blog/checkout-flow-average-form-fields | Observed |
| W29 | Shopify Shop Pay (study by an unnamed "Big Three" consultancy) | E-commerce | n/a | no | web | Accelerated checkout vs guest checkout | Conversion | "Up to 50%" vs guest checkout; ≥10% vs other accelerated checkouts; mere presence +5% lower-funnel conversion. No sample, no period | Updated 2023-05-18 | https://www.shopify.com/enterprise/blog/shopify-checkout | Directional (vendor-commissioned) |

## E. Post-purchase upsells and order bumps

| ID | App/company | Category | Bucket | AI tag | Surface | Change | Metric | Result | Date | URL | Tier |
|---|---|---|---|---|---|---|---|---|---|---|---|
| W30 | FunnelFox, State of Web2App 2026 | Cross-category | All | mixed | web | **Same as upsell #U34.** Funnels with post-purchase upsells vs without | LTV; upsell share; upsell price | Headline "+20% LTV", body "x2 revenue lift in median terms", chart ">200%" (incompatible). Upsells average 4.07% of total revenue; global median upsell price ≈ $9.31 | Pub. 2026-01-15 | https://funnelfox.com/state-of-web2app-2026 | Directional (self-selected) |
| W31 | English on Smartphone (FunnelFox) | Language learning | Education | no | web | Move from direct-to-store ads to a web funnel (lead form → paywall → checkout → download), later one-click upsells (songs course, phrasebooks) | Upsell share of revenue; revenue; CAC | Upsells ~10% of total revenue; refunds on upsells "low" (no figure). Whole move: revenue 2× in the first month, ad spend −50%, CAC ~−50% (was $30–40) | Not dated (© 2026) | https://funnelfox.com/case-studies/x2-revenue-half-budget-with-funnelfox/ | Directional (before/after, bundled) |
| W32 | SamCart (platform data, $7B+ processed) | Info products / e-commerce | n/a | no | web | Order bump at checkout; one-click upsell after purchase | Take rate; AOV | Order bumps "convert at 30–40% on average"; AOV +30%+; one-click upsells AOV +68%. No method, no definition of conversion | Pub. 2026-03-30 | https://www.samcart.com/blog/the-complete-guide-to-order-bumps | Directional (vendor aggregate) |

Flashbook's one-click upsells (#W18) are part of a bundle and carry no exact figure.

## F. Account creation, app download, handoff and login

| ID | App/company | Category | Bucket | AI tag | Surface | Change | Metric | Result | Date | URL | Tier |
|---|---|---|---|---|---|---|---|---|---|---|---|
| W33 | Unnamed $25B retailer ("$300 million button", Jared Spool) | E-commerce | n/a | no | web | "Register" button at checkout replaced by "Continue"; account creation offered as optional during checkout | Purchasing customers; revenue | Purchasing customers +45%; +$15M in month one, ~$300M in year one. Database: 45% of customers had 2+ accounts; ~160,000 password resets a day; ~75% of reset requesters never finished the purchase | Pub. 2009-01-14 | https://articles.centercentre.com/three_hund_million_button/ | Directional (before/after) |
| W34 | Apartment List (AppsFlyer) | Apartment search | Social & Lifestyle (inferred) | no | web → app | Web survey, then a registration overlay asking only name, email, phone (no password); a unique parameter in a deep link (SMS + welcome email) creates a one-time magic sign-in in the app and restores saved searches | Day-0 logins; web-to-app transfer; CPI; LTV | Day-0 logins 2×; transfer of highest-value web users to the app 10×; CPI −15%; LTV +30%. No baseline, window or control | Page updated 2026-04-12 | https://www.appsflyer.com/customers/apartment-list/ | Directional (vendor) |
| W35 | Todoist (Google Smart Lock hints) | Task manager | Productivity | no | Android | Email suggestions (Smart Lock hints) on the sign-up form | Sign-ups; download → sign-up | Sign-ups +80% in an A/B test; download-to-sign-up conversion about +6–7% | Not dated | https://developers.google.cn/identity/smartlock-passwords/case-studies?hl=en | Strong (A/B per Google), no sample |
| W36 | Komoot (Google Smart Lock) | Outdoor route planning | Not verified (Navigation) | no | Android | Smart Lock sign-in / sign-up | Sign-up conversion | +19%, "measured in an A/B test". Same page: Mobills login abandonment −50%; Ticketmaster manual sign-in failures 40% → 5% (method not stated) | Not dated | https://developers.google.cn/identity/smartlock-passwords/case-studies?hl=en | Strong (A/B) for Komoot; others directional |
| W37 | Flo Health (Auth0) | Period tracking | Health & Fitness | no | in-app | Registration replaced with social logins incl. Sign in with Apple | New-user sign-ups (metric not defined) | 6% → 75% ("12.5×") | Not dated (© 2026) | https://www.casestudies.com/company/auth0/case-study/flo-health-boosts-new-user-sign-ups-125x-with-auth0 | Directional (vendor summary, metric undefined) |
| W38 | FunnelFox blog, "5 hidden metrics" | Web2app | All | mixed | web → app | Purchase-to-download rate (rule of thumb) | Downloads per web buyer | "Best-in-class" 90%+; below 85% "needs fixing". No source or data; the 100 → 90 → 80 → 50 → 25 funnel on the page is illustrative | Pub. 2026-07-14 | https://blog.funnelfox.com/hidden-post-purchase-metrics/ | Anecdotal (unsourced benchmark) |

## G. US iOS link-out and external offers (in-app → web)

| ID | App/company | Category | Bucket | AI tag | Surface | Change | Metric | Result | Date | URL | Tier |
|---|---|---|---|---|---|---|---|---|---|---|---|
| W39 | Dipsea (RevenueCat-owned) | Audio fiction (App Store: Books) | Media & Entertainment (nearest fit) | no | iOS link-out, new US customers | 4 arms (RevenueCat Experiments, from 2025-05-07): A original native paywall; B clone, IAP only (control); C IAP + "subscribe on web and save 30%" ($47.99 web vs $69.99 IAP annual); D web only, same prices | Per customer in arm (initial conversion = trial or subscription start); per CTA tap; trial conversion per completed trial; revenue and proceeds per customer | ~3 weeks, ~3,100 customers per arm: initial conversion B 27.0%, C 23.5%, D 18.1%. CTA tap → initial conversion 70.9% (IAP) vs 44.4% (web); paywall view → CTA tap ~50% vs 52% at day 6. Trial conversion B 25.0%, C 28.2%, D 26.3%. Conversion to paying 6.3% / 5.9% / 5.3%. Revenue per customer $2.98 / $2.46 / $2.09; proceeds per customer at 30% Apple fee and ~6% web cost $2.09 / $1.94 / $1.96; at 15%: $2.53 / $2.17 / $1.96. Web share of C's revenue ~36% | Pub. 2025-05-14, update 2025-05-28 | https://revenuecat.com/blog/growth/iap-vs-web-purchases-conversion-test | Strong (randomized, 4 arms). Note: the update's two tables give slightly different counts for B and D; total participants (12,500) ≠ sum of three arms (9,431, arm A not reported) |
| W40 | Unnamed RevenueCat-owned app (launched May 2025; possibly a later read of #W39, not merged) | Not stated | n/a | no | iOS link-out | IAP only vs IAP + web | Conversion to paying (denominator not stated); counts | 7.8% vs 7.4% (−5.1%; text says −6%). Active subscribers 211 vs 209; set to renew 46 vs 101; churned 121 vs 104; refunded customers 28 vs 38 (+35.7%) | Pub. 2026-04-14 | https://www.revenuecat.com/blog/growth/why-you-shouldnt-use-app-to-web | Directional (method and sample not stated; text and table disagree) |
| W41 | Superwall, early app-to-web data | Cross-app (not named) | All | mixed | iOS link-out | IAP paywall (control) vs CTA opening external web checkout | Initial conversion; net proceeds | Initial conversion −11.9%; net proceeds ≈ +19.85%. Sample, period and denominators not given | Pub. 2025-05-07 | https://superwall.com/blog/initial-data-is-in-app-to-web-conversion-rates-after-the-app-store-ruling | Directional |
| W42 | Unnamed US iOS app, 30% tier (Adapty, App 1) | Not stated | n/a | unknown | iOS link-out, post-onboarding paywall | Native IAP vs web checkout | Purchase per paywall view; ARPPU; ARPU per paywall viewer | 4.95% vs 3.69% (−26%); ARPPU $23.76 vs $47.59; ARPU $1.16 vs $1.77 (+53%; elsewhere the article says 47%) | Pub. 2026-05-06, upd. 2026-09-28 | https://adapty.io/blog/app-to-web-paywalls-ios-one-year-data/ | Directional ("directional read", not a 50/50 test; no sample) |
| W43 | Unnamed language-learning app, 15% tier (Adapty, App 3) | Language learning | Education | unknown | iOS link-out | Native IAP vs web, same audience and placement | Trial conversion; purchase per view; ARPPU; ARPU | Trial conversion 5.80% vs 6.04%; purchase per view 2.54% vs 3.93% (+55%); ARPPU $65.99 vs $52.83 (−20%); ARPU $1.67 vs $1.52 (−9%). Reverted; net saving after Stripe ~10 pp, not 25 | Same | https://adapty.io/blog/app-to-web-paywalls-ios-one-year-data/ | Directional ("similar sample sizes", none given) |
| W44 | Unnamed AI companion app (Adapty, App 2) | AI companion | Social & Lifestyle (inferred) | yes | iOS link-out | Same web paywall in different placements | Conversion; ARPU | Post-onboarding 3.38%, $2.55; last-chance offer 2.90%, $4.57; mid-funnel offer 2.18%, $1.69; contextual upsell 0.87%, $0.98. A web paywall variant on the main placement: 5.54% vs 3.38% | Same | https://adapty.io/blog/app-to-web-paywalls-ios-one-year-data/ | Directional (no sample) |
| W45 | Kompanion (Stoikk, via Paddle) | Fasting / nutrition | Health & Fitness | no | iOS link-out (checkout in a browser inside the app) | Paywall: "Pay on web to save 25%" beside "Continue" (IAP). Web checkout Apple Pay only (cards disabled); email, country, ZIP only | Revenue; conversion | Revenue +25% "(est)"; conversion "0% drop", "a slight uplift". Results after "a few days" | Not dated | https://www.paddle.com/customers/stoikk-web-checkout-third-party-payments | Directional (estimate, days of data) |
| W46 | Hily (Solidgate) | Dating | Social & Lifestyle | no | iOS link-out / direct billing, US | App2web direct billing beside Apple billing; A/B on a small loyal segment first, then rolled out to 100% of US iOS | ARPU (not defined) | ~+20% on the US iOS segment, attributed to higher renewals and lower fees (not split). A/B results not reported | Not dated (© 2026) | https://solidgate.com/case-studies/hily-direct-ios-billing/ | Directional |
| W47 | Fortnite (Epic Games) | Game | n/a (Gaming) | no | iOS, in-app choice | Epic payments offered beside Apple IAP, with 20% back in Epic Rewards | Share of players choosing each | ~40% Epic payments, ~60% Apple IAP (Tim Sweeney to The Verge) | 2025-06-03 | https://tech.slashdot.org/story/25/06/03/1914219 | Directional (CEO statement, incentive bundled) |
| W48 | Paddle, aggregate of Paddle customers and RevenueCat content | Cross-app | All | mixed | iOS link-out | App-to-web vs IAP, bands | Conversion change; net proceeds; LTV | Conversion: average 5–12% decline, "good" 0–1%+. Net proceeds: average 15% (small-business tier), good 24%+. LTV: average 10%+, good 17%+. Denominator not stated | Not dated (written ~10 months after the ruling) | https://www.paddle.com/resources/how-are-teams-growing-faster-with-ios-external-payments | Directional (vendor bands) |
| W49 | Adapty, State of In-App Subscriptions 2026 | Cross-app, US web paywalls since mid-2025 | All | mixed | iOS web paywall vs in-app | Plain web paywall vs in-app paywall (not a test; not a full web2app funnel) | Install → paid; retention; LTV | Install → paid 1.10% web vs 1.60% in-app ("in-app converts 45% better"); LTV $35.8 vs $40.1. Retention M1 64.5% web vs 46.2% in-app; M6 ~20% vs ~30% | Report 2026 (data 2025) | https://adapty.io/state-of-in-app-subscriptions-report/ | Directional (vendor aggregate, early data) |
| W50 | Spotify | Music streaming | Media & Entertainment | no | iOS link-out | Prices and an external purchase link shown in the iOS app after the ruling | Free → Premium upgrades on iOS | "Significant increase"; Android rate "relatively constant" over the same two weeks. No figures | Filing reported 2025-05-21 | https://techcrunch.com/2025/05/21/spotify-says-support-for-external-payments-on-ios-has-already-boosted-subscriptions | Anecdotal |

Android external offers: no published conversion or revenue result found (see gaps).

## H. Refunds, chargebacks, retention: web vs store buyers

| ID | App/company | Category | Bucket | AI tag | Surface | Change | Metric | Result | Date | URL | Tier |
|---|---|---|---|---|---|---|---|---|---|---|---|
| W51 | FunnelFox, State of Web2App 2026 | Cross-category | All | mixed | web vs store | Web vs app-store LTV, US (not a test) | Cumulative LTV at month 12 | Annual $69 vs $34; monthly $55 vs $38; weekly $45 vs $35 (no store fees, retention per report). Expert note: H&F web LTV $80–90 vs app $40–45, but web CPAs higher | Pub. 2026-01 | https://funnelfox.com/state-of-web2app-2026 | Directional (vendor aggregate; buyers self-select into web) |
| W52 | FunnelFox, State of Web2App 2026 | Cross-category | All | mixed | web | Refunds on web funnels (not a test) | Refund rate | By revenue: US 5.67%, Europe 3.47%, LATAM 2.60%, APAC 8.00%. By transactions: US 3.67%, Europe 4.18%, LATAM 2.50%, APAC 6.72%. By plan: weekly 0.20%, monthly 1.81%, annual 3.69%. 45.36% of refunds within 24 h, 73.46% within 7 days | Pub. 2026-01 | https://funnelfox.com/state-of-web2app-2026 | Directional (chart titles mislabelled in the report) |
| W53 | Runna (Paddle) | Running coach | Health & Fitness | no | web vs in-app | Web sales added beside the app stores; Paddle Retain for cancel and win-back on web | Retention (not defined) | Web subscribers 15% higher retention than in-app. No window, cohort or method | Not dated; also cited 2026-05-13 | https://www.paddle.com/customers/how-mobile-app-runna-monetized-on-the-web ; https://www.paddle.com/blog/app-retention-fltr | Directional |

Dipsea (#W39) and the RevenueCat follow-up (#W40) also belong here: trial conversion was higher on web in both web arms (28.2% and 26.3% vs 25.0%), more web subscribers kept auto-renew on (101 vs 46) and more were refunded (38 vs 28). Adapty's web paywall retention (#W49) runs the other way after month 1.

---

## Count by tier

One tier per row.

| Tier | All rows | New rows | "Same as" rows |
|---|---|---|---|
| Strong | 12 (W1, W2, W8, W9, W10, W17, W19, W20, W21, W35, W36, W39) | 11 | 1 (W8 = onboarding #38) |
| Directional | 37 | 34 | 3 (W7 = onboarding #39, W12 = onboarding #37, W30 = upsell #U34) |
| Anecdotal | 2 (W38, W50) | 2 | 0 |
| Observed | 2 (W13, W28) | 2 | 0 |
| **Total** | **53** | **49** | **4** |

Of the 12 strong rows, only one is a subscription app's web checkout or link-out test (#W39 Dipsea). Three are web-funnel UX tests from non-app or SaaS businesses (W1, W2, W8), one is Lasting's quiz pacing (W9), one is a survey-science meta-analysis (W10), four are Stripe payment-method holdbacks across many businesses (W17, W19, W20, W21), and two are Android sign-in tests (W35, W36).

## Notes for the skill

**What the evidence supports** (research notes; the skill uses only what bears on screens: fee and proceeds notes are background)

1. **Link-out from an iOS paywall usually lowers conversion and may still raise net revenue. It depends on the fee tier.** The only randomized test (#W39 Dipsea) found web-only cut initial conversion by a third (27.0% → 18.1% per customer) and roughly matched IAP proceeds at a 30% fee ($1.96 vs $2.09 per customer), but lost clearly at 15% ($1.96 vs $2.53). The losses happen at the hand-off: CTA tap → start was 70.9% for IAP vs 44.4% for web, while taps on the paywall were equal. Vendor reads point the same way: Superwall −11.9% conversion (#W41), Adapty App 1 −26% (#W42), Paddle "average 5–12% decline" (#W48), Adapty cross-app install→paid 1.10% vs 1.60% (#W49). The language app on the 15% tier reverted despite higher web conversion (#W43). The skill should model net proceeds per paywall viewer at the app's real fee tier, not headline fee savings.
2. **Offer both, don't replace.** The IAP + web arm (#W39 C) beat web-only on conversion (23.5% vs 18.1%) and took ~36% of its revenue on web. A side-by-side "Pay on web, save 25%" button with Apple Pay-only checkout reported no conversion drop (#W45, days of data). Replacing IAP with web is the riskiest version.
3. **Wallet-first checkout is the best-supported checkout lever.** Apple Pay has two Stripe controlled results (+22.3% conversion in the 2025 holdback, #W19; +10% in an earlier A/B, #W20) and is ~60% of web2app transactions (#W26). Saved details (Link) +14% for returning buyers (#W21). Local methods matter by market: PayPal in Germany +47% for digital media, and it is ~90% of web2app payments there (#W19, #W26). Local currency +17.8% international revenue (#W17).
4. **Fewer fields and no forced account at checkout.** Forced account creation is the third-largest fixable abandonment reason (18%, #W27); removing it was worth +45% purchasers in the classic retailer case (#W33, before/after). Rino's field cut was bundled with a provider switch (#W23). Most checkouts need about 8 fields and carry 11.3 (#W28). In web2app, the account belongs after payment, as a passwordless hand-off into the app (#W34: Day-0 logins 2×).
5. **The first screens decide the funnel.** Only 47.5% of web funnel sessions reach screen 2 (#W4). Matching the landing headline to the ad or search intent (+31.4%, #W1), a quiz as the hero (+34% members, #W2), faster load (+8.4% retail conversion per 0.1 s, #W3) and shorter waits between quiz questions (+60%, #W9) all act on the top of the funnel.
6. **Payment failures are a large, fixable leak in web2app.** 30–50% of initiated payments fail (#W26). A retry screen offering another method recovered ~20% of failed prepaid-card payments (#W24); a fallback provider plus retries recovered 24% of failed first payments and 31% of failed renewals (#W25). The first three retries do most of the work (19.3%, 12.5%, 9.3%, #W26).

**Where it flips**

- **Fee tier flips link-out.** At 30%, web-only roughly broke even in Dipsea and won in Adapty App 1; at 15%, Dipsea lost ~23% of proceeds per customer and the Adapty language app reverted (#W39, #W43).
- **Web conversion can be higher or lower than IAP.** Lower in #W39, #W41, #W42, #W49; higher per view in #W43 (+55%) with lower ARPPU. Who sees the web option (post-onboarding vs contextual) changes the result 4× (#W44).
- **Web buyers: better trial conversion and renewal intent, more refunds, and maybe worse retention.** Dipsea web arms converted trials better (#W39), the RevenueCat follow-up had 2.2× more web subscribers set to renew but more refunds (#W40), Runna reports +15% retention on web (#W53), yet Adapty's cross-app web retention drops below in-app by month 6 (#W49). Treat "web buyers retain better" as unproven.
- **Long vs short quizzes.** A 51-step funnel won at Rino (#W11, no number) and Noom runs up to 113 screens (#W13), while shortening waits lifted Lasting +60% (#W9). The evidence supports "quiz length is a test, not a rule"; it cuts pacing and dead time, not necessarily questions.
- **Progress bars.** A constant progress bar doesn't reduce drop-off; one that moves fast first and slows later does, and slow-to-fast increases it (#W10). Fake-fast bars raise honesty questions; the skill should not reward them.

**Metric traps**

- Dipsea's "initial conversion" is per customer in arm, not per paywall view; Adapty App 1–3 are per paywall view; Adapty SOIS is install → paid; FunnelFox is per ad click or per session. Don't compare across them.
- FunnelFox's web vs app LTV (#W51) and upsell ">200%" (#W30) compare self-selected funnels; they are not tests.
- Stripe lifts (#W19–#W21) are across many businesses and mostly not subscription apps. Use them for direction and order of magnitude, not as an app's expected lift.
- "Revenue +X%" case studies (#W18, #W31, GenioKid, Glam AI) measure a whole move to web plus other changes; none isolates a funnel element.

## Sources checked with no usable numbers

- RevenueCat, "Meet the Web Purchase button" (2025-05-02): no results. https://www-docs.revenuecat.com/blog/growth/introducing-web-paywall-buttons
- RevenueCat, "Pros, cons and gotchas of external iOS payments" (2025-05-02): premortem; only an anecdote of 3× year-one renewals for one client's web buyers, called a "red herring" by the author. https://www.revenuecat.com/blog/growth/external-ios-payments-pros-cons-gotchas
- RevenueCat, "Free trials don't make sense anymore" (2026-03-23): SOSA aggregates only; no paid-trial or web discount result. https://www.revenuecat.com/blog/growth/free-trials-dont-make-sense-anymore/
- RevenueCat SOSA 2026 page: web revenue 3.2% of revenue globally (4.9% North America); 41% of top-tier vs 1.3% of hobby apps have web revenue; Rise Science's web discount vs trial point has no numbers. Benchmark, not a test. https://www.revenuecat.com/state-of-subscription-apps/
- Superwall "App to Web Checkout" feature page and 26 case studies: none about web checkout. https://superwall.com/features/app-to-web-checkout ; https://superwall.com/case-studies
- Stripe guide "How app developers can reduce fees…": "double-digit" fee savings, Link 3× faster; no conversion figures. https://stripe.com/guides/how-app-developers-can-reduce-fees-and-create-an-optimized-checkout
- Paddle, "What's next for app2web" (2025-02-26): repeats Stoikk, Superwall, Dipsea. Paddle external-payments guide: repeats Dipsea and Runna; mentions a Dipsea auto-renew-off split (2.5% web vs 18% App Store, 2,000 subscriptions) that we could not find on a RevenueCat page, so it is not used. https://www.paddle.com/blog/whats-next-for-app2web ; https://www.paddle.com/resources/external-payments-guide-ios-app-developers
- Betterlaunch playbook of a Sub Club video quoting "3.5% vs 19%" auto-renew cancellations for web vs IAP: secondhand; the video was not watched. https://www.betterlaunch.co/playbooks/revenuecat-web-payments-experiment-4
- FunnelFox case studies with no funnel-element numbers: Talaboos/Yolume (purchase CR 2.5–3%, up to 3.5%; email capture 11–13%; no comparison), GenioKid (MRR 20× in 7 months, whole move), Glam AI (no conversion figures), FitLens AI (launch speed only). FunnelFox blog: A/B testing guide (sizing advice only), "wallet-first Apple Pay" release note (claim without data), chargeback prevention post (processor thresholds ~0.5% Stripe, ~1% Paddle; no effect sizes).
- web2wave: Once chat case ("more than doubled", no figures); community thread on quiz length (anonymous "+12%" for 8 → 4 questions and "~8%" for 10 → 4–5, no method; not used).
- Patreon (TechCrunch, 2025-05-06), Kindle "Get book" (GeekWire, 2025): launches, no results.
- Subscription Index, "Web to app funnels: is saving 30% a good idea?" (2025-12-19): qualitative comparison; cites a Cornell one-click study (+43% order frequency) we did not open.
- AppsFlyer "web-to-app conversion leak" (2026-03-01) and Airbridge deep-linking post: vendor figures without method (deep links "+51%"); the Apartment List case was opened and used (#W34).
- Blue Stout "express checkout message in drawer cart +10.7%" (2022): agency claim, store and method not stated; not used.

**Could not open or verify:** The Verge interview behind the Fortnite split (Slashdot summary used); Solidgate's A/B numbers for Hily (not published); the Sub Club video.

## Biggest evidence gaps

1. **Android external offers / alternative billing.** No published conversion, revenue or user-choice share for Google Play's US external-offer or alternative-billing programs. Spotify's statement is iOS.
2. **Only one randomized link-out test (Dipsea).** Everything else is vendor reads without samples. No test of in-app browser (SFSafariViewController) vs Safari, of a discount size on the web button, or of Apple Pay-only vs card on the link-out sheet.
3. **Hand-off and login after a web purchase.** No published purchase → install → login rates for subscription web2app (FunnelFox's 90% is unsourced). Apartment List is real estate, Smart Lock rows are Android sign-in, not post-purchase.
4. **Quiz length in web2app.** No controlled test of question count with numbers. Only pacing (#W9), the Rino anecdote and survey-science progress-bar evidence.
5. **Web paywall plan and price tests.** No controlled web2app test of trial vs no trial, paid trial, or plan order. Prehab and Reading.com are bundled before/after.
6. **Post-purchase upsell design.** No test of one-click vs re-entry, number of upsells, or upsell refund rates; only share-of-revenue figures.
7. **Refunds and chargebacks by surface.** No published chargeback rate for web2app vs App Store refunds; RevenueCat's one count (38 vs 28 refunded, #W40) is the only side-by-side number.
8. **Category coverage.** Health & Fitness and Education dominate the app rows. Nothing for Photo & Video, Productivity (except Todoist sign-up) or Business web2app funnels.


# Part 2. Benchmarks from public reports

Checked 2026-10-30. Public sources only; every figure carries its URL, the source date and a tier:

- **strong benchmark**: large platform dataset with a stated metric (still vendor data; say whose)
- **directional**: numbers without method, sample or denominator, or confounded/vendor-claimed
- **case**: one app or one experiment
- **rule**: binding text (fees from official price lists count here)
- **pending**: not settled

"Secondary" = a source reporting someone else's data. Vendor caveat: FunnelFox, Superwall, Adapty, RevenueCat, Stripe and Paddle all sell web checkout or IAP tooling; RevenueCat's app-to-web posts argue *against* moving, FunnelFox's *for*. Quote both as findings, never as settled fact.

---

## B0. Metric definitions (never merge across rows)

| Source | Denominator | What "conversion" means | Revenue basis |
|---|---|---|---|
| FunnelFox State of Web2App 2026 | **web funnel session** (ad click / session created) | session → 2nd screen → paywall → purchase; app comparison counts from **ad click** | web gross |
| RevenueCat SOSA 2026 | install / trial start; web share = share of revenue | download → paid (D35), trial → paid | net of store fees and refunds |
| Adapty State of In-App Subscriptions 2026 (web section) | **install** | install → paid (plain US web paywall, not a quiz funnel) | gross |
| Adapty blog "App-to-web paywalls: one year" | **paywall view** | purchases per paywall view; ARPU = net proceeds per viewer | net |
| RevenueCat Dipsea test | **customer in arm (new US users assigned to the paywall test)**, not per paywall view | "initial conversion" = trial start or purchase; "conversion to paying" | gross and modelled net |
| Superwall app-to-web | not stated | "initial conversions" | modelled net proceeds |
| Recurly 2026 | subscriber / renewal attempt (web-billed merchants, mostly non-app) | trial conversion denominator not stated | billing data |
| Stripe | checkout session in Stripe's Optimized Checkout Suite holdback | checkout conversion | — |
| Baymard | e-commerce cart (not subscriptions) | cart abandonment | — |
| AppsFlyer | **installer** (web-to-app campaign user) | paying users within 30 days, incl. one-time IAP | — |

Fees: keep **store fees** (Apple/Google commission) apart from **payment processing** (Stripe/Paddle/PSP) and from **merchant-of-record** fees (tax, chargebacks, support). A "web saves 25 points" claim usually compares 30% store fee with ~5% processing and ignores tax engines, MoR, refunds, chargebacks and engineering.

---

## B1. Funnel conversion by step

| Metric | Value | Definition | Source, date | Tier |
|---|---|---|---|---|
| Web funnel: session → 2nd screen | **47.5%** | share of sessions | FunnelFox, State of Web2App 2026 (Jan 2026) https://funnelfox.com/state-of-web2app-2026 | strong benchmark (vendor; sample size not stated) |
| Web funnel: session → paywall | **13%** | share of sessions | same | strong benchmark (vendor) |
| Web funnel: session → purchase | **3%** | share of sessions | same | strong benchmark (vendor) |
| App-store funnel: ad click → install → purchase | 100% → **30.0%** → **1.5%** | share of ad clicks | same | directional (no method for app side) |
| "Web converts 2×" | 3.0% vs 1.5% | per ad click | same | directional (vendor headline; different audiences and CPAs) |
| Biggest drop | screen 2 | — | same | strong benchmark (vendor) |
| ARPU per session (web) | US **$1.46** · Canada $1.06 · APAC $0.81 · Europe $0.74 · LATAM $0.43 | revenue ÷ all sessions | same | strong benchmark (vendor) |
| ARPPU per paying session | US $26.99 · CA $30.57 · APAC $30.90 · EU $29.47 · LATAM $27.31 | per paying session | same | strong benchmark (vendor) |
| Plain US web paywall vs in-app, install → paid | web **1.10%** vs in-app **1.60%** ("in-app converts 45% better") | per install; US web paywalls since mid-2025; early data | Adapty, State of In-App Subscriptions 2026 https://adapty.io/state-of-in-app-subscriptions-report/ | strong benchmark (early, small web sample, not a quiz funnel) |
| Paid users within 30 days, web-to-app campaign installers | **13.6%** average across categories; Food & Drink EU 30.2%, Shopping APAC 23.1%, Finance NA 18.2% | per installer, any IAP | AppsFlyer web-to-app guide (May 2025, upd. Apr 2026) https://www.appsflyer.com/blog/measurement-analytics/web-to-app-guide/ | directional (undated; includes e-commerce, not subscriptions) |
| Web-to-app campaign conversions growth | **+77%** 2024 vs 2023 | AppsFlyer owned media | same | directional |
| Post-payment handoff loss | "up to 40–50%" pay on web and never log in when handoff is unclear | no study cited | FunnelFox blog, Marcus Burke (Aug 2025) https://blog.funnelfox.com/web2app-quizzes-as-profit-engine/ | directional (anecdotal estimate) |

## B2. Quiz length

| Metric | Value | Source, date | Tier |
|---|---|---|---|
| Observed quiz lengths | Calm ~40 screens; Flo close to 40; Runna 19; Homemade Method "long" | FunnelFox blog "Funnel patterns that work in 2026: Part 2" (16 Feb 2026) https://blog.funnelfox.com/web2app-funnel-patterns-2026-part-2/ | observed (author's walk-throughs) |
| "Thirty to sixty screens are acceptable" in health and vulnerability-driven categories | recommendation | same | anecdotal |
| Quiz trades volume for intent (higher LTV, lower volume) | no numbers | FunnelFox report, expert view (Jessica Gotti, Paired) | anecdotal |

**No public controlled test of quiz length vs conversion or LTV was found.** Screen-2 drop (47.5% reach it) is the only aggregate step benchmark.

## B3. Web vs store price, plan mix and trials

| Metric | Value | Source, date | Tier |
|---|---|---|---|
| Web revenue by plan | 1 month **48.8%** · 1 week **30.5%** · 1 year 12.2% · 3 months 8.4% | FunnelFox 2026 | strong benchmark (vendor) |
| Web revenue by trial type | no trial **56.9%** (landing page: 56.8%) · paid trial **28.9%** · free trial **14.3%** | FunnelFox 2026 | strong benchmark (vendor) |
| Average web price, US | 1 wk $8.14 · 1 mo $15.76 · 3 mo $31.76 · 1 yr $45.71; report says web prices "closely match" in-app | FunnelFox 2026 | strong benchmark (vendor) |
| Most popular web price, US | 1 wk $7.99 · 1 mo $12.49 · 3 mo $40.80 · 1 yr $74.94 | FunnelFox 2026 | strong benchmark (vendor) |
| Common web discounts vs in-app | 20%, 30% or 50% off (examples) | FunnelFox blog (Aug 2025) | anecdotal |
| Discounted paid first month beats free trial on web (better ad-optimisation signal) | no numbers | RevenueCat SOSA 2026, Leon Sasson (Rise) essay https://www.revenuecat.com/state-of-subscription-apps/ | anecdotal |
| Web annual 30% cheaper next to IAP (Dipsea arm C) → 36% of that arm's revenue came via web | $47.99 web vs $69.99 IAP | RevenueCat test (May 2025, upd. Mar 2026) https://www.revenuecat.com/blog/growth/iap-vs-web-purchases-conversion-test | case |
| Web ARPPU vs native | App 1: $47.59 web vs $23.76 native (+100%); App 3: $52.83 vs $65.99 (−20%) | Adapty blog, Victoria Kharlan (6 May 2026, upd. 28 Sep 2026) https://adapty.io/blog/app-to-web-paywalls-ios-one-year-data/ | case (App 1 "directional read", not 50/50) |

## B4. App-to-web link-out (US iOS) conversion and adoption

| Metric | Value | Definition | Source, date | Tier |
|---|---|---|---|---|
| Dipsea 4-arm test, initial conversion | IAP-only **27.0%** · IAP+web 23.5% · web-only **18.1%** | new US users, ~3,100/arm | RevenueCat (14 May 2025; upd. 18 Mar 2026) https://www.revenuecat.com/blog/growth/iap-vs-web-purchases-conversion-test | case (strong design, one app, reader-app exempt) |
| Dipsea, CTA tap → initial conversion | IAP **70.9%** vs web **44.4%** | per CTA tap | same | case |
| Dipsea, trial → paid | IAP 25.0% · IAP+web 28.2% · web-only 26.3% | per trial | same | case |
| Dipsea, conversion to paying | 6.3% · 5.9% · 5.3% | per user | same | case |
| Dipsea, take-home | web-only ≈ **94¢** per IAP dollar at 30% Apple fee; ≈ **77¢** at 15% (post summary says 86¢: inconsistent) | ~6% blended web cost assumed | same | case |
| Second RevenueCat test (owned app, May 2025) | conversion to paying 7.8% IAP vs 7.4% IAP+web (−5.1%); refunded customers 28 vs 38 (+35.7%); active set-to-renew 46 vs 101 (+119%; text says "+170%") | — | RevenueCat, "Why you shouldn't use app-to-web checkout" (14 Apr 2026) https://www.revenuecat.com/blog/growth/why-you-shouldnt-use-app-to-web | case |
| Superwall early data | initial conversions **−11.9%**; net proceeds **+19.85%** (modelled, assumes unchanged trial conversion); at 15% SBP rate −1.30% | definition, sample and dates not given | Superwall (7 May 2025) https://superwall.com/blog/initial-data-is-in-app-to-web-conversion-rates-after-the-app-store-ruling | directional |
| Adapty App 1 | 4.95% native vs **3.69%** web per paywall view (−26%); ARPU per viewer $1.16 vs $1.77 (+53%; text also says 47%) | per paywall view | Adapty (6 May 2026) https://adapty.io/blog/app-to-web-paywalls-ios-one-year-data/ | case |
| Adapty App 3 | 2.54% native vs **3.93%** web per view (+55%); ARPU $1.67 vs $1.52 (−9%) | per paywall view | same | case |
| Adapty App 2, web paywall by placement | post-onboarding 3.38% · last-chance offer 2.90% · mid-funnel 2.18% · contextual upsell **0.87%** per view; A/B variant on main placement 5.54% | per view, web only | same | case |
| Dipsea retention signal (secondary, not found on a RevenueCat page: don't cite as a result) | 2.5% of web subscribers had auto-renew off vs 18% of App Store subscribers (2,000 subs started in May) | — | Paddle guide (undated, 2026) https://www.paddle.com/resources/external-payments-guide-ios-app-developers citing RevenueCat | case, secondary |
| Unnamed apps | 10–15% conversion drop offset by "2–3×" better trial-to-paid on web | — | same | directional, secondary |
| Runna | web subscribers 15% higher retention | — | same | case, secondary |
| Link-out **adoption** (share of apps) | **No public count found.** SOSA: "continue in-app" CTAs seen, "indicating more app-to-web flows", no figure | — | RevenueCat SOSA 2026 | gap |

**Read:** every controlled number so far shows a lower purchase rate at the link-out (−5% to −33% at the first conversion), sometimes offset by price, trial-to-paid or fees. Sign of net revenue depends on the app's Apple rate (30% vs 15%).

## B5. Web adoption and revenue share

| Metric | Value | Source, date | Tier |
|---|---|---|---|
| Top-100 grossing apps using web2app | **82%** in 2025, from 30% in 2024 (PDF); landing page says ~46% in 2024 | FunnelFox 2026 | strong benchmark (vendor; inconsistent baseline) |
| Apps with web2app funnels | +77% YoY 2025, +63% 2024 | FunnelFox 2026 | strong benchmark (vendor) |
| Global web2app revenue 2025 | "$60B+" (landing page only) | https://funnelfox.com/state-of-web2app-2026 | directional |
| Web2app revenue by region | US 63.6% (landing: 63.7%) · EU 14.2% · APAC 7.7% · LATAM 5.6% · MEA 4.6% · CA 4.2% | FunnelFox 2026 | strong benchmark (vendor) |
| Web share of subscription revenue (RevenueCat apps) | **3.2%** global · 4.9% North America · 0.8% IN/SEA | RevenueCat SOSA 2026 https://www.revenuecat.com/state-of-subscription-apps/ (re-read 2026-10-30) | strong benchmark |
| Apps with any web revenue by tier | top tier **41%** · tier 4 28% · hobby 1.3% | same | strong benchmark |

## B6. Payment method mix and wallets

| Metric | Value | Source, date | Tier |
|---|---|---|---|
| Web2app transactions by method (worldwide) | Apple Pay **~60%** · cards 20% · PayPal 18% · Google Pay 2%; PayPal ~90% in Germany | FunnelFox 2026 | strong benchmark (vendor) |
| Web-billed subscription transactions, US | debit 48.8% · credit 34.7% · PayPal 9.6% · rest Apple Pay/Amazon Pay/other | Recurly 2026 State of Subscriptions (14 Jan 2026) https://recurly.com/resources/report/state-of-subscriptions/ | strong benchmark (Recurly merchants, mostly non-app) |
| Same, EMEA | debit 50.9% · credit 12.8% · PayPal **27.7%** | same | strong benchmark |
| Apple Pay offered in checkout | **+22.3%** conversion, +22.5% revenue | Stripe (10 Apr 2025) https://stripe.com/blog/testing-the-conversion-impact-of-50-plus-global-payment-methods | strong benchmark (holdback in Stripe's suite; sample not stated) |
| Apple Pay shown early (Express Checkout) vs at end | ~**2×** conversion | same | directional |
| PayPal, Germany, digital books/music/movies | +47% conversion | same | strong benchmark (vendor) |
| iDEAL NL +39% · BLIK PL +46% · Konbini JP (digital apps) +27% · SEPA DD EU +12% · Cash App US (games) +5% | conversion | same | strong benchmark (vendor) |
| Any relevant method added (all methods) | +7.4% conversion, +12% revenue | same | strong benchmark (vendor) |

## B7. Authorization, declines and recovery

| Metric | Value | Source, date | Tier |
|---|---|---|---|
| Initiated web2app payments that fail | **30–50%** (3DS/bank auth friction, issuer declines, missing wallets, gateway errors) | FunnelFox 2026 | directional (range, no denominator) |
| Renewal outcome | 60% succeed first attempt · 17.5% fail then recovered · 22.5% lost; recovery adds 15–20% revenue | FunnelFox 2026 | strong benchmark (vendor) |
| Retry success by attempt 1–10 | 19.3 · 12.5 · 9.3 · 6.5 · 5.5 · 4.8 · 3.3 · 3.0 · 3.3 · 4.7%; first 3 ≈ half of recoverable | FunnelFox 2026 | strong benchmark (vendor) |
| Renewal attempts declined into dunning | ~**9 in 100** | Recurly 2026 | strong benchmark |
| Dunning recovery | monthly plans **53%**; failed **annual** renewals **23.3%** | Recurly 2026 | strong benchmark |
| Decline geography | US twice as likely declined at **sign-up** (cards); EMEA twice as likely at **renewal** (wallets/APMs) | Recurly 2026 | strong benchmark (ratio only) |
| Involuntary churn | ~1/3 of total churn in every industry (32–38%); $10–25 price band 1.30% vs voluntary 2.99% (monthly) | Recurly churn benchmarks (Jul 2026) https://www.recurly.com/research/churn-rate-benchmarks | strong benchmark |
| Stripe average recovery | "Businesses using Stripe recover **55%** of failed payments on average"; $8.2B recovered in 2025 | https://stripe.com/billing (read 2026-10-30) | directional (vendor claim, no method) |
| Paddle | "close to 35% of all transactions fail" (unnamed study); ProfitWell Retain ">50%" recovery | https://www.paddle.com/resources/payment-failure (undated) | directional |
| Online vs in-person authorization | online can be ~10% lower; card account updater +1.72% (Postmates) | Stripe guide https://stripe.com/guides/optimizing-authorization-rates (undated) | directional / case |
| Retry limits | Stripe guide: networks allow 4–6 retries in 15 days; Paddle cites J.P. Morgan: up to 15 in 30 days (Visa, except category-1 declines) | same; Paddle page | rule, secondary (re-check with acquirer) |
| Checkout abandonment due to card declined | **10%** of US shoppers who abandoned (e-commerce) | Baymard (upd. 22 Sep 2025) https://baymard.com/lists/cart-abandonment-rate | strong benchmark (e-commerce, not subs) |

## B8. Checkout UX (e-commerce baseline, Baymard)

| Metric | Value | Tier |
|---|---|---|
| Average documented cart abandonment | **70.22%** (50 studies) | strong benchmark |
| Abandonment reasons (excl. "just browsing") | extra costs 40% · didn't trust site with card 19% · forced account creation 18% · too long/complicated 17% · total cost not visible up front 12% · card declined 10% · not enough payment methods 9% | strong benchmark (survey) |
| Average US checkout | 23.48 form elements by default; 14.88 form fields | strong benchmark |
| Conversion gain from fixing solvable checkout issues | 35.26% (large e-commerce sites) | directional (Baymard estimate) |

Source: https://baymard.com/lists/cart-abandonment-rate (last updated 22 Sep 2025). Physical-goods context: shipping costs drive the top reason; for subscriptions the analogue is hidden renewal price or taxes.

## B9. Upsell share (post-purchase on web)

| Metric | Value | Source | Tier |
|---|---|---|---|
| Upsells as share of total web2app revenue | **4.07%** | FunnelFox 2026 | strong benchmark (vendor) |
| Upsell LTV effect | headline "+20% LTV"; bullet "×2 revenue lift (median)"; chart ">200%" — **incompatible; quote all three** | FunnelFox 2026 | directional |
| Average upsell price by primary plan, US | 1 wk $10.51 · 1 mo $15.77 · 3 mo $17.56 · 1 yr $8.72; global median ~$9.31 | FunnelFox 2026 | strong benchmark (vendor) |
| Enforcement signal | FTC v. Genesis Tech (Jun 2026): add-on products added "without consumers' knowledge or consent", double charges | https://www.ftc.gov/news-events/news/press-releases/2026/06/ftc-sues-stop-sprawling-enterprise-operating-unlawful-subscription-schemes | case (allegation, pending) |

## B10. Refunds and chargebacks

| Metric | Value | Source | Tier |
|---|---|---|---|
| Web2app refund rate, share of revenue | APAC 8.00% · US **5.67%** · Europe 3.47% · LATAM 2.60% | FunnelFox 2026 (charts mis-titled "renewal cycles") | strong benchmark (vendor) |
| Same, share of transactions | APAC 6.72% · Europe 4.18% · US 3.67% · LATAM 2.50% | same | strong benchmark (vendor) |
| By plan | 1 wk 0.20% · 1 mo 1.81% · 1 yr 3.69% | same | strong benchmark (vendor) |
| Timing | 45.36% within 24 h; 73.46% within 7 days; 91.69% within 30 days; median 1.6 days | same | strong benchmark (vendor) |
| RevenueCat owned-app test | refunded customers +35.7% with IAP+web vs IAP only (28 → 38) | RevenueCat (Apr 2026) | case |
| Cal AI | "high chargebacks" after a second purchase flow shown on decline | Paddle blog https://www.paddle.com/blog/what-cal-ai-taught-us-about-app2web | case, secondary, no number |
| Card-network thresholds (see platform-rules.md) | Visa VAMP excessive merchant **1.5%** (US/CA/EU/AP from 1 Apr 2026), min 1,500 TC40+TC15/month; Mastercard ECM **1.5%** and 100 chargebacks/month, HECM 3% and 300 | Justt (31 Mar 2026), Chargebacks911 (Nov 2025) | rule, secondary |

**Gap:** no public chargeback *rate* benchmark for web2app subscriptions was found.

## B11. Retention and LTV, web vs store

| Metric | Value | Source | Tier |
|---|---|---|---|
| US 12-month cumulative LTV, web vs app | annual $69 vs $34 · monthly $55 vs $38 · weekly $45 vs $35 | FunnelFox 2026 | directional (vendor; app curve labelled only at months 1/3/6/9/12) |
| H&F web vs app LTV | web $80–90 vs app $40–45; web CPAs higher | FunnelFox 2026, Anton Kuzmin (AdQuantum) | anecdotal |
| Web weekly retention by period | 54.0% (2) · 29.0% (3) · 9.5% (6) · 3.1% (12) | FunnelFox 2026 | strong benchmark (vendor) |
| Web monthly retention | 56.5% (M2) · 43.6% (M3) · 21.3% (M6) · 10.2% (M12) | same | strong benchmark (vendor) |
| Avg renewal cycles | 1 wk 4.21 · 1 mo 2.18 · 3 mo 1.80 · 1 yr 1.20 | same | strong benchmark (vendor) |
| Churn timing, annual web plans | 12.8% same day, 12.2% days 1–3, 26.9% days 4–7 → auto-renew turned off early | same | strong benchmark (vendor) |
| Plain web paywall vs in-app (Adapty), retention M1 / M6 | web **64.5% / ~20%** vs in-app **46.2% / ~30%** (web starts higher, drops faster) | Adapty 2026 report | strong benchmark (early) |
| Same, average LTV | web $35.8 vs in-app $40.1 (month 1); "without App Store fees, web LTV is still $4 lower" | same | strong benchmark (early; gross) |
| Web-billed trial → paid (all Recurly merchants) | 47% (2021) → **34%** (2025); denominator not stated | Recurly 2026 | strong benchmark (not app-specific) |
| Annual renewal rate, web-billed | 82.9% | Recurly 2026 | strong benchmark |

## B12. Fees (store vs processing vs MoR)

| Item | Rate | Source | Tier |
|---|---|---|---|
| Apple IAP, US | 30% standard; 15% Small Business Program and subscriptions after year one | https://developer.apple.com/app-store/small-business-program/ (not re-opened) | rule |
| Apple, US link-out purchases | **0% today**; court allows a cost-based fee to be set on remand; Supreme Court review (No. 25-1311), ruling expected by Jun 2027 | TNW (30 Jun 2026) https://thenextweb.com/news/supreme-court-apple-epic-contempt-app-store-commission | pending |
| Apple, EU (from 1 Oct 2026) | IAP 26% / 15% reduced · own in-app checkout 20% / 10% · link-out **15% / 10%** | RevenueCat (1 Oct 2026) https://www.revenuecat.com/blog/company/apple-in-app-web-checkouts-eu | rule, secondary |
| Apple, EU (Jun 2025 – Sep 2026 terms) | 2% initial acquisition + 5%/13% store services + 5% Core Technology Commission | TechCrunch (26 Jun 2025) https://techcrunch.com/2025/06/26/apple-updates-the-rules-for-its-eu-app-store-by-adding-more-complicated-fees | rule, secondary (superseded) |
| Apple, Japan (from 18 Dec 2025) | out-of-app offers **15%**; 10% for SBP/partner programs and subscriptions after year 1; purchases within **7 days** of link tap commissionable; IAP has separate 5% processing | Appcharge (18 Dec 2025) https://appcharge.com/blog/external-payments-in-japan-the-fine-print-behind-apple-and-google-compliance | rule, secondary |
| Apple, South Korea / NL dating | Korea external purchase 26% (app can't also offer IAP); NL dating 3 points below standard | RevenueCat guidelines https://www.revenuecat.com/app-to-web-purchase-guidelines.md (undated) | rule, secondary |
| Google Play, EEA/UK/US from 30 Jun 2026 (AU/JP 30 Sep 2026) | subscriptions **10% + 5% billing fee** if Play Billing; other new installs 20%+5%; external web links on subscriptions 10% | Play Console Help, Service fees https://support.google.com/googleplay/android-developer/answer/112622 | rule |
| Google Play billing choice program (EEA/UK/AU/JP) | alternative billing and external links: subscriptions **10%**; link fee applies to purchases within **24 h** of the link | https://support.google.com/googleplay/android-developer/answer/17161464 | rule |
| Google Play, US programs | alternative billing / external content links: 10% subscriptions, 25% / 20% other (as proposed Dec 2025); reporting and fees from 1 Oct 2026, link developers given until 1 Feb 2027 | https://support.google.com/googleplay/android-developer/answer/15582165 ; Neon (10 Dec 2025) https://www.neonpay.com/blog/google-plays-new-u.s.-billing-linking-policies-what-game-developers-need-to-know | rule / secondary |
| Google Play, rest of world | 15% subscriptions; 15%/30% other | Play Console Help | rule |
| Stripe, US | **2.9% + 30¢** domestic card; +1.5% international card; +1% FX; Billing 0.7%; Tax 0.5%; dispute $15; Managed Payments (MoR) +3.5% | https://stripe.com/pricing (read 2026-10-30) | rule (price list) |
| Paddle (MoR) | **5% + 50¢** per checkout transaction incl. tax, fraud, chargebacks; bespoke under $10 | https://www.paddle.com/pricing (read 2026-10-30) | rule (price list) |
| Small-ticket effect | $5 weekly plan ≈ 9% in Stripe fees | RevenueCat (Apr 2026) | directional |
| Blended web cost assumed in tests | ~5–6% | RevenueCat Dipsea; Adapty; Paddle | directional |

---

## Gaps

- **Link-out adoption**: no public count (Appfigures, Sensor Tower) of US iOS apps that added external purchase links since May 2025 was found. FunnelFox's 82% is web2app (web-first), not app-to-web.
- **Quiz length**: no controlled test or aggregate of screen count vs conversion; only observations (19–40 screens) and advice ("30–60 acceptable").
- **Step benchmarks after the paywall**: no public numbers for paywall view → checkout start → payment success, email-capture rate, account-creation completion or app-download/login rate after web purchase (only the anecdotal "40–50% never log in").
- **Chargeback rates** for web2app; **3DS challenge rates and frictionless share** for subscription checkout: not found in public reports.
- **Post-purchase upsell take rates** (share of buyers accepting one-click upsells): not found; only revenue share (4.07%) and prices.
- **AppsFlyer** has no dedicated web-to-app benchmark report; only guide figures (installer-based, mixed verticals).
- **Sensor Tower / Appfigures** web revenue estimates not found.
- FunnelFox: sample, period granularity and means vs medians not stated; several text-vs-chart errata (see the local skill's Errata section). Landing page and PDF disagree on 2024 adoption (30% vs ~46%).
- Dipsea is a reader-exempt app; its web-only arm is not available to non-reader apps outside the US storefront rules.
