---
name: retention-teardown
description: >-
  Tear down the screens a mobile subscription app shows between the first
  purchase (or trial start) and the first renewal: welcome after purchase,
  notification primer, reminders, first-week guidance, streaks and progress,
  value recaps, the in-app trial-ending notice, the return screen and the
  rating and widget asks. For product designers: a 100-point score for what
  can be changed on screen (never rewarding pressure), Apple and Google
  screen flags, a report card and ranked tests from 61 published tests and
  public benchmarks. Use this WHENEVER someone shares welcome-to-Premium,
  notification, reminder, streak, recap, trial-status, welcome-back or
  rating-prompt screens, or asks how to keep new subscribers until the first
  renewal. For paywalls prefer paywall-teardown, onboarding
  onboarding-teardown, upsells upsell-teardown, cancel flows
  cancel-flow-teardown.
---

# Retention Teardown

The first renewal is the steepest drop for every plan length, and most of
the decision comes early: more than half of 3-day-trial cancellations happen
on the day the trial starts, and a third of annual cancellations come in
month 1. This skill reviews the screens that sit in that window as one
system: what a new payer sees first, how the app asks for notifications and
reminders, how progress and streaks behave (including when they break), how
the user sees their own value before the charge, and how the app treats them
when they come back.

**Scope: the designer's surfaces.** Only what a designer changes on a screen
is scored or put in the table. Push and email programmes, send times,
pricing, billing setup and legal review are out of scope: don't mention them.
Paywalls, upsells and the cancel flow have their own skills; mention them in
one line if they show up here.

Never invent a number. Every figure you quote comes from the references
(`evidence.md` test #R1–#R61 or benchmark row B1–B64, `categories.md`,
`platform-rules.md`, or counts in `flows.md`), with its strength. Arithmetic
on the user's own numbers is fine; say it's yours.

**The evidence is uneven.** Most strong tests are Duolingo or lab studies of
streaks (#R25, #R28, #R29, #R37–#R39). No public test covers the welcome
screen after purchase, an in-app trial-ending notice, an in-app weekly
recap, a return screen, empty states or a mobile checklist. Label those
recommendations hypotheses.

## Input

- **Screens**, in the order a new payer meets them: the screen after
  purchase or trial start, the first session, the notification ask and
  primer, reminder setup, home with progress, the post-session screen, a
  missed-day or broken-streak state, a recap, the trial status and
  trial-ending notice, a return after a gap, the rating ask, a widget
  prompt. If you number them, use W (welcome), N (notifications), H
  (habit), V (value), R (return and asks).
- **Or a description**; say the score is from a description.
- **Offer**: trial or direct purchase. **Platform**: iOS, Android or both.
  Infer and say so if not given.
- **Habit fit**: does the product have a recurring task? If it doesn't, the
  habit dimension scores "no habit loop".
- **Optional numbers**: new payers or trial starts per day, D7 or week-1
  activity, trial → paid, first renewal, notification opt-in.
- **Two versions**: comparison mode below.

Reason only from what you were given. If the broken-streak state, the
trial-ending notice or the return screen is missing, score what you have and
ask.

## References

- `references/scoring.md` — the rubric, offer and habit rules, blockers, held back.
- `references/patterns.md` — 22 screen patterns with evidence and traps,
  plus the sign-flip table.
- `references/evidence.md` — tests #R1–#R61, benchmarks B1–B64, metric definitions, gaps.
- `references/categories.md` — trial → paid, first renewal and "not enough
  usage" by bucket, and which screens matter most in each.
- `references/platform-rules.md` — Apple and Google rules behind the flags
  (notification asks, rating prompt, widgets, Live Activities), regulator
  guidance on nagging and confirmshaming, and a screen-flag list.
- `references/flows.md` — 98 screens from about 60 apps on public Mobbin
  captures (iOS), described in our own words with links.

## Process (internal — do NOT show these steps)

1. **Inventory.** Order the screens as a new payer meets them. Set the
   offer, platform, bucket (RevenueCat SOSA buckets; "AI app" is a tag) and
   habit fit. Mark the welcome screen, the notification ask, the progress
   surface, the trial-ending notice and the rating ask.
2. **Score** with `scoring.md`: offer and habit rules, the unseen-screen
   rule and the blockers. Count held-back points.
3. **Sign-flip sweep.** Check every tactic against "Where it flips" in
   `patterns.md`. A tactic on its losing side is a Fix first or High row.
4. **Flag sweep.** Check the screens against the flag list in
   `platform-rules.md` §5; only screen elements become flags.
5. **Category fit.** Look up the bucket in `categories.md`. A bucket with no
   daily habit is not missing a streak.
6. **Pick rows.** Up to 8 screen changes, never pad (fewer when the flow has
   few gaps). Priority is one of four values:
   - **Fix first**: a blocker or a flag from the closed list in
     `scoring.md`, or a sign flip on its losing side backed by a store rule
     or a strong in-app test (other flips, including those backed only by
     lab studies, take the priority of their evidence).
   - **High**: a strong test on the same kind of change in an app (#R25 easy
     streak rule, #R28 commitment screen, #R29 streak protection, #R2 primer
     copy, #R48 for the reminder opt-in ask at trial start, a Dimension 2
     row). Lab studies (#R37–#R39) and off-target field tests (#R40, #R41,
     #R47) are Medium. Rows on the welcome screen's content, an in-app trial
     card or the trial-ending notice have no test: Medium at most, even when
     #R48 is cited.
   - **Medium**: directional evidence, a benchmark, an off-target strong
     test, or a ⚠️ item from `platform-rules.md` §5 that isn't on the
     closed flag list (asking at launch, primer layout, rating timing). Hypotheses with no public test are Medium at
     most and say "hypothesis".
   - **Low**: anecdotal or observed only.
   Order: Fix first → rows for the weakest dimension (as defined in
   `scoring.md`) → the rest by priority, then evidence strength × effort.
   Never recommend more asks, more notifications, guilt or loss copy, or
   countdowns as a lever. Never add a streak to an app with no recurring
   task.
7. **Durations** (only with traffic). Run `scripts/test_duration.py`. These
   screens are randomised per new payer or trial starter: pass new payers
   (or trial starts) per day as `--installs`, and the decision metric's rate
   as `--baseline`. For trial → paid use `--metric paid --trial-days N`; for
   an activity metric (week-1 active, a streak kept) use `--metric trial`
   and say which metric you mean. Default to a 10% relative change. First
   renewal can't be read inside a normal test window (a monthly plan needs a
   month plus the billing lag, an annual plan a year): read an early metric
   and say which. If a test runs past 8 weeks, say so and give the change
   detectable in 4 weeks (`--weeks 4`).
8. **Render the card** (below), then write the response.

## Output format

**Line 1 — read.** Offer, platform, bucket, habit fit and the single biggest
issue in one sentence. If it's a strong system, say so.

**Line 2 — score.**
**64/100 — Leaking** · Welcome 13/20 · Notifications 12/20 · Habit 15/25 · Value 12/20 · Return & asks 12/15
(Add "· 12 held back" when held-back points reach 10. Blocker: "49/100 (cap)", or "49/100 (cap; 90 before the cap)" when the cap binds.)

**Line 3 — the system in numbers.** When the notification ask comes, what
keeps the streak, what a missed day shows, whether the user sees their own
value or the trial date in the app, where the rating ask fires. Example:
"System prompt at launch; streak needs the full 20-minute goal; a missed day
resets to 0 with a sad mascot; no trial date in the app; rating asked on the
welcome screen."

**Line 4 — numbers** (only if given): each against its benchmark row
(trial → paid B9–B11, first renewal B15–B18, push opt-in B38 or B44).

**Line 5 — already working.** One prose line.

**Sign flips** (only if any): one bullet per tactic on its losing side, with
the screen, the side it should be on, and the evidence.

**Screen flags** (only if any): one bullet each with the screen, the rule
and its source name. End with: "Flags, not legal advice."

**The table**, in the order from step 6:

| # | Priority | Screen | Pattern | Change to test | Evidence | Duration |

- **Pattern**: the name from `patterns.md`.
- **Change to test**: the concrete screen change, with copy direction.
- **Evidence**: the most on-target test or benchmark with its number and
  tier; "hypothesis" where no test exists. Never an expected lift for this
  app.
- **Duration**: only with traffic; otherwise drop the column.

**The report card** right after the table.

**Not captured**: one line on missing screens.

**Closing line**, verbatim:
> *Published results are one company's outcome in its own setting, not the change your screens will get. Most streak evidence comes from Duolingo and lab studies, welcome, recap and return screens have no public test, and flags are not legal advice. Run your own A/B test before shipping.*

## Report card

A PNG with the score, a line of key screens, thumbnails with pins, the five
dimension bars and the ranked tests.

1. Pick up to 8 key screens: the welcome, the notification ask, home with
   progress, the broken-streak state, the recap or trial notice, the return
   screen, the rating ask, and any screen a row touches.
2. Write `retention.json` (see `scripts/example.json`). In `flow`: `order`
   lists the screen ids in the order you show them (W1, N1, H1, V1, R1…),
   `paywall_at` = the trial-ending notice or recap with `"marker_label":
   "renewal"`, `value_at` = the first-session screen with `"value_label":
   "first value"`, and return or rating screens as `extra` with
   `"extra_label": "later"`. Dimension keys: `welcome`, `notifications`,
   `habit`, `value`, `return`. Use plain characters (~, -, x); the bundled
   font has no ≈, ✓ or ✗.
3. Run `python3 <skill-dir>/scripts/render_report.py --data retention.json
   --out <output-dir>/retention-teardown.png` (Pillow). Output dir:
   `/mnt/user-data/outputs/` on claude.ai, the working directory elsewhere.
4. Share the PNG after the table. If rendering fails, skip it silently.

## Comparison mode

Two versions: score both, map screens between them in "What changed". If
held-back points differ by 10+, compare on checks seen in both. Show before →
after per dimension, what changed with evidence, new risks (more asks, loss
or guilt copy, promos on progress surfaces), then the remaining table for the
better version. If several things changed, name the one change to test
alone first.

## Framing rules

- **Screens only.** If it can't be changed in a design file, leave it out.
- **Never reward pressure.** Guilt at a broken streak, countdowns, re-asks on
  every open and promos on progress surfaces can raise a short-term number
  and cost engagement and trust (#R38 broken streak vs no streak; #R61 promo
  in a Live Activity; FTC "confirmshaming" and "nagging").
- **Evidence, never prediction.** Quote what a company saw; never "this will
  lift X%".
- **Position matters.** Check the sign-flip table before recommending any
  tactic (the trial reminder flipped between Blinkist and Slopes).
- **Habit fit first.** Streaks and daily reminders are for products with a
  recurring task. A utility needs a good first session and an honest trial
  notice, not a streak.
- **Category first.** Use the bucket's numbers, not a generic retention
  figure.
- **Mobbin and other sources.** Describe in your own words and link; don't
  copy. Example teardowns don't name the app.
- **Flags are flags, not legal rulings.** For a store-rules review, suggest
  paywall-store-compliance if installed.
