# Lite checks (fallback when a part's own skill isn't installed)

Use these only when the onboarding-teardown or paywall-teardown skill isn't
available. Label the part's score "lite" everywhere, always in the same form:
"Paywall 64 (lite)". Each check is 10 points: full, half or zero. Same unseen-
screen and description-gap rules as `seam-scoring.md`; nothing to judge means
full.

Lite scores are coarser than the full rubrics. Don't compare a lite score with
a full score from an earlier run.

## Onboarding (screens before the first paywall) — 100

1. Screen 1 (after any logo splash) states an outcome for the user.
2. The user does the core action once before the paywall, or sees their own
   data organised. Half: a sample, a demo, or a plan without the core action.
3. A plan, report or result screen reflects the user's answers or data.
4. A goal or intent question sits in the first third of the screens before the
   paywall (link-first apps that link before the paywall, VPN, password and AI
   chat apps earn this with no questions).
5. Answers or linked data are visibly used before the user leaves onboarding.
6. Hard or sensitive inputs have a reason line or an "I don't know" option. No
   hard inputs: full.
7. Account timing fits the bucket: after value, or framed as saving what the
   user built, or early only when sync or security is the product.
8. Permissions are asked in context with a preview, via a platform-compliant
   pre-prompt (iOS: one "Continue", never "Allow"). None needed: full.
9. Social proof or the category's trust signal appears on the screens before
   the paywall (the paywall's own proof belongs to the paywall part).
10. A retention loop is set up (reminder time, goal, streak, widget, commitment).
    On-demand utilities earn this in full.

## Paywall (the first paywall screen or steps) — 100

Condensed from Adapty's paywall teardown rubric (MIT, © Adapty Tech Inc.),
reworded.

1. The headline states an outcome or the user's goal, not "Go Premium". Half:
   a trial offer as the headline ("Try PRO free for 7 days").
2. Value points describe results, are 5 or fewer, one line each.
3. One plan is clearly dominant (fill, border, size or pre-selection). Single
   plan: full.
4. Every plan shows its billing period next to the price.
5. The longer plan shows a per-week or per-month equivalent, or a comparison
   with the shorter one.
6. Savings are visible and legible (badge, strikethrough, "Save X%"). Single
   plan: full if the price is framed against something (per-month, per-day).
7. With a trial: its length and the price that follows are stated on the
   selected plan or under the CTA, linked explicitly ("then $X/year"). No
   trial: today's charge is unambiguous.
8. Social proof with specifics is on screen (rating with volume, or a review
   naming a result).
9. A reassurance line sits next to the CTA ("Cancel anytime", "No charge
   today").
10. The CTA names what happens ("Start my free week"), not "Continue", and is
    the most prominent element. From a description, judge the wording; the
    visual half is a description gap.

Hard cap: if prices contradict each other or a billing period is unreadable,
the paywall's lite score is at most 50 and that row is "Fix first".
