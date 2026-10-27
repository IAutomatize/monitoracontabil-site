/*
  A CALCULADORA (#503) — entre "Você não está vigiando o seu time" e
  "Saiba para onde vai o dia que o seu escritório paga".

  O que ela promete:
   · abre com o preço por computador (está no HTML, funciona sem JavaScript);
   · a primeira escolha é mensal ou anual, num seletor de duas posições;
   · o total só aparece DEPOIS que a pessoa digita quantos computadores;
   · a ajuda na implantação NÃO é pergunta: é obrigatória (dono, 27/10/2026).
     O resultado diz quanto ela custa, ou que é grátis no anual;
   · a conta vem da API (POST /api/publico/orcamento) — o preço mora no
     backend, nunca escrito aqui. Fora do ar, mostra só o preço por computador
     e o botão, sem total inventado;
   · nada de mínimo: aceita a partir de 1. O mínimo só aparece na contratação;
   · o botão leva ao cadastro com a escolha na URL (computadores, ciclo,
     cupom), e o painel a carrega até a contratação.
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
      const partes = [
        anual ? total(o.recorrente.valorCentavos, '/ano') : total(o.mensalidadeCheiaCentavos, '/mês'),
        el('p', 'calc-linha', `${n} ${n === 1 ? 'computador' : 'computadores'} × ${brl(o.precoPorComputadorCentavos)}${anual ? ' × 12 meses' : ''}`),
        o.adesao.cobradaCentavos === 0
          ? el('p', 'calc-linha ok', anual ? 'Ajuda na implantação grátis no anual' : 'Ajuda na implantação grátis')
          : el('p', 'calc-linha', `+ ${brl(o.adesao.cobradaCentavos)} de ajuda na implantação, uma vez`),
      ];
      if (o.teste) partes.push(el('p', 'calc-linha ok', `${o.teste.dias} dias grátis antes da primeira mensalidade`));
      if (c) partes.push(el('p', c.aplicado ? 'calc-linha ok' : 'calc-linha', c.mensagem));
      if (c && c.aplicado) {
        partes.push(el('p', 'calc-linha', `Com o cupom, hoje: ${brl(o.hoje.totalCentavos)}. Depois, ${brl(o.recorrente.valorCentavos)} ${anual ? 'por ano' : 'por mês'}.`));
      }
      resultado.replaceChildren(...partes);
      resultado.hidden = false;
    } catch {
      if (meu !== pedido) return;
      // fora do ar: o preço por computador e o botão, nunca um total inventado
      // o preço por computador já está no título da seção: aqui, sem número nenhum
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
})();
