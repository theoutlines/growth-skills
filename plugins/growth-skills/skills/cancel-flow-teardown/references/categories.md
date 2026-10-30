# Cancel-flow norms by category (RevenueCat SOSA buckets)

Collected 2026-10-29. Bucket = primary App Store category, the same taxonomy as the onboarding and paywall skills. "AI app" is a tag, not a bucket. Numbers come from SOSA 2026 (App Store + Google Play) unless another source is named; app examples are from `flows.md`. Category save-rate data for cancel flows does **not** exist publicly; the "what to lean on" lines are hypotheses tied to the reason mix, not tested norms.

SOSA 2026 source: https://www.revenuecat.com/state-of-subscription-apps/.

## Quick table

| Bucket | Play cancel reasons: cost / usage / better app / technical / other (%) | Reactivation within 12 months: weekly / monthly / annual (%) | Annual cancels in month 1 (%) | Typical cancel flow seen | Offer that fits the reason mix (hypothesis) |
|---|---|---|---|---|---|
| Health & Fitness | 38.7 / 40.4 / 7.7 / 3.1 / 10.1 | 8.1 / 12.4 / 4.8 | 33.8 | Survey + loss or plan screen, then store (Centr, Lifesum, MyFitnessPal, Strava, Peloton); discount rare (Pillow) | Usage is the top reason: pause (web/Play), downgrade tier (Peloton), "reached my goal" → maintenance plan |
| Education | 36.5 / 39.5 / 8.6 / 3.8 / 11.5 | 9.1 / 10.8 / 3.6 | 30.5 | Trial-cancel flows dominate (Blinkist, Headway, Babbel); plan switch (Duolingo); long surveys | Usage-led: reminder/schedule help, lighter plan; Education also has the longest time-to-paid tail, so win-back has room |
| Productivity | 44.4 / 26.4 / 9.5 / 7.0 / 12.7 | 6.6 / 36.1 / 4.8 | 34.0 | Web-billed tools run their own flow (Grammarly: one loss modal) | Most price-driven bucket: cheaper cadence or tier; monthly reactivation 36.1% is the highest of all — let people leave cleanly and win back |
| Utilities | 28.4 / 33.1 / 11.2 / 12.4 / 14.8 | 6.4 / 10.5 / 5.1 | 35.3 | Manage row with upsells (Tide Guide); fintech pause (Dave); in-app discount (Plum) | Highest "technical" share (12.4%): route to support/fix before any discount |
| Photo & Video | 33.4 / 37.4 / 11.9 / 6.6 / 10.6 | 11.5 / 20.2 / 8.4 | 38.3 | Few captured flows; reactivation paywall case (Unscripted #C21) | Highest annual reactivation (8.4%) and high monthly (20.2%): invest in win-back offers after lapse |
| Media & Entertainment | 36.7 / 34.4 / 9.5 / 6.5 / 12.9 | 11.8 / 15.8 / 7.0 | 34.5 | Big players web-bill or hand off with little friction (Spotify no in-app cancel on iOS; Audible text only; YouTube text link; SiriusXM long survey with Skip) | Content gaps and seasonality: pause / come back later; win-back promos (Spotify 3 months for $9.99, #C25) |
| Social & Lifestyle | 31.2 / 34.3 / 9.3 / 8.6 / 16.5 | 10.2 / 13.9 / 4.5 | 33.8 | Dating apps: no cancel flow on Mobbin, account "pause" (hide profile) instead (Tinder); gifting app cancels in-app (Givingli) | Highest "other" (16.5%): read free-text answers; dating churn is often success ("met someone") — don't fight it |
| Business | 28.3 / 38.5 / 12.8 / 7.7 / 12.7 | 7.9 / 10.3 / 5.6 | 32.0 | Mostly web-billed SaaS | Highest "found a better app" (12.8%): competitive comparison or feature roadmap; downgrade to a lower tier |
| All categories | 36.4 / 33.7 / 9.7 / 7.3 / 12.9 | 9.0 / 20.1 / 5.2 | 34.2 | — | — |

Shopping, Travel and Gaming exist in SOSA but are outside this skill's eight buckets (Travel: usage 46.7%, the most usage-driven; Shopping: 50% of annual cancels in month 1).

## Notes by bucket

**Health & Fitness.** Most captured flows (8 of 22) and the most varied. Common shape: Settings › Manage, a reason survey, a personalised "are you sure" (Centr uses the trainer's photo and the user's name), then the App Store. Peloton makes "Change membership" the primary button and puts a cheaper tier and annual switch first; that matches the 40.4% "not enough usage" reason. Pause is the natural offer for seasonal use (Recurly: pauses rise Oct–Jan, unpause peaks in March), but only exists on web billing or Google Play. Noom's 2022 class action (cancel only via coach chat) and its checkout now stating "cancel any time in the app" make this bucket's legal history relevant. AI-tagged calorie trackers (3-day trials) face the 55.4% day-0 cancel share on 3-day trials.

**Education.** Trial cancellations dominate the captured flows (Blinkist, Headway, Babbel all cancel a free trial). Shapes range from nothing (Babbel opens Apple's sheet) to an 11-reason survey (Headway). Duolingo's plan-switch screen with "keep my 12-month plan" is the clearest downsell. Blinkist's shared-library loss screen is the only social-loss pattern seen. SOSA: Education has the lowest annual reactivation (3.6%). On the web, Education has the highest monthly churn in the Recurly 2026 report (5.7% in 2025) and the highest involuntary churn of the three industries on Recurly's separate benchmarks page (1.69%); the two Recurly sources cover different periods, so quote each on its own. Reminder tests (#C15 Blinkist, #C16 Shaw Academy) are both Education.

**Productivity.** The most price-driven bucket on Play (44.4% cost) and the one where churned monthly users come back most (36.1% within a year). That argues for low-friction exits plus a clean re-activate path (Grammarly "Re-activate your plan") rather than heavy saves. AI-tagged assistants: SOSA shows AI apps with lower annual retention (21.1% vs 30.7%) and higher refunds (4.2% vs 3.5%) (SOSA 2026, see Benchmarks in `evidence.md`), so expect more early cancels.

**Utilities.** Highest technical-issue share (12.4%) and highest "other" after Social. A save screen that routes "technical problems" to support matches Wavve's routing (#C5). Fintech utilities on own billing use pause (Dave) and steep discounts (Plum 50% for 6 months). Truecaller (#C13) is the clearest involuntary-churn case: 54% of its cancels were payment failures.

**Photo & Video.** Shortest trials (68.2% of trials ≤4 days, SOSA 2026, see `evidence.md`) and high reactivation (monthly 20.2%, annual 8.4%, the highest annual). Win-back after lapse looks more valuable than in-flow saves; Unscripted's reactivation paywall (#C21) is the only case.

**Media & Entertainment.** Large players either web-bill and keep cancel off iOS (Spotify) or hand off with minimal in-app UI (Audible, YouTube). SiriusXM runs the longest survey (11 reasons) but makes it skippable. Netflix proactively cancels inactive members (#C22). Recurly web data: Digital media & entertainment 5.5% monthly churn (Recurly 2026 report); 1.59% involuntary on Recurly's separate benchmarks page (different period, don't combine). News publishers (outside the app taxonomy, mapped here) supply most of the save-flow cases: Aftenposten #C1, Star Tribune #C2/#C3, NYT #C23, and the field experiments #C17/#C18.

**Social & Lifestyle.** Dating apps don't expose a cancel-subscription flow on Mobbin; account deletion offers "pause my account" (visibility, not billing). Match Group's $14M FTC settlement (2025) required a simple, reachable way to end accounts. Social has the highest "other" reason share (16.5%).

**Business.** "Found a better app" is highest here (12.8%). Business is mostly web-billed SaaS (Chargebee/Churnkey/ProsperStack territory), so cancel-flow tooling and web save-rate cases (Wavve #C5) apply most directly.
