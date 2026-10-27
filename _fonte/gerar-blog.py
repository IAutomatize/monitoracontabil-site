#!/usr/bin/env python3
"""
GERADOR DO BLOG — um template, dez artigos, zero divergência.

Por que gerar em vez de escrever dez arquivos à mão: o que faz um artigo ser
encontrado e compartilhado não é o texto, é o CABEÇALHO — canonical, Open Graph,
Twitter card, JSON-LD. São ~25 linhas idênticas em cada página, e à mão elas
divergem no terceiro arquivo: um esquece o `og:image`, outro fica com a
descrição do anterior colada. Aqui o cabeçalho existe UMA vez.

O conteúdo mora em `artigos.py`. Para publicar um artigo novo: acrescente a
entrada lá e rode

    python3 site/_fonte/gerar-blog.py

que reescreve `site/blog/*.html`, o índice, o `sitemap.xml` e, pelo
`respostas.py`, o `llms.txt`. Os HTML gerados SÃO versionados — o GitHub Pages
não roda Python.

Esta pasta (`_fonte`) não vai para o repo do site: é fonte, não site. Por isso a
fonte dos cartões de compartilhamento fica em `_fonte/og/`; só o JPG vai para
`blog/og/`.
"""
import json
import os
import re
import shutil
import subprocess
import tempfile
import unicodedata
from datetime import date

import respostas
from artigos import ARTIGOS

SITE = 'https://monitoracontabil.com.br'
APP = 'https://plataforma.monitoracontabil.com.br'
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
BLOG = os.path.join(RAIZ, 'blog')
OGDIR = os.path.join(AQUI, 'og')

# O logotipo (marca/guia.html, seção 02): a íris no lugar do primeiro "o", e a
# letra escondida (.sr) para o nome continuar inteiro no texto. O estilo mora em
# site/marca.css, o mesmo da página principal e das páginas legais.
IRIS_O = ('<svg class="o" viewBox="0 0 64 64" aria-hidden="true">'
          '<circle cx="32" cy="32" r="25.75" fill="none" stroke="currentColor" stroke-width="11.5"/>'
          '<circle cx="32" cy="32" r="8.97" fill="#f5b93d"/></svg>')
LOGOTIPO = f'<span class="wm">M{IRIS_O}<span class="sr">o</span>nitora <span class="c">Contábil</span></span>'

# A letra vem do próprio site (site/fontes), não do Google.
FONTES = ('<link rel="stylesheet" href="/fontes/plex.css">\n'
          '<link rel="stylesheet" href="/marca.css">')

CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

# A íris cheia do fundo do cartão sai da geometria da marca (marca/iris.py):
# com 500 px, ela leva as três fatias; a simples é só para o tamanho de letra.
import sys  # noqa: E402
sys.path.insert(0, os.path.join(os.path.dirname(RAIZ), 'marca'))
from iris import formas  # noqa: E402
IRIS_CHEIA = formas({'tema': 'noite', 'pupila': 'ambar'})


def texto_puro(html: str) -> str:
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', html)).strip()


def minutos(html: str) -> int:
    """Tempo de leitura a 200 palavras/min — a régua usual em português."""
    return max(1, round(len(texto_puro(html).split()) / 200))


def escapar(s: str) -> str:
    return (s.replace('&', '&amp;').replace('<', '&lt;')
             .replace('>', '&gt;').replace('"', '&quot;'))


def data_br(iso: str) -> str:
    a, m, d = iso.split('-')
    meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho',
             'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
    return f'{int(d)} de {meses[int(m) - 1]} de {a}'


def topo(ativo_blog: bool = True) -> str:
    return f'''<header class="topo"><div class="topo-in">
  <a class="topo-marca" href="/" aria-label="Monitora Contábil, início">{LOGOTIPO}</a>
  <nav class="topo-nav">
    <a class="some" href="/blog/">Blog</a>
    <a class="some" href="/#produto">O que ele mede</a>
    <a class="topo-cta" href="{APP}/cadastro">Testar 7 dias grátis</a>
  </nav>
</div></header>'''


def rodape() -> str:
    return f'''<footer class="rodape"><div class="rodape-in">
  <span>Monitora Contábil — produtividade para escritórios de contabilidade.</span>
  <nav class="rodape-links">
    <a href="/">Início</a>
    <a href="/blog/">Blog</a>
    <a href="/privacidade">Privacidade</a>
    <a href="/termos">Termos</a>
    <a href="{APP}">Entrar</a>
  </nav>
</div></footer>'''


def cabecalho(titulo, descricao, url, og_img, tipo='article', extra_ld=None) -> str:
    lds = json.dumps(extra_ld, ensure_ascii=False, indent=2) if extra_ld else None
    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#f7f6f2">
<title>{escapar(titulo)}</title>
<meta name="description" content="{escapar(descricao)}">
<link rel="canonical" href="{url}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">
<meta property="og:type" content="{tipo}">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="Monitora Contábil">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{escapar(titulo)}">
<meta property="og:description" content="{escapar(descricao)}">
<meta property="og:image" content="{og_img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:alt" content="{escapar(titulo)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{escapar(titulo)}">
<meta name="twitter:description" content="{escapar(descricao)}">
<meta name="twitter:image" content="{og_img}">
{FONTES}
<link rel="stylesheet" href="/blog.css">
{'<script type="application/ld+json">' + lds + '</script>' if lds else ''}
</head>
<body>'''


def render_artigo(a, todos) -> str:
    url = f'{SITE}/blog/{a["slug"]}'
    og = f'{SITE}/blog/og/{a["slug"]}.jpg'
    mins = minutos(a['corpo'])

    ld = {
        '@context': 'https://schema.org',
        '@graph': [
            {
                '@type': 'BlogPosting',
                '@id': f'{url}#post',
                'headline': a['titulo'],
                'description': a['descricao'],
                'inLanguage': 'pt-BR',
                'datePublished': a['data'],
                'dateModified': a.get('revisado', a['data']),
                'mainEntityOfPage': {'@type': 'WebPage', '@id': url},
                'image': og,
                'articleSection': a['categoria'],
                'wordCount': len(texto_puro(a['corpo']).split()),
                'author': {'@type': 'Organization', 'name': 'Monitora Contábil', 'url': SITE},
                'publisher': {
                    '@type': 'Organization',
                    'name': 'Monitora Contábil',
                    'url': SITE,
                    'logo': {'@type': 'ImageObject', 'url': f'{SITE}/logo.png'},
                },
            },
            {
                '@type': 'BreadcrumbList',
                'itemListElement': [
                    {'@type': 'ListItem', 'position': 1, 'name': 'Início', 'item': SITE},
                    {'@type': 'ListItem', 'position': 2, 'name': 'Blog', 'item': f'{SITE}/blog/'},
                    {'@type': 'ListItem', 'position': 3, 'name': a['titulo'], 'item': url},
                ],
            },
        ],
    }

    # "Leia também": os dois seguintes na ordem do arquivo, circular. Ordem fixa
    # em vez de aleatória para o HTML ser idêntico entre duas gerações — diff de
    # build que muda sozinho esconde a mudança de verdade.
    i = todos.index(a)
    vizinhos = [todos[(i + 1) % len(todos)], todos[(i + 2) % len(todos)]]
    leia = '\n'.join(
        f'    <li><a href="/blog/{v["slug"]}">{escapar(v["titulo"])}</a></li>' for v in vizinhos)

    return f'''{cabecalho(a['titulo'] + ' — Monitora Contábil', a['descricao'], url, og, 'article', ld)}
<div class="progresso" aria-hidden="true"></div>
{topo()}

<main>
<article class="artigo">
  <div class="artigo-head">
    <p class="migalha"><a href="/">Início</a> › <a href="/blog/">Blog</a></p>
    <h1>{escapar(a['titulo'])}</h1>
    <p class="resumo">{a['resumo']}</p>
    <div class="artigo-meta">
      <span class="tag">{escapar(a['categoria'])}</span>
      <time datetime="{a['data']}">{data_br(a['data'])}</time>
      <span>{mins} min de leitura</span>
    </div>
  </div>

{a['corpo']}

  <aside class="cta">
    <h2>{escapar(a['cta_titulo'])}</h2>
    <p>{a['cta_texto']}</p>
    <a href="{APP}/cadastro">Testar 7 dias grátis</a>
  </aside>

  <div class="share">
    <span>Achou útil?</span>
    <button type="button" data-share>Compartilhar</button>
    <a href="https://wa.me/?text={escapar(a['titulo'])}%20{url}"
       target="_blank" rel="noopener noreferrer">WhatsApp</a>
    <a href="https://www.linkedin.com/sharing/share-offsite/?url={url}"
       target="_blank" rel="noopener noreferrer">LinkedIn</a>
  </div>
</article>

<section class="relacionados">
  <h2>Leia também</h2>
  <ul>
{leia}
  </ul>
</section>
</main>

{rodape()}
<script src="/blog.js" defer></script>
</body>
</html>
'''


def render_indice(todos) -> str:
    url = f'{SITE}/blog/'
    cats = []
    for a in todos:
        if a['categoria'] not in cats:
            cats.append(a['categoria'])

    ld = {
        '@context': 'https://schema.org',
        '@type': 'Blog',
        '@id': f'{url}#blog',
        'name': 'Blog da Monitora Contábil',
        'description': 'Gestão, produtividade e conformidade para escritórios de contabilidade.',
        'inLanguage': 'pt-BR',
        'url': url,
        'publisher': {'@type': 'Organization', 'name': 'Monitora Contábil', 'url': SITE},
        'blogPost': [
            {
                '@type': 'BlogPosting',
                'headline': a['titulo'],
                'description': a['descricao'],
                'datePublished': a['data'],
                'url': f'{SITE}/blog/{a["slug"]}',
            } for a in todos
        ],
    }

    botoes = '\n'.join(
        f'  <button class="filtro" data-cat="{escapar(c)}" aria-pressed="false">{escapar(c)}</button>'
        for c in cats)

    cartoes = '\n'.join(f'''  <a class="post" href="/blog/{a['slug']}" data-cat="{escapar(a['categoria'])}">
    <span class="tag">{escapar(a['categoria'])}</span>
    <h2>{escapar(a['titulo'])}</h2>
    <p>{escapar(a['descricao'])}</p>
    <span class="meta"><time datetime="{a['data']}">{data_br(a['data'])}</time>
      <span>{minutos(a['corpo'])} min</span></span>
  </a>''' for a in todos)

    return f'''{cabecalho(
        'Blog — Monitora Contábil',
        'Gestão, produtividade e conformidade para escritórios de contabilidade: LGPD, '
        'NR-1, controle de jornada e o que realmente vale medir numa equipe.',
        url, f'{SITE}/og.png', 'website', ld)}
{topo()}

<main>
<div class="capa">
  <p class="sobre">Blog</p>
  <h1>Gestão de equipe em escritório contábil</h1>
  <p class="lead">O que a lei exige, o que vale medir e o que fazer com o número
  depois de medido. Escrito por quem constrói a ferramenta — sem promessa que o
  software não cumpre.</p>
</div>

<div class="filtros">
  <button class="filtro" data-cat="tudo" aria-pressed="true">Tudo</button>
{botoes}
</div>

<div class="lista">
{cartoes}
  <p class="vazio" hidden>Nenhum artigo neste assunto ainda.</p>
</div>
</main>

{rodape()}
<script src="/blog.js" defer></script>
</body>
</html>
'''


def render_og(a) -> str:
    """O cartão de link do artigo (1200 × 630), no desenho dos cartões da marca
    (marca/icones.py): azul-noite com a pauta, o logotipo, o assunto, o título na
    voz leve e a íris ao fundo. A letra vem de site/fontes, pelo caminho do disco:
    o cartão é fotografado aqui, não servido."""
    plex = 'file://' + os.path.join(RAIZ, 'fontes', 'plex.css')
    marca = 'file://' + os.path.join(RAIZ, 'marca.css')
    tamanho = 60 if len(a['titulo']) < 50 else 52 if len(a['titulo']) < 70 else 46
    return f'''<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="{plex}"><link rel="stylesheet" href="{marca}">
<style>
  html,body{{margin:0;width:1200px;height:630px;overflow:hidden}}
  body{{background:#0b1c33;background-image:repeating-linear-gradient(to bottom,transparent 0 31px,rgba(255,255,255,.05) 31px 32px);
       position:relative;font-family:'IBM Plex Sans',sans-serif;color:#fff}}
  body::before,body::after{{content:"";position:absolute;top:0;bottom:0;width:1px;background:rgba(255,255,255,.08)}}
  body::before{{left:80px}}body::after{{right:80px}}
  .wm{{position:absolute;left:120px;top:84px;font-size:30px}}
  .tag{{position:absolute;left:120px;top:176px;margin:0;font:600 18px/1 'IBM Plex Sans',sans-serif;letter-spacing:.16em;
       text-transform:uppercase;color:#9cc0ff}}
  h1{{position:absolute;left:120px;top:214px;width:760px;margin:0;font-weight:300;font-size:{tamanho}px;line-height:1.1;
     letter-spacing:-.025em;text-wrap:balance}}
  .url{{position:absolute;left:120px;bottom:64px;font:400 20px 'IBM Plex Mono',monospace;color:#8fa5c2}}
  svg.fundo{{position:absolute;right:-150px;top:120px;width:500px;height:500px;opacity:.18}}
</style></head><body>
<span class="wm claro">M{IRIS_O}<span class="sr">o</span>nitora <span class="c">Contábil</span></span>
<p class="tag">{escapar(a['categoria'])}</p>
<h1>{escapar(a['titulo'])}</h1>
<div class="url">monitoracontabil.com.br/blog</div>
<svg class="fundo" viewBox="0 0 64 64">{IRIS_CHEIA}</svg>
</body></html>'''


def fotografar_cartoes(todos) -> None:
    """Fotografa cada cartão em blog/og/<slug>.jpg. Precisa do Chrome e do `sips`
    (macOS); sem eles, avisa e segue: o HTML do artigo não depende do JPG."""
    if not os.path.exists(CHROME) or not shutil.which('sips'):
        print('  (cartões não fotografados: falta o Chrome ou o sips)')
        return
    for a in todos:
        fonte = os.path.join(OGDIR, f'{a["slug"]}.html')
        with tempfile.TemporaryDirectory() as tmp:
            png = os.path.join(tmp, 'c.png')
            subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--force-device-scale-factor=1',
                            '--allow-file-access-from-files', '--window-size=1200,630', '--virtual-time-budget=4000',
                            f'--screenshot={png}', f'file://{fonte}'], check=True, capture_output=True)
            subprocess.run(['sips', '-s', 'format', 'jpeg', '-s', 'formatOptions', '86', png,
                            '--out', os.path.join(BLOG, 'og', f'{a["slug"]}.jpg')], check=True, capture_output=True)
    print(f'  {len(todos)} cartões de link fotografados em blog/og/')


def revisao(pagina: str) -> str:
    """A data de "Última revisão" impressa na página legal: o sitemap não inventa outra."""
    with open(os.path.join(RAIZ, pagina), encoding='utf-8') as f:
        d, m, a = re.search(r'Última revisão</b>\s*(\d\d)/(\d\d)/(\d{4})', f.read()).groups()
    return f'{a}-{m}-{d}'


def render_sitemap(todos) -> str:
    hoje = date.today().isoformat()
    urls = [
        (f'{SITE}/', hoje, 'weekly', '1.0'),
        (f'{SITE}/blog/', max(a.get('revisado', a['data']) for a in todos), 'weekly', '0.8'),
        (f'{SITE}/privacidade', revisao('privacidade.html'), 'yearly', '0.3'),
        (f'{SITE}/termos', revisao('termos.html'), 'yearly', '0.3'),
    ] + [
        (f'{SITE}/blog/{a["slug"]}', a.get('revisado', a['data']), 'monthly', '0.7')
        for a in todos
    ]
    corpo = '\n'.join(
        f'  <url>\n    <loc>{u}</loc>\n    <lastmod>{m}</lastmod>\n'
        f'    <changefreq>{f}</changefreq>\n    <priority>{p}</priority>\n  </url>'
        for u, m, f, p in urls)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            f'{corpo}\n</urlset>\n')


def main():
    os.makedirs(BLOG, exist_ok=True)
    os.makedirs(OGDIR, exist_ok=True)

    slugs = [a['slug'] for a in ARTIGOS]
    assert len(slugs) == len(set(slugs)), 'slug repetido'

    for a in ARTIGOS:
        with open(os.path.join(BLOG, f'{a["slug"]}.html'), 'w', encoding='utf-8') as f:
            f.write(render_artigo(a, ARTIGOS))
        with open(os.path.join(OGDIR, f'{a["slug"]}.html'), 'w', encoding='utf-8') as f:
            f.write(render_og(a))

    with open(os.path.join(BLOG, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(render_indice(ARTIGOS))
    with open(os.path.join(RAIZ, 'sitemap.xml'), 'w', encoding='utf-8') as f:
        f.write(render_sitemap(ARTIGOS))

    print(f'{len(ARTIGOS)} artigos + índice + sitemap gerados')
    for a in ARTIGOS:
        print(f'  /blog/{a["slug"]:<44} {minutos(a["corpo"]):>2} min')

    fotografar_cartoes(ARTIGOS)
    respostas.gravar()  # artigo novo também entra no llms.txt


if __name__ == '__main__':
    main()
