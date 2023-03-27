# Objetivo

Essa pasta tem o objetivo de armazenar e organizar todos os códigos fonte, criados pela equipe, exclusivamente referente ao desenvolvimento dos códigos do Raspberry Pi Pico W . Ao decorrer do projeto precisamos testas vários scripts diferentes, e cada arquivo python é uma feature que precisamos testar ao longo do desenvolvimento. Ao final da sprint 5, essa pasta será excluida pois seu propósito é para apenas a organização do time. Na pasta `raspberry/test` contém um arquivo python responsável por apenas testarmos a conexão serial antes de implementarmos essa lógica em nosso backend.

# Como rodar o projeto

## Sem venv

Caso deseja rodar o projeto sem criar nenhuma "venv" de python, apenas rode os seguintes comandos em seu terminal na "root" da pasta `/embedded`:

```shell
pip install -r requirements.txt
```

```shell
python3 "NOME_DO_ARQUIVO_QUE_DESEJE_RODAR.py"
```

## Criando uma venv

### Como criar uma venv

Rode esse código na "root" dessa pasta `/embedded`:
Em mac:

```bash
python3 -m venv .venv
```

Em windows:

```bash
py -m venv .venv
```

### Para ativar a venv

Rode esse código no terminal na root dessa pasta `/embedded`:
Em mac:

```bash
source .venv/bin/activate
```

Em windows:

```bash
.\.venv\Scripts\activate
```

Para sair da venv rode:

```bash
deactivate
```

### Instalando as bibliotecas na venv

Rode esse código no terminal na root dessa pasta `/embedded`:

```bash
pip install -r requirements.txt
```

### Exportando as bibliotecas instaladas na venv

Rode esse código no terminal na root dessa pasta `/embedded`:

```bash
pip freeze --> requirements.txt
```
