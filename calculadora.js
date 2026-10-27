/*
  A CALCULADORA (#503) — entre "Você não está vigiando o seu time" e
  "Saiba para onde vai o dia que o seu escritório paga".

  O que ela promete:
   · abre com o preço por computador (está no HTML, funciona sem JavaScript);
   · a primeira escolha é mensal ou anual, num seletor de duas posições;
   · o total só aparece DEPOIS que a pessoa digita quantos computadores;
   · a ajuda na implantação NÃO é pergunta: é obrigatória (dono, 27/10/2026).
     O resultado diz quanto ela custa, ou que é grátis no anual;
   · com cupom, o valor com desconto em destaque e o de antes riscado embaixo —
     sem texto explicando o cupom (o dono, 27/10/2026: "só pega o valor");
   · a conta vem da API (POST /api/publico/orcamento) — o preço mora no
     backend, nunca escrito aqui. Fora do ar, mostra só o preço por computador
     e o botão, sem total inventado;
   · nada de mínimo: aceita a partir de 1. O mínimo só aparece na contratação;
   · o botão leva ao cadastro com a escolha na URL (computadores, ciclo,
     cupom), e o painel a carrega até a contratação;
   · a página /calculadora (o QR do estande) usa este mesmo arquivo, e a
     escolha pode vir na URL: ?cupom=, ?computadores=, ?ciclo=anual.
*/
(() => {
  const raiz = document.getElementById('calculadora');
  if (!raiz) return;
  const local = /^(localhost|127\.0\.0\.1)$/.test(location.hostname);
  const API = local ? 'http://localhost:5198' : 'https://api.monitoracontabil.com.br';
  const CADASTRO = local ? 'http://localhost:5199/cadastro' : 'https://plataforma.monitoracontabil.com.br/cadastro';

  const $ = (s) => raiz.querySelector(s);
  const controles = $('.calc-controles');
  const qtd = $('#calc-qtd');
  const ciclos = [...raiz.querySelectorAll('.calc-ciclo [data-ciclo]')];
  const cupomCampo = $('#calc-cupom');
  const cupomBotao = $('#calc-cupom-aplicar');
  const cupomAviso = $('#calc-cupom-aviso');
  const resultado = $('.calc-resultado');
  const cta = $('#calc-cta');
  controles.hidden = false;

  const brl = (centavos) => (centavos / 100).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
  let ciclo = 'mensal';
  let cupom = '';
  let pedido = 0;

  function linkDoCadastro(n) {
    const p = new URLSearchParams();
    if (n > 0) p.set('computadores', String(n));
    p.set('ciclo', ciclo);
    if (cupom) p.set('cupom', cupom);
    return `${CADASTRO}?${p}`;
  }

  function el(tag, classe, texto) {
    const x = document.createElement(tag);
    x.className = classe;
    if (texto) x.textContent = texto;
    return x;
  }

  function total(valor, periodo) {
    const p = el('p', 'calc-total', brl(valor));
    p.append(el('small', '', periodo));
    return p;
  }

  async function calcular() {
    const n = Number(qtd.value.replace(/\D/g, ''));
    cta.href = linkDoCadastro(n || 0);
    if (!n) { resultado.replaceChildren(); resultado.hidden = true; return; }
    const anual = ciclo === 'anual';
    const meu = ++pedido;
    try {
      const r = await fetch(`${API}/api/publico/orcamento`, {
        method: 'POST',
        headers: { 'content-type': 'application/json' },
        body: JSON.stringify({ quantidade: Math.min(n, 10000), ciclo, cupom: cupom || null }),
      });
      if (!r.ok) throw new Error(String(r.status));
      const { orcamento: o, cupom: c } = await r.json();
      if (meu !== pedido) return;
      const periodo = anual ? '/ano' : '/mês';
      const cheio = anual ? o.mensalidadeCheiaCentavos * 12 : o.mensalidadeCheiaCentavos;
      // com cupom, o valor do 1º período: o que sai hoje, sem a ajuda na implantação
      const comCupom = c && c.aplicado ? Math.max(0, o.hoje.totalCentavos - o.adesao.cobradaCentavos) : cheio;
      const partes = [];
      if (comCupom < cheio) {
        // o valor com desconto em destaque, e o de antes embaixo, riscado
        const novo = el('p', 'calc-total desconto', comCupom === 0 ? 'Grátis' : brl(comCupom));
        if (comCupom > 0) novo.append(el('small', '', periodo));
        partes.push(novo, el('p', 'calc-de', brl(cheio)));
      } else {
        partes.push(total(cheio, periodo));
      }
      partes.push(el('p', 'calc-linha', `${n} ${n === 1 ? 'computador' : 'computadores'} × ${brl(o.precoPorComputadorCentavos)}${anual ? ' × 12 meses' : ''}`));
      if (o.adesao.cobradaCentavos === 0) {
        partes.push(el('p', 'calc-linha ok', anual ? 'Ajuda na implantação grátis no anual' : 'Ajuda na implantação grátis'));
      } else {
        partes.push(el('p', 'calc-linha', `+ ${brl(o.adesao.cobradaCentavos)} de ajuda na implantação, uma vez`));
      }
      if (o.teste) partes.push(el('p', 'calc-linha ok', `${o.teste.dias} dias grátis antes da primeira mensalidade`));
      resultado.replaceChildren(...partes);
      resultado.hidden = false;
      // o retorno do cupom fica junto do campo dele, curto
      cupomAviso.textContent = c ? (c.aplicado ? '✓ Cupom aplicado' : c.mensagem) : '';
      cupomAviso.className = `calc-cupom-aviso${c && c.aplicado ? ' ok' : ''}`;
    } catch {
      if (meu !== pedido) return;
      // fora do ar: nunca um total inventado (o preço por computador já está no título)
      resultado.replaceChildren(el('p', 'calc-linha', 'Não conseguimos calcular o total agora. O preço por computador está logo acima.'));
      resultado.hidden = false;
    }
  }

  function escolherCiclo(novo) {
    ciclo = novo;
    for (const b of ciclos) b.setAttribute('aria-checked', String(b.dataset.ciclo === novo));
    calcular();
  }

  let espera;
  const recalcular = () => { clearTimeout(espera); espera = setTimeout(calcular, 250); };
  qtd.addEventListener('input', () => { qtd.value = qtd.value.replace(/\D/g, '').slice(0, 5); recalcular(); });
  $('#calc-menos').addEventListener('click', () => { qtd.value = String(Math.max(1, (Number(qtd.value) || 1) - 1)); calcular(); });
  $('#calc-mais').addEventListener('click', () => { qtd.value = String(Math.min(10000, (Number(qtd.value) || 0) + 1)); calcular(); });
  for (const b of ciclos) {
    b.addEventListener('click', () => escolherCiclo(b.dataset.ciclo));
    // setas trocam a escolha, como num grupo de rádio
    b.addEventListener('keydown', (e) => {
      if (e.key !== 'ArrowLeft' && e.key !== 'ArrowRight') return;
      e.preventDefault();
      const outro = ciclos.find((x) => x !== b);
      outro.focus();
      escolherCiclo(outro.dataset.ciclo);
    });
  }
  cupomBotao.addEventListener('click', () => { cupom = cupomCampo.value.trim().replace(/[^A-Za-z0-9_-]/g, ''); calcular(); });
  cupomCampo.addEventListener('keydown', (e) => { if (e.key === 'Enter') { e.preventDefault(); cupomBotao.click(); } });
  cta.href = linkDoCadastro(0);

  // A escolha pela URL — o QR do estande leva o cupom do evento:
  // /calculadora?cupom=CODIGO (e ?computadores=10, ?ciclo=anual)
  const url = new URLSearchParams(location.search);
  const doLink = (url.get('cupom') ?? '').replace(/[^A-Za-z0-9_-]/g, '').slice(0, 40);
  if (doLink) { cupom = doLink; cupomCampo.value = doLink; $('.calc-cupom').open = true; }
  const n = Number(url.get('computadores'));
  if (Number.isInteger(n) && n > 0 && n <= 10000) qtd.value = String(n);
  if (url.get('ciclo') === 'anual') escolherCiclo('anual');
  else if (doLink || qtd.value) calcular();
})();
