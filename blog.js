/* ─── Blog — o mínimo de JavaScript ──────────────────────────────────────────
   Três comportamentos, nenhuma dependência, nada que bloqueie a renderização
   (o script é `defer`). A página inteira funciona com o JS desligado: o texto
   está no HTML, os links são links, e o que some é só o conforto.            */
(function () {
  'use strict';

  /* 1. Barra de progresso da leitura.
        Existe só no artigo, e só quando há rolagem suficiente para significar
        alguma coisa — numa página curta ela ficaria cheia o tempo todo. */
  var barra = document.querySelector('.progresso');
  if (barra) {
    var pintar = function () {
      var alcance = document.documentElement.scrollHeight - window.innerHeight;
      if (alcance < 400) { barra.style.width = '0'; return; }
      var pct = (window.scrollY / alcance) * 100;
      barra.style.width = (pct < 0 ? 0 : pct > 100 ? 100 : pct) + '%';
    };
    addEventListener('scroll', pintar, { passive: true });
    addEventListener('resize', pintar);
    pintar();
  }

  /* 2. Compartilhar.
        Usa o menu nativo do sistema quando existe (é o caminho do celular, que
        é onde a maioria compartilha). Sem ele, copia o endereço e diz que
        copiou — botão que não confirma parece botão quebrado. */
  var botao = document.querySelector('[data-share]');
  if (botao) {
    botao.addEventListener('click', function () {
      var dados = {
        title: document.title,
        text: (document.querySelector('meta[name="description"]') || {}).content || '',
        url: location.href
      };
      if (navigator.share) {
        navigator.share(dados).catch(function () { /* cancelar não é erro */ });
        return;
      }
      var rotulo = botao.textContent;
      var pronto = function () {
        botao.textContent = 'Link copiado';
        setTimeout(function () { botao.textContent = rotulo; }, 2000);
      };
      if (navigator.clipboard) {
        navigator.clipboard.writeText(location.href).then(pronto, function () {
          botao.textContent = 'Copie da barra de endereço';
        });
      } else {
        botao.textContent = 'Copie da barra de endereço';
      }
    });
  }

  /* 3. Filtro por assunto, no índice.
        Filtra o que já está na página — sem requisição, sem recarregar. Os
        cartões existem no HTML desde o começo, então quem chega pelo Google
        (e quem está sem JS) vê a lista inteira de qualquer jeito. */
  var filtros = document.querySelectorAll('.filtro');
  if (filtros.length) {
    var posts = document.querySelectorAll('.post');
    var vazio = document.querySelector('.vazio');
    filtros.forEach(function (f) {
      f.addEventListener('click', function () {
        var alvo = f.dataset.cat;
        filtros.forEach(function (o) {
          o.setAttribute('aria-pressed', String(o === f));
        });
        var visiveis = 0;
        posts.forEach(function (p) {
          var mostra = alvo === 'tudo' || p.dataset.cat === alvo;
          p.hidden = !mostra;
          if (mostra) visiveis++;
        });
        if (vazio) vazio.hidden = visiveis > 0;
      });
    });
  }
})();
