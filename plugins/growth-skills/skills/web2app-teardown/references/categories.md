# Web2app norms by category and by market

Collected 2026-10-30. Buckets are the RevenueCat SOSA buckets (primary App Store category), the same taxonomy as the onboarding, flow, upsell and cancel-flow skills. "AI app" is a tag, not a bucket. Finance apps have no SOSA bucket: use Utilities and say so.

On the web, **the market decides more than the category**: payment methods, consent wording, withdrawal rights and link-out rules change by country. Read the market table first.

Figures come from `evidence.md` (test #W numbers and Part 2 benchmark rows). App examples come from `flows.md` (observed, no performance data). The classic paid-social quiz funnels (Noom, BetterMe, Simple and similar) aren't on Mobbin; `walkthroughs.md` covers five of them up to their email or consent gate. "What to lean on" lines are hypotheses tied to those numbers, not tested norms.

## Markets

| Market | Payment methods to lead with | Consent and button | Withdrawal and reminders | In-app link to web (iOS) |
|---|---|---|---|---|
| United States | Apple Pay (~60% of web2app transactions worldwide, FunnelFox; +22.3% conversion when offered, Stripe holdback #W19); cards; PayPal 9.6% of web-billed subs (Recurly) | ROSCA: all material terms before billing info, express informed consent; California ARL: express affirmative consent to auto-renewal, consent records; NY: price increases need consent or a 14-day pro-rata exit | Card networks: trial reminder ≥7 days before (Visa), 3–7 days for digital trials over 7 days (Mastercard); California annual reminder | Allowed without an entitlement (3.1.1(a)); commission pending in court; IAP must stay for non-reader apps (3.1.3(b)) |
| Germany | PayPal (~90% of web2app transactions, FunnelFox; +47% for digital media, Stripe #W19) | §312j BGB: key terms directly above the button; button "zahlungspflichtig bestellen" or equally clear, otherwise no contract; "start free trial" on an auto-converting trial may not count as clear enough (court decision not opened) | 14-day withdrawal; waiver for digital content only with express consent and acknowledgement; withdrawal button since 19 Jun 2026; §312k cancel button | Only with Apple's EU entitlement (fees from 1 Oct 2026) |
| Other EU | iDEAL (NL +39%), BLIK (PL +46%), SEPA Direct Debit (+12%), PayPal 27.7% of web-billed subs in EMEA (Recurly) | CRD Art. 8(2): order button "with obligation to pay"; SCA / 3-D Secure on the first payment, including €0 trial setups | Withdrawal button; personalised streaming-type subscriptions are digital services (CJEU C-234/25), so the 14-day right can survive use | EU entitlement only |
| United Kingdom | Cards, wallets, PayPal | DMCC unfair practices since 6 Apr 2025: no auto-opted-in extras, no fake time limits (CMA v. Emma Sleep) | Subscription regime from 1 Jan 2027: reminders before a trial or discount ends, cooling-off at start and renewal | Entitlement regime (not US rules) |
| Japan | Konbini (+27% for digital apps, Stripe #W19) | — | — | Apple MSCA entitlement from 18 Dec 2025; 15% on sales within 7 days of the link |
| LATAM, APAC | Local methods; refunds run highest in APAC (8.00% of revenue, FunnelFox) | — | — | No link without an entitlement |

## Categories

| Bucket | What web funnels look like (`flows.md`) | Evidence in the library | What to lean on (hypothesis) |
|---|---|---|---|
| Health & Fitness | The classic paid-social quiz funnel: long quizzes, projection charts, "your plan is ready", $0-today trials or discounted first periods, reminder promises (Calm, Headspace) | Most app rows: Lasting quiz pacing +60% (#W9), Reading-style rebuilds, Rino, Shmoody and wellbeing payment recovery (#W23–#W25), Kompanion link-out (#W45), Runna retention (#W53). FunnelFox expert note: H&F web LTV $80–90 vs app $40–45 with higher web CPAs (anecdotal) | Health claims in "results" screens carry legal risk (FTC v. Genesis Tech allegations). Lean on pacing, honest plan screens and payment recovery before adding screens |
| Education | Trial-led (Duolingo: timeline, reminder screen) or discount-led (countdown banners, preset yearly toggle); lifetime next to annual (Babbel) | Reading.com rebuild (#W14), Flashbook localisation (#W18), English on Smartphone upsells (#W31), Adapty language app link-out reverted at the 15% tier (#W43) | Localised funnels and one-click upsells are the reported levers |
| Productivity (often AI) | Tier comparison tables instead of a single offer, mostly no trial, seat upsells after purchase (Grammarly) | Few app rows; Todoist sign-up hints (#W35) | Keep the comparison honest; post-purchase seat or tier upsells, each with its own accept |
| Utilities | Email-only checkout with account after payment, wide payment coverage, money-back guarantees, extra-months upsells (VPNs) | Payment recovery (#W24, #W25) is the closest evidence | Account after payment and broad payment methods |
| Photo & Video (often AI) | Aggressive pricing pages: "personal" discounts, one-time-offer clocks, stacked strike-throughs (AI creative tools); Canva the cleanest trial checkout | None in the test library (gap) | Timers here are the main flag risk; test without them |
| Media & Entertainment | Address for tax at checkout, long auto-renew text, bundles; Spotify the main US iOS link-out | Dipsea link-out test (#W39, the only randomized one), Spotify anecdote (#W50) | Reader apps can go web-only; others must keep IAP |
| Social & Lifestyle | Simple two-plan modals, preselected recommendations after purchase (Substack) | Hily direct billing (#W46, directional), AI companion placements (#W44) | Watch preselection after purchase |
| Business | Mostly web-native SaaS; landing-message match (#W1) and product tours (#W8) are the web evidence | #W1, #W8 | Landing-to-ad match and a tour before the ask |

Other facts that change advice:
- **Web share of subscription revenue** is small on average (3.2% globally, 4.9% in North America, RevenueCat SOSA), but 41% of top-tier apps have some web revenue. Top-100 grossing apps using web2app: 82% in 2025 (FunnelFox, inconsistent baseline).
- **Trial types on web** differ from the stores: 56.9% of web2app revenue comes from offers with no trial, 28.9% from paid trials, 14.3% from free trials (FunnelFox).
- **Plans on web** are monthly-heavy: 1-month 48.8%, 1-week 30.5%, 1-year 12.2% of web2app revenue (FunnelFox).
- **Refunds** are higher on web than many teams expect: US 5.67% of revenue, APAC 8.00%; 45% of refunds come within 24 hours (FunnelFox).
