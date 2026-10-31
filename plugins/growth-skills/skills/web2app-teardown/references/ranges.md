# Ranges seen in published tests

How to read: the lowest and highest measured lift in published tests of this kind of change, on one metric, with the number of tests. Seen in other apps' tests; not a forecast for your app. Built only from Part 1 rows of `evidence.md`; never averaged.

Denominators are kept apart: per landing visitor, per checkout session, per customer in arm, per CTA tap, per paywall view, per completed trial and "denominator not stated" are different metrics, so each gets its own row even when the change is the same. "(computed)" = relative change worked out from the two rates or counts the row gives; both are shown.

| Pattern | Metric | Range seen | Tests | Strongest tier | Caveats |
|---|---|---|---|---|---|
| 1. Match the ad on the first screen | Trial sign-ups, per landing visitor | +31.4% | 1 (#W1) | strong | off-target (web SaaS, Campaign Monitor); 1,274 visitors |
| 1. Match the ad on the first screen | Trial starts, denominator not stated | +5% | 1 (#W7) | directional | Houzz dedicated paid-traffic landing (same as onboarding #39) |
| 2. Start with one easy answer | Memberships (conversion to paid) | +34% | 1 (#W2) | strong | off-target (web membership, Seamwork); sample not given |
| 2. Start with one easy answer | Revenue per visitor | +56% | 1 (#W2) | strong | off-target (web membership); includes pattern sales; sample not given |
| 3. Honest pacing and progress | Conversions (landing + sign-up completion), denominator not stated | +60% | 1 (#W9) | strong | strong per vendor, thin details: no sample, no date. #W10 (progress bars) gives direction only, no effect size |
| 4. A result screen built from the answers, with no claims | Conversion to test sign-up | +50% as stated (35% → 52%; computed +48.6%) | 1 (#W12) | directional | bundled (quiz reorder + results screen); a diagnostics sign-up, not a subscription (same as onboarding #37) |
| 5. Email after value | — | no published range | — | — | only observed (#W13, walkthroughs) and benchmark (Baymard); no test of email position |
| 6. Quiz length is a test, not a rule | — | no published range | — | — | no controlled test of length: #W11 has no conversion number, #W13 observed, FunnelFox screen counts anecdotal |
| 7. The charge first, per-day second | — | no published range | — | — | only cases and rules (Cal AI, ROSCA, CMA) and observed |
| 7. *Aggregate, not a range:* per-day price as the main number, total secondary | Paywall conversion, denominator not stated | +25% (vendor average across client tests) | aggregate (#W56), tests not shown | directional | web2wave via Botsi; not a single test and not folded into any range. It goes against this pattern: Apple removed Cal AI partly for this layout, so don't defend it with this figure |
| 8. Trial terms and a dated timeline | Trial sign-ups | +23% | 1 (onboarding #1) | strong | off-target (in-app, Blinkist); no web test |
| 8. Trial terms and a dated timeline | Complaints | −55% | 1 (onboarding #1) | strong | off-target (in-app); same test as the row above |
| 9. Plans that compare honestly | Conversion, denominator not stated | +50% | 1 (#W14) | directional | bundled (screen order, monthly plan made more visible, Apple Pay made primary); A/B on one ad set; at scale (before/after) +40% |
| 9. Plans that compare honestly | Revenue (blended) | +40% | 1 (#W14) | directional | bundled as above; ARPPU dropped (no figure); at scale (before/after) +30% |
| 10. No fake urgency | — | no published range | — | — | only cases and rules; #W15 (countdown in a bundle) has no baseline number |
| 11. Wallets first | Checkout conversion (Stripe, per checkout session) | +10% to +22.3% | 3 (#W20, #W21, #W19) | strong | off-target (cross-business, mostly not subscription apps). #W19 Apple Pay +22.3% (eligible checkouts); #W20 Apple Pay +10% (earlier, separate test); #W21 Link saved details +14% (businesses with many returning customers) |
| 11. Wallets first | Lower-funnel conversion, denominator not stated | +5% | 1 (#W29) | directional | off-target (e-commerce, Shop Pay presence); vendor-commissioned, no sample. Same row: "up to 50%" vs guest checkout, ≥10% vs other accelerated checkouts |
| 11. Wallets first | Conversion, denominator not stated | +50% | 1 (#W14) | directional | bundled (Apple Pay made primary + screen order + plan visibility); at scale (before/after) +40% |
| 11. Wallets first | Revenue | +22.5% to +40% | 2 (#W19, #W14) | strong | #W19 off-target (cross-business, Apple Pay); #W14 bundled, blended revenue |
| 12. Local methods and currency | Checkout conversion (Stripe, per checkout session) | neutral to +47% | 1 (#W19; 5 method results) | strong | off-target (cross-business). PayPal in Germany +47% (digital media), Konbini Japan +27% (digital apps), SEPA Debit +12%, Cash App US +5% (digital games), ACH/pre-authorised debit neutral. Any extra method beyond cards +7.4% |
| 12. Local methods and currency | Revenue | +12% to +17.8% | 2 (#W19, #W17) | strong | off-target (cross-business). #W19 any extra method beyond cards +12%; #W17 local currency, international revenue only, +17.8% |
| 13. Email and payment only | Purchasing customers | +45% | 1 (#W33) | directional | off-target (e-commerce retailer); before/after; optional account instead of "Register" |
| 13. Email and payment only | Users reaching payment (extra phone-number field at web sign-up) | about −30% | 1 (#W63) | anecdotal | forum post; a field added, not removed; no sample or control stated |
| 13. Email and payment only | Checkout conversion, baseline and denominator not stated | 2.5× (+150%; body says 2–2.5×) | 1 (#W23) | directional | bundled (payment provider switched + ZIP and full name removed); before/after |
| 14. Consent at the button, by market | — | no published range | — | — | only rules, a settlement and observed |
| 15. A decline screen that keeps the sale | Failed transactions recovered (a rate, not a lift) | ~20% of failed transactions | 1 (#W24) | directional | first week only; base count not disclosed; no control |
| 16. Risk reversal stated plainly | — | no published range | — | — | only observed and a pending case |
| 17. Post-purchase upsells done right | — | no published range | 0 | — | #W32 (SamCart) left out: off-target, comparison basis not stated |
| 18. Confirmation that a reminder could replace | — | no published range | — | — | only card-network rules |
| 19. Into the app without a password | Day-0 logins | 2× (+100%) | 1 (#W34) | directional | off-target (apartment search, Apartment List); vendor; no baseline, window or control |
| 19. Into the app without a password | Web-to-app transfer of highest-value users | 10× | 1 (#W34) | directional | as above |
| 19. Into the app without a password | LTV | +30% | 1 (#W34) | directional | as above |
| 19. Into the app without a password | Sign-ups | +19% to +80% | 2 (#W36, #W35) | strong | off-target (Android sign-in hints, not post-purchase). #W35 Todoist +80% (also download → sign-up "about +6–7%"); #W36 Komoot +19%; no samples |
| 19. Into the app without a password | Login abandonment / manual sign-in failures | −50% to −87.5% | 2 results in 1 row (#W36: Mobills −50%; Ticketmaster 40% → 5%, computed −87.5%) | directional | off-target (Android); method not stated |
| 19. Into the app without a password | New-user sign-ups, metric not defined | 12.5× (6% → 75%; computed +1,150%) | 1 (#W37) | directional | off-target (in-app, social logins incl. Sign in with Apple); vendor summary |
| 20. Offer web beside IAP, don't replace it | *Web beside IAP vs IAP only:* initial conversion, per customer in arm | −13.0% (computed; 27.0% → 23.5%) | 1 (#W39 C vs B) | strong | reader app (Dipsea), US; ~3,100 per arm; web annual 30% cheaper |
| 20. Offer web beside IAP, don't replace it | *Beside:* conversion to paying, per customer in arm | −6.3% (computed; 6.3% → 5.9%) | 1 (#W39 C vs B) | strong | reader app |
| 20. Offer web beside IAP, don't replace it | *Beside:* conversion to paying, denominator not stated | −5.1% (7.8% → 7.4%; text says −6%) | 1 (#W40) | directional | possibly a later read of #W39, not merged; text and table disagree |
| 20. Offer web beside IAP, don't replace it | *Beside:* conversion, denominator not stated | "0% drop" ("a slight uplift") | 1 (#W45) | directional | bundled (Apple Pay-only web checkout, email/country/ZIP only); a few days of data |
| 20. Offer web beside IAP, don't replace it | *Beside:* trial → paid, per completed trial | +12.8% (computed; 25.0% → 28.2%) | 1 (#W39 C vs B) | strong | reader app |
| 20. Offer web beside IAP, don't replace it | *Beside:* revenue per customer in arm | −17.4% (computed; $2.98 → $2.46) | 1 (#W39 C vs B) | strong | reader app; gross revenue |
| 20. Offer web beside IAP, don't replace it | *Beside:* revenue, denominator not stated | +25% (est) | 1 (#W45) | directional | estimate after a few days; bundled as above |
| 20. Offer web beside IAP, don't replace it | *Beside:* ARPU, not defined | ~+20% | 1 (#W46) | directional | Hily, US iOS; attributed to renewals and lower fees (not split); A/B results not reported |
| 20. Offer web beside IAP, don't replace it | *Beside:* subscribers set to renew (counts) | +119% (46 → 101; text says +170%) | 1 (#W40) | directional | method and sample not stated |
| 20. Offer web beside IAP, don't replace it | *Beside:* churned subscribers (counts) | −14.0% (computed; 121 → 104) | 1 (#W40) | directional | method and sample not stated |
| 20. Offer web beside IAP, don't replace it | *Beside:* refunded customers (counts) | +35.7% (28 → 38) | 1 (#W40) | directional | method and sample not stated |
| 20. Offer web beside IAP, don't replace it | *Web instead of IAP:* initial conversion, per customer in arm | −33.0% (computed; 27.0% → 18.1%) | 1 (#W39 D vs B) | strong | reader app; web-only is not open to non-reader apps |
| 20. Offer web beside IAP, don't replace it | *Instead:* initial conversion, per CTA tap | −37.4% (computed; 70.9% → 44.4%) | 1 (#W39) | strong | reader app; taps on the paywall were about equal (~50% vs 52%) |
| 20. Offer web beside IAP, don't replace it | *Instead:* initial conversion, denominator not stated | −11.9% | 1 (#W41) | directional | Superwall cross-app; sample and period not given. #W54 indie utility moved the paywall to Stripe and reverted: "small conversion dip" that cost more than the fee saved, loss, no figure |
| 20. Offer web beside IAP, don't replace it | *Instead:* paywall conversion, denominator not stated (in-app checkout vs link-out) | −42% | 1 (#W61) | directional | talk summary (Growth Gems), original not opened; not merged with #W41 (different source and wording) |
| 20. Offer web beside IAP, don't replace it | *Instead:* trial → paid, denominator not stated | +27 to +54 percentage points (one test, as reported) | 1 (#W61) | directional | points, not percent; same test as the row above: fewer start, more of them pay |
| 20. Offer web beside IAP, don't replace it | *Instead:* net revenue after fees, denominator not stated | +20% | 1 (#W60) | anecdotal | forum post, cohort comparison (first subscription only); conversion "slightly higher", no figure |
| 20. Offer web beside IAP, don't replace it | *Instead:* conversion to paying, per customer in arm | −15.9% (computed; 6.3% → 5.3%) | 1 (#W39 D vs B) | strong | reader app |
| 20. Offer web beside IAP, don't replace it | *Instead:* purchase per paywall view | −26% to +55% | 2 (#W42, #W43) | directional | sign flips. #W42 4.95% → 3.69% (−26%), not a 50/50 test; #W43 2.54% → 3.93% (+55%), language app, reverted |
| 20. Offer web beside IAP, don't replace it | *Instead:* trial → paid, per completed trial | +5.2% (computed; 25.0% → 26.3%) | 1 (#W39 D vs B) | strong | reader app |
| 20. Offer web beside IAP, don't replace it | *Instead:* trial conversion, denominator not stated | +4.1% (computed; 5.80% → 6.04%) | 1 (#W43) | directional | language app; no sample |
| 20. Offer web beside IAP, don't replace it | *Instead:* revenue per customer in arm | −29.9% (computed; $2.98 → $2.09) | 1 (#W39 D vs B) | strong | reader app; gross revenue |
| 20. Offer web beside IAP, don't replace it | *Instead:* ARPU per paywall viewer | −9% to +53% | 2 (#W43, #W42) | directional | net of fees, so the fee tier drives it (#W42 30% tier, +53%, article also says 47%; #W43 15% tier, −9%) |
| 20. Offer web beside IAP, don't replace it | *Instead:* ARPPU | −20% to +100% | 2 (#W43, #W42) | directional | #W42 $23.76 → $47.59 (computed +100%); #W43 $65.99 → $52.83 (−20%) |
| 21. Placement decides the web paywall's rate | Conversion per paywall view, each placement vs post-onboarding (3.38%) | −74.3% to −14.2% (computed) | 1 (#W44; 3 placements) | directional | AI companion app; no sample; placements reach different users. Last-chance 2.90% (−14.2%), mid-funnel 2.18% (−35.5%), contextual upsell 0.87% (−74.3%) |
| 21. Placement decides the web paywall's rate | ARPU per paywall view, each placement vs post-onboarding ($2.55) | −61.6% to +79.2% (computed) | 1 (#W44; 3 placements) | directional | sign flips: last-chance offer $4.57 (+79.2%), mid-funnel $1.69 (−33.7%), contextual upsell $0.98 (−61.6%) |
| 22. Compliance flags | — | no published range | — | — | flags, not a change to test; only rules and cases |

## Checks

- Patterns: 22. With at least one range: 14 (1, 2, 3, 4, 8, 9, 11, 12, 13, 15, 17, 19, 20, 21). Pattern 15 has only a recovery rate, not a lift; 17's take rate is also a rate. Without a range: 8 (5, 6, 7, 10, 14, 16, 18, 22).
- Records covered: #W1–#W63 (deep sweep 2026-10-31 added #W54–#W63: #W60, #W61, #W63 in rows; #W56 as an aggregate line; #W54 noted in a Caveat).
- Excluded on purpose:
  - #W55 three welcome screens, each matched to a different ad creative (58.3% / 41.3% / 53.7% reach the second screen): rates per arm with different traffic behind each, no control, so not a lift. Supports pattern 1 as direction only.
  - #W57 free trial → $6.99 paid intro week (LTV +30%) and #W62 Sumizeit card-required 7-day trial → two free summaries with no card (net revenue per visitor about +22%, strong; more sign-ups on the card trial, ~60% fake or failed cards, no figure): not mapped. Both change the offer itself, and no pattern here covers the offer type (pattern 8 is about how trial terms are shown).
  - #W58 personalised coupon with a countdown (+15%): vendor figure across clients, tests not shown, and bundled (discount + personalisation + timer), so the timer can't be credited. Pattern 10 stays rules-only; never reward urgency.
  - #W59 Shmoody whole web funnel rebuilt from templates (+41% payment conversion within a week): before/after and bundled; no single pattern.
  - #W3 page speed: observational (commissioned by Google), not a test of a change.
  - #W4, #W16, #W26, #W49, #W51, #W52: marked "not a test" (vendor aggregates).
  - #W6: no lift on a stated metric; its "acquisition cost 30% lower" is a cost figure for an unisolated change. #W34's CPI −15% left out for the same reason (acquisition cost, not a screen outcome).
  - #W8 YNAB product-tour page (+85%): a landing content change, not ad matching; no pattern here covers it.
  - #W10: randomized, but direction only, no effect sizes.
  - #W11: the 51-step win has no number; the segment share 35% → 80% is not a conversion lift.
  - #W15, #W18: no baseline number / share of revenue, not a lift; #W18 is before/after and bundled.
  - #W22 Payment Element +10.5% revenue: matched observational comparison of businesses, not an A/B.
  - #W25: payment-provider fallback and retries (not a screen change), bundled; rates without a control.
  - #W27, #W28: benchmark / observed.
  - #W30 upsell LTV (+20%, ×2, >200%): self-selected with-vs-without comparison, figures contradict each other. #W31: share of revenue, not a lift; whole move bundled.
  - #W38, #W50: anecdotal. #W13: observed.
  - #W45 left out of pattern 11 on purpose: its "0% drop" measures adding the web button, not wallet vs card; it sits under pattern 20.
  - #W47 Fortnite: share of players choosing each option, not a lift; a game, incentive bundled.
  - #W48 Paddle: vendor bands ("average 5–12% decline"), a benchmark-style aggregate, not a test.
  - #W44's "web paywall variant on the main placement 5.54% vs 3.38%": a paywall design A/B with no stated change, not a placement result.
  - Dipsea and Superwall proceeds and take-home figures: fee modelling, background only (not a screen outcome).
  - iDEAL +39% and BLIK +46% appear only in Part 2 (B6), not in the #W19 row, so they are not used.
