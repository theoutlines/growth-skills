# Cancel-flow Score Rubric

A 100-point score for the screens around a subscriber leaving: the way in,
the exit, the save, and the screens around the flow (a billing-issue banner,
help, coming back). **Only what a product designer changes on a screen is
scored**; store settings, billing setup, emails and legal review are out of
scope. Score from the checks, never from impression.

## How to score

- Each check is **full**, **half** (round down) or **zero**. Nothing else.
  When half is held back, the held-back amount is the rest of the check
  (a 5-point check: 2 scored, 3 held back).
- **One path.** Score the path of the plan the user describes (an annual
  subscriber's path if the plan is annual). Screens shown only to other users
  (trial users, another plan) are noted, not counted.
- **Surface first.** App Store, Google Play or **web** (web = any billing the
  app runs itself: card on a website, own in-app payments). Checks marked
  with a surface apply only there; on other surfaces they score full.
- **Bucket.** RevenueCat SOSA buckets; "AI app" is a tag. Finance apps have no
  SOSA bucket of their own: use Utilities and say so.
- **Unseen and undescribed.** If what you saw already earns full → full. If
  a screen or element the check needs wasn't captured or described at all →
  half, the other half held back (never the whole check). If you saw it
  missing or wrong → that's seen; score it. Uncaptured screens that could only
  hold a violation → don't assume it.
- **Several parts in one check.** Full when every part is met; half when one
  part is seen missing or one is not covered (held back); zero when two or
  more parts are seen missing, unless the check says otherwise.
- **One issue, one deduction.** Deduct an element once, in the check that
  names it most directly.
- **Offer screen** = any own screen between the first cancel tap and the
  exit that shows an alternative (plan, pause, discount) or a loss reminder.
  A subscription page whose only action is an alternative (e.g. only
  "Pause") counts as an offer screen.
- **Nothing to judge** → full, where a check says so.
- **Never reward friction.** No check gives points for extra steps.

### Blockers (hard cap)

Any of these caps **Exit at 14** and the **total at 49** (Needs work), and is
a "Fix first" row:
1. **No self-serve cancel**: cancelling needs support, chat, phone or email,
   or the app gives no way at all to find where to cancel. Text instructions
   to the store's settings are a way to cancel (scored in Way in check 3), not
   blocker 1.
2. **An offer screen with no cancel action** on it.
3. **A pre-selected alternative**: a radio button or toggle already set to
   pause, discount or another plan. A highlighted current plan or a primary
   "Keep" button is not pre-selected (it's judged in Exit check 1).

If the cap doesn't bind (Exit already ≤14, total already ≤49), still write
"(cap)" after the score. Held-back points inside a capped dimension aren't
counted.

A required survey is not a blocker: it scores zero on the survey check and is
a "Fix first" row (a dark pattern regulators have cited).

Under blocker 1 there is no exit path, so the save-screen count and the
confirmation check score zero.

### Screen flags

A flag is a screen element that a store rejects or that regulators name as a
dark pattern: cancel hidden, a save offer without a visible cancel, a
required survey, a pre-selected alternative, guilt or false claims, and (for
users in Germany) any offer or survey between the cancel button and the
confirmation page. Each is a "Fix first" row stated as a design rule with its
source name. No legal analysis, case amounts or open legal questions: if it
needs a lawyer, a pricing decision or engineering, leave it out. Markets: US,
Germany, other EU, UK (all four if none named, phrased "if you sell in…").

### Consistency and held back

- Every dimension that loses 4+ points on what you saw needs a row (held-back
  points don't). A row may fix several checks.
- **Weakest dimension** = the largest share of its maximum lost on what you
  saw; ties go to the earlier dimension in this file.
- **Held back**: points lost only to unseen screens. At
  10 or more, show them on the score line and say the grade reflects missing
  captures.

## 1. The way in — 20

| Check | Pts |
|---|---|
| A plainly labelled entry ("Subscription", "Manage subscription", "Membership") in Settings, Account or Profile. Half: only under an unrelated label (a "Go Premium" promo page) or only via a help article. Zero: none found | 7 |
| The subscription page shows plan, price and renewal date before any action. Half: one or two of the three | 7 |
| The last step is a button, not instructions. Store-billed: a button that opens the store's own subscription sheet in the app (`showManageSubscriptions`, Play deep link). Half: a link that leaves the app. Zero: text instructions only. Web: the app cancels in place (full); zero if it doesn't | 6 |

## 2. The exit — 35

| Check | Pts |
|---|---|
| Every offer screen has a cancel action as a peer button or a link in body-size, full-contrast text. Half: present but de-emphasised (small grey text, below the fold, under a big "Keep"). Zero: missing (blocker 2). No offer screens: full | 9 |
| **Save screens**: own screens between the first cancel tap and the exit, not counting the subscription page and the survey. Loss screens, offer screens and reminder-promise screens all count. One or none: full. Two: half. Three or more, or a loop back to offers: zero. Web-billed or own-billed flows with users in Germany (if named): any offer or survey between the app's own "cancel" button and its final confirmation page is a zero and a flag; if Germany isn't named, it's a Medium row ("if you sell in Germany") | 9 |
| The survey is optional (Skip visible) with 3–6 reasons plus "Other". Half: optional, but fewer than 3 or more than 6 reasons. Zero: an answer is required. No survey: full | 6 |
| Nothing pre-selected; copy is factual. Half: a countdown timer or loaded copy on the offer ("Are you giving up?"). Zero: a pre-selected alternative (blocker 3), guilt copy, or a false refund or loss claim | 6 |
| Confirmation states the end-of-access date and that no further charge will happen (Apple's or Google's sheet counts when the flow opens it). Half: one of the two, or a text-only hand-off (seen: the store's confirmation is outside the flow) | 5 |

## 3. The save — 30

**Clean-exit buckets.** Where `categories.md` says the bucket's norm is to let
people leave cleanly (Productivity; dating in Social & Lifestyle), a flow with
at most one save screen, no discount and a one-tap way back (resubscribe or
re-activate) scores full on checks 1 and 2.

| Check | Pts |
|---|---|
| The save matches the reason: at least two reasons lead to different next steps (a survey, or reason chips on the save screen). Half: one save for everyone that fits the bucket's top reason or the offer `categories.md` names for the bucket. Zero: one save that doesn't fit, a discount for every answer, or no save at all (outside clean-exit buckets) | 9 |
| A non-discount alternative on the save screen: plan switch, cheaper tier or cadence, or a pause where the billing allows it (web, Google Play). Zero: none (outside clean-exit buckets) | 8 |
| If a discount is shown: one offer, once, with its duration and the price after it. Half: one of duration or price-after missing. Zero: stacked or repeated discounts. No discount: full | 6 |
| The loss reminder is personal and factual (the user's own usage, progress or saved items). Half: a generic feature or benefits list. Zero: guilt copy, or a save screen with no loss reminder at all. No save screen at all: full. No save screen in a clean-exit bucket: full | 7 |

## 4. Around the flow — 15

| Check | Pts |
|---|---|
| A billing-issue banner or screen in the app when a payment fails, with a button to fix the payment method. Not captured: half, held back | 5 |
| Technical problems reach help: a "technical problem" answer routes to support or a fix, or a help link is visible on the subscription page or a save screen. Half: help exists only elsewhere in the app, or not seen (held back). Zero: a technical answer leads to a discount, or support is the only way to cancel (blocker 1) | 4 |
| Coming back is designed: after cancel, the subscription card shows the end date with a one-tap resubscribe; after expiry, opening the app shows a way back (a reactivation screen), not a discount pushed to active users. Half: one of the two, or only the store's own "Renew". Not captured: half, held back | 6 |

## Grade bands

| Score | Grade | How to frame the teardown |
|---|---|---|
| 85–100 | Strong | Refinements. Say it's a strong flow. |
| 70–84 | Solid | A few clear gaps worth testing. |
| 50–69 | Leaking | The basics are costing saves or trust. |
| 0–49 | Needs work | Fix the exit and compliance first. |

