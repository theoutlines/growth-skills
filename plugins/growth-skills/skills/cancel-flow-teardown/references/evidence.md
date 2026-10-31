# Cancel-flow evidence: published tests, benchmarks and gaps

Collected 2026-10-29. Every number was read on the page it comes from (WebFetch of the page; Apple docs via their `.md` rendering). Where a summary page cites another source, both URLs are listed and the figure is attributed to the one actually opened. Cite rows as **#C1, #C2 …** in a teardown. The `C` prefix keeps this list separate from the onboarding library (#1–#77); rows copied from there keep their original number in the "Same as" note and are never renumbered.

Numbers are **relative** lifts unless marked **absolute** (a rate) or **pp** (percentage points).

**Evidence strength** (same definitions as the onboarding-teardown skill):
- **strong**: controlled test (A/B, randomized field experiment, holdout) with numbers
- **directional**: numbers, but no stated method, a before/after or channel comparison, a confounded or bundled change, or a vendor-reported aggregate
- **anecdotal**: claim without numbers (including controlled tests whose numbers were not published)
- **observed**: seen in top apps or official materials, no public test

**Bucket** uses the RevenueCat SOSA taxonomy (Health & Fitness, Education, Productivity, Utilities, Photo & Video, Media & Entertainment, Social & Lifestyle, Business). "n/a" = outside the app taxonomy (news site, telecom, web SaaS). "AI app" is a tag.

**Surface** says where the change ran, because the three mobile cancel surfaces behave differently:
- **in-app → store**: screens inside the app, then a hand-off to Apple/Google subscription settings
- **store**: Apple's or Google's own cancel/billing UI (retention messaging, Play cancel flow, grace period)
- **web-billed**: the app or site runs the whole cancel flow (web2app, Stripe, Recurly, Chargebee…)

## A. Save flows: offers, surveys, friction

| # | App / org | Category | Bucket | AI? | Surface | What changed | Metric | Result | Date | Source URL | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C1 | Aftenposten | News | Media & Entertainment (nearest fit) | no | web-billed | Cancel flow cut from 5 to 3 steps; cancel button moved onto "my page"; downgrade options replaced by one holdback offer (best: 3 months for the price of 1); sharing users warned a friend loses access; 4 cancel reasons | Subscribers retained per month after starting to cancel | About 600 → almost 900 per month (+50%); old flow saved or downgraded 1 in 100 (absolute); 5,000+ changed their mind in 6 months; est. €320k/yr | Old flow 2018; article undated | https://www.inma.org/blogs/ideas/post.cfm/how-aftenposten-convinced-more-people-to-stay-by-making-it-easier-to-leave | Directional (before/after, bundled: fewer steps + new offer) |
| C2 | Star Tribune | News | n/a (news site) | no | web-billed | Online self-serve cancellation added (Dec 2021) with a few questions and a targeted offer, alongside the call centre | Save rate by channel | Online 18.5% vs call centre 8.8% (absolute). About 100k digital subscribers. The paper says online cancel did not raise cancellations (no figure) | Post 2023-01-12 | https://niemanlab.org/2023/01/the-minneapolis-star-tribune-found-that-allowing-online-cancellation-actually-helps-keep-subscribers | Directional (channel comparison, self-selected) |
| C3 | Star Tribune (vendor view) | News | n/a | no | web-billed | Same program: exit survey + conditional offers, 15 A/B test sequences in year 1 | Offer acceptance; save rate | Offer acceptance 14.6%; online stop-save 18.5%; "10% better than their call center" (unclear if relative or pp) | Undated (pandemic era) | https://info.prosperstack.com/hubfs/Case%20Studies/ProsperStack%20-%20Star%20Tribune%20Case%20Study.pdf | Directional (vendor; tests mentioned, no results per test) |
| C4 | TouchNote | Greeting-card app (web store billing) | Social & Lifestyle (nearest fit) | no | web-billed | Cancel page tested discounts, pause and downgrade; audiences split domestic/international; 40% vs 50% discount compared | Save rate | 40% discount performed "almost identically" to 50% (no figures); save rate 16% → 25% (+9 pp, +56%) within <12 months | Tests from Jul 2020 | https://chargebee.com/customers/touchnote | Directional (vendor case, no control described) |
| C5 | Wavve | Podcast clip tool (SaaS with app) | Business / Productivity (nearest fit) | no | web-billed | Cancel survey; "need a break" answers get a pause; 50% coupon; missing-feature / technical answers routed to live chat | Deflection; offer mix; churn | 2,590 entered the flow; 39% deflection; 848 accepted an offer (32%): 637 two-month pause, 116 one-month pause, 94 took 50% coupon. Monthly churn was 10–14%; "15%" churn reduction after the pause incentive | Pub. 2020-10-22 | https://churnkey.co/blog/how-wavve-cut-churn-by-2-over-two-months-with-better-cancellation-flows/ | Directional (vendor before/after). Pause was 89% of accepted offers |
| C6 | Unnamed meditation app (web2wave forum) | Meditation | Health & Fitness | unknown | web-billed | One-question survey with reason-matched offer: "too expensive" → 50% off 3 months; "don't use it enough" → 2-month pause; "missing features" → lighter plan | Saved cancellations; monthly churn | 47% of cancellations saved; monthly churn about 13% → just under 7% (absolute) | Undated forum post | https://community.web2wave.com/t/we-halved-our-churn-rate-with-custom-win-back-offers-at-cancellation/1243 | Directional (unverified forum post, unnamed app). Replies claim pause saved 39% (productivity app) and 60% of 3-month pausers reactivated (language app); same caveat |
| C7 | Amazon Prime ("Iliad" flow) | Shopping membership | n/a | no | web-billed | Four-page, six-click, fifteen-option cancel flow with "remind me later", "keep my benefits", discounted pricing pages | Prime cancellations | 14% drop in cancellations in 2017 as fewer members reached the final page | Article 2025-09-24 (BI leak 2023; FTC complaint) | https://www.fastcompany.com/91409096/amazon-iliad-flow-prime-lawsuit | Directional (leaked internal figure). This flow is the basis of the FTC case settled for $2.5B (see `platform-rules.md`): a "win" that became a legal liability |
| C29 | Coconote | AI note-taker | Productivity | yes | Save offer | Save offer at cancel: discount → 7-day trial extension | Share of cancelling users retained | 25% retained with the trial extension; discount figure not given | Pub. 2026-03 | https://www.revenuecat.com/blog/growth/brett-zack-coconote-sub-club-podcast-2026 | Directional (founder report) |

## B. Store-level retention surfaces (Apple, Google)

| # | Platform / panel | Category | Bucket | AI? | Surface | What changed | Metric | Result | Date | Source URL | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C8 | Apple Retention Messaging (Apple's own data) | Cross-category | All | mixed | store (iOS cancel confirmation page) | Developer message, image, plan switch or promotional offer shown on Apple's Confirm Cancellation page | Save rate = share who keep the subscription after reaching the cancel confirmation page | Adopters: +1.4 pp (+82%) average save rate; promotional-offer messages +5.5 pp (+223%), the highest observed. "Varying results across developers" | WWDC26 session 309 (June 2026) | https://developer.apple.com/videos/play/wwdc2026/309 ; summary https://www.revenuecat.com/blog/engineering/wwdc26-whats-new-for-apps | Directional (baseline, period and sample not stated) |
| C9 | RevenueCat panel, Apple Retention Messaging | Cross-category | All | mixed | store | Early-access apps using retention messages; 406 apps, 309 with ≥100 messages; 21.96M messages (Mar 22 – Sep 20, 2026) | Save rate = saw message and did not cancel within 24h, or took the offer | Median 16.7% (bottom quartile <10%, top quartile >27%, top 10% ≥42%) (absolute). By setup: includes plan switch 38%; text + promo offer 27%; mainly promo offer 22%; mainly text 13%. Offer acceptance: promo ~1.1% of 4.3M shown; plan switch ~0.6% of 1.3M shown. 64-app cancellation comparison: median decline around launch 3.6% for adopters vs 7.3% matched non-adopters | Pub. 2026-10-06 | https://www.revenuecat.com/blog/growth/apple-retention-messaging-benchmarks | Directional (observational; author says the 64-app gap "could easily be chance"; early adopters skew to $1M+/month apps) |
| C10 | Google Play | Cross-category | All | mixed | store (Play subscription center, reminder emails, purchase and cancellation flows) | Developers list subscription benefits, which Play shows in the cancellation flow and elsewhere | Voluntary churn | "Reducing voluntary churn by 2%" (relative vs what is not stated) | Pub. 2025-06 (I/O '25 recap) | https://android-developers.googleblog.com/2025/06/top-announcements-to-know-from-google-play-google-io-25.html | Directional (platform claim, no method) |

## C. Involuntary churn: grace period, account hold, billing messages

| # | App / platform | Category | Bucket | AI? | Surface | What changed | Metric | Result | Date | Source URL | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C11 | Google Play (developers using both features) | Cross-category | All | mixed | store | Grace period + account hold both enabled | Decline recovery rate | 10% → 33% (absolute; "more than 3x"). Involuntary = "over a third of all cancellations" on Play | Pub. 2019-04-11 | https://android-developers.googleblog.com/2019/04/optimize-your-subscriptions-with-new.html | Directional (platform comparison of adopters vs not) |
| C12 | Google Play | Cross-category | All | mixed | store | Recovery window extended from 30 to 60 days (grace + hold) | Involuntary churn on renewals | Average 10% reduction (relative) | Pub. 2025-06 | https://android-developers.googleblog.com/2025/06/top-announcements-to-know-from-google-play-google-io-25.html | Directional (platform claim) |
| C13 | Truecaller | Caller ID | Utilities | no | store + in-app | RTDN; grace period + account hold; email/push on failed payment; red alert icons in app linking to the account page; restore-window messages for users who cancelled | Recovery; resubscription | Grace/hold users recovered 40% vs 15% before (absolute); cancelled users resubscribing 20% vs 3% earlier (absolute). Baseline: 50% of Monthly Premium cancelled within 60 days; 46% voluntary / 54% involuntary | Page last updated 2020-06-26 | https://developer.android.com/stories/apps/truecaller | Directional (before/after, bundled) |

Not added as rows (secondary only): RevenueCat's 2026-04-02 post cites "Google's published data" for +57% recovery with grace period, +35% with account hold, 2x with the In-App Messaging API, and "90% of billing issues resolve within" Apple's 28-day grace period. I could not find the Google or Apple pages carrying those figures, so they stay out until the original is opened: https://www.revenuecat.com/blog/growth/google-play-billing-error-churn-how-to-fix

## D. Reminders and renewal design (what happens before the cancel tap)

| # | App / org | Category | Bucket | AI? | Surface | What changed | Metric | Result | Date | Source URL | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C14 | ShareFile | File transfer (web SaaS) | Business | no | web-billed | Pre-checked box on sign-up: "email me 3 days before my free trial expires" | Trial registrations; trial → paid | Registrations +16.4%; trial → paid 53% → 62% (absolute). Paid-search traffic split, 6 weeks, 90% confidence | Pub. 2007-06-14 | https://marketingsherpa.com/article/case-study/simple-email-cancellation-reminder-lifts | Strong (A/B; old, web) |
| C15 | Blinkist (same as onboarding #1) | Book summaries | Education | no | in-app | Trial timeline on paywall + reminder opt-in, push 2 days before trial end | Trial sign-ups; complaints; in-trial cancels | +23% trial sign-ups; −55% complaints; push opt-in 6% → 74%; −4% in-trial cancellations | Pub. 2021-01-19 | https://uxplanet.org/how-solving-our-biggest-customer-complaint-at-blinkist-led-to-a-23-increase-in-conversion-b60ad514134b | Strong (A/B) |
| C16 | Shaw Academy (same as onboarding #65) | Online courses | Education | no | web-billed | Reminder email 3 days before trial end | Sales | +14% (>99% significance) | Not dated | https://abtest.design/tests/free-trial-reminder | Strong |
| C17 | European daily newspaper (Miller, Sahni, Strulov-Shlain) | News | n/a | no | web-billed | Randomized 8-arm field experiment, 2018–2020: trial ends in auto-renew vs auto-cancel (× €0/€0.99 × 2/4 weeks); >2M potential subscribers | Take-up; subscribers; revenue | Auto-renew: subscription rate 20% higher in the first 4 months; revenue from new subscribers +21%; total new subscribers over 2 years 10% lower; 72% monthly chance of not cancelling; about half of auto-renew takers paid for unwanted months | Article 2023-03-01 | https://gsb.stanford.edu/insights/auto-renew-snags-new-subscribers-its-not-good-way-keep-them | Strong (randomized field experiment) |
| C18 | Same experiment, 2026 presentation | News | n/a | no | web-billed | Same design, reported on 1.4M paywall readers, 20 months, AEA RCT registry | Take-up; retention; revenue; engagement | Auto-renew cut readers starting any subscription by 35% (promo-period rate −41%); retention 20–38% higher per period early; cumulative revenue per reader +55% (medium run); auto-renew survivors read 62% fewer pages; total subscribers −23% after 20 months; ~49% of readers inert; 86% monthly chance an unhappy subscriber fails to cancel | Deck June 2026 | https://www.inma.org/modules/event/2026SubscriberRetention/replay/KlausMiller_INMAMCJUN26.pdf | Strong. Figures differ from #C17 (different sample cut and horizon); quote each with its source, never blend |

## E. Proactive retention and win-back

| # | App / org | Category | Bucket | AI? | Surface | What changed | Metric | Result | Date | Source URL | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C19 | Unnamed telecom (Ascarza, Iyengar, Schleicher) | Mobile carrier | n/a | no | n/a (outbound campaign) | Proactive retention campaign recommending a better-fitting plan vs no contact | Churn after 2 months | 10% vs 6% control (+4 pp) — contacting customers raised churn | Article 2015-06-11 (JMR 2016) | https://knowledge.wharton.upenn.edu/article/why-retention-plans-dont-work/ | Strong (randomized field experiment) |
| C20 | Calm | Meditation | Health & Fitness | no | push/email | Re-engagement message to dormant paying subscribers ("zombie users") vs holdout | Cancellation | Recipients cancelled at a "substantially higher" rate than holdout; a small subset re-activated. No figures published | Post 2026-01-07 | https://lifecycle-leaders.hightouch.com/p/the-one-audience-you-actually-shouldn-t-re-engage | Anecdotal (holdout test, numbers not published) |
| C21 | Unscripted | Photography business tool | Photo & Video | no | in-app (Superwall) | Reactivation paywall for previously unsubscribed active users: extra 7-day trial, name-personalised copy, renewal timeline, several plans | Trial starts; trial conversion; proceeds per user | Trial starts "over 240%"; trial conversion "over 30%"; proceeds per user from reactivated cohort "nearly doubled" | Pub. 2025-12-03 | https://superwall.com/case-studies/unscripted | Directional (compared with new users on the standard paywall, not randomized) |
| C22 | Netflix | Video streaming | Media & Entertainment | no | web-billed | Asks members with no viewing for 12 months (or 2+ years) to confirm, cancels if no reply; rejoin within 10 months keeps profiles | Share affected | "Less than half of 1%" of 182M+ members; no outcome reported | 2020-05-21 | https://techcrunch.com/2020/05/21/netflix-to-start-cancelling-inactive-accounts/ | Anecdotal (no outcome numbers). Ties to #C18 "inert subscribers" and the DFA/UK reminder rules |
| C30 | Mojo | Video and story editor | Photo & Video | no | Exit and win-back offers | Exit discounts and win-back discounts | Not stated | "Didn't perform as strongly for us" (no figures) | Pub. 2024-12 | https://www.revenuecat.com/blog/growth/guide-to-mobile-paywalls-subscription-apps | Anecdotal (no figures) |
| C31 | Unnamed (Sara Grana, Sub Club) | Not stated | Not stated | unknown | Win-back offer | Win-back offer after auto-renew is turned off | Net revenue | Users refunded, then took the offer: "net negative" (no figures) | Not stated | https://pod.wave.co/podcast/sub-club-by-revenuecat/stop-celebrating-conversion-wins-before-checking-renewals-sara-grana-yousician | Anecdotal (podcast, no figures) |

## F. Reason-based routing and goodbye design (no numbers)

| # | App / org | Bucket | Surface | What | Source URL | Evidence |
|---|---|---|---|---|---|---|
| C23 | New York Times | Media & Entertainment | web-billed | Survey routes price complaints to a cheaper plan and service complaints to chat or phone; warns a discounted rate will be lost; confirmation shows end date | https://www.get.pelcro.com/blog/subscription-retention-strategies-how-the-new-york-times-manages-subscriber-cancellations-to-reduce (2025-10-02) | Anecdotal |
| C24 | Loom ("graceful goodbye"); Strava (no acknowledgement after cancel); Audible (most 1-star reviews about cancelling) | Productivity; H&F; Media | mixed | Author's examples; Loom reports a retention improvement without a figure | https://www.revenuecat.com/blog/growth/app-cancellation-flow-best-practices (2024-11-14) | Anecdotal |

## G. Observed (no test)

| # | What | Source URL | Evidence |
|---|---|---|---|
| C25 | Spotify win-back promo: users who cancelled Individual Premium before a cutoff get 3 months for $9.99 (135 markets); first-timers get 3 months free. No results published | https://newsroom.spotify.com/tag/winback-offer/ (2022-08-15) | Observed |
| C26 | Apple HIG shows a win-back example (lapsed subscribers offered six months at 50% off) and recommends a personalised offer as an alternative to cancellation inside a branded management screen | https://developer-mdn.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/auto-renewable-subscriptions | Observed |
| C27 | In 48 apps with cancel-intent screens (401 screenshots, July 2026), a discount appeared in 30 (63%); pause 0/48; downgrade 0/48 (keyword detection in captured text) | https://www.lazyweb.com/research/are-pause-and-downgrade-save-offers-worth-building (2026-07-07) | Observed (directional sample) |
| C28 | Cancel-subscription screens were the 2nd most experimented-on screen category (371 detected experiments, vs 117 on paywalls) across ~800 apps / 276 companies | https://www.lazyweb.com/research/which-apps-experiment-most-on-cancellation (2026-07-07) | Observed (LLM-detected variations, no lift) |

## Count

31 entries (#C1–#C31).

- **Strong: 6** — #C14, #C15, #C16, #C17, #C18, #C19
- **Directional: 14** — #C1–#C13, #C21
- **Anecdotal: 4** — #C20, #C22, #C23, #C24
- **Observed: 4** — #C25–#C28 (plus 22 Mobbin flows in `flows.md`)

None of the six strong rows tests an in-app save offer on mobile. They cover reminders before renewal (#C14–#C16), auto-renew vs auto-cancel design (#C17–#C18) and proactive outreach (#C19). Every save-offer number (#C1–#C9) is directional. Treat save-offer recommendations as hypotheses to test, and say so in the teardown.

## Notes for the skill

- **Pause dominates accepted offers where it is offered**: #C5 (pause = 753 of 848 accepted offers) and the Recurly pause figures in the Benchmarks section below. But on iOS there is no store pause, and Lazyweb saw no pause in 48 apps' cancel screens (#C27). On Google Play, pause is user-initiated in the Play Store only.
- **Plan switch beats discounts on Apple's cancel page** (#C9: 38% vs 22–27% save rate), but acceptance of the offer itself is around 1% (#C9). Most of the "save" comes from people who read the message and then don't cancel within 24h. That is a soft save and may only delay the cancel. No public data on post-save retention yet.
- **Friction "wins" are legal liabilities**: #C7 (Amazon −14% cancellations) is the textbook case the FTC sued over. Do not recommend extra steps as a growth lever.
- **Auto-renew vs auto-cancel trials** (#C17, #C18): auto-renew earns more short-term revenue but fewer subscribers long-term and many inert payers. This underpins reminder rules in the UK DMCC regime and the EU DFA proposal.
- **Don't wake sleeping payers** (#C19, #C20): contacting dormant subscribers can raise cancellations. Win-back and "we miss you" nudges belong after the lapse, not to active-but-idle payers, unless tested with a holdout.
- **Don't merge**: #C2 and #C3 are the same programme from two sources; #C17 and #C18 are the same experiment reported twice. Quote one with its source.

## Sources checked that produced no usable tests

- RevenueCat win-back guide (2024-12-03) and reactivation strategy (2026-06-11): how-to, no results. https://www.revenuecat.com/blog/growth/guide-to-apple-win-back-offers ; https://www.revenuecat.com/blog/growth/app-reactivation-strategy-how-to
- RevenueCat "9 win-back campaign ideas" (2023, upd. 2024): named examples (VSCO, Backbone, Apple Music, Rise), no results. https://www.revenuecat.com/blog/growth/win-back-campaign-examples-ideas
- RevenueCat post-purchase screen (2026-05-05): SOSA day-0 stats + examples (AllTrails "we'll remind you"), no tests. https://www.revenuecat.com/blog/growth/post-purchase-screen
- Superwall Retention Messaging explainer (2026-05-08) and trial-cancel solution page: mechanics only. https://superwall.com/blog/apple-retention-messaging-one-last-conversation-before-cancel
- FunnelFox "reduce churn by 40%" (2025-07-11): the 8–40% range, the 20–30% failed-payment share and BetterMe/Simple examples are unattributed. https://blog.funnelfox.com/how-to-reduce-subscription-churn-by-40-with-custom-cancellation-flows/
- Churnkey customers page: testimonials only (e.g. "lower churn by over 40%", "33%+ → 26% churn in 8 weeks"), no method; product claim "save ~54%". https://churnkey.co/customers
- Butter Payments press release (2026-01-29): year-over-year platform totals (+56% recovered revenue), not a test. https://www.businesswire.com/news/home/20260129364045/en/Butter-Payments-Drives-56-More-Recurring-Revenue-for-Subscription-Brands-Powering-Sustainable-Growth-Through-Failed-Payment-Recovery
- Adapty grace-period guide (2023-03-02): "15–20% more subscriptions recovered" with no source. https://adapty.io/blog/how-to-handle-apple-billing-grace-period/
- Duolingo "resurrected users" (2017-08-30): learners, not subscribers; newsletter 5% → 8% resurrected share of DAU, observational. https://blog.duolingo.com/back-from-the-brink-what-duolingo-learned-about-its-resurrected-users
- Ascarza "Retention Futility" (JMR 2018): target by uplift, not churn risk. Summary page has no numbers. https://www.ama.org/2019/04/24/escarzas-retention-futility-targeting-high-risk-customers-might-be-ineffective-wins-2018-award/
- Not searched in depth (paywalled or no public archive): Lenny's Newsletter, Reforge, Sub Club episode transcripts, Growth.Design, Paddle/ProfitWell retention studies (ProfitWell's public pages now redirect to Paddle docs without data). abtest.design returned no cancel-flow tests.

# Benchmarks

Collected 2026-10-29. One source per number; never average across panels. Every row names the panel and the definition, because "save rate", "churn" and "reactivation" mean different things at each vendor.

**Panels used**
- **SOSA 2026** = RevenueCat State of Subscription Apps 2026: App Store + Google Play, 115k+ apps. https://www.revenuecat.com/state-of-subscription-apps/ 
- **RC RM** = RevenueCat Apple Retention Messaging panel, 309 apps, Mar–Sep 2026. https://www.revenuecat.com/blog/growth/apple-retention-messaging-benchmarks
- **Recurly 2026** = Recurly State of Subscriptions 2026 (released 2026-01-14): web billing only, 2,200+ merchants, 76M subscriptions, data 2021–2025, plus a consumer survey of unpublished size. https://recurly.com/resources/report/state-of-subscriptions/
- **Recurly benchmarks** = Recurly churn-rate benchmarks page, July 2026 data, web billing. https://www.recurly.com/research/churn-rate-benchmarks
- **FunnelFox 2026** = State of Web2App 2026, web-billed app funnels. https://funnelfox.com/state-of-web2app-2026
- Vendor platform claims (Churnkey, Google, Apple) are marked as such.

Web panels (Recurly, FunnelFox, Churnkey) fit **web-billed** app subscriptions. They do not describe App Store behaviour, where the cancel happens in Apple's settings.

### 1. Voluntary vs involuntary churn

| Benchmark | Value | Panel / definition | Source | Strength |
|---|---|---|---|---|
| Why subscriptions end, App Store | 82.9% voluntary / 15.2% billing error; price increases, developer cancels and pauses ≤0.5% each | SOSA 2026, share of subscription ends | SOSA 2026 | Strong benchmark |
| Why subscriptions end, Google Play | 66.3% voluntary / 32.2% billing error | SOSA 2026 | SOSA 2026 | Strong benchmark |
| Same, previous edition | Billing errors 28.2% of Play vs 15.1% of App Store cancellations (99.5M entries) | SOSA 2025 via RevenueCat blog 2025-05-21 | https://www.revenuecat.com/blog/growth/subscription-app-churn-reasons-how-to-fix | Strong benchmark (older) |
| Involuntary share on Play (2019) | "Over a third of all cancellations" | Google Play, all developers | https://android-developers.googleblog.com/2019/04/optimize-your-subscriptions-with-new.html | Platform claim |
| Web billing, all industries | Voluntary 2.34%, involuntary 1.25% (monthly or annual is inconsistent on the page; page total says 3.27%, which doesn't match the sum) | Recurly benchmarks, subscriber-level churn | Recurly benchmarks | Benchmark with known inconsistencies |
| Web billing by industry (total / voluntary / involuntary) | Digital media & entertainment 4.14 / 2.55 / 1.59; Education 4.99 / 3.30 / 1.69; SaaS 3.22 / 2.16 / 1.06 | Recurly benchmarks | Recurly benchmarks | Benchmark |
| Web billing by price ($10–25 per customer) | 4.29 / 2.99 / 1.30; involuntary falls to 0.18 above $250 | Recurly benchmarks | Recurly benchmarks | Benchmark |
| Failed payments as share of total churn | 32–38% in every industry; ~6% above $250 per customer | Recurly 2026 | Recurly 2026 | Benchmark |
| Single app | Truecaller Monthly Premium: 46% voluntary / 54% involuntary | One app (Play) | https://developer.android.com/stories/apps/truecaller | Anecdotal benchmark |

**Takeaway:** on Google Play, about one cancellation in three is a failed payment. Fix billing recovery before polishing a save offer.

### 2. Save rates (cancel-flow outcomes)

Definitions differ; never compare across rows as if they were the same metric.

| Benchmark | Value | Definition | Source | Strength |
|---|---|---|---|---|
| Apple Retention Messaging, median app | 16.7% (bottom quartile <10%, top quartile >27%, top 10% ≥42%) | Saw message on Apple's cancel page and did not cancel within 24h, or took the offer; equal weight per app | RC RM | Benchmark (early adopters, skewed to large apps) |
| Apple RM by setup | Includes plan switch 38%; text + promo 27%; mainly promo 22%; mainly text 13% | Same; an app is typed if a type is ≥15% of its messages | RC RM | Benchmark |
| Apple RM offer take-up | Promo offers ~1.1% accepted (of ~4.3M shown); plan switch ~0.6% (of ~1.3M) | Share of shown offers accepted, Jun–Sep 2026 | RC RM | Benchmark |
| Apple RM lift (Apple's data) | +1.4 pp (+82%) average; promo-offer messages +5.5 pp (+223%) | Save rate = keep subscription after reaching the cancel confirmation page; baseline not stated | https://developer.apple.com/videos/play/wwdc2026/309 | Platform claim |
| Web news, online cancel flow vs phone | 18.5% online vs 8.8% call centre | Star Tribune save rate | https://niemanlab.org/2023/01/the-minneapolis-star-tribune-found-that-allowing-online-cancellation-actually-helps-keep-subscribers | Single case |
| Web, reason-matched offers | 16% → 25% | TouchNote save rate | https://chargebee.com/customers/touchnote | Single case (vendor) |
| Web SaaS, survey + pause + coupon | 39% deflection; 32% accepted an offer | Wavve: deflection = left without cancelling; acceptance = took an offer | https://churnkey.co/blog/how-wavve-cut-churn-by-2-over-two-months-with-better-cancellation-flows/ | Single case (vendor) |
| Old-style flow with downgrade menu | 1 in 100 saved or downgraded | Aftenposten before redesign | https://www.inma.org/blogs/ideas/post.cfm/how-aftenposten-convinced-more-people-to-stay-by-making-it-easier-to-leave | Single case |
| Churnkey platform claim | "Save ~54% of customers"; discounts at the cancel moment "22 percent" (metric unclear) | Churnkey marketing, no panel size | https://churnkey.co/customers ; https://churnkey.co/growth/library/pause-offer-at-cancellation | Vendor claim (do not quote as a benchmark) |

No public panel gives save rates by offer type for **in-app pre-redirect screens** on iOS or for Google Play's new in-store retention offers (Sept 2026). See Gaps below.

### 3. Pause

| Benchmark | Value | Definition | Source | Strength |
|---|---|---|---|---|
| Pause before cancel | Brands offering it saw 337% more pauses; ~3 of 4 pausers returned "within months" | Recurly merchants (web) | Recurly 2026 | Benchmark (directional per Recurly) |
| Consumer preference | 38% prefer pausing to cancelling | Recurly consumer survey | Recurly 2026 | Survey |
| Seasonality | Pauses rise Oct–Jan; unpause rate peaks 61.9% in March 2025 | Recurly | Recurly 2026 | Benchmark |
| Resume after pause | 54% average; top orgs 89%; range 43–89% | Churnkey platform, "hundreds of orgs" | https://churnkey.co/growth/library/pause-offer-at-cancellation | Vendor claim |
| Pause as a share of all subscription ends (App Store) | ≤0.5% | SOSA 2026 | SOSA 2026 | Strong benchmark — pause is rare on stores |
| Pause rules on Google Play | Weekly: 1–3 weeks; monthly: 1–3 months; quarterly and longer not eligible; user-initiated in the Play Store only; developer opts in and sets max | Platform rule | https://www.revenuecat.com/guides/google-play-billing/cancellations-pauses-and-winback | Rule |
| Pause in iOS cancel screens | Not seen in 48 apps (0/48) | Lazyweb keyword detection, July 2026 | https://www.lazyweb.com/research/are-pause-and-downgrade-save-offers-worth-building | Observed |

### 4. Trial cancellations and when people cancel

| Benchmark | Value | Definition | Source | Strength |
|---|---|---|---|---|
| Trial cancels on day 0 | 3-day 55.4%; 7-day 39.8%; 14-day 35.7%; 30-day 31.1% | Share of all cancellations of that trial length | SOSA 2026 | Strong benchmark |
| AI vs non-AI apps | Annual retention 21.1% vs 30.7%; refund rate 4.2% vs 3.5% | AI tag vs rest | SOSA 2026 (https://www.revenuecat.com/state-of-subscription-apps/); same row as the onboarding-teardown library | Strong benchmark |
| Photo & Video trial length | 68.2% of trials are 4 days or shorter | Share of trials | SOSA 2026; same row as the onboarding-teardown library | Strong benchmark |
| Trial cancels on days 0–1 | 84% of 3-day; 64% of 7-day (7-day has a second bump on days 3–6) | Same | SOSA 2026 | Strong benchmark |
| Annual plans, month of first-year cancellation | M1 34.2%; M2 8.9%; then 4–7%/month; M12 11.1% | Share of annual cancellations in year 1 (auto-renew turned off) | SOSA 2026 | Strong benchmark |
| Web-billed plans, days after purchase (0d / 1–3d / 4–7d) | Weekly 5.1 / 5.7 / 23.6; monthly 5.2 / 3.7 / 12.4; annual 12.8 / 12.2 / 26.9 | Share of cancellations | FunnelFox 2026 | Benchmark (web) |
| Early auto-renew opt-outs, news | 72% monthly chance of not cancelling an unwanted auto-renewal (2023 summary); 86% (2026 deck) | Field experiment | #C17, #C18 above | Strong (experiment-derived) |

**Takeaway:** most "cancellations" in trials are auto-renew switched off on day 0, often as self-protection. A save screen at that moment talks to people who still have days of access left.

### 5. Why people cancel

| Benchmark | Value | Panel | Source | Strength |
|---|---|---|---|---|
| Google Play cancel survey, all categories | Cost 36.4%; not enough usage 33.7%; found better app 9.7%; technical 7.3%; other 12.9% | SOSA 2026 (Play survey answers) | SOSA 2026 | Strong benchmark |
| Same, 2025 edition | Usage 37.02%; cost 34.64%; other 11.68%; better app 9.54%; technical 7.12% | SOSA 2025 | https://www.revenuecat.com/blog/growth/subscription-app-churn-reasons-how-to-fix | Strong benchmark (older) |
| Most price-driven / usage-driven category | Productivity 44.4% cost; Travel 46.7% usage | SOSA 2026 | SOSA 2026 | Strong benchmark |
| Consumer survey (multiple answers) | Not using it enough 51%; price 45%; lost interest 32%; didn't meet expectations 23%; replaced 23%; limited content 19%; unclear billing 12% | Recurly consumer survey (size not published) | Recurly 2026 | Survey |
| Ease of cancelling | 71% prioritise being able to cancel easily; 40% rate it "extremely important" when subscribing | Recurly consumer survey | Recurly 2026 | Survey |

### 6. Reactivation and win-back

| Benchmark | Value | Definition | Source | Strength |
|---|---|---|---|---|
| Reactivation within 12 months, all categories | Weekly 9.0%; monthly 20.1%; annual 5.2% | Share of churned subscribers who resubscribe within a year | SOSA 2026 | Strong benchmark |
| By region | Monthly 18–24% (APAC 24% high, NA 18% low); annual 4.9–5.9% | SOSA 2026 | SOSA 2026 | Strong benchmark |
| By price | High-priced monthly 28.9% vs low 15.4% / mid 12.4%; high-priced annual 4.4% | SOSA 2026 | SOSA 2026 | Strong benchmark |
| Win-backs as share of new sign-ups | Nearly 1 in 4 | Recurly merchants (web) | Recurly 2026 | Benchmark |
| One app, e-receipt panel | Headspace cancellers: 4.9% resumed within 180 days (n=290); 1.5% started Calm (n=268) vs 1.34% of continuing subscribers | YipitData US e-receipts, Oct 2024 – Feb 2026 | https://ask.yipitdata.com/insights/headspace-cancelers-calm-starts | Small-sample panel |
| Win-back offer adoption, iOS | 2.5% of apps that use promo offers use win-back offers (offer codes 47.6%, intro 41.2%, promotional 8.6%) | SOSA 2026, among the 9.3% of apps using any promo offer | SOSA 2026 | Strong benchmark |
| Win-back offer adoption, Play | Promo / win-back 0% of offer users (before Play's Sept 2026 win-back launch) | SOSA 2026 | SOSA 2026 | Strong benchmark |

### 7. Billing retry and involuntary-churn recovery

| Benchmark | Value | Definition | Source | Strength |
|---|---|---|---|---|
| Apple billing retry | Up to 60 days; grace period 3 or 6 days (weekly), 3, 16 or 28 days (monthly and longer) | Platform rule | https://developer.apple.com/documentation/storekit/reducing-involuntary-subscriber-churn | Rule |
| Google Play recovery window | Grace up to 30 days, hold up to 60, combined ≤60 days; both on by default | Platform rule | https://android-developers.googleblog.com/2025/06/top-announcements-to-know-from-google-play-google-io-25.html ; https://support.google.com/googleplay/android-developer/answer/7391949 | Rule |
| Grace + hold recovery | 10% → 33% decline recovery | Google Play, 2019 | #C11 | Platform claim |
| Web renewal outcomes | 60% renew on first attempt; 17.5% fail then recover; 22.5% fail for good | FunnelFox 2026 | FunnelFox 2026 | Benchmark (web) |
| Web retry success by attempt (1–5) | 19.3%, 12.5%, 9.3%, 6.5%, 5.5% | FunnelFox 2026 | FunnelFox 2026 | Benchmark (web) |
| Web dunning | ~9 in 100 renewal attempts decline into dunning; monthly plans recover 53% of failed payments; only 23.3% of failed annual renewals recovered | Recurly 2026 | Recurly 2026 | Benchmark |

### 8. Retention Messaging adoption (Apple)

| Benchmark | Value | Source |
|---|---|---|
| Share of apps using it, by monthly App Store revenue | ≥$1M 44.4%; $100K–1M 16.9%; $10K–100K 4.7%; $1K–10K 1.3%; <$1K 0.06% | RC RM |

### 9. Monthly churn context (web)

| Industry | Avg monthly customer churn 2024 → 2025 | Source |
|---|---|---|
| Education | 6.1% → 5.7% | Recurly 2026 |
| Digital media & Entertainment | 5.6% → 5.5% | Recurly 2026 |
| Software | 3.0% → 2.9% | Recurly 2026 |
| Healthcare | 2.7% → 3.0% | Recurly 2026 |

These conflict with the Recurly benchmarks page (e.g. Digital media 4.14% total). Different period and definition; quote each with its source.

### Metric definitions to keep apart

- **Save rate (Apple / RevenueCat)**: of people who reach Apple's cancel confirmation page, the share who don't cancel within 24h or take the offer. Includes people who simply back out.
- **Save rate (Churnkey)**: sessions not ending in cancellation ÷ valid sessions (bounces excluded). https://docs.churnkey.co/cancel-flows/analytics/save-rate
- **Deflection (Chargebee/Churnkey)**: left the flow without cancelling; **acceptance**: took an offer. Wavve: 39% vs 32%.
- **Reactivation (SOSA)**: churned subscribers who resubscribe within 12 months, by plan length.
- **Win-back share (Recurly)**: share of *new sign-ups* that are former customers — a different denominator.
- **Day-0 cancellation share (SOSA)**: share of all trial cancellations that happen on day 0, not share of trials cancelled.

# Gaps

Collected 2026-10-29. What the public evidence does not cover, so the skill labels these as hypotheses instead of inventing numbers.

### Evidence gaps (biggest first)

1. **No controlled test of an in-app save screen on mobile.** All six strong rows are about reminders (#C14–#C16), auto-renew design (#C17–#C18) or proactive outreach (#C19). Every save-offer figure (discount, pause, downgrade, plan switch) is directional, mostly web-billed news or SaaS (#C1–#C6). Nothing public shows whether a pre-store save screen on iOS raises net retention or just delays the cancel.
2. **No save rates by offer type for in-app pre-redirect screens.** RevenueCat's panel covers only Apple's own cancel page (#C9). Vendors (Churnkey, ProsperStack, Chargebee) publish aggregates without panel or method.
3. **Post-save retention.** No source reports how long "saved" subscribers stay (e.g. renewal rate after accepting a discount or pause). RevenueCat notes retention offers carry `offerType` 5 so this can be measured; nobody has published it yet. The one hint is negative: a client in RevenueCat's 2025 post saw 50%-off sign-ups with a £50 lower LTV (acquisition discount, not a save offer).
4. **Google Play's new in-store retention offers, plan change and win-back offers** (Sept 2026, Early Access): announced with no data.
5. **Apple Retention Messaging methodology.** Apple's +1.4 pp / +5.5 pp (#C8) gives no baseline, period or sample. RevenueCat's matched comparison is 64 apps and possibly chance.
6. **Apple win-back offers (iOS 18+) results.** No public case study with numbers found. SOSA shows only 2.5% of offer-using iOS apps use them.
7. **Exit survey effect.** No test isolates whether a survey screen itself changes cancellation or retention, or compares mandatory vs optional, or short vs long.
8. **Friction vs one-click cancel in apps.** Only news cases (Aftenposten 5→3 steps, Star Tribune online vs phone) and Amazon's leaked −14%. No app-store test.
9. **Pause on iOS.** No store pause; no data on app-run "pause" workarounds on App Store billing (e.g. switch-plan to a cheaper tier, deferred billing via offer codes).
10. **Cancellation reminders for paid renewals** (annual-renewal reminders now required by California and, from 2027, the UK): no app test on how they change renewal or refunds. Trial reminders are covered (#C14–#C16).
11. **Category-level save data.** None. Category notes rely on cancel-reason mix (SOSA Play survey) and reactivation, not on save outcomes.
12. **AI-tag specifics.** No cancel-flow data for AI apps beyond SOSA's lower retention and higher refunds.

### Sources not opened or not found

- Google's own figures quoted by RevenueCat (grace period +57% recovery, account hold +35%, In-App Messaging 2x) and Apple's "90% of billing issues resolve within the 28-day grace period": original pages not found. Not used.
- Apple HIG current page renders only via JavaScript; quotes come from Apple's mirror `developer-mdn.apple.com`, which may be an older HIG version (sample dates from 2021).
- California AB 2863 statute text (leginfo fetch failed); rules come from Kilpatrick Townsend and DWT summaries.
- BGH I ZR 200/25 judgment text (only law-firm summaries). BGH ruling on login before the cancel button is due 5 Nov 2026.
- UK draft Regulations and 77-page DBT guidance (only CMS summaries).
- Paywalled or unsearchable: Lenny's Newsletter, Reforge, Sub Club transcripts, Growth.Design (case studies are teardowns), ProfitWell's older retention studies (pages now redirect to Paddle docs), Brightback benchmark reports (Chargebee shows them only in-product).
- Company blogs searched without cancel-flow numbers: Duolingo (learner resurrection only), Headspace, Calm (zombie-user test without figures), Spotify (win-back promo terms only), Strava, Peloton (SEC filings turned up in search but were not opened), Noom, Netflix (inactive-account policy only).

### Legal gaps

- US state ARLs beyond California (New York's 2025 amendments, Minnesota, Virginia, Colorado, others) were not researched. Some have their own save-offer and click-to-cancel rules; check before a US teardown makes a legal call.
- How the UK DMCC regime and the EU withdrawal button apply when Apple or Google is merchant of record. Sources opened discuss merchants that bill directly.
- FTC v. Uber outcome (pending) and the FTC's negative-option rulemaking (ANPRM only; no draft).
- EU Digital Fairness Act text (expected Q4 2026; not yet published on 2026-10-29).

### Mobbin gaps

- Previews show only some screens per flow; middle screens (e.g. Headspace after the survey, YouTube after "Cancel") were not seen.
- No Android flows were reviewed (Mobbin search was iOS + one web flow). Google Play's own cancel UI (survey, pause) is system UI and isn't on Mobbin.
- Not found or not searched: Canva, Tinder subscription cancel, Noom cancel, Babbel/Duolingo win-back screens after lapse, Apple's win-back offer sheet in third-party apps.
