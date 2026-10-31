# Ranges seen in published tests

How to read: the lowest and highest measured lift in published tests of this kind of change, on one metric, with the number of tests. Seen in other apps' tests; not a forecast for your app. Built only from Part 1 rows of `evidence.md`; never averaged.

No strong test in this library measures an in-app save screen on mobile. Every save-flow range below is directional and comes from web-billed news, SaaS or Apple's own cancel page. Save-rate definitions differ by source (Apple/RevenueCat save rate, Chargebee save rate, Churnkey deflection, Aftenposten's count of retained subscribers), so each definition gets its own row and is never put in one range with another.

| Pattern | Metric | Range seen | Tests | Strongest tier | Caveats |
|---|---|---|---|---|---|
| 1. Plain "Manage subscription" entry with plan, price and renewal date | — | no published range | — | — | only platform rules, legal cases and a consumer survey; #C1 moved the cancel button as part of a bundle (listed under 11) |
| 2. One-tap store hand-off | — | no published range | — | — | only observed and platform rules |
| 3. Optional reason survey (3–6 reasons, Skip) | — | no published range | — | — | no test isolates the survey (Gaps 7); surveys appear only inside bundled programmes (#C3, #C5, #C6) |
| 4. Route by reason | Save rate (Chargebee definition) | +56% (16% → 25%, +9 pp) | 1 (#C4) | directional | vendor case, no control; bundled (discount, pause, downgrade tested together); off-target (web-billed) |
| 4. Route by reason | Monthly churn | −15% to about −46% (computed for #C6: ~13% → just under 7%) | 2 (#C5, #C6) | directional | both before/after and off-target (web-billed); both bundled (survey + several offers); #C6 is an unverified forum post, unnamed app |
| 5. Plan switch or downgrade | — | no published range | — | — | only benchmark (#C9 setup comparison is cross-app and observational); #C4 and #C6 bundle a downgrade into programme results listed under 4 |
| 6. Pause (web and Google Play only) | Monthly churn | −15% | 1 (#C5) | directional | vendor before/after; bundled (survey, pause, coupon, chat); off-target (web SaaS); no iOS store pause exists |
| 7. One discount, shown once | Subscribers kept per month after starting to cancel (Aftenposten count) | +50% (about 600 → almost 900 a month) | 1 (#C1) | directional | before/after; bundled (5 → 3 steps, cancel button moved, one holdback offer replaced a downgrade menu); off-target (web news) |
| 7. One discount, shown once | Save rate (Apple definition: keeps the subscription after reaching Apple's cancel confirmation page) | +223% (+5.5 pp) | 1 (#C8) | directional | Apple platform claim, baseline, period and sample not stated; store surface (Apple's page), not an in-app screen. #C30 Mojo: exit and win-back discounts "didn't perform as strongly", null, no figure |
| 8. Personal loss reminder | — | no published range | — | — | only observed |
| 9. Fix the problem (technical reasons → support) | — | no published range | — | — | #C5 routed technical answers to chat but reports no number for that route |
| 10. Cancel stays visible next to every offer | — | no published range | — | — | only legal summaries (California, Germany, UK) |
| 11. At most one save screen, then cancel | Subscribers kept per month after starting to cancel (Aftenposten count) | +50% (5 → 3 steps; about 600 → almost 900 a month) | 1 (#C1) | directional | before/after; bundled (fewer steps + one holdback offer + cancel button moved); off-target (web news) |
| 11. At most one save screen, then cancel | Cancellations | −14% (the opposite change: a 4-page, 6-click friction flow) | 1 (#C7) | directional | leaked internal figure; off-target (web shopping membership); basis of the FTC case: a friction "win" is a legal liability, never a recommendation |
| 12. Clear confirmation: end date, no further charge | — | no published range | — | — | only observed and Apple HIG |
| 13. A billing-issue banner in the app | Failed-payment recovery | +167% (computed; 15% → 40%) | 1 (#C13) | directional | before/after; bundled (grace period, account hold, email/push, in-app alert icons); store + in-app (Google Play) |
| 14. One-tap resubscribe while access lasts | — | no published range | — | — | only benchmark (SOSA reactivation) and observed |
| 15. Win-back after lapse, not before | Churn when contacting customers who have not lapsed (the "before" this pattern avoids) | +67% (computed; 6% control → 10%, +4 pp) | 1 (#C19) | strong | randomized field experiment; off-target (telecom, outbound campaign recommending a better plan); shows the sign flip, not a win-back result. #C31 (Sub Club podcast): a win-back offer sent once auto-renew was off, before lapse: users refunded, then took the offer, "net negative", loss, no figure |
| 16. Compliance flags | — | no published range | — | — | rules and legal summaries, not tests |

## Checks

- Patterns: 16. With a range: 6 (4, 6, 7, 11, 13, 15; 4, 7 and 11 have two metrics each). Without a range: 10 (1, 2, 3, 5, 8, 9, 10, 12, 14, 16).
- Same test in more than one pattern: #C1 (7 and 11, one bundled redesign), #C5 (4 and 6, one bundled flow). Read them as one result each, not two.
- Records covered: #C1–#C31 (deep sweep 2026-10-31 added #C29–#C31; none adds a range: #C29 is a rate, #C30 and #C31 have no figure and are noted in the Caveats of 7 and 15).
- Excluded on purpose:
  - #C29 Coconote: 25% of cancelling users kept by a 7-day trial extension that replaced a discount; the discount's rate isn't given, so there is no lift, only a single rate (founder report). Fits pattern 7 (one offer at cancel) as direction only.
  - #C2 Star Tribune online 18.5% vs call centre 8.8%: a self-selected channel comparison (users who used the online flow vs users who phoned), not a test of the change.
  - #C3 Star Tribune (vendor view): absolute rates only; "10% better" is unclear as relative or pp; same programme as #C2.
  - #C5 39% deflection and #C6 "47% of cancellations saved": single absolute rates with no baseline.
  - #C8 "+82% average" for all adopters: mixes every message type, so it matches no single pattern.
  - #C9 RevenueCat panel: setup save rates (38% / 27% / 22% / 13%) are cross-app comparisons, and the 64-app cancellation gap is adopters vs non-adopters (observational, author says it could be chance).
  - #C10 Google Play benefits in the cancel flow (−2% voluntary churn): generic benefits, not the user's own usage (pattern 8 needs personal data); baseline not stated.
  - #C11, #C12 grace period and account hold: billing settings, not a screen.
  - #C13 resubscription 3% → 20%: "restore-window messages" for cancelled users, bundled, channel unclear (message vs in-app action), so not used for pattern 14.
  - #C14–#C18 trial reminders and auto-renew design: no matching pattern in this file (pre-renewal reminders belong to retention).
  - #C21 Unscripted reactivation paywall: compares reactivated users with new users on the standard paywall, not randomized (a saw-vs-didn't comparison).
  - #C20, #C22–#C24 anecdotal; #C25–#C28 observed; all Part 2 benchmarks.
