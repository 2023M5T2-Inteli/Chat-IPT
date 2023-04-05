#!/bin/bash

# Verifica se a pasta Chat-IPT existe
if [ ! -d "./Chat-IPT" ]; then
    echo "Pasta 'Chat-IPT' não encontrada, favor seguir os passos de instalação!"
    exit 1
fi

# Ativa a venv do projeto
source ./Chat-IPT/src/backend/.venv/bin/activate

# Executa o arquivo app.py
python3 ./Chat-IPT/src/backend/app.py