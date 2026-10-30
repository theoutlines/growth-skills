# Ranges seen in published tests

How to read: the lowest and highest measured lift in published tests of this kind of change, on one metric, with the number of tests. Seen in other apps' tests; not a forecast for your app. Built only from the test rows and E-rows of `evidence.md`; never averaged.

E-rows are aggregated priors from a vendor library, not single tests. They appear only where they report a measured figure, and are marked "aggregate". "Computed" means the relative change was worked out from two figures the row states; the figures are shown next to it. Section A tactics get one row per tactic and position, using the position wording from `seam-patterns.md`.

## A. Tactics that flip sign by position

| Pattern | Metric | Range seen | Tests | Strongest tier | Caveats |
|---|---|---|---|---|---|
| A. Second-chance discount: right after the onboarding paywall is closed | Premium conversion | about +25% to +30% (as stated) | 1 (E2, aggregate) | directional | aggregate of Adapty library tests, no single test named |
| A. Second-chance discount: after the main in-app paywall | ARPU | about −50% ("roughly half") | 1 (E2, aggregate) | directional | aggregate; the sign flips against the row above |
| A. "How your trial works" explainer: next to the price | Trial starts | +23% | 1 (#1) | strong | timeline shipped together with a reminder opt-in screen (see S5) |
| A. "How your trial works" explainer: several screens before the paywall | — | no published range | — | — | only a direction with no figure (E3) |
| A. Comparison table: on the paywall | — | no published range | — | — | only a direction with no figure (E4) |
| A. Comparison table: bare teaser screen before the paywall | — | no published range | — | — | only a direction with no figure (E4) |
| A. Guarantee or refund promise: at the ask, next to the CTA | — | no published range | — | — | no row tests this position |
| A. Guarantee or refund promise: own screen before the paywall | — | no published range | — | — | only a direction with no figure (E5) |
| A. Loader / "building your plan": after real personalisation | — | no published range | — | — | no row tests a loader followed by a plan that shows the answers |
| A. Loader / "building your plan": nothing personal after it (loader removed) | Trial conversion | +22% | 1 (#15) | directional | lift is for removing the loader |
| A. Loader / "building your plan": nothing personal after it (loader removed) | ARPU | +30% | 1 (#15) | directional | lift is for removing the loader |
| A. Loader / "building your plan": loader plus plan screen kept | ARPU | about −50% | 1 (E1, aggregate) | directional | one flow from the Adapty library; the row doesn't say whether the plan showed the user's answers |
| A. Paywall position: after a few motivation or value screens | Trial starts (download → trial) | +10% to about +143% (computed, about 7% → about 17%) | 1 (#8) | directional | one app, two figures: +10% for one move two screens earlier; the +143% is cumulative over many iterations |
| A. Paywall position: moved to the start of onboarding | Install → trial | +100% ("doubled") | 1 (#71) | directional | bundled (video added to the paywall at the same time); this is the position section A lists as losing, so the sign there is contested |
| A. Paywall position: moved to the start of onboarding | Revenue | +100% ("doubled") to +400% (computed from "5×") | 2 (#71, #72) | directional | #71 bundled; #72 before/after |
| A. Paywall position: moved to the start of onboarding | Trial → paid | unchanged (no figure) | 1 (#71) | directional | bundled; null result |
| A. Paywall position: after a long tail where reach collapses | — | no published range | — | — | only anecdotal (40% reach, E7) |
| A. Discount on store-sheet abandon: on abandon | — | no published range | — | — | #75 reports a share of revenue (17%) from a cohort comparison, not a lift |
| A. Discount on store-sheet abandon: App Review risk | — | no published range | — | — | a policy risk, no measured figure |

## B. Seam patterns

| Pattern | Metric | Range seen | Tests | Strongest tier | Caveats |
|---|---|---|---|---|---|
| S1. Paywall right after the value moment | Trial starts (install/download → trial) | +10% to +143% (computed, about 7% → about 17%) | 2 (#8, #71) | directional | #8 cumulative over many iterations (single move +10%); #71 +100% and bundled (video added) |
| S1. Paywall right after the value moment | Paywall reach | +50% paywall viewers | 1 (#71) | directional | bundled |
| S1. Paywall right after the value moment | Trial → paid | unchanged (no figure) | 1 (#71) | directional | bundled; null result |
| S1. Paywall right after the value moment | Revenue | +100% ("doubled") to +400% (computed from "5×") | 2 (#71, #72) | directional | #71 bundled; #72 before/after |
| S2. Paywall echoes the onboarding | Trial starts | +183% | 1 (#54) | strong | off-target: geo-specific paywalls, not onboarding answers; design and pricing changed together |
| S2. Paywall echoes the onboarding | Trial → paid | +20% | 1 (#22) | directional | confounded with pricing and product changes |
| S2. Paywall echoes the onboarding | Revenue (MRR, 30 days) | +83% | 1 (#22) | directional | confounded with pricing and product changes |
| S3. Promise continuity | Trial conversion | +17% | 1 (#11) | directional | onboarding copy (outcome vs feature), not only the paywall |
| S3. Promise continuity | ARPU | +13% | 1 (#11) | directional | as above |
| S3. Promise continuity | Conversion (type not stated) | +54% or more | 1 (#58) | directional | conference talk, app and category not named |
| S4. Pre-paywall step | Conversion | +27% | 1 (#55) | strong | — |
| S4. Pre-paywall step | Conversion (unclear: conversion or annual trials) | +16% | 1 (#56) | strong | metric ambiguous; this variant also adds a trial reminder step |
| S4. Pre-paywall step | Revenue (proceeds) | +36% | 1 (#55) | strong | — |
| S4. Pre-paywall step (reverse change: prices upfront beat a benefits-only pitch) | Trial conversion | +15% for prices upfront | 1 (#50) | directional | sign check: here the benefits-first version lost; also paid conversion +3%, MRR +33%, ARPU +17% for prices upfront |
| S5. Trial timeline and a kept reminder | Trial starts | +23% | 1 (#1) | strong | timeline and reminder opt-in shipped together |
| S5. Trial timeline and a kept reminder | Push opt-in | +1133% (computed, 6% → 74%) | 1 (#1) | strong | — |
| S5. Trial timeline and a kept reminder | In-trial cancels | −4% | 1 (#1) | strong | lower is better |
| S5. Trial timeline and a kept reminder | Complaints | −55% | 1 (#1) | strong | lower is better |
| S5. Trial timeline and a kept reminder | Sales (conversion to paid) | +14% | 1 (#65) | strong | off-target: a reminder email, not a screen; online courses |
| S6. Trial structure at the seam | Trial starts / trial conversion (as stated) | +7% to +25% | 3 (#57, #21, #45) | strong | three different changes (paid longer trial, early toggle-off paywall, one-tap trial); #21 bundled (two paywalls) |
| S6. Trial structure at the seam | View → subscription | +39% | 1 (#41) | strong | sample not given |
| S6. Trial structure at the seam | Revenue per 100 installs | +47% | 1 (#41) | strong | sample not given |
| S6. Trial structure at the seam | ARPPU | +5% | 1 (#41) | strong | sample not given |
| S6. Trial structure at the seam | Trial → paid | about flat | 1 (#45) | strong | null result |
| S6. Trial structure at the seam | Onboarding conversion | +10% | 1 (#21) | directional | bundled (two paywalls) |
| S7. A deliberate post-close step | Premium conversion | about +25% to +30% (as stated) | 1 (E2, aggregate) | directional | aggregate; only right after the onboarding paywall |
| S7. A deliberate post-close step | ARPU (same discount after the main in-app paywall) | about −50% ("roughly half") | 1 (E2, aggregate) | directional | aggregate; the sign flips by position |
| S8. Dismiss treatment | DAU | +8.2% | 1 (#6) | strong | off-target (sign-up wall, not a paywall); bundled ("combined wall optimization"); self-reported |
| S9. First limit (freemium) | Power-user conversion | +83% | 1 (#63) | directional | — |
| S9. First limit (freemium) | Trial starts | about +200% (computed from "about 3×") | 1 (#46) | directional | kill-switch rollout, not A/B |
| S9. First limit (freemium) | Conversion | about −7% (year over year) | 1 (#46) | directional | year-over-year figure, not a test arm; shows the sign can flip |

## Checks

- Section A: 7 tactics, 19 tactic-and-position rows. With a range: second-chance discount (both positions), trial explainer next to the price, loader with nothing personal after it (removed, and kept), paywall position (after value screens; at the start of onboarding). No range: trial explainer far from the paywall, comparison table (both positions), guarantee (both positions), loader after real personalisation, paywall after a long tail, store-sheet abandon discount (both).
- Section B: 9 patterns, all 9 with a range (S1–S9).
- Excluded on purpose:
  - #24 Superwall multi-page vs single-page (12.41% vs 9.07%): observational comparison of paywall opens, not randomized.
  - #75 transaction-abandon paywalls: share of revenue from a cohort comparison, not a lift.
  - #9 Opal close button, E3, E4, E5: no figures. E6 reverse trial (0.4% → 4.5%) and E7 contextual copy (+10–15%): anecdotal.
  - E8 goal personalisation in onboarding (CR +8–17%, ARPU +13–35%): an onboarding change, not the paywall echoing the onboarding, so left out of S2.
  - #67 "Trial for free" CTA (+104%): a CTA wording test, not promise continuity; left out of S3.
  - Paywall-element rows not tied to a seam pattern: #12, #42, #43, #60, #62, #64, #70. Benchmarks section: not tests.
