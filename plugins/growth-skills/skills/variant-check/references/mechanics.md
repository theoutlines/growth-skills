# Paywall mechanics: ranges and what the winning versions had

One section per mechanic a paywall variant can change. Each gives:

- **Spot it**: what you see on screen when B uses this mechanic and A doesn't
  (or B does it differently).
- **Fits when**: when the mechanic makes sense for a paywall. Use it before
  suggesting a mechanic B doesn't use.
- **Range seen**: lifts from published tests, per metric and denominator,
  never merged. The **call** line says which range decides detectability.
- **What the winners had**: traits of the versions that won, each tagged with
  its source. **Key** traits are the ones a test stands behind; the rest are
  observed suggestions.
- **Where it flips**: where the same mechanic lost, or a screen rule it can
  break.

## Sources

- **Adapty library**: Adapty's A/B test library as summarised in the
  `paywall-ab-test-assistant` skill (`references/evidence-library.md`). Each
  band pools many tests.
- **#N**: a published test, same numbering as the onboarding-teardown
  evidence library. The link is given in the line.
- **Prior**: Adapty's expected effect for a type of change (paywall-teardown
  impact tiers). Not a measured lift; use only when nothing measured exists,
  and say "prior".
- **Observed**: what top apps' paywalls do (paywall-teardown pattern
  library). No test behind it.

## Tiers (print only these)

- **strong**: controlled test with numbers. Adapty bands labelled Strong or
  Solid map here.
- **directional**: numbers without method, bundled or confounded. Adapty
  bands labelled Mixed or Thin map here.
- **prior**: an expected effect, not a measurement.
- **observed**: seen in top apps, no public test.

## Metrics and denominators (keep apart)

- **Revenue per user**: say the denominator: per paywall view, per install,
  per 100 installs, per user in the test (ARPU). Two revenue numbers with
  different denominators are two metrics.
- **Paid conversion**: view → purchase or subscription.
- **Trial starts**, **trial-to-paid**.

## Rules for the call

- The **call range** is the one on the test's metric. If the mechanic has
  only ranges on other metrics, there is no call: write "no call (measured on
  <metric>)". A mechanic with no call never decides the verdict on its own.
- **One test = one number.** The call compares that number with the bar:
  number ≥ bar → likely visible (one test); below → unlikely.
- **Outliers stay out.** Ranges marked *outlier* are listed for context and
  never used for the call.
- **Markets and platforms split**: if the range splits by market or platform
  and the test mixes them, the call uses the market with most of the
  traffic; if unknown, the lowest figure. Suggest reading markets apart.

---

## 1. Trial explained next to the price (timeline)

**Spot it:** a step-by-step "how your trial works": today (full access, no
charge), a reminder before the end, the day of the first charge.
**Fits when:** at least one plan has a free trial.

**Range seen**
- Revenue per user +12% to +36%: Adapty library band, strong.
- Trial starts +23% (one test), complaints −55%, in-trial cancels −4%: #1
  Blinkist, strong; timeline + reminder opt-in as one change.
  https://uxplanet.org/how-solving-our-biggest-customer-complaint-at-blinkist-led-to-a-23-increase-in-conversion-b60ad514134b
**Call:** revenue per user → Adapty band; trial starts → #1.

**What the winners had**
- **Key** Three steps with named days: today, reminder on day N, charge on
  day N+1 or a date. (#1)
- **Key** The reminder step is shown as a promise on screen ("We'll remind
  you on day 5"). Designer's part ends at the promise; flag to the team that
  the app must send it, without designing the push. (#1)
- The price after the trial inside the last step and next to the button.
  (observed)
- On the paywall or the step right before it. (Adapty library)

**Where it flips:** earlier in onboarding it adds drop-off before the paywall
(Adapty library). A timeline that hides the price (vague steps, price moved
away) reads as a hidden charge: screen flag.

## 2. Annual as the hero (plan steering)

**Spot it:** annual preselected, shown first or largest, a savings badge or a
per-month equivalent; other plans muted or behind "View all plans".
**Fits when:** there is an annual plan and at least one shorter plan.

**Range seen**
- Revenue per user (per user in test) +25% to +40%: Adapty library band,
  strong (annual-forward layouts and toggle selectors; the band includes
  "trial on annual", see Bundles).
- Annual share +15 to +20 percentage points, cancellations slightly up: #42
  Mojo, strong (only yearly shown, monthly behind "View all plans").
  https://www.revenuecat.com/blog/growth/mojo-60-percent-arpu-growth-five-months/
- Revenue per paywall impression: US +8%, Mexico +26%, Brazil +45%: #43 Mojo,
  strong (annual price shown as a monthly equivalent). Same link.
- Click-through +13.5%: #64 Unacademy, strong (monthly price highlighted
  instead of the full course price; web).
  https://abtest.design/tests/highlighting-monthly-pricing
**Call:** revenue per user → Adapty band (per user). #43 is per impression
and splits by market: use it only when the change is just the per-month
display, with the market rule.

**What the winners had**
- **Key** Annual preselected and dominant: filled card, first position.
  (Adapty library)
- **Key** The annual price also shown per month or week, so it compares with
  the short plan at a glance, with the billed yearly amount still the most
  prominent price. (#43; store rule below)
- **Key** Short plans still reachable ("View all plans"), not removed. (#42)
- A saving named against a plan the user can see ("Save 50% vs monthly").
  Anchoring to a hidden or rarely bought plan inflates the number and costs
  trust. (observed; paywall-teardown playbooks)

**Where it flips:** cutting the plan count (four down to two) lost revenue in
the double digits (Adapty library). Conversion can drop while revenue rises:
judge by revenue per user. **Store rule:** the billed amount must be the most
prominent price; a per-month figure bigger than the yearly total is a
rejection risk on Apple and a listed violation on Google (paywall-store-
compliance, A1).

## 3. Trial on the annual plan only

**Spot it:** the trial appears only when annual is selected; short plans
start paid. A already had a trial on more plans, or none.
**Fits when:** an annual plan and a shorter plan; deciding which plans get a
trial is the team's offer decision, the check covers how it reads.

**Range seen**
- Paid conversion +15% to +30%: Adapty library band, strong.
- Paywall view → subscription +39%, revenue per 100 installs +47%, ARPPU +5%:
  #41 Moonly, strong (trial added to the annual plan only).
  https://adapty.io/case-studies/moonly/
**Call:** paid conversion → Adapty band; revenue per 100 installs → #41
(one test).

**What the winners had**
- **Key** The trial named on the annual option itself (badge or line). (#41)
- The button text follows the selected plan ("Start free trial" on annual,
  "Continue" on others). (observed)

**Where it flips:** results split by platform (Adapty library); read iOS and
Android apart.

## 4. Social proof at the decision point

**Spot it:** a rating with a count, short reviews or a user count near the
plans or the button.
**Fits when:** always; strongest in trust-heavy categories (health, finance,
kids).

**Range seen**
- Paid conversion +10% to +30%: Adapty library band, strong.
- Paid subscriptions +44% (one test): #60 Runtastic, directional (a promo
  statement replaced with a real 5-star user review).
  https://abtest.design/tests/user-reviews-on-paywall
**Call:** paid conversion → Adapty band. Revenue per user: no call.

**What the winners had**
- **Key** A real review with a name and stars, instead of a claim the app
  makes about itself. (#60)
- A specific number ("4.8 from 200K+ ratings"), near the button or plans.
  (observed)

**Where it flips:** a redesign adding a comparison table and testimonials
together lost (Adapty library). Test proof on its own.

## 5. Free vs paid comparison as the paywall

**Spot it:** a table of what free gets and what paid adds, on the paywall.
**Fits when:** the app has a real free tier to compare with.

**Range seen**
- Revenue per user about +15% as an in-app paywall (iOS up, Android flat):
  Adapty library band, strong. Larger onboarding-paywall figures exist but are
  directional (small samples): *outlier*.
**Call:** revenue per user → +15% (treat as one number).

**What the winners had**
- **Key** On the paywall itself, not as a teaser screen before it. (Adapty
  library)
- 3 to 5 rows of decision-relevant differences, above the plans. (observed)

**Where it flips:** a bare comparison step before the paywall lost on revenue
and conversion; one "win" was a randomisation bug (Adapty library).

## 6. Prices shown up front

**Spot it:** A pitches benefits and asks to continue; B shows plans and
prices on the same screen.
**Fits when:** A hides prices behind a tap.

**Range seen**
- Trial conversion +15%, paid conversion +3%, ARPU +17%, MRR +33% (one test):
  #50 VEED, directional.
  https://abtest.design/tests/showing-pricing-options-upfront
**Call:** the matching single number from #50.

**What the winners had**
- **Key** Yearly and monthly prices visible without a tap. (#50)

**Where it flips:** none published. Mechanic 7 also won with price on a later
step: what matters is that the price step is clear.

## 7. Value first, price on the next step (multi-step paywall)

**Spot it:** the paywall becomes two or three screens: benefits, then the
trial or reminder, then plans and price.
**Fits when:** A crams value and price into one screen.

**Range seen**
- Conversion +27%, proceeds +36% (one test): #55 Speak4Me, strong.
  https://superwall.com/case-studies/speak4me
- Conversion +16% (one test; metric may be annual trials): #56 Stompers,
  strong. https://superwall.com/case-studies/stompers
- Paywall view → trial or purchase 12.41% vs 9.07%: Superwall aggregate,
  observational, not randomised: *outlier*.
**Call:** paid conversion → +16% to +27% (two tests).

**What the winners had**
- **Key** Benefits first, then the trial reminder, then the price. (#56)
- **Key** Features before price. (#55)

**Where it flips:** an extra step loses people if it repeats what onboarding
just said (observed, onboarding-teardown pattern 23).

## 8. The button

**Spot it:** the CTA wording, contrast or width changes.
**Fits when:** always.

**Range seen**
- Trial starts and purchase conversion +15% to +30%: Adapty library band,
  directional (one-off test).
- Trial starts +104% month over month: #67 Going, directional; web: *outlier*.
  https://abtest.design/tests/trial-for-free-cta
**Call:** paid conversion or trial starts → Adapty band. Revenue per user:
no call.

**What the winners had**
- **Key** Says what happens and that it's free now ("Try for free", "Start my
  free week"). (#67; Adapty library)
- Highest-contrast element on screen, full width. (observed)

**Where it flips:** none published; easy to over-read one win. When the
button changes because the offer changed (a new trial), it's part of that
mechanic, not a separate one.

## 9. Delayed close button

**Spot it:** the ✕ appears after a few seconds instead of at once.
**Fits when:** A shows the ✕ at once.

**Range seen**
- Paid conversion +8% to +15%: Adapty library band, strong.
**Call:** paid conversion → Adapty band.

**What the winners had**
- **Key** A short delay, then a normal ✕. (Adapty library)

**Where it flips:** an "Are you sure?" popup on close lost (Adapty library).
A missing ✕ is a store and trust problem, never a strength.

## 10. Visuals and motion

**Spot it:** a new hero image, animation or product video.
**Fits when:** always; strongest for apps with a visual result.

**Range seen**
- Paid conversion +13% to +27%, revenue per user +16% to +34%: Adapty library
  band, strong (strongest on intro and onboarding screens).
- Conversion +13% (one test): #68 Neos Kosmos, directional (news, web).
  https://abtest.design/tests/paywall-visuals
**Call:** the Adapty band on the test's metric.

**What the winners had**
- **Key** The visual shows the product or the result, not decoration.
  (Adapty library: "supports the offer")

**Where it flips:** load time on slow devices; decoration that pushes plans
below the fold.

## 11. Price level

**Spot it:** the same layout with different prices.
**Fits when:** never suggested by this check: price is the team's decision.

**Range seen**
- Revenue per user +15% to +25% in top-paying markets: Adapty library band,
  directional (geo split).
- Conversion −5% after a +30% price (one test): #59 travel app, strong.
  https://adapty.io/case-studies/travel-app/
**Call:** revenue per user → Adapty band, top markets only.

**What the winners had:** rises limited to top-paying markets. The
designer's part is how the price reads (mechanics 2, 13).

**Where it flips:** the same rise lost badly outside top markets.

## 12. Headline and copy only

**Spot it:** new headline, bullets or captions; layout and plans unchanged.
**Fits when:** always, but rarely enough alone.

**Range seen**
- Paid conversion +3% to +8%, revenue per user +1% to +3%: prior
  (copy-only changes).
- Only 34.6% of visual or text-only tests lifted LTV (31.4% lifted
  conversion), against about 57–62% for structural tests: Adapty State of
  In-App Subscriptions 2026, 105,000 paywalls (win rates, not lift sizes).
- Conversion +54% or more: #58, directional, conference talk, no method:
  *outlier*. https://growthgems.substack.com/p/growth-gems-127-onboarding-activation
- Conversion +16%: #69 Neos Kosmos, directional (emotional appeal vs
  benefits list, news, web): *outlier* (another category and platform).
**Call:** the prior on the test's metric.

**What the winners had**
- Outcomes instead of features, in the user's words. (#58; #2 Five Minute
  Journal, onboarding)
- Headline wins often come from a plan-mix shift: check what moved (Adapty
  library).

**Where it flips:** claims the app can't back ("in under 15 minutes") are a
trust and review risk: screen flag. Copy-only variants usually land below
what a normal test can see.

## 13. A trial where there was none

**Spot it:** A starts paid; B adds a free trial to one or more plans.
**Fits when:** the team is open to a trial; it's their offer decision, the
check covers how it reads.

**Range seen**
- Subscription conversion 1.63% (weekly) → 2.29% (weekly + trial), about
  +40% computed (one test): "the pdf scanner", directional.
  https://abtest.design/tests/monthly-vs-weekly-vs-free-trial
- Trial tests lifted LTV in 59.6% of tests (conversion 39.9%): Adapty State
  of In-App Subscriptions 2026 (win rate, not a lift size).
**Call:** paid conversion → +40% (one test, directional).

**What the winners had**
- **Key** The trial and what follows it stated next to the button ("3 days
  free, then $49.99/year"). (observed; store rule)

**Where it flips:** removing a trial won where trial-to-paid was very low,
and the same change lost on another platform (Adapty library).

---

## Bundles

When B changes several mechanics at once:
- Detectability: the variant is as visible as its strongest called
  mechanic, never the sum.
- Attribution: a win can't be credited to one mechanic. Say so and name the
  one to isolate next.
- Overlap: mechanic 2's Adapty band already includes trial-on-annual
  layouts; with 2 + 3 together, cite the band once.
- Conflicts: comparison table + testimonials together lost (mechanic 4).

## Screen flags (any variant; not legal advice)

- The ✕ or "Not now" exists.
- The billed amount is the most prominent price; per-month or per-week
  breakdowns and "save X%" are smaller (paywall-store-compliance A1).
- Trial terms and the price after the trial sit next to the button at
  normal contrast, not in grey small print or below the fold.
- No claim the app can't support; no countdown without a real offer.
- A change that makes these worse (price moved away, ✕ hidden) is a fix
  with priority over everything else.

## Checks

- Mechanics: 13. Calls rest on an Adapty band: 1, 2, 3, 4, 5, 8, 9, 10, 11;
  on single tests only: 6, 7, 13; on a prior: 12.
- Every "What the winners had" line carries its source; key traits have a
  test behind them.
- Rebuild when the Adapty library summary or the onboarding evidence changes.
