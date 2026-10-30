---
name: growth-map
description: >-
  Map which growth levers a mobile subscription app already uses across the
  whole journey (web funnel, onboarding, first paywall, upsells, first weeks
  to renewal, cancel and win-back) and which ones it doesn't use at all. For
  product designers and growth leads: a coverage map by stage, the absent
  levers worth starting with (with the range of results seen in published
  tests), and which teardown to run next. Use this WHENEVER someone asks
  "what are we not doing", "where should our growth team focus", "audit our
  growth", "what levers do we have", plans a growth roadmap or team
  structure, or describes their app and wants to know what's missing. For a
  scored review of specific screens, use the teardown for that stage.
---

# Growth map

A teardown asks "how good is this screen?". This skill asks the question
before it: **which levers does the product pull at all, and which ones has
nobody touched?** It walks the 42 levers in `references/levers.md`, stage by
stage, and marks each one present, weak, absent, not applicable or unknown.

**Scope: what a designer and a growth team change on screen.** Pricing
decisions, ad buying, CRM programmes and engineering are out of scope.

Never invent a number. The ranges you quote come from the teardowns'
`references/ranges.md` files, with their test count and tier. Arithmetic on
the user's own numbers is fine; say it's yours.

## Input

- **A description of the app**: what it does, who it's for, how people pay
  (trial or not, hard paywall or free use, web or store), the main recurring
  task if there is one.
- **Screens or flows** for any stage, if available. Screenshots, a Figma
  link (read the frames through the Figma connector when it's available) or
  a written walk-through.
- **Optional funnel numbers**: install → trial, trial → paid, first renewal,
  cancel rate, web share. They point the map at the leakiest stage.
- **Optional focus**: one stage, or "for our team structure".

If the description is thin, ask up to five quick questions in one message
(trial or not, free use or hard paywall, web funnel or not, recurring task or
not, cancel in-app or store), then map.

## References

- `references/levers.md` — 42 levers in six stages, how to tell each status,
  when each applies, and the teardown pattern that holds its evidence.
- Each teardown's `references/ranges.md` and `references/evidence.md` — the
  range of measured lifts and the tier for a lever's pattern.
- `subscription-benchmarks` — stage benchmarks when the user gives numbers.

## Process (internal — do NOT show these steps)

1. **Fit.** Set what applies: web funnel yes/no, trial yes/no, free use
   yes/no, recurring task yes/no. Levers that don't apply are N/A.
2. **Mark every lever** with one status: Present, Weak, Absent, N/A or
   Unknown. Only what was shown or described counts; anything else is
   Unknown. Never mark Absent from silence.
3. **Stage coverage.** Per stage: present / applicable levers. Unknowns are
   listed, not counted as absent.
4. **Weakest stage.** With numbers: the stage furthest below its benchmark
   (compare like for like, per the router's denominators). Without numbers:
   the stage with the largest share of absent levers. Say which rule you
   used.
5. **Pick up to 5 levers to start with**, from Absent first, then Weak:
   - rank by: weakest stage first, then the strongest evidence tier for the
     lever's pattern, then effort (copy or one screen before a new flow);
   - a lever whose pattern has a strong in-app test ranks above a hypothesis;
   - never recommend pressure (timers, guilt, hidden prices, blocked exits)
     as a lever; never add a streak to an app with no recurring task.
6. **Next teardown.** Name the one teardown that would score the weakest
   stage, and what to share with it.

## Output format

**Line 1 — read.** The app's model in a few words and the one-sentence
finding ("Strong at the paywall, nothing after the purchase").

**Line 2 — coverage.**
**Coverage** · Web 0/0 (N/A) · Onboarding 4/7 · Paywall 3/6 · Upsells 2/6 · Renewal 2/9 · Cancel 3/6 · 7 unknown

**The map**, one table per stage that applies (skip N/A stages in one line):

| Lever | Status | What we saw | Pattern |

Status as words (Present, Weak, Absent, Unknown), not symbols.

**Start here** (up to 5):

| # | Stage | Lever | What to add or change | Range seen | Evidence | Teardown |

- **Range seen**: from that teardown's `ranges.md`, e.g. "+8% to +36% ·
  3 tests". "No published range" when there is none. What other apps saw,
  never a forecast.
- **Evidence**: the strongest test behind it with its tier, or "hypothesis".

**Unknowns**: one line listing levers to check, grouped by stage.

**Next step**: the teardown to run and what screens to share.

**Your data** (one line; skip it when the user gave numbers): the map ranks
stages by missing levers; with their own funnel numbers it ranks by where
money actually leaks. If an analytics or subscription connector is available
in this session (Amplitude, Mixpanel, RevenueCat, Adapty or similar), offer
to pull install → trial, trial → paid and first renewal.

**Closing line**, verbatim:
> *A missing lever is a place to look, not a promise of growth. Ranges are what other apps saw in published tests, not a forecast for yours. Run your own A/B test before shipping.*

## Comparison mode

Two apps (yours and a competitor, or two markets): one map with two status
columns, then the levers the other has and you don't. Competitor statuses
come only from what was shown; mark the rest Unknown.

## Framing rules

- **Absent isn't bad by default.** Some levers don't fit (a utility needs no
  streak). Say why a lever applies before calling it missing.
- **Silence is Unknown.** Ask; don't assume a lever is missing.
- **Evidence, never prediction.** Quote ranges as what others saw.
- **Never reward pressure.** The map has no "urgency" or "friction" levers.
- **Hand off.** The map says where to look; the teardown says what to change.
