---
name: test-readout
description: >-
  Read a finished A/B test on a subscription app's paywall or onboarding and
  say what to do with it. Pulls each version's numbers from an analytics or
  subscription connector when one is available (Amplitude, Mixpanel,
  RevenueCat, Adapty), or takes them typed in. Checks whether the test can be
  trusted (groups split as planned, the last trials billed, refunds, a lift
  that fades), reads the decision metric with its likely range against the
  change the team planned to catch, shows where the difference came from (how
  many paid vs which plans they chose), and ends with keep, kill or iterate.
  Use this WHENEVER someone asks "did our test win", "how do I read this
  experiment", "is this result real", "B looks better, should we ship it", or
  shares test results, an experiment chart or a variant breakdown.
---

# Test readout

On decision day the eye sees "B made more money". It can't see whether that
is real or noise, whether the test itself broke, or whether B won because
more people paid or because they picked a pricier plan. This skill answers
those three, then says what to do with the idea.

**Private by default.** The team's numbers stay in this conversation. Never
write them into files you create or into examples unless the user asks.

## Input

- **From a connector** (preferred when one is available in this session).
  Find the experiment and its versions:
  - Amplitude: the experiment or flag (experiments tools), or a funnel from
    the exposure event to the payment event grouped by the variant property
    (often a user property set by the paywall tool). Payments split by plan
    or product id.
  - Mixpanel: the same funnel, broken down by the experiment property.
  - RevenueCat or Adapty: their experiment results per variant.
  Show which events, properties and dates you used and ask the user to
  confirm before reading anything: event names differ between apps.
- **Or typed in**, per version: people who entered the test, payers per plan,
  optionally trial starts, refunds and the lift week by week. Prices per plan.
- **The plan made before the test**: what decides it (revenue per person,
  paid conversion or trial starts), the smallest change worth catching, the
  split (50/50 unless said), and the decision date (last day of traffic +
  the longest trial on any plan in the test + about 3 days for stores to
  bill). Dates without a year: assume the current year and say so. If there was no plan, say
  the result is read against a 10% bar and that deciding the metric after
  seeing the data is a trap.

Count people, not views, when the test split people. Use the same window for
both versions. Revenue = each payer's first payment at list price, unless the
team gives a value per plan (e.g. weekly price × expected weeks); say which.
A shift toward weekly plans looks worse on first payments than it is.

## Process (internal — do NOT show these steps)

1. Write the numbers to a JSON file in the working directory (format:
   `scripts/example.json`) and run
   `python3 <skill-dir>/scripts/readout.py <file>` (add `--json` to parse).
2. **Trust first.** Groups not split as planned (p < 0.001) → the test is
   broken: say so and stop reading the result. Decision date not reached and
   the metric is paid → too early: say how many days are left.
3. **The result**: B vs A with the 95% range, next to the plan's smallest
   change. Range above 0 → win; below 0 → loss; crosses 0 → can't tell.
4. **Where it came from**: conversion change vs revenue-per-payer change and
   the plan mix. Name the screen part that most likely drove it (plan
   selection, trial copy, price display) only as a lead, not a finding.
5. **Guardrails**: refunds up beyond chance (one-sided z > 2.58), or a lift
   that shrinks every week → a win with a cost. No weekly numbers → say the
   fading check wasn't run.
6. **What to do** (one of):
   - Win: ship B, make it the new control, plan on the low end of the range.
   - Win with a cost: don't ship as is; fix the cause, retest as B2.
   - Loss: keep A; say what the loss teaches.
   - Can't tell: keep A. The test only sees changes at least as big as the
     planned bar; "no difference" isn't proof of no effect. Kill the idea,
     or iterate with a bolder version (suggest the matching teardown).
   - Broken: don't read the numbers. Say the test setup counted people
     unevenly and ask whoever set up the experiment to find where one group
     loses people; then rerun with the same plan. No engineering detail.
   - Too early: wait until the decision date; say how many days.

## Output format

Reply in the user's language. Short; the answer first.

**Line 1 — the answer**, e.g. "B wins: +13% money per person, most likely
between +5% and +21%." or "Can't tell: B looks 6% better, but the range runs
from −2% to +13%." Broken: "Don't read this test: the groups didn't split as
planned." Too early: "Too early: the last trials bill on <date>." For broken
and too early, never state the lift or the range, and skip "Where it came
from"."

**Trust:** one line of marks: "Split as planned ✓ · Last trials billed ✓ ·
Refunds held ✓ · Lift held ✓". Expand only the failed ones, one sentence each.

**Where it came from:** one or two sentences with the conversion change, the
revenue-per-payer change and the plan mix.

**What to do:** one paragraph.

**Numbers used:** a small table per version (people, payers per plan, revenue)
and the events or source they came from.

**Closing line** (win, loss or can't tell only), verbatim:
> *A result describes this test, in this app, in these weeks. Wins usually shrink after launch; plan on the low end.*

## Framing rules

- **Never call a winner from the point estimate.** The range decides.
- **One metric decides**, the one picked before the test. Others are
  guardrails or leads.
- **Slices are leads.** A win in one country or platform alone is a reason
  for a new test, not a result.
- **No stopping early for a win.** Stop early only for harm.
- **Design scope.** The recommendation is about the screens tested; pricing
  and billing setup are out of scope.

## References

- `scripts/readout.py` — the checks and the math (method and sources in its
  header).
- `scripts/example.json` — the input format (illustrative numbers).
