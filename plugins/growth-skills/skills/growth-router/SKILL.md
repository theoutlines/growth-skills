---
name: growth-router
description: >-
  Start here for growth work on a mobile subscription app. Works out which
  part of the user's journey a screen, flow or question belongs to (web
  funnel, onboarding, paywall, the seam between them, upsells, the first
  weeks before renewal, the cancel flow) and hands it to the right teardown
  or benchmark skill, combining two when the screens span both. Use this
  WHENEVER someone shares app screens, Figma frames or a flow and asks what to fix, test or
  improve without naming a skill, asks where to start on growth, or sends a
  mix of screens from different parts of the app.
---

# Growth router

This skill decides **which skill should answer**, then loads it and follows
its instructions. It never scores screens itself.

## The journey and its skills

| Part of the journey | What the screens look like | Skill |
|---|---|---|
| Web funnel | Ad landing, web quiz, plan screen, web paywall, web checkout, "get the app" | `web2app-teardown` |
| Onboarding | First launch to the first paywall: questions, permissions, personalisation, loaders | `onboarding-teardown` |
| Paywall | One paywall screen or its steps | `paywall-teardown` |
| Onboarding + paywall as one system | Onboarding, the first paywall and what happens on close, shared together | `flow-teardown` |
| Upsells | Locked features, limits and counters, contextual paywalls, upgrade screens for payers, credits | `upsell-teardown` |
| First weeks to renewal | Welcome after purchase, notification ask, reminders, streaks, recaps, trial-ending notice, welcome back, rating ask | `retention-teardown` |
| Cancel flow | Manage subscription, reason survey, save offers, cancel confirmation, resubscribe | `cancel-flow-teardown` |
| The whole journey | "What are we not doing?", a growth audit or roadmap, no specific screens | `growth-map` |
| Own funnel numbers | Install → trial, trial → paid, renewal, cancels; or "pull our numbers" | `funnel-check` |
| A paywall variant before launch | "Is this bold enough?", "check my variant", A and B screens before a test | `variant-check` |
| A finished test | "Did B win?", an experiment chart or variant numbers | `test-readout` |

Questions about numbers ("is our trial→paid good?", "what should we charge
in Brazil?") go to `subscription-benchmarks`. Store-rule questions ("will
this get rejected?") go to `paywall-store-compliance`. "Is this test idea
worth running?" goes to `paywall-ab-test-assistant`. All three ship in this
plugin.

## How to route

1. **Sort the screens** by the table. Use what the screen does, not its
   title: a paywall shown after a locked feature is an upsell; a paywall at
   the end of onboarding is onboarding or flow.
2. **One part** → load that skill and follow it.
3. **Onboarding and the first paywall together** → `flow-teardown` (it calls
   the onboarding and paywall rubrics itself). Don't run the three
   separately.
4. **Other mixes** (e.g. upsells and retention screens) → run each skill on
   its own screens, in journey order, and say which screens went where. Give
   one combined list of tests at the end, keeping each row's priority and
   evidence from its own skill. Never add the scores together.
5. **Unclear** → ask one question: which part of the app are these screens
   from?
6. **No screens, only "where do we start?"** → with numbers (or an analytics
   connector), run `funnel-check`; without them, run `growth-map` on a
   description of the app. Both end by naming the teardown to run next.
7. **Figma frames** count as screens: route them the same way. A teardown of
   a design before hand-off is the same teardown.

## Rules all skills here share

- Only what a designer changes on a screen is scored or recommended.
- Every number comes from a skill's references with its source and evidence
  strength; nothing is invented.
- No skill rewards pressure: fake timers, guilt copy, hidden prices or
  blocked exits score lower, never higher.
- Flags are not legal advice.
