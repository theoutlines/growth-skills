# Weekly evidence sweep

What a scheduled run does, once a week. The owner approves by merging the pull request; nothing enters `main` without that.

## 1. Look

Search for published A/B tests, case studies and talks about mobile subscription apps (paywall, onboarding, upsells, the first weeks before renewal, cancel flow, web funnels) published or updated since the last sweep (see the last `evidence/inbox/*.md`). Sources, in this order:

- Adapty: https://adapty.io/blog/ and https://adapty.io/case-studies/
- RevenueCat: https://www.revenuecat.com/blog/ and the Sub Club podcast https://subclub.com/
- Superwall: https://superwall.com/blog and https://superwall.com/case-studies
- Botsi: https://www.botsi.com/blog
- Apphud, Qonversion, FunnelFox, Purchasely blogs; Growth Gems https://growthgems.substack.com/
- Losses and nulls on purpose: search "A/B test lost", "didn't work", "no significant difference", "what we learned" with paywall / onboarding / subscription app. Published tests lean to wins (277 records: 5 losses, 2 nulls); a found loss is worth more than another win.

Skip: reports already in the base as benchmarks, vendor marketing without a number, anything behind a login, Reddit (blocked), anything about the owner's employer.

## 2. Check each candidate

- Open the page itself. Read the number on the page; never take it from a summary, a search snippet or another blog. If the page cites an original source, open that too and list both URLs.
- Already in the base? Compare app + change with `evidence/tests.csv`. A second report of the same experiment is a new record with a "Same as" note in `change`, never a merged number.
- Fill every field of the base (see `evidence/README.md`): library by where the screen sits in the journey (onboarding, upsell, cancel, web2app, retention; a first paywall in onboarding is onboarding), the next free ID in that library, `section` and `columns` copied from an existing table of that library that fits, SOSA bucket, metric with its denominator as the page states it ("denominator not stated" if it doesn't), result word for word in short, tier (strong only for a controlled test with numbers), outcome (win, loss, null, mixed, none), bundled, `checked` = today.
- No number → only if it's a loss or a null worth knowing (outcome none, tier anecdotal). Otherwise skip it.
- Public sources only. Describe screens in your own words.

## 3. Propose

- Branch `evidence/sweep-YYYY-MM-DD` from `main`. Add the records to `evidence/tests.csv`, run `python3 scripts/evidence.py build` (it writes them into each skill's `evidence.md`) and `python3 scripts/evidence.py check` (0 problems).
- Write `evidence/inbox/YYYY-MM-DD.md`: one line per added record (ID, app, change, the number, tier, outcome, link) and one line per candidate skipped, with the reason. If nothing new was found, write that and open no pull request.
- Open a pull request titled "Evidence sweep YYYY-MM-DD: N new records (W wins, L losses, X other)". The body is the inbox file.
- Do not touch `ranges.md`, the mechanics files or the planner: after the merge the owner asks for those to be rebuilt.
- Never bump the version, never push to `main`, never merge.
