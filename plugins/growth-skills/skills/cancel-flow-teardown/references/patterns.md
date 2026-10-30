# Cancel-flow Pattern Library

The reference for the cancel-flow teardown. It covers the screens around a
subscriber leaving: how they find "manage subscription", what the app shows
before the store or its own cancel step, the confirmation, the billing-issue
banner and the way back after cancel.

Each pattern has **When**, **Cross-check**, **How**, **Evidence** (test numbers
#C1–#C28 and benchmarks in `evidence.md`), **Seen in** (apps from `flows.md`)
and **Trap**. Tiers: strong, directional, anecdotal, observed.

**Read this first.** None of the strong tests in the library measures an
in-app save screen on mobile. Every save-offer number is directional and
mostly from web-billed news or SaaS. Present save offers as hypotheses to
test.

**Three surfaces.** Always say which one the flow runs on:
- **iOS (App Store billing):** the app shows its own screens, then hands off
  to Apple's subscription sheet. No store pause.
- **Google Play:** own screens, then the Play subscription center, which has
  its own survey, user-initiated pause and (since Sept 2026, early access)
  retention offers and plan change.
- **Web-billed:** the app runs the whole flow, so consumer law applies in full.

## Contents

**A. Finding the exit**
1. Plain "Manage subscription" entry with plan, price and renewal date
2. One-tap store hand-off

**B. Before any offer**
3. Optional reason survey (3–6 reasons, Skip)
4. Route by reason

**C. The save screen**
5. Plan switch or downgrade
6. Pause (web and Google Play only)
7. One discount, shown once
8. Personal loss reminder
9. Fix the problem (technical reasons → support)
10. Cancel stays visible next to every offer

**D. The exit itself**
11. At most one save screen, then cancel
12. Clear confirmation: end date, no further charge

**E. Around the flow**
13. A billing-issue banner in the app

**F. After cancel**
14. One-tap resubscribe while access lasts
15. Win-back after lapse, not before

**G. Legal and store flags**
16. Compliance flags

---

## A. Finding the exit

### 1. Plain "Manage subscription" entry with plan, price and renewal date
**When:** cancel is buried, mislabelled or missing in account settings.
**Cross-check:** a "Manage subscription" (or "Subscription") row in Settings or
Account that opens a page with plan, price and renewal date counts.
**How:** Settings → Subscription page: plan, price, renewal date, then
"Change plan" and "Cancel subscription" as plain actions.
**Evidence:** platform rules (HIG: "always make it easy to cancel"; Play
policy requires an easy online method); the Noom class action (cancel only
through the in-app coach chat) and FTC v. Chegg (hard-to-find cancel,
mandatory surveys); Recurly survey: 71% prioritise
easy cancellation (survey).
**Seen in:** Spotify, YouTube, Strava, MyFitnessPal, Dave, Grammarly show
plan, price and renewal date first.
**Trap:** a red "Cancel" row at the bottom of a benefits page looks bold but
reads as a dark pattern if the page above is an upsell.

### 2. One-tap store hand-off
**When:** an App Store or Play-billed app ends its flow with text
instructions ("go to Settings › Apple Account…").
**Cross-check:** opening Apple's sheet in-app (`showManageSubscriptions`) or a
deep link to the Play subscription center counts.
**How:** the final button opens the store's own management sheet.
**Evidence:** observed (Babbel, Headway end on Apple's sheet); platform rules.
**Seen in:** good: Babbel, Headway; weak: Finimize, Audible, Deepstash (text
instructions only).
**Trap:** text instructions go stale as iOS menus change and add steps.

## B. Before any offer

### 3. Optional reason survey
**When:** no survey, or a survey that blocks the exit.
**Cross-check:** a survey with 3–6 reasons and a visible Skip counts; a
required answer scores zero and is a flag.
**How:** one screen, 3–6 reasons in the user's words ("not using it enough",
"too expensive", "found something better", "technical problem", "other" with
free text), Skip in the header.
**Evidence:** FTC v. Chegg cited mandatory surveys; UK draft guidance says
feedback must be optional. Reason mix: Play survey all categories cost 36.4%,
usage 33.7%, better app 9.7%, technical 7.3%, other 12.9% (SOSA 2026). No test
isolates the survey's own effect (Gaps).
**Seen in:** visibly optional: SiriusXM, Plum, Headspace; apparently required:
Centr, Lifesum.
**Trap:** 11-reason lists (Headway, SiriusXM) slow the exit and blur routing.

### 4. Route by reason
**When:** a survey exists, but every answer leads to the same screen.
**Cross-check:** at least two reasons lead to different next steps.
**How:** price → cheaper cadence or tier, or one discount; not using it →
pause (where possible) or a lighter plan; technical → support; found a better
app → what's coming, or let them go; "other" → straight to cancel.
**Evidence:**
- #C6 unnamed meditation app (web): reason-matched offers, 47% of cancellations
  saved, monthly churn about 13% → just under 7% (directional, unverified forum
  post).
- #C4 TouchNote (web): save rate 16% → 25% (directional, vendor).
- #C5 Wavve (web): routing "need a break" to pause, 39% deflection (directional).
- #C23 NYT routes price to a cheaper plan (anecdotal).
**Seen in:** none of the 22 mobile flows routes visibly; Strava lists
"temporarily pausing" as a reason without offering a pause.
**Trap:** routing everyone to a discount trains users to threaten to cancel.

## C. The save screen

### 5. Plan switch or downgrade
**When:** the only alternative to cancel is a discount, or nothing.
**Cross-check:** a cheaper tier, a different cadence (annual, monthly) or a
smaller plan offered on the save screen counts.
**How:** "Change plan" as a peer of "Cancel": cheaper tier first, cadence
switch second.
**Evidence:** Apple Retention Messaging panel (RevenueCat): setups including a plan switch
saved 38% vs 22–27% with promo offers and 13% with text only (RevenueCat
panel, benchmark); offer acceptance itself is ~0.6% of plan switches shown,
so most saves are people who read and didn't cancel within 24 h (soft saves).
**Seen in:** Peloton (cheaper App One tier, annual switch), Duolingo (plan
switch).
**Trap:** App Review 3.1.2(b): no duplicate subscriptions to variants of the
same thing; make the switch replace the old plan.

### 6. Pause (web and Google Play only)
**When:** the top reason is "not using it enough" or seasonal use, and the
app bills on the web or Google Play.
**Cross-check:** a billing pause (no charge, access paused) counts; an account
"pause" that hides a profile doesn't.
**How:** "Take a break for 1–3 months" on the save screen, not pre-selected;
on Google Play, point users to Play's own pause.
**Evidence:**
- Recurly 2026 (web): brands offering pause before cancel saw 337% more pauses,
  and 3 of 4 pausers returned within months (benchmark).
- #C5 Wavve: pause was 753 of 848 accepted offers (directional).
- Recurly survey: 38% prefer pausing to cancelling (survey).
- Pause is ≤0.5% of App Store subscription ends (SOSA 2026) and none of 48
  apps' captured cancel screens showed one (#C27, observed).
**Seen in:** Dave (own billing). No App Store app in the sample.
**Trap:** iOS has no store pause; a fake "pause" that keeps charging is a
deceptive pattern. FTC v. Chegg cited a default "pause" button.

### 7. One discount, shown once
**When:** the top reason is price and the flow has no price option, or the
flow stacks several discounts.
**Cross-check:** a single discount offer, not pre-selected, once per user.
**How:** one offer with a clear duration and the price after it ("50% off for
3 months, then $X"); show it once.
**Evidence:** #C4 TouchNote: 40% off performed about the same as 50% (no
figures; directional). #C1 Aftenposten replaced a downgrade menu with one
holdback offer, saves about 600 → 900 a month (directional, bundled). Apple
RM: promo-offer messages +5.5 pp save rate (#C8, directional: platform claim); promo
offers accepted ~1.1% of the time (RevenueCat panel).
**Seen in:** Pillow (25% off annual for a year, countdown), Plum (50% off for
6 months).
**Trap:** countdown timers on a save offer add pressure regulators dislike;
no public data shows how long discount-saved subscribers stay (Gaps in
`evidence.md`), so measure renewal, not just the save.

### 8. Personal loss reminder
**When:** the save screen is generic ("Are you sure?").
**Cross-check:** the user's own usage, progress or saved items on the screen
counts.
**How:** one line of what they built or use ("12 workouts this month, 3
saved routes"), stated truthfully; for shared plans, who else loses access.
**Evidence:** observed only (Finimize articles read; Glovo savings per order;
Blinkist shared-library partner). No public test.
**Seen in:** Finimize, Strava (benefits recap), Grammarly, Centr (name and
trainer photo), Blinkist.
**Trap:** guilt copy ("You're giving up on yourself") is the confirm-shaming
pattern; keep it factual.

### 9. Fix the problem (technical reasons → support)
**When:** "technical problem" or "missing feature" leads to an offer.
**Cross-check:** a support or chat route for technical answers counts.
**How:** technical → "Let us fix it" (chat or help article) with cancel
still visible.
**Evidence:** #C5 Wavve routed technical and missing-feature answers to chat
(directional). Utilities have the highest technical share (12.4%, SOSA 2026).
**Seen in:** none in the mobile sample.
**Trap:** a support detour without a cancel button is a block.

### 10. Cancel stays visible next to every offer
**When:** an offer screen hides or demotes cancel to a tiny link, or requires
dismissing the offer first.
**Cross-check:** a clearly labelled cancel action on the same screen as each
offer.
**How:** offer as one button, "Cancel subscription" as a peer button or a
plain, readable link on the same screen.
**Evidence** (law-firm summaries; statute and judgment texts not opened):
California ARL (from 1 July 2025): online save offers allowed
only with a click-to-cancel link shown at the same time; Germany BGH (16 July
2026): no retention offers on the §312k confirmation page, so for German
users alternatives go before the cancel button or after submission; UK (from
1 Jan 2027, draft regulations): offers must not prolong exit. All from
law-firm summaries; see platform rules.
**Seen in:** cancel as primary: Centr, Grammarly, Strava; keep as primary with
cancel as link: Duolingo, Deepstash, Blinkist, Glovo, Peloton.
**Trap:** "Keep" as the big button and "cancel" as grey small text fails the
"as easy as signing up" principle.

## D. The exit itself

### 11. At most one save screen, then cancel
**When:** the flow has 3+ own screens before the store or the final cancel.
**Cross-check:** count own screens between "Cancel" and the hand-off or
confirmation.
**How:** survey (optional) → one save screen → cancel. Nothing more.
**Evidence:** #C7 Amazon Prime's 4-page, 6-click flow cut cancellations 14%
(directional, leaked) and was part of the FTC's Amazon case; Uber One up to 23
screens (FTC case pending); #C1 Aftenposten went from 5 to 3 steps and saved
more (directional); #C2 Star Tribune online save rate 18.5% vs 8.8% by phone
(directional).
**Seen in:** 3+ screens: Duolingo, Deepstash, Strava, Headway, SiriusXM.
**Trap:** friction "wins" are legal liabilities; never recommend adding steps.

### 12. Clear confirmation
**When:** the flow ends without the end-of-access date or a statement that no
further charge will happen.
**Cross-check:** end date and "you won't be charged again" on the screen.
Apple's own sheet gives the date for free.
**How:** "Cancelled. You keep Premium until 12 Dec. No further charges."
**Evidence:** Apple HIG (show the renewal date). Observed in Centr, Grammarly, Givingli, Strava, Headway,
Pillow, Blinkist.
**Trap:** a "gift for you" nudge right after cancel (Headway, Plum) reads as
pressure if it comes before the confirmation.

## E. Around the flow

### 13. A billing-issue banner in the app
**When:** a payment fails and the app shows nothing until access ends.
**Cross-check:** an in-app banner or screen when the subscription is in a
billing-issue state, with a button to fix the payment method.
**How:** a calm banner at the top of the main screen ("Your payment didn't
go through · Update payment"), opening the store's payment page
(`apps.apple.com/account/billing` on iOS, Play's payment page on Android) or
the app's own form on web billing.
**Evidence:** billing errors are 15.2% of App Store and 32.2% of Google Play
subscription ends (SOSA 2026); #C13 Truecaller added in-app alerts linking to
the account page with other changes and recovered 40% vs 15% (directional,
bundled).
**Trap:** a red alarm on every screen reads as a threat; one banner and one
reminder are enough.

## F. After cancel

### 14. One-tap resubscribe while access lasts
**When:** after cancel, the subscription page offers no way back.
**Cross-check:** a "Resubscribe" or "Reactivate" action on the same card that
shows the end date.
**How:** status card: "Ends 12 Dec · Resubscribe".
**Evidence:** reactivation within 12 months: weekly 9.0%, monthly 20.1%,
annual 5.2% (SOSA 2026); Productivity monthly 36.1%, the highest (SOSA 2026).
Observed in Strava, Pillow, Grammarly, Blinkist.
**Trap:** none; it's the cheapest win in the flow.

### 15. Win-back after lapse, not before
**When:** the app has no offer for lapsed subscribers, or pushes discounts to
people who are still active.
**Cross-check:** a reactivation screen for expired subscribers when they
open the app.
**How:** after expiry, on next open, a screen that names what they had and
offers the way back (their old plan, or a time-limited return offer).
**Evidence:** nearly 1 in 4 new sign-ups are former subscribers (Recurly
2026, web); #C21 Unscripted reactivation paywall: trial starts "over 240%"
vs new users (directional); #C25 Spotify win-back promo (observed). Apple
win-back offers are used by only 2.5% of offer-using iOS apps (SOSA 2026).
**Seen in:** Headway shows a "gift" button after cancel.
**Trap:** win-back aimed at people who haven't lapsed is just a discount.

## G. Legal and store flags

### 16. Compliance flags
Flag, don't rule. Each flag is a design rule about a screen element, with its
source name.
- Cancel not findable in account settings, or only by chat, phone or email.
- A save offer without a visible cancel action on the same screen
  (California); offers on a §312k confirmation page (Germany).
- A mandatory survey (cited in FTC v. Chegg allegations; UK draft guidance);
  a pre-selected pause or discount (Chegg).
- Signed up in the app or on the web but can't cancel through the same
  channel.
- Misleading loss or refund claims; hidden fees; a "pause" that still
  charges.
- A discount on abandoning the store purchase sheet (App Review risk).
