/*
  SITE — o que precisa de JavaScript, e só isso.

  1. O MERGULHO NA ÍRIS. O roteiro está no guia (marca/guia.html, seção 9),
     em cinco momentos ao longo da rolagem do .trilho:
       0–26%   a abertura: a íris se forma e o texto se apresenta
       24–44%  a câmera aproxima e os números do dia aparecem em volta
       44–64%  o mergulho: a pupila âmbar (a Alice) cresce até cobrir a tela
       66–88%  dentro da pupila: o dia em barra, com os números contando
       86–100% a virada para o papel: "você não está vigiando..."
     Cada momento é um trecho [a, b] de p (0 a 1), e cada peça lê o seu trecho.
     Nada anima por relógio: só a rolagem move, então quem para de rolar vê
     a cena parada, e quem volta vê a cena voltar.

  2. A ALICE DIGITANDO, quando a conversa aparece na tela.
  3. O TOPO, que troca de escuro para claro quando o cinema acaba.
  4. O SURGIMENTO SUAVE das seções.

  Com "reduzir movimento" ligado, o <head> não liga o .com-movimento, e
  nada disto anima: o cinema fica parado e a Alice aparece com o texto pronto.
*/
(() => {
  window.__siteOk = true;
  const raiz = document.documentElement;
  const movimento = raiz.classList.contains('com-movimento');
  const topo = document.querySelector('.topo');
  const trilho = document.querySelector('.trilho');
  const palco = document.querySelector('.palco');
  const iris = document.querySelector('.iris-hero');
  const abertura = document.querySelector('.abertura');
  const chips = [...document.querySelectorAll('.chip')];
  const mergulho = document.querySelector('.mergulho');
  const dia = document.querySelector('.dia');
  const virada = document.querySelector('.virada');
  const frase = virada.querySelector('.frase');
  const numeros = [...dia.querySelectorAll('.num')];

  const lim = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
  const trecho = (p, a, b) => lim((p - a) / (b - a));
  const suave = (t) => (t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2);
  const freia = (t) => 1 - Math.pow(1 - t, 3);
  const acelera = (t) => t * t * t;
  // arredonda o total antes de dividir: arredondar só os minutos daria "3h60"
  const hm = (min) => { const m = Math.round(min); return `${Math.floor(m / 60)}h${String(m % 60).padStart(2, '0')}`; };

  /* A escala do mergulho depende da tela: a pupila tem de crescer até cobrir
     o canto mais distante do centro da íris. Medido, não chutado. */
  const PUPILA = (2 * 7.41) / 64;              // diâmetro da pupila ÷ largura da íris
  let mergulhoMax = 20;
  let deslocaX = 0;
  function medir() {
    const w = innerWidth, h = innerHeight;
    const y = (parseFloat(getComputedStyle(palco).getPropertyValue('--iris-y')) || 60) / 100 * h;
    const raio = Math.hypot(w / 2, Math.max(y, h - y));
    // <svg> não tem offsetWidth: mede sem escala nem giro, e o cinema() devolve o transform
    iris.style.transform = 'translate(-50%, -50%)';
    const tam = iris.getBoundingClientRect().width || 300;
    mergulhoMax = ((2 * raio) / (tam * PUPILA)) * 1.08;
    deslocaX = w >= 1020 ? w * 0.2 : 0;       // no desktop a íris começa à direita do texto
  }

  function cinema() {
    const total = trilho.offsetHeight - innerHeight;
    const p = lim(total > 0 ? -trilho.getBoundingClientRect().top / total : 0);

    const saiAbertura = trecho(p, .14, .26);
    abertura.style.opacity = String(1 - saiAbertura);
    abertura.style.translate = `0 ${-24 * saiAbertura}px`;

    const aproxima = suave(trecho(p, .24, .44));
    const mergulha = acelera(trecho(p, .44, .64));
    const escala = mergulha > 0 ? 1.55 * Math.pow(mergulhoMax / 1.55, mergulha) : 1 + .55 * aproxima;
    const x = deslocaX * (1 - aproxima);
    iris.style.transform = `translate(calc(-50% + ${x}px), -50%) scale(${escala}) rotate(${p * 70}deg)`;
    iris.style.opacity = String(1 - trecho(p, .63, .67));

    const chipEntra = trecho(p, .28, .34);
    const chipSai = trecho(p, .42, .48);
    chips.forEach((c) => {
      c.style.opacity = String(chipEntra * (1 - chipSai));
      c.style.translate = `0 ${(1 - chipEntra) * 10 - chipSai * 10}px`;
    });

    // o âmbar chapado só entra quando a pupila já cobre quase tudo: antes disso,
    // âmbar translúcido sobre o azul vira um verde-oliva sujo
    mergulho.style.opacity = String(trecho(p, .625, .645) * (1 - trecho(p, .66, .72)));

    dia.style.opacity = String(trecho(p, .66, .72) * (1 - trecho(p, .86, .9)));
    const cresce = freia(trecho(p, .7, .82));
    dia.style.setProperty('--cresce', `${(cresce * 100).toFixed(2)}%`);
    numeros.forEach((n) => {
      const v = Number(n.dataset.conta) * cresce;
      n.textContent = n.dataset.formato === 'h' ? `${Math.round(v)}h` : hm(v);
    });

    virada.style.opacity = String(trecho(p, .86, .93));
    frase.style.translate = `0 ${(1 - trecho(p, .86, .95)) * 24}px`;

    topo.dataset.tema = p > .9 ? 'claro' : 'escuro';
  }

  /* sem movimento, o topo fica escuro enquanto houver cinema escuro atrás dele */
  function topoParado() {
    topo.dataset.tema = dia.getBoundingClientRect().bottom > topo.offsetHeight ? 'escuro' : 'claro';
  }

  let pedido = false;
  function aoRolar() {
    if (pedido) return;
    pedido = true;
    requestAnimationFrame(() => {
      pedido = false;
      topo.toggleAttribute('data-rolou', scrollY > 8);
      movimento ? cinema() : topoParado();
    });
  }

  if (movimento) { medir(); cinema(); addEventListener('resize', () => { medir(); cinema(); }); }
  else topoParado();
  addEventListener('scroll', aoRolar, { passive: true });

  /* ── a Alice digitando ── */
  const fala = document.querySelector('[data-digita]');
  if (fala && movimento && 'IntersectionObserver' in window) {
    const original = fala.innerHTML;
    const partes = original.split(/(<[^>]+>)/).filter(Boolean);
    fala.innerHTML = '';
    const obs = new IntersectionObserver((entradas) => {
      if (!entradas.some((e) => e.isIntersecting)) return;
      obs.disconnect();
      fala.classList.add('digitando');
      let i = 0, j = 0, feito = '';
      (function passo() {
        if (i >= partes.length) { fala.classList.remove('digitando'); fala.innerHTML = original; return; }
        const parte = partes[i];
        if (parte.startsWith('<')) { feito += parte; i++; }
        else { feito += parte[j++]; if (j >= parte.length) { i++; j = 0; } }
        fala.innerHTML = feito;
        setTimeout(passo, 16);
      })();
    }, { threshold: .6 });
    obs.observe(fala);
  }

  /* ── as seções surgem, de leve ── */
  if (movimento && 'IntersectionObserver' in window) {
    const alvos = document.querySelectorAll('.secao h2, .secao .lead, .cartao, .plano, .passos li, .recusas div, .conversa, .doc-cena');
    alvos.forEach((a) => a.classList.add('reveal'));
    const obs = new IntersectionObserver((entradas) => {
      entradas.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('visto'); obs.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    alvos.forEach((a) => obs.observe(a));
  }
})();
