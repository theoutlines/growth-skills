# Onboarding Pattern Library

The reference for the onboarding teardown. It covers the first run of a mobile
subscription app, from the first screen up to and including the first paywall
and what happens when the user closes it.

Each pattern has:
- **When** it applies.
- **Cross-check**, so you never recommend adding something the flow already has.
- **How** a good version looks, described in our own words.
- **Evidence**: published results with their strength tier and the test number
  in `evidence.md`. Quote numbers exactly as written there. Never round up,
  never merge two tests into one number.
- **Seen in**: SOSA buckets (see `categories.md`) and example apps observed on
  Mobbin in October 2026.
- **Trap**: the way this pattern most often goes wrong.

## Evidence tiers (do not inflate)

| Tier | Meaning | How to word it |
|---|---|---|
| Strong | Controlled A/B or split test with numbers | "In a published A/B test, X saw +N%." |
| Directional | Numbers without a stated method, a bundle of changes, or a cumulative result | "Reported +N%, not a clean test." |
| Anecdotal | A claim without numbers | "Teams report it helps; no numbers." |
| Observed | Seen in top apps, no published result | "Common in top <bucket> apps; untested in public." |

A published number is one app's result. It is not the lift this app will get.
When a pattern only has Observed evidence, say so and frame it as a hypothesis.

## Contents

**A. Opening**
1. Value promise on screen 1
2. Outcome copy over feature copy

**B. Questions**
3. Goal or intent question early
4. "Why we ask" microcopy and reassurance
5. Level or placement step
6. Flow length fits the category
7. Progress and chapters
8. Relate-to-statement cards

**C. Value before the paywall**
9. First result before the paywall
10. Personal plan reveal that echoes answers
11. Outcome projection or quantified problem
12. Endowment: the user builds something
13. Real-data reveal

**D. Proof and commitment**
14. Social proof before the ask
15. Commitment device

**E. Friction and setup**
16. Account timing
17. Permissions in context, with a preview
18. Reminder setup inside onboarding
19. Loader or "building your plan" screen
20. Escape hatches for heavy steps
21. Sensible defaults instead of setup

**F. The seam (onboarding → paywall)**
22. Paywall position
23. Multi-step paywall or pre-paywall
24. Trial timeline and reminder promise
25. Paywall echoes the onboarding
26. Trial structure on the first paywall
27. Second chance after the first paywall
28. Dismiss treatment
29. No onboarding paywall (freemium, metered, credits)

**G. Store and platform flags**
30. Compliance flags

---

## A. Opening

### 1. Value promise on screen 1
**When:** The first screen is a logo, a generic welcome, or a sign-in sheet
with no statement of what the user gets.
**Cross-check:** A one-line outcome promise, a short brand video with a promise,
or an emotional opener (a breathing animation, hatching a pet) counts as present.
**How:** One sentence naming the outcome for this user, a visual of the product
in use, one primary button. Put legal consent in small print under the button
rather than on its own screen.
**Evidence:** #17 travel app: shorter copy, value proposition up front and
testimonials lifted conversion to purchase +30% (Strong, but a bundle of three
changes).
**Seen in:** All buckets. Dating and astrology apps (Hinge, Co–Star) open on a
brand promise; meditation apps (Headspace) on a feeling.
**Trap:** A promise the product can't keep in the first session. Store rule
2.3 also requires the promise to match the real app.

### 2. Outcome copy over feature copy
**When:** Interstitials and headlines name features ("AI-powered", "500 recipes")
rather than what changes for the user.
**Cross-check:** If most screens already name a result or job, improve the
weakest one instead of flagging the whole flow.
**How:** Rewrite each value line as the job the user hired the app for
("Fall asleep in 10 minutes" rather than "Sleep sounds library").
**Evidence:**
- #11 unnamed productivity app: outcome-focused vs feature-focused onboarding,
  trial conversion +17%, ARPU +13% (Directional).
- #2 Five Minute Journal: Jobs-to-be-Done rebuild, ARPU +20% (p = 0.04) (Strong,
  bundle of changes).
- #58 paywall copy from features to outcomes, +54% or more (Directional).
**Seen in:** Health & Fitness, Education, Productivity.
**Trap:** Copy-only changes are small. Don't promise a redesign-sized lift for
rewording.

## B. Questions

### 3. Goal or intent question early
**When:** The flow asks nothing about the user's goal, or asks only for
profile data (name, age) before the paywall.
**Cross-check:** Any question whose answer changes what the user sees next
counts. A question whose answer is never used later counts as half: flag it
under pattern 10 instead.
**How:** One question per screen, 3–6 large answer cards, multi-select where
people have several reasons. Use the answer on a later screen.
**Evidence:**
- #3 Headspace (Irrational Labs): quiz before the same course, +7.6 pp course
  starts; the "perceived fit" arm took course starts from about 31.25% to
  62.97%. Active meditation days did not change (Strong).
- #4 Headspace: intent question changed to multi-select, about +10% free-trial
  conversion (Directional).
- #12 unnamed education app: survey plus trial lesson beat either alone,
  +25% trial starts, +78% ARPU (Directional).
- Adapty library (paywall-ab-test-assistant): goal personalisation commonly
  CR +8–17%, ARPU +13–35% (aggregated priors, not one test).
**Seen in:** Health & Fitness, Education, Productivity (behaviour-change apps),
Utilities AI tools (Speechify). Rare in VPN, password and AI chat apps.
**Trap:** Personalisation lifts starts more reliably than long-term use (#3).
Judge it on paid conversion and retention, not on course starts alone.

### 4. "Why we ask" microcopy and reassurance
**When:** Hard or sensitive inputs (weight, birth time, income, phone number)
appear with no reason or reassurance.
**Cross-check:** A subtitle such as "this calibrates your plan", "it's OK to
estimate" or "we never sell your data" next to the field counts.
**How:** One short line under the question saying how the answer is used, plus
an "I don't know" or Skip where an answer is optional.
**Evidence:** Observed only (Cal AI, MyFitnessPal, Co–Star, Copilot Money).
**Seen in:** Health & Fitness, Social & Lifestyle (astrology, dating),
Utilities (finance).
**Trap:** Reassurance that isn't true is a store and legal risk. Only claim what
the privacy policy says.

### 5. Level or placement step
**When:** An education or skill app gives everyone the same starting content.
**Cross-check:** A self-rated level ladder or a "find my level" test counts.
**How:** A 4–5 rung ladder from beginner to fluent, then a choice between
"start from scratch" and a short placement, then a line confirming where the
user starts.
**Evidence:** Observed only (Duolingo, Brilliant, Elevate).
**Seen in:** Education (category signature), music-instrument apps (not
reviewed: no flows on Mobbin).
**Trap:** A placement test long enough to feel like an exam before any value.

### 6. Flow length fits the category
**When:** Always check. Compare the number of questions and screens before the
paywall with the bucket norm in `categories.md`.
**Cross-check:** Length is not the problem by itself. Flag length only when
steps don't pay off later (no answer reused, no value shown).
**How:** Keep steps that feed the plan, the paywall or a retention loop. Cut
steps that don't.
**Evidence:**
- #14 unnamed entertainment app: long onboarding vs none, +40% payment
  conversion (iOS) and +20% ARPU; a shortened version then lost −13%
  (Directional).
- #10 Opal: one simple default beat offering many setup options, "clear win",
  no figure (Anecdotal).
**Seen in:** Long quiz funnels in Health & Fitness, book-summary Education,
behaviour-change Productivity, Endel-style audio (20–40 screens). Short flows
in Utilities, AI chat, Photo & Video (0–2 questions).
**Trap:** "Cut onboarding to reduce friction" is the most common wrong
recommendation. Cutting lost in the published data.

### 7. Progress and chapters
**When:** A flow longer than about 8 screens shows no progress indicator.
**Cross-check:** A top bar, "Step 2 of 6", segmented dashes or named sections
all count.
**How:** A thin bar or step count; for 20+ screens, named chapters or a divider
screen before the hardest step (photos, bank linking).
**Evidence:** #29 Houzz: one contact form split into three screens, "15+%"
conversion (Directional, web). Otherwise Observed.
**Seen in:** All long flows (Cal AI, Noom, Monarch, Hinge, Headway).
**Trap:** A bar that jumps backwards or stalls near 100% reads as a trick.

### 8. Relate-to-statement cards
**When:** A behaviour-change app asks only factual questions.
**Cross-check:** Yes/No cards with a first-person statement count.
**How:** An illustrated card ("I find it hard to keep habits") with No / Yes.
Use the yeses on the plan or paywall screen.
**Evidence:** Observed only (Headway, Elevate, Me+, Endel).
**Seen in:** Education (self-growth), Productivity (habits), Health & Fitness.
**Trap:** Negative statements piled up without a payoff screen feel like
manipulation. Follow them with the plan.

## C. Value before the paywall

### 9. First result before the paywall
**When:** The paywall arrives before the user has seen the product do its core
job once.
**Cross-check:** A completed lesson, an edited photo, a first workout, a heard
voice, a playable sample or a filled product state before the paywall counts.
A feature carousel does not.
**How:** Let the user do the core action once on their own input (with a sample
fallback if they won't grant access yet), show the result, then the paywall.
**Evidence:**
- #5 Duolingo: sign-up moved after a first lesson, about +20% DAU (Strong;
  registration wall, not a paywall).
- #12 education app: trial lesson plus survey won, +25% trial starts, +78% ARPU
  (Directional).
- #28 Pinterest (web): three pages of content before sign-up, +15–20% sign-ups
  (Directional).
- #61 PepTalk: soft preview then paywall beat a hard paywall, no figure
  (Anecdotal).
**Seen in:** Photo & Video (Photoroom: your photo, the AI result, then the
paywall), Education (lesson-first), Utilities (Speechify reads real text,
Not Boring Weather works before the paywall), Health & Fitness (Fitbod's first
workout).
**Trap:** In AI apps every free result costs inference money. Pair the free
result with a short trial or credits (see category notes).

### 10. Personal plan reveal that echoes answers
**When:** The flow asks questions but the screen before the paywall is
generic.
**Cross-check:** A plan, course, report or summary that repeats the user's own
answers counts.
**How:** A results screen with the goal in the headline, 2–4 personal numbers
or items (editable where possible), and a short "why this plan" line.
**Evidence:**
- #3 Headspace: "perceived fit" doubled course starts, about 31% → 63%
  (Strong).
- #13 unnamed productivity app: up-front personalisation plus a "customising"
  screen vs generic demos, +8.5% trial starts, +17% paid, +22% ARPU
  (Directional).
- #27 Grammarly: answers drive a personalised plan, "10%+" upgrades
  (Directional, unsourced number).
**Seen in:** Health & Fitness (Cal AI numeric plan, Headspace course card),
Utilities AI (Speechify "finalizing your listening plan"), Education
(Brilliant plan as the reward for sign-up).
**Trap:** Health numbers need a source. Cal AI cites medical sources on its
plan screen; an unsourced health claim is a store and trust risk.

### 11. Outcome projection or quantified problem
**When:** A behaviour-change app never shows the size of the problem or the
expected result.
**Cross-check:** A slider asking for the user's own number, a "with us vs
without us" chart, or a before/after report counts.
**How:** Ask for the user's number (hours on the phone, hours of sleep), show
it projected over time, then show the improved curve. Keep the projection
plausible and labelled as an estimate.
**Evidence:**
- #8 Opal: motivation sequence with a lifetime phone-time projection, download
  → trial from about 7% to about 17% over several iterations (Directional,
  cumulative).
- #37 GEM SLEEP: results screen reframed with the next step and a price
  comparison, 35% → 52% (Directional).
**Seen in:** Productivity (Opal), Health & Fitness (Cal AI weight curve).
**Trap:** Fake precision. A projection presented as a promise invites refunds
and review complaints; AI apps already refund more (see categories).

### 12. Endowment: the user builds something
**When:** The user leaves onboarding with nothing they made or chose.
**Cross-check:** Liked books saved to a library, a first task created, a care
schedule, a profile built, a routine signed all count.
**How:** One short creation step on real content, saved and visible on the
paywall or home ("your 6 books are waiting").
**Evidence:** Observed only (Blinkist taste test, Structured first task, Greg
plant schedule, Hinge profile).
**Seen in:** Education (books), Productivity (planners), Social & Lifestyle.
**Trap:** A creation step that is tedious (long forms) is friction, not
endowment.

### 13. Real-data reveal
**When:** The app's value depends on the user's own data (bank accounts,
health data, screen time) and the paywall comes before that data appears.
**Cross-check:** Linking or syncing before the paywall, followed by a screen of
the user's own numbers, counts.
**How:** Link first, show the user's own organised data ("your bills this
month"), then the paywall. Offer a demo mode for people who won't link.
**Evidence:**
- #34 Swish: about 65 iterations of the bank-linking flow, +251% cumulative
  (Directional).
- #35 Stash: switched linking provider, +21% accounts connected, +19% funded
  (Directional).
**Seen in:** Utilities (finance: Copilot Money, Monarch), Productivity (Opal
Screen Time report).
**Trap:** Linking is the biggest trust hurdle. Without read-only reassurance
and a demo mode, this step is the drop-off point.

## D. Proof and commitment

### 14. Social proof before the ask
**When:** No social proof appears anywhere before or on the first paywall.
**Cross-check:** A rating with volume, a user count, dated reviews or a research
claim on any screen before the paywall counts.
**How:** One screen or block before the hardest step (sign-up or paywall):
rating with volume, a real review naming a result, or a research claim in
health. Keep the paywall's own proof short.
**Evidence:**
- #60 Runtastic: promo statement on the paywall replaced by a real 5-star
  review, +44% paid subscriptions (Directional).
- #2 Five Minute Journal and #17 travel app moved testimonials earlier as part
  of bundles that won (Strong, bundled).
- #49 Headspace: in-session social validation, +3% (Directional).
**Seen in:** All buckets. Health uses authority and research; consumer apps use
ratings and counts.
**Trap:** Live counters and invented reviews. Use only real numbers; a
fabricated count is a store and consumer-law risk.

### 15. Commitment device
**When:** A habit or behaviour-change app has no moment where the user commits.
**Cross-check:** A daily-minutes goal with identity labels, a signed contract,
a future-self letter or a precommitment plan counts.
**How:** One commitment screen after the goal question, with the CTA phrased as
the commitment ("I'm committed").
**Evidence:**
- #25 unnamed sustainability app: one commitment screen doubled D30 retention
  (Directional).
- #3 Headspace precommitment arm: app opens +7.5%, unique open days +4%, no
  change in meditation days (Strong).
**Seen in:** Education (Duolingo daily goal, Headway letter), Productivity
(Me+ contract), Health & Fitness.
**Trap:** A goal that's too demanding backfires. Duolingo's A/B test that let
one lesson keep the streak, instead of the full daily goal, raised D14
retention +3.3% and learners on a streak +10.5% (#74, strong). Don't default
users into the hardest option.

## E. Friction and setup

### 16. Account timing
**When:** Account creation comes before any value, and the product doesn't need
an account to show value.
**Cross-check:** If sync or security is the product (VPN, password manager,
cross-device notes, AI chat history), an early account is the category norm.
Don't flag it.
**How:** Delay sign-up until the user has something to save ("save your plan"),
frame it as free, offer Sign in with Apple. Replace "discard my progress" with
a quiet "Later".
**Evidence:**
- #5 Duolingo: delayed sign-up, about +20% DAU (Strong).
- #6 Duolingo: softer sign-up wall wording, +8.2% DAU (Strong).
- #33 TikTok: start before linking a bank account, +25% enrolment (Directional).
- Counterpoint #73 Tiimo: moving account creation from just before the paywall
  to right after the welcome screen raised both account creation and trial
  starts, no figures (Anecdotal). Early sign-up can work when the account is
  framed as saving the user's plan.
- Platform: App Review 5.1.1(v); HIG Sign in with Apple says ask for sign-in
  only when it delivers value (see `platform-rules.md`).
**Seen in:** Late in Education, Health & Fitness (MyFitnessPal, Fitbod),
Photo & Video. Early in Utilities (VPN, passwords), AI chat, dating.
**Trap:** Delaying sign-up past the paywall means a purchase with no account to
restore on another device. Check the restore path.

### 17. Permissions in context, with a preview
**When:** The flow fires a system permission (notifications, ATT, camera,
location, health) on launch or with no explanation.
**Cross-check:** A pre-prompt screen that shows what the user will get,
followed by the system dialog, counts. Check it against the platform rules.
**How:** Ask at the moment the feature needs it. Before the system dialog, show
a preview (a sample notification, the report the permission unlocks) with one
"Continue" button. Never "Allow" on your own screen, never an arrow pointing at
the system button.
**Evidence:**
- #7 Calm: reminder prompt after the first session, 40% set a reminder vs
  under 1% who found it in Settings; retention about 3× (Directional).
- #1 Blinkist: reminder opt-in on the trial welcome screen took push opt-in
  from 6% to 74% (Strong, part of the timeline test).
**Seen in:** Health & Fitness (Fitbod sample notification), Productivity (Opal
Screen Time framed as a report), Media & Entertainment (Endel reason screens),
Education (Duolingo widget).
**Benchmarks:** ATT opt-in 38% (Q1 2026, Adjust); push opt-in medians iOS
48.85%, Android 53.3% (2025, Airship). Use them to size the ask, not as a
target for this app.
**Trap:** Apple rejects pre-prompts that mimic the system alert, offer
incentives or use "Allow". Android denies permanently after two refusals, so
asking early burns the ask.

### 18. Reminder setup inside onboarding
**When:** A habit app leaves reminders for Settings.
**Cross-check:** A time picker or reminder slot during onboarding counts.
**How:** After the goal, ask when the user wants to practise, with a preview of
the reminder.
**Evidence:** #16 unnamed education app: reminder setup inside onboarding vs on
the home screen, +6.4% trial conversion, +24% ARPU (Directional). #7 Calm as
above.
**Seen in:** Education, Health & Fitness (meditation), Productivity.
**Trap:** A reminder prompt that leads straight into the system dialog without
a preview (pattern 17).

### 19. Loader or "building your plan" screen
**When:** The flow has a loading or "analysing your answers" screen.
**Cross-check:** This pattern is about judging an existing loader. Don't
recommend adding one.
**How:** Keep a loader only if it follows real personalisation and leads
straight to a plan that shows the answers back. Keep it short. Otherwise test
removing it.
**Evidence (contested):**
- #15 unnamed education app: removing the loader won, +22% trial conversion,
  +30% ARPU (Directional).
- #13 unnamed productivity app: personalisation questions plus a "customising
  your experience" screen beat generic demos (Directional, bundle).
- Adapty library: a loading plus personalised-plan screen lost ARPU around
  −50% in another flow.
**Seen in:** Education (Elevate), Health & Fitness, Utilities AI (Speechify).
**Trap:** A loader with nothing personal after it is pure delay. Recommend a
removal test, not a redesign.

### 20. Escape hatches for heavy steps
**When:** A heavy step (bank linking, photo access, KYC, long form) has no way
round it.
**Cross-check:** Demo mode, a sample image, "I don't know", or Skip counts.
**How:** Offer a sample or demo path next to the heavy step, with a later
prompt to do it for real.
**Evidence:** #33 TikTok delayed KYC, +25% (Directional). Otherwise Observed
(Copilot demo mode, Photoroom sample image, Opal "I don't know").
**Seen in:** Utilities (finance), Photo & Video, Productivity.
**Trap:** A demo that is better than the real product sets wrong expectations.

### 21. Sensible defaults instead of setup
**When:** Onboarding asks the user to configure options a default would cover.
**Cross-check:** Pre-filled schedules, pre-selected recommended options count.
**How:** Pick one recommended default, show it, let the user edit later.
**Evidence:** #10 Opal: one default 9–5 weekday block beat offering many
options, no figure (Anecdotal). HIG Onboarding says defer non-essential setup.
**Seen in:** Productivity, Health & Fitness (Cal AI "Balanced – Recommended").
**Trap:** A default that charges or shares data. Defaults are for settings,
not consent.

## F. The seam (onboarding → paywall)

These patterns change sign depending on where they sit in the flow. Judge them
together with the paywall, not alone.

### 22. Paywall position
**When:** Always check where the first paywall sits: screen 1, after a few
value screens, at the end of a long flow, or at the first premium action.
**Cross-check:** Compare with the bucket norm in `categories.md`.
**How:** In quiz-funnel apps, after the plan reveal; in try-first apps, right
after the first result; in tool apps with free value, at the first premium
action.
**Evidence:**
- #8 Opal: paywall after a few motivation screens, part of the 7% → 17% gain
  (Directional). The founder says position alone is worth about 10% of trial
  starts; moving it two screens earlier was worth about +10% relative, and the
  rule he draws is "as early as possible, but after the personal report".
- #71 FitnessAI: paywall moved before onboarding, paywall viewers +50%,
  install-to-trial doubled, trial-to-paid unchanged (Directional, bundled
  with a video).
- #72 Rootd: paywall moved to the start of onboarding, revenue 5×
  (Directional, before/after).
- #51 Instasize: paywall placement test, +16% premium conversions; which
  placement won is unverified (Directional).
- #20 paywall two screens earlier, "up to +15%" (Anecdotal).
- Benchmark: Adapty 2026, install-to-paid 1.35% for an onboarding paywall
  with trial vs 0.89% in-app.
**Seen in:** All buckets; see `categories.md`.
**Trap:** Position tests move trial starts and activation in opposite
directions. Read both. The other failure is reach: in one long onboarding only
40% of new users ever saw the paywall. Check what share of installs reaches
it.

### 23. Multi-step paywall or pre-paywall
**When:** The first paywall is a single dense screen that shows benefits,
trial and price at once.
**Cross-check:** A "try for free, no payment due now" screen, a separate
benefits screen or a trial-explainer screen before the price counts.
**How:** Step 1: what you get (or "we want you to try it free"). Step 2: how
the trial works. Step 3: plans and price.
**Evidence:**
- #55 Speak4Me: features first, then price, +27% conversion, +36% proceeds
  (Strong).
- #56 Stompers: benefits, trial reminder, then price, +16% (Strong, metric
  ambiguous).
- #24 Superwall aggregate: multi-page onboarding paywalls 12.41% vs 9.07%
  single-page (Directional, observational).
- #18 ASL Bloom: value screen plus trial-timeline screen, +15% trial
  conversion, +12% ARPU (Directional).
**Seen in:** Health & Fitness (Cal AI "try for free" screen), Utilities AI,
Education.
**Trap:** A trial explainer placed too early adds drop-off before the paywall
is ever seen (Adapty library). Keep it next to the price.

### 24. Trial timeline and reminder promise
**When:** A trial is offered but the paywall doesn't say when the user will be
reminded and charged.
**Cross-check:** A Today / reminder day / charge day timeline, a reminder toggle,
or a one-line reminder promise counts (a one-liner is half).
**How:** Three steps with dates, a reminder 2 days before the charge, and the
promise kept (push or email).
**Evidence:**
- #1 Blinkist: timeline plus reminder, +23% trial sign-ups, −55% complaints,
  −4% in-trial cancellations (Strong).
- #65 Shaw Academy: reminder email 3 days before trial end, +14% sales (Strong).
**Seen in:** Education, Health & Fitness (meditation), Productivity (Opal),
Utilities (finance).
**Trap:** Promising a reminder and not sending it. Check that the app asks for
notification permission or email to keep the promise.

### 25. Paywall echoes the onboarding
**When:** The user answered questions but the paywall is the same for everyone.
**Cross-check:** The goal in the headline, the user's plan or numbers on the
paywall, or segment-specific paywalls count.
**How:** Put the user's goal and one personal number on the paywall headline;
route clear segments to their own paywall.
**Evidence:**
- #22 Flirt AI: segments routed to 3 paywalls, +83% MRR, +20% trial-to-paid
  (Directional, confounded with other changes).
- #54 Daily Horoscope: country-specific paywalls, +183% trial starts (Strong;
  geo, not answers).
**Seen in:** Productivity (Opal before/after bars), Health & Fitness (Calm
"plan is ready"), Utilities AI (Speechify).
**Trap:** Echoing an answer the user doesn't remember giving feels creepy.
Echo goals, not sensitive data.

### 26. Trial structure on the first paywall
**When:** Always check: is there a trial, on which plan, for how long, opt-in or
default.
**Cross-check:** Compare with the bucket norm (AI apps and Photo & Video run
short trials; meditation runs long ones).
**How options to test:**
- Trial only on the annual plan.
- An opt-in trial toggle.
- A one-tap trial button that skips the plan screen.
- A paid longer trial next to the free one.
**Evidence:**
- #41 Moonly: trial on annual only, +39% view-to-subscription, +47% revenue
  per 100 installs (Strong).
- #45 Slopes: one-tap trial quickstart, +25% trial starts, trial-to-paid about
  flat (Strong).
- #57 Ahead: paid 30-day trial added beside the free 7-day, +7% (Strong).
- #21 Rizz God: early paywall with the trial toggle off plus a second paywall,
  +10% onboarding and +10% trial conversion (Directional).
- #52 PDF scanner: weekly plus trial 2.29% vs weekly 1.63% vs monthly 1.21%
  conversion (Directional).
**Seen in:** All buckets with an onboarding paywall.
**Trap:** Trial lengths mature at different speeds, so a trial-length test
can't be read on day 7 (see the test planner).

### 27. Second chance after the first paywall
**When:** Closing the onboarding paywall drops the user straight into the app
with no offer.
**Cross-check:** A one-time discount, a downsell to monthly, a longer trial, or
a second paywall at the end of onboarding counts.
**How:** One full-screen offer right after the onboarding paywall is closed: a
discount, a cheaper plan or a longer trial. Show it once.
**Evidence:**
- Adapty library: a second-chance discount right after the onboarding paywall
  won premium conversion about +25–30%; the same offer after the main in-app
  paywall lost about half of ARPU.
- #21 Rizz God: second paywall at the end of onboarding, part of a +10% win
  (Directional).
**Seen in:** Health & Fitness (Cal AI 80% off, Flo 44% off), Productivity (Opal
monthly downsell), Photo & Video (Picsart extra free month).
**Trap:** Training users to close the paywall. Show it only once and only
after the onboarding paywall. A discount shown when a user abandons the
store purchase sheet produced 17% of revenue across 18 apps (#75,
directional), but Apple has scrutinised it as causing unintended purchases.
Flag it as an App Review risk.

### 28. Dismiss treatment
**When:** Always note how the first paywall is closed: X, delayed X, "Skip for
now" text, equal-weight button, none.
**Cross-check:** Hard paywalls in paid-only products (VPN, finance, password
managers) are the category norm.
**How:** Make the trade-off explicit. A quieter close tends to raise ARPU and
lower activation.
**Evidence:**
- #9 Opal: a more visible close raised activation and lowered ARPU slightly,
  no figures (Anecdotal).
- #6 Duolingo: a subtle "Later" beat "discard my progress" on the sign-up wall
  (Strong; sign-up, not paywall).
**Seen in:** Equal-weight Skip (Structured), delayed close (Rizz God), no close
(Cal AI trial screen).
**Trap:** Google Play's subscription policy and consumer law expect a clear way
to dismiss; verify the current wording before recommending a hidden close.

### 29. No onboarding paywall (freemium, metered, credits)
**When:** The flow ends in the product with no paywall.
**Cross-check:** This is a valid model in AI chat, dating, some workout,
meditation and creative-tool apps. Don't recommend adding an onboarding paywall
by default.
**How:** Judge the first limit-hit or premium-action paywall instead: is the
limit visible early (a counter, an upgrade pill), and does the paywall appear
at a peak moment (just after a first workout, a boost, a generation)?
**Evidence:**
- #63 Busuu: free users limited to one language, +83% power-user conversion
  (Directional).
- #46 Slopes: trial popup when recording starts at mapped resorts, about 3×
  trial starts, conversion about −7% year on year (Directional).
**Seen in:** Productivity AI (ChatGPT, Claude, Copilot), Social & Lifestyle
(Hinge, Tinder, Bumble), Health & Fitness (Fitbod "2 more free workouts",
Finch), Photo & Video (CapCut), Media & Entertainment (Suno credits).
- Superwall reports that paywall copy mirroring the user's last action lifted
  conversion 10–15% in coaching sessions (Anecdotal, no app named).
- A "reverse trial" after the paywall is dismissed (temporary premium, no
  card) is reported to have lifted freemium conversion from 0.4% to 4.5%
  (Anecdotal; from the RevenueCat SOSA 2026 expert notes).
**Trap:** Reviewing only the first-run screens of a freemium app misses where
it actually monetises. Ask for the limit-hit screens; they're scored in
dimension 5b.

## G. Store and platform flags

### 30. Compliance flags
Flag these whenever you see them; details and links are in
`platform-rules.md`. For a full review, point to the paywall-store-compliance
skill.
- A permission pre-prompt that says "Allow", mirrors the system alert, points
  at its button, or offers a reward for allowing.
- A feature or reward gated on ATT, notifications or location.
- A required account in an app with no account-based features (5.1.1(v)).
- Social login with no privacy-preserving equivalent (4.8).
- A "free" trial without the post-trial price, length and renewal stated next
  to the button (3.1.2; Play subscriptions policy).
- Health or outcome claims with no source; store screenshots promising what
  onboarding doesn't deliver (2.3).
- A purchase reachable by a child with no parental gate in a kids app (1.3).
- A cleaner or utility showing an invented scan result or "virus" claim
  (2.3.1).
- A biometric or one-tap confirm on a "start free trial" button with no clear
  commitment step (reported as a deceptive pattern for a music-learning app,
  see `evidence.md`).
