# site/site-novo/ — o site na marca nova (prova 1)

Primeira prova do site em HTML, CSS e JS puros, sem biblioteca e sem build.
Escrito para o celular primeiro. A régua é o guia da marca: [`marca/guia.html`](../../marca/guia.html).

**Enquanto for teste, mora numa subpasta do site:** publicada, abre em
**monitoracontabil.com.br/site-novo/**, ao lado do site atual, que continua na raiz.
A página tem `noindex` e não entra no Google.

## Ver aqui

```
python3 -m http.server 5397 --directory site
```

e abra http://localhost:5397/site-novo/. No celular de verdade, use o IP do Mac na mesma rede.

## Publicar o teste

O mesmo caminho do resto do site (ver [`site/README.md`](../README.md)): copiar a pasta
`site-novo/` para a raiz do repositório `IAutomatize/monitoracontabil-site` e dar push.
O GitHub Pages publica em ~40 s.

## O que tem aqui

| Arquivo | O que é |
|---|---|
| `index.html` | a página inteira; a íris vai desenhada dentro dela, sem imagem |
| `estilo.css` | celular primeiro; `@media (min-width)` só acrescenta para tela maior |
| `site.js` | o mergulho na íris, a Alice digitando, o topo que troca de cor |
| `favicon.svg` | a íris sobre azul-tinta |
| `og.png` | a imagem que aparece quando alguém compartilha o link (1200 × 630) |

## O cinema

Rolar é mergulhar na íris, em cinco momentos (guia, seção 9): a abertura, os
números em volta, o mergulho na pupila, o dia dentro dela e a virada para o papel.
Nada anima por relógio, só a rolagem. Com "reduzir movimento" ligado, ou sem
JavaScript, os momentos aparecem parados, um embaixo do outro.

## Quando virar o site principal

- Mover os arquivos para a raiz de `site/`, no lugar do `index.html`, `styles.css` e `app.js` de hoje.
- Trocar o `noindex` por `index,follow`, e tirar o `/site-novo` do canônico, do `og:url` e do `og:image`.
- A **Política de Privacidade** ainda diz que os dados ficam "12 meses, configurável".
  A regra do produto mudou para **36 meses para todo mundo** em 01/10/2026, e esta
  página já diz 36. A política precisa ser revista antes, porque é texto jurídico.
- As fontes vêm do Google Fonts. O guia pede que venham junto com o produto: servir
  os arquivos da IBM Plex daqui mesmo.
- Os números do cinema e do resumo da semana são ilustrativos, e a página diz isso.
