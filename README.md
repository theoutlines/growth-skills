# Growth Skills for Claude

Claude skills for **growth work on mobile subscription apps**, made for product designers. Share the screens of any part of the user's journey and get a score for what can be changed on screen, store and dark-pattern flags, and a ranked list of tests backed by published A/B tests and public benchmarks.

Made by a monetization design lead for day-to-day work on onboarding, paywalls, upsells, retention and churn.

**Works with:** Claude Code and the Claude app as one plugin, and any agent that supports the open [Agent Skills](https://agentskills.io) format (Codex, Gemini CLI, Cursor, GitHub Copilot). See [Install](#install).

## What's inside

Skills follow the user's journey. Not sure which one you need? Start with `growth-router`: share the screens and it picks.

| Part of the journey | Skill | What it reviews |
|---|---|---|
| Start here | `growth-router` | Sorts screens or a question to the right skill, or combines two |
| Web funnel | `web2app-teardown` | Ad landing, web quiz, plan screen, web paywall, checkout, the way into the app, and the in-app "buy on the web" screen |
| Onboarding | `onboarding-teardown` | First launch to the first paywall and what happens when it's closed |
| Onboarding + paywall | `flow-teardown` | Onboarding, the first paywall and the seam between them as one system: tactics on the wrong side of the seam |
| Upsells | `upsell-teardown` | Locked features, limits and counters, contextual paywalls, upgrade screens for payers, AI credits |
| First weeks to renewal | `retention-teardown` | Welcome after purchase, notification ask, reminders, streaks, recaps, trial-ending notice, welcome back, rating ask |
| Cancel flow | `cancel-flow-teardown` | Manage subscription, reason survey, save offers, confirmation, resubscribe |
| The whole journey | `growth-map` | Which growth levers the app uses and which nobody has touched, stage by stage, and where to start |
| Your own numbers | `funnel-check` | Your funnel against public benchmarks with matching definitions; finds the leakiest step and the teardown for it. Can pull numbers from Amplitude, Mixpanel, RevenueCat or Adapty when connected |
| A variant before launch | `variant-check` | Paywall A vs B before live traffic: which mechanics B changes, whether the test can see it, what the winning versions had that B lacks, a clarity pretest to run first. Figma frames, screenshots or a description |
| A finished test | `test-readout` | Did B really win? Trust checks, the likely range, where the difference came from (how many paid vs which plans), keep / kill / iterate. Pulls the numbers from Amplitude, Mixpanel, RevenueCat or Adapty when connected |

**Included:** everything in [Subscription Skills](https://github.com/theoutlines/subscription-skills), for the paywall itself and the numbers:

| Skill | What it answers |
|---|---|
| `subscription-benchmarks` | Routes a numbers question to the right report and keeps denominators apart |
| `state-of-subscription-apps-2026` | RevenueCat: download→trial, trial→paid, LTV, retention, renewals, refunds |
| `state-of-in-app-subscriptions-2026` | Adapty: LTV curves, retention by plan, prices by region, placement, AI apps |
| `state-of-web2app-2026` | FunnelFox: web funnels, web pricing, upsells, web vs app LTV |
| `subscription-pricing-index` | Adapty Pricing Index: weekly, monthly and annual prices in 64 countries |
| `paywall-teardown` | Scores a paywall screenshot out of 100. By Adapty, MIT |
| `paywall-ab-test-assistant` | Grades a test idea against Adapty's A/B test library. By Adapty, MIT |
| `paywall-store-compliance` | Will this paywall, trial or cancel flow pass App Review and Play policy? |

Only need the paywall part? Install [Subscription Skills](https://github.com/theoutlines/subscription-skills) on its own instead.

Every teardown:
- scores only what a designer changes on a screen, out of 100, and never rewards pressure (fake timers, guilt copy, hidden prices, blocked exits score lower);
- flags screens that break Apple or Google rules or match a named dark pattern (flags, not legal advice);
- ranks tests by evidence: every number links to its source and carries a tier (strong, directional, anecdotal, observed), and ideas with no public test are labelled hypotheses;
- shows a **range seen** next to each test idea: the lowest and highest lift measured in published tests of that kind of change, with the number of tests (what other apps saw, not a forecast for yours);
- takes screenshots, a description or Figma frames (via the Figma connector), so a design can be checked before hand-off;
- returns a report card (PNG) and test durations when you give traffic numbers, and offers to pull your own numbers from an analytics connector.

## Install

**Claude Code:**

```
/plugin marketplace add theoutlines/growth-skills
/plugin install growth-skills@theoutlines-growth-skills
```

Growth Skills already includes Subscription Skills. If you installed Subscription Skills before, remove it so the skills don't load twice.

**Claude app (web, desktop; paid plans):**
1. Customize → Plugins → Add → Add marketplace → `theoutlines/growth-skills`.
2. Discover → search "Growth Skills" → Add.

**Other agents:** `npx skills add theoutlines/growth-skills`.

**Just one skill?**

- **Claude app:** download that skill's zip from the [latest release](https://github.com/theoutlines/growth-skills/releases/latest) and upload it in Settings → Capabilities → Skills.
- **Claude Code:** install the plugin. Skills Claude doesn't need cost nothing: until a skill is used, only its short description is loaded.
- **Other agents:** `npx skills add theoutlines/growth-skills` and pick the skills you want.

## Example prompts

- "Here's our onboarding, 14 screens up to the paywall. What should we test first?"
- "Tear down our cancel flow. We're on iOS and web billing in Germany."
- "These are our locked-feature sheets and the limit screen. Are we blocking the habit?"
- "Our trial users cancel on day 0. Here are the screens after the trial starts."
- "Compare these two web quiz funnels."

## Accuracy and attribution

- **Unofficial and vendor-neutral.** Not made or endorsed by Apple, Google, RevenueCat, Adapty, FunnelFox, Mobbin or any company whose test is cited. Results belong to their publishers and are linked next to every number.
- App screens from Mobbin are described in our own words and linked, never copied.
- Store rules change. Flags point to the rule; they are not legal advice.

Found a mistake? Open an issue.

License: teardowns and router MIT; the included Subscription Skills text CC BY 4.0 and Adapty's two skills MIT. See [LICENSE](LICENSE), [LICENSES](LICENSES/) and [NOTICE](NOTICE.md).

## Maintainers

Teardowns and the router are edited here, in `plugins/growth-skills/skills/`. The Subscription Skills skills are edited in their own repo and copied in with `scripts/sync-subscription.sh` before each release. Project rules are in `CLAUDE.md`. On every release, bump the version in both manifests and attach one zip per skill to the GitHub release.
