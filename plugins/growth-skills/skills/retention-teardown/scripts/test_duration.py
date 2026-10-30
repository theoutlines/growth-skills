#!/usr/bin/env python3
"""How long a screen A/B test needs, counted in people entering the test.

In the retention teardown, tests are randomised per new payer or trial
starter: pass those per day as --installs (the name is kept for the shared
script). The decision date adds
the trial length plus billing lag when the test is judged on paid conversion.

Math (two-sided z-test on a conversion rate, relative MDE):
  n per variant = 2 * (z_{1-a/2} + z_{1-b})^2 * CV^2 / MDE^2,  CV^2 = (1 - p) / p
  Bonferroni for k > 2 variants: alpha / (k - 1)
  collect days  = max(min_days, ceil(n / (installs_per_day / k)))
  decision days = collect + (trial_days + billing_lag if metric == paid else 0)

Usage:
  python3 test_duration.py --installs 2000 --baseline 0.08 --mde 0.10
  python3 test_duration.py --installs 2000 --baseline 0.08 --weeks 4   # smallest lift a 4-week test sees
  add --metric paid --trial-days 7 for tests judged on paid conversion
  add --json for machine-readable output

Simplifications: no sequential testing, no variance reduction, equal split.
"""

import argparse
import json
import math
from statistics import NormalDist

Z = NormalDist().inv_cdf


def n_per_variant(p, mde, k=2, alpha=0.05, power=0.8):
    a = alpha / (k - 1) if k > 2 else alpha
    z = Z(1 - a / 2) + Z(power)
    cv2 = (1 - p) / p
    return math.ceil(2 * z * z * cv2 / (mde * mde))


def plan(installs, p, mde, k=2, metric="trial", trial_days=7, billing_lag=3, min_days=14):
    n = n_per_variant(p, mde, k)
    collect = max(min_days, math.ceil(n / (installs / k)))
    wait = trial_days + billing_lag if metric == "paid" else 0
    return {"n_per_variant": n, "collect_days": collect, "wait_days": wait,
            "decision_days": collect + wait, "decision_weeks": round((collect + wait) / 7, 1)}


def detectable(installs, p, weeks, k=2):
    n = installs / k * weeks * 7
    a = 0.05 / (k - 1) if k > 2 else 0.05
    z = Z(1 - a / 2) + Z(0.8)
    return math.sqrt(2 * z * z * (1 - p) / p / n)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--installs", type=float, required=True, help="installs (or onboarding starts) per day entering the test")
    ap.add_argument("--baseline", type=float, required=True, help="current rate per install of the decision metric, e.g. 0.08")
    ap.add_argument("--mde", type=float, help="smallest relative change worth detecting, e.g. 0.10 for 10%%")
    ap.add_argument("--weeks", type=float, help="instead of --mde: test length in weeks, returns the smallest detectable change")
    ap.add_argument("--variants", type=int, default=2)
    ap.add_argument("--metric", choices=["trial", "paid"], default="trial")
    ap.add_argument("--trial-days", type=int, default=7)
    ap.add_argument("--billing-lag", type=int, default=3)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    if not 0 < a.baseline < 1:
        ap.error("--baseline must be a rate between 0 and 1")
    if a.weeks:
        r = {"detectable_change": round(detectable(a.installs, a.baseline, a.weeks, a.variants), 4)}
        txt = f"A {a.weeks:g}-week test sees changes of {r['detectable_change']*100:.1f}% or more (relative)."
    elif a.mde:
        r = plan(a.installs, a.baseline, a.mde, a.variants, a.metric, a.trial_days, a.billing_lag)
        txt = (f"{r['n_per_variant']:,} installs per variant; collect {r['collect_days']} days"
               + (f" + {r['wait_days']} days for trials to bill" if r["wait_days"] else "")
               + f" = decision in {r['decision_days']} days (~{r['decision_weeks']} weeks).")
    else:
        ap.error("give --mde or --weeks")
    print(json.dumps(r) if a.json else txt)


if __name__ == "__main__":
    main()
