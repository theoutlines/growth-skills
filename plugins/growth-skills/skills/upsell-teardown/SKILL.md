---
name: upsell-teardown
description: >-
  Tear down a mobile subscription app's in-product upsells, everything that
  sells after onboarding: locked-feature gates, usage limits and counters,
  contextual paywalls, upgrade screens for people who already pay (higher
  tier, annual switch, family, lifetime), AI credit packs, reverse trials and
  always-on Premium surfaces. Returns a 100-point score that never rewards
  pressure, store and legal flags, a report card and ranked test ideas
  grounded in 50 published tests, case studies and benchmark rows plus public reports, each labelled by
  evidence strength. Use this WHENEVER someone shares feature-gate, limit,
  "upgrade to Pro", credits, plan-upgrade or Premium-tab screens, asks how to
  monetize free users or upsell existing subscribers, where to put paywalls
  inside the product, how to sell AI credits, or compares two upsell designs.
  For the first paywall after onboarding prefer onboarding-teardown or
  flow-teardown; for a single paywall screenshot prefer paywall-teardown.
---

# Upsell Teardown

Most paywall views happen after the first session, and they start more than a
third of subscription revenue, but each one converts about four times less
than the onboarding paywall. This skill reviews that in-product layer as a
system: what triggers an upsell, what the gate blocks, what the screen says,
how it treats people who already pay, and how often it comes back.

**Scope: the designer's surfaces.** Only screen changes are scored or go in
the table. Billing setup, credit policy, campaigns and legal review are out of
scope: don't mention them.

Never invent a number. Every figure you quote comes from the references
(`evidence.md` test #U1–#U66 or benchmark row, `categories.md`,
`platform-rules.md`, or counts in `flows.md`), with its strength. Arithmetic
on the user's own numbers is fine; say it's yours.

**The evidence is thinnest where teams ask most.** Only three strong tests
are from subscription apps (#U1, #U22, #U32). No public test covers the
annual switch for monthly payers, family upsells, frequency caps, locked
badges or push upsells with a holdout. Label those recommendations
hypotheses.

## Input

- **Screens**, grouped by trigger: locked-feature taps, limit screens,
  upgrade screens for payers, Premium tab or settings card, credit store,
  trial countdowns. Order inside a group as the user sees it. If you number
  them, number by group (G1 gate, L1 limit, P1 payer, S1 surface).
- **Or Figma frames**: a figma.com link to the frames or a section. When a
  Figma connector is available, read each frame as an image (its screenshot
  tool) in the order of the flow, and use layer text for copy. Say which
  frames you read. A design not shipped yet is scored the same way; call it
  a pre-hand-off check.
- **Or a description**; say the score is from a description.
- **The model**: free use (freemium, soft paywall, reverse trial, ads tier) or
  hard paywall. If not given, infer it and say so.
- **Billing surface**: App Store, Google Play or web.
- **Optional facts** that screens can't show: frequency rules, subscription
  groups, Android replacement mode, plan mix (share monthly), credit
  allowances.
- **Optional numbers**: paywall views or trigger hits per day, view → paid,
  share of revenue from in-app paywalls, monthly share.
- **Optional markets** (US, EU, UK) for the compliance flags.
- **Two versions**: comparison mode below.

Reason only from what you were given. If payer screens or limit screens are
missing, score what you have and ask.

## References

- `references/scoring.md` — the 100-point rubric, model rule, blockers, held back.
- `references/patterns.md` — 24 patterns with evidence, examples and traps,
  plus the sign-flip table.
- `references/evidence.md` — tests #U1–#U66, benchmarks, metric definitions, gaps.
- `references/ranges.md` — the range of measured lifts per pattern and metric, built only from `evidence.md`.
- `references/categories.md` — placement share, later-paywall conversion,
  plan mix and consumables by bucket, and what each bucket leans on.
- `references/platform-rules.md` — Apple (3.1.1, 3.1.2, HIG, subscription
  groups and levels, offers), Google Play (offers, replacement modes), US, EU,
  UK, and an upsell checklist.
- `references/flows.md` — about 55 apps' in-product upsells from public
  Mobbin captures, described in our own words with links.

## Process (internal — do NOT show these steps)

1. **Inventory.** Group the screens by trigger. Set the model, surface,
   bucket (RevenueCat SOSA buckets; "AI app" is a tag) and markets. Mark the
   main upsell screen and the trigger that opens it most often.
2. **Score** with `scoring.md`: the model rule, the unseen-screen rule and
   the blockers. Count held-back points.
3. **Sign-flip sweep.** Check every tactic against "Where it flips" in
   `patterns.md`. A tactic on its losing side is a Fix first or High row.
4. **Compliance sweep.** Run pattern 24 and the checklist in
   `platform-rules.md`. Every hit is a flag with the rule and a link, never a
   legal ruling.
5. **Category fit.** Look up the bucket in `categories.md`: how much revenue
   later paywalls carry, the plan mix (room for an annual switch), consumables
   and what the bucket leans on. A bucket's normal shape is not a gap.
6. **Pick rows.** Up to 8 rows, never pad (fewer when the flow has few gaps). Priority is one of four values:
   - **Fix first**: a blocker, a screen flag, a zero on "core habit not
     blocked" or on frequency, or a sign flip on its losing side backed by a
     strong test or a store rule (other flips take the priority of their
     evidence).
   - **High**: a strong test on the same kind of change (#U1 gate copy, #U22
     lifetime anchor, #U32 credits off the first paywall, also on a later
     paywall) for a single
     change. A strong test from a non-subscription business is Medium.
   - **Medium**: directional evidence; a benchmark (Part 2 rows, or Part 1
     rows marked "not a test": they describe what apps see, not what a change
     does); a strong test that's off-target (games, web books, Pandora); a
     ⚠️ checklist item. Hypotheses with no public test are Medium at most and
     say "hypothesis".
   - **Low**: anecdotal or observed only.
   Order: Fix first → rows for the weakest dimension (as defined in
   `scoring.md`) → the rest by priority, then evidence strength × effort.
   Never recommend blocking more, showing more often or adding urgency as a
   growth lever; tightening a free tier is a test with an engagement cost
   (pattern 8), never a default.
7. **Durations** (only with traffic). Run `scripts/test_duration.py`:
   - gate and upsell-screen tests are randomised per user who hits the
     trigger: pass trigger hits (or paywall views) per day as `--installs`
     and view → paid as `--baseline`; say this unit.
   - tests on the free tier itself are randomised at install: installs per
     day and install → paid; add a note that engagement needs a longer read
     (#U13).
   - payer-ladder tests are randomised per subscriber who sees the offer.
   - add `--metric paid --trial-days N` when the offer starts a trial.
   Default to a 10% relative change unless the user names another. Later
   paywalls convert about 0.17–0.32% per view by category, so a 10% change
   needs a very large sample (run the script to see it). If a test runs past 8 weeks,
   say so and give the change detectable in 4 weeks (`--weeks 4`), or test
   on a higher-rate step (upsell open → purchase start) and say which.
8. **Render the card** (below), then write the response.

## Output format

**Line 1 — read.** Model, surface, bucket and the single biggest issue in one
sentence. If it's a strong system, say so.

**Line 2 — score.**
**68/100 — Leaking** · Triggers 14/20 · Gate 12/20 · Upsell screen 19/25 · Payer ladder 10/20 · Surfaces 13/15
(Add "· 12 held back" when held-back points reach 10. Hard paywall: "Payers-only score: 72/100 — Solid (Upsell screen 19/25 · Payer ladder 12/20 · Surfaces 12/15)". Blocker: "49/100 (cap)".)

**Line 3 — the system in numbers.** How many triggers, what each blocks, what
the user sees first at a limit, what payers are offered, what's always on.
Example: "3 locked features open one generic paywall; scans stop at 5 a
week with no meter; payers see the same subscribe paywall; a Pro card sits in
settings."

**Line 4 — numbers** (only if given): each against its benchmark row
(later-paywall view → paid by category, placement share, plan mix).

**Line 5 — already working.** One prose line.

**Sign flips** (only if any): one bullet per tactic on its losing side, with
the screen, the side it should be on, and the evidence.

**Screen flags** (only if any): one bullet each with the screen, the
rule and its source name. End with: "Flags, not legal advice."

**The table**, in the order from step 6:

| # | Priority | Screen | Pattern | Test idea | Evidence | Range seen | Duration |

- **Pattern**: the name from `patterns.md`.
- **Test idea**: the concrete change, including copy direction.
- **Evidence**: the most on-target test or benchmark with its number and
  tier; "hypothesis" where no test exists. Never an expected lift for this app.
- **Range seen**: from `references/ranges.md`, the lowest to highest lift
  measured in published tests of this pattern, on the metric the row is
  judged on, with the number of tests ("+8% to +36% · 3 tests"). One test:
  its number. None: "no published range". It shows what other apps saw,
  never a forecast for this app; don't compute new ranges or mix metrics.
- **Duration**: only with traffic; otherwise drop the column.

**The report card** right after the table.

**Not captured**: one line on missing screens.

**Your data** (one line; skip it when the user gave their numbers): the
ranking and durations get sharper on their own funnel (trigger hits or in-app paywall views per day, view → paid, share of monthly payers). If an
analytics or subscription connector is available in this session (Amplitude,
Mixpanel, RevenueCat, Adapty or similar), offer to pull those numbers.

**Closing line**, verbatim:
> *Published results are one company's outcome in its own setting, not the change your upsells will get. Annual switches, family upsells and frequency caps have no public test, and compliance notes are flags, not legal advice. Run your own A/B test before shipping.*

## Report card

A PNG with the score, a line of key screens, thumbnails with pins, the five
dimension bars and the ranked tests.

1. Pick up to 8 key screens: the main gate, the limit screen, the main
   upsell, the payer upgrade screen, the plan surface, and any screen a row
   touches.
2. Write `upsell.json` (see `scripts/example.json`). In `flow`: `order` lists
   the screen ids in the order you show them (G1, L1, U1, P1, S1…),
   `paywall_at` = the main upsell screen with `"marker_label": "upsell"`,
   `value_at` = the trigger that opens it most with `"value_label":
   "trigger"`, and payer screens as `extra` with `"extra_label": "payers"`.
   Dimension keys: `triggers`, `gate`, `screen`, `ladder`, `surfaces`. For a
   hard paywall, list only the three scored dimensions, set `total` to the
   scaled score and add "payers-only score" to `subtitle`. Use plain characters (~, -, x); the
   bundled font has no ≈, ✓ or ✗.
3. Run `python3 <skill-dir>/scripts/render_report.py --data upsell.json --out
   <output-dir>/upsell-teardown.png` (Pillow). Output dir:
   `/mnt/user-data/outputs/` on claude.ai, the working directory elsewhere.
4. Share the PNG after the table. If rendering fails, skip it silently.

## Comparison mode

Two versions: score both, map screens between them in "What changed". If
held-back points differ by 10+, compare on checks seen in both. Show before →
after per dimension, what changed with evidence, new risks (more blocking,
more frequency, new urgency, compliance hits), then the remaining table for
the better version. If several things changed, name the one change to test
alone first.

## Framing rules

- **Screens only.** If it can't be changed in a design file, leave it out.
- **Never reward pressure.** Blocking the habit, showing more often and fake
  urgency can raise short-term conversion and cost engagement and legal risk
  (#U4, #U13 on engagement; ACM v. Epic and CMA v. Emma Sleep on timers; FTC
  v. Amazon on decline wording).
- **Evidence, never prediction.** Quote what a company saw; never "this will
  lift X%".
- **Position matters.** Check the sign-flip table before recommending any
  tactic.
- **Payers are a different audience.** Never sell them the subscription they
  have; sell the next step, with the store's billing timing.
- **Model first.** A hard-paywall app has no free-user upsells to fix; don't
  recommend a freemium switch as a design change.
- **Category first.** Use the bucket's numbers, not a generic upsell.
- **Mobbin and other sources.** Describe in your own words and link; don't
  copy. Example teardowns don't name the app.
- **Compliance is a flag, not a ruling.** For a store-rules review, suggest
  paywall-store-compliance if installed.
