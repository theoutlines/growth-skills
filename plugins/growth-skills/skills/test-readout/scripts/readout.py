#!/usr/bin/env python3
"""Read a finished A/B test on a subscription paywall or onboarding.

Input: a JSON file (see example.json). Per version: people who entered the test, payers per plan
(prices are given once), optional trial starts, refunds and weekly payers. Plus the plan the team
made before the test (decision metric, the smallest change worth catching, decision date) and today.

Output (JSON with --json, text otherwise): trust checks, the decision metric with a 95% range,
where the difference came from (how many paid vs which plans they chose), guardrails, and a verdict
class: win / loss / cant_tell / broken / too_early, or for a 'prove it's not worse' test:
not_worse / maybe_worse (one-sided: the low end of the 95% range must stay above -margin).

Method: sample-ratio check = chi-square, flagged at p < 0.001. Revenue per person = sum over plans of
payers * price / people; its variance per person from the plan mix; relative difference with a
delta-method 95% interval. Conversion = two-proportion test. Decomposition: ln(rev ratio) =
ln(conversion ratio) + ln(revenue-per-payer ratio). Refunds = two-proportion z-test on payers.
Sources: Kohavi, Tang, Xu, Trustworthy Online Controlled Experiments; Fabijan et al., KDD 2019.
"""
import argparse, datetime, json, math, sys


def norm_sf(z):
    return 0.5 * math.erfc(z / math.sqrt(2))


def rev_stats(v, prices):
    """Revenue per person from one value per payer per plan (first payment, or a value the team gives per plan)."""
    n = v['people']
    s1 = sum(v['payers'].get(p, 0) * prices[p] for p in prices)
    s2 = sum(v['payers'].get(p, 0) * prices[p] ** 2 for p in prices)
    m = s1 / n
    return m, s2 / n - m * m, s1


def rel_ci(mA, vA, nA, mB, vB, nB):
    r = mB / mA - 1
    se = math.sqrt(vB / nB / mA ** 2 + mB ** 2 * vA / nA / mA ** 4)
    return r, r - 1.96 * se, r + 1.96 * se


def prop_rel(xA, nA, xB, nB):
    if not xA or not xB:
        return float('nan'), float('nan'), float('nan')
    pA, pB = xA / nA, xB / nB
    se = math.sqrt((1 - pA) / xA + (1 - pB) / xB)                    # on the log of the ratio
    lr = math.log(pB / pA)
    return math.exp(lr) - 1, math.exp(lr - 1.96 * se) - 1, math.exp(lr + 1.96 * se) - 1


def z2(xA, nA, xB, nB):
    p = (xA + xB) / (nA + nB)
    se = math.sqrt(p * (1 - p) * (1 / nA + 1 / nB))
    return (xB / nB - xA / nA) / se if se else 0.0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('data')
    ap.add_argument('--json', action='store_true')
    args = ap.parse_args()
    d = json.load(open(args.data))
    A, B = d['A'], d['B']
    prices = d.get('value_per_payer') or d['prices']   # value_per_payer: e.g. weekly price x expected weeks, if the team has it
    plan = d.get('plan', {})
    metric = plan.get('decide_on', 'revenue')          # revenue | conversion | trial_starts
    bar = plan.get('smallest_change', 0.10)
    goal = plan.get('goal', 'win')                      # win | not_worse
    margin = plan.get('margin', 0.05)                   # for not_worse: how much worse is still fine
    out = {'checks': [], 'notes': []}

    # 1. sample ratio
    nA, nB = A['people'], B['people']
    exp_share = plan.get('share_B', 0.5)
    n = nA + nB
    eB = n * exp_share
    chi = (nB - eB) ** 2 / eB + (nA - (n - eB)) ** 2 / (n - eB)
    p_srm = math.erfc(math.sqrt(chi / 2))   # chi-square, 1 degree of freedom
    srm_ok = p_srm >= 0.001
    out['checks'].append({'name': 'groups split as planned', 'ok': srm_ok, 'value': f'{nA / n * 100:.1f} / {nB / n * 100:.1f}', 'p': p_srm})

    # 2. timing
    today = datetime.date.fromisoformat(d.get('today', datetime.date.today().isoformat()))
    decide = plan.get('decision_date')
    if decide:
        dd = datetime.date.fromisoformat(decide)
        timing_ok = today >= dd
        out['checks'].append({'name': 'waited for the last trials', 'ok': timing_ok, 'value': decide, 'days_left': max(0, (dd - today).days)})
    else:
        timing_ok = True
        out['notes'].append('No decision date given: check that the last trials have billed before trusting paid numbers.')

    # 3. decision metric
    payA, payB = sum(A['payers'].values()), sum(B['payers'].values())
    mA, vA, revA = rev_stats(A, prices)
    mB, vB, revB = rev_stats(B, prices)
    if metric == 'revenue':
        r, lo, hi = rel_ci(mA, vA, nA, mB, vB, nB)
        out['metric'] = {'name': 'revenue per person', 'A': mA, 'B': mB}
    elif metric == 'trial_starts':
        r, lo, hi = prop_rel(A['trials'], nA, B['trials'], nB)
        out['metric'] = {'name': 'trial starts per person', 'A': A['trials'] / nA, 'B': B['trials'] / nB}
    else:
        r, lo, hi = prop_rel(payA, nA, payB, nB)
        out['metric'] = {'name': 'paid conversion', 'A': payA / nA, 'B': payB / nB}
    out['metric'].update(lift=r, lo=lo, hi=hi, bar=bar)

    # 4. where the difference came from (revenue = how many paid x what they paid)
    cA, cB = payA / nA, payB / nB
    aA, aB = revA / payA, revB / payB
    lr = math.log(mB / mA) if mA and mB else 0
    lc, la = math.log(cB / cA), math.log(aB / aA)
    mixA = {p: A['payers'].get(p, 0) / payA for p in prices}
    mixB = {p: B['payers'].get(p, 0) / payB for p in prices}
    out['decomposition'] = {'conversion_change': cB / cA - 1, 'revenue_per_payer_change': aB / aA - 1,
                            'share_from_conversion': lc / lr if lr else None, 'share_from_plan_mix': la / lr if lr else None,
                            'plan_mix_A': mixA, 'plan_mix_B': mixB}

    # 5. guardrails
    if 'refunds' in A and 'refunds' in B:
        z = z2(A['refunds'], payA, B['refunds'], payB)
        bad = z > 2.58
        out['checks'].append({'name': 'refunds held', 'ok': not bad, 'value': f"{A['refunds'] / payA * 100:.1f}% -> {B['refunds'] / payB * 100:.1f}%", 'z': z})
    if 'value_per_payer' not in d and len(prices) > 1:
        out['notes'].append('Revenue counts each payer\'s first payment. A weekly payer usually pays again, so a shift toward weekly plans looks worse here than it is. Give value_per_payer to correct it.')
    if 'weekly_lift' not in d:
        out['notes'].append('No week-by-week numbers: whether the lift faded was not checked.')
    if 'weekly_lift' in d:
        w = d['weekly_lift']
        fading = len(w) >= 3 and all(w[i + 1] < w[i] for i in range(len(w) - 1))
        out['checks'].append({'name': 'lift held week to week', 'ok': not fading, 'value': ' / '.join(f'{x:+.0%}' for x in w)})

    # verdict
    guard_bad = any(not c['ok'] for c in out['checks'] if c['name'] in ('refunds held', 'lift held week to week'))
    if not srm_ok:
        v = 'broken'
    elif not timing_ok and metric != 'trial_starts':
        v = 'too_early'
    elif goal == 'not_worse':
        v = ('not_worse_with_cost' if guard_bad else 'not_worse') if lo > -margin else 'maybe_worse'
    elif lo > 0:
        v = 'win_with_cost' if guard_bad else 'win'
    elif hi < 0:
        v = 'loss'
    else:
        v = 'cant_tell'
    out['verdict'] = v
    out['plan_on'] = lo if v.startswith('win') else None
    out['goal'] = {'goal': goal, 'margin': margin if goal == 'not_worse' else None}

    sc, sm = out['decomposition']['share_from_conversion'], out['decomposition']['share_from_plan_mix']
    if sc is not None and (sc < 0 or sm < 0):
        out['decomposition']['plain'] = 'Conversion and revenue per payer moved in opposite directions; the net change is their difference.'
    elif sc is not None:
        out['decomposition']['plain'] = f'About {sc * 100:.0f}% of the change from how many paid, {sm * 100:.0f}% from which plans they chose.'
    if args.json:
        print(json.dumps(out, indent=2, default=float))
        return
    m = out['metric']
    pct = lambda x: f'{x * 100:+.1f}%'
    print(f"Verdict: {v}")
    if v in ('broken', 'too_early'):
        print('Result: not shown. Fix or wait first; reading these numbers would anchor on a result that can\'t be trusted.')
    else:
        tail = f"margin for 'not worse' {-margin * 100:.0f}%" if goal == 'not_worse' else f"plan's smallest change {bar * 100:.0f}%"
        print(f"{m['name']}: A {m['A']:.4g}, B {m['B']:.4g}; B vs A {pct(m['lift'])} (95% range {pct(m['lo'])} to {pct(m['hi'])}); {tail}")
    for c in out['checks']:
        print(f"  [{'ok' if c['ok'] else '!!'}] {c['name']}: {c['value']}")
    dc = out['decomposition']
    if v not in ('broken', 'too_early'):
        print(f"Where it came from: paid conversion {pct(dc['conversion_change'])}, revenue per payer {pct(dc['revenue_per_payer_change'])}. {dc.get('plain', '')}")
    print('  plan mix A: ' + ', '.join(f'{p} {s * 100:.0f}%' for p, s in dc['plan_mix_A'].items()) + ' | B: ' + ', '.join(f'{p} {s * 100:.0f}%' for p, s in dc['plan_mix_B'].items()))
    for n_ in out['notes']:
        print('Note:', n_)


if __name__ == '__main__':
    main()
