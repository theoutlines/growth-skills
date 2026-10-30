# Funnel benchmarks for onboarding

Use this file when the user shares funnel numbers next to the screens. Compare
each number with the matching benchmark, by the same definition, and say which
step leaks most. Never mix definitions: RevenueCat counts per install or per
trial start; Adapty counts per paywall view or per install, as labelled below.

Quartiles are written p25 / median / p75 / p90.

## 1. Install → trial start (within 30 days, trial-using apps)

RevenueCat SOSA 2026. 78–90% of trial starts happen on day 0 (RevenueCat panel; Adapty reports 89.4%), so this is
almost entirely an onboarding metric.

| Bucket | p25 / median / p75 / p90, % |
|---|---|
| Business | 3.4 / 9.1 / 16.5 / 22.5 |
| Education | 2.7 / 6.5 / 11.8 / 18.9 |
| Health & Fitness | 2.7 / 6.9 / 13.6 / 23.2 |
| Media & Entertainment | 1.3 / 4.0 / 9.0 / 16.7 |
| Photo & Video | 2.0 / 5.2 / 9.6 / 18.2 |
| Productivity | 2.1 / 5.7 / 11.5 / 19.2 |
| Social & Lifestyle | 2.1 / 6.2 / 12.1 / 20.7 |
| Utilities | 2.4 / 6.5 / 14.2 / 24.3 |
| All | 2.2 / 5.8 / 12.4 / 21.0 |

AI apps: median 8.5% vs 5.6% for non-AI.
Source: https://www.revenuecat.com/state-of-subscription-apps/

## 2. Trial start → paid

RevenueCat SOSA 2026. This is mostly decided by trial length and what the
onboarding promised, but the seam (timeline, reminder) moves it too.

| Bucket | p25 / median / p75 / p90, % |
|---|---|
| Business | 19.9 / 29.4 / 46.8 / 60.4 |
| Education | 24.2 / 36.1 / 50.6 / 65.7 |
| Health & Fitness | 26.1 / 37.7 / 51.4 / 65.4 |
| Media & Entertainment | 19.0 / 32.2 / 52.7 / 69.5 |
| Photo & Video | 14.4 / 22.2 / 33.1 / 45.3 |
| Productivity | 18.0 / 27.2 / 42.1 / 58.7 |
| Social & Lifestyle | 17.0 / 28.8 / 45.1 / 59.9 |
| Utilities | 19.7 / 31.1 / 47.1 / 66.3 |
| All | 20.2 / 32.2 / 48.1 / 64.7 |

By trial length (all apps, median): ≤4 days 25.5%, 5–9 days 37.4%, 10–16 days
35.4%, 17–32 days 42.5%. 55.4% of 3-day-trial cancellations happen on day 0.

## 3. Install → paid (day 35)

| Bucket | p25 / median / p75 / p90, % |
|---|---|
| Business | 1.1 / 2.6 / 5.0 / 10.9 |
| Education | 0.7 / 2.2 / 5.4 / 11.6 |
| Health & Fitness | 1.1 / 2.9 / 6.2 / 12.2 |
| Media & Entertainment | 0.5 / 1.5 / 3.7 / 7.4 |
| Photo & Video | 0.8 / 2.1 / 4.4 / 7.9 |
| Productivity | 0.7 / 1.9 / 4.2 / 8.2 |
| Social & Lifestyle | 0.7 / 2.0 / 4.5 / 8.4 |
| Utilities | 0.6 / 1.9 / 4.4 / 8.2 |
| All | 0.7 / 2.0 / 4.6 / 9.1 |

Adapty 2026 by paywall placement (install → paid, a different panel; don't
compare with the table above): onboarding paywall with trial 1.35% vs in-app
0.89%; without trial 0.82% vs 0.76%.
Source: https://adapty.io/blog/high-performing-paywall-2026/

## 4. Reach: installs that see the first paywall

No panel benchmark is published. Reference points only:
- One top Health & Fitness app: 87% of new users see a paywall (#70).
- One long-onboarding app: only 40% of new users ever saw it (Superwall,
  anecdotal).
- Adapty's own guidance conflicts (90–95% on one page, 60–80% on another), so
  don't quote either as a norm.

Read it as: if reach is far below what the flow length suggests, the leak is
before the paywall, and paywall tests won't fix it.

Onboarding completion (installs that finish onboarding) has no public benchmark. Report the number, compare it with reach to the paywall if both are given, and say there's no norm.

## 5. Paywall → purchase start → purchase complete

Single-app reference (#70): 57% of paywall viewers start a purchase and 63% of
started purchases complete. Superwall claims about 50% of started purchases
complete across apps (method not stated). A big gap between starts and
completions points to the store sheet (price shock, Face ID friction), not the
onboarding.

## 6. Permission opt-ins

| Permission | Benchmark | Source |
|---|---|---|
| ATT (users shown the prompt) | 38% average (Q1 2026); 35% (Q2 2025); Education 14% (2025) | https://www.adjust.com/blog/att-opt-in-rates-2025/ |
| Push, iOS | 48.85% median (2025 data, Airship) | https://www.airship.com/mobile-app-push-notification-benchmarks-for-2026/ |
| Push, Android | 53.3% median (2025 data, Airship); Airship says Android opt-in dropped after the Android 13 runtime permission | same |
| Push, Health & Fitness | iOS 53.98%, Android 85.28% (Pushwoosh panel; not comparable with Airship) | https://www.pushwoosh.com/blog/increase-push-notifications-opt-in/ |

Single-app reference: Blinkist's reminder opt-in on the trial welcome screen
took push opt-in from 6% to 74% (#1).

## How to report

Add one line after "the flow in numbers": "Funnel: install → trial 4.1% (H&F
median 6.9%, p25 2.7%) · trial → paid 41% (median 37.7%) · push opt-in 35%
(iOS median 48.85%). The leak is before the trial." Then let the table lead
with the step that leaks most. If the user gave no numbers, skip the line and
don't ask for them unless they ask what to measure.
