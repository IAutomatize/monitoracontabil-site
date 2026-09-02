(function(){
  const RM = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const track = document.getElementById('track');
  const stage = document.getElementById('stage');
  const vision = document.getElementById('vision');

  const clamp = (v,a=0,b=1)=>v<a?a:v>b?b:v;
  const seg = (p,a,b)=>clamp((p-a)/(b-a));
  const outCubic = t=>1-Math.pow(1-t,3);
  const inOut = t=>t<.5?4*t*t*t:1-Math.pow(-2*t+2,3)/2;

  /* ---- roteiro (0 a 1 do scroll do palco) ---- */
  const SCRIPT = {
    reveal : [0.02, 0.32],
    turn   : [0.36, 0.66],   // o mergulho na pupila
    transit: [0.38, 0.60],
    arrive : [0.61, 0.81],
    lines  : [0.70, 0.92]
  };

  /* Quanto a camera precisa avancar para a pupila cobrir a tela.
     Medido da largura de layout (nao afetada pelo transform). */
  const media = document.querySelector('.eye-media');
  let DIVE = 14;
  function measureDive(){
    const mw = parseFloat(getComputedStyle(media).width) || 600;
    const pupil = mw * 0.155;                    // pupila = 15.5% da foto
    DIVE = clamp(Math.hypot(innerWidth, innerHeight) / pupil * 1.15, 6, 34);
  }

  const metrics = [...document.querySelectorAll('.metric')];
  const chips   = [...document.querySelectorAll('.chip')];
  const counts  = [...document.querySelectorAll('[data-count]')];
  const leitura = document.querySelector('.leitura');

  let ticking = false, pA = 0;
  function render(){
    ticking = false;
    const max = track.offsetHeight - innerHeight;
    const p = clamp(max > 0 ? (-track.getBoundingClientRect().top) / max : 0);

    pA = seg(p, ...SCRIPT.reveal);
    const pB  = seg(p, ...SCRIPT.turn);
    const pC  = outCubic(seg(p, ...SCRIPT.arrive));
    const pTr = seg(p, ...SCRIPT.transit);
    const pT  = Math.sin(pTr * Math.PI);

    /* Escala EXPONENCIAL: numa aproximacao real a velocidade aparente
       e proporcional a distancia. Linear aqui pareceria travar no fim. */
    const dive = RM ? 1 : Math.pow(DIVE, Math.pow(pB, 1.25));
    const blur = RM ? 0 : Math.max(0, pB - .55) * 16;

    const fade  = seg(p, SCRIPT.turn[0] + .78 * (SCRIPT.turn[1] - SCRIPT.turn[0]), SCRIPT.turn[1]);
    const scrim = seg(p, SCRIPT.turn[0] + .70 * (SCRIPT.turn[1] - SCRIPT.turn[0]), SCRIPT.turn[1]);

    const s = stage.style;
    s.setProperty('--pA', pA.toFixed(4));
    s.setProperty('--pB', (RM ? 0 : pB).toFixed(4));
    s.setProperty('--pTr', pTr.toFixed(4));
    s.setProperty('--dive', dive.toFixed(4));
    s.setProperty('--eyeblur', blur.toFixed(2) + 'px');
    s.setProperty('--pC', pC.toFixed(4));
    s.setProperty('--pT', pT.toFixed(4));
    s.setProperty('--fade', (RM ? seg(p, ...SCRIPT.turn) : fade).toFixed(4));
    s.setProperty('--scrim', scrim.toFixed(4));

    const [la, lb] = SCRIPT.lines, st = (lb - la) / 5;
    for (let i = 0; i < 3; i++)
      s.setProperty('--l' + (i+1), outCubic(seg(p, la + i*st, la + i*st + st*2)).toFixed(4));

    metrics.forEach((el,i)=> el.classList.toggle('on', pA > 0.10 + i * 0.15));
    leitura.classList.toggle('on', pA > 0.76);
    chips.forEach((el,i)=> el.classList.toggle('on', pA > 0.36 + i * 0.22 && pB < 0.14));

    counts.forEach(el=>{
      const t = +el.dataset.count, e = outCubic(clamp(pA * 1.4));
      el.textContent = Math.round(t * e) + (el.dataset.suffix && e > .98 ? el.dataset.suffix : '');
    });

    vision.style.pointerEvents = pC > 0.85 ? 'auto' : 'none';
    vision.setAttribute('aria-hidden', pC > 0.5 ? 'false' : 'true');
  }
  const onScroll = ()=>{ if(!ticking){ ticking = true; requestAnimationFrame(render); } };
  addEventListener('scroll', onScroll, {passive:true});
  addEventListener('resize', ()=>{ fit(); measureDive(); onScroll(); });

  /* ============================================================
     GRÁFICO VIVO NA PUPILA
     ============================================================ */
  const cv = document.getElementById('cv'), ctx = cv.getContext('2d');
  let W = 0, H = 0;
  function fit(){
    const dpr = Math.min(devicePixelRatio || 1, 2);
    const r = cv.getBoundingClientRect();
    W = Math.max(40, r.width); H = Math.max(28, r.height);
    cv.width = W * dpr; cv.height = H * dpr;
    ctx.setTransform(dpr,0,0,dpr,0,0);
  }

  const N = 18;
  let bars = [], price = 100;
  const nextBar = ()=>{
    price += (Math.random() - .46) * 4.4; const o = price;
    price += (Math.random() - .46) * 4.4; const c = price;
    return { o, c, h:Math.max(o,c)+Math.random()*2.4, l:Math.min(o,c)-Math.random()*2.4 };
  };
  for (let i = 0; i < N; i++) bars.push(nextBar());

  let last = 0;
  function draw(t){
    if (!W) fit();
    if (t - last > 700){ last = t; bars.push(nextBar()); bars.shift(); }
    ctx.clearRect(0,0,W,H);

    if (pA > 0.02){
      const hi = Math.max(...bars.map(b=>b.h)), lo = Math.min(...bars.map(b=>b.l));
      const y  = v => H - 4 - ((v - lo) / ((hi - lo) || 1)) * (H - 8);
      const bw = W / N, cw = Math.max(1.2, bw * .46);

      bars.forEach((b,i)=>{
        const x = i*bw + bw/2, up = b.c >= b.o;
        ctx.strokeStyle = up ? 'rgba(238,250,252,.85)' : 'rgba(232,80,70,.9)';
        ctx.fillStyle   = up ? 'rgba(238,250,252,.95)' : 'rgba(232,80,70,.96)';
        ctx.lineWidth = Math.max(.7, cw * .22);
        ctx.beginPath(); ctx.moveTo(x, y(b.h)); ctx.lineTo(x, y(b.l)); ctx.stroke();
        const top = y(Math.max(b.o,b.c)), bot = y(Math.min(b.o,b.c));
        ctx.fillRect(x - cw/2, top, cw, Math.max(1, bot - top));
      });

      // media movel em dourado, puxando os raios da iris
      ctx.strokeStyle = 'rgba(224,161,58,.8)'; ctx.lineWidth = 1;
      ctx.beginPath();
      bars.forEach((b,i)=>{
        const w = bars.slice(Math.max(0,i-3), i+1);
        const m = w.reduce((s,k)=>s+k.c,0)/w.length;
        const x = i*bw + bw/2;
        i ? ctx.lineTo(x, y(m)) : ctx.moveTo(x, y(m));
      });
      ctx.stroke();
    }
    requestAnimationFrame(draw);
  }
  fit(); measureDive(); requestAnimationFrame(draw);
  render();
})();

/* ==== bloco ==== */

(function(){
  const RM = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* scroll-reveal das seções claras */
  const alvos = document.querySelectorAll('.reveal');
  if (RM || !('IntersectionObserver' in window)) {
    alvos.forEach(e => e.classList.add('in'));
  } else {
    const io = new IntersectionObserver((ents) => {
      ents.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: .14, rootMargin: '0px 0px -8% 0px' });
    alvos.forEach(e => io.observe(e));
  }

  /* a Alice narrando a semana — dispara quando entra na tela */
  const box = document.getElementById('aliceBubbles');
  if (box) {
    if (RM || !('IntersectionObserver' in window)) chatAlice(box, true);
    else {
      const io2 = new IntersectionObserver((ents) => {
        ents.forEach(e => { if (e.isIntersecting) { chatAlice(box, false); io2.disconnect(); } });
      }, { threshold: .45 });
      io2.observe(box);
    }
  }

  function chatAlice(box, rm){
    const seg = [
      { t: 'A semana veio ' }, { t: '43% de foco', b: 1 },
      { t: ' — abaixo das últimas (61%). O nó é a terça: ' },
      { t: '82 trocas de janela por hora', b: 1 },
      { t: ', e nenhum trecho chega a 25 min. A Marina segurou a média, com 3 blocos de foco profundo.' }
    ];
    const add = (cls, html) => {
      const d = document.createElement('div'); d.className = 'bubble ' + cls; d.innerHTML = html;
      box.appendChild(d); requestAnimationFrame(() => d.classList.add('show')); return d;
    };
    const addAct = () => {
      const a = document.createElement('a'); a.className = 'alice-act';
      a.href = 'https://plataforma.monitoracontabil.com.br/cadastro';
      a.textContent = 'Ver a terça da equipe →';
      box.appendChild(a); requestAnimationFrame(() => a.classList.add('show'));
    };
    const doAlice = () => {
      const b = add('alice', '');
      if (rm) { b.innerHTML = seg.map(s => s.b ? '<b>' + s.t + '</b>' : s.t).join(''); addAct(); return; }
      const cursor = document.createElement('span'); cursor.className = 'cursor'; b.appendChild(cursor);
      let si = 0, ci = 0, node = null;
      const tick = () => {
        if (si >= seg.length) { cursor.remove(); addAct(); return; }
        const sg = seg[si];
        if (ci === 0) { node = sg.b ? document.createElement('b') : document.createTextNode(''); b.insertBefore(node, cursor); }
        if (ci < sg.t.length) { node.textContent = sg.t.slice(0, ci + 1); ci++; setTimeout(tick, 15 + Math.random() * 26); }
        else { si++; ci = 0; setTimeout(tick, 45); }
      };
      tick();
    };
    add('user', 'Como foi a semana da equipe?');
    if (rm) { doAlice(); return; }
    setTimeout(() => {
      const t = add('alice', '<span class="typing"><span></span><span></span><span></span></span>');
      setTimeout(() => { t.remove(); doAlice(); }, 1150);
    }, 560);
  }
})();
