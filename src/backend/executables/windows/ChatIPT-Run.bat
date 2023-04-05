@echo off

REM Verifica se a pasta Chat-IPT existe
if not exist ".\Chat-IPT" (
    echo Pasta 'Chat-IPT' não encontrada, favor seguir os passos de instalação!
    exit /b 1
)

REM Ativa a venv do projeto
call .\Chat-IPT\src\backend\.venv\Scripts\activate.bat

REM Executa o arquivo app.py
python .\Chat-IPT\src\backend\app.py