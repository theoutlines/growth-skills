#!/usr/bin/env python3
"""The evidence base: one record per published test, the single source of truth.

  python3 scripts/evidence.py import   # one-time: read the skills' evidence.md tables into evidence/tests.csv
  python3 scripts/evidence.py build    # rewrite the test tables in each skill's evidence.md from the base
  python3 scripts/evidence.py check    # fail if a skill, the mechanics files or the planner cite an ID the base doesn't have,
                                       # or if a skill's table drifted from the base

Fields the skills print are rendered back exactly; the base adds fields the tables don't have
(tier, outcome, bundled, mechanics, checked) so tools can filter on them.
"""
import csv, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SK = os.path.join(ROOT, 'plugins/growth-skills/skills')
BASE = os.path.join(ROOT, 'evidence/tests.csv')

# library -> (skill folder, id pattern, ranges-style prefix)
LIBS = {
    'onboarding': ('onboarding-teardown', r'(\d+|E\d+)'),
    'upsell': ('upsell-teardown', r'(U\d+)'),
    'cancel': ('cancel-flow-teardown', r'(C\d+)'),
    'web2app': ('web2app-teardown', r'(W\d+)'),
    'retention': ('retention-teardown', r'(R\d+)'),
    'flow': ('flow-teardown', r'(\d+|E\d+)'),   # its own aggregates (E3–E5); its copies of onboarding rows are checked against 'onboarding'
}
SHARED = {'flow': 'onboarding'}   # library whose rows may be copies of another library's records (same ID, same text)
# column name in a table -> field in the base
COLS = {
    '#': 'id', 'ID': 'id', 'App': 'app', 'App / org': 'app', 'App / platform': 'app', 'Platform / panel': 'app', 'App/company': 'app',
    'Item': 'change', 'Figure': 'result', 'Source': 'sources', 'Strength': 'tier_text', 'What': 'change',
    'Category': 'category', 'Bucket': 'bucket', 'AI app?': 'ai', 'AI tag': 'ai', 'AI?': 'ai', 'Surface': 'surface',
    'What changed': 'change', 'Change': 'change', 'Metric': 'metric', 'Result': 'result', 'Date': 'date',
    'Source URL': 'sources', 'URL': 'sources', 'Evidence': 'tier_text', 'Tier': 'tier_text',
}
FIELDS = ['id', 'library', 'kind', 'section', 'columns', 'app', 'category', 'bucket', 'ai', 'surface', 'change', 'metric', 'result',
          'date', 'sources', 'tier_text', 'tier', 'outcome', 'bundled', 'same_as', 'mechanics', 'checked']


def cells(line):
    return [c.strip() for c in line.strip()[1:-1].split(' | ')] if line.strip().endswith('|') else None


def tables(path, idre):
    """Yield (section, header, row cells, line index) for every table row whose first cell is a record ID."""
    sec, head = '', None
    lines = open(path).read().split('\n')
    for i, line in enumerate(lines):
        if line.startswith('## '):
            sec = line[3:].strip()
        if not line.startswith('| '):
            head = None if not line.startswith('|') else head
            continue
        c = cells(line)
        if c is None:
            continue
        if c[0] in ('#', 'ID'):
            head = c
            continue
        if head and re.fullmatch(idre, c[0]) and len(c) == len(head):
            yield sec, head, c, i


def tier_of(t):
    t = t.lower()
    for k in ('strong', 'directional', 'anecdotal', 'observed'):
        if t.startswith(k):
            return k
    if 'aggregat' in t or 'prior' in t:
        return 'aggregate'
    for k in ('strong', 'directional', 'anecdotal', 'observed'):
        if k in t:
            return k
    return ''


def load():
    with open(BASE, newline='') as f:
        return list(csv.DictReader(f))


def save(rows):
    with open(BASE, 'w', newline='') as f:
        w = csv.DictWriter(f, FIELDS, lineterminator='\n')
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, '') for k in FIELDS})


def cmd_import():
    old = {(r['library'], r['id']): r for r in load()} if os.path.exists(BASE) else {}
    rows = []
    for lib, (folder, idre) in LIBS.items():
        for sec, head, c, _ in tables(os.path.join(SK, folder, 'references/evidence.md'), idre):
            if lib in SHARED and any(x['library'] == SHARED[lib] and x['id'] == c[0] for x in rows):
                continue
            r = {'library': lib, 'section': sec, 'columns': ' | '.join(head)}
            for h, v in zip(head, c):
                r[COLS[h]] = v
            r['kind'] = 'aggregate' if re.fullmatch(r'E\d+', r['id']) else 'test'
            r['tier'] = tier_of(r.get('tier_text', ''))
            keep = old.get((lib, r['id']), {})
            for k in ('outcome', 'bundled', 'same_as', 'mechanics', 'checked'):
                r[k] = keep.get(k, '')
            rows.append(r)
    save(rows)
    print(f'{len(rows)} records')


def row_text(r):
    head = r['columns'].split(' | ')
    return '| ' + ' | '.join(r.get(COLS[h], '') for h in head) + ' |'


def last_row(lines, section, columns):
    """Index of the last row of the first table under `## section` whose header is `columns`."""
    sec, head, last = '', None, None
    for i, line in enumerate(lines):
        if line.startswith('## '):
            if last is not None:
                return last
            sec = line[3:].strip()
        c = cells(line) if line.startswith('|') else None
        if c and c[0] in ('#', 'ID'):
            head = ' | '.join(c)
            continue
        if sec == section and head == columns and c and not set(line) <= set('|- '):
            last = i
        elif last is not None and not line.startswith('|'):
            return last
    return last


def cmd_build(write=True):
    base = load()
    by = {(r['library'], r['id']): r for r in base}
    drift = []
    for lib, (folder, idre) in LIBS.items():
        path = os.path.join(SK, folder, 'references/evidence.md')
        lines = open(path).read().split('\n')
        seen = set()
        for sec, head, c, i in list(tables(path, idre)):
            r = by.get((lib, c[0])) or by.get((SHARED.get(lib), c[0]))
            if r and r['library'] != lib:
                r = dict(r, columns=' | '.join(head))   # a copy: same record, this table's columns
            if not r:
                drift.append(f'{folder}: {c[0]} is in evidence.md but not in the base')
                continue
            seen.add(c[0])
            new = row_text(r)
            if lines[i] != new:
                drift.append(f'{folder}: {c[0]} differs from the base')
                lines[i] = new
        for r in base:
            if r['library'] == lib and r['id'] not in seen:
                at = last_row(lines, r['section'], r['columns'])
                if at is None:
                    drift.append(f'{folder}: base record {r["id"]} has no table for section "{r["section"]}" with these columns')
                    continue
                drift.append(f'{folder}: {r["id"]} added to "{r["section"]}"')
                lines.insert(at + 1, row_text(r))
        if write:
            open(path, 'w').write('\n'.join(lines))
    return drift


CITE = {   # files that cite records, and how an ID looks in them
    'onboarding': [('onboarding-teardown/references/ranges.md', r'#(\d+)\b|\b(E\d+)\b'),
                   ('flow-teardown/references/ranges.md', r'#(\d+)\b|\b(E\d+)\b'),
                   ('variant-check/references/onboarding-mechanics.md', r'#(\d+)\b'),
                   ('variant-check/references/mechanics.md', r'#(\d+)\b')],
    'upsell': [('upsell-teardown/references/ranges.md', r'\b(U\d+)\b')],
    'cancel': [('cancel-flow-teardown/references/ranges.md', r'\b(C\d+)\b')],
    'web2app': [('web2app-teardown/references/ranges.md', r'\b(W\d+)\b')],
    'retention': [('retention-teardown/references/ranges.md', r'\b(R\d+)\b')],
}
PLANNER = os.path.join(ROOT, 'evidence/planner-ideas.csv')


def cmd_check():
    base = load()
    ids = {(r['library'], r['id']) for r in base}
    bad = cmd_build(write=False)
    for r in base:
        if r['kind'] == 'test' and r['tier'] not in ('strong', 'directional', 'anecdotal', 'observed'):
            bad.append(f'{r["library"]} {r["id"]}: tier not recognised ({r["tier_text"][:40]})')
        if r['outcome'] not in ('win', 'loss', 'null', 'mixed', 'none', ''):
            bad.append(f'{r["library"]} {r["id"]}: outcome must be win, loss, null, mixed or none')
        if r['kind'] == 'test' and not r['outcome']:
            bad.append(f'{r["library"]} {r["id"]}: outcome missing (win, loss, null, mixed, none)')
    for lib, files in CITE.items():
        for rel, rx in files:
            text = open(os.path.join(SK, rel)).read()
            for m in re.finditer(rx, text):
                i = next(g for g in m.groups() if g)
                if (lib, i) not in ids and ('flow', i) not in ids:
                    bad.append(f'{rel}: cites {i}, not in the base')
    if os.path.exists(PLANNER):
        for p in csv.DictReader(open(PLANNER)):
            for ref in filter(None, p['records'].split()):
                lib, i = ref.split(':')
                if (lib, i) not in ids and lib != 'adapty':
                    bad.append(f'planner idea {p["area"]}/{p["idea"]}: cites {ref}, not in the base')
                if p['lost'] == 'yes' and lib != 'adapty':
                    r = next((x for x in base if (x['library'], x['id']) == (lib, i)), None)
                    if r and r['outcome'] not in ('loss', 'mixed'):
                        bad.append(f'planner idea {p["idea"]} is marked lost but {ref} is not a loss')
    lib_md = open(os.path.join(SK, 'paywall-ab-test-assistant/references/evidence-library.md')).read()
    heads = [h.strip('# ').strip() for h in re.findall(r'^#{2,3} .+$', lib_md, re.M)]
    if os.path.exists(PLANNER):
        for p in csv.DictReader(open(PLANNER)):
            for ref in p['records'].split():
                if ref.startswith('adapty:') and not any(h.startswith(ref[7:].replace('_', ' ')) for h in heads):
                    bad.append(f'planner idea {p["idea"]}: no Adapty library section starting "{ref[7:]}"')
        js_path = os.path.join(os.path.dirname(ROOT), 'growth-test-planner/js/data.js')   # the planner, when cloned next to this repo
        if os.path.exists(js_path):
            js = open(js_path).read()
            parts = {'paywall': js[js.index('paywall: ['):js.index('onboarding: [')], 'onboarding': js[js.index('onboarding: ['):js.index('export const DECIDE')]}
            mapped = {(p['area'], p['idea']) for p in csv.DictReader(open(PLANNER))}
            for area, part in parts.items():
                for i in re.findall(r"id: '(\w+)'", part):
                    if (area, i) not in mapped:
                        bad.append(f'planner idea {area}/{i} has no row in evidence/planner-ideas.csv')
                for m in re.finditer(r"id: '(\w+)', lost: true", part):
                    if (area, m.group(1)) in mapped and next(p for p in csv.DictReader(open(PLANNER)) if (p['area'], p['idea']) == (area, m.group(1)))['lost'] != 'yes':
                        bad.append(f'planner idea {m.group(1)} is lost in data.js but not in planner-ideas.csv')
    for b in bad:
        print('✗', b)
    print(f'{len(base)} records, {len(bad)} problems')
    return 1 if bad else 0


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'check'
    if cmd == 'import':
        cmd_import()
    elif cmd == 'build':
        d = cmd_build(True)
        print('\n'.join(d) or 'evidence.md tables match the base')
    else:
        sys.exit(cmd_check())
