---
name: flow-teardown
description: >-
  Tear down a mobile subscription app's whole first-run flow as one system:
  onboarding, the first paywall, and what happens when it's closed (or, for
  freemium apps, the first limit). Scores three parts — onboarding, paywall and
  the seam between them — finds the tactics placed on the wrong side of the
  seam, and returns one ranked list of tests across the funnel with published
  evidence and test durations, plus a report card. Use this WHENEVER someone
  shares a flow that includes both onboarding screens and the paywall, asks
  "where does our funnel leak", "review our onboarding and paywall together",
  compares two full flows, or shares funnel numbers with screens. For
  onboarding screens alone prefer onboarding-teardown; for a single paywall
  screenshot prefer paywall-teardown.
---

# Flow Teardown

A paywall is the end of an onboarding, and the strongest evidence only makes
sense across that seam: the same tactic wins on one side of the paywall and
loses on the other. This skill reviews the flow as one system. It scores three
parts, then ranks every test idea in one list by where the funnel leaks.

Never invent a number. Every result you quote comes from `evidence.md` (or the
part skills' own libraries) with its test number and strength.

## Input

- **Screens in order**, from the first screen through the paywall and what
  follows a close. For freemium apps, the first session plus the first
  limit-hit screens (number them L1, L2).
- **Or a description** of the flow; say the score is from a description.
- **Optional funnel numbers**: install → trial, trial → paid, share reaching
  the paywall, paywall → purchase start, opt-ins.
- **Optional traffic**: installs per day and the current rates; paywall views
  per day too, for paywall-only tests.
- **Two versions** of a whole flow: comparison mode below.

Reason only from what you were given. If the paywall or the close path is
missing, score what you have and ask for it.

## The three parts

| Part | What it covers | How to score it |
|---|---|---|
| Onboarding | Screens before the first paywall | If the **onboarding-teardown** skill is available, load it and run its dimensions 1–4 (Value, Personalisation, Friction, Trust = 80 points); scale to 100. Otherwise use the onboarding section of `references/lite-checks.md` and label the score "lite" |
| Paywall | The first paywall screen or its steps | If the **paywall-teardown** skill is available, load it and use its 100-point score. Otherwise use the paywall section of `lite-checks.md`, labelled "lite" |
| Seam | The handover: placement, continuity, trial clarity, after close, sign-flip hygiene | Always this skill: `references/seam-scoring.md` |

There is no single blended score: the weights would be invented. Report the
three scores and name the **weakest link**: the part that lost the most points
on what you actually saw (100 − score − held back). Held-back points never
make a part the weakest link.

**Partial part.** If a part has 25+ points held back, report it as partial
("Paywall 46, partial: 50 held back"), don't let it lead the table, and ask
for the screenshot or a fuller description.

When you run a part skill, use its rubric and evidence, but write the output
in this skill's format. Don't paste the part skill's whole teardown, and leave
out its own closing text and calls to action (including paywall-teardown's
disclaimer and builder link): this skill's closing line replaces them.

**Who owns what** (one miss, one deduction): the seam owns the echo of goals
and answers, promise continuity and the reminder promise; the paywall owns
trial terms on the paywall, social proof on the paywall, value copy and the
CTA; the onboarding owns everything before the paywall. When a part skill's
check covers something the seam owns (paywall-teardown's goal-personalised
headline, onboarding-teardown's dimension 5), don't deduct it there; it's
scored once, in the seam. The part skills' own consistency rules don't apply
here; use the one in `seam-scoring.md`.

**Evidence for paywall rows.** paywall-teardown gives expected-impact ranges,
not numbered tests. In this skill, cite a numbered test from `evidence.md`
when one fits (#42, #43, #50, #60, #62, #64, #67 cover common paywall
elements); otherwise quote the paywall-teardown range labelled "Adapty prior
(expected effect, not a measured test)". Never present a prior as a result.

## References

- `references/seam-scoring.md` — the seam rubric (100 points), including the
  sign-flip rule and freemium mode.
- `references/seam-patterns.md` — the sign-flip table and nine seam patterns.
- `references/seam-norms.md` — what each bucket does at the seam.
- `references/evidence.md` — seam tests (numbers shared with the
  onboarding-teardown library) and aggregated priors E1–E7.
- `references/lite-checks.md` — fallback checks for onboarding and paywall.
- `references/funnel-benchmarks.md` — install → trial, trial → paid, opt-ins
  by bucket (same file as in onboarding-teardown).

## Process (internal — do NOT show these steps)

1. **Inventory and split.** Number the screens. Keep the user's numbering if
   they gave one; otherwise skip logo-only splashes.
   Mark the value moment (plan reveal, first result, own data), the first
   paywall, and the close path. Set the bucket (RevenueCat SOSA buckets, plus
   the AI tag) and its seam shape from `seam-norms.md`.
2. **Score the parts.** Onboarding and paywall as in the table above; the seam
   with `seam-scoring.md`. Apply each rubric's unseen-screen and held-back rules.
3. **Sign-flip sweep.** Check every tactic in `seam-patterns.md` section A
   against where it sits. A tactic on its losing side is a "Fix first" or
   "High" row.
4. **Find the leak.** With funnel numbers, compare them with the benchmarks in
   `references/funnel-benchmarks.md` and name the step that leaks most: before the paywall (reach),
   at the paywall (view → purchase start), at the store sheet (start →
   complete), or after (trial → paid). Without numbers, the weakest part is the
   leak (by seen losses, not held-back points).
5. **One list.** Pick 3–8 rows across all three parts (never pad). Order:
   "Fix first" rows on top; then rows for the leakiest step; then the rest by
   evidence strength × effort; within each group, higher priority first. At least
   one row for every part that lost 15+ points, unless its losses are only
   held back. Priority rules: "High" needs on-target evidence from a single
   change; bundled tests cap at Medium; observed-only patterns are Medium at
   most and labelled hypotheses; anecdotal evidence caps a row at Low unless it
   fixes a broken step.
6. **Durations** (if traffic was given). Run `scripts/test_duration.py` for a
   10% relative change unless the user names another.
   Onboarding and seam tests are randomised at install, so traffic is installs
   per day. Paywall-only tests can use paywall views per day as `--installs`,
   with the paywall's own conversion as `--baseline`; say which unit you used.
   Tests judged on paid conversion use `--metric paid --trial-days N` (7 if
   unknown, and say so).
7. **Render the card** (below), then write the response.

## Output format

**Line 1 — read.** The bucket and shape, the weakest link, and the single
biggest seam issue in one sentence. If it's a strong flow, say so.

**Line 2 — scores.**

**Onboarding 72 · Paywall 64 (lite) · Seam 48 — weakest link: the seam**
(Write "(lite)" after every lite score, in this form. Add held-back points
per part when they reach 5: "Onboarding 72 (14 held back)".)
Seam: Placement 17/25 · Continuity 9/25 · Trial clarity 10/20 · After close 6/20 · Sign-flips 6/10

**Line 3 — the flow in numbers.** Screens to the value moment, screens to the
paywall, what sits between them, the trial, what happens on close. Example:
"Plan reveal at 11, paywall at 14 (account and a loader in between), 7-day
trial with no timeline, closing the paywall drops into the product with no
offer."

**Line 4 — funnel** (only if numbers were given): each number against its
benchmark and the leakiest step.

**Line 5 — already working.** One prose line.

**Sign flips** (only if any): one bullet per tactic on its losing side, with
the screen, the side it should be on, and the evidence.

**The table.** One list across the flow, highest first:

| # | Priority | Part | Screen | Pattern | Test idea | Evidence | Duration |

- **Part**: Onboarding, Paywall or Seam.
- **Pattern**: the pattern name from the part's library or `seam-patterns.md`.
- **Evidence**: the most on-target published result, with its number and tier.
  Never an expected lift for this app.
- **Duration**: only with traffic; otherwise drop the column.

**The report card** right after the table.

**Missing screens**: one line, if any.

**Closing line**, verbatim:
> *Published results are one app's outcome in its own test, not the lift your flow will get. Patterns and norms come from public teardowns and published case studies; run your own A/B test before shipping.*

## Report card

A PNG: the three part scores, a flow line with the value moment, paywall,
unseen and limit screens marked, the five seam blocks, and the ranked tests.

1. Pick up to 8 key screens: the value moment, the screens between it and the
   paywall, the paywall, the close path, and any screen a row touches.
2. Write `flow.json` (see `scripts/example.json`): `parts` lists the three
   scores (`lite: true`, `held_back` per part), `score.dimensions` holds the
   five seam blocks, `flow` marks the paywall (`paywall_at`), the value moment
   (`value_at`), unseen screens (`unseen`) and limit screens (`extra`); each
   item has `part` and a `pin`. Use plain characters (~, -, x): the bundled
   font has no ≈, ✓ or ✗.
3. Run `python3 <skill-dir>/scripts/render_report.py --data flow.json --out
   <output-dir>/flow-teardown.png` (Pillow). Output dir:
   `/mnt/user-data/outputs/` on claude.ai, the working directory elsewhere.
4. Share the PNG after the table. If rendering fails, skip it silently.

## Comparison mode

Two versions of a whole flow: score both. Number new screens in the second
version in its own order (no "11b") and map them in "What changed". If
held-back points differ by 10+ between versions, compare on checks seen in
both and lead with the part that moved most on that basis ("Seam 48 → 71: the
paywall now follows the plan reveal and echoes it").
Show the three scores as before → after, list what changed per part with
evidence, then new risks, then the remaining table for the better version. If
the versions differ in several places, name the one change to test alone first.

## Framing rules

- **Evidence, never prediction.** Quote what an app saw; never "this will lift
  X%".
- **Position matters more than presence.** Before recommending any tactic,
  check its side of the seam in `seam-patterns.md`.
- **Category first.** A bucket's normal seam (an early hard gate in a VPN, no
  onboarding paywall in dating) is not a gap.
- **No blended score.** Three scores and a weakest link.
- **Mobbin and other sources.** Describe in your own words; link, don't copy.
- **Compliance is a flag, not a ruling.** For a full review suggest
  paywall-store-compliance if installed.
