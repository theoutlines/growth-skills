# Seam evidence

Published tests that bear on the seam between onboarding and the paywall. Test
numbers match the onboarding-teardown evidence library, so #1 is the same test
everywhere in the suite. Every number was read on its source page (collected
October 2026). Lifts are relative unless marked pp.

**Tiers:** strong = controlled test with numbers; directional = numbers without
a stated method, or a bundled or cumulative result; anecdotal = a claim without
numbers; observed = seen in top apps, no public test.

## Tests

Includes a small set of paywall-element tests (#42, #43, #50, #60, #62, #64, #67) so paywall rows have numbered evidence in lite mode. When paywall-teardown is installed, its own impact ranges may also be quoted, labelled "Adapty prior (expected effect, not a measured test)".

| # | App | Category | Bucket | AI app? | What changed | Metric | Result | Date | Source URL | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Blinkist | Book summaries | Education | no | Paywall shows a day-by-day 7-day trial timeline. A trial welcome screen offers a reminder opt-in, with a push 2 days before the trial ends (iOS + Android). | Trial sign-ups; complaints; push opt-in; in-trial cancels | +23% trial sign-ups; -55% complaints; push opt-in 6% → 74%; -4% in-trial cancellations | Pub. 2021-01-19 | https://uxplanet.org/how-solving-our-biggest-customer-complaint-at-blinkist-led-to-a-23-increase-in-conversion-b60ad514134b ; https://abtest.design/tests/how-your-free-trial-works | Strong (A/B) |
| 6 | Duolingo | Language learning | Education | no | Soft/hard sign-up walls tuned: a subtle "Later" replaced "Discard my progress" | DAU | +8.2% DAU (combined wall optimization) | Article 2017-07-17 | https://review.firstround.com/the-tenets-of-a-b-testing-from-duolingos-master-growth-hacker | Strong (A/B; self-reported) |
| 8 | Opal | Screen time | Productivity | no | Paywall placed early, after a few motivation-building screens (incl. a lifetime screen-time projection) | Download → trial start | About 7% → about 17% absolute, over many iterations. The founder's rule: paywall as early as possible but after the personalised report, not on screen 1; moving it two screens earlier was worth about +10% relative trial starts (re-checked 2026-10-29) | Episode 2024-01-10 | https://subclub.com/episode/lessons-from-121-ab-tests-kenneth-schlenker-opal ; https://abtest.design/tests/driving-motivation | Directional (cumulative iterations) |
| 9 | Opal | Screen time | Productivity | no | Close button on the onboarding paywall made more visible | Activation; ARPU | Activation up, ARPU slightly down (no figures) | Episode 2024-01-10 | https://subclub.com/episode/lessons-from-121-ab-tests-kenneth-schlenker-opal | Anecdotal |
| 11 | Unnamed (Adapty data) | Productivity | Productivity | unknown | Outcome-focused onboarding vs feature-focused | Trial conversion; ARPU | +17% trial conv.; +13% ARPU | Pub. 2025-11-25 | https://adapty.io/blog/how-to-fix-your-onboarding-flow/ | Directional (anonymized, no method) |
| 12 | Unnamed (Adapty data) | Education | Education | unknown | Survey + trial lesson vs lesson only vs survey only | Trial starts; ARPU | Survey + lesson won: +25% trial starts; +78% ARPU | Pub. 2025-11-25 | https://adapty.io/blog/how-to-fix-your-onboarding-flow/ | Directional |
| 15 | Unnamed (Adapty data) | Education | Education | unknown | Onboarding loading screen removed vs kept | Trial conv.; ARPU | Removing the loader won: +22% trial conv., +30% ARPU (re-checked 2026-10-29) | Pub. 2025-11-25 | https://adapty.io/blog/how-to-fix-your-onboarding-flow/ | Directional |
| 21 | Rizz App (Rizz God) | AI dating helper | Social & Lifestyle | yes | One onboarding paywall replaced by two: early paywall (trial toggle off) + end-of-onboarding paywall with a delayed close button | Onboarding conv.; trial conv. | +10%; +10% | Pub. 2026-01-26 | https://superwall.com/case-studies/rizz-god | Directional |
| 22 | Flirt AI | AI dating helper | Social & Lifestyle | yes | Onboarding demographics used to route each segment to one of 3 paywalls | MRR; trial-to-paid | +83% MRR in 30 days; +20% trial-to-paid | Pub. 2026-02-28 | https://superwall.com/case-studies/flirt-ai | Directional (confounded with pricing/product changes) |
| 24 | Superwall aggregate (no app named) | Cross-category | All | mixed | Multi-page vs single-page onboarding paywalls | Paywall-view → trial/purchase | 12.41% vs 9.07% (about +37%), from 40M+ paywall opens, Feb–May 2026 | Pub. 2026-05-26 | https://www.superwall.com/blog/new-postmulti-page-onboarding-paywalls-convert-37-better-than-single-page-heres-why | Directional (observational, not randomized) |
| 41 | Moonly | Astrology/moon calendar | Social & Lifestyle | no | Free trial added to the annual plan only, on the first paywall | View → subscription; revenue/100 installs; ARPPU | +39%; +47%; +5% | Pub. 2024-05-08 | https://adapty.io/case-studies/moonly/ ; https://abtest.design/tests/free-trial-only-for-annual-subscription | Strong (A/B), sample not given |
| 42 | Mojo | Video/story editor | Photo & Video | no | Only the yearly plan shown; monthly behind "View all plans" | Yearly uptake | +15–20%; cancellations up slightly | Pub. 2023-10-12 | https://www.revenuecat.com/blog/growth/mojo-60-percent-arpu-growth-five-months/ ; https://abtest.design/tests/yearly-plan-as-the-default | Strong (experiment program) |
| 43 | Mojo | Video/story editor | Photo & Video | no | Annual price shown as a monthly equivalent | New revenue per paywall impression | Brazil +45%, Mexico +26%, US +8% | Pub. 2023-10-12 | https://www.revenuecat.com/blog/growth/mojo-60-percent-arpu-growth-five-months/ | Strong |
| 45 | Slopes | Ski tracker | Health & Fitness | no | "Trial Quickstart": one-tap redeem-trial button that skips the paywall screen | Trial starts; trial → paid | +25% trial starts; trial-to-paid about flat | Pub. 2022-04-12 | https://blog.curtisherbert.com/slopes-diaries-42-building-ramps-not-walls/ ; https://abtest.design/tests/payramp-not-paywall | Strong (A/B) |
| 46 | Slopes | Ski tracker | Health & Fitness | no | Trial popup when recording starts at mapped resorts | Trial starts; conversion | About 3x trial starts; conversion about -7% YoY | Pub. 2022-04-12 | https://blog.curtisherbert.com/slopes-diaries-42-building-ramps-not-walls/ | Directional (kill-switch rollout, not A/B) |
| 50 | VEED | Video editor | Photo & Video | yes | Paywall shows yearly/monthly prices upfront vs a benefits-only Pro pitch | Trial conv.; paid conv.; MRR; ARPU | +15%; +3%; +33%; +17% | Not dated (X post) | https://abtest.design/tests/showing-pricing-options-upfront (source: https://x.com/sab8a/status/2100593618385780885) | Directional |
| 54 | Daily Horoscope | Astrology | Social & Lifestyle | no | Country-specific paywall designs and pricing vs a generic global paywall | Trial start rate | +183% | Pub. 2026-03-26 | https://superwall.com/case-studies/daily-horoscope | Strong (A/B, geo audiences) |
| 55 | Speak4Me | Text-to-speech | Productivity | yes | Multi-step paywall (features first) vs single screen | Conversion; proceeds | +27%; +36% | Not dated | https://superwall.com/case-studies/speak4me | Strong (A/B) |
| 56 | Stompers | Walking | Health & Fitness | no | Multi-page paywall (benefits, trial reminder, then price) vs single page | Conversion | +16% (headline says annual trials, so unclear which) | Pub. 2026-01-01 | https://superwall.com/case-studies/stompers | Strong (A/B), metric ambiguous |
| 57 | Ahead | Emotional skills | Health & Fitness | no | Add-on offer: 30-day trial for a small fee besides the free 7-day trial | Trial conversion | +7% | Pub. 2026-04-11 | https://superwall.com/case-studies/ahead-app | Strong (control vs variant) |
| 58 | Unnamed (Léa Samrani talk) | n/a | n/a | unknown | Paywall copy changed from features to Jobs-to-be-Done outcomes | Conversion | +54% or more | Post 2025-07-01 | https://growthgems.substack.com/p/growth-gems-127-onboarding-activation | Directional |
| 60 | Runtastic | Running | Health & Fitness | no | Promo statement on the paywall replaced with a real 5-star user review | Paid subscriptions | +44% | About 2017-05 | https://abtest.design/tests/user-reviews-on-paywall | Directional |
| 62 | TIPSTOP | Betting tips | Media & Entertainment | no | "Free during the month" message + "Save 60%" badge | Direct conversion | +190% | Not dated | https://abtest.design/tests/clear-free-trial-message-discount-badge | Directional |
| 63 | Busuu | Language learning | Education | no | Free users limited to 1 language | Power-user conversion | +83% | About 2017-12 | https://abtest.design/tests/content-locking | Directional |
| 64 | Unacademy | Test prep | Education | no | Monthly price highlighted instead of full course price | CTR | +13.5% | Not dated | https://abtest.design/tests/highlighting-monthly-pricing | Strong (stated significance) |
| 65 | Shaw Academy | Online courses | Education | no | Reminder email 3 days before trial end | Sales | +14% (>99% significance) | Not dated | https://abtest.design/tests/free-trial-reminder | Strong |
| 67 | Going | Flight deals (web) | Social & Lifestyle | no | CTA "Trial for free" vs "Sign up for free" | Trial starts (MoM) | +104% | Not dated | https://abtest.design/tests/trial-for-free-cta | Directional |
| 70 | Cal AI | Calorie tracker (AI) | Health & Fitness | yes | 123 A/B tests over 12 months, 61 on the onboarding paywall (layout, offer framing, price, urgency, spin-wheel discount, video paywall) | Trial-to-paid; revenue | +31% relative trial-to-paid; monthly revenue 3×+ in 10 months. Funnel: 87% of new users see a paywall, 57% of viewers start a purchase, 63% of started purchases complete | Pub. 2026-04-15 | https://superwall.com/case-studies/cal-ai | Directional (cumulative programme, vendor-authored) |
| 71 | FitnessAI | Workout planner (AI) | Health & Fitness | yes | Paywall moved before onboarding, plus a video on the paywall | Paywall views; install-to-trial; trial-to-paid | Paywall viewers +50%; install-to-trial doubled; trial-to-paid unchanged; revenue doubled | Pub. 2023-09, upd. 2024-06 | https://www.revenuecat.com/blog/growth/paywall-tests-grow-app-revenue | Directional (two changes at once) |
| 72 | Rootd | Anxiety relief | Health & Fitness | no | Paywall moved to the start of onboarding | Revenue | 5× revenue, "almost no negative feedback" | Same article | https://www.revenuecat.com/blog/growth/paywall-tests-grow-app-revenue | Directional (before/after) |
| 75 | Superwall cohort of 18 apps | Cross-category | All | mixed | Discounted paywall shown when a user starts a purchase but doesn't confirm it (transaction abandon) | Share of revenue; refunds | 17% of total revenue came from these paywalls; refund rate lower than control (control: 438,144 users) | Pub. 2024-08-06 | https://superwall.com/blog/17-revenue-boost-with-transaction-abandon-paywalls-a-case-study/ | Directional (cohort comparison). Superwall notes some apps drew Apple scrutiny for this |

## E. Aggregated priors and expert notes

E-IDs are shared with the onboarding-teardown library.

| ID | Item | Figure | Source | Strength |
|---|---|---|---|---|
| E1 | Loading screen plus personalised-plan screen (Adapty A/B library, one flow) | ARPU around −50% | paywall-ab-test-assistant evidence library (Adapty, MIT) | Directional |
| E2 | Second-chance discount right after the onboarding paywall vs after the main in-app paywall (Adapty library) | Premium conversion about +25–30% after the onboarding paywall; ARPU down by roughly half after the main paywall | same | Directional |
| E3 | "How your trial works" explainer next to the paywall vs earlier in the flow (Adapty library) | Wins on ARPU next to the paywall; earlier it adds drop-off before the paywall is seen (no figure) | same | Directional, no figure |
| E4 | Comparison table on the paywall vs a comparison teaser screen before it (Adapty library) | Wins as the paywall, including the onboarding paywall; the teaser before it lost (no figure) | same | Directional, no figure |
| E5 | Guarantee screens before the paywall (Adapty library) | Tend to lose (no figure) | same | Directional, no figure |
| E6 | "Reverse trial" after paywall dismissal (temporary premium, no card) | Freemium conversion 0.4% → 4.5% | RevenueCat SOSA 2026 expert notes (Steve P. Young), https://www.revenuecat.com/state-of-subscription-apps/ | Anecdotal |
| E8 | Goal personalisation in onboarding (Adapty A/B library, many tests) | CR commonly +8–17%, ARPU +13–35% | paywall-ab-test-assistant evidence library (Adapty, MIT) | Aggregated prior, not one test |
| E7 | Paywall copy mirroring the user's last action (Superwall coaching sessions) | Conversion +10–15%; in one long-onboarding app only 40% of new users ever saw the paywall | https://superwall.com/blog/the-paywall-growth-lever-framework-how-to-build-smarter-experiments-faster | Anecdotal |

## Benchmarks used at the seam

| Benchmark | Value | Source |
|---|---|---|
| Install → paid by paywall placement (Adapty 2026) | Onboarding paywall with trial 1.35% vs in-app 0.89%; without trial 0.82% vs 0.76% | https://adapty.io/blog/high-performing-paywall-2026/ |
| Trial starts on day 0 | RevenueCat: 78–90% by category. Adapty: 89.4% overall. Different panels | https://www.revenuecat.com/state-of-subscription-apps/ ; https://adapty.io/state-of-in-app-subscriptions/ |
| Paywall reach and purchase steps (one app, #70) | 87% of new users see a paywall; 57% of viewers start a purchase; 63% of started purchases complete | https://superwall.com/case-studies/cal-ai |
| Trial → paid by trial length (RevenueCat, median) | ≤4 days 25.5%; 5–9 days 37.4%; 10–16 days 35.4%; 17–32 days 42.5% | https://www.revenuecat.com/state-of-subscription-apps/ |
