"""Programmatic salary pages: '$X a year is how much?' with unique computed content."""
from lib import write, crumbs, faq, helpful, lead_cta, UPDATED

STD = {"single": 16100, "mfj": 32200}
BR = {"single": [(12400, .10), (50400, .12), (105700, .22), (201775, .24), (256225, .32), (640600, .35), (1e18, .37)],
      "mfj": [(24800, .10), (100800, .12), (211400, .22), (403550, .24), (512450, .32), (768700, .35), (1e18, .37)]}
BLS_MEAN = 69770

def fed(t, st):
    tax, prev, marg = 0, 0, .10
    for top, r in BR[st]:
        if t > prev:
            tax += (min(t, top) - prev) * r; marg = r
        prev = top
    return tax, marg

def net(g, st="single", state=0.0):
    f, m = fed(max(0, g - STD[st]), st)
    fi = min(g, 184500) * .062 + g * .0145 + max(0, g - (200000 if st == "single" else 250000)) * .009
    s = g * state
    return g - f - fi - s, f, fi, s, m

def d(x, dec=0):
    return f"${x:,.{dec}f}"

AMOUNTS = list(range(30000, 150001, 5000)) + [55300]
AMOUNTS = sorted(set(AMOUNTS))

def slug(a):
    return f"{a}-a-year"

def build():
    for idx, a in enumerate(AMOUNTS):
        h = a / 2080
        n0, f0, fi0, _, m0 = net(a)
        n5, *_ = net(a, state=.05)
        nm, fm, *_ = net(a, "mfj")
        ratio = a / BLS_MEAN
        cmp = "above" if a > BLS_MEAN else "below"
        mo = n0 / 12
        rent = a / 12 * .28
        prev_a = AMOUNTS[idx - 1] if idx else None
        next_a = AMOUNTS[idx + 1] if idx + 1 < len(AMOUNTS) else None
        rows = "".join(f'<tr><td>{p}</td><td class="r num">{d(a/div, 2)}</td><td class="r num">{d(n0/div, 2)}</td><td class="r num">{d(n5/div, 2)}</td></tr>'
                       for p, div in [("Year", 1), ("Month", 12), ("Semi-monthly", 24), ("Bi-weekly", 26), ("Week", 52), ("Day (8h)", 260), ("Hour", 2080)])
        flagship = ""
        if a == 55300:
            flagship = f'''<h2 id="why">Why $55,300 is our benchmark</h2>
<p>$55,300 sits in the middle of the American pay distribution: it is close to the U.S. median household income the Census Bureau reported for 2015 ($55,775), below the {d(BLS_MEAN)} mean annual wage across all occupations in the BLS May 2025 survey, and inside the Pew Research Center's middle-income band. That makes it a useful reference point for "an ordinary full-time salary" — and the number this site is named after.</p>
<p>Use it as an anchor: if you earn more, you can see exactly how much more; if you earn less, every calculator shows the gap in hourly, monthly and take-home terms.</p>'''
        fh, fld = faq([
            (f"How much is ${a:,} a year per hour?", f"{d(h, 2)} an hour, based on 40 hours a week for 52 weeks (2,080 hours)."),
            (f"How much is ${a:,} a year per month after taxes?", f"About {d(mo)} a month for a single filer in a state with no income tax in 2026, or about {d(n5/12)} with a 5% state income tax."),
            (f"Is ${a:,} a good salary?", f"It is {abs(ratio-1)*100:.0f}% {cmp} the {d(BLS_MEAN)} mean annual wage for all U.S. occupations (BLS, May 2025). Whether it is comfortable depends mostly on local housing costs and household size."),
            (f"What tax bracket is ${a:,} in?", f"A single filer's top federal bracket is {m0*100:.0f}% (taxable income {d(max(0,a-16100))} after the standard deduction). The average federal rate is only {f0/a*100:.1f}%.")])
        c, cld = crumbs([("{root}index.html", "Home"), ("{root}salary/index.html", "Salary tables"), (None, f"${a:,} a year")])
        nav = '<div style="display:flex;justify-content:space-between;gap:10px;margin:24px 0">' + (f'<a class="btn btn-ghost" href="{slug(prev_a)}.html">← ${prev_a:,}</a>' if prev_a else "<span></span>") + (f'<a class="btn btn-ghost" href="{slug(next_a)}.html">${next_a:,} →</a>' if next_a else "") + "</div>"
        body = f'''<section class="hero" style="padding-bottom:24px"><div class="wrap">{c}<span class="eyebrow">Salary table · {UPDATED[-4:]} tax year</span>
<h1>${a:,} a year is how much an hour?</h1><p class="lead"><b class="num">${a:,}</b> a year is <b class="num">{d(h,2)}</b> an hour, <b class="num">{d(a/12)}</b> a month before tax and about <b class="num">{d(mo)}</b> a month after federal tax and FICA.</p>
<div class="stats" style="max-width:820px"><div class="stat"><div class="k">Hourly</div><div class="v">{d(h,2)}</div></div><div class="stat"><div class="k">Monthly gross</div><div class="v">{d(a/12)}</div></div><div class="stat"><div class="k">Bi-weekly gross</div><div class="v">{d(a/26)}</div></div><div class="stat"><div class="k">Take-home / yr*</div><div class="v">{d(n0)}</div></div><div class="stat"><div class="k">Marginal fed. rate</div><div class="v">{m0*100:.0f}%</div></div></div></div></section>
<section class="section"><div class="wrap layout"><article class="article">
<h2>${a:,} salary by pay period</h2><div class="table-wrap"><table><thead><tr><th>Period</th><th class="r">Gross</th><th class="r">Take-home (no state tax)*</th><th class="r">Take-home (5% state)*</th></tr></thead><tbody>{rows}</tbody></table></div>
<p class="small muted">*Single filer, 2026 standard deduction ($16,100), federal brackets, Social Security 6.2% and Medicare 1.45%. No pre-tax deductions. <a href="{{root}}calculators/take-home-pay.html?salary={a}">Personalise in the take-home calculator →</a></p>
<h2>Where the money goes</h2><ul><li>Federal income tax: <b>{d(f0)}</b> (average rate {f0/a*100:.1f}%).</li><li>Social Security + Medicare: <b>{d(fi0)}</b>.</li><li>Married filing jointly (one earner): take-home rises to about <b>{d(nm)}</b> because the standard deduction doubles.</li></ul>
<h2>A realistic monthly budget on ${a:,}</h2><p>Using the 50/30/20 rule on {d(mo)} monthly take-home: <b>{d(mo*.5)}</b> for needs, <b>{d(mo*.3)}</b> for wants and <b>{d(mo*.2)}</b> for savings and debt. The common 28%-of-gross housing guideline puts rent or mortgage at about <b>{d(rent)}</b> a month. <a href="{{root}}calculators/budget.html?income={round(mo)}">Open the budget planner →</a></p>
<h2>How ${a:,} compares</h2><p>${a:,} is <b>{abs(ratio-1)*100:.0f}% {cmp}</b> the {d(BLS_MEAN)} mean annual wage for all U.S. occupations (BLS Occupational Employment and Wage Statistics, May 2025). The mean is pulled up by high earners, so the typical worker earns less than the mean.</p>
{flagship}
<h2>Frequently asked questions</h2>{fh}{nav}{helpful()}</article>
<aside class="sidebar"><div class="card"><h3>Is your pay fair?</h3><p class="small muted">Get a free Pay Check-Up: market range for your role and a script to ask for more.</p><a class="btn btn-primary btn-block" href="{{root}}pay-checkup.html?goal=raise&income={a}">Check my pay →</a></div>
<div class="card"><h3>Other salaries</h3><p class="small">{" · ".join(f'<a href="{slug(x)}.html">${x//1000}k</a>' if x % 1000 == 0 else f'<a href="{slug(x)}.html">${x:,}</a>' for x in AMOUNTS[max(0,idx-4):idx+5] if x != a)}</p><a href="index.html" class="small">All salary tables →</a></div></aside></div></section>
<div class="wrap">{lead_cta(q=f"?goal=raise&income={a}")}</div>'''
        write(f"salary/{slug(a)}.html", f"${a:,} a Year Is How Much an Hour? After-Tax Pay (2026) | 55300",
              f"${a:,} a year is {d(h,2)} an hour, {d(a/12)} a month. See 2026 take-home pay, taxes, budget and how ${a:,} compares to the U.S. average.",
              body, [cld, fld], active="salary/index.html", priority="0.9" if a == 55300 else "0.7")

    # index
    rows = "".join(f'<tr><td><a href="{slug(a)}.html"><b>${a:,}</b></a></td><td class="r num">{d(a/2080,2)}</td><td class="r num">{d(a/12)}</td><td class="r num">{d(net(a)[0]/12)}</td></tr>' for a in AMOUNTS)
    hourly = "".join(f'<tr><td>${x}/h</td><td class="r num">{d(x*2080)}</td><td class="r num">{d(x*2080/12)}</td></tr>' for x in [15, 18, 20, 22, 25, 28, 30, 35, 40, 45, 50, 60, 75])
    c, cld = crumbs([("{root}index.html", "Home"), (None, "Salary tables")])
    body = f'''<section class="hero"><div class="wrap">{c}<span class="eyebrow">2026 salary tables</span><h1>Salary to hourly &amp; take-home tables</h1><p class="lead">Every salary from $30,000 to $150,000 converted to hourly, monthly and after-tax pay with 2026 federal rates. Click any row for the full breakdown.</p></div></section>
<section class="section"><div class="wrap grid g2" style="align-items:start"><div><h2>Annual salary</h2><div class="table-wrap"><table><thead><tr><th>Salary</th><th class="r">Hourly</th><th class="r">Monthly gross</th><th class="r">Monthly take-home*</th></tr></thead><tbody>{rows}</tbody></table></div><p class="small muted">*Single, no state tax, no pre-tax deductions, 2026.</p></div>
<div><h2>Hourly to annual</h2><div class="table-wrap"><table><thead><tr><th>Hourly</th><th class="r">Annual</th><th class="r">Monthly</th></tr></thead><tbody>{hourly}</tbody></table></div>{lead_cta("Negotiating a salary right now?","We'll benchmark your offer and draft the counter — free.","?goal=offer")}</div></div></section>'''
    write("salary/index.html", "Salary to Hourly & Take-Home Pay Tables (2026) | 55300", "Salary tables from $30,000 to $150,000: hourly, monthly and after-tax take-home pay with 2026 federal tax rates.", body, [cld], active="salary/index.html", priority="0.8")
