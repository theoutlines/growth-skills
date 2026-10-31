---
name: variant-check
description: >-
  Check a paywall test variant before it gets live traffic. Takes version A
  (control) and version B (and C) as Figma frames, screenshots or a
  description, plus the test plan (what decides it and the smallest change
  the test can see, e.g. from planner.theoutlines.xyz). Says which paywall
  mechanics B changes, whether published tests of those mechanics moved
  numbers enough for this test to see it, what the winning versions had that
  B lacks, and writes a short clarity pretest (Lyssna, Maze) to run first.
  Use this WHENEVER someone shares a paywall variant before launch and asks
  "is this bold enough", "will the test show anything", "check my variant",
  "what's missing before we test this", or compares a new paywall design
  with the current one. For a teardown of one paywall prefer
  paywall-teardown; for reading a finished test prefer test-readout.
---

# Variant check

Most paywall tests end "can't tell": the variant changed too little for the
traffic, or it used a strong mechanic weakly. Both are visible before launch.
This skill looks at A and B the way a growth design lead would before
signing off: is B bold enough for this test, and does it have what the
versions that won in published tests had.

For product designers: what changes on the screen is checked and suggested.
Plans, trials and prices are the team's offer decisions: the check says
whether the test can see them and how they read, never which price to set.
No billing setup, push programmes or engineering.

**It never forecasts a lift.** It compares B with ranges other apps saw and
with what their winning versions had. Say this once, plainly.

## Input

- **Versions**: A (control) and B, optionally C. Figma frames (use the Figma
  connector to get screenshots of the frames when a link is given),
  screenshots, or a description. If only B is given, ask for A: the check is
  about the difference.
- **The plan** (ask once if missing, then use defaults and say so):
  - what decides the test: revenue per user (default for a paywall; read it
    as money per paywall view, i.e. per user in the test, unless the plan
    says per install), paid conversion, or trial starts;
  - the smallest change the test can see ("your test catches +X% and up").
    From the planner (planner.theoutlines.xyz) or their own calculator. If
    unknown, use 10% and say so;
  - the goal: find a win (default) or prove B isn't worse. For "not worse",
    skip part 1 (detectability) and say why.
- Platform and main markets, if known (several mechanics split by platform
  or market).

## Process (internal — do NOT show these steps)

1. Read `references/mechanics.md`. Describe A and B in a few words each
   (what is on screen, top to bottom). Describe, never copy text from
   screenshots at length.
2. List what B changes vs A, element by element. Map each change to a
   mechanic (1–13). A change that fits no mechanic: name it, say there's no
   published range, and check it against the screen flags (a change that
   makes the screen less clear is a fix, not a neutral change).
3. **Part 2 first, execution.** For each mechanic B uses, go through "What
   the winners had" and mark each trait: has it / partly / missing / can't
   tell from the screen. Keep the source tag. Key traits (a test behind
   them) come first; observed traits are suggestions, not requirements.
4. **Part 1, can the test see it.** Follow "Rules for the call" in
   `references/mechanics.md` (call range on the test's metric and
   denominator; one test = one number; outliers out; market rule). Compare
   with the bar the test can see:
   - low end ≥ bar → "likely visible";
   - high end ≥ bar > low end → "maybe: only if B lands near the top";
   - high end < bar → "unlikely to show". Copy-only variants land here
     almost always.
   - no range on the test's metric → "no call (measured on <metric>)".
   **Execution caps the call:** if B misses a key trait, or has it only
   partly, lower the call one step ("likely" → "maybe", "maybe" →
   "unlikely") and say "as built"; give the uncapped call as "if built like
   the winners". A capped single-test call ("likely") becomes "maybe". A
   mechanic with no key traits is never capped, so both cells match.
   "Can't tell" doesn't cap: ask about it instead. The ranges describe
   versions that had the key traits.
   The variant as a whole is as visible as its strongest called mechanic,
   never the sum. Bundled mechanics: say attribution will be unclear and
   name the one to isolate next.
5. Check "Where it flips" for each mechanic against B's placement, platform
   and markets. Flag clashes (e.g. comparison + testimonials added together).
6. Screen flags from `references/mechanics.md` (not legal advice): ✕
   present; billed amount the most prominent price; trial terms and the
   price after the trial next to the button at normal contrast; no claim the
   app can't back; a savings badge whose arithmetic is right and whose
   anchor plan is visible. When a description leaves one out (often the ✕),
   ask once rather than guess; until it's answered the verdict can't be
   "ready to test". A flag A also has: say "fix in both A and B
   before launch", so the fix doesn't become a second change in B. For a
   full store check, point to paywall-store-compliance.
   If the test decides on trial starts, add under Watch for: a variant can
   win trial starts by making the price harder to see; keep trial-to-paid
   and refunds in view.
7. **Part 3, pretest.** From `references/pretest.md`: the four standard
   questions plus one per mechanic B uses, with what counts as a pass.
8. Decide: **ready to test**, **ready after fixes** (list them, screen
   flags first, then missing key traits, at most five), or **rethink** (B
   can't be seen by this test even if built like the winners: suggest one
   stronger mechanic whose "Fits when" matches this paywall, so a win stays
   attributable. Pick by, in order: its call on this test's metric, a
   screen-only change over an offer change (offer changes: the team
   decides), and whether it also fixes a flag A has. Name one alternative.
   Screen flags still go under "Fix before launch").

## Output format

Answer in the user's language. Short, scannable, no step numbers.

```
**Variant check: <one-line verdict: ready / ready after fixes / rethink>**
A: <a few words> → B: <a few words>
<one sentence: what B changes and whether this test can see it as built>

**What B changes**
| Change | Mechanic | Range seen (metric, tier, source) | This test (bar +X%) |
|---|---|---|---|
| ... | ... | ... | as built: likely / maybe / unlikely / no call · if built like the winners: ... |

**What the winning versions had**
- <Mechanic>: ✓ <trait> · ✗ <trait> (source) · ~ <trait> (observed)
...

**Fix before launch**   (only if any; also under "rethink", with the
suggested stronger mechanic as the first line)
1. <the change, on screen, in one line> — why (source)
...

**Watch for**   (sign flips, platform or market splits, bundling)

**Pretest before live traffic** (Lyssna / Maze, before launch)
- Q: ... → pass: ...
...

Ranges are what other apps saw in published tests, not a forecast for yours.
```

Close with one line: re-run the plan on planner.theoutlines.xyz if the fixes
change what decides the test, and offer to check the fixed version.

## Rules

- Never invent a number. Every range keeps its source and tier; traits keep
  their tag. Never merge ranges, never add mechanics together.
- On-target beats strong: a range on the test's own metric matters more than
  a stronger test on another metric. Say when the metric differs.
- Never reward pressure or friction: no fake timers, no hidden ✕, no
  confirm-shaming. If B adds one, it's a fix, not a strength.
- Don't recommend what A or B already has (cross-check before suggesting).
- If the screens are unreadable or cut off, say what you can't see and mark
  those traits "can't tell", rather than guessing.
- Mobbin or other gallery screens: describe in your own words, never copy.
- Private by default: the team's screens and numbers stay in this
  conversation.
