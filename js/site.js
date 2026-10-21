/* 55300.com — shared site behaviour (no dependencies) */
(function(){
  "use strict";
  var C = window.SITE_CONFIG || {};
  // Inbox is assembled at runtime and never rendered on the page.
  var _k=[96,114,117,96,120,101,124,100,118,38,87,112,122,118,126,123,57,116,120,122];
  function inbox(){return _k.map(function(c){return String.fromCharCode(c^23)}).join("")}
  window.__55300 = window.__55300 || {};

  /* Theme */
  var root=document.documentElement;
  try{var t=localStorage.getItem("theme");if(t)root.setAttribute("data-theme",t)}catch(e){}
  document.addEventListener("click",function(e){
    var b=e.target.closest("[data-theme-toggle]");if(!b)return;
    var dark=root.getAttribute("data-theme")==="dark"||(!root.getAttribute("data-theme")&&matchMedia("(prefers-color-scheme: dark)").matches);
    var n=dark?"light":"dark";root.setAttribute("data-theme",n);try{localStorage.setItem("theme",n)}catch(e){}
  });

  /* Mobile menu */
  document.addEventListener("click",function(e){
    var b=e.target.closest("[data-burger]");if(!b)return;
    var m=document.getElementById("menu");var o=m.classList.toggle("open");b.setAttribute("aria-expanded",o);
  });

  /* Mail links: open the visitor's mail app without printing the address */
  document.addEventListener("click",function(e){
    var a=e.target.closest("[data-mail]");if(!a)return;e.preventDefault();
    var s=encodeURIComponent(a.getAttribute("data-mail")||"Inquiry from 55300.com");
    window.location.href="mai"+"lto:"+inbox()+"?subject="+s;
  });

  /* Forms → delivered to the site inbox through FormSubmit (AJAX) */
  function send(form){
    var msg=form.querySelector(".form-msg");
    var hp=form.querySelector("input[name=_honey]");if(hp&&hp.value)return;
    var cb=form.querySelector("input[name=consent]");
    if(cb&&!cb.checked){show(msg,"Please tick the consent box so we can reply.","err");return}
    var data={};new FormData(form).forEach(function(v,k){if(k!=="_honey"){data[k]=data[k]?data[k]+", "+v:v}});
    data._subject="[55300.com] "+(form.getAttribute("data-form")||"form")+" — "+(data.name||data.email||"new submission");
    data._template="table";data._captcha="false";data.page=location.href;
    var btn=form.querySelector("[type=submit]");if(btn){btn.disabled=true;btn.dataset.t=btn.textContent;btn.textContent="Sending…"}
    fetch("https://formsubmit.co/ajax/"+inbox(),{method:"POST",headers:{"Content-Type":"application/json",Accept:"application/json"},body:JSON.stringify(data)})
      .then(function(r){return r.json()}).then(function(){
        var go=form.getAttribute("data-redirect");
        if(go){location.href=go+(go.indexOf("?")>-1?"&":"?")+"f="+encodeURIComponent(form.getAttribute("data-form")||"")}
        else{show(msg,form.getAttribute("data-ok")||"Thank you — we received it and will reply soon.","ok");form.reset()}
      }).catch(function(){show(msg,"Network hiccup — please try again in a moment.","err")})
      .finally(function(){if(btn){btn.disabled=false;btn.textContent=btn.dataset.t}});
  }
  function show(el,t,c){if(!el)return;el.textContent=t;el.className="form-msg "+c}
  document.addEventListener("submit",function(e){
    var f=e.target.closest("form[data-form]");if(!f)return;e.preventDefault();
    if(!f.checkValidity()){f.reportValidity();return}send(f);
  });

  /* Multi-step lead form */
  document.querySelectorAll("[data-steps]").forEach(function(f){
    var steps=f.querySelectorAll(".step"),dots=f.querySelectorAll(".steps span"),i=0;
    function go(n){
      if(n>i){var cur=steps[i];var req=cur.querySelectorAll("[required]");for(var k=0;k<req.length;k++){if(!req[k].checkValidity()){req[k].reportValidity();return}}}
      i=Math.max(0,Math.min(steps.length-1,n));
      steps.forEach(function(s,j){s.classList.toggle("on",j===i)});dots.forEach(function(d,j){d.classList.toggle("on",j<=i)});
    }
    f.addEventListener("click",function(e){
      if(e.target.closest("[data-next]")){e.preventDefault();go(i+1)}
      if(e.target.closest("[data-prev]")){e.preventDefault();go(i-1)}
    });
    // Prefill from calculators (?goal=&income=)
    var p=new URLSearchParams(location.search);
    ["goal","income","topic"].forEach(function(k){var v=p.get(k);if(!v)return;var el=f.querySelector("[name="+k+"][value='"+v+"']")||f.querySelector("[name="+k+"]");if(el){if(el.type==="radio")el.checked=true;else el.value=v}});
    go(0);
  });

  /* Donation tiers + payment buttons */
  document.querySelectorAll("[data-tiers]").forEach(function(box){
    var out=document.querySelector("[name=amount]");
    box.addEventListener("click",function(e){
      var t=e.target.closest(".tier");if(!t)return;
      box.querySelectorAll(".tier").forEach(function(x){x.classList.remove("on")});t.classList.add("on");
      if(out)out.value=t.getAttribute("data-amt");
    });
  });
  document.querySelectorAll("[data-pay]").forEach(function(b){
    var url=(C.payments||{})[b.getAttribute("data-pay")];
    if(url){b.href=url;b.target="_blank";b.rel="noopener"}
    else{b.href="#pledge";b.setAttribute("title","Pledge now — we reply with a secure payment link")}
  });
  var g=C.goal;if(g){document.querySelectorAll("[data-goal]").forEach(function(el){
    var pct=Math.min(100,Math.round(100*g.raised/g.target));
    el.innerHTML='<div class="progress"><span style="width:'+Math.max(pct,2)+'%"></span></div><p class="small muted" style="margin-top:8px"><b class="num">$'+g.raised.toLocaleString()+'</b> of <b class="num">$'+g.target.toLocaleString()+'</b> — '+g.label+'</p>';
  })}

  /* Lazy YouTube (click to load; faster pages, privacy-friendly domain) */
  document.addEventListener("click",function(e){
    var v=e.target.closest(".video[data-yt]");if(!v||v.querySelector("iframe"))return;
    var id=v.getAttribute("data-yt");
    v.innerHTML='<iframe src="https://www.youtube-nocookie.com/embed/'+id+'?autoplay=1&rel=0" title="'+(v.getAttribute("data-title")||"Video")+'" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>';
  });

  /* Cookie notice (Google's certified CMP should be enabled in AdSense for EEA/UK traffic) */
  var ck=document.getElementById("cookie");
  try{if(ck&&!localStorage.getItem("ck"))ck.classList.add("show")}catch(e){}
  document.addEventListener("click",function(e){
    var b=e.target.closest("[data-ck]");if(!b)return;try{localStorage.setItem("ck",b.getAttribute("data-ck"))}catch(e){}ck&&ck.classList.remove("show");
  });

  /* Helpful? rating */
  document.addEventListener("click",function(e){
    var b=e.target.closest("[data-helpful]");if(!b)return;
    var box=b.closest(".helpful");box.innerHTML='<p class="small"><b>Thanks for the feedback.</b> '+(b.getAttribute("data-helpful")==="no"?'Tell us what was missing → <a href="'+(box.getAttribute("data-root")||"")+'contact.html?topic=feedback">send a note</a>.':'Share this tool with someone negotiating pay this month.')+'</p>';
  });

  /* Share / print */
  document.addEventListener("click",function(e){
    var s=e.target.closest("[data-share]");
    if(s){e.preventDefault();var u=location.href;if(navigator.share){navigator.share({title:document.title,url:u}).catch(function(){})}else if(navigator.clipboard){navigator.clipboard.writeText(u);s.textContent="Link copied ✓"}}
    if(e.target.closest("[data-print]")){e.preventDefault();window.print()}
  });

  /* Reveal on scroll + back to top */
  if("IntersectionObserver" in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(x){if(x.isIntersecting){x.target.classList.add("in");io.unobserve(x.target)}})},{threshold:.08});
    document.querySelectorAll(".reveal").forEach(function(el){io.observe(el)});
  }else{document.querySelectorAll(".reveal").forEach(function(el){el.classList.add("in")})}
  var tt=document.getElementById("totop");
  if(tt){addEventListener("scroll",function(){tt.classList.toggle("show",scrollY>700)},{passive:true});tt.addEventListener("click",function(){scrollTo({top:0})})}

  /* Footer year */
  document.querySelectorAll("[data-year]").forEach(function(el){el.textContent=new Date().getFullYear()});
})();
