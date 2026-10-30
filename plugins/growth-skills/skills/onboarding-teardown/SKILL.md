---
name: onboarding-teardown
description: >-
  Tear down a mobile subscription app's onboarding flow, from the first screen
  to the first paywall and what happens when it's closed. Returns a 100-point
  flow score, short notes per screen, a shareable report card, and a ranked set
  of test ideas, each tied to a named pattern, the category norm and a published
  test result with its evidence strength, plus how long each test would take.
  Use this WHENEVER someone shares several onboarding or first-run screenshots,
  a screen recording's frames, or a description of a first-run flow and asks
  what to change, test or fix — "here's our onboarding", "roast this flow",
  "why don't people start the trial", a competitor's onboarding, two versions
  of a flow to compare, or a flow still in design. For a single paywall
  screenshot, prefer paywall-teardown when it's installed.
---

# Onboarding Teardown

Someone shares the screens of a first-run flow. You give back a score, notes on
the screens that matter, a report card, and a ranked set of test ideas. Each
idea names a pattern, applies it to this flow, says how common it is in the
app's category, and cites what published tests found, with how strong that
evidence is.

The value is not generic advice ("personalise more"). It's **the pattern + the
change on this flow + the category norm + the evidence**: "Move sign-up after
the first lesson: account timing; language apps that delay sign-up are the
norm; Duolingo's A/B test saw about +20% DAU (strong)." Never collapse to
generic tips, and never invent a number.

## Input

- **Screens in order**: screenshots, frames from a recording, or a Figma frame
  sequence. The order they arrive in is the flow order unless the user says
  otherwise. If the order is unclear, state the order you assumed.
- **Or Figma frames**: a figma.com link to the frames or a section. When a
  Figma connector is available, read each frame as an image (its screenshot
  tool) in the order of the flow, and use layer text for copy. Say which
  frames you read. A design not shipped yet is scored the same way; call it
  a pre-hand-off check.
- **Or a description** of the flow. Score it the same way, award half on checks
  you can't see, and say the score is from a description.
- **Optional funnel numbers**: install → trial, trial → paid, install → paid,
  share of installs reaching the paywall, push or ATT opt-in. Compare them with
  `references/funnel-benchmarks.md`.
- **Optional traffic**: installs per day and the current install → trial (or
  install → paid) rate. With these, each test idea gets a duration.
- **Two versions of the same flow** (before and after, or theirs and a
  competitor's): use the comparison mode below.
- Useful context: the app's category, whether it has a free tier, the trial
  offered, which metric worries the team.

Reason only from what you were given. Don't assert what happens on screens you
didn't see. If the first paywall or what happens on close is missing, say so
and ask for it at the end.

If the user's flow is their own company's and they share internal numbers,
use them for this answer only.

## References

Read these before writing the teardown:

- `references/categories.md`: bucket norms. The same flow scores differently
  in a VPN app and a meditation app. Set the bucket first.
- `references/patterns.md`: the 30 patterns with when, cross-check, how,
  evidence and trap. Recommendations are lookups against this library.
- `references/scoring.md`: the 100-point rubric, including dimension 5b for
  freemium flows. The score comes from its checks, never from impression.
- `references/evidence.md`: the published tests (#1–#77) and benchmarks.
  Quote numbers exactly as written there.
- `references/ranges.md` — the range of measured lifts per pattern and metric, built only from `evidence.md`.

Read when needed:
- `references/funnel-benchmarks.md` when the user gives funnel numbers.
- `references/platform-rules.md` when a permission prompt, an account wall, a
  trial disclosure or a post-close offer is on screen.
- `examples/ai-calorie-tracker.md` for the expected format and tone.

## Process (internal — do NOT show these steps in the output)

1. **Inventory.** Number the screens. Keep the user's numbering if they gave
   one; otherwise skip logo-only splash screens. For each,
   note its job in one or two words: promise, question, interstitial,
   permission, account, proof, loader, plan reveal, first value, pre-paywall,
   paywall, second chance, home, limit. Count questions and screens before the
   paywall.

2. **Set the bucket.** Use the app's primary App Store category, mapped to the
   RevenueCat SOSA buckets in `categories.md`, plus the AI tag if it applies.
   Pick the sub-shape inside the bucket (e.g. Utilities: finance; Education:
   books). If unsure, state your read ("reading this as a meditation app — tell
   me if not") and proceed. If the flow has no onboarding paywall by design,
   switch dimension 5 to 5b.

3. **Pattern audit.** Against `patterns.md`, mark each relevant pattern as
   present and good, missing, or present but weak. Run every cross-check:
   never recommend adding something the flow already has in some form. Judge
   seam patterns (22–29) together, since their effect depends on position.

4. **Score.** Run every check in `scoring.md`: full, half or zero, nothing
   else. Apply the bucket exceptions, the compliance cap and the
   held-back rule. Then apply the consistency rule.

5. **Funnel (if numbers were given).** Compare each number with
   `funnel-benchmarks.md` by the same definition and name the step that leaks
   most. Let it lead the table when the leak is clear.

6. **Prioritise.** Rank by expected impact × evidence strength × effort.
   Pick 5–8 items (3–8 for a Strong flow, or when many points are held back;
   never pad). Label each **Fix first**
   (compliance or a broken step), **High**, **Medium** or **Low**. **High**
   needs on-target evidence from a single change: Strong, or Directional that
   isn't confounded. A test that bundled several changes caps the row at
   Medium, whatever its tier. Observed-only patterns are Medium at most and are
   labelled hypotheses. Don't add rows for things you couldn't see; ask for
   those screens instead.

7. **Durations (if traffic was given).** For each row, run
   `scripts/test_duration.py` with the installs per day, the baseline rate of
   the metric the test is judged on, and a 10% relative change. Use
   `--metric paid --trial-days N` for rows judged on paid conversion (trial
   structure, timeline, paywall echo). If the trial length is unknown, use 7
   days and say so. Use the current (or "before") version's rates as the
   baseline. Round to weeks.

8. **Render the report card** (below), then write the response.

## Report card

A single PNG: score and grade, a flow line with one dot per screen and the
paywall marked, thumbnails of the key screens with numbered pins on the spot
each test changes, the five dimension bars, and the ranked tests. People save
and share it, so make it.

1. **Pick up to 8 key screens**: every screen a row touches, plus the paywall.
   On claude.ai uploads live in `/mnt/user-data/uploads/`; in Claude Code use
   the paths the user gave. No readable files (pasted images, a description):
   render without screens, the flow line still shows.
2. **Write `teardown.json`** in a scratch folder. Shape: see
   `scripts/example.json`. `items[].n` matches the table's `#`;
   `pin.screen` is the screen number; `pin.x` / `pin.y` are fractions of that
   screenshot; `type` is `change` (an element that exists) or `add` (where a
   missing element should go). For text, pin just past the end of the line.
   Mark the value moment (`flow.value_at`) and uncaptured screens
   (`flow.unseen`). Use plain characters (~, -, x); the font has no ≈, ✓, ✗.
   Set `held_back` to the points lost only to unseen screens, and
   `previous_total` on re-runs. Put `duration` only if you computed it.
3. **Run** `python3 <skill-dir>/scripts/render_report.py --data teardown.json
   --out <output-dir>/onboarding-teardown.png`. Output dir:
   `/mnt/user-data/outputs/` on claude.ai, the working directory elsewhere.
   Needs Pillow (`pip install pillow`).
4. **Check the pins** if you can view the PNG; fix clearly wrong fractions and
   re-render once.
5. **Share the PNG** after the table. Don't describe it.

If rendering fails, skip the card silently and deliver the text. Never show
the user errors, JSON or script output.

## Output format

ALWAYS use this structure. Do NOT show the internal steps.

**Line 1 — read.** One sentence: the bucket and sub-shape, the flow's shape
(quiz funnel, try-first, account-first, freemium), and whether it's a strong
flow or one with real problems. If it's good, say so. If 10+ points are held
back by missing screens, say the grade reflects missing captures.

**Line 2 — score.** Bold total and grade, then the five dimensions (Seam or
First limit), and held-back points if 10+:

**Onboarding score: 58/100 · Leaking**
Value 12/25 · Personalisation 13/20 · Friction 11/20 · Trust 10/15 · Seam 12/20

**Line 3 — the flow in numbers.** Screens before the paywall, questions asked,
where the account and permissions sit, trial offered, against the bucket
norm. Example: "14 screens to the paywall, 9 questions (norm 10–20), account at
screen 2 (norm: after value), notifications on launch, 7-day trial with no
timeline."

For a freemium flow: screens to the product, questions, account and
permissions, then the first limit: what's metered, when the limit paywall
appears, the free path after it. Number limit screens L1, L2 after the last
onboarding screen.

**Line 4 — funnel** (only if numbers were given). Each number against its
benchmark and the leakiest step, as in `funnel-benchmarks.md`.

**Line 5 — already working.** One prose line of genuine strengths to keep.

**Screen notes.** Only the screens that matter, 3–6 bullets, each starting with
the screen number: "**Screen 4** — the weight question has no reason line; add
'this sets your daily target'." Skip screens with nothing to say.

**The table.** Highest impact first. Columns, exactly:

| # | Priority | Screen | Pattern | Test idea (applied to your flow) | Category norm | Evidence | Range seen | Duration |

- **Screen**: the screen number(s) the change touches, or "new, after 6".
- **Pattern**: the pattern name from the library.
- **Test idea**: one sentence starting with a verb, specific to this flow.
- **Category norm**: how common it is in this bucket ("Norm in language
  apps", "Rare in utilities", "Common across buckets"). You may name an app
  from the library as an example. If the library has nothing for this bucket,
  write "No norm for <bucket> in the library".
- **Evidence**: the most on-target published result for this pattern, with its
  test number and tier, e.g. "Blinkist, +23% trial sign-ups (#1, strong)".
  On-target beats strong: if the only strong test measured something else (a
  sign-up wall, not a paywall; geo, not answers), cite the on-target one and
  add the strong one with a few words on how it differs. If the library has
  only Observed evidence, write "Observed in top apps; no public test". Never
  write an expected lift for this app.
- **Range seen**: from `references/ranges.md`, the lowest to highest lift
  measured in published tests of this pattern, on the metric the row is
  judged on, with the number of tests ("+8% to +36% · 3 tests"). One test:
  its number. None: "no published range". It shows what other apps saw,
  never a forecast for this app; don't compute new ranges or mix metrics.
- **Duration**: only when traffic was given, e.g. "~3 wk (trial starts)" or
  "~4 wk (paid)". Otherwise drop the column.

If the surface can't render tables, use bullets in the same order with the
same fields.

**The report card** — the PNG, right after the table.

**Missing screens.** If you scored without the paywall, the screen after
closing it, or (for freemium apps) the limit screens, list them in one line and
ask for them.

**Your data** (one line; skip it when the user gave their numbers): the
ranking and durations get sharper on their own funnel (installs or onboarding starts per day, install → trial, trial → paid). If an
analytics or subscription connector is available in this session (Amplitude,
Mixpanel, RevenueCat, Adapty or similar), offer to pull those numbers.

**Closing line**, verbatim:
> *Published results are one app's outcome in its own test, not the lift your flow will get. Patterns and norms come from public teardowns and published case studies; run your own A/B test before shipping.*

## Comparison mode

When the user shares two versions of one flow (before/after, A/B variants, or
theirs vs a competitor's in the same bucket):

1. Score both with the same rubric, independently. Number new screens in the
   second version in its own order (don't use "11b"); map them to the first
   version in "What changed".
2. **Line 1**: which version scores higher and the one change that explains
   most of the gap.
3. **Line 2**: "**Before 58 → After 71**" and the five dimensions as deltas:
   "Value 12 → 18 (+6) · Personalisation 13 → 13 · …". If held-back points
   differ by 10 or more between the versions, add the seen-only delta (checks
   judged on visible screens in both) so missing captures don't inflate the
   gap.
4. **What changed**: 3–6 bullets, each a pattern that was added, fixed or
   broken, with the screen numbers in both versions and its evidence.
5. **New risks**: anything the new version breaks (a compliance flag, a lost
   escape hatch, a longer path to the paywall). Say "None found" if so.
6. **The table** for the better version's remaining gaps, as usual.
7. **Report card** for the better version with `previous_total` set to the
   other score.
8. Skip "Already working", "Screen notes" and "Missing screens" unless they
   add something the "What changed" list doesn't; keep the closing line.
9. **What to test first**: if the two versions differ in several patterns,
   say that a head-to-head test of the whole flow can't tell which change
   worked, and name the change to test alone first.

## Framing rules

- **Evidence, never prediction.** Quote a published result as what that app
  saw. Never say "this will lift trials by X%".
- **Keep tiers honest.** A directional or bundled result is labelled as such.
  Two tests are never merged into one number. Contested patterns (the loader)
  are presented as contested.
- **Category first.** Don't flag the category norm as a gap: an early hard
  paywall in a VPN, no onboarding paywall in dating or AI chat, 25 profile
  screens in dating.
- **Length isn't the problem.** Never recommend cutting the flow just to make it
  shorter; cutting lost in published data (#14). Recommend removing steps
  that serve nothing.
- **Benchmarks are context, not targets.** "Below the median" is a reason to
  look at that step, not a verdict.
- **Mobbin and other teardown sources.** Describe patterns in your own words.
  Don't reproduce screenshots or copy from them; link instead.
- **Compliance is a flag, not a ruling.** Point to the rule; for a full review
  suggest the paywall-store-compliance skill if it's installed.
- **Paywall detail belongs elsewhere.** Score the paywall only on the seam
  checks. For a deep paywall critique, suggest paywall-teardown if installed.

## Re-runs

If the user returns with an updated flow, score it with the same rubric and
open with the change: "58 → 71. Sign-up now follows the first lesson and the
trial has a timeline; the paywall still ignores the goal answers." Rows that
were fixed move into "Already working". Set `previous_total` on the card.

## Test planning

Onboarding tests are randomised at install, so traffic is installs per day,
not paywall views. Tests judged on paid conversion wait for trials to bill
(`--metric paid`). If the user asks what a test can detect in a fixed time,
run `scripts/test_duration.py --weeks N`. The script's simplifications (no
sequential testing, no variance reduction) are in its header; mention them if
the user is planning a real test.
