# Platform and legal rules for in-app upsells

> **How the skill uses this file.** Background for screen flags only. The skill uses an item when it's about what a screen shows (a price, a button, a checkbox, a decline, a timer, copy). Items about billing setup, emails, reporting, records, fees or monitoring are context, not output.

Checked 2026-10-29/30. Paraphrased unless in quotes; open the link for exact wording. Law-firm and press summaries are secondary sources and are marked as such. Not legal advice: the skill should flag the risk and name the rule, not give a legal opinion. Every row is tier **rule** (binding text or official guidance) unless marked **guidance** (non-binding platform design guidance), **case** (enforcement precedent) or **pending**.

Related: the cancel-flow-teardown skill's platform rules (cancel and save flows), the onboarding-teardown skill's platform rules, and the `paywall-store-compliance` skill checklist (sign-up screen disclosures).

## 1. Apple

### 1.1 App Review Guidelines (page "Last Updated: October 16, 2026") — https://developer.apple.com/app-store/review/guidelines/

| Rule | What it says (key wording) | Upsell implication |
|---|---|---|
| 3.1.1 IAP | Unlocking "features or functionality" (subscriptions, in-game currencies, levels, premium content, full version) "must use in-app purchase" | Every feature gate, credit pack and tier upgrade sold in the app goes through IAP (US storefront exception in 3.1.1(a)/3.1.3) |
| 3.1.1 credits | "Any credits or in-game currencies purchased via in-app purchase **may not expire**", and provide a restore mechanism for restorable purchases | AI credit packs bought as consumables can't carry an expiry date. Monthly allowances included in a subscription are a different thing (3.1.2(a)), so label them as the plan's monthly allowance, not as purchased credits |
| 3.1.1 loot boxes | Randomised paid items must disclose odds before purchase | Not relevant unless "mystery" credit bundles |
| 3.1.1 non-subscription trials | A free time-based trial via a $0 non-consumable named "XX-day Trial"; before it starts, state duration, what is lost at the end, and downstream charges | Only for one-time-unlock apps |
| 3.1.1(a) / 3.1.3 external links | Link entitlements in specific regions; "these entitlements are not required for developers to include buttons, external links, or other calls to action in their **United States storefront** apps". Elsewhere apps "may not include buttons, external links, or other calls to action" to non-IAP purchasing, except via entitlements | A US upsell can offer a web-checkout button next to (or instead of) IAP. Outside the US, no steering in the upsell. Misleading marketing around the entitlement → removal |
| 3.1.2(a) ongoing value | Subscriptions must give ongoing value, last ≥7 days, work on all the user's devices | A "boost" or one-off unlock should be a consumable/non-consumable, not a subscription |
| 3.1.2(a) à la carte | "Subscriptions may be offered alongside à la carte offerings" | Selling single features or credits next to the subscription is allowed |
| 3.1.2(a) credits in subs | "Subscriptions may include consumable credits, gems, in-game currencies, etc., and you may offer subscriptions that include access to discounted consumable goods" | AI pattern "Pro includes N credits/month + cheaper top-ups" is explicitly allowed |
| 3.1.2(a) no extra tasks | Users get what they paid for "without performing additional tasks, such as posting on social media, uploading contacts, checking in to the app a certain number of times" | No "invite 3 friends to unlock what you paid for" |
| 3.1.2(a) model switch | Don't take away primary functionality existing users already paid for when moving to subscriptions | Grandfather old purchasers before gating a feature they bought |
| 3.1.2(a) bait-and-switch | Apps that "trick users into purchasing a subscription under false pretenses or engage in bait-and-switch" are removed | Upsell copy must match what the tier delivers |
| **3.1.2(b) upgrades/downgrades** | "Users should have a seamless upgrade/downgrade experience and should not be able to inadvertently subscribe to multiple variations of the same thing" | Put all tiers in **one subscription group**; never let a Pro user buy Pro Annual as a second subscription |
| 3.1.2(c) subscription info | Before asking someone to subscribe, describe clearly what they get for the price ("How much cloud storage?") and meet DPLA Schedule 2 | Upgrade screens must say what the higher tier adds (limits, credits, features), not just "Pro" |
| 3.1.3(g) | Buying "boosts" for posts in a social app, consumed in the same app, must use IAP | Promotional boosts are IAP items |
| 5.6 Code of Conduct | Apps must never "trick them into making unwanted purchases… raise prices in a tricky manner, charge for features or content that are not delivered, or engage in any other manipulative practices within or outside of the app" | The general hook for fake urgency, deceptive upgrade prompts, confusing button layouts |
| 5.6.1 | Use the provided API for rating prompts; custom review prompts disallowed | Don't bundle a rating ask into an upsell |
| 5.6.4 App Quality | "excessive refund requests" and negative reviews are signals of failing the Code of Conduct | Aggressive upsells that drive refunds put the developer account at risk |

"What must stay free?" Nothing in 3.1.2 requires a free tier. Apple's only free-access duties are: don't remove functionality already paid for (3.1.2(a)), deliver paid features without extra tasks, and Kids Category / account-deletion rules elsewhere. The HIG (below) *recommends* limited free access.

### 1.2 Auto-renewable subscriptions page — https://developer.apple.com/app-store/subscriptions/

| Topic | What it says | Upsell implication |
|---|---|---|
| Subscription groups | "people can only buy one subscription within a group at a time"; a single group is best practice "as it prevents people from accidentally purchasing multiple subscriptions". Multiple groups bill separately; switching groups resets renewal date | Tiers, durations and Family variants of the same product belong in one group |
| Levels | Rank from most (level 1) to least; several products can share a level | Ranking defines what counts as an upgrade |
| **Upgrade** | Higher level: "immediately upgraded and receive a refund of the prorated amount of their original subscription" | Upsell copy can promise instant access; don't state a refund amount (Apple computes it) |
| **Downgrade** | Lower level: continues "until the next renewal date, then is renewed at the lower level and price" | Show "Your plan changes on {renewal date}" |
| **Crossgrade** | Same level: same duration → immediate; different duration → next renewal date; for monthly-with-12-month-commitment plans, commitment and billing type also count | Monthly → annual at the **same level** takes effect at renewal, not now. If you want monthly → annual to be immediate, rank annual higher (it then becomes an upgrade) — a product decision with refund consequences |
| Introductory offers | One introductory offer per subscription group per customer | A user who had a trial on monthly can't get another intro offer on annual in the same group |
| Promotional offers | Free or discounted period for "existing or former subscribers"; up to 10 per subscription | The store-native tool for "upgrade to annual at 30% off" offers to current subscribers |
| Offer codes | One-time or custom codes; "Existing subscribers can only redeem codes that are an upgrade from or at the same level as their current subscription" | Codes can't be used to sell a downgrade |
| Win-back offers | Shown by Apple to eligible former subscribers (App Store, Settings, in-app) | For lapsed users, not for current-subscriber upsells |
| Family Sharing | Up to five family members; enabling it "can't be undone"; to offer upgrade to a Family-enabled plan, rank it so the upgrade is seamless | Family upsell = separate product in the same group with Family Sharing on |
| Existing subscribers | "make sure to verify that they're active subscribers before showing any subscription options"; show status, upgrade/crossgrade/downgrade options and a way to manage or turn off renewal; example: a promotional offer "that provides a higher service level for a discounted price" | Never show the generic paywall to an active subscriber; show an upgrade screen instead |
| StoreKit messages | Billing-issue sheet on launch (iOS 16.4+) and price-increase consent sheet can be **delayed or suppressed** via StoreKit messages "to avoid interrupting someone during a critical moment" | Don't stack your own upsell on top of a pending Apple sheet; present store messages at a calm moment |
| Price increases | Some need opt-in; if not accepted, the subscription expires at period end; you can keep existing subscribers at the old price | Moving users to a pricier tier is an upgrade they choose, not a price increase you impose |
| Monthly-billed annual (12-month commitment) | iOS 26.5, outside the US and Singapore; 12 monthly payments; cancelling stops renewal after the commitment (RevenueCat WWDC26 summary) | A new "monthly → annual commitment" upsell; disclose the commitment clearly. Source: https://www.revenuecat.com/blog/engineering/wwdc26-whats-new-for-apps (secondary) |

### 1.3 StoreKit Message — https://developer.apple.com/documentation/storekit/message (summary via Adapty docs: https://adapty.io/docs/ios-store-messages)

Message reasons: `generic`, `priceIncreaseConsent`, `billingIssue` (iOS 16.4+), `winBackOffer` (iOS 18+); API iOS 16+. StoreKit shows them automatically while the app is open unless the app defers them and calls `display` later. If the app defers and never displays, users never see the price-consent or billing notice. Tier: rule (API behaviour).

### 1.4 HIG, Apple In-App Purchase (revised 17 Sep 2026) — https://developer.apple.com/design/human-interface-guidelines/apple-in-app-purchase

Tier: guidance (App Review can cite it, but it isn't a guideline number).

| Guidance | Wording | Upsell implication |
|---|---|---|
| Experience first | "Let people experience your app before making a purchase… consider supporting limited free access to your content" | Supports freemium + contextual upsell |
| Relevant moments | "Prompt people to subscribe at relevant times, like when they near their monthly limit of free content… including prompts at relevant points throughout your app" | Apple's own endorsement of limit-triggered paywalls |
| Not to existing subscribers | "Encourage a new subscription only when someone isn't already a subscriber. Otherwise, people may believe their existing subscription has lapsed" | Suppress subscribe prompts for subscribers; show upgrade-specific copy |
| Integrated store | Present products in the app's own style | |
| Total billing price | "Display the total billing price for each in-app purchase you offer, regardless of type" | Credit packs and upgrades show the full charge, not only "per credit" or "+$X/mo" |
| Store only when payments possible | Hide the store or explain when the user can't pay (e.g. parental restrictions) | |
| Confirmation sheet | "Don't modify or replicate this sheet" | No fake confirm screens in the upsell |
| Manage in app | Upgrade, downgrade or cancel without leaving the app; show renewal date; system management UI recommended; "Always make it easy for customers to cancel" | Upgrade entry points belong in a subscription-status screen |
| Offer codes | Support in-app redemption (system screens) | |

(The older HIG onboarding page also says to ask for purchases only after people have engaged with the app: https://developer.apple.com/design/human-interface-guidelines/onboarding.)

### 1.5 US external purchase links (status)

| Item | Status | URL |
|---|---|---|
| Guideline text | US storefront apps may include buttons, links and calls to action to other purchase methods without an entitlement (3.1.1(a), 3.1.3) | https://developer.apple.com/app-store/review/guidelines/ |
| Contempt order (N.D. Cal., 30 Apr 2025) | Apple barred from charging commission on link-out purchases (it had charged 27%); Ninth Circuit upheld the contempt finding (Dec 2025); Supreme Court (Kagan) denied Apple's stay on 6 May 2026; cert petition pending; remanded to decide what commission, if any, Apple may charge. Per press, Apple was not charging on link-outs as of May 2026 | https://thenextweb.com/news/supreme-court-apple-epic-contempt-stay-denial ; https://www.iclarified.com/100784/supreme-court-rejects-apples-bid-to-pause-app-store-contempt-ruling/comments (press, secondary) |
| Implication | In the US an upsell may show "Upgrade on the web" next to IAP. The commission question is **pending**; re-check before modelling margins. Web-billed upgrades fall under consumer law in full (ROSCA, state ARLs) and outside StoreKit proration | — |

## 2. Google Play

| Rule | What it says | Upsell implication | URL |
|---|---|---|---|
| Base plans and offers | One subscription can have several base plans (auto-renewing, **prepaid**, **installments** in BR/FR/IT/ES) and offers; "you can create an upgrade offer for users who are already subscribed" | Monthly and annual can live as base plans of one subscription | https://developer.android.com/google/play/billing/subscriptions |
| Offer eligibility | New customer acquisition (Play decides); **Upgrade** (only customers who currently have another subscription of yours; configurable products); Developer determined (app decides). Up to two pricing phases per offer | Use "Upgrade" eligibility for monthly → annual or tier offers | https://www.revenuecat.com/docs/subscription-guidance/subscription-offers/google-play-offers (secondary) |
| Google's own example | "50% discount on the first year when switching from a monthly to an annual plan, … limit this offer to users subscribed to a monthly plan who haven't purchased this offer" | | https://developer.android.com/google/play/billing/subscriptions |
| Replacement modes | `WITH_TIME_PRORATION` (API default: immediate, remaining time pushes next billing date) · `CHARGE_PRORATED_PRICE` (immediate, same cycle, charge difference; upgrades only) · `CHARGE_FULL_PRICE` (immediate, full new price now) · `WITHOUT_PRORATION` (immediate, new price at renewal) · `DEFERRED` (at renewal) · `KEEP_EXISTING` (add-ons) | You choose the billing behaviour; the upsell copy must describe the chosen mode ("You'll be charged $X today" vs "starting {date}"). Note: RevenueCat's SDK defaults to `WITHOUT_PRORATION` if none is set | same; https://www.revenuecat.com/docs/subscription-guidance/managing-subscriptions |
| Google recommendations | Upgrade to pricier tier → `CHARGE_PRORATED_PRICE`; downgrade → `DEFERRED`; upgrade during trial keeping trial → `WITHOUT_PRORATION`; upgrade ending trial → `CHARGE_PRORATED_PRICE`; add-ons → `KEEP_EXISTING`. Same-subscription base-plan switches: Console default is charge immediately (`CHARGE_FULL_PRICE`) or at next billing date (`WITHOUT_PRORATION`) | | same |
| Prepaid | No auto-renew; user tops up; top-ups always `CHARGE_FULL_PRICE`; must be acknowledged (≥1 week: within 3 days) or the top-up and remaining subscription are revoked and refunded. Switching **to** prepaid allows only `CHARGE_FULL_PRICE`; installments → non-installments plan change not allowed | Prepaid passes suit "extend access" upsells in markets with low card use | same |
| In-App Messaging | `showInAppMessages` with `TRANSACTIONAL` category shows Play messages for payment issues and opt-in price increases; call on app open. Available to all developers (Sept 2026) | Same caution as StoreKit messages: don't collide with your upsell | same; https://android-developers.googleblog.com/2026/09/unlocking-Google-play-subscription-growth.html |
| New Sept 2026 (mostly Early Access) | Multi-quantity subscription purchase (seats); **usage-based billing** with auto top-up below a threshold; **mixed carts** (subscription + one-time items, upsell discounts); cross-developer hard bundles; Play Store retention offers, plan change to a lower tier in cancel flow; native win-back offers | Usage-based billing and mixed carts are the store-native routes for AI credits and bundles on Android | https://android-developers.googleblog.com/2026/09/unlocking-Google-play-subscription-growth.html |
| Subscriptions policy | Clear terms before purchase (price, billing period, auto-renewal, trial/intro terms and price after); no extra action needed to see terms; a clearly visible dismiss button; don't imply content needs a subscription when it's free; one-time benefits must not be sold as auto-renewing subscriptions; "Free trial" naming that hides a charge is a violation; offer an easy online way to cancel | Applies to every upgrade and feature-gate screen, not only the onboarding paywall | https://support.google.com/googleplay/android-developer/answer/9900533 (see `paywall-store-compliance` for item-by-item mapping) |

## 3. United States

| Rule / case | Status (Oct 2026) and upsell relevance | URL |
|---|---|---|
| ROSCA | In force. Online negative-option sales need clear disclosure of material terms before billing, express informed consent, and simple cancellation. Applies to web-billed upgrades in full | https://www.kirkland.com/publications/kirkland-alert/2026/03/ftc-restarts-subscription-rulemaking (secondary) |
| FTC Negative Option ("click-to-cancel") Rule 2024 | **Vacated** by the Eighth Circuit, 8 Jul 2025; never in effect. New ANPRM announced 11 Mar 2026; no proposed text | same |
| FTC Rule on Unfair or Deceptive Fees (junk fees) | Final rule 17 Dec 2024, effective **12 May 2025**; covers **live-event tickets and short-term lodging only**: total price incl. mandatory fees, more prominent than other pricing. Other sectors: case-by-case under Section 5. For apps: not directly binding, but "drip pricing" is an FTC dark-pattern category | https://www.ftc.gov/news-events/news/press-releases/2024/12/federal-trade-commission-announces-bipartisan-rule-banning-junk-ticket-hotel-fees |
| FTC staff report "Bringing Dark Patterns to Light" (15 Sep 2022) | Four categories: disguising ads / misleading (incl. **countdown timers on offers that aren't time-limited**), hard-to-cancel subscriptions, **burying key terms and junk fees** (drip pricing), tricking into sharing data. Guidance, not a rule | https://www.ftc.gov/news-events/news/press-releases/2022/09/ftc-report-shows-rise-sophisticated-dark-patterns-designed-trick-trap-consumers |
| California ARL (AB 2863, Bus. & Prof. Code §17600 ff.) | Effective 1 Jul 2025 for contracts entered, **amended or extended** from then. Express affirmative consent to the auto-renewal terms (in effect a separate consent); keep consent records 3 years or 1 year after termination, whichever is longer; notice of fee changes 7–30 days ahead; annual reminder; subdivision on material changes "amended significantly". Whether an in-app upgrade counts as an "amended" contract needing fresh consent is not addressed in the summaries opened: treat a tier or price change on a web-billed plan as needing clear disclosure and affirmative consent. Statute text not opened | https://ktslaw.com/insights/alert/2024/10/california-latest-automatic-renewal-law-amendments-take-effect-in-july-2025 ; https://dwt.com/insights/2024/10/ab-2863-updates-california-automatic-renewal-law (secondary) |
| **Case: FTC v. Amazon (Prime)** | Settled 25 Sep 2025, $2.5B. Alleged "confusing and deceptive user interfaces" enrolling users in Prime during checkout. Order: a clear, conspicuous button to **decline** Prime; no decline text like "No, I don't want Free Shipping" (confirmshaming); disclose cost, charge dates/frequency, auto-renewal and how to cancel during enrolment | https://www.ftc.gov/news-events/news/press-releases/2025/09/ftc-secures-historic-25-billion-settlement-against-amazon |
| **Case: FTC v. Epic Games (Fortnite)** | 19 Dec 2022: $245M refunds for dark patterns (plus $275M COPPA). "Counterintuitive, inconsistent, and confusing" button layout let one press trigger a charge (waking from sleep, loading screens, previewing items); purchases without cardholder action until 2018; accounts locked after chargebacks | https://www.ftc.gov/news-events/news/press-releases/2022/12/fortnite-video-game-maker-epic-games-pay-more-half-billion-dollars-over-ftc-allegations |
| Other cancel-side cases (Chegg, Uber One, Adobe, Match, Noom) | See the cancel-flow-teardown skill; relevant here only where an upsell hides terms (Adobe: early-termination fee in small print on annual-paid-monthly) | https://github.com/theoutlines/growth-skills/tree/main/plugins/growth-skills/skills/cancel-flow-teardown |

## 4. European Union

| Rule | Status and upsell relevance | URL |
|---|---|---|
| UCPD (2005/29/EC) Annex I blacklist, incl. **point 7**: falsely stating a product or terms are available only for a very limited time to elicit an immediate decision | In force. Per secondary summaries, a false limited-time claim is on the blacklist (unfair in all circumstances); fake countdowns on upgrade offers would fall under it. Text not opened in this pass | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32005L0029 (not opened; permission timed out on EUR-Lex) |
| **Case: ACM (NL) v. Epic Games** | 14 May 2024: €1.125M. €562,500 for **countdown timers** in the Fortnite Item Shop that implied scarcity when items stayed available at the same price; €562,000 for direct exhortations to children ("buy now", "get it now"). Press headline says the Rotterdam court upheld the fine on 14 Jan 2026 (headline only, not read) | https://nltimes.nl/node/72816 (press) |
| Omnibus Directive (EU) 2019/2161 | Since 28 May 2022: inform consumers when a price is **personalised by automated decision-making**; announced price reductions must show the lowest price of the prior 30 days (Price Indication Directive, goods; national laws may extend to services) | https://7learnings.com/blog/what-retailers-need-to-know-about-the-new-eu-consumer-protection-directive/ (secondary; EUR-Lex not opened) |
| CPC Network key principles on in-game virtual currencies | 21 Mar 2025: show prices in real money; no obscured costs via multiple currencies; **don't force buying more currency than needed** (pack-size mismatch); clear pre-contract info; withdrawal rights info (14 days where applicable); fair terms; protect minors. Scope: video games only, but the logic maps onto AI credit packs and is a stated DFA topic | https://www.reedsmith.com/en/perspectives/2025/03/qas-on-the-eu-consumer-protection-authorities-joint-guidance-paper (secondary) |
| DSA Art. 25 | Platforms must not design interfaces that deceive or manipulate; overlaps with UCPD for traders | https://www.insideprivacy.com/consumer-protection/digital-fairness-act-series-topic-4-digital-subscriptions/ (secondary) |
| **Digital Fairness Act** | **Pending: no proposal adopted** as of the latest pages; Commission work programme lists Q4 2026; impact assessment ongoing (Aug 2026). Topics: dark patterns (incl. countdown time pressure), addictive design, unfair personalisation (disclose personalised prices/offers), subscription cancel/renewal, virtual currencies obscuring real price, **pre-selected paid add-ons** | https://www.europarl.europa.eu/legislative-train/theme-protecting-our-democracy-upholding-our-values/file-digital-fairness-act ; https://www.heuking.de/en/news-events/newsletter-articles/detail/digital-fairness-act-implementation-obligations-companies-need-to-prepare-for.html |
| EU withdrawal function (Dir. 2023/2673) | From 19 Jun 2026 for online distance contracts with a withdrawal right; matters for web-billed upgrades in the EU | see the cancel-flow-teardown skill |

## 5. United Kingdom

| Rule | Status and upsell relevance | URL |
|---|---|---|
| DMCC Act 2024, Part 4 (unfair commercial practices) | In force **6 Apr 2025**. CMA can fine directly up to £300,000 or 10% of global turnover. The CMA's first cases target drip pricing, misleading time-limited sales and automatic add-on opt-ins (below). The Schedule 20 banned-practices list itself was not opened | https://www.rpclegal.com/snapshots/consumer/winter-2025/cma-launches-first-dmcca-enforcement-cases-and-finalises-price-transparency-guidance/ (secondary) |
| CMA price transparency guidance (final, 18 Nov 2025) | Mandatory fees in the headline price; subscriptions may show total cumulative cost **or** per-period cost if mandatory charges are included and the commitment is prominent; **optional extras/upsells** may sit outside the headline price but must be clear, genuinely optional and **not auto-opted-in** | same |
| CMA first DMCCA cases (18 Nov 2025) | 8 investigations: drip pricing (StubHub, viagogo, AA/BSM Driving School, Gold's Gym joining fees), **misleading time-limited sales** (Wayfair, Appliances Direct), **automatic opt-ins to add-ons** (Marks Electrical, Appliances Direct); 100 warning letters; countdown timers flagged as high-risk | same |
| **Case: CMA v. Emma Sleep** | Consent order 22 May 2026: Emma admitted infringements on countdown-timer discount claims ("Each was presented as time-limited — none were") and high-demand claims. Timers must not falsely suggest urgency, must end with the promotion, can't be reused within 28 days; was/now pricing went to trial 4 Jun 2026 | https://www.mondaq.com/uk/dodd-frank-consumer-protection-act/1796032/uk-consumer-law-revolution-emma-sleep-case-is-partly-settled-but-the-other-part-is-keeping-us-awake-at-night (secondary) |
| DMCC subscription contracts regime | From **1 Jan 2027** (draft regulations laid 19 Oct 2026): pre-contract info, reminders (e.g. 6-monthly; before a free trial or discount ends), cooling-off at start and at renewal, easy exit. How a mid-term upgrade is treated (new contract vs variation) and how the regime applies when Apple/Google is merchant of record: **not confirmed** in sources opened | https://cms.law/en/gbr/legal-updates/uk-subscription-contracts-the-government-publishes-the-missing-detail (secondary) |

## 6. Checklist for in-app upsells

Strictest common bar across the sources above. ❌ = likely rejection or legal violation; ⚠️ = reviewer discretion or regulator risk.

**Who sees it**
1. ⚠️ Active subscribers never see the "subscribe" paywall; they see an upgrade screen with their current plan named (HIG; Apple subscriptions page).
2. ❌ All tiers, durations and Family variants are in **one subscription group**; the upgrade can't create a second active subscription (3.1.2(b)).
3. ⚠️ Don't fire an upsell over a pending StoreKit / Play message (billing issue, price consent); defer one or the other.

**When**
4. ⚠️ Trigger at a relevant moment: limit reached, locked feature tapped, after value (HIG). Interruptions on launch are allowed but weakest per the evidence; the HIG frames prompts around relevant moments.
5. ⚠️ A second offer after a dismissed in-app paywall is a different bet from one after the onboarding paywall (sign flips in Adapty tests); keep it to one, with a clear decline.

**What it says**
6. ❌ State what the higher tier adds in concrete terms (limits, credits, features) (3.1.2(c); Play policy). ⚠️ Show the full billed price and period, not only a per-month or per-credit figure (HIG guidance; Play policy for terms).
7. ❌ (wrong timing) / ⚠️ (missing timing) Describe timing and charge correctly for the store mechanics: iOS upgrade = immediate with prorated refund; downgrade = at renewal; same-level duration change = at renewal. Android = the replacement mode you chose ("$X today" vs "from {date}"). Don't quote Apple's refund amount.
8. ❌ Purchased credits don't expire on iOS (3.1.1). ⚠️ Show the real-money price of each pack; no forced overbuying through pack sizes (CPC principle 3, EU, games guidance); say what happens to unused monthly allowance in a subscription.
9. ⚠️ Discount claims ("Save 40%", "was $X") are true against a plan actually offered; EU price-reduction rule (lowest price in prior 30 days) where it applies.
10. ⚠️ Personalised offers in the EU: disclose when the price is personalised by automated decision-making (Omnibus).

**How the choice looks**
11. ❌ A clear, equal-standing decline ("Not now"), no confirmshaming ("No, I don't want free shipping" was ordered out in FTC v. Amazon).
12. ❌ No fake urgency: countdowns only for real deadlines, ending when the offer ends, not reset on reopen (ACM v. Epic; CMA v. Emma; UCPD Annex I #7; Apple 5.6 as the general manipulative-practices clause, which doesn't name timers, cited from secondary sources).
13. ❌ No pre-checked paid add-ons (CMA opt-in cases; Apple 5.6; a stated DFA topic).
14. ❌ No button layouts that turn navigation into purchase; never imitate Apple's confirmation sheet (FTC v. Epic; HIG).
15. ⚠️ No "do tasks to unlock" (invite friends, post) for something already paid for (3.1.2(a)).

**Where the money goes**
16. ⚠️ US storefront: a web-checkout CTA is allowed; outside the US, no steering without an entitlement (3.1.1(a), 3.1.3). Commission on US link-outs is pending in court.
17. ⚠️ Web-billed upgrades (whether an upgrade is an "amended" contract under the California ARL is unresolved): express consent to the auto-renewal terms, consent records, fee-change notice 7–30 days, annual reminder (California ARL); UK reminders and cooling-off from 1 Jan 2027.

**After**
18. ⚠️ Show plan, price and next renewal date in the app, with upgrade/downgrade/cancel paths (HIG; Apple subscriptions page).
19. ⚠️ Watch refund rate after launching an upsell: Apple treats excessive refund requests as a Code of Conduct signal (5.6.4).

## Gaps

- EUR-Lex texts (UCPD Annex I, Omnibus 2019/2161) not opened this pass (permission timed out); cited from secondary summaries and the Directive's known structure. Re-open before quoting article numbers.
- Apple HIG JSON was read via the developer.apple.com data endpoint for "apple-in-app-purchase"; the StoreKit `Message` page body did not render, so reason values come from Adapty docs.
- California statute text not opened; whether an in-app tier upgrade is an "amended" contract requiring new ARL consent is unresolved.
- UK DMCC subscription regime: treatment of mid-term upgrades and of app-store merchant-of-record purchases not confirmed.
- Other US state ARLs (NY, MN, VA, CO) not researched.
- No case found specifically about a deceptive **subscription upgrade** prompt inside a mobile app; the nearest are FTC v. Amazon (enrolment upsell), FTC v. Epic and ACM v. Epic (in-app purchase UI and fake timers), CMA v. Emma (timers).
