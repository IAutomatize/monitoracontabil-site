#!/usr/bin/env python3
"""
AS RESPOSTAS — a seção de perguntas da página principal vira dado para máquina.

Por quê: o Google só aceita FAQPage que bata com o que a tela mostra, e as IAs
(ChatGPT, Gemini, Perplexity, AI Overviews) citam o trecho que responde direto.
A mesma resposta escrita em três lugares diverge no segundo ajuste; aqui ela é
escrita uma vez, na seção #perguntas do index.html, e o resto é gravado dela:

  - o bloco <script type="application/ld+json" id="ld-perguntas"> do index.html;
  - o /llms.txt, o resumo em Markdown para quem lê o site como modelo de
    linguagem: o que o produto é, as perguntas, as páginas e os artigos do blog.

Uso:
    python3 site/_fonte/respostas.py

O gerar-blog.py chama este arquivo no fim, porque artigo novo também muda o
llms.txt. Rodar de novo regrava igual: é idempotente.
"""
import html
import json
import os
import re

from artigos import ARTIGOS

SITE = 'https://monitoracontabil.com.br'
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
INDEX = os.path.join(RAIZ, 'index.html')
LLMS = os.path.join(RAIZ, 'llms.txt')

_SECAO = re.compile(r'<section[^>]*\bid="perguntas"[^>]*>(.*?)</section>', re.S)
_PAR = re.compile(r'<details>\s*<summary>(.*?)</summary>\s*<div class="resposta">(.*?)</div>\s*</details>', re.S)
_BLOCO = re.compile(r'(<script type="application/ld\+json" id="ld-perguntas">).*?(</script>)', re.S)


def _absoluto(trecho: str) -> str:
    return re.sub(r'href="/', f'href="{SITE}/', trecho)


def _markdown(trecho: str) -> str:
    t = re.sub(r'<a href="([^"]+)">(.*?)</a>', lambda m: f'[{m.group(2)}]({m.group(1)})', _absoluto(trecho))
    t = re.sub(r'</p>\s*<p>', '\n\n', t)
    return html.unescape(re.sub(r'<[^>]+>', '', t)).strip()


def perguntas(pagina: str) -> list[tuple[str, str]]:
    secao = _SECAO.search(pagina)
    assert secao, 'a seção id="perguntas" sumiu do index.html'
    pares = [(html.unescape(q).strip(), r.strip()) for q, r in _PAR.findall(secao.group(1))]
    assert pares, 'a seção de perguntas está sem nenhuma <details>'
    return pares


def faqpage(pares) -> str:
    dado = {
        '@context': 'https://schema.org',
        '@type': 'FAQPage',
        '@id': f'{SITE}/#perguntas',
        'mainEntity': [
            {'@type': 'Question', 'name': q,
             'acceptedAnswer': {'@type': 'Answer', 'text': _absoluto(r)}}
            for q, r in pares
        ],
    }
    # "</" dentro de <script> fecharia o bloco antes da hora
    return json.dumps(dado, ensure_ascii=False, indent=1).replace('</', '<\\/')


def llms(pagina: str, pares) -> str:
    resumo = html.unescape(re.search(r'<meta name="description" content="([^"]+)"', pagina).group(1))
    faq = '\n\n'.join(f'**{q}**\n{_markdown(r)}' for q, r in pares)
    artigos = '\n'.join(f'- [{a["titulo"]}]({SITE}/blog/{a["slug"]}): {a["descricao"]}' for a in ARTIGOS)
    return f'''# Monitora Contábil

> {resumo}

Site: {SITE}/ · Contato: contato@monitoracontabil.com.br · Idioma: português do Brasil

{faq}

## Páginas

- [Página principal]({SITE}/): o que o painel mostra, a Alice, privacidade, planos e perguntas frequentes
- [Política de Privacidade]({SITE}/privacidade): o que o agente coleta, o que nunca coleta, bases legais e prazos de guarda
- [Termos de Uso]({SITE}/termos): as regras do serviço
- [Blog]({SITE}/blog/): gestão, produtividade e conformidade para escritórios de contabilidade

## Blog

{artigos}
'''


def gravar():
    with open(INDEX, encoding='utf-8') as f:
        pagina = f.read()
    pares = perguntas(pagina)
    novo, n = _BLOCO.subn(lambda m: m.group(1) + '\n' + faqpage(pares) + '\n' + m.group(2), pagina)
    assert n == 1, 'o <script id="ld-perguntas"> precisa existir uma vez no <head> do index.html'
    with open(INDEX, 'w', encoding='utf-8') as f:
        f.write(novo)
    with open(LLMS, 'w', encoding='utf-8') as f:
        f.write(llms(novo, pares))
    print(f'{len(pares)} perguntas gravadas no FAQPage do index.html e no llms.txt')


if __name__ == '__main__':
    gravar()
