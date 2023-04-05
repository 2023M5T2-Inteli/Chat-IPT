#!/bin/bash

# Verifica se o Homebrew está instalado
if ! command -v brew &> /dev/null
then
    echo "Homebrew não está instalado. Instalando..."
    # Instala o Homebrew
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else
    echo "Homebrew já está instalado."
fi

# Verifica se o Python 3.10 ou superior está instalado
if ! command -v python3.10 &> /dev/null
then
    echo "Python 3.10 ou superior não está instalado. Instalando..."
    # Instala o Python 3.10 ou superior
    brew install python@3.10
else
    echo "Python 3.10 ou superior já está instalado."
fi

# Verifica se o Git está instalado
if ! command -v git &> /dev/null
then
    echo "Git não está instalado. Instalando..."
    # Instala o Git
    brew install git
else
    echo "Git já está instalado."
fi

# Clona o projeto e entra no diretório backend
git clone https://github.com/2023M5T2-Inteli/Chat-IPT Chat-IPT
cd Chat-IPT/src/backend

# Cria e ativa a venv
python3.10 -m venv .venv
source .venv/bin/activate

# Roda o app
python app.py