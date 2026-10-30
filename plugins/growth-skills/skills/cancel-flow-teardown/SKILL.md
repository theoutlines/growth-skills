---
name: cancel-flow-teardown
description: >-
  Tear down the screens of a mobile subscription app's cancel flow: the way
  to "manage subscription", the reason survey, save offers, the last step to
  the store or the app's own cancel, the confirmation, and the screens around
  it (billing-issue banner, resubscribe, coming back). For product designers:
  a 100-point score for what can be changed on screen (never rewarding
  friction), screen flags (Apple, Google Play, California, Germany, UK), a
  report card and ranked screen tests grounded in 28 published cases and observations and
  public benchmarks, each labelled by evidence strength. Use this
  WHENEVER someone shares cancel, downgrade, "are you sure", exit-survey or
  manage-subscription screens, asks how to reduce churn at cancel, what save
  offer to show, whether a cancel flow is legal or a dark pattern, or compares
  two cancel flows.
---

# Cancel-flow Teardown

A cancel flow is where a product either keeps a subscriber honestly or loses
their trust on the way out. This skill scores the screens on what actually
helps people stay (the right alternative for their reason, a clean exit, an
easy way back), flags screen elements that stores reject or regulators name
as dark patterns, and ranks what to change and test.

**Scope: the designer's surfaces.** Only screen changes are scored or go in
the table. Store settings, billing setup, emails and legal review are out of
scope: don't mention them.

Never invent a number. Every figure you quote comes from the references
(`evidence.md` test #C1–#C28 or benchmark row, `categories.md`,
`platform-rules.md`, or counts in `flows.md`), with its strength. Arithmetic
on the user's own numbers is fine; say it's yours.

**The evidence is thin where designers need it most.** No public controlled
test measures an in-app save screen on mobile. Save-offer figures are
directional and mostly from web-billed news or SaaS. Say so whenever you
recommend a save offer, and label it a hypothesis to test. The strong
evidence (reminders, auto-renew design, contacting idle payers) is about
things outside the screens, so it rarely backs a row here.

## Input

- **Screens in order**, from the subscription entry in settings through the
  last screen (store sheet, confirmation, or what follows). After-cancel
  screens (resubscribe card, win-back offer) can be numbered A1, A2.
- **Or a description**; say the score is from a description.
- **The billing surface**: App Store, Google Play or web (any billing the
  app runs itself). If not given, infer
  it (Apple's sheet on the last screen means App Store) and say so.
- **Optional numbers**: cancel-flow entries per day, save rate, share of
  churn from failed payments, reactivation.
- **Optional markets** (US, Germany, other EU, UK) for the screen flags.
- **Two versions**: comparison mode below.

Reason only from what you were given. If a part is missing (the survey's
other branches, the screen after the offer), score what you have and ask.

## References

- `references/scoring.md` — the 100-point rubric, the hard cap and held-back rules.
- `references/patterns.md` — 16 patterns with evidence, examples and traps.
- `references/evidence.md` — cases #C1–#C28, benchmarks, metric definitions, gaps.
- `references/categories.md` — cancel reasons, reactivation and month-1
  annual cancels by bucket, and the offer that fits each reason mix.
- `references/platform-rules.md` — Apple, Google Play, US (FTC, ROSCA,
  California), Germany §312k, EU, UK DMCC, and the save-flow checklist.
- `references/flows.md` — 22 cancel flows from public Mobbin captures,
  described in our own words with links.

## Process (internal — do NOT show these steps)

1. **Inventory.** Number the screens (keep the user's numbering). Set the
   surface, the bucket (RevenueCat SOSA buckets; "AI app" is a tag) and the
   markets. Mark the first save screen and the exit (store sheet, own cancel
   button or confirmation).
2. **Score** with `scoring.md`. Apply the surface rules, the unseen-screen
   rule, the clean-exit bucket rule and the blockers. Count held-back points.
3. **Flag sweep.** Check the screens against pattern 16 and the screen
   flags in `scoring.md`. Every hit is a design rule with its source name
   ("a save offer needs a visible cancel next to it, California"), never a
   legal analysis. For users in Germany, alternatives go before the cancel
   button, never between it and the confirmation page.
4. **Match the reason mix.** Look up the bucket in `categories.md`: its top
   cancel reasons decide which alternative fits (usage → pause or lighter
   plan, cost → cadence or tier, technical → support, better app → let go or
   roadmap). A bucket's normal shape is not a gap: clean-exit buckets get
   the rule in `scoring.md`, and their rows favour a clean exit and an easy
   way back over new save screens.
5. **Pick rows.** Up to 8 rows, never pad (fewer when the flow has few gaps). Priority is one of four values:
   - **Fix first**: a blocker, a screen element flagged by the sweep (a
     required survey always), a zero on the save-screen count, or a broken
     step (text-only last step, no confirmation). Evidence tier doesn't matter.
   - **High**: a strong test on the same kind of screen change.
   - **Medium**: directional evidence, or strong but bundled or off-target.
     Save-offer rows are Medium at most and say "hypothesis on mobile".
   - **Low**: anecdotal or observed only.
   Order: Fix first → rows for the weakest dimension (as defined in
   `scoring.md`) → the rest by priority, then evidence strength × effort.
   Anything that isn't a screen change is out of scope. Never recommend adding a step, screen or
   delay, except a missing cancel button or confirmation; a save that needs a reason uses reason chips on an existing
   screen, not a new survey.
6. **Durations** (only with traffic). Run `scripts/test_duration.py`:
   - save-screen tests are randomised at cancel-flow entry, so pass
     cancel-flow entries per day as `--installs` and the save rate (share
     who don't cancel) as `--baseline`; say this unit.
   - tests judged on still paying later: add `--metric paid --trial-days 30`
     (the follow-up window) and say so, because soft saves can just delay
     the cancel.
   Default to a 10% relative change unless the user names another.
7. **Render the card** (below), then write the response.

## Output format

**Line 1 — read.** Surface, bucket and the single biggest issue in one
sentence. If it's a strong flow, say so.

**Line 2 — score.**
**71/100 — Solid** · Way in 20/20 · Exit 26/35 · Save 15/30 · Around the flow 10/15
(Add "· 12 held back" when held-back points reach 10. If a blocker applied,
write "Exit 14/35 (cap)" and "49/100 (cap)" where the cap binds, or "(cap)"
after the score where it doesn't.)

**Line 3 — the flow in numbers.** The path from settings to the exit, own
screens before the store (save screens as counted in `scoring.md`), what each
one asks, what's pre-selected, how the flow ends.
Example: "Settings › Subscription › Cancel: an 11-reason survey (Skip
visible), one plan-switch screen with cancel as a grey link, then Apple's
sheet. 4 taps, 2 own screens."

**Line 4 — numbers** (only if given): each against its benchmark row.

**Line 5 — already working.** One prose line.

**Screen flags** (only if any): one bullet each with the screen, the rule
(Apple 3.1.2, Play policy, California ARL, §312k BGB, UK DMCC…) and a link.
End with: "Flags, not legal advice."

**The table**, in the order from step 5:

| # | Priority | Screen | Pattern | Test idea | Evidence | Duration |

- **Pattern**: the name from `patterns.md`.
- **Test idea**: the concrete change, including the copy direction.
- **Evidence**: the most on-target case or benchmark with its number and
  tier; for save offers add "hypothesis on mobile". Never an expected lift
  for this app.
- **Duration**: only with traffic; otherwise drop the column.

**The report card** right after the table.

**Not captured**: one line on missing screens.

**Closing line**, verbatim:
> *Published results are one company's outcome in its own setting, not the change your flow will get. Save offers have no public controlled test on mobile, and compliance notes are flags, not legal advice. Run your own A/B test before shipping.*

## Report card

A PNG with the score, a flow line, thumbnails with pins, the four dimension
bars and the ranked tests.

1. Pick up to 8 key screens: the subscription page, the survey, each save
   screen, the exit and any screen a row touches.
2. Write `cancel.json` (see `scripts/example.json`). In `flow`: `screens`
   (count), `paywall_at` = the first save screen with `"marker_label":
   "save"`, `value_at` = the exit with `"value_label": "exit"`, `unseen`,
   and after-cancel screens as `extra` with `"extra_label": "after"`. If
   there's no save screen, omit `paywall_at`. Dimension keys: `way_in`,
   `exit`, `save`, `around`. Use plain characters (~,
   -, x); the bundled font has no ≈, ✓ or ✗.
3. Run `python3 <skill-dir>/scripts/render_report.py --data cancel.json --out
   <output-dir>/cancel-flow-teardown.png` (Pillow). Output dir:
   `/mnt/user-data/outputs/` on claude.ai, the working directory elsewhere.
4. Share the PNG after the table. If rendering fails, skip it silently.

## Comparison mode

Two versions: score both, number the second version's screens in its own
order and map them in "What changed". If held-back points differ by 10+,
compare on checks seen in both. Show before → after per dimension, what
changed with evidence, new risks (especially new friction or compliance
hits), then the remaining table for the better version. If several things
changed, name the one change to test alone first.

## Framing rules

- **Screens only.** If it can't be changed in a design file, leave it out.
- **Never reward friction.** Extra steps that lower cancellations break trust
  and draw regulators (#C7, Amazon's multi-page cancel flow), not a win.
- **Evidence, never prediction.** Quote what a company saw; never "this will
  save X%".
- **Surface first.** No pause on App Store billing; Google Play has its own
  survey and pause; web billing carries the full consumer-law load.
- **Category first.** Use the bucket's reason mix, not a generic save offer.
- **Respect the leaver.** Some churn is success (reached a goal, met
  someone); a clean exit and an easy way back are the right design there.
- **Mobbin and other sources.** Describe in your own words and link; don't
  copy. Example teardowns don't name the app.
- **Compliance is a flag, not a ruling.** For a store-rules review, suggest
  paywall-store-compliance if installed.
