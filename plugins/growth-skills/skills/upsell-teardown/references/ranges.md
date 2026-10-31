# Ranges seen in published tests

How to read: the lowest and highest measured lift in published tests of this kind of change, on one metric, with the number of tests. Seen in other apps' tests; not a forecast for your app. Built only from Part 1 rows of `evidence.md`; never averaged.

| Pattern | Metric | Range seen | Tests | Strongest tier | Caveats |
|---|---|---|---|---|---|
| 1. Gate the feature at the moment it's wanted (contextual gate) | Conversion to paid / subscription registrations | +8% to +28% | 2 (#U1, #U2) | strong | #U1 compares two benefit framings on the same gate, not gate vs no gate (Android); #U2 reported after rollout, baseline unclear |
| 1. ... | Trial starts | about 3x (about +200%) | 1 (#U6) | directional | year-over-year; contextual trial popup (same as onboarding #46) |
| 1. ... | Conversion (denominator not stated) | about −7% | 1 (#U6) | directional | year-over-year; same test as the trial-start row: more trials, lower conversion |
| 1. ... | Usage of the gated mode | +9.7% | 1 (#U1) | strong | compares two gate designs |
| 2. Limit-reached upsell | — | no published range | — | — | only a conversion rate with no comparison (#U10: 10% after the 40 free minutes, bundled) and an anonymised benchmark band (Adapty A/B library, Part 2) |
| 3. Upsell after a success moment | Conversion | +50% to +81% | 2 (#U5, #U37) | directional | #U5 bundled with onboarding paywall tests; #U37 vendor-reported, cut prompt volume ~50% at the same time as retiming |
| 3. ... | Revenue / LTV | +20% to +50% | 2 (#U20, #U37) | directional | #U20 off-target (puzzle game, revenue during peak periods only); both vendor-reported (ContextSDK), no method |
| 4. Never block the core habit | Engagement (listening hours) | −2.08% per extra ad per hour | 1 (#U13) | strong | off-target: ad load in music streaming, not a feature gate; long-run effect about 3x the one-month estimate. Paid conversion rose, effect size not reported. #U61 Lose It!: upsell messages during food logging (vs after) hurt attrition and conversion, loss, no figure (podcast) |
| 4. ... | Active users (weekly) | about −2% | 1 (#U13) | strong | off-target (as above); highest-load arm vs control |
| 5. Show the meter before the wall | — | no published range | — | — | only observed |
| 6. Soft gate: preview, blur or partial result | — | no published range | — | — | only anecdotal (#U17, no figure); Adapty hard vs soft (#U16) is a close-button benchmark, not this change |
| 7. A free way past the wall | Revenue | +158% | 1 (#U12) | directional | year-over-year, no control; three access tiers launched together with the ad option |
| 7. ... | ARPPU | +98% | 1 (#U12) | directional | as above |
| 7. ... | Paying users | +30% | 1 (#U12) | directional | as above |
| 7. ... | Conversion (denominator not stated) | 0.08% → 1.2% (+1,400%, computed) | 1 (#U12) | directional | as above |
| 8. Size the free tier on value, and price the engagement cost | Conversion to paid / subscriptions (tighter free tier) | +18% to +83% | 4 (#U7, #U8, #U9, #U63) | strong | #U8 off-target (mobile game); #U9 off-target (web news meter); #U7 is power-user conversion; #U63 Sumizeit is the 1-free-summary arm of an A/B/C vs control (directional); its looser arm (20+ free, no daily limit) was "only marginally better", null, no figure. #U60 Lose It! locked all macro features: users angry, "not worth that much money", loss, no figure |
| 8. ... | Subscriber conversion (looser: move to freemium) | more than −50% | 1 (#U15) | directional | anonymous app, reverted after a couple of weeks; a model switch |
| 8. ... | Download → paid (looser: hard paywall → freemium) | 20% → 9% (−55%, computed) | 1 (#U57) | directional | before/after, model switch (Opal); DAU and revenue growth claimed, no figures. #U56 Zing Coach (hard, no trial → soft with trial): start rate down "a couple of points", user base grew, no figures |
| 8. ... | Conversions, denominator not stated (tighter: switch to hard paywall) | about +25% | 1 (#U52) | directional | before/after, shipped by accident (Stronger); social sharing fell, no figure; a model switch |
| 8. ... | Trial starts (count cap → gate on the value feature) | about +400% trial sign-ups; sign-up → trial 3% → 15% (+400%, computed) | 1 (#U11) | directional | bundled: gate type and placement changed together (shown in onboarding); before/after |
| 8. ... | Retention (free D30) | +70% | 1 (#U10) | directional | bundled (free tier, paywall placement and design changed over 8 months) |
| 8. ... | Engagement (content demand / listening time) | −9.9% to +100% (2x) | 2 (#U9, #U10) | directional | sign flips: tighter meter cut demand (#U9, web); a value-based weekly allowance doubled free listening (#U10, bundled) |
| 9. Name the blocked task in the headline | Conversion to paid / upgrades | +22% to +28% | 2 (#U1, #U3) | strong | #U3 no baseline, product spans web/desktop/mobile; #U1 Android |
| 9. ... | Annual plan purchases | +4% | 1 (#U3) | directional | no baseline |
| 9. ... | Revenue (incremental annual upgrade revenue) | more than +20% | 1 (#U3) | directional | growth "by 2024", not a test arm |
| 10. Say what the higher tier adds, in units | — | no published range | — | — | only store rules |
| 11. Full price, period and when the charge happens | — | no published range | — | — | only store rules and guidance |
| 12. One clear decline, no pressure | — | no published range | — | — | only legal cases and observed (countdowns on ≤1.4% of paywalls). #U64 BoldVoice removed the paywall close button: trial starts up, refunds up by more than the gain, loss, no figure (podcast) |
| 13. One upsell per trigger, decline respected | Conversion | +50% to +81% | 2 (#U36, #U37) | directional | the two changes go opposite ways: #U36 showed the offer more often (every 21st vs 49th session, likely before/after); #U37 showed prompts ~50% less often at better moments (vendor-reported) |
| 13. ... | LTV | +20% | 1 (#U37) | directional | vendor-reported, no method |
| 14. Second-chance offers: position decides | Revenue, denominator not stated (promotional offer moved from day one to day five) | +17% | 1 (#U54) | strong | Pregnancy+; compared with the day-one offer, not with no offer; sample not given. #U44 (anonymised vendor band) is not a test and is left out; position flips the sign (see patterns.md) |
| 14. ... | Revenue per user, denominator not stated (day-30 discount to trial users who didn't convert) | +87% | 1 (#U55) | directional | Mojo; design and comparison not stated. #U65 BoldVoice: an unclosable discount after dismissing looked strong on trial starts, lost once refunds were counted, loss, no figure |
| 15. Upgrade screen, never the subscribe paywall | — | no published range | — | — | only Apple rules and guidance |
| 16. Annual switch for happy monthly subscribers | Conversions (daily) | −20% | 1 (#U28) | directional | off-target change: annual-only offer to all users for one week, not a switch offer to payers; no control named |
| 16. ... | Revenue per day | +32% | 1 (#U28) | directional | as above; baseline not named |
| 17. Tier ladder, decoy and lifetime anchor | Total initial conversions | about +10% | 1 (#U22) | strong | lifetime shown next to annual on the paywall, not to existing subscribers |
| 17. ... | Conversions by plan | −30% (annual) to +266% (lifetime) | 1 (#U22) | strong | one test, two plans: lifetime cannibalises annual |
| 17. ... | Revenue / ARPU | +6% to +21.5% | 2 (#U23, #U25) | strong | #U23 off-target (web books; revenue of the middle option: +8.9% with a premium tier, +21.5% with a similar-priced option); #U25 company-reported year-over-year tier shift, not a test. #U53 Glam AI: the decoy layout that won on the main paywall did nothing on inner paywalls, null, no figure |
| 17. ... | Higher-tier share of new subscribers (top tier offered instead of the middle one) | "doubled" (about 2x) | 1 (#U58) | directional | Life360 podcast; a model picks high-propensity new users for the Platinum offer; no Gold subscribers lost; design not stated |
| 18. Family plan offer | — | no published range | — | — | only a company-reported share (#U24, not a test) |
| 19. Store mechanics in the copy | — | no published range | — | — | only store rules |
| 20. Allowance in the plan, credits as a top-up for subscribers | New subscription revenue | +14% | 1 (#U32) | strong | no baseline; paywall drop-off and AI cost showed no significant rise |
| 20. ... | Conversion (denominator not stated) | 8.3% → 15.0% (+81%, computed) | 1 (#U33) | directional | bundled: credit-pack hard paywall → trial plus higher weekly price; sequential campaigns |
| 21. Credit packs priced in real money | — | no published range | — | — | only store rules and guidance |
| 22. Plan status surface | Revenue (persistent "Buy now" upgrade button added) | +10% to +20% (one test, reported as a band) | 1 (#U62) | directional | Avast (security); net of cannibalisation; design and placement not stated. Adapty library band (Part 2) left out |
| 23. Trial and reverse-trial countdown with usage | Trial starts (adoption) | +11.1% | 1 (#U45) | strong | off-target: freemium image-editing SaaS, surface not stated; tests 7-day vs 3-day trial length, not the countdown screen |
| 23. ... | Conversion to paid | +7.3% (immediate, not significant) to +42.4% (delayed) | 1 (#U45) | strong | as above; one test, two time windows |

## Checks

- Patterns: 24. With a range: 13 (1, 3, 4, 7, 8, 9, 13, 14, 16, 17, 20, 22, 23). Without: 11 (2, 5, 6, 10, 11, 12, 15, 18, 19, 21, 24).
- Records covered: #U1–#U66 (deep sweep 2026-10-31 added #U52–#U66).
- 24. Compliance flags: no published range (rules and cases only); not a row in the table above because the pattern is a flag list.
- Excluded on purpose:
  - Benchmarks or "not a test" rows: #U14, #U16, #U18, #U19, #U24, #U34, #U35, #U43.
  - Anecdotal: #U4, #U17, #U21, #U46, #U49.
  - #U10 download-to-paid 7.6x and the 3x trials: whole 8-month programme and a paywall move, not a free-tier change. Only the free-tier retention and listening figures are used (flagged bundled).
  - #U9 net revenue (+$230,000): absolute amount, no baseline.
  - #U13 paid subscriptions: direction only, no effect size.
  - #U26 ABBYY and #U27 Superwall default: first-paywall layout and default plan, not an upsell pattern in this library.
  - #U29 Uscreen: compares cash against a projected baseline. #U30 Churnkey: observational matched pairs. #U31: acceptance rates, no lift and not causal.
  - #U38–#U42 (Splice, Lifesum, Headspace, Fishbrain, Blinkist): messaging and CRM programmes measured against history, unexposed groups or nothing; they test channels, not a screen pattern here.
  - #U47 Lumosity: the 11% compares recipients with non-recipients (assignment not stated); engagement figures compare with the prior year's single email.
  - #U48 Dropbox: "10–40%" is a secondhand range from one person's experience, not a measured test.
  - #U50 Outseta: model switch (card-required trial vs freemium, web SaaS), not a screen pattern here.
  - #U51 crypto tracker (added 2026-10-31): a bundled redesign of a promotional sale paywall for free users, method not stated; no single pattern here.
  - Losses and nulls with no figure (noted in the rows' Caveats so the file shows what didn't work): #U53 (17), #U56 (8), #U60 (8), #U61 (4), #U63 looser arm (8), #U64 (12), #U65 (14).
  - #U66 e-book field experiment (free → paid, with vs without a bonus feature for payers): no rates in the summary; the bonus lowered subscriptions under a hard switch and slightly raised them under a soft one. Not mapped: a payer bonus during a model switch, no figure.
  - #U59 Lose It! email vs in-app message (about 10x revenue per eligible user): a channel comparison for the same offer, not a screen pattern here (as #U38–#U42).
  - Adapty A/B library bands cited in patterns 1, 2, 17, 20, 22 (daily-limit +50–60%, relevant-action trigger, paywall tab, lifetime +10–15%, mixed cross-placement): Part 2 rows, not used.
