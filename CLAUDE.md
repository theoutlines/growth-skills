# growth-skills — project memory

A Claude marketplace and plugin, `growth-skills`: screen teardowns for growth work on mobile subscription apps, for product designers. Author: Ivan Polushin (theoutlines). Public repo, MIT.

## Product split (agreed 2026-10-30)
- `subscription-skills` (theoutlines/subscription-skills) = the paywall and its numbers: benchmark reports (RevenueCat, Adapty, FunnelFox), Pricing Index, benchmark router, store compliance, Adapty's paywall-teardown and A/B test assistant. Self-contained product.
- `growth-skills` (this repo) = the journey around the paywall: web funnel, onboarding, the onboarding↔paywall seam, upsells, retention to first renewal, cancel flow, plus `growth-router`. It keeps growing (non-subscription directions later: currency, one-time purchases, etc.).
- This marketplace lists both plugins. `growth-skills` declares `subscription-skills` as a dependency (one install gets both). `subscription-skills` is referenced by `git-subdir` from its own repo, never copied: edit it there.
- Standalone skill repos are retired. Skills are edited only here, in `plugins/growth-skills/skills/`.

## Layout
- `.claude-plugin/marketplace.json` at the root (two entries); plugin at `plugins/growth-skills/` with its own `plugin.json`.
- Skills: `growth-router`, `web2app-teardown`, `onboarding-teardown`, `flow-teardown`, `upsell-teardown`, `retention-teardown`, `cancel-flow-teardown`. Each has `SKILL.md`, `references/`, `scripts/` (`render_report.py`, `test_duration.py`, `example.json`), `assets/fonts` (Inter, OFL).
- Evidence IDs per skill: onboarding #1–#77 and E1–E8 (shared with flow-teardown), upsell #U, cancel #C, web2app #W, retention #R (regulator rows in retention platform-rules use D). Rows copied between libraries keep their original number in a "Same as" note; never renumber.
- Raw research lives outside the repo: `/home/claude/onboarding-teardown-research/`, `/home/claude/upsell-research/`, `/home/claude/cancel-flow-research/`, `/home/claude/web2app-research/`, `/home/claude/retention-research/`.

## Rules
- Purpose: tools for product designers in the AI era. Only what a designer changes on a screen is scored, recommended or mentioned. No PM, engineering, push/CRM programme, payment-setup or legal-ops content.
- Never invent a number. Every figure links to its source with a tier: strong, directional, anecdotal, observed. On-target evidence beats strong evidence; bundled tests cap a row at Medium; never merge two tests into one number.
- Never reward pressure or friction. Flags are design rules with a source name, not legal advice.
- Rubric rules shared by all teardowns: full / half (round down) / zero; unseen → half held back; one issue, one deduction; blockers cap the total at 49; held back ≥10 shown; up to 8 rows, never pad.
- Buckets = RevenueCat SOSA categories; "AI app" is a tag. Keep metric definitions apart (per install / trial start / paywall view / session / subscription).
- Mobbin content is described in our own words, never copied; example teardowns don't name the app. Public sources only; no employer data. Walkthroughs never enter a name, phone, password or payment data and never skip a gate by URL.
- Test changes with independent subagent runs on the same briefs (scores must reproduce within a few points). Run `claude plugin validate .` before every push. Bump `version` in plugin.json and the marketplace entry on every release; attach one zip per skill to the GitHub release (the owner publishes releases; this session can't).

## Status (Oct 2026)
- v1.0.0: six teardowns moved in from their standalone repos (onboarding v0.1.1, flow v0.1.1, upsell v0.2.0, retention v0.1.2, cancel v0.2.0, web2app v0.1.1) plus `growth-router`. Install tested: growth-skills installs with subscription-skills as a dependency.
- Standalone teardown repos deleted; release v1.0.0 with per-skill zips published by the owner. Repo About and topics set (changed through the owner's signed-in Chrome; the session proxy can't write repo settings).
- Not submitted to the Anthropic directory yet. No icon (deliberately).

## Next (plan)
1. Test the router and the dependency in the Claude app (Customize → Plugins → Add marketplace).
2. Launch post for Growth Skills.
3. Paywall test planner: clickable prototype, then live build on the owner's domain; link "read the result" from the plan screen.
4. Bundle Adapty's State of Paywalls into subscription-skills once the MIT licence lands.
5. New growth directions only with enough public evidence (e.g. in-app currency / one-time purchases); hypotheses-only topics are dropped.
