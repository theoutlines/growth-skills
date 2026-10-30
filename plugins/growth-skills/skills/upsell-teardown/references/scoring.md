# In-product Upsell Score Rubric

A 100-point score for the upsells a subscription app shows after onboarding:
what triggers them, the gate, the upsell screen, the ladder for people who
already pay, and the always-on surfaces, frequency and credits. **Only what
a product designer changes on a screen is scored**; billing setup, credit
policy, campaigns and legal review are out of scope. Score from the checks,
never from impression.

## How to score

- Each check is **full**, **half** (round down) or **zero**. Nothing else.
  When half is held back, the held-back amount is the rest of the check (a
  5-point check: 2 scored, 3 held back).
- **Model first.**
  - **Free use** (freemium, soft paywall that lets people in, reverse trial,
    ads tier): all five dimensions.
  - **Hard paywall** (nobody uses the product without paying): dimensions 1
    and 2 don't apply. Score 3–5 out of 60, multiply by 100/60 and round half
    up. Say "payers-only score" on the score line. Held-back points are
    scaled the same way, and the 10-point threshold applies to the scaled
    number. In dimension 5, judge payers only (see the checks).
- **Surface.** App Store, Google Play or web (any billing the app runs
  itself). Ladder check 4 (the timing copy) is judged per surface.
- **Bucket.** RevenueCat SOSA buckets; "AI app" is a tag. Finance apps: use
  Utilities and say so.
- **Unseen and undescribed.** If what you saw already earns full → full. If
  a screen, audience or element the check needs wasn't captured or described
  at all (no payer screens, no frequency rule, no decline mentioned) → half,
  the other half held back (never the whole check). If you saw it missing or
  wrong → that's seen; score it. Uncaptured screens that could only hold a
  violation → don't assume it. An element mentioned without detail scores on
  what's stated, seen.
- **Several parts in one check.** Full when every part is met; half when one
  part is seen missing or one is not covered (held back); zero when two or
  more parts are seen missing, unless the check says otherwise.
- **One issue, one deduction.** Deduct an element once, in the check that
  names it most directly: what the tier gives on a limit screen → Triggers
  check 2 (not the screen check); upgrade timing → Ladder check 4 (not the
  price check); a fake timer → blocker 1 and the pressure check (not
  frequency; the frequency "daily discount banner" is for real offers).
- **Half is never Fix first by itself.** A missing element (price, timing,
  amounts) is a Medium row; a wrong or misleading one is Fix first.
- **Nothing to judge** → full, where a check says so.
- **Never reward pressure.** No check gives points for blocking more, showing
  more often or adding urgency.

### Blockers (hard cap)

Visible on the screens. Any of these caps **The upsell screen at 10** and the
**total at 49** (Needs work), and is a "Fix first" row:
1. **Fake urgency**: a countdown or "only today" claim on an offer that isn't
   really ending, or a timer that resets.
2. **No real choice**: an upsell over the product with no way to decline, a
   shaming decline ("No, I don't want…"), a pre-checked paid add-on that gets bought along with the main purchase, or
   a layout where navigating buys. A highlighted or pre-selected option on a
   choice sheet that still needs the store's confirmation is a default, not
   a blocker.

If the cap doesn't bind, still write "(cap)" after the score. Held-back
points inside a capped dimension aren't counted; held-back points elsewhere
are still shown.

### Screen flags

A flag is a screen element that a store rejects or that regulators name as a
dark pattern: a fake or resetting timer, no way to decline, a shaming
decline, a pre-checked paid add-on, the subscribe paywall shown to people who
already pay. Each is a "Fix first"
row stated as a design rule with its source name. No legal analysis, case
amounts or open legal questions: if it needs a lawyer, a pricing decision or
engineering, leave it out. Flags change the score only through the checks
below.

### Consistency and held back

- Every dimension that loses 4+ points on what you saw needs a row (held-back
  points don't). A row may fix several checks.
- **Weakest dimension** = the largest share of its maximum lost on what you
  saw; ties go to the earlier dimension in this file.
- **Held back**: points lost only to unseen screens or invisible settings. At
  10 or more, show them on the score line and say the grade reflects missing
  captures.

## 1. Triggers — 20 (free use only)

| Check | Pts |
|---|---|
| A locked feature opens an upsell about that feature (contextual gate). Half: some locks open a contextual upsell and some a generic paywall, or all open a generic paywall. Zero: no way to upgrade from the lock, or an error. No locked features: full | 7 |
| A limit-reached screen says what ran out, when it resets (or that it doesn't) and what the tier gives. Half: one or two of the three. Zero: silence, an error, or a generic paywall. No limits: full | 6 |
| The core habit isn't blocked: what free users do daily keeps working, and gates sit on extras. Full also when the core action keeps working at reduced quality without paying (a smaller model, a lower resolution). Half: a core action is limited (including mid-task) but has an allowance with a reset and a free way through (wait, ad, earn). Zero: a core action is hard-blocked or stopped halfway with paying as the only way to continue; this zero is also a sign flip (Fix first). A half here is not a sign flip | 7 |

## 2. The gate — 20 (free use only)

| Check | Pts |
|---|---|
| Remaining use is visible before the wall (counter, bar, "x of y") near the action or in a usage screen. Half: only on a settings or account screen, or only after the first hit. Zero: limits exist and no meter. No limits: full | 6 |
| The limit is set in the unit people value (minutes, outputs, scans, exports) or on a feature. Half: an arbitrary count not tied to an outcome (5 items, 3 projects). No limits: full | 5 |
| A free way past a limit (wait with a timer, remaining allowance, ad, "continue free") is offered next to the upgrade. Half: it exists but is hidden or greyed out. Zero: a hard limit with paying as the only option. No limits: full | 5 |
| Where the paid value is a result, a preview, blur or partial result comes first. Half: a hard gate where a preview was possible. Zero: the gate takes away something the user already had or made (own content, earlier free feature). Value not showable: full | 4 |

## 3. The upsell screen — 25

Judge every upsell screen seen (free users and payers); a check that fails
on one screen fails.

| Check | Pts |
|---|---|
| A contextual upsell names the blocked task or feature in its headline. Half: some do, or the task is named below a generic headline. Zero: none do. No contextual upsells: full | 6 |
| The screen says what the tier adds: every limited thing with its amount (scans, credits, messages), other features by name. Half: limited things named without amounts, or "unlimited" without detail. Zero: only "Pro" or "Premium" | 5 |
| Total billed price and period, and when the charge happens, before the purchase button. Half: one of the two missing (e.g. "+$2/mo" only, or no timing on an upgrade). Zero: no price on the screen before the store sheet | 6 |
| A clear decline: a readable "Not now" or close. Half: a small grey or delayed close. Zero: none, or a shaming decline (blocker 2) | 4 |
| No pressure: no countdown unless the offer truly ends, nothing pre-checked. Half: a real deadline shown loudly, or loaded copy. Zero: fake or resetting timer, pre-checked add-on (blockers 1 and 2) | 4 |

## 4. The payer ladder — 20

| Check | Pts |
|---|---|
| Active subscribers see an upgrade screen naming their current plan, never the subscribe paywall. Half: plan list without the current plan marked. Zero: the subscribe paywall shown to subscribers. Not captured: half, held back | 6 |
| A next step exists for payers: a higher tier, family plan or bundle with a concrete extra, offered in the app. Half: only a plan list in settings, or only on the web. Zero: none | 6 |
| Monthly payers are offered annual outside the cancel flow (status screen, banner after engaged use, store upgrade offer). Half: only in a plan list or only on the cancel sheet. Zero: an annual plan exists and monthly payers are never offered it. No monthly plan, or no annual plan: full. Not covered: half, held back | 4 |
| Upgrade copy matches store billing: iOS upgrade now with prorated refund, downgrade and same-level duration change at renewal; Android and web the actual start and charge date. Half: timing missing. Zero: wrong timing | 4 |

## 5. Surfaces, frequency and credits — 15

| Check | Pts |
|---|---|
| A persistent plan surface: for free users a plan card or row; for payers plan, renewal date and upgrade/downgrade/cancel paths. Half: one of the two audiences covered. Hard paywall: payers only (full if covered) | 5 |
| Frequency: one upsell per trigger, a decline is respected, no discount after dismissing an in-app paywall, no standing daily discount. Half: the same upsell returns within a day of a decline, or a discount banner runs every day. Zero: the same upsell on every open or after every dismissal, or a discount right after an in-app paywall is closed (a pressure pattern: Fix first). Unknown: half, held back | 5 |
| Credits and trials. Credit apps (three parts): the plan states its allowance; packs are a top-up for subscribers, not on the first paywall (on a later main paywall: counts as half a part); each pack shows its real-money price. Trial apps: a countdown before the trial ends with what the user used, plus a plain "keep free" path (free use) or the charge date and how to cancel (hard paywall). Full: all parts met. Half: one part missing. Zero: two or more missing. Apps with both: count parts across both. Neither: full | 5 |

## Grade bands

| Score | Grade | How to frame the teardown |
|---|---|---|
| 85–100 | Strong | Refinements. Say it's a strong system. |
| 70–84 | Solid | A few clear gaps worth testing. |
| 50–69 | Leaking | Upsells are costing revenue or trust. |
| 0–49 | Needs work | Fix blockers and the basics first. |

