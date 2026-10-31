# Onboarding mechanics: ranges and what the winning versions had

One section per mechanic an onboarding variant can change, from the first
screen to the first paywall and what happens when it's closed. Same format as
`mechanics.md` (Spot it, Fits when, Range seen with the call, What the
winners had, Where it flips).

A change to the paywall screen itself (plans, trial timeline, button, close,
visuals, proof on the paywall) is a paywall mechanic: use `mechanics.md`, with
the denominator rule below.

## Sources

- **#N**: a published test in the onboarding-teardown evidence library
  (`onboarding-teardown/references/evidence.md`), same numbers. The link is
  in the line.
- **Adapty library**: Adapty's A/B test library as summarised in the
  `paywall-ab-test-assistant` skill (`references/evidence-library.md`,
  sections ONBOARDING and ACROSS THE FLOW). Each band pools many tests.
- **Observed**: what top apps' onboarding does (onboarding-teardown pattern
  library). No test behind it.

Tiers are the same as in `mechanics.md`: strong, directional, observed.
Adapty bands labelled Strong or Solid are strong.

## Metrics and denominators (keep apart)

An onboarding test splits people when they first open the app, so every
metric is **per new user (per install)** unless a line says otherwise.

- **Trial starts**: new users who start a trial.
- **Paid conversion**: new users who pay (conversion to purchase, to paid, to
  subscription).
- **Revenue per new user**: Adapty's ARPU in an onboarding test (per user in
  the test).
- **"Trial conversion (as reported)"**: the source doesn't say whether it means
  trial starts or trial-to-paid. It never makes a call; list it under "also
  seen".
- **Off-target metrics** (DAU, retention, course starts, push opt-in,
  sign-ups on the web, landing visitor → paid): never make a call on trial
  starts, paid or revenue.

**Per view → per install.** A paywall range measured per paywall view
carries over to an onboarding test only when B doesn't change how many new
users reach the paywall. If B also moves the paywall or adds or removes
screens before it, say the paywall range describes the people who reach it,
not every new user.

## Rules for the call

Everything in `mechanics.md` "Rules for the call" applies (call range on the
test's metric, one test = one number, outliers out, bands before single
tests, market rule). Two more for onboarding:

- **Bundled or directional only → "maybe" at most.** When every test behind
  a call changed several things at once (marked *bundled*) or is directional
  (no stated method), the call is at most "maybe", even if the number clears
  the bar. Execution can still cap it one step lower. Name the mechanic to
  isolate. Only Adapty bands and strong unbundled tests can make "likely".
- **One issue, one cap.** A missing key trait that is also a screen flag caps
  the call once and is listed once under "Fix before launch".
- **No call anywhere → rethink.** If no change in B has a call on the test's
  metric, the verdict is "rethink": there is no published reason to expect a
  visible change. Say "no call", never "won't work".
- **Rethink tie-break**, after the order in SKILL.md: a stronger call, then a
  stronger tier (band or strong over directional), then the same library as
  the test. For an onboarding test, a paywall mechanic may be suggested for
  the paywall at the end of the flow, with the per view → per install rule.
- **Losses make a "likely to lose" call.** When the published results for
  the change B makes are losses (mechanic O7 shortening, mechanic O5 adding a
  loader before a plan screen), the call is "likely to lose", whatever the
  bar. Under "find a win", that means rethink; under "prove not worse", it
  means the test is likely to fail its margin: say so.

---

## O1. Value promise on screen 1

**Spot it:** A opens on a logo, a generic welcome or a sign-in sheet with no
statement at all; B's first screen says what the user gets, with a product
visual and one button.
**Fits when:** screen 1 has no statement of what the user gets. If A's screen
1 already states something (a feature line, a tagline) and B rewords it into
an outcome, that's O2, not O1.

**Range seen**
- Paid conversion +30% (one test, *bundled*: shorter copy + value promise up
  front + testimonials): #17 travel app, strong.
  https://adapty.io/case-studies/travel-app/
**Call:** paid → +30% (bundled: "maybe" at most).

**What the winners had**
- **Key** The value promise is on the very first screen. (#17)
- **Key** Copy cut down: one promise, not a paragraph. (#17)
- A visual of the product in use and one primary button; consent in small
  print under it. (observed)

**Where it flips:** a promise the first session can't keep. App Review 2.3
expects the promise to match the app: screen flag.

## O2. Outcome copy over feature copy

**Spot it:** B rewrites screens, including screen 1's headline, from what
the app has ("AI-powered", "500 recipes") to what changes for the user
("Fall asleep in 10 minutes").
**Fits when:** most screens name features.

**Range seen**
- Revenue per new user +13% to +20% (two tests): #11 unnamed productivity
  app, directional (outcome vs feature onboarding); #2 Five Minute Journal,
  strong, *bundled* (JTBD rebuild: segment-specific content, testimonials
  earlier, benefit copy; p = 0.04).
  https://adapty.io/blog/how-to-fix-your-onboarding-flow/ ;
  https://www.revenuecat.com/blog/growth/five-minute-journal-onboarding-redesign-arpu/
- Trial starts about +10% (one test): #2, strong, *bundled*.
- Also seen: trial conversion (as reported) about +14% to +17% (#2, #11);
  landing visitor → paid +39% (#19 Smart Tales, conference talk; other
  denominator).
**Call:** revenue per new user → +13% to +20%; trial starts → +10% (bundled:
"maybe" at most). Paid: no call.

**What the winners had**
- **Key** Content changes by the user's segment or job, not only the wording.
  (#2)
- **Key** Each value line names a result for the user. (#11, #2)

**Where it flips:** wording-only edits are small; the winners changed what
the screens show. A copy-only B usually lands below the bar.

## O3. Goal questions that change what follows

**Spot it:** B adds one or more questions about the user's goal, reason or
level (A asks none, or only profile data), or turns a single-select into
multi-select. If A already asks the goal question and B only starts using
the answer, that change is O4 or O13 (the answers are now used), not O3; a
question B adds next to it (a level question) is O3.
**Fits when:** the app serves several goals or levels; rare in VPN, password
and AI chat apps (observed).

**Range seen**
- Paid conversion +8% to +17%, revenue per new user +13% to +35%: Adapty
  library band (goal personalisation, many tests), strong.
- Trial starts +8.5% to +25% (two tests, both *bundled*): #13 unnamed
  productivity app (questions + loader vs generic demos), #12 unnamed
  education app (survey + trial lesson), directional.
  https://adapty.io/blog/how-to-fix-your-onboarding-flow/
- Also seen: trial conversion (as reported) about +10% (#4 Headspace,
  multi-select, interview); course starts +7.6 pp (#3 Headspace, strong),
  with no change in active days.
**Call:** paid and revenue → Adapty band; trial starts → +8.5% to +25%
(bundled: "maybe" at most).

**What the winners had**
- **Key** The answers change what comes next: the plan, the next screens or
  the paywall headline. (Adapty library; #13)
- One question per screen, large answer cards, multi-select where people have
  several reasons. (#4 directional; observed)
- A short line on why you ask, for sensitive questions. (observed)

**Where it flips:** questions whose answers are never used read as a survey
and add drop-off (onboarding-teardown pattern 3). Personalisation lifts
starts more reliably than use (#3): read paid, not only trial starts.

## O4. A plan built from the answers

**Spot it:** before the paywall B shows a plan, course or report that repeats
the user's goal and answers; A's screen before the paywall is generic.
**Fits when:** the flow asks questions (mechanic O3) and the product can
actually tailor something.

**Range seen**
- Paid conversion +10% to +17% (two tests): #27 Grammarly ("10%+", number
  without a source), #13 (*bundled*, global; US +27%), directional.
  https://growth.design/case-studies/grammarly-onboarding-survey
- Trial starts +8.5% (one test, *bundled*): #13.
- Revenue per new user +22% (one test, *bundled*; US +35%): #13.
- Also seen: course starts 31.25% → 62.97% (#3 Headspace "perceived fit",
  strong, off-target, bundled with a course choice).
**Call:** paid → +10% to +17%; trial starts → +8.5%; revenue → +22%. Market
rule for #13. Every test is directional; #13 is bundled.

**What the winners had**
- **Key** The plan uses the answers: the goal in the headline, items that
  differ by answer. (#3, #13, #27)
- 2–4 personal numbers or items, editable where possible, and a short "why
  this plan" line. (observed)

**Real personalisation** (used here and in O5): the plan shows at least one
item that differs by answer beyond repeating the goal's words: a schedule,
a level, a content list, a number. A headline that only echoes the goal is
O13, not a plan.

**Where it flips:** a loader plus a personalised-plan screen lost about half
of revenue per user in another flow (Adapty library). A plan screen that
doesn't really use the answers is the version that loses. Health numbers
need a source on screen: screen flag.

## O5. Loader ("building your plan")

**Spot it:** B removes A's loading or "analysing your answers" screen, or
adds one.
**Fits when:** removing: A has a loader with nothing personal after it.
Adding: never suggested by this check.

**Range seen**
- Loader removed: revenue per new user +30% (one test): #15 unnamed
  education app, directional. Also seen: trial conversion (as reported) +22%.
  https://adapty.io/blog/how-to-fix-your-onboarding-flow/
- Loader + personalised-plan screen added: revenue per user around −50% (one
  flow): Adapty library.
**Call:** removal, revenue → +30% (one test). Removal, trials or paid: no
call. Adding a loader → "likely to lose", unless it comes with real
personalisation (then call mechanic O4 instead, with this as a watch item).

**What the winners had**
- **Key** Removal won where no real personal plan followed the loader. (#15)

**Where it flips:** a loader that follows real personalisation and leads
straight to a plan built from the answers can be part of a win (#13, bundled).

## O6. Core action first

**Spot it:** before the paywall B lets the user do the app's core job once
on their own input (a lesson, an edited photo, a heard voice) and see the
result; A shows a feature carousel or goes straight to the paywall.
**Fits when:** the core action fits into a minute or two; in AI apps, each
free result costs money (pair with a short trial).

**Range seen**
- Trial starts +25%, revenue per new user +78% (one test, *bundled*: survey +
  trial lesson): #12 unnamed education app, directional.
  https://adapty.io/blog/how-to-fix-your-onboarding-flow/
- Also seen: DAU about +20% (#5 Duolingo, sign-up moved after a first lesson,
  strong, off-target); engagement +4% per step (#77 Fender Play, "Play a song"
  first); web sign-ups +15–20% (#28 Pinterest).
**Call:** trial starts → +25%; revenue → +78% (bundled: "maybe" at most).
Paid: no call.

**What the winners had**
- **Key** The user does the core action once and sees the result before the
  paywall. (#12, #5, #77)
- **Key** Paired with the goal question: survey + lesson beat either alone.
  (#12)
- A sample fallback when the user won't give access yet (photo, data).
  (observed)

**Where it flips:** a free result that is better than the paid product sets
wrong expectations. A carousel of features is not this mechanic.

## O7. Flow length

**Spot it:** B adds screens that set up the value (A had none or very few),
or B cuts A's flow down.
**Fits when:** adding: A lands people on the paywall or the app with no
set-up. Cutting: only steps whose answers are never used.

**Range seen**
- Longer onboarding vs none: paid conversion +40% (iOS), revenue per new user
  +20% (one test): #14 unnamed entertainment app, directional.
  https://adapty.io/blog/how-to-fix-your-onboarding-flow/
- Shortened vs long: conversion −13% (#14, directional); cutting onboarding
  down lost, conversion and ARPU both around −13% (Adapty library, solid).
**Call:** adding → paid +40% (iOS figure: market/platform rule), revenue
+20%. Cutting steps that ask, show value or set something up → "likely to lose".
Removing only a screen that asks nothing, shows no product result and sets
nothing up (one feature slide) → no published range; note under Watch for
that cutting lost in published tests.

**What the winners had**
- **Key** The added steps feed something later: the plan, the paywall, a
  reminder. (#14; Adapty library: "relevant steps (age, reminders, setup)")
- A progress bar or step count in flows over about 8 screens. (observed)

**Where it flips:** "shorter to reduce friction" is the most common losing
change. Cutting only steps whose answers go unused is a different change:
no published range; say so.

## O8. Social proof before the ask

**Spot it:** B adds ratings, reviews or a user count on a screen before the
paywall (or before sign-up).
**Fits when:** no proof anywhere before the paywall. Proof on the paywall
itself is paywall mechanic 4.

**Range seen**
- Paid conversion +30% (one test, *bundled* with shorter copy and the value
  promise): #17 travel app, strong.
- Trial starts about +10%, revenue per new user +20% (one test, *bundled*):
  #2 Five Minute Journal, strong (testimonials moved earlier).
- Also seen: +3% on an unclear metric (#49 Headspace, in-session messages).
**Call:** paid → +30%; trial starts → +10%; revenue → +20%. All bundled:
"maybe" at most.

**What the winners had**
- **Key** Testimonials from real users, placed earlier in the flow. (#2, #17)
- A rating with its volume, or a review naming a result; one screen or block
  before the hardest step. (observed)

**Where it flips:** invented reviews or live counters: screen flag. Stacking
proof with a comparison table in one change lost on the paywall (Adapty
library).

## O9. Sign-up later

**Spot it:** B moves account creation after the first value, makes it
skippable, or softens the wall ("Later" instead of "Discard my progress").
**Fits when:** the product shows value without an account. If sync or
security is the product (VPN, passwords, AI chat history), an early account
is the norm: don't suggest it.

**Range seen**
- Paid conversion about +8%, revenue per new user about +17%: Adapty library
  (registration friction reduced), solid → strong; one band, treat each as one
  number.
- Also seen: DAU about +20% (#5 Duolingo, delayed sign-up) and +8.2% (#6,
  softer wall wording), strong, off-target; creator enrolment +25% (#33
  TikTok, delayed KYC).
**Call:** paid → +8%; revenue → +17%. Trial starts: no call.

**What the winners had**
- **Key** Sign-up after the user has something to save. (#5)
- **Key** A quiet way past the wall: "Later", not "Discard my progress". (#6)
- Sign-up framed as saving their plan, with Sign in with Apple. (observed;
  Tiimo #73 anecdotal: early sign-up framed this way also won)

**Where it flips:** a purchase with no account must still restore on another
device; flag the restore path to the team, without designing it.

## O10. Reminder set-up inside onboarding

**Spot it:** B adds a step to pick when to practise, with a preview of the
reminder; A leaves reminders for later or Settings.
**Fits when:** a habit app (education, meditation, fitness, productivity).

**Range seen**
- Revenue per new user +24% (one test): #16 unnamed education app,
  directional. Also seen: trial conversion (as reported) +6.4%.
  https://adapty.io/blog/how-to-fix-your-onboarding-flow/
**Call:** revenue → +24%. Trials and paid: no call.

**What the winners had**
- **Key** The step sits inside onboarding, not on the home screen. (#16)
- A preview of the reminder before the system notification dialog. (#7
  Calm, directional; observed)

**Where it flips:** a pre-prompt that mimics the system alert or says "Allow"
is a rejection risk: screen flag. On Android a refusal can't be asked again
easily, so an early ask burns it.

## O11. Commitment screen

**Spot it:** B adds a moment where the user commits: a daily goal with an
"I'm committed" button, a signed pledge, a plan to stick to.
**Fits when:** a habit or behaviour-change app.

**Range seen**
- Only off-target metrics: D30 retention doubled (#25, directional); app
  opens +7.5%, no change in active meditation days (#3 Headspace, strong).
**Call:** no call on trial starts, paid or revenue (measured on retention and
opens).

**What the winners had**
- **Key** A goal the user can keep; a less demanding goal raised retention
  (#74 Duolingo, strong, post-onboarding).

**Where it flips:** the hardest option as the default backfires (#74).

## O12. Paywall position

**Spot it:** B moves the first paywall at least two screens earlier or later
relative to the value steps (before vs after the plan, the first result or
the questions). A paywall that shifts by one position only because screens
before it were added or removed is not O12: record it under the reach check.
**Fits when:** compare with the bucket norm (onboarding-teardown
`categories.md`).

**Range seen**
- Trial starts about +10% (paywall two screens earlier, founder's estimate
  inside a cumulative programme): #8 Opal, directional.
  https://subclub.com/episode/lessons-from-121-ab-tests-kenneth-schlenker-opal
- Install-to-trial doubled, trial-to-paid unchanged (*bundled* with a paywall
  video): #71 FitnessAI, directional: *outlier*.
- Revenue 5× (#72 Rootd, before/after) and +16% premium conversions (#51,
  which placement won is unverified): *outlier*.
**Call:** trial starts → +10% (one test, directional). Paid and revenue: no
call.

**What the winners had**
- **Key** As early as possible, but after the personal report or plan, not on
  screen 1. (#8)
- Benchmark for context, not a lift: install-to-paid 1.35% for an onboarding
  paywall with trial vs 0.89% in-app (Adapty State of In-App Subscriptions
  2026).

**Where it flips:** an earlier paywall raises paywall views and can lower
activation; read trial starts and paid apart. Later paywalls lose reach: in
one long onboarding only 40% of new users saw it (anecdotal).

## O13. Paywall echoes their answers

**Spot it:** B's paywall headline or benefits repeat the goal the user
picked, or segments go to their own paywall; A's paywall is the same for
everyone.
**Fits when:** the flow asks questions.

**Range seen**
- Paid conversion "10%+" (#27 Grammarly, number without a source) to +50%
  (#23 JourneyStamp, *bundled*: context-specific paywalls, metric as
  reported), directional.
  https://superwall.com/case-studies/journeystamp
- Also seen: trial-to-paid +20%, MRR +83% (#22 Flirt AI, confounded with
  pricing and product changes); trial starts +183% (#54 Daily Horoscope,
  country segments with different prices): *outlier* (another change).
**Call:** paid → +10% to +50% (both directional; "maybe" at most because
neither test isolates the echo).

**What the winners had**
- **Key** The user's goal is in the paywall headline. (#27)
- One personal number or the plan name from the previous screen. (observed)

**Where it flips:** echoing sensitive data (weight, health, money) feels
intrusive: echo goals, not data.

## O14. A value step before the plans

**Spot it:** the first paywall becomes two or three screens: what you get
(or "try it free"), how the trial works, then plans and price.
**Fits when:** A's first paywall is one dense screen.

**Range seen:** paywall mechanic 7 in `mechanics.md` (paid +16% to +27%, two
tests, strong), measured per paywall view: apply the per view → per install
rule. Also seen in onboarding: #18 ASL Bloom value + trial-timeline screens,
+15% trial conversion (as reported), +12% ARPU, *bundled*; #24 Superwall
aggregate 12.41% vs 9.07%, observational: *outlier*.
**Call:** as paywall mechanic 7.

**What the winners had:** as paywall mechanic 7 (benefits first, then the
trial reminder, then the price).

**Where it flips:** a trial explainer placed further back in onboarding adds
drop-off before the paywall (Adapty library). An extra step that repeats
what the flow just said loses people (observed).

## O15. One-tap trial start

**Spot it:** B starts the trial from one clear button with the plan chosen
for the user, skipping the plan screen.
**Fits when:** the onboarding paywall offers a trial; which plan gets it is
the team's offer decision.

**Range seen**
- Trial starts +25%, trial-to-paid about flat (one test): #45 Slopes, strong.
  https://blog.curtisherbert.com/slopes-diaries-42-building-ramps-not-walls/
**Call:** trial starts → +25%. Paid and revenue: no call; flat trial-to-paid
means paid can rise only through more trials.

**What the winners had**
- **Key** One button that starts the trial, plan picked. (#45)
- **Key** What happens after the trial still stated next to the button
  (store rule; observed).

**Where it flips:** more trials with flat trial-to-paid is a win only if
refunds and cancels don't rise: watch them.

## O16. A second offer after the paywall closes

**Spot it:** when the user closes the onboarding paywall, B shows one more
screen: a discount, a cheaper plan or a longer trial.
**Fits when:** A drops people into the app with no offer after the close.

**Range seen**
- Paid (premium) conversion about +25% to +30%: Adapty library band, strong,
  iOS-heavy.
- Also seen: +10% onboarding and +10% trial conversion (#21 Rizz God,
  *bundled*: two paywalls + delayed close).
**Call:** paid → Adapty band (platform rule: read iOS and Android apart).
Revenue: no call.

**What the winners had**
- **Key** Right after the onboarding paywall, not after the main in-app
  paywall. (Adapty library)
- Shown once. (observed)

**Where it flips:** the same offer after the main in-app paywall lost about
half of revenue per user (Adapty library). A discount fired when the user
abandons the store purchase sheet is an App Review risk (#75).

---

## Bundles

- A goal question (O3), a plan from answers (O4), a loader (O5) and an
  echoing paywall (O13) often ship together: tests #13 and #12 measured them as one.
  Call the variant by its strongest called mechanic, say attribution will be
  unclear, and name the one to isolate next (usually O4 or O13: they decide
  whether the answers are used).
- O3 + O6 (questions + core action) beat either alone (#12): don't split them
  into two variants unless the question is which one matters.
- A loader added with no plan after it is a loss inside any bundle.

## Flow checks (any onboarding variant)

- **Reach.** Does B change how many new users reach the paywall (screens
  added or removed before it, the paywall moved)? Say which way, and that
  paywall-screen ranges then describe only the people who reach it.
- **Sign flips** (Adapty library, ACROSS THE FLOW): a comparison teaser
  before the paywall lost while a comparison paywall won; a guarantee screen
  before the paywall lost; a trial explainer too early adds drop-off; a
  second-chance offer wins only after the onboarding paywall.
- **Decision metric.** Trial starts can rise while paid stays flat (#45,
  #71): if the test decides on trial starts, keep paid, refunds and
  cancels in view.

## Screen flags (any onboarding variant; not legal advice)

- Permission pre-prompts: no "Allow" on the app's own screen, no copy of the
  system alert, no reward for allowing (App Review 5.1.1; HIG).
- Health or result numbers on a plan or projection carry a source or say
  they are an estimate.
- Ratings, counts and reviews are real; no live counters that aren't.
- Progress bars don't jump back or stall near the end as a trick; a loader
  doesn't pretend to compute what isn't computed.
- The first screen's promise matches the app (App Review 2.3).
- The paywall at the end follows the paywall flags in `mechanics.md` (✕,
  billed amount most prominent, trial terms next to the button).

## Checks

- Mechanics: 16 (O1–O16). Calls on an Adapty band: O3 (paid, revenue), O7
  (losses), O9, O16. On single or few tests: O1, O2, O4, O5, O6, O8, O10,
  O12, O13, O15. No call on any of the three metrics: O11. O14 uses paywall
  mechanic 7.
- "Maybe" at most (bundled or directional only): O1, O2 (trial starts), O3
  (trial starts), O4, O5, O6, O8, O10, O12, O13. Can reach "likely": O3 (paid,
  revenue band), O9, O14 (as paywall mechanic 7), O15, O16.
- Left out on purpose: patterns with no published range (why-we-ask
  microcopy, level step, relate-to cards, endowment), real-data linking
  (#34–#36 test the linking step, not a screen B would change in a
  subscription onboarding), progress indicators (#29 is a web form split).
- Built from `onboarding-teardown/references/ranges.md` and `evidence.md`.
  Rebuild when either changes.
