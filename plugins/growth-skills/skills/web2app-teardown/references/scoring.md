# Web2app Score Rubric

A 100-point score for the screens of a web funnel that sells a mobile
subscription: landing and quiz, the web paywall, the checkout screen, and the
screens after payment, up to the first screen in the app. **Only what a
product designer changes on a screen is scored**; payment setup, fees,
emails, store settings and legal review are out of scope. Score from the
checks, never from impression.

## How to score

- Each check is **full**, **half** (round down) or **zero**. Nothing else.
  When half is held back, the held-back amount is the rest of the check (a
  5-point check: 2 scored, 3 held back).
- **Mode first.**
  - **Web funnel** (landing → quiz → paywall → checkout → app): dimensions
    1–4.
  - **Link-out** (an in-app paywall with a "buy on the web" option): replace
    dimension 1 with dimension 1L. Dimension 2 judges the in-app paywall
    itself (its prices and terms). In dimension 4, check 3 judges only the
    return into the app (no download step needed). Say "link-out score".
  - Both: score the funnel; judge the in-app link-out screen in a short
    note, not in the score.
- **Market.** Some checks depend on the market (which payment button leads,
  the order-button wording). Use the markets the user names; if none, use the
  US and say so.
- **Bucket.** RevenueCat SOSA buckets; "AI app" is a tag. Finance apps: use
  Utilities and say so.
- **Unseen and undescribed.** If what you saw already earns full → full. If
  a screen or element the check needs wasn't captured or described at all →
  half, the other half held back (never the whole check). If you saw it
  missing or wrong → that's seen; score it. Uncaptured screens that could only
  hold a violation → don't assume it. An element mentioned without detail
  scores on what's stated, seen; "details sent by email" on a screen is seen.
- **Several parts in one check.** Full when every part is met; half when one
  part is seen missing or one is not covered (held back); zero when two or
  more parts are seen missing, unless the check says otherwise.
- **One issue, one deduction.** Deduct an element once, in the check that
  names it most directly.
- **Your own arithmetic** on prices the user gave (e.g. $29.99 every 4 weeks
  ≈ $1.07 a day) is allowed; say it's yours.
- **Nothing to judge** → full, where a check says so.
- **Never reward pressure.** No check gives points for timers, more screens,
  pre-selection or hiding the price.

### Blockers (hard cap)

Visible on the screens. Any of these caps **the dimension it sits in at 40% of
its maximum (round down)** and the **total at 49** (Needs work), and is a
"Fix first" row:
1. **Hidden recurring terms**: before payment details, no screen says that it
   renews or what it costs after the trial or intro period, or the offer is
   called one-time while it renews. A disclosed free trial is not a blocker.
   Dimension 2.
2. **Fake urgency**: a countdown or "discount reserved" that resets on reload
   or isn't a real deadline. Dimension 2.
3. **Charges without a choice**: a pre-checked paid add-on, an upsell charged
   without its own accept, or a second, different purchase screen shown after
   a decline. Dimension 4.

If the cap doesn't bind, still write "(cap)" after the score. Held-back
points inside a capped dimension aren't counted; held-back points elsewhere
are still shown.

### Screen flags and priority

A flag is a screen element that a store rejects or that regulators name as a
dark pattern: hidden renewal terms, a fake timer, a pre-checked add-on, a
per-day figure that doesn't match the real charge, a missing order-button
wording in Germany, terms only behind a link. Each is a "Fix first" row
stated as a design rule with its source name. No legal analysis, case
amounts or open legal questions; if it needs a lawyer, a pricing decision or
engineering, leave it out.

- **Fix first**: a blocker or a screen flag.
- A missing element that isn't a flag is a Medium row.
- Anything that isn't a screen change is out of scope.

### Consistency and held back

- Every dimension that loses 4+ points on what you saw needs a row
  (held-back points don't). A row may fix several checks.
- **Weakest dimension** = the largest share of its maximum lost on what you
  saw (a capped dimension counts its capped score); ties go to the earlier
  dimension. If nothing was lost on what you saw, say there is none.
- **Held back**: points lost only to unseen screens. At 10 or more, show them
  on the score line and say the grade reflects missing captures.

## 1. Landing and quiz — 25 (web funnel)

| Check | Pts |
|---|---|
| The first screen restates the ad's promise and the product, and starts with one easy answer or a clear start button. Half: one of the two is missing (e.g. a generic homepage with a clear start button). Zero: both missing, or a form first | 7 |
| Pacing is honest: no long dead waits between questions, loaders short and few, a progress indicator that tracks the real remaining steps (moving faster early because easy questions come first is fine). Half: one or two loaders longer than 5 seconds, or a bar that jumps. Zero: three or more loaders that add nothing, a loader that stalls until the user answers, a bar that starts slow and speeds up, or a bar unrelated to real progress | 6 |
| The result or plan screen uses the answers (goal, numbers, timeline) and makes no diagnosis, cure or guaranteed-outcome claim. Half: a generic "your plan is ready", or a dated projection without a hedge. Zero: a health or outcome claim the product can't back. No result screen: half (the row is "show the plan the answers built", on an existing screen such as the paywall header) | 7 |
| The email screen comes after the user has seen value (result, plan), or not before payment, and says why. Half: before any value but with a reason, or after value but with no reason. Zero: as the first step, or before any value with no reason. (A forced password account is judged once, in Checkout check 2) | 5 |

## 1L. In-app link-out screen — 25 (link-out mode)

| Check | Pts |
|---|---|
| The store purchase and the web option sit side by side, each labelled with its price and what happens next. Half: the web option without a price, or IAP visually hidden. Zero: no store purchase option on the screen | 9 |
| A short, neutral note that the user leaves the app to pay, near the web button. Half: only an icon. Zero: none | 8 |
| The savings claim matches the prices shown ("save 30%" really is 30% at the same period). Half: rounded up or a different period. Zero: false | 8 |

## 2. Web paywall — 25

| Check | Pts |
|---|---|
| The amount actually charged and its period are the most prominent price; per-day, per-week or "free" figures are secondary. Half: the charge is shown but smaller than a per-day, per-week or "free" headline. Zero: the charge isn't on the paywall | 8 |
| Trial or intro terms on the paywall before payment details: what's charged today, length, the price after, how often it renews, where to cancel, ideally as a dated today / reminder / charge timeline. Half: one or two missing. Zero: recurring terms missing (blocker 1). No trial and no intro price: judge renewal terms only | 8 |
| Plans are easy to compare: at most three, the default visibly marked, strike-through prices tied to an explained reference. Half: four or more plans, or an unexplained reference price. Zero: a pre-selected plan the user can't see is selected | 5 |
| No pressure: no countdown unless the offer truly ends, no "discount reserved for you" that resets. Half: a real deadline shown loudly. Zero: fake or resetting timer (blocker 2) | 4 |

## 3. Checkout screen — 25

| Check | Pts |
|---|---|
| Payment buttons ordered for the market: Apple Pay (or the device wallet) above the card form on phones; PayPal visible in Germany and EMEA; local methods where the market expects them. Half: wallets present but below the card form, or PayPal missing in Germany. Zero: a card form only | 7 |
| Few fields: email and payment (plus fields tax needs); no password or account before paying. Half: name, address or phone without a stated reason, or an account step before payment with social or email-code sign-up. Zero: a full account with password before paying | 6 |
| Terms and consent at the button: the renewal sentence directly above or under the pay button; consent given by a clear action (an unticked checkbox is the safest form); the button label fits the market (in Germany "zahlungspflichtig bestellen" or an equally clear wording; in the EU, if the funnel asks users to waive the 14-day withdrawal, a separate checkbox for it). Half: consent only by "by continuing you agree" text, or the right label missing in a named market. Zero: terms only behind a link or below the fold, or two of these problems at once | 6 |
| Error and waiting states are designed: a decline screen that says what happened and offers another method; a 3-D Secure or bank-app wait that keeps the user's place. Half: a generic error. Not captured: half, held back | 6 |

## 4. After payment — 25

| Check | Pts |
|---|---|
| Upsell screens: each has its own accept with the exact price and whether it recurs, and a decline of equal weight; at most two in a row. Half: price or recurrence missing, a weaker decline, or three or more. Zero: blocker 3. No upsells: full | 7 |
| The confirmation screen says what was bought, today's charge, the next charge date and amount, and where to cancel. Half: one or two missing. Zero: three or more missing | 5 |
| The hand-off screen into the app: a clear "get the app" step (store button on phones, QR code on desktop, or a text link) and a first login without a new password (magic link, deep link, the same email code). Half: a download link, but the app then asks for a password (new or the same one) or a fresh sign-up; or only "check your email" for the app link. Zero: no path to the app. Not captured: half, held back | 8 |
| The first app screen for a web buyer recognises the purchase (no paywall shown again, a welcome that names the plan). Half: lands on a generic home. Not captured: half, held back | 5 |

## Grade bands

| Score | Grade | How to frame the teardown |
|---|---|---|
| 85–100 | Strong | Refinements. Say it's a strong funnel. |
| 70–84 | Solid | A few clear gaps worth testing. |
| 50–69 | Leaking | The screens are costing purchases or trust. |
| 0–49 | Needs work | Fix blockers and disclosures first. |

