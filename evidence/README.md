# Evidence base

One record per published test, the single source of truth for every growth skill and the [Growth Test Planner](https://planner.theoutlines.xyz). Public sources only.

| File | What it holds |
|---|---|
| `tests.csv` | 290 records: published tests and aggregated priors from the onboarding, flow, upsell, cancel, web2app and retention libraries |
| `SWEEP.md`, `inbox/` | The weekly sweep: what a scheduled run does and what it found each week (a pull request the owner merges) |
| `planner-ideas.csv` | Which records stand behind each idea in the planner (`adapty:<section>` = a band from Adapty's A/B library) |

## Fields

- `id`, `library`: the ID the skills cite (#12, U3, C17, W40, R48, E1). Copies between libraries keep the original ID; never renumber.
- `section`, `columns`: where the row sits in the skill's `evidence.md` and which columns that table prints.
- `app`, `category`, `bucket` (RevenueCat SOSA), `ai`, `surface`, `change`, `metric`, `result`, `date`, `sources`, `tier_text`: what the skills print, word for word.
- `tier`: strong, directional, anecdotal, observed (or aggregate for E rows).
- `outcome`: win, loss, null, mixed (one metric up, another down, or one arm won and another lost) or none (no lift to read: no numbers, not a test, a share of revenue). **Losses and nulls are recorded, never dropped.**
- `bundled`: yes when the change came with other changes, so the number can't be credited to one mechanic.
- `same_as`: `library:id` when the row is a copy or a second report of the same experiment (C18 = C17, U6 = #46). Second reports stay separate records; their numbers are never merged.
- `split`: `market:`, `platform:` or `segment:` and the figures, when one test reports different numbers by market or platform (#13 global vs US, #43 by country, #14 iOS only). Anything that shows one number from such a record says which figure it uses (`split_choice` in `planner-ideas.csv`; the check enforces it).
- `mechanics`: the patterns (library:number) whose ranges cite this record.
- `checked`: the date the source page was last opened and the number read.

## How to change it

1. Add or edit the record in `tests.csv` first (open the page, read the number, set tier, outcome and bundled).
2. `python3 scripts/evidence.py build` writes the rows into each skill's `evidence.md`.
3. Rebuild that skill's `ranges.md` and anything citing the record (variant-check mechanics, planner ideas).
4. `python3 scripts/evidence.py check` must report 0 problems before a push (also runs in CI).

Not in the base yet: benchmark tables (section C of each library, retention B rows) and Adapty's library bands, which stay in their own files.
