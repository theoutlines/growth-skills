# Platform, payment and consumer-law rules for web2app funnels, web checkout and link-outs

> **How the skill uses this file.** Background for screen flags only. The skill uses an item when it's about what a screen shows (a price, a button, a checkbox, a decline, a timer, copy). Items about billing setup, emails, reporting, records, fees or monitoring are context, not output.

Checked 2026-10-30. Paraphrased unless in quotes; open the link for exact wording. Law-firm, vendor and press pages are **secondary** and marked. Not legal advice: the skill flags risk and names the rule. Tiers: **rule** (binding text or official program terms), **guidance** (non-binding), **case** (enforcement or court precedent), **pending**.

Related: the cancel-flow-teardown skill (cancel flows, §312k, UK DMCC exit, US cases), the upsell-teardown skill (upsell UI, dark patterns, US link-out history) and the `paywall-store-compliance` skill (in-app sign-up disclosures).

## 0. Which rules apply where

| Surface | Merchant | Rules that bite |
|---|---|---|
| Ad landing → web quiz → web paywall → checkout (web2app) | the app (or its MoR, e.g. Paddle) | Consumer law in full (ROSCA, state ARLs, EU CRD/UCPD, §312j/§312k BGB, UK DMCC), card-network rules, PSD2 SCA. Store rules apply only to what the **app** later says and does (login, access, links) |
| iOS app → link-out → web checkout (app2web) | the app | Apple 3.1.1(a)/3.1.3 by storefront + everything above |
| Android app → external link / alternative billing | the app | Google Play payments policy and enrolled program + everything above |
| In-app IAP / Play Billing | Apple / Google | Store rules; see paywall-store-compliance |

## 1. Apple

### 1.1 App Review Guidelines — https://developer.apple.com/app-store/review/guidelines/ (read 2026-10-30)

| Rule | What it says | Web2app implication | Tier |
|---|---|---|---|
| 3.1.1 | Unlocking "features or functionality" (subscriptions, premium content, full version) "you must use in-app purchase"; no own unlock mechanisms (license keys, QR codes…) | A non-reader app must still offer IAP for what it sells | rule |
| 3.1.1(a) | Entitlements (StoreKit External Purchase Link, Music Streaming Services) allow a link in specific regions. "In all other storefronts, **except for the United States storefront**, where this prohibition does not apply, apps and their metadata may not include buttons, external links, or other calls to action that direct customers to purchasing mechanisms other than in-app purchase." | US: buttons, links and web prices allowed in the app. Elsewhere: no web CTA, no web price mention, no "cheaper on our site" unless an entitlement covers that storefront | rule |
| 3.1.3 intro | Apps under 3.1.3 "cannot, within the app, encourage users to use a purchasing method other than in-app purchase, except for apps on the United States storefront and as set forth in 3.1.1(a) and 3.1.3(a)". "Developers can send communications outside of the app to their user base about purchasing methods other than in-app purchase." | Email/SMS/web pages may promote web prices anywhere; the app UI may not (outside US/entitlements) | rule |
| 3.1.3(a) Reader apps | Magazines, newspapers, books, audio, music, video may let users access previously bought content; may apply for External Link Account Entitlement (one informational link); entitlement "not required … in their United States storefront apps" | Only reader apps may skip IAP entirely (Dipsea, Spotify, Kindle). Fitness, AI, productivity apps are not reader apps | rule |
| 3.1.3(b) Multiplatform services | Apps may let users access "content, subscriptions, or features they have acquired in your app on other platforms or your web site … **provided those items are also available as in-app purchases** within the app" | The legal basis for web2app login. A web subscription can unlock the app, but the same tier must exist as IAP | rule |
| 3.1.3(f) | Free stand-alone companions to paid web tools (VoIP, cloud storage, email, hosting) skip IAP only with no purchasing or calls to action | Narrow; not for typical consumer subscription apps | rule |
| 3.1.2(c) | Before asking to subscribe, describe clearly what the user gets for the price | Applies to any in-app screen that leads to a web checkout | rule |
| 4.8 Login Services | Apps using third-party or social login "to set up or authenticate the user's primary account" must also offer an equivalent login that limits data to name and email, allows a private email, and doesn't track for ads without consent (Sign in with Apple qualifies). Exceptions exist (e.g. app uses only the company's own account system; verify text) | If the web funnel creates accounts with Google/Facebook login and the app accepts that login, the app needs Sign in with Apple (or equivalent). Email/password or magic link from the funnel avoids the trigger. Web accounts created with Apple ID on the web need Sign in with Apple for Web set up for the same Services ID | rule |
| 5.1.1(v) | "If your app supports account creation, you must also offer account deletion within the app" | Web-created accounts used in the app need in-app deletion; deletion must also explain how to cancel the web subscription (Apple's account-deletion guidance says to tell users about billing; not re-opened) | rule |
| 5.6 Code of Conduct | No tricking into unwanted purchases or manipulative practices "within or outside of the app"; 5.6.4 excessive refund requests are a quality signal | Web funnel dark patterns can still cost the app listing | rule |
| Metadata | 3.1.1(a): "apps **and their metadata**" may not include purchase CTAs outside the US | Screenshots/description advertising web prices: only US storefront | rule |

### 1.2 External purchase by region

| Region | Mechanism | Commission / conditions | Source | Tier |
|---|---|---|---|---|
| **United States** | No entitlement needed; buttons, links, web prices allowed (3.1.1(a), 3.1.3) | **0% today.** Apr 2025 contempt order barred commission; Ninth Circuit (Dec 2025) upheld contempt but said Apple may charge a fee for "genuinely and reasonably necessary" costs, to be set on remand; SCOTUS denied stay (May 2026), granted cert (No. 25-1311), ruling expected by Jun 2027 | https://thenextweb.com/news/supreme-court-apple-epic-contempt-app-store-commission (30 Jun 2026, secondary) | **pending** |
| US link behaviour | Apple may not restrict placement, format or copy of link buttons; neutral redirect notice allowed, no scare screens | RevenueCat (1–3 May 2025) https://www.revenuecat.com/blog/growth/apple-anti-steering-ruling-monetization-strategy | rule, secondary |
| **EU (from 1 Oct 2026)** | StoreKit External Purchase entitlement; in-app own checkout or link-out; Apple disclosure sheet; IAP button at least as prominent as developer's when both shown; report every transaction; link-out attributed to token within 7 days; not for minors | IAP 26%/15% · own checkout 20%/10% · link-out 15%/10% | https://www.revenuecat.com/blog/company/apple-in-app-web-checkouts-eu (1 Oct 2026, secondary; verify with Apple's EU docs) | rule, secondary |
| EU (Jun 2025 – Sep 2026) | Links on any channel, in or outside the app, web view allowed, warning screens no longer required | 2% initial acquisition + 5/13% store services + 5% CTC | https://techcrunch.com/2025/06/26/apple-updates-the-rules-for-its-eu-app-store-by-adding-more-complicated-fees | rule, secondary (superseded) |
| **Japan (MSCA, from 18 Dec 2025)** | StoreKit External Purchases or Offers entitlement; IAP on every merchandising screen, at least as prominent; Apple disclosure sheets; product page may not reference external purchase; monthly reporting, audit | 15%; 10% SBP/partner programs/subs after year 1; sales within 7 days of tap | https://appcharge.com/blog/external-payments-in-japan-the-fine-print-behind-apple-and-google-compliance (18 Dec 2025, secondary) | rule, secondary |
| South Korea | StoreKit External Purchase Entitlement with qualifying PSP; app can't also offer IAP | 26% | https://www.revenuecat.com/app-to-web-purchase-guidelines.md (secondary) | rule, secondary |
| Netherlands (dating apps) | Entitlement, NL storefront | 3 points below standard (27%/12%) | same | rule, secondary |
| Rest of world | No CTA in app or metadata; communications outside the app allowed | — | Guidelines 3.1.1(a), 3.1.3 | rule |
| Entitlement docs | allowed-regions entitlement key | https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.storekit.custom-purchase-link.allowed-regions | rule (not opened) |

### 1.3 Case: Cal AI (Apr 2026)

Apple briefly removed Cal AI (H&F #4) for: **3.1.1** (embedded Stripe checkout inside the app, IAP removed; not a reader app), **3.1.2(c)** (weekly-calculated price more prominent than the actual charge; free-trial toggle obscured auto-renewal), **5.6** (a second, different purchase flow shown to users who declined the first; "scam" reviews, high chargebacks). Fixed and reinstated ~4 days later. Sources: TechCrunch (21 Apr 2026) https://techcrunch.com/2026/04/21/apples-cal-ai-crackdown-signals-its-still-policing-the-app-store/ ; Paddle (secondary) https://www.paddle.com/blog/what-cal-ai-taught-us-about-app2web. Tier: case.

## 2. Google Play

| Rule / program | Status and requirements | URL | Tier |
|---|---|---|---|
| Payments policy (default, outside programs) | Digital goods via Play Billing; no steering to other payment methods unless enrolled in a program | https://support.google.com/googleplay/android-developer/answer/9858738 (not re-opened) | rule |
| **US (Epic v. Google injunction)** | From **29 Oct 2025** for US users: Google won't prohibit communicating other prices/availability, linking to transactions or downloads, or other in-app payment methods; won't require Play Billing or price parity. Programs: **alternative billing** and **external content links** (launched 9 Dec 2025). Enrolled developers report transactions and pay fees from 1 Oct 2026; link developers got until 1 Feb 2027. Settlement (4 Mar 2026) pending revised injunction | https://support.google.com/googleplay/android-developer/answer/15582165 | rule |
| US fees (as proposed Dec 2025) | alternative billing 10% subs / 25% other; external links 10% subs / 20% other | https://www.neonpay.com/blog/google-plays-new-u.s.-billing-linking-policies-what-game-developers-need-to-know (secondary) | rule, secondary |
| **Billing choice program** (EEA, UK from 30 Jun 2026; AU, JP from 30 Sep 2026) | Alternative billing and external web links, **Play Billing must also be offered**; inform users of the link destination and purpose before linking; Google one-time info screen; report transactions within 24 h; offer refunds, order history, subscription management and support links; PCI-DSS; no PII in links unless secured. Fees: subscriptions 10%; link fee on purchases within **24 h** of the link | https://support.google.com/googleplay/android-developer/answer/17161464 | rule |
| EEA external offers program; EEA UCB pilot | Still available alongside billing choice | same | rule |
| UCB / alternative billing (Korea, India) | 4 points below Play Billing rate | https://support.google.com/googleplay/android-developer/answer/112622 | rule |
| Japan external payments | Links alongside Play Billing only; only after user selects an item; disclose destination; 10% subs; 24 h window | Appcharge (secondary) | rule, secondary |
| Subscriptions policy | Clear terms, easy online cancel, free-trial cancel instructions (applies to Play-billed subs) | https://support.google.com/googleplay/android-developer/answer/9900533 | rule |

## 3. United States

| Rule / case | Requirement for web funnels and checkout | URL | Tier |
|---|---|---|---|
| **ROSCA** 15 U.S.C. §8403 | Online negative-option sales: (1) "clearly and conspicuously disclose all material terms" **before obtaining billing information**; (2) "express informed consent" before charging; (3) "simple mechanisms … to stop recurring charges" | https://www.law.cornell.edu/uscode/text/15/8403 | rule |
| FTC Negative Option ("click-to-cancel") Rule 2024 | **Vacated** 8 Jul 2025 (8th Cir.); new ANPRM 11 Mar 2026, no text | https://www.kirkland.com/publications/kirkland-alert/2026/03/ftc-restarts-subscription-rulemaking (secondary) | pending |
| **California ARL (AB 2863)**, from 1 Jul 2025 | Express affirmative consent to the auto-renewal terms (in effect a separate consent from the service terms); pre-billing notice that it renews until cancelled, renewal length, amount; covers free-to-pay conversions; online sign-up → online cancel as easy as sign-up; save offers only with a cancel link shown alongside; consent records (3 years or 1 year after termination); annual reminder; price-change notice 7–30 days | https://www.dwt.com/insights/2024/10/ab-2863-updates-california-automatic-renewal-law ; https://ktslaw.com/insights/alert/2024/10/california-latest-automatic-renewal-law-amendments-take-effect-in-july-2025 (secondary; statute not opened) | rule, secondary |
| New York (Gen. Oblig. Law §5-903), from Nov 2025 | Price increases: advance affirmative consent, or cancel within 14 days of the increased charge with pro-rata refund | https://www.arnoldporter.com/en/perspectives/advisories/2026/02/ftc-and-state-ags-continue-to-scrutinize-subscription-practices (6 Feb 2026, secondary) | rule, secondary |
| Massachusetts (940 CMR 38.05), from Sep 2025 | Terms >31 days: pre-renewal notice 5–30 days before cancellation deadline | same | rule, secondary |
| Minnesota (§325G.57) | Save offers barred unless customer affirmatively consents to hear them | same | rule, secondary |
| Colorado, Connecticut, Utah, Virginia | New/updated ARLs named; details not researched | same | gap |
| **Case: FTC v. Genesis Tech** (filed Jun 2026, TRO granted; pending) | Web2app-style apps (MadMuscles, Harna, Unimeal, Nebula, PDF Guru, Wisey, Lumi): sold as "free" or low one-time cost with money-back guarantee; recurring terms in "the smallest print on the page"; **add-on products added without knowledge or consent**; double charges; no cancel option on sites/apps; forced reason before cancel; charges after cancel; new entities and **merchant accounts to avoid fraud monitoring**. ROSCA + FTC Act | https://www.ftc.gov/news-events/news/press-releases/2026/06/ftc-sues-stop-sprawling-enterprise-operating-unlawful-subscription-schemes | case (allegations) |
| Case: Noom class action (Feb 2022, $56M + $6M credits) | Quiz-funnel H&F app: cancel only via in-app coach; agreed to a cancel button and **separate auto-renew consent** | https://www.hunton.com/privacy-and-cybersecurity-law-blog/2022/02/22/fitness-app-agrees-to-pay-56-million-to-settle-class-action-alleging-dark-pattern-practices/ | case |
| Case: FTC v. Instacart (Dec 2025, $60M) | Free-trial sign-ups auto-converted to paid annual; refund limits not disclosed | Arnold & Porter (secondary) | case |
| Case: FTC v. JustAnswer (filed Jan 2026) | Enrolled in recurring monthly plan without consent, with immediate higher charge (classic "$1 trial" checkout pattern) | same | case (pending) |
| Case: FTC v. Amazon Prime (Sep 2025, $2.5B) | Enrolment in checkout: clear decline button, no confirmshaming, disclose cost, dates, auto-renewal, how to cancel | https://www.ftc.gov/news-events/news/press-releases/2025/09/ftc-secures-historic-25-billion-settlement-against-amazon | case |
| Other cancel cases (Chegg, Uber One, Adobe, Match) | See the cancel-flow-teardown skill | https://github.com/theoutlines/growth-skills/tree/main/plugins/growth-skills/skills/cancel-flow-teardown | case |
| BetterMe | No lawsuit or FTC action found (only consumer complaints) | — | gap |

## 4. European Union

| Rule | Requirement | URL | Tier |
|---|---|---|---|
| CRD 2011/83/EU Art. 6 / Art. 8(2) pre-contract info + order button | Main characteristics, total price incl. taxes, duration, auto-renewal and cancellation conditions shown **directly before** the order; button labelled "order with obligation to pay" or unambiguous equivalent, else consumer not bound (DE implementation §312j below) | https://eur-lex.europa.eu/eli/dir/2011/83/oj (not opened this pass) | rule |
| Withdrawal right, 14 days | Distance contracts, incl. digital services | https://europa.eu/youreurope/citizens/consumers/shopping/returns/index_en.htm | rule |
| Digital content exception Art. 16(m) | Lost only with prior **express consent** to start in the period + **acknowledgement** of losing the right (+ confirmation on durable medium). German courts: separate declaration, e.g. an unticked checkbox (LG Köln 2019) | Europa Your Europe; Osborne Clarke (15 Aug 2019) https://www.osborneclarke.com/insights/withdrawal-right | rule / case |
| **CJEU C-234/25 Sky Österreich** (9 Jul 2026) | A dynamic, personalised streaming catalogue is a **digital service**, not digital content; Art. 16(m) read strictly; in doubt, service rules apply. Consumer can withdraw within 14 days even after use; trader may claim proportionate payment (Art. 14(3)) if performance was requested in the period | https://www.insideprivacy.com/consumer-protection/cjeu-decides-when-streaming-subscriptions-are-subject-to-the-right-of-withdrawal/ (18 Jul 2026, secondary); press release https://curia.europa.eu/site/upload/docs/application/pdf/2026-07/cp260097en.pdf (not opened) | case |
| **Withdrawal function** (Dir. 2023/2673, new Art. 11a CRD), from **19 Jun 2026** | Online contracts with a withdrawal right, websites **and apps**: prominent function "withdraw from contract here" for the whole period, no login/app download unless the contract was concluded that way; step 2 "confirm withdrawal"; acknowledgement on durable medium with content, date and time; no extra steps that delay it | https://www.hlc.com/en/publications/eu-consumer-protection-law-update-new-mandatory-withdrawal-button-what-online-traders-need-to-know (4 May 2026, secondary) | rule |
| UCPD 2005/29/EC Annex I #7 | Per secondary summaries, a false "limited time" claim is on the blacklist (fake countdowns on web paywalls would fall under it); text not opened | see the upsell-teardown skill | rule |
| Omnibus 2019/2161 | Disclose personalised prices set by automated decision-making | https://7learnings.com/blog/what-retailers-need-to-know-about-the-new-eu-consumer-protection-directive/ (secondary) | rule |
| **PSD2 SCA / 3-D Secure** | First customer-initiated payment that sets up a subscription needs SCA, **also when €0** (free-trial card setup); later fixed-interval charges are merchant-initiated (out of scope) when the first transaction's network reference is stored | Adyen docs https://docs.adyen.com/online-payments/psd2-sca-compliance-and-implementation-guide/business-models-overview (secondary) | rule, secondary |
| Digital Fairness Act | Not adopted; proposal listed for Q4 2026; topics: dark patterns, subscription traps, express consent before free-trial conversion | https://www.europarl.europa.eu/legislative-train/theme-protecting-our-democracy-upholding-our-values/file-digital-fairness-act | pending |

## 5. Germany

| Rule | Requirement | URL | Tier |
|---|---|---|---|
| **§312j(2)–(4) BGB "Buttonlösung"** | Key information (Art. 246a §1 EGBGB) "unmittelbar bevor der Verbraucher seine Bestellung abgibt, klar und verständlich in hervorgehobener Weise"; the button must read **"zahlungspflichtig bestellen"** or an equally unambiguous wording; otherwise **no contract** (Abs. 4) | https://www.gesetze-im-internet.de/bgb/__312j.html | rule |
| §312j and free trials | German courts have applied the button rule to free trials that convert to paid (KG Berlin "Probeabo" decision); "Jetzt kostenlos testen" on a trial that auto-converts is high risk. Decision text not opened | https://www.ferner-alsdorf.de/entscheidung-des-kg-berlin-zur-buttonloesung-bei-probeabo/ (title only) | case, unverified |
| §312k BGB "Kündigungsbutton" | "Verträge hier kündigen" → confirmation page with "jetzt kündigen"; BGH I ZR 200/25 (16 Jul 2026): no retention offers on that page; login question pending (BGH due 5 Nov 2026) | see the cancel-flow-teardown skill | rule / case |
| §356(5) BGB | Digital content waiver needs a separate express declaration | Osborne Clarke (2019) | case |
| Payment method expectations | PayPal ~90% of web2app transactions in Germany (FunnelFox); PayPal +47% conversion for digital media in DE (Stripe) | Part 2 of `evidence.md` | benchmark |

## 6. United Kingdom

| Rule | Requirement | URL | Tier |
|---|---|---|---|
| DMCC Act 2024 Part 4 Ch. 2 (subscription contracts), from **1 Jan 2027** (draft regulations laid 19 Oct 2026) | Pre-contract key information; reminders (e.g. 6-monthly; **before a free trial or discount ends**); 14-day cooling-off at start and again at renewal / after a free trial ends; online sign-up → online exit; end-of-contract notice within 24 h; retention offers must not prolong exit | https://cms.law/en/gbr/legal-updates/uk-subscription-contracts-the-government-publishes-the-missing-detail (secondary) | rule (commencing) |
| DMCC Part 4 unfair practices (from 6 Apr 2025) + CMA price-transparency guidance | Mandatory fees in headline price; optional extras clear and **not auto-opted-in**; fake time-limited offers targeted (CMA v. Emma Sleep, May 2026); fines up to 10% global turnover | see the upsell-teardown skill | rule / case |
| App stores as merchant of record | Not confirmed how the regime applies | — | gap |

## 7. Card networks and chargeback programs

| Rule | Requirement | URL | Tier |
|---|---|---|---|
| **Visa trial / intro-offer rules** (global, from 18 Apr 2020), physical and digital | Express consent to the ongoing subscription at enrolment even if $0 due; confirmation (email/SMS) with start date, goods/services, ongoing amount and frequency, cancel link; **reminder ≥7 days before** a trial/intro price ends or terms change, with cancel link; receipts show trial length and "charged unless cancelled"; online cancel whatever the sign-up channel; first post-trial charge descriptor includes "trial"; misrepresentation dispute right expanded | https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/visa-new-subscription-rules-flier.pdf | rule |
| **Mastercard subscription rules** (Braintree summary: effective 22 Sep 2022; trial rules first announced 2019/2020) | Terms at point of payment (price, frequency; trial length, post-trial price); express acceptance; terms **not hidden behind a link, message box or scroll**; post-enrolment email with terms and cancel instructions; receipt after each billing with cancel instructions; online cancel; **digital-goods trials >7 days: reminder 3–7 days before end**; billing less than every 6 months: notice 7–30 days ahead | https://developer.paypal.com/braintree/articles/guides/recurring-billing/mastercard-requirements (secondary) | rule, secondary |
| **Visa VAMP** (from Jun 2025; enforcement Oct 2025) | Ratio = (TC40 fraud reports + TC15 disputes) ÷ settled CNP transactions. Excessive merchant **1.5%** in US, Canada, EU, AP from **1 Apr 2026** (was 2.2%); LAC 1.5%; CEMEA 2.2%; monitored from 1,500 combined events/month; $8 per dispute/TC40 for excessive merchants | https://justt.ai/blog/visa-vamp-threshold-changes-april-2026/ (31 Mar 2026, secondary); https://www.chargebackgurus.com/blog/visa-announces-even-more-vamp-changes (27 May 2025, secondary) | rule, secondary |
| **Mastercard ECM / HECM** | ECM: 100–299 chargebacks and 1.5–2.99% per month; HECM: ≥300 and ≥3%; ratio uses prior month's transactions; assessments escalate from month 2 (up to 100k/200k); three clean months to exit | https://chargebacks911.com/mastercard-chargeback-threshold/ (Nov 2025, secondary) | rule, secondary |
| Retry limits | Visa: up to 15 reattempts in 30 days, none after category-1 declines; Stripe guide cites 4–6 in 15 days as network practice | Paddle (citing J.P. Morgan), Stripe guide (secondary) | rule, secondary |
| Evasion | Splitting merchant accounts to stay under monitoring is alleged as part of FTC v. Genesis Tech | FTC (Jun 2026) | case |

## 8. Checklist for web funnels and checkout

❌ = rule or likely violation; ⚠️ = guidance, reviewer discretion or regulator/chargeback risk.

**Landing and quiz**
1. ⚠️ Ad and landing promise match the checkout (no "free" if a charge follows; no one-time price if it renews) — FTC v. Genesis Tech, Visa misrepresentation disputes.
2. ❌ No fake urgency: countdowns only for real deadlines, not reset on reload (CMA v. Emma; ACM v. Epic; UCPD Annex I #7 cited from secondary sources).
3. ⚠️ Quiz "results" and "your plan is ready" claims must not imply diagnosis or guaranteed outcomes (Wisey ADHD claims in Genesis Tech).

**Web paywall**
4. ❌ (terms hidden or misleading) / ⚠️ (per-day or per-week price louder than the charge) Show the **amount actually charged** and the billing period as the most prominent price; per-week/per-day breakdowns secondary (ROSCA "material terms"; Apple 3.1.2(c) in Cal AI applies to in-app screens; CMA price transparency).
5. ❌ Trial / intro terms: length, what is charged today (incl. $0 or $1), price after, renewal frequency, how to cancel, **before card details** (ROSCA; Visa; Mastercard; CA ARL).
6. ❌ Terms on the checkout page itself, not behind a link, tooltip or scroll (Mastercard; Genesis Tech "smallest print").

**Checkout**
7. ❌ California: express affirmative consent to the auto-renewal terms (CA ARL, secondary sources). Elsewhere in the US: clear disclosure and express informed consent (ROSCA). ⚠️ A separate unticked checkbox is the safest form (Noom settlement; CA practice), not a stated requirement in the sources opened.
8. ❌ EU: key info directly above the button; button "order with obligation to pay" or an equally unambiguous wording; Germany "zahlungspflichtig bestellen" (§312j BGB; CRD Art. 8(2)). ⚠️ "Start free trial" on an auto-converting trial is high risk in Germany (KG Berlin decision, not opened).
9. ❌ EU digital content: withdrawal waiver only via express consent + acknowledgement (separate checkbox); a dynamic, personalised streaming catalogue was held to be a **digital service**, so the 14-day withdrawal right stays there (CJEU C-234/25); add the withdrawal function from 19 Jun 2026.
10. ❌ EU/UK cards: SCA/3DS on the first payment, including €0 trial setups; then MIT for renewals (PSD2).
11. ⚠️ Wallets first (Apple Pay ~60% of web2app transactions; +22% conversion in Stripe holdback); PayPal in DE/EMEA; local methods (iDEAL, BLIK).
12. ⚠️ No forced account creation before payment (Baymard: 18% abandon) — collect email, create the account after.

**Post-purchase upsells**
13. ❌ No pre-checked add-ons and no upsell charged without its own accept (Genesis Tech allegations; CMA opt-in cases); a recurring upsell must say it recurs (ROSCA). ⚠️ Price on the accept button and an equal-weight decline (FTC v. Amazon order on decline wording).
14. ⚠️ One-click upsells charge a stored card: show the exact amount and recurrence on the button; recurring upsells need their own ROSCA disclosure and consent.

**Confirmation, account and app access**
15. ❌ Confirmation email with terms, start date, amount, frequency and cancel link (Visa; Mastercard; CA ARL acknowledgement).
16. ⚠️ Clear handoff: download link, login method that matches the app, deep link (handoff loss "up to 40–50%", anecdotal).
17. ❌ iOS: the subscription tier sold on the web must also exist as IAP in the app (3.1.3(b)), unless reader app or US-only setup accepted by review; never embed a non-IAP checkout inside the iOS app outside allowed regions (Cal AI, 3.1.1).
18. ❌ If the funnel uses Google/Facebook login and the app accepts it, offer Sign in with Apple (4.8). In-app account deletion for web-created accounts, with a note on cancelling the web subscription (5.1.1(v)).
19. ❌ Outside the US storefront: no web prices, "cheaper on web" or buttons in the app or its metadata without an entitlement (3.1.1(a)). Email/web communications are fine.

**Link-out from the app (app2web)**
20. ⚠️ US: link opens the default browser; IAP stays available (non-reader apps); don't serve a second, different purchase flow after a decline (Cal AI, 5.6); commission on US link-outs is **pending**.
21. ❌ EU/Japan/Korea: use the entitlement, Apple's disclosure sheet, IAP at least as prominent where required, report transactions (7-day attribution window).
22. ❌ Android: only via an enrolled program (US alternative billing / external content links; billing choice in EEA/UK/AU/JP); Play Billing offered alongside where required; disclose the link destination; report within 24 h.

**Renewal, reminders, cancel**
23. ❌ Trial-end / intro-price reminder ≥7 days before (Visa flier; how this applies to trials of 7 days or less isn't stated in the sources opened: ⚠️, check with your acquirer); 3–7 days for digital trials >7 days (Mastercard); annual reminder (CA); MA 5–30 days before deadline for terms >31 days; UK before trial/discount ends (from 2027).
24. ❌ Online cancel as easy as sign-up, cancel link next to any save offer (CA ARL; ROSCA; §312k; EU/UK).
25. ❌ NY: price increase needs consent or a 14-day cancel with pro-rata refund.
26. ⚠️ Keep Visa VAMP < 1.5% and Mastercard < 1.5% / 100 chargebacks per month; never split merchant accounts to stay under thresholds (Genesis Tech). Trial descriptor contains "trial" on the first post-trial charge (Visa).

## Gaps

- Apple App Review Guidelines: last-updated date not shown in the fetched text; 4.8 exception list and Apple's account-deletion guidance page not re-opened. StoreKit entitlement region docs not opened (EU and Japan terms via RevenueCat and Appcharge, secondary).
- US Apple link-out commission: pending remand and Supreme Court (No. 25-1311).
- Google US program fees: proposal-stage figures (Neon, secondary); revised injunction after the Mar 2026 settlement not confirmed.
- EUR-Lex CRD text, CJEU press release, and KG Berlin / BGH "Probeabo" decisions under §312j not opened; Cologne 2019 is an LG ruling summarised by Osborne Clarke.
- California statute text not opened; trial-end reminder obligations under CA law not confirmed. CO, CT, UT, VA ARL details not researched.
- Mastercard's own rules document not opened (Braintree summary, effective date 22 Sep 2022); original 2019/2020 announcement date not verified.
- VAMP figures from Justt and Chargeback Gurus (secondary); Visa's own VAMP fact sheet not opened.
- No public enforcement action specific to quiz length or a "personalised plan" claim; BetterMe: none found. Genesis Tech complaint not read (press release only).
- UK DMCC: app-store merchant-of-record treatment unknown.

## Cases cited for screen flags

| Case | What it says about a screen | URL |
|---|---|---|
| ACM (Netherlands) v. Epic Games, May 2024 | Fined for countdown timers in the item shop that implied scarcity when items stayed available | https://nltimes.nl/node/72816 (press) |
| CMA v. Emma Sleep, consent order May 2026 | Countdown discount claims presented as time-limited when none were; timers must end with the promotion | https://www.mondaq.com/uk/dodd-frank-consumer-protection-act/1796032/uk-consumer-law-revolution-emma-sleep-case-is-partly-settled-but-the-other-part-is-keeping-us-awake-at-night (secondary) |
| FTC v. Amazon (Prime), Sept 2025 | Order requires a clear decline button and bans shaming decline text | https://www.ftc.gov/news-events/news/press-releases/2025/09/ftc-secures-historic-25-billion-settlement-against-amazon |
