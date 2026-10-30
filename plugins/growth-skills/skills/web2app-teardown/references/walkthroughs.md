# Web2app quiz funnel walkthroughs (observed)

Status: six funnels attempted on 2026-10-30 in two passes.

- **Pass 1** (no consent ticked, no email entered): two funnels reached the email gate (Noom, Headway), two stopped at a health-data consent checkbox (BetterMe Wall Pilates, Simple), one stopped on screen 1 at a terms-and-cookies checkbox (Lasta), one has no reachable web quiz (Flo).
- **Pass 2** (same day; the researcher authorised ticking required consent boxes and entering a real email address on email gates, for this task only): **one funnel reached a paywall and checkout** (Simple at screen 84). Three stopped at a required first-name field (Noom at screen 23 and BetterMe at screen 53, both right after the email gate; Lasta at screen 26, before any email gate). Headway (account gate) and Flo were not re-walked.

So this file now has observed prices, plans, intro terms, a timer, a gamified discount, an exit offer and a checkout layout, but from one funnel. Treat the paywall section as one example, not a frequency.

## Method

- Date: 2026-10-30. Desktop browser, mobile viewport preset 375x812, which also sends an Android Chrome user agent. The first session dropped after three BetterMe screens. The second session resumed in the same tab.
- Region detected (pass 1): not established directly. Noom and Simple defaulted to metric units (cm, kg) and BetterMe offered cm. That fits the browser's location (Serbia/EU) but proves nothing. No currency was shown in pass 1.
- Pass 1, what we did not enter: no name, email, phone, account or payment details. We ticked no checkbox. Numbers we did enter: height 165 cm, current weight 68 kg, target weight 64 kg (Noom), height 165 cm (BetterMe, Simple; not submitted). No sign-in, no pay, subscribe or start-trial clicks. No cookie banner was accepted.
- How we answered: middle-of-the-list picks, made by a small script and checked screen by screen. Some picks were less neutral than intended: BetterMe diet "vegan", Simple diet "pescatarian" and children "live separately", Noom event "summer" and age "50s", Headway "follower" and "introvert". These answers can change later branches. Treat the screen counts as one path, not as the funnel's only length.
- Screen counts include every distinct screen: questions, interstitials, loaders, gates. A loader that stops for embedded questions counts as one screen.
- Pass 2 inputs: ticked the required consent checkboxes (BetterMe and Simple health data, Lasta terms + cookies, Lasta health data). Entered the researcher's email on three email gates (Noom, BetterMe, Simple); none of them offered a separate marketing opt-out, so there was nothing to untick (Noom and Simple bundle marketing email into the button's fine print). Extra numbers: BetterMe weight 68 kg, goal 64 kg, age 35; Simple weight 68, target 64; Lasta height 165 cm, weight 68, target 64, age 35. Never entered: name, phone, password, payment details. We ticked no payment-terms checkbox and clicked no pay, wallet or start-trial button. On Simple we tapped a gift box and "Claim my 75% off" to dismiss the discount modal (this applies a discount; it charges nothing).
- **Name gates.** Noom, BetterMe and Lasta ask for a required first name with no skip. We don't enter names, so each of those walks stops at the name screen.
- Region and currency, pass 2: Noom priced in EUR with VAT and offered Serbian regions in the billing address. Simple priced in USD. Lasta defaulted height to inches but weight to kg.
- The browser pane was hidden for most of pass 2. Hidden tabs throttle animations, so several loaders stalled until a screenshot was taken. Loader durations below are rough.
- Tier for everything here: **observed**. Each walk is one session on one variant. These funnels are heavily A/B tested, so another visit may get a different flow.
- Screens are described in our own words. Label quotes are a few words at most.

## 1. BetterMe Wall Pilates (pass 1 stopped at screen 38, health-data checkbox; pass 2 stopped at screen 53, required name)

- Start URL: `https://betterme-wallpilates.com/en/first-page-generated?flow=1416`
- It redirected straight to a different variant: `https://betterme-wallpilates.com/first-page-brand-palette?flow=6122`. The flow ID changed from 1416 to 6122 and the page template from "first-page-generated" to "first-page-brand-palette". An earlier session in the same browser had reached flow 6122 from BetterMe's corporate site ("get started" slider button, `utm_source=corpsite`), so the browser may have kept that assignment (sticky cookie or bucketing). We can't tell whether a fresh visitor gets flow 1416.
- After the first answer the quiz runs at `/onboarding?flow=6122&order=<uuid>`, one URL for every screen.

Screens:

1. **Landing / age gate as the first question.** Brand header, a challenge headline promising a visible change by December if you start "this Monday", and four photo cards of women by age band (18–29, 30–39, 40–49, 50+). Tapping a card is the first answer. Small print under the cards says that choosing an age and continuing means agreeing to the Terms of Service and Privacy Policy (browsewrap consent attached to a quiz answer). There is a floating help button. No cookie banner was visible, though a OneTrust preference centre is in the DOM and linked in the footer ("e-Privacy Settings").
2. **Social-proof interstitial, personalised by the previous answer.** It claims over 1.7 million women "in their 30s" have tried the challenge (echoing the age band from screen 1), then a press-logo strip and CONTINUE. No progress bar.
3. **Tried Wall Pilates before?** Yes/No, auto-advance. From here the header shows the section title and a **segmented progress bar with 5 segments**, one per section: My Profile, Activity, Lifestyle & Habits, Nutrition, Almost There. (The earlier partial write-up said 6. The DOM and a screenshot both show 5.)
4. Interstitial: what Wall Pilates is, at home, no equipment.
5. Main goal (lose weight / maintain and get fit).
6. Interstitial: a personalised challenge, no exhausting gym.
7. Secondary goals, multi-select with a "None of the above" option and NEXT STEP.
8. Body build (four image options).
9. Interstitial: small steps, "not another Monday promise".
10. Dream body (four image options).
11. How your weight usually changes.
12. When you were last in your best shape.
13. Interstitial: 10–20 minutes a day.
14. Exercise frequency (section 2, Activity).
15. Target zones, multi-select.
16. Interstitial that **echoes the chosen zone** ("toned chest at home").
17. Flexibility. 18. Walking frequency. 19. How you feel on stairs.
20. Sensitive back or knees, multi-select.
21. Interstitial that **echoes the answer** (gentle exercises for knees).
22. Work schedule (section 3, Lifestyle & Habits). 23. Typical day. 24. Energy levels.
25. Interstitial that **echoes the answer** (the post-lunch slump).
26. Water intake. 27. Sleep hours.
28–30. Breakfast, lunch and dinner times (section 4, Nutrition).
31. Diet type, grouped into "with meat" and "without meat".
32. Interstitial: **personalised meal-plan preview** with three meals, calories and prep minutes.
33. Eating habits, multi-select. 34. Cravings, multi-select.
35. Interstitial: **expert authority**, three named instructors and a dietitian with credentials.
36. Life events that affected your fitness, multi-select (includes divorce, finances, Covid) (section 5, Almost There).
37. Interstitial: reassurance ("we know how to help").
38. **Height (ft/cm), with an unticked checkbox consenting to BetterMe processing health onboarding data.** NEXT STEP stays disabled until the box is ticked, even with a valid height. **Walk stopped here.**

Pass 1 did not reach: weight and target weight, loaders, projection chart, email gate, paywall, timers.

Pass 2, from screen 38 (consent ticked, height 165 cm):

39. Current weight. An inline result appears under the field: BMI 25 "considered normal" plus an upbeat line. (The exact BMI is 24.98; Simple and Lasta call the same numbers "overweight".)
40. Goal weight. Inline: "realistic goal", lose 6% of your weight, and a claim that 4 kg a month is safe and healthy.
41. Exact age (number field), with a one-line reason (older people carry more body fat at the same BMI).
42. **Loader** "analysing your answers": one progress bar per quiz section (the same five sections), an "app of the day" badge with a date, a rating. About 20 s, no questions inside.
43. **Wellness profile**: BMI on a coloured scale with the user's marker, then four labels derived from answers (body type, lifestyle, fitness level, metabolism). CONTINUE.
44. Upcoming event (vacation, wedding, reunion...; "no events" is an option).
45. Event date on a calendar.
46. **Projection chart**: "we estimate you could be 64 kg by December 11, 2026", "just in time for the" event, a line from 68 to 64 kg with the event pinned on the timeline and an asterisk citing user data. It echoes three answers: current weight, goal weight, event.
47. Motivation, multi-select. 48. Interstitial: 15 minutes a day.
49. Confidence question that **repeats the projected date** ("how confident are you in getting in shape by December 11?").
50. Trust screen: three awards with years (2022, 2022, 2025).
51. **Loader** "creating your personalised challenge" with a review carousel and "over 2 million women" (screen 2 said 1.7 million). About 8 s.
52. **Email gate**: "enter your email to get your personalised challenge". One field, CONTINUE, a privacy line. No marketing checkbox, no account wording, no skip.
53. **First name** ("what's your name?"), CONTINUE disabled until filled, no skip. **Walk stopped here** (we don't enter names).

Counts: 52 screens to the email gate, paywall beyond screen 53. Two loaders in screens 39–53, both after the body measurements. The plan reveal (profile + projection) comes before the email gate, unlike Noom where the projection is held behind the email.

Also seen: the cookie preference centre in the page had targeting, performance and functional switches set to on by default (the banner itself never showed).

Counts to the stop: 38 screens. Roughly 25 questions and 12 interstitials, about one interstitial per two questions. Question types: single-select text rows (auto-advance), image cards, multi-select with "None" and a NEXT STEP button, one number input. No loader appeared in the first 38 screens.

Footer on every screen: FAQ, Terms, Privacy, Subscription Policy, Money-Back Policy, e-Privacy Settings, support email. The money-back and subscription policies are linked from screen 1, before any price.

Reviewer flags:
- Terms consent comes from tapping an age card (browsewrap), not from a separate checkbox.
- The health-data consent is a separate, unticked checkbox (explicit opt-in, as GDPR asks for health data). The quiz can't go on without it, so the consent is a hard condition of using the quiz.
- The life-events question asks about divorce and financial trouble with no stated reason.

## 2. Noom (email gate at screen 21; pass 2 stopped at screen 23, required name)

- Start URL: `https://www.noom.com/`. On a mobile viewport the homepage is itself the first quiz screen, with no marketing page in front. Continue leads to `/lp/survey/weightLossGoal`, then `/ps/main-survey`, then a single-page app under `/survey/<question-id>` (each question has its own readable path, e.g. `/survey/basicHeight`, `/survey/building`, `/survey/email`).
- No cookie banner appeared. Footer links (on the homepage only): Cookie Policy, HIPAA Notice, Terms, Privacy. Metric units by default.

Screens:

1. **Homepage slide**: food photo, a mindful-eating headline, Continue.
2. Weight-loss goal, in kg bands, plus "maintain" and "haven't decided". Section header "Demographic profile" with a **segmented progress bar of 8 dotted sections**.
3. Sex assigned at birth, with a one-line reason (hormones). 4. Gender identity (separate question, Next button).
5. Pregnant? If you answer Yes, a notice says the programme isn't designed for pregnancy and recommends seeing a doctor.
6. Age by decade (20s–80s+).
7. Height (number). 8. Current weight (number), with a "we don't mean to pry" line. **If BMI is under 18.5, a modal says the programme isn't for underweight people, and to continue you must read a liability waiver.** (We saw this once by accident, when an empty weight was submitted; with 68 kg it went straight through.)
9. Health conditions, multi-select with None. 10. Diabetes diagnosis. 11. Eating-disorder diagnosis.
12. **Social proof**: "you're not alone", a large exact count of people helped, with an asterisk defining "lost weight" as at least 2% of body weight (as of 2021).
13. Ideal weight (number), with a note that Noom will **predict the date** you reach it and a typical weekly loss range.
14. Interstitial: behaviour change rather than diets, citing a study percentage. "Got it!" button.
15. Plan focus (nutrition / activity / habits). Section header becomes "Weight loss goals".
16. Upcoming event (vacation, wedding, summer...). 17. Event date picker, with **Skip**.
18. Preferred pace (fast / slow and steady / in between).
19. Interstitial: a testimonial quote with first name, plus the typical-loss disclaimer.
20. **Loader** ("building"): a headline claiming twice the weight loss compared with going alone, a percentage counter and staged labels (analysing responses → calculating weight-loss pace → preparing results). About 12 seconds, no input. No progress bar.
21. **Email gate**: "enter your email to see when Noom can help you reach 64 kg" (it echoes the target weight). One email field, a "See my result" button, and a note that the results copy is emailed. The fine print says that clicking the button accepts the Terms and Privacy Policy and that you may receive marketing emails (unsubscribe later). **No skip and no back-to-results option. Walk stopped here.**

Counts: 21 screens to the email gate. About 15 questions, 3 interstitials, 1 loader. No paywall, price or timer before the gate. The projection ("when you'll reach X kg") is promised but held behind the email.

Reviewer flags:
- Email is asked before the result the user was promised. The result works as the bait.
- Marketing email consent is bundled into the same click (soft opt-in by browsewrap).
- Safety screening is built into the quiz: pregnancy, eating disorder, BMI under 18.5 with a liability waiver. That's good practice, and it doubles as liability cover.
- The social-proof count is exact and has a disclaimer, but the success definition (2% loss) is weak and the date is old (2021).
- The path was short because we answered "maintain weight". Other goals may branch longer, and Noom is known for much more of the quiz after the email.

### Noom pass 2: after the email gate

22. **First projection**: "the last weight loss program you'll ever need", "we predict you'll be 64 kg by 14 Jan" with an animated date, a line chart from 68 to 64 kg (Nov → Jan), "conservatively", and "tell us more so we can see if you can reach your goal sooner". A testimonial with a first name and kg lost, the 1–2 lb/week disclaimer, press logos.
23. **First name**, required, no skip. **Walk stopped here** (we don't enter names).

Reviewer flags (pass 2):
- The name gate sits right after the email gate, so personal data is collected well before any price.
- The projection invites more answers to reach the goal "sooner", which sets up date changes later in the funnel (not observed past the name).

## 3. Simple (pass 1 stopped at screen 20, health-data checkbox; pass 2 reached the paywall at screen 84 and the checkout sheet)

- Start URL: `https://simple.life/` → "Get started" → `https://simple.life/survey/?utm_source=simple_landing&lang=en` → `/survey/main` → `/survey/main/ob/age`. Questions then run under `/survey/main/ob/<id>` and, after the goal question, `/survey/f/ob/<id>`.
- A OneTrust banner script is on the landing page, but no banner was visible to us. Metric units.

Screens:

1. **Splash loader before any answer**: a "see how fast you can hit your goals" headline, an animated dot ring, "please don't close this page", "analysing your profile" and a results-may-vary disclaimer. It works as a load screen dressed as analysis.
2. **Age as the first question**: four photo cards for 40–49, 50–59, 60–69 and 70–80. Ages 18–39 get only a small text link underneath. The funnel is aimed at 40+.
3. Sex (with "prefer not to say").
4. Heard of intermittent fasting? 5. Interstitial: fasting explained simply.
6. Weight-loss focus in kg bands, plus maintain and "not sure".
7. Meals per day. From here a "My profile" header and a **single continuous progress bar** (about 70% full by screen 20).
8. Carbs frequency. 9. Habits, multi-select ("no judgment" sub-line).
10. Dietary pattern. 11. Interstitial: "guiding you with care", we'll fit your diet.
12. Target zones. 13. Sleep hours. 14. Sleep problems (includes hot flushes, again pointing at a 40+ female audience).
15. Interstitial: better sleep makes weight loss easier.
16. Water intake. 17. Lifestyle (sitting / moving / on feet). 18. Children.
19. Interstitial: a testimonial with first name, pounds lost and a photo.
20. **Height (cm/ft), with an unticked checkbox consenting to processing health data such as height and weight.** With a valid height and the box unticked, Next stays disabled, and an inline error asks you to accept the Privacy Policy. **Walk stopped here.**

Counts to the stop: 20 screens. About 14 questions, 4 interstitials, 1 splash loader. No terms consent on the first screen that we could see (no browsewrap text on the age screen).

Reviewer flags:
- Health-data consent is a hard gate (the same pattern as BetterMe), placed on the first body-measurement question.
- The opening "analysing your profile" loader runs before any answer, so the analysis it claims is theatre.
- The age picker hides the younger band as a link. That's segmentation by design; the reviewer note is that 18–39 users get a weaker option.

### Simple pass 2: from the height screen to checkout

(The browser tab title on every screen reads "Create Your Account", but no screen asked for a password or created an account.)

21. Current weight. Inline: BMI 25 "considered overweight" and a we'll-help line.
22. Goal weight. Inline: "Realistic goal!" with a 5%-loss health claim attributed to the American Heart Association.
23. **Loader** "preliminary processing" (target weight, Simple users).
24. **Starting-point screen**: BMI scale with the user's marker and a list of health risks of an unhealthy BMI.
25. Interstitial: "now let's estimate when you'll reach your goal", "see if you can hit it even sooner".
26. Upcoming event (vacation, wedding, birthday...). 27. Event date, **skippable** (we skipped).
28–30. Three questions whose sub-lines **echo the age band and sex** ("as a woman in her 40s", "in your 40s").
31–36. Fruit and veg, hunger, energy, each followed by a reassuring interstitial.
37–42. **Six 1–5 Likert statements** (emotional eating, falling back, people around me, multitasking, clearing the plate, unhealthy cycles).
43. Loader "analysing your answers".
44. **"Your weight-loss blockers"**: three blockers with percentages (poor sleep, emotional eating, stress), derived from mid-scale answers.
45–49. Motivation: how I'd like to feel, what I'd like to do, how I see myself at my happy weight, biggest drive.
50. Current priorities (lose weight / tone up / strength).
51. Weight gain from life events. 52. Skin concerns. 53. Interstitial: fasting and skin.
54. **Weight-loss programmes tried, naming competitors** (Noom, WW, Nutrisystem, Jenny Craig). 55. Methods tried.
56. "Almost done!" interstitial ("let's finish this").
57–63. **Health and safety block**: diagnosed conditions, eating disorder, medications, two supplement questions (familiarity, what matters when choosing one), pregnancy or breastfeeding, menopause. Each says the information is for your safety.
64. Interstitial. 65. **Social proof**: "join 1.8M happy women".
66–68. Motivation over time, readiness, "what makes you uncertain".
69. Loader with a statistic ("the #1 reason women give up is starting too big").
70. **"Meet your future self"**: now vs goal, weight 68 → 64 kg, **body fat 32%+ → 14–20%**, an energy bar. (A 4 kg loss doesn't move body fat by that much; reviewer flag.)
71. Confidence about "hitting 64 kg by January 30th, 2027" (**first date reveal**).
72–76. Cravings timing, snacking triggers, what else to explore, meal prep, weekend break from fasting.
77. "Your plan is ready!" plus a pace question. 78. "Great job!" 79. Trust interstitial: the yo-yo effect with two cited statistics.
80. **Email gate**: "your action plan is ready", one email field, "See my plan". Fine print: submitting the email may bring marketing emails (unsubscribe any time), and use is bound by the terms and privacy policy. No marketing checkbox, no skip, no account wording.
81. **Loader with an embedded question**: eight "analysing" labels, four section bars, "trusted by over 141,562 clients", a review carousel, and a three-option question (morning lark / night owl / not sure).
82. **Projection**: "we predict you'll hit 64 kg by February 4" with a chart and four benefit bullets. "Get my plan". (Screen 71 and the paywall say January 30.)
83. **Progress teaser**: "just 10 minutes a day", milestones on dated days ("by Nov 2 you'll feel the difference, by Nov 9 you'll see it, by Nov 16 others will notice"), "people joined today". Auto-advances.
84. **Paywall** (`/survey/plan/o`).

Counts: 80 screens to the email gate, 84 to the paywall. Five loaders in the whole walk (splash, 23, 43, 69, 81). Social-proof counts on one path: 1.8M women (screen 65), 141,562 clients (loader), 15+ million users (paywall).

**Paywall, observed 2026-10-30, USD:**
- On arrival a **"Pick a gift, unlock up to 75% off!" modal** covers the page with three gift boxes. Every box carries the same 75% (the page text lists "75%" three times before any tap). Tapping one opens it to 75%, then a "Jackpot! You unlocked the highest discount" step, both with "Claim my 75% off · applied automatically at checkout".
- Then the page: a **sticky header "75% discount reserved for: 10:00"** counting down with a GET MY PLAN button; headline "64 kg by January 30" with a chart (68 kg now → goal → "maintain weight"; "for illustrative purposes only"); "Grab your Personal Plan before it's gone!"; a red bar "This offer ends in 09:59 min".
- **Three plan cards, 4-week pre-selected** (the middle one); the 12-week card wears the "MOST POPULAR" badge. Prices with the discount applied:
  - 1-week: ~~$22~~ $5.19; per day ~~$3.14~~ **$0.74**.
  - 4-week (pre-selected): ~~$44~~ $9.99, "75% OFF"; per day ~~$1.57~~ **$0.35**.
  - 12-week: ~~$79~~ $19.99, "75% OFF"; per day ~~$0.94~~ **$0.23**.
  The per-day price sits in a large tag on the right of each card and is the biggest number on the card; the actual charge is small grey text under the plan name. Before the gift, the same cards showed the full prices ($22 / $44 / $79) with per-day $3.14 / $1.57 / $0.94.
- Under the cards: "people using Simple for 12 weeks lose twice as much weight as for 4 weeks" (own user research, 2023); **"Get my plan"**; "I have Promo code".
- **Terms under the button**, small grey: you'll pay $9.99 today for 4 weeks, then **$44 every 4 weeks** until you cancel; cancel before November 27th, 2026 to stop future charges; payment details are kept for future payments. The renewal is 4.4 times the first charge.
- Further down: 15+ million users, 4.8 rating on both stores, "over 351,000 5-star ratings", a before/after comparison (restrictive diets vs Simple plan) that **echoes the event answer** ("lose weight for your birthday"), a second "-75% discount reserved for" badge, three named reviews with kg results, then the plan cards and terms repeated, then a **30-day money-back guarantee** block at the very bottom, and "guaranteed safe checkout".
- **Checkout sheet** (opens from "Get my plan", bottom sheet over the paywall, nothing charged): a confetti banner "You save 77% OFF" (the card said 75%), "4-WEEK PLAN ~~$44~~ $9.99", the renewal terms again as "by tapping Continue you agree to pay...", an **unticked checkbox "I agree to the above terms of the autorenewing subscription"**, then **"Continue with Google Pay" first, "Continue with PayPal" second, "Credit Card" as a collapsed row** with Visa/Mastercard/Amex/Maestro logos, and the 30-day money-back line with a badge. The wallet buttons look greyed until the box is ticked. (We ticked nothing. Google Pay probably appears because the viewport sends an Android user agent; an iPhone would likely see Apple Pay. Not observed.)
- **Exit offer**: closing the checkout sheet (X) triggers confetti and a modal **"You've unlocked a special 80% discount!"** with a chart (your weight under "regular diets" vs "Simple plan" over the first month), a Columbia University statistic about regaining weight, and "Get my discount". The header changes to "80% discount reserved". The card prices stayed $5.19 / $9.99 / $19.99 while the badges read "80% OFF". We didn't accept.
- **Back button**: browser back from the paywall goes to the progress teaser, which auto-forwards to the paywall again. On that re-entry the timer had **reset to 10:00**, the discount was back to 75%, and the gift modal didn't reappear.
- **Reload**: reloading the paywall URL kept the running timer (no reset). So the countdown survives a reload but resets when the paywall is entered again through the funnel.

Reviewer flags (pass 2):
- The "pick a gift" is rigged: all three boxes hold the same 75%. Then "highest discount" and later 80% escalate with no change in the price.
- The countdown resets on re-entry, so the urgency is not real.
- Per-day prices are the hero numbers; the renewal at $44 every 4 weeks is in small grey text under the button.
- Pre-selecting the middle plan while badging the longest plan "most popular" splits the anchor.
- The savings figure differs between the card (75%), the checkout sheet (77%) and the exit offer (80%).
- Three different user counts on one path (1.8M, 141,562, 15+ million).
- The projected date moves between screens (January 30, 2027 → February 4 → January 30).
- The terms checkbox on the checkout sheet is good practice: explicit consent to auto-renewal before the wallet buttons work.
- Asks about supplements inside a health-and-safety block, which reads as a lead-in to a supplement upsell.

## 4. Headway (reached the email gate at screen 37)

- Start URL: `https://makeheadway.com/` → "Get started" (`/onboarding/start?utm_source=makeheadway1&...`) → `/onboarding/self-growth/landing` → `/onboarding/self-growth/social-proof` → `/onboarding/self-growth/quiz` (one URL for every question after that). Some homepage buttons carry a `test_home=title` parameter, a visible A/B test on the homepage.
- No cookie banner appeared. Footer on every screen: company address in Cyprus, Terms, Privacy, Subscription policy, a "Do not sell or share my personal information" link, support email.

Screens:

1. **Landing / age as the first question**: a headline promising you'll be the most interesting person in the room, a "3-minute quiz" label, four age cards (18–24 to 45+). Small print says that choosing Continue, an age or a gender means agreeing to the Terms, Privacy and Cookie Policy, **including tracking such as the Meta Pixel** (browsewrap consent to ad tracking attached to a quiz answer).
2. **Social proof**: 55M+ downloads, a "mentioned in" press strip, Continue. (The homepage says 60M+: the two pages don't match.)
3. Gender (emoji cards). Section header "Profile".
4. Areas to improve, multi-select of 12 chips, with a note that the choice won't limit you.
5. Interstitial: big ideas in 15 minutes.
6. Whose success inspires you: a multi-select of celebrities.
7. Big-picture or detail-oriented.
8–12. A **run of 5-point emoji Likert statements** (thumbs down to thumbs up, auto-advance) on self-doubt, decisiveness, inner strength; plus leader/follower.
13. Extrovert / introvert (section "Personality").
14–19. More Likert statements, including time management, relationship boundaries, **satisfaction with your sex life** and understanding your body and desires.
20–25. Section "Patterns": celebrate or critique wins, do you like your job, work-life balance, professional potential, **feelings about your finances**, worrying you're not good enough.
26. Attribution: did you hear about Headway from a coach or mentor?
27–31. **Five book cards, one at a time, each with a Yes/No** ("does this book interest you?"), like a swipe deck.
32. Specific reason for self-growth (promotion, parenthood, life transition...).
33. Daily goal: 5 / 10 / 15 / 20+ minutes a day.
34. Preferred learning format (reading, listening, video...).
35. **Loader with embedded questions**: "crafting your learning experience", four checklist stages (goals, growth areas, content, challenges) and a percentage bar. **The bar stops at 49% and a modal asks a Yes/No question** ("to move forward, specify..."). This happened four times, with one question per stage. App-store-style reviews rotate under the loader, plus the 55M+ claim.
36. **Ready screen**: "your learning experience is up and running", the four stages ticked off, Continue.
37. **Email gate**: "achieve your goals", enter your email to create a personal account. One email field, Continue, and browsewrap text saying that continuing means agreeing to the Terms, Privacy and Subscription Policy. **No skip. Walk stopped here.**

Counts: 37 screens to the email gate. About 31 questions (17 of them Likert), 2 interstitials, 1 loader with 4 embedded questions, 1 ready screen. No projection chart, price or timer before the gate.

Reviewer flags:
- Browsewrap consent to ad-pixel tracking on the first tap.
- Sensitive questions (sex life, finances, self-worth) that a book-summary app has no obvious need for. They read as commitment and self-disclosure devices.
- The loader is a fake progress bar: it stalls until you answer, and the "crafting" is cosmetic.
- The download count differs between the homepage (60M+) and the quiz (55M+).
- The "3-minute quiz" label promises 3 minutes for 37 screens. Probably achievable, but tight.
- The email gate says "create a personal account", which frames the email as an account rather than as a lead capture.

## 5. Lasta (pass 1 stopped at screen 1, terms + cookie checkbox; pass 2 stopped at screen 26, required name)

- Start URL: `https://lasta.app/` → "Try now" → `https://lasta.app/quiz/en/cN3isSy7dGll787O?utm_source=homepage&utm_medium=button&utm_campaign=homepage`. The homepage links several separate quiz funnels by ID (weight loss, Tai Chi walking `TCW-...`, indoor walking, calisthenics), each with its own UTM campaign.
- Screen 1: a "28-day wellness & workout plan" headline. **Above the fold it says plainly that the quiz leads to a paid auto-renewing subscription** and that results are informational, not medical advice. Below: a "3-minute quiz" label, two photo cards (male / female, older-looking models), a language switcher, and an **unticked checkbox** agreeing to the Terms and Privacy Policy and consenting to cookies under the Cookie Policy. Tapping a gender card without ticking shows an inline error asking you to accept the terms. **Walk stopped here.**

Counts: 1 screen.

Reviewer flags:
- This is the most explicit disclosure of the six: subscription, auto-renewal and not medical advice, all on screen 1.
- Cookie consent is bundled with terms acceptance in one checkbox, and the checkbox is a hard gate. Under GDPR, bundled, forced cookie consent is a known problem (consent has to be separable and refusable).

### Lasta pass 2 (checkbox ticked, "Female" card)

Quiz URLs: `/quiz/en/quiz/<id>`, one per screen. From screen 3 a header shows a numeric counter ("1 / 21") and a bar.

2. "Start your wellness journey today!" Continue.
3. Primary goal, multi-select (counter 1/21). 4. Interstitial: one app, multiple wellness goals.
5. Physical build. 6. Target body type. 7. Interstitial.
8. Tried workout programmes before (the URL still says "fasting-experience", a leftover from another funnel). 9. Interstitial.
10. Fitness experience. 11. Flexibility. 12. Exercise frequency. 13. Stairs. 14. Walking.
15. Sensitive back, knees or elbows, with "None of the above". 16. Interstitial.
17. Workload. 18. Typical day. 19. Sleep. 20. Habits, multi-select. 21. Interstitial.
22. **Height**, defaulting to inches (ft/in) with a cm toggle, a BMI explainer box, and **a second, separate unticked checkbox consenting to processing health information (height, weight, age)**. Continue shows an error until ticked.
23. Current weight (kg by default). Inline: BMI 25.0 "commonly classified as overweight", plus "general information, not medical advice".
24. Target weight. Inline: "steady progress", lose 6%, the same disclaimer.
25. Exact age.
26. **First name** ("2–20" characters), Continue does nothing while empty, no skip (counter 19/21). **Walk stopped here.**

Counts: 26 screens to the name gate, no email gate yet, no loader yet, no projection yet. The counter says 21 questions; interstitials aren't counted in it.

Reviewer flags (pass 2):
- The most cautious copy of the five: every result line carries a not-medical-advice disclaimer, and BMI is described as a screening measure.
- Two consent checkboxes (terms + cookies on screen 1, health data on screen 22).
- Imperial default for height but metric default for weight on the same visit.

## 6. Flo (no web quiz reached)

- `https://flo.health/`: the homepage's main "Try Flo today" button goes to an AppsFlyer OneLink (`flohealth.onelink.me/...`), an app-store deep link, not a web quiz. A "Quizzes" nav item goes to content quizzes.
- `https://app.flo.health/` is the web-subscription host (Flo's help centre says web subscriptions are bought there). On load it showed only a cookie notice (Usercentrics) whose sole button is "Got it", with no reject or settings option. The page behind it stayed blank. `/onboarding` redirected back to the root. We didn't accept the notice, so nothing was walked.
- Reviewer flag: an accept-only cookie notice (no reject) on an EU-reachable health app.
- Re-run idea: Flo's web funnel is probably reached through paid-ad landing URLs that carry a funnel ID. Find one through an ad library (Meta Ad Library) and walk it, accepting the cookie notice only with the researcher's approval.

## Cross-funnel patterns (n = 6 attempted; 5 with a web quiz; tier: observed)

All counts are from one walk per funnel on 2026-10-30. Quiz-side counts use the 5 funnels with a web quiz (Headway counted from pass 1 only). The paywall and checkout notes come from **one funnel** (Simple); treat them as an example, not a frequency.

Where each walk ended:
- Email gate reached: 4 of 5 (Noom at screen 21, Headway 37, BetterMe 52, Simple 80). Lasta had no email gate in its first 26 screens.
- Passed the email gate: 3 (Noom, BetterMe, Simple; Headway's gate creates an account, so not attempted).
- **First-name field required, no skip: 3 of 5** (Noom right after the email, BetterMe right after the email, Lasta before any email). Only Simple went from email to paywall without asking for a name.
- Paywall reached: 1 of 5 (Simple at screen 84).
- Price before any personal data: 0 of 5. Nothing about price or plan appears before the email gate in any funnel (Lasta discloses "paid auto-renewing subscription" on screen 1 but shows no price).

First screen:
- 4 of 5 quizzes open with a demographic answer as the first tap, no "start quiz" button: age cards (BetterMe, Simple, Headway), gender cards (Lasta). Noom opens with one brand slide and then the goal question.
- 3 of 5 attach consent to the first screen: browsewrap on tapping an answer (BetterMe, Headway, which also covers Meta Pixel tracking) or a hard checkbox (Lasta).
- 2 of 5 show a "3-minute quiz" label (Headway, Lasta). BetterMe frames the funnel as a challenge with a start date instead.
- 1 of 5 discloses the paid auto-renewing subscription on screen 1 (Lasta).

Social proof and authority:
- 5 of 5 show a user count inside the quiz or on the paywall. 3 funnels showed **different counts on the same path**: BetterMe 1.7M then 2M; Simple 1.8M, 141,562 and 15+ million; Headway 55M+ in the quiz vs 60M+ on the homepage.
- 3 of 5 use press-logo strips or award screens (BetterMe, Headway, Noom; Simple on its landing page).
- 4 of 5 use named testimonials or reviews (Noom, Simple, Headway, BetterMe).
- 1 of 5 has an expert-credentials screen (BetterMe).
- Inline BMI verdicts on the weight screen: 3 of 5 (BetterMe, Simple, Lasta). For the same 165 cm / 68 kg (BMI 24.98) BetterMe said "normal" and Simple and Lasta said "overweight".

Interstitials and echoing:
- 5 of 5 put info screens between questions.
- Answer echoing: 4 of 5. BetterMe echoes answers in interstitials and pins the chosen event on the projection; Simple echoes age band and sex in question sub-lines and the event on the paywall; Noom echoes target weight on the email gate; Headway echoes nothing specific.
- Teach-by-asking blocks (a question followed by an explainer that names the concept): 1 of 5 seen (Simple's answer → reassurance pairs).
- A derived "profile" or "diagnosis" screen built from answers: 3 of 5 seen (BetterMe wellness profile, Simple starting point and "weight-loss blockers" with percentages, Headway ready screen).

Loaders:
- 4 of 5 have at least one "analysing / building" loader (Lasta none in 26 screens). Simple had five on one path, BetterMe two, Noom one before the email gate, Headway one.
- **Loaders with questions inside: 2 of 4** (Headway four Yes/No, Simple one three-option question). The progress stops until you answer.
- A loader sits right before the email gate in 4 of 4 funnels that have one (Noom, Headway, BetterMe, Simple).

Plan reveal and projection:
- A dated weight projection ("X kg by date"): 3 of 4 funnels that ask for weight (Noom, BetterMe, Simple). Lasta not reached.
- Placement: before the email gate in BetterMe (screen 46); promised before the gate and shown right after it in Noom (screen 22); a date inside a question before the gate (screen 71) and the chart after it in Simple.
- **The date moves**: Simple shows January 30, then February 4, then January 30 again. Noom's first projection invites more answers to reach the goal "sooner" (later updates not observed).
- The projection is repeated on the paywall: Simple ("64 kg by January 30" with the chart).
- An event (wedding, reunion, birthday) is asked for in 3 of 5 (Noom, BetterMe, Simple) and comes back later in 2 of them: BetterMe pins it on the projection chart, Simple names it in paywall copy ("lose weight for your birthday"). Noom showed no tie on our path.

Progress bars:
- 5 of 5 have one, never on the first screen or on interstitials/loaders. Segmented by named section: BetterMe (5), Noom (8 dotted), Headway (section labels). Continuous: Simple. Numeric counter: Lasta ("19 / 21", interstitials not counted).

Question types seen (5 walked funnels):
- Single-select text rows with auto-advance: 5 of 5.
- Image or photo cards: 4 of 5.
- Multi-select with "None of the above" and a Next button: 5 of 5.
- Number inputs (height, weight, target, age): 4 of 5 (Headway none). Exact age as a number: 2 (BetterMe, Lasta).
- Likert scales: 2 of 5 (Headway 17 emoji items, Simple six 1–5 items).
- Swipe-deck content cards: 1 (Headway). Date picker with Skip: 2 (Noom, Simple).
- Competitor names as answer options: 1 (Simple: Noom, WW, Nutrisystem, Jenny Craig).
- Attribution ("where did you hear about us"): 1 (Headway mid-quiz).

Data-protection mechanics:
- **Health-data consent as a separate, unticked, mandatory checkbox on the first body-measurement screen: 3 of 4** funnels that ask for measurements (BetterMe, Simple, Lasta). Noom asks for height and weight with no checkbox.
- Medical safety screens: 2 of 5 (Noom: pregnancy, eating disorder, BMI under 18.5 waiver; Simple: conditions, eating disorder, medications, pregnancy or breastfeeding, menopause).
- Sensitive, off-topic questions (sex life, finances, divorce): 2 of 5 (Headway, BetterMe).
- Cookie handling: no visible banner on 4 of 5 quiz sites. One bundled forced checkbox (Lasta). One accept-only notice (Flo web host). BetterMe's hidden preference centre had all optional categories on.

Email gate (4 reached):
- 4 of 4: one field, no skip.
- Marketing consent bundled into the button's fine print: 2 of 4 (Noom, Simple). No separate opt-out checkbox anywhere (0 of 4).
- Account framing: 1 of 4 (Headway). Note Simple's browser-tab title says "Create Your Account" throughout, though no screen does.
- 4 of 4 come right after a loader or "ready" moment, and the email is the price of seeing the result or plan.

Time pressure:
- Before the paywall: 0 of 5 (no timers, countdowns or "reserved" messages anywhere in the quizzes).
- On the paywall: Simple has a countdown (10:00, sticky header + red bar, survives a reload, **resets when the paywall is re-entered**).

**Paywall (Simple, observed 2026-10-30):**
- Structure: a long single page (plans, terms, proof, reviews, plans again, guarantee) with a checkout bottom sheet.
- Offer type: 1/4/12-week plans with an intro discount (first period discounted, then full price).
- Plans shown: 3. The middle plan (4-week) is pre-selected while the longest plan carries "most popular".
- Price framing: **per-day is the hero number** ($0.35/day); the actual charge ($9.99) is small and grey; full prices struck through.
- Renewal gap: $9.99 today, then $44 every 4 weeks (4.4x).
- Renewal terms: small grey text under the CTA, and again in the checkout sheet next to a checkbox.
- Gamified discount: a three-gift "unlock up to 75% off" picker where every box holds 75%.
- Guarantee: 30-day money-back at the bottom of the page and in the checkout sheet.
- Social proof: user counts, store ratings and reviews.
- Answer echoes: goal weight, date and event.
- CTA label: "Get my plan". A promo-code link.

**Checkout (Simple):**
- Format: a bottom sheet over the paywall.
- Payment order: **Google Pay → PayPal → card (collapsed)**, on an Android user agent. Apple Pay on iOS not seen.
- Consent at payment: an **unticked "I agree to the autorenewing terms" checkbox above the wallet buttons**.
- A "you'll pay $9.99 today" line and "You save 77%".

**Leaving the paywall (Simple):**
- Exit offer: closing the checkout sheet triggers "You've unlocked a special 80% discount!", with prices unchanged.
- Browser back loops to the paywall through an auto-forwarding teaser and resets the timer.

Still not observed (gaps for the skill): Noom's, BetterMe's, Lasta's and Headway's paywalls; Apple Pay ordering on iOS; card-field layouts; post-purchase upsells; any trial with a free (€0/$0) first period; timers on more than one funnel; a second checkout layout. Getting them needs either entering a name (the researcher's call) or other funnels without a name gate.
