# Retention Score Rubric

A 100-point score for the in-app screens a subscription app shows between the
first purchase (or trial start) and the first renewal: the welcome and first
session, the notification and reminder asks, habit and progress screens, the
value and trial-ending screens, the return screen and the rating ask. **Only
what a product designer changes on a screen is scored**; push and email
programmes, pricing, billing setup and legal review are out of scope. Score
from the checks, never from impression.

## How to score

- Each check is **full**, **half** (round down) or **zero**. Nothing else.
  When half is held back, the held-back amount is the rest of the check (a
  7-point check: 3 scored, 4 held back).
- **Offer.** Trial (free or paid intro) or direct purchase. Checks marked
  "trial apps" score full for direct-purchase apps.
- **Platform.** iOS, Android or both. Primer rules differ (see Dimension 2,
  check 2). Use the platforms the user names; if none, judge iOS and say so.
- **Habit fit.** Some apps have no daily habit (a VPN, a photo editor used
  monthly, a utility). Checks in Dimension 3 that say "no habit loop: full"
  then score full; say so on the read line. Never recommend adding a streak to
  an app with no recurring task.
- **Bucket.** RevenueCat SOSA buckets; "AI app" is a tag. Finance apps: use
  Utilities and say so.
- **Unseen and undescribed.** If what you saw already earns full → full. If
  a screen or element the check needs wasn't captured or described at all →
  half, the other half held back (never the whole check). If you saw it
  missing or wrong → that's seen; score it. Uncaptured screens that could
  only hold a violation → don't assume it. An element mentioned without
  detail scores on what's stated, seen. An element the user says exists but
  didn't share ("we also have a trial banner") is not captured: half, held
  back, in the check that names it.
- **Several parts in one check.** Full when every part is met; half when one
  part is seen missing or one is not covered (held back); zero when two or
  more parts are seen missing, unless the check says otherwise.
- **One issue, one deduction.** Deduct an element once, in the check that
  names it most directly: a guilt line on a lapsed-streak screen → Dimension
  3 check 3 (not the return screen); a rating ask on the welcome screen →
  Dimension 5 check 2 (not the welcome check); a primer that blocks the app →
  blocker 1 and Dimension 2 check 4 (not check 1).
- **What silence scores.** A screen or element the check needs that isn't
  shown or described → the unseen rule (half, held back), even when the
  user lists other things as "not captured". Exceptions,
  judged only when seen or described and otherwise ignored (no loss, nothing
  held back): empty screens other than home (1.3), milestone moments (3.4),
  a setting to hide streaks or celebrations (3.5), a widget or Live Activity
  prompt (5.3). An element the user says exists but didn't share is held
  back once, in the check that names it most directly (a trial-ending banner
  → 4.3, not 1.2).
- **Half is never Fix first by itself.** A missing element is a Medium row;
  a wrong or misleading one is Fix first.
- **Nothing to judge** → full, where a check says so.
- **Never reward pressure.** No check gives points for more asks, more
  notifications, loss or guilt framing, or countdowns.

### Blockers (hard cap)

Visible on the screens. Any of these caps **the dimension it sits in at 40%
of its maximum (round down)** and the **total at 49** (Needs work), and is a
"Fix first" row:
1. **Forced ask**: the app, a feature or the next step is blocked until the
   user allows notifications or leaves a rating (Apple 4.5.4 and 3.2.2(x);
   Android "don't block the user"). Dimension 2 (notifications) or 5
   (rating).
2. **Manipulated ask**: a reward for rating or for allowing notifications, a
   "do you enjoy the app?" screen that sends only happy users to the store
   rating dialog, or a custom screen made to look like the system permission
   alert (Google Play in-app review rules and ratings policy; Apple 5.6.1
   and "filtered" feedback; Apple HIG; FTC "design elements that induce
   false beliefs"). Dimension 2 or 5.
3. **Loss pressure**: a streak or progress screen that resets a countdown,
   or sells the streak back with a timer at the moment of loss, or shames the
   decline ("No, I don't care about my goals") (FTC "confirmshaming" and
   "baseless countdown"; ICO/CMA "harmful nudges"). Dimension 3.

Cap arithmetic: first cap the blocker's dimension (its score becomes the
lower of its score and 40% of its maximum), then sum the dimensions. If that
sum is above 49, the total is 49 and the cap binds: write "49/100 (cap; 90
before the cap)", where 90 is the sum after the dimension cap. If the sum is
49 or less, the total is the sum: write "45/100 (cap)". Held-back points in a
dimension that holds a blocker aren't counted, whether or not the dimension
cap binds; held-back points elsewhere are still shown.

### Screen flags and priority

The flag list is closed. A flag is one of: the three blockers above; a
"Rate us" button that opens the system rating prompt instead of the store
page; a promotion inside a Live Activity or widget; one toggle or one ask
for both reminders and marketing (Apple 4.5.4; ICO/CMA "bundled consent"); a re-ask on every launch after a decline.
Each is a "Fix first" row stated as a design rule with its source name.
Other items in `platform-rules.md` §5 (asking at launch, primer layout,
rating timing) are scored by the checks and become Medium rows. No legal
analysis, case amounts or open legal questions: if it needs a lawyer, a
pricing decision or engineering, leave it out. Flags change the score only
through the checks below.

- **Fix first**: a blocker or a flag from the closed list.
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

## 1. Welcome and first session — 20

| Check | Pts |
|---|---|
| The screen right after purchase or trial start names what the user now has (the paid features or limits that changed) and one first step (tied to their goal when onboarding asked for one). Half: one of the two (a feature list with no first step, or a "Get started" with no word on what's included), or no welcome screen but home shows the first step. Zero: a generic congratulations only, no welcome screen and no first step, or the user lands on another paywall, upsell or rating ask | 7 |
| Trial apps: inside the app, after the trial starts, the user can see when the trial ends, what they'll be charged and where to cancel (a trial status row, card or timeline). Half: the date without the amount or the cancel path, or only on a settings screen three taps deep. Zero: none in the app. Direct purchase: full | 6 |
| Home on day 0 has a next action: a recommended first session, task or template is visible and one tap away, and any empty screen seen (library, history, gallery) carries a starter action or sample. Judge home and empty states only; the welcome screen's first step is check 1. Half: the next action is below the fold or behind a tab, or one empty state seen is bare. Zero: home is empty with no next action | 7 |

## 2. Notifications and reminders — 20

| Check | Pts |
|---|---|
| The notification ask comes in context: after the user sets a reminder, finishes a first session, starts a streak or turns on a "remind me before my trial ends" option, and it says what the user gets (their reminder, their streak, their trial date). Half: asked on the welcome screen or in onboarding with a stated benefit, or in context with generic copy ("stay updated"). Zero: the system prompt at launch with no explanation. No notifications used: full | 7 |
| The primer is honest: no fake system alert, no "Allow" button on the custom screen, no arrow at the system "Allow", no reward; reminders and marketing are separate choices (a marketing toggle with its own wording). Platform: on Android the rationale screen has a "No thanks"; on iOS a single "Continue" is fine and a "Not now" is acceptable. Half: one part missing (e.g. reminders and offers on one toggle). Zero: a look-alike system alert or a reward (blocker 2). No primer: judge the system prompt's context in check 1 and give full here | 6 |
| Reminder setup: the user picks a time (and, where it fits, days or a weekly goal) with a sensible default, offered after the first session, and can change it later in settings. Half: a fixed time the user can't pick, or set only during onboarding with no later entry point. Zero: reminders exist and the user can't set or find them. No reminders: full | 4 |
| After a decline the app keeps working, a short note says what won't happen and where to turn reminders on later, and the ask returns only at a new moment, never on every launch. Half: no note. Zero: re-asked on every launch (flag) or blocked (blocker 1). No notifications used: full. Not captured: half, held back | 3 |

## 3. Habit and progress — 25

Apps with no recurring task: checks 1–4 score full ("no habit loop"); check
5 still applies to any progress or achievement screen seen. A weekly goal or
ring counts as a goal: checks 2–4 apply to it (a missed week is its broken
state).

| Check | Pts |
|---|---|
| Progress toward the user's goal is visible where they land (home, today screen, or a widget): a streak, weekly goal, level or "x of y" in the unit the user cares about. Half: only on a profile or stats screen. Zero: the app has a recurring task and shows no progress | 6 |
| The bar is easy to keep: one short session or action keeps the streak or counts toward the goal; a weekly goal or rest days are offered where daily use doesn't fit the product. Half: the streak needs the full daily goal (whatever its length), or only a daily streak where use is naturally weekly. Zero: the streak needs more than the daily goal (several sessions, or an extra task on top). No streak or goal: full | 5 |
| The broken state is designed: missing a day shows a repair, freeze, pause or "start again" with neutral copy, and protection isn't only for sale at the moment of loss. Half: a freeze or repair exists only in a store or settings, or the lapse copy is negative without shaming. Zero: a broken streak or missed goal shown with no way back, or guilt, shame or a countdown at the loss (blocker 3). No streak or goal: full. Not captured: half, held back | 7 |
| Progress is acknowledged right after the action: a post-session screen that shows the streak or goal moving, with bigger moments at milestones. Half: only a toast, or only at milestones. Zero: the session ends with no feedback, or the post-session screen is an upsell | 4 |
| The user is in control: streaks (or celebrations) can be hidden or turned off, a promo never takes over a progress screen, widget or Live Activity, and apps for minors keep streaks off by default. Half: no way to hide streaks or celebrations. Zero: a promotion in a widget or Live Activity, (flag), or an upsell placed on the progress screen itself | 3 |

## 4. Value and renewal — 20

| Check | Pts |
|---|---|
| A recap shows the user's own value in the app before the first renewal: a weekly or monthly summary of what they did, in their unit (minutes, workouts, words, money saved), with change since last time where it helps. Half: a recap exists only once a year, or shows app-wide numbers instead of the user's. Zero: no recap anywhere in the app | 7 |
| New payers can find what they pay for: a checklist, benefits page or "your Premium" area that lists paid features, marks what's been tried and can be dismissed or collapsed. Half: a static list with no progress, or a checklist that can't be dismissed or collapsed. Zero: paid features are named only on the paywall | 5 |
| Trial apps: before the charge, an in-app notice (card, banner or screen) shows when it ends (days left or the day), the amount, what the user used during the trial, and how to cancel, without an offer that pressures the choice. Half: one or two parts missing (e.g. no usage, or no cancel path). Zero: three or more missing, or the notice is only a discount push. Direct purchase: full. Not captured: half, held back | 8 |

## 5. Return and asks — 15

| Check | Pts |
|---|---|
| A user back after days away lands on a return screen or state that resumes where they left off and, in habit apps, offers a lighter restart (a short session, a reset plan), with no guilt and no paywall for a payer. No habit loop: resuming the last item is full. Half: a habit app that resumes with no lighter option, a greeting only, or a plain home that still shows the next action. Zero: a paywall, an upsell or a guilt screen first, or a cold home with no next action and no acknowledgement of the gap. Not captured: half, held back | 6 |
| The rating ask uses the system prompt after a completed task or milestone, never in onboarding, on the welcome screen, at launch or on return; a "Rate us" button opens the store page. Half: the system prompt at a neutral moment (on app open later in the life cycle), or a custom pre-step that asks no opinion. Zero: a sentiment gate or a reward (blocker 2), or a "Rate us" button that opens the system prompt (flag). No rating ask seen: full | 5 |
| Asks are rationed: one ask per event (notifications, rating, widget, upgrade), a decline is respected for a period, no fake badges, and a widget or Live Activity prompt shows a preview of the user's own content. Half: two asks stacked in one session, or a widget prompt with only a logo tile. Zero: an ask on every open, or fake red badges to pull users back. Unknown: half, held back | 4 |

## Grade bands

| Score | Grade | How to frame the teardown |
|---|---|---|
| 85–100 | Strong | Refinements. Say it's a strong system. |
| 70–84 | Solid | A few clear gaps worth testing. |
| 50–69 | Leaking | The screens let new payers drift before the first renewal. |
| 0–49 | Needs work | Fix blockers and the basics first. |
