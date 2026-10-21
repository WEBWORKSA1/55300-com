# 55300.com — Paycheck & Money Lab

Free, private salary, paycheck and money calculators with 2026 U.S. tax data. Static site, built for GitHub Pages (free plan).

- **9 calculators**: take-home pay, salary ⇄ hourly, raise, 50/30/20 budget, job-offer comparison, freelance rate, loan, savings goal, AI Pay-Resilience Score
- **27 salary pages** ($30k–$150k + the $55,300 benchmark), **6 long-form guides**, video library
- **Lead generation**: 3-step Free Pay Check-Up funnel + homepage quick form + calculator CTAs
- **Monetization**: Google AdSense (Auto ads), donations, sponsorships, partner referrals, contests, careers, ambassadors
- **Compliance**: privacy/cookies, terms, disclaimer, trademark & copyright disclosure, methodology, ads.txt, sitemap, structured data

## Structure
```
index.html, *.html        generated pages (do not hand-edit — edit build/ and rebuild)
calculators/ salary/ guides/
css/style.css             design system (light/dark)
js/config.js              payment links, donation goal  ← edit freely, no rebuild needed
js/site.js                nav, forms, donations, video, cookies
js/calc.js                2026 tax engine + calculators
build/                    Python generator (python3 build/build.py)
PROMPTS.md                phase-wise build prompts
```

## Rebuild
```
python3 build/build.py
```

## Forms
All forms post via FormSubmit to the site's private inbox (address is encoded and never shown). **The first submission sends a one-time activation email to that inbox — click "Activate" once** and every form starts delivering.

## Payments
Paste your hosted PayPal / Stripe Payment Link / Buy Me a Coffee / Ko-fi URLs into `js/config.js`. Blank links fall back to the pledge form.

## Custom domain (needed for AdSense approval)
1. DNS at your registrar: apex `A` → 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153; `www` `CNAME` → `webworksa1.github.io`.
2. Repo Settings → Pages → Custom domain → `55300.com` (this creates the CNAME file) → Enforce HTTPS.
3. In AdSense: add site `55300.com`, enable Auto ads, and enable the Google-certified CMP (Privacy & messaging → GDPR) for EEA/UK visitors.

© 2026 55300.com. "55300" is used solely as a numeric domain name; see `legal.html`.
