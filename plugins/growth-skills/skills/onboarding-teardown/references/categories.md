# Onboarding norms by category

Use the same buckets as the paywall skills: RevenueCat State of Subscription
Apps (SOSA) categories. An app's bucket is its primary App Store category.
"AI app" is a tag on top of the bucket, not a bucket of its own.

When the store category and the product's function disagree (Endel is listed
under Health & Fitness but works like an audio app), use the store category
and say which norms you borrowed.

Norms come from Mobbin iOS flows viewed in October 2026 (1–7 apps per bucket)
plus published tests. They describe what top apps do, not what wins. Screen
counts are approximate.

## Quick table

| Bucket | Typical shape | Questions before paywall | First paywall | Trial | Signature screens |
|---|---|---|---|---|---|
| Health & Fitness: diet, workouts, cycle | Long quiz funnel | 10–20 | End of flow, after a numeric plan | 3 days (AI) to 1 month | Body-metric quiz, projection chart, plan reveal, health-data consent |
| Health & Fitness: meditation, sleep | Short state quiz | 3–6 | After a recommended course | 7–14 days, very transparent | Emotional opener, course recommendation, trial timeline, reminder setup |
| Education: language, brain | Lesson-first freemium | 5–8 | Soft, in-feed or contextual | 7 days | Subject pick, level or placement, daily-minutes goal, mascot |
| Education: books, self-growth | Long quiz funnel | 4–25 | End of flow | 7 days with timeline | Taste test, statement cards, future-self letter |
| Productivity: tools (todo, notes) | Account then product | 0–1 | None at first run | — | Pre-filled checklist or welcome content |
| Productivity: behaviour change (focus, habits, planners) | Quiz funnel | 4–20 | End of flow, after a report | 3–7 days | Quantified problem, bad-news/good-news reveal, contract |
| Productivity: AI assistants | Auth, age, chat | 0–2 | None (big assistants) or soft after sign-up | None or ≤3 days | Age gate, name, starter chips, upgrade pill |
| Utilities: VPN, password | Account, then hard paywall | 0 | Within the first ~12 screens | None (intro discount) or 14 days | Account and verification |
| Utilities: finance | Setup, linking, reveal | 0–6 (linking replaces questions) | After setup and the user's own data | 7 days to 1 month, timeline | Demo mode, read-only reassurance, real-data reveal |
| Utilities: AI tools, scanners, weather | Customise or try the tool | 0–6 | After the first result or at the first premium action | 3 days, weekly plans common | Live product preview, plan summary |
| Photo & Video | Try first, then paywall | 0–2 | Right after the first result | ≤4 days, toggles, weekly decoys | Use-case question, your photo → AI result |
| Media & Entertainment: music, audio | Three shapes (see below) | 0–10+ | Varies | Toggle or $0 due today | Varies |
| Social & Lifestyle: dating | Profile building | 10–25 (profile) | None in onboarding | — | Phone identity, age confirm, verification gate |
| Social & Lifestyle: astrology, plant, pet | Core inputs then payoff | 3–6 | Soft, often from inside the app | Varies | Birth data, camera-first, personalised first screen |
| Education: AI tutors, homework | Grade, then paywall, then scan | 0–2 (grade only) | Usually before the first scan | 3–7 days, weekly plans, credits | ATT first, camera ask, solve-a-problem as first value |
| Education: instrument, singing | Short quiz, account, paywall | 4–5 (instrument, level, goal, genre) | After the account, before the first lesson | 7–14 days, annual-first, family plans | Microphone pre-prompt, "do you have an instrument" |
| Education / Lifestyle: kids, parenting | Questions about the child | 5–7 | Behind a parental gate (kids); after a plan loader (parenting) | 7–14 days | Adult check before money, account first in parenting trackers |
| Utilities: phone cleaners | ATT, paywall, then scan | 0 | 3–5 screens in, before the scan | Trial toggle, weekly default | Close leads to a "free plan" that reopens the paywall at the first delete |
| Business: invoicing, scanning | Business name, paywall or first invoice | 0–3 | Split: before or after a first invoice draft | 1–14 days, tiers by business size | "Continue to your invoice" sign-up, free basic tier |

## Health & Fitness

**Diet, workouts, period tracking.** Body-metric questions (sex, age, height,
weight, goal) are the core, with ruler sliders and "you can change this later"
microcopy. The output is a numeric plan (calories, macros) the user can edit,
so the paywall has something concrete to unlock. Health-data consent comes
before the quiz where sensitive data is processed (Flo, MyFitnessPal).
Cal AI shows a "with us vs without us" weight chart, a plan with cited medical
sources, a "try for free, no payment due now" pre-paywall, a reminder promise,
then the price, and an 80%-off one-time offer on close. Workout apps can skip
the onboarding paywall entirely: Fitbod meters free workouts.
- Trust axis: results proof and medical credibility.
- Watch for: unsourced health claims, permissions asked at launch, HealthKit
  offered as a shortcut is a plus.

**Meditation and sleep.** Fewer, softer questions about state and intent. The
output is a recommended course, not numbers. Proof is research and authority.
Trials are long (7–14 days) and very transparent (Headspace timeline, Calm
reminder toggle). Reminder setup is part of activation. Several leaders
(Finch, Balance) have no onboarding paywall.
- Watch for: personalisation that lifts course starts without lifting practice
  (Headspace test #3).

## Education

Two shapes:
- **Language and brain apps** (Duolingo, Babbel, Speak, Elevate): subject pick,
  level or placement, a minutes-per-day goal with identity labels, widget or
  reminder setup, then the first lesson. Sign-up is usually required before
  the paywall because progress syncs, framed as free. The paywall is soft or
  in-feed.
- **Book-summary and self-growth apps** (Blinkist, Headway): quiz funnels with
  statement cards, a taste test of real content, sometimes a future-self letter,
  and a trial paywall with a timeline at the end.
- Level calibration is the category signature. Mascot narrators are common.
- Late converters: Education has the largest share of conversions after day 31 (23.5%, Adapty 2026), so what happens after the paywall is closed matters more here.
- Strongest public evidence of any bucket: Blinkist timeline (#1), Duolingo
  delayed sign-up (#5, #6), education loader removal (#15), survey plus lesson
  (#12), reminders in onboarding (#16).
- **AI tutors and homework helpers** (Gauth, Photomath, Brainly, Quizard,
  QANDA): 0–2 questions (grade, never subject), ATT often first, and in most
  flows the paywall comes before the first scan. QANDA lets you solve first.
  Many target under-18s while rated 4+, with no age check seen; flag that.
- **Instrument and singing apps** (flowkey, Fender Play, Simply Sing, MWM
  Piano): a 4–5 step quiz and an account before the paywall. Fender names
  finishing a first song as the aha moment (#77), yet every instrument flow
  reviewed puts the first lesson after the paywall. Simply Sing's microphone
  voice test is the only try-before-pay. Simply Piano and Yousician flows
  weren't available.

## Productivity

- **Tool-first apps** (Todoist, Bear) ask almost nothing, require or allow
  sign-up at once, and have no first-run paywall. Don't score them against quiz
  funnels.
- **Behaviour-change apps** (Opal, Me+, Structured) run 17–30-screen funnels
  with a quantified problem, emotional statements, a commitment device and an
  end-of-flow trial paywall. Opal's sequence took download-to-trial from about
  7% to 17% (#8).
- **AI assistants** (ChatGPT, Claude, Copilot) go auth → age and name → chat,
  with no onboarding paywall; monetisation is on usage limits and a persistent
  upgrade pill. Second-tier assistants and companions (Perplexity, Character
  AI, Tolan) show a soft paywall after sign-up or before the first chat.
- Permissions are core here (Screen Time, calendar, notifications). Good flows
  frame them as producing a report.

## Utilities

- **VPN and password managers**: intent is already formed, so 0 questions, an
  early account and an early hard paywall. NordVPN uses an intro discount
  instead of a trial; 1Password subscribes before sign-up.
- **Finance** (Copilot Money, Monarch, Rocket Money): value needs a bank
  connection. The best flows link before the paywall, show the user's own
  numbers, offer a demo mode, and use a trial timeline. Paid-only apps put the
  hard paywall after setup (Copilot screen ~13 of 23, Monarch ~16 of 18). Trust
  copy (read-only, "we don't sell your data", "why isn't it free") carries
  more weight than elsewhere.
- **AI tools, scanners, weather**: Speechify behaves like a quiz funnel
  (customise voice and speed on real text, plan summary, live counter, 3-day
  trial with weekly framing). Scanners show a paywall at the first premium
  action, with weekly plans. Weather apps work for free and sell extras.
- **Phone cleaners** (Cleanup, Cleaner Guru, Smart Cleaner, CleanMy®Phone):
  ATT first, 0 questions, a trial toggle and a weekly default. Three of four
  flows put photo access and the scan after the paywall; only Cleanup shows a
  found-items count before it. Closing the paywall leads to a "free plan" that
  reopens it at the first delete. Fake scan results or "virus" claims break
  App Review 2.3.1; flag broad permission asks unrelated to cleaning.
- Rule of thumb: branch on "is there a free tier?" and "how many setup
  questions?", not on the store category alone.

## Photo & Video

- The aha moment is visual and fast, so the strongest flows let the user
  produce one result before the paywall (Photoroom: pick a photo or a sample,
  background removed, then the paywall).
- 0–2 questions (use case, seller vs hobbyist).
- Short trials, trial toggles, weekly plans as decoys or real options, heavy
  discount anchoring. AI credits appear as a paywall line.
- Freemium with credits is the alternative (CapCut).
- SOSA 2026: 68.2% of Photo & Video trials are 4 days or shorter; weekly plans
  have their highest paywall share here (33%); trial-to-paid median 22.2%.

## Media & Entertainment

Music and audio split into three shapes:
- Wellness audio copies Health & Fitness (Endel: long problem quiz, permission
  reason screens, claim-led paywall with a trial toggle).
- Creator tools ask about use case or platform and sell licensing or storage
  (Epidemic Sound web checkout with $0 due today).
- AI generation is freemium with credits and no first-run paywall (Suno).
- No reviewed flow played audio before the paywall (it may be a capture
  limit).
- Benchmarks are thin: SOSA 2026 shows download-to-trial median 4.0% and the
  widest trial-to-paid spread of any bucket.

## Social & Lifestyle

- **Dating** (Hinge, Tinder, Bumble): no paywall in onboarding. The flow is
  profile building, and profile quality is the activation metric. Trust and
  safety gates (age confirmation, verification, house rules) are accepted
  friction here. Monetisation comes later via consumables and tiers at
  high-intent moments.
- **Astrology** (Co–Star): birth date, place and time are mandatory inputs,
  each on its own screen; Pro is upsold from inside the app with a "why are you
  going Pro" question first.
- **Plant and pet**: camera-first; the first identification is the activation.
- **AI dating helpers** (Rizz God, Flirt AI) do run onboarding paywalls and have
  published tests (#21, #22).
- **Kids and parenting** (Pok Pok, Duolingo ABC, Spotify Kids, Huckleberry,
  Kinedu): questions are about the child (age, name, interests) or the baby
  (birthday, naps, schedule). Kids Category apps must put purchases behind a
  parental gate (Apple 1.3): Pok Pok asks the parent's birth year, Duolingo
  ABC a spelled-number task, Spotify Kids a PIN. Parenting trackers create the
  account first because data syncs between caregivers, show a plan loader
  before the paywall, and offer longer trials (Huckleberry 14 days). The
  UK Children's Code bans nudges that push children to share data.
- Not reviewed: pet care.

## Business

Invoicing and business scanners (Invoice2go, GetPaid, Invoice Home, Genius
Scan; Invoice Simple, Joist and Square from help pages): 0–3 questions before
the paywall (business name), goals asked after it. Account timing splits three
ways: before the paywall (Invoice2go), after it (GetPaid, Genius Scan), or
after a first invoice draft, framed as "continue to your invoice" (Invoice
Home, the value-first variant). Genius Scan shows a paywall on screen 2 but
keeps a free basic option. Trials run 1–14 days with tiers by business size.
The only controlled number is Square's invoice-form redesign (#76), a
first-task result, not a paywall one. CRM-lite apps weren't reviewed.

## AI apps (tag across buckets)

- Trials are short or absent because every free session costs inference; trial
  on the yearly plan only is common.
- The paywall that matters is often the first limit hit, not the onboarding
  one. Ask for it.
- SOSA 2026: AI apps start more trials (download-to-trial 8.5% vs 5.6%; the
  report's summary mislabels this as trial-to-paid) but retain worse (annual retention 21.1% vs 30.7%) and refund more (4.2% vs
  3.5%). An onboarding that oversells capability can lift conversion and hurt
  retention.
- Photo and video AI: your input, the AI result, then the paywall. Assistants:
  starter chips and an upgrade pill. Companions: the paywall sits between
  "meet your character" and the first message.
