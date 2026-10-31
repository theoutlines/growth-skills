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
  evidence library. The link is given in the line. **U#** is a row of the
  upsell-teardown library.
- **Losses and nulls** without a figure are listed so the file shows what
  didn't work. They never enter a range or make a call.
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

- **Revenue per user**: say the denominator. In a paywall test people are
  split when they see the paywall, so "per user in the test" (Adapty's ARPU)
  and "per paywall view / impression" both match the planner's "money per
  paywall view". Per install or per 100 installs is a different metric unless
  the test split people at install. Adapty bands are per user in the test.
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
- **Bands before single tests**: when a mechanic has an Adapty band on the
  test's metric, the band makes the call; single tests on the same metric
  are context. A single test makes the call only when it is the only range
  on the metric, or when B changes exactly what that test changed.
- **Markets and platforms split** (single tests): if the figure splits by
  market or platform and the test mixes them, use the market with most of
  the traffic; if unknown, the lowest figure. Suggest reading markets apart.
- **Print the call range** in the table; other-metric ranges go in one short
  "also seen" line; outliers are left out of the report.

---

## 1. Trial explained next to the price (timeline)

**Spot it:** a step-by-step "how your trial works": today (full access, no
charge), a reminder before the end, the day of the first charge.
**Fits when:** at least one plan has a free trial.

**Range seen**
- Revenue per user +12% to +36%: Adapty library band, strong.
- Trial starts +23% (one test), complaints −55%, in-trial cancels −4%: #1
  Blinkist, directional (timeline + reminder opt-in as one change, so
  bundled).
  https://uxplanet.org/how-solving-our-biggest-customer-complaint-at-blinkist-led-to-a-23-increase-in-conversion-b60ad514134b
- LTV +50% (one test): #78 Pepper, directional (two-step paywall with the
  trial as a timeline; staged rollout, no concurrent control).
  https://superwall.com/case-studies/pepper
- Trial starts +13.6%, trial-to-paid "not impacted" (no figure) (one test):
  #97 Stardust, strong (the paywall redesigned as a trial timeline).
  https://superwall.com/blog/how-stardust-increased-ios-app-revenue-by-4x-in-six-weeks
- Revenue +27% vs control, denominator not stated (one test): #116
  Pregnancy+, strong (timeline added: today, day 3, charge day).
  https://adapty.io/case-studies/pregnancy-plus/
**Call:** revenue per user → Adapty band (#116 sits inside it but doesn't
state its denominator: context); trial starts → +13.6% to +23% (two tests,
#97 and #1; #1 is bundled).

**What the winners had**
- **Key** Three steps with named days: today, reminder on day N, charge on
  day N+1 or a date. (#1, #116)
- **Key** The reminder step is shown as a promise on screen ("We'll remind
  you on day 5"). Designer's part ends at the promise; flag to the team that
  the app must send it, without designing the push. (#1)
- The price after the trial inside the last step and next to the button.
  (observed)
- On the paywall or the step right before it. (Adapty library)

**Where it flips:** earlier in onboarding it adds drop-off before the paywall
(Adapty library). A timeline that hides the price (vague steps, price moved
away) reads as a hidden charge: screen flag. In #150 Fits an honest-timeline
paywall lost to a trial-toggle paywall on ARPU (toggle version +19%, strong,
but bundled: it also showed the yearly price per week and a "Most Popular"
badge, which the team credits, not the toggle). The toggle is an iOS
rejection risk (screen flags): borrow the hierarchy (mechanic 2), not the
toggle. https://www.revenuecat.com/blog/growth/rip-toggle-paywall

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
- ARPU about +20%, conversion to paid over +50% (one test, bundled: weekly
  plan added + annual flagged as the top choice): #80 Rash ID, strong.
  https://superwall.com/case-studies/rash-id
- Proceeds per user +80%, trial conversion +22% (one test): #79 Preu AI,
  strong (an annual plan added as an anchor next to a monthly-only paywall;
  an offer change, the team's decision). https://superwall.com/case-studies/preu-ai
- Conversion +50%, proceeds per user +62.5% (one test): #94 Stardust, strong
  (yearly + weekly paywall: a discount % on the yearly plan and its
  weekly-equivalent price added).
  https://superwall.com/blog/how-stardust-increased-ios-app-revenue-by-4x-in-six-weeks
- Conversion 3.14% → 3.77% (one test): #105 Glam AI, strong (onboarding
  paywall: the $59.99 year moved to the top with "Most Popular", the $119.99
  Business plan below it). https://adapty.io/blog/glam-ai-paywall-tests/
- Yearly conversion 0.43% → 0.55%, net revenue per user $0.261 → $0.292,
  weekly flat (one test): #104 Glam AI, strong (a $119.99 "Yearly Business"
  plan added as a decoy next to the $59.99 year; an offer change). Same link.
- ARPU +56.8%, yearly conversions +23.7% (one test, bundled: a discounted
  yearly plan offered next to a free trial that was promoted alone, with
  value copy; truck-plan users only): #142 TomTom, directional.
  https://www.purchasely.com/case-studies/increasing-mrr-85-percent-against-free-competitors
**Call:** revenue per user → Adapty band (per user). #43 is per impression
and splits by market: use it only when the change is just the per-month
display, with the market rule. #94, #104, #105 and #142 are context.

**What the winners had**
- **Key** Annual preselected and dominant: filled card, first position.
  (Adapty library; #105: year on top with "Most Popular" won)
- **Key** The annual price also shown per month or week, so it compares with
  the short plan at a glance, with the billed yearly amount still the most
  prominent price. (#43; store rule below)
- **Key** Short plans still reachable ("View all plans"), not removed. (#42;
  but the same layout lost in #95, see below)
- A saving named against a plan the user can see ("Save 50% vs monthly").
  Anchoring to a hidden or rarely bought plan inflates the number and costs
  trust. (observed; paywall-teardown playbooks; #94 won with a discount % on
  the yearly plan and a weekly-equivalent price)

**Where it flips:** cutting the plan count (four down to two) lost revenue in
the double digits (Adapty library). Hiding short plans lost too: in #95
Stardust both "yearly first + More Pricing button" and "yearly plan only"
lost to the control on conversion and proceeds per user (anecdotal, no
figures), so #42 is a result to test, not a rule. Plan sets are the team's
offer decision; what they did on screen: weekly pairs lost to
monthly/annual (#123 travel app, no figures); several price options lost to
one, and a single weekly price "always won" (#124, #126 GlowUp, no figures);
weekly plans added went up in some markets and flat or down in others (#127
Feeld, no figures); a 3-month plan added with a higher annual price moved
annual share 75% → 17% with install → subscription unchanged (#122
OctaZone, directional, bundled). A decoy plan that won on the main paywall
had no measurable effect on inner paywalls (U53 Glam AI, no figures), and
cutting the decoy's price did nothing (#110, no figures). Conversion can drop while revenue rises:
judge by revenue per user. **Store rule:** the billed amount must be the most
prominent price; a per-month figure bigger than the yearly total is a
rejection risk on Apple and a listed violation on Google (paywall-store-
compliance, A1).

## 3. Trial on the annual plan only

**Spot it:** A had a trial on more plans; B keeps it only on annual. (If A
had no trial at all, it's mechanic 13, with "on annual only" as one of its
traits.)
**Fits when:** an annual plan and a shorter plan; deciding which plans get a
trial is the team's offer decision, the check covers how it reads.

**Range seen**
- Paid conversion +15% to +30%: Adapty library band, strong.
- Paywall view → subscription +39%, revenue per 100 installs +47%, ARPPU +5%:
  #41 Moonly, strong (trial added to the annual plan only).
  https://adapty.io/case-studies/moonly/
- Subscriptions by plan, no baseline given: monthly +2,000%, quarterly +46%,
  annual +21% (one test): #149 Natal, directional, podcast (the trial
  removed from the monthly plan; quarterly and annual kept theirs).
  https://www.revenuecat.com/blog/growth/nancy-anderson-natal-sub-club-podcast-2026
**Call:** paid conversion → Adapty band; revenue per 100 installs → #41
(one test). #149 is per plan with no baseline: context only.

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
- Conversion 2.54% vs 2.43%, called noise (one test, **null**): #106 Glam
  AI, directional (a social-proof video added to a new plan picker).
  https://adapty.io/blog/glam-ai-paywall-tests/
**Call:** paid conversion → Adapty band. Revenue per user: no call.

**What the winners had**
- **Key** A real review with a name and stars, instead of a claim the app
  makes about itself. (#60)
- A specific number ("4.8 from 200K+ ratings"), near the button or plans.
  (observed)

**Where it flips:** a redesign adding a comparison table and testimonials
together lost (Adapty library). Test proof on its own. Proof as a video in
the plan picker moved nothing (#106).

## 5. Free vs paid comparison as the paywall

**Spot it:** a table of what free gets and what paid adds, on the paywall.
**Fits when:** the app has a real free tier to compare with.

**Range seen**
- Revenue per user about +15% as an in-app paywall (iOS up, Android flat):
  Adapty library band, strong. Larger onboarding-paywall figures exist but are
  directional (small samples): *outlier*.
- Conversion "+1%" (relative or points not stated), paid activation +5% (one
  test): #81 Symmetry, directional (feature list → Free vs Pro table, headline
  and button unchanged). https://superwall.com/case-studies/symmetry
**Call:** revenue per user → +15% (treat as one number). #81 is a reminder
that a table alone can land far below the band.

**What the winners had**
- **Key** On the paywall itself, not as a teaser screen before it. (Adapty
  library)
- 3 to 5 rows of decision-relevant differences, above the plans. (observed)

**Where it flips:** a bare comparison step before the paywall lost on revenue
and conversion; one "win" was a randomisation bug (Adapty library). The
reverse won once: a comparison-chart paywall (feature table, three tiers,
heavy copy) → one simple page "beat control by 111%" (#100, unnamed app,
directional, bundled, denominator not stated).
https://superwall.com/blog/the-paywall-tactics-behind-usd100k-month-apps

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
- Trial opt-in +60%, cancellations lower (no figure) (one test): #157 Mimo,
  directional, podcast (single-screen → multi-screen paywall).
  https://subclub.com/episode/how-to-build-more-successful-paywalls-sylvain-gauchet
**Call:** paid conversion → +16% to +27% (two tests); trial starts → #157
(one test, directional).

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
- Trial conversion 19.05% → 23.64% (one test): #114 Quiet portfolio app,
  strong (button colour purple → white, nothing else changed).
  https://adapty.io/case-studies/quiet/
- Registration → trial 3% → 27% (one test): #132, directional, conference
  talk ("Subscribe" → "Start your 7-day free trial"): *outlier*.
  https://adapty.io/blog/how-to-build-app-onboarding-flows-that-convert/
- Conversion 1.14% vs 0.78% (one test, bundled: "Continue" → "Start for
  $0.00", emphasis moved from weekly to annual, yearly price changed): #121
  Going Merry, directional. https://adapty.io/case-studies/going-merry/
**Call:** paid conversion or trial starts → Adapty band. Revenue per user:
no call. #114 sits inside the band: context.

**What the winners had**
- **Key** Says what happens and that it's free now ("Try for free", "Start my
  free week"). (#67; Adapty library; #132)
- Highest-contrast element on screen, full width. (observed; #114: a colour
  change alone moved trial conversion)

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
- Conversion over +50%, estimated ARPU +64% (one test): #82 Unchaind, strong
  (text paywall → visual app-preview paywall): *outlier* (no baseline, above
  the band). https://superwall.com/case-studies/unchaind
- View → payment 1% → 1.25%, but net revenue per user below control on all
  traffic and in the US (no figures); control kept (one test, **mixed**):
  #103 Glam AI, strong (static images → video hero, plans and prices
  unchanged). https://adapty.io/blog/glam-ai-paywall-tests/
- Conversion +67%, proceeds per user +12.5% for the video arm, against
  +55.7% and +9% for the same earlier winners without video, both vs control
  (one test, bundled): #96 Stardust, strong (video background instead of a
  text-heavy design).
  https://superwall.com/blog/how-stardust-increased-ios-app-revenue-by-4x-in-six-weeks
- "Flat" (**null**, no figures): #158 Citizen, anecdotal, podcast (video
  added to the paywall).
  https://subclub.com/episode/a-systematic-approach-to-paywall-optimization-live-at-app-promotion-summit-nyc
- Conversion about +80%: #159 FitnessAI (same as #71), directional, bundled
  (video added and the paywall moved before onboarding): *outlier*. Same
  link.
- 2.9x average lift: #153 CoinStats, directional (animated, playful paywall
  reveal): *outlier*.
  https://www.revenuecat.com/blog/growth/weird-paywalls-drive-subscription-growth
- Conversion 20% → 30%, denominator not stated (one test): #98 Clear 30,
  directional (a feature carousel → the programme's first seven days laid out
  day by day; a content change, not motion).
  https://superwall.com/blog/how-two-founders-tripled-their-app-revenue-in-8-weeks
**Call:** the Adapty band on the test's metric.

**What the winners had**
- **Key** The visual shows the product or the result, not decoration.
  (Adapty library: "supports the offer"; #98 showed the first week of the
  programme)

**Where it flips:** load time on slow devices; decoration that pushes plans
below the fold. Video is the weak spot in single tests: #103's video hero
raised conversion and lost revenue per user, #158 was flat, #106's
social-proof video was noise, and in #96 video added little over the same
layout without it. Judge a video variant on revenue per user, not
conversion. Taking visuals out lost too: a carousel of premium-feature cards
→ a minimal bulleted list on a dark screen with no images "failed" and was
taken down (#165 Adobe, anecdotal, no figures).
https://adobe.design/ideas/growth-design-and-the-art-of-failing-successfully

## 11. Price level

**Spot it:** the same layout with different prices.
**Fits when:** never suggested by this check: price is the team's decision.

**Range seen**
- Revenue per user +15% to +25% in top-paying markets: Adapty library band,
  directional (geo split).
- Conversion −5% after a +30% price (one test): #59 travel app, strong.
  https://adapty.io/case-studies/travel-app/
- Yearly price +50%: conversions −19%, proceeds per user +25% (one test):
  #85 BuyBye, strong. https://superwall.com/case-studies/buybye
- Annual price lowered $59.99 → $44.99: ARPU +10% (one test): #84 SellRaze,
  strong. https://superwall.com/case-studies/sellraze
- ARPU +83% for the highest of three price tiers (prices not stated, other
  tiers not reported) (one test): #90 Planner 5D, strong.
  https://superwall.com/case-studies/planner-5d
- Weekly $6.99 → $9.99: proceeds per user +47.5%, conversion "minimal"
  erosion (no figure) (one test, mixed): #91 PropGPT, strong.
  https://superwall.com/case-studies/propgpt
- $59.99/yr + $8.99/wk → $79.99/yr + $11.99/wk for owners of $800+ iPhones:
  conversion 2.55% → 2.09%, ARPU flat (one test, **loss**): #107 Glam AI,
  strong. https://adapty.io/blog/glam-ai-paywall-tests/
- Annual $9.99 → $14.99: won at 99% probability to be best, conversion did
  not move (no lift figure): #117 AppDevLabs, strong. Annual $19.99 → $14.99
  (a cut): more subscribers and higher total revenue (no lift figure): #118,
  directional. https://adapty.io/case-studies/appdevlabs/
- Price cut of 25% in Mexico: new revenue +25% (Mexico only): #137 Mojo,
  directional.
  https://www.botsi.com/blog/pricing-experiments-the-backbone-of-mojos-monetization-success
- Discounts on the paywall: subscriptions "roughly" +20% with a discount
  offer vs none, repeated across campaigns (#146 The Economist, directional,
  https://blog.funnelfox.com/cracking-the-app-paywall-playbook/); a 50%
  coupon on the Business plan cut placement revenue per user 5x (#111 Glam
  AI, directional, **loss**); a $59 intro year against the standing $79 year
  sold 0 yearly plans to 2,500 users (#109 Glam AI, directional, **loss**).
- Losses and nulls without figures: higher yearly prices with no trial gave
  lower conversion and similar proceeds per user (#93 Stardust); weekly kept
  at $11.99 after the yearly went back sagged (#108 Glam AI); weekly $1.99 →
  $2.99 failed in the UK while the same move worked in Europe for another app
  (#119 AppDevLabs); every price above $19.99 lost on every metric (#141
  TomTom); very low vs mid price, no difference (#125 GlowUp); standard
  pricing or no offer beat intro discounts or a Black Friday offer in some
  cases (#128 Feeld, #163 Mojo). A slightly higher weekly price next to the
  annual cut weekly purchases and lifted annual ones (#120 AppDevLabs, mixed).
**Call:** revenue per user → Adapty band, top markets only. Single tests run
both ways: rises won in #85, #90, #91, #117 and lost or went flat in #59,
#93, #107, #141; cuts won in #84, #118, #137. The direction isn't settled by
the band.

**What the winners had:** rises limited to top-paying markets. The
designer's part is how the price reads (mechanics 2, 13).

**Where it flips:** the same rise lost badly outside top markets; a rise for
one device segment lost too (#107). A rise that won at rollout can lose
later: six months on, the control was ahead because it renewed more (#167,
anecdotal, podcast). Read renewals before calling a price rise.
https://pod.wave.co/podcast/sub-club-by-revenuecat/stop-celebrating-conversion-wins-before-checking-renewals-sara-grana-yousician

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
- Paywall conversion +9.5%, ARPU +13% (one test): #139 Dogo, directional
  (one generic paywall → a paywall per user segment, each leading with a
  different value). Above the prior, but copy per segment is more than a
  headline swap. https://www.botsi.com/blog/personalize-paywall-messaging
- Install → trial +72%: #152, directional (a second paywall leading with a
  results statistic, "86% improved their diet"): *outlier* (other metric,
  second paywall).
  https://www.revenuecat.com/blog/growth/paywalls-unexpected-uses
- "10% difference" (direction implied, metric not stated): #101, anecdotal,
  bundled (plain plan names, a "Continue" button, "No commitment, cancel
  anytime"). Not used.
  https://superwall.com/blog/the-paywall-tactics-behind-usd100k-month-apps
**Call:** the prior on the test's metric.

**What the winners had**
- Outcomes instead of features, in the user's words. (#2 Five Minute
  Journal, onboarding rebuild, directional:
  https://www.revenuecat.com/blog/growth/five-minute-journal-onboarding-redesign-arpu/ ;
  observed on paywalls)
- Headline wins often come from a plan-mix shift: check what moved (Adapty
  library).

**Where it flips:** specific promises the app can't back (a time, a
percentage, a result) are a trust and review risk: screen flag. Copy-only variants usually land below
what a normal test can see. A red brand-promise banner added above the plan
cards dropped conversion "drastically" (#144 The Economist, anecdotal, no
figure). https://blog.funnelfox.com/cracking-the-app-paywall-playbook/

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
- Paywall conversion (as reported) +131%, proceeds per user +78%, paying
  subscribers +45% (one test): #92 Stardust, strong (a 7-day free trial
  added to the $24.99/year plan at the same price; one of five price arms).
  https://superwall.com/blog/how-stardust-increased-ios-app-revenue-by-4x-in-six-weeks
- Revenue +140% vs control, denominator not stated (one test): #115
  Pregnancy+, strong (a discounted intro price replaced by a free trial with
  no upfront cost). https://adapty.io/case-studies/pregnancy-plus/
- No figures: on a monthly plan, no trial "clearly hurt" conversion and 30
  days beat 7 (#145 The Economist, anecdotal).
  https://blog.funnelfox.com/cracking-the-app-paywall-playbook/
**Call:** paid conversion → +40% (one test, directional); revenue per user
→ +78% (#92, one test, strong). #92's +131% is paywall conversion as
reported, not paid conversion; #115 doesn't state its denominator: context.

**Trial length** (A and B both have a trial; the days are the team's offer
decision): 14 → 7 days, install → paid +8% (#156 Zumba, directional,
https://www.revenuecat.com/customers/stepping-up-growth-how-zumba-boosted-conversion-by-8-with-revenuecat);
7 → 14 days, slightly more trial starts and fewer paid (#154, anecdotal,
**loss**); 3 vs 7 days, "minimal" difference (#138 Mojo, anecdotal,
**null**); a long "design your own trial" offer lost to a short trial at a
higher price for frequent diners (#102, anecdotal, **loss**); on The
Economist's monthly plan 30 days beat 7 (#145, anecdotal). No call: the one
figure is per install and the rest point both ways.

**What the winners had**
- **Key** The trial and what follows it stated next to the button ("3 days
  free, then $49.99/year"). (store rule; observed)
- When the trial is on the annual plan only, it's named on that card. (#41
  Moonly, mechanic 3)

**Where it flips:** removing a trial won where trial-to-paid was very low,
and the same change lost on another platform (Adapty library). Making the
trial opt-in (the user picks it) raised trial conversion +10% but lowered
trial starts (#83 Linearity Curve, directional). A trial toggle on the
paywall: Apple rejects it as of February 2026 (per RevenueCat's paywall
redesigns article, #87–#89): screen flag on iOS. Removing every trial and
showing six plans lifted LTV per payer ($35–40 → over $60) while new trials
fell to zero (#155, directional, mixed).
https://www.revenuecat.com/blog/growth/should-your-app-stop-offering-free-trials

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
- iOS: no free-trial toggle on the paywall (Apple rejects it as of February
  2026, per RevenueCat's paywall redesigns article; check the current App
  Review guidelines).
- A change that makes these worse (price moved away, ✕ hidden) is a fix
  with priority over everything else.

## Checks

- Mechanics: 13. Calls rest on an Adapty band: 1, 2, 3, 4, 5, 9, 10, 11;
  on single tests only: 6, 7, 13; on a prior: 12. Mechanic 8 is called only
  when the button changes on its own; tied to an offer change it's part of
  that mechanic. Single tests also call where no band covers the metric: 1
  (trial starts, #97 + #1), 3 (revenue per 100 installs, #41), 7 (trial
  starts, #157), 13 (revenue per user, #92).
- 2026-10-31 deep sweep: paywall rows #90–#165 folded in as single-test
  context (bands unchanged): 1 (#97, #116, #150), 2 (#94, #95, #104, #105,
  #110, #122, #123, #124, #126, #127, #142, U53), 3 (#149), 4 (#106), 5
  (#100), 7 (#157), 8 (#114, #121, #132), 10 (#96, #98, #103, #153, #158,
  #159, #165), 11 (#90, #91, #93, #107–#109, #111, #117–#120, #125, #128,
  #137, #141, #146, #163, #167), 12 (#101, #139, #144, #152), 13 (#92,
  #102, #115, #138, #145, #154–#156). Losses and nulls without a figure are
  listed in the text and never enter a range.
- Not mapped (not a change on the paywall screen): onboarding rows #99,
  #112, #113, #129–#131, #133–#136, #140, #143, #147, #148, #160–#162,
  #164 (onboarding-mechanics.md covers them); #151 (where the paywall sits in
  the flow, not a paywall variant); #166 (card required for the trial: a
  billing setting); U52 (hard paywall: a business model); U62 (upgrade
  button for payers: upsell-teardown).
- Every "What the winners had" line carries its source; key traits have a
  test behind them.
- Rebuild when the Adapty library summary or the onboarding evidence changes.
