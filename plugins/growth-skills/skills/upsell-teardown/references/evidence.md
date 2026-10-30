# In-product upsell evidence: published tests, benchmarks and gaps

Collected 2026-10-29/30. Every number was read on the page it comes from. Cite tests as **#U1, #U2 …** and benchmarks by their row (e.g. "Adapty State of Paywalls 2026, placement"). The `U` prefix keeps this list apart from the onboarding library (#1–#77) and the cancel-flow library (#C1–#C28).

Part 1 is published tests and case studies. Part 2 is benchmarks from public reports. Never merge two rows into one number, and keep metric definitions apart (Part 2, section 8).

# Part 1. Published tests and case studies

**Tiers in the two parts.** Part 1 tiers grade a row as evidence that a *change* works, so a vendor aggregate there is "directional". Part 2 tiers grade a benchmark as a *description* of what apps see, so the same dataset can be a "strong benchmark". For priority, a benchmark is Medium at most.

## Tiers

- **Strong**: controlled A/B test or randomized field experiment, with numbers on the page.
- **Directional**: numbers, but no stated method, a before/after or year-over-year comparison, bundled or confounded changes, or a vendor-reported aggregate.
- **Anecdotal**: no numbers (or a test is described but its figures are not published).
- **Observed**: seen in apps, no test.

Conventions:
- Lifts are **relative** unless marked "pp" (percentage points) or given as two absolute rates (a% → b%).
- The metric's denominator is named when the page names it (per paywall view, per download, per install, per user in arm). "Denominator not stated" means the page doesn't say.
- Buckets are RevenueCat SOSA buckets. "AI" is a tag, not a bucket. Games and non-app products get **n/a**. "(inferred)" means the bucket comes from the app's description, not from a checked store listing.
- Rows that already exist in the onboarding-teardown library (https://github.com/theoutlines/growth-skills/tree/main/plugins/growth-skills/skills/onboarding-teardown) are listed as **Same as onboarding #N** and keep that number in the note; they are never renumbered.
- Bundled changes are flagged. Two tests are never merged into one number.

---

## A. Contextual and feature-gated paywalls

| ID | App | Category | Bucket | AI tag | Surface | Change | Metric | Result | Date | URL | Tier |
|---|---|---|---|---|---|---|---|---|---|---|---|
| U1 | Memrise | Language learning | Education | no | Google Play (Android) | Two upgrade-message designs on a locked Pro game mode, each pitching a different benefit ("difficult words" vs "favourite words") | Conversion to Pro; Pro-mode usage | Design A converted 28% higher than B; Pro-mode usage +9.7%. After rollout, subscriptions from that mode rose 16% as a share of all subscriptions | 2016-11-30 | https://android-developers.googleblog.com/2016/11/learn-tips-from-memrise-to-increase-in-app-conversions-with-pricing-experiments.html | Strong (A/B, stated on page; no sample size) |
| U2 | Tapple | Dating | Social & Lifestyle | no | In-app store billing (platform not stated; Firebase A/B Testing) | Variants of the subscription prompt shown when a non-subscribed male user tries to open messages (feature gate on messaging) | Subscription registrations | +8% "after implementing the winning design"; baseline and control comparison not stated | Not dated | https://firebase.google.com/case-studies/tapple | Directional (A/B run, but the +8% is reported after rollout, baseline unclear) |
| U3 | Grammarly | Writing assistant | Productivity | yes | In-product (web/desktop/mobile; billing not stated) | Premium suggestions shown inside the user's own text; three upgrade framings tested ("Unlock for Free", "Get Premium", "Peel and Reveal" = suggestions visible, upgrade framed as "more value"). An earlier "sticker peel" (peek at a locked suggestion) also shipped in 2024 | Upgrades; annual purchases; uninstalls; WAU | Winner: +22% upgrades, +4% annual plan purchases (no baseline). Sticker peel: conversion up, but uninstalls rose and WAU of engaged free cohorts fell (no figures). By 2024: 20%+ growth in incremental annual upgrade revenue | Pub. 2025-08-19 (work 2024) | https://growth-designers.beehiiv.com/p/newsletter-august-shane-fontane-turning-locks-into-gifts-a-better-way-to-upgrade | Directional (variants compared, no method or sample) |
| U4 | Duolingo | Language learning | Education | no | In-app store billing | Plus ad shown when a learner who is offline tries to start a lesson (hard gate on offline use) | Plus sign-ups; revenue; retention; DAU | "Much higher" Plus sign-up rate, slight revenue increase, but retention down and DAU slightly down; Duolingo shut it down | Pub. 2020-01-10 | https://blog.duolingo.com/improving-duolingo-one-experiment-at-a-time | Anecdotal (experiment, no figures) |
| U5 | JourneyStamp | GPS photo stamp | Photo & Video | no | In-app store billing | **Same as onboarding #23.** In-app paywalls triggered at high-engagement moments with copy tailored to features used, bundled with onboarding paywall tests | Conversion | +50%; overall 7.3%; no separate in-app figure | Pub. 2026-02-15 | https://superwall.com/case-studies/journeystamp | Directional (bundled) |
| U6 | Slopes | Ski tracker | Health & Fitness | no | In-app store billing | **Same as onboarding #46.** Trial popup when the user starts recording at a mapped resort (contextual trigger) | Trial starts; conversion | About 3x trial starts; conversion about −7% YoY | Pub. 2022-04-12 | https://blog.curtisherbert.com/slopes-diaries-42-building-ramps-not-walls/ | Directional |

## B. Usage limits and free-tier size

| ID | App | Category | Bucket | AI tag | Surface | Change | Metric | Result | Date | URL | Tier |
|---|---|---|---|---|---|---|---|---|---|---|---|
| U7 | Busuu | Language learning | Education | no | In-app | **Same as onboarding #63.** Free users limited to 1 language | Power-user conversion | +83% | About 2017-12 | https://abtest.design/tests/content-locking | Directional |
| U8 | Unnamed mobile game (Berlin publisher) | Mobile game | n/a (Gaming) | no | In-app | Three freemium designs randomized across about 300,000 users; fewer levels playable for free | Conversion to paid (14-day window); usage; virality | Fewer free features raised conversion by "more than 20 percent" without hurting users' invites; working-paper abstract adds that usage fell and that managers "gave away too much for free" | Article 2018-07-03; working paper 2016 | https://esmt.berlin/index%2Ephp/node/46483 ; https://ideas.repec.org/p/esm/wpaper/esmt-16-06.html | Strong (randomized field experiment) |
| U9 | New York Times (Aral & Dhillon) | News | Media & Entertainment | no | Web | Paywall meter varied: fewer free articles and fewer free sections | Total subscriptions; content demand; net revenue | Subscriptions +31% over 7 months; total content demand −9.9%; net revenue +$230,000+ after ad loss | Management Science, 2020-08 | https://dspace.mit.edu/handle/1721.1/129936 | Directional (quasi-experiment, web) |
| U10 | Alpe Audio | Audio learning | Education | no | In-app store billing | Free tier changed from "first 1–2 lessons per course + a few free courses" to 40 free listening minutes per week across the whole library. Bundled with moving the paywall right after onboarding and a new paywall design, over 8 months | Download → paid; trials; free-user retention | Download-to-paid 7.6x over 8 months (whole program). Paywall move alone: 3x trials started, no drop in trial-to-paid. Users who hit the paywall after their 40 free minutes converted at 10%. Free users' median listening time 2x; free D30 retention +70% (plateau 35%) | 2022-02-17 | https://www.indiehackers.com/post/how-we-increased-conversion-from-free-to-paid-by-7-6x-e067256502 | Directional (bundled, sequential tests) |
| U11 | Greg | Plant care | Social & Lifestyle (inferred) | no | In-app store billing | Usage-cap paywall (5 plants free, paywall on the 6th) replaced by a feature gate (watering reminders need a subscription), shown in onboarding to all users | Trial sign-ups; sign-up → trial | Trial sign-ups about +400%; sign-up-to-trial 3% → 15% | Pub. 2023-11-20 | https://www.revenuecat.com/blog/growth/paywall-placement/ | Directional (before/after; gate type and placement changed together) |
| U12 | Ryn VPN | VPN | Utilities | no | In-app store billing + rewarded ads | Freemium paywall replaced by one with three access tiers and a "Continue with Ads" option (one ad = 30 minutes of VPN) | Revenue; ARPPU; paying users; conversion | Revenue +158% (28 days after launch vs the previous year); ARPPU +98%; paying users +30%; conversion 0.08% → 1.2% (denominator not stated) | Pub. 2025-12-28 | https://superwall.com/case-studies/ryn-vpn | Directional (year-over-year, no control) |
| U13 | Pandora (Goli, Huang, Reiley, Riabov) | Music streaming | Media & Entertainment | no | Mobile app; paid ad-free tier ($4.99/mo) | Ad load randomized across ~34.4M listeners for 21 months, 9 arms from 3 to 6 interruptions/hour × 1 to 2 ads (2.74 to 5.02 realized ads/hour) | Listening hours; active listeners; paid ad-free subscriptions | Each extra ad per hour cut listening hours by about 2.08%; the long-run effect was about 3x the one-month estimate. Highest-load arm about 2% fewer weekly active listeners than control. More ads led to more paid ad-free subscriptions (effect size not in the part of the paper read; control share of paid users 1.103%) | arXiv v1 2024-12-04 (first version 2018) | https://arxiv.org/html/2412.05516v1 | Strong (randomized) for listening; subscription direction only |

## C. Gate type: soft vs hard, freemium vs hard paywall

| ID | App | Category | Bucket | AI tag | Surface | Change | Metric | Result | Date | URL | Tier |
|---|---|---|---|---|---|---|---|---|---|---|---|
| U14 | RevenueCat SOSA 2026 (cross-app) | Cross-category | All | mixed | In-app store billing | Apps with a hard paywall vs freemium apps (not a test: apps choose their model) | Download-to-paid (median); revenue per install | 10.7% vs 2.1% download-to-paid; top 10% of hard-paywall apps 38.7%; RPI day 14 $2.32 vs $0.27; day 60 $3.09 vs $0.38 | RC blog 2026-04-29; SaaStr 2026-03-07 | https://www.revenuecat.com/blog/growth/hard-paywall-vs-freemium ; https://saastr.com/the-top-10-learnings-from-revenuecats-state-of-subscription-apps-how-115000-mobile-apps-deliver-16b-in-revenue-whats-working-whats-quietly-killing-growth | Directional (benchmark, self-selected) |
| U15 | Two unnamed apps (Phil Carter, advisor) | Not stated | n/a | unknown | Not stated | (a) Hard paywall → multistep paywall plus other pricing/packaging changes; (b) a different app moved to freemium | LTV per user; subscriber conversion | (a) +75% LTV per user; (b) subscriber conversion down more than 50%, reverted after a couple of weeks | Pub. 2026-04-29 | https://www.revenuecat.com/blog/growth/hard-paywall-vs-freemium | Directional (anonymous, bundled) |
| U16 | Adapty State of Paywalls 2026 (cross-app) | Cross-category | All | mixed | App Store | Paywalls with no close button ("hard") vs with one ("soft"), same-app medians. Note: this is close-button type, not freemium vs hard-paywall model | View → trial; view → direct purchase | 4.7% vs 3.2% trial starts per view (+48%); 0.50% vs 0.75% direct purchases per view (−33%); hard wins on combined starts in 57% of apps. 11% of apps run a hard paywall; 57% of hard-paywall views happen in onboarding | Pub. 2026-10-16 (data Oct 2025–Sep 2026) | https://adapty.io/state-of-paywalls-2026/ | Directional (vendor aggregate) |
| U17 | PepTalk | Motivational video | Media & Entertainment | no | In-app | **Same as onboarding #61.** Soft (10 s preview, then paywall) vs hard (detail screen, then paywall) | Conversion | "Significantly" higher for soft (no figure) | Not dated | https://abtest.design/tests/hard-vs-soft-paywall | Anecdotal |

Grammarly's sticker-peel result (U3) and Duolingo's offline gate (U4) also belong here: both raised conversion and hurt engagement.

## D. Timing: when the upsell appears

| ID | App | Category | Bucket | AI tag | Surface | Change | Metric | Result | Date | URL | Tier |
|---|---|---|---|---|---|---|---|---|---|---|---|
| U18 | Adapty State of Paywalls 2026 (cross-app) | Cross-category | All | mixed | App Store | Onboarding (first-session) paywalls vs later paywalls (not a test) | Paywall view → paid (median); revenue per 1,000 views; share of subscription revenue | 0.85% vs 0.23% per paywall view ("almost 4x"); $170 vs $40 per 1,000 views. 53% of subscription revenue comes from subscriptions started in the first session, 38% after it (Lifestyle and Utilities 48%; monthly plans 47%, weekly 38%, annual 32%). About 7 in 10 paywall views happen after the first session | Pub. 2026-10-16 | https://adapty.io/state-of-paywalls-2026/ | Directional (vendor aggregate) |
| U19 | Adapty State of Paywalls 2026 (cross-app) | Cross-category | All | mixed | App Store | Number of paywall views before purchase (not a test) | Share of buyers (first 90 days) | 60% buy on the first view, 15% on the second; 84% of 2nd+-view buyers buy within 24 h of the first view; 4% come back on another day. First-view share: Health & Fitness 40%, Photo & Video 44% | Pub. 2026-10-16 | https://adapty.io/state-of-paywalls-2026/ | Directional (vendor aggregate) |
| U20 | Blackbox (via ContextSDK) | Puzzle game | n/a (Gaming) | no | In-app | Paywalls shown during peak periods at natural pauses (context model) | Revenue | +50% during peak periods; sustained conversion lift (no figure) | Pub. 2025-12-04 | https://www.revenuecat.com/blog/growth/contextual-paywall-targeting/ ; https://contextsdk.com/blogposts/context-wins-the-hidden-third-dimension-of-paywall-targeting | Directional (vendor-reported, no method) |
| U21 | Unnamed (Superwall Bootcamp) | Not stated | n/a | unknown | Not stated | **Same as the onboarding benchmark "Paywall reach".** Only 40% of new users saw a paywall; raising reach to 80% | Total revenue | Revenue rose "linearly" (no figure) | Pub. 2026-02-06 | https://superwall.com/blog/the-paywall-growth-lever-framework-how-to-build-smarter-experiments-faster | Anecdotal |

## E. Plan upgrades, tiers and the annual switch

| ID | App | Category | Bucket | AI tag | Surface | Change | Metric | Result | Date | URL | Tier |
|---|---|---|---|---|---|---|---|---|---|---|---|
| U22 | Dark Noise | Ambient/sleep sounds | Health & Fitness (inferred) | no | App Store | Paywall shows all three plans by default (incl. lifetime) vs only annual | Initial conversions by product | Lifetime +266%; annual −30%; total initial conversions almost +10% | Pub. 2024-01-03 | https://www.revenuecat.com/blog/engineering/how-i-successfully-migrated-my-indie-app-to-revenuecat-paywalls/ | Strong (RevenueCat Experiments A/B) |
| U23 | Gu, Kannan & Ma (National Academies Press) | Books: free PDF, paid paperback | n/a (web) | no | Web | Randomized: adding a higher-priced premium tier (hardback) or a similar-priced e-book next to the paperback | Paperback revenue | Adding hardback +8.9% (compromise effect); adding e-book +21.5% (attraction effect); larger for popular or lower-priced titles | Journal of Marketing 2018-11; data Jan–Aug 2016 | https://www.ama.org/2018/12/06/winning-the-freemium-to-premium-product-wars/ | Strong (randomized field experiment) |
| U24 | Duolingo | Language learning | Education | yes (Max) | In-app store billing | Three tiers (free, Super, Max); Family plan (not a test) | Share of subscribers | Family plan 23% of subscribers, with higher retention and LTV than individual plans; Max about 5% of subscribers; Max growth came from both Super upgrades and new subscribers | Q4 2024 call, 2025-02-27 | https://www.fool.com/earnings/call-transcripts/2025/02/27/duolingo-duol-q4-2024-earnings-call-transcript/ | Directional (company-reported mix) |
| U25 | Duolingo | Language learning | Education | yes (Max) | In-app store billing | Tier mix shift; Energy replaced Hearts for free users | Subscription ARPU; paid penetration; conversion | Subscription ARPU +6% YoY, "primarily driven by more subscribers shifting to higher-priced tiers"; paid penetration 9.0% of LTM MAUs (8.6% a year earlier). Energy's iOS rollout raised DAU, time spent and subscriber conversion (no figures) | Q2 2025 letter, 2025-08-06 | https://www.sec.gov/Archives/edgar/data/1562088/000156208825000165/q2fy25duolingo6-30x25share.htm | Directional (company-reported; Energy part anecdotal) |
| U26 | ABBYY FineReader | Document scanner | Productivity (inferred) | no | In-app store billing | Paywall: annual plan highlighted with "save 71%", 14-day trial on annual, list layout vs monthly-highlighted gallery (bundled) | Plan mix; paywall view → purchase; annual revenue | Annual chosen about 2x as often; 1.37% → 1.54% per paywall view; annual subscription revenue +58.5% | Pub. 2024-05-08 | https://adapty.io/case-studies/abbyy | Directional (A/B, but bundled) |
| U27 | Superwall (cross-app) | Cross-category | All | mixed | In-app store billing | Default-selected plan switched from monthly to yearly | Yearly plan selection | 37% → 63%; among users who didn't close the paywall, 82% took the default yearly | Pub. 2024-05-13 | https://superwall.dev/blog/the-superwall-newsletter-volume-1 | Directional (vendor aggregate) |
| U28 | Memrise | Language learning | Education | no | Google Play | One week ("Back to School", Sept 2016): only a discounted annual plan offered to all users; weekly and monthly removed | Daily conversions; revenue per day | Daily conversions to Pro −20%; average revenue per day +32% (baseline not named) | 2016-11-30 | https://android-developers.googleblog.com/2016/11/learn-tips-from-memrise-to-increase-in-app-conversions-with-pricing-experiments.html | Directional (no control named) |
| U29 | Uscreen (278 video-membership creators) | Video membership | Media & Entertainment | no | Uscreen web + OTT apps (billing not stated) | Monthly → annual upsell feature for existing members | Upgrades; revenue | 5,251 members upgraded in the first 4 months of 2021; revenue $704,811 vs a projected $107,789 without upsells ("6.5x"). Counts annual cash collected up front against a projection | Not dated (2021 data) | https://www.uscreen.tv/blog/membership-upsells/ | Directional (vendor, projected baseline) |
| U30 | Churnkey research corpus | Subscription businesses | n/a (web billing) | no | Web | Annual subscribers vs matched monthly "statistical twins"; forever-percent discount on annual | Subscriber lifetime; revenue; churn | Annual: +189 days lifetime, +$146 per subscriber (50,000 matched pairs). Forever discount on annual: a further 11.2 pp churn reduction (100,000+ pairs) | Not dated | https://churnkey.co/growth/library/monthly-to-annual-conversion | Directional (observational, selection into annual) |
| U31 | Apple Retention Messaging (RevenueCat data) | Cross-category | All | mixed | App Store (cancellation sheet) | Plan-switch offers shown when subscribers cancel | Offer acceptance; cancellation rate | About 0.6% of plan-switch offers accepted vs about 1.1% of promotional offers (~1.3M plan-switch offers, Mar–Sep 2026); no measurable effect on cancellation rates across 64 apps | Pub. 2026-10-06 | https://www.revenuecat.com/blog/growth/apple-retention-messaging-benchmarks | Directional (early adopters, not causal) |

## F. AI credits, consumables and add-ons

| ID | App | Category | Bucket | AI tag | Surface | Change | Metric | Result | Date | URL | Tier |
|---|---|---|---|---|---|---|---|---|---|---|---|
| U32 | Mojo | Video/story editor | Photo & Video | yes | In-app store billing | Credit packs removed from the first paywall (subscriptions only); existing Pro AI subscribers can still top up | New subscription revenue; paywall drop-off; AI cost | +14% new subscription revenue (no baseline); no significant rise in drop-off; no meaningful rise in AI cost | Test mid-Jan 2026; pub. 2026-07-21 | https://superwall.com/case-studies/mojo | Strong (A/B, no sample size) |
| U33 | LookLab AI | AI appearance analysis | Not stated | yes | In-app store billing | Hard paywall selling 20 weekly credits at a fixed price → 3-day free trial plus a higher weekly price (price and paywall type changed together) | Campaign conversion | 8.3% → 15.0% (denominator not stated) | Pub. 2026-03-09 | https://superwall.com/case-studies/looklab-ai | Directional (bundled, sequential campaigns) |
| U34 | FunnelFox State of Web2App 2026 (cross-funnel) | Cross-category | All | mixed | Web billing | Funnels with post-purchase upsells vs without | LTV; upsell price | Upsells "lift LTV by >200%"; global median upsell price about $9.31, rising with subscription length; 3-month subscribers have the highest average upsell value | Pub. 2026-01-15 | https://funnelfox.com/state-of-web2app-2026 | Directional (cross-funnel, self-selected) |
| U35 | RevenueCat SOSA 2026 (cross-app) | Cross-category | All | AI vs non-AI | In-app store billing | AI vs non-AI apps (not a test) | Plan mix; LTV per payer | Monthly plans 59.8% of subscriptions sold in AI apps vs 26.2% in non-AI apps; Year-1 realized LTV per payer $30.16 vs $21.37 | Pub. 2026-03-14 | https://ppc.land/ai-apps-earn-41-more-per-user-but-churn-30-faster-revenuecat-finds/ | Directional (benchmark) |

Ryn VPN (U12, rewarded ads as a third access tier) and Duolingo Max (U24) also belong here.

## G. Messaging, push, frequency and second offers

| ID | App | Category | Bucket | AI tag | Surface | Change | Metric | Result | Date | URL | Tier |
|---|---|---|---|---|---|---|---|---|---|---|---|
| U36 | Memrise | Language learning | Education | no | Google Play | Free trial of a Pro mode (then a subscription offer) shown every 21st session instead of every 49th | Conversion | +50%; other conversion rates unchanged | 2016-11-30 | https://android-developers.googleblog.com/2016/11/learn-tips-from-memrise-to-increase-in-app-conversions-with-pricing-experiments.html | Directional (design not stated; "instead of" suggests before/after) |
| U37 | Wizz (via ContextSDK) | Social chat | Social & Lifestyle | no | In-app store billing | Prompt volume cut by about 50%; in-app offers timed to "receptive" moments by a context model | Primary offer flow conversion; cohort LTV | +81%; LTV about +20%. The Wizz case page shows only the headline (other fields read "0%") | Pub. 2025-12-04 | https://www.revenuecat.com/blog/growth/contextual-paywall-targeting/ ; https://contextsdk.com/case-study/wizz | Directional (vendor-reported, no method) |
| U38 | Splice | Music samples | Media & Entertainment | no | Web billing mostly (not stated) | In-app messages (8 variants tested on 400 legacy-plan users, then sent to 5,000) to move "Sounds" legacy users to new subscription plans; Content Cards | Conversion; trial-to-paid | IAM conversion 64x the historical email-only average; legacy migration conversion +114%; educational Content Card +11% trial-to-paid | Not dated | https://braze.com/customers/splice-adds-new-channels-to-lift-conversions-by-64x | Directional (historical comparison) |
| U39 | Lifesum (Phiture) | Diet tracker | Health & Fitness | no | In-app | Branching survey in-app message routing free users to meal plans that match their activities | Conversion to Premium (free users) | +12.58% (title) / +12.48% (body); no baseline | Not dated (page modified 2024-11-11) | https://phiture.com/success-stories/lifesum-blayer/ | Directional (no control stated) |
| U40 | Headspace (Phiture) | Meditation | Health & Fitness | no | In-app + push + email | CRM program: dynamic in-app modals, rich push deep-linking to packs, reactivation | Paid conversions within 1 day; W1 retention | +49% paid conversions within a day (no baseline); W1 retention +109% vs control | Not dated | https://phiture.com/success-stories/headspace-retention/ | Directional (control named only for retention) |
| U41 | Fishbrain (Phiture) | Fishing | Not verified (Sports) | no | In-app + push + email | CRM program measured against unexposed control groups (push pre-permission, in-app surveys, email) | Paid conversions within a day; W6 retention | +14.9%; W6 retention +50.6% vs control (no baselines) | Not dated (award 2019) | https://phiture.com/success-stories/fishbrain-crm/ | Directional (control stated, no baselines or sizes) |
| U42 | Blinkist (Braze) | Book summaries | Education | no | In-app notifications + Canvas | "Daily Pick" free content; engaged users routed to a flow showing premium-only content | Subscription purchases | +64% (no baseline or control) | Not dated | https://www.braze.com/customers/blinkist-case-study | Directional |
| U43 | Adapty State of Paywalls 2026 (cross-app) | Cross-category | All | mixed | App Store | Second-chance paywall shown right after the first is closed (not a test) | Conversion vs main paywall | 4% of apps use it; converts at 0.88x the main paywall (same app); beats the main paywall in 45% of apps; typical discount 38%, about 1 in 4 at 50%+ | Pub. 2026-10-16 | https://adapty.io/state-of-paywalls-2026/ | Directional (vendor aggregate) |
| U44 | Adapty library | n/a | n/a | unknown | In-app | **Same as onboarding E2.** Second-chance discount: after the onboarding paywall about +25–30% premium conversion; the same offer after the main in-app paywall cut ARPU by about half | Premium conversion; ARPU | See onboarding E2 | — | paywall-ab-test-assistant library (Adapty, MIT) | Directional |

## H. Reverse trials and free → paid nudges

| ID | App | Category | Bucket | AI tag | Surface | Change | Metric | Result | Date | URL | Tier |
|---|---|---|---|---|---|---|---|---|---|---|---|
| U45 | Unnamed image-editing SaaS (Zhang & Duan) | Image editing, freemium, ~400k DAU | Photo & Video | partly (AIGC feature launch mentioned) | Not stated | Free users randomized to a 3-day (479,317 users) or 7-day (201,271 users) premium trial, 190 countries, 2023–2024 | Trial adoption; immediate and delayed paid conversion (per user in arm) | Adoption 0.856% vs 0.951% (+11.1%); immediate paid 0.224% vs 0.241% (+7.3%, not significant); delayed paid 0.144% vs 0.205% (+42.4%). Longer-trial users responded more to feature promotions, shorter-trial users to price incentives | Frontiers in Psychology, 2025 | https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2025.1568868/full | Strong (randomized field experiment) |
| U46 | Unnamed (RevenueCat SOSA expert note) | n/a | n/a | unknown | In-app | **Same as onboarding E6.** Reverse trial after paywall dismissal (temporary premium, no card) | Freemium conversion | 0.4% → 4.5% | 2026 | https://www.revenuecat.com/state-of-subscription-apps/ | Anecdotal |
| U47 | Lumosity (Braze) | Brain training | Education | no | Email + in-app | New Year campaign: engaged free users got temporary access to premium features; a premium progress report unlocked after a 3-day streak; a follow-up sale | Purchase likelihood; engagement | Sale recipients 11% more likely to buy than non-recipients (assignment not stated); free-user engagement +170% vs the prior year's single email; streak completion +350% | Not dated | https://braze.com/customers/lumos-labs-case-study | Directional (no randomized control described) |
| U48 | Dropbox (Elena Verna, secondhand) | Cloud storage | Productivity | no | Web/desktop | Reverse trial | Free → premium conversion | "10–40%" lift "in her experience"; Dropbox said to be A/B testing it, no details | Not dated | https://userpilot.com/blog/?p=13042 | Directional (secondhand range, no test details) |
| U49 | Unnamed free-to-play game (Runge, Levav & Nair) | Mobile game | n/a (Gaming) | no | In-app purchases | Randomized cohorts with in-game price promotions on or off, about 6 months | Conversion; revenue | Both improved; no harmful intertemporal substitution (no figures on the page) | QME 2022-07 | https://www.gsb.stanford.edu/faculty-research/publications/price-promotions-freemium-app-monetization | Anecdotal (randomized, figures not on page) |
| U50 | Outseta | SaaS (web) | Business | no | Web | **Same as onboarding #66.** 7-day card-required trial vs freemium | Conversion | 35% vs 7.25% | Not dated | https://abtest.design/tests/credit-card-required-free-trial | Directional (model switch) |

---

## Count by tier

One tier per row.

| Tier | All rows | New rows | "Same as onboarding" rows |
|---|---|---|---|
| Strong | 7 (U1, U8, U13, U22, U23, U32, U45) | 7 | 0 |
| Directional | 38 | 33 | 5 (U5, U6, U7, U44, U50) |
| Anecdotal | 5 (U4, U17, U21, U46, U49) | 2 (U4, U49) | 3 (U17, U21, U46) |
| Observed | 0 | 0 | 0 |
| **Total** | **50** | **42** | **8** |

Of the 7 strong rows, only 3 are subscription apps (U1 Memrise, U22 Dark Noise, U32 Mojo); one is a freemium SaaS (U45), and three are a mobile game, Pandora and a publisher's website (U8, U13, U23).

## Notes for the skill

**What the evidence supports**

1. **A smaller free tier raises conversion and costs engagement.** Three independent sources agree in direction: a randomized game experiment (U8: fewer free levels, conversion +20%+, usage down), the NYT meter (U9: subscriptions +31%, demand −9.9%) and Pandora's ad-load experiment (U13: more friction → more paid subscriptions, fewer listening hours, and the long-run engagement cost was about 3x the one-month estimate). The skill should treat "tighten the free tier" as a trade between conversion and the engagement/virality/ad revenue the free tier produces, and should say that short tests understate the engagement cost.
2. **Gate the feature people came for, framed as a gain.** Memrise (U1, strong) shows that the copy on a locked feature matters (+28% between two benefit framings). Grammarly (U3) found the "already unlocked value, here's more" framing beat lock/peek framings, and Tapple (U2) gated the highest-intent action (opening messages). Greg (U11) went from a count cap that didn't line up with value to a gate on the feature that delivers it (sign-up-to-trial 3% → 15%, bundled).
3. **Later paywalls convert far less per view but carry real revenue.** Adapty's 2026 data (U18): 0.23% vs 0.85% per view, but 38% of subscription revenue starts after the first session (48% in Lifestyle and Utilities; 47% of monthly-plan revenue). 70% of paywall views are post-onboarding, so in-app placements are where most impressions are. Buyers decide fast (U19: 60% on the first view; 4% return another day), so a repeated upsell mostly works within a day of the first exposure.
4. **Frequency and timing cut both ways.** Showing a Pro-mode trial more often helped Memrise (U36: every 21st session vs every 49th, +50%), while Wizz gained from showing prompts half as often at better moments (U37, vendor-reported). Neither is a clean test; the skill should treat "more often" vs "better timed" as a test question, not a rule.
5. **Plan mix and tiers: defaults and anchors move the mix a lot.** Default yearly selection (U27: 37% → 63%), lifetime shown beside annual (U22: lifetime +266%, annual −30%, total +10%) and a premium decoy tier (U23: +8.9% for the middle option) all show that what sits beside a plan changes which plan sells. Duolingo's tier ladder (U24/U25) shows upgrades within paid tiers are a real ARPU lever (Family 23% of subscribers; ARPU +6% from tier shift).
6. **AI credits: keep the first purchase simple.** The one controlled credits test (U32 Mojo) found that hiding credit packs from the first paywall raised new subscription revenue 14% with no cost increase; credits work better as a top-up for existing subscribers. AI apps skew heavily monthly (U35: 59.8% vs 26.2%), which is the opening for annual-switch offers in AI apps.

**Where it flips**

- **Hard gates on habitual use.** Duolingo's offline gate (U4) and Grammarly's sticker peel (U3) both raised conversion and cut retention/DAU or raised uninstalls. Both teams pulled back. Gating something users already rely on daily is the clearest flip.
- **Moving to freemium.** One app lost more than half its subscriber conversion going freemium and reverted (#U15 b), while the cross-app benchmark favours hard paywalls by about 5x on download-to-paid (U14, self-selected). But freemium with a generous limit can raise both conversion and retention when the limit sits on value (U10 Alpe Audio).
- **Second-chance discounts by position.** Same offer: helps after the onboarding paywall, cuts ARPU by about half after the main in-app paywall (U44 = onboarding E2). Adapty's cross-app view (U43) says second-chance paywalls convert at 0.88x the main one and beat it in only 45% of apps.
- **Annual-only offers.** Removing short plans raised revenue per day but cut daily conversions 20% (U28). Pushing annual trades conversion for cash and LTV.
- **Plan-switch at cancellation is weak.** Apple's plan-switch offers in Retention Messaging were accepted 0.6% of the time (U31), about half the rate of promotional offers. The annual switch should be pitched to happy monthly subscribers, not saved for the cancel sheet.
- **Longer trials for free users pay later, not now.** The 7-day vs 3-day trial had no significant immediate effect, but delayed paid conversion rose 42% (U45). Judge reverse trials and free→paid trial nudges on delayed conversion, not the first week.

**Metric traps for the skill**

- Adapty "hard" (U16) means no close button, not a hard-paywall business model (U14). Don't mix them.
- Uscreen's "6.5x" (U29) compares upfront annual cash with a projected monthly baseline; it is not an LTV lift.
- FunnelFox's ">200% LTV" (U34) compares funnels with and without upsells, not a test.
- Churnkey's annual "twins" (U30) are matched observationally; people who choose annual differ from those who don't.

## Sources checked with no usable numbers

- RevenueCat, "AI hybrid monetization" (2026-02-05): no figures on credits or consumables. https://www.revenuecat.com/blog/growth/ai-hybrid-monetization
- RevenueCat, "Lifetime subscriptions" (2025-11-12): price multiples only (lifetime 2x–12x annual), no effect of adding lifetime. https://www.revenuecat.com/blog/growth/lifetime-subscriptions
- RevenueCat, "How to increase your annual subscription uptake" (2024-09-19) and "Annual subscriptions pros and cons" (2025-06-06): benchmarks only, no upgrade-offer results.
- RevenueCat, "Paywall redesigns case studies" (2025-03-27): all four cases are onboarding or promo paywalls.
- RevenueCat, "Monetizing without a paywall using ads" (2026-08-20): no results; cites SOSA 2026 that about 10% of apps use hybrid monetization.
- RevenueCat, "Freemium tier design" (2026-04-21): limits described (Loom, Zoom, Fitbod) without results; Slack/Spotify conversion figures cited from third parties without method.
- Superwall blog: "How to create feature-based paywalls" (2024-09-11), Newsletter Vol. 3 (2024-07-30), "Two paywall trends" (2025-10-09): no upsell results.
- Superwall case studies Linearity Curve (opt-in trial, +10% trial conversion, not an upsell), Unchaind (app-preview paywall, placement not stated), indie developer switch-back (platform migration).
- Adapty case studies list (31 cases): none about upsells, credits, annual upgrades or limits; "photo-editing-app-and-autopilot" and "productivity-app-and-autopilot" are initial-paywall pricing.
- Adapty, "Freemium to premium conversion techniques": figures without sources or methods.
- Adapty Paywall Newsletter #23: no numbers on upgrades.
- Apphud, "How to increase subscription revenue using subscription offers" (2019): no results.
- Taplytics, Spotify freemium A/B tests: no results.
- Slopes Diaries #17 (feature-gated stats screen, backdate offer): no numbers.
- Duolingo Q1 2025 shareholder letter: Max and Family named as bookings drivers, no figures.
- ContextSDK, "The hybrid pivot" (2026-01-29): hybrid buyers spend "multiple times more", no multiple.
- Pushwoosh × Qonversion: strategies, no results.
- Braze, "App subscriptions: 7 brands" (2017): describes upgrade messaging, numbers are not results.
- Phiture Blinkist "Year in Blinks" (renewal +51%, internal goals) and Headspace opt-in story: not upsell outcomes.
- Amplitude (Elena Verna) "Reverse trial" (2022-09-07): conceptual, no reverse-trial results.
- RevenueCat Community reverse-trial thread (2025-06-22): question, no data.
- Paddle/ProfitWell "annual vs monthly": no figures on page.
- Firebase Mobills case: subscription CTA copy test (+15% subscriptions) but placement not stated; not clearly an upsell.
- LBS (Lambrecht) freemium launch in games: free version launch effect on paid demand, not an upsell.
- Lazyweb/lazylanding research: YouTube Premium framing experiment observed, no outcome data.

**Could not open:** abtest.design index (robots disallowed; existing rows reused only via the onboarding library); ESMT PDF of the Runge et al. working paper (proxy refused; abstract and ESMT article used instead); PMC copy of the Frontiers paper (captcha; Frontiers full text used instead); Sub Club "How Headspace optimized revenue by gating content" (site error); lazylanding "how often do apps experiment on upsell and gating" (permission request timed out). Pandora's subscription effect size is in section 5.2 of the arXiv paper, which the fetch didn't reach.

## Biggest evidence gaps

1. **Annual-switch offers to monthly subscribers inside mobile apps.** No published in-app test with numbers. Only web/OTT (Uscreen, U29), matched-pair observation (Churnkey, U30) and cancel-sheet acceptance (U31).
2. **Family plans.** Only Duolingo's share (23%) and "higher retention and LTV" (U24). No test of a family-plan upsell.
3. **Lifetime upsell to existing subscribers.** Dark Noise (U22) tested lifetime on the paywall, not as an upsell to people already subscribed.
4. **Credit pack pricing and credit-limit size in AI apps.** One controlled test (Mojo, U32). Nothing on the size of the free credit allowance, pack sizes, or top-up prompts at zero balance.
5. **Upsell frequency caps and fatigue.** Memrise (U36) and Wizz (U37) only; no test of caps per session/day, or of long-run churn from repeated prompts.
6. **Push for upsell with a randomized holdout.** CRM case studies (U38–U42, U47) are vendor-published with no baselines.
7. **Soft vs hard feature gates inside the product** (preview/blur/limited-use vs locked). Grammarly (U3) and Duolingo (U4) give direction without numbers on the downside.
8. **Locked-feature badges** (lock icons, PRO tags in menus). Nothing published with numbers.
9. **Category coverage.** Thin for Business, Utilities (only Ryn VPN) and Social & Lifestyle; most strong rows are Education, Photo & Video and non-app experiments.


# Part 2. Benchmarks from public reports

Checked 2026-10-29/30. The citation is always the original report URL.

**Tiers**
- **Strong benchmark**: large platform dataset, defined metric, per-app medians or full distributions.
- **Directional**: numbers, but vendor claim, undefined denominator, anonymised test bands, self-reported survey, or text that disagrees with its own chart.
- **Anecdotal**: expert quote or a single company story with a number but no method.
- **Observed**: pattern share in top apps (what apps do, not what converts).

**Sources and periods (keep apart; never merge their numbers)**

| Key | Source | Period | Sample | Unit of measure | URL |
|---|---|---|---|---|---|
| SOSA | RevenueCat, State of Subscription Apps 2026 | calendar 2025 | 115k+ apps, iOS + Android + web | per install (D35 download → paid, RPI), per trial start (trial → paid), per subscription (retention), per payer (RLTV). Medians | https://www.revenuecat.com/state-of-subscription-apps |
| SOIS | Adapty, State of In-App Subscriptions 2026 | calendar 2025 | 16k+ apps, mostly App Store | per install (install → trial/paid, averages of per-app rates), per subscriber (LTV, retention) | https://adapty.io/state-of-in-app-subscriptions-report/ |
| SOP | Adapty, State of Paywalls 2026 | Oct 2025 – Sep 2026 | 78k+ paywalls, 30k+ apps, App Store only | per **paywall view** (view → paid within 30 days), per app medians. Ch. 3 = 100 Mobbin paywalls (observed, not performance) | https://adapty.io/state-of-paywalls-2026/ |
| AF | AppsFlyer, State of App Monetization 2026 | Jan 2025 – Mar 2026 | $0.9B IAP, $0.8B IAS, $7.2B IAA store revenue; gaming-heavy | per installer (ARPU), per payer (ARPPU), share of D60 revenue | https://www.appsflyer.com/resources/reports/app-marketing-monetization-report/ |
| FF | FunnelFox, State of Web2App 2026 | 2025 (published Jan 2026) | not stated | web funnels; means vs medians not stated | https://funnelfox.com/state-of-web2app-2026 |
| AAB | Adapty paywall A/B test library (anonymised bands, MIT skill) | not dated | not stated | test outcome bands | https://github.com/vkharlan-adapt/paywall-ab-test-assistant |

---

## B1. Placement: onboarding paywall vs in-app (feature, contextual, later) paywalls

| Metric | Value | Definition / slice | Source, period | Tier |
|---|---|---|---|---|
| Share of subscription revenue started in the first session vs later | **52.8% onboarding / 37.7% later paywalls / 9.5% other paths** | revenue by where the subscription started, all categories | SOP Ch. 4.1, Oct 2025–Sep 2026, https://adapty.io/state-of-paywalls-2026/ | Strong |
| Same, by category (onboarding / later / other) | Lifestyle 46.9 / **48.3** / 4.8 · Utilities 46.0 / **47.5** / 6.5 · Health & Fitness 43.9 / 35.8 / 20.3 · Productivity 61.5 / 35.1 / 3.4 · Education 59.1 / 27.9 / 13.1 · Entertainment 62.8 / 24.8 / 12.4 · Photo & Video 64.2 / 26.2 / 9.5 · Graphics & Design 66.4 / 28.3 / 5.3 | % of revenue | SOP Ch. 4.1 | Strong |
| Same, by plan | weekly 55.2 / 38.0 / 6.7 · **monthly 40.5 / 46.9 / 12.6** · annual 52.2 / 31.6 / 16.2 | % of revenue; monthly is the plan most often bought later | SOP Ch. 4.1 | Strong |
| Paywall view → paid, onboarding vs later | **0.85% vs 0.23%** (≈3.7×) | per paywall view, paid within 30 days, typical app | SOP Ch. 4.4 | Strong |
| Revenue per 1,000 views, onboarding vs later | **$170 vs $40** | per 1,000 paywall views | SOP Ch. 4.4 | Strong |
| View → paid later, by category | Lifestyle 0.31% · Graphics & Design 0.32% · Photo & Video 0.29% · H&F 0.29% · Education 0.27% · Entertainment 0.23% · Productivity 0.22% · Utilities 0.17% | per later paywall view | SOP Ch. 4.4 | Strong |
| Revenue / 1,000 later views, by category | Education $73 · Photo & Video $64 · Lifestyle $61 · Graphics & Design $49 · Entertainment $48 · H&F $48 · Productivity $31 · Utilities $28 | | SOP Ch. 4.4 | Strong |
| Share of paywall views after the first session | **7 in 10 views** come after the first session (and earn 38% of revenue) | | SOP Ch. 4.4 | Strong |
| Install → paid by placement | with trial: onboarding **1.35%** vs in-app **0.89%**; without trial: onboarding 0.82% vs in-app 0.76% | per install, average of per-app rates | SOIS, calendar 2025, https://adapty.io/state-of-in-app-subscriptions-report/ | Strong (different denominator from SOP; don't combine) |
| Apps showing a second paywall right after the first is closed | **4%** of apps; converts at **0.88×** the main paywall in the same app; beats it in 45% of apps; typical discount 38% (p25 23%, p75 50%) | 162 second-chance paywalls: 126 lower price only, 20 lower price + intro, 16 intro/promo only | SOP Ch. 4.5 | Strong |
| Paywalls in use per app | 80% of apps use 2+ paywalls; 44% use 5+; 500K+ monthly views: 72% use 5+ | | SOP Ch. 5.4 | Strong |
| Hard paywall views by placement | 57% of hard-paywall views are in onboarding vs 29% for other paywall types | hard = no close button | SOP Ch. 3.7 | Strong |
| Contextual, limit-triggered paywall (A/B) | conversion to purchase roughly **+50–60%**, significant on iOS and Android | paywall shown when a user hits a daily limit vs control | AAB, https://github.com/vkharlan-adapt/paywall-ab-test-assistant | Directional (anonymised band, n not given) |
| Other earned placements (A/B) | in-app paywall tab/icon: CR to open ~+20–25%; paywall triggered by a relevant action (language switch): ARPU ~+20%, CR ~+15% | | AAB | Directional |
| Mixed consumable + subscription cross-placement (A/B) | **lost** | | AAB | Directional |
| Second-chance discount by position (A/B) | after the **onboarding** paywall: premium conversion ~+25–30% (iOS-heavy); after the **main in-app** paywall: ARPU down by roughly half | same tactic, sign flips by position | AAB | Directional |
| Weekly paywall-on-open for free users | drove **15% of new revenue** (Mojo) | expert comment | SOSA expert takeaways, https://www.revenuecat.com/state-of-subscription-apps | Anecdotal |

## B2. Freemium vs hard paywall: conversion and retention

| Metric | Value | Definition | Source | Tier |
|---|---|---|---|---|
| D35 download → paid | **hard paywall 10.7%** (p25 6.5, p75 20.0, p90 38.7) vs **freemium 2.1%** (p25 0.8, p75 4.5, p90 8.2) | per install, median | SOSA Ch. 3 / App. G | Strong |
| RPI D14 / D60 | hard $2.32 / $3.09 vs freemium $0.27 / $0.38 | revenue per install, median | SOSA App. D | Strong |
| Y1 realized LTV per payer | hard $53.70 vs freemium $25.63 | per payer | SOSA App. E | Strong |
| 12-month retention, annual / monthly / weekly | freemium 27.7 / 8.3 / 1.3% vs hard 26.8 / 9.2 / 1.2% | per subscription, median | SOSA App. M | Strong ("paywall type changes how fast you get paid, not who stays") |
| Refund rate | freemium 2.9% vs hard 2.5% | first-period refunds, median | SOSA App. O | Strong (gap is noise per report) |
| Time to paid, freemium vs hard | Day 0 36.5 / 32.2% · Days 4–7 15.4 / 25.7% · **Week 6+ 22.9 / 15.5%** | share of paid conversions by time since install | SOSA App. H | Strong |
| Hard vs soft, same app | trial starts 4.7% hard vs 3.2% soft (+48%); direct purchases 0.50% hard vs 0.75% soft (−33%); hard wins in 57% of apps | per paywall view | SOP Ch. 1.7 | Strong |
| Hard vs soft one-year LTV | median hard $24.0 vs soft $20.0 (+21%); p90 $89.9 vs $70.0. View → payment: soft 4.85% vs hard 3.34% | LTV per subscriber | SOIS | Strong (note: view→payment favours soft here, SOP's same-app trial starts favour hard; different cuts) |
| Reverse trial after paywall dismissal | freemium conversion **0.4% → 4.5%** (temporary premium, no card) | one expert's example | SOSA expert takeaways (Steve P. Young) | Anecdotal |
| Web SaaS: freemium self-serve free → paid | good **3–5%**, great 6–8%; sales-assisted good 5–7%, great 10–15%; free trial good 8–12%, great 15–25% | survey of 1,000+ (mostly B2B SaaS) products with OpenView, Growth Unhinged, Pendo; Aug 2023 | https://www.lennysnewsletter.com/p/what-is-a-good-free-to-paid-conversion | Directional (web B2B, context only) |
| Web SaaS: free trial vs freemium | free-trial products "often 2–3× the conversion rates of freemium ones"; median time to purchase ~14 days (trial) vs 60–90 days (freemium); 5% conversion within 3 months would be a step-change from 2–3% | Kyle Poyar, citing OpenView; page dated 23 Apr 2026 | https://www.growthunhinged.com/p/your-guide-to-reverse-trials | Anecdotal |
| Airtable reverse trial | 14-day Pro trial, then default to Free; free/paid line drawn where ~80% stay, ~20% want to upgrade (rule of thumb) | | same | Anecdotal |
| Reverse trial projection | free trial (no card) ~15% trial → paid; freemium ~5% free → paid; reverse trial "may capture" both (projection, not result) | Elena Verna, orig. 7 Sep 2022, updated 3 Jun 2025 | https://www.amplitude.com/blog/reverse-trial | Anecdotal |
| Free users limited to one language (content lock) | power-user conversion +83% (Busuu, ~2017) | | https://abtest.design/tests/content-locking | Directional |

## B3. Plan mix and annual share (the base an upgrade moves from)

| Metric | Value | Definition | Source | Tier |
|---|---|---|---|---|
| Plan mix of subscriptions **sold** | monthly 41.7% · yearly 33.6% · weekly 23.2% (annual was 41.4% the prior year) | share of subscriptions sold, all categories | SOSA Ch. 4 / App. C | Strong |
| By region (W/M/Y sold) | NA 23.0/36.2/**39.7** (most annual) · MEA 25.0/**54.5**/19.2 · LATAM **29.0**/40.6/29.1 · WEU 21.7/41.0/35.3 | | SOSA App. C | Strong |
| By category (W/M/Y sold) | H&F 4.0/23.8/**68.4** · Productivity 10.7/**76.7**/12.5 · Education 6.8/29.0/58.9 · Photo & Video 31.2/17.2/51.5 · Media & Ent. 26.9/39.5/31.9 · Utilities 41.2/20.4/38.0 · Gaming 81.7/12.7/5.4 | | SOSA App. C | Strong |
| Revenue share by plan (Adapty) | weekly **62.0%** · annual 21.3% · monthly 12.0% · other 3.4% · lifetime 1.1% | share of subscription revenue, App Store | SOP App. G, Oct 2025–Sep 2026 | Strong |
| Revenue share trend (Adapty SOIS) | weekly 43.3% (2023) → 51.5% (2024) → **55.5%** (2025); annual 29.2 → 25.7 → 22.5%; monthly 21.1 → 15.0 → 11.7% | | SOIS | Strong |
| Plan lengths on the main paywall | 1: 41.4% · 2: 38.6% · 3: 18.2% · 4+: 1.8% | % of paywalls | SOP App. H | Strong |
| A/B: adding products | variant with more products won 53% of 1,022 tests (322 apps); median diff +0.02pp; 2 vs 3 won 58% | | SOP App. H | Strong |
| Pre-selection stickiness | 90% of buyers take a pre-selected weekly; 46% take a pre-selected annual; annual pre-selection doesn't hurt conversion | | SOP Ch. 2.4 / App. I | Strong |
| Annual vs monthly price ratio | median annual ≈ 3× monthly (≈75% saving) | | SOIS | Strong |
| Annual-forward layout (A/B) | ARPU **+25–40%** in winning tests | annual pre-selected, trial on annual | SOP Ch. 5.3 | Directional (range from winning tests only) |
| Lifetime next to annual (A/B) | revenue **+10–15%** | | SOP Ch. 5.3 | Directional |
| Lifetime adoption | 14.4% of apps sell lifetime; 5.6% of revenue in the typical app that sells it; 1.1% of total revenue; median lifetime $35.03 = 1.32× annual (H&F 19.9% of apps; Productivity 11.7% of revenue) | | SOP Ch. 2.5 / App. J | Strong |
| Lifetime / consumables in the mix | 63.5% of apps subscriptions-only; 23.2% add lifetime; 10.7% add consumables; 2.5% all three | % of apps | SOSA Ch. 2 / App. B | Strong |
| Tiers and family on top paywalls | 16% offer tiers (Pro, Family); 13% monthly/annual switch; 12% hide extra plans behind "View all plans"; 10% lifetime | 100 top iOS paywalls | SOP Ch. 3.2 | Observed |
| Annual retention vs monthly/weekly | 12-month retention: annual 27.5% · monthly 8.2% · weekly 1.2% | per subscription, median | SOSA Ch. 6 | Strong |
| Annual cancellations timing | 34.2% of annual cancellations happen in month 1; month 12 bump 11.1% | | SOSA App. P | Strong |

## B4. Upgrades, crossgrades, tiers, family

| Metric | Value | Source | Tier |
|---|---|---|---|
| Upgrade / downgrade / crossgrade **rates** | **No public 2025–2026 benchmark found** in SOSA, SOIS, SOP, AF, FF or Recurly's open pages. SOSA's RLTV per payer *includes* upgrades but does not break them out | SOSA methodology | Gap |
| Monthly → annual upgrade path mid-flow (A/B) | "can capture a large share of purchases on their own" (no number) | AAB | Directional |
| Upgrade-offer example (store docs) | Google's own example: 50% off the first year when switching monthly → annual, limited to monthly subscribers who haven't used the offer | https://developer.android.com/google/play/billing/subscriptions | Rule/example, not a result |
| Web2app upsells (after first purchase) | upsells average **4.07%** of total revenue; headline "+20% LTV", body "x2 revenue lift in median terms", chart ">200% LTV growth with upsells vs ~100% without" (incompatible; report doesn't reconcile) | FF, https://funnelfox.com/state-of-web2app-2026 | Directional (vendor; inconsistent text) |
| Web2app average upsell price by primary plan, US | 1 week $10.51 · 1 month $15.77 · **3 months $17.56** · 1 year $8.72; global median ≈ $9.31 | FF | Directional |
| À la carte features | Tinder prices à la carte features at the weekly-equivalent of the subscription; ML-picked single product beat showing all tiers | SOSA expert takeaways (Shawn Gong) | Anecdotal |
| Family plan share / tier mix in public filings | Duolingo Q4 FY25 and Q2 FY26 shareholder letters give no Max or Family share; paid subscribers 10.9M → 12.7M (Q2 25 → Q2 26); IAP revenue $10.4M → $8.0M (−23%) | https://www.sec.gov/Archives/edgar/data/0001562088/000162828026053299/q2fy26duolingo6-30x26share.htm | Gap for tier data |
| Weekly vs annual price-bucket LTV | one-year LTV by price bucket (low → high): weekly $6.99 → $17.48; monthly $6.99 → $19.99; annual $19.99 → $59.99 | SOIS | Strong |

## B5. AI apps, credits and hybrid monetization

| Metric | Value | Definition | Source | Tier |
|---|---|---|---|---|
| Share of apps that are AI | 27.1% (Photo & Video 61.4%, Productivity 41.1%) | | SOSA App. T | Strong |
| AI vs non-AI download → **trial start** | **8.5% vs 5.6%** | per install, within 30 days. The report's summary mislabels this as trial-to-paid | SOSA App. G | Strong |
| AI vs non-AI D35 download → paid | 2.4% vs 2.0% | per install | SOSA | Strong |
| AI vs non-AI Y1 RLTV per payer | **$30.16 vs $21.37** (+41%); M1 $18.92 vs $13.59 | per payer | SOSA App. E | Strong |
| AI vs non-AI plan mix (sold) | AI 59.8% monthly / 24.0% yearly / 15.0% weekly; non-AI 26.2 / 41.8 / 30.3 | | SOSA Ch. 8 | Strong |
| AI vs non-AI 12-month retention | annual **21.1% vs 30.7%**; monthly 6.1% vs 9.5%; weekly 1.2% vs 1.7% | per subscription, median | SOSA App. M | Strong |
| AI vs non-AI refund rate | 4.2% vs 3.5% | | SOSA | Strong |
| AI apps' monetization mix | 67.7% subs only · 17.9% + lifetime · **12.5% + consumables** · ~2% all three (non-AI: 61.9 / 25.3 / 10.0 / 2.8) | % of apps | SOSA App. B | Strong |
| Adapty AI conversion (contradicts SOSA direction on trial starts) | install → trial 5.31% (AI) vs 10.92% (all apps); trial → paid 20.60% vs 25.59%; install → direct purchase 4.20% vs 3.71% | medians, App Store-heavy | SOIS | Strong, but different sample and definition; present side by side |
| AI apps LTV (Adapty) | median install LTV $1.44 (AI) vs $0.84 (all) (+70%); annual with trial month 0 → 12: $55.1 → $66.7 (AI) vs $42.1 → $49.9 | | SOIS | Strong |
| Consumables share by category | Gaming 27.5% of apps + consumables; Social & Lifestyle 20.3%; Photo & Video 18.7%; Media 13.9% | % of apps | SOSA App. B | Strong |
| Hybrid revenue timing | non-gaming IAP: **70%** of D60 revenue on Day 1 (one-off unlocks, lifetime); non-gaming IAS: 33% D1, 60% D7, 85% D30 | cumulative share of D60 revenue | AF, Jan 2025–Mar 2026 | Strong (gaming-heavy sample, store revenue only) |
| Subscription vs IAP growth | IAS +105% YoY, IAP +29%, IAA +14% (Q1 26 vs Q1 25) | store revenue | AF | Strong |
| Non-gaming apps using subscriptions | 16% (10% IAS only + 6% IAS + IAP); text says 15.6% = 10.2% + 5.4% | % of apps with purchase revenue | AF | Strong |
| Repeat buyers | non-gaming: 9.84% one-time buyers vs 4.64% repeat (2+ purchases) within 30 days | per installer | AF | Strong |
| Hybrid as the 2026 default | qualitative: separate access (subscription) from consumption (metered/credits); heavy users pay for usage; "low single digit" % convert to premium; ARPU must rise 20–25%/yr to offset UA inflation | Thomas Petit, 5 Feb 2026 | https://www.revenuecat.com/blog/growth/ai-hybrid-monetization | Anecdotal |
| Pricing optimisation in AI apps | adds 5–15% revenue; matters most with LLM costs | Phil Carter in SOIS | SOIS expert takeaways | Anecdotal |
| Credit pack sizes, top-up conversion, credit-burn → upgrade rates | **No public benchmark found** | — | Gap |

## B6. Conversion timing (day 0 vs later)

| Metric | Value | Definition | Source | Tier |
|---|---|---|---|---|
| Trial starts on Day 0 | 78–90% by category (Business 89.9%, Education 78.5%); after Day 3 <5% | share of trial starts | SOSA Ch. 3 | Strong |
| Paid conversions on Day 0 | **50.6%** overall (Productivity 71.9%, Education 28.5%); **19.2% in Week 6+** (Travel 28.2%) | share of paid conversions by time since install | SOSA Ch. 3 / App. H | Strong |
| First purchase on Day 0 (Adapty) | **93.1%** of first purchases, 89% of first-90-day revenue; Days 8–30 2.1%, Days 31–90 1.9% | new users, first 90 days | SOP Ch. 4.2 | Strong |
| Day 0 by plan | weekly 92%, annual 88%, **monthly 81%** | | SOP Ch. 4.2 | Strong |
| Later buyers | bring 23% more 90-day revenue, but the gap nearly disappears within the same plan (they pick longer plans, buy directly) | | SOP Ch. 4.2 | Strong |
| Purchase on which paywall view | 1st view 60.2% · 2nd 15.4% · 3rd 8.9% · 4th 4.3% · 5th+ 11.2% (H&F 5th+ 24.2%, Photo & Video 25.6%) | share of buyers | SOP Ch. 4.3 | Strong |
| Come back another day to buy | 84% of 2nd+-view buyers buy within 24h of the first view; **4%** in the typical app return on another day | | SOP Ch. 4.3 | Strong |
| Install → paid timing by category (Adapty) | Day 0 share: Photo & Video 68.9%, Graphics & Design 63.9%, Productivity 47.9%, H&F 31.9%, Utilities 19.0% (Utilities 48.6% on Days 1–3); Day 31+: 6.6–11.6% | | SOIS | Strong |
| IAS revenue maturity | non-gaming IAS reaches 60% of D60 revenue by D7, 85% by D30 | | AF | Strong |
| Activation baseline (product analytics) | Day 7 return of **7%** = top 25% for activation; median Day 7 2.1% vs top 10% 12.4%; >98% of new users gone by Day 14 for half of products | 2,600+ companies, Amplitude 2025 Product Benchmark Report; 30 Sep 2025 | https://www.amplitude.com/blog/7-percent-retention-rule | Directional (cross-industry, not subscription apps) |

## B7. Messaging, offers and opt-in

| Metric | Value | Source | Tier |
|---|---|---|---|
| Experiment win rates by change type | share of tests lifting LTV / conversion: localization 62 / 45% · trial 60 / 40% · plan duration 59 / 38% · number of plans 57 / 46% · price 46 / 28% · **visual/text only 35 / 31%** (105k paywalls) | SOIS; SOP Ch. 5.2 | Strong |
| Promo offer usage | only 9.3% of apps use promo offers; on iOS among offer users: offer codes 47.6%, intro 41.2%, **promotional 8.6%, win-back 2.5%**; Google Play: intro 72.9%, codes 27.1% | SOSA Ch. 5 / App. L | Strong |
| Discounts and revenue | up to 30% off → 90% of full-price 6-month revenue; 31–60% → 70%; >60% → 46%; renewal −6.3 to −10.5pp vs full price. Win-back offers: 56% of returning subscribers on an offer still pay at 3 months vs ~1 in 10 new users who start with one | SOP Ch. 2.7 / App. L | Strong |
| Discount usage | 28.0% of first payments sold at a discount (weekly 38.6%, annual 2.6%); 17.1% of apps use discounts | SOP App. L | Strong |
| Personalisation | 24% of apps personalise paywalls; of those, by subscription status 19%, custom attributes 15%, install date 7%, acquisition source 6% | SOP Ch. 5.5 | Strong |
| Paywall copy patterns | CTA "Continue" most common (SOSA); top-100 paywalls: 56% CTAs lead with the trial; 9% use direct purchase language; headlines typically 5 words; only 2% personalised | SOSA Ch. 5; SOP Ch. 3.5–3.6 | Observed |
| Countdown timers | ≤1.4% of RevenueCat paywalls use countdowns | SOSA App. K | Observed |
| Trial-timeline copy | trial explainer screen: ARPU +12–36% in winning tests; Duolingo: a timeline (what happens, when charged, refunds) beat harder selling; letting users pick their reminder day lifted conversion | SOP Ch. 5.3; SOSA expert (Anmol Tiwari) | Directional / Anecdotal |
| Push opt-in (channel for upsell messages) | median opt-in Android 53.3%, iOS 48.85%; Jan–Dec 2025, 3B+ users | Airship 2026 benchmarks, https://www.airship.com/mobile-app-push-notification-benchmarks-for-2026/ | Directional (vendor) |
| "Upsell after value" | Android advice: upsell after value; location-based pricing (Burakova) | SOIS expert | Anecdotal |

## B8. Metric definitions (do not mix)

| Metric | Source | Denominator | Note |
|---|---|---|---|
| Download → trial (trial start rate) | SOSA | installs, trial within 30 days; trial-using apps only | the "AI 8.5% vs 5.6%" figure is this, **not** trial → paid |
| Trial → paid | SOSA | trial starts | |
| D35 download → paid | SOSA | installs, paid within 35 days | median |
| RPI D14 / D60 | SOSA | all revenue ÷ installs | |
| RLTV per payer | SOSA | paying users; includes reactivations, upgrades, one-time purchases | |
| Retention | SOSA | subscriptions (not users) | |
| View → paid | SOP | paywall views, paid within 30 days | onboarding vs later is the placement split |
| View → trial | SOP | paywall views, apps with trials only | |
| Install → trial / → paid | SOIS | installs; average of per-app rates; same across durations | onboarding vs in-app split lives here |
| LTV per subscriber | SOIS | subscribers in that plan/trial cohort | |
| ARPU / ARPPU | AF | installers / payers, within N days; store revenue only | |
| Revenue share by placement | SOP | subscription revenue by where it started | |
| Upsell share of revenue | FF | web funnel revenue | means/medians not stated |
| Churn | Recurly | subscribers per period, web-billed | no app-store data; no upgrade/downgrade rates on open pages |

## B9. Gaps

1. **Upgrade / downgrade / crossgrade rates** (monthly → annual, tier, family) on the app stores: no public 2025–2026 benchmark. RevenueCat folds upgrades into RLTV; Adapty, AppsFlyer and Recurly publish none.
2. **AI credit economics**: share of revenue from credit packs, top-up conversion, credit-limit-hit → upgrade rate, typical pack sizes. Only adoption shares (SOSA App. B) and qualitative guidance exist.
3. **Contextual vs generic in-app paywall** conversion as a platform-wide benchmark: SOP gives "later" paywalls as one bucket; the limit-trigger evidence is anonymised A/B bands (AAB).
4. **Reverse trials on mobile**: one anecdote (0.4% → 4.5%); the rest is web SaaS.
5. **Family plan and tier mix**: no public share data (Duolingo doesn't disclose; Spotify reports by product line, not reviewed).
6. **Upsell messaging channels** (in-app message, push, email) → purchase conversion: no public subscription-app benchmark. Push opt-in is the only number.
7. **Purchasely, Apphud, Superwall, Mixpanel**: no public 2025–2026 report with in-app upsell numbers found. Superwall's blog has onboarding-paywall claims (multi-page +37%) not related to in-product upsells.
8. **Recurly 2026**: open pages have no upgrade/downgrade data; the gated PDF was not reviewed.
