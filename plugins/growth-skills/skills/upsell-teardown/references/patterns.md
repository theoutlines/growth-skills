# In-product Upsell Pattern Library

The reference for the upsell teardown. It covers everything that sells after
onboarding: the triggers that open an upsell, the gate itself (limit,
locked feature, preview), the upsell screen, how often it comes back, the
ladder for people who already pay (higher tier, annual, family, lifetime),
AI credits, and the always-on surfaces and lifecycle nudges.

Each pattern has **When**, **Cross-check**, **How**, **Evidence** (tests
#U1–#U50 and benchmark rows in `evidence.md`), **Seen in** (apps from
`flows.md`) and **Trap**. Tiers: strong, directional, anecdotal, observed.

**Read this first.**
- Later paywalls convert about 4x less per view than the onboarding paywall
  (0.23% vs 0.85%) but start 38% of subscription revenue, and 7 in 10
  paywall views happen after the first session (Adapty State of Paywalls
  2026, benchmark). In-product upsells are where most impressions are.
- Only 7 rows are strong tests, and only 3 of those are subscription apps
  (#U1 Memrise, #U22 Dark Noise, #U32 Mojo). Everything about the annual
  switch, family plans, frequency caps, badges and push upsells is a
  hypothesis: no public test exists.
- The same tactic flips sign by position and by what it blocks. Check the
  flips in section G before recommending anything.

## Contents

**A. Triggers**
1. Gate the feature at the moment it's wanted (contextual gate)
2. Limit-reached upsell
3. Upsell after a success moment
4. Never block the core habit

**B. The gate**
5. Show the meter before the wall
6. Soft gate: preview, blur or partial result
7. A free way past the wall
8. Size the free tier on value, and price the engagement cost

**C. The upsell screen**
9. Name the blocked task in the headline
10. Say what the higher tier adds, in units
11. Full price, period and when the charge happens
12. One clear decline, no pressure

**D. Frequency and second offers**
13. One upsell per trigger, decline respected
14. Second-chance offers: position decides

**E. The ladder for people who pay**
15. Upgrade screen, never the subscribe paywall
16. Annual switch for happy monthly subscribers
17. Tier ladder, decoy and lifetime anchor
18. Family plan offer
19. Store mechanics in the copy

**F. AI credits and consumables**
20. Allowance in the plan, credits as a top-up for subscribers
21. Credit packs priced in real money

**G. Always-on surfaces and lifecycle**
22. Plan status surface
23. Trial and reverse-trial countdown with usage

**H. Legal and store flags**
24. Compliance flags

**Where it flips** (summary at the end)

---

## A. Triggers

### 1. Gate the feature at the moment it's wanted (contextual gate)
**When:** paid features are sold only from a generic Premium screen, or a
locked feature opens the same paywall as everything else.
**Cross-check:** tapping a locked feature opens an upsell about that feature
counts.
**How:** each gated feature opens its own sheet: what it does, what the user
gets with the tier, one CTA. Gate the highest-intent action in the product
(opening messages, exporting, generating the video).
**Evidence:** #U1 Memrise: two benefit framings on the same locked mode
differed by 28% in conversion (strong, Android). #U2 Tapple gated opening
messages: +8% registrations after rollout (directional). Adapty A/B library: a
paywall triggered by a relevant action (language switch) ARPU ~+20%, CR
~+15% (directional, anonymised band). The +50–60% band is for daily-limit
paywalls (pattern 2), not feature gates.
Apple HIG endorses prompts "at relevant points throughout your app" (rule
guidance).
**Seen in:** Duolingo (AI explain), Photoroom (video generator), Apple
Invites, Insight Timer (course), Coffee Meets Bagel, Figma and Mixpanel (web).
**Trap:** a contextual gate with generic copy wastes the context; see 9.

### 2. Limit-reached upsell
**When:** a free allowance runs out and the app shows nothing, an error, or a
generic paywall.
**Cross-check:** the limit screen states what ran out, when it resets and
what the tier gives.
**How:** at zero, one screen: "You've used your 5 scans this week · resets
Monday · Pro: unlimited scans". Offer the free way out (7) alongside.
**Evidence:** Adapty A/B library: daily-limit paywall roughly +50–60%
conversion on iOS and Android (directional). #U10 Alpe Audio: users who hit
the paywall after their 40 free minutes converted at 10% (directional,
bundled). Apple HIG: prompt "when they near their monthly limit" (guidance).
**Seen in:** Duolingo (hearts), Lex (daily cap), Bevel (weekly AI allowance),
Perplexity (credits), X (AI limit inline), Recime (weekly imports).
**Trap:** a limit that stops a task halfway with paying as the only way to
finish is a habit block (4). With an allowance and a free way through
(wait, ad, earn) it is a normal limit: Duolingo reported its Energy model
raised DAU and subscriber conversion (#U25, anecdotal: no figures).

### 3. Upsell after a success moment
**When:** the only upsells are walls; nothing sells when the user just got
value.
**Cross-check:** a light upsell (card, banner) right after a finished task.
**How:** after the export or the workout, a small card that names the next
thing the tier adds; never block the success screen.
**Evidence:** #U5 JourneyStamp: in-app paywalls at high-engagement moments
with copy about features used, +50% conversion (directional, bundled with
onboarding tests). #U20 Blackbox and #U37 Wizz: prompts timed to receptive
moments (vendor-reported, directional). Observed only in a few apps.
**Seen in:** Synthesia (time left right after a video is made), MyFitnessPal
("your meal plan is ready" behind Premium+).
**Trap:** no clean public test in consumer iOS apps; call it a hypothesis.

### 4. Never block the core habit
**When:** a gate sits on something users already do daily (the lesson, the
log, the core tool), or the free product gets worse to push upgrades.
**Cross-check:** list what free users do every day; none of it should be
newly blocked.
**How:** gate extras on top of the habit (more, faster, smarter), not the
habit. If you must limit it, use a generous allowance with a reset.
**Evidence:** #U4 Duolingo offline gate: much higher Plus sign-ups, slight
revenue rise, retention and DAU down, shut down (anecdotal: no figures).
#U3 Grammarly "sticker peel": conversion up, uninstalls up and WAU of engaged
free cohorts down (directional). #U13 Pandora: each extra ad per hour cut
listening hours about 2.08%, and the long-run cost was about 3x the one-month
estimate (strong for listening; for subscriptions only the direction, more
paid, is reported).
**Trap:** short tests show the conversion gain and miss the engagement cost.
Judge habit gates on retention and DAU over months.

## B. The gate

### 5. Show the meter before the wall
**When:** a limit exists but users only find out when they hit it.
**Cross-check:** a visible counter, bar or "x of y" with a reset time near
the action or in a usage screen.
**How:** show remaining uses where the action is ("1 of 5 left · resets in
2 days"); add the tier's number next to it.
**Evidence:** observed (17 apps in `flows.md`). No public test.
**Seen in:** Canva (under the generate button), Photoroom, Ahead, Raycast,
Recime, Google One, Duolingo energy.
**Trap:** a meter shown with "Upgrade" on every screen is an always-on
prompt; keep the upsell to the limit moment.

### 6. Soft gate: preview, blur or partial result
**When:** the paid value is visible (a result, a list, an insight) but the
gate hides it completely.
**Cross-check:** a preview, blur or partial result before the upsell.
**How:** show the shape of the result (blurred faces, the first insight, a
watermarked export) and sell the full version.
**Evidence:** #U17 PepTalk: 10-second preview then paywall converted
"significantly" better than a hard gate (anecdotal). Adapty "hard vs soft"
(no close button vs close button) is a different thing: don't cite it here.
**Seen in:** Tinder (blurred likes), Photoroom (blurred example), Neuecast
(partial stats).
**Trap:** a teaser that the user already sees as theirs (their own
suggestion, their own data) reads as taking it away: #U3 Grammarly's peel
raised uninstalls.

### 7. A free way past the wall
**When:** a hard limit with no option but paying, in an app whose free tier
drives engagement or ads.
**Cross-check:** waiting (with a timer), an ad, earning, or the remaining free
allowance offered next to the upgrade.
**How:** put the free path on the same sheet, quieter than the paid one but
plain and readable.
**Evidence:** #U12 Ryn VPN: "continue with ads" as a third access tier,
revenue +158% year over year (directional, no control). Observed in 12 apps.
**Seen in:** Duolingo (trial, gems, ad, practice, wait on one sheet), Forest,
Google One (clean up space first), Otter.
**Trap:** Apple 3.1.2(a): don't make people do tasks (invite friends, post)
to get what they already paid for. For free users it's allowed.

### 8. Size the free tier on value, and price the engagement cost
**When:** the team plans to tighten or loosen the free tier.
**Cross-check:** the limit sits on the unit of value (minutes, scans,
outputs), not an arbitrary count.
**How:** set the limit where the value lands (Alpe: 40 minutes a week across
the whole library instead of the first lessons). Test tightening with a
long horizon and watch engagement, virality and ad revenue too.
**Evidence:**
- #U8 randomized mobile game (~300k users): fewer free levels, conversion
  +20%+, usage down (strong, not a subscription app).
- #U9 NYT meter: subscriptions +31%, content demand −9.9% (directional).
- #U11 Greg: count cap → gate on the value feature, sign-up → trial 3% → 15%
  (directional, bundled with placement).
- #U10 Alpe Audio: time-based limit across the library, free D30 retention
  +70% (directional, bundled).
- Freemium vs hard paywall: 2.1% vs 10.7% download → paid, similar 12-month
  retention (SOSA 2026, self-selected benchmark). #U15 (b): an app that moved to
  freemium lost more than half its conversion and reverted (directional).
**Trap:** a model switch (freemium ↔ hard paywall) is a business decision,
not a design test; raise it, don't prescribe it.

## C. The upsell screen

### 9. Name the blocked task in the headline
**When:** a contextual gate shows generic Premium copy.
**Cross-check:** the headline names the feature or task the user tapped.
**How:** "Export in 4K with Pro" rather than "Go Premium"; benefits after,
3–4 bullets max.
**Evidence:** #U1 Memrise: changing only the benefit on the locked mode
moved conversion 28% (strong). #U3 Grammarly: framing as more value beat
lock framing, +22% upgrades (directional). Observed in 16 apps.
**Trap:** naming the task and then showing the full generic feature grid
dilutes it; keep the task first.

### 10. Say what the higher tier adds, in units
**When:** the screen says "Pro" or "unlimited" without numbers.
**Cross-check:** limits, credits or features of the tier in concrete terms.
**How:** "Pro: 100 scans a month, 4K export, no watermark".
**Evidence:** Apple 3.1.2(c): describe what the user gets for the price
("How much cloud storage?") (rule). Play subscriptions policy: clear terms
(rule).
**Trap:** "unlimited" with a hidden fair-use cap is a bait-and-switch risk
(Apple 3.1.2(a)).

### 11. Full price, period and when the charge happens
**When:** an upgrade or credit pack shows only "+$2/mo", a per-credit price,
or no timing.
**Cross-check:** the total billed price and period, and when it's charged.
**How:** "$59.99 a year, charged today" or "Your plan changes on 12 Dec".
Match the store mechanics (19).
**Evidence:** HIG: "Display the total billing price for each in-app purchase"
(guidance). Play: show price, period and terms before purchase (rule).
**Trap:** family offers framed only as the extra per month need the total
too.

### 12. One clear decline, no pressure
**When:** the upsell has no visible decline, a shaming decline, a fake timer,
or a pre-checked add-on.
**Cross-check:** a plain "Not now", no countdown unless the offer truly ends,
nothing pre-checked.
**How:** decline as a readable text button; timers only for real deadlines,
ending when the offer ends.
**Evidence:** FTC v. Amazon order: clear decline button, no "No, I don't want
Free Shipping" (case); ACM v. Epic: fined for countdown timers implying
scarcity (case); CMA v. Emma Sleep consent order on timers (case). Countdowns appear on ≤1.4% of RevenueCat paywalls (observed).
**Trap:** a "48 hours left" offer that resets on reopen is the textbook
violation.

## D. Frequency and second offers

### 13. One upsell per trigger, decline respected
**When:** the same upsell fires on every open, or after each dismissal.
**Cross-check:** a stated cap or rule (one per trigger, a cool-down after
decline). Usually invisible on screens: ask.
**How:** show at the trigger; after a decline, don't repeat for that trigger
for a set period; let persistent surfaces (22) carry the rest.
**Evidence:** buyers decide fast: 60% buy on the first view, 84% of
2nd+-view buyers within 24 h, 4% come back another day (Adapty SOP,
benchmark). Frequency cuts both ways: #U36 Memrise showed a trial every 21st
session instead of every 49th, +50% (directional), while #U37 Wizz cut
prompts ~50% at better moments, +81% offer conversion (vendor, directional).
**Trap:** no public test of frequency caps or long-run fatigue; treat "more
often" vs "better timed" as a test, not a rule.

### 14. Second-chance offers: position decides
**When:** a discount follows a dismissed in-app paywall.
**Cross-check:** where the second offer sits (after onboarding or after an
in-app paywall).
**How:** after an in-app paywall, prefer a different plan or trial over a
discount; keep it to one.
**Evidence:** Adapty A/B library: the same second-chance discount lifts
premium conversion ~+25–30% after the onboarding paywall but roughly halves
ARPU after the main in-app paywall (#U44 = onboarding E2, directional).
Second-chance paywalls convert at 0.88x the main one and beat it in 45% of
apps (#U43, benchmark).
**Trap:** a discount that trains users to close paywalls.

## E. The ladder for people who pay

### 15. Upgrade screen, never the subscribe paywall
**When:** active subscribers see the same "subscribe" paywall as free users.
**Cross-check:** subscribers get a screen naming their current plan and what
the next tier adds.
**How:** "You're on Plus · Premium adds…", current plan marked, upgrade CTA.
**Evidence:** HIG: encourage a new subscription only when someone isn't a
subscriber, "otherwise, people may believe their existing subscription has
lapsed"; Apple: verify active status before showing subscription options
(rule guidance).
**Seen in:** Azar (current tier named), Duolingo (manage-plan stack), WHOOP
(upgrade and downgrade side by side).
**Trap:** an upgrade screen that looks like a new purchase makes people
think they'll pay twice; name the current plan and what changes.

### 16. Annual switch for happy monthly subscribers
**When:** monthly subscribers are a large share and nothing offers the
annual plan after purchase.
**Cross-check:** an annual-switch offer to monthly payers (status screen,
banner after an engaged period, store upgrade offer).
**How:** a card or banner for active monthly payers (not at cancel) with the
annual price, the saving and the date annual billing starts.
**Evidence:** no public in-app test (gap). Context: plan-switch offers on
Apple's cancel sheet were accepted ~0.6% of the time (#U31, directional), so
the switch belongs with engaged payers. #U28 Memrise annual-only week: daily
conversions −20%, revenue per day +32% (directional). #U29 Uscreen and #U30
Churnkey (web, directional, don't cite as LTV lifts). Monthly-heavy buckets:
Productivity 76.7% monthly sold; AI apps 59.8% (SOSA).
**Seen in:** Coinbase (annual pre-selected, billing start stated), GoPro Quik
(banner).
**Trap:** on iOS a same-level switch from monthly to annual takes effect at
renewal, not now (19).

### 17. Tier ladder, decoy and lifetime anchor
**When:** one paid tier only, or tiers that differ in name but not in units.
**Cross-check:** a higher tier with a concrete extra (AI, family, limits),
and what sits next to each plan.
**How:** a top tier with a clear extra; consider a lifetime option next to
annual.
**Evidence:** #U22 Dark Noise: showing lifetime next to annual, lifetime
+266%, annual −30%, total conversions about +10% (strong). #U23 adding a
premium tier raised the middle option's revenue 8.9% (strong, web books).
#U25 Duolingo: subscription ARPU +6% mainly from shifts to higher tiers
(directional). SOP: lifetime next to annual +10–15% revenue in winning tests
(directional).
**Trap:** lifetime cannibalises annual (#U22); judge on total revenue.

### 18. Family plan offer
**When:** an individual plan with sharing potential and no family offer.
**Cross-check:** a family upsell to individual payers.
**How:** a family option on the plan screen with the total price and the
price per member.
**Evidence:** #U24 Duolingo: Family is 23% of subscribers with higher
retention and LTV (directional, company-reported). No test of a family
upsell (gap).
**Seen in:** Duolingo, Calm, Cal AI, Apple Music, YouTube, Waking Up.
**Trap:** showing only the per-member price hides the total; show both.

### 19. Store mechanics in the copy
**When:** upgrade copy doesn't match how the store bills it.
**Cross-check:** iOS: upgrade immediate with a prorated refund; downgrade and
same-level duration change at renewal. Android: ask how the change is billed.
**How:** "Premium starts now; Apple refunds the unused part of Plus" or
"Annual starts on 12 Dec". Don't quote Apple's refund amount.
**Evidence:** Apple auto-renewable subscriptions page; Google Play
replacement modes (rules; see `platform-rules.md`).
**Trap:** "Upgrade now" when the change only starts at renewal breaks trust;
put the start date on the button's screen.

## F. AI credits and consumables

### 20. Allowance in the plan, credits as a top-up for subscribers
**When:** credit packs sit on the first paywall next to the subscription, or
AI use has no visible allowance.
**Cross-check:** the subscription includes a stated allowance; packs are
offered to subscribers who run out.
**How:** "Pro includes 200 generations a month"; at zero, a top-up for
subscribers and the plan for free users.
**Evidence:** #U32 Mojo: credit packs off the first paywall, +14% new
subscription revenue, no rise in AI cost (strong). Adapty A/B library: a
mixed consumable + subscription cross-placement lost (directional). Apple
3.1.2(a) allows subscriptions that include credits and discounted
consumables (rule).
**Seen in:** Bevel, Ahead, Mimo, CapCut, Perplexity, Riveo.
**Trap:** no public data on allowance size or pack pricing (gap).

### 21. Credit packs priced in real money
**When:** packs show only credits, bonuses and strikethroughs.
**Cross-check:** the real-money price of each pack and what one action
costs.
**How:** price per pack, cost per action, rollover rules stated.
**Evidence:** Apple 3.1.1: purchased credits "may not expire" (rule); EU CPC
principles on virtual currencies: show real-money prices, don't force buying
more than needed (guidance, games); HIG total billing price.
**Seen in:** Bevel (per-action cost table), Riveo (cost of this action),
CapCut (credits valid for a fixed period: an iOS 3.1.1 risk).
**Trap:** pack sizes that never match action costs leave stranded balances.

## G. Always-on surfaces and lifecycle

### 22. Plan status surface
**When:** no place in the app shows the plan or how to upgrade.
**Cross-check:** a settings card or plan row with status, and for payers the
renewal date and upgrade/downgrade/cancel paths.
**How:** one persistent card; for free users the main tier's value, for
payers their plan and the next step.
**Evidence:** HIG: manage subscriptions in app, show renewal date (guidance).
Adapty A/B library: in-app paywall tab or icon, opens ~+20–25% (directional).
Observed in 15 apps.
**Trap:** a non-dismissable banner on top of the core screen is noise; keep
persistent surfaces out of the main task.

### 23. Trial and reverse-trial countdown with usage
**When:** free users on a trial or reverse trial get no signal before it ends.
**Cross-check:** a countdown with what they've used and what they'll lose.
**How:** "3 days left · you've used 4 Pro features" with the plan and a plain
"keep free" path.
**Evidence:** #U45 randomized trials for free users: 7-day vs 3-day, no
significant immediate effect, delayed paid conversion +42% (strong, SaaS;
it tests trial length, not the countdown screen).
#U46 reverse trial after paywall dismissal 0.4% → 4.5% (anecdotal, = onboarding
E6). #U47 Lumosity, #U48 Dropbox (directional).
**Seen in:** Monzo (reverse trial tab with usage), Duolingo, Headway, Atoms.
**Trap:** judge reverse trials on delayed conversion, not the first week.

## H. Legal and store flags

### 24. Compliance flags
Flag, don't rule. Details and links in `platform-rules.md`; most legal sources
are secondary summaries.
- Active subscribers shown the subscribe paywall (HIG).
- No total billed price or period; per-credit price only (HIG, Play).
- Fake countdown, reset timers, scarcity claims (UCPD Annex I; ACM v. Epic;
  CMA v. Emma).
- No clear decline, confirmshaming decline (FTC v. Amazon order).
- Pre-checked paid add-ons (CMA opt-in
  cases).
- Button layouts where navigation triggers a purchase; an imitation of
  Apple's confirmation sheet (FTC v. Epic; HIG).
- Tasks required to get what was paid for (3.1.2(a)).
- Outside the US: a link or button to web checkout without an entitlement
  (3.1.1(a), 3.1.3). In the US it's allowed; the commission is still in court.
- Web-billed upgrades: express consent to the new terms (California ARL;
  whether an upgrade counts as an amended contract is unresolved).
- EU personalised prices by automated decision-making need disclosure
  (Omnibus).

## Where it flips

| Tactic | Wins when | Loses when | Evidence |
|---|---|---|---|
| Tighter free tier | Measured on conversion over weeks | Measured on engagement, ads, virality over months | #U8, #U9, #U13 |
| Gate a feature | It's an extra on top of the habit | It's the habit itself | #U4, #U3 vs #U1, #U7 |
| Teaser of locked value | The value is new | The value already feels owned | #U3 |
| Second-chance discount | After the onboarding paywall | After the main in-app paywall | #U44 |
| Plan-switch offer | To engaged monthly payers (hypothesis) | On the cancel sheet (~0.6% accepted) | #U31 |
| Annual-only | Revenue per day | Daily conversions (−20%) | #U28 |
| Lifetime next to annual | Total conversions (+10%) | Annual share (−30%) | #U22 |
| Credits on the first paywall | — | Removing them raised subscription revenue 14% (strong). On a later in-app paywall the test is off-target: High at most | #U32 |
