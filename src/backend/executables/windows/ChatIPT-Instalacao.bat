@echo off

REM Verifica a versão do Python
for /f "delims=" %%v in ('python --version 2^>^&1') do set "python_version=%%v"
echo %python_version% | findstr /r /c:"^Python 3\.[1-9][0-9]*" > nul
if errorlevel 1 (
    echo A versão mínima do Python necessária é 3.10.
    exit /b 1
)

REM Verifica se o git está instalado
where git > nul 2>&1
if %errorlevel% neq 0 (
    echo O Git não está instalado.
    exit /b 1
)

REM Clona o projeto para uma pasta "Chat-IPT"
git clone https://github.com/2023M5T2-Inteli/Chat-IPT Chat-IPT

REM Navega para a pasta "Chat-IPT/src/backend"
cd Chat-IPT\src\backend

REM Cria a venv de Python com o nome ".venv"
py -m venv .venv

REM Ativa a venv
call .\.venv\Scripts\activate

REM Instala as dependências do projeto a partir do arquivo "requirements.txt"
pip install -r requirements.txt

REM Desativa a venv
deactivate