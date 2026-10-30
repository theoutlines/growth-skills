# Onboarding Flow Score Rubric

A 100-point score for a first-run flow, from the first screen to the first
paywall and what happens when it's closed. The score exists so two people who
run the same screens get the same number, and so a team can re-run the
teardown after shipping changes and see it move. Score from the checks below,
never from overall impression.

## How to score

- Each check has a point value. Award **full** points when the check is
  clearly met, **half** (round down) when it is partly met, **zero** when it
  is missing. No other values.
- **Judge against the category.** Several checks say "fits the bucket norm".
  Use `categories.md`. An early account in a VPN app or no onboarding paywall
  in a dating app is the norm, not a gap.
- **Counting screens.** Skip system splash and launch screens (logo only):
  "screen 1" is the first screen with content. "The first third" means the
  first third of the screens before the first paywall, counted by position
  (unseen screens and carousel slides count), rounded up: with 11 screens
  before the paywall, positions 1–4 are the first third.
- **Score only what you were given.** If a check depends on screens you didn't
  get (the paywall, what happens on close), award half and list those screens
  under "Missing screens". Never guess what an unseen screen does.
- **Absent is not missing.** When the flow simply has nothing to judge (no
  permission is needed, no heavy step exists) and you saw the whole flow, award
  full.
- **Unseen screens: one rule.** If what you saw already earns full, award full.
  If what you saw earns less and uncaptured screens could hold what's missing,
  award half and count the other half as held back. If what you saw earns less
  and no unseen screen could change it (the paywall is visible and has no
  proof), score it as seen; nothing is held back. A row in the table is allowed
  only for what you saw.
- **Points held back.** Add up the points lost only to unseen screens. If they
  reach 10 or more, show them on the score line ("· 13 pts held back by
  missing screens") and say in the read line that the grade reflects missing
  captures, not a weak flow.
- **Input means answers or data.** Linked or imported data (bank accounts,
  Screen Time, a photo) counts as the user's input wherever a check says
  "answers".
- **No onboarding paywall.** If the flow ends in the product with no paywall
  and that fits the bucket (pattern 29), replace dimension 5 with 5b, "The
  first limit" (also 20 points). If the limit screens weren't shared, award
  half on every 5b check and ask for them.
- **Consistency rule:** every dimension that loses 4+ points on what you saw
  must show up in the hypotheses table. Points lost only to unseen screens
  don't count; they go under "Missing screens". A deduction with no matching
  test idea means the score or the table is wrong. Fix one.
- **One miss, one deduction.** Whether the paywall reuses the onboarding is
  scored only in dimension 5. Don't take it again in dimension 2.
- **Hard cap (compliance):** if a permission pre-prompt breaks a platform rule
  (says "Allow", mimics the system alert, rewards allowing, gates a feature on
  ATT), or a "free" trial hides the price that follows, cap Friction & setup
  at 5 and make that row "Fix first". A two-button pre-prompt that doesn't say
  "Allow" or mimic the alert (e.g. "Enable notifications" / "Not now") is a
  flag in the notes, not a cap.

## 1. Value before the ask — 25

| Check | Pts |
|---|---|
| Screen 1 states an outcome for the user, not a logo, a generic welcome or a bare sign-in sheet | 5 |
| The user does the app's core action once before the paywall and sees the result: an edited photo, a lesson, a heard voice, their own data organised. Half: a sample, a demo, a mockup, or a personal plan without the core action. Zero: a feature carousel only | 8 |
| A plan, report or result screen before the paywall reflects the user's own answers or input. Half: personal but generic ("your plan is ready" with nothing personal in it) | 7 |
| Interstitials and headlines describe outcomes or jobs, not feature names. Half: a mix | 5 |

Tie-break: a flow with no questions and no paywall (tool-first apps) earns
the plan-reveal check in full when the user lands in a working product.

## 2. Personalisation — 20

| Check | Pts |
|---|---|
| A goal or intent question appears in the first third of the screens before the paywall. Half: later than that. Bucket exceptions earn full with no questions: VPN, password and AI-chat apps; link-first apps (finance, Screen Time) that link before the paywall | 5 |
| Answers or linked data are visibly used before the user leaves onboarding: on a plan, report or result screen, or a first home screen that names them. Half: only a generic "picked for you" claim | 6 |
| Hard or sensitive inputs carry a "why we ask" line, a reassurance or an "I don't know" option | 4 |
| Question count isn't above the bucket's range, and no step serves nothing (no personalisation, value, proof, setup or legal purpose; one attribution question is fine). Half: above the range, or 1 dead step. Zero: 2+ dead steps. Fewer questions than the range is not a miss | 5 |

## 3. Friction & setup — 20

| Check | Pts |
|---|---|
| Account creation timing fits the bucket. Full: after first value, or after the user has built something and the account is framed as saving it ("save your plan"), or early when sync or security is the product. Half: after setup but framed as a gate. Zero: before any value with no reason | 5 |
| Permissions are asked in context with a preview of the benefit, via a pre-prompt compliant for the platform (iOS: one "Continue", never "Allow"; Android: a "No thanks" option is expected). Half: in context but with no preview. Zero: on launch with no reason. None needed before the paywall: full | 6 |
| Heavy steps (bank linking, photo access, KYC, long forms) offer a way round: demo, sample, Skip, "I don't know". No heavy step: full | 4 |
| Flows longer than about 8 screens show progress; 20+ screens use chapters. Flows of 8 or fewer earn this in full | 3 |
| No dead weight: no loader without a personal payoff after it, no setup a default would cover | 2 |

## 4. Trust & commitment — 15

| Check | Pts |
|---|---|
| Social proof appears before or on the first paywall. Full: rating with volume, a result-naming review, or research in health. Half: vague ("loved by millions") | 5 |
| The category's trust axis is addressed somewhere in the flow — see the table below | 5 |
| A retention loop is set up before the user leaves onboarding: a reminder time, a notification opt-in with a reason, a widget, a daily or weekly goal the app checks in on (a calorie target counts), a streak, or a commitment. Exception: on-demand utilities (VPN, password, scanner, weather) earn full. Budgeting and habit apps are not exempt | 5 |

## 5. The seam — 20

| Check | Pts |
|---|---|
| Paywall position fits the bucket: after the plan reveal in quiz funnels, right after the first result in try-first apps, at the first premium action in tool apps | 5 |
| If a trial is offered, the user sees when they'll be reminded and charged (timeline, reminder toggle or a dated line), next to the price. Half: a one-line reminder promise. No trial: full if the charge today is unambiguous | 5 |
| The paywall echoes the onboarding: the user's goal, plan or numbers appear on it | 4 |
| Closing the first paywall is handled on purpose: one second-chance offer, a downsell, or a clear free path into a working product. Zero: dead end or a loop back to the paywall | 3 |
| Trial structure fits the bucket and the AI tag (short or none in AI and Photo & Video, longer in meditation), and it's stated on the selected plan | 3 |

## 5b. The first limit — 20 (freemium flows only, replaces 5)

| Check | Pts |
|---|---|
| The limit is visible before it's hit: a counter ("2 more free workouts"), credits left, or an upgrade pill from day one | 5 |
| The limit-hit paywall appears right after a success (a finished workout, a generation, a match), not mid-task where work would be lost | 5 |
| The limit paywall names what the user was just doing and what upgrading unlocks for it | 4 |
| A free path continues and is clear: wait for a reset, watch an ad, use a smaller model | 3 |
| The offer fits the cost of free use: short or no trial, or credits, in AI apps; terms stated next to the CTA | 3 |

## Trust axis by bucket

| Bucket | What earns the 5 points |
|---|---|
| Health & Fitness | Credibility of claims: sourced numbers, research, results from real users |
| Education | Outcomes with timeframes, or credible teaching (level calibrated to the user) |
| Productivity | Honest free tier or clear trial terms; for AI assistants, usage limits stated up front |
| Utilities: VPN, passwords | Security credibility: audits, encryption, no-logs claims stated plainly |
| Utilities: finance | Data safety at linking: read-only, "we don't sell your data", why it costs money |
| Photo & Video | Realism: the result is the user's own photo, not a styled mockup |
| Media & Entertainment | Proof of quality: a sample to hear or watch, or recognisable proof of volume |
| Social & Lifestyle | Safety and privacy: verification, what others see, data use next to sensitive inputs |
| Business | Professional output: the invoice or document looks client-ready; data and payment security stated |
| Education: kids | Parent trust: a parental gate before purchases, no nudges aimed at the child |

## Grade bands

| Score | Grade | How to frame the teardown |
|---|---|---|
| 85–100 | Strong | Refinements. Say it's a strong flow. |
| 70–84 | Solid | A few clear gaps worth testing. |
| 50–69 | Leaking | The basics are costing trials or activation. |
| 0–49 | Needs work | Fix the basics before testing anything subtle. |
