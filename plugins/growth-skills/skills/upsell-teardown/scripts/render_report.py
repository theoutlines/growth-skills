#!/usr/bin/env python3
"""Render a teardown report card as a PNG (onboarding, flow and cancel-flow teardowns).

Header: either one score (score.dimensions summed) or, when "parts" is given,
three part scores with the weakest link and per-part "held_back".
Flow line extras: "value_at" (value moment), "unseen" (screens not captured),
"extra" (limit screens L1, L2), "paywall_at". Labels can be renamed with
"marker_label" (default "paywall"), "value_label" ("value moment") and
"extra_label" ("limit"); the cancel-flow teardown uses "save", "exit", "after",
the upsell teardown "upsell", "trigger", "payers". An explicit "total" overrides
the sum of the dimensions (scaled scores).

The card, top to bottom:
  header     - score out of 100, grade, the read line (and "58 -> 71" on re-runs)
  flow line  - one dot per screen, the first paywall marked, numbered rings on
               screens that a test idea touches
  strip      - thumbnails of the key screens with numbered pins on the spot
               each test idea changes (filled pin = change, ring pin = add)
  bars       - the five rubric dimensions
  tests      - ranked test ideas: priority, pattern, change, evidence, duration
  footer     - the evidence disclaimer

Usage:
  python3 render_report.py --data teardown.json --out report.png

Screens without an image (or whose file can't be opened) are skipped in the
strip; the flow line still shows them. With no images at all the strip is
omitted. Requires Pillow (pip install pillow).

teardown.json shape (see example.json next to this script):
{
  "subtitle": "Health & Fitness - diet - AI tag",
  "verdict": "Solid quiz funnel; the paywall ignores the plan it just built.",
  "previous_total": null,
  "held_back": 0,
  "score": {"dimensions": [{"key": "value", "label": "Value", "score": 18, "max": 25}, ...]},
  "flow": {"screens": 17, "paywall_at": 14},
  "duration_note": "Assumes 2,000 installs a day ...",
  "screens": [{"n": 11, "image": "shots/11.png", "label": "Plan reveal"}, ...],
  "items": [
    {"n": 1, "priority": "High", "pattern": "Trial timeline",
     "test": "Put a dated reminder timeline under the price.",
     "evidence": "Blinkist +23% trial sign-ups (#1, strong)",
     "duration": "~4 weeks",
     "pin": {"screen": 14, "x": 0.5, "y": 0.62, "type": "change"}}
  ]
}
Freemium flows: add "extra": ["L1", "L2"] to "flow" for limit screens after
onboarding, and pin them with "screen": "L1". Screen ids may be strings; a
custom "order" list overrides 1..screens.
Image paths are relative to the JSON file unless absolute.
pin.x / pin.y are fractions (0-1) of that screen's width / height.
"""

import argparse
import json
import os
import sys

try:
    from PIL import Image, ImageDraw, ImageFont, ImageOps
except ImportError:  # pragma: no cover
    sys.exit("Pillow is required: pip install pillow")

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.normpath(os.path.join(HERE, "..", "assets", "fonts"))

SURFACE = (252, 252, 251)
PANEL = (243, 242, 238)
INK = (11, 11, 11)
INK_2 = (82, 81, 78)
INK_3 = (128, 127, 122)
RULE = (228, 227, 222)
ACCENT = (40, 96, 220)

PRIORITY = {
    "fix first": {"fill": (208, 59, 59), "text": (255, 255, 255), "label": "Fix first"},
    "high": {"fill": (236, 131, 90), "text": (255, 255, 255), "label": "High"},
    "medium": {"fill": (250, 178, 25), "text": (11, 11, 11), "label": "Medium"},
    "low": {"fill": (138, 137, 132), "text": (255, 255, 255), "label": "Low"},
}
GRADES = [(85, "Strong", (12, 163, 12)), (70, "Solid", (42, 120, 214)),
          (50, "Leaking", (236, 131, 90)), (0, "Needs work", (208, 59, 59))]

DISCLAIMER = ("Published results are one company's outcome in its own setting, not the change your "
              "upsells will get. Annual switches, family upsells and frequency caps have no public test, "
              "and compliance notes are flags, not legal advice. Run your own A/B test before shipping.")
DEFAULT_KICKER = "UPSELL TEARDOWN"
GLYPHS = {"≈": "~", "✓": "v", "✗": "x", "→": "->", "−": "-"}

SCALE = 2
W = 1200
PAD = 48
THUMB_H = 300


def s(v):
    return int(round(v * SCALE))


_FILES = {"regular": "Inter-Regular.ttf", "semibold": "Inter-SemiBold.ttf", "bold": "Inter-Bold.ttf"}
_FALLBACK = {
    "regular": ["DejaVuSans.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
                "/System/Library/Fonts/Supplemental/Arial.ttf", "C:/Windows/Fonts/arial.ttf"],
    "bold": ["DejaVuSans-Bold.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
             "/System/Library/Fonts/Supplemental/Arial Bold.ttf", "C:/Windows/Fonts/arialbd.ttf"],
}
_cache = {}


def font(weight, size):
    key = (weight, size)
    if key in _cache:
        return _cache[key]
    paths = [os.path.join(FONT_DIR, _FILES[weight])]
    paths += _FALLBACK["regular" if weight == "regular" else "bold"]
    f = None
    for p in paths:
        try:
            f = ImageFont.truetype(p, s(size))
            break
        except (OSError, IOError):
            continue
    if f is None:
        try:
            f = ImageFont.load_default(size=s(size))
        except TypeError:
            f = ImageFont.load_default()
    _cache[key] = f
    return f


def clean(txt):
    t = str(txt or "")
    for k, v in GLYPHS.items():
        if k != "→" and k != "−":
            t = t.replace(k, v)
    return t


def wrap(draw, txt, fnt, width, max_lines=None):
    words, lines, cur = clean(txt).split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= s(width):
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    if max_lines and len(lines) > max_lines:
        lines = lines[:max_lines]
        last = lines[-1]
        while last and draw.textlength(last + "…", font=fnt) > s(width):
            last = last[:-1]
        lines[-1] = last.rstrip() + "…"
    return lines


def prio(p):
    return PRIORITY.get(str(p or "").strip().lower(), PRIORITY["low"])


def grade(total):
    for lo, label, color in GRADES:
        if total >= lo:
            return label, color
    return GRADES[-1][1:]


def pin(draw, cx, cy, n, p, kind="change", r=13):
    c = prio(p)
    box = [cx - s(r), cy - s(r), cx + s(r), cy + s(r)]
    if kind == "add":
        draw.ellipse(box, fill=(255, 255, 255), outline=c["fill"], width=s(3))
        color = c["fill"]
    else:
        draw.ellipse([b + (s(1) if i < 2 else -s(1)) for i, b in enumerate(box)],
                     fill=(255, 255, 255))
        draw.ellipse([box[0] + s(2), box[1] + s(2), box[2] - s(2), box[3] - s(2)], fill=c["fill"])
        color = c["text"]
    f = font("bold", 13)
    t = str(n)
    draw.text((cx - draw.textlength(t, font=f) / 2, cy - s(8.5)), t, font=f, fill=color)


def load(path, base):
    if not path:
        return None
    if not os.path.isabs(path):
        path = os.path.join(base, path)
    try:
        im = Image.open(path)
        im = ImageOps.exif_transpose(im).convert("RGB")
        return im
    except Exception:
        return None


def rounded(im, radius):
    mask = Image.new("L", im.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, im.size[0] - 1, im.size[1] - 1], radius=radius, fill=255)
    out = Image.new("RGBA", im.size)
    out.paste(im, (0, 0), mask)
    return out


def render(data, base, out):
    canvas = Image.new("RGB", (s(W), s(6000)), SURFACE)
    d = ImageDraw.Draw(canvas)
    x0, inner = s(PAD), W - 2 * PAD
    y = s(PAD)

    dims = data.get("score", {}).get("dimensions", [])
    total = sum(int(x.get("score", 0)) for x in dims)
    if data.get("total") is not None:  # e.g. a scaled payers-only score
        total = int(data["total"])
    g_label, g_color = grade(total)

    # ---- header
    d.text((x0, y), data.get("kicker") or DEFAULT_KICKER, font=font("bold", 13), fill=ACCENT)
    y_head = y
    y += s(24)
    sub = data.get("subtitle") or ""
    if sub:
        d.text((x0, y), sub, font=font("semibold", 22), fill=INK)
        y += s(34)
    for line in wrap(d, data.get("verdict"), font("regular", 17), inner - (440 if data.get("parts") else 300), 3):
        d.text((x0, y), line, font=font("regular", 17), fill=INK_2)
        y += s(25)
    # score block, right aligned
    cx1 = s(W - PAD)
    parts = data.get("parts") or []
    extra_y = y_head
    if parts:
        def seen_loss(p):
            return 100 - int(p.get("score", 0)) - int(p.get("held_back") or 0)
        weakest = max(parts, key=seen_loss)
        for p in parts:
            val = str(p.get("score", 0))
            gl, gc = grade(int(p.get("score", 0)))
            if int(p.get("held_back") or 0) >= 25:
                gl, gc = "Partial", INK_3
            fb = font("bold", 34)
            fl = font("semibold", 15)
            lab = p.get("label", "") + (" (lite)" if p.get("lite") else "")
            hb = int(p.get("held_back") or 0)
            # chip
            chip_f = font("bold", 12)
            cw = d.textlength(gl, font=chip_f) + s(18)
            d.rounded_rectangle([cx1 - cw, extra_y + s(10), cx1, extra_y + s(32)], radius=s(11), fill=gc)
            d.text((cx1 - cw + s(9), extra_y + s(13)), gl, font=chip_f, fill=(255, 255, 255))
            vx = cx1 - cw - s(12) - d.textlength(val, font=fb)
            d.text((vx, extra_y), val, font=fb, fill=INK)
            lx = vx - s(12) - d.textlength(lab, font=fl)
            d.text((lx, extra_y + s(12)), lab, font=fl, fill=INK if p is weakest else INK_2)
            if p is weakest:
                t = "weakest link"
                d.text((lx - s(10) - d.textlength(t, font=font("regular", 12)), extra_y + s(14)), t, font=font("regular", 12), fill=(208, 59, 59))
            if hb >= 5:
                t = f"{hb} held back"
                d.text((lx - s(10) - d.textlength(t, font=font("regular", 12)) - (d.textlength("weakest link", font=font("regular", 12)) + s(10) if p is weakest else 0), extra_y + s(14)), t, font=font("regular", 12), fill=INK_3)
            extra_y += s(46)
        prev = data.get("previous_parts")
        if prev:
            t = "was " + " · ".join(f"{k} {v}" for k, v in prev.items())
            d.text((cx1 - d.textlength(t, font=font("regular", 13)), extra_y), t, font=font("regular", 13), fill=INK_2)
            extra_y += s(20)
    else:
        big = font("bold", 64)
        tot = str(total)
        sx = cx1 - d.textlength(tot, font=big) - s(4) - d.textlength("/100", font=font("semibold", 22))
        d.text((sx, y_head - s(6)), tot, font=big, fill=INK)
        d.text((sx + d.textlength(tot, font=big) + s(4), y_head + s(40)), "/100", font=font("semibold", 22), fill=INK_3)
        chip_f = font("bold", 14)
        cw = d.textlength(g_label, font=chip_f) + s(24)
        cy0 = y_head + s(84)
        d.rounded_rectangle([cx1 - cw, cy0, cx1, cy0 + s(28)], radius=s(14), fill=g_color)
        d.text((cx1 - cw + s(12), cy0 + s(5)), g_label, font=chip_f, fill=(255, 255, 255))
        extra_y = cy0 + s(38)
        prev = data.get("previous_total")
        if prev is not None:
            t = f"was {prev}  →  {total}"
            d.text((cx1 - d.textlength(t, font=font("semibold", 14)), extra_y), t, font=font("semibold", 14), fill=INK_2)
            extra_y += s(22)
    held = int(data.get("held_back") or 0)
    if held >= 10:
        t = f"{held} pts held back by missing screens"
        d.text((cx1 - d.textlength(t, font=font("regular", 13)), extra_y), t, font=font("regular", 13), fill=INK_3)
        extra_y += s(20)
    y = max(y, extra_y) + s(22)

    items = data.get("items") or []
    touched = {}
    for it in items:
        pn = (it.get("pin") or {}).get("screen")
        if pn not in (None, ""):
            touched.setdefault(str(pn), []).append(it)

    # ---- flow line
    flow = data.get("flow") or {}
    order = [str(x) for x in (flow.get("order") or range(1, int(flow.get("screens") or 0) + 1))]
    order += [str(x) for x in (flow.get("extra") or [])]
    n_screens = len(order)
    paywall_at = flow.get("paywall_at")
    paywall_at = None if paywall_at in (None, "") else str(paywall_at)
    if n_screens:
        d.line([x0, y, s(W - PAD), y], fill=RULE, width=s(1))
        y += s(22)
        d.text((x0, y), "Flow", font=font("semibold", 14), fill=INK_3)
        lx0 = x0 + s(70)
        extra_ids = [str(x) for x in (flow.get("extra") or [])]
        main_ids = [o for o in order if o not in extra_ids]
        group_w = s(46 * len(extra_ids) + 40) if extra_ids else 0
        lx1 = s(W - PAD - 10) - group_w
        cy = y + s(10)
        step = (lx1 - lx0) / max(1, len(main_ids) - 1)
        pos = {sid: lx0 + step * i for i, sid in enumerate(main_ids)}
        gx = lx1 + s(40)
        for j, sid in enumerate(extra_ids):
            pos[sid] = gx + s(46) * j + s(10)
        d.line([lx0, cy, lx1, cy], fill=RULE, width=s(2))
        if extra_ids:
            d.line([lx1 + s(8), cy, gx - s(4), cy], fill=RULE, width=s(2))
            # dashed gap = time passes in the product
            for k in range(3):
                xx = lx1 + s(14) + s(7) * k
                d.ellipse([xx - s(1.5), cy - s(1.5), xx + s(1.5), cy + s(1.5)], fill=SURFACE)
        unseen = set(str(x) for x in (flow.get("unseen") or []))
        value_at = flow.get("value_at")
        value_at = None if value_at in (None, "") else str(value_at)
        for sid in order:
            cx = pos[sid]
            special = sid == paywall_at or sid in extra_ids
            if sid == value_at:
                d.polygon([(cx, cy - s(15)), (cx + s(15), cy), (cx, cy + s(15)), (cx - s(15), cy)], outline=(12, 163, 12), width=s(3))
            if special:
                d.rounded_rectangle([cx - s(15), cy - s(15), cx + s(15), cy + s(15)], radius=s(6),
                                    outline=ACCENT, width=s(3))
            if sid in touched:
                its = sorted(touched[sid], key=lambda it: it.get("n", 99))
                pin(d, cx, cy, its[0].get("n"), its[0].get("priority"), "change", r=11)
                if len(its) > 1:
                    t = f"+{len(its) - 1}"
                    d.text((cx + s(9), cy - s(26)), t, font=font("bold", 11), fill=INK_2)
                if sid == value_at:
                    d.polygon([(cx, cy - s(19)), (cx + s(19), cy), (cx, cy + s(19)), (cx - s(19), cy)], outline=(12, 163, 12), width=s(3))
            elif sid in unseen:
                d.ellipse([cx - s(4), cy - s(4), cx + s(4), cy + s(4)], outline=INK_3, width=s(1), fill=SURFACE)
            elif special:
                d.rounded_rectangle([cx - s(7), cy - s(7), cx + s(7), cy + s(7)], radius=s(3), fill=ACCENT)
            else:
                d.ellipse([cx - s(4), cy - s(4), cx + s(4), cy + s(4)], fill=INK_3)
        y = cy + s(22)
        f12, fs = font("regular", 12), font("semibold", 12)
        d.text((lx0 - s(3), y), main_ids[0], font=f12, fill=INK_3)
        lab_last = main_ids[-1]
        pw_txt = f"{flow.get('marker_label') or 'paywall'} · {paywall_at}" if paywall_at in pos else None
        pwx = None
        if pw_txt:
            pwx = min(max(pos[paywall_at] - d.textlength(pw_txt, font=fs) / 2, lx0), lx1 - d.textlength(pw_txt, font=fs))
            d.text((pwx, y), pw_txt, font=fs, fill=ACCENT)
        lw = d.textlength(lab_last, font=f12)
        if pwx is None or pwx + d.textlength(pw_txt, font=fs) < lx1 - lw - s(8):
            d.text((lx1 - lw, y), lab_last, font=f12, fill=INK_3)
        lgx = lx0 + s(40)
        if value_at in pos:
            c0 = (lgx + s(6), y + s(8))
            d.polygon([(c0[0], c0[1] - s(6)), (c0[0] + s(6), c0[1]), (c0[0], c0[1] + s(6)), (c0[0] - s(6), c0[1])], outline=(12, 163, 12), width=s(2))
            vlab = flow.get("value_label") or "value moment"
            d.text((lgx + s(18), y), vlab, font=f12, fill=INK_3)
            lgx += s(18) + d.textlength(vlab, font=f12) + s(20)
        if unseen:
            d.ellipse([lgx + s(2), y + s(4), lgx + s(10), y + s(12)], outline=INK_3, width=s(1))
            d.text((lgx + s(18), y), "not captured", font=f12, fill=INK_3)
        if extra_ids:
            t = (flow.get("extra_label") or "limit") + " · " + (extra_ids[0] if len(extra_ids) == 1 else f"{extra_ids[0]}–{extra_ids[-1]}")
            cxm = (pos[extra_ids[0]] + pos[extra_ids[-1]]) / 2
            d.text((min(cxm - d.textlength(t, font=fs) / 2, s(W - PAD) - d.textlength(t, font=fs)), y), t, font=fs, fill=ACCENT)
        y += s(30)

    # ---- strip
    shots = []
    for sc in data.get("screens") or []:
        im = load(sc.get("image"), base)
        if im is not None:
            shots.append((sc, im))
    if shots:
        gap = 14
        th = THUMB_H
        widths = [int(th * im.size[0] / im.size[1]) for _, im in shots]
        rows, cur, cw_sum = [], [], 0
        for (sc, im), tw in zip(shots, widths):
            need = tw + (gap if cur else 0)
            if cur and cw_sum + need > inner:
                rows.append(cur)
                cur, cw_sum = [], 0
                need = tw
            cur.append((sc, im, tw))
            cw_sum += need
        if cur:
            rows.append(cur)
        for row in rows:
            x = x0
            for sc, im, tw in row:
                thumb = im.resize((s(tw), s(th)), Image.LANCZOS)
                canvas.paste(rounded(thumb, s(14)), (x, y), rounded(thumb, s(14)))
                is_pw = str(sc.get("n")) == paywall_at or str(sc.get("n")) in set(str(x) for x in (flow.get("extra") or []))
                d.rounded_rectangle([x, y, x + s(tw), y + s(th)], radius=s(14),
                                    outline=ACCENT if is_pw else RULE, width=s(3 if is_pw else 1))
                for it in touched.get(str(sc.get("n")), []):
                    p = it.get("pin") or {}
                    px = x + s(tw) * float(p.get("x", 0.5))
                    py = y + s(th) * float(p.get("y", 0.5))
                    pin(d, px, py, it.get("n"), it.get("priority"), p.get("type", "change"))
                lab = f"{sc.get('n')} · {sc.get('label') or ''}".strip(" ·")
                for line in wrap(d, lab, font("regular", 12), tw, 1):
                    d.text((x, y + s(th + 8)), line, font=font("regular", 12), fill=ACCENT if is_pw else INK_2)
                x += s(tw + gap)
            y += s(th + 34)
        y += s(6)

    # ---- bars
    d.line([x0, y, s(W - PAD), y], fill=RULE, width=s(1))
    y += s(22)
    if data.get("bars_title"):
        d.text((x0, y), data["bars_title"], font=font("semibold", 14), fill=INK_3)
        y += s(28)
    cols = 5 if len(dims) == 5 else 3
    cwid = (inner - (cols - 1) * 20) / cols
    for i, dm in enumerate(dims):
        r, c = divmod(i, cols)
        bx = x0 + s(c * (cwid + 20))
        by = y + s(r * 64)
        lab = dm.get("label", "")
        sc_t = f"{dm.get('score', 0)}/{dm.get('max', 0)}"
        d.text((bx, by), lab, font=font("semibold", 14), fill=INK)
        d.text((bx + s(cwid) - d.textlength(sc_t, font=font("regular", 14)), by), sc_t, font=font("regular", 14), fill=INK_2)
        d.rounded_rectangle([bx, by + s(26), bx + s(cwid), by + s(34)], radius=s(4), fill=RULE)
        frac = 0 if not dm.get("max") else max(0, min(1, dm["score"] / dm["max"]))
        if frac > 0:
            d.rounded_rectangle([bx, by + s(26), bx + s(cwid) * frac, by + s(34)], radius=s(4), fill=ACCENT)
    y += s(((len(dims) - 1) // cols + 1) * 64 + 10)

    # ---- tests
    d.line([x0, y, s(W - PAD), y], fill=RULE, width=s(1))
    y += s(22)
    d.text((x0, y), "What to test", font=font("semibold", 18), fill=INK)
    y += s(30)
    note = data.get("duration_note")
    if note:
        for line in wrap(d, note, font("regular", 13), inner, 2):
            d.text((x0, y), line, font=font("regular", 13), fill=INK_3)
            y += s(20)
    y += s(8)
    for it in items:
        c = prio(it.get("priority"))
        pin(d, x0 + s(14), y + s(12), it.get("n"), it.get("priority"))
        tx = x0 + s(40)
        pf = font("bold", 12)
        pl = c["label"].upper()
        pw = d.textlength(pl, font=pf) + s(16)
        d.rounded_rectangle([tx, y + s(2), tx + pw, y + s(22)], radius=s(10), fill=c["fill"])
        d.text((tx + s(8), y + s(5)), pl, font=pf, fill=c["text"])
        px = tx + pw + s(10)
        part = it.get("part")
        if part:
            pf2 = font("semibold", 12)
            ptw = d.textlength(part.upper(), font=pf2) + s(16)
            d.rounded_rectangle([px, y + s(2), px + ptw, y + s(22)], radius=s(10), outline=INK_3, width=s(1))
            d.text((px + s(8), y + s(5)), part.upper(), font=pf2, fill=INK_2)
            px += ptw + s(10)
        d.text((px, y + s(1)), it.get("pattern", ""), font=font("semibold", 16), fill=INK)
        dur = it.get("duration")
        if dur:
            d.text((s(W - PAD) - d.textlength(dur, font=font("semibold", 14)), y + s(3)), dur, font=font("semibold", 14), fill=INK_2)
        y += s(30)
        for line in wrap(d, it.get("test"), font("regular", 15), inner - 40, 2):
            d.text((tx, y), line, font=font("regular", 15), fill=INK)
            y += s(22)
        ev = it.get("evidence")
        if ev:
            for line in wrap(d, ev, font("regular", 13), inner - 40, 2):
                d.text((tx, y + s(2)), line, font=font("regular", 13), fill=INK_3)
                y += s(21)
        y += s(16)

    # ---- footer
    d.line([x0, y, s(W - PAD), y], fill=RULE, width=s(1))
    y += s(16)
    for line in wrap(d, DISCLAIMER, font("regular", 12), inner):
        d.text((x0, y), line, font=font("regular", 12), fill=INK_3)
        y += s(18)
    y += s(PAD - 10)

    canvas.crop((0, 0, s(W), y)).save(out, optimize=True)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--data", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    with open(a.data, encoding="utf-8") as fh:
        data = json.load(fh)
    render(data, os.path.dirname(os.path.abspath(a.data)), a.out)
    print(a.out)


if __name__ == "__main__":
    main()
