"""Original long-form guides (E-E-A-T content for AdSense approval)."""
from lib import write, crumbs, helpful, lead_cta, video, UPDATED, UPDATED_ISO

GUIDES = []

def g(slug, title, desc, minutes, sections, vid=None, cta_q=""):
    GUIDES.append((slug, title, desc, minutes))
    toc = "".join(f'<li><a href="#s{i}">{h}</a></li>' for i, (h, _) in enumerate(sections))
    content = "".join(f'<h2 id="s{i}">{h}</h2>{b}' for i, (h, b) in enumerate(sections))
    if vid:
        content += f"<h2>Watch: related explainer</h2>{video(*vid)}"
    c, cld = crumbs([("{root}index.html", "Home"), ("{root}guides/index.html", "Guides"), (None, title)])
    art = {"@context": "https://schema.org", "@type": "Article", "headline": title, "description": desc,
           "dateModified": UPDATED_ISO, "datePublished": UPDATED_ISO, "author": {"@type": "Organization", "name": "55300 Editorial Team"},
           "publisher": {"@type": "Organization", "name": "55300"}}
    body = f'''<section class="section"><div class="wrap layout"><article class="article">{c}
<span class="eyebrow">Guide</span><h1>{title}</h1>
<div class="byline"><span>By the 55300 Editorial Team</span><span>Updated {UPDATED}</span><span>{minutes} min read</span></div>
<p class="lead">{desc}</p>{content}
{lead_cta(q=cta_q)}{helpful()}
<p class="small muted">Educational content only — not tax, legal or financial advice. Sources and assumptions: <a href="{{root}}methodology.html">methodology</a>.</p></article>
<aside class="sidebar"><div class="card toc"><h3>On this page</h3><ol>{toc}</ol></div>
<div class="card"><h3>Run your numbers</h3><p class="small muted">Every figure in this guide can be recalculated with your own inputs.</p><a class="btn btn-primary btn-block" href="{{root}}calculators/index.html">Open calculators</a></div></aside></div></section>'''
    write(f"guides/{slug}.html", f"{title} | 55300", desc, body, [art, cld], active="guides/index.html", priority="0.8")

def build():
    g("what-a-55300-salary-means", "What a $55,300 Salary Really Means in 2026",
      "Hourly, monthly, after-tax and in real life: a complete, numbers-first breakdown of a $55,300 salary using 2026 tax rules.", 7, [
        ("The headline conversions", "<p>At a standard 2,080 paid hours, $55,300 a year is <b>$26.59 an hour</b>, <b>$4,608 a month</b>, <b>$2,127 every two weeks</b> and <b>$1,063 a week</b> before tax. Those are the numbers recruiters quote; they are not the numbers that reach your bank account.</p>"),
        ("Take-home pay, step by step", "<p>For a single filer in 2026, the $16,100 standard deduction leaves $39,200 of taxable income. The first $12,400 is taxed at 10% ($1,240) and the next $26,800 at 12% ($3,216), for <b>$4,456 of federal income tax</b> — an average rate of about 8%, even though the marginal rate is 12%.</p><p>FICA then takes 7.65%: $3,429 for Social Security and $802 for Medicare, or <b>$4,230</b>. In a state with no income tax, take-home is about <b>$46,614 a year ($3,884 a month)</b>. A 5% state tax lowers that to roughly $43,849.</p><div class='callout'>Add a 5% 401(k) contribution and $200 a month of health premiums and take-home falls to about $40,250 in a 4% state — but the 401(k) money is still yours, just invested.</div>"),
        ("What it buys: a realistic budget", "<p>On $3,884 a month, the 50/30/20 rule allocates $1,942 to needs, $1,165 to wants and $777 to savings and debt. The 28%-of-gross housing guideline caps rent at about $1,290. In many mid-sized U.S. metros that is enough for a one-bedroom; in the most expensive coastal cities it usually is not, and a 60/20/20 split is the honest alternative.</p>"),
        ("How it compares", "<p>The Bureau of Labor Statistics reported a mean annual wage of $69,770 across all occupations in May 2025, so $55,300 is about 21% below the mean. Means are pulled up by top earners, however, so the typical (median) worker earns noticeably less than the mean. $55,300 is solidly within the middle-income band most researchers use.</p>"),
        ("Five moves that change the math", "<ol><li><b>Capture the full employer match.</b> A 4% match is a $2,212 raise you can't negotiate any other way.</li><li><b>Use pre-tax accounts.</b> Each $1,000 into a traditional 401(k) costs about $880 of take-home at a 12% bracket.</li><li><b>Negotiate base, not just bonus.</b> Raises compound off base pay.</li><li><b>Price your commute.</b> See the <a href='{root}calculators/job-offer-compare.html'>offer comparison tool</a>.</li><li><b>Check your withholding</b> after any life change so a large refund isn't an interest-free loan to the government.</li></ol>"),
      ], ("V86YyZ1EY_o", "How to read a paycheck"), "?goal=takehome")

    g("gross-vs-net-pay-stub", "Gross vs. Net Pay: How to Read Every Line of Your Pay Stub",
      "A line-by-line walkthrough of a U.S. pay stub — earnings, pre-tax deductions, taxes and year-to-date totals — so you can spot errors fast.", 6, [
        ("Gross pay: the top line", "<p>Gross pay is everything you earned in the period before anything is withheld: salary or hourly wages, overtime (at least 1.5× for eligible hourly workers beyond 40 hours a week under federal law), shift differentials, bonuses and commissions. Check the hours and rate first — most paycheck errors start here.</p>"),
        ("Pre-tax deductions", "<p>These come out before income tax is calculated: traditional 401(k) or 403(b) contributions, health/dental/vision premiums under a Section 125 plan, HSA and FSA contributions, and some commuter benefits. Health premiums under Section 125 also reduce FICA wages; 401(k) contributions do not.</p>"),
        ("Taxes withheld", "<ul><li><b>Federal income tax</b> — based on your W-4 and IRS withholding tables.</li><li><b>Social Security</b> — 6.2% of wages up to $184,500 in 2026.</li><li><b>Medicare</b> — 1.45% of all wages, plus 0.9% above $200,000.</li><li><b>State and local income tax</b> — varies; nine states have no tax on wages.</li><li><b>State disability or paid-leave programs</b> in some states.</li></ul>"),
        ("Post-tax deductions and net pay", "<p>After taxes come Roth 401(k) contributions, union dues, wage garnishments and voluntary insurance. What remains is net pay — the deposit. Divide net by gross: most full-time workers keep between 70% and 80%.</p>"),
        ("Year-to-date (YTD) columns", "<p>YTD totals show cumulative earnings and withholding since January. Use them to confirm your 401(k) is on track for the annual limit ($24,500 in 2026), to see if Social Security stopped after the wage base, and to estimate your tax bill before filing.</p>"),
        ("A 60-second audit checklist", "<ol><li>Hours and rate correct?</li><li>Overtime paid at the right multiple?</li><li>Benefit deductions match your enrollment?</li><li>401(k) percentage matches your election?</li><li>State matches where you live/work?</li></ol><p>Found a mistake? Email payroll with the pay date, the line and the expected amount. Then use the <a href='{root}calculators/take-home-pay.html'>take-home calculator</a> to check the corrected figure.</p>"),
      ], ("yju47Tiw4JM", "Gross pay vs net pay explained"))

    g("how-to-negotiate-a-raise", "How to Negotiate a Raise With Data: A Step-by-Step Playbook",
      "A practical, numbers-based process for asking for more pay — research, timing, the exact ask and how to handle 'no'.", 8, [
        ("Step 1: Know your number", "<p>Gather three data points: market pay for your role and location (public salary surveys, job postings that list pay ranges), inflation since your last raise, and the measurable value you created. Turn each into dollars. A raise request built on numbers is a business decision for your manager; one built on need is a favor.</p>"),
        ("Step 2: Choose the timing", "<p>The best windows are 4–8 weeks before budgets are set, right after a visible win, or when your responsibilities have clearly grown. The worst are during layoffs or the week of a missed target.</p>"),
        ("Step 3: Anchor with a specific figure", "<p>Ask for a specific number slightly above your target — '$61,500' rather than 'around $60k'. Precise numbers signal research. Anchoring research in negotiation consistently shows that the first credible number shapes the final outcome.</p><div class='callout'>Script: \"Over the last year I took over X and delivered Y, worth about $Z. Market data for this role in our area is $A–$B. I'd like to move my base to $C. What would it take to get there this cycle?\"</div>"),
        ("Step 4: Translate the ask", "<p>Show your manager what it costs. A move from $55,300 to $59,000 is $3,700 a year — about $308 a month, or less than 7% of base. Use the <a href='{root}calculators/raise.html'>raise calculator</a> to show the after-tax value to you and keep emotion out of it.</p>"),
        ("Step 5: Handle 'not now'", "<ul><li>Ask what specific results would justify the raise and by when — get it in writing.</li><li>Negotiate non-salary items: title, remote days, training budget, extra PTO, an earlier review date.</li><li>Set a calendar check-in. If the goalposts move twice, the market is your answer.</li></ul>"),
        ("Step 6: The outside offer", "<p>Changing employers often produces a larger pay increase than staying, because new hires are priced at market. If you use an outside offer as leverage, be prepared to accept it.</p>"),
      ], ("e2_HXKNIzaM", "How to negotiate a higher salary: evidence-based tips"), "?goal=raise")

    g("50-30-20-budget-real-incomes", "The 50/30/20 Budget, Stress-Tested on Real Incomes",
      "Does the most popular budget rule survive real rents and real paychecks? We run it at $35k, $55.3k and $90k — and show when to switch rules.", 6, [
        ("The rule", "<p>Split after-tax income: 50% needs, 30% wants, 20% savings and extra debt payments. It was popularised as a simple alternative to line-item budgets, and its strength is that you only track three numbers.</p>"),
        ("Test 1: $35,000 salary", "<p>Take-home (single, no state tax) is about $2,525 a month in 2026. Needs get $1,263 — tight for rent plus food plus transport almost anywhere. At this income a 70/20/10 split is often more realistic; the priority is a $1,000 starter emergency fund and avoiding high-interest debt.</p>"),
        ("Test 2: $55,300 salary", "<p>Take-home is about $3,884 a month. Needs get $1,942, wants $1,165, savings $777. Works in moderate-cost cities with a one-bedroom or roommates. In high-cost cities, 60/20/20 protects the savings rate by trimming wants instead.</p>"),
        ("Test 3: $90,000 salary", "<p>Take-home is roughly $6,012 a month (single, no state tax). The rule now leaves meaningful room: $1,202 a month of savings. At this level, consider 40/30/30 — lifestyle creep is the main risk, not affordability.</p>"),
        ("When to switch rules", "<ul><li>Needs above 55% for three months → 60/20/20.</li><li>High-interest debt → push savings bucket to 25–30% and point it at the debt.</li><li>Income up 10%+ → bank at least half of the raise before adjusting lifestyle.</li></ul><p>Try it with your income in the <a href='{root}calculators/budget.html'>budget planner</a>.</p>"),
      ], ("MOa_hXL9Fz8", "50/30/20 vs 70/20/10 budget rule"), "?goal=budget")

    g("salary-vs-hourly-vs-freelance", "Salary vs. Hourly vs. Freelance: Comparing Offers Apples-to-Apples",
      "How to convert any pay structure into comparable numbers — including benefits, overtime, paid leave and self-employment tax.", 7, [
        ("Three structures, three hidden costs", "<p>Salaried roles bundle paid leave and benefits but may require unpaid extra hours. Hourly roles pay for every hour (and overtime if non-exempt) but may lack paid leave. Freelance work pays the most per billable hour but makes you the employer: you pay both halves of FICA, your own benefits and your own downtime.</p>"),
        ("Step 1: Put everything on an annual basis", "<p>Hourly × expected annual hours (not 2,080 if you'll get less). Salary + expected bonus. Freelance: realistic billable hours × rate − expenses.</p>"),
        ("Step 2: Add the benefits an employer pays", "<p>Employer health premiums commonly run several thousand dollars a year for single coverage, the employer 401(k) match is often 3–6% of pay, and employers pay 7.65% FICA on top of wages. A $55,300 salaried job with typical benefits can be worth well over $65,000 in total compensation.</p>"),
        ("Step 3: Subtract the costs you'd carry", "<p>Freelancers pay self-employment tax of 15.3% on 92.35% of net earnings (Social Security portion capped at $184,500 in 2026), plus insurance, equipment and unpaid admin time. That is why a contractor typically needs 1.5–2× an employee's hourly rate to come out even — see the <a href='{root}calculators/freelance-rate.html'>freelance rate calculator</a>.</p>"),
        ("Step 4: Compare per hour of life", "<p>Divide total value by real hours — including commute and the unpaid evenings a salaried role may expect. The <a href='{root}calculators/job-offer-compare.html'>offer comparison tool</a> does this automatically.</p>"),
      ], ("bx9bTbN5wH0", "Salary negotiation: top mistakes to avoid"), "?goal=offer")

    g("ai-and-your-paycheck", "AI and Your Paycheck: A Practical Framework for the Next Five Years",
      "Which parts of your work AI is likely to change, how that affects pay, and a 90-day plan to stay on the right side of the shift.", 7, [
        ("Tasks change before jobs do", "<p>Economic research on automation consistently finds that technologies replace specific <i>tasks</i> first. Most jobs are bundles of tasks; when some become cheap, the remaining human tasks — judgment, accountability, relationships, physical skill — usually become a larger share of the role and of its value.</p>"),
        ("Where exposure is highest", "<ul><li>Routine text production: first drafts, summaries, standard emails.</li><li>Structured data work: entry, reconciliation, templated reports.</li><li>Well-specified analysis that can be written down as a brief.</li></ul><p>High exposure does not automatically mean lower pay — workers who use AI to do more of the higher-value work can become more productive. It does mean the routine part of the paycheck is at risk of being repriced.</p>"),
        ("Where resilience is highest", "<ul><li>Decisions under uncertainty where someone must be accountable.</li><li>In-person, hands-on and care work.</li><li>Owning trust: clients, patients, partners and teams.</li><li>Directing, checking and integrating AI output.</li></ul>"),
        ("Pay strategy", "<p>Price your outcomes, not your hours. If AI makes you twice as fast, an hourly rate halves your income while a project or value-based price keeps the gain. Employees can make the same argument in reviews: document time saved and what you did with it.</p>"),
        ("A 90-day plan", "<ol><li>Weeks 1–2: list your tasks and hours; mark each routine or judgment.</li><li>Weeks 3–6: automate one routine task with an AI tool and measure the time saved.</li><li>Weeks 7–10: reinvest that time in a visible, decision-heavy project.</li><li>Weeks 11–13: bring the results — in numbers — to your next pay conversation.</li></ol><p>Take the <a href='{root}calculators/ai-pay-resilience.html'>AI Pay-Resilience Score</a> to see where you start.</p>"),
      ], None, "?goal=career")

    cards = "".join(f'<a class="card tool-card reveal" href="{s}.html"><span class="tag">{m} min read</span><h3>{t}</h3><p>{d}</p></a>' for s, t, d, m in GUIDES)
    c, cld = crumbs([("{root}index.html", "Home"), (None, "Guides")])
    body = f'''<section class="hero"><div class="wrap">{c}<span class="eyebrow">Guides</span><h1>Money guides that show their math</h1><p class="lead">Plain-English explainers with real 2026 numbers. Every figure links back to a calculator so you can rerun it with yours.</p></div></section>
<section class="section"><div class="wrap"><div class="grid g3">{cards}</div>{lead_cta()}</div></section>'''
    write("guides/index.html", "Salary, Paycheck & Budget Guides | 55300", "Original guides on take-home pay, pay stubs, raise negotiation, budgeting, offer comparison and AI's effect on pay — with 2026 numbers.", body, [cld], active="guides/index.html", priority="0.8")
