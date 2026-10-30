# Seam patterns

What happens at the seam between onboarding and the paywall. Test numbers
(#N) match `evidence.md` here and the onboarding-teardown evidence library, so
the same test has the same number across the suite. Evidence tiers: strong,
directional, anecdotal, observed (see `evidence.md`).

## A. Tactics that flip sign by position

The same element wins in one place and loses in another. This is the main
reason to review onboarding and paywall together.

| Tactic | Wins where | Loses where | Evidence |
|---|---|---|---|
| Second-chance discount | Right after the onboarding paywall is closed: premium conversion about +25–30% | After the main in-app paywall: ARPU cut by roughly half | Adapty library (E2, directional) |
| "How your trial works" explainer | Next to the price: ARPU up; Blinkist timeline +23% trial sign-ups (#1, strong) | Several screens before the paywall: drop-off before the paywall is ever seen | Adapty library (E3, directional) |
| Comparison table | On the paywall, including the onboarding paywall | As a bare teaser screen before the paywall | Adapty library (E4, directional) |
| Guarantee or refund promise | At the ask, next to the CTA | As its own screen before the paywall: plants doubt ahead of the ask | Adapty library (E5, directional) |
| Loader / "building your plan" | After real personalisation, leading straight to a plan that shows the answers | With nothing personal after it: removal won +22% trial conversion, +30% ARPU (#15, directional); loader + plan lost ARPU about −50% (E1) | contested |
| Paywall position | After a few motivation or value screens, at peak intent: Opal 7% → 17% download → trial over many tests (#8, directional) | On screen 1 with nothing shown, or after a long tail where reach collapses (one app: only 40% saw the paywall, anecdotal) | #8, #71, #72 |
| Discount on store-sheet abandon | 17% of revenue across 18 apps (#75, directional) | App Review scrutiny for "unintended purchases" | #75 |

## B. Seam patterns

### S1. Paywall right after the value moment
**When:** a neutral or heavy screen sits between the plan, first result or own
data and the paywall. **How:** move the paywall to follow the value moment
directly; move account and permissions after the paywall or before the value
moment. **Evidence:** #8 (directional); #71 FitnessAI paywall moved earlier,
install-to-trial doubled, trial-to-paid unchanged (directional, bundled);
#72 Rootd revenue 5× (directional, before/after). **Trap:** earlier moves trial
starts and activation in opposite directions; read both.

### S2. Paywall echoes the onboarding
**When:** the user answered questions, built a plan or linked data, and the
paywall is generic. **How:** goal or plan in the headline, one personal number,
saved items. **Evidence:** #22 Flirt AI answer-routed paywalls, +20% trial-to-
paid (directional, confounded); #54 Daily Horoscope geo paywalls +183% (strong,
geo not answers). **Trap:** echo goals, not sensitive data.

### S3. Promise continuity
**When:** screen 1 or the value moment promises one outcome and the paywall
sells features or a different outcome. **How:** reuse the outcome words from
screen 1 in the paywall headline and CTA. **Evidence:** #11 outcome vs feature
copy, +17% trial conversion, +13% ARPU (directional); #58 paywall copy from
features to jobs, +54% or more (directional). **Trap:** copy-only changes are
small; don't promise more.

### S4. Pre-paywall step
**When:** a dense paywall carries benefits, trial terms and price at once.
**How:** "try it free, no payment due now" or a what-you-get screen, then the
price. **Evidence:** #55 Speak4Me multi-step paywall +27% conversion, +36%
proceeds (strong); #56 Stompers +16% (strong, metric ambiguous); #24 Superwall
multi-page 12.41% vs 9.07% (directional, observational). **Trap:** a trial
explainer placed far from the price flips sign (section A).

### S5. Trial timeline and a kept reminder
**When:** a trial is offered without a dated reminder and charge next to the
price, or a reminder is promised with no permission or email collected.
**How:** Today / reminder day / charge day under the price; ask for
notifications behind a sample reminder right after the trial starts.
**Evidence:** #1 Blinkist +23% trial sign-ups, −55% complaints, push opt-in
6% → 74% (strong); #65 Shaw Academy reminder email +14% sales (strong).
**Trap:** a promise not kept turns into refunds and reviews.

### S6. Trial structure at the seam
**When:** always check the trial against the bucket and the AI tag.
**How options:** trial on annual only; opt-in trial toggle; one-tap trial
button; a paid longer trial beside the free one. **Evidence:** #41 Moonly trial
on annual only +39% view-to-subscription (strong); #45 Slopes one-tap trial
+25% trial starts (strong); #57 Ahead paid 30-day trial +7% (strong); #21 Rizz
God early toggle-off paywall plus a second paywall +10% / +10% (directional).
**Trap:** trial lengths mature at different speeds; don't read a trial test on
day 7.

### S7. A deliberate post-close step
**When:** closing the onboarding paywall drops the user into the product with
nothing, or into a loop. **How:** one offer shown once: discount, monthly
downsell, longer trial, or a reverse trial (temporary premium, no card).
**Evidence:** E2 second chance after the onboarding paywall +25–30% (Adapty
library); reverse trial 0.4% → 4.5% freemium conversion (E6, anecdotal);
Headway, Tolan, Opal show monthly or lite plans as the second offer (observed).
**Trap:** after the main in-app paywall the same discount halves ARPU.

### S8. Dismiss treatment
**When:** always note how the paywall closes. **How:** make the trade-off
explicit; a quieter close tends to raise ARPU and lower activation.
**Evidence:** #9 Opal (anecdotal); #6 Duolingo quiet "Later" +8.2% DAU (strong,
sign-up wall). **Trap:** Play policy and consumer law expect a clear way out.

### S9. First limit (freemium)
**When:** the app has no onboarding paywall by design. **How:** make the limit
visible from day one, show the limit paywall right after a success, name what
the user was doing, keep a free path. **Evidence:** #63 Busuu one-language
limit +83% power-user conversion (directional); #46 Slopes trial popup at the
moment of use, about 3× trial starts (directional); E7 contextual copy +10–15%
(anecdotal). **Trap:** reviewing only first-run screens misses where the app
monetises.
