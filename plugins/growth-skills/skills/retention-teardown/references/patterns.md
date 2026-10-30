# Retention Screen Pattern Library

The reference for the retention teardown. It covers the in-app screens
between the first purchase (or trial start) and the first renewal: the
welcome and first session, the notification and reminder asks, streaks and
progress, value recaps and the trial-ending notice, the return screen after
a gap, and the rating and widget asks.

Each pattern has **When**, **Cross-check**, **How**, **Evidence** (tests
#R1–#R61 and benchmark rows B1–B64 in `evidence.md`, rules in
`platform-rules.md`), **Seen in** (apps from `flows.md`) and **Trap**.
Tiers: strong, directional, anecdotal, observed.

**Read this first.**
- The first renewal is the steepest drop for every plan length (SOSA 2026,
  B15), and most of the decision comes early: 55.4% of 3-day-trial
  cancellations happen on Day 0 (B1), and 34.2% of annual cancellations come
  in month 1 (B26). Screens in the first session and first week carry the
  renewal, not a reminder the day before.
- "Not enough usage" is 33.7% of Google Play cancel-survey answers (B36).
  That is the problem these screens try to solve; it is a survey answer, not
  proof that a screen fixes it.
- 13 rows are strong tests, but most are Duolingo or lab studies. **No public
  test exists** for the welcome-after-purchase screen, an in-app trial-ending
  notice, an in-app weekly recap, a return screen, empty states or a mobile
  checklist. Those patterns are hypotheses: Medium at most.
- The same tactic flips sign. Check "Where it flips" at the end before
  recommending anything.

## Contents

**A. Welcome and first session**
1. Welcome that says what you have and the first step
2. Trial status inside the app
3. Starter content instead of empty screens

**B. Notifications and reminders**
4. Ask for notifications in context
5. Primer copy tied to the user's goal
6. An honest primer, per platform
7. Reminder setup after the first session
8. Reminders apart from marketing
9. After a decline: fallback, not nagging

**C. Habit and progress**
10. Progress where the user lands
11. Make the streak easy to keep
12. Design the broken streak
13. Acknowledge progress right after the action
14. A commitment screen after a session
15. Let people hide streaks and celebrations
16. A widget with the user's own progress

**D. Value and renewal**
17. A recap of the user's own value
18. A home for what they pay for
19. Trial-ending notice with what they used

**E. Return and asks**
20. Return screen: resume or restart lighter
21. Rating ask after a completed task
22. Ration the asks

**Where it flips** (summary at the end)

---

## A. Welcome and first session

### 1. Welcome that says what you have and the first step
**When:** the screen after purchase or trial start is a generic
congratulations, or drops the user on home with no direction.
**Cross-check:** does it name what changed (features, limits) and one next
action tied to the user's goal?
**How:** a short list of what's now included (the two or three things that
matter for this user's goal), then one primary button for the first step
("Start your first 5-minute session"). Use the goal or name from onboarding.
**Evidence:** no public test of the screen itself (gap). R1 (RevenueCat
blog): argues for a dedicated "what you now have" screen (anecdotal). Day-0
cancel share 55.4% (B1) frames why the first session matters (benchmark).
**Seen in:** Telegram and Fabric (feature list), Runna and Lifesum (goal in
the headline), 5 Minute Journal and mymind (first step). 4 of 14 welcome
screens on Mobbin were a generic congratulations.
**Trap:** another offer on this screen (lifetime, add-on, rating ask) spends
the first session on selling. Hypothesis: Medium at most.

### 2. Trial status inside the app
**When:** after the trial starts, the app never shows when it ends or what
it will cost.
**Cross-check:** can the user find the end date, the amount and how to
cancel without leaving the app?
**How:** a trial card on home or in the account area: "Trial ends Thu 14
Nov · then $39.99/year · Cancel anytime in Settings". If the paywall
promised a reminder, show the same promise on the card.
**Evidence:** #R48 Blinkist: a paywall trial timeline plus a trial welcome
screen with a reminder opt-in: +23% trial sign-ups, −55% complaints, push
opt-in 6% → 74%, −4% in-trial cancels (strong, bundled; the in-app status
part is not separated). No test of an in-app trial card (gap).
**Seen in:** Monzo (trial tab with days left), Babbel (trial strip on the
weekly summary), Duolingo (the reminder promise repeated after the start).
**Trap:** a trial card that only says "Upgrade" or shows a discount reads as
a sales banner; keep it informational.

### 3. Starter content instead of empty screens
**When:** a new payer lands on an empty library, history or home.
**Cross-check:** every screen a new payer sees on day 0 has a next action.
**How:** a starter plan, template or sample entry in the empty state, with
one action ("Add your first plant", "Try today's 3-minute lesson").
**Evidence:** no public test (gap). Mural's first-session checklist: 1-week
retention +10% relative (#R20 = onboarding #30, directional, web B2B,
off-target). Step's first-open walkthrough (#R21, directional, vendor,
off-target).
**Seen in:** Buddy (empty state with a first step after the welcome splash).
**Trap:** tooltips over an empty screen don't fix the empty screen.

## B. Notifications and reminders

### 4. Ask for notifications in context
**When:** the system prompt fires at launch, on the welcome screen or in
onboarding with no tie to something the user just chose.
**Cross-check:** what did the user do right before the ask?
**How:** ask right after the user sets a reminder time, finishes the first
session, starts a streak or turns on "remind me before my trial ends". Say
what they get: "We'll remind you at 8:00 to keep your streak".
**Evidence:** Apple: "provides a better experience than automatically
requesting authorization on first launch" (A13, guidance); Android: ask
after a user action (G2, guidance). Cluster: a benefit explanation before
the prompt raised acceptance from under 40% to 66% (#R5, directional, small
samples). Houseparty: push opt-in +9% with an explainer before each prompt
(#R7, directional, vendor). Headspace in-app opt-in asks by segment (#R10,
directional, vendor). Blinkist's trial reminder opt-in: opt-in 6% → 74%
(#R48, strong, bundled). Notifications are off by default on Android 13+
(G1).
**Seen in:** YNAB ties the ask to the trial reminder. 11 of 12 notification
asks on Mobbin sit in onboarding, before purchase.
**Trap:** Android stops showing the system dialog after two denials (G5);
spending the first ask at launch can cost the reminder that matters.

### 5. Primer copy tied to the user's goal
**When:** the ask says "stay updated" or "we need to send you
notifications".
**Cross-check:** does the copy name the user's own benefit?
**How:** tie it to their goal or habit ("Reminders help you keep a daily
habit"). Re-test copy per market.
**Evidence:** #R2 Duolingo: copy tied to learning goals, +8% opt-in for
German learners (strong). #R3: the same copy had no significant effect for
Spanish learners (strong, null). #R4: Japanese learners 50% less likely to
opt in (directional).
**Seen in:** Finch, 5 Minute Journal, ChatGPT (primers with a sample
notification).
**Trap:** claim-based nudges ("people who allow get far better results")
and "allowing unlocks the full experience" are pressure, not value.

### 6. An honest primer, per platform
**When:** a custom screen precedes the system prompt.
**Cross-check:** no look-alike system alert, no "Allow" button, no arrow at
the system button, no reward; Android has "No thanks".
**How:** iOS: one "Continue" that opens the system alert (a "Not now" is
acceptable for notifications). Android: "Continue" and "No thanks".
**Evidence:** HIG pre-alert rules (A16, A17; stated for data permissions
and tracking, best practice for notifications); Android: "Always provide the
option to cancel an educational UI flow" (G4). Platforms disagree on the
cancel option (platform-rules §4).
**Seen in:** 6 of 7 primers on Mobbin had a visible decline; Badoo had none.
**Trap:** a fake system alert or a reward for allowing is blocker 2.

### 7. Reminder setup after the first session
**When:** reminders exist but the user never picks a time, or only in
onboarding.
**Cross-check:** a time picker (and days or weekly goal where it fits)
after the first value moment, editable in settings.
**How:** after the first session: "When should we remind you?" with a
default near the time they just used the app.
**Evidence:** #R17 Calm (= onboarding #7): a reminder screen after the
first session, retention about 3x for prompted users, 40% set a reminder vs
under 1% who found it in Settings (directional, vendor, holdout implied).
#R18 (= onboarding #16): reminder setup inside onboarding vs on home, +6.4%
trial conversion, +24% ARPU (directional).
**Seen in:** a time wheel on all 9 reminder screens on Mobbin; Calm and
Speechify add days of the week; Waking Up and Duolingo keep it in settings.
**Trap:** several reminders a day by default is "constant push" (D4).

### 8. Reminders apart from marketing
**When:** one toggle or one ask covers reminders and offers.
**Cross-check:** a separate, worded consent for promotional messages, with
an in-app opt-out.
**How:** "Reminders" on by the user's choice; "Offers and news" as its own
toggle with its own wording.
**Evidence:** Apple 4.5.4: promotional push needs explicit opt-in via
consent language in the app's UI and an in-app opt-out (A1, rule); HIG (A18).
ICO/CMA name "bundled consent" (D6, guidance).
**Seen in:** Peloton Strength+ bundles reminders and marketing in one ask.
**Trap:** a primer that promises reminders while settings bundle "offers"
into the same toggle reads as bait; name both choices on screen.

### 9. After a decline: fallback, not nagging
**When:** the user declined, and the app re-asks on every open or goes
silent.
**Cross-check:** the app works, says what won't happen, offers a fallback
and re-asks only with a new reason.
**How:** a short note: "No reminders for now. You can turn them on in
Settings." Show the ask again only at a new moment (e.g. when they start a
streak).
**Evidence:** Apple 5.1.1(iv) (A4, applied by analogy); Android "gracefully
degrade" (G4) and two-denial limit (G5); FTC "nagging" (D1); DSA 25(3)(b)
on repeated requests (D2, narrow scope). Airship: in-app messages to
opted-out users, +14% average opt-in (B40, directional, vendor).
**Seen in:** not captured on Mobbin.
**Trap:** after two Android denials only a Settings link works; say why
before sending people there.

## C. Habit and progress

Skip this section for apps with no recurring task (scoring: "no habit
loop"). Never add a streak to a utility used once a month.

### 10. Progress where the user lands
**When:** progress lives only on a profile or stats tab.
**Cross-check:** home or today screen shows the streak, weekly goal or
"x of y" in the user's unit.
**How:** a compact progress element at the top of home that taps through to
the detail.
**Evidence:** Duolingo: a streak counter always visible at the top of the
app, DAU +3%, D14 +1% (#R30, directional, second-hand). Silverman &
Barasch: an intact streak log raised engagement 92.47% vs 64.94% with no log
(#R38, strong, lab, off-target). Stash: showing what users put in kept 12%
more saving at 8 months (#R47, strong, second-hand, off-target).
**Seen in:** Blinkist, Calm and WHOOP use weekly goals; Duolingo the
streak.
**Trap:** a visible streak hurts after it breaks (#R38): pair with
pattern 12.

### 11. Make the streak easy to keep
**When:** the streak needs the full daily goal or a long task.
**Cross-check:** what is the smallest action that keeps it?
**How:** one short session keeps the streak; the daily goal stays separate.
Offer a weekly goal or rest days where daily use doesn't fit.
**Evidence:** #R25 Duolingo (= onboarding #74): streak decoupled from the
daily goal, D14 retention +3.3%, learners on a 7+ day streak +40% a year
later, fewer users hit their daily goal (strong).
**Seen in:** Blinkist, Calm, WHOOP (weekly goals).
**Trap:** easier streaks mean less done per day (#R25); check the metric
that matters for the product.

### 12. Design the broken streak
**When:** a missed day shows a reset to zero, a sad mascot or nothing.
**Cross-check:** is there a repair, freeze, pause or neutral restart, and
is protection free at least once?
**How:** "You missed yesterday. Repair your streak" with one free repair;
a planned pause for holidays; neutral copy. Don't sell the streak back with
a timer at the moment of loss.
**Evidence:** #R38: a broken streak log cut engagement to 45.21%, below the
60.90% with no log (strong, lab). #R39: a repairable broken streak kept
85.20% engagement vs 68.66% unrepairable (strong, lab). #R29 Duolingo
Weekend Amulet: 4% more likely to return a week later, 5% less likely to
lose the streak (strong). #R27: two freezes instead of one, daily actives
+0.38% (directional).
**Seen in:** Finch (first repair free, pause mode), Duolingo (freeze; gem
refill at loss), Deepstash (more freezes with Pro), Noom. Cal AI shows a
full-screen streak-lost moment with no repair.
**Trap:** guilt copy, a countdown or a paid refill under pressure at the
loss is blocker 3 (FTC "confirmshaming", D1; Apple 5.6, A10, our reading).

### 13. Acknowledge progress right after the action
**When:** a session ends with no feedback.
**Cross-check:** a post-session screen moves the streak or goal; milestones
get more.
**How:** a short post-session screen with the streak or goal bar moving;
bigger animation on milestone days.
**Evidence:** Duolingo: streak shown after every lesson, DAU +1%, D14 +3%
(#R31, directional, second-hand); milestone animation, 7-day activity of new
learners +1.7% (#R26, directional). A single sign-up badge did nothing
(#R32); a wider range of badges raised DAU +2% and D14 +2% (#R33),
directional, second-hand.
**Seen in:** Duolingo, Cal AI (with an opt-out of badge celebrations).
**Trap:** turning the post-session screen into an upsell is a flag
(scoring 3.5).

### 14. A commitment screen after a session
**When:** the app has a streak but nothing that turns the next week into a
goal.
**Cross-check:** an optional "commit to 7 days" after a session.
**How:** after a session, offer a one-tap commitment ("Keep it going for 7
days?") with a visible goal; optional, no penalty copy.
**Evidence:** #R28 Duolingo Streak Wager: significant gains at D1, D7, D14;
D7 +14% (strong; used in-game currency). #R19 (= onboarding #25): one
commitment screen in onboarding doubled D30 retention (directional).
**Seen in:** Atoms (identity sentence with the reminder).
**Trap:** a wager with real money or a lost purchase is pressure; keep the
stake symbolic.

### 15. Let people hide streaks and celebrations
**When:** streaks or celebrations can't be turned off.
**Cross-check:** a setting to hide streaks or celebrations; minors get
streaks off by default.
**How:** a "Show streaks" toggle in settings and on the streak screen.
**Evidence:** Headspace lets users hide streaks (#R45, observed). EU
guidelines on minors: "communication streaks" off by default (D3, guidance).
#R38: a broken streak can hurt more than none (strong, lab).
**Seen in:** stoic. (opt out of streaks), Cal AI (opt out of badge
celebrations).
**Trap:** none known; low effort.

### 16. A widget with the user's own progress
**When:** the app offers a widget with a logo tile, or never mentions it.
**Cross-check:** the prompt previews the user's own streak or goal; the
widget deep-links to it; no promos in widgets or Live Activities.
**How:** after a session: a preview of their streak widget plus short
add-it instructions (iOS has no add-widget API); on Android a pin prompt.
**Evidence:** Duolingo: widget users had "far better retention" and
installs rose after an in-app promotion (#R58, anecdotal, no effect sizes).
Gratitude: "25% increase in retention for widget users" (#R59,
directional, likely self-selected). Hahow Live Activity: no significant
effect (#R60, anecdotal). Duolingo promo in a Live Activity drew complaints
(#R61, observed). Apple: no ads in widgets (A6, rule); no promotions in Live
Activities (A27, guidance); prefer dynamic personal content (A25).
**Seen in:** 6 of 10 widget prompts on Mobbin preview the user's own data;
5 of 10 tie to the streak. Vocabulary gives how-to steps.
**Trap:** a "streak ends in" countdown on the lock screen (yope) is loss
pressure.

## D. Value and renewal

### 17. A recap of the user's own value
**When:** the user never sees what they've done before the renewal.
**Cross-check:** a weekly or monthly in-app recap in the user's unit,
before the first renewal.
**How:** a weekly summary card: sessions, minutes, streak, change vs last
week; a monthly or year-end story for annual payers well before month 11.
**Evidence:** Blinkist Year in Blinks recipients 51% more likely to renew
(#R46, directional, vendor, no holdout). Conecta Ideas RCT: streak-
highlighting messages raised the share of weeks connected by 9.4 pp vs 2.5 pp
for generic reminders (#R40, strong; delivered as notifications). Stash
(#R47, strong, off-target). No in-app weekly recap test (gap). 34.2% of
annual cancellations happen in month 1 (B26, benchmark).
**Seen in:** weekly recaps in Babbel, MyFitnessPal, Headway, WHOOP, Oura,
stoic.; Strava monthly; Duolingo and Spotify yearly.
**Trap:** app-wide stats ("our community read 1M books") aren't the
user's value; show theirs first.

### 18. A home for what they pay for
**When:** paid features are named only on the paywall.
**Cross-check:** a benefits page or checklist that marks what's been tried,
dismissible.
**How:** "Your Premium" with each paid feature as a tile, a tick when tried,
and one tap into each.
**Evidence:** Mural checklist +10% 1-week retention (#R20 = onboarding #30,
directional, web B2B). Blinkist session-start message to premium users: add
rate +6.62% (#R22, directional, vendor). No mobile test (gap).
**Seen in:** Spotify "Your benefits" (ticks when tried), YouTube, Vivino;
checklists with a counter in 5 of 9 Mobbin examples.
**Trap:** a checklist that can't be dismissed becomes noise for people who
already know the app.

### 19. Trial-ending notice with what they used
**When:** the only trial-end message is a store email or a discount push.
**Cross-check:** before the charge, in the app: days left, date and amount,
what they used, how to cancel.
**How:** a card two to three days before the charge: "Your trial ends Thu.
You did 6 sessions and saved 3 plans. $39.99/year from Thu. Manage in
Settings."
**Evidence:** #R48 Blinkist reminder: +23% trial sign-ups, −4% in-trial
cancels (strong, bundled). #R50 Slopes copied it: 75% opted in, but
trial-to-paid −7.8% for opted-in users; test stopped (directional). #R51
Shaw Academy reminder email 3 days before the end: +14% sales (strong,
email, context only). No in-app notice test (gap).
**Seen in:** Monzo (lists features used with counts), Babbel (strip on the
weekly summary), Duolingo (full screen).
**Trap:** the sign depends on whether the user got value before the notice
(#R50: Slopes is used on the slopes, not at home on day 5). Show what they
used; if they used nothing, point to one first step.

## E. Return and asks

### 20. Return screen: resume or restart lighter
**When:** a returning user lands on a paywall, an upsell, a guilt screen or
a cold home.
**Cross-check:** resume where they left off, plus a lighter restart.
**How:** "Welcome back. Pick up lesson 4, or start with a 3-minute
refresher." No paywall for a payer.
**Evidence:** Duolingo: about 5% of users return after 30+ days and are
about 20% less likely to be retained than new users (#R52, directional,
observational; no test). No public test of a return screen (gap).
**Seen in:** Runna (three ways back in), Skillshare, Brilliant and Quizlet
(resume), Tinder and Finch (a user-chosen pause).
**Trap:** guilt copy ("we missed you, your streak is gone") is pattern 12's
trap.

### 21. Rating ask after a completed task
**When:** the rating prompt fires at launch, in onboarding, on the welcome
screen or behind a "do you enjoy the app?" gate.
**Cross-check:** system prompt only, after a completed task or milestone;
"Rate us" buttons link to the store.
**How:** show the system prompt after a finished workout or a 7-day
milestone; "Rate us" in settings opens the store page. Don't design a step
that depends on the prompt appearing: the system may not show it.
**Evidence:** WordBoard moved the prompt earlier (after one use): ratings
per month +400%+, average held around 4.84 (#R53, directional, before/
after). Tokopedia: 5-star ratings 4x after the Play in-app review sheet
(#R56, directional). Apple: system API only, custom prompts disallowed (A8,
rule); "filtered" feedback named (A9); timing guidance (A21–A24). Google:
no question before the card, including "Do you like the app?" (G7); no
button trigger (G9); no incentives (G10, rule).
**Seen in:** BitePal (after the first log), Headway (after the weekly
recap). 3 of 8 Mobbin examples use a yes/no pre-screen (flag).
**Trap:** a sentiment gate or a reward is blocker 2.

### 22. Ration the asks
**When:** notifications, rating, widget and upgrade asks stack in the same
session or return on every open.
**Cross-check:** one ask per event, a decline respected, no fake badges.
**How:** a simple order: value first, then one ask tied to what just
happened. Space the next ask by days.
**Evidence:** Apple: one notification per event, badges only for unread
notifications (A20, guidance); FTC "nagging" (D1); DSA 25(3)(b) (D2, narrow
scope). No test of ask frequency (gap).
**Seen in:** not measurable on Mobbin (timing not shown).
**Trap:** the upgrade ask belongs to the upsell teardown; here, count it
only as one more ask in the session.

---

## Where it flips

| Tactic | Wins when | Loses when | Evidence |
|---|---|---|---|
| Trial-ending reminder | The user got value before it fires; it repeats the paywall's promise | It asks "still want this?" before the user has used the product | #R48 vs #R50 |
| Visible streak | While it's intact (92.47% vs 64.94% with no log) | After a break (45.21% vs 60.90% with no log); worse when self-blamed | #R38 |
| Easier streak rule | Retention and streak counts | Daily goal completion (fewer hit it) | #R25 |
| Primer copy | In the market it was tested in (+8% German) | Copied to another market (no effect in Spanish) | #R2, #R3, #R4 |
| Provisional push (iOS) | Reach (+36% reachable base, off-target) | Opt-in and early retention looked the same | #R12, #R13 |
| Promo on a retention surface | Short-term sign-ups | Retention, DAU and complaints; breaks Apple's Live Activity guideline | #R61, upsell #U4, A27 |
| Earlier rating ask | Volume (+400%+) with the average held | Untested in a controlled split; both cases were apps rated above 4.8 | #R53, #R54 |
| More streak protection | Fewer lost streaks (Weekend Amulet) | Small gains for more inventory (+0.38%) | #R29, #R27 |
