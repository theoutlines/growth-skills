# Growth levers by journey stage

The levers a designer can pull in a mobile subscription app, from the ad to
the win-back. Each lever points to the teardown pattern that holds its
evidence and its range. Ranges live in that teardown's `references/ranges.md`
(row = the pattern named here); tiers are the strongest tier in its
`evidence.md`. This file holds no numbers of its own.

How to tell the status:
- **Present**: the screen or element exists and matches the "Looks like" line.
- **Weak**: it exists but misses the "Looks like" line (a generic version, the
  wrong moment, missing parts).
- **Absent**: the product has the stage but not the lever.
- **N/A**: the stage or lever doesn't fit the product (see "Applies when").
- **Unknown**: not shown or described. Ask about it; never guess.

Status rules:
- A step missing from a sequence the user described in full ("questions →
  loader → paywall") is **Absent**; a step never mentioned is **Unknown**.
- A lever that is a property of an element that exists (a forgiving streak,
  a paywall right after value) is **Absent** when the element lacks that
  property entirely, **Weak** when it has part of it.
- **Wrong moment is Weak.** An element that exists at the wrong time (a
  notification ask at launch, a rating ask on the 3rd open) is Weak, never
  Absent.
- **Partial surfaces are Weak.** A Settings link to the store page with no
  plan or date in the app is Weak for U6. A cap on free content items is a
  usage limit for U2.
- **One observation, one lever.** When one element fits two levers, it
  counts only for the lever that owns it (below); the other lever is judged
  on the rest of its "Looks like" line, or Unknown.
  - The first notification ask belongs to O5. R3 is judged on reminder setup
    after the first session.
  - The in-app plan, price and renewal date belong to U6 (a store link
    alone is Weak there). C1 is judged only on whether the way to cancel
    can be found.
- Only rows in `ranges.md` that measure this lever's change count as its
  range. A row about a nearby change (a reminder promised before the trial
  for R7, a notification for an in-app screen) is off-target: say so, or
  write "no published range".

## W. Web funnel (only if the app sells on the web or plans to)

| ID | Lever | Looks like | Applies when | Teardown · pattern |
|---|---|---|---|---|
| W1 | Landing matches the ad | First screen repeats the ad's promise, one easy first answer | Paid traffic to the web | web2app-teardown · 1, 2 |
| W2 | Honest quiz pacing | Short loaders, progress that tracks real steps | A web quiz exists | web2app-teardown · 3, 6 |
| W3 | Result built from the answers | A plan screen that uses the answers, no outcome claims | A web quiz exists | web2app-teardown · 4 |
| W4 | Email after value | Email asked after the result, with a reason | Web funnel | web2app-teardown · 5 |
| W5 | Charge-first web paywall | The real charge is the biggest price; dated trial timeline | Web paywall | web2app-teardown · 7, 8 |
| W6 | Wallets first at checkout | Apple Pay / Google Pay above the card form, local methods by market | Web checkout | web2app-teardown · 11, 12 |
| W7 | Into the app without a password | Store button + magic link or deep link after purchase | Web purchase | web2app-teardown · 19 |
| W8 | Web option beside in-app purchase | Link-out next to IAP with both prices | iOS app in a market that allows link-outs | web2app-teardown · 20 |

## O. Onboarding and activation

| ID | Lever | Looks like | Applies when | Teardown · pattern |
|---|---|---|---|---|
| O1 | Value promise on screen 1 | Outcome headline, not a logo or sign-up wall | Always | onboarding-teardown · 1, 2 |
| O2 | Goal question early | One question that changes what comes next | Always | onboarding-teardown · 3 |
| O3 | Answers echoed back | Plan, copy or visuals name what the user chose | A goal or intent question exists | onboarding-teardown · 10 |
| O4 | First own result before the paywall | The user makes or hears something of their own | The product can produce a result in under a minute | onboarding-teardown · 9, 12, 13 |
| O5 | Permissions in context | Ask after the user sees why, with a preview | The app asks for permissions | onboarding-teardown · 17 |
| O6 | Account at the right time | Sign-up after value, or skippable | An account is required | onboarding-teardown · 16 |
| O7 | Length fits the category | Steps match the bucket norm; heavy steps have an escape hatch | Always | onboarding-teardown · 6, 20 |

## P. The first paywall and the seam

| ID | Lever | Looks like | Applies when | Teardown · pattern |
|---|---|---|---|---|
| P1 | Paywall right after the value moment | No filler screens between value and price | Onboarding paywall | flow-teardown · S1 |
| P2 | Paywall echoes the onboarding | Headline and visuals repeat the goal | Onboarding paywall | flow-teardown · S2 |
| P3 | Trial timeline and kept reminder | Today / reminder / charge on the paywall, and the reminder really sent | Free trial | flow-teardown · S5 |
| P4 | Pre-paywall or two-step paywall | A "how your trial works" step before plans | Onboarding paywall | flow-teardown · S4 |
| P5 | A deliberate step after close | Close leads to the product, or one second offer only after the onboarding paywall | Onboarding paywall | flow-teardown · S7, S8 |
| P6 | Paywall itself | Plans, social proof, CTA, close (run paywall-teardown). Unknown without a paywall screen. No ranges.md: quote paywall-teardown's expected effect labelled "Adapty prior" | Any paywall | paywall-teardown |

## U. Monetizing inside the product

| ID | Lever | Looks like | Applies when | Teardown · pattern |
|---|---|---|---|---|
| U1 | Contextual gates | A locked feature opens an upsell about that feature | Free use exists | upsell-teardown · 1, 9 |
| U2 | Meter before the wall | "x of y left" near the action | Usage limits exist | upsell-teardown · 5 |
| U3 | Upsell after a success moment | Offer after a finished task, not mid-task | Free use exists | upsell-teardown · 3 |
| U4 | Core habit stays free | Daily core action never hard-blocked | Free use exists | upsell-teardown · 4 |
| U5 | Payer ladder | Upgrade screen for payers, annual switch for happy monthly payers | Payers can upgrade | upsell-teardown · 15, 16, 17 |
| U6 | Plan status surface | Plan, renewal date and options in one place | Always | upsell-teardown · 22 |

## R. First weeks to the first renewal

| ID | Lever | Looks like | Applies when | Teardown · pattern |
|---|---|---|---|---|
| R1 | Welcome with a first step | What you now have + one first action | Always | retention-teardown · 1 |
| R2 | Trial status in the app | End date, amount and where to cancel | Free trial | retention-teardown · 2 |
| R3 | Reminder after the first session | Time picker after the first session | Recurring task | retention-teardown · 4, 7 |
| R4 | Progress where the user lands | Streak, weekly goal or "x of y" on home | Recurring task | retention-teardown · 10 |
| R5 | Forgiving streak | Easy to keep; repair, freeze or pause when broken | A streak exists | retention-teardown · 11, 12 |
| R6 | Recap of the user's value | Weekly or monthly summary in the user's unit | Always | retention-teardown · 17 |
| R7 | Trial-ending notice with usage | In-app card before the charge: what they used, date, amount, cancel path | Free trial | retention-teardown · 19 |
| R8 | Return screen | Resume or a lighter restart after a gap | Always | retention-teardown · 20 |
| R9 | Rating ask after a task | System prompt after a completed task, no sentiment gate | Always | retention-teardown · 21 |

## C. Cancel and win-back

| ID | Lever | Looks like | Applies when | Teardown · pattern |
|---|---|---|---|---|
| C1 | Findable cancel | "Manage subscription" or a cancel link that a user finds in two taps from Settings or Profile | Always | cancel-flow-teardown · 1, 2 |
| C2 | Reason survey routes the offer | Optional reasons; each leads to its own help or offer | Always | cancel-flow-teardown · 3, 4 |
| C3 | Pause or plan switch | Pause (where billing allows) or a cheaper plan | The app has a pause or a cheaper plan to offer; otherwise N/A | cancel-flow-teardown · 5, 6 |
| C4 | Clean exit | Cancel visible next to every offer; one save screen at most (no save screen at all counts as Present) | Always | cancel-flow-teardown · 10, 11 |
| C5 | Billing-issue banner | In-app banner when a payment fails | Always | cancel-flow-teardown · 13 |
| C6 | Easy way back | One-tap resubscribe; win-back after lapse | Always | cancel-flow-teardown · 14, 15 |
