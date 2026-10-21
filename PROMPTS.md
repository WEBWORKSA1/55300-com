# 55300.com — Phase-wise Build Prompts

Concept: **55300 — Paycheck & Money Lab.** A free, private, calculator-first finance site anchored on the "$55,300 benchmark salary". Finance/career is one of the highest-CPC AdSense verticals; salary-to-hourly and take-home queries have huge, evergreen, yearly-recurring search demand; and programmatic salary pages scale indexed pages without thin content.

Use these prompts in order with any capable AI coding assistant to rebuild, extend or fork the site. Each phase is self-contained and ends with a checkable outcome.

---

## Phase 0 — Research & positioning
> Research the number "55300" across commerce, business, AI, the economy and people (salary benchmarks, postal codes, codes, cultural meanings). Pick the meaning with the highest commercial search intent. Audit at least 25 leading salary/paycheck/finance-calculator sites (Calculator.net, SmartAsset, ADP, PaycheckCity, Omni, Bankrate, Talent.com, Salary.com, Levels.fyi, PayScale, Indeed, CalculatorSoup, SalaryAfterTax, Wealthsimple, Ramsey, MIT Living Wage, Numbeo, BLS OOH, Glassdoor, Adzuna, TheSalaryCalculator, ListenToTaxman, TaxTips, TurboTax, H&R Block, IRS Withholding Estimator, Forbes Advisor). Output: must-have features, lead-gen patterns, AdSense-safe layout patterns, design patterns and the gaps competitors leave open (stale tax years, broken tables, sign-up walls).

**Outcome:** positioning statement + feature list.

## Phase 1 — Foundation & design system
> Create a static, dependency-free site for GitHub Pages (free plan). Use a Python generator (`build/`) that writes plain HTML to the repo root so every page shares one header/footer. Design tokens in `css/style.css`: ink navy, money green, amber accent; Inter + Space Grotesk numerals; light and dark themes; 16px gutters; no horizontal scroll at 390px. On every page: the exact AdSense `<script>` in `<head>` (client ca-pub-6620975821265271); a top bar reading "Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership" linked to https://web.works/contact; sticky header with nav and theme toggle; footer with legal links; cookie notice; back-to-top.

**Outcome:** `build/lib.py`, `css/style.css`, empty pages render consistently.

## Phase 2 — Calculator engine
> Write `js/calc.js` with a 2026 US federal tax engine (IRS 2026 brackets, $16,100/$32,200 standard deduction, SS 6.2% to $184,500, Medicare 1.45% + 0.9% above $200k/$250k, 401(k) $24,500 cap). Build nine calculators that recalculate live and save inputs to the URL for sharing: take-home pay (every pay period, marginal vs average rate, "your next $1,000 raise nets $X"), salary⇄hourly (PTO-adjusted), raise (after-tax and inflation-adjusted), 50/30/20 budget (target vs actual, red/green), job-offer comparison (true hourly value incl. commute and benefits), freelance rate (self-employment tax), loan (amortization + extra payments), savings goal (compound growth, goal date) and an AI Pay-Resilience Score quiz.

**Outcome:** each calculator page shows inputs left, results right, formula + worked example + FAQ below. Verify: $55,300 single, 4% state, 5% 401(k), $2,400 premiums → $40,247 take-home.

## Phase 3 — Content for AdSense approval (E-E-A-T)
> Generate 27 programmatic salary pages ($30k–$150k in $5k steps plus $55,300) with unique computed tables, budgets, comparisons to the BLS May 2025 mean wage ($69,770), FAQ schema and prev/next links. Write six original long-form guides (what $55,300 means, reading a pay stub, raise negotiation, 50/30/20 stress test, salary vs hourly vs freelance, AI and your paycheck). Add About (incl. "Why 55300"), Methodology & Sources, Privacy & Cookies (Google advertising-cookie wording + opt-out links), Terms, Disclaimer and Trademark & Copyright disclosure. Add JSON-LD (WebSite, WebApplication, Article, FAQPage, BreadcrumbList), sitemap.xml, robots.txt, ads.txt.

**Outcome:** 55+ indexable pages, no thin or duplicate pages, every number sourced and dated.

## Phase 4 — Lead generation
> Build a 3-step "Free Pay Check-Up" funnel (goal → situation → contact) with progress bar, prefill from calculator URLs (?goal=&income=), partner opt-in checkbox, consent, honeypot and a thank-you page. Add a 60-second inline lead form on the homepage and result-adjacent CTAs in every calculator sidebar. Deliver all forms through FormSubmit AJAX to the site inbox. The inbox address must never appear on the page or in plain text in the source: assemble it at runtime from an XOR-encoded array; mail links use `data-mail` and open the visitor's mail app on click.

**Outcome:** every form submits to the single site inbox; address not visible anywhere.

## Phase 5 — Monetization & community
> Support page: donation tiers ($5/$15/$55/$300), PayPal/Stripe/Buy Me a Coffee/Ko-fi buttons driven by `js/config.js` (fall back to a pledge form when a link is blank), goal progress bar, fund-allocation bar (operations, tools, promotion, hiring, prizes), honest "not tax-deductible" FAQ. Community page: skill-based contests with official rules (no purchase necessary, 18+), entry form; careers table + application form; ambassador/promotions form. Advertise page: sponsorship packages, editorial standards, media-kit form, domain/website acquisition link. Embed page with iframe code for backlinks.

**Outcome:** donations, contests, hiring, promotions and sponsorship all have working forms.

## Phase 6 — Media & engagement
> Videos page and in-guide videos using click-to-load YouTube (youtube-nocookie) thumbnails for speed. "Was this helpful?" rating, share and print buttons, newsletter "tax-change alert" capture in every footer.

## Phase 7 — Deploy
> Push to GitHub repo `webworksa1/55300-com` (branch `main`, plus `gh-pages` for Pages). Enable Pages from the branch root. When DNS is ready, add a `CNAME` file containing `55300.com`, point apex A records to 185.199.108.153 / .109.153 / .110.153 / .111.153 and `www` CNAME to `webworksa1.github.io`, then tick "Enforce HTTPS".

## Phase 8 — Grow & scale (next)
> Add state-specific take-home pages (50 states with real bracket tables), Canada/UK/India paycheck calculators, hourly pages ($15–$100/h), a cost-of-living comparison with sourced indexes, Spanish/French versions, a PDF "pay report" export behind email capture, and a quarterly salary survey ("contribute your salary") to build proprietary data.
