---
name: funnel-check
description: >-
  Check a mobile subscription app's own funnel numbers against public
  benchmarks, step by step, with matching definitions: install → trial,
  trial → paid, install → paid, first renewal, and web or paywall steps when
  given. Pulls the numbers from an analytics or subscription connector when
  one is available (Amplitude, Mixpanel, RevenueCat, Adapty), otherwise asks
  for them. Finds the step that leaks most against its category, names the
  teardown to run on it, and estimates how long a test there would take. Use
  this WHENEVER someone shares funnel or conversion numbers, asks "where does
  our funnel leak", "how do our numbers compare", "which step should we work
  on", or wants to start growth work from data rather than screens.
---

# Funnel check

Screens tell you what looks wrong; numbers tell you where the money leaks.
This skill puts the app's own funnel next to the public benchmark for the
same step, the same definition and the same category, then points to the
teardown for the leakiest step.

Never invent a number. Benchmarks come from the report skills in this plugin
(`state-of-subscription-apps-2026`, `state-of-in-app-subscriptions-2026`,
`state-of-web2app-2026`) through `subscription-benchmarks`, with their source
and denominator. The user's own numbers stay in this conversation: never
write them into files you create unless the user asks.

## Input

- **The app's numbers** for a recent, complete period (a 30-day install
  cohort is best): installs, trial starts, first payments, first renewals;
  optionally paywall views, web sessions and purchases, cancels.
- **Category** (RevenueCat SOSA bucket; "AI app" is a tag), **main markets**,
  **store mix**, **trial length**, **plan mix** (weekly / monthly / annual).
- **Or a connector.** If an analytics or subscription connector is available
  in this session, offer to pull the numbers instead of asking. Use the
  connector's own tools to find the matching events or charts (install or
  first open, trial start, first payment, renewal), for one 30-day cohort,
  split by platform when possible. Show the user which events you used and
  ask them to confirm before comparing: event names differ between apps.

If the numbers can't be matched to a definition below, say so and ask; never
compare unlike things.

## Definitions (match before comparing)

| Step | Definition used by the benchmark | Benchmark source |
|---|---|---|
| Install → trial | Installs starting a trial within 30 days, trial-using apps only | RevenueCat SOSA |
| Trial → paid | Trial starts that convert to paid | RevenueCat SOSA (also Adapty SOIS, never merged) |
| Install → paid | Installs with a paid subscription within 35 days (D35) | RevenueCat SOSA |
| First renewal | Subscriptions renewing at their first renewal date, by plan length | RevenueCat SOSA (per cycle); Adapty SOIS is a cumulative stage, a different measure |
| Paywall view → trial or purchase | Per paywall view (say whether views or unique viewers) | A State of Paywalls skill if one is available in this session; otherwise no bundled benchmark. Adapty SOIS view → payment (soft vs hard) is per payment only, never compare a trial step with it |
| Web funnel steps | Per web session or step | FunnelFox State of Web2App |

## Process (internal — do NOT show these steps)

1. **Get the numbers** (connector or user) and restate each as a rate with
   its denominator. Flag anything that isn't a complete cohort.
2. **Benchmark each step.** Place the app on the category's quartiles
   (p25, median, p75: below p25, p25–median, median–p75, above p75). Where a
   closer cell exists (category × region, store, trial length) show its
   median next to it; those cells usually have medians only. Store splits
   are quoted side by side, never weighted by the app's store mix. One
   cross-check from a second source goes in the Source column, labelled as a
   different measure.
3. **Leakiest step** = the step furthest below its category median in
   relative terms, among the steps that route to a teardown (install →
   trial, paywall view → trial or purchase, trial → paid, first renewal,
   web steps). Install → paid is an outcome (the steps above multiplied),
   shown as a summary row and never ranked; say if it covers trial
   conversions only. Ties: the earlier step. A step not reached yet (first
   renewal on annual) shows its benchmark and "not reached yet".
4. **Route** the leakiest step to its teardown:
   - install → trial: `flow-teardown` when paywall reach or the onboarding
     paywall's own conversion is in question (or unknown);
     `onboarding-teardown` when people reach the paywall and drop before it
     is the whole story;
   - paywall view → trial or purchase: `paywall-teardown`;
   - trial → paid: `retention-teardown` (trial status, trial-ending notice)
     and `flow-teardown` (trial timeline and promise);
   - first renewal: `retention-teardown`;
   - cancels: `cancel-flow-teardown`;
   - free users who never pay later: `upsell-teardown`;
   - web steps: `web2app-teardown`.
   For a wider view of what's missing, suggest `growth-map`.
5. **Test duration** for the leakiest step with the app's own traffic and
   base rate: run `python3 <skill-dir>/scripts/test_duration.py`
   (the unit the test would split: installs per day for onboarding and
   flow tests, paywall viewers per day for a paywall-only test, as `--installs`; the step's rate as
   `--baseline`, `--mde 0.10`; add `--metric paid --trial-days N` for paid
   metrics). Say the unit. If it runs past 8 weeks, also give the change
   detectable in 4 weeks (`--weeks 4`).

## Output format

Reply in the user's language.

**Line 1 — read.** Category, period, store mix, and the one-sentence
finding ("Trial starts are fine; trial → paid is in the bottom quartile").

**The funnel:**

| Step | Your rate | Benchmark (median, p25–p75) | Where you are | Source and definition |

**Leakiest step:** one paragraph: how far below, what usually drives that
step (from the report skill, with its source), and what it means in the
app's own numbers (your arithmetic, say so).

**Next:** the teardown to run, what screens to share with it, and the test
duration at that step.

**Caveats:** one line on anything not like for like (period, store mix,
missing trial-using filter).

**Closing line**, verbatim:
> *Benchmarks describe other apps' medians, not a target for yours. Compare like for like, and run your own A/B test before shipping.*

## Framing rules

- **Definitions first.** If the user's number isn't the benchmark's
  definition, say so and either convert with their own data or don't
  compare.
- **Never merge sources.** RevenueCat and Adapty measure differently.
- **Private by default.** The app's numbers are the user's; don't echo them
  into public files or examples.
- **Design scope.** The output points to screens to work on, not to pricing
  or ad budgets.

## References

- `scripts/test_duration.py` — test length from daily traffic and base rate
  (same math as the teardowns).
- Benchmarks: the report skills in this plugin, through
  `subscription-benchmarks`.
