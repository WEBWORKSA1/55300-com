"""Shared layout for the 55300.com static site generator.
Every page gets: AdSense script, top interest banner, header/nav, footer, cookie notice, JS."""
import json, os, html

SITE = "https://55300.com"
OUT = os.path.join(os.path.dirname(__file__), "..")
UPDATED = "October 21, 2026"
UPDATED_ISO = "2026-10-21"
ADSENSE = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6620975821265271" crossorigin="anonymous"></script>'
PAGES = []  # for sitemap

NAV = [
    ("calculators/index.html", "Calculators"),
    ("salary/index.html", "Salary Tables"),
    ("guides/index.html", "Guides"),
    ("videos.html", "Videos"),
    ("community.html", "Community"),
    ("support.html", "Support Us"),
]

def esc(s):
    return html.escape(s, quote=True)

def head(title, desc, path, root, schema=None, noindex=False):
    canon = SITE + "/" + ("" if path == "index.html" else path.replace("index.html", ""))
    ld = ""
    base_ld = {"@context": "https://schema.org", "@type": "WebSite", "name": "55300", "url": SITE + "/",
               "description": "Free salary, paycheck and money calculators with 2026 tax data."}
    for s in ([base_ld] if path == "index.html" else []) + (schema or []):
        ld += '<script type="application/ld+json">' + json.dumps(s, ensure_ascii=False) + "</script>\n"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
{'<meta name="robots" content="noindex">' if noindex else '<meta name="robots" content="index,follow,max-image-preview:large">'}
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website"><meta property="og:site_name" content="55300">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canon}">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#0a8f5b">
<link rel="icon" href="{root}img/favicon.svg" type="image/svg+xml">
<link rel="manifest" href="{root}manifest.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}css/style.css">
{ADSENSE}
{ld}</head>
"""

def header(root, active):
    cur = ' aria-current="page"'
    links = "".join(
        f'<a href="{root}{h}"{cur if active == h else ""}>{t}</a>' for h, t in NAV)
    return f"""<body>
<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><a href="https://web.works/contact" target="_blank" rel="noopener">Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership →</a></div>
<header class="header"><div class="wrap nav">
  <a class="logo" href="{root}index.html" aria-label="55300 home"><span class="mark">55·300</span><span>55300<small>Paycheck &amp; Money Lab</small></span></a>
  <button class="icon-btn burger" data-burger aria-label="Menu" aria-expanded="false" aria-controls="menu">☰</button>
  <nav class="menu" id="menu" aria-label="Main">{links}<a class="btn btn-primary btn-sm" href="{root}pay-checkup.html">Free Pay Check-Up</a><button class="icon-btn" data-theme-toggle aria-label="Toggle dark mode">◐</button></nav>
</div></header>
<main id="main">
"""

def footer(root):
    return f"""</main>
<section class="section alt" aria-label="Newsletter"><div class="wrap strip">
  <div><h3 style="margin:0">Get the 2027 tax-change alert</h3><p class="muted" style="margin:0">One short email when brackets, limits or paycheck rules change. No spam.</p></div>
  <form class="inline-form" data-form="newsletter" data-ok="You're on the list — watch for our next alert.">
    <input class="hp" name="_honey" tabindex="-1" autocomplete="off">
    <input type="email" name="email" placeholder="you@email.com" required aria-label="Email">
    <input type="hidden" name="consent" value="on">
    <button class="btn btn-primary" type="submit">Notify me</button>
    <p class="form-msg" role="status"></p>
  </form>
</div></section>
<footer class="footer"><div class="wrap">
  <div class="fgrid">
    <div><a class="logo" href="{root}index.html" style="color:#fff"><span class="mark">55·300</span><span>55300</span></a>
      <p style="margin-top:12px">Free, fast, privacy-friendly salary and money calculators. Every number dated, sourced and recalculated for the {UPDATED[-4:]} tax year.</p>
      <p class="small">Calculations run in your browser — nothing you type into a calculator is stored.</p></div>
    <div><h4>Calculators</h4><ul>
      <li><a href="{root}calculators/take-home-pay.html">Take-home pay</a></li><li><a href="{root}calculators/salary-to-hourly.html">Salary ⇄ hourly</a></li>
      <li><a href="{root}calculators/raise.html">Raise</a></li><li><a href="{root}calculators/budget.html">Budget 50/30/20</a></li>
      <li><a href="{root}calculators/job-offer-compare.html">Job offer compare</a></li><li><a href="{root}calculators/freelance-rate.html">Freelance rate</a></li>
      <li><a href="{root}calculators/loan.html">Loan payment</a></li><li><a href="{root}calculators/savings-goal.html">Savings goal</a></li>
      <li><a href="{root}calculators/ai-pay-resilience.html">AI Pay-Resilience Score</a></li></ul></div>
    <div><h4>Learn</h4><ul>
      <li><a href="{root}salary/index.html">Salary tables</a></li><li><a href="{root}salary/55300-a-year.html">$55,300 a year</a></li>
      <li><a href="{root}guides/index.html">Guides</a></li><li><a href="{root}videos.html">Video library</a></li>
      <li><a href="{root}methodology.html">Methodology &amp; sources</a></li><li><a href="{root}about.html#why-55300">Why “55300”?</a></li></ul></div>
    <div><h4>Community</h4><ul>
      <li><a href="{root}pay-checkup.html">Free Pay Check-Up</a></li><li><a href="{root}support.html">Donate / support</a></li>
      <li><a href="{root}community.html#contests">Contests &amp; prizes</a></li><li><a href="{root}community.html#careers">Careers &amp; talent</a></li>
      <li><a href="{root}advertise.html">Advertise &amp; sponsor</a></li><li><a href="{root}embed.html">Embed our calculators</a></li></ul></div>
    <div><h4>Company</h4><ul>
      <li><a href="{root}about.html">About</a></li><li><a href="{root}contact.html">Contact</a></li>
      <li><a href="{root}privacy.html">Privacy &amp; cookies</a></li><li><a href="{root}terms.html">Terms of use</a></li>
      <li><a href="{root}disclaimer.html">Disclaimer</a></li><li><a href="{root}legal.html">Trademark &amp; copyright</a></li></ul></div>
  </div>
  <div class="legal">© <span data-year>2026</span> 55300.com. All original content and code © 55300.com. “55300” is used solely as a numeric domain name; we claim no exclusive rights in the number and are not affiliated with any postal service, municipality, government agency, employer or brand that uses the same digits. See <a href="{root}legal.html">Trademark &amp; copyright disclosure</a>. Information is educational and not tax, legal or financial advice.</div>
</div></footer>
<div class="cookie" id="cookie" role="dialog" aria-label="Cookie notice"><b>Cookies &amp; ads.</b> We use cookies to run the site and, with Google AdSense, to show and measure ads. <a href="{root}privacy.html#cookies">Learn more</a>.
  <div class="actions"><button class="btn btn-primary btn-sm" data-ck="all">Accept</button><button class="btn btn-ghost btn-sm" data-ck="essential">Essential only</button></div></div>
<button class="btn btn-primary btn-sm totop" id="totop" aria-label="Back to top">↑</button>
<script src="{root}js/config.js"></script>
<script src="{root}js/site.js" defer></script>
<script src="{root}js/calc.js" defer></script>
</body></html>
"""

def write(path, title, desc, body, schema=None, active=None, noindex=False, priority="0.6"):
    depth = path.count("/")
    root = "../" * depth
    body = body.replace("{root}", root)
    full = head(title, desc, path, root, schema, noindex) + header(root, active or path) + body + footer(root)
    dest = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as f:
        f.write(full)
    if not noindex:
        PAGES.append((path, priority))

def crumbs(items):
    """items: list of (href or None, label) — hrefs may use {root}."""
    parts = [f'<a href="{h}">{esc(t)}</a>' if h else esc(t) for h, t in items]
    ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": t} for i, (h, t) in enumerate(items)]}
    return '<nav class="crumbs" aria-label="Breadcrumb">' + " / ".join(parts) + "</nav>", ld

def faq(items):
    html_ = "".join(f"<details><summary>{esc(q)}</summary><p>{a}</p></details>" for q, a in items)
    import re
    ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}} for q, a in items]}
    return html_, ld

def helpful():
    return '<div class="helpful card" data-root="{root}" style="margin-top:20px;display:flex;gap:12px;align-items:center;flex-wrap:wrap"><b>Was this helpful?</b><button class="btn btn-ghost btn-sm" data-helpful="yes">👍 Yes</button><button class="btn btn-ghost btn-sm" data-helpful="no">👎 No</button><span style="margin-left:auto;display:flex;gap:8px"><button class="btn btn-ghost btn-sm" data-share>Share</button><button class="btn btn-ghost btn-sm" data-print>Print</button></span></div>'

def lead_cta(title="Want a human to check your numbers?", text="Book a free 15-minute Pay Check-Up: offer review, raise strategy or a take-home plan built around your real situation.", q=""):
    return f'''<section class="lead-box reveal" style="margin:32px 0"><div style="position:relative;z-index:1;max-width:640px">
<span class="eyebrow" style="color:#7ef0bd">Free · No obligation</span><h2>{title}</h2><p class="lead">{text}</p>
<a class="btn btn-accent" href="{{root}}pay-checkup.html{q}">Start my free Pay Check-Up →</a></div></section>'''

def video(vid, title):
    return f'<figure style="margin:0"><div class="video" data-yt="{vid}" data-title="{esc(title)}" role="button" tabindex="0" aria-label="Play: {esc(title)}"><img loading="lazy" src="https://i.ytimg.com/vi/{vid}/hqdefault.jpg" alt="{esc(title)}" width="480" height="360"><div class="play"><span>▶</span></div></div><figcaption class="small muted" style="margin-top:8px">{esc(title)} · <a href="https://www.youtube.com/watch?v={vid}" target="_blank" rel="noopener">Watch on YouTube</a></figcaption></figure>'

def sitemap():
    urls = "".join(
        f"<url><loc>{SITE}/{'' if p == 'index.html' else p.replace('index.html','')}</loc><lastmod>{UPDATED_ISO}</lastmod><priority>{pr}</priority></url>\n"
        for p, pr in PAGES)
    with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "</urlset>\n")
