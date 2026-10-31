# Web2app Pattern Library

The reference for the web2app teardown: the web funnel that sells a mobile
subscription before install (landing, quiz, paywall, checkout, upsells,
getting into the app) and the in-app link-out to a web checkout.

Each pattern has **When**, **Cross-check**, **How**, **Evidence** (tests
#W1–#W63 and benchmark rows in `evidence.md`), **Seen in** (`flows.md`) and **Trap**. Tiers: strong, directional, anecdotal,
observed.

**Read this first.**
- Only one strong test is a subscription app's web checkout or link-out
  (#W39 Dipsea). The other strong rows are web UX tests from non-app
  businesses, Stripe payment-method holdbacks across many businesses, and
  Android sign-in tests. Use them for direction, not as an app's expected lift.
- The funnel leaks earliest: only 47.5% of sessions reach screen 2, 13% the
  paywall, 3% a purchase (FunnelFox, per session, vendor data).
- Every controlled link-out number shows a lower first conversion at the
  hand-off (tap → start 70.9% in-app vs 44.4% web, #W39): the web option's
  screens have to earn it back.
- Web funnels carry consumer law and card-network rules in full; the store
  doesn't do the disclosures for you. Check the market table in
  `categories.md`.

## Contents

**A. Landing and quiz**
1. Match the ad on the first screen
2. Start with one easy answer
3. Honest pacing and progress
4. A result screen built from the answers, with no claims
5. Email after value
6. Quiz length is a test, not a rule

**B. Web paywall**
7. The charge first, per-day second
8. Trial terms and a dated timeline
9. Plans that compare honestly
10. No fake urgency

**C. Checkout**
11. Wallets first
12. Local methods and currency
13. Email and payment only
14. Consent at the button, by market
15. A decline screen that keeps the sale
16. Risk reversal stated plainly

**D. After payment**
17. Post-purchase upsells done right
18. Confirmation that a reminder could replace
19. Into the app without a password

**E. Link-out from the app**
20. Offer web beside IAP, don't replace it
21. Placement decides the web paywall's rate

**F. Flags**
22. Compliance flags

**Where it flips** (table at the end)

---

## A. Landing and quiz

### 1. Match the ad on the first screen
**When:** the ad promises one thing and the first screen opens on a generic
brand page or a different promise.
**Cross-check:** the first screen restates the ad's outcome and names the product.
**How:** one landing per ad angle; headline in the ad's words; the first
question or CTA right under it.
**Evidence:** #W1 Campaign Monitor: headline verb matched to the search,
+31.4% sign-ups (strong, web SaaS). #W7 Houzz: a dedicated landing for paid
traffic, +5% trials (directional, = onboarding #39). #W6: funnels built
around the creative that worked (directional).
**Trap:** a promise the plan screen can't keep becomes a refund later (US
web refunds 5.67% of revenue, FunnelFox).

### 2. Start with one easy answer
**When:** the first screen asks for an email, a long form, or nothing at all.
**Cross-check:** the first interaction is a single tap.
**How:** open with the goal question (one tap, big options); Skip or back
visible.
**Evidence:** #W2 Seamwork: a 5-question quiz as the homepage hero,
memberships +34% (strong, web membership). Screen 2 is the biggest drop:
47.5% of sessions reach it (FunnelFox, benchmark).
**Seen in:** Calm (first question in the hero), Headspace, Canva, ChatGPT;
in `walkthroughs.md`, 4 of 5 paid-social quizzes open with an age or gender
card as the first tap.
**Trap:** a first question that feels like a medical intake scares people off.

### 3. Honest pacing and progress
**When:** long "analysing" loaders, animated waits between questions, or a
progress bar that jumps.
**Cross-check:** time spent waiting vs answering; how the bar fills.
**How:** cut dead time; keep one short loader where real work is shown; a
bar that reflects the real remaining steps.
**Evidence:** #W9 Lasting: shorter animations between questions, +60%
conversions (strong per vendor, thin details). #W10 meta-analysis of 32
experiments: a constant progress bar doesn't reduce drop-off, fast-to-slow
does, slow-to-fast increases it (strong, survey science).
**Seen in:** `walkthroughs.md`: one quiz's loader stalls at 49% until the
user answers a pop-up question; another runs an "analysing your profile"
loader before any answer.
**Trap:** front-loading easy questions so the bar moves fast early is
fine; a bar that runs ahead of the real remaining steps reads as
manipulation in a paid funnel. Don't recommend it.

### 4. A result screen built from the answers, with no claims
**When:** "your plan is ready" ignores the answers, or promises an outcome
(weight by a date, a diagnosis).
**Cross-check:** the plan shows the user's goal, numbers and a realistic
timeline; no medical or guaranteed claims.
**How:** echo two or three answers, show what the first week looks like, and
say it's an estimate.
**Evidence:** #W12 GEM SLEEP: quiz order and a results screen with the next
step and price, 35% → 52% (directional, = onboarding #37). FTC v. Genesis
Tech (pending): claims about conditions in quiz results among the
allegations (case).
**Trap:** projection charts with a target date are a promise; keep them
hedged and consistent with the product.

### 5. Email after value
**When:** the funnel asks for an email before the user has seen anything
for themselves.
**Cross-check:** where the email gate sits, and whether it says why.
**How:** ask after the plan or result ("save your plan"), or at checkout.
**Evidence:** #W13 Noom: email about a third of the way, before the results
graph (observed). In `walkthroughs.md`, all four email gates reached sit
right after a loader or "ready" moment and trade the email for the result;
three of five quizzes then ask for a required first name; none of the five
shows a price before an email or consent gate. Baymard: forced account creation is 18% of checkout
abandonment (benchmark, e-commerce). No controlled test of email position.
**Trap:** the email is the retargeting list; moving it later trades list
size for completion. Test, don't assume.

### 6. Quiz length is a test, not a rule
**When:** someone wants to cut questions to raise conversion, or add them to
raise intent.
**Cross-check:** count screens, and how many feed the plan.
**How:** cut dead time and questions that never show up in the plan first;
test the length itself.
**Evidence:** no controlled test of length. #W11 Rino: a 51-step funnel won
(no number, directional); #W13 Noom up to 113 screens (observed); FunnelFox
blog: 30–60 screens "acceptable" in health (anecdotal).
**Trap:** short tests reward short quizzes; check refunds and LTV too.

## B. Web paywall

### 7. The charge first, per-day second
**When:** the paywall leads with "$0.43 a day" or a weekly-calculated price
while the charge is a 3-month or annual amount.
**Cross-check:** the biggest price figure is the amount charged and its period.
**How:** "$39.99 every 3 months" as the price; "about $0.44 a day" small
below it.
**Evidence:** Cal AI (Apr 2026): Apple removed the app partly for a
weekly-calculated price shown more prominently than the actual charge,
3.1.2(c) (case, in-app). ROSCA: all material terms clearly before billing
info (rule). CMA price transparency (guidance).
**Seen in:** `walkthroughs.md`: one paid-social paywall makes the per-day
figure the biggest number on every plan card, with the first charge small and
grey and a 4.4x jump at renewal (observed).
**Trap:** Apple has removed an app partly for this (Cal AI); don't defend it
with a conversion test.

### 8. Trial terms and a dated timeline
**When:** a trial or $1 intro without a clear "today / reminder / charge"
sequence.
**Cross-check:** today's charge, length, the price after, how often, how to
cancel, before payment details.
**How:** a three-step timeline with real dates; the reminder promise on it.
**Evidence:** onboarding library #1 Blinkist: trial timeline and reminder,
+23% trial sign-ups (strong, in-app). Card-network trial rules (Visa,
Mastercard) and ROSCA (rules). Observed in 12 web checkouts with "$0 today"
and a dated charge.
**Seen in:** Headspace, Duolingo, Canva, Spotify.
**Trap:** "$1 trial" checkouts that enrol into a higher monthly charge are an
FTC allegation (JustAnswer, pending).

### 9. Plans that compare honestly
**When:** four or more plans, a strike-through with no explained reference,
or a pre-selected plan the user can't see is chosen.
**Cross-check:** at most three plans, the default visible, reference prices
explained.
**How:** two or three plans; the default marked; a footnote on how the
reference price is calculated.
**Evidence:** web plan mix: 1-month 48.8%, 1-week 30.5%, 1-year 12.2% of
web2app revenue (FunnelFox). Observed: Babbel footnotes its reference price.
**Trap:** EU price-reduction rules apply to announced discounts in some
markets.

### 10. No fake urgency
**When:** a countdown, "discount reserved for 10 minutes", or "only today".
**Cross-check:** reload: does it reset? Is there a real end date?
**How:** remove it, or use a real end date that ends the offer.
**Evidence:** ACM v. Epic (fine for countdowns implying scarcity), CMA v.
Emma Sleep (consent order on timers), UCPD Annex I #7 per secondary sources
(cases, rule). Observed: timers cluster in AI-creative and edtech funnels;
none in the wellness funnels on Mobbin.
**Seen in:** `walkthroughs.md`: one paid-social paywall runs a 10-minute
"discount reserved" timer that resets when the paywall is entered again, opens
with a "pick a gift" discount where every box holds the same 75%, and shows
"you've unlocked 80%" on exit with the prices unchanged (observed).
**Trap:** a timer that resets is the cleanest violation to spot; flag it.

## C. Checkout

### 11. Wallets first
**When:** a card form first and Apple Pay below it, or no wallet.
**Cross-check:** on iPhone Safari, Apple Pay is the first option.
**How:** Express Checkout (Apple Pay, Google Pay) at the top; card below.
**Evidence:** #W19 Stripe holdback: Apple Pay +22.3% conversion (strong,
many businesses); #W20 earlier A/B +10% (strong); Apple Pay ~60% of web2app
transactions (#W26, FunnelFox); showing Apple Pay early ~2× vs at the end
(Stripe, directional). #W45 Kompanion: Apple Pay-only link-out checkout,
"0% drop" (directional, days of data).
**Trap:** wallets show only in supported browsers; test on a phone.

### 12. Local methods and currency
**When:** one card-and-USD checkout for every market.
**Cross-check:** PayPal in Germany, local methods by market, prices in local
currency.
**How:** show the payment buttons and currency the market expects.
**Evidence:** #W19 Stripe: PayPal in Germany +47% (digital media), iDEAL,
BLIK, Konbini lifts (strong, vendor); #W17 local currency +17.8% international
revenue (strong); PayPal ~90% of web2app payments in Germany (FunnelFox).
#W18 Flashbook: localised funnels 57% of web revenue (directional).
**Trap:** each method has its own failure and refund behaviour.

### 13. Email and payment only
**When:** name, address, phone or a password before paying.
**Cross-check:** count fields; is an account forced first?
**How:** email and payment (plus tax fields where required); account after
payment.
**Evidence:** Baymard: forced account creation 18% of abandoners; most
checkouts need about 8 fields and carry 11.3 (#W27, #W28, e-commerce).
#W33: optional account at checkout, +45% buyers (directional, before/after).
#W23 Rino: fields cut with a provider switch, "2–2.5×" (directional,
bundled).
**Seen in:** ExpressVPN (email only, password after); most Mobbin web
checkouts still create an account first.

### 14. Consent at the button, by market
**When:** renewal terms sit behind a link, or consent is only "by continuing
you agree".
**Cross-check:** terms next to the button; how consent is given; the button
wording in Germany; the withdrawal checkbox in the EU.
**How:** renewal sentence right above the button; an unticked checkbox for
auto-renewal (safest form); "zahlungspflichtig bestellen"-type wording in
Germany; for EU digital content, a separate waiver checkbox with
acknowledgement.
**Evidence:** ROSCA, California ARL (express affirmative consent, records),
§312j BGB, CRD Art. 8(2), Mastercard (terms not behind a link or scroll)
(rules); Noom settlement agreed to separate auto-renew consent (case).
Observed: 13 checkouts put the renewal text by the button, mostly as "by
continuing you agree" text; one paid-social checkout sheet uses an unticked
"I agree to the autorenewing terms" box above the wallet buttons
(`walkthroughs.md`).
**Trap:** in Germany, "Start free trial" on an auto-converting trial may not
count as an equally clear order wording (a court decision we couldn't open);
use the explicit wording there.

### 15. A decline screen that keeps the sale
**When:** a decline shows a generic error and the session ends.
**Cross-check:** a decline screen that explains and offers another method;
a waiting state for bank verification that keeps the user's place.
**How:** "Your bank declined this card. Try Apple Pay or another card", with
the other payment buttons right there.
**Evidence:** 30–50% of initiated web2app payments fail (FunnelFox,
directional). #W24 Shmoody: a decline screen offering another method
recovered ~20% of failed prepaid-card payments in week one (directional).
**Trap:** blaming the user ("invalid card") when the bank declined reads as
an accusation; say what happened in plain words.

### 16. Risk reversal stated plainly
**When:** a money-back guarantee with conditions buried, or none at all in a
high-refund market.
**Cross-check:** guarantee terms stated where they're claimed.
**How:** one line with the window and the condition, linked to the policy.
**Evidence:** observed (ExpressVPN 30 days, Babbel 20 days). FTC v. Genesis
Tech alleges a "money-back guarantee" framing that hid recurring terms
(case, pending). No test.
**Trap:** a guarantee with hidden conditions is worse than none.

## D. After payment

### 17. Post-purchase upsells done right
**When:** one-click offers after the purchase.
**Cross-check:** each offer: its own accept, the exact price, whether it
recurs, an equal decline; how many in a row.
**How:** one or two offers that extend the purchase (a guide, a plan, extra
months), each with "Add for $9.99, one-time" and "No thanks".
**Evidence:** upsells 4.07% of web2app revenue; LTV claims +20%, ×2 and
>200% contradict each other (#W30 = upsell #U34, directional). #W31 English
on Smartphone: upsells ~10% of revenue (directional). #W32 SamCart order
bumps 30–40% take (directional, info products). FTC v. Genesis Tech: add-ons
charged without consent (case, pending).
**Trap:** a recurring upsell needs its own ROSCA disclosure and consent.

### 18. Confirmation that a reminder could replace
**When:** the thank-you page and email don't restate the terms.
**Cross-check:** what was bought, today's charge, the next charge date and
amount, how to cancel.
**How:** one block on the page and the same in the email.
**Evidence:** Visa and Mastercard require a post-enrolment confirmation with
terms and a cancel link (rules).

### 19. Into the app without a password
**When:** the buyer has to find the app, sign up again or set a password.
**Cross-check:** a download step (store link, QR on desktop, SMS) and a first
login by magic link, deep link or email code.
**How:** "Get the app" as the next step; a deep link that opens the app
signed in; the same email everywhere.
**Evidence:** #W34 Apartment List: a deep-link magic sign-in, Day-0 logins
2× (directional, vendor). FunnelFox blog: up to 40–50% pay and never log in
when the hand-off is unclear (anecdotal). #W35/#W36 Android sign-in hints
+80% / +19% sign-ups (strong, not post-purchase).
**Seen in:** HBO Max (QR + badges), Rocket Money (SMS link), Cal AI and Hatch
(magic links in the app).
**Trap:** no public purchase → install → login benchmark; measure your own.

## E. Link-out from the app

### 20. Offer web beside IAP, don't replace it
**When:** an iOS app (US storefront) adds a web checkout.
**Cross-check:** is IAP still offered? For non-reader apps it must be (3.1.3(b)).
**How:** IAP as the main button; "Pay on web, save X%" beside it; neutral
note that the user leaves the app.
**Evidence:** #W39 Dipsea (randomized, ~3,100 per arm): initial conversion
IAP only 27.0%, IAP + web 23.5%, web only 18.1%; CTA tap → start 70.9% IAP
vs 44.4% web (strong, reader app). #W45 Kompanion beside-IAP button, "0%
drop" (directional, days). #W40: more web subscribers set to renew, more
refunds (directional).
**Trap:** Cal AI was removed for an embedded Stripe checkout with no IAP
(case, 3.1.1).

### 21. Placement decides the web paywall's rate
**When:** one web paywall reused in every placement.
**Cross-check:** where the link-out appears.
**How:** start with the post-onboarding placement; treat contextual
placements separately.
**Evidence:** #W44: the same web paywall converted 3.38% after onboarding and
0.87% as a contextual upsell (directional).


## F. Flags

### 22. Compliance flags
Flag, don't rule. Use the checklist in `platform-rules.md`; most legal sources
are secondary summaries. The most common hits in web funnels:
- "Free" or a one-time price on a recurring charge; renewal terms below the
  fold or behind a link.
- Per-day or per-week price louder than the charge.
- Countdown that resets on reload.
- Consent only by "by continuing you agree" where a market needs more
  (California, Germany's button wording, the EU waiver checkbox).
- Pre-checked add-ons or upsells charged without their own accept.
- No online cancel; no reminder before a trial ends.
- In the iOS app: a non-IAP checkout embedded, IAP dropped, or web prices
  outside the US storefront.

## Where it flips

| Tactic | Wins when | Loses when | Evidence |
|---|---|---|---|
| Web paywall placement | After onboarding | As a contextual upsell (about 4× lower) | #W44 |
| Longer quiz | Higher intent in health (reported) | Dead time and loaders (pacing +60% when cut) | #W11, #W9 |
| Progress bar | Fast-to-slow, honest | Constant (no effect) or slow-to-fast (more drop-off) | #W10 |
