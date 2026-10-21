/* 55300.com — calculator engine. Tax year 2026 (US federal). Rates verified Oct 2026:
   IRS 2026 brackets & standard deduction (Rev. Proc. 2025-32), SSA 2026 wage base $184,500. */
(function(){
  "use strict";
  var TAX = {
    year: 2026,
    std: {single:16100, mfj:32200},
    brackets: {
      single:[[12400,.10],[50400,.12],[105700,.22],[201775,.24],[256225,.32],[640600,.35],[Infinity,.37]],
      mfj:[[24800,.10],[100800,.12],[211400,.22],[403550,.24],[512450,.32],[768700,.35],[Infinity,.37]]
    },
    ssRate:.062, ssBase:184500, medRate:.0145, addMed:.009, addMedThr:{single:200000,mfj:250000},
    k401:24500
  };
  window.TAX2026 = TAX;

  var $=function(s,r){return (r||document).querySelector(s)}, $$=function(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s))};
  function n(v){v=String(v==null?"":v).replace(/[^0-9.\-]/g,"");var x=parseFloat(v);return isFinite(x)?x:0}
  function $f(x,d){d=d==null?0:d;return (x<0?"-$":"$")+Math.abs(x).toLocaleString("en-US",{minimumFractionDigits:d,maximumFractionDigits:d})}
  function pct(x,d){return (x*100).toFixed(d==null?1:d)+"%"}
  window.fmt$=$f;

  function fedTax(taxable,st){
    var b=TAX.brackets[st]||TAX.brackets.single,tax=0,prev=0,marg=b[0][1];
    taxable=Math.max(0,taxable);
    for(var i=0;i<b.length;i++){var top=b[i][0],r=b[i][1];if(taxable>prev){tax+=(Math.min(taxable,top)-prev)*r;marg=r}prev=top}
    return {tax:tax,marginal:marg};
  }
  function fica(wages,st){
    var ss=Math.min(wages,TAX.ssBase)*TAX.ssRate;
    var med=wages*TAX.medRate+Math.max(0,wages-TAX.addMedThr[st])*TAX.addMed;
    return {ss:ss,med:med,total:ss+med};
  }
  /* Full take-home model */
  function takeHome(o){
    var st=o.status||"single",gross=Math.max(0,o.gross||0);
    var k=Math.min(gross*(o.k401pct||0)/100,TAX.k401);
    var pre=Math.max(0,o.pretax||0);
    var fedTaxable=Math.max(0,gross-k-pre-TAX.std[st]);
    var f=fedTax(fedTaxable,st);
    var fi=fica(Math.max(0,gross-pre),st); // health premiums (Sec.125) reduce FICA wages; 401k does not
    var state=Math.max(0,gross-k-pre)*(o.stateRate||0)/100;
    var net=gross-k-pre-f.tax-fi.total-state;
    return {gross:gross,k401:k,pretax:pre,fed:f.tax,marginal:f.marginal,ss:fi.ss,med:fi.med,fica:fi.total,state:state,net:net,
      avg:gross?(f.tax+fi.total+state)/gross:0};
  }
  window.takeHome2026=takeHome;

  var PER={hour:2080,day:260,week:52,biweek:26,semimonth:24,month:12,year:1};
  var PER_LABEL={hour:"Hourly",day:"Daily",week:"Weekly",biweek:"Bi-weekly",semimonth:"Semi-monthly",month:"Monthly",year:"Annual"};

  /* URL state helpers: shareable calculations */
  function readURL(box){var p=new URLSearchParams(location.search);$$("[name]",box).forEach(function(el){var v=p.get(el.name);if(v!=null&&el.type!=="radio")el.value=v})}
  function writeURL(box){try{var p=new URLSearchParams();$$("input[name],select[name]",box).forEach(function(el){if(el.value!=="")p.set(el.name,el.value)});history.replaceState(null,"","?"+p.toString())}catch(e){}}
  function v(box,name){var el=$("[name="+name+"]",box);return el?el.value:""}

  /* Bar renderer */
  function bar(parts){
    var tot=parts.reduce(function(a,p){return a+Math.max(0,p[1])},0)||1;
    return '<div class="bar">'+parts.map(function(p){return '<span style="width:'+(100*Math.max(0,p[1])/tot)+'%;background:'+p[2]+'" title="'+p[0]+'"></span>'}).join("")+'</div><div class="legend">'+parts.map(function(p){return '<span><i style="background:'+p[2]+'"></i>'+p[0]+' '+$f(p[1])+'</span>'}).join("")+'</div>';
  }
  var COL={net:"#0fb877",fed:"#2f6fde",fica:"#8b5cf6",state:"#f5a524",k:"#14b8a6",pre:"#94a3b5"};

  /* ---------- 1. QUICK converter (home hero) ---------- */
  function quick(box){
    function run(){
      var amt=n(v(box,"amount")),per=v(box,"per")||"year",annual=amt*PER[per];
      var th=takeHome({gross:annual,status:"single"});
      var out=$(".out",box);
      out.innerHTML='<div class="small muted">Annual gross</div><div class="big">'+$f(annual)+'</div>'+
        '<div class="stats">'+["hour","week","biweek","month"].map(function(k){return '<div class="stat"><div class="k">'+PER_LABEL[k]+'</div><div class="v">'+$f(annual/PER[k],k==="hour"?2:0)+'</div></div>'}).join("")+
        '<div class="stat"><div class="k">Est. take-home / mo*</div><div class="v">'+$f(th.net/12)+'</div></div></div>'+
        '<p class="small muted" style="margin:10px 0 0">*Single filer, '+TAX.year+' federal + FICA, no state tax. <a href="'+(box.getAttribute("data-root")||"")+'calculators/take-home-pay.html?salary='+Math.round(annual)+'">Full breakdown →</a></p>';
    }
    box.addEventListener("input",run);run();
  }

  /* ---------- 2. TAKE-HOME ---------- */
  function takehome(box){
    readURL(box);
    function run(){
      var gross=n(v(box,"salary"))*PER[v(box,"per")||"year"];
      var o={gross:gross,status:v(box,"status"),stateRate:n(v(box,"state")),k401pct:n(v(box,"k401")),pretax:n(v(box,"pretax"))};
      var r=takeHome(o);
      var r2=takeHome(Object.assign({},o,{gross:gross+1000}));
      var rows=["year","month","semimonth","biweek","week","day","hour"].map(function(k){var d=PER[k];return '<tr><td>'+PER_LABEL[k]+'</td><td class="r num">'+$f(gross/d,2)+'</td><td class="r num">'+$f((r.fed+r.fica+r.state)/d,2)+'</td><td class="r num"><b>'+$f(r.net/d,2)+'</b></td></tr>'}).join("");
      $(".out",box).innerHTML='<div class="small muted">Estimated take-home pay ('+TAX.year+')</div><div class="big">'+$f(r.net)+'<span class="small muted"> / year</span></div>'+
        '<div class="stats"><div class="stat"><div class="k">Per month</div><div class="v">'+$f(r.net/12)+'</div></div><div class="stat"><div class="k">Per paycheck (bi-wk)</div><div class="v">'+$f(r.net/26)+'</div></div><div class="stat"><div class="k">Marginal fed. rate</div><div class="v">'+pct(r.marginal,0)+'</div></div><div class="stat"><div class="k">Average total tax</div><div class="v">'+pct(r.avg)+'</div></div></div>'+
        bar([["Take-home",r.net,COL.net],["Federal",r.fed,COL.fed],["FICA",r.fica,COL.fica],["State",r.state,COL.state],["401(k)",r.k401,COL.k],["Pre-tax deductions",r.pretax,COL.pre]])+
        '<div class="callout" style="margin-top:16px"><b>Your next $1,000 raise</b> nets about <b class="num">'+$f(r2.net-r.net)+'</b> after tax.</div>'+
        '<div class="table-wrap" style="margin-top:12px"><table><thead><tr><th>Period</th><th class="r">Gross</th><th class="r">Taxes</th><th class="r">Take-home</th></tr></thead><tbody>'+rows+'</tbody></table></div>'+
        '<div class="table-wrap" style="margin-top:12px"><table><tbody>'+
        [["Gross pay",r.gross],["401(k) contribution",-r.k401],["Other pre-tax deductions",-r.pretax],["Federal income tax",-r.fed],["Social Security (6.2%)",-r.ss],["Medicare",-r.med],["State / local tax (est.)",-r.state],["Take-home pay",r.net]].map(function(x){return '<tr><td>'+x[0]+'</td><td class="r num">'+$f(x[1],2)+'</td></tr>'}).join("")+'</tbody></table></div>';
      writeURL(box);
      var cta=$("[data-cta-income]");if(cta)cta.href=cta.getAttribute("data-base")+"?income="+Math.round(gross);
    }
    box.addEventListener("input",run);box.addEventListener("change",run);run();
  }

  /* ---------- 3. SALARY ⇄ HOURLY ---------- */
  function hourly(box){
    readURL(box);
    function run(){
      var amt=n(v(box,"amount")),per=v(box,"per")||"year",hpw=n(v(box,"hours"))||40,wks=n(v(box,"weeks"))||52,off=n(v(box,"daysoff"));
      var hoursYr=hpw*wks, annual;
      var table={hour:hoursYr,day:wks*5,week:wks,biweek:wks/2,semimonth:24,month:12,year:1};
      annual=amt*table[per];
      var worked=hoursYr-off*(hpw/5);
      var out='<div class="small muted">Equivalent annual pay</div><div class="big">'+$f(annual)+'</div><div class="table-wrap" style="margin-top:12px"><table><thead><tr><th>Period</th><th class="r">Unadjusted</th><th class="r">Adjusted for '+off+' days off</th></tr></thead><tbody>'+
        Object.keys(table).map(function(k){var adj=k==="hour"?annual/Math.max(1,worked):k==="day"?annual/Math.max(1,wks*5-off):annual/table[k];return '<tr><td>'+PER_LABEL[k]+'</td><td class="r num">'+$f(annual/table[k],2)+'</td><td class="r num">'+$f(adj,2)+'</td></tr>'}).join("")+'</tbody></table></div>'+
        '<p class="small muted" style="margin-top:10px">Formula: annual = rate × periods per year. Hourly uses '+hpw+' h/week × '+wks+' weeks = '+hoursYr.toLocaleString()+' paid hours. Paid time off raises your effective rate per hour actually worked.</p>';
      $(".out",box).innerHTML=out;writeURL(box);
    }
    box.addEventListener("input",run);box.addEventListener("change",run);run();
  }

  /* ---------- 4. RAISE ---------- */
  function raise(box){
    readURL(box);
    function run(){
      var cur=n(v(box,"current")),p=n(v(box,"pct")),inf=n(v(box,"inflation")),st=v(box,"status")||"single";
      var nw=cur*(1+p/100),a=takeHome({gross:cur,status:st}),b=takeHome({gross:nw,status:st});
      var real=((1+p/100)/(1+inf/100)-1);
      $(".out",box).innerHTML='<div class="small muted">New salary</div><div class="big">'+$f(nw)+'</div><div class="stats">'+
        '<div class="stat"><div class="k">Gross gain / yr</div><div class="v">'+$f(nw-cur)+'</div></div>'+
        '<div class="stat"><div class="k">After-tax gain / yr</div><div class="v">'+$f(b.net-a.net)+'</div></div>'+
        '<div class="stat"><div class="k">After-tax / month</div><div class="v">'+$f((b.net-a.net)/12)+'</div></div>'+
        '<div class="stat"><div class="k">Real raise (vs '+inf+'% inflation)</div><div class="v" style="color:'+(real<0?"var(--danger)":"var(--brand)")+'">'+pct(real,2)+'</div></div></div>'+
        (real<0?'<div class="callout warn" style="margin-top:14px">This raise is below inflation — your purchasing power falls. Use our <a href="../guides/how-to-negotiate-a-raise.html">negotiation playbook</a>.</div>':'<div class="callout" style="margin-top:14px">You keep about <b>'+pct((b.net-a.net)/Math.max(1,nw-cur),0)+'</b> of every new dollar after tax.</div>');
      writeURL(box);
    }
    box.addEventListener("input",run);box.addEventListener("change",run);run();
  }

  /* ---------- 5. BUDGET ---------- */
  function budget(box){
    readURL(box);
    function run(){
      var inc=n(v(box,"income")),rule=(v(box,"rule")||"50-30-20").split("-").map(Number);
      var names=["Needs","Wants","Savings & debt"],cols=["#2f6fde","#f5a524","#0fb877"];
      var actual=[n(v(box,"needs")),n(v(box,"wants")),n(v(box,"savings"))],has=actual.some(function(x){return x>0});
      var plan=rule.map(function(r){return inc*r/100});
      var html='<div class="small muted">Monthly plan on '+$f(inc)+' take-home</div>'+bar(names.map(function(nm,i){return [nm,plan[i],cols[i]]}))+
        '<div class="table-wrap" style="margin-top:12px"><table><thead><tr><th>Bucket</th><th class="r">Target</th>'+(has?'<th class="r">Actual</th><th class="r">Difference</th>':'')+'</tr></thead><tbody>'+
        names.map(function(nm,i){var d=i===2?actual[i]-plan[i]:plan[i]-actual[i];return '<tr><td>'+nm+' ('+rule[i]+'%)</td><td class="r num">'+$f(plan[i])+'</td>'+(has?'<td class="r num">'+$f(actual[i])+'</td><td class="r num" style="color:'+(d<0?"var(--danger)":"var(--brand)")+'">'+(d>=0?"+":"")+$f(d)+'</td>':'')+'</tr>'}).join("")+'</tbody></table></div>';
      if(has){var left=inc-actual[0]-actual[1]-actual[2];html+='<div class="callout '+(left<0?"warn":"")+'" style="margin-top:14px">'+(left<0?'You are overspending by <b>'+$f(-left)+'</b>/month.':'Unassigned this month: <b>'+$f(left)+'</b> — send it to savings or debt.')+'</div>'}
      html+='<p class="small muted" style="margin-top:10px">Emergency fund target (6 months of needs): <b class="num">'+$f(plan[0]*6)+'</b></p>';
      $(".out",box).innerHTML=html;writeURL(box);
    }
    box.addEventListener("input",run);box.addEventListener("change",run);run();
  }

  /* ---------- 6. JOB OFFER COMPARE ---------- */
  function offer(box){
    function calc(p){
      var base=n(v(box,p+"base")),bonus=n(v(box,p+"bonus")),match=n(v(box,p+"match")),prem=n(v(box,p+"health")),pto=n(v(box,p+"pto")),cm=n(v(box,p+"commute")),cc=n(v(box,p+"commutecost")),hrs=n(v(box,p+"hours"))||40;
      var total=base+bonus+base*match/100-prem*12-cc*12;
      var hours=hrs*52-pto*(hrs/5)+cm*48;
      return {total:total,hourly:total/Math.max(1,hours),hours:hours,net:takeHome({gross:base+bonus}).net+base*match/100-prem*12-cc*12};
    }
    function run(){
      var a=calc("a_"),b=calc("b_"),win=a.hourly>=b.hourly?"A":"B";
      $(".out",box).innerHTML='<div class="table-wrap"><table><thead><tr><th></th><th class="r">Offer A</th><th class="r">Offer B</th></tr></thead><tbody>'+
        [["Total value / yr",a.total,b.total,0],["After-tax value / yr",a.net,b.net,0],["Real hours / yr (incl. commute)",a.hours,b.hours,-1],["True hourly value",a.hourly,b.hourly,2]].map(function(r){return '<tr><td>'+r[0]+'</td><td class="r num">'+(r[3]<0?Math.round(r[1]).toLocaleString():$f(r[1],r[3]))+'</td><td class="r num">'+(r[3]<0?Math.round(r[2]).toLocaleString():$f(r[2],r[3]))+'</td></tr>'}).join("")+
        '</tbody></table></div><div class="callout" style="margin-top:14px"><b>Offer '+win+'</b> pays more per hour of your life — by <b class="num">'+$f(Math.abs(a.hourly-b.hourly),2)+'/h</b> ('+$f(Math.abs(a.hourly-b.hourly)*Math.min(a.hours,b.hours))+'/yr equivalent).</div>';
    }
    box.addEventListener("input",run);run();
  }

  /* ---------- 7. FREELANCE RATE ---------- */
  function freelance(box){
    readURL(box);
    function run(){
      var target=n(v(box,"target")),exp=n(v(box,"expenses")),hrs=n(v(box,"billable"))||25,wks=n(v(box,"weeks"))||46,tax=n(v(box,"taxrate"))/100,margin=n(v(box,"margin"))/100;
      // Self-employment tax: 15.3% on 92.35% of net earnings (SS part capped at wage base)
      var seBase=target*.9235, se=Math.min(seBase,TAX.ssBase)*.124+seBase*.029;
      var needed=(target+se)/(1-tax)+exp;needed=needed*(1+margin);
      var hours=hrs*wks,rate=needed/Math.max(1,hours);
      $(".out",box).innerHTML='<div class="small muted">Minimum hourly rate</div><div class="big">'+$f(rate,2)+'<span class="small muted"> / hour</span></div><div class="stats">'+
        '<div class="stat"><div class="k">Day rate (8h)</div><div class="v">'+$f(rate*8)+'</div></div><div class="stat"><div class="k">Revenue needed / yr</div><div class="v">'+$f(needed)+'</div></div><div class="stat"><div class="k">Self-employment tax</div><div class="v">'+$f(se)+'</div></div><div class="stat"><div class="k">Billable hours / yr</div><div class="v">'+hours.toLocaleString()+'</div></div></div>'+
        '<p class="small muted" style="margin-top:10px">An employee earning '+$f(target)+' gets ~'+$f(target/2080,2)+'/h. Freelancers need about <b>'+(rate/(target/2080)).toFixed(1)+'×</b> that to end up in the same place.</p>';
      writeURL(box);
    }
    box.addEventListener("input",run);run();
  }

  /* ---------- 8. LOAN ---------- */
  function loan(box){
    readURL(box);
    function run(){
      var P=n(v(box,"principal")),apr=n(v(box,"apr"))/100,yrs=n(v(box,"years"))||1,extra=n(v(box,"extra"));
      var r=apr/12,N=Math.round(yrs*12),pmt=r?P*r/(1-Math.pow(1+r,-N)):P/N;
      var bal=P,ti=0,m=0,rows=[],yi=0,yp=0;
      while(bal>0.005&&m<1200){var i=bal*r,pr=Math.min(bal,pmt-i+extra);bal-=pr;ti+=i;yi+=i;yp+=pr;m++;if(m%12===0||bal<=0.005){rows.push([Math.ceil(m/12),yp,yi,Math.max(0,bal)]);yi=0;yp=0}}
      $(".out",box).innerHTML='<div class="small muted">Monthly payment</div><div class="big">'+$f(pmt+extra,2)+'</div><div class="stats">'+
        '<div class="stat"><div class="k">Total interest</div><div class="v">'+$f(ti)+'</div></div><div class="stat"><div class="k">Total paid</div><div class="v">'+$f(P+ti)+'</div></div><div class="stat"><div class="k">Payoff</div><div class="v">'+Math.floor(m/12)+'y '+(m%12)+'m</div></div></div>'+
        bar([["Principal",P,"#2f6fde"],["Interest",ti,"#f5a524"]])+
        '<div class="table-wrap" style="margin-top:12px;max-height:340px;overflow:auto"><table><thead><tr><th>Year</th><th class="r">Principal</th><th class="r">Interest</th><th class="r">Balance</th></tr></thead><tbody>'+rows.map(function(x){return '<tr><td>'+x[0]+'</td><td class="r num">'+$f(x[1])+'</td><td class="r num">'+$f(x[2])+'</td><td class="r num">'+$f(x[3])+'</td></tr>'}).join("")+'</tbody></table></div>';
      writeURL(box);
    }
    box.addEventListener("input",run);run();
  }

  /* ---------- 9. SAVINGS / COMPOUND ---------- */
  function savings(box){
    readURL(box);
    function run(){
      var p0=n(v(box,"initial")),pm=n(v(box,"monthly")),r=n(v(box,"rate"))/100,yrs=n(v(box,"years"))||1,goal=n(v(box,"goal"));
      var bal=p0,rows=[],contrib=p0,hit=0;
      for(var m=1;m<=yrs*12;m++){bal=bal*(1+r/12)+pm;contrib+=pm;if(goal&&!hit&&bal>=goal)hit=m;if(m%12===0)rows.push([m/12,contrib,bal])}
      $(".out",box).innerHTML='<div class="small muted">Balance after '+yrs+' years</div><div class="big">'+$f(bal)+'</div>'+
        bar([["You contributed",contrib,"#2f6fde"],["Growth",bal-contrib,"#0fb877"]])+
        (goal?'<div class="callout" style="margin-top:14px">'+(hit?'You reach your '+$f(goal)+' goal in <b>'+Math.floor(hit/12)+'y '+(hit%12)+'m</b>.':'Goal not reached in '+yrs+' years — raise the monthly amount or extend the timeline.')+'</div>':'')+
        '<div class="table-wrap" style="margin-top:12px;max-height:320px;overflow:auto"><table><thead><tr><th>Year</th><th class="r">Contributed</th><th class="r">Balance</th></tr></thead><tbody>'+rows.map(function(x){return '<tr><td>'+x[0]+'</td><td class="r num">'+$f(x[1])+'</td><td class="r num">'+$f(x[2])+'</td></tr>'}).join("")+'</tbody></table></div>';
      writeURL(box);
    }
    box.addEventListener("input",run);run();
  }

  /* ---------- 10. AI PAY-RESILIENCE SCORE ---------- */
  function ai(box){
    function run(){
      var qs=$$(".q",box),score=0,max=0,ans=0;
      qs.forEach(function(q){var c=$("input:checked",q);max+=3;if(c){score+=n(c.value);ans++}});
      var out=$(".out",box);
      if(ans<qs.length){out.innerHTML='<p class="muted small">Answer all '+qs.length+' questions to see your score ('+ans+'/'+qs.length+' done).</p>';return}
      var s=Math.round(100*score/max),band=s>=70?["Strong","Your pay rests on skills AI amplifies rather than replaces. Lean in: price your judgment, not your hours."]:s>=45?["Mixed","Part of your work is automatable. Shift time toward client-facing, decision and AI-supervision tasks within 12 months."]:["Exposed","Much of your current task mix is routine and text/data-based. Start an upskilling plan now — the earlier, the cheaper."];
      out.innerHTML='<div class="small muted">Your Pay-Resilience Score</div><div class="big">'+s+'<span class="small muted"> / 100 — '+band[0]+'</span></div><div class="meter"><i style="left:calc('+s+'% - 2px)"></i></div><p>'+band[1]+'</p><a class="btn btn-primary" href="'+(box.getAttribute("data-root")||"")+'pay-checkup.html?goal=career&topic=ai-score-'+s+'">Get a free personalised upskilling plan →</a><p class="small muted" style="margin-top:10px">A self-assessment framework for reflection, not a prediction.</p>';
    }
    box.addEventListener("change",run);run();
  }

  var MAP={quick:quick,takehome:takehome,hourly:hourly,raise:raise,budget:budget,offer:offer,freelance:freelance,loan:loan,savings:savings,ai:ai};
  $$("[data-calc]").forEach(function(b){var f=MAP[b.getAttribute("data-calc")];if(f)f(b)});
  $$("[data-seg]").forEach(function(seg){
    var input=$("[name="+seg.getAttribute("data-seg")+"]",seg.closest("[data-calc]")||document);
    seg.addEventListener("click",function(e){var b=e.target.closest("button");if(!b)return;e.preventDefault();$$("button",seg).forEach(function(x){x.classList.toggle("on",x===b)});input.value=b.value;input.dispatchEvent(new Event("input",{bubbles:true}))});
  });
})();
