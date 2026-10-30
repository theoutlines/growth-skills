# Seam Score Rubric

A 100-point score for the seam: how the onboarding hands over to the paywall,
and what happens around it. It's judged on the screens just before the first
paywall, the paywall's framing (not its layout), and the screens after it is
closed. The onboarding and the paywall themselves get their own scores.

## How to score

- Each check is **full**, **half** (round down) or **zero**. Nothing else.
- Score only what you were given:
  - What you saw already earns full → full.
  - What you saw earns less, and uncaptured screens could hold what's missing →
    half; the other half is held back.
  - Uncaptured screens could only hold a violation (a heavy step, a loader) →
    don't assume it; score what you saw.
  - An element on a captured screen that the description doesn't cover (the
    paywall's look, its headline) → half, held back as a description gap.
  - Nothing to judge (no explainer, no discount, no promise) → full.
- **One miss, one deduction across the three parts.** In this skill the seam
  owns the echo of goals and answers, promise continuity and the reminder; the
  paywall owns trial terms on the screen, social proof on the paywall and the
  CTA; the onboarding owns everything before the paywall. Don't deduct the same
  fact in two parts.
- **The value moment** is the last one before the paywall: a plan reveal, a
  first result, the user's own data, a finished session, or a saved selection
  of real content (a taste test that fills a library). A feature carousel is
  not one.
- **Held back per part** is reported after scaling (onboarding points × 1.25).
- Judge against the bucket's flow shape in `seam-norms.md`: an early hard
  paywall in a VPN or no onboarding paywall in dating is the norm, not a gap.
- **Freemium flows** (no onboarding paywall by design): score the seam between
  the first session and the first limit-hit paywall instead. Read "paywall" as
  "limit paywall" in every check.
- **Sign-flip rule:** a tactic placed on its losing side (see
  `seam-patterns.md`, section A) scores zero on its check and becomes a
  "Fix first" or "High" row, whatever else the flow does well.
- **Consistency rule:** every seam block that loses 4+ points on seen screens
  needs a row. In this skill, the part skills' own consistency rules are
  replaced by one rule: every part that loses 15+ seen points gets at least one
  row. Held-back points never require rows.
- **Rounding:** scale onboarding dimensions 1–4 (out of 80) to 100 and round
  half up.

## A. Placement — 25

| Check | Pts |
|---|---|
| The paywall arrives right after the value moment. Half: one or two screens of any kind in between. Zero: three or more, or no value moment before the paywall (unless the bucket norm is an early gate) | 8 |
| Position fits the bucket's flow shape in `seam-norms.md` | 7 |
| Reach is protected: no step that costs effort sits between the value moment and the paywall. Half: one light step (a one-tap Sign in with Apple, a single permission). Zero: a heavy step (a multi-field form, a permission chain, email verification) | 5 |
| One deliberate onboarding paywall, or a deliberate multi-step paywall; not two unrelated paywalls back to back. In freemium mode a soft first limit and a hard later limit count as deliberate | 5 |

## B. Continuity — 25

| Check | Pts |
|---|---|
| The paywall echoes what the onboarding built: the goal, the plan, the user's numbers or saved items | 8 |
| What the paywall sells doesn't contradict what the first screen and the value moment promised. Full: the same outcome, or a generic pitch (the paywall part already scores a generic headline). Half: a related but shifted outcome. Zero: a different outcome | 6 |
| A pre-paywall step (what you get, or "try it free, no payment due now") sits before a dense price screen. Full also for a light paywall: it fits one screen without scrolling and has three or fewer value lines | 6 |
| The paywall looks like part of the flow (same design language and tone), not a different product | 5 |

## C. Trial and commitment clarity — 20

| Check | Pts |
|---|---|
| The trial story is consistent across the flow: what the pre-paywall, onboarding and paywall say about the trial (length, reminder, what happens on day N) matches, and the user learns when they'll be reminded and charged before they commit. Half: told only in one line. Zero: the screens contradict each other. The paywall's own trial terms belong to the paywall part, not here. No trial and no trial talk: full | 8 |
| A reminder promise is backed by a way to keep it: notification permission or an email (Sign in with Apple counts). No promise made: full | 6 |
| Trial or commitment explainers sit next to the price, not several screens before it (sign flip) | 6 |

## D. After close — 20

| Check | Pts |
|---|---|
| Closing the paywall leads somewhere deliberate: one second-chance offer, a downsell, a longer or reverse trial, or a clear free path into a working product | 8 |
| Any second-chance offer (discount or cheaper plan) follows the onboarding paywall only, not the main in-app paywall (sign flip), and is shown once. None present: full | 6 |
| No dead end or loop: the user can reach the product or the store sheet without being trapped. A discount on abandoning the store sheet is flagged as an App Review risk | 6 |

## E. Sign-flip hygiene — 10

| Check | Pts |
|---|---|
| No comparison teaser before the paywall; comparison lives on the paywall itself | 4 |
| No guarantee or refund screen before the paywall; guarantees answer the ask at the ask | 3 |
| No loader between the plan and the paywall without a personal payoff after it | 3 |

## Grade bands

Same bands as the other teardowns: 85–100 Strong, 70–84 Solid, 50–69 Leaking,
0–49 Needs work.
