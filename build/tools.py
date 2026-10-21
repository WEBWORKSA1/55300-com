"""Calculator pages."""
from lib import write, crumbs, faq, helpful, lead_cta, esc, UPDATED

TOOLS = [
    ("take-home-pay", "💵", "Take-Home Pay Calculator", "Net pay after 2026 federal tax, FICA, state tax, 401(k) and deductions — every pay period at once."),
    ("salary-to-hourly", "⏱️", "Salary ⇄ Hourly Converter", "Convert any pay rate between hourly, daily, weekly, bi-weekly, monthly and annual, adjusted for time off."),
    ("raise", "📈", "Raise Calculator", "See what a raise is really worth after tax and after inflation."),
    ("budget", "🧮", "50/30/20 Budget Planner", "Split take-home pay into needs, wants and savings — and compare with what you actually spend."),
    ("job-offer-compare", "⚖️", "Job Offer Comparison", "Compare two offers on total value and true hourly pay, including bonus, match, benefits and commute."),
    ("freelance-rate", "🧑‍💻", "Freelance Rate Calculator", "The hourly and day rate you need to match an employee salary, including self-employment tax."),
    ("loan", "🏦", "Loan Payment Calculator", "Monthly payment, total interest and a yearly amortization schedule — with extra-payment savings."),
    ("savings-goal", "🎯", "Savings Goal & Compound Growth", "How fast your savings grow and when you hit your target."),
    ("ai-pay-resilience", "🤖", "AI Pay-Resilience Score", "An 8-question self-check: how exposed is your paycheck to automation, and what to do next."),
]

def money(name, label, val, hint=""):
    return f'<div class="field"><label for="{name}">{label}</label><div class="money"><input id="{name}" name="{name}" inputmode="decimal" value="{val}"></div>{f"<span class=hint>{hint}</span>" if hint else ""}</div>'

def num(name, label, val, hint="", step="any"):
    return f'<div class="field"><label for="{name}">{label}</label><input id="{name}" name="{name}" type="number" step="{step}" value="{val}">{f"<span class=hint>{hint}</span>" if hint else ""}</div>'

PER_SELECT = '<select id="per" name="per"><option value="year">per year</option><option value="month">per month</option><option value="biweek">every two weeks</option><option value="week">per week</option><option value="hour">per hour</option></select>'

def related(skip):
    cards = "".join(f'<a class="card tool-card" href="{{root}}calculators/{s}.html"><span class="ico">{i}</span><h3>{t}</h3><p>{d}</p></a>' for s, i, t, d in TOOLS if s != skip)
    return f'<section class="section"><div class="wrap"><h2>More free calculators</h2><div class="grid g4">{cards}</div></div></section>'

def page(slug, title, desc, intro, calc_type, form, article, faqs, cta_q=""):
    name = next(t for s, i, t, d in TOOLS if s == slug)
    c, cld = crumbs([("{root}index.html", "Home"), ("{root}calculators/index.html", "Calculators"), (None, name)])
    fh, fld = faq(faqs)
    app = {"@context": "https://schema.org", "@type": "WebApplication", "name": name, "applicationCategory": "FinanceApplication",
           "operatingSystem": "Any", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "description": desc}
    body = f'''<section class="hero" style="padding-bottom:20px"><div class="wrap">{c}
<span class="eyebrow">Free calculator · Updated {UPDATED}</span><h1>{title}</h1><p class="lead">{intro}</p></div></section>
<section style="padding:8px 0 32px"><div class="wrap"><div class="grid g2" data-calc="{calc_type}" data-root="{{root}}" style="align-items:start">
<form class="calc" onsubmit="return false" aria-label="{esc(name)} inputs">{form}
<p class="small muted" style="margin:6px 0 0">🔒 Runs in your browser. Nothing is stored or sent.</p></form>
<div class="calc out" aria-live="polite" style="position:sticky;top:84px"></div></div>
{helpful()}</div></section>
<section class="section alt"><div class="wrap layout"><article class="article">{article}
<h2 id="faq">Frequently asked questions</h2>{fh}
<p class="small muted">Last reviewed {UPDATED} by the 55300 editorial team. Read our <a href="{{root}}methodology.html">methodology &amp; sources</a>.</p></article>
<aside class="sidebar"><div class="card"><h3>Talk to a person</h3><p class="small muted">Turn this result into a plan: offer review, raise script or a budget built for you.</p><a class="btn btn-primary btn-block" data-cta-income data-base="{{root}}pay-checkup.html" href="{{root}}pay-checkup.html{cta_q}">Free Pay Check-Up</a></div>
<div class="card"><h3>Keep this site free</h3><p class="small muted">No paywalls, no sign-ups. Reader support funds tax-data updates and new tools.</p><a class="btn btn-ghost btn-block" href="{{root}}support.html">Support 55300</a></div></aside></div></section>
<div class="wrap">{lead_cta(q=cta_q)}</div>{related(slug)}'''
    write(f"calculators/{slug}.html", f"{title} | 55300", desc, body, [app, cld, fld], active="calculators/index.html", priority="0.9")

BRACKETS = [("10%", "$0 – $12,400", "$0 – $24,800"), ("12%", "$12,401 – $50,400", "$24,801 – $100,800"),
            ("22%", "$50,401 – $105,700", "$100,801 – $211,400"), ("24%", "$105,701 – $201,775", "$211,401 – $403,550"),
            ("32%", "$201,776 – $256,225", "$403,551 – $512,450"), ("35%", "$256,226 – $640,600", "$512,451 – $768,700"),
            ("37%", "Over $640,600", "Over $768,700")]
BRACKET_TABLE = '<div class="table-wrap"><table><thead><tr><th>Rate</th><th>Single (taxable income)</th><th>Married filing jointly</th></tr></thead><tbody>' + "".join(f"<tr><td><b>{r}</b></td><td>{a}</td><td>{b}</td></tr>" for r, a, b in BRACKETS) + "</tbody></table></div><p class='small muted'>Source: IRS 2026 inflation adjustments. Standard deduction: $16,100 single, $32,200 married filing jointly, $24,150 head of household.</p>"

def build():
    # 1 Take-home
    form = f'''<div class="row"><div class="field"><label for="salary">Gross pay</label><div class="money"><input id="salary" name="salary" inputmode="decimal" value="55300"></div></div><div class="field"><label for="per">Pay basis</label>{PER_SELECT}</div></div>
<div class="row"><div class="field"><label for="status">Filing status</label><select id="status" name="status"><option value="single">Single</option><option value="mfj">Married filing jointly</option></select></div>
{num("state","State + local income tax rate (%)","4","0 in AK, FL, NV, NH, SD, TN, TX, WA, WY. Use your state's flat or effective rate.","0.1")}</div>
<div class="row">{num("k401","401(k) contribution (% of pay)","5","2026 limit $24,500","0.5")}{money("pretax","Other pre-tax deductions / yr","2400","Health, dental, HSA, FSA (Section 125)")}</div>'''
    art = f'''<h2>How take-home pay is calculated</h2>
<p>Your paycheck shrinks in a fixed order. First, pre-tax deductions such as 401(k) contributions and employer health premiums come out. Next, federal income tax is applied to what is left after the standard deduction, using progressive brackets — each rate only touches the slice of income inside its band. Then FICA takes 6.2% for Social Security (on wages up to $184,500 in 2026) and 1.45% for Medicare, plus an extra 0.9% Medicare on wages above $200,000 for single filers. Finally your state and local tax is subtracted.</p>
<div class="callout"><b>Worked example — $55,300 salary, single, 4% state tax, 5% 401(k), $2,400 health premiums:</b> 401(k) $2,765 · taxable income after the $16,100 standard deduction ≈ $34,035 · federal tax ≈ $3,836 · FICA ≈ $4,047 · state ≈ $2,005 · <b>take-home ≈ $40,247/yr ($3,354/month)</b>.</div>
<h2>Marginal vs. average tax rate</h2>
<p>Your <b>marginal</b> rate is the rate on your next dollar; your <b>average</b> rate is total tax divided by gross pay. At $55,300 a single filer's marginal federal rate is 12% because taxable income stays below $50,400, but the average federal rate is only about 8%. That is why a raise never "pushes you into a bracket where you take home less" — only the dollars above the threshold are taxed at the higher rate.</p>
<h2>2026 federal income tax brackets</h2>{BRACKET_TABLE}
<h2>What this calculator does not include</h2>
<ul><li>Local taxes with special bases (e.g., NYC, Philadelphia wage tax) — include them in the state rate field.</li><li>Itemized deductions, tax credits (Child Tax Credit, EITC) and W-4 adjustments — these change refunds and withholding.</li><li>Roth 401(k) contributions — enter 0% in the 401(k) field and treat Roth as an after-tax expense.</li></ul>'''
    page("take-home-pay", "Take-Home Pay Calculator 2026", "Free 2026 take-home pay calculator: net pay per paycheck after federal tax, FICA, state tax, 401(k) and benefits. Marginal and average rates included.",
         "Enter your salary or hourly rate. See net pay for every period, your marginal and average tax rate, and what your next raise is really worth.",
         "takehome", form, art,
         [("How much is $55,300 a year after taxes?", "For a single filer with no state income tax and no pre-tax deductions, about $46,614 a year or $3,884 a month in 2026. With 4% state tax, a 5% 401(k) and $2,400 of health premiums it drops to roughly $40,250."),
          ("Is FICA charged on 401(k) contributions?", "Yes. Traditional 401(k) contributions lower federal (and most state) income tax but not Social Security or Medicare. Section 125 health premiums lower both."),
          ("Why is my actual paycheck different?", "Employers withhold using your W-4 and the IRS percentage method, which can differ slightly from annual tax owed. Credits, bonuses taxed at the 22% supplemental rate and local taxes also cause differences."),
          ("What is the Social Security wage base for 2026?", "$184,500. Earnings above that are not subject to the 6.2% Social Security tax; Medicare has no cap.")], "?goal=takehome")

    # 2 Hourly
    form = f'''<div class="row">{money("amount","Pay amount","55300")}<div class="field"><label for="per">Paid</label><select id="per" name="per"><option value="year">per year</option><option value="month">per month</option><option value="semimonth">twice a month</option><option value="biweek">every two weeks</option><option value="week">per week</option><option value="day">per day</option><option value="hour">per hour</option></select></div></div>
<div class="row">{num("hours","Hours per week","40")}{num("weeks","Paid weeks per year","52")}</div>
{num("daysoff","Paid days off (vacation + holidays)","15","Used to show your effective rate per hour actually worked")}'''
    art = '''<h2>The formula</h2><p>Annual salary = hourly rate × hours per week × weeks per year. With the standard 40 hours and 52 weeks, a year has 2,080 paid hours, so you can divide a salary by 2,080 — or roughly halve it and drop the thousands: $55,300 ≈ $26.59 an hour.</p>
<div class="callout"><b>Quick mental math:</b> $1 an hour ≈ $2,000 a year. $30/h ≈ $62,400. $55,300/yr ≈ $26.59/h ≈ $4,608/month ≈ $2,127 per bi-weekly check.</div>
<h2>Why paid time off matters</h2><p>If you receive 15 paid days off, you are paid for 2,080 hours but work about 1,960. Your effective rate per hour worked rises by roughly 6%. When comparing a salaried role with an hourly contract that has no paid leave, compare effective rates, not headline rates.</p>
<h2>Semi-monthly vs. bi-weekly</h2><p>Bi-weekly pay arrives 26 times a year, so two months each year contain three paychecks. Semi-monthly arrives 24 times on fixed dates. The annual total is identical; the per-check amount is about 8% larger with semi-monthly pay.</p>'''
    page("salary-to-hourly", "Salary to Hourly Converter", "Convert salary to hourly and hourly to salary instantly — daily, weekly, bi-weekly, semi-monthly, monthly and annual, adjusted for paid time off.",
         "Type any rate and see every pay period instantly, including your true rate per hour actually worked after vacation and holidays.",
         "hourly", form, art,
         [("How much is $55,300 a year per hour?", "$26.59 an hour at 40 hours a week for 52 weeks (2,080 hours)."),
          ("How many work hours are in a year?", "2,080 for a standard 40-hour week. In 2026 there are 261 weekdays, so a calendar-exact count is 2,088 hours, which some payroll systems use."),
          ("How much is $25 an hour annually?", "$52,000 a year at 40 hours a week, or $4,333 a month before tax.")])

    # 3 Raise
    form = f'''{money("current","Current salary","55300")}
<div class="row">{num("pct","Raise (%)","4","","0.1")}{num("inflation","Expected inflation (%)","3","","0.1")}</div>
<div class="field"><label for="status">Filing status</label><select id="status" name="status"><option value="single">Single</option><option value="mfj">Married filing jointly</option></select></div>'''
    art = '''<h2>Nominal vs. real raises</h2><p>A 4% raise in a year with 3% inflation increases your purchasing power by only about 1%. The calculator divides (1 + raise) by (1 + inflation) to show the real change. A raise below inflation is a pay cut in disguise.</p>
<h2>How much of a raise do you keep?</h2><p>Your raise is taxed at your <b>marginal</b> rate plus 7.65% FICA plus state tax. For most people earning $50,000–$100,000 that means keeping roughly 65–75 cents of each new dollar.</p>
<h2>Benchmarks to anchor a raise request</h2><ul><li>Inflation over your last raise period.</li><li>Market pay for your role — see our <a href="{root}salary/index.html">salary tables</a>.</li><li>Measurable value you added (revenue, savings, time).</li></ul><p>Then use the step-by-step <a href="{root}guides/how-to-negotiate-a-raise.html">raise negotiation playbook</a>.</p>'''
    page("raise", "Raise Calculator: What Your Raise Is Really Worth", "Calculate the after-tax and inflation-adjusted value of a raise. See monthly gain and how much of each new dollar you keep in 2026.",
         "Plug in your salary and raise percentage. We show the after-tax gain, the monthly difference and whether you beat inflation.",
         "raise", form, art,
         [("What is a good raise percentage in 2026?", "A raise that beats inflation plus 1–2 points keeps you ahead. Promotions and job changes typically produce larger jumps than annual merit increases."),
          ("Can a raise lower my take-home pay?", "No. Progressive brackets tax only the income above each threshold, so take-home always rises with gross pay (benefit cliffs from income-tested programs are a separate issue).")], "?goal=raise")

    # 4 Budget
    form = f'''{money("income","Monthly take-home pay","3884")}
<div class="field"><label>Budget rule</label><input type="hidden" name="rule" value="50-30-20"><div class="seg" data-seg="rule"><button class="on" value="50-30-20">50/30/20</button><button value="60-20-20">60/20/20</button><button value="70-20-10">70/20/10</button><button value="40-30-30">40/30/30</button></div></div>
<p class="small muted" style="margin:0 0 10px">Optional — what you actually spend each month:</p>
<div class="row">{money("needs","Needs (rent, food, bills)","")}{money("wants","Wants (dining, fun, travel)","")}</div>{money("savings","Savings & extra debt payments","")}'''
    art = '''<h2>The 50/30/20 rule in one minute</h2><p>Half of after-tax income goes to needs (housing, utilities, groceries, insurance, minimum debt payments), 30% to wants and 20% to savings and extra debt payoff. It is a starting point, not a law: in expensive cities needs often reach 60%, which is why the planner lets you switch to 60/20/20 or 70/20/10.</p>
<div class="callout"><b>On a $55,300 salary</b> (≈ $3,884/month take-home, no state tax): needs $1,942 · wants $1,165 · savings $777. The 28% gross-income housing rule caps rent near $1,290.</div>
<h2>Making the plan stick</h2><ol><li>Automate the savings transfer for payday.</li><li>Track only three numbers — needs, wants, savings — not 40 categories.</li><li>Review monthly; adjust the rule, not your honesty.</li></ol>
<p>Read the full stress-test in <a href="{root}guides/50-30-20-budget-real-incomes.html">our 50/30/20 guide</a>.</p>'''
    page("budget", "50/30/20 Budget Calculator & Planner", "Free 50/30/20 budget calculator. Split monthly take-home pay into needs, wants and savings, compare with real spending and get an emergency-fund target.",
         "Enter your monthly take-home pay, pick a rule, and optionally add what you spend now. Red means over budget, green means room to spare.",
         "budget", form, art,
         [("Is 50/30/20 realistic in 2026?", "For many renters in high-cost metros, needs exceed 50%. A 60/20/20 split keeps savings at 20% by trimming wants — usually the more realistic trade."),
          ("Does debt go in needs or savings?", "Minimum payments are needs. Anything above the minimum counts toward the 20% savings-and-debt bucket.")], "?goal=budget")

    # 5 Offer compare
    def side(p, base, bonus, match, health, pto, commute, cc):
        return f'''<fieldset style="border:1px solid var(--line);border-radius:12px;padding:12px;margin:0 0 12px"><legend><b>Offer {p.upper()[0]}</b></legend>
<div class="row">{money(p+"base","Base salary",base)}{money(p+"bonus","Expected bonus / yr",bonus)}</div>
<div class="row">{num(p+"match","401(k) match (% of base)",match,"","0.5")}{money(p+"health","Your health premium / month",health)}</div>
<div class="row">{num(p+"pto","Paid days off",pto)}{num(p+"hours","Hours per week","40")}</div>
<div class="row">{num(p+"commute","Commute hours / week",commute,"","0.5")}{money(p+"commutecost","Commute cost / month",cc)}</div></fieldset>'''
    form = side("a_", "55300", "2000", "4", "150", "15", "5", "180") + side("b_", "60000", "0", "3", "250", "10", "8", "320")
    art = '''<h2>Why base salary is the wrong comparison</h2><p>Two offers with the same salary can differ by thousands once you add employer 401(k) match, bonus, health premiums, paid leave and the unpaid hours you spend commuting. This tool converts everything into one number: <b>value per hour of your life committed to the job</b>.</p>
<h2>What we count</h2><ul><li>Total value = base + bonus + employer match − your health premiums − commute costs.</li><li>Real hours = scheduled hours − paid leave + commute time (48 working weeks).</li><li>True hourly value = total value ÷ real hours.</li></ul>
<h2>Things to price in yourself</h2><p>Equity, remote flexibility, career trajectory and team quality. A higher-hourly offer is not automatically better — but you should know exactly what the trade costs.</p>'''
    page("job-offer-compare", "Job Offer Comparison Calculator", "Compare two job offers side by side: salary, bonus, 401(k) match, health premiums, PTO and commute converted into true hourly value.",
         "Enter both offers. We convert salary, bonus, benefits, paid leave and commute into one honest number: true hourly value.",
         "offer", form, art,
         [("How do I value a 401(k) match?", "A 4% match on $55,300 is $2,212 a year of free money — as valuable as a 4% raise, and often tax-deferred."),
          ("Should I count commute time?", "Yes. Eight hours a week of commuting is about 384 unpaid hours a year — roughly ten 40-hour weeks.")], "?goal=offer")

    # 6 Freelance
    form = f'''{money("target","Salary you want to replace","55300")}
<div class="row">{money("expenses","Business expenses / yr","6000","Software, insurance, health plan, equipment")}{num("taxrate","Income tax rate (%)","15","Federal + state effective estimate","0.5")}</div>
<div class="row">{num("billable","Billable hours / week","25","Most freelancers bill 50–70% of hours worked")}{num("weeks","Working weeks / yr","46")}</div>
{num("margin","Safety margin (%)","10","Gaps between clients, late payments")}'''
    art = '''<h2>Why freelancers must charge 1.5–2× the employee hourly rate</h2><p>Employers pay half of FICA, provide paid leave, equipment and benefits, and pay you for non-billable time. As a freelancer you pay 15.3% self-employment tax on 92.35% of net earnings, fund your own health and retirement, and only get paid for billable hours.</p>
<div class="callout"><b>Example:</b> to replace a $55,300 salary with $6,000 of expenses, a 15% income-tax rate, 25 billable hours for 46 weeks and a 10% buffer, you need roughly $75–80 an hour — about 2.9× the $26.59 employee rate.</div>
<h2>Pricing beyond hourly</h2><p>Once you know your floor, move to project or value pricing. Clients buy outcomes, and a fixed price rewards you for getting faster with experience and AI tools.</p>'''
    page("freelance-rate", "Freelance Hourly Rate Calculator", "Calculate the freelance or contractor hourly and day rate needed to match a salary, including self-employment tax, expenses and unbilled time.",
         "Find the minimum rate that replaces a salary after self-employment tax, expenses and the hours you can't bill.",
         "freelance", form, art,
         [("What is self-employment tax in 2026?", "15.3% (12.4% Social Security up to the $184,500 wage base plus 2.9% Medicare) on 92.35% of net self-employment earnings. Half is deductible for income tax."),
          ("How many billable hours are realistic?", "20–30 per week for most solo professionals once you account for sales, admin and learning.")], "?goal=freelance")

    # 7 Loan
    form = f'''{money("principal","Loan amount","25000")}
<div class="row">{num("apr","Interest rate (APR %)","7.5","","0.01")}{num("years","Term (years)","5","","1")}</div>
{money("extra","Extra payment / month","0","See how much interest an extra payment saves")}'''
    art = '''<h2>The payment formula</h2><p>Monthly payment = P × r ÷ (1 − (1 + r)<sup>−n</sup>), where P is the principal, r the monthly rate (APR ÷ 12) and n the number of months. Early payments are mostly interest; later payments are mostly principal.</p>
<h2>How extra payments help</h2><p>Every extra dollar goes straight to principal, which reduces the interest charged on every future month. On a 5-year, $25,000 loan at 7.5%, adding $100 a month pays it off 11 months sooner and saves about $1,000 in interest.</p>
<h2>Affordability rule of thumb</h2><p>Lenders look at debt-to-income: total monthly debt payments under roughly 36% of gross monthly income. On $55,300 a year ($4,608/month) that is about $1,660 a month across all debts.</p>'''
    page("loan", "Loan Payment Calculator with Amortization", "Free loan calculator: monthly payment, total interest, payoff date and a yearly amortization schedule. Test extra payments for auto, personal and student loans.",
         "Works for auto, personal, student and small-business loans. Add an extra monthly payment to see the interest you save.",
         "loan", form, art,
         [("What is a good APR for a personal loan?", "It depends on credit score and lender. Compare the APR (which includes fees) across at least three lenders before accepting."),
          ("Does paying extra reduce my monthly payment?", "Usually not — it shortens the loan and cuts total interest. Some lenders will re-amortize on request.")], "?goal=debt")

    # 8 Savings
    form = f'''<div class="row">{money("initial","Starting balance","1000")}{money("monthly","Monthly contribution","400")}</div>
<div class="row">{num("rate","Annual return (%)","6","Savings ~3–4%, diversified stocks long-run ~6–8% (not guaranteed)","0.1")}{num("years","Years","10")}</div>
{money("goal","Goal (optional)","50000")}'''
    art = '''<h2>Compound growth, simply</h2><p>Each month your balance earns a return, and next month's return is earned on the bigger balance. Over long periods growth can exceed what you put in — which is why starting early matters more than starting big.</p>
<div class="callout"><b>The 20% of $55,300:</b> saving 20% of take-home (≈ $777/month) at 6% for 10 years grows to roughly $127,000, of which about $34,000 is growth.</div>
<h2>Tax-advantaged accounts (2026 limits)</h2><ul><li>401(k)/403(b): $24,500 employee deferral (+$8,000 catch-up at 50+).</li><li>IRA (traditional or Roth): $7,500 (+$1,100 catch-up at 50+).</li><li>HSA: $4,400 self-only, $8,750 family.</li></ul>'''
    page("savings-goal", "Savings Goal & Compound Interest Calculator", "See how your savings grow with monthly contributions and compound interest, and how long it takes to reach your goal. Includes 2026 401(k), IRA and HSA limits.",
         "Set a starting balance, monthly deposit and return. We chart contributions vs. growth and tell you when you'll reach your goal.",
         "savings", form, art,
         [("What return should I assume?", "Use a conservative figure. High-yield savings pays a few percent; diversified stock portfolios have historically averaged more over long periods but fluctuate and are not guaranteed."),
          ("How much should I save from a $55,300 salary?", "20% of take-home (about $775 a month) is a solid target; capture any employer 401(k) match first.")], "?goal=savings")

    # 9 AI
    QS = [("How much of your week is routine writing, data entry or reporting?", ["Most of it", "About half", "Little"]),
          ("How often do you make judgment calls with real consequences?", ["Rarely", "Weekly", "Daily"]),
          ("How much of your work is face-to-face with clients, patients or teams?", ["Almost none", "Some", "A lot"]),
          ("Do you already use AI tools to do your job faster?", ["No", "Occasionally", "Every day"]),
          ("Does your work require physical presence or hands-on skill?", ["No", "Partly", "Yes"]),
          ("Do you own relationships that bring in revenue or trust?", ["No", "Some", "Yes, key ones"]),
          ("When did you last learn a new paid skill?", ["3+ years ago", "1–3 years", "This year"]),
          ("Could your output be fully specified in a written brief?", ["Yes, easily", "Partly", "No, it's ambiguous"])]
    qh = "".join(f'<div class="q"><p>{i+1}. {q}</p><div class="pill-row">' + "".join(f'<label><input type="radio" name="q{i}" value="{k+1}">{o}</label>' for k, o in enumerate(opts)) + "</div></div>" for i, (q, opts) in enumerate(QS))
    art = '''<h2>What the score measures</h2><p>Research on AI and work consistently finds that tasks — not whole jobs — get automated first: routine, well-specified, text-and-data tasks are most exposed, while judgment, physical presence, trust relationships and supervising AI output are more resilient. This quiz scores your current <b>task mix</b> on those dimensions.</p>
<h2>How to raise your score in 90 days</h2><ol><li><b>Automate your own routine work</b> before someone else does — and show the time saved.</li><li><b>Move toward decisions</b>: volunteer for work where you own outcomes, not drafts.</li><li><b>Build trust capital</b>: client relationships and cross-team credibility are hard to replicate.</li><li><b>Learn one adjacent, billable skill</b> per year and put it on your résumé with numbers.</li></ol>
<p>Read our framework guide: <a href="{root}guides/ai-and-your-paycheck.html">AI and your paycheck</a>.</p>'''
    page("ai-pay-resilience", "AI Pay-Resilience Score", "Free 8-question self-assessment: how exposed is your paycheck to AI and automation, and what to do about it in the next 90 days.",
         "Eight quick questions about how you actually spend your work week. Get a 0–100 score and a 90-day plan to make your pay harder to automate.",
         "ai", qh, art,
         [("Is this a prediction of job loss?", "No. It is a reflective framework based on task characteristics. Use it to decide what to learn and where to spend time."),
          ("Which skills hold value as AI spreads?", "Judgment under uncertainty, accountability for outcomes, hands-on and in-person work, relationship ownership and the ability to direct and check AI output.")], "?goal=career")

    # Hub
    cards = "".join(f'<a class="card tool-card reveal" href="{s}.html"><span class="ico">{i}</span><h3>{t}</h3><p>{d}</p></a>' for s, i, t, d in TOOLS)
    c, cld = crumbs([("{root}index.html", "Home"), (None, "Calculators")])
    body = f'''<section class="hero"><div class="wrap">{c}<span class="eyebrow">9 free tools · {UPDATED[-4:]} tax data</span><h1>Salary, paycheck &amp; money calculators</h1><p class="lead">Fast, accurate and private. Every tool runs in your browser, shows its formula and links to official sources.</p></div></section>
<section class="section"><div class="wrap"><div class="grid g3">{cards}</div>{lead_cta()}</div></section>'''
    write("calculators/index.html", "Free Salary, Paycheck & Money Calculators (2026) | 55300", "Nine free calculators: take-home pay, salary to hourly, raise, budget, job offer comparison, freelance rate, loan, savings and an AI pay-resilience score.", body, [cld], active="calculators/index.html", priority="0.9")
