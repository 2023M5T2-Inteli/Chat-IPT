@echo off

REM Verifica se Chocolatey está instalado
where choco >nul 2>&1
if %errorlevel% neq 0 (
    echo Chocolatey não está instalado. Instalando...
    powershell.exe -ExecutionPolicy Bypass -NoLogo -NonInteractive -NoProfile -Command ^
        "[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12; " ^
        "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" ^
        " && refreshenv"
) else (
    echo Chocolatey já está instalado.
)

REM Verifica se python 3.10 ou superior está instalado
where python3.10 >nul 2>&1
if %errorlevel% neq 0 (
    echo Python 3.10 ou superior não está instalado. Instalando...
    REM Instala python 3.10 ou superior usando o Python Launcher for Windows
    choco install python --params "/InstallLauncher:0 /InstallDir:C:\Python310" -y
) else (
    echo Python 3.10 ou superior já está instalado.
)

REM Verifica se git está instalado
where git >nul 2>&1
if %errorlevel% neq 0 (
    echo Git não está instalado. Instalando...
    REM Instala git usando o Git for Windows
    choco install git -params "/GitAndUnixToolsOnPath /NoAutoCrlf" -y
) else (
    echo Git já está instalado.
)

REM Clona o projeto e entra no diretório backend
git clone https://github.com/2023M5T2-Inteli/Chat-IPT Chat-IPT
cd Chat-IPT\src\backend

REM Cria e ativa a venv
python -m venv .venv
call .venv\Scripts\activate.bat

REM Roda o app
python app.py