<table>
<tr>
<td>
<a href= "https://www.ipt.br/"><img src="https://www.ipt.br/imagens/logo_ipt.gif" alt="IPT" border="0" width="70%"></a>
</td>
<td><a href= "https://www.inteli.edu.br/"><img src="https://www.inteli.edu.br/wp-content/uploads/2021/08/20172028/marca_1-2.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0" width="30%"></a>
</td>
</tr>
</table>

<font size="+12"><center>
Concepção de sistema de automação industrial

</center></font>

> _Observação 1: A estrutura inicial deste documento é só um exemplo. O seu grupo deverá alterar esta estrutura de acordo com o que está sendo solicitado nos artefatos._

> _Observação 2: O índice abaixo não precisa ser editado se você utilizar o Visual Studio Code com a extensão **Markdown All in One**. Essa extensão atualiza o índice automaticamente quando o arquivo é salvo._

**Conteúdo**

- [Autores](#autores)
- [Visão Geral do Projeto](#visão-geral-do-projeto)
  - [Empresa](#empresa)
  - [O Problema](#o-problema)
  - [Objetivos](#objetivos)
 	- [Objetivos gerais](#objetivos-gerais)
  	- [Objetivos específicos](#objetivos-específicos)
  - [Partes interessadas](#partes-interessadas)
  - [Análise do cenário: Matriz SWOT](#análise-do-cenário-matriz-swot)
  - [Proposta de Valor: Value Proposition Canvas](#proposta-de-valor-value-proposition-canvas)
  - [Matriz de Risco](#matriz-de-risco)
  - [Oceano Azul](#oceano-azul)
  - [Análise Financeira](#análise-financeira)
- [Requisitos do Sistema](#requisitos-do-sistema)
  - [Personas](#personas)
  - [Mapa de Jornada do Usuário](#mapa-de-jornada-do-usuário)
  - [Histórias dos usuários (user stories)](#histórias-dos-usuários-user-stories)
- [Arquitetura do Sistema](#arquitetura-do-sistema)
  - [Módulos do Sistema e Visão Geral (Big Picture)](#módulos-do-sistema-e-visão-geral-big-picture)
   - [Croqui](#croqui)
    - [Diagrama da solução](#diagrama-da-solução)
  - [Descrição dos Subsistemas](#descrição-dos-subsistemas)
   - [Requisitos de software](#requisitos-de-software)
  - [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [UX e UI Design](#ux-e-ui-design)
  - [Frontend](#frontend--storyboard)
- [Testes de Hardware](#testes-de-hardware)
  - [Braço robótico](#braço-robótico)
   - [Alcance do braço](#alcance-do-braço)
    - [Posicionamento das bandejas](#posicionamento-das-bandejas)
    - [Conexão com servidor](#conexão-com-servidor)
  - [Eletroímã](#eletroímã)
   - [Controle do eletroímã](#controle-do-eletroímã)
    - [Controle de potência do eletroímã](#controle-de-potência-do-eletroímã)
     - [_Controle de potência do eletroímã através de um servidor_](#controle-de-potência-do-eletroímã-através-de-um-servidor)
- [Backend](#backend)
- [Frontend](#frontend)
- [Requisitos de conectividade](#requisitos-de-conectividade)
- [Controle de movimentação](#controle-de-movimentação)
- [Tabela de testes](#tabela-de-testes)
- [Dispositivo Eletrônico](#dispositivo-eletrônico)
  - [Esquemático](#esquemático)
   - [Identificação das ligações](#identificação-das-ligações)
  - [Layout da placa](#layout-da-placa)
  - [Montagem placa de cobre](#montagem-placa-de-cobre)
- [Dispositivos Mecânicos](#dispositivos-mecânicos)
  - [Lista de Peças](#lista-de-peças)
  - [Lista de Materiais](#lista-de-materiais)
  - [Desenho Técnico](#desenho-técnico)
   - [Suporte para a Célula de Carga](#suporte-para-a-célula-de-carga)
   - [Suporte para o Eletroímã](#suporte-para-o-eletroímã)
    - [Base](#base)
    - [Tampa](#tampa)
  - [Modelagem 3D](#modelagem-3d)
   - [Suporte para Eletroímã](#suporte-para-eletroímã)
      	- [Base - 1° Versão](#base---1-versão)
      	- [Tampa - 1° Versão](#tampa---1-versão)
      	- [Base - 2° Versão](#base---2-versão)
      	- [Tampa - 2° Versão](#tampa---2-versão)
  - [Planejamento do Método de Fabricação](#planejamento-do-método-de-fabricação)
    	- [Suporte Célula de Carga](#suporte-célula-de-carga)
    	- [Base suporte para Eletroímã](#base-suporte-para-eletroímã)
    	- [Tampa suporte para Eletroímã](#tampa-suporte-para-eletroímã)
    	- [Primeira versão construída do suporte para eletroímã](#primeira-versão-construída-do-suporte-para-eletroímã)
    	- [Segunda versão do suporte para eletroíma](#segunda-versão-do-suporte-para-eletroíma)
    	- [Base para os componentes eletrônicos](#base-para-os-componentes-eletrônicos)
      	- [Primeira versão base para os componentes eletrônicos](#primeira-versão-base-para-os-componentes-eletrônicos)
    	- [Segunda versão base para os componentes eletrônicos](#segunda-versão-base-para-os-componentes-eletrônicos)
  - [Testes dispositivos mecânicos](#testes-dispositivos-mecânicos)
- [**Planejamento do Método de Fabricação**](#planejamento-do-método-de-fabricação-1)
- [**Lista de Materiais**](#lista-de-materiais-1)
- [**Resultados integração do projeto**] (#resultados-integração-do-projeto)
- [Referências](#referências)

# Autores

-   Alysson Cordeiro 
-   Giovana Rodrigues Araujo 
-   Henrique Lemos Freire Matias 
-   Lucas Henrique Sales de Souza 
-   Lyorrei Shono Quintão 
-   Mihaell Brenno Alves 
-   Patricia Honorato Moreira 

# Visão Geral do Projeto

## Empresa

O IPT (Instituto de Pesquisas Tecnológicas), localizado em São Paulo, é uma instituição brasileira focada em promover o desenvolvimento tecnológico e a inovação em diversos setores.

Fundade em 1899, é um dos principais centros de pesquisa do país, sendo referência pelo mundo na sua prestção de serviços de consultoria e assistência técnica.

## O Problema

O processo de separação de minerais realizado pelo IPT é manual, executado por meio de um técnico operador, que aproxima uma barra de ímã de ferrite, envolto em um saco plástico, do material que está submerso e espalhado em um recipente com água.

Nessa etapa, o operador aproxima o íma sobre um primeiro recipiente que contém toda a amostra, para em seguida, em um segundo recipiente, limpar as impurezas contidas na amostra. Por fim os minerais são depositados em um recipiente final, que também contém água.

Infere-se que esse processo é impreciso, sendo realizado diversas vezes e demandando treinamento apropriado do operador. Os metais não são totalmente retirados na primeira passagem pelo ferromagnético, em suma pela imprecisão do campo magnético do eletroímã devido a distância de manipulação, mas também pela necessidade de se testar diferentes campos por meio da troca de ímãs.

## Objetivos

### Objetivos gerais

Desenvolveremos um equipamento automatizado que tenha capacidade de aplicar um campo magnético constante, com intensidade e distância ajustáveis, ao longo de toda a amostra, promovendo, assim, uma separação dos minerais magnéticos, os quais serão depositados em um recipiente diferente dos minerais não magnéticos que permanecerão depositados na bandeja original.

### Objetivos específicos

<ul> <li> Controle do campo magnético sobre toda a amostra a fim de reduzir os erros de ensaio decorrentes da ação humana; </li> <li> Maior qualidade na execução do ensaio, principalmente no que tange a repetibilidade e reprodutibilidade; </li> <li> Maior flexibilidade de ensaios, pois o uso de eletroímãs ajustáveis dispensa a necessidade de se ter ímãs com o campo desejado; </li> <li> Determinação mais precisa do campo magnético adequado para diferentes ensaios. </li> </ul>

## Partes interessadas

-   IPT;
-   Laboratório de Processos Metalúrgicos;
-   Inteli.

## Proposta de Valor: Value Proposition Canvas

<br/>
<a href="https://miro.com/welcomeonboard/TXJwR01NMXBRZ0U4SXFvYml2S3J5UlRNdnlUdWhFM3dRRUpSTWdYaDgzdjhOUFU0aTZzcjN4MURmenhKNmpXQ3wzNDU4NzY0NTE5NDk4MTY1NjAxfDI=?share_link_id=204094303509" >
<img src="./img/Chat_IPT___Proposta_de_Valor.jpg" alt="Proposta de Valor do GPT Robot" />
</a>
Nossa proposta de valor envolve automatizar o processo de separação de metais que o IPT faz, sem alterar sua metodologia. Além disso, ela conta com um dispositivo magnético (um eletroímã) e um braço robótico (Magician Lite). Nesse sentido, nossa solução levará precisão no projeto, tendo em vista que não será necessária a alocação de recurso humano para o processo de separação (o qual possui um erro humano atrelado); consistência, visto que garantimos que a ciclicidade do processo seja completamente idêntica em todos os ciclos; escalabilidade devido à variabilidade que nossos produtos podem ter em questão de usos; por fim, automação ao processo, já que não será mais executado por humanos.

## Matriz de Risco

<img width="693" alt="matriz de risco" src="https://user-images.githubusercontent.com/99269584/221373748-9b2fa2d7-169c-47b1-82e6-fc9b0e694f41.png">

RISCOS

-   Planejar um escopo maior do que o possível de entregar - Probabilidade: Médio; Impacto: Alta
-   Não entregar o projeto completo (integração com web app e etc) - Probabilidade: Médio; Impacto: Muito Alta
-   Falta de acesso a um teste real poderá prejudicar a criação de um produto escalável - Probabilidade: Muito Alta; Impacto: Baixo
-   Demandar muito tempo para determinadas atividades do projeto e negligenciar outras (como na configuração microcontrolador para a web application ou no frontend do serviço) - Probabilidade: Baixo; Impacto: Alta
-   Parâmetros de medidas para relatórios de ensaio não bem definidos - Probabilidade: Baixo; Impacto: Muito Alta
-   Não ter a participação de todos no desenvolvimento do frontend e backend - Probabilidade: Alta; Impacto: Médio
-   Desacordo do grupo nas ferramentas utilizadas - Probabilidade: Muito Baixo; Impacto: Muito Baixo
-   Ausência de integrantes do grupo nos desenvolvimentos - Probabilidade: Baixo; Impacto: Médio
-   Dias das instruções de programação incompatíveis com o tempo de desenvolvimento desejado para entregas da SPRINT - Probabilidade: Médio; Impacto: Médio
-   Erro na construção da peça de encaixe para o braço robôtico - Probabilidade: Médio; Impacto: Muito Alta

OPORTUNIDADES

-   Suporte do inteli e professores altamente qualificados - Probabilidade: Muito Alta; Impacto: Muito Alta
-   IPT ser um parceiro muito acessível e amigável em geral - Probabilidade: Alta; Impacto: Muito Alta
-   IPT ter conhecimento técnico e científico sobre o problema que estamos prototipando uma solução, nos auxiliará na resolução de possíveis dúvidas e sugestões de melhorias - Probabilidade: Baixo; Impacto: Alta
-   Desenvolver uma tecnologia escalável - Probabilidade: Médio; Impacto: Muito Alta
-   Curva de aprendizado do python ser muito simples - Probabilidade: Médio; Impacto: Alta

## Matriz do Oceano Azul

<img src="./img/Chat_IPT___Oceano_Azul.png"
alt="Gráfico do oceano azul"/>

Tendo em vista o gráfico acima, o qual compara nossa solução com o método tradicional e manual do IPT e com uma alternativa do mercado, a Grade Magnética, é necessário evidenciar 4 pontos importantes para nossa matriz de oceano azul:

<ul> <li> Primeiro, <strong>aumentaremos</strong> a <strong>consistência</strong> em relação aos métodos comparados, tendo em vista que o braço robótico, embora ajustável, executará todos os processos de maneira igual e consistente; </li> <li> Além disso, é evidente que precisamos <strong>criar</strong>, também, <strong>facilidade na manutenção</strong> do hardware e do código que compõem o projeto; </li> <li> Outrossim, visto que o <strong>preço</strong> de nossa solução é alto, precisamos encontrar formas de <strong>reduzir</strong> esse fator; </li> <li> Por fim, <strong>eliminaremos</strong> a necessidade de um <strong>técnico de instalação</strong> do braço robótico por meio de um manual de instalação limpo e simples de compreender.</li>  </ul>

## Análise Financeira

### Análise do custo do método atual

Pensando no método atual, os custos existentes são pertinentes a compra dos ímãs de neodímio e a remuneração do operador, contudo, em relação aos ímas, não levaremos como valor relevante já que esse é investido apenas inicialmente e que não há custos operacionais a curto prazo. Portanto, focando no salário de um operador, estimamos um valor de R$2800,00/mês, logo, há o gasto de R$140,00/dia. Num dia, temos uma carga horária de 8 horas e, de acordo com informações adquiridas com o parceiro, cada ensaio possui a duração de 30 minutos, consequentemente, são 16 ensaios/dia. Dividindo o gasto diário pela quantidade de ensaios sabemos que cada operação terá um custo de R$8,75/ensaio.

### Análise do custo do método ChatIPT

| **Componente** | **Preço** |
| :------------- | :-------- |
| Magitian Lite | R$15.000,00 |
| Eletroímã | R$53,96 |
| Garra personalizada | R$10,00 |
| Raspeberry Pi Pico W | R$49,90 |

Nessa primeira análise, pode-se notar que, com um investimento inicial de R$15.103,86 (quinze mil, cento e três reais e oitenta e seis centavos), nossa solução pode já ser implementada no ambiente de separação de metais do IPT. Além disso, prevemos despesas operacionais que podem estar relacionadas com o valor da energia que os esquipamentos utilizam e com a reposição das peças que mais posuem chance de quebrar após um ano de uso com poucos cuidados.

### ROI

É calculado para estimar o tempo necessário para recuperar o montante investido inicialmente. Diante disso, levando em consideração o custo operacional no valor de R$2,15 (energia elétrica e eventuais reposições de peças), para alcançar o valor inicial, um total de de 2290 ensaios deverão ser realizados, se tomarmos em conta a quantia de 16 ensaios/dia, 144 dias serão necessários. 

# Requisitos do Sistema

## Personas

<img src="./img/Chat_IPT___Persona.png" alt="Persona Rodrigo (técnico)"/>

## Mapa de Jornada do Usuário

<img src="./img/Chat_IPT___Jornada.png"
alt="Mapa de Jornada de usuário"/>

## Histórias dos usuários (user stories)

-   Eu, como técnico, quero poder automatizar a tarefa de manipulação de amostra de metais, para que eu possa alocar meu tempo em atividades mais valiosas.
-   Eu, como técnico, quero poder delegar a tarefa repetitiva de separação metálica para um braço mecânico, a fim de evitar o desgaste físico e mental que esse processo manual e repetitivo causa.
-   Eu, como técnico, gostaria de utilizar um braço mecânico preciso e confiável, para que eu possa realizar a tarefa de separação dos metais com eficiência e precisão, sem comprometer a qualidade dos resultados.
-   Eu, como técnico, quero poder anexar o braço mecânico à minha estação de trabalho, para que possa automatizar a separação de liga metálica da amostra através de um processo magnético.
-   Eu, como técnico, quero ter uma interface física, para controlar a movimentação precisa do braço mecânico.
-   Eu, como técnico, quero ter uma estrutura fácil de manutenção para garantir que o dispositivo possa ser mantido em boas condições de funcionamento ao longo do tempo.
-   Eu, como técnico, quero ter um encaixe para o braço mecânico criado a partir de modelagem 3D, para que possa garantir que o braço tenha uma interação perfeita com restante da estação e não prejudique o processo de separação de liga metálica.

# Arquitetura do Sistema

## Módulos do Sistema e Visão Geral (Big Picture)

### Croqui

<img src="./img/Chat_IPT___Croqui_V1.png"
alt="Primeira versão do croqui"/>

### Diagrama da solução

<img src="./img/Chat_IPT___Diagrama.png" 
alt="Diagrama da soluçao" />

## Descrição dos Subsistemas

### Requisitos de software

## Tecnologias Utilizadas

![image](./img/tecnologias.png)
<i>Tecnologias utilizadas</i>


## Frontend

O frontend do projeto que desenvolvemos em Flutter e Dart é uma parte crucial do projeto. Ele é responsável por apresentar as informações e funcionalidades para o usuário de maneira clara e intuitiva, sendo composto por três páginas que desempenham diferentes funções.

A primeira página é apenas uma página placeholder, ou seja, uma introdução que não apresenta nenhum conteúdo relevante. Ela serve apenas para dar uma ideia geral do que o aplicativo se trata.

A segunda página é onde o usuário pode ver como deve ser posicionado o robô e as bandejas para o processo de separação magnética. Além disso, há um botão que inicia o processo. Ela é fundamental para o usuário entender como deve ser feita a montagem do equipamento e iniciar a operação.

A terceira página é o acompanhamento em tempo real do processo. Além disso, ela possui botões que permitem executar funções no robô que está realizando o processo, como a parada de emergência, pausa, play, passar o processo para o próximo estágio, voltar o estágio e desligar o robô. Esses botões são importantes para dar ao usuário o controle total sobre a operação e garantir que ele possa pará-la ou modificá-la a qualquer momento.

Finalmente, foi realizada a ação de compilar o aplicativo e criar um APK para a utilização. Isso significa que o aplicativo será disponibilizado para download e poderá ser usado em dispositivos Android. Ademais, é interessante ressaltar que aplicativos desenvolvidos em Flutter tem suporte tanto para IOS, quanto para Android. Cabe ao parceiro decidir qual formato é mais viável para o sistema em produção. Com o frontend bem desenvolvido e as funcionalidades implementadas, esperamos oferecer uma ótima experiência ao usuário e atender a todas as suas necessidades em relação ao processo de separação magnética.

<a href="https://www.figma.com/file/b6kygCfYtm0hWXsw0XNdXH/Figma-ChatIPT?node-id=0%3A1&t=wsF46PhOCzPIPRJS-1">
<img src="./img/Chat_IPT___Interface.png" alt="Protótipo de interface"/>
</a>

# Backend

O backend da aplicação está localizado na pasta src/backend/app.py. Esse arquivo, quando executado, inicia um servidor socket na porta 3001. Nesse mesmo arquivo, criamos uma instância da classe "Dobot", a qual está localizada na pasta ´src/backend/services/dobot.py´. Nessa classe, estão definidos diversas funções que utilizam da biblioteca "pydobot" para executar comandos no robô. No arquivo app.py, fazemos subscribe em diversos tópicos socket, cada um responsável por algum tipo de interação com o robô, ou seja, cada um chamando diferentes funções da classe Dobot.

__Bibliotecas importadas na aplicação:__
- _socketio:_ cria um servidor WebSocket para comunicação entre o servidor e cliente.
- _services.dobot:_ módulo responsável por controla o Dobot Magician.
- _services.raspberry:_ módulo para comunicação com o Raspberry Pi.
- _socket:_ fornece funcionalidades de rede de baixo nível.
- _eventlet:_ biblioteca para lidar com redes e concorrência.
- _PySimpleGUI:_ biblioteca para criar interfaces gráficas de usuário simples (GUI).
- _threading:_ permite trabalhar com threads em Python.
- _os:_  funções para interagir com o sistema operacional.
- _Configuração do servidor WebSocket usando socketio.Server e socketio.WSGIApp._ As opções de configuração incluem a ativação de manipuladores assíncronos, logs e intervalos de ping personalizados.

A função __get_wifi_ip()__  obtém o endereço o IP da rede Wi-Fi do dispostivo que o código é executado por meio do __socket__. Na ocorrência de erros, é retornado o endereço IP local "127.0.0.1". Posteriormente, o endereço IP será usado para iniciar o servidor Flask. Após isso, a classe Dobot é instanciada para conexão do robô com o cliente, localmente, para envio e recebimento das informações que serão realizadas na rota do robô.

O conjunto de funções __@sio.event__, __@sio.on__ e __@sio.eventlet__ se referem ao conjunto de eventos que deverão acontecer após o servidor receber os comandos realizados pelo cliente na interface, que em seguida, são executados no robô e dispostivo eletrônico. Como descrito a seguir:
<br>
- _connect:_ exibe uma mensagem quando o cliente se conecta ao servidor.
- _dobot_connect:_ inicia conexão com o robô.
- _handle_start_cicle_: inicia os ciclos de movimentos do braço robótico e controla o número de ciclos. 
- _stop:_ pausa o movimento do robô.
- _reactivate:_retoma o movimento do robô. 
- _handle_emergency_stop:_interrompe o movimento do robô em caso de emergência. 
- _handle_advance_stage e handle_previous_stage:_ avançam ou retornam os estágios do ciclo de movimento do robô.
- _disconnect:_ desconecta o cliente e para a execução do robô.
- _Início do servidor:_ _ a função _ _start_server_ é usada para iniciar a aplicação em flask no servidor, na porta 3001.

Após execução do código, o servidor em flask abre uma interface web para o cliente e quando o usuário clica no botão "ENCERRAR" a aplicação é encerrada. 

# Requisitos de conectividade
O projeto apresentado requer uma conectividade estável e confiável entre todas as partes envolvidas, para garantir que as informações e comandos possam ser transmitidos de forma eficiente e segura.

Em primeiro lugar, o backend do sistema precisa ser executado em um computador com recursos adequados para rotear a rede wifi e estabelecer uma conexão socket. É importante que o computador seja capaz de processar grandes quantidades de dados rapidamente, para garantir que as informações sejam transmitidas de forma eficiente entre o robô e o cliente.

Em segundo lugar, o cliente precisa estar na mesma rede wifi que o servidor para se conectar por socket e emitir eventos. Isso significa que a rede wifi precisa ter uma conexão estável e forte o suficiente para permitir a comunicação entre os dois dispositivos sem interrupções ou perda de dados.

Em síntese, é importante que todo o sistema esteja em uma rede local, que não precise estar conectada à internet para funcionar. Isso garante que as informações sejam mantidas seguras e protegidas, sem o risco de serem interceptadas por terceiros mal-intencionados. Com esses requisitos atendidos, o sistema poderá executar as tarefas de forma eficiente e segura, sem interrupções ou falhas na comunicação.

# Desenvolvimento do Hardware e Testes

## Braço robótico

O primeiro item que analisamos no braço foi seu tipo de conexão. A forma de conexão que iniciamente é a mais fácil é via USB. Através disso, o conectamos a um notebook, e via uma biblioteca em python conseguimos solicitar movimentos e utilizar todas as suas ferramentas. Os primeiro testes então ocorreram a partir desse tipo de conexão mas almejamos solicitar essas atividades através de um microcontrolador.

### Alcance do braço

Primeiramente, seguindo o esquema de conexão mencionado anteriormente, testamos se o braço robótico possui alcance suficiente para trabalhar nas três bandejas. Para esse teste, alteramos manualmente no script a posição que estávamos solicitando para que o braço fosse sem alterar a sua altura. Assim que encontrávamos o ponto máximo para cada lado de movimento do braço, realizávamos a sua demarcação na mesa com uma caneta.
Os testes foram bem sucedidos, como pode ser visto no vídeo: 

[Teste sobre o alcance do braço.](https://user-images.githubusercontent.com/99269584/221435514-a22eae79-256b-4c16-8d6d-9cd2edccdae1.mp4)

### Posicionamento das bandejas

As bandejas são dispostas lateralmente no entorno do braço robótico. 

![SPRINT 5 CHAT GPT ](https://user-images.githubusercontent.com/99269584/230797724-b26a5411-fc41-4ad0-840b-2584c4af3e12.png)

# Controle de movimentação

O controle de movimentação do braço robótico permite que o sistema determine a trajetória ideal do braço robótico com base nas dimensões da bandeja de amostras e suas posições na bancada. Com base no escopo do projeto descrito, podemos entender que o Magician Lite é usado para manusear três bandejas diferentes, cada uma com um conjunto diferente de tarefas a serem executadas.

Na primeira bandeja, o braço robótico é programado para passar com o eletroímã três vezes para garantir que todos os materiais magnéticos sejam coletados. Na segunda bandeja, o braço robótico passa apenas uma vez, mas é utilizado para limpar o material. Por fim, na terceira bandeja, o braço robótico despeja o material magnético coletado anteriormente na primeira bandeja. O objetivo é armanezar esse material para o técnico realizar análises posteriormente. 

No escopo descrito, o controle do Magician Lite é realizado por meio do front end, que permite que um técnico controle cada etapa do processo de manuseio das bandejas de amostras. No teste realizado, é possível observar a integração do sistema, com a passagem do braço robótico nas amostras e o controle feito pelo usuário via interface web.

[Primeira versão dessa execução](https://user-images.githubusercontent.com/99269584/228046923-2ec1882a-0378-4bec-870e-582873d45abb.mp4)

### Conexão com servidor

Foi planejada a criação de um servidor que conseguisse receber requisições e se comunicar diretamente com o braço mecânico, executando movimentações e entendendo o status do processo de separação em tempo real. 

Ao final, foi possível criar um servidor embarcado no Raspberry Pi Pico W, o qual tinha a funcionalidade de receber um valor via uma requisição http que continha o valor que queríamos acionar o PWM. Os teste estam descritos da seção de testes do imã abaixo. O código da feature descrita pode ser encontrada em `src/embedded/websocketserver.py` .

## Eletroímã

Um eletroímã utiliza corrente elétrica para gerar um campo magnético. Nesse projeto realizaremos o controle do eletroímã por meio do sinal PWM (modulação por largura de pulso), o qual possibilita controlar a força do campo magnético por meio da quantidade de energia que se é entregue ao sistema. Esperamos controlar a intensidade do imã para facilitar a separação de materiais magnéticos.

### Controle do eletroímã

O primeiro teste realizado com eletroímã controlado pelo raspberry pi pico W, foi o de ligar e desligar o ímã. Para isso, conectamos o eletroímã a ponte H, um circuito eletrônico que controla a velocidade do motor variando a largura dos pulsos do sinal PWM.

Ademais, nesse circuito, o eletroímã conectado a ponte H, é controlado pelo pino 0 do rapsberry pi pico W. Ao definir-se o valor de 0 no código, o eletroímã liga, e com 1, o eletroímã é desligado. Nesse ciclo o eletroímã liga por 1s e depois desliga por 1s. Na montagem realizada para este projeto, a ponte H recebe alimentação por uma fonte de 5v.

No vídeo é demonstrado o teste realizado com uma moeda, que consistiu na montagem do eletroímã no braço robótico.

[vídeo](https://user-images.githubusercontent.com/99269584/221374609-9ee725ef-596e-4a0a-968d-72518479a653.mp4) 

### Controle de potência do eletroímã

Para realizar-se o teste de variação de força do campo magnético, delimitou-se uma rampa variando os valores do PWM de 0 até o máximo 65536, variando-se a largura do pulso de forma linear ao longo do tempo. Modificando-se a largura do pulso do sinal PWM, é possível controlar a corrente que passa pelo eletroímã, e portanto, controlar sua força magnética.

No teste realizado com uma moeda, o intervalo de tempo aplicado foi de 1ms, e observou-se que quanto mais próximo do valor máximo, maior era a aderância da moeda ao eletroímã.

Assim, por meio do teste, infere-se a possibilidade de implementação do sistema de controle da intensidade do eletroímã por meio da interface web desenvolvida, visto que os materiais magnéticos necessitam da aplicabilidade de diferentes intensidades no eletroímã para melhor aderência.

### Controle de potência do eletroímã através de um servidor

O controle de potência do eletroímã pelo servidor é realizado por meio de um código que implementa a funcionalidade da frequência PWM para o eletroímã, e conecta o microcontrolador Raspberry Pi Pico W a rede wifi para se comunicar com o backend, que recebe comandos do usuário via interface gráfica.

No [*código*](https://github.com/2023M5T2-Inteli/Chat-IPT/blob/main/src/raspberry/pwm_serial.py) é importada as bibliotecas: _sys, machine, time, socket e network_. Em seguida, existe a tentativa de importar a biblioteca _usocket_, se esta biblioteca não estiver disponível, é importada a biblioteca padrão socket.

Após isso, o código define o pino PWM e a frequência PWM. A função "turn_on_PWM" é criada para ligar o PWM eletroímã. Ela recebe um valor inteiro (entre 0 e 65_000) como parâmetro e tenta definir a intensidade do PWM para esse valor. A função retorna True se for bem sucedida e False caso contrário.

A função "turn_off_PWM" é criada para desligar o eletroímã. Ela não recebe nenhum parâmetro e define a intensidade do PWM para 0. A função retorna True se for bem sucedida e False caso contrário.

O loop de execução começa verificando se o programa está sendo executado diretamente (e não como um módulo importado). Em seguida, ele configura a placa Wi-Fi para criar um ponto de acesso SSID e a senha. O LED é definido como um pino de saída e é ligado.

Em seguida, o código entra em um loop infinito que lê qualquer informação que foi passada através do pino padrão da Raspberry Pi Pico. Se o valor passado for 0, o eletroímã é desligado chamando a função "turn_off_PWM". Se o valor passado for um número entre 1 e 65_000, o eletroímã é ligado com a intensidade definida pelo valor passado, chamando a função "turn_on_PWM".

No *teste realizado*, obervasse o funcionamento do circuito com alimentação de 10V para ponte H. O eletroímã é acionado via valores enviados pelo backend, a conexão com o Rapsberry Pi Pico W é feita via cabo USB. 

[teste realizado](https://user-images.githubusercontent.com/99269584/227998601-90640557-b044-4615-bfa4-ae840086af07.mp4)


# Tabela de testes

| Componentes                          | Entrada                                                    | Saída esperada                                                                                                   | Resultado                                                                                                                            |
| :----------------------------------- | :--------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------- |
| Braço robótico                       | Ativação por meio do aplicativo.                           | Movimentação feita corretamente pelas bandeja.                                                                   | Percorreu todas as bandejas sem esbarrar ou travar.                                                                                  |
| Eletroímã                            | Pelo código, inserção de diversos níveis de intensidade.  | Mudança da intensidade da atração do ímã proporcional ao valor inserido.                                         | Pela interface, as mudanças de intensidade não foram possíveis, contudo, por método hardcoding, o valor do campo magnético foi modificado.     |
| Aplicativo                           | Movimentação do robô pelas bandejas.                       | Exibição correta do estágio do processo e do ciclo.                                                              | A exibição foi feita corretamente.                                                                                                   |
| Aplicativo                           | Ativação do botão de pause pelo aplicativo.                | Parada do robô e permanência no estágio atual.                                                                   | A priori, houve um problema com a biblioteca utilizada, mas ele já foi resolvido e o processo ocorre corretamente. |
| Aplicativo                           | Ativação do botão de play pelo aplicativo.                 | Retorno da movimentação do estágio em que foi pausado.                                                           | A priori, houve um problema com a biblioteca utilizada, mas ele já foi resolvido e o processo ocorre corretamente. |
| Aplicativo                           | Ativação do botão de avanço pelo aplicativo.               | Avanço do estágio do processo, com o robô passando para a próxima bandeja e a mudança do estágio na interface.   |  A priori, houve um problema com a biblioteca utilizada, mas ele já foi resolvido e o processo ocorre corretamente. |
| Aplicativo                           | Ativação do botão de retorno pelo aplicativo.              | Retorno do estágio do processo, com o robô passando para a bandeja anterior e a mudança do estágio na interface. | A priori, houve um problema com a biblioteca utilizada, mas ele já foi resolvido e o processo ocorre corretamente. |
| Aplicativo                           | Ativação do botão de parada de emergência pelo aplicativo. | Parada imediata do robô, depois, movimentação levemente para cima.                                               | A priori, houve um problema com a biblioteca utilizada, mas ele já foi resolvido e o processo ocorre corretamente.  |

# Dispositivo Eletrônico

A construção do um dispositivo eletrônico foi feito em uma placa de cobre, na qual o Raspberry Pi Pico foi soldado na placa e os componentes de ligação com os sensores foram parafusados e soldados na placa.

## Esquemático

![image](./img/esquematico.png)
<i>Esquemático</i>

### Identificação das ligações

| Ponte H       | Regulador de tensão | Cor da ligação |
| :------------ | :------------------ | :------------- |
| GND (porta 8) | OUT-                | Preto          |
| VSS (porta 9) | OUT+                | Vermelho       |

| Ponte H | Eletroímas | Cor da ligação |
| :------ | :--------- | :------------- |
| OUT 1   | Negativo   | Preto          |
| OUT 2   | Positivo   | Vermelho       |

| Ponte H       | Microcontrolador | Cor da ligação |
| :------------ | :--------------- | :------------- |
| ENA (porta 6) | GP0 (porta 1)    | Amarelo        |

## Layout da placa

![image](./img/layout.png)
<i>Layout da placa</i>

## Montagem placa de cobre

A montagem da placa utilizada nesse projeto apresenta Raspberry Pi Pico W e ponte H soldados na placa. Também contém dois plugs banana fêmea que recebem VCC e GND para alimentar o circuito da ponte H. 

![SPRINT 5 CHAT GPT  (1)](https://user-images.githubusercontent.com/99269584/230798846-39709bf4-6899-41b8-8cbb-9083fc1af6f4.png)

No teste realizado, o funcionamento do circuito é feito por meio da alimentação de 12V para ponte H e com conexão via cabo USB com o Rapsberry Pi Pico W ao computador. **O teste pode ser visualizado na seção de resultados da integração desse documento.**

# Dispositivos Mecânicos

Peças criadas para o suporte dos componentes eletrônicos.

## Lista de Peças

| Peça                         | Quantidade | Descrição                                                                                                                                          |
| :--------------------------- | :--------- | :------------------------------------------------------------------------------------------------------------------------------------------------- |
| Base suporte para Eletroímã  | 1          | Peça inferior (base) onde os eletroímãs serão sustentados                                                                                          |
| Tampa suporte para Eletroímã | 1          | Peça superior (tampa) que será acoplada a base do suporte. A tampa terá uma haste para ser usada no braço robô assim como a caneta padrão do Dobot |
| Caixa protetora para Placa   | 1          | Caixa feita por um polímero onde ficará nossa placa, protegendo de impactos e certo nível de umidade                                               |

## Lista de Materiais

| Material                              | Descrição                                                                                                            |
| :------------------------------------ | :------------------------------------------------------------------------------------------------------------------- |
| ABS ou PA (Filamento de Impressão 3d) | Material plástico ou derivativo usado na impressão 3D. Os tipos escolhidos são ambos resistentes a certa temperatura |
| Pote plástico com tampa 15cm x 20cm   | Usado para a construção da caixa protetora da placa. 

## Desenho Técnico

### Suporte para o Eletroímã

#### Base

![Desenho técnico da base do suporte para o Eletroíma](./img/disp_mecanicos/base-suporte-ima.jpg)

#### Tampa

![Desenho técnico da parte superior do suporte para o Eletroíma](./img/disp_mecanicos/tampa-suporte-ima.jpg)

## Modelagem 3D

### Suporte para Eletroímã

#### Base - 1° Versão

![Render 3D da base do suporte para o Eletroíma](./img/disp_mecanicos/render-base-eletroima.jpg)

#### Tampa - 1° Versão

![Render 3D da base da parte superior do suporte para o Eletroíma](./img/disp_mecanicos/render-tampa-eletroima.jpg)

#### Base - 2° Versão

![Render 3D da base do suporte para o Eletroíma](./img/disp_mecanicos/inventor-base.jpg)

#### Tampa - 2° Versão

![Render 3D da base da parte superior do suporte para o Eletroíma](./img/disp_mecanicos/inventor-tampa.jpg)

## Planejamento do Método de Fabricação

### Base suporte para Eletroímã

A base de suporte para o Eletroímã consiste em uma caixa com a face superior aberta que segura os eletroímãs, sendo sustentado pela tampa dessa caixa. No centro há uma divisória de 4 pontas com um arco entre cada ponta adjacente, deixando o espaço necessário para os ímãs em formato de cilindro se encaixarem no suporte.

A partir da modelagem 3D da peça, iremos imprimir usando um filamento com a característica de resistência à temperatura, visto que nos testes do Eletroímã, notamos que apesar de baixa, houve aumento da temperatura ao usarmos por algum tempo. Ao pesquisar alguns materiais chegamos em 2 possíveis candidatos. São eles, o Nylon de Poliamida, um termoplástico semi-cristalino com baixa densidade e alta estabilidade térmica, e o ABS (**acrilonitrila butadieno estireno**) que possui a resistência ao calor semelhante

### Tampa suporte para Eletroímã

A tampa suporte para o eletroímã é a parte superior do conjunto de peças de suporte (base e tampa), ela tem a função de sustentar a base, conectar os fios do eletroímã ao controlador de potência, além de se acoplar ao robô através da haste cilíndrica similar a caneta padrão do dobot. Por se tratar de uma peça pertencente ao mesmo conjunto da peça anterior (Suporte ao Eletroímã), todas as informações dos planejamento de fabricação são as mesmas.

### Primeira versão construída do suporte para eletroímã
 
 A primeira versão da base do eletroímã foi construída com o recorte de uma placa de cobre e montagem dos eletroímãs parafusados. O eletroímã foi conectado aa ponte H por meio da extensão construída com fio de rede. Tal versão foi pensada para uma rápida prototipação e testes dos eletroímãs acoplados no braço robótico
 
 ![WhatsApp Image 2023-03-27 at 4 49 43 PM](https://user-images.githubusercontent.com/99269584/228051480-8b6ef59c-575f-4d1b-86fe-8c3d50003c03.jpeg)

### Segunda versão do suporte para eletroímã

 A segunda versão do suporte já foi impressa a partir da segunda versão do modelo 3D. O modelo foi pensado para sustentar até 4 imãs, havendo o espaço exato para encaixe, não necessitando parafusos além da tampa. Há 4 espaços entre os encaixes para os imãs e a haste do suporte para que a fiação passe por dentro da haste, facilitando o manuseio deles. Já a haste nessa versão foi passada para a própria base, isso foi pensado para facilitar a sustentação do conjunto da peça pelo robô (na outra versão ela estava localizada na tampa). Há também 4 buracos para parafusos M3 para vedação da tampa e do suporte, evitando que entre água no momento da separação magnética. Devido a alguns erros de medidas em relação a tampa, essa versão não foi testada acoplada ao braço robótico.

 ![Foto do conjunto Base e Tampa impresso em 3D](./img/disp_mecanicos/ft-part-impressa.jpg)

### Terceira versão do suporte para eletroímã

A versão final do suporte do eletroímã foi impressa em modelo 3D. Essa versão é igual a segunda versão mas possui as medidas corretas para encaixe do eletroímã. **O teste realizado com essa versão se encontra na seção de integração desse projeto.**

![SPRINT 5 CHAT GPT  (2)](https://user-images.githubusercontent.com/99269584/230799037-3ca5bb3e-02d4-4ef7-af06-5f79c4677821.png)

### Base para os componentes eletrônicos

#### Primeira versão base para os componentes eletrônicos
A primeira versão da base foi feita sem a soldagem dos componentes na placa de cobre perfurada, mas como os fios não poderia ficar soltos pelo riscos sd eperfuração e danos no circuito, elaborou-se uma base para a fixação foi criada por meio de uma placa de MDF. Porém, para ter uma vida útil melhor, essa placa deverá ser trocada por algum polímero e uma peça superior para a proteção será criada.

![image](./img/base.jpg)
<i>Imagem top-down</i>

### Segunda versão base para os componentes eletrônicos

Na segunda versão da base, perfuramos a placa e parafusamos os componentes que não poderiam ser soldados. Também adicionamos dois conectores de plug banana para recebimento de alimentação na ponte H. E utilizamos um pote de plástico para proteger a placa de cobre perfurada. Os próximos incluem tampar o pote com uma tampa e realizar furos de diâmetro pequeno para passagem dos cabos de rede, fonte de alimentação dos plugs e cabo USB que conecta-se com o Rapsberry Pi Pico W.

![IMG_20230327_113725](https://user-images.githubusercontent.com/99269584/228053083-7250744f-570f-4b9f-8a60-1a458787f18a.jpg)

### Terceira versão base para os componentes eletrônicos

Na versão final da base, a placa de cobre de fenolite foi reduzida e foram mantidos apenas a ponte H e Raspberry Pi Pico W soldados. O pote de plástico foi perfurado para passagem dos cabos USB e do fio de ligação da ponte H com o eletroímã. Os conectores de plug de banana também foram parafusados na lateral do pote para alimentação do sistema com a fonte. Nessa versão, objetivou-se assegurar que o protótipo final não tivesse falhas dos componentes com umidade por estarem próximos às bandejas. **O funcionamento desse sistema pode ser visto na seção de resultados de integração desse protótipo.**

![SPRINT 5 CHAT GPT  (1)](https://user-images.githubusercontent.com/99269584/230798846-39709bf4-6899-41b8-8cbb-9083fc1af6f4.png)

## Testes dispositivos mecânicos

O protótipo possui uma base com uma placa de cobre que contém os seguintes componentes: Raspberry Pi Pico W, ponte H e dois plugs banana fêmea. Além disso, há um dispositivo eletromecânico feito para um eletroímã com placa de cobre, que está acoplado no braço robótico por meio de uma caneta. A ponte H se interliga ao dispositivo eletromecânico do eletroímã por meio de um cabo de rede.

O principal objetivo do sistema é controlar o eletroímã e assegurar que o dispostivo esteja adequado no braço robótico. Nos passos a seguir, será descrito as respostas esperadas para cada um dos componentes e os testes realizados:

| Dispositivo Eletromecânico | Descrição e Resultado Esperado | Testes |
| --- | --- | --- |
| Placa de Cobre Base | É a base do sistema, na qual os componentes são fixados. Foi-se avaliado a resistência da placa e sua estabilidade para comportar os componentes, com uma conexão elétrica confiável, evitando-se possíveis problemas de curto. No teste realizado o sistema apresentou curto circuito no regulador de tensão de eletricidade da ponte H. Com isso, foi-se descartado esse componente e optou-se por realizar ligação do VCC de 10V diretamente na ponte H. A ponte H não apresentou falhas após essa alteração e apresentou os resultados esperados no eletroímã. A conexão com o Raspberry Pi Pico W também não apresentou falhas. | O teste foi realizado conectando os componentes à placa de cobre base e realizando as conexões elétricas. Foram realizados testes de resistência e estabilidade da placa, bem como testes de curto circuito, após a alteração na conexão elétrica da ponte H. |
| Base do Eletroímã | Esse componente é ativado pela passagem de energia elétrica por ele. Avaliou-se às alterações de corrente elétrica controladas pela ponte H, exercendo a força magnética esperada no dispositivo eletromecânico. Além disso, o eletroímã foi parafusado na placa de cobre de modo que não alterasse a sua força magnética. Para acoplamento no braço robótico, foi utilizada uma caneta em uma peça do próprio braço robótico. | O teste foi realizado aplicando diferentes correntes elétricas no eletroímã e avaliando a força magnética gerada no dispositivo eletromecânico. Também foi avaliada a fixação do eletroímã na placa de cobre e o acoplamento do dispositivo ao braço robótico. |

**O funcionamento completo do dispositivo mecânico pode ser visto na seção de resultados da integração desse documento.**

# **Planejamento do Método de Fabricação**

## **Lista de Materiais**

1. **MICROCONTROLADOR:** o microcontrolador responsável pela atuação é o RASPBERRY PI PICO W com Wi-Fi RP2040 133MHZ detensão de alimentação é de 1.8-5.5v dc, cuja fabricante é a Newark Corporation, RS Components, Farnell element14. O microcontrolador será responsável pela intervenção entre a interface amigável e o braço robótico e seus adjacentes.
2. **PONTE H:** módulo ponte H L298N; 2 canais de 2A DC. Permite controlar a direção, velocidade e sentido de rotação de um motor elétrico. Servirá para controlar as rotações do braço robótico.
3. **ELETROÍMÃ:** usado eletroímã solenóide redondo de.\*\* Atrai e separa o material ferromagnético do restante da amostra.
4. **PCB:** a placa de circuito impresso (PCB) usada para conectar os componentes eletrônicos, como resistores, capacitores e, inclusive, usado para o microcontrolador. Vale ressaltar que a placa é universal e inflexível. Além do mais, no protótipo, foi usado a placa perfurada de 12cm x 18cm de material fenolite; marca: _piscaled_.
5. **COMPONENTE MOBILE:** será necessária, para interação com o robô, um celular com interface amigável.
6. **BANDEJA:** deve ser usado 3 bandejas de plástico seco para não ter interferência no eletroímã.
7. **BRAÇO ROBÓTICO:** automação responsável pela separação diretamente dos sedimentos magnéticos. É usado o braço robótico DOBOT MAGICIAN LITE da empresa Dobot company.

|**Componentes**|**Quantidade**|**Descrição**|
| :---------------------------------------: | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------- |
|   Raspberry Pi Pico W com conexão wifi    | 1              | Coletar e processar informações                                                                                                          |
|         Placa de cobre perfurada          | 1              | Conectar, por meio da solda, todos os componentes.                                                                                       |
|                  Ponte H                  | 1              | Permite controlar a direção, velocidade e sentido de rotação de um motor elétrico. Servirá para controlar as rotações do braço robótico. |
|                 Eletroímã                 | 4              | Atrai e separa o material ferromagnético do restante da amostra.                                                                         |
|            Dobot Magitian Lite            | 1              | Braço robótico utilizado na movimentação dos eletroímãs entre as bandejas.                                                               |
|                 Bandejas                  | 3              | Utilizadas para o depósito da amostra, da limpeza do material e o depósito desse.                                                        |
|             Plug Fêmea Banana             | 2              | Usados para a alimentação.                                |
##

## Fabricação Dispostivo Eletrônico

A figura a seguir contém identificação dos conjuntos de passos a serem seguidos para a construção do dispositivo eletrônico e suas ligações com o computador e dispositivos mecânicos que se conectam ao computador.

![SPRINT 5 CHAT GPT  (1)](https://user-images.githubusercontent.com/99269584/230799652-26b24fae-0843-40e7-b7dd-c8c6cfa395d7.png)

**1. Montagem da Placa PCB**

  Nessa placa são soldados os componentes: Raspberry Pi Pico W e Ponte H. São também inseridas as trilhas de ligação que foram definidas anteriormente na montagem do circuito virtual no software Easy Eda. Em seguida, essa placa é disposta no centro de um pote plástico.

**2. Instalação dos fios** 

  No pote plástico são perfuradas duas passagens para os conectores de plug de banana, um conector é alimentado com 12V e o outro é o GND. Também são perfuradas entradas para passagem dos fio conector do eletroímã e do cabo USB do microcontrolador. 

**3. Conexão dos componentes do circuito**

  A ponte H se conecta à ligação dos conectores de plug de bananas. O Raspberry Pi Pico W é conectado ao computador via cabo USB. Por fim, a ponte H recebe dois fios que são conectados aos polos dos eletroímãs. Os eletroímas são conectados a base do braço robótico e o fio de ligação passa por cima. 
	
# Resultados integração do projeto

Durante a realização dos testes de integração do sistema do braço robótico com controle do eletroímã via interface gráfica, foram obtidos resultados satisfatórios que indicam um alto potencial de eficiência e precisão do processo realizado pelo IPT.

Através da interface gráfica, é possível controlar o braço robótico para realizar rotas planejadas com base nas informações fornecidas pela interface gráfica, permitindo ao usuário delimitar quais rotas deseja que o robô realize e pausar o sistema caso seja necessário.

Outra funcionalidade presente na interface é o controle de intensidade do eletroímã, que permite ao usuário delimitar a intensidade com que o processo de separação dos materiais magnéticos deve ser realizado, tornando-o mais preciso e eficiente.

Por fim, no teste realizado também observou-se que o robô executa com sucesso a passagem do dispositivo mecânico com os eletroímãs nas amostras e o dispositivo eletrônico cumpre sua função em se conectar com o computador e controlar o eletroímã, não apresentando falhas. 

O video abaixo mostra todos os passos a serem realizados pelo usuário na interface e a rota executada pelo braõ robótico.


# Referências

<!--
Modelo:
TÍTULO da matéria. Nome do site, ano. Disponível em: <URL>. Acesso em: dia, mês e ano.
ou
SOBRENOME, Nome. Título da matéria. Nome do site, ano. Disponível em: <URL>. Acesso em: dia, mês e ano.
-->

Separação Magnética. Oximag, 2022. Disponível em: https://www.oximag.com/separacao-magnetica.html. Acesso em: 6/02/2023.

Eletroimã / Solenóide 20mm 2,5Kg. Usinainfo. Disponível em: https://www.usinainfo.com.br/outros-modulos-arduino/eletroima-solenoide-20mm-25kg-2815.html. Acesso em: 7/02/2023.

Pydobot. Python library for Dobot Magician. Github, 2021. Disponível em: https://github.com/luismesas/pydobot. Acesso em: 13/02/2023.

SDK Updates. Raspberrypi forums, 2021. Disponível em: https://forums.raspberrypi.com/viewtopic.php?t=301936. Acesso em: 13/02/2023.

McAleer, Kevin. Build your own web server using a Raspberry Pi Pico W using Phew!. Youtube. Disponível em: https://www.youtube.com/watch?v=0sPPxIq4hg8. Acesso em: 15/02/2023.

rahulkhanna. Automatic Plant Watering System using Raspberry Pi Pico - Share Project - PCBWay. pcbway, 2021. Disponível em: https://www.pcbway.com/project/shareproject/Automatic_Plant_Watering_System_using_Raspberry_Pi_Pico.html. Acesso em: 17/02/2023.

Ponte H – O que é e como funciona!. Disponível em: https://www.manualdaeletronica.com.br/ponte-h-o-que-e-como-funciona/. Acesso em: 25/02/2023

Eletroímã. Dísponivel em: https://www.ufrgs.br/amlef/glossario/eletroima-2/. Acesso em 25/02/2023
