# -*- coding: utf-8 -*-
"""
Artigos de eixo jurídico e de conformidade.

REGRA DE CONTEÚDO, e ela não é estilo: nenhum artigo pode afirmar sobre o
produto algo que o código não faça. O que vale para a política de privacidade
vale aqui — texto público que promete proteção inexistente é o mesmo defeito
que `conferencia.ts` existe para pegar no documento do cliente.
"""

JURIDICO = [

# ─────────────────────────────────────────────────────────────────────────────
{
 'slug': 'monitorar-computador-do-funcionario-e-legal',
 'categoria': 'Jurídico',
 'data': '2026-07-14',
 'titulo': 'É legal monitorar o computador do funcionário?',
 'descricao': 'Sim, dentro de limites claros: equipamento da empresa, comunicação prévia '
              'e finalidade legítima. Veja o que a lei brasileira permite e o que torna o '
              'monitoramento ilícito.',
 'resumo': 'A resposta curta é sim — e a longa é o que separa uma prática defensável de '
           'um processo trabalhista. Três condições decidem de que lado você está.',
 'cta_titulo': 'Monitoramento que nasce dentro da regra',
 'cta_texto': 'A Monitora Contábil mede atividade de trabalho em computadores da empresa e '
              'vem com um kit de implantação pronto: roteiro de reunião, comunicado, FAQ e '
              'minuta de termo de ciência.',
 'corpo': '''
  <p>A pergunta chega quase sempre depois do fato: o escritório já desconfia que
  parte do expediente evapora, alguém sugere instalar um monitor de atividade, e
  então vem o freio — <em>isso pode?</em></p>

  <p>Pode. O empregador tem <strong>poder diretivo</strong> sobre a organização do
  trabalho (art. 2º da CLT), e fiscalizar o uso dos equipamentos que ele fornece é
  parte disso. O Tribunal Superior do Trabalho tem entendimento consolidado de que
  ferramenta de trabalho fornecida pela empresa é <strong>bem corporativo</strong>,
  não espaço privado do empregado — e o que trafega nela pode ser fiscalizado.</p>

  <p>O que transforma isso em risco não é o monitoramento. É a forma.</p>

  <h2>As três condições que sustentam a prática</h2>

  <h3>1. O equipamento tem que ser da empresa</h3>
  <p>Esta é a linha mais nítida do assunto. Monitorar o notebook que a empresa
  comprou, entregou e destinou ao trabalho é fiscalização de bem próprio. Instalar
  qualquer coisa no computador pessoal de alguém — ainda que ele use para
  trabalhar — é invasão de dispositivo, com repercussão civil e possivelmente
  penal.</p>

  <p>Se o seu escritório adota BYOD (cada um usa a própria máquina), o
  monitoramento de atividade não é o caminho. Nem com autorização assinada: no
  vínculo de emprego, autorização dada sob subordinação é frágil e costuma ser
  desconsiderada.</p>

  <h3>2. A equipe precisa saber antes</h3>
  <p>Monitoramento oculto é o erro que mais gera condenação. A jurisprudência
  aceita a fiscalização quando ela é <strong>prévia e conhecida</strong> — a pessoa
  sabe que o equipamento é monitorado, e por isso não tem expectativa legítima de
  privacidade ali. Sem comunicação, essa expectativa existe, e violá-la é dano
  moral.</p>

  <blockquote><p>Comunicar não enfraquece o monitoramento. É o que o torna
  defensável — e, na prática, o que faz o número ser levado a sério pela
  equipe.</p></blockquote>

  <h3>3. A finalidade tem que ser de trabalho, e proporcional</h3>
  <p>Medir tempo de uso de sistemas fiscais para dimensionar equipe é finalidade
  legítima. Ler conversa pessoal para saber a opinião de alguém sobre a chefia não
  é — e nenhum consentimento conserta isso.</p>

  <p>Proporcionalidade significa coletar o necessário para a finalidade declarada,
  e nada além. Contar quantas vezes o teclado foi acionado responde “houve
  atividade?”. Gravar <em>o que</em> foi digitado responde uma pergunta que
  ninguém precisava fazer — e cria um passivo enorme.</p>

  <h2>O que torna o monitoramento ilícito</h2>

  <div class="tw"><table>
    <thead><tr><th>Prática</th><th>Por que é problema</th></tr></thead>
    <tbody>
      <tr><td>Instalação oculta, sem aviso</td>
          <td>Viola a expectativa de privacidade; é a hipótese clássica de dano moral</td></tr>
      <tr><td>Software em dispositivo pessoal</td>
          <td>Invasão de dispositivo informático alheio</td></tr>
      <tr><td>Leitura de e-mail ou mensagem pessoal</td>
          <td>Sigilo das comunicações (CF, art. 5º, XII). Conta corporativa avisada é outra coisa</td></tr>
      <tr><td>Captura ou gravação de tela sem aviso prévio</td>
          <td>Alta invasividade: alcança conteúdo de terceiros e dado sensível por tabela.
          O que a torna ilícita não é existir — é acontecer sem comunicação individual
          prévia, sem acesso restrito e registrado, e sem prazo curto de guarda</td></tr>
      <tr><td>Registro do conteúdo digitado (keylogger)</td>
          <td>Captura senhas pessoais, dados bancários e conversas privadas</td></tr>
      <tr><td>Monitorar fora do expediente</td>
          <td>Fora da finalidade de trabalho; alcança a vida privada</td></tr>
    </tbody>
  </table></div>

  <h2>Câmera, e-mail e computador não são a mesma coisa</h2>

  <p>Vale separar, porque a discussão costuma misturar tudo:</p>

  <ul>
    <li><strong>Atividade no computador corporativo</strong> — a mais aceita. Mede
    uso de ferramenta de trabalho.</li>
    <li><strong>E-mail corporativo</strong> — aceito quando há política escrita e
    conhecida, e quando se fiscaliza a conta da empresa, não a pessoal.</li>
    <li><strong>Câmera</strong> — aceita em área comum, com aviso; vedada em
    banheiro, vestiário e refeitório.</li>
    <li><strong>Rastreamento por GPS</strong> — aceito para função externa
    (motorista, técnico de campo), com finalidade clara e limitado à jornada.</li>
  </ul>

  <h2>E a LGPD?</h2>

  <p>A licitude trabalhista é metade da resposta. A outra metade é a Lei
  13.709/2018: mesmo um monitoramento perfeitamente lícito perante a CLT precisa de
  base legal, finalidade declarada, minimização e respeito aos direitos do titular.
  O tratamento disso está em <a href="/blog/lgpd-monitoramento-de-funcionarios">LGPD
  e monitoramento de funcionários</a>.</p>

  <div class="destaque">
    <span class="rot">O resumo prático</span>
    <p>Equipamento da empresa, aviso prévio por escrito, finalidade de trabalho
    declarada e coleta proporcional. Com os quatro, você está num terreno que a
    jurisprudência reconhece há anos. Faltando qualquer um, o risco deixa de ser
    teórico.</p>
  </div>

  <p>Uma observação final que vale mais que todas as anteriores: escritório que
  implanta monitoramento como ameaça colhe o resultado da ameaça — gente que
  aprende a parecer ocupada. Quem implanta explicando o que vai medir e para quê
  colhe dado que serve para decidir. O roteiro disso está em
  <a href="/blog/implantar-monitoramento-sem-perder-a-equipe">como implantar sem
  quebrar a confiança da equipe</a>.</p>

  <p><em>Este artigo é informativo e não substitui a orientação de um advogado
  sobre o seu caso concreto.</em></p>
''',
},

# ─────────────────────────────────────────────────────────────────────────────
{
 'slug': 'lgpd-monitoramento-de-funcionarios',
 'categoria': 'Jurídico',
 'data': '2026-07-22',
 'titulo': 'LGPD e monitoramento de funcionários: o guia prático',
 'descricao': 'Base legal, teste de legítimo interesse, minimização, retenção e direitos do '
              'titular — o que a LGPD exige de quem monitora a atividade da própria equipe.',
 'resumo': 'Monitorar é tratar dado pessoal. Isso significa base legal, finalidade escrita '
           'e um conjunto de obrigações que quase ninguém cumpre inteiro — e que é mais '
           'simples do que parece.',
 'cta_titulo': 'A conformidade não devia ser trabalho seu',
 'cta_texto': 'A Monitora Contábil já nasce com retenção configurável, trilha de auditoria '
              'e relatório do titular por pessoa — as ferramentas que a LGPD pede, dentro '
              'do painel.',
 'corpo': '''
  <p>Toda medição de atividade de uma pessoa identificada é tratamento de dado
  pessoal. Não importa que o dado pareça inofensivo: “Maria usou o e-CAC por 3h12”
  é informação sobre pessoa natural identificada, e portanto está sob a Lei
  13.709/2018.</p>

  <p>Isso não proíbe nada. Só define como fazer.</p>

  <h2>1. A base legal — e por que não é consentimento</h2>

  <p>A tentação natural é pedir uma assinatura autorizando o monitoramento. É a
  escolha errada, e por um motivo estrutural: <strong>consentimento exige
  liberdade</strong>, e na relação de emprego ela não existe de forma plena. Quem
  recebe do empregador um papel para assinar não está livre para recusar — e um
  consentimento viciado é um consentimento inválido, que pode ser revogado a
  qualquer momento (art. 8º, §5º), derrubando a base do tratamento inteiro.</p>

  <p>A base adequada é o <strong>legítimo interesse</strong> (art. 7º, IX), com
  transparência reforçada. Ela exige três coisas do controlador:</p>

  <ul>
    <li><strong>Finalidade concreta e legítima</strong> — “dimensionar equipe no
    fechamento fiscal”, não “fiscalizar funcionários”;</li>
    <li><strong>Necessidade</strong> — não haver meio menos invasivo de chegar ao
    mesmo resultado;</li>
    <li><strong>Balanceamento</strong> — o interesse da empresa pesado contra os
    direitos e liberdades de quem é monitorado, com as salvaguardas que reduzem o
    impacto.</li>
  </ul>

  <p>Esse raciocínio precisa estar <strong>escrito</strong>. É o teste de legítimo
  interesse (LIA), e ele não é burocracia: é a única prova de que a decisão foi
  tomada, e não presumida. Documento de uma a três páginas, revisado quando a
  finalidade mudar.</p>

  <h2>2. Transparência</h2>

  <p>Legítimo interesse só se sustenta com transparência reforçada. Na prática, a
  equipe precisa saber, por escrito e antes do início:</p>

  <ul>
    <li>que os equipamentos da empresa são monitorados;</li>
    <li><strong>o que exatamente</strong> é coletado — e o que não é;</li>
    <li>para que serve, e quem tem acesso;</li>
    <li>por quanto tempo o dado é guardado;</li>
    <li>como exercer os direitos do art. 18.</li>
  </ul>

  <p>“O que não é coletado” costuma ser esquecido e é a parte mais eficaz do
  documento. Dizer que o sistema <em>não</em> registra o que é digitado, não tira
  foto da tela e não liga microfone muda completamente a reação de quem lê — e é
  informação verificável.</p>

  <div class="destaque">
    <span class="rot">Cuidado com o exagero para o seu lado</span>
    <p>Declarar coleta que não acontece parece prudente e é o contrário: cria
    obrigação sobre dado inexistente e destrói a confiança quando alguém descobre.
    Declarar de menos é pior ainda — coletar sem declarar é o risco jurídico de
    verdade. O documento precisa bater exatamente com o que a ferramenta faz.</p>
  </div>

  <h2>3. Minimização</h2>

  <p>O art. 6º, III manda limitar o tratamento ao mínimo necessário. Traduzindo
  para decisões concretas de configuração:</p>

  <div class="tw"><table>
    <thead><tr><th>Pergunta de gestão</th><th>Dado suficiente</th><th>Dado excessivo</th></tr></thead>
    <tbody>
      <tr><td>A equipe está sobrecarregada?</td>
          <td>Horas ativas por dia, por setor</td><td>Conteúdo do que foi digitado</td></tr>
      <tr><td>Quanto tempo vai para o e-CAC?</td>
          <td>Domínio do site e duração</td><td>Captura de tela do portal</td></tr>
      <tr><td>Quem precisa de treinamento?</td>
          <td>Retrabalho e vaivém entre sistemas</td><td>Gravação da sessão</td></tr>
    </tbody>
  </table></div>

  <h2>4. Retenção</h2>

  <p>Dado pessoal tem prazo. Guardar “para sempre, porque disco é barato” viola o
  art. 15 e transforma qualquer incidente futuro num incidente maior. Defina o
  prazo pela finalidade — doze meses cobre a sazonalidade contábil inteira e ainda
  permite comparar um fechamento com o do ano anterior — e garanta que o expurgo
  <strong>acontece de verdade</strong>, automaticamente.</p>

  <h2>5. Direitos do titular</h2>

  <p>A pessoa monitorada pode pedir confirmação, acesso, correção, anonimização e
  eliminação (art. 18). Na prática isso significa conseguir responder, em prazo
  razoável: <em>o que exatamente vocês têm sobre mim?</em></p>

  <p>Se a resposta exigir consulta manual ao banco de dados, o processo vai
  falhar na primeira vez que for usado. Ferramenta madura tem essa tela pronta.</p>

  <h2>6. Quando é preciso um relatório de impacto</h2>

  <p>Monitoramento sistemático de trabalhadores costuma ser tratado como
  tratamento de <strong>alto risco</strong>. Um Relatório de Impacto à Proteção de
  Dados (RIPD) documenta os riscos e as medidas que os reduzem. Ele é a peça que a
  ANPD pede primeiro numa fiscalização — e, mais útil que isso, é o exercício que
  costuma revelar coleta desnecessária que ninguém tinha questionado.</p>

  <h2>Checklist</h2>

  <ul>
    <li>☐ Finalidade escrita, específica</li>
    <li>☐ Teste de legítimo interesse documentado</li>
    <li>☐ Aviso à equipe, entregue antes do início, com o que é e o que não é coletado</li>
    <li>☐ Coleta limitada à finalidade</li>
    <li>☐ Prazo de retenção definido e expurgo automático</li>
    <li>☐ Canal para os direitos do art. 18</li>
    <li>☐ Acesso restrito e registrado</li>
    <li>☐ RIPD quando o risco for alto</li>
    <li>☐ Contrato com o fornecedor, na condição de operador</li>
  </ul>

  <p>A parte trabalhista da mesma pergunta está em
  <a href="/blog/monitorar-computador-do-funcionario-e-legal">é legal monitorar o
  computador do funcionário?</a></p>

  <p><em>Conteúdo informativo, não substitui parecer jurídico.</em></p>
''',
},

# ─────────────────────────────────────────────────────────────────────────────
{
 'slug': 'nr-1-riscos-psicossociais',
 'categoria': 'Jurídico',
 'data': '2026-08-04',
 'titulo': 'NR-1 e riscos psicossociais: o que a sua empresa precisa fazer',
 'descricao': 'A NR-1 passou a exigir a gestão de riscos psicossociais no PGR. O que isso '
              'significa na prática, quais evidências valem e como registrar sem rotular '
              'pessoas.',
 'resumo': 'Sobrecarga deixou de ser assunto de RH e virou item de programa de gestão de '
           'riscos, sujeito a fiscalização. O que muda no dia a dia de um escritório.',
 'cta_titulo': 'Evidência objetiva para o seu PGR',
 'cta_texto': 'Jornada real, dias sem pausa e trabalho fora do horário — medidos por '
              'setor, sem rótulo clínico e sem nota individual. É o tipo de evidência que '
              'um inventário de riscos precisa.',
 'corpo': '''
  <p>A Norma Regulamentadora nº 1 sempre tratou de gerenciamento de riscos
  ocupacionais. A mudança recente é o que entrou na lista: <strong>riscos
  psicossociais</strong> passaram a integrar expressamente o Gerenciamento de
  Riscos Ocupacionais, e portanto o PGR — o Programa de Gerenciamento de
  Riscos.</p>

  <p>Deixou de ser tema de bem-estar. Virou item auditável.</p>

  <h2>O que é risco psicossocial</h2>

  <p>São características da organização do trabalho capazes de causar dano à saúde
  mental e física. No trabalho administrativo, os que mais aparecem:</p>

  <ul>
    <li><strong>Sobrecarga</strong> — volume incompatível com o tempo disponível;</li>
    <li><strong>Jornada excessiva</strong> — extensão, horas extras habituais,
    trabalho noturno e em fim de semana;</li>
    <li><strong>Ausência de pausas</strong> — sequências longas sem interrupção;</li>
    <li><strong>Falta de autonomia</strong> — nenhum controle sobre o próprio ritmo;</li>
    <li><strong>Pressão temporal</strong> — prazos concentrados e inegociáveis;</li>
    <li><strong>Assédio e conflito</strong>;</li>
    <li><strong>Insegurança</strong> quanto à permanência no emprego.</li>
  </ul>

  <p>Escritório contábil coleciona vários deles por natureza. A sazonalidade
  fiscal produz picos de carga com prazo legal inegociável — a combinação exata que
  a norma quer ver gerenciada.</p>

  <h2>O que a norma exige</h2>

  <div class="tw"><table>
    <thead><tr><th>Etapa</th><th>O que fazer</th></tr></thead>
    <tbody>
      <tr><td><b>Identificar</b></td>
          <td>Levantar os perigos psicossociais existentes nas atividades reais</td></tr>
      <tr><td><b>Avaliar</b></td>
          <td>Estimar o risco por probabilidade e severidade</td></tr>
      <tr><td><b>Controlar</b></td>
          <td>Definir medidas, prazos e responsáveis</td></tr>
      <tr><td><b>Registrar</b></td>
          <td>Documentar tudo no inventário de riscos e no plano de ação</td></tr>
      <tr><td><b>Acompanhar</b></td>
          <td>Reavaliar periodicamente e após mudança relevante</td></tr>
    </tbody>
  </table></div>

  <p>O ponto sensível é o segundo. Avaliar sobrecarga sem dado vira opinião — e
  opinião não sustenta um inventário de riscos numa fiscalização.</p>

  <h2>Que evidência serve</h2>

  <p>As fontes usuais são questionário de percepção, entrevista, absenteísmo e
  registro de afastamentos. Todas são úteis e todas têm o mesmo limite: chegam
  depois, ou dependem de a pessoa relatar.</p>

  <p>Dado de jornada real complementa isso com um sinal que aparece antes:</p>

  <ul>
    <li>quantos dias no mês a pessoa trabalhou além do expediente previsto;</li>
    <li>quantos dias seguidos sem uma pausa significativa;</li>
    <li>quanto de atividade caiu em fim de semana ou de madrugada;</li>
    <li>como o pico de fechamento se distribui entre setores.</li>
  </ul>

  <blockquote><p>“Achamos que o Fiscal está sobrecarregado” não entra num
  inventário de riscos. “No Fiscal, 9 dos 12 colaboradores registraram atividade
  além do expediente em mais de 15 dias no último trimestre” entra.</p></blockquote>

  <h2>A linha que não se cruza</h2>

  <p>Medir carga de trabalho é gestão de risco. Medir <em>pessoas</em> é outra
  coisa, e o caminho errado. Três limites que valem escrever na sua política:</p>

  <ul>
    <li><strong>Nenhum rótulo clínico.</strong> Software não diagnostica burnout,
    ansiedade ou depressão. Sugerir isso a partir de uso de computador é
    irresponsável e cria dado de saúde — categoria sensível sob a LGPD, com
    exigências muito mais duras.</li>
    <li><strong>Nenhum escore individual de risco.</strong> Uma nota por pessoa
    vira classificação, e classificação vira decisão sobre a carreira dela.</li>
    <li><strong>A leitura é do trabalho, não do trabalhador.</strong> Sobrecarga
    concentrada num setor é problema de dimensionamento e de prazo — não é falta
    de resiliência de quem está lá.</li>
  </ul>

  <h2>Por onde começar</h2>

  <ol>
    <li>Inclua os fatores psicossociais no seu levantamento de perigos — por
    setor, não por pessoa.</li>
    <li>Reúna evidência dos dois tipos: percepção (questionário) e objetiva
    (jornada, picos, pausas).</li>
    <li>Avalie e classifique cada risco no inventário.</li>
    <li>Defina medidas com prazo e responsável. Redistribuir carga no fechamento,
    contratar temporário no pico e escalonar prazos internos são medidas
    legítimas — e mensuráveis.</li>
    <li>Reavalie depois do próximo ciclo e registre se a medida funcionou.</li>
  </ol>

  <div class="destaque">
    <span class="rot">O efeito colateral bom</span>
    <p>Escritório que passa a olhar carga por setor costuma descobrir, no primeiro
    trimestre, que o gargalo não estava onde todo mundo achava. A conformidade é a
    obrigação; a informação é o que sobra dela.</p>
  </div>

  <p>Sobre reconhecer o sinal antes do afastamento, veja
  <a href="/blog/sinais-de-sobrecarga-na-equipe">sinais de sobrecarga na equipe</a>.</p>

  <p><em>Conteúdo informativo. A aplicação da NR-1 ao seu caso deve ser conduzida
  pelo seu SESMT ou consultoria de segurança do trabalho.</em></p>
''',
},

# ─────────────────────────────────────────────────────────────────────────────
{
 'slug': 'controle-de-jornada-home-office',
 'categoria': 'Jurídico',
 'data': '2026-08-12',
 'titulo': 'Controle de jornada em home office: o que a lei exige',
 'descricao': 'Quem trabalha remoto tem jornada controlada? Depende do regime. Entenda a '
              'diferença entre teletrabalho por jornada e por produção, e o risco de horas '
              'extras.',
 'resumo': 'A resposta muda conforme o que está escrito no contrato — e o contrato de '
           'muita gente diz uma coisa enquanto a rotina diz outra. É aí que nasce o '
           'passivo.',
 'cta_titulo': 'Saiba como a jornada realmente acontece',
 'cta_texto': 'Fitas de 24 horas por dia, expediente esperado marcado e cada vazio '
              'explicado. A Monitora mostra o padrão real da rotina — sem transformar '
              'horário de entrada em nota.',
 'corpo': '''
  <p>Desde a reforma trabalhista, e com os ajustes trazidos pela Lei 14.442/2022, o
  teletrabalho tem duas modalidades — e a diferença entre elas decide se existe ou
  não obrigação de controlar jornada.</p>

  <h2>Os dois regimes</h2>

  <div class="tw"><table>
    <thead><tr><th></th><th>Por jornada</th><th>Por produção ou tarefa</th></tr></thead>
    <tbody>
      <tr><td><b>Como se mede</b></td><td>Horas trabalhadas</td><td>Entregas concluídas</td></tr>
      <tr><td><b>Controle de ponto</b></td><td>Obrigatório</td><td>Dispensado</td></tr>
      <tr><td><b>Horas extras</b></td><td>Devidas</td><td>Em regra, não</td></tr>
      <tr><td><b>Base</b></td><td>Regra geral da CLT</td><td>CLT, art. 62, III</td></tr>
    </tbody>
  </table></div>

  <p>A exclusão do art. 62, III alcança quem presta serviço <strong>por produção ou
  por tarefa</strong>. Não é uma etiqueta que se escolhe: precisa corresponder à
  realidade.</p>

  <h2>Onde nasce o passivo</h2>

  <p>O padrão que mais aparece em reclamação trabalhista é este: o contrato diz
  “por produção”, mas na prática a pessoa tem horário para começar, precisa estar
  disponível no expediente, participa de reunião marcada e responde mensagem em
  tempo real.</p>

  <blockquote><p>Se há controle de horário na rotina, há jornada — independentemente
  do que o contrato chama. E se há jornada não registrada, há horas extras não
  pagas.</p></blockquote>

  <p>Três sinais de que o regime declarado não corresponde à realidade:</p>

  <ul>
    <li>o time tem horário fixo de início, ainda que informal;</li>
    <li>há expectativa de resposta imediata durante o expediente;</li>
    <li>reuniões recorrentes em horário marcado.</li>
  </ul>

  <p>Com qualquer um deles presente, tratar como “por produção” é assumir risco.</p>

  <h2>O que precisa estar no contrato</h2>

  <p>O regime de teletrabalho exige acordo <strong>escrito e expresso</strong>,
  especificando as atividades. Além do regime, vale registrar:</p>

  <ul>
    <li>quem fornece e mantém os equipamentos, e como despesas são reembolsadas;</li>
    <li>as regras de disponibilidade e os limites de contato fora do horário;</li>
    <li>as condições para retorno ao presencial, com prazo de transição;</li>
    <li>as instruções de saúde e segurança, com termo de ciência assinado.</li>
  </ul>

  <h2>Tempo à disposição e o direito de desconectar</h2>

  <p>Tempo à disposição do empregador é tempo de trabalho. Em remoto, isso alcança
  a exigência de permanecer disponível fora do expediente — cobrar resposta às 22h
  é estender jornada, mesmo que a mensagem leve dois minutos para ser respondida.</p>

  <p>A recomendação prática é escrever a regra: janela de contato definida, e nada
  esperado fora dela salvo urgência declarada. Além de reduzir risco, é medida de
  controle de risco psicossocial no PGR — o assunto de
  <a href="/blog/nr-1-riscos-psicossociais">NR-1 e riscos psicossociais</a>.</p>

  <h2>Como registrar sem transformar em vigilância</h2>

  <p>Controle de jornada e monitoramento de atividade são coisas diferentes, e
  confundi-las gera resistência à toa:</p>

  <div class="tw"><table>
    <thead><tr><th></th><th>Controle de jornada</th><th>Monitoramento de atividade</th></tr></thead>
    <tbody>
      <tr><td><b>Pergunta</b></td><td>Quantas horas?</td><td>Como o trabalho acontece?</td></tr>
      <tr><td><b>Serve para</b></td><td>Folha e horas extras</td><td>Dimensionar equipe e processo</td></tr>
      <tr><td><b>Obrigatório?</b></td><td>Sim, no regime por jornada</td><td>Não</td></tr>
    </tbody>
  </table></div>

  <p>O registro de ponto é a fonte legal da jornada. Dado de atividade não
  substitui ponto — mas mostra o <strong>padrão</strong>: se a rotina real começa
  antes do horário previsto, se as noites viram extensão do dia no fechamento, se
  as pausas sumiram no último trimestre.</p>

  <div class="destaque">
    <span class="rot">Uma trava que vale adotar</span>
    <p>Horário de entrada não é mérito. Quem começa às 7h não é melhor que quem
    começa às 9h — são rotinas, não notas. Transformar isso em ranking é o começo
    exato do uso punitivo que faz a equipe deixar de confiar no painel.</p>
  </div>

  <p><em>Conteúdo informativo. Enquadramento de regime deve ser avaliado
  caso a caso com apoio jurídico.</em></p>
''',
},

# ─────────────────────────────────────────────────────────────────────────────
{
 'slug': 'implantar-monitoramento-sem-perder-a-equipe',
 'categoria': 'Gestão',
 'data': '2026-08-19',
 'titulo': 'Como implantar monitoramento sem quebrar a confiança da equipe',
 'descricao': 'O roteiro de implantação que separa monitoramento que gera informação de '
              'monitoramento que gera teatro: reunião, comunicado, termo de ciência e os '
              'primeiros 30 dias.',
 'resumo': 'A ferramenta é a parte fácil. O que decide o resultado é a primeira conversa — '
           'e o que acontece nos trinta dias seguintes.',
 'cta_titulo': 'O kit de implantação vem junto',
 'cta_texto': 'Roteiro de reunião, e-mail de anúncio, FAQ do colaborador e minuta de termo '
              'de ciência — prontos dentro do painel, com checklist de progresso.',
 'corpo': '''
  <p>Existe um jeito de instalar monitoramento que produz dado confiável, e um
  jeito que produz um teatro caro. A diferença não está no software.</p>

  <p>Quando a equipe descobre o monitoramento por acidente — um processo estranho
  no gerenciador de tarefas, um comentário do gestor sobre algo que ele não
  deveria saber — o que se instala não é uma ferramenta. É a certeza de que a
  empresa age pelas costas. E a resposta natural a isso é aprender a parecer
  produtivo: deixar a planilha aberta, mexer o mouse, encher o dia de atividade
  que não é trabalho.</p>

  <blockquote><p>Monitoramento oculto não mede trabalho. Mede a habilidade de cada
  um em parecer ocupado — e ainda cria passivo jurídico.</p></blockquote>

  <h2>Antes: decida o que você vai fazer com o número</h2>

  <p>Escreva a resposta antes de instalar qualquer coisa. Se ela for “descobrir
  quem está enrolando”, pare — esse projeto vai custar mais do que entrega. Se for
  “entender por que o fechamento estoura todo mês”, siga.</p>

  <p>A pergunta que vale: <em>que decisão eu vou tomar com esse dado, que hoje eu
  tomo no escuro?</em></p>

  <ul>
    <li>dimensionar equipe por setor antes do próximo pico;</li>
    <li>descobrir quanto tempo vai para retrabalho e transporte manual de dado;</li>
    <li>identificar sobrecarga antes que ela vire afastamento;</li>
    <li>saber quais sistemas realmente consomem o dia.</li>
  </ul>

  <h2>A reunião, e a ordem que ela precisa ter</h2>

  <p>Anuncie ao vivo, para todo mundo junto, <strong>antes</strong> de instalar.
  E-mail sozinho não resolve: as pessoas precisam poder perguntar na hora.</p>

  <ol>
    <li><strong>Por que</strong> — o problema concreto que você quer resolver.
    Comece pela dor da equipe, não pela sua.</li>
    <li><strong>O que é medido</strong> — programa em uso, site, tempo ativo,
    contagem de teclado e mouse. Sem eufemismo.</li>
    <li><strong>O que não é medido</strong> — este é o momento mais importante da
    reunião. Não registra o que é digitado. Não tira foto da tela. Não liga
    microfone nem câmera. Diga com essas palavras.</li>
    <li><strong>Quem vê</strong> — nominalmente.</li>
    <li><strong>Por quanto tempo</strong> — o prazo de retenção.</li>
    <li><strong>O que não vai acontecer</strong> — não vira meta individual, não
    vira ranking público, não é usado isolado para decisão disciplinar.</li>
    <li><strong>Perguntas</strong> — reserve metade do tempo. Elas vêm.</li>
  </ol>

  <h2>As perguntas que sempre aparecem</h2>

  <div class="tw"><table>
    <thead><tr><th>Pergunta</th><th>Resposta honesta</th></tr></thead>
    <tbody>
      <tr><td>“Vocês vão ler minhas conversas?”</td>
          <td>Não. O sistema registra qual programa esteve em foco e por quanto tempo — não o conteúdo.</td></tr>
      <tr><td>“E se eu precisar resolver algo pessoal?”</td>
          <td>Ninguém trabalha 8 horas ininterruptas. O painel olha padrão de semanas, não o minuto.</td></tr>
      <tr><td>“Isso vai virar meta?”</td>
          <td>Não. É insumo de conversa e de dimensionamento — o que vira meta é entrega.</td></tr>
      <tr><td>“Funciona no meu computador de casa?”</td>
          <td>Só é instalado em equipamento da empresa. Máquina pessoal, nunca.</td></tr>
      <tr><td>“Quem garante que é assim?”</td>
          <td>Está no termo de ciência que você recebe, e o registro é auditável.</td></tr>
    </tbody>
  </table></div>

  <h2>Os documentos</h2>

  <ul>
    <li><strong>Comunicado</strong> — o mesmo conteúdo da reunião, por escrito, para consulta.</li>
    <li><strong>Política de monitoramento</strong> — o documento formal: finalidade,
    base legal, o que se coleta, retenção, quem acessa, direitos.</li>
    <li><strong>Termo de ciência</strong> — ciência, não autorização. A distinção
    importa: com legítimo interesse como base, você não está pedindo permissão; está
    registrando que a pessoa foi informada.</li>
    <li><strong>FAQ</strong> — as perguntas da tabela acima, respondidas.</li>
  </ul>

  <h2>Os primeiros 30 dias</h2>

  <p>Não abra o painel para a liderança na primeira semana. O dado inicial é ruim:
  faltam categorias configuradas, PCs sem dono definido, e a novidade distorce o
  comportamento. Decisão tomada em cima disso queima a credibilidade do projeto
  logo no começo.</p>

  <ol>
    <li><strong>Semana 1</strong> — instalar, atribuir cada máquina a uma pessoa,
    ajustar o catálogo do que é trabalho no <em>seu</em> escritório.</li>
    <li><strong>Semana 2</strong> — conferir se os números fazem sentido para quem
    conhece a operação. Se não fizerem, o problema é de configuração.</li>
    <li><strong>Semanas 3 e 4</strong> — primeira leitura por setor, nunca por
    pessoa.</li>
    <li><strong>Dia 30</strong> — devolva algo à equipe. Um achado, uma mudança de
    processo, um prazo redistribuído.</li>
  </ol>

  <div class="destaque">
    <span class="rot">O teste de fogo</span>
    <p>O primeiro uso público do painel define o resto. Se for para cobrar uma
    pessoa, todo mundo entende o recado e o dado morre ali. Se for para tirar
    trabalho manual do caminho ou redistribuir carga no fechamento, o projeto vira
    ferramenta da equipe — e aí ele funciona.</p>
  </div>

  <p>A base legal disso está em
  <a href="/blog/lgpd-monitoramento-de-funcionarios">LGPD e monitoramento de
  funcionários</a>.</p>
''',
},

]
