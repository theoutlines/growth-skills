---
name: web2app-teardown
description: >-
  Tear down the screens of a mobile subscription app's web funnel: the ad
  landing, web quiz, plan screen, web paywall, checkout screen,
  post-purchase upsells and the hand-off into the app, plus the in-app "buy
  on the web" screen. For product designers: a 100-point score for what can
  be changed on screen (never rewarding pressure), a report card and ranked
  screen tests grounded in published tests and public benchmarks, each
  labelled by evidence strength. Use this WHENEVER someone shares web funnel, quiz,
  web paywall, checkout, upsell or link-out screens, asks how to design a
  web2app funnel or web checkout, or compares two web funnels. For the
  in-app onboarding prefer onboarding-teardown; for in-app paywalls prefer
  paywall-teardown.
---

# Web2app Teardown

A web funnel sells the subscription before the app is installed, so its
screens carry what the store usually shows for you: the price and renewal
terms, the consent, the payment buttons, the errors and the way into the app.
This skill reviews those screens and ranks what to change and test.

**Scope: the designer's surfaces.** Only what a designer changes on a screen
is scored or put in the table. Fees, payment setup, emails, the cancel path,
store settings and legal review are out of scope: don't mention them.

Never invent a number. Every figure you quote comes from the references
(`evidence.md` test #W1–#W63 or benchmark row, `categories.md`,
`platform-rules.md`, or counts in `flows.md` and `walkthroughs.md`), with its
strength. Arithmetic on the user's own prices is fine; say it's yours.

**The evidence is thinner than the vendor headlines.** Only one strong test
is a subscription app's web checkout or link-out (#W39 Dipsea); the other
strong rows are web UX tests from non-app businesses, Stripe payment-method
holdbacks and Android sign-in tests. Most web2app numbers come from vendors
who sell web checkout (FunnelFox, Paddle, Stripe) or argue against it
(RevenueCat). Say so when it matters.

## Input

- **Screens in order**: landing, quiz, plan screen, email screen, paywall,
  checkout, upsells, confirmation, the "get the app" screen, the first app
  screen. For a link-out: the in-app paywall with the web option and the
  return to the app.
- **Or Figma frames**: a figma.com link to the frames or a section. When a
  Figma connector is available, read each frame as an image (its screenshot
  tool) in the order of the flow, and use layer text for copy. Say which
  frames you read. A design not shipped yet is scored the same way; call it
  a pre-hand-off check.
- **Or a description**; say the score is from a description.
- **Mode**: web funnel or link-out. Infer it if not given.
- **Markets** (US, EU countries, UK, others).
- **Optional numbers**: sessions per day and step rates (session → screen 2 →
  paywall → purchase) for test durations.
- **Two versions**: comparison mode below.

Reason only from what you were given. If the checkout or the hand-off is
missing, score what you have and ask.

## References

- `references/scoring.md` — the rubric, modes, blockers, priority, held back.
- `references/patterns.md` — 22 screen patterns with evidence and traps,
  plus the sign-flip table.
- `references/evidence.md` — tests #W1–#W63, benchmarks, metric definitions, gaps.
- `references/ranges.md` — the range of measured lifts per pattern and metric, built only from `evidence.md`.
- `references/categories.md` — the market table (which payment buttons lead,
  button wording, consent) and what each bucket does on the web.
- `references/platform-rules.md` — rules behind the flags, and a checklist.
- `references/flows.md` — web funnels, checkouts and link-outs from public
  Mobbin captures, in our own words with links.
- `references/walkthroughs.md` — paid-social quiz funnels walked on a phone
  viewport (observed).

## Process (internal — do NOT show these steps)

1. **Inventory.** Number the screens in funnel order (keep the user's
   numbering). Set the mode, markets and bucket (RevenueCat SOSA buckets;
   "AI app" is a tag). Mark the plan screen, the paywall, the checkout and the
   hand-off.
2. **Score** with `scoring.md`: mode, market, unseen-screen and description
   rules, blockers.
3. **Sign-flip sweep.** Check each tactic against "Where it flips" in
   `patterns.md`.
4. **Flag sweep.** Check the screens against the checklist in
   `platform-rules.md`; only screen elements become flags in the response.
5. **Market and category fit.** Use the market table in `categories.md`
   first, then the bucket.
6. **Pick rows.** Up to 8 screen changes, never pad (fewer when the funnel has few gaps). Priority:
   - **Fix first**: as defined in `scoring.md`.
   - **High**: a strong test on the same kind of screen change (#W19/#W20
     Apple Pay placement, #W9 quiz pacing, #W39 web option beside IAP).
   - **Medium**: directional evidence, a benchmark, a strong test that's
     off-target (e-commerce, surveys), or a ⚠️ checklist item. Hypotheses
     with no public test are Medium at most and say "hypothesis".
   - **Low**: anecdotal or observed only.
   Order: Fix first → rows for the weakest dimension → the rest by priority,
   then evidence strength × effort. Never recommend timers, hidden prices,
   pre-selection or more screens.
7. **Durations** (only with traffic). Run `scripts/test_duration.py`:
   funnel tests are randomised per session (sessions per day as `--installs`,
   session → purchase as `--baseline`; FunnelFox's 3% (mean vs median not stated) if unknown, and
   say so); checkout-screen tests can use checkout starts and checkout →
   payment. Default to a 10% relative change. If a test runs past 8 weeks,
   say so and give the change detectable in 4 weeks (`--weeks 4`).
8. **Render the card**, then write the response.

## Output format

**Line 1 — read.** Mode, markets, bucket and the single biggest screen issue
in one sentence. If it's a strong funnel, say so.

**Line 2 — score.**
**66/100 — Leaking** · Landing & quiz 18/25 · Paywall 14/25 · Checkout 17/25 · After payment 17/25
(Link-out: "Link-out score: 72/100 — Solid (Link-out screen … · Paywall … ·
Checkout … · After payment …)". Add "· 12 held back" when held-back points
reach 10. Blocker: "49/100 (cap)".)

**Line 3 — the funnel in numbers.** Screens to the paywall, where email is
asked, loaders, the price shown largest vs the charge, payment buttons order,
how the buyer gets into the app. Example: "34 screens to the paywall, email at
22, 4 loaders; '$0.43/day' larger than the $38.99 3-month charge; card form
above Apple Pay; the thank-you page has no app link."

**Line 4 — numbers** (only if given): each against its benchmark row.

**Line 5 — already working.** One prose line.

**Sign flips** (only if any): one bullet per tactic on its losing side.

**Screen flags** (only if any): one bullet each with the screen, the rule and
the market. End with: "Flags, not legal advice."

**The table**, in the order from step 6:

| # | Priority | Screen | Pattern | Change to test | Evidence | Range seen | Duration |

- **Change to test**: the concrete screen change, with copy direction.
- **Evidence**: the most on-target test or benchmark with its number and
  tier; "hypothesis" where none exists. Never an expected lift for this
  funnel.
- **Range seen**: from `references/ranges.md`, the lowest to highest lift
  measured in published tests of this pattern, on the metric the row is
  judged on, with the number of tests ("+8% to +36% · 3 tests"). One test:
  its number. None: "no published range". It shows what other apps saw,
  never a forecast for this app; don't compute new ranges or mix metrics.
- **Duration**: only with traffic; otherwise drop the column.

**The report card** right after the table.

**Not captured**: one line on missing screens.

**Your data** (one line; skip it when the user gave their numbers): the
ranking and durations get sharper on their own funnel (sessions per day, session → paywall, paywall → purchase). If an
analytics or subscription connector is available in this session (Amplitude,
Mixpanel, RevenueCat, Adapty or similar), offer to pull those numbers.

**Closing line**, verbatim:
> *Published results are one company's outcome in its own setting, not the change your funnel will get. Most web2app numbers come from vendors, and flags are not legal advice. Run your own A/B test before shipping.*

## Report card

1. Pick up to 8 key screens: landing, plan screen, email screen, paywall,
   checkout, first upsell, hand-off, and any screen a row touches.
2. Write `web2app.json` (see `scripts/example.json`). In `flow`: `screens`,
   `paywall_at` with `"marker_label": "paywall"`, `value_at` = the plan
   screen with `"value_label": "plan"`, `unseen`, and after-payment screens as
   `extra` (A1, A2) with `"extra_label": "after"`. Dimension keys: `landing`
   (or `linkout`), `paywall`, `checkout`, `after`. Use plain characters (~,
   -, x); the font has no ≈, ✓ or ✗.
3. Run `python3 <skill-dir>/scripts/render_report.py --data web2app.json
   --out <output-dir>/web2app-teardown.png` (Pillow). Output dir:
   `/mnt/user-data/outputs/` on claude.ai, the working directory elsewhere.
4. Share the PNG after the table. If rendering fails, skip it silently.

## Comparison mode

Two versions: score both, map screens in "What changed". If held-back points
differ by 10+, compare on checks seen in both. Show before → after per
dimension, what changed with evidence, new risks (timers, hidden terms,
pre-selection), then the remaining table for the better version. If several
things changed, name the one change to test alone first.

## Framing rules

- **Screens only.** If it can't be changed in a design file, leave it out.
- **Never reward pressure.** Timers, per-day prices louder than the charge
  and pre-checked add-ons raise short-term conversion and cost refunds and
  trust (FTC v. Genesis Tech allegations; Cal AI; ACM v. Epic; CMA v. Emma).
- **Evidence, never prediction.** Quote what a company saw; never "this will
  lift X%".
- **Market first** for payment buttons and button wording.
- **Vendor data is vendor data.** Name the source.
- **Mobbin and other sources.** Describe in your own words and link; don't
  copy. Example teardowns don't name the app.
