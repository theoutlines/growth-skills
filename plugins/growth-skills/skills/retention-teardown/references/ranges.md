# Ranges seen in published tests

How to read: the lowest and highest measured lift in published tests of this kind of change, on one metric, with the number of tests. Seen in other apps' tests; not a forecast for your app. Built only from Part 1 rows of `evidence.md`; never averaged.

Lifts are relative unless marked pp. "(computed)" means the relative change was worked out from the two rates the row gives; the rates are shown next to it. Lab rows (#R38, #R39) measure engagement with a simulated log, not a live app.

| Pattern | Metric | Range seen | Tests | Strongest tier | Caveats |
|---|---|---|---|---|---|
| 1. Welcome that says what you have and the first step | — | no published range | — | — | only anecdotal (#R1); no test of the screen itself |
| 2. Trial status inside the app | Trial starts | +23% | 1 (#R48) | strong | bundled (paywall trial timeline + trial welcome screen with reminder opt-in); the in-app status part is not separated |
| 2. Trial status inside the app | Push opt-in | 6% → 74% (+1133%, computed) | 1 (#R48) | strong | bundled, as above |
| 2. Trial status inside the app | Cancels (in-trial) | −4% | 1 (#R48) | strong | bundled, as above |
| 2. Trial status inside the app | Complaints | −55% | 1 (#R48) | strong | bundled, as above |
| 3. Starter content instead of empty screens | Retention (1 week) | +10% | 1 (#R20) | directional | off-target (web B2B checklist); design not described |
| 4. Ask for notifications in context | Push opt-in | +9% to 6% → 74% (+1133%, computed) | 4 (#R5, #R7, #R10, #R48) | strong | #R48 bundled; #R5 under 40% → 66% (more than +65%, computed; small samples); #R7 vendor, pre-purchase onboarding, no baseline; #R10 two segments, +118.35% and +157.05%, vendor, control not described |
| 4. Ask for notifications in context | Photo access granted | 67% → 89% (+32.8%, computed) | 1 (#R6) | directional | off-target (photos permission, not push); small tests |
| 5. Primer copy tied to the user's goal | Push opt-in | no significant effect to +8% | 2 (#R3, #R2) | strong | same copy: +8% German learners (#R2), null for Spanish learners (#R3); the sign does not travel between markets |
| 6. An honest primer, per platform | — | no published range | — | — | only platform rules and guidance |
| 7. Reminder setup after the first session | Retention | about 3x for prompted users | 1 (#R17) | directional | vendor; holdout implied, no baseline numbers |
| 7. Reminder setup after the first session | Reminder adoption | 40% prompted vs under 1% via Settings | 1 (#R17) | directional | as above; two paths compared, not computed |
| 7. Reminder setup after the first session | Conversion (trial) | +6.4% | 1 (#R18) | directional | reminder setup inside onboarding vs on home (pre-purchase placement) |
| 7. Reminder setup after the first session | ARPU | +24% | 1 (#R18) | directional | as above |
| 8. Reminders apart from marketing | — | no published range | — | — | only platform rules and regulator guidance |
| 9. After a decline: fallback, not nagging | — | no published range | — | — | only a benchmark (B40) and rules |
| 10. Progress where the user lands | DAU | +3% | 1 (#R30) | directional | second-hand report |
| 10. Progress where the user lands | Retention (D14) | +1% | 1 (#R30) | directional | second-hand report |
| 10. Progress where the user lands | Engagement (lab) | log shown vs no log: intact 92.47% vs 64.94% (+42.4%, computed); broken 45.21% vs 60.90% (−25.8%, computed) | 1 (#R38) | strong | off-target (lab study); one test, two conditions; the sign flips after a break |
| 10. Progress where the user lands | Users kept saving at 8 months | +12% | 1 (#R47) | strong | off-target (finance app); second-hand write-up |
| 11. Make the streak easy to keep | Retention (D14) | +3.3% | 1 (#R25) | strong | fewer users hit their daily goal (no figure) |
| 11. Make the streak easy to keep | DAU | +1% | 1 (#R25) | strong | — |
| 11. Make the streak easy to keep | Learners on a streak | +10.5% in 20 days (+19% for new learners) | 1 (#R25) | strong | — |
| 11. Make the streak easy to keep | Learners on a 7+ day streak a year later | +40% | 1 (#R25) | strong | — |
| 12. Design the broken streak | Engagement (lab) | −25.8% to +24.1% (computed) | 2 (#R38, #R39) | strong | off-target (lab studies). #R38: broken log shown vs no log, 45.21% vs 60.90%. #R39: repairable vs unrepairable broken streak, 85.20% vs 68.66% |
| 12. Design the broken streak | Return a week later | +4% | 1 (#R29) | strong | Weekend Amulet, a store item offered on Fridays |
| 12. Design the broken streak | Streak loss | −5% | 1 (#R29) | strong | as above |
| 12. Design the broken streak | DAU | +0.38% | 1 (#R27) | directional | two freezes instead of one; method not stated |
| 13. Acknowledge progress right after the action | DAU | 0% to +2% | 4 (#R32, #R31, #R34, #R33) | directional | all second-hand; #R32 single sign-up badge null; #R33 wider badge range; #R34 tiered badges |
| 13. Acknowledge progress right after the action | Retention (D14) | 0% to +3% | 4 (#R32, #R34, #R33, #R31) | directional | as above |
| 13. Acknowledge progress right after the action | Retention (D7, new learners active 7 days later) | +1.7% | 1 (#R26) | directional | milestone animation; method not stated |
| 13. Acknowledge progress right after the action | Revenue (IAP) | +5% | 1 (#R33) | directional | second-hand |
| 14. A commitment screen after a session | Retention (D7) | +14% | 1 (#R28) | strong | uses in-game currency as the stake; D1 and D14 also significant (no figures) |
| 14. A commitment screen after a session | Retention (D30) | doubled | 1 (#R19) | directional | commitment screen in onboarding (pre-purchase); not a subscription app (n/a bucket) |
| 15. Let people hide streaks and celebrations | Engagement (lab) | log shown vs hidden: intact +42.4%, broken −25.8% (computed; 92.47% vs 64.94%, 45.21% vs 60.90%) | 1 (#R38) | strong | off-target (lab study); one test, two conditions; hiding helps only after a break |
| 16. A widget with the user's own progress | — | no published range | — | — | only anecdotal (#R58, #R60) and observed (#R61); #R59 compares widget users with others, likely self-selected |
| 17. A recap of the user's own value | Retention (share of weeks connected) | +9.4 pp (31.7% → 41.1%, +29.7% computed) | 1 (#R40) | strong | off-target: delivered as a notification (in-app only if push was off); draft paper |
| 17. A recap of the user's own value | Connected at least once | +2.8 pp (5.3% → 8.1%, +52.8% computed) | 1 (#R40) | strong | as above |
| 17. A recap of the user's own value | Users kept saving at 8 months | +12% | 1 (#R47) | strong | off-target (finance app); second-hand write-up |
| 18. A home for what they pay for | Retention (1 week) | +10% | 1 (#R20) | directional | off-target (web B2B checklist) |
| 18. A home for what they pay for | Engagement (content added) | +6.62% | 1 (#R22) | directional | vendor; session-start message, no control described |
| 18. A home for what they pay for | Engagement (content started) | +6.55% | 1 (#R22) | directional | as above |
| 19. Trial-ending notice with what they used | Trial starts | +4% to +23% | 2 (#R49, #R48) | strong | #R48 bundled; #R49 indie self-report, no sample; both are pre-trial reminder promises, not an in-app notice |
| 19. Trial-ending notice with what they used | Conversion (trial to paid) | −7.8% | 1 (#R50) | directional | opted-in users vs baseline; test stopped after 2 weeks |
| 19. Trial-ending notice with what they used | Conversion (sales) | +14% | 1 (#R51) | strong | off-target (email reminder 3 days before trial end); the sign flips vs #R50 |
| 19. Trial-ending notice with what they used | Cancels (in-trial) | −4% | 1 (#R48) | strong | bundled |
| 19. Trial-ending notice with what they used | Refunds | no change ("equal") | 1 (#R50) | directional | as #R50 above |
| 20. Return screen: resume or restart lighter | — | no published range | — | — | only an observational baseline (#R52); no test |
| 21. Rating ask after a completed task | Ratings per month | +400%+ | 1 (#R53) | directional | before/after; vendor author; average held around 4.84 |
| 21. Rating ask after a completed task | 5-star ratings | +50% to 4x | 2 (#R55, #R56) | directional | both before/after; #R55 vendor, no baseline; #R56 off-target (marketplace, not a subscription app) |
| 22. Ration the asks | — | no published range | — | — | no test of ask frequency; only guidance |

## Checks

- Patterns: 22. With a range: 15 (2, 3, 4, 5, 7, 10, 11, 12, 13, 14, 15, 17, 18, 19, 21). Without: 7 (1, 6, 8, 9, 16, 20, 22).
- Rows excluded on purpose:
  - Anecdotal or observed: #R1, #R13, #R24, #R42, #R45, #R54, #R57, #R58, #R60, #R61.
  - Benchmarks or correlations in Part 1: #R14, #R15 (vendor benchmarks), #R16 (opted-in vs opted-out correlation), #R36 (Friend Streak users vs others), #R52 (observational baseline), #R4 (50% figure is an analysis; follow-up tests unreported).
  - Saw vs didn't see, not called an A/B: #R21 (Step walkthrough), #R46 (Blinkist Year in Blinks recipients, no holdout), #R59 (Gratitude widget users).
  - #R8 Crossfader: compared with an industry average, not a control.
  - #R9 onX Hunt: "+10.6%" with the unit (relative or pp) not stated, and bundled with a win-back push.
  - #R11 Fishbrain and #R23 Headspace: CRM programmes (push, email, in-app); the screen's own effect is not separated and the metrics are programme outcomes.
  - #R12 Talabat: iOS provisional push (reach, no control); no matching pattern in `patterns.md`.
  - #R35 Duolingo leagues: no matching pattern (leaderboards); test design not stated.
  - #R37: intact vs broken streak state, not a design change a designer makes.
  - #R41 Café loyalty card: endowed progress on a physical card; no pattern cites it or tests the same change.
  - #R43 8fit and #R44 Lumosity: multi-channel campaigns with no control (#R44 compares with the prior year's email and bundles a sale).
- Second-hand rows within a row are not used: the "+3% from a similar change" quoted inside #R49.
