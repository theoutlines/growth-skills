# Retention screens on Mobbin: first purchase to first renewal

Collected 2026-10-30 from public Mobbin captures. Scope: in-app screens of a mobile subscription app between the first purchase (or trial start) and the first renewal.

How to read this file:
- **Observed only.** Every row is a screen seen on Mobbin. None carries performance data, and nothing here claims an effect. Use it for "top apps do X" lines (tier: observed), never for an uplift.
- Screens are described in our own words. Only a few words of a button or label are quoted where the wording is the point. Open the `mobbin_url` to see the screen.
- Bucket = RevenueCat SOSA bucket (primary App Store category). Finance apps have no SOSA bucket: they are filed under Utilities, marked "(finance)". Travel and food apps are filed under the nearest bucket and marked too.
- **Platform gap:** every example is iOS. Android-specific surfaces (Android 13+ notification permission, Play in-app review, widgets) are covered only by the rules in `platform-rules.md`.
- **Timing caveat:** Mobbin shows a screen but not when it appears. Most notification primers, reminder pickers and widget asks below sit in onboarding, before the paywall, not after purchase. That placement is itself a finding (see "Patterns across apps").

Surface numbers:
1. Welcome after purchase or trial start
2. Notification permission primer
3. Reminder or habit setup
4. First-week checklist and feature discovery
5. Streaks, freeze or repair, progress, goals, achievements
6. Value recaps
7. Trial-ending notices and trial timelines inside the app
8. Welcome back after inactivity
9. Rating prompts and pre-prompts
10. Widget or Live Activity prompts

---

## 1. Welcome after purchase or trial start

- **Telegram** (iOS, Social & Lifestyle): a confetti confirmation followed by a long, scrollable list of every unlocked feature, each with a coloured icon and a one-line explanation. A full inventory, with no single first step. — https://mobbin.com/screens/7288bc47-763a-4b9f-8f91-b57c6681d46c
- **Fabric** (iOS, Productivity, AI tag): a small green "payment successful" chip, a "Welcome to Pro" headline and a six-row list of Pro capabilities. The way forward is a small "Start exploring" pill, not a full-width button. — https://mobbin.com/screens/48390d49-371c-4731-80ab-e82d3f40c06e
- **X** (iOS, Social & Lifestyle): a success toast sits on top of a full-bleed Premium hero. One button offers a quick tour of the new features. — https://mobbin.com/screens/03c501e7-abaa-4543-9b95-9ece4cc0de2c
- **Runna** (iOS, Health & Fitness): a celebratory photo with confetti, the user's first name in the headline and a line tied to their running goal. One Continue button. — https://mobbin.com/screens/7c658b13-5583-41a3-b7ed-37806f36ccae
- **Lifesum** (iOS, Health & Fitness): an illustration, a small "Premium activated" label under the headline, and copy that points back to the goal the user set in onboarding. The button sends them to explore the app. — https://mobbin.com/screens/1aa5560a-1e01-4b98-93bc-b7f4daa21c26
- **5 Minute Journal** (iOS, Health & Fitness): a "Premium unlocked" screen whose only job is to start a short setup (preferences and the new features). The first step after purchase is configuration, not a tour. — https://mobbin.com/screens/0031fd0f-f2e4-4e3d-85a1-f2e6ceeff86f
- **Paired** (iOS, Social & Lifestyle): a crown on the brand colour, plus a note that the partner has Premium too. The shared benefit is the whole message. Single Next button. — https://mobbin.com/screens/307a3a1f-23a4-4d33-b09e-33bb58fa787a
- **Headway** (iOS, Education): a star badge and a member count as social proof. Generic, with no feature or first step named. — https://mobbin.com/screens/8b8714eb-2ed6-4468-bde5-59df3f8ae4f2
- **Deezer** (iOS, Media & Entertainment): a minimal centred tick, one line of confirmation and a "Get started" button. Nothing about what changed. — https://mobbin.com/screens/789bdd09-de9e-4782-81b7-d5699366d4cf
- **Tinder** (iOS, Social & Lifestyle): a small modal over the profile tab welcomes the user to the Gold tier. The choice is "Take me there" (to the feature list) or "Maybe Later". — https://mobbin.com/screens/944a9799-fb50-4c98-8dc5-ca2cde110800
- **YouTube** (iOS, Media & Entertainment): a three-page welcome carousel. Page one names the three core Premium benefits in a single line. — https://mobbin.com/screens/9a389617-5ecd-4f0f-b3bd-fcac30361f1d
- **The Weather Channel** (iOS, Utilities): the purchase flow ends in a Premium welcome card, then a five-page benefit carousel whose last button goes straight to the forecast. — https://mobbin.com/screens/4894e295-5046-407c-9c7e-d8e27cd3d7b5 · flow: https://mobbin.com/flows/4539bacc-bfaa-4312-98c5-c70127946fe7
- **mymind** (iOS, Productivity): after a plain system-style "you're all set" alert, the user lands on an empty home screen that names the one action that matters (save something through the share sheet) and offers a camera-roll button. — flow: https://mobbin.com/flows/e5893443-6b29-4cfb-813d-156ee8142960
- **Buddy** (iOS, Utilities (finance)): a large "Success!" splash, then an empty budget overview with a floating "Add transaction" button as the first step. — flow: https://mobbin.com/flows/b055c728-1094-44ae-88e2-b861db4a7d03

## 2. Notification permission primer

- **5 Minute Journal** (iOS, Health & Fitness): a mock notification card at the top previews a reminder. The copy lists the three things notifications will carry (journal reminders, quotes, new content), with a primary enable button and a "Maybe later" text link. — https://mobbin.com/screens/b94c8034-63e4-47ba-b030-975df4167c79
- **Finch** (iOS, Health & Fitness): the pet is named in the title and sends the sample notification itself (a water reminder). Green allow button and a grey "Maybe later" of equal size. — https://mobbin.com/screens/3e88469e-f60a-439d-ac4d-0bd06fd8eae4
- **ChatGPT** (iOS, Productivity, AI tag): frames notifications around things the product finishes for you (a task done, a summary ready) and shows one sample card. "Maybe later" sits under the main button. — https://mobbin.com/screens/6ca31203-996b-46c7-abbc-ebc8a7486035
- **Peloton Strength+** (iOS, Health & Fitness): a dark primer that ties notifications to the user's goals, then adds that offers and new features will come through the same channel. It says the setting can be changed later. Reminders and marketing are bundled in one ask. — https://mobbin.com/screens/d030c568-4577-46b8-a3e1-1ff84fc8e317
- **Apple TV** (iOS, Media & Entertainment): a lock-screen mock and copy built on what the user follows (shows, teams). Continue or "Not Now". — https://mobbin.com/screens/dfb35f09-5705-4d68-be2f-6bae3e1927fa
- **YNAB** (iOS, Utilities (finance)): a modal over a setup step asks for notifications for one stated reason: a reminder before the trial ends. "Remind Me" or "Not Now". The trial reminder is the reason to allow notifications. — https://mobbin.com/screens/b4044271-2016-425d-b57f-dbb875a457f2
- **Duolingo** (iOS, Education): the mascot frames reminders as help to build a habit. The system dialog appears on the same screen, with an arrow pointing at Allow, and the main button reads "Remind me to practice". — https://mobbin.com/screens/817844ed-f7df-4645-b18b-a9803879821f
- **Headway** (iOS, Education): an onboarding step lists three notification types (morning inspiration, streak protection, recommendations), each with its own toggle, and the system prompt fires on top. A granular choice before the binary one. — https://mobbin.com/screens/23f2827d-0aee-4d28-8a25-9e59ad2c0b3a
- **Breathwrk** (iOS, Health & Fitness): the system prompt is highlighted with a drawn frame and arrow, and a line under it claims that users who allow notifications get much better results. An unsourced claim used as pressure. — https://mobbin.com/screens/400d8291-3d8c-4b78-99ae-6a59c56ae6a3
- **Numo** (iOS, Productivity): the system prompt fires over a headline promising "100%" of the app's value, and the CTA repeats the promise. Allowing is framed as the price of full value. — https://mobbin.com/screens/6fb97e6d-a209-4b7a-8c60-570b6d59d6b0
- **Ladder** (iOS, Health & Fitness): the system prompt over a "get notified when workouts drop" screen, with Skip in the corner. One clear reason, tied to content. — https://mobbin.com/screens/4aae4d39-84b9-41aa-a571-efb4b5fba3b2
- **Badoo** (iOS, Social & Lifestyle): a minimal primer (bell icon, one line about matches and messages) with a single Continue button and no visible way to decline before the system dialog. — https://mobbin.com/screens/5e261bab-de17-4a5a-a641-79dd69d2ac74

## 3. Reminder or habit setup

- **Duolingo** (iOS, Education): the reminder settings split reminders by type (practice, streak freeze used, streak saver, weekly progress), each with push and email toggles, plus a reminder time and a "smart scheduling" switch. The weekly-progress reminder is a value recap delivered by email. — https://mobbin.com/screens/ec850b9f-5407-470f-8d3c-548f4ac5c2df
- **Calm** (iOS, Health & Fitness): a mindfulness-reminder sheet with a reason line, a single time button that opens a wheel and seven weekday checkmarks. — https://mobbin.com/screens/6d39ad82-b826-4742-a7cd-a711aafe52a9
- **stoic.** (iOS, Health & Fitness): three reminder slots (morning, during the day, evening), each with its own time and toggle, and a line recommending three a day. — https://mobbin.com/screens/bf867df9-6820-4519-adca-d573fba434d1
- **Speechify** (iOS, Productivity): a "build your reading habit" sheet that combines a weekly schedule (day chips), a daily goal, a reminder toggle and a time. Goal and reminder are set together. — https://mobbin.com/screens/679becc9-e973-4cee-a3a4-ec39257fdd29
- **Atoms** (iOS, Productivity): the user's habit, written as an identity sentence, stays visible behind the time sheet, so the time is chosen against the commitment. Includes a Remove option. — https://mobbin.com/screens/cde3d7db-3316-4269-bc8b-01095cf9699f
- **Fable** (iOS, Education (books)): one question (when do you want to read), a time wheel and a line saying a notification will come at that time. "Set reminder" button. — https://mobbin.com/screens/63fde944-72e0-4983-9089-2508eab01c25
- **CapWords** (iOS, Education): a daily-reminder sheet with an on/off switch, a time wheel and a habit-stacking tip at the bottom. — https://mobbin.com/screens/b43509a4-11cb-4d22-9121-1b2afe39a7e5
- **Waking Up** (iOS, Health & Fitness): a plain form (time, repeat) with a "Set a Reminder" button, inside the app's settings rather than in onboarding. — https://mobbin.com/screens/e4c6a47e-d33e-476c-8dc6-c0d5d02fc4d0
- **Numo** (iOS, Productivity): a separate time wheel for each habit the user picked (brushing teeth, drinking water), on one scrolling screen. — https://mobbin.com/screens/f36e016d-7321-4c14-8eb8-8696c73bc0fc

## 4. First-week checklist and feature discovery

- **Strava** (iOS, Health & Fitness): a home-feed card with a 0/4 progress bar and four steps (record an activity, follow three people, add a photo, connect a device). The device step has a direct "Connect" button and an "I don't have one" way out. — https://mobbin.com/screens/91cd1603-5d79-4dfa-914c-3bb3bdcf78a5
- **Peloton** (iOS, Health & Fitness): a dedicated getting-started page with a segmented progress bar. Each row expands to one sentence and one action button (for example, edit profile). — https://mobbin.com/screens/35166d20-06cd-4104-9355-9feba7f3290a
- **Google Health (Fitbit), Premium** (iOS, Health & Fitness): a "1/3" set-up card on the Today tab with image rows (connect records, add friends, connect Apple Health). Finished rows fade with a tick, and the card can be dismissed. — https://mobbin.com/screens/fe7208b2-ff98-4e64-be36-31f8c23435a3
- **Future** (iOS, Health & Fitness): a home checklist run by the human coach (say hello, schedule a kickoff call, finish the profile), with a "your first workout is being built" card in the middle. — https://mobbin.com/screens/f76775cf-09ab-4664-8d1c-b2db91ddb7e0
- **Preply** (iOS, Education): the home screen is the checklist: numbered steps, with the current step (a booked trial lesson) expanded and a join button. — https://mobbin.com/screens/c3d369c6-c1bd-4deb-8daa-62903d11d95b
- **Speechify** (iOS, Productivity): a compact "great start" list with the finished step struck through, plus a coach mark arrow pointing at the add button for the next step. — https://mobbin.com/screens/315dbdf5-0cd1-4dc4-90f4-80faf9d30b24
- **Spotify** (iOS, Media & Entertainment): a "Your benefits" hub with a grid of tappable feature tiles (AI playlist, offline backup, listen together, queue, audiobooks). A tile gets a tick once tried. Each tile opens a one-feature explainer card. — https://mobbin.com/screens/853e9f95-b1e1-4ec7-8dec-8724c766fbd0 · explainer: https://mobbin.com/screens/a4845a96-4d9e-4482-bd55-d1e3be2e84d2
- **YouTube** (iOS, Media & Entertainment): a dismissible "Explore your benefits" carousel at the top of Home, next to a "New to you" filter chip. Each card goes to one Premium feature. — https://mobbin.com/screens/af3e64eb-1f2a-40d7-9b7a-a7430fa6d37c
- **Vivino** (iOS, Social & Lifestyle (food & drink)): Premium benefits shown as a story-style sequence with a progress bar, one benefit per page with a product mock. It is reached from a permanent "My Premium Benefits" row in the More tab. — flow: https://mobbin.com/flows/af6eaa74-ab21-4e83-8b39-da8bb5504d68

## 5. Streaks, freeze or repair, progress, goals, achievements

- **Duolingo** (iOS, Education): after a missed day, a bottom sheet says a freeze protected the streak. It shows the used freeze and an empty slot, with a refill priced in gems and "No thanks". Protection, then a currency upsell. — https://mobbin.com/screens/3b18d128-382c-4604-9f98-214c7d239779
- **Finch** (iOS, Health & Fitness): a streak-repair screen where the pet says missing a day is fine. The repair is free the first time (the normal gem price is struck through), and "Start over" is the equal-size alternative. — https://mobbin.com/screens/d6e7a7b1-4b61-40b1-8ff7-1c602badec85
- **Finch** (iOS, Health & Fitness): a "Pause mode" card that freezes the streak for a set number of days, drops goals for the duration and can be turned off at any time. A planned absence without loss. — https://mobbin.com/screens/a5edeeba-6436-4e55-a691-63b508711579
- **Noom** (iOS, Health & Fitness): a streak screen with a month calendar and a note that a freeze is applied automatically if a day is missed. — https://mobbin.com/screens/e8d88c93-7fb9-4411-a5e2-1be6d3d0d8a5
- **Deepstash** (iOS, Education): a sheet explaining freezes (used automatically to restore a lost streak) with a Pro badge noting that subscribers get two a week. Streak insurance as a paid perk. — https://mobbin.com/screens/67778ca7-d035-482f-a321-87938f865712
- **stoic.** (iOS, Health & Fitness): the first-streak screen includes a "Use streaks" toggle and says streaks can be hidden later in settings. Opting out is offered at the moment the streak starts. — https://mobbin.com/screens/5fddacf1-5456-43e4-9a72-8bec9591bd75
- **Cal AI** (iOS, Health & Fitness, AI tag): a "streak lost" modal with a greyed flame and an empty week row, and one line urging the user to log today. Neutral wording, but a full-screen loss moment with no repair or pause option. — https://mobbin.com/screens/f48da1ad-4de3-4900-9abd-6978316b5bb7
- **Blinkist** (iOS, Education): a weekly goal ring (days done out of a target) with an Edit link, and two lifetime stats under it. The goal is weekly, not daily, and editable in place. — https://mobbin.com/screens/8fb088c9-d0d7-41f9-b5ac-f9087c7e1cd0
- **Calm** (iOS, Health & Fitness): a progress sheet that asks for a three-days-a-week commitment, shows a ring for this week with day checks, and lists the sessions done. — https://mobbin.com/screens/56e1a984-3812-4790-988c-76c793ab1b67
- **Cal AI** (iOS, Health & Fitness, AI tag): a badge-unlocked screen (three days of water logging) with share and view-all buttons, plus a quiet text link for people who don't want badge celebrations. — https://mobbin.com/screens/40baeea4-067a-40ef-99d9-2334bea66716
- **YouTube** (iOS, Media & Entertainment): a badge awarded just for being a Premium member, with copy inviting the user to use Premium features to earn more. Badges can be seen on the Premium benefits page. — https://mobbin.com/screens/e39cc715-bdd1-4645-a654-01ed7226e037 · shelf: https://mobbin.com/screens/aeba2c60-7203-43db-8841-3e31b5c73ee1
- **Runna** (iOS, Health & Fitness): a personal-best badge (fastest 1K) shown full screen with confetti, built from the user's own run data. — https://mobbin.com/screens/0e8a24e7-31ae-4657-bc16-6ace3abc70ea

## 6. Value recaps

- **Babbel** (iOS, Education): a weekly summary with lessons per day, a weekly-goal bar, review score and new items. A pink strip at the bottom says the free trial ends in three days. The value recap and the trial notice share one screen. — https://mobbin.com/screens/65435f22-30a8-440c-9868-8fb64d41c7e9
- **MyFitnessPal** (iOS, Health & Fitness): a weekly digest that ends with all-time counts since the member date (foods, meals, exercises, steps) and a "keep it up" block naming the streak the user could reach this week. — https://mobbin.com/screens/59f5fcf9-86f9-4255-87ca-2a1d2496b759
- **Headway** (iOS, Education): after a summary, "your growth this week" shows three counts with week-on-week deltas, then asks for a rating of that summary (content feedback, not the store). — https://mobbin.com/screens/360a3557-3436-46f0-a3d0-594490bc373e
- **WHOOP** (iOS, Health & Fitness): weekly plan results as a large percentage gauge with a list of goals, plus two buttons: continue the plan or change it. A low score is met with an encouraging line. — https://mobbin.com/screens/2f82e79e-543d-43c6-b74c-14248de208b0
- **Oura** (iOS, Health & Fitness): a weekly report page with bars for each day, a plain explanation of what the score means and how many times the goal was reached. — https://mobbin.com/screens/90ebee77-8190-44c5-95cf-8904ec501a49
- **stoic.** (iOS, Health & Fitness): a Journey tab that groups past weeks into cards, each with a one-line count of journals, reflections and exercises. The recap is a permanent archive, not a one-off push. — https://mobbin.com/screens/5e124ffa-c154-4e2c-8faf-6bad200a3b81
- **Strava** (iOS, Health & Fitness): a monthly "Month in Sport" story with a progress bar, between a weekly and a yearly cadence. — https://mobbin.com/screens/03177fff-c9b1-40a4-bcbd-2f332d44318d
- **Duolingo** (iOS, Education): a year-in-review opener with the mascot and a single start arrow into a story sequence. — https://mobbin.com/screens/fb0dd69e-4641-4853-845b-cf723882a462
- **Spotify** (iOS, Media & Entertainment): a yearly recap summarised as swipeable share cards (top artists, top songs, minutes, top genre), with a share button. — https://mobbin.com/screens/9f826cdd-afb0-4c1f-b50c-29cba57659e1

## 7. Trial-ending notices and trial timelines inside the app

- **Duolingo** (iOS, Education): a full-screen in-app notice that the trial ends in four days. A "Stay on Super" button sits above a list of benefits, with a settings gear in the corner. Sent mid-trial, not at the paywall. — https://mobbin.com/screens/a3e467db-f7e3-4d4e-9eea-11c639c2e32a
- **Duolingo** (iOS, Education): right after the trial starts, a confirmation step says the trial has begun and when the reminder will come (two days before the end). The trial-reminder promise is repeated after purchase. — https://mobbin.com/screens/1a40c1b8-449c-488c-9479-a47e2d4f9d78
- **Duolingo** (iOS, Education): the Max trial offer lets the user choose when to be reminded (two or three days before), with the calendar date shown for each option. — https://mobbin.com/screens/66959fc7-7c36-4713-a034-531e04c1e510
- **Monzo** (iOS, Utilities (finance)): during a free week, the Extra tab shows days left, says plainly that no charge will happen at the end, and lists the features the user actually used with usage counts ("Most used"). A "Get Extra" button keeps it. — https://mobbin.com/screens/da9f02af-72af-4af8-abd1-e06147f4872e
- **Babbel** (iOS, Education): a persistent strip on the weekly summary counting down the trial days (see surface 6). — https://mobbin.com/screens/65435f22-30a8-440c-9868-8fb64d41c7e9
- **Cal AI** (iOS, Health & Fitness, AI tag): the trial-reminder promise carries a small caveat that it only works if notifications are on. The reminder depends on the permission. — https://mobbin.com/screens/ca622b90-453e-40d0-b981-7fbdc7ec41dd
- **Headway** (iOS, Education): the reminder promise names the exact reminder date in a chip under the headline. — https://mobbin.com/screens/9dad1fe1-84aa-4920-8637-0cc2cbbe2420
- **Strava** (iOS, Health & Fitness): a three-step vertical timeline (today: everything unlocked; day 28: a reminder; day 30: the charge, with the price), plus the charge date under the button. Shown at the offer. It is the timeline the in-app notices should echo later. — https://mobbin.com/screens/40d104f8-8f25-4ae3-90eb-373e30e35acd
- **Bevel** (iOS, Health & Fitness): the trial reminder shown as a lock-screen mock with the actual notification text and cancel-by date. — https://mobbin.com/screens/4e61701e-2514-4dc9-b6a8-a7c1e9e187e7

## 8. Welcome back after inactivity

- **Runna** (iOS, Health & Fitness): the Today tab greets a returning user by name, says they have been inactive for a while and offers three ways back: start a new plan, restart the current one or carry on. — https://mobbin.com/screens/0116015c-bb3b-46fd-a2f6-3194ad72193a
- **Lovi** (iOS, Health & Fitness): a warm full-screen greeting with a smiling blob and one "let's start" button. Tone only, with no recap or re-entry choice. — https://mobbin.com/screens/e5c1876c-e70a-43f7-86c4-ef926523e5e8
- **Skillshare** (iOS, Education): the Home header says welcome back, shows badge counts and a "next achievement" bar (one of three classes done), then a "Continue watching" row with minutes left in the lesson. — https://mobbin.com/screens/eaa37d84-6ac3-44d2-a888-35e0198919db
- **Brilliant** (iOS, Education): Home opens on the course in progress, with the last finished lesson ticked and a large "Continue course" button. — https://mobbin.com/screens/9ae00b56-ed93-44fc-9d1f-0e608ce6e78d
- **Quizlet** (iOS, Education): a "Jump back in" carousel at the top of Home with a Continue button on the last study set. — https://mobbin.com/screens/816e9f43-98be-4455-bf27-bba42fb4193a
- **Tinder** (iOS, Social & Lifestyle): a paused-account state explains what is hidden and offers a single "Jump back in" button. The user chose the absence, and coming back is one tap. — https://mobbin.com/screens/dc1a56d1-25a2-487f-8cd1-1d97c2f7a314

Note: Mobbin's "welcome back" results are mostly sign-in screens (DoorDash, Wolt, Credit Karma), which are out of scope. Return screens for paying users who were inactive are thin on Mobbin.

## 9. Rating prompts and pre-prompts

- **BitePal** (iOS, Health & Fitness, AI tag): a custom star sheet appears right after the first meal is logged (a reward toast is still visible above). It asks about the logging experience, not the app in general, and offers "Not now". — https://mobbin.com/screens/bf79d202-5e82-47bc-b1eb-5db218375af5
- **Headway** (iOS, Education): after the weekly growth screen, a custom sheet asks for a detailed App Store review. One button and a close X. It asks for a written review straight away, with no sentiment check. — https://mobbin.com/screens/15e7abf3-08fd-4142-a7c6-9891246e1bc3
- **Ahead** (iOS, Health & Fitness): during the course path, a bottom sheet asks by name whether the user is enjoying the app. "Yes" or "Not sure yet". A sentiment gate in front of the store dialog. — https://mobbin.com/screens/c53659e5-340a-467d-a312-cdd19285e38c
- **ElevenLabs** (iOS, Productivity, AI tag): a sheet with decorative stars and two answers ("Yes, I love it" / "Not really"). The same two-way gate. — https://mobbin.com/screens/3618714a-f02b-4f50-9bc1-fa604e548d82
- **Preply** (iOS, Education): a thumbs-up screen with "It's great!" and "It could be better". A sentiment split before any store ask. — https://mobbin.com/screens/bb6607f5-7c59-44c9-b76e-a07e474ec463
- **Insight Timer** (iOS, Health & Fitness): an in-app star rating and review box, followed by a modal asking the user to also rate on the App Store. The rating is collected in-app first, then the store is asked for. — https://mobbin.com/screens/3b003d04-a3e2-4597-8386-1ea8d5959fc7
- **ABY Journal** (iOS, Health & Fitness, AI tag): a full onboarding step, before the product has been used, asks for a five-star rating with laurels, a user count and testimonial cards. "Skip for now" is a text link. — https://mobbin.com/screens/3143f57c-defc-43ec-9081-a8c9a656b470
- **Revolut Business** (iOS, Business): a dark sheet that asks outright for five stars. The button text names the star count. — https://mobbin.com/screens/276dbcd4-37b1-4ef7-95c5-087e0802b338

## 10. Widget or Live Activity prompts

- **Insight Timer** (iOS, Health & Fitness): a widget preview showing the user's consecutive days with day ticks, a line saying the widget helps people stay consistent, and Skip in the corner. — https://mobbin.com/screens/b62e5de5-b834-4c15-b43a-d4b285f1202f
- **Duolingo** (iOS, Education): the widget ask comes with a reason to add it this week (a new mascot look each day). "Add widget" or "Not now". — https://mobbin.com/screens/a238f3ab-2e49-420a-89b6-0c22d6865c31
- **Ladder** (iOS, Health & Fitness): the widget is presented as a "welcome gift" the user has unlocked (weekly streak plus workout of the day). The only button is "unlock free gift", and a small X closes it. Gift framing for a free OS feature. — https://mobbin.com/screens/9d8a6a03-dffd-4f6a-b05b-565a4543c265
- **Liven** (iOS, Health & Fitness): a phone mock with a streak widget in place, framed as keeping the streak on track. "Maybe later" at the top. — https://mobbin.com/screens/0dea0bc7-d875-469c-aae1-aa0216855133
- **Mimo** (iOS, Education): a phone outline with a streak-count widget and the mascot. One reason line, "Add widget" or "Not now". — https://mobbin.com/screens/4d17aee0-2022-4faa-9eac-466535de7150
- **Vocabulary** (iOS, Education): the widget preview (a word of the day) with the how-to steps written under the headline, because iOS gives apps no add-widget API. "Remind me later" as the alternative. — https://mobbin.com/screens/bb4fe10e-35ee-4c29-94e7-dde6d5323f5c
- **BitePal** (iOS, Health & Fitness, AI tag): a widget showing calories left with the mascot, on a bold blue screen. "Add widget" or "Maybe later". — https://mobbin.com/screens/69b5a69d-2172-48b2-a0a9-e0248ed03de4
- **Finch** (iOS, Health & Fitness): a bottom sheet over the pet's room offering the pet as a home-screen widget, with "No thanks". — https://mobbin.com/screens/d11b11e0-3abc-4c9a-8cc7-31e98c571367
- **Flighty** (iOS, Utilities (travel)): a Live Activities settings page with a lock-screen preview, a Pro tag on the live flight-status feature and a toggle for friends' flights. The Live Activity is a paid feature shown where it is set up. — https://mobbin.com/screens/8db79b88-d9db-40c1-a9f8-5fb90c155f0a
- **yope** (iOS, Social & Lifestyle): a lock-screen Live Activity counting down the hours left to save a 15-day streak, with flame graphics. Streak-loss urgency carried outside the app. — https://mobbin.com/screens/bcb66346-6e57-45ff-9bf7-028336fafb7c

---

## Patterns across apps

Counts cover the examples in this file only (98 bullets, about 60 apps). Mobbin captures designed flows, so the absence of a pattern here is not evidence that it is rare.

**Welcome after purchase (14)**
- A generic congratulations with no feature or next step named: 4 of 14 (Deezer, Headway, Paired, Buddy's splash screen before its empty state).
- Lists what's included (list or carousel): 4 of 14 (Telegram, Fabric, YouTube, The Weather Channel). Vivino's story-style benefit tour (surface 4) is the same idea, reached from the More tab.
- Names one first step or setup action: 5 of 14 (5 Minute Journal, mymind, Buddy's empty state, X's tour, Lifesum's goal link).
- Personalised with the name or onboarding goal: 2 of 14 (Runna, Lifesum).
- Variant: a dismissible modal over the app rather than a full screen (Tinder).

**Notification asks (12)**
- A separate primer before the system prompt: 7 of 12 (5 Minute Journal, Finch, ChatGPT, Peloton Strength+, Apple TV, YNAB, Badoo). 6 of the 7 offer a visible decline ("Maybe later", "Not now"). Badoo does not.
- The system prompt fired over a context screen with no separate primer step: 5 of 12 (Duolingo, Headway, Breathwrk, Numo, Ladder).
- A sample notification shown on the primer: 5 of 12.
- Asked during onboarding, before purchase: 11 of 12. Only YNAB ties the ask to something the user just bought into (the trial reminder). No post-purchase or "first habit done" notification ask surfaced on Mobbin.
- Granular types before the binary ask: 1 (Headway). Per-type control later in settings: Duolingo.
- Anti-patterns seen: a claim-based nudge ("people who allow get far better results", Breathwrk); framing allowing as the price of full value (Numo); reminders bundled with marketing in one ask (Peloton Strength+); no decline before the system dialog (Badoo). A system prompt at bare launch with no context: 0 seen in this sample.

**Reminder or habit setup (9)**
- A time wheel: 9 of 9. Days of the week chosen too: 2 (Calm, Speechify). Several reminder slots a day: 2 (stoic., Numo).
- Goal and reminder set on one screen: 2 (Speechify, Atoms with its identity sentence).
- Reachable from settings after onboarding: 2 (Waking Up, Duolingo).

**Checklists and feature discovery (9)**
- A progress counter (x/y or bar): 5 of 9.
- Lives on Home or Today rather than in a modal: 6 of 9.
- Dismissible: 3 (Fitbit Premium, YouTube, Spotify's hub is optional).
- A way out for a step that doesn't apply ("I don't have one"): 1 (Strava).
- A permanent "your benefits" page for payers: 3 (Spotify, YouTube, Vivino).

**Streaks, progress and achievements (12)**
- Some form of streak protection (freeze, repair or pause): 4 apps, 5 screens (Duolingo, Finch ×2, Noom, Deepstash).
- Protection sold or gated: Duolingo (gem refill), Deepstash (more freezes with Pro), Finch (repair costs gems after the first free one).
- A planned pause: 1 (Finch). Opting out of streaks offered: 1 (stoic.). Opting out of badge celebrations: 1 (Cal AI).
- Weekly rather than daily goals: 3 (Blinkist, Calm, WHOOP).
- Anti-patterns seen: a full-screen streak-loss moment with no repair or pause (Cal AI); a streak-save countdown on the lock screen (yope, surface 10); protection used as a currency upsell right at the loss moment (Duolingo refill).

**Value recaps (9)**
- Weekly: 6 (Babbel, MyFitnessPal, Headway, WHOOP, Oura, stoic.). Monthly: 1 (Strava). Yearly: 2 (Duolingo, Spotify).
- Shows week-on-week change: 1 (Headway).
- Recap plus trial notice on the same screen: 1 (Babbel).
- A recap with a share action: 1 (Spotify). Strava's story format is built for sharing.

**Trial-ending notices and timelines (9)**
- An in-app notice during the trial (not at the paywall): 3 (Duolingo full screen, Babbel strip, Monzo tab).
- Lists features the user actually used: 1 (Monzo). Lists generic benefits: 1 (Duolingo).
- The reminder promise repeated after the trial starts: 1 (Duolingo). The user picks the reminder timing: 1 (Duolingo Max).
- The reminder tied to the notification permission: 2 (Cal AI caveat, YNAB primer).

**Welcome back (6)**
- Offers a choice of how to re-enter: 1 (Runna). Resumes the last item directly: 3 (Skillshare, Brilliant, Quizlet). Greeting only: 1 (Lovi). A user-chosen pause: 1 (Tinder, and Finch in surface 5).
- None mention what the subscription still includes or what changed while the user was away.

**Rating prompts (8)**
- A sentiment gate before the store (yes/no or great/could be better): 3 of 8 (Ahead, ElevenLabs, Preply). Mobbin doesn't show the branch, but this two-way split is the shape of a pre-prompt that sends only happy users to the review dialog. Flag it, don't score it as best practice.
- In-app stars first, then a store ask: 2 (Insight Timer, BitePal).
- Asked right after a success moment: 2 (BitePal after the first log, Headway after the weekly recap).
- Asked before the product has been used (in onboarding): 1 (ABY Journal).
- Asks for a specific star count: 2 (ABY Journal, Revolut Business).

**Widgets and Live Activities (10)**
- Shows the user's own data (streak, calories) in the preview: 6 of 10.
- Tied to the streak: 5 of 10.
- A visible decline: 9 of 10. Ladder's has only an X.
- Gives how-to instructions (iOS has no add-widget API): 1 (Vocabulary).
- Live Activity as a Pro feature: 1 (Flighty). Live Activity used for streak urgency: 1 (yope).
