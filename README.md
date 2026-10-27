# monitoracontabil-site — o site institucional (monitoracontabil.com.br)

**Publicar é commit e push neste repositório.** O site vai ao ar por **GitHub
Pages**, direto do `main`, em ~40 s. A raiz do repo **é** a raiz do site, e o
`CNAME` com o domínio mora aqui.

Na máquina do dono, este repositório é a pasta `site/` do projeto
`monitora-contabil` (que a ignora no `.gitignore`), como no zap-do-representante-site.
Até 27/10/2026, `site/` era só uma cópia dentro do monitora-contabil, e publicar
era copiar à mão para cá: em 03/09 o site ficou no ar com a marca antiga porque
ninguém copiou, e de 09/10 a 27/10 com o preço velho.

## A página principal

Desde 08/10/2026 a raiz é o site na marca nova (o guia está em `marca/guia.html`).
HTML, CSS e JS puros, sem biblioteca e sem build, escritos para o celular primeiro.

| Arquivo | O que é |
|---|---|
| `index.html` | a página inteira; a íris vai desenhada dentro dela, sem imagem |
| `estilo.css` | celular primeiro; `@media (min-width)` só acrescenta para tela maior |
| `site.js` | o mergulho na íris, a Alice digitando, o topo que troca de cor |
| `favicon.svg` | a íris sobre azul-tinta (vale para o site, o blog e as páginas legais) |
| `og.png` | o cartão que aparece quando alguém compartilha o link (1200 × 630) |
| `marca.css` | o logotipo (a íris no "o"), num lugar só: a página principal, as legais e o blog carregam |
| `fontes/` | a IBM Plex servida pelo próprio site (licença OFL em `fontes/OFL.txt`); nenhuma página pede nada ao Google |

O cinema do topo é um mergulho na íris guiado pela rolagem, em cinco momentos
(guia, seção 9). Nada anima por relógio. Com "reduzir movimento" ligado, ou sem
JavaScript, os momentos aparecem parados, um embaixo do outro. Os números do cinema
são ilustrativos, e a página diz isso.

Para ver aqui: `python3 -m http.server 5397 --directory site` e abra http://localhost:5397.

Desde 08/10/2026 (#424) o site inteiro está na marca nova: a página principal, a
Política, os Termos e o blog, com a letra servida pelo próprio site.

`site-novo/` só redireciona para a raiz, para quem guardou o link da fase de teste.

## Ser encontrado (Google, Bing e as IAs)

Um site bonito que ninguém acha não vende. O que cada peça faz:

| Peça | Para quê |
|---|---|
| `<title>`, descrição e `<h1>` da raiz | dizem **o que é** (software de produtividade para escritório de contabilidade), não só a frase de efeito |
| JSON-LD do `<head>` | Organization, WebSite (faz o Google mostrar "Monitora Contábil" no lugar do domínio), SoftwareApplication com os três planos |
| seção `#perguntas` | respostas que começam pela resposta: é o trecho que o Google e as IAs citam |
| `_fonte/respostas.py` | grava, a partir da seção `#perguntas`, o FAQPage do `<head>` e o `llms.txt`. **Não edite os dois à mão** |
| `llms.txt` | o resumo em Markdown para quem lê o site como modelo de linguagem |
| `logo.png` | a íris em 512 px, o logo que o Google pede no Organization |
| `<chave>.txt` na raiz | a chave do IndexNow, que avisa o Bing (e quem usa o índice dele, como o ChatGPT) na hora em que uma página muda |

O "o" do logotipo é a íris no desenho e uma letra escondida no texto (`.sr`): sem
ela, o Google e o leitor de tela liam "M nitora".

Depois de publicar uma mudança, avise o Bing pelo IndexNow (a chave é o nome do
arquivo `.txt` de 32 caracteres na raiz):

```
K=$(basename site/????????????????????????????????.txt .txt)
curl -s -X POST https://api.indexnow.org/indexnow -H 'Content-Type: application/json' \
  -d "{\"host\":\"monitoracontabil.com.br\",\"key\":\"$K\",\"urlList\":[\"https://monitoracontabil.com.br/\"]}"
```

## Publicar

```
cd site && git add -A && git commit -m "…" && git push
```

O Pages publica em ~40 s. A API, o painel e o chat são outro caminho: o
`monitora-deploy`, no droplet do console, a partir do `monitora-contabil`.

A calculadora lê o preço da API (`/api/publico/*`): mudança de preço sobe primeiro
na API e depois aqui.

## Blog

```
# 1. acrescente a entrada em _fonte/artigos_juridico.py ou _fonte/artigos_gestao.py
python3 _fonte/gerar-blog.py        # reescreve blog/, o índice, o sitemap.xml e o llms.txt
#    o mesmo comando fotografa o cartão de link de cada artigo em blog/og/<slug>.jpg
#    (precisa do Google Chrome e do sips do macOS; a fonte fica em _fonte/og/,
#    que não é versionada nem publicada)
```

`_fonte/` é a fonte do blog. Ela fica no repositório (o Pages a serve, e não há
nada nela além dos textos e dos geradores); só `_fonte/og/`, as imagens de
origem dos cartões, fica fora (`.gitignore`).

## O que havia aqui antes

Uma pasta `deploy/` com `nginx.conf`, `preparar-droplet.sh`, `subir-site.sh` e um
README descrevendo um droplet dedicado com nginx e certbot. **Esse droplet nunca
existiu** — foi um plano que ficou escrito como se fosse a realidade, e custou
caro: instruções de deploy erradas foram dadas duas vezes com base nele. Removida
em 03/09/2026.
