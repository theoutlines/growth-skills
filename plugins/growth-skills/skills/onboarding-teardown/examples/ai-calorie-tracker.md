# Example teardown: an AI calorie tracker

Input: 17 screens of a Health & Fitness diet app with the AI tag, from public Mobbin captures (October 2026), shared as a written description. Screens 16–17 were not described. The app is left unnamed here; the patterns and evidence are what matter.

---

Health & Fitness: diet, with the AI tag. A compact quiz funnel that leads to an editable numeric plan, two pre-paywall screens, a 3-day trial and a one-time offer on close. It's a solid flow: trust and setup are excellent, and the gaps sit at the opening and at the paywall itself.

**Onboarding score: 83/100 · Solid**
Value 18/25 · Personalisation 17/20 · Friction 20/20 · Trust 15/15 · Seam 13/20

12 screens to the paywall (2–13; order of 5–16 assumed: 5–8 body questions, 9 social proof, 10 daily goals, 11 plan reveal, 12–13 pre-paywalls, 14 paywall, 15 one-time offer). 6 questions (norm 10–20; fewer is fine). No account and no permission before the paywall. Paywall right after the plan reveal (the norm). 3-day trial on annual (the AI norm), reminder promised on a separate screen.

Keep these: "this calibrates your plan" lines on every body question, a progress bar, social proof with a rating count and dated reviews, a plan reveal with editable numbers and cited sources (Harvard, NIH, ISSN), a recommended macro default, a "try for free" pre-paywall, and a single one-time offer on close.

**Screen notes**
- **Screen 2**: the flow opens cold on "How many workouts do you do per week?". The user meets a question before any promise, and the goal question (lose / maintain / gain) only comes around halfway through.
- **Screen 4**: the "with a plan vs without a plan" weight chart has no label marking it as illustrative. That projection is the trap pattern 11 warns about, and it matters more in an AI app, where refunds already run higher.
- **Screen 11**: the strongest screen. Goal headline, editable calorie and macro tiles, and sources directly under the numbers.
- **Screen 13**: "We'll send you a reminder before your free trial ends" is promised, but no notification permission is asked anywhere before the paywall. The promise can't be kept unless it's backed by permission or an email.
- **Screen 14**: closing relies on the back arrow alone, and the annual plan is shown as a monthly equivalent. Check that the billed annual amount sits next to the CTA (3.1.2 and the Play subscriptions policy; this is a flag, not a ruling, and paywall-store-compliance can run a full review). For a full paywall critique, use paywall-teardown.

| # | Priority | Screen | Pattern | Test idea (applied to your flow) | Category norm | Evidence |
|---|---|---|---|---|---|---|
| 1 | High | 13–14 | Trial timeline and reminder promise | Replace the one-line reminder promise with a dated Today / day 2 reminder / day 3 charge timeline directly under the annual price on screen 14, and ask for notification permission on screen 13 behind a sample reminder and a single "Continue". | Norm in meditation and Education trials | Blinkist, timeline plus reminder: +23% trial sign-ups, −55% complaints (#1, strong) |
| 2 | Medium | new, after 11 | First result before the paywall | Let the user scan one meal (their own photo, with a sample plate as fallback) and see calories counted against the new daily target before the "try for free" screen. Hypothesis. | Norm in Photo & Video (Photoroom: your photo, the result, then the paywall); diet funnels usually stop at the plan | Unnamed education app, trial lesson + survey: +25% trial starts, +78% ARPU (#12, directional, other bucket). Duolingo's about +20% DAU (#5, strong) was a sign-up wall, not a paywall |
| 3 | Medium | 14 | Paywall echoes the onboarding | Put the goal and target weight in the paywall headline, plus the daily calorie target from screen 11 ("Reach 72 kg on 1,850 kcal a day"). | Seen in Health & Fitness (Calm "plan is ready"), Opal, Speechify | Flirt AI, answer-based routing to 3 paywalls: +83% MRR in 30 days, +20% trial-to-paid (#22, directional, confounded with pricing changes). Daily Horoscope +183% trial start rate (#54, strong) segmented by country, not by answers |
| 4 | Medium | 2 | Value promise on screen 1 | Add a single opening screen before the workouts question that promises the outcome ("Track calories from a photo — your plan in 2 minutes") over a short clip of a scan. | Common across buckets | Travel app, value proposition up front plus shorter copy and testimonials: +30% conversion to purchase (#17, strong, bundle of three changes) |
| 5 | Medium | 2, 7 | Goal or intent question early | Move the lose / maintain / gain question to screen 2, ahead of workouts, and reflect it in the screen 4 chart's headline. | Norm in Health & Fitness quiz funnels | Headspace, quiz before the same course: +7.6 pp course starts (#3, strong; course starts, not trials). Headspace multi-select intent question: about +10% free-trial conversion (#4, directional) |
| 6 | Low | 14 | Dismiss treatment | Test a visible close (X) on the paywall against the back arrow alone, and read both trial starts and the take rate on the 80%-off offer. | Hard paywalls are the norm only in paid-only utilities | Opal, more visible close: activation up, ARPU slightly down, no figures (#9, anecdotal) |

**Missing screens:** 16–17 (not described). Please also confirm the order of screens 5–16 and whether the paywall at 14 states the billed annual price. AI apps usually monetise at the first limit-hit paywall, so please share that one too if a free scan allowance exists.

> *Published results are one app's outcome in its own test, not the lift your flow will get. Patterns and norms come from public teardowns and published case studies; run your own A/B test before shipping.*
