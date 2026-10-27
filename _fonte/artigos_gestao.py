# -*- coding: utf-8 -*-
"""
Artigos de eixo gestão e operação.

Mesma regra do outro arquivo: nada aqui promete comportamento que o produto não
tem. Os números usados em exemplo são declarados COMO exemplo — número inventado
com cara de pesquisa é o tipo de coisa que o cliente cita numa reunião e depois
descobre que não existe.
"""

GESTAO = [

# ─────────────────────────────────────────────────────────────────────────────
{
 'slug': 'produtividade-em-escritorio-contabil',
 'categoria': 'Gestão',
 'data': '2026-08-25',
 'titulo': 'Produtividade em escritório contábil: o que medir e o que ignorar',
 'descricao': 'Nem toda métrica de produtividade diz algo útil. Quais indicadores realmente '
              'ajudam a decidir num escritório contábil — e quais só produzem teatro.',
 'resumo': 'Medir a coisa errada é pior que não medir: gera ação confiante na direção '
           'errada. Um guia do que olhar, do que descartar e por quê.',
 'cta_titulo': 'Os números que fecham entre si',
 'cta_texto': 'Produtividade, jornada e padrões de trabalho — calculados pelo sistema, com '
              'a leitura do período em português ao lado de cada número.',
 'corpo': '''
  <p>“Produtividade” em escritório contábil costuma virar uma planilha de horas
  lançadas por cliente. Ela responde quanto foi cobrado. Não responde por que a
  equipe está afogada em maio, nem por que dois analistas com a mesma carteira
  entregam em ritmos diferentes.</p>

  <p>Para responder isso é preciso medir outra coisa — e deixar de medir
  algumas.</p>

  <h2>O que ignorar</h2>

  <h3>Horas na cadeira</h3>
  <p>Tempo de máquina ligada não é trabalho. Um dia de 10 horas com três horas de
  vaivém entre sistemas produz menos que um de 7 horas com blocos inteiros de
  atenção. Usar tempo total como indicador premia justamente quem trabalha pior.</p>

  <h3>Contagem de teclas e cliques como desempenho</h3>
  <p>São bons sinais de <em>atividade</em> — servem para distinguir “trabalhando”
  de “tela aberta e ninguém na frente”. Como medida de desempenho são péssimos:
  quem revisa um balanço complexo digita pouco e pensa muito, e quem faz digitação
  repetitiva bate recorde. Vira métrica, vira apertar tecla à toa.</p>

  <h3>Ranking individual público</h3>
  <p>Ranking de pessoas por qualquer métrica de atividade produz duas reações
  previsíveis: quem está embaixo aprende a inflar o número, e quem está em cima
  para de ajudar os outros. O comparativo útil é entre <em>períodos</em> e entre
  <em>setores</em> — ou de uma pessoa com ela mesma ao longo do tempo.</p>

  <h2>O que medir</h2>

  <h3>Tempo em ferramenta de trabalho, por setor</h3>
  <p>Quanto do expediente vai para e-CAC, SPED, eSocial, o sistema contábil, a
  planilha. É o indicador mais direto de para onde o dia vai — e o mais fácil de
  agir sobre. Descobrir que o Fiscal gasta duas horas por dia dentro do portal da
  Receita é o começo de uma conversa sobre automação.</p>

  <h3>Sessão de foco</h3>
  <p>Blocos contínuos de atenção numa mesma tarefa. Trabalho contábil pede
  concentração: conferência de apuração feita em pedaços de seis minutos gera
  erro. Poucos blocos longos e muita fragmentação é um sinal de processo
  interrompido — reunião demais, notificação demais, ou uma equipe pequena demais
  atendendo cliente o dia inteiro.</p>

  <div class="destaque">
    <span class="rot">Dois números que são o mesmo fato</span>
    <p>“82 trocas de janela por hora” e “zero minutos de foco profundo” não são
    dois problemas. São um só: com 82 trocas por hora, nenhum trecho chega aos 25
    minutos que definem um bloco de foco. Painel que mostra os dois em linhas
    distantes obriga o leitor a fazer essa ligação sozinho — e a maioria não
    faz.</p>
  </div>

  <h3>Vaivém entre sistemas</h3>
  <p>Quantas vezes por hora a pessoa alterna entre as mesmas duas ou três
  ferramentas. Alternância alta e repetitiva entre o sistema contábil e uma
  planilha quase sempre significa <strong>transporte manual de dado</strong> — o
  candidato número um a automação, e o que mais consome tempo sem ninguém
  notar.</p>

  <h3>Distribuição da carga no tempo</h3>
  <p>Não a média do mês: a forma da curva. Um escritório que fecha tudo nos
  últimos cinco dias tem um problema de processo que a média esconde
  completamente.</p>

  <h3>Trabalho fora do expediente</h3>
  <p>Quantos dias, por setor, tiveram atividade além do horário previsto. É
  indicador de dimensionamento — e evidência para o inventário de riscos da
  <a href="/blog/nr-1-riscos-psicossociais">NR-1</a>.</p>

  <h2>Três travas que mantêm o número honesto</h2>

  <div class="tw"><table>
    <thead><tr><th>Trava</th><th>Por quê</th></tr></thead>
    <tbody>
      <tr><td><b>“Não sei” nunca vira zero</b></td>
          <td>Dia sem medição não é dia sem trabalho. Marcar como zero derruba a média e acusa alguém pelo defeito da ferramenta.</td></tr>
      <tr><td><b>Tempo não identificado fica fora da conta</b></td>
          <td>Navegador aberto sem que o sistema identifique o site é limitação de medição, não ociosidade.</td></tr>
      <tr><td><b>O contexto vem junto do número</b></td>
          <td>52% de produtividade significa coisas opostas para quem entrou há três semanas e para quem está há cinco anos na função.</td></tr>
    </tbody>
  </table></div>

  <h2>Um roteiro de leitura mensal</h2>

  <ol>
    <li>A carga está distribuída entre os setores, ou concentrada em um?</li>
    <li>Onde o tempo foi, por ferramenta — e isso bate com a receita de cada
    serviço?</li>
    <li>A fragmentação subiu em relação ao mês anterior? O que mudou no
    processo?</li>
    <li>Que atividade repetitiva aparece todo dia e poderia ser automatizada?</li>
    <li>Alguém está com jornada fora do padrão de forma sustentada?</li>
  </ol>

  <p>Cinco perguntas, uma hora por mês. É mais gestão do que a maioria dos
  escritórios faz — e nenhuma delas exige olhar o dia de ninguém em particular.</p>
''',
},

# ─────────────────────────────────────────────────────────────────────────────
{
 'slug': 'fechamento-fiscal-carga-da-equipe',
 'categoria': 'Operação',
 'data': '2026-08-28',
 'titulo': 'Fechamento fiscal: como distribuir a carga sem queimar a equipe',
 'descricao': 'O pico de fechamento é previsível — e mesmo assim pega o escritório de '
              'surpresa todo mês. Como usar dado para achatar a curva e proteger a equipe.',
 'resumo': 'Todo escritório sabe que o dia 20 vem. Poucos conseguem dizer, com número, '
           'onde a fila trava — e é por isso que o pico se repete idêntico.',
 'cta_titulo': 'Veja a curva do seu fechamento',
 'cta_texto': 'Carga por setor ao longo do mês, trabalho fora do expediente e dias sem '
              'pausa — para o próximo pico ser planejado em vez de sofrido.',
 'corpo': '''
  <p>A sazonalidade contábil é o raro problema de gestão com data marcada.
  Obrigações acessórias, apuração, folha, entrega — tudo se acumula nos mesmos dias
  de todo mês, e o pico anual é conhecido com um ano de antecedência.</p>

  <p>Mesmo assim, o roteiro se repete: a semana do prazo vira maratona, o
  atendimento a cliente para, alguém vira a noite, e no mês seguinte tudo
  acontece de novo do mesmo jeito.</p>

  <p>O motivo é quase sempre o mesmo: <strong>o escritório sabe que o pico existe,
  mas não sabe onde ele trava.</strong></p>

  <h2>Achar o gargalo real</h2>

  <p>Numa cadeia — cliente envia documento, alguém confere, alguém lança, alguém
  apura, alguém revisa, alguém transmite — a etapa que trava não é a mais visível.
  A mais visível é a última, porque é ela que estoura o prazo.</p>

  <p>Três perguntas que localizam o gargalo de verdade:</p>

  <ul>
    <li><strong>Em que dia do mês a carga de cada setor sobe?</strong> Se o
    lançamento só ganha volume no dia 15, o gargalo está antes — na chegada do
    documento do cliente.</li>
    <li><strong>Quanto tempo vai para retrabalho?</strong> Vaivém alto entre o
    sistema e a planilha, ou reabertura repetida do mesmo documento, indica
    conferência acontecendo tarde demais.</li>
    <li><strong>Qual setor entra em jornada estendida primeiro?</strong> Ele é o
    gargalo, mesmo que o atraso apareça em outro.</li>
  </ul>

  <blockquote><p>Contratar mais gente para a etapa final quando o gargalo está na
  entrada de documentos é caro e não resolve nada — a fila só passa a esperar em
  outro lugar.</p></blockquote>

  <h2>Quatro medidas que achatam a curva</h2>

  <h3>1. Escalonar prazos internos por carteira</h3>
  <p>Se todos os clientes têm o mesmo prazo interno, todo o trabalho chega junto.
  Dividir a carteira em blocos com prazos escalonados ao longo do mês transforma
  um pico em três ondas — mesma carga total, um terço da pressão de pico.</p>

  <h3>2. Antecipar o que não depende do fechamento</h3>
  <p>Boa parte do trabalho do dia 20 poderia ter sido feita no dia 8: conferência
  cadastral, conciliação parcial, validação de documento recebido. Medir quando
  cada tipo de tarefa acontece revela quanta coisa está sendo empurrada sem
  necessidade.</p>

  <h3>3. Atacar o transporte manual de dado</h3>
  <p>Alternância repetitiva entre as mesmas duas ferramentas é quase sempre alguém
  copiando dado de um lugar para outro. É o trabalho mais fácil de automatizar e o
  mais invisível na planilha de horas — some no meio da tarefa.</p>

  <h3>4. Reforço temporário no lugar certo</h3>
  <p>Reforço só funciona se entrar antes do pico e na etapa que trava. Com a curva
  medida, dá para saber qual semana e qual setor — em vez de contratar em pânico
  na semana do prazo, quando treinar alguém custa mais tempo do que economiza.</p>

  <h2>Proteger a equipe é parte do plano</h2>

  <p>Fechamento é o momento de maior risco psicossocial do ano contábil:
  concentração de prazo, pressão inegociável e pouca autonomia sobre o ritmo — a
  combinação exata que a <a href="/blog/nr-1-riscos-psicossociais">NR-1</a> pede
  para gerenciar.</p>

  <p>Duas coisas simples ajudam mais do que parecem:</p>

  <ul>
    <li><strong>Compensação real depois do pico</strong>, com dia efetivamente
    livre — não “tira quando der”, que nunca dá.</li>
    <li><strong>Limite explícito de horário</strong> durante o pico. Sem regra, o
    trabalho ocupa a noite inteira e a produtividade do dia seguinte cai, o que
    alonga o pico.</li>
  </ul>

  <div class="destaque">
    <span class="rot">O ciclo que se paga</span>
    <p>Meça um fechamento inteiro sem mudar nada. Escolha uma medida para o
    próximo. Meça de novo e compare. Em três ciclos você tem um processo ajustado
    com evidência — e um argumento concreto na hora de discutir preço com o
    cliente que dá mais trabalho do que paga.</p>
  </div>
''',
},

# ─────────────────────────────────────────────────────────────────────────────
{
 'slug': 'como-escolher-software-de-monitoramento',
 'categoria': 'Gestão',
 'data': '2026-08-31',
 'titulo': 'Como escolher um software de monitoramento: 7 perguntas',
 'descricao': 'Nem toda ferramenta de monitoramento serve para uma empresa brasileira. As '
              'sete perguntas que separam um produto defensável de um passivo jurídico.',
 'resumo': 'A maioria das ferramentas do mercado foi desenhada num contexto legal diferente '
           'do brasileiro. Sete perguntas revelam isso antes da assinatura.',
 'cta_titulo': 'Faça as sete perguntas para a gente',
 'cta_texto': 'A Monitora Contábil responde todas por escrito, na Política de Privacidade — '
              'incluindo a lista do que o sistema nunca coleta.',
 'corpo': '''
  <p>Há dezenas de ferramentas de monitoramento no mercado, e a maior parte nasceu
  em outro contexto legal — onde captura de tela periódica e gravação de sessão são
  práticas comuns. Trazer isso para uma empresa brasileira é importar um passivo.</p>

  <p>Estas sete perguntas resolvem a triagem antes da demonstração comercial.</p>

  <h2>1. O que ele captura, item por item?</h2>

  <p>Peça a lista completa, por escrito. As respostas que devem acender alerta:</p>

  <div class="tw"><table>
    <thead><tr><th>Recurso</th><th>Leitura</th></tr></thead>
    <tbody>
      <tr><td>Captura de tela periódica</td><td>Alta invasividade. Alcança dado de cliente e dado sensível por tabela</td></tr>
      <tr><td>Gravação de sessão em vídeo</td><td>Mesmo alcance, continuado no tempo</td></tr>
      <tr><td>Registro do conteúdo digitado</td><td>Captura senha pessoal e conversa privada. Difícil de justificar</td></tr>
      <tr><td>Acesso à webcam</td><td>Sem justificativa em trabalho administrativo</td></tr>
      <tr><td>Contagem de teclas e cliques</td><td>Aceitável: mede atividade sem conteúdo</td></tr>
      <tr><td>Programa e site em foco, com tempo</td><td>O núcleo útil da medição</td></tr>
    </tbody>
  </table></div>

  <p>Alta invasividade não significa “proibido”: significa que o recurso precisa
  vir cercado. Se a ferramenta oferece captura ou gravação de tela, as perguntas
  seguintes são estas — e a ausência de qualquer uma delas é o alerta de verdade:
  vem desligado por padrão? é contratado computador a computador, e não para a
  empresa inteira de uma vez? a pessoa é avisada individualmente antes do primeiro
  quadro? quem assiste fica registrado? o prazo de guarda é curto e próprio?</p>

  <p>Se o fornecedor tratar “o que não coletamos” como pergunta incômoda, isso já
  é a resposta.</p>

  <h2>2. Dá para desligar o que não interessa?</h2>

  <p>Recurso invasivo que não pode ser desligado é recurso que você vai ter que
  declarar na sua política — e defender numa fiscalização. Ferramenta madura
  permite escolher; e o que ela faz por padrão diz muito sobre a mentalidade de
  quem a construiu.</p>

  <h2>3. Onde os dados ficam, e por quanto tempo?</h2>

  <ul>
    <li>Em que país estão os servidores?</li>
    <li>Qual o prazo de retenção padrão, e ele é configurável?</li>
    <li>O expurgo é <strong>automático</strong> ou depende de alguém lembrar?</li>
    <li>O que acontece com os dados quando o contrato acaba?</li>
  </ul>

  <p>Retenção infinita é o padrão de muitas ferramentas, e é incompatível com o
  art. 15 da LGPD.</p>

  <h2>4. Como ele responde a um pedido do titular?</h2>

  <p>Um colaborador pede para ver tudo o que foi registrado sobre ele. Quanto tempo
  leva? Se a resposta envolver abrir chamado com o fornecedor e esperar dias, o
  processo vai falhar na primeira vez que for usado — e o prazo do art. 18 é seu,
  não do fornecedor.</p>

  <h2>5. Ele produz ranking e nota individual?</h2>

  <p>Ferramentas que atribuem “produtividade: 73/100” a cada pessoa vendem bem e
  fazem estrago. O número parece objetivo, esconde o método, e vira base para
  decisão sobre a carreira de alguém.</p>

  <p>Pergunte também se há qualquer inferência sobre estado emocional ou saúde
  mental. Se houver, você passou a tratar <strong>dado sensível</strong> — outra
  categoria da LGPD, com exigências muito mais duras.</p>

  <h2>6. O que acontece quando ele não consegue medir?</h2>

  <p>Pergunta técnica que revela a honestidade do produto. Quando o agente não
  identifica o que está em foco, aquele tempo vira zero na conta, ou fica de fora
  como “não medido”?</p>

  <blockquote><p>Ferramenta que transforma ausência de medição em zero produz
  relatório dizendo que alguém não trabalhou num dia em que ela apenas não
  conseguiu enxergar. E esse relatório vai chegar na mesa de um gestor.</p></blockquote>

  <h2>7. Ele ajuda na implantação, ou só entrega o instalador?</h2>

  <p>A implantação correta é o que separa dado confiável de teatro. Fornecedor que
  entrega apenas o executável está deixando com você a parte que dá processo:
  comunicado, política, termo de ciência, condução da reunião.</p>

  <h2>Uma pergunta bônus, específica do seu setor</h2>

  <p>Se você é escritório contábil: <strong>o catálogo já vem curado?</strong> Uma
  ferramenta genérica não sabe que e-CAC, SPED, eSocial, Sefaz e o sistema
  contábil são trabalho — e alguém do seu time vai passar horas classificando
  centenas de aplicativos e sites na mão. É nessa tela que a implantação costuma
  morrer.</p>

  <div class="destaque">
    <span class="rot">A regra de bolso</span>
    <p>Escolha a ferramenta menos invasiva que responde à sua pergunta de gestão.
    Capacidade que você não usa não fica neutra: ela precisa ser declarada,
    defendida e protegida — e é ela que vai aparecer no dia do incidente.</p>
  </div>
''',
},

# ─────────────────────────────────────────────────────────────────────────────
{
 'slug': 'custo-da-hora-ociosa-no-escritorio',
 'categoria': 'Gestão',
 'data': '2026-09-01',
 'titulo': 'Quanto custa a hora ociosa no seu escritório contábil',
 'descricao': 'Como calcular o custo real de uma hora de trabalho, o que conta como '
              'ociosidade de verdade e por que a conta simples engana.',
 'resumo': 'A conta que a maioria faz — salário dividido por horas — subestima o custo pela '
           'metade. E a maior parte do desperdício não é o que se imagina.',
 'cta_titulo': 'Descubra para onde o dia vai',
 'cta_texto': 'Tempo por ferramenta, retrabalho e transporte manual de dado — medidos por '
              'setor, com a leitura do período junto de cada número.',
 'corpo': '''
  <p>“Hora ociosa” é uma expressão que atrapalha mais do que ajuda, porque sugere
  gente parada. Na prática, quase todo o desperdício em escritório contábil
  acontece com a pessoa <strong>ocupada</strong> — fazendo trabalho que não
  precisava existir.</p>

  <p>Mas para dimensionar isso é preciso saber quanto custa uma hora.</p>

  <h2>O custo real de uma hora</h2>

  <p>A conta comum é salário dividido por 220 horas. Ela erra por uma margem
  grande, porque ignora encargos, benefícios e — o mais esquecido — que ninguém
  trabalha 220 horas produtivas por mês.</p>

  <p>A estrutura correta, com valores de exemplo para um analista fiscal
  hipotético:</p>

  <div class="tw"><table>
    <thead><tr><th>Componente</th><th>Exemplo mensal</th></tr></thead>
    <tbody>
      <tr><td>Salário</td><td>R$ 3.500</td></tr>
      <tr><td>Encargos, provisões de férias e 13º</td><td>R$ 2.450</td></tr>
      <tr><td>Benefícios (VT, VR, plano)</td><td>R$ 800</td></tr>
      <tr><td>Rateio de estrutura (posto, software, energia)</td><td>R$ 600</td></tr>
      <tr><td><b>Custo total</b></td><td><b>R$ 7.350</b></td></tr>
    </tbody>
  </table></div>

  <p>O divisor também não é 220. Descontando férias, feriados, faltas e o tempo
  legítimo que não é tarefa — reunião, treinamento, pausa — sobra algo próximo de
  <strong>150 horas efetivas</strong> por mês.</p>

  <p>R$ 7.350 ÷ 150 = <strong>R$ 49 por hora</strong>. A conta ingênua daria R$ 16.
  Três vezes menos.</p>

  <div class="destaque">
    <span class="rot">Use os seus números</span>
    <p>Os valores acima são ilustrativos. A estrutura é o que importa: custo total
    dividido por horas efetivas, nunca salário dividido por horas contratuais.</p>
  </div>

  <h2>Onde o tempo realmente vai</h2>

  <p>Com a hora precificada, dá para dimensionar cada tipo de desperdício. Os
  quatro que mais aparecem em escritório contábil:</p>

  <h3>Transporte manual de dado</h3>
  <p>Copiar de um sistema para uma planilha, e da planilha para outro sistema.
  Aparece como alternância repetitiva entre as mesmas ferramentas, dia após dia.
  É o mais caro e o mais invisível — ninguém registra “passei 40 minutos copiando
  dado” na planilha de horas.</p>

  <h3>Retrabalho</h3>
  <p>O mesmo documento reaberto três vezes porque a conferência acontece tarde
  demais na cadeia. Custa duas vezes: o tempo refeito e o atraso que ele empurra
  para a frente.</p>

  <h3>Fragmentação</h3>
  <p>Aqui a conta é menos óbvia. Cada interrupção cobra o tempo dela <em>mais</em>
  o custo de recuperar o contexto. Numa tarefa de conferência, retomar a linha de
  raciocínio depois de uma interrupção leva vários minutos — e às vezes o erro que
  passa despercebido nasce exatamente aí.</p>

  <h3>Espera</h3>
  <p>Documento do cliente que não chegou, aprovação pendente, sistema fora do ar.
  Não é ociosidade de quem espera: é gargalo de processo. Some quando o processo
  muda, não quando alguém cobra a pessoa.</p>

  <h2>A conta que decide investimento</h2>

  <p>Com a hora precificada, decisões de automação deixam de ser palpite.</p>

  <p>Suponha que a medição mostre 45 minutos por dia de transporte manual de dado,
  por analista, num time de seis pessoas:</p>

  <ul>
    <li>0,75 h × 6 pessoas × 21 dias = <strong>94,5 horas por mês</strong></li>
    <li>94,5 × R$ 49 = <strong>R$ 4.630 por mês</strong></li>
    <li><strong>R$ 55.560 por ano</strong> em trabalho que uma integração elimina</li>
  </ul>

  <p>Nenhuma dessas horas aparece como ociosidade. Todas aparecem como gente
  trabalhando duro.</p>

  <h2>A armadilha da conversa individual</h2>

  <p>É tentador levar esse número para uma conversa com uma pessoa específica.
  Não faça — por dois motivos.</p>

  <p>O primeiro é que quase todo desperdício desse tipo é <strong>de processo</strong>:
  a pessoa copia dado porque não existe integração, não porque escolheu copiar.
  O segundo é o efeito: cobrado individualmente pelo tempo em cada ferramenta, o
  time aprende a produzir o número certo. E aí você perdeu a medição.</p>

  <blockquote><p>O dado serve para mudar o processo. Quando ele vira cobrança
  individual, ele para de ser verdadeiro — e você fica sem os dois.</p></blockquote>

  <p>Sobre o que vale a pena acompanhar, veja
  <a href="/blog/produtividade-em-escritorio-contabil">o que medir e o que
  ignorar</a>.</p>
''',
},

# ─────────────────────────────────────────────────────────────────────────────
{
 'slug': 'sinais-de-sobrecarga-na-equipe',
 'categoria': 'Gestão',
 'data': '2026-09-02',
 'titulo': 'Sinais de sobrecarga na equipe: como identificar antes do afastamento',
 'descricao': 'Sobrecarga aparece na rotina meses antes de virar atestado. Quais sinais são '
              'observáveis, como interpretá-los sem rotular ninguém e o que fazer.',
 'resumo': 'Quando o afastamento chega, o processo que o causou já rodava há meses. Os '
           'sinais estavam visíveis — só não estavam sendo olhados.',
 'cta_titulo': 'Enxergue o padrão antes do problema',
 'cta_texto': 'Jornada estendida, dias sem pausa e trabalho em fim de semana — por setor, '
              'sem diagnóstico e sem escore individual.',
 'corpo': '''
  <p>Afastamento por transtorno mental não acontece de repente. Ele é o fim de um
  processo que costuma levar meses, e esse processo deixa rastro na rotina de
  trabalho muito antes de virar atestado.</p>

  <p>O problema é que quase ninguém olha para esse rastro — e quando olha, olha
  para a pessoa errada.</p>

  <h2>Os sinais observáveis</h2>

  <p>São padrões de <strong>rotina</strong>, não de personalidade. Nenhum deles
  isolado significa alguma coisa; o que importa é a combinação, e a persistência
  por semanas.</p>

  <h3>Extensão sustentada da jornada</h3>
  <p>Trabalhar além do horário num fechamento é normal. Fazer isso quinze dias por
  mês, três meses seguidos, é outro fenômeno — deixou de ser pico e virou o
  padrão.</p>

  <h3>Ausência de pausa</h3>
  <p>Sequências longas sem interrupção significativa, dia após dia. É um dos
  sinais mais consistentes, porque a pausa é a primeira coisa que some quando a
  carga aperta.</p>

  <h3>Invasão do fim de semana</h3>
  <p>Atividade em sábado e domingo de forma recorrente, fora do período de pico.
  Quando aparece, quase sempre significa que a carga da semana não cabe na semana.</p>

  <h3>Trabalho noturno fora do padrão da pessoa</h3>
  <p>A comparação aqui é com o próprio histórico, nunca com o time. Quem sempre
  trabalhou à noite não mudou nada; quem nunca trabalhou e passou a trabalhar,
  mudou.</p>

  <h3>Fragmentação crescente</h3>
  <p>Aumento sustentado do vaivém entre tarefas, com queda dos blocos de atenção.
  É frequentemente o primeiro sinal — e costuma ser lido, erradamente, como falta
  de foco da pessoa. Sob carga alta, a fragmentação é sintoma, não causa.</p>

  <h2>Como ler sem rotular</h2>

  <p>Aqui mora o risco de todo o assunto, e ele é grande o suficiente para ter
  regra própria:</p>

  <div class="tw"><table>
    <thead><tr><th>Não faça</th><th>Faça</th></tr></thead>
    <tbody>
      <tr><td>Inferir burnout, ansiedade ou depressão</td>
          <td>Descrever o padrão de rotina observado</td></tr>
      <tr><td>Criar escore de risco por pessoa</td>
          <td>Olhar a distribuição por setor e por período</td></tr>
      <tr><td>Comparar pessoas entre si</td>
          <td>Comparar a pessoa com o próprio histórico</td></tr>
      <tr><td>Concluir a partir de uma semana</td>
          <td>Exigir persistência de várias semanas</td></tr>
      <tr><td>Tratar como problema de resiliência</td>
          <td>Tratar como problema de dimensionamento e prazo</td></tr>
    </tbody>
  </table></div>

  <blockquote><p>Software não diagnostica ninguém. Ele mostra que uma pessoa
  trabalhou 14 dias seguidos sem pausa — o que é um fato sobre a organização do
  trabalho, não sobre a saúde dela.</p></blockquote>

  <p>Inferência sobre saúde mental cria <strong>dado sensível</strong> sob a LGPD,
  com exigências muito mais duras — e, pior que isso, é imprecisa. Vários dos
  sinais acima aparecem em quem está apenas com prazo apertado, e não aparecem em
  quem está em sofrimento silencioso.</p>

  <h2>O que fazer com o sinal</h2>

  <p>A resposta certa quase nunca é falar com a pessoa sobre o número. É verificar
  o contexto antes de concluir qualquer coisa:</p>

  <ol>
    <li><strong>Confira o óbvio primeiro.</strong> Férias de um colega, licença,
    saída de alguém do setor, cliente novo grande. Metade dos sinais tem explicação
    imediata na escala.</li>
    <li><strong>Olhe o setor, não a pessoa.</strong> Se três das cinco pessoas
    apresentam o mesmo padrão, o problema é de carga, e falar com uma delas seria
    responsabilizá-la por um problema seu.</li>
    <li><strong>Se for individual, converse — sobre o trabalho.</strong> “Notei que
    você tem ficado bem além do horário nas últimas semanas. O que está pegando?”
    Aberta, sobre a tarefa, sem números na mesa.</li>
    <li><strong>Aja no processo.</strong> Redistribuir carteira, escalonar prazo,
    contratar reforço, cortar retrabalho. Conversa sem mudança de carga não muda
    nada — e queima a próxima conversa.</li>
    <li><strong>Registre.</strong> Sinal identificado, medida adotada, resultado.
    É isso que o plano de ação da <a href="/blog/nr-1-riscos-psicossociais">NR-1</a>
    pede.</li>
  </ol>

  <div class="destaque">
    <span class="rot">O sinal mais confiável não está no software</span>
    <p>É a conversa de rotina. Dado serve para dizer <em>onde</em> olhar e para
    tornar visível o que se acumula devagar demais para ser percebido. A pergunta
    ainda tem que ser feita por uma pessoa.</p>
  </div>

  <p>Sobre o dever legal de gerenciar esse risco, veja
  <a href="/blog/nr-1-riscos-psicossociais">NR-1 e riscos psicossociais</a>.</p>
''',
},

]
