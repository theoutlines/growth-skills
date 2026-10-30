# In-product upsell norms by category

Collected 2026-10-30. Buckets are the RevenueCat SOSA buckets (primary App Store category), the same taxonomy as the onboarding, flow and cancel-flow skills. "AI app" is a tag, not a bucket. Finance apps have no SOSA bucket: use Utilities and say so.

Two sources use different category sets, and the tables keep them apart:
- **Adapty State of Paywalls 2026** (SOP, https://adapty.io/state-of-paywalls-2026/) uses App Store categories. Its "Lifestyle" is the nearest match to Social & Lifestyle, "Entertainment" to Media & Entertainment, and "Graphics & Design" sits next to Photo & Video. Units: per paywall view, App Store only, Oct 2025–Sep 2026.
- **RevenueCat SOSA 2026** (https://www.revenuecat.com/state-of-subscription-apps/) uses the eight buckets. Units: per subscription sold or per app, calendar 2025.

Rows and figures come from Part 2 of `evidence.md`. App examples come from `flows.md` (observed, no performance data). The "what to lean on" lines are hypotheses tied to these numbers, not tested norms.

## Quick table

| Bucket | Revenue from later paywalls (SOP, % of subscription revenue) | Later paywall view → paid; revenue per 1,000 later views (SOP) | Plan mix sold, weekly / monthly / yearly % (SOSA) | Apps adding consumables (SOSA) | Typical in-product upsell seen (`flows.md`) | What to lean on (hypothesis) |
|---|---|---|---|---|---|---|
| Health & Fitness | 35.8 | 0.29%; $48 | 4.0 / 23.8 / 68.4 | — | Persistent surfaces (crown row, settings card), tier, family and bundle offers to payers; AI coaches add a daily or weekly allowance plus credit packs | Annual-heavy already: the payer ladder (family, higher tier) and AI allowances matter more than an annual switch. H&F buyers often buy on a 5th+ paywall view (24.2%), so later surfaces carry weight |
| Education | 27.9 | 0.27%; $73 (highest per 1,000) | 6.8 / 29.0 / 58.9 | — | Gamified scarcity (hearts or energy) with several free ways out; tier ladder (Super → Max → Family); trial-ending loss lists | Highest revenue per later view: contextual gates on learning features (Memrise #U1, Busuu #U7) and a tier ladder for payers (Duolingo #U24/#U25). Don't gate the daily habit itself (#U4) |
| Productivity | 35.1 | 0.22%; $31 | 10.7 / 76.7 / 12.5 | — | AI usage metered by messages or credits; limits shown inline where the work happens; cheap entry tier next to the main one | Monthly-heavy (76.7% monthly sold): where an annual plan exists, an annual-switch card for engaged monthly payers is the obvious screen gap (no public test, hypothesis). Keep credits as a top-up for payers (#U32) |
| Utilities | 47.5 (one of the two highest) | 0.17%; $28 (lowest) | 41.2 / 20.4 / 38.0 | — | Storage meters with a cheapest-tier card; a free "clean up" step before the paid one; annual-switch banners | Nearly half the revenue starts on later paywalls but each view earns little: lean on the meter and the limit moment, not on frequent generic prompts |
| Photo & Video | 26.2 | 0.29%; $64 | 31.2 / 17.2 / 51.5 | 18.7% | Credits and packs, counters next to the generate button, top-tier gates on video, blurred example previews | Most AI-heavy bucket (61.4% of apps are AI, SOSA): a subscription with an allowance, credits as a top-up (#U32). Buyers come back: 25.6% buy on a 5th+ view |
| Media & Entertainment | 24.8 ("Entertainment") | 0.23%; $48 | 26.9 / 39.5 / 31.9 | 13.9% | Permanent upsell real estate (Premium tab, home banner), long $0 intro offers, family offers to individual payers | Free-tier size is the main lever and it costs engagement (#U9, #U13): test tightening with long horizons |
| Social & Lifestyle | 48.3 ("Lifestyle", the highest) | 0.31% (highest); $61 | — | 20.3% | Blurred "who likes you" grids, daily caps, consumables with volume pricing, a currency next to the subscription, multi-tier ladders | Gate the highest-intent action (Tapple #U2), keep consumables as an alternative for non-subscribers; tier ladders are normal here |
| Business | — | — | — | — | Quota-based soft gates that still let the action finish; value-echo modals; usage dashboards with confirm-upgrade dialogs (mostly web) | Mostly web billing: consumer law applies in full to upgrades (California ARL), and seat/plan upgrades are the main upsell |

"—" = not reported for that bucket in the source.

Other category facts:
- **Plan mix is subscriptions sold**, not the active base. A user's "70% of subscribers are monthly" is the active base: compare with care.
- **Annual share by bucket** decides how much room an annual-switch offer has: Productivity sells 12.5% yearly, Health & Fitness 68.4% (SOSA). AI apps sell 59.8% monthly vs 26.2% for non-AI apps (SOSA; #U35).
- **First-view purchase share** (SOP): 60% of buyers overall buy on the first paywall view; Health & Fitness 40%, Photo & Video 44%. Repeated in-app paywalls matter most in those two.
- **Consumables** are added by 10.7% of apps overall and 12.5% of AI apps (SOSA).
- **Day 0** carries 50.6% of paid conversions overall (Productivity 71.9%, Education 28.5%) and 19.2% arrive in week 6 or later (SOSA). Education and freemium apps have the longest tail, so later upsells have more to work with there.

## Notes by bucket

**Health & Fitness.** Daily logging is rarely hard-walled. Upsells live in persistent surfaces and in offers to people who already pay: family plans (Calm, Cal AI), higher tiers (MyFitnessPal Premium+, WHOOP showing downgrade beside upgrade) and partner bundles (Strava). AI coach apps (Bevel, Ahead) meter AI use with a daily or weekly allowance plus credit packs. The bucket is already annual-heavy (68.4% yearly sold), so an annual switch has less room than a tier or family upsell.

**Education.** The clearest gamified scarcity: hearts or energy that stop a lesson, with a trial, gems, ads, practice and waiting all offered on one sheet (Duolingo). Two flips sit here: gating offline lessons raised Plus sign-ups and cut retention and DAU (#U4), while a content lock for free users raised power-user conversion (#U7). Memrise's copy test on a locked mode is the strongest single gate result (#U1). Education earns the most per later paywall view ($73 per 1,000).

**Productivity.** AI assistants meter messages or credits and show the limit where the work happens (chat thread, agent run). Two-tier pickers with a cheap entry tier appear (ChatGPT). Team or permission features are gated with a hand-off to the web (Todoist). Monthly-heavy (76.7%), so the annual switch is the largest untested opportunity. Grammarly's "already unlocked value, here's more" framing beat lock framings (#U3, directional).

**Utilities.** Storage and capacity meters with the cheapest tier next to the meter; Google puts "clean up space" before the paid plan. Later paywalls carry 47.5% of revenue but convert at 0.17% per view, the lowest: frequency without a trigger wastes views. VPN case: rewarded ads as a third access tier (#U12, directional).

**Photo & Video.** The heaviest use of credits and packs; counters under the generate button (Canva), credit stores split into subscription and purchased credits (CapCut), blurred example previews on top-tier gates (Photoroom). Mojo's strong test: credit packs off the first paywall, kept as a top-up for subscribers (#U32). Note that CapCut shows purchased credits valid for a fixed period: on iOS, credits bought through in-app purchase may not expire (Apple 3.1.1).

**Media & Entertainment.** Permanent upsell space (Spotify's Premium tab, Suno's home banner), long $0 intro offers, family offers to individual payers (YouTube, Apple Music). The two big field experiments on free-tier size are here: the NYT meter (#U9) and Pandora's ad load (#U13). Both show conversion up and engagement down, and Pandora shows the long-run engagement cost is about 3x the one-month estimate.

**Social & Lifestyle.** The densest mix: blurred likes grids, daily caps, consumables with volume pricing, a currency as an alternative to subscribing, and multi-tier ladders (Plus/Gold/Platinum). Later paywalls carry the most revenue here (48.3%) and convert best (0.31% per view). Tapple gated opening messages, the highest-intent action (#U2, directional).

**Business.** Mostly web-billed. Quota-based soft gates let the action finish (Otter), empty states on locked tabs sell the upgrade (Universe), and confirm-upgrade dialogs state when billing starts (Rox). Web billing means consumer law applies to every upgrade (see `platform-rules.md`).
