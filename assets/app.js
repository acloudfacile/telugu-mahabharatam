(function(){
  const P = window.MB_PARVAS, C = window.MB_CONTENT || {}, CH = window.MB_CHARS || [], G = window.MB_GURUS || {gurus:[]};
  const IMG = window.MB_IMG || 'img/', ICO = window.MB_ICO || 'icons/', EV = window.MB_EVOLUTION || null;
  const TN = ['౦','౧','౨','౩','౪','౫','౬','౭','౮','౯'];
  const tnum = n => String(n).split('').map(d => TN[+d]).join('');
  const esc = s => String(s).replace(/[&<>"]/g, m => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[m]));
  const img = f => (IMG === 'inline' ? (window.MB_IMAGES||{})[f] : IMG + f);
  const ico = f => (ICO === 'inline' ? (window.MB_ICONS||{})[f] : ICO + f);
  const $ = document.getElementById('app');
  const statusText = {published:'ప్రచురితం', next:'తరువాతి భాగం', coming:'రానున్నది'};
  const sideText = {pandava:'పాండవ పక్షం', kaurava:'కౌరవ పక్షం', guru:'గురువులు, మునులు', deva:'దేవతలు', kuru:'కురు వంశ పూర్వీకులు', other:'ఇతరులు'};

  const byName = {};
  CH.forEach(c => { byName[c.name] = c; c.aliases.forEach(a => byName[a] = c); byName[c.name.replace(/ \(.*\)$/,'')] = c; });
  const findChar = n => byName[n] || byName[n.replace(/\s*\(.*\)$/,'')] || null;
  const findCharById = id => CH.find(c => c.id === id);
  const appearances = {};
  Object.keys(C).forEach(pid => C[pid].episodes.forEach(e => e.characters.forEach(n => {
    const c = findChar(n); if(!c) return;
    (appearances[c.id] = appearances[c.id] || []).push({pid, num:e.num, title:e.title});
  })));

  const avatar = (c, size=44) => c ? `<img class="av" src="${ico(c.id+'.png')}" alt="" width="${size}" height="${size}">` : '';
  const charChip = n => { const c = findChar(n); return c
    ? `<a class="chip" href="#/patra/${c.id}">${avatar(c,28)}<span>${esc(n)}</span></a>`
    : `<span class="chip">${esc(n)}</span>`; };
  const emblem = (p, cls='emblem') => `<img class="${cls}" src="${ico('parva_'+String(p.num).padStart(2,'0')+'.png')}" alt="">`;

  function home(){
    const done = P.parvas.filter(p => p.status === 'published').length;
    document.title = P.site.title;
    $.innerHTML = `
      <section class="hero">
        <div>
          <h1>${esc(P.site.title)}</h1>
          <p class="tag">${esc(P.site.tagline)}</p>
          <div class="quick">
            <a href="#/patralu"><span class="avs">${['krishna','arjuna','draupadi','bhishma','karna'].map(i=>avatar(findCharById(i),36)).join('')}</span><span>పాత్రలు · ${tnum(CH.length)}</span></a>
            <a href="#/guruvulu"><span class="avs">${G.gurus.slice(0,4).map(g=>avatar(findCharById(g.id),36)).join('')}</span><span>గురు పరంపర</span></a>
          </div>
        </div>
        <div class="progress">
          <span class="count">${tnum(done)} / ${tnum(P.parvas.length)}</span>
          <span class="label">పర్వాలు ప్రచురితమయ్యాయి</span>
          <a href="#/parva/adi">ఆది పర్వము చదవండి</a>
        </div>
      </section>
      <p class="about">${esc(P.site.about)}</p>
      <ol class="parvas">
        ${P.parvas.map(p => `
          <li class="${p.status}">
            ${emblem(p)}
            <div>
              <div class="name"><span class="num sm">${tnum(p.num)}</span>${p.status === 'published' ? `<a href="#/parva/${p.id}">${esc(p.te)}</a>` : esc(p.te)}<span class="en">${esc(p.en)}</span></div>
              <div class="sum">${esc(p.summary)}</div>
              <span class="pill ${p.status}">${statusText[p.status]}${p.status==='published' && C[p.id] ? ' · ' + tnum(C[p.id].episodes.length) + ' కథలు' : ''}</span>
            </div>
          </li>`).join('')}
      </ol>`;
  }

  function parva(id){
    const p = P.parvas.find(x => x.id === id), c = C[id];
    if(!p){ return notfound(); }
    document.title = `${p.te} — ${P.site.title}`;
    const head = `<div class="parva-head">${emblem(p,'emblem big')}<div><span class="num sm">${tnum(p.num)}</span><h1>${esc(p.te)}</h1><div class="en">${esc(p.en)}${c ? ' · ' + tnum(c.episodes.length) + ' కథలు' : ''}</div></div></div>`;
    if(!c){ $.innerHTML = head + `<p class="empty">ఈ పర్వము ఇంకా ప్రచురించలేదు. ముందు <a href="#/parva/adi">ఆది పర్వము</a> చదవండి.</p>`; return; }
    $.innerHTML = head + `
      <div class="intro measure" style="margin:0">${c.intro.map(t => `<p>${esc(t)}</p>`).join('')}</div>
      <ol class="episodes">
        ${c.episodes.map(e => `
          <li>
            <a href="#/parva/${id}/${e.num}"><img src="${img(e.image)}" alt="${esc(e.caption)}" loading="lazy"></a>
            <div>
              <div class="t"><span class="n">${tnum(e.num)}</span><a href="#/parva/${id}/${e.num}">${esc(e.title)}</a></div>
              <div class="chips">${e.characters.map(charChip).join('')}</div>
            </div>
          </li>`).join('')}
      </ol>`;
  }

  function episode(id, n){
    const p = P.parvas.find(x => x.id === id), c = C[id];
    if(!p || !c) return notfound();
    const i = +n - 1, e = c.episodes[i];
    if(!e) return notfound();
    const prev = c.episodes[i-1], next = c.episodes[i+1];
    document.title = `${e.title} — ${p.te}`;
    $.innerHTML = `
      <div class="measure">
        <div class="crumbs"><a href="#/">హోమ్</a> › <a href="#/parva/${id}">${esc(p.te)}</a></div>
        <div class="ep-head">
          <span class="num big">${tnum(e.num)}</span>
          <h1>${esc(e.title)}</h1>
          <div class="pos">${esc(p.te)} · కథ ${tnum(e.num)} / ${tnum(c.episodes.length)}</div>
        </div>
        <figure><img src="${img(e.image)}" alt="${esc(e.caption)}"><figcaption>${esc(e.caption)}</figcaption></figure>
        <div class="chars-box"><b>ముఖ్య పాత్రలు</b><div class="chips">${e.characters.map(charChip).join('')}</div></div>
        <div class="story">${e.paras.map(t => `<p>${esc(t)}</p>`).join('')}</div>
        <nav class="pager">
          ${prev ? `<a href="#/parva/${id}/${prev.num}"><small>మునుపటి కథ</small>${esc(prev.title)}</a>` : ''}
          ${next ? `<a class="next" href="#/parva/${id}/${next.num}"><small>తరువాతి కథ</small>${esc(next.title)}</a>` : ''}
        </nav>
        ${!next ? `<div class="closing"><p>${esc(c.closing)}</p><a href="#/">అన్ని పర్వాలు</a></div>` : ''}
      </div>`;
  }

  function characters(filter){
    document.title = `పాత్రలు — ${P.site.title}`;
    const sides = ['pandava','kaurava','kuru','guru','deva','other'];
    const active = sides.includes(filter) ? filter : null;
    const list = active ? CH.filter(c => c.side === active) : CH;
    $.innerHTML = `
      <div class="page-head"><h1>పాత్రలు</h1><p>మహాభారత పాత్రలు — ఎవరు ఎవరో, ఏ కథలలో కనిపిస్తారో. పాత్రను నొక్కి ఆ పాత్ర ఉన్న కథలు చూడండి.</p></div>
      <div class="filters"><a class="${!active?'on':''}" href="#/patralu">అందరూ</a>${sides.map(s=>`<a class="${active===s?'on':''}" href="#/patralu/${s}">${sideText[s]}</a>`).join('')}</div>
      <ul class="char-grid">
        ${list.map(c => `<li><a href="#/patra/${c.id}">${avatar(c,88)}<span class="cn">${esc(c.name)}</span><span class="cr">${esc(c.role)}</span>${appearances[c.id]?`<span class="cc">${tnum(appearances[c.id].length)} కథలు</span>`:''}</a></li>`).join('')}
      </ul>`;
  }

  function character(id){
    const c = findCharById(id); if(!c) return notfound();
    document.title = `${c.name} — ${P.site.title}`;
    const eps = appearances[c.id] || [];
    const guru = G.gurus.find(g => g.id === id);
    const learnedFrom = G.gurus.filter(g => g.disciples.includes(id));
    const discChips = ds => ds.map(d => { const dc = findCharById(d); return dc ? charChip(dc.name) : `<span class="chip">${esc(d)}</span>`; }).join('');
    $.innerHTML = `
      <div class="measure">
        <div class="crumbs"><a href="#/">హోమ్</a> › <a href="#/patralu">పాత్రలు</a></div>
        <div class="char-head">${avatar(c,140)}<div><h1>${esc(c.name)}</h1><p>${esc(c.role)}</p><span class="pill side-${c.side}">${sideText[c.side]}</span>${c.aliases.length?`<div class="al">ఇతర పేర్లు: ${c.aliases.join(', ')}</div>`:''}</div></div>
        ${learnedFrom.length ? `<div class="chars-box"><b>గురువులు</b><div class="chips">${learnedFrom.map(g=>charChip(findCharById(g.id).name)).join('')}</div></div>` : ''}
        ${guru ? `<div class="chars-box"><b>శిష్యులు</b><div class="chips">${discChips(guru.disciples)}</div></div>` : ''}
        <h2 class="sub">ఈ పాత్ర ఉన్న కథలు</h2>
        ${eps.length ? `<ol class="ep-links">${eps.map(e => { const p = P.parvas.find(x=>x.id===e.pid); return `<li><a href="#/parva/${e.pid}/${e.num}"><span class="n">${tnum(e.num)}</span>${esc(e.title)}<small>${esc(p.te)}</small></a></li>`; }).join('')}</ol>`
                     : `<p class="empty">ఈ పాత్ర కథలు తరువాతి పర్వాలలో వస్తాయి.</p>`}
      </div>`;
  }

  function gurus(){
    document.title = `గురు పరంపర — ${P.site.title}`;
    $.innerHTML = `
      <div class="page-head"><h1>గురు పరంపర</h1><p>${esc(G.intro)}</p></div>
      <div class="guru-list">
        ${G.gurus.map(g => { const c = findCharById(g.id); return `
          <section class="guru">
            <a href="#/patra/${g.id}">${avatar(c,110)}</a>
            <div>
              <div class="gt">${esc(g.title)}</div>
              <h2><a href="#/patra/${g.id}">${esc(c ? c.name : g.id)}</a></h2>
              <div class="taught">బోధించినది: ${esc(g.taught)}</div>
              <p>${esc(g.note)}</p>
              ${g.disciples.length ? `<div class="chips"><span class="lbl">శిష్యులు</span>${g.disciples.map(d => { const dc = findCharById(d); return dc ? charChip(dc.name) : `<span class="chip">${esc(d)}</span>`; }).join('')}</div>` : ''}
            </div>
          </section>`; }).join('')}
      </div>`;
  }

  function search(q){
    q = (q||'').trim();
    document.title = `వెతుకు — ${P.site.title}`;
    const chars = q ? CH.filter(c => (c.name + ' ' + c.aliases.join(' ') + ' ' + c.role).includes(q)) : [];
    const eps = [];
    if(q) Object.keys(C).forEach(pid => C[pid].episodes.forEach(e => {
      const hay = e.title + ' · ' + e.characters.join(', ') + ' · ' + e.paras.join(' ');
      const at = hay.indexOf(q); if(at < 0) return;
      const s = Math.max(0, at - 60); eps.push({pid, e, snip: (s?'…':'') + hay.slice(s, at+120) + '…'});
    }));
    const mark = t => esc(t).split(esc(q)).join('<mark>'+esc(q)+'</mark>');
    $.innerHTML = `
      <div class="page-head"><h1>వెతుకు</h1>
        <form class="search-big" id="sform"><input name="q" value="${esc(q)}" placeholder="పాత్ర పేరు, కథ పేరు, లేదా ఏదైనా పదం"><button>వెతుకు</button></form></div>
      ${!q ? '' : `
        <h2 class="sub">పాత్రలు (${tnum(chars.length)})</h2>
        ${chars.length ? `<ul class="char-grid small">${chars.map(c=>`<li><a href="#/patra/${c.id}">${avatar(c,64)}<span class="cn">${esc(c.name)}</span><span class="cr">${esc(c.role)}</span></a></li>`).join('')}</ul>` : '<p class="empty">పాత్రలు దొరకలేదు.</p>'}
        <h2 class="sub">కథలు (${tnum(eps.length)})</h2>
        ${eps.length ? `<ol class="ep-links">${eps.map(x => { const p = P.parvas.find(y=>y.id===x.pid); return `<li><a href="#/parva/${x.pid}/${x.e.num}"><span class="n">${tnum(x.e.num)}</span>${esc(x.e.title)}<small>${esc(p.te)}</small></a><div class="snip">${mark(x.snip)}</div></li>`; }).join('')}</ol>` : '<p class="empty">కథలలో ఈ పదం దొరకలేదు.</p>'}`}`;
    const f = document.getElementById('sform');
    f.addEventListener('submit', ev => { ev.preventDefault(); location.hash = '#/vetuku/' + encodeURIComponent(f.q.value); });
    if(!q) f.q.focus();
  }

  function evolution(){
    if(!EV) return notfound();
    document.title = `${EV.title} — ${P.site.title}`;
    $.innerHTML = `
      <div class="page-head"><h1>${esc(EV.title)}</h1><p>${esc(EV.lead)}</p></div>
      <ol class="timeline">${EV.timeline.map(t => `<li><span class="tw">${esc(t.when)}</span><span class="tt">${esc(t.what)}</span><span class="td">${esc(t.detail)}</span></li>`).join('')}</ol>
      <div class="measure evo">
        ${EV.sections.map(sec => `<section><h2 class="sub">${esc(sec.h)}</h2>${sec.p.map(t=>`<p>${esc(t)}</p>`).join('')}</section>`).join('')}
        <section><h2 class="sub">ఆధారాలు</h2><ol class="sources">${EV.sources.map(x=>`<li><a href="${esc(x.u)}" target="_blank" rel="noopener">${esc(x.t)}</a></li>`).join('')}</ol></section>
      </div>`;
  }

  function notfound(){ $.innerHTML = `<p class="empty">ఈ పేజీ దొరకలేదు. <a href="#/">హోమ్ పేజీకి వెళ్లండి</a>.</p>`; }

  function route(){
    const h = location.hash.replace(/^#\/?/, '').split('/').filter(Boolean).map(decodeURIComponent);
    if(h[0] === 'parva' && h[1] && h[2]) episode(h[1], h[2]);
    else if(h[0] === 'parva' && h[1]) parva(h[1]);
    else if(h[0] === 'patralu') characters(h[1]);
    else if(h[0] === 'patra' && h[1]) character(h[1]);
    else if(h[0] === 'guruvulu') gurus();
    else if(h[0] === 'vetuku') search(h[1]);
    else if(h[0] === 'parinamam') evolution();
    else home();
    window.scrollTo(0,0);
  }
  const hs = document.getElementById('hsearch');
  if(hs) hs.addEventListener('submit', ev => { ev.preventDefault(); location.hash = '#/vetuku/' + encodeURIComponent(hs.q.value); hs.q.value=''; });
  window.addEventListener('hashchange', route);
  route();
})();
