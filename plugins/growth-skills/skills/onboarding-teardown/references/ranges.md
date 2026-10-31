# Ranges seen in published tests

How to read: the lowest and highest measured lift in published tests of this kind of change, on one metric, with the number of tests. Seen in other apps' tests; not a forecast for your app. Built only from Part 1 rows of `evidence.md` (sections A and B, tests #1–#167); never averaged. Second reports of one test (#143 = #3, #159 = #71) are cited next to the original and never counted as another test.

- Rows marked **aggregate** come from section E of `evidence.md` (Adapty's A/B library summarised in paywall-ab-test-assistant). They are kept on their own line and never folded into a test range.
- "(computed)" means `evidence.md` gives two absolute rates and the relative change was worked out from them; both rates are shown.
- "pp" is a percentage-point change with no usable baseline; it is not converted.
- Where the metric says "as reported", the source doesn't say whether it means trial starts, trial-to-paid or purchase per view. Don't compare it with a named metric.
- When a pattern can be added or removed (loader, flow length), the direction of the change is written in the Metric column.

| Pattern | Metric | Range seen | Tests | Strongest tier | Caveats |
|---|---|---|---|---|---|
| 1. Value promise on screen 1 | Conversion to purchase | +30% | 1 (#17) | strong | bundled (shorter copy + value proposition + testimonials); sample size not given |
| 2. Outcome copy over feature copy | Trial starts | about +10% | 1 (#2) | strong | bundled (JTBD rebuild) |
| 2. Outcome copy over feature copy | Trial conversion (as reported) | about +14% to +17% | 2 (#2, #11) | strong | #2 bundled; #11 anonymised, no method |
| 2. Outcome copy over feature copy | Conversion to paid | +39% to "+54% or more" | 2 (#19, #58) | directional | #19 conference talk (landing → paid); #58 is paywall copy, bucket n/a |
| 2. Outcome copy over feature copy | ARPU | +13% to +20% | 2 (#11, #2) | strong | #2 bundled |
| 3. Goal or intent question early | Trial starts | +8.5% to +25% | 2 (#13, #12) | directional | both bundled (#13 with a loader vs generic demos; #12 with a trial lesson) |
| 3. Goal or intent question early | Trial conversion (as reported) | about +10% | 1 (#4) | directional | interview, no method; multi-select vs single-select |
| 3. Goal or intent question early | Conversion to paid | +17% | 1 (#13) | directional | bundled; global figure (US segment of the same test: +27%) |
| 3. Goal or intent question early | ARPU | +22% to +78% | 2 (#13, #12) | directional | both bundled; #13 global (US: +35%) |
| 3. Goal or intent question early | Conversion (as reported), "How did you hear about us?" question added | about +10% | 1 (#134) | directional | attribution question, not a goal question; whether the answer changed later screens not stated; design not stated |
| 3. Goal or intent question early | Course starts | +7.6 pp | 1 (#3) | strong | quiz vs no quiz on the same course; pp only |
| 3. Goal or intent question early | Course starts | +101.5% (computed; 31.25% → 62.97%) | 1 (#3) | strong | "perceived fit" arm: quiz + a different default course vs a breathing exercise, so bundled; #143 is a second report of this test (63% vs 31%), not counted again |
| 3. Goal or intent question early | Active meditation days | no significant change | 1 (#3) | strong | null result: starts rose, use did not |
| 3. Goal or intent question early | Conversion (aggregate) | +8% to +17% | E8 | aggregate | many Adapty tests summarised, not one test |
| 3. Goal or intent question early | ARPU (aggregate) | +13% to +35% | E8 | aggregate | many Adapty tests summarised, not one test |
| 4. "Why we ask" microcopy and reassurance | — | no published range | — | — | only observed |
| 5. Level or placement step | — | no published range | — | — | only observed |
| 6. Flow length fits the category | Payment conversion (long onboarding vs none) | +40% | 1 (#14) | directional | iOS figure; anonymised |
| 6. Flow length fits the category | Conversion to paid (shorter vs long) | −13% to +8% | 2 (#14, #140) | directional | sign flips: #14 shortened version lost; #140 simplified carousel beat long-form content onboarding (the page labels the control inconsistently). #133 short onboarding "seems to be outperforming", no figure, early read |
| 6. Flow length fits the category | Trial starts (shorter vs long) | +2.5% | 1 (#140) | directional | simplified carousel vs long-form content; control labels inconsistent |
| 6. Flow length fits the category | Trial starts (longer vs shorter) | +16% | 1 (#147) | directional | founder report; bundled (flow doubled to 15 screens and made more personal). #160 longer onboarding "up double digits" on trial take, no figure |
| 6. Flow length fits the category | ARPU (long onboarding vs none) | +20% | 1 (#14) | directional | — |
| 7. Progress and chapters | Form conversion | "15+%" | 1 (#29) | directional | a form split into 3 screens, not a progress indicator |
| 8. Relate-to-statement cards | — | no published range | — | — | only observed |
| 9. First result before the paywall | Trial starts | +25% | 1 (#12) | directional | bundled (survey + trial lesson) |
| 9. First result before the paywall | ARPU | +78% | 1 (#12) | directional | bundled (survey + trial lesson) |
| 9. First result before the paywall | DAU | about +20% | 1 (#5) | strong | off-target: registration wall, not a paywall; self-reported |
| 9. First result before the paywall | Sign-ups | +15% to +20% (one test, stated as a range) | 1 (#28) | directional | web |
| 9. First result before the paywall | Engagement per step | +4% | 1 (#77) | directional | "Play a song" first; conversion up, no figure |
| 10. Personal plan reveal that echoes answers | Course starts | +101.5% (computed; 31.25% → 62.97%) | 1 (#3) | strong | "perceived fit" arm, bundled (quiz + course choice) |
| 10. Personal plan reveal that echoes answers | Trial starts | +8.5% | 1 (#13) | directional | bundled (questions + "customising" screen vs generic demos) |
| 10. Personal plan reveal that echoes answers | Conversion to paid | "+10%+" to +17% | 2 (#27, #13) | directional | #27 number has no source (abtest.design says 10–20%); #13 bundled, global (US: +27%) |
| 10. Personal plan reveal that echoes answers | ARPU | +22% | 1 (#13) | directional | bundled; global (US: +35%) |
| 11. Outcome projection or quantified problem | Download → trial start | +143% (computed; about 7% → about 17%) | 1 (#8) | directional | cumulative over many iterations, not one change |
| 11. Outcome projection or quantified problem | Conversion to test sign-up | +50% (35% → 52%) | 1 (#37) | directional | bundled (quiz reorder + results screen); method not stated; diagnostic test sign-up, not a subscription |
| 12. Endowment: the user builds something | — | no published range | — | — | only observed |
| 13. Real-data reveal | Account linking / link conversion | about +11% to +251% | 3 (#36, #35, #34) | directional | all test the linking step, not the reveal screen; #34 cumulative over about 65 iterations (+40% after 4 weeks); #35 provider switch; #36 vendor tests across many apps, part mobile web |
| 13. Real-data reveal | Accounts funded | +19% | 1 (#35) | directional | provider switch |
| 14. Social proof before the ask | Conversion to paid | +30% to +44% | 2 (#17, #60) | strong | #17 bundled (testimonials one of three changes) |
| 14. Social proof before the ask | Trial starts | about +10% | 1 (#2) | strong | bundled (testimonials moved earlier inside a JTBD rebuild) |
| 14. Social proof before the ask | Trial conversion (as reported) | about +14% | 1 (#2) | strong | bundled |
| 14. Social proof before the ask | ARPU | +20% | 1 (#2) | strong | bundled |
| 14. Social proof before the ask | Install → trial (second paywall leads with a results statistic) | +72% | 1 (#152) | directional | design not stated; "86% improved their diet" on a second paywall |
| 14. Social proof before the ask | Conversion (as reported), social-proof video on the plan picker | no change (2.54% vs 2.43%, called noise) | 1 (#106) | directional | null; which figure belongs to which arm not stated, so no lift computed |
| 14. Social proof before the ask | Free-trial survival or free-to-paid (unclear) | +3% | 1 (#49) | directional | in-session messages, not before the paywall; metric ambiguous |
| 15. Commitment device | Retention D30 | doubled | 1 (#25) | directional | bucket n/a (sustainability app) |
| 15. Commitment device | Retention D14 | +3.3% | 1 (#74) | strong | off-target: post-onboarding streak change (a less demanding goal) |
| 15. Commitment device | App opens | +7.5% | 1 (#3) | strong | precommitment arm |
| 15. Commitment device | Active days | +4% unique open days; no significant change in meditation days | 1 (#3) | strong | precommitment arm; null on meditation days |
| 15. Commitment device | Learners on a streak | +10.5% (+19% for new learners) | 1 (#74) | strong | off-target: post-onboarding; fewer users hit their daily goal |
| 16. Account timing | DAU | +8.2% to about +20% | 2 (#6, #5) | strong | self-reported; #6 is combined wall optimisation (wording + soft/hard walls) |
| 16. Account timing | Creator enrolment | +25% | 1 (#33) | directional | delayed bank-account (KYC) step, not sign-up |
| 16. Account timing | Onboarding drop-off (login moved from the start to after the paywall) | "eliminated a 10% drop-off" (relative or points not stated) | 1 (#148) | directional | founder report; check the restore path (pattern trap) |
| 16. Account timing | Trial start rate | +37% | 1 (#135) | directional | before/after, bundled (welcome screen + simpler sign-up + permission prompts spaced out); same row under 17 |
| 17. Permissions in context, with a preview | Push opt-in | +1133% (computed; 6% → 74%) | 1 (#1) | strong | bundled with the trial-timeline paywall |
| 17. Permissions in context, with a preview | ATT opt-in (prompt moved earlier: first open or start of onboarding) | +62.5% to +150% (computed; 8% → 13% and about 6% → 15%) | 2 (#130, #129) | directional | design not stated; both from one speaker's talk. Earlier, not in context: runs against this pattern's "ask when the feature needs it". #164 (same speaker, ATT at first launch: "the least impact on anything", no figures) may describe one of these tests. #136 an explainer before the ATT prompt did not grow conversions, no figure |
| 17. Permissions in context, with a preview | Onboarding completion and trial starts (ATT at the start of onboarding) | no change | 1 (#130) | directional | null on the money metrics while opt-in rose |
| 17. Permissions in context, with a preview | Trial start rate | +37% | 1 (#135) | directional | before/after, bundled (welcome screen + simpler sign-up + prompts spaced out) |
| 18. Reminder setup inside onboarding | Trial conversion (as reported) | +6.4% | 1 (#16) | directional | anonymised, no method |
| 18. Reminder setup inside onboarding | ARPU | +24% | 1 (#16) | directional | anonymised, no method |
| 19. Loader or "building your plan" screen | Trial conversion (loader removed) | +22% | 1 (#15) | directional | anonymised |
| 19. Loader or "building your plan" screen | ARPU (loader removed) | +30% | 1 (#15) | directional | anonymised |
| 19. Loader or "building your plan" screen | Trial starts (questions + loader added) | +8.5% | 1 (#13) | directional | bundled with personalisation questions |
| 19. Loader or "building your plan" screen | Conversion to paid (questions + loader added) | +17% | 1 (#13) | directional | bundled; global (US: +27%) |
| 19. Loader or "building your plan" screen | ARPU (questions + loader added) | +22% | 1 (#13) | directional | bundled; global (US: +35%) |
| 19. Loader or "building your plan" screen | ARPU (loader + personalised-plan screen, aggregate) | around −50% | E1 | aggregate | one flow in Adapty's library; sign flips against #13 |
| 20. Escape hatches for heavy steps | Creator enrolment | +25% | 1 (#33) | directional | delayed KYC step |
| 21. Sensible defaults instead of setup | — | no published range | 0 | — | #32 left out: cited source does not match |
| 22. Paywall position | Trial starts (paywall earlier) | about +10% to +300% (computed for #151; about 2% → 8%) | 3 (#8, #71, #151) | strong | #8 paywall two screens earlier (founder's estimate within a cumulative programme); #71 bundled with a paywall video; #151 trial opt-in, paywall right after welcome vs after home, rates given as "roughly" |
| 22. Paywall position | Trial opt-in (3-slide carousel added before the paywall vs paywall right after welcome) | +87.5% (computed; about 8% → 15%) | 1 (#151) | strong | third arm of the same A/B/C test; rates "roughly"; sample not given |
| 22. Paywall position | Trial-to-paid | unchanged | 1 (#71) | directional | bundled with a video |
| 22. Paywall position | Premium conversions | +16% | 1 (#51) | directional | conflicting numbers; which placement won is unverified |
| 22. Paywall position | Revenue | doubled to 5× | 2 (#71, #72) | directional | #71 bundled; #72 before/after |
| 22. Paywall position | Paywall viewers | +50% | 1 (#71) | directional | bundled; #159 (second report of #71, podcast) gives conversion about +80% and paywall views about 40% → 85% of installs, not counted again |
| 23. Multi-step paywall or pre-paywall | Conversion (as reported) | +16% to +50% | 3 (#56, #55, #23) | strong | #56 metric ambiguous (annual trials or conversion); #23 bundled (context-specific paywalls) |
| 23. Multi-step paywall or pre-paywall | Proceeds / ARPU | +12% to +36% | 2 (#18, #55) | strong | #18 bundled (onboarding changes + split paywall), no controlled comparison stated |
| 23. Multi-step paywall or pre-paywall | Trial conversion (as reported) | +15% | 1 (#18) | directional | bundled |
| 23. Multi-step paywall or pre-paywall | Retention D30 | +18% | 1 (#18) | directional | bundled |
| 23. Multi-step paywall or pre-paywall | Trial opt-in (multi-screen vs single-screen paywall) | +60% | 1 (#157) | directional | design not stated; cancellations lower, no figure |
| 23. Multi-step paywall or pre-paywall | Conversion (as reported), onboarding says the app costs money before the paywall | +3% (relative or points not stated) | 1 (#99) | directional | a price-expectation line anchored to a cost the user already pays, not a separate paywall step; design not stated |
| 24. Trial timeline and reminder promise | Trial starts | +13.6% to +23% | 2 (#97, #1) | strong | #1 timeline + reminder opt-in treated as one change; #97 trial-timeline paywall design, trial-to-paid "not impacted" (no figure) |
| 24. Trial timeline and reminder promise | Revenue (denominator not stated) | +27% | 1 (#116) | strong | timeline (today, day 3, charge day) added to the paywall; sample not given |
| 24. Trial timeline and reminder promise | ARPU (timeline paywall vs trial-toggle paywall) | lost (the toggle arm +19% against it) | 1 (#150) | strong | bundled; the team credits the toggle arm's hierarchy (yearly price per week, "Most Popular"), not the toggle; same test under 26 |
| 24. Trial timeline and reminder promise | In-trial cancels | −4% | 1 (#1) | strong | — |
| 24. Trial timeline and reminder promise | Complaints | −55% | 1 (#1) | strong | — |
| 24. Trial timeline and reminder promise | Push opt-in | +1133% (computed; 6% → 74%) | 1 (#1) | strong | — |
| 24. Trial timeline and reminder promise | Sales | +14% | 1 (#65) | strong | off-target: reminder email, not a screen |
| 24. Trial timeline and reminder promise | LTV | +50% | 1 (#78) | directional | bundled (two-step paywall + timeline); staged rollout, no concurrent control |
| 25. Paywall echoes the onboarding | Trial starts | +183% | 1 (#54) | strong | segments by country, not by answers; pricing changed too |
| 25. Paywall echoes the onboarding | Trial-to-paid | +20% | 1 (#22) | directional | confounded with pricing/product changes |
| 25. Paywall echoes the onboarding | Conversion (as reported) | "+10%+" to +50% | 2 (#27, #23) | directional | #27 number has no source; #23 context-specific paywalls, bundled |
| 25. Paywall echoes the onboarding | MRR | +83% | 1 (#22) | directional | confounded |
| 25. Paywall echoes the onboarding | Paywall conversion (one paywall per user segment) | +9.5% | 1 (#139) | directional | each segment's paywall leads with a different value; design not stated |
| 25. Paywall echoes the onboarding | ARPU (one paywall per user segment) | +13% | 1 (#139) | directional | design not stated |
| 26. Trial structure on the first paywall | Trial starts | +25% | 1 (#45) | strong | one-tap trial quickstart |
| 26. Trial structure on the first paywall | Trial-to-paid | about flat | 1 (#45) | strong | — |
| 26. Trial structure on the first paywall | Trial conversion (as reported) | +7% to +10% | 2 (#57, #21) | strong | #21 bundled (two paywalls, delayed close) |
| 26. Trial structure on the first paywall | Onboarding conversion | +10% | 1 (#21) | directional | bundled |
| 26. Trial structure on the first paywall | Conversion to subscription | +39% to +40.5% | 2 (#41, #52) | strong | denominators differ (#41 per paywall view); #52 +40.5% (computed; weekly 1.63% → weekly + trial 2.29%) |
| 26. Trial structure on the first paywall | Revenue / ARPPU | +5% to +47% | 2 (#41, #48) | strong | #41 revenue per 100 installs +47%, ARPPU +5%; #48 revenue +8%, referral guest pass (30-day vs 14-day trial) |
| 26. Trial structure on the first paywall | Sign-ups | +7% | 1 (#48) | directional | referral guest pass |
| 26. Trial structure on the first paywall | Trial conversion (as reported), opt-in trial vs default | +10% | 1 (#83) | directional | trial starts fell in the same test (no figure): mixed |
| 26. Trial structure on the first paywall | Install-to-trial (short paywall with a trial toggle) | +31% to +72% | 2 (#88, #89) | directional | both bundled redesigns; Apple rejects trial toggles as of February 2026 (per the source) |
| 26. Trial structure on the first paywall | ARPU / revenue (short paywall with a trial toggle) | +17.02% to +64% | 2 (#87, #88) | directional | both bundled redesigns; #88 is revenue, #87 ARPU; trial-toggle caveat as above |
| 26. Trial structure on the first paywall | ARPU (trial-toggle paywall vs trial-timeline paywall) | +19% | 1 (#150) | strong | bundled; the team credits hierarchy (yearly price per week, "Most Popular"), not the toggle; trial-toggle caveat as above |
| 26. Trial structure on the first paywall | Paywall conversion (as reported), 7-day trial added at the same price vs no trial | +131% | 1 (#92) | strong | one of five price arms; sample not given |
| 26. Trial structure on the first paywall | Proceeds per user after trials (trial added vs none) | +78% | 1 (#92) | strong | paying subscribers +45% in the same arm |
| 26. Trial structure on the first paywall | Revenue (denominator not stated), free trial vs discounted intro price | +140% | 1 (#115) | strong | sample not given |
| 26. Trial structure on the first paywall | Install → paid (trial shortened 14 → 7 days) | +8% | 1 (#156) | directional | design not stated. Trial-length tests point both ways with no figures: #154 7 → 14 days lost (reverted), #138 3 vs 7 days "minimal" difference, #145 30-day beat 7-day and no trial on a monthly plan |
| 26. Trial structure on the first paywall | Subscriptions by plan (free trial removed from the monthly plan only) | monthly +2,000%; quarterly +46%; annual +21% | 1 (#149) | directional | per plan, not total; no baseline; design not stated |
| 26. Trial structure on the first paywall | LTV per paying customer (trial removed, six plan tiers) | $35–40 → over $60 (absolute; not converted) | 1 (#155) | directional | before/after; bundled with six tiers; new trials fell to zero (mixed) |
| 27. Second chance after the first paywall | Onboarding conversion; trial conversion | +10%; +10% | 1 (#21) | directional | bundled (early paywall with trial off + second paywall + delayed close) |
| 27. Second chance after the first paywall | Premium conversion (aggregate) | about +25% to +30% | E2 | aggregate | discount right after the onboarding paywall |
| 27. Second chance after the first paywall | ARPU (aggregate) | roughly −50% | E2 | aggregate | same offer after the main in-app paywall: the sign flips with position |
| 28. Dismiss treatment | DAU | +8.2% | 1 (#6) | strong | off-target: sign-up wall, not a paywall |
| 28. Dismiss treatment | Trial conversion (as reported) | +10% | 1 (#21) | directional | bundled (delayed close is one of several changes) |
| 29. No onboarding paywall (freemium, metered, credits) | Conversion to paid | about −7% to +83% | 2 (#46, #63) | directional | #46 year on year, kill-switch rollout; #63 power-user conversion |
| 29. No onboarding paywall (freemium, metered, credits) | Trial starts | about 3× | 1 (#46) | directional | kill-switch rollout, not A/B |
| 30. Compliance flags | — | no published range | — | — | not a test pattern; only platform rules and a risk signal |

## Checks

- Patterns: 30. With a range: 25. Without: 5 (4, 5, 8, 12 only observed; 30 not a test pattern).
- Ranges that rest on bundled or directional rows only: 3, 6, 9, 10, 11, 13, 18, 19, 20, 21, 27, 29 (22 left this list on 2026-10-31: #151 is a strong A/B/C position test). Read these as "this kind of change has moved numbers", not as the size for one isolated change.
- Excluded on purpose:
  - Anecdotal rows: #9, #10, #20, #26, #40, #44, #47, #61, #73; E6 and E7 (anecdotal aggregates).
  - #7 Calm: retention about 3× and 40% vs under 1% compare prompted users with others (holdout implied, no baseline); the row doesn't call it an A/B test.
  - #24 Superwall aggregate (pattern 23): observational, not randomised.
  - #75 transaction-abandon paywalls (pattern 27 trap): cohort comparison and a share of revenue, not a lift.
  - #18 and #56 also contain a trial-timeline or reminder step; they are counted under pattern 23 only, not 24, because the timeline is one part of a multi-step change.
  - Benchmarks (section C) and section D risk signals.
- Rows with numbers that fit no pattern, left out: #30 Mural checklist, #31 conversational tone, #38 YNAB product tour (web, pre-install), #39 Houzz paid-traffic landing, #42–#43, #53, #59, #64 (plan and price presentation), #50 VEED prices upfront vs benefits-only, #62 TIPSTOP trial message + discount badge, #67 Going trial CTA copy, #68–#69 Neos Kosmos paywall visual and copy, #70 Cal AI cumulative programme, #76 Square Invoices form. Added 2026-10-31 and also left out (paywall plan, price, comparison and visual changes; they belong to the paywall mechanics in variant-check): #79 Preu AI, #80 Rash ID, #81 Symmetry, #82 Unchaind, #84 SellRaze, #85 BuyBye, #86 Prosto.
- Rows added beyond what `patterns.md` cites, as the same kind of change: #19 (pattern 2), #13 (pattern 3), #77 (pattern 9), #36 (pattern 13), #74 (pattern 15), #23 (patterns 23 and 25), #27 (pattern 25), #48 (pattern 26), #21 (pattern 28).
- Deep sweep 2026-10-31 (#90–#167), mapped: #134 (3); #140, #147 (6); #106, #152 (14); #135 (16 and 17, one bundled test); #148 (16); #129, #130 (17); #151 (22); #99, #157 (23); #97, #116, #150 (24); #139 (25); #92, #115, #149, #150, #155, #156 (26). #78–#89 from the first sweep were already in (#78 under 24; #83, #87, #88, #89 under 26; #79–#86 left out below).
- Second reports, not counted as tests: #143 (= #3, cited on the #3 course-starts row) and #159 (= #71, cited on the #71 paywall-viewers row).
- Stated losses, nulls or mixed results with no figure (never in a range; listed so the file shows what didn't work): pattern 1/6 #112 web quiz-first funnel ported into the app lost on completion, #113 a welcome screen before it brought completion back but purchases fell; pattern 3/6 #161 a "set a carb goal" step "lost quite badly"; pattern 6 #133 short beat long (early read), #160 longer won "double digits"; pattern 9 #162 premium features shown in onboarding "a lot of times doesn't work"; pattern 17 #136 ATT explainer did not grow conversions, #164 ATT at first launch "the least impact"; pattern 26 #102 long "design your own trial" offer lost, #138 3 vs 7 days minimal, #145 30-day trial won on every metric, #154 7 → 14 days lost, #166 card required for the trial: fewer starts, higher conversion, fewer accounts.
- Deep sweep rows with figures left out because they are paywall plan, price, offer, CTA or visual changes (they belong to the paywall mechanics in variant-check, as #79–#86 above): #90 Planner 5D price tiers, #91 PropGPT weekly price, #94 Stardust discount % and weekly equivalent, #96 Stardust video background, #98 Clear 30 feature carousel → first seven days, #100 comparison chart → simple page, #103 Glam AI video hero, #104 decoy plan, #105 plan order, #107 price for $800+ iPhones, #109 intro offer (0 of 2,500), #111 coupon on Business, #114 button colour, #121 Going Merry CTA + plan emphasis + price, #122 OctaZone 3-month plan, #132 "Subscribe" → "Start your 7-day free trial", #137 Mojo Mexico price cut, #142 TomTom discounted yearly beside the trial, #146 The Economist discount offer (pattern across campaigns), #153 CoinStats animated reveal. With no figure, same reason: #93, #95, #101, #108, #110, #117 (won, no lift figure), #118, #119, #120, #123–#128, #141, #144, #158, #163, #165, #167.
- Not mapped: #131 an unused name field, +13% activation (definition not stated). It is profile data whose answer is never used, which pattern 3 does not count as a goal question and no other pattern covers.

- Left out after review: #32 (cited source does not match) and #66 (business-model switch, not an A/B test).
