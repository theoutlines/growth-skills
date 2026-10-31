# Retention screens evidence: published tests, benchmarks and gaps

Collected 2026-10-30. Every number was read on the page it comes from. Part 1 is published tests and case studies (#R1–#R63). Part 2 is benchmarks from public reports (B1–B64). Never merge two rows into one number, and keep metric definitions apart (end of Part 2).

# Part 1. Published tests and case studies

Every number was read on the page it comes from. Cite rows as **#R1, #R2 …**. The `R` prefix keeps this list apart from the onboarding library (#1–#77), the cancel-flow library (#C1–#C28), the upsell library (#U1–#U50) and the web2app library (#W1–#W53).

**Tiers in the two parts.** Part 1 tiers grade a row as evidence that a *change* works. Part 2 tiers grade a benchmark as a *description* of what apps see. For priority, a benchmark is Medium at most.

## Tiers

- **Strong**: controlled A/B test or randomised experiment, with numbers on the page.
- **Directional**: numbers, but no stated method, a before/after comparison, users-who-saw vs users-who-didn't, bundled changes, a second-hand report, or a vendor aggregate.
- **Anecdotal**: no numbers (or a test is described but its figures are not published).
- **Observed**: seen in apps, no test.

Conventions:
- Lifts are **relative** unless marked "pp" (percentage points) or given as two absolute rates (a% → b%).
- The denominator is named when the page names it. "Denominator not stated" means the page doesn't say.
- Buckets are RevenueCat SOSA buckets. "AI" is a tag, not a bucket. Non-subscription products, games, lab studies and finance apps get **n/a**. "(inferred)" means the bucket comes from the app's description, not a checked store listing.
- Rows that already exist in the onboarding-teardown library (https://github.com/theoutlines/growth-skills/tree/main/plugins/growth-skills/skills/onboarding-teardown) are listed as **Same as onboarding #N**; rows from the upsell library as **Same as upsell #UN**. They keep their original numbers and are never renumbered.
- Bundled changes are flagged. Two tests are never merged into one number.
- **Vendor bias**: Phiture, Braze, Airship, OneSignal, CleverTap, Plotline, Taplytics, Kahuna and Appbot sell the channel or tool they report on. Their rows are vendor sources.
- Several rows are off-target (not a subscription app, or not a mobile screen). They are kept because the mechanism transfers, and the note says so. Off-target rows cap at Medium priority.

---

## A. Welcome screen after purchase or trial start

| ID | App | Category | Bucket | AI tag | Surface | Change | Metric | Result | Date | URL | Tier |
|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | Several (Headway, Flo, Beside) | Article on post-purchase screens | Education / Health & Fitness / Business (inferred) | no | Welcome screen after purchase (observed in Mobbin screenshots) | Author argues for a dedicated "what you now have" screen after purchase; describes Headway's community framing and Flo's lifetime offer after its welcome screen | Early retention (claimed) | Says apps with dedicated screens "see significantly higher early retention", with no figure. Context number the article quotes from SOSA 2026: "55.4% of 3-day trials are cancelled on Day 0" (second-hand; check the SOSA report before reusing) | Pub. 2026-05-05 | https://www.revenuecat.com/blog/growth/post-purchase-screen | Anecdotal (no test; vendor blog) |

See also **R48 / Same as onboarding #1** (Blinkist trial welcome screen with a reminder opt-in), which sits in section G.

## B. Notification permission primer and timing

| ID | App | Category | Bucket | AI tag | Surface | Change | Metric | Result | Date | URL | Tier |
|---|---|---|---|---|---|---|---|---|---|---|---|
| R2 | Duolingo | Language learning | Education | no | Push permission prompt copy (German learners) | Original "Duolingo needs to send you notifications" replaced by copy tying notifications to learning goals and habit-building | Notification opt-in | +8% opt-in for German learners | Pub. 2022-01-14 | https://blog.duolingo.com/copy-testing-experiments | Strong (A/B in Duolingo's experiment platform; no sample size) |
| R3 | Duolingo | Language learning | Education | no | Same prompt, Spanish | The R2 winning copy retested for Spanish-language learners | Notification opt-in | "had no significant impact" | Pub. 2022-01-14 | https://blog.duolingo.com/copy-testing-experiments | Strong (A/B; null result) |
| R4 | Duolingo | Language learning | Education | no | Push permission ask (Japan) | Local research found Japanese learners opt in less; follow-up experiments moved the prompt, changed its pitch and added asks in new contexts (leaderboard promotion, running out of hearts) | Notification opt-in | Japanese learners "50% less likely to opt into receiving reminder notifications" (analysis, not a test). No results published for the follow-up experiments | Pub. 2021-02-02 | https://blog.duolingo.com/lessons-from-asia-turning-local-research-into-global-experiments | Directional (observational figure; experiments unreported) |
| R5 | Cluster | Private photo-sharing | Photo & Video (inferred) | no | Push pre-permission screen | All permission prompts at first launch replaced by a benefit explanation before the iOS prompt | Push acceptance | First launch "only about 30-40 percent of users accepted"; with explanation, under 40% → 66%. Asking only after the user taps "Notify Me" while inviting friends: 100% in user testing (dozens of people) | Pub. 2014-04-04 | https://techcrunch.com/2014/04/04/the-right-way-to-ask-users-for-ios-permissions/ | Directional (own tests, small samples, no method) |
| R6 | Cluster | Private photo-sharing | Photo & Video (inferred) | no | Photos permission timing and double dialog | Photo prompt moved from right after "Create Cluster" to after the user taps a camera icon and "Choose Photos"; custom first dialog before the system one | Photo access granted | 67% → 89% granted. With the double dialog, 3% of "Give Access" tappers then denied, so under 2% of all users denied at system level; 46% who declined the custom dialog granted later when asked again | Pub. 2014-04-04 | https://techcrunch.com/2014/04/04/the-right-way-to-ask-users-for-ios-permissions/ | Directional (off-target: photos, not push; small tests) |
| R7 | Houseparty | Group video chat | Social & Lifestyle (inferred) | no | Onboarding permission screens | Messaging, order and imagery varied; a screen explaining why access matters shown before each system pop-up | Push opt-in; contacts access | Push opt-in +9%; contact access +15% | Not dated | https://taplytics.com/blog/house-party-ab-test-onboarding-flow | Directional (A/B named by vendor; no baseline, no primary source; pre-purchase onboarding) |
| R8 | Crossfader | DJ / music | Media & Entertainment (inferred) | no | In-app tutorial explaining push before the system ask | Tutorial that explains push's role, then the request | Push enablement rate | 55%, vs a quoted 44% "industry average" for News & Media apps | Pub. 2014-08-06 | https://andrewchen.com/why-people-are-turning-off-push/amp | Directional (vendor data, Kahuna; compared with an industry average, not a control) |
| R9 | onX Hunt | Hunting maps | Utilities (inferred) | no | iOS push pre-permission window (new users) + win-back push to settings (opted-out users) | Native prompt replaced by a two-button in-app window; system prompt fires only on accept, so a dismiss keeps the one system ask | Push opt-in rate | Baseline 49.7% for new iOS users; "overall opt-in rate increase of 10.6%" after copy and design iterations (relative or pp not stated) | Not dated (page modified 2026-05-04) | https://phiture.com/success-stories/onx-inapp/ | Directional (vendor; bundled with a win-back push; control not described) |
| R10 | Headspace | Meditation | Health & Fitness | no | Segment-targeted in-app opt-in messages | Free trialists (Germany): opt in "so they could be reminded when their free trial ends". Subscribers: nudge in onboarding without interrupting a session (German) or on app open unless a meditation had started (English); message window extended to 3 weeks | Push opt-ins | German free trialists +118.35%; English-language members in GDPR countries who completed one meditation +157.05% (no baselines) | Not dated (page modified 2024-11-11) | https://phiture.com/success-stories/headspace-inapps/ | Directional (vendor; control not described; several segments and copies) |
| R11 | Fishbrain (Phiture) | Fishing | Not verified (Sports) | no | Push pre-permission inside a CRM programme | **Same as upsell #U41.** Push pre-permission, in-app surveys and email, measured against unexposed control groups | Paid conversions within a day; W6 retention | +14.9%; W6 retention +50.6% vs control (no baselines). The pre-permission's own effect is not separated | Not dated (award 2019) | https://phiture.com/success-stories/fishbrain-crm/ | Directional (bundled) |
| R12 | Talabat (Delivery Hero) | Food delivery | n/a (not a subscription app) | no | In-app message for iOS provisional authorisation | Animated in-app message showing how to reveal the first quiet push and opt in for more, for iOS 12+ users who had not opted in | Reachable iOS base | +36% reachable iOS base (no baseline, no control) | Not dated (iOS change late 2019) | https://braze.com/customers/delivery-hero-provisional-push | Directional (vendor; off-target) |
| R13 | Unnamed (Phiture interviews) | Several | n/a | no | iOS provisional authorisation vs the standard prompt | Provisional (quiet) authorisation instead of the system prompt at launch | Opt-in; D1, D3, D7 retention | Companies reported "the same opt-in rate"; D1, D3 and D7 retention "looked similar" (no figures, no apps named) | Pub. 2020-04-08 | https://phiture.com/blog/provisional-push-what-is-it-and-how-will-it-impact-your-addressable-audience/ | Anecdotal |
| R14 | Cross-category (OneSignal benchmarks) | Benchmark | Several | no | Push opt-in rate by category | None (benchmark) | Push opt-in rate, iOS / Android | Health & fitness 33.5% / 43.2%; Education 37.1% / 39.7%; Productivity 44.8% / 53.6%; Utilities 51.6% / 51.5%; Lifestyle 34% / 38.8%; Entertainment 27% / 40.3%. Page also says in-app messages before the native prompt "significantly" raise opt-in (no figure) | 2024 report (page undated) | https://onesignal.com/mobile-app-benchmarks-2024 | Directional (vendor aggregate) |
| R15 | Cross-category (Airship benchmarks) | Benchmark | Several | no | Push opt-in rate; onboarding opt-in campaigns | None (benchmark) | Push opt-in rate | Median iOS 48.85%, Android 53.3%; Education iOS 90th percentile 88.7%; apps running onboarding campaigns see opt-in "as high as 40% above their category average" | Page modified 2026-06-05 | https://www.airship.com/mobile-app-push-notification-benchmarks-for-2026/ | Directional (vendor aggregate; the 40% is a ceiling, not an average) |
| R16 | Cross-category (Airship) | Benchmark | Several | no | Push opt-in status vs retention | None (correlation) | Retention of opted-in vs opted-out users | iOS users opted in to push "are retained at nearly 2x the rate" of those who aren't | Pub. 2021-05-22 | https://www.airship.com/blog/7-mobile-engagement-statistics-that-show-how-push-notifications-boost-roi/ | Directional (vendor; correlational, self-selected) |
| R62 | Badoo | Dating | Social & Lifestyle | no | Permission screens | Permission prompts on the home screen → a separate explainer screen for each permission | Conversion | Conversions went down (no figures) | Pub. 2022-10 | https://adapty.io/blog/subhub-podcast-16-vivid-money/ | Anecdotal (no figures) |

## C. Reminder and habit setup

| ID | App | Category | Bucket | AI tag | Surface | Change | Metric | Result | Date | URL | Tier |
|---|---|---|---|---|---|---|---|---|---|---|---|
| R17 | Calm | Meditation | Health & Fitness | no | Reminder-setup screen after the first session | **Same as onboarding #7.** After the first session, a screen prompts a portion of new users to set a daily reminder | Retention; reminder adoption | Retention about 3x for prompted users; 40% of prompted users set a reminder (vs <1% who found it in Settings) | Pub. 2016-07-14 (restated 2017-04-12) | https://amplitude.com/blog/calm-increased-retention-amplitude ; https://amplitude.com/blog/2017/04/12/meditate-every-day | Directional (holdout implied, no baseline numbers; vendor) |
| R18 | Unnamed (Adapty data) | Education | Education | unknown | Reminder setup placement | **Same as onboarding #16.** Reminder setup inside onboarding vs on the home screen | Trial conversion; ARPU | +6.4% trial conversion; +24% ARPU | Pub. 2025-11-25 | https://adapty.io/blog/how-to-fix-your-onboarding-flow/ | Directional |
| R19 | Unnamed sustainability app | Sustainability | n/a | unknown | Commitment screen | **Same as onboarding #25.** One commitment screen added to onboarding (pre-purchase; relevant as the goal-commitment pattern) | D30 retention | Doubled | Pub. 2025-11-17 | https://www.revenuecat.com/blog/growth/fix-onboarding-funnels/ | Directional |

The streak wager (R28) is also a commitment screen; it sits in section E.

## D. First-week guidance (checklists, feature discovery, tooltips)

| ID | App | Category | Bucket | AI tag | Surface | Change | Metric | Result | Date | URL | Tier |
|---|---|---|---|---|---|---|---|---|---|---|---|
| R20 | Mural | Whiteboard | Business | no | First-session checklist | **Same as onboarding #30.** Five-step checklist replaced pop-ups and banners | 1-week retention | +10% relative | Not dated | https://abtest.design/tests/onboarding-checklist | Directional (listed as A/B; design not described; web B2B, off-target for mobile) |
| R21 | Step | Teen banking | n/a (Finance) | no | First-open guided walkthrough (4 tooltips) on home; pinned banner | Walkthrough for new users on first open after sign-up; separate banner surfacing Auto-Reload | Users who "add money"; Auto-Reload enablement | Saw walkthrough: ~45% more likely to add money. Saw banner: ~14% higher Auto-Reload enablement | Not dated ("last 3 months") | https://www.plotline.so/success-stories/step-sees-an-uplift-in-users-starting-their-financial-journey/ | Directional (vendor; saw vs didn't see, no stated randomisation; off-target) |
| R22 | Blinkist (Phiture) | Book summaries | Education | no | Session-start in-app message to premium users | New-release message at session start promoting the latest title, to premium English-speaking users, over two weeks | Book add rate; start rate | Overall add rate +6.62%; overall start rate +6.55%; 90% CTR. Also "3220%" and "4367%" uplifts on the promoted title itself (no baseline) | Not dated (page modified 2024-11-11) | https://phiture.com/success-stories/blinkist-inapp/ | Directional (vendor; no control described) |
| R23 | Headspace (Phiture) | Meditation | Health & Fitness | no | In-app modals + push + email | **Same as upsell #U40.** CRM programme with dynamic in-app modals and rich push deep-linking to packs | Paid conversions within 1 day; W1 retention | +49% paid conversions within a day (no baseline); W1 retention +109% vs control | Not dated | https://phiture.com/success-stories/headspace-retention/ | Directional (bundled; the in-app part is not separated) |
| R24 | The Tapping Solution | Meditation (EFT tapping) | Health & Fitness (inferred) | no | "Recommended for you" in-app message after onboarding | Message pointing new users to their first meditation | First meditation started | "Been effective at driving users to start their first meditation" (no figures) | Not dated | https://braze.com/resources/articles/how-the-tapping-solution-uses-braze-to-boost-engagement-and-drive-subscriptions | Anecdotal (vendor) |

## E. Streaks, progress, goals, achievements, streak freeze or repair

| ID | App | Category | Bucket | AI tag | Surface | Change | Metric | Result | Date | URL | Tier |
|---|---|---|---|---|---|---|---|---|---|---|---|
| R25 | Duolingo | Language learning | Education | no | Streak rule | **Same as onboarding #74.** Streak decoupled from the daily goal (one lesson keeps the streak) | D14 retention; learners on a streak; DAU | D14 retention +3.3%; daily active learners +1%; daily learners on a streak +10.5% in 20 days (+19% for new learners); learners on a 7+ day streak +40% a year later; fewer users hit their daily goal | Pub. 2020-11-19 | https://blog.duolingo.com/improving-the-streak/ | Strong (company A/B) |
| R26 | Duolingo | Language learning | Education | no | Streak-extended screen (milestone animation) | Elaborate animation on the post-lesson streak screen on milestone days | New learners still active 7 days later | +1.7% | Pub. 2022-01-31 | https://blog.duolingo.com/how-duolingo-streak-builds-habit/ | Directional (method not stated on the page) |
| R27 | Duolingo | Language learning | Education | no | Streak Freeze inventory | Learners can equip up to two Streak Freezes instead of one | Relative number of daily active learners | +0.38% | Pub. 2022-01-31 | https://blog.duolingo.com/how-duolingo-streak-builds-habit/ | Directional (method not stated on the page) |
| R28 | Duolingo | Language learning | Education | no | Streak Wager (commitment screen after a lesson) | Learners spend in-game currency to bet they keep the streak 7 more days; success doubles the stake | D1, D7, D14 retention | Statistically significant gains at D1, D7 and D14; largest at D7: +14% | Pub. 2017-05-10 | https://blog.duolingo.com/how-streaks-keep-duolingo-learners-committed-to-their-language-goals/ | Strong (A/B vs control) |
| R29 | Duolingo | Language learning | Education | no | Weekend Amulet (streak protection item, offered Fridays) | Store item that keeps the streak through the weekend without practice | Return a week later; streak loss | 4% more likely to return a week later; 5% less likely to lose the streak | Pub. 2017-05-10 | https://blog.duolingo.com/how-streaks-keep-duolingo-learners-committed-to-their-language-goals/ | Strong (A/B) |
| R30 | Duolingo | Language learning | Education | no | Streak counter always visible at the top of the app | Show streak days at the top of the app at all times | DAU; D14 retention | DAU +3%; D14 +1% | Not dated | https://econsultancy.com/six-a-b-tests-used-by-duolingo-to-tap-into-habit-forming-behaviour/ | Directional (second-hand report of a conference talk; speaker and date not identified) |
| R31 | Duolingo | Language learning | Education | no | Streak emphasised after every lesson ("ring of fire") | Streak celebration shown at the end of each lesson | DAU; D14 retention | DAU +1%; D14 +3% | Not dated | https://econsultancy.com/six-a-b-tests-used-by-duolingo-to-tap-into-habit-forming-behaviour/ | Directional (second-hand) |
| R32 | Duolingo | Language learning | Education | no | Sign-up congratulation badge | One badge for signing up | DAU, D14, all other metrics | 0% on every metric | Not dated | https://econsultancy.com/six-a-b-tests-used-by-duolingo-to-tap-into-habit-forming-behaviour/ | Directional (second-hand; null) |
| R33 | Duolingo | Language learning | Education | no | Wider range of achievement badges | More badges for a wider range of actions | DAU; D14; IAP | DAU +2%; D14 +2%; IAP +5% | Not dated | https://econsultancy.com/six-a-b-tests-used-by-duolingo-to-tap-into-habit-forming-behaviour/ | Directional (second-hand) |
| R34 | Duolingo | Language learning | Education | no | Tiered badges | Badges with levels | DAU; D14 | DAU +1%; D14 +1% | Not dated | https://econsultancy.com/six-a-b-tests-used-by-duolingo-to-tap-into-habit-forming-behaviour/ | Directional (second-hand) |
| R35 | Duolingo | Language learning | Education | no | Leaderboards (weekly leagues) | League system modelled on game leaderboards | Learning time; highly engaged learners; D1/D7 retention | Overall learning time +17%; highly engaged learners (1+ hour/day, 5 days/week) tripled; D1 and D7 retention improved "materially and with statistical significance" (no figures) | Pub. 2023-02-28 | https://lennysnewsletter.com/p/how-duolingo-reignited-user-growth | Directional (former CPO's account; test design not stated) |
| R36 | Duolingo | Language learning | Education | no | Friend Streak (shared streak, up to 5 friends) | Shared streak that breaks if either friend misses a day | Daily lesson completion | Learners with at least one Friend Streak are 22% more likely to complete their daily lesson | Pub. 2024-09-20 (same figure 2023-06-06) | https://blog.duolingo.com/product-lessons-friend-streak/ | Directional (observational "our data"; self-selected) |
| R37 | Lab study (Silverman & Barasch, Study 2) | Exercise (simulated app log) | n/a | no | Behaviour log showing an intact vs broken streak | Same past behaviour shown as an intact or a broken streak | Choosing the target behaviour again | Intact 66.23% vs broken 57.86% (n = 601 recruited; p = .035) | JCR, online 2022-06-30 | https://udspace.udel.edu/bitstreams/7e3e3b64-8bf2-4527-ac93-94a160358165/download | Strong (randomised online experiment; off-target: not a live app) |
| R38 | Lab study (Silverman & Barasch, Study 3) | Language learning (simulated) | n/a | no | Streak log present vs absent | Log shown or hidden, crossed with intact vs broken streak | Engagement in the target behaviour | Intact: log 92.47% vs no log 64.94%. Broken: log 45.21% vs no log 60.90% (n = 602 recruited) | JCR, online 2022-06-30 | https://udspace.udel.edu/bitstreams/7e3e3b64-8bf2-4527-ac93-94a160358165/download | Strong (randomised online experiment; off-target) |
| R39 | Lab study (Silverman & Barasch, Study 7) | Games (simulated) | n/a | no | Streak repair | Broken streak that can be repaired vs one that can't | Engagement in the target behaviour | Intact 93.14%; repairable broken 85.20%; unrepairable broken 68.66% (n = 601 recruited; repair vs broken OR = 2.63) | JCR, online 2022-06-30 | https://udspace.udel.edu/bitstreams/7e3e3b64-8bf2-4527-ac93-94a160358165/download | Strong (randomised online experiment; off-target) |
| R40 | Conecta Ideas (Aulagnon, Cristia, Cueto, Malamud) | Math practice for 4th–6th graders, Peru | Education (inferred; free school app) | no | Streak-highlighting message (app notification, shown in-app if push was off) | 60,000 students randomised: streak message, personalised reminders, generic reminders, or no messages (control 40%) over a 6-week summer break | Connected at least once; share of weeks connected; math score | Streak arm: +2.8 pp connected at least once (control 5.3%); +9.4 pp share of weeks connected among those who connected (control 31.7%), vs +6.9 pp personalised and +2.5 pp generic reminders; math +0.13 to 0.17 SD (not significantly different from other arms; endline n = 1,503) | Working paper 2026-02-19 | https://www.ipr.northwestern.edu/documents/working-papers/2026/wp-26-05.pdf | Strong (RCT; delivered as a notification, so check scope; draft paper) |
| R41 | Café loyalty card (Kivetz, Urminsky, Zheng) | Coffee shop | n/a | no | Progress card with bonus stamps (illusionary progress) | 12-stamp card with 2 pre-filled vs plain 10-stamp card; both need 10 purchases | Days to complete 10 purchases | 12.7 vs 15.6 days, "nearly three days or 20% faster" (p < .05) | JMR 2006 | https://business.columbia.edu/sites/default/files-efs/pubfiles/1200/goalgradient.pdf | Strong (field experiment; off-target: physical card) |
| R42 | Car wash loyalty card (Nunes & Drèze) | Car wash | n/a | no | Endowed progress (10 steps with 2 done vs 8 steps) | Same 8 purchases framed as a 10-step card with 2 already stamped | Completion likelihood; completion time | Abstract says completion goes up and time goes down; the rates are not on the fetched page (full text paywalled; PDF blocked by robots.txt) | JCR 2006 | https://ideas.repec.org/a/oup/jconrs/v32y2006i4p504-512.html | Anecdotal (on the page we could read) |
| R43 | 8fit | Workouts and meal plans | Health & Fitness | no | Streak campaign across push, email and in-app messages | Personalised messages to keep workout streaks alive, split by whether the user kept the streak | Weekly class views; users completing classes; free-to-paid | Weekly class views +40%; users completing classes +17%; free-to-paid conversion 13% | Not dated | https://braze.com/customers/8fit-case-study | Directional (vendor; bundled channels; no control stated) |
| R44 | Lumosity (Braze) | Brain training | Education | no | Premium progress report unlocked after a 3-day streak | **Same as upsell #U47.** New Year campaign: temporary premium access, a progress report unlocked after a 3-day streak, then a sale (email + in-app) | Streak completion; engagement; purchase likelihood | Streak completion +350%; free-user engagement +170% vs the prior year's single email; sale recipients 11% more likely to buy than non-recipients | Not dated | https://braze.com/customers/lumos-labs-case-study | Directional (bundled; no randomised control described) |
| R45 | Headspace | Meditation | Health & Fitness | no | Streak display setting | Users can hide their streaks | n/a | No figures | Pub. 2024-10-18 | https://builtformars.com/ux-bites/hiding-your-headspace-streaks | Observed |
| R63 | Duolingo | Language learning | Education | no | Lesson mechanic | Moves counter from a match-3 game: limited chances to answer before the lesson restarts | Retention; DAU | "Completely neutral" (no figures) | Pub. 2023-02-28 | https://www.lennysnewsletter.com/p/how-duolingo-reignited-user-growth | Anecdotal (no figures) |

## F. Value recaps (weekly progress, "you've done X", year in review)

| ID | App | Category | Bucket | AI tag | Surface | Change | Metric | Result | Date | URL | Tier |
|---|---|---|---|---|---|---|---|---|---|---|---|
| R46 | Blinkist (Phiture) | Book summaries | Education | no | Year-in-review story (in-app message, Story format) | "Year in Blinks" recap on mobile in two versions: community stats or personal stats per active user | Renewal; premium content starts; new-user revenue | Recipients "51% more likely to renew their subscription"; 130% of the premium-content-starts goal; 104% of the new-user revenue goal | Not dated (filename suggests Dec 2023) | https://phiture.com/success-stories/blinkist-inapps/ | Directional (vendor; recipients vs others, no holdout; the two versions not compared) |
| R47 | Stash | Investing | n/a (Finance) | no | Portfolio screen showing what the user has put in | Individual investment amounts shown, not only the total portfolio value | Users keeping automatic saving on | "12% more users kept automatically saving even 8 months later" | c. 2019-01 (from the original URL) | https://abtest.design/tests/displaying-individual-investment-amount | Strong (A/B per the write-up; second-hand, the original Apptimize post now redirects; off-target) |

## G. In-app trial-ending notices and trial timelines

| ID | App | Category | Bucket | AI tag | Surface | Change | Metric | Result | Date | URL | Tier |
|---|---|---|---|---|---|---|---|---|---|---|---|
| R48 | Blinkist | Book summaries | Education | no | Trial timeline + trial welcome screen with reminder opt-in | **Same as onboarding #1.** Paywall shows a day-by-day 7-day trial timeline; a trial welcome screen offers a reminder opt-in, with a push 2 days before the trial ends | Trial sign-ups; complaints; push opt-in; in-trial cancels | +23% trial sign-ups; −55% complaints; push opt-in 6% → 74%; −4% in-trial cancellations | Pub. 2021-01-19 | https://uxplanet.org/how-solving-our-biggest-customer-complaint-at-blinkist-led-to-a-23-increase-in-conversion-b60ad514134b ; https://abtest.design/tests/how-your-free-trial-works | Strong (A/B; bundled timeline + reminder) |
| R49 | Slopes | Ski tracker | Health & Fitness | no | Pass picker explaining the trial reminder before the trial; permission prompt after | Reminder explained before starting the trial, notification permission asked afterwards | Trial starts | +4% trial starts (another developer reported +3% from a similar change) | Pub. 2021-04-05 | https://blog.curtisherbert.com/slopes-diaries-39-risky-business/ | Directional (behind an A/B flag; indie self-report, no sample) |
| R50 | Slopes | Ski tracker | Health & Fitness | no | Day-5 trial reminder opt-in (7-day trial) | Users opt in to a reminder on day 5, tailored to their activity | Opt-in; day-0 cancels; trial-to-paid; refunds | About 75% of trial starters asked to be reminded; day-0 cancels dropped sharply (no figure); trial-to-paid for opted-in users −7.8% vs baseline; refund requests equal. Test turned off after 2 weeks | Pub. 2021-04-05 | https://blog.curtisherbert.com/slopes-diaries-39-risky-business/ | Directional (A/B per author, but opted-in users vs baseline; no sample) |
| R51 | Shaw Academy | Online courses | Education | no | Trial-end reminder (email) | **Same as onboarding #65.** Reminder email 3 days before trial end | Sales | +14% (>99% significance) | Not dated | https://abtest.design/tests/free-trial-reminder | Strong (channel is email: context only for an in-app notice) |

## H. Return screen after inactivity

| ID | App | Category | Bucket | AI tag | Surface | Change | Metric | Result | Date | URL | Tier |
|---|---|---|---|---|---|---|---|---|---|---|---|
| R52 | Duolingo | Language learning | Education | no | Returning ("resurrected") learners, 30+ days away | None tested: analysis of returners; a re-onboarding experience was "being built" (no results) | Share who resurrect; 7- and 14-day retention of returners | About 5% of users resurrect after 30+ days; resurrected users "roughly 20% less likely than a new user to be retained" | Pub. 2017-08-30 | https://blog.duolingo.com/back-from-the-brink-what-duolingo-learned-about-its-resurrected-users | Directional (observational baseline, no change tested) |

## I. In-app rating and review prompts

| ID | App | Category | Bucket | AI tag | Surface | Change | Metric | Result | Date | URL | Tier |
|---|---|---|---|---|---|---|---|---|---|---|---|
| R53 | WordBoard | Keyboard phrases | Utilities (inferred) | no | System rating prompt timing | Prompt moved earlier: after one key added (before: after several uses or a purchase); at least 4 months between prompts | Ratings per month; average rating | Ratings per month +400%+; average stayed around 4.84 | Pub. 2023-11-17 | https://appbot.co/blog/app-ratings-reviews-strategy-experiment/ | Directional (before/after; vendor author) |
| R54 | 7 Minute Workout | Workouts | Health & Fitness (inferred) | no | System rating prompt timing | Prompt after one completed workout (before: after several workouts or a purchase) | Rating volume; average rating | Volume grew "significantly" and the average, already trending up, rose (no figures) | Pub. 2023-11-17 | https://appbot.co/blog/app-ratings-reviews-strategy-experiment/ | Anecdotal |
| R55 | CleverTap (own app) | Marketing SDK | n/a | no | SKStoreReviewController after engagement | Native review request after users show engagement, with a per-version limit | 5-star ratings | +50% 5-star ratings (no baseline or period) | Pub. 2017-05-01 | https://clevertap.com/blog/improve-ios-app-ratings-with-skstorereviewcontroller/ | Directional (vendor; before/after) |
| R56 | Tokopedia | Marketplace | n/a (not a subscription app) | no | Google Play In-App Review API | In-app review sheet instead of sending users to the store | 5-star ratings | "Increased by 4x" since implementing | Pub. 2020-08-05 | https://android-developers.googleblog.com/2020/08/in-app-review-api.html | Directional (before/after; platform owner's blog) |
| R57 | Calm | Meditation | Health & Fitness | no | Google Play In-App Review API | Same as R56 | Positive ratings and reviews | "Almost immediate increase" (no figures) | Pub. 2020-08-05 | https://android-developers.googleblog.com/2020/08/in-app-review-api.html | Anecdotal |

## J. Home-screen widget and Live Activity prompts

| ID | App | Category | Bucket | AI tag | Surface | Change | Metric | Result | Date | URL | Tier |
|---|---|---|---|---|---|---|---|---|---|---|---|
| R58 | Duolingo | Language learning | Education | no | Streak widget + in-app widget promotion after a lesson | iOS widget (July 2022); tested instruction flows, incl. an in-app promotion shown after a lesson | Retention; widget installs | Widget users had "far better retention" even after accounting for higher commitment (no figures); installs "skyrocket" after the in-app promotion (no figures). Half of learners with the widget have a 6-month+ streak (descriptive) | Pub. 2023-08-29 | https://blog.duolingo.com/widget-feature | Anecdotal (no effect sizes) |
| R59 | Gratitude | Gratitude journal | Health & Fitness (inferred) | no | In-app bottom sheet to pin a home-screen widget (Android) | In-app widget pinning prompt; re-prompt for users whose widgets were removed by an update | Retention of widget users; widget adoption | "25% increase in retention for widget users" (baseline not given); widgets used by 10% of DAU; ~1K weekly journal entries from widgets | Pub. 2026-05-08 | https://android-developers.googleblog.com/2026/05/how-gratitude-widgets-boosted-user-retention-25-percent.html | Directional (method not stated; likely self-selected) |
| R60 | Hahow | Online courses | Education (inferred) | no | Dynamic Island / Live Activity "Learning Records" with weekly medals | Live Activity tracking daily learning time against a 15-minute goal; control without it; 4 weeks | Learning time | Treatment averaged 40 minutes a week; result "insignificant"; no sample or control figure | Dec 2022 | https://pattychien.super.site/more-ive-done/app-learning-records-project-dynamic-island-ab-testing | Anecdotal (A/B, null, no comparison figures; designer portfolio) |
| R61 | Duolingo | Language learning | Education | no | Live Activity / Dynamic Island used for a "Super offer" | Users reported a subscription promotion shown as a Live Activity | Complaints | Multiple Reddit reports; could not be reproduced and may have been stopped. Apple's guideline: "Don't use a Live Activity to display ads or promotions" | Pub. 2026-01-02 | https://www.macrumors.com/2026/01/02/duolingo-dynamic-island-ad/ | Observed (compliance flag, not legal advice) |

---

## Strongest findings (Part 1)

- **Make the streak easy to keep and cheap to save.** Duolingo's strongest retention wins are all about lowering the bar or protecting the streak: one lesson extends it (R25: D14 +3.3%, learners on a 7+ day streak +40%), the Weekend Amulet (R29: 4% more likely to return, 5% less likely to lose it), the Streak Wager (R28: D7 +14%). Freezes and repair help too (R27; R39: a repairable broken streak keeps 85.20% engagement vs 68.66% unrepairable).
- **A broken streak on screen can do more harm than no streak at all.** In R38, showing a log with a broken streak cut engagement to 45.21%, below the 60.90% of people who saw no log. The streak screen needs a designed "broken" state (repair, reset framing, or hide), not only a "kept" state.
- **Where the streak is shown matters, with small effects.** Always-visible counter: DAU +3%, D14 +1% (R30); post-lesson celebration: DAU +1%, D14 +3% (R31); milestone animation: D7 +1.7% (R26). A single sign-up badge did nothing (R32); a wider badge range did (R33). These are second-hand or method-free reports, so treat sizes as directional.
- **Highlighting a streak beats a generic reminder.** In a 60,000-student RCT (R40), streak-highlighting messages raised the share of weeks connected by 9.4 pp vs 2.5 pp for generic reminders. Only the message content changed, which supports streak framing on reminder and recap screens.
- **Permission asks: explain the value and ask in context.** The only strong test is copy (R2: +8% opt-in for German learners with copy tied to the learner's goal), and it did not transfer to Spanish (R3). The primer and timing rows (R5–R10) all point the same way but are directional, vendor or small samples.
- **Ask for the reminder after the first value moment.** Calm's post-session reminder screen (R17: about 3x retention, 40% set a reminder vs <1% in Settings) and Blinkist's trial welcome screen (R48: push opt-in 6% → 74%) are the two best-evidenced reminder screens.
- **Progress framing works in the field.** Pre-filled progress speeds completion (R41: 12.7 vs 15.6 days). Showing users what they've put in kept more of them saving (R47: +12% at 8 months). Both are off-target, so cap at Medium.
- **A value recap tied to renewal is promising but untested.** Blinkist's Year in Blinks recipients were 51% more likely to renew (R46), with no holdout.

## Where it flips (Part 1)

- **Trial reminder: honesty vs conversion.** Blinkist's reminder screen raised trial sign-ups +23% and cut in-trial cancels −4% (R48). Slopes copied it: day-0 cancels dropped and 75% opted in, but trial-to-paid fell 7.8% for opted-in users and the test was stopped (R50). The author's reading: a reminder that asks "do you still want this?" invites a second value check; one that sends users back to a feature they haven't used may not. The sign depends on whether the user gets value before the reminder fires (Slopes is used at the ski resort, not at home on day 5).
- **Streak goal vs daily goal.** Decoupling the streak from the daily goal raised retention and streak counts but fewer users hit their daily goal (R25). More users kept going; each did less per day.
- **Visible streak vs broken streak.** A streak log boosts engagement while it's intact (92.47% vs 64.94% with no log) and lowers it after a break (45.21% vs 60.90%) (R38). Self-blame for the break makes it worse (Study 6 on the same page: 28.87% after a self-attributed break vs 42.00% external). Headspace lets users hide streaks (R45), which suggests the same cost in practice.
- **Promotional use of a retention surface.** A subscription promo in a Live Activity drew complaints and breaks Apple's Live Activity guideline (R61). Duolingo's offline-lesson Plus ad (upsell #U4) raised sign-ups but cut retention and DAU. Retention surfaces lose their effect when they turn into ad slots.
- **Copy wins don't travel.** The German permission copy that lifted opt-in +8% had no significant effect in Spanish (R3); Japanese learners opted in 50% less to begin with (R4). Re-test primer copy per market.
- **Rating prompts asked earlier.** The worry is that an earlier ask lowers the average. In R53 and R54 volume rose and the average held or rose, but both are before/after on apps already rated above 4.8.
- **Provisional push.** Reach goes up (R12: +36% reachable base) but opt-in and early retention looked the same as the standard prompt (R13). More reach is not more engagement.
- **Small wins can be costly at scale.** Two equipped freezes added only +0.38% daily actives (R27); the Hahow Live Activity showed no significant effect (R60). Not every streak or Live Activity feature pays back.

## Gaps (no public test found)

- **Welcome screen after purchase or trial start ("what you now have").** No public A/B test of the screen itself. Only Blinkist's bundled trial welcome + reminder (R48) and an anecdotal RevenueCat article (R1).
- **Notification permission timing after the first value moment vs at launch.** Only small or vendor reports (R5, R7, R10). No controlled test in a subscription app comparing ask-at-launch with ask-after-first-session. No WWDC session with numbers was found on provisional authorisation or primers.
- **Reminder time picker and goal-setting screens after purchase.** Only Calm (R17) and the onboarding rows R18–R19. No test of default reminder time, goal difficulty presets or weekly-goal vs daily-goal screens for payers. (An academic study of goal difficulty in an investment app exists, but it is observational and has no retention figure.)
- **First-week checklists in mobile subscription apps.** Only Mural (web B2B, R20) and vendor tooltip cases (R21, R22). No mobile checklist test with retention numbers.
- **Empty states for new payers.** Nothing found.
- **Achievements and badges in a subscription app.** Only Duolingo's second-hand figures (R32–R34). Hamari's peer-to-peer marketplace field study (Computers in Human Behavior, 2017) reports badges raised activity, but the page shows no effect sizes, so it is not listed.
- **Weekly progress recap in-app.** The only controlled recap result found is an email (Lifesum weekly progress report, D7 +14% and D14 +62% vs control, Braze community post), which is outside this scope, so it is not listed as a row. No in-app weekly recap test.
- **Year-in-review.** Only Blinkist (R46, no holdout). Wikipedia app Year in Review experiment pages on mediawiki.org could not be fetched (not found).
- **In-app trial-ending notice or trial countdown inside the app (not the paywall).** None; the evidence is reminder push or email (R48, R50, R51).
- **Return screen after inactivity ("welcome back", re-onboarding).** Only Duolingo's baseline (R52). No published test of a returning-user screen.
- **Rating prompt timing in a subscription app with a controlled split.** Only before/after (R53–R57). Babbel's "ratings volume +64% with In-App Review API" case study on Google Play could not be fetched (permission not granted), so its number is not used.
- **Live Activities in subscription apps.** Only a null portfolio A/B (R60) and a compliance incident (R61). Vendor Live Activity cases found are sports media, not subscription apps.
- **Widget prompt A/B with numbers.** Duolingo (R58) gives no effect sizes; Gratitude (R59) does not state a method.

## Pages not used

- Lenny's Podcast "Behind the product: Duolingo streaks" (Dec 2024): the figures circulating for it (two vs three freezes, "7x more likely" goal copy, ~10,000 incremental DAU from streak copy) appear only in a third-party transcript summary (recall.it), not on the Lenny's page, so they are not used.
- Taplytics "How Duolingo A/B tested their push notifications" (+5% DAU): no primary source named; push copy is out of scope.
- Lazyweb research pages on Duolingo experiments: they cite a Twitter thread, not Duolingo; not used.
- Nunes & Drèze full text (USC PDF): blocked by robots.txt; only the abstract was read (R42).
- Apptimize original Stash post: redirects to airship.com; R47 relies on abtest.design.
- Google Play Babbel case study: fetch not permitted.
- UXCam Inspire Fitness case: the numbers describe adopting an analytics tool, not a screen change.


# Part 2. Benchmarks

Checked 2026-10-30. Public numbers that frame the screens between the first purchase (or trial start) and the first renewal.

Tiers:
- **Strong benchmark**: a large panel whose size, period and metric are stated.
- **Directional**: a vendor aggregate whose method, denominator or panel is unclear, or an old or stale figure.
- **Single app**: one company's own product data (A/B results are marked "company A/B"). Not a benchmark; use as a reference point only.

Sources used throughout:
- **SOSA 2026** = RevenueCat, *State of Subscription Apps 2026*. 115,000+ apps, $16B+ revenue, App Store + Google Play + web, apps using RevenueCat. Target period: calendar 2025 (some renewal metrics use 2024 cohorts). Medians unless stated. Page: https://www.revenuecat.com/state-of-subscription-apps . Values come from the report; the headline figures marked "(web)" were re-checked on the web page on 2026-10-30. The page shows no publish date.
- **SOIS 2026** = Adapty, *State of In-App Subscriptions 2026*. 16,000+ apps, $3B+ revenue, mostly App Store, calendar 2025, benchmarks computed per app and then aggregated. Page (behind an email form): https://adapty.io/state-of-in-app-subscriptions-report/ .. Curve values were read from chart geometry (about ±1–2 points); bar values are exact.
- Rows copied from the onboarding library (https://github.com/theoutlines/growth-skills/tree/main/plugins/growth-skills/skills/onboarding-teardown, `evidence.md` Part 2) are marked **"Same as onboarding Part 2 row …"** and keep their original source. Those rows have no numbers, so the original row label is used. Nothing is renumbered.

Cite benchmarks as **B1, B2 …**.

---

## 1. Trial window: when trials start, convert and get cancelled

| ID | Benchmark | Number | Definition and denominator | Source, date | Tier |
|---|---|---|---|---|---|
| B1 | Trial cancellations on Day 0, 3-day trials | **55.4%** (web: "55% of all 3-day trial cancellations happen on Day 0"; chart: "3-day trials: 55.4% cancel on Day 0") | Share of all cancellations of 3-day trials that happen on the day the trial starts. Denominator: **cancelled 3-day trials**, not all trials | SOSA 2026 (web, verified 2026-10-30) | Strong benchmark |
| B2 | Trial cancellations on Day 0, other lengths | 7-day 39.8% (web) · 14-day 35.7% · 30-day 31.1% | Same definition, per trial length | SOSA 2026 | Strong benchmark |
| B3 | Trial cancellations on Day 1 | About 29% (3-day) · 23% (7-day) · 17% (14-day) · 15% (30-day) | Same definition. Read from the chart ("roughly") | SOSA 2026 | Strong benchmark (chart reading) |
| B4 | Cancellations in Day 0–1 | 84% of 3-day and 64% of 7-day trial cancellations; 7-day trials show a second bump on Days 3–6 | Same denominator | SOSA 2026 | Strong benchmark |
| B5 | Trial starts on Day 0 | 78–90% of trial starts happen on Day 0 (Business 89.9%, H&F 82.1%, Gaming 81.5%, Education 78.5%, Productivity 78%); after Day 3 under 5% in every category | Share of trial starts by days since install | SOSA 2026 | Strong benchmark |
| B6 | Trial starts on Day 0 (Adapty panel) | 89.37% overall; Day 1–3 2.04%; Day 31+ 6.28%. By category 71.3% (Education) to 94.5% (Entertainment) | Share of trial activations by days since install, average of per-app rates | SOIS 2026 | Strong benchmark |
| B7 | Purchases on Day 0 (Adapty panel) | 44.5% of purchases happen on Day 0, against ~90% of trial starts. Utilities buyers mostly pay on days 1–3 (48.6%); Education 47.9% and H&F 33.8% on days 4–14 | Share of install → paid by days since install | SOIS 2026 | Strong benchmark |
| B8 | Paid conversions on Day 0 (RevenueCat panel) | 50.6% overall (Productivity 71.9%, Education 28.5%); 19.2% in Week 6+. Hard paywalls spike on Days 4–7 (25.7%, 7-day trial expiries) | Share of paid conversions by time since install | SOSA 2026 | Strong benchmark |
| B9 | Trial → paid, all apps | Median **32.2%** (p25 20.2, p75 48.1, p90 64.7) | Share of **trial starts** that convert to paid | SOSA 2026 | Strong benchmark |
| B10 | Trial → paid by category (median) | Travel 43.5 · H&F 37.7 · Education 36.1 · Shopping 33.3 · Media & Ent. 32.2 · Utilities 31.1 · Business 29.4 · Social & Lifestyle 28.8 · Productivity 27.2 · Gaming 25.0 · Photo & Video 22.2 | Per trial start | SOSA 2026 | Strong benchmark |
| B11 | Trial → paid by trial length (median) | ≤4 days 25.5% (web) · 5–9 days 37.4% (web) · 10–16 days 35.4% · 17–32 days 42.5% (web) | Per trial start | SOSA 2026 | Strong benchmark |
| B12 | Trial → paid by store | App Store 32.0% vs Google Play 32.5% | Per trial start | SOSA 2026 | Strong benchmark |
| B13 | Trial → paid (Adapty panel) | Weekly 27.8% · monthly 45.0% · annual 32.1% | Per trial start, by the plan the trial was on, average of per-app rates | SOIS 2026 | Strong benchmark |
| B14 | Trial → paid, AI vs all (Adapty) | All apps 25.59% vs AI apps 20.60% (median) | Per trial start | SOIS 2026 | Strong benchmark |

**Why it matters for screens:** most trial cancellations happen in the first hours, so the welcome screen after a trial start and the first session carry the trial-ending risk, not a day-before reminder alone. SOSA itself names "first-session value" as the lever for the Day-0 cancel spike. That is the report's interpretation, not a test.

## 2. First renewal and retention by plan length

| ID | Benchmark | Number | Definition and denominator | Source, date | Tier |
|---|---|---|---|---|---|
| B15 | Renewal rates, all categories (RevenueCat) | Typical medians, 1st → 3rd renewal: weekly ~35–58% → ~77–81%; monthly ~42–61% → ~73–82%; annual ~23–40% → ~56–76%. Renewal rates jump 18–30 points between the 1st and 2nd renewal | Share of subscriptions renewing at each billing cycle. Ranges are the spread of category medians | SOSA 2026 | Strong benchmark |
| B16 | First renewal by category (median, weekly / monthly / annual) | Business 52.2/61.4/40.0 · Education 57.8/56.2/23.7 · Gaming 50.5/53.1/25.6 · H&F 54.2/57.3/24.6 · Media & Ent. 45.4/57.8/37.1 · Photo & Video 37.6/47.8/23.2 · Productivity 44.8/53.6/23.1 · Shopping 50.7/57.7/29.8 · Social & Lifestyle 35.4/42.1/25.2 · Travel 47.8/53.3/39.9 · Utilities 48.5/57.2/34.9 | Per subscription reaching its first renewal date | SOSA 2026 | Strong benchmark |
| B17 | First renewal by store (weekly / monthly / annual) | App Store 47.7 / 54.1 / 26.1 · Google Play 43.3 / 57.6 / 33.4 | Same | SOSA 2026 | Strong benchmark |
| B18 | First renewal by price tier (W/M/Y) | Low 51/60/37 · mid 46/55/27 · high 45/51/24; 3rd renewals converge (68–81%) | Same | SOSA 2026 | Strong benchmark |
| B19 | YoY change, annual first renewal | Annual 1st renewal fell 3.6 points; 3rd renewals flat (weekly/monthly 77–79%, annual 62.5%) | Points, not percent | SOSA 2026 | Strong benchmark |
| B20 | "Active renewal" rate (W / M / Y, all apps) | 18.7 / 39.2 / 83.4. By category, e.g. H&F 23.9/61.9/86.4, Productivity 14.4/28.2/85.6 | The report's definition: share of renewals made by subscribers **seen in the app in the second half of the previous period**. It describes renewals, not a causal effect of engagement | SOSA 2026 | Strong benchmark (definition is narrow, read it carefully) |
| B21 | 12-month retention (median) | Annual **27.5%** · monthly **8.2%** · weekly **1.2%**. Previous cohort: 31.2 / 9.6 / 1.7 | Share of paid **subscriptions** still active after 12 months (subscription-level) | SOSA 2026 | Strong benchmark |
| B22 | 12-month retention by category (median, monthly / weekly / annual) | Business 14.2/1.8/39.9 · Education 6.3/1.6/23.5 · Gaming 6.6/1.3/25.3 · H&F 8.5/2.2/24.4 · Media & Ent. 10.5/1.0/36.0 · Photo & Video 8.2/1.6/23.3 · Productivity 8.8/1.4/22.9 · Shopping 6.8/2.1/30.2 · Social & Lifestyle 3.9/0.5/24.7 · Travel 9.0/2.0/38.6 · Utilities 10.3/1.3/34.2 | Same | SOSA 2026 | Strong benchmark |
| B23 | 6-month retention (median) | Monthly 18.3% · weekly 3.7% | Same | SOSA 2026 | Strong benchmark |
| B24 | 12-month retention, AI vs non-AI (median) | Annual 21.1% vs 30.7% · monthly 6.1% vs 9.5% · weekly 1.2% vs 1.7% | Same | SOSA 2026 | Strong benchmark |
| B25 | 12-month retention, hard paywall vs freemium | Annual 26.8% vs 27.7% | Same | SOSA 2026 | Strong benchmark |
| B26 | Annual cancellations by month of year one | Month 1 **34.2%**, then 4–9% a month, month 12 11.1%. Month-1 share by category 30.5% (Education) to 50.0% (Shopping) | Share of annual-plan cancellations (auto-renew turned off) by month | SOSA 2026 | Strong benchmark |
| B27 | Renewal stages (Adapty) | With trial: weekly 1st renewal 59.2% · monthly 48.0% · annual 19.1%. Direct (no trial): weekly 37.0% · monthly 37.0% · annual 17.7% | Share of **paid subscribers** reaching the nth renewal (a cumulative stage, not a per-cycle rate like B15) | SOIS 2026 | Strong benchmark |
| B28 | Retention curves (Adapty, Month 1 / 3 / 6 / 12) | With trial: weekly 36.8 / 17.4 / 10.3 / 5.5 · monthly 51.8 / 33.3 / 22.4 / 14.2 · annual M12 19.9. Direct: weekly 21.1 / 11.0 / 7.1 / 3.9 · monthly 38.6 / 23.9 / 15.6 / 9.4 · annual M12 19.0 | % of subscribers still active. Chart readings (±1–2 points) | SOIS 2026 | Strong benchmark |
| B29 | Retention by category, trial (Adapty; annual M12 · monthly M1/M3/M6/M12 · weekly M1/M3/M6/M12) | H&F 20.6 · 56.6/35.3/23.8/15.1 · 38.1/17.8/10.8/4.9 — Education 19.4 · 54.5/32.7/20.7/12.1 · 37.6/17.5/10.3/5.3 — Lifestyle 20.2 · 54.1/34.4/22.9/15.3 · 30.9/14.1/8.1/4.4 — Photo & Video 17.2 · 51.1/34.3/23.9/16.0 · 34.0/17.5/10.8/6.2 — Productivity 21.9 · 50.9/32.6/21.6/13.8 · 37.9/18.9/11.8/6.6 — Utilities 22.2 · 48.3/30.0/19.7/11.3 · 38.7/17.8/10.2/5.3 — Entertainment 18.1 · 42.1/27.5/18.2/12.4 · 31.9/14.3/8.1/4.3 — Graphics & Design 18.7 · 46.1/31.2/23.1/15.8 · 32.6/15.0/9.1/5.0 | Same. Adapty categories are App Store categories, **not** SOSA buckets | SOIS 2026 | Strong benchmark |
| B30 | Weekly first renewal by price bucket (Adapty) | Paid → 1st: low 48 · lower-mid 46 · upper-mid 47 · high 54; 1st → 2nd 73–74 | Per-cycle renewal rate, % | SOIS 2026 | Strong benchmark |

**Why it matters for screens:** the first renewal is the steepest drop for every plan length. Annual buyers decide early (a third of annual cancellations come in month 1), so a value recap that waits until month 11 arrives after most of the decision.

## 3. Refunds and churn reasons

| ID | Benchmark | Number | Definition and denominator | Source, date | Tier |
|---|---|---|---|---|---|
| B31 | Refund rate by category (median) | Most categories 3–4.5%: Productivity 4.7 · Business 4.5 · Education 4.3 · Photo & Video 4.2 · H&F 3.9 · Utilities 3.7 · Social 3.4 · Media 3.3 · Shopping 3.1 · Gaming 3.0 · Travel 2.5 | Share of paid subscriptions refunded in their **first billing period** | SOSA 2026 | Strong benchmark |
| B32 | Refund rate by region and model | NA 3.4% vs IN/SEA 7.7% (emerging-region p90 ~33%); low price 2.7 / mid 3.9 / high 4.5; AI 4.2 vs non-AI 3.5; freemium 2.9 vs hard paywall 2.5 (the report calls the last gap noise) | Same | SOSA 2026 | Strong benchmark |
| B33 | Refund stage (Adapty) | With trial: weekly 8.3% · monthly 14.9% · annual 15.5%. Direct: 4.0 / 5.0 / 8.5 | The report's "refund" stage on the user-journey chart; the chart does not state the denominator. Do not compare with B31 | SOIS 2026 | Directional (denominator unclear) |
| B34 | Revenue lost to refunds (Adapty) | With trial 3.69% · direct 3.11% (global) | Share of subscription revenue | SOIS 2026 | Strong benchmark |
| B35 | Why subscriptions end | App Store 82.9% voluntary / 15.2% billing error; Google Play 66.3% / 32.2% | Share of subscription ends | SOSA 2026 | Strong benchmark |
| B36 | Google Play cancel survey reasons (all categories) | Cost 36.4% · **not enough usage 33.7%** · found a better app 9.7% · technical 7.3% · other 12.9%. "Not enough usage" is highest in Travel (46.7%), H&F (40.4%), Education (39.5%) | Share of Google Play cancel-survey answers (Play only) | SOSA 2026 | Strong benchmark |

**Why it matters for screens:** "not enough usage" is about a third of stated Play cancel reasons. That is the problem first-week guidance, reminders and value recaps try to solve. It is a survey answer, not proof that those screens fix it.

## 4. Push notification opt-in (keep each vendor separate; never average)

| ID | Benchmark | Number | Definition and denominator | Source, date | Tier |
|---|---|---|---|---|---|
| B37 | **Same as onboarding Part 2 row "Push opt-in medians"** | "2025: iOS 48.85%, Android 53.3%; Android fell from 71.3% (2023) after the Android 13 runtime permission" | As in the onboarding row | Onboarding row's source: Airship 2025 and 2026 benchmarks, https://growth.airship.com/rs/313-QPJ-195/images/Airship-2025-Push-Notification-Benchmarks-EN.pdf | Strong benchmark (as in the onboarding library). **See the citation note under the table** |
| B38 | Airship 2026 benchmarks: opt-in medians | **Android 53.3% · iOS 48.85%**. 90th percentile: Android Utility & Productivity 86.63%, iOS Education 88.7%. 10th percentile: Android Charities 51.25%, iOS Finance & Insurance 44.68% (as stated on the page). Lowest floors: iOS Retail 18.1%, Android Gambling & Gaming 21.35% | "The percentage of an app's audience that has granted permission — opted in — to receive push notifications", monthly rate averaged over 12 months. Panel: Jan–Dec 2025, 681B+ notifications, 3B+ users, 15 verticals; apps with ≥1,000 active users that sent ≥1,000 pushes in a month | https://www.airship.com/mobile-app-push-notification-benchmarks-for-2026/ (page modified 2026-06-05) | Strong benchmark |
| B39 | Airship: onboarding campaigns | Apps running onboarding campaigns reach opt-in "as high as 40% above their category average" (in both the 2025 PDF and the 2026 page) | Ceiling claim, no median | Airship 2025 PDF and 2026 page | Directional |
| B40 | Airship: in-app messages to opted-out users | "in-app messages drive a 14% average increase in opt-in rates among opted-out users" | Relative lift; method not stated | Airship 2025 PDF (data Jan–Dec 2024) | Directional |
| B41 | Airship 2025 PDF: YoY direction | Key takeaway: "While iOS opt-in rates remained steady, Android opt-in rates dropped significantly across all percentiles", attributed to the Android 13+ runtime consent. A text extraction of the year-over-year chart read 2023 → 2024 medians as Android 71.3% → 59.5% and iOS 49.1% → 49.4%, but the chart values were jumbled in extraction | Panel: Jan–Dec 2024, 9B+ app users, 13 verticals | Airship 2025 PDF (above) | Strong benchmark for the direction; **the 2024 medians are unverified** |
| B42 | **Same as onboarding Part 2 row "Push opt-in, Health & Fitness"** | iOS 53.98%, Android 85.28% | Pushwoosh panel; not comparable with Airship | Pushwoosh 2025, 600+ apps: https://www.pushwoosh.com/blog/increase-push-notifications-opt-in/ | Benchmark (as in the onboarding library). **Not re-checked:** the page fetch was blocked on 2026-10-30 |
| B43 | Pushwoosh benchmark post | Opt-in values appear only in charts; the text has no numbers. Push CTR (Q4 2024–Q2 2025): Media & Ent. Android 1.69% / iOS 0.83%; Fintech 2.84 / 2.09; E-commerce 3.78 / 3.05 | Opt-in: "the percentage of users who have enabled push notifications out of all app users" (period Q1–Q4 2024). CTR: push opens ÷ push recipients, weighted | https://www.pushwoosh.com/blog/push-notification-benchmarks/ (published 2025-08-14; 600+ apps) | Directional |
| B44 | OneSignal opt-in by category (Android / iOS) | Business 56.7/46.3 · Education 39.7/37.1 · Entertainment 40.3/27 · Finance 49.5/48.7 · Food & drink 32.8/40 · Games 27.8/20.6 · **Health & fitness 43.2/33.5** · Lifestyle 38.8/34 · News 36.7/29.8 · Productivity 53.6/44.8 · Shopping 36/33.2 · Utilities 51.5/51.6 | "Category averages". No definition, denominator, app count or period on the page ("based on data from trillions of messages"; titled 2024 benchmarks) | https://onesignal.com/mobile-app-benchmarks-2024 (no date shown) | Directional |
| B45 | Business of Apps | Overall 60%; Android median 81% (range 49–95%); iOS median 51% (29–73%) | All attributed to Airship's 2021 benchmark, H1 2021 data. The page was updated 2022-04-01 | https://www.businessofapps.com/marketplace/push-notifications/research/push-notifications-statistics/ | Directional (stale; predates the Android 13 permission. Don't use for current screens) |
| B46 | **Same as onboarding #1 (Blinkist)** | Push opt-in 6% → 74% after a reminder opt-in on the trial welcome screen (bundled with a paywall trial timeline) | Single-app A/B | https://uxplanet.org/how-solving-our-biggest-customer-complaint-at-blinkist-led-to-a-23-increase-in-conversion-b60ad514134b | Strong (A/B), bundled |

**Citation note for B37 (for the onboarding library owner):** the 48.85% / 53.3% medians are on Airship's **2026** benchmarks page (data Jan–Dec 2025), not in the 2025 PDF that the onboarding row links. The 2025 PDF covers 2024 data, and its medians could not be read reliably (B41). The 71.3% "2023" figure comes only from that garbled chart extraction. Suggested fix in the source libraries: link https://www.airship.com/mobile-app-push-notification-benchmarks-for-2026/ for 48.85/53.3, and mark 71.3% as unverified. This file keeps the onboarding row as written, as instructed.

**Panels differ:** Airship takes the median of per-app monthly rates. OneSignal reports category averages with no stated method. Pushwoosh shows enabled users ÷ all app users. Quote one vendor per number.

## 5. App retention curves (D1 / D7 / D30), all apps, not subscribers

These are **install-cohort usage retention** (did the user open the app on day N), not subscription retention. None of them states whether it is classic or rolling (see Metric definitions).

| ID | Benchmark | Number | Definition and denominator | Source, date | Tier |
|---|---|---|---|---|---|
| B47 | Adjust, all verticals (median) | D1 26% · D7 13% · D14 10% · D30 7%. Android 24/11/8/6; iOS 27/14/11/8 | "Percentage of users who continue to use an app after installing it"; 30-day cohort; a day = 24h. Dataset and period not named | https://www.adjust.com/blog/what-makes-a-good-retention-rate/ (published 2024-04-16) | Directional |
| B48 | Adjust D1 by vertical | Games and social 29% · Health & fitness 27% · Fintech 22% · Utility 21% · Entertainment 20% · Shopping 18% · Travel 16% · Food & drink 13% (D1 only; no D7/D30 by vertical on the page) | Same | Same | Directional |
| B49 | OneSignal, all categories (average) | D1 28.29% · D7 17.86% · D30 7.88% | No definition | https://onesignal.com/mobile-app-benchmarks-2024 | Directional |
| B50 | OneSignal by category (D1 / D7 / D30) | Business 25.38/16.85/6.94 · Education 27.5/17.76/8.02 · Entertainment 28.4/18.15/8.46 · Finance 26.84/18.54/8.03 · Food & drink 22.86/18.85/7.86 · Games 32.22/18.08/7.67 · **Health & Fitness 28/18.13/8.48** · Lifestyle 25/13.13/5.94 · News 26.67/15.83/7.55 · **Productivity 32.86/24.23/9.63** · Shopping 29.09/18.26/7.2 · Utilities 28.18/16.75/9.2 | No definition | Same | Directional |
| B51 | OneSignal: onboarding messages | "Apps that send onboarding messages earn higher 30-day retention rates and 24% higher install-to-purchase conversion rates" (channel not stated) | Correlation | Same | Directional |
| B52 | AppsFlyer 2025 retention report | Text gives only D30 by country (Android Japan 4.15%, UK 2.73%; iOS UK 3.22%, US 3.02%), "iOS rates are 46% higher than Android overall", and YoY category changes (e.g. iOS H&F +22%, Android Education +29%). Category D1/D7/D30 tables are images, not readable | ~11K apps, 10.6B installs; 2024 data (tables Q3 2024) | https://appsflyer.com/?p=453529 ("2025 app retention benchmarks report"; no publish date on the page) | Directional (category values not extractable) |
| B53 | Expert claim in SOIS 2026 | "77% of users never return after day one" (Hannah Parvaz, Aperture) | Source of the number not given | SOIS 2026 | Directional (expert quote) |

Not used: aggregator posts (UXCam, getpanto, quashbugs, enable3, unstar, semnexus and similar) that reprint D1/D7/D30 tables without a primary source.

## 6. Streaks: Duolingo's public numbers

Only figures that a Duolingo page or shareholder letter states. All are one app's product data, mostly correlational.

| ID | Item | Number | What kind of number | Source, date | Tier |
|---|---|---|---|---|---|
| B54 | Share of daily learners with a 7+ day streak | "just over half of our daily learners have a streak at least 7 days long", up from "about a third of our daily learners a year ago" | Product data | https://blog.duolingo.com/improving-the-streak/ (2020-11-19) | Single app |
| B55 | Decouple streak from daily goal (one lesson keeps the streak) | D14 retention +3.3%; daily active learners +1%; share of daily learners on a streak +10.5% in 20 days (+19% for new learners); learners with 7+ day streaks "over 40%" up | Company A/B, relative changes | Same | Single app, company A/B |
| B56 | 7-day streak and next-day return | Learners who reach a 7-day streak are "2.4 times more likely to continue using Duolingo the next day" | Correlational | Same | Single app |
| B57 | Two streak freezes equipped at once | Daily active learners +0.38% (relative); "did not encourage more days off" | Company experiment (method not described) | https://blog.duolingo.com/how-duolingo-streak-builds-habit/ (2022-01-31; also the Japanese edition https://blog.duolingo.com/duolingo-streak-research/ , 2024-05-13) | Single app, company A/B |
| B58 | Streak-extension animation for new learners | Likelihood a brand-new learner is still active 7 days later +1.7% | Company experiment | Same | Single app, company A/B |
| B59 | 7-day streak and course completion | 3.6× more likely to complete their course; "over 6 million people on a streak of 7 days or more" at the time of writing | Correlational; point-in-time count | Same | Single app |
| B60 | Year-long streaks (shareholder letter) | "Over 10 million of our users now maintain streaks of one year or longer, and one-third of our DAUs have a Friend Streak." | Point-in-time count | Duolingo Q4/FY2024 shareholder letter, 2025-02-27: https://www.sec.gov/Archives/edgar/data/1562088/000156208825000039/q4fy24duolingo12-31x24shar.htm | Single app |
| B61 | Year-long streaks by age | "Nearly 30% of learners age 60+ have year-long streaks"; "less than 5% of learners 13-17" | Product data, inferred (no sample stated) | https://blog.duolingo.com/which-generation-most-serious-about-streak/ (2023-07-24) | Single app |

Not found: a Duolingo-stated "share of DAU with a 7+ day streak" in any 2025–2026 shareholder letter (the Q3 2025 and Q4 2025 releases opened have no streak, notification or widget sentences). Duolingo also reported a notification-copy test (+5% DAU) via First Round Review; not used here.

## 7. Rating prompts

No public benchmark gives a rating-prompt conversion rate (prompts shown → ratings left) for subscription apps.

| ID | Item | Number | Definition | Source, date | Tier |
|---|---|---|---|---|---|
| B62 | Share of apps showing a rating-request screen | Broad tag match 12.7% (103 of 809 apps); strict count 22 apps; the page puts prevalence at "approximately 3% and 13%". H&F 10/56, Travel 6/41, Productivity 6/64 | Captured in-market screens, July 2026, LLM tagging. Lower bound, because prompts are transient | https://www.lazyweb.com/research/what-percent-of-apps-show-a-rating-request-screen.md (2026-07-07) | Directional (observed, small panel) |
| B63 | Effect of Apple's one-tap prompt | Median number of ratings +15% after SKStoreReviewController launched; more than one in five users opted out of review dialogs or stopped seeing them | Apptentive study, sample not reported | https://www.marketingdive.com/news/study-apple-update-increases-app-ratings-by-15/445029/ (2017-06-15) | Directional (old) |
| B64 | System cap | iOS shows the system prompt at most 3 times per app in 365 days; Google Play enforces an undisclosed time-bound quota | Platform rule, not a benchmark | See `platform-rules.md` §1.3 and §2.2 | Rule |

---

## Metric definitions (keep these apart)

**Denominators**
- **Per install** (download): SOSA D35 download → paid; SOSA download → trial (within 30 days); RevenueCat RPI; Adapty install → trial and install → paid (average of per-app rates); Adapty "install LTV". D1/D7/D30 usage retention (Adjust, OneSignal, AppsFlyer) is also per install cohort.
- **Per trial start**: SOSA trial → paid (B9–B12); Adapty trial → paid (B13–B14).
- **Per cancelled trial**: SOSA trial-cancellation timing (B1–B4). 55.4% means 55.4% of 3-day-trial **cancellations** happen on Day 0. It does not mean 55.4% of 3-day trials cancel on Day 0.
- **Per subscription / subscriber**:
  - SOSA retention (B21–B25) is subscription-level: the share of paid subscriptions still active after N months.
  - SOSA renewal rate (B15–B19) is per billing cycle: of those due to renew at cycle n, how many did.
  - Adapty renewal stages (B27) are cumulative: of all paid subscribers, how many reached the nth renewal. A 59.2% Adapty first renewal and a 54.2% SOSA first renewal are not the same measure.
- **Per refunded subscription**: SOSA refund rate = refunded in the first billing period ÷ paid subscriptions. Adapty "revenue lost to refunds" is a revenue share.
- **Per app audience (push)**: Airship opt-in is opted-in ÷ the app's audience, per app per month, averaged over 12 months, then the median across apps. Pushwoosh is users with push enabled ÷ all app users. OneSignal gives no definition.
- **Per paywall view**: Adapty *State of Paywalls* (not used here). Don't mix it with per-install or per-trial numbers.

**Relative vs points**
- A test result such as "D14 retention +3.3%" (Duolingo) is a **relative** change. Retention of 20% becomes about 20.66%, not 23.3%.
- Differences between benchmarks are in **points**: "annual first renewal fell 3.6 points"; "the 1st → 2nd renewal jump is 18–30 points".
- Ratios ("2.4× more likely", "iOS 46% higher than Android") are relative and usually correlational.
- Never turn a relative lift into points (or the reverse) without the baseline.

**Classic vs rolling D7**
- **Classic (N-day, "Return On")**: the share of the install cohort active **on** day 7 exactly (day 7 = the 24h window seven days after install, by the vendor's day boundary). Amplitude: "Return On retention tells you the percentage of users that came back to trigger your return event on a specific day."
- **Rolling (unbounded, "Return On or After")**: the share active on day 7 **or any later day**. Always ≥ classic for the same cohort. Amplitude: "Return On or After retention tells you how many of your users triggered your return event on a specific day or after." Source: https://amplitude.com/docs/en/analytics/charts/retention-analysis/retention-analysis-interpret
- **Bracket / range**: active at any time within a window (e.g. days 7–13).
- Adjust, OneSignal and AppsFlyer do not say which one they use. Adjust's figures behave like classic N-day (they fall day by day), but that is an inference. Never compare a client's rolling D7 with these classic-looking benchmarks.
- None of these is subscription retention: D30 usage retention of 7% (Adjust) and 12-month annual subscription retention of 27.5% (SOSA) measure different things.

**Other traps**
- SOSA "AI 8.5% vs 5.6%" is download → trial (trial start rate), not trial → paid.
- Adapty categories (App Store categories such as Lifestyle, Entertainment, Graphics & Design) are not SOSA buckets. Map by primary App Store category and name the source.
- SOSA cells are medians (p25 / median / p75 / p90). Adapty mixes medians, averages and per-app averages depending on the chart.
