"""Core pages: home, lead gen, community, support, advertise, legal, etc."""
from lib import write, crumbs, faq, helpful, lead_cta, video, UPDATED
from tools import TOOLS

VIDEOS = [
    ("V86YyZ1EY_o", "How to read a paycheck", "Paychecks"),
    ("yju47Tiw4JM", "How to read your paycheck: gross pay vs net pay", "Paychecks"),
    ("-4qkis2FooU", "How to read a pay stub (with sample paycheck)", "Paychecks"),
    ("XQ0f87stf_o", "Understanding your paycheck", "Paychecks"),
    ("e2_HXKNIzaM", "How to negotiate a higher salary: 3 evidence-based tips", "Negotiation"),
    ("bx9bTbN5wH0", "Salary negotiation: top mistakes to avoid", "Negotiation"),
    ("MOa_hXL9Fz8", "50/30/20 vs 70/20/10 budget rule — which is best?", "Budgeting"),
    ("Je1xvK75Ihw", "Payslips, wages and tax codes explained (UK)", "Global pay"),
]

def consent(label="I agree to be contacted about this request and accept the <a href='{root}privacy.html'>privacy policy</a>."):
    return f'<label class="consent"><input type="checkbox" name="consent" value="yes" required> <span>{label}</span></label>'

HP = '<input class="hp" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">'

def home():
    tools = "".join(f'<a class="card tool-card reveal" href="{{root}}calculators/{s}.html"><span class="ico">{i}</span><h3>{t}</h3><p>{d}</p></a>' for s, i, t, d in TOOLS[:8])
    chips = " ".join(f'<a class="btn btn-ghost btn-sm" href="{{root}}salary/{a}-a-year.html">${a:,}</a>' for a in [35000, 40000, 45000, 50000, 55000, 55300, 60000, 65000, 70000, 75000, 80000, 90000, 100000, 120000, 150000])
    vids = "".join(video(v, t) for v, t, _ in VIDEOS[:3])
    fh, fld = faq([
        ("Is 55300 free?", "Yes. Every calculator, table and guide is free with no sign-up. The site is funded by advertising, reader support and clearly labelled sponsorships."),
        ("Are the tax numbers current?", f"Yes. Calculations use the IRS 2026 brackets and standard deduction and the 2026 Social Security wage base. Last reviewed {UPDATED}."),
        ("Do you store what I type?", "No. Calculators run entirely in your browser. Only forms you choose to submit (like the Pay Check-Up) are sent to us."),
        ("Why is the site called 55300?", "$55,300 is a useful benchmark for a typical full-time American salary — and our domain. Read <a href='{root}about.html#why-55300'>why 55300</a>."),
    ])
    body = f'''<section class="hero"><div class="wrap hero-grid">
<div><span class="eyebrow">Free · Private · 2026 tax data</span>
<h1>Every paycheck, <span>decoded.</span></h1>
<p class="lead">Turn any salary into hourly, monthly and real take-home pay in seconds. Then use the numbers to negotiate, budget and plan — with tools that show their math.</p>
<div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:18px"><a class="btn btn-primary" href="{{root}}calculators/take-home-pay.html">Calculate take-home pay</a><a class="btn btn-ghost" href="{{root}}pay-checkup.html">Free Pay Check-Up</a></div>
<div class="trust"><span><b>9</b> calculators</span><span><b>27</b> salary tables</span><span><b>0</b> sign-ups</span><span>🔒 runs in your browser</span></div></div>
<div class="calc" data-calc="quick" data-root="{{root}}"><h3>Quick pay converter</h3>
<div class="row"><div class="field"><label for="q-amt">Amount</label><div class="money"><input id="q-amt" name="amount" inputmode="decimal" value="55300"></div></div>
<div class="field"><label for="q-per">Paid</label><select id="q-per" name="per"><option value="year">per year</option><option value="month">per month</option><option value="biweek">every 2 weeks</option><option value="week">per week</option><option value="hour">per hour</option></select></div></div>
<div class="out" aria-live="polite"></div></div></div></section>

<section class="section"><div class="wrap"><div class="center"><span class="eyebrow">Calculators</span><h2>Answer the money question in front of you</h2><p class="lead">Built after studying more than 25 of the world's leading salary and finance tools — then fixing what they get wrong: stale tax years, hidden formulas and sign-up walls.</p></div>
<div class="grid g4" style="margin-top:28px">{tools}</div><p class="center" style="margin-top:20px"><a href="{{root}}calculators/index.html">All calculators →</a></p></div></section>

<section class="section alt"><div class="wrap grid g2" style="align-items:center">
<div class="reveal"><span class="eyebrow">The 55,300 benchmark</span><h2>What does an ordinary salary really buy?</h2>
<p class="muted">$55,300 sits in the middle of the U.S. pay distribution — close to the Census Bureau's 2015 median household income ($55,775) and about 21% below the BLS May 2025 mean wage for all occupations ($69,770). We use it as a reference point across the site.</p>
<a class="btn btn-primary" href="{{root}}salary/55300-a-year.html">See the full $55,300 breakdown</a></div>
<div class="stats reveal"><div class="stat"><div class="k">Hourly</div><div class="v">$26.59</div></div><div class="stat"><div class="k">Monthly gross</div><div class="v">$4,608</div></div><div class="stat"><div class="k">Take-home / mo*</div><div class="v">$3,884</div></div><div class="stat"><div class="k">Federal avg. rate</div><div class="v">8.1%</div></div><div class="stat"><div class="k">Max rent (28%)</div><div class="v">$1,290</div></div><div class="stat"><div class="k">Save 20%/mo</div><div class="v">$777</div></div>
<p class="small muted" style="grid-column:1/-1;margin:0">*Single filer, 2026, no state tax.</p></div></div></section>

<section class="section"><div class="wrap"><div class="lead-box reveal"><div class="grid g2" style="position:relative;z-index:1;align-items:center">
<div><span class="eyebrow" style="color:#7ef0bd">Free Pay Check-Up</span><h2>Are you being paid what you're worth?</h2><p class="lead">Tell us your situation in 60 seconds. We'll reply with a market range, a take-home plan or a negotiation script — free.</p>
<ul class="checks"><li>Job-offer and counter-offer review</li><li>Raise strategy with real numbers</li><li>Take-home, budget &amp; debt plan</li><li>AI-era career and upskilling plan</li></ul></div>
<form class="card" data-form="lead-quick" data-redirect="{{root}}thank-you.html" style="color:var(--ink)">{HP}
<h3 style="margin-top:0">Start in 60 seconds</h3>
<div class="field"><label for="lq-goal">I want help with</label><select id="lq-goal" name="goal" required><option value="">Choose one…</option><option value="offer">Reviewing a job offer</option><option value="raise">Asking for a raise</option><option value="takehome">Take-home pay &amp; taxes</option><option value="budget">Budget or debt plan</option><option value="career">Career &amp; AI upskilling</option><option value="business">Business / partnership inquiry</option></select></div>
<div class="row"><div class="field"><label for="lq-name">First name</label><input id="lq-name" name="name" required autocomplete="given-name"></div><div class="field"><label for="lq-email">Email</label><input id="lq-email" type="email" name="email" required autocomplete="email"></div></div>
{consent()}<button class="btn btn-primary btn-block" type="submit" style="margin-top:12px">Get my free Check-Up →</button><p class="form-msg" role="status"></p>
<p class="small muted" style="margin:8px 0 0">Reply within 2 business days. No spam, unsubscribe anytime.</p></form></div></div></div></section>

<section class="section alt"><div class="wrap"><span class="eyebrow">Salary tables</span><h2>Popular salaries, fully broken down</h2><div style="display:flex;flex-wrap:wrap;gap:8px;margin-top:16px">{chips}</div></div></section>

<section class="section"><div class="wrap"><div style="display:flex;justify-content:space-between;align-items:end;gap:12px;flex-wrap:wrap"><div><span class="eyebrow">Watch &amp; learn</span><h2>Video explainers</h2></div><a href="{{root}}videos.html">Video library →</a></div>
<div class="grid g3" style="margin-top:16px">{vids}</div></div></section>

<section class="section alt"><div class="wrap"><div class="center"><span class="eyebrow">Community</span><h2>Build the 55300 community with us</h2></div>
<div class="grid g3" style="margin-top:24px">
<a class="card tool-card reveal" href="{{root}}community.html#contests"><span class="ico">🏆</span><h3>Contests &amp; prizes</h3><p>Monthly money challenges with cash and gift-card prizes funded by sponsors and supporters.</p></a>
<a class="card tool-card reveal" href="{{root}}community.html#careers"><span class="ico">🧑‍🤝‍🧑</span><h3>Join the team</h3><p>We hire freelance writers, tax reviewers, developers, video creators and ambassadors.</p></a>
<a class="card tool-card reveal" href="{{root}}support.html"><span class="ico">💚</span><h3>Support the mission</h3><p>Keep calculators free and tax data current. Every contribution funds operations, promotion and prizes.</p></a>
</div></div></section>

<section class="section"><div class="wrap" style="max-width:820px"><h2 class="center">Questions</h2>{fh}</div></section>'''
    write("index.html", "55300 — Salary, Paycheck & Take-Home Pay Calculators (2026)",
          "Free 2026 salary and paycheck calculators: take-home pay, salary to hourly, raises, budgets, job offers, freelance rates, loans and savings. Private, fast, sourced.",
          body, [fld], active="index.html", priority="1.0")

def videos():
    cats = {}
    for v, t, c in VIDEOS:
        cats.setdefault(c, []).append(video(v, t))
    secs = "".join(f'<h2 style="margin-top:32px">{c}</h2><div class="grid g3">{"".join(vs)}</div>' for c, vs in cats.items())
    c, cld = crumbs([("{root}index.html", "Home"), (None, "Videos")])
    body = f'''<section class="hero"><div class="wrap">{c}<span class="eyebrow">Video library</span><h1>Paycheck &amp; money videos</h1><p class="lead">Hand-picked explainers on paychecks, negotiation and budgeting. Videos load only when you press play — faster pages, more privacy.</p></div></section>
<section class="section"><div class="wrap">{secs}
<div class="card" style="margin-top:32px"><h3>Make videos with us</h3><p class="muted">Are you a finance creator? We commission short explainers and feature creators who teach money clearly. <a href="{{root}}community.html#careers">Apply as a video creator</a> or <a href="{{root}}advertise.html">sponsor a series</a>.</p></div>
<p class="small muted" style="margin-top:20px">Videos are embedded from YouTube and remain the property of their creators. Inclusion is not endorsement; 55300 is not affiliated with these channels.</p></div></section>'''
    write("videos.html", "Paycheck, Salary & Budget Video Explainers | 55300", "Curated video explainers on reading a pay stub, gross vs net pay, salary negotiation and budgeting rules.", body, [cld], priority="0.6")

def checkup():
    c, cld = crumbs([("{root}index.html", "Home"), (None, "Free Pay Check-Up")])
    goals = [("offer", "📝 Review a job offer"), ("raise", "📈 Ask for a raise"), ("takehome", "💵 Take-home & taxes"), ("budget", "🧮 Budget plan"), ("debt", "🏦 Debt payoff plan"), ("savings", "🎯 Savings & retirement"), ("freelance", "🧑‍💻 Freelance pricing"), ("career", "🤖 Career & AI upskilling"), ("employer", "🏢 I'm an employer / HR"), ("business", "🤝 Partnership / business")]
    gh = "".join(f'<label><input type="radio" name="goal" value="{v}" required> {t}</label>' for v, t in goals)
    body = f'''<section class="hero"><div class="wrap">{c}<div class="grid g2" style="align-items:start">
<div><span class="eyebrow">Free · 2 business days · No obligation</span><h1>Your free Pay Check-Up</h1>
<p class="lead">Answer a few questions and get a personalised reply: a fair-pay range, an offer or raise strategy, or a take-home and budget plan built around your real numbers.</p>
<ul class="checks" style="color:var(--ink)"><li>Written by a person, using the same 2026 data behind our calculators</li><li>Specific numbers and a script you can use this week</li><li>Optional follow-up call if you want one</li><li>Your details are never sold</li></ul>
<div class="card" style="margin-top:20px"><h3>What happens next</h3><ol class="small" style="padding-left:1.2em;margin:0"><li>You submit the form (about 60 seconds).</li><li>We review your situation and run the numbers.</li><li>You get a reply by email within 2 business days.</li><li>If it helps, we connect you with vetted partners — only with your permission.</li></ol></div>
<p class="small muted" style="margin-top:14px">Not tax, legal or investment advice. For regulated advice we refer you to licensed professionals.</p></div>
<form class="calc" data-form="pay-checkup" data-steps data-redirect="{{root}}thank-you.html" aria-label="Pay Check-Up form">{HP}
<div class="steps" aria-hidden="true"><span></span><span></span><span></span></div>
<div class="step"><h3>1. What can we help with?</h3><div class="choice">{gh}</div><button class="btn btn-primary btn-block" data-next>Continue →</button></div>
<div class="step"><h3>2. Your situation</h3>
<div class="row"><div class="field"><label for="income">Annual income (approx.)</label><input id="income" name="income" inputmode="decimal" placeholder="e.g. 55300"></div>
<div class="field"><label for="timeline">Timeline</label><select id="timeline" name="timeline"><option>This week</option><option>This month</option><option>Next 3 months</option><option>Just exploring</option></select></div></div>
<div class="row"><div class="field"><label for="role">Role / industry</label><input id="role" name="role" placeholder="e.g. Registered nurse, Marketing"></div><div class="field"><label for="location">City / region</label><input id="location" name="location" placeholder="e.g. Austin, TX"></div></div>
<div class="field"><label for="details">Anything we should know?</label><textarea id="details" name="details" rows="3" placeholder="Offer details, current pay, goals…"></textarea></div>
<input type="hidden" name="topic" value="">
<div class="row"><button class="btn btn-ghost" data-prev>← Back</button><button class="btn btn-primary" data-next>Continue →</button></div></div>
<div class="step"><h3>3. Where should we send it?</h3>
<div class="row"><div class="field"><label for="name">Full name</label><input id="name" name="name" required autocomplete="name"></div><div class="field"><label for="email">Email</label><input id="email" type="email" name="email" required autocomplete="email"></div></div>
<div class="row"><div class="field"><label for="phone">Phone (optional)</label><input id="phone" type="tel" name="phone" autocomplete="tel"></div><div class="field"><label for="pref">Preferred contact</label><select id="pref" name="preferred_contact"><option>Email</option><option>Phone call</option><option>WhatsApp</option></select></div></div>
<label class="consent" style="margin-bottom:8px"><input type="checkbox" name="partner_optin" value="yes"> <span>You may introduce me to vetted partners (advisors, tax pros, recruiters) relevant to my request.</span></label>
{consent()}
<div class="row" style="margin-top:12px"><button class="btn btn-ghost" data-prev>← Back</button><button class="btn btn-primary" type="submit">Send my Check-Up →</button></div><p class="form-msg" role="status"></p></div>
</form></div></div></section>'''
    write("pay-checkup.html", "Free Pay Check-Up: Offer Review, Raise Strategy & Take-Home Plan | 55300", "Get a free, personalised pay review: job offer and raise strategy, take-home pay, budget and debt plan, or an AI-era career plan. Reply in 2 business days.", body, [cld], priority="0.9")

    body = '''<section class="section"><div class="wrap center" style="max-width:720px"><span class="eyebrow">Received ✓</span><h1>Thank you — we've got it.</h1>
<p class="lead">Your request is in our queue. Expect a personal reply within 2 business days. Check your spam folder if you don't see it.</p>
<div class="grid g3" style="margin-top:28px;text-align:left"><a class="card tool-card" href="{root}calculators/take-home-pay.html"><span class="ico">💵</span><h3>Run your take-home</h3><p>Have your exact numbers ready.</p></a><a class="card tool-card" href="{root}guides/how-to-negotiate-a-raise.html"><span class="ico">📈</span><h3>Read the raise playbook</h3><p>Prepare while you wait.</p></a><a class="card tool-card" href="{root}support.html"><span class="ico">💚</span><h3>Support 55300</h3><p>Keep this service free for everyone.</p></a></div></div></section>'''
    write("thank-you.html", "Thank You | 55300", "Your submission was received.", body, noindex=True)

def support():
    c, cld = crumbs([("{root}index.html", "Home"), (None, "Support 55300")])
    tiers = "".join(f'<div class="tier{" on" if a == 55 else ""}" data-amt="{a}" role="button" tabindex="0"><div class="amt">${a}</div><div class="small muted">{l}</div></div>' for a, l in [(5, "Coffee for the team"), (15, "Funds one tax-data check"), (55, "Sponsors a contest prize"), (300, "Funds a new calculator")])
    alloc = [("Operations & hosting", 35, "#2f6fde"), ("Tax data & new tools", 25, "#0fb877"), ("Promotion & marketing", 15, "#f5a524"), ("Hiring talent", 15, "#8b5cf6"), ("Contests & prizes", 10, "#e64980")]
    bar = '<div class="bar" style="height:20px">' + "".join(f'<span style="width:{p}%;background:{col}"></span>' for _, p, col in alloc) + '</div><div class="legend">' + "".join(f'<span><i style="background:{col}"></i>{n} {p}%</span>' for n, p, col in alloc) + "</div>"
    fh, fld = faq([
        ("Is my donation tax-deductible?", "No. 55300 is an independent website, not a registered charity, so contributions are not tax-deductible."),
        ("How do I pay?", "Use any payment button shown. If a button says 'pledge', submit the pledge form and we'll reply with a secure payment link — we never ask for card details by email or form."),
        ("Can I give monthly?", "Yes — choose 'Monthly' in the pledge form and we'll set up a recurring link you can cancel anytime."),
        ("Can my company sponsor instead?", "Yes. Sponsorships include visible, clearly-labelled recognition. See <a href='{root}advertise.html'>Advertise &amp; sponsor</a>."),
    ])
    body = f'''<section class="hero"><div class="wrap">{c}<div class="grid g2" style="align-items:start">
<div><span class="eyebrow">Reader-supported</span><h1>Keep 55300 free, accurate and independent</h1>
<p class="lead">No paywalls, no sign-up walls, no sold data. Your support pays for servers, yearly tax-data updates, new calculators, promotion, the people who build them and prizes for our community contests.</p>
<div data-goal style="margin:20px 0"></div><h3>Where your money goes</h3>{bar}</div>
<div class="calc"><h3>Choose an amount</h3><div class="tiers" data-tiers>{tiers}</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:16px">
<a class="btn btn-primary" data-pay="paypal" href="#pledge">PayPal</a><a class="btn btn-primary" data-pay="stripe" href="#pledge">Card (Stripe)</a>
<a class="btn btn-accent" data-pay="buymeacoffee" href="#pledge">Buy Me a Coffee</a><a class="btn btn-ghost" data-pay="kofi" href="#pledge">Ko-fi</a></div>
<p class="small muted" style="margin-top:10px">Secure checkout is handled by the payment provider. We never see or store card numbers.</p></div></div></div></section>
<section class="section alt" id="pledge"><div class="wrap grid g2" style="align-items:start">
<div><h2>Pledge or give monthly</h2><p class="muted">Prefer a bank transfer, a monthly gift, or giving on behalf of a company? Send a pledge and we'll reply with a secure link and a receipt.</p>
<h3>Supporter perks</h3><ul class="checks"><li>Name on the Supporters wall (optional)</li><li>Early access to new calculators</li><li>Vote on the next tool we build</li><li>$300+: credit on a calculator page</li></ul></div>
<form class="card" data-form="donation-pledge" data-ok="Thank you! We'll email your secure payment link and receipt shortly.">{HP}
<div class="row"><div class="field"><label for="amount">Amount (USD)</label><input id="amount" name="amount" type="number" min="1" value="55" required></div>
<div class="field"><label for="freq">Frequency</label><select id="freq" name="frequency"><option>One-time</option><option>Monthly</option><option>Yearly</option></select></div></div>
<div class="field"><label for="purpose">Direct it to (optional)</label><select id="purpose" name="purpose"><option>Where it's needed most</option><option>Operations &amp; hosting</option><option>New calculators</option><option>Promotion &amp; marketing</option><option>Hiring talent</option><option>Contests &amp; prizes</option></select></div>
<div class="row"><div class="field"><label for="d-name">Name</label><input id="d-name" name="name" required></div><div class="field"><label for="d-email">Email</label><input id="d-email" type="email" name="email" required></div></div>
<div class="field"><label for="d-msg">Message (optional)</label><textarea id="d-msg" name="message" rows="2"></textarea></div>
<label class="consent" style="margin-bottom:8px"><input type="checkbox" name="public_credit" value="yes"> <span>List my name on the Supporters wall.</span></label>
{consent()}<button class="btn btn-primary btn-block" type="submit" style="margin-top:12px">Send pledge</button><p class="form-msg" role="status"></p></form></div></section>
<section class="section"><div class="wrap" style="max-width:820px"><h2>Support FAQ</h2>{fh}</div></section>'''
    write("support.html", "Support 55300 — Donate to Keep Free Pay Calculators Running", "Support free, independent salary and paycheck calculators. Donations fund operations, tax-data updates, promotion, hiring and community contest prizes.", body, [cld, fld], active="support.html", priority="0.6")

def community():
    c, cld = crumbs([("{root}index.html", "Home"), (None, "Community")])
    contests = [("🏆", "Budget Builder Challenge", "Share a one-page 50/30/20 plan built with our planner. Judged on clarity, realism and creativity.", "$300 + 2 × $100", "Monthly"),
                ("📈", "Best Raise Story", "Tell us how you negotiated a raise or offer using real numbers. Winners featured (anonymously if preferred).", "$250", "Quarterly"),
                ("💡", "Calculator Idea Prize", "Pitch the money tool you wish existed. The best idea gets built and credited to you.", "$200 + credit", "Rolling")]
    ch = "".join(f'<div class="card reveal"><div style="font-size:1.8rem">{i}</div><h3>{t}</h3><p class="muted">{d}</p><p><span class="tag">Prize: {p}</span> <span class="tag">{f}</span></p></div>' for i, t, d, p, f in contests)
    roles = [("Freelance personal-finance writer", "Remote · Per article", "Plain-English money writing with sourced numbers."),
             ("Tax reviewer (CPA / EA)", "Remote · Per review", "Annual review of calculator logic and guide accuracy."),
             ("Front-end developer", "Remote · Contract", "Vanilla JS, accessibility, performance; build new calculators."),
             ("Video creator / editor", "Remote · Per video", "Short explainers for YouTube and Shorts."),
             ("Growth & SEO marketer", "Remote · Part-time", "Content strategy, partnerships, newsletter growth."),
             ("Campus & community ambassador", "Anywhere · Commission", "Bring 55300 to your school, union or community group.")]
    rh = "".join(f'<tr><td><b>{t}</b><div class="small muted">{d}</div></td><td>{m}</td></tr>' for t, m, d in roles)
    ropts = "".join(f"<option>{t}</option>" for t, _, _ in roles)
    body = f'''<section class="hero"><div class="wrap">{c}<span class="eyebrow">Community</span><h1>Contests, careers &amp; promotions</h1><p class="lead">Win prizes for smart money moves, build tools with us, or help spread financial clarity — and get paid for it.</p>
<div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn btn-primary" href="#contests">Enter a contest</a><a class="btn btn-ghost" href="#careers">See open roles</a><a class="btn btn-ghost" href="#promote">Promote 55300</a></div></div></section>
<section class="section" id="contests"><div class="wrap"><h2>Current contests</h2><div class="grid g3">{ch}</div>
<div class="grid g2" style="margin-top:28px;align-items:start">
<form class="calc" data-form="contest-entry" data-ok="Entry received — good luck! Winners are announced on this page and by email.">{HP}<h3>Submit an entry</h3>
<div class="field"><label for="contest">Contest</label><select id="contest" name="contest" required>{"".join(f"<option>{t}</option>" for _, t, *_ in contests)}</select></div>
<div class="row"><div class="field"><label for="c-name">Name</label><input id="c-name" name="name" required></div><div class="field"><label for="c-email">Email</label><input id="c-email" type="email" name="email" required></div></div>
<div class="field"><label for="c-link">Link to your entry (Google Doc, image, video)</label><input id="c-link" type="url" name="entry_link" placeholder="https://"></div>
<div class="field"><label for="c-text">Or describe it here</label><textarea id="c-text" name="entry_text" rows="4"></textarea></div>
<label class="consent" style="margin-bottom:8px"><input type="checkbox" name="age_confirm" value="18+" required> <span>I am 18 or older and accept the official rules below.</span></label>
{consent()}<button class="btn btn-primary btn-block" type="submit" style="margin-top:12px">Submit entry</button><p class="form-msg" role="status"></p></form>
<div class="card"><h3>Official rules (summary)</h3><ul class="small"><li><b>No purchase or donation necessary</b> to enter or win. A donation does not improve your chances.</li><li>Open to individuals 18+ where permitted by law; void where prohibited.</li><li>Skill-based: winners are chosen by a judging panel on the published criteria — not by random draw.</li><li>One entry per person per contest period. Entries must be your original work.</li><li>By entering you grant 55300 a non-exclusive licence to feature your entry with credit (or anonymously on request).</li><li>Prizes are paid electronically within 30 days of announcement; winners are responsible for any taxes.</li><li>Prize amounts are funded by sponsors and supporters and are stated per period on this page.</li></ul><p class="small muted">Want to fund a prize? <a href="{{root}}advertise.html">Sponsor a contest</a>.</p></div></div></div></section>
<section class="section alt" id="careers"><div class="wrap"><h2>Careers &amp; talent</h2><p class="lead">We're a remote-first team. Paid, flexible projects for people who can make money clearer.</p>
<div class="grid g2" style="align-items:start;margin-top:20px"><div class="table-wrap"><table><thead><tr><th>Role</th><th>Type</th></tr></thead><tbody>{rh}</tbody></table></div>
<form class="calc" data-form="job-application" data-ok="Application received. If there's a fit we'll reach out within 10 business days.">{HP}<h3>Apply or join the talent pool</h3>
<div class="field"><label for="j-role">Role</label><select id="j-role" name="role" required>{ropts}<option>Other / talent pool</option></select></div>
<div class="row"><div class="field"><label for="j-name">Full name</label><input id="j-name" name="name" required></div><div class="field"><label for="j-email">Email</label><input id="j-email" type="email" name="email" required></div></div>
<div class="row"><div class="field"><label for="j-port">Portfolio / LinkedIn</label><input id="j-port" type="url" name="portfolio" placeholder="https://"></div><div class="field"><label for="j-rate">Rate / availability</label><input id="j-rate" name="rate" placeholder="e.g. $60/h, 10 h/week"></div></div>
<div class="field"><label for="j-why">Why you?</label><textarea id="j-why" name="message" rows="3" required></textarea></div>
{consent()}<button class="btn btn-primary btn-block" type="submit" style="margin-top:12px">Send application</button><p class="form-msg" role="status"></p></form></div></div></section>
<section class="section" id="promote"><div class="wrap grid g2" style="align-items:center"><div><h2>Promote 55300 — ambassadors &amp; partners</h2><p class="muted">Teachers, HR teams, unions, credit unions, creators and student groups: share our free calculators with your audience. Ambassadors get co-branded resources, early tool access and paid referral opportunities for sponsor introductions.</p>
<ul class="checks"><li>Free embeddable calculators for your site</li><li>Workshop slides on paychecks &amp; budgeting</li><li>Co-branded contest for your community</li></ul></div>
<form class="calc" data-form="ambassador" data-ok="Thanks! We'll send your ambassador kit soon.">{HP}<h3>Become an ambassador</h3>
<div class="row"><div class="field"><label for="a-name">Name</label><input id="a-name" name="name" required></div><div class="field"><label for="a-email">Email</label><input id="a-email" type="email" name="email" required></div></div>
<div class="row"><div class="field"><label for="a-org">Organisation / channel</label><input id="a-org" name="organisation"></div><div class="field"><label for="a-size">Audience size</label><select id="a-size" name="audience"><option>&lt; 1,000</option><option>1,000 – 10,000</option><option>10,000 – 100,000</option><option>100,000+</option></select></div></div>
{consent()}<button class="btn btn-primary btn-block" type="submit" style="margin-top:12px">Get the ambassador kit</button><p class="form-msg" role="status"></p></form></div></section>'''
    write("community.html", "Community: Money Contests, Careers & Ambassadors | 55300", "Enter monthly money contests with cash prizes, apply for paid remote roles, or become a 55300 ambassador.", body, [cld], active="community.html", priority="0.6")

def advertise():
    c, cld = crumbs([("{root}index.html", "Home"), (None, "Advertise & sponsor")])
    pk = [("Calculator sponsor", "Your brand on one calculator page: logo, short message and link, labelled “Sponsored”.", "Monthly"),
          ("Guide sponsorship", "Sponsor an evergreen guide. Editorial stays independent; sponsorship is disclosed.", "Quarterly"),
          ("Newsletter feature", "A clearly labelled sponsor slot in our tax-change alert email.", "Per send"),
          ("Contest prize sponsor", "Fund a contest prize and get recognition across the contest page and announcement.", "Per contest"),
          ("Lead partnership", "Receive opt-in Pay Check-Up referrals in your category (advisors, tax prep, recruiting, lending).", "Per qualified lead"),
          ("Acquire / partner on 55300.com", "Interested in the website or the domain itself, or a strategic partnership?", "Let's talk")]
    ph = "".join(f'<div class="card reveal"><h3>{t}</h3><p class="muted">{d}</p><span class="tag">{f}</span></div>' for t, d, f in pk)
    body = f'''<section class="hero"><div class="wrap">{c}<span class="eyebrow">Advertise · Sponsor · Partner</span><h1>Reach people at the exact moment they think about money</h1>
<p class="lead">Our visitors are actively calculating salaries, comparing job offers, planning budgets and taking on loans. Sponsorships are clearly labelled and never change our numbers.</p>
<a class="btn btn-primary" href="https://web.works/contact" target="_blank" rel="noopener">Contact about website / domain / sponsorship</a></div></section>
<section class="section"><div class="wrap"><h2>Packages</h2><div class="grid g3">{ph}</div>
<div class="grid g2" style="margin-top:28px;align-items:start"><div class="card"><h3>Our standards</h3><ul class="small"><li>All paid placements are labelled “Sponsored” or “Partner”.</li><li>Sponsors never influence calculator results, rankings or editorial conclusions.</li><li>We don't accept payday-loan, crypto-pump, gambling or misleading offers.</li><li>Google AdSense placements follow Google Publisher Policies.</li></ul></div>
<form class="calc" data-form="sponsorship-inquiry" data-ok="Thanks — we'll send the media kit and availability within 2 business days.">{HP}<h3>Request the media kit</h3>
<div class="row"><div class="field"><label for="s-name">Name</label><input id="s-name" name="name" required></div><div class="field"><label for="s-email">Work email</label><input id="s-email" type="email" name="email" required></div></div>
<div class="row"><div class="field"><label for="s-co">Company</label><input id="s-co" name="company" required></div><div class="field"><label for="s-pk">Interested in</label><select id="s-pk" name="package">{"".join(f"<option>{t}</option>" for t, *_ in pk)}</select></div></div>
<div class="row"><div class="field"><label for="s-bud">Budget</label><select id="s-bud" name="budget"><option>&lt; $500</option><option>$500 – $2,000</option><option>$2,000 – $10,000</option><option>$10,000+</option></select></div><div class="field"><label for="s-start">Start</label><input id="s-start" name="start" placeholder="e.g. January 2027"></div></div>
<div class="field"><label for="s-msg">Goals</label><textarea id="s-msg" name="message" rows="3"></textarea></div>
{consent()}<button class="btn btn-primary btn-block" type="submit" style="margin-top:12px">Send inquiry</button><p class="form-msg" role="status"></p></form></div></div></section>'''
    write("advertise.html", "Advertise, Sponsor or Partner with 55300", "Sponsorship, advertising, lead-partnership and acquisition opportunities with 55300.com — a free salary and paycheck calculator site.", body, [cld], priority="0.5")

def embed():
    c, cld = crumbs([("{root}index.html", "Home"), (None, "Embed calculators")])
    code = '&lt;iframe src="https://55300.com/calculators/take-home-pay.html" width="100%" height="900" style="border:0;border-radius:16px" title="Take-home pay calculator by 55300" loading="lazy"&gt;&lt;/iframe&gt;\n&lt;p&gt;Calculator by &lt;a href="https://55300.com/"&gt;55300.com&lt;/a&gt;&lt;/p&gt;'
    body = f'''<section class="hero"><div class="wrap">{c}<span class="eyebrow">Free for websites, schools &amp; HR teams</span><h1>Embed our calculators</h1><p class="lead">Add an accurate, always-updated pay calculator to your site in one line. Free — please keep the credit link.</p></div></section>
<section class="section"><div class="wrap" style="max-width:860px"><h2>Copy this code</h2><pre class="card" style="overflow:auto;font-size:.85rem;white-space:pre-wrap">{code}</pre>
<p class="muted">Swap the file name for any calculator: take-home-pay, salary-to-hourly, raise, budget, job-offer-compare, freelance-rate, loan, savings-goal.</p>
<form class="calc" data-form="embed-request" data-ok="Thanks! We'll send custom embed options shortly.">{HP}<h3>Need a branded or custom version?</h3>
<div class="row"><div class="field"><label for="e-name">Name</label><input id="e-name" name="name" required></div><div class="field"><label for="e-email">Email</label><input id="e-email" type="email" name="email" required></div></div>
<div class="field"><label for="e-site">Your website</label><input id="e-site" name="website" type="url" placeholder="https://"></div>{consent()}
<button class="btn btn-primary" type="submit" style="margin-top:12px">Request custom embed</button><p class="form-msg" role="status"></p></form></div></section>'''
    write("embed.html", "Embed Free Salary & Paycheck Calculators | 55300", "Embed free, accurate take-home pay and salary calculators on your website with one line of code.", body, [cld], priority="0.4")

def about():
    c, cld = crumbs([("{root}index.html", "Home"), (None, "About")])
    body = f'''<section class="section"><div class="wrap layout"><article class="article">{c}<span class="eyebrow">About</span><h1>About 55300</h1>
<p class="lead">55300 is an independent, free toolkit for understanding pay: what a salary is worth per hour, what reaches your bank account, and how to use those numbers to negotiate, budget and plan.</p>
<h2>Our mission</h2><p>Most people make their biggest money decisions — accepting a job, asking for a raise, signing a loan — with fuzzy numbers. We make the numbers clear, current and private, and we show the math so you can trust it.</p>
<h2 id="why-55300">Why “55300”?</h2><p>We researched what the number means across commerce, the economy and people's lives before building anything:</p>
<ul><li><b>As money:</b> $55,300 is a realistic “middle” salary — close to the U.S. Census Bureau's 2015 median household income of $55,775 and inside the middle-income band, while about 21% below the BLS May 2025 mean annual wage for all occupations ($69,770). That makes it a natural benchmark for a site about ordinary paychecks.</li>
<li><b>As a place:</b> 55300 is the French postal code for Saint-Mihiel and about 30 surrounding communes in the Meuse department — a reminder that the same five digits mean different things around the world.</li>
<li><b>As a pattern:</b> “55 · 3 · 00” is short, numeric and language-neutral — easy to remember and to type in any country, which suits a global, calculator-first brand.</li></ul>
<p>We chose the money meaning. The number is used purely as our domain name; we have no connection to any town, agency or business that uses the same digits.</p>
<h2>Editorial standards</h2><ul><li>Every tax figure is dated and linked to an official source (IRS, SSA, BLS, Census).</li><li>Formulas are shown on every calculator page.</li><li>Content is reviewed at least once a year and whenever tax law changes.</li><li>Corrections are welcome — <a href="{{root}}contact.html?topic=correction">report one</a>.</li></ul>
<h2>How we make money</h2><p>Display advertising (Google AdSense), reader support, clearly labelled sponsorships and opt-in partner referrals from the Pay Check-Up. None of these change calculator results or editorial conclusions. See <a href="{{root}}advertise.html">our standards</a>.</p>
<h2>Contact</h2><p>Questions, partnerships or press: use our <a href="{{root}}contact.html">contact form</a>. Interested in this website or domain? <a href="https://web.works/contact" target="_blank" rel="noopener">Contact us here</a>.</p></article>
<aside class="sidebar"><div class="card"><h3>At a glance</h3><ul class="small"><li>9 calculators</li><li>27 salary tables</li><li>6 in-depth guides</li><li>Tax year 2026</li><li>Updated {UPDATED}</li></ul></div></aside></div></section>'''
    write("about.html", "About 55300 — Why We Built Free Pay Calculators", "About 55300: mission, why the number 55300, editorial standards and how the site is funded.", body, [cld], priority="0.5")

def contact():
    c, cld = crumbs([("{root}index.html", "Home"), (None, "Contact")])
    body = f'''<section class="section"><div class="wrap grid g2" style="align-items:start"><div>{c}<span class="eyebrow">Contact</span><h1>Get in touch</h1>
<p class="lead">Questions, corrections, partnerships, press or feedback — we read everything and reply within 2 business days.</p>
<div class="card" style="margin-top:16px"><h3>Fast routes</h3><ul class="small" style="padding-left:1.1em"><li>Personal pay question → <a href="{{root}}pay-checkup.html">Free Pay Check-Up</a></li><li>Sponsorship / advertising → <a href="{{root}}advertise.html">Media kit</a></li><li>Website, domain or partnership interest → <a href="https://web.works/contact" target="_blank" rel="noopener">web.works/contact</a></li><li>Prefer your own email app? <a href="#" data-mail="Inquiry from 55300.com">Email us</a></li></ul></div></div>
<form class="calc" data-form="contact" data-ok="Message sent — we'll reply within 2 business days.">{HP}
<div class="field"><label for="topic">Topic</label><select id="topic" name="topic"><option value="general">General question</option><option value="correction">Report a correction</option><option value="feedback">Feedback / feature idea</option><option value="partnership">Partnership</option><option value="press">Press</option><option value="domain">Website / domain purchase</option></select></div>
<div class="row"><div class="field"><label for="ct-name">Name</label><input id="ct-name" name="name" required></div><div class="field"><label for="ct-email">Email</label><input id="ct-email" type="email" name="email" required></div></div>
<div class="field"><label for="ct-msg">Message</label><textarea id="ct-msg" name="message" rows="6" required></textarea></div>
{consent()}<button class="btn btn-primary btn-block" type="submit" style="margin-top:12px">Send message</button><p class="form-msg" role="status"></p></form></div></section>'''
    write("contact.html", "Contact 55300", "Contact the 55300 team about questions, corrections, partnerships, sponsorship or press.", body, [cld], priority="0.4")

def legal_pages():
    def simple(path, title, desc, html_):
        c, cld = crumbs([("{root}index.html", "Home"), (None, title)])
        write(path, f"{title} | 55300", desc, f'<section class="section"><div class="wrap"><article class="article">{c}<h1>{title}</h1><p class="muted">Last updated {UPDATED}</p>{html_}</article></div></section>', [cld], priority="0.3")

    simple("privacy.html", "Privacy & Cookie Policy", "How 55300 handles data, cookies and advertising.", '''
<h2>Summary</h2><p>Calculators run in your browser; what you type into them is not sent to us. We only receive information you choose to submit through a form. We do not sell personal information.</p>
<h2>Information we collect</h2><ul><li><b>Forms</b> (Pay Check-Up, contact, pledges, contest entries, applications, newsletter): the details you enter. Submissions are delivered to our inbox through the FormSubmit form-processing service.</li><li><b>Usage data</b>: standard server logs from our host (GitHub Pages) and advertising partners, such as IP address, browser type and pages viewed.</li><li><b>Local storage</b>: your theme and cookie choice are saved in your own browser.</li></ul>
<h2 id="cookies">Cookies and advertising</h2><p>We use Google AdSense to show ads. Third-party vendors, including Google, use cookies to serve ads based on a user's prior visits to this website or other websites. Google's use of advertising cookies enables it and its partners to serve ads to you based on your visit to this site and/or other sites on the Internet.</p><p>You may opt out of personalised advertising by visiting <a href="https://www.google.com/settings/ads" target="_blank" rel="noopener">Google Ads Settings</a>, or opt out of some third-party vendors' use of cookies at <a href="https://www.aboutads.info/choices/" target="_blank" rel="noopener">aboutads.info</a>. Learn <a href="https://policies.google.com/technologies/partner-sites" target="_blank" rel="noopener">how Google uses information from sites that use its services</a>.</p><p>Visitors in the EEA, UK and Switzerland are shown a consent message through a Google-certified consent management platform before personalised ads are served.</p>
<h2>Embedded content</h2><p>Videos are embedded from YouTube (privacy-enhanced mode) and only load after you press play. YouTube's own privacy policy then applies.</p>
<h2>How we use information</h2><p>To answer your request, send emails you asked for, run contests, consider applications, prevent abuse and improve the site. With your explicit opt-in only, we may introduce you to a relevant partner.</p>
<h2>Retention</h2><p>Form submissions are kept for up to 24 months unless you ask us to delete them sooner.</p>
<h2>Your rights</h2><p>Depending on where you live (e.g., GDPR, UK GDPR, CCPA/CPRA, PIPEDA), you may request access, correction, deletion or portability of your data and object to processing. Use our <a href="contact.html">contact form</a>.</p>
<h2>Children</h2><p>This site is intended for adults. We do not knowingly collect information from children under 13 (or 16 in the EEA). Contests are open to adults 18+.</p>''')

    simple("terms.html", "Terms of Use", "Terms governing use of 55300.com.", '''
<h2>Acceptance</h2><p>By using 55300.com you agree to these terms. If you do not agree, please do not use the site.</p>
<h2>Educational use only</h2><p>Calculators, tables and guides provide estimates for general education. They are not tax, legal, accounting or investment advice and may not reflect your individual circumstances. Verify important decisions with a qualified professional.</p>
<h2>Accuracy</h2><p>We work to keep figures current but do not guarantee completeness or accuracy. Tax laws change; results may differ from your actual withholding or tax liability.</p>
<h2>Acceptable use</h2><p>Do not misuse the site, attempt to disrupt it, scrape it at volume, or submit unlawful, false or harmful content through forms.</p>
<h2>Contests</h2><p>Contests are governed by the official rules on the <a href="community.html#contests">Community page</a>. No purchase or donation is necessary.</p>
<h2>Donations</h2><p>Contributions support the website's operations; they are voluntary, generally non-refundable and not tax-deductible.</p>
<h2>Intellectual property</h2><p>Site content and code are owned by 55300.com unless stated otherwise. See the <a href="legal.html">trademark &amp; copyright disclosure</a>.</p>
<h2>Third-party links</h2><p>We are not responsible for the content or practices of external sites, including payment providers and YouTube.</p>
<h2>Limitation of liability</h2><p>To the maximum extent permitted by law, 55300.com is not liable for any loss arising from use of the site or reliance on its content.</p>
<h2>Changes</h2><p>We may update these terms; the date above shows the latest version.</p>''')

    simple("disclaimer.html", "Disclaimer", "Financial, tax and advertising disclaimer.", '''
<p>The information on 55300.com is provided for general educational purposes only and does not constitute financial, investment, tax, legal or professional advice. We are not a financial institution, broker, registered investment adviser, CPA firm or law firm.</p>
<p>Calculator outputs are estimates based on stated assumptions (for example, 2026 U.S. federal tax brackets, the standard deduction and FICA rates). Actual paychecks depend on your W-4, employer payroll practices, state and local rules, credits and deductions.</p>
<p><b>Advertising disclosure:</b> 55300.com displays ads served by Google AdSense and may feature clearly labelled sponsors or partners. We may receive compensation when you opt in to partner introductions. This never affects calculator results.</p>
<p><b>External content:</b> embedded videos and linked resources are created by third parties; inclusion is not endorsement.</p>''')

    simple("legal.html", "Trademark & Copyright Disclosure", "Trademark and copyright disclosure for 55300.com.", '''
<h2>About the name “55300”</h2><p>“55300” is a number. It is used on this website solely as a descriptive, numeric domain name and site identifier. 55300.com does not claim exclusive trademark rights in the number 55300 and does not use it to suggest any affiliation, sponsorship or endorsement.</p>
<h2>No affiliation</h2><p>55300.com is independent and is <b>not affiliated with, endorsed by or connected to</b> any postal authority (including La Poste or the communes sharing postal code 55300 such as Saint-Mihiel), any government agency (including the IRS, SSA, BLS or U.S. Census Bureau), any employer, product, model number, part number, tariff code, telephone number or brand that uses the same digits. Any such references are factual and for identification or education only.</p>
<h2>Third-party marks</h2><p>Names such as Google, AdSense, YouTube, PayPal, Stripe, Buy Me a Coffee and Ko-fi are trademarks of their respective owners and are used only to identify services. Their use does not imply endorsement.</p>
<h2>Copyright</h2><p>© 2026 55300.com. The text, calculators, code, data tables, design and graphics on this site are original works of 55300.com unless otherwise stated, and are protected by copyright. You may link to any page and embed our calculators with the provided embed code and credit link. Do not republish substantial portions of content without written permission.</p><p>Government data cited (IRS, SSA, BLS, Census) is in the public domain and is credited to its source. Embedded YouTube videos remain the property of their creators.</p>
<h2>Copyright complaints</h2><p>If you believe content on this site infringes your rights, please send a notice through our <a href="contact.html">contact form</a> identifying the work, the location on our site, your contact details and a good-faith statement. We respond promptly and remove infringing material where appropriate.</p>''')

    simple("methodology.html", "Methodology & Sources", "How 55300 calculates take-home pay, salary conversions and budgets, with official sources.", '''
<h2>Federal income tax (2026)</h2><p>Progressive brackets and standard deductions published by the IRS for tax year 2026: standard deduction $16,100 (single), $32,200 (married filing jointly), $24,150 (head of household). Brackets: 10%, 12%, 22%, 24%, 32%, 35% and 37% with thresholds shown on the <a href="calculators/take-home-pay.html">take-home calculator</a>. Source: <a href="https://www.irs.gov/" target="_blank" rel="noopener">IRS</a> inflation adjustments for tax year 2026.</p>
<h2>FICA</h2><p>Social Security 6.2% employee share on wages up to $184,500 (2026 wage base, <a href="https://www.ssa.gov/" target="_blank" rel="noopener">SSA</a>); Medicare 1.45% on all wages plus Additional Medicare Tax of 0.9% above $200,000 (single) / $250,000 (MFJ). Self-employment tax: 15.3% on 92.35% of net earnings.</p>
<h2>Retirement and HSA limits (2026)</h2><p>401(k) employee deferral $24,500 (+$8,000 catch-up at 50+); IRA $7,500 (+$1,100); HSA $4,400 self-only / $8,750 family.</p>
<h2>Wage benchmarks</h2><p>Mean annual wage for all occupations $69,770 — <a href="https://www.bls.gov/oes/" target="_blank" rel="noopener">BLS Occupational Employment and Wage Statistics</a>, May 2025. U.S. median household income $55,775 (2015) — <a href="https://www.census.gov/" target="_blank" rel="noopener">U.S. Census Bureau</a>, American Community Survey.</p>
<h2>Simplifications</h2><ul><li>Annual tax liability is estimated; payroll withholding can differ.</li><li>State and local tax is applied as a single flat rate you choose.</li><li>Credits (e.g., Child Tax Credit, EITC) and itemized deductions are not modelled.</li><li>2,080 hours per year is used for hourly conversions unless you change it.</li></ul>
<h2>Review cycle</h2><p>Figures are reviewed every October–January when new-year limits are announced, and whenever tax law changes. Spotted an error? <a href="contact.html?topic=correction">Tell us</a>.</p>''')

def build():
    home(); videos(); checkup(); support(); community(); advertise(); embed(); about(); contact(); legal_pages()
