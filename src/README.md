<table>
<tr>
<td>
<a href= "https://www.ipt.br/"><img src="https://www.ipt.br/imagens/logo_ipt.gif" alt="IPT" border="0" width="70%"></a>
</td>
<td><a href= "https://www.inteli.edu.br/"><img src="https://www.inteli.edu.br/wp-content/uploads/2021/08/20172028/marca_1-2.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0" width="30%"></a>
</td>
</tr>
</table>

# Organização do diretório de arquivos fonte

Este diretório é destinado para o armazenamento e versionamento dos arquivos fonte relacionados à aplicação desenvolvida pelos alunos. Aqui, subdivide-se o diretório em [frontend](./frontend), [backend](./backend) e [embedded](./embedded).

# Guia de Instalação

Para rodar o projeto, é necessário ter um notebook com acesso à internet, o [Python 3.10](https://www.python.org/downloads/) (ou superior) instalado, o [Git](https://git-scm.com/downloads) instalado, um [Raspberry Pi Pico W](https://www.raspberrypi.com/products/raspberry-pi-pico/) conectado via USB/USB-C ao computador e um [Dobot Magician Lite](https://www.dobot-robots.com/products/education/magician-lite.html) conectado via USB/USB-C ao computador.

## Mac e Linux

### Baixando os arquivos do Google Drive

Primeiro é necessário baixar os arquivos necessários para executar o projeto. Para isso, é preciso acessar esse [drive](https://drive.google.com/drive/folders/1oS3QKMD9rQIigUscy2HzCbeCbKk6_16J?usp=sharing) do Google Drive e baixar os arquivos .sh.

## Executando o arquivo de instalação

Após baixar os arquivos .sh, execute os seguintes comandos para tornar os arquivos executáveis:

```shell
chmod +x ChatIPT-Instalacao.sh
```

```shell
chmod +x ChatIPT-Run.sh
```

Após os comandos serem bem-sucedidos, rode o [arquivo de instalação](./backend/executables/mac-linux/ChatIPT-Instalacao.sh):

```shell
./ChatIPT-Instalacao.sh
```

Esse arquivo só precisa ser executado uma vez. Após a instalação, execute o [arquivo .sh para rodar o servidor](./backend/executables/mac-linux/ChatIPT-Run.sh). A pasta "Chat-IPT" será criada e essa pasta será a aplicação, portanto, não poderá ser apagada:

```shell
./ChatIPT-Run.sh
```

Pronto! A aplicação estará rodando com sucesso, e basta seguir o passo a passo informado na tela!

## Windows

### Baixando os arquivos do Google Drive

Primeiro é necessário baixar os arquivos necessários para executar o projeto. Para isso, é preciso acessar esse [drive](https://drive.google.com/drive/folders/1rTx39fP7dyOFzlQyAo6skIqGli20Q7qH?usp=sharing) do Google Drive e baixar os arquivos .bat.

## Executando o arquivo de instalação

Após baixar os arquivos .bat, execute primeiro o arquivo de instalação, o [`ChatIPT-Instalacao.bat`](./backend/executables/windows/ChatIPT-Instalacao.bat). Esse arquivo só precisa ser executado uma vez. Após a instalação, execute o arquivo [`ChatIPT-Run.bat`](./backend/executables/windows/ChatIPT-Run.bat) para rodar o servidor. A pasta "Chat-IPT" será criada e essa pasta será a aplicação, portanto, não poderá ser apagada.  
Pronto! A aplicação estará rodando com sucesso, e basta seguir o passo a passo informado na tela!
