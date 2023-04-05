#!/bin/bash

# Verifica a versão do Python
python_version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
if [ $(echo "$python_version >= 3.10" | bc -l) -ne 1 ]; then
    echo "A versão mínima do Python necessária é 3.10."
    exit 1
fi

# Verifica se o git está instalado
if ! command -v git &> /dev/null; then
    echo "O Git não está instalado."
    exit 1
fi

# Clona o projeto para uma pasta "Chat-IPT"
git clone https://github.com/2023M5T2-Inteli/Chat-IPT Chat-IPT

# Navega para a pasta "Chat-IPT/src/backend"
cd Chat-IPT/src/backend

# Cria a venv de Python com o nome ".venv"
python3 -m venv .venv

# Ativa a venv
source .venv/bin/activate

# Instala as dependências do projeto a partir do arquivo "requirements.txt"
pip install -r requirements.txt

# Desativa a venv
deactivate