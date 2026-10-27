/*
  A CALCULADORA (#503) — entre "Você não está vigiando o seu time" e
  "Saiba para onde vai o dia que o seu escritório paga".

  O que ela promete:
   · abre com R$ 29,90 por computador (está no HTML, funciona sem JavaScript);
   · o total do mês só aparece DEPOIS que a pessoa digita quantos computadores;
   · a conta vem da API (POST /api/publico/orcamento) — o preço mora no
     backend, nunca escrito aqui. Fora do ar, mostra só o preço por computador
     e o botão, sem total inventado;
   · nada de mínimo: aceita a partir de 1. O mínimo só aparece na contratação;
   · o botão leva ao cadastro com a escolha na URL (computadores, ajuda, ciclo,
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
  const ajuda = $('#calc-ajuda');
  const anual = $('#calc-anual');
  const cupomCampo = $('#calc-cupom');
  const cupomBotao = $('#calc-cupom-aplicar');
  const resultado = $('.calc-resultado');
  const cta = $('#calc-cta');
  controles.hidden = false;

  const brl = (centavos) => (centavos / 100).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
  let cupom = '';
  let pedido = 0;

  function linkDoCadastro(n) {
    const p = new URLSearchParams();
    if (n > 0) p.set('computadores', String(n));
    p.set('ajuda', ajuda.checked ? '1' : '0');
    p.set('ciclo', anual.checked ? 'anual' : 'mensal');
    if (cupom) p.set('cupom', cupom);
    return `${CADASTRO}?${p}`;
  }

  function linha(texto, forte) {
    const el = document.createElement('p');
    el.className = forte ? 'calc-total' : 'calc-linha';
    el.textContent = texto;
    return el;
  }

  async function calcular() {
    const n = Number(qtd.value.replace(/\D/g, ''));
    cta.href = linkDoCadastro(n || 0);
    if (!n) { resultado.replaceChildren(); resultado.hidden = true; cta.textContent = 'Começar 7 dias grátis'; return; }
    const meu = ++pedido;
    try {
      const r = await fetch(`${API}/api/publico/orcamento`, {
        method: 'POST',
        headers: { 'content-type': 'application/json' },
        body: JSON.stringify({ quantidade: Math.min(n, 10000), ciclo: anual.checked ? 'anual' : 'mensal', comAjuda: ajuda.checked, cupom: cupom || null }),
      });
      if (!r.ok) throw new Error(String(r.status));
      const { orcamento: o, cupom: c } = await r.json();
      if (meu !== pedido) return;
      const partes = [];
      partes.push(linha(anual.checked
        ? `${brl(o.recorrente.valorCentavos)} por ano`
        : `${brl(o.mensalidadeCheiaCentavos)} por mês`, true));
      partes.push(linha(`${n} ${n === 1 ? 'computador' : 'computadores'} × ${brl(o.precoPorComputadorCentavos)}${anual.checked ? ' × 12 meses' : ''}`));
      if (ajuda.checked) {
        partes.push(linha(o.adesao.cobradaCentavos === 0
          ? 'Ajuda na implantação: grátis'
          : `Ajuda na implantação: ${brl(o.adesao.cobradaCentavos)}, uma vez`));
      }
      if (c) partes.push(linha(c.mensagem));
      if (c && c.aplicado) {
        partes.push(linha(`Com o cupom, hoje: ${brl(o.hoje.totalCentavos)}. Depois, ${brl(o.recorrente.valorCentavos)} ${anual.checked ? 'por ano' : 'por mês'}.`));
      }
      if (o.teste) partes.push(linha(`Os ${o.teste.dias} primeiros dias são grátis.`));
      resultado.replaceChildren(...partes);
      resultado.hidden = false;
      cta.textContent = o.teste ? 'Começar 7 dias grátis' : 'Contratar';
    } catch {
      if (meu !== pedido) return;
      // fora do ar: o preço por computador e o botão, nunca um total inventado
      resultado.replaceChildren(linha('R$ 29,90 por computador por mês. Não conseguimos calcular o total agora.'));
      resultado.hidden = false;
    }
  }

  let espera;
  const recalcular = () => { clearTimeout(espera); espera = setTimeout(calcular, 250); };
  qtd.addEventListener('input', () => { qtd.value = qtd.value.replace(/\D/g, '').slice(0, 5); recalcular(); });
  $('#calc-menos').addEventListener('click', () => { qtd.value = String(Math.max(1, (Number(qtd.value) || 1) - 1)); calcular(); });
  $('#calc-mais').addEventListener('click', () => { qtd.value = String(Math.min(10000, (Number(qtd.value) || 0) + 1)); calcular(); });
  ajuda.addEventListener('change', calcular);
  anual.addEventListener('change', calcular);
  cupomBotao.addEventListener('click', () => { cupom = cupomCampo.value.trim().replace(/[^A-Za-z0-9_-]/g, ''); calcular(); });
  cupomCampo.addEventListener('keydown', (e) => { if (e.key === 'Enter') { e.preventDefault(); cupomBotao.click(); } });
  cta.href = linkDoCadastro(0);
})();
