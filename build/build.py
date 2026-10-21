"""Build 55300.com: python3 build/build.py  (outputs static HTML to the repo root)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import lib, tools, salary, guides, pages

OUT = lib.OUT

def static():
    files = {
        "ads.txt": "google.com, pub-6620975821265271, DIRECT, f08c47fec0942fa0\n",
        "robots.txt": "User-agent: *\nAllow: /\n\nUser-agent: Mediapartners-Google\nAllow: /\n\nSitemap: https://55300.com/sitemap.xml\n",
        ".nojekyll": "",
        "manifest.webmanifest": '{"name":"55300 — Paycheck & Money Lab","short_name":"55300","start_url":"./index.html","display":"standalone","background_color":"#f7f9fc","theme_color":"#0a8f5b","icons":[{"src":"img/favicon.svg","sizes":"any","type":"image/svg+xml"}]}\n',
        "img/favicon.svg": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0a8f5b"/><stop offset="1" stop-color="#0b5c8f"/></linearGradient></defs><rect width="64" height="64" rx="16" fill="url(#g)"/><text x="32" y="40" font-family="Arial,Helvetica,sans-serif" font-size="20" font-weight="700" fill="#fff" text-anchor="middle">553</text></svg>\n',
    }
    for p, c in files.items():
        d = os.path.join(OUT, p); os.makedirs(os.path.dirname(d), exist_ok=True)
        open(d, "w").write(c)
    # 404: works on github.io/55300-com/ and on the custom domain root
    open(os.path.join(OUT, "404.html"), "w").write('''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Page not found | 55300</title><meta name="robots" content="noindex">
<script>var b=location.pathname.indexOf("/55300-com/")===0?"/55300-com/":"/";document.write('<base href="'+b+'">');</script>
<link rel="stylesheet" href="css/style.css">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6620975821265271" crossorigin="anonymous"></script></head>
<body><div class="topbar"><a href="https://web.works/contact" target="_blank" rel="noopener">Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership →</a></div>
<section class="section"><div class="wrap center" style="max-width:640px"><div class="big">404</div><h1>This page took an unpaid day off.</h1><p class="lead">The page you're looking for doesn't exist or has moved.</p>
<p><a class="btn btn-primary" href="index.html">Go home</a> <a class="btn btn-ghost" href="calculators/index.html">Calculators</a> <a class="btn btn-ghost" href="salary/index.html">Salary tables</a></p></div></section></body></html>''')

if __name__ == "__main__":
    tools.build(); salary.build(); guides.build(); pages.build(); static(); lib.sitemap()
    print(f"Built {len(lib.PAGES)} indexable pages")
