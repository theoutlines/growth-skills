# Platform and legal rules for cancel and retention flows

> **How the skill uses this file.** Background for screen flags only. The skill uses an item when it's about what a screen shows (a price, a button, a checkbox, a decline, a timer, copy). Items about billing setup, emails, reporting, records, fees or monitoring are context, not output.

Checked 2026-10-29. Paraphrased; open the link for exact wording. Law firm summaries are secondary sources: where the statute or judgment itself was not opened, the row says so. Not legal advice; the skill should flag risk and point to the rule, not give a legal opinion.

## 1. The three mobile cancel surfaces

| Surface | Who owns the final cancel | What the app can show | Rules that bite |
|---|---|---|---|
| **iOS (App Store billing)** | Apple: Settings › Apple Account › Subscriptions, or the in-app sheet from `showManageSubscriptions(in:)` | Own screens *before* handing off; Apple's Retention Messaging on Apple's confirmation page; win-back offers after lapse | App Review 3.1.2, 5.6; HIG; consumer law on the app's own pre-screens |
| **Android (Play billing)** | Google: Play Store › Payments & subscriptions › Subscriptions | Own screens before a deep link to the Play subscription center; Play's survey, pause, resubscribe; (Sept 2026) Play retention offers and win-back offers in the Play Store | Play Subscriptions policy ("easy-to-use, online method to cancel"); consumer law |
| **Web-billed (web2app, Stripe, Recurly…)** | The app/merchant | Whole flow: survey, offers, pause, confirmation | Consumer law applies in full: ROSCA + state ARLs (US), §312k BGB (DE), UK DMCC regime (from 1 Jan 2027), EU withdrawal button |

## 2. Apple

| Rule | Plain summary | URL |
|---|---|---|
| App Review 3.1.2(a) | Subscriptions must give ongoing value; apps that "trick users into purchasing a subscription under false pretenses or engage in bait-and-switch" are removed. 3.1.2 itself says nothing about cancel-flow length | https://developer.apple.com/app-store/review/guidelines/#subscriptions |
| App Review 3.1.2(b) | Upgrades and downgrades must be seamless; users must not subscribe twice to variants of the same thing (relevant to plan-switch save offers) | same |
| App Review 4.9 (Apple Pay recurring) | Must disclose the renewal term, that it continues until cancelled, and how to cancel | https://developer.apple.com/app-store/review/guidelines/ |
| App Review 5.6 Code of Conduct | Apps must not "trick them into making unwanted purchases… raise prices in a tricky manner… or engage in any other manipulative practices"; 5.6.4 lists "excessive refund requests" as a quality signal | https://developer.apple.com/app-store/review/guidelines/#developer-code-of-conduct |
| HIG: auto-renewable subscriptions | "Always make it easy for customers to cancel an auto-renewable subscription." If manage-subscription is buried or hard to recognise, subscribers lose trust. Show a summary with the renewal date. Consider the system management UI; a branded screen around it may offer alternatives (personalised offer, other tier). Survey feedback can inform retention and win-back | https://developer-mdn.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/auto-renewable-subscriptions |
| `showManageSubscriptions(in:)` / SwiftUI `manageSubscriptionsSheet` | iOS 15+. Shows the same sheet as Settings › Apple Account › Subscriptions (view, upgrade, downgrade, cancel) without leaving the app. Not supported on Mac Catalyst / iOS-on-Mac | https://developer.apple.com/documentation/storekit/appstore/showmanagesubscriptions(in:) |
| Billing deep link | `https://apps.apple.com/account/billing` opens Manage Payments (for billing-retry prompts) | https://developer.apple.com/documentation/storekit/reducing-involuntary-subscriber-churn |
| Billing retry and grace period | Retry up to 60 days. Grace period (opt-in): 3 or 6 days for weekly; 3, 16 or 28 days for monthly and longer; full service required during grace | same |
| Retention Messaging (App Store Connect) | Message (text, optional image or offer) shown on Apple's Confirm Cancellation page, labelled "From the developer", with Cancel Subscription / Keep Subscription. ASC version "open to all" (WWDC26). Apple reviews content; "Don't upload content that is misleading or inaccurate." The App Store picks the best eligible offer; an eligible offer replaces the image. New offer type 5 (retention offer) | https://developer.apple.com/videos/play/wwdc2026/309 ; https://developer.apple.com/documentation/retentionmessaging |
| Retention Messaging (real-time API) | Access by request form. Server responds in real time (Superwall cites 700 ms) with a message, a switch plan (same group; includes the 12-month-commitment monthly plan, iOS 26.5) or a signed promotional offer. Default text message required per product and locale, or nothing shows in that locale. Visible on iOS 15.1+, macOS 14+. Must pass a sandbox performance test | https://developer.apple.com/documentation/retentionmessaging ; https://superwall.com/blog/apple-retention-messaging-one-last-conversation-before-cancel |
| Win-back offers | iOS 18+, StoreKit 2. Free or discounted offer for *churned* subscribers (expired, not auto-renewing). Eligibility only by paid duration, time since expiry, and wait between redemptions; region selectable. Shown on the App Store product page, in editorial, in Settings › Subscriptions, in-app (win-back sheet via `Message.Reason.winBackOffer`, StoreKit views) and via a direct link `apps.apple.com/win-back/<id>`. Streamlined Purchasing on by default | https://developer.apple.com/documentation/storekit/supporting-win-back-offers-in-your-app |
| Monthly-billed annual (iOS 26.5) | 12 monthly payments with a 12-month commitment; outside the US and Singapore. Can be offered as a switch plan in Retention Messaging. Cancelling stops renewal after the commitment, so disclose the commitment clearly | https://www.revenuecat.com/blog/engineering/wwdc26-whats-new-for-apps |

**What Apple allows in an app's own pre-store screens:** retention offers, a plan switch and a survey are explicitly encouraged by the HIG. Nothing in App Review sets a step limit. The risk is 5.6 (manipulative practices) and the HIG principle that cancel must be easy to find. Practical bar (the paywall-store-compliance skill uses the same bar): "Cancel anyway" reachable within one step and clearly labelled.

## 3. Google Play

| Rule | Plain summary | URL |
|---|---|---|
| Subscriptions policy: management | Apps must "clearly disclose how a user can manage or cancel their subscription" and "include in your app access to an easy-to-use, online method to cancel": a link to the Play subscription center or direct access to your cancel process, in account settings. Missing link = listed violation | https://support.google.com/googleplay/android-developer/answer/9900533 |
| Subscriptions policy: refunds | No refund for the current period on user cancel; access continues to period end; some countries allow immediate cancel with prorated refund; developers may be more generous | same |
| Free-trial disclosure | Must explain how to cancel a free trial before it converts | same |
| Cancellation survey | Play asks users who cancel in the subscription center why (cost, not enough usage, better app, technical, other + free text). Aggregates in Play Console; "Other" responses as CSV. Reason arrives in `canceledStateContext` | https://support.google.com/googleplay/android-developer/answer/7391949 ; https://www.revenuecat.com/guides/google-play-billing/cancellations-pauses-and-winback |
| Pause | User-initiated in the Play Store only (apps can't pause). Weekly: 1–3 weeks; monthly: 1–3 months; quarterly and longer not eligible. Developer opts in and sets max. Starts at period end; no access, no charge during pause | https://www.revenuecat.com/guides/google-play-billing/cancellations-pauses-and-winback |
| Restore / Resubscribe | Before expiry: "Resubscribe" (formerly Restore) in the subscription center keeps the same token; supporting it is required. After expiry: Resubscribe to the same SKU for up to 1 year, new token, on by default | https://developer.android.com/google/play/billing/subscriptions |
| Deferred billing | `subscriptionsv2.defer`: extend expiry by 1 day to 1 year, access continues, no charge; not on cancelled subs. A goodwill "free month" tool | https://www.revenuecat.com/guides/google-play-billing/cancellations-pauses-and-winback |
| Grace period + account hold | Grace up to 30 days (access kept), hold (access removed), combined ≤60 days; both on by default | https://android-developers.googleblog.com/2025/06/top-announcements-to-know-from-google-play-google-io-25.html |
| New (Sept 2026, many in Early Access) | **Retention Offers** inside the Play Store cancellation flow (developer-funded discount); **Plan Change** to a lower tier in the cancel flow; **Subscription Winback Offers** surfaced in the Play Store to lapsed users; **Dynamic Grace Period** set by ML; In-App Messaging API for all developers | https://android-developers.googleblog.com/2026/09/unlocking-Google-play-subscription-growth.html |
| Benefits listing | Subscription benefits shown in the subscription center, reminder emails, purchase and cancel flows | https://android-developers.googleblog.com/2025/06/top-announcements-to-know-from-google-play-google-io-25.html |

## 4. United States

| Rule | Status (Oct 2026) and what it means for save flows | URL |
|---|---|---|
| FTC Negative Option ("Click-to-Cancel") Rule 2024 | Vacated by the Eighth Circuit on 8 July 2025 (procedural grounds); never took effect. Its save-offer limits (ask before showing offers) are not law | https://www.kirkland.com/publications/kirkland-alert/2026/03/ftc-restarts-subscription-rulemaking |
| FTC new rulemaking | ANPRM sent to OIRA 30 Jan 2026, announced 11 Mar 2026. No proposed text; a final rule is "likely years away" | same; https://www.goodwinlaw.com/en/insights/publications/2026/02/alerts-practices-ba-ftcs-click-to-cancel-rule-gets-new-life |
| ROSCA (federal statute) | In force. Requires "simple mechanisms" to stop recurring charges for online negative-option sales; the FTC enforces it case by case. Since Jan 2025: 5 new negative-option cases, 6 settlements | same |
| California ARL (AB 2863, Bus. & Prof. Code §17600 ff.) | Effective 1 July 2025 for contracts entered, amended or extended from then. Online save offers allowed **only if** a "prominently located and continuously and proximately displayed direct link" or "click to cancel" button is shown at the same time. Phone: tell the consumer they can cancel at any time by saying "cancel". Annual reminder (what, how often, how much, how to cancel). Price-change notice 7–30 days ahead. Covers free-to-paid conversions. Statute text not opened (leginfo fetch failed); per Kilpatrick Townsend and DWT summaries | https://ktslaw.com/insights/alert/2024/10/california-latest-automatic-renewal-law-amendments-take-effect-in-july-2025 ; https://dwt.com/insights/2024/10/ab-2863-updates-california-automatic-renewal-law |
| Other state ARLs | Not researched in this pass (e.g. New York, Minnesota, Virginia, Colorado). See Gaps in `evidence.md` | — |

### US enforcement cases (what regulators called out)

| Case | Date / outcome | Cancel-flow conduct alleged or ordered | URL |
|---|---|---|---|
| FTC v. Amazon (Prime) | Settled 25 Sep 2025: $2.5B ($1B civil penalty + $1.5B refunds) | "Iliad" cancel flow: 4 pages, 6 clicks, 15 options, discount pages, "remind me later". Order: cancel must not be "difficult, costly, confusing or time consuming"; clear decline option | https://abc7news.com/post/amazon-pay-25-billion-settle-ftc-allegations-duped-customers-enrolling-prime/17881451/ ; https://www.fastcompany.com/91409096/amazon-iliad-flow-prime-lawsuit |
| FTC v. Chegg | 15 Sep 2025: $7.5M | Cancel buried in menus; multi-step retention flows; **default "pause"**, **mandatory surveys**, prominent keep/pause buttons; mobile users had to use desktop until early 2023; ~200k post-cancel charges. Order: cancel at least as easy as enrolment; charges stop immediately | https://www.goodwinlaw.com/en/insights/publications/2026/02/alerts-practices-ba-ftcs-click-to-cancel-rule-gets-new-life ; https://www.dglaw.com/ftc-lessons-learned-cheggs-7-5-million-rosca-settlement/ |
| FTC + 21 states + DC v. Uber (Uber One) | Filed 21 Apr 2025, amended 15 Dec 2025; pending | Cancellation took up to 23 screens and 32 actions; "cancel anytime" claims; charges before trial end | https://www.goodwinlaw.com/en/insights/publications/2026/02/alerts-practices-ba-ftcs-click-to-cancel-rule-gets-new-life |
| DOJ/FTC v. Adobe | Settled 13 Mar 2026: $150M ($75M cash + $75M free services) | Early-termination fee hidden in small print; "complex and challenging" cancellation; ROSCA simple-mechanism count | https://www.pymnts.com/legal/2026/adobe-ends-federal-subscription-lawsuit-with-150-million-settlement-package |
| FTC v. Match Group | Aug 2025: $14M | Order: simple, reachable way to end accounts; stop penalising chargeback users | https://www.loeb.com/en/insights/passle/2025/08/match-groups-14-million-lesson-even-without-clicktocancel-subscription-companies-cant-play-hard-to-g |
| FTC v. LA Fitness | Filed 20 Aug 2025 | In-person / certified-mail-only cancellation; forms only via web login, not the app | Goodwin, above |
| Noom (class action, not FTC) | Settled Feb 2022: $56M + $6M credits | Cancel only via the in-app virtual coach; agreed to add a cancel button on the account page and separate auto-renew consent | https://www.hunton.com/privacy-and-cybersecurity-law-blog/2022/02/22/fitness-app-agrees-to-pay-56-million-to-settle-class-action-alleging-dark-pattern-practices/ |

## 5. European Union and Germany

| Rule | Status and what it means for save flows | URL |
|---|---|---|
| Germany §312k BGB "Kündigungsbutton" | In force since 1 July 2022. Cancel button labelled "Verträge hier kündigen" (or equally unambiguous), leading to a confirmation page with a "jetzt kündigen" button; the page asks only type of cancellation, identity, contract and date. OLG Hamburg (26 Sep 2024): "Kündigungsabsicht abschicken" is not enough. KG Berlin (21 Jan 2025): button reachable from the homepage and every subpage. If non-compliant, the consumer can cancel any time without notice. **Login before the button: BGH ruling due 5 Nov 2026**; until then Händlerbund advises removing login prompts (law-firm advice, not settled law) | https://www.haendlerbund.de/de/ratgeber/recht/kuendigungsbutton-nach-312k-bgb |
| BGH I ZR 200/25 (16 July 2026) | Confirmation page must be strictly about submitting the cancellation: **no retention offers on it** (pause, discounts, contract changes, "alternatives to cancellation"; Händlerbund adds satisfaction surveys and customer-service references); the button must lead directly to it; the data fields allowed are exhaustive. Alternatives may be shown **after** the cancellation is submitted, or through other channels. Per MTR Legal and Händlerbund summaries, judgment not opened | https://www.mtrlegal.com/bgh-urteil-zum-kuendigungsbutton-klaert-ablauf-ohne-ablenkung/ |
| EU withdrawal function (Directive 2023/2673) | Applies from 19 June 2026 to B2C online distance contracts with a withdrawal right: a function labelled "withdraw from the contract here" (or equivalent), two-step confirmation, automatic confirmation email, available for the 14-day withdrawal period | https://www.arnoldporter.com/en/perspectives/advisories/2026/05/eu-withdrawal-button-uk-subscription-rules-and-data-protection-risks-for-us-online-sellers |
| UCPD guidance / DSA Art. 25 | Making cancellation unreasonably hard may be unfair; "cancelling should be as easy as subscribing". Platforms can't use designs that make cancelling harder than subscribing | https://www.insideprivacy.com/consumer-protection/digital-fairness-act-series-topic-4-digital-subscriptions/ |
| France, Netherlands | Cancel through the same channel used to subscribe | same |
| Digital Fairness Act | Not adopted. Commission work programme 2026 lists it for Q4 2026. Ideas floated: cancel buttons, termination confirmations, auto-renew off by default with reminders, express consent before a free trial converts, limits on taking card details for free trials | https://www.europarl.europa.eu/legislative-train/theme-protecting-our-democracy-upholding-our-values/file-digital-fairness-act |

## 6. United Kingdom (DMCC Act 2024, Part 4 Ch. 2: subscription contracts)

| Item | Status and detail | URL |
|---|---|---|
| Commencement | DBT consultation response 2 Apr 2026 (then: spring 2027); brought forward to **1 January 2027** for contracts entered from that date. Draft Consumer Subscription Contracts (Cancellation and Information) Regulations 2026 laid 19 Oct 2026; needs approval by both Houses | https://cms.law/en/gbr/legal-updates/uk-subscription-contracts-the-government-publishes-the-missing-detail ; https://www.subscriptioninsider.com/blog/uk-accelerates-subscription-rules-to-january-2027-shortening-compliance-runway-news |
| Exit | End at any time (reg. 32); straightforward, no steps not reasonably necessary; online sign-up → online exit (an email address alone is not enough); end-of-contract notice within 24h for online exit | CMS 2026-10-23, above |
| Retention offers and surveys | Permitted, but "should not prolong exit"; feedback requests must be optional | same |
| Reminders | Durable medium, clearly a reminder, more prominent than other content; e.g. every 6 months for monthly payers; before a free trial or discount ends; push notifications and generic emails unlikely to be enough | same |
| Cooling-off | 14 days at start and again at renewal (after a free trial ends, or after a 12-month+ renewal); extended up to 12 months if not explained | https://cms.law/en/gbr/legal-updates/cancel-culture-uk-subscription-contracts-regime-takes-shape |
| App stores | Not covered by the sources opened: how the regime applies when Apple or Google is the merchant of record. See Gaps in `evidence.md` | — |

## 7. What this means for a save flow (checklist for the skill)

The strictest common bar across the opened sources:

1. **Findable**: a "Manage / Cancel subscription" entry in account settings, labelled plainly (Play policy, HIG, Noom, Chegg).
2. **Same channel**: web sign-up → web cancel (California, UK, FR/NL, Chegg). For store-billed apps the store's own cancel is the channel; a one-tap hand-off to it (`showManageSubscriptions`, Play deep link) is good practice (HIG), not a legal requirement in the sources opened, and how these laws apply when Apple or Google is merchant of record is an open question (see Gaps).
3. **Cancel stays visible next to any offer**: California requires a "click to cancel" link shown alongside the save offer. Germany (BGH 2026, per law-firm summaries; judgment not opened) bars offers on the §312k confirmation page; alternatives go before the cancel button or after submission.
4. **One offer, not a maze**: no regulator sets a number, but Amazon (4 pages, 6 clicks, 15 options) and Uber (up to 23 screens, 32 actions) are the cautionary cases. The UK says offers must not prolong exit. Practical bar: at most one save screen, then cancel.
5. **Surveys optional**: Chegg's mandatory surveys were cited; UK guidance says feedback must be optional. Offer "Skip" (SiriusXM does on Mobbin).
6. **No pre-selected alternatives**: Chegg's default "pause" was cited. Don't pre-select pause or a discount.
7. **Clear confirmation**: end-of-access date, no further charge, an email confirmation (UK draft rules: end-of-contract notice within 24h; EU withdrawal confirmation; HIG renewal date).
8. **Truthful copy**: no false refund claims (Play gives none for the current period; Apple handles refunds), no hidden fees (Adobe), no misleading retention messages (Apple RM content rule).
9. **Reminders**: annual reminder (California), 6-monthly and pre-trial-end reminders (UK from 2027, draft regulations). These are also the strongest-tested lever (#C14–#C16).
