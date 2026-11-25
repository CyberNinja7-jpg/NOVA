@echo off

title NOVA Setup

cd /d "%~dp0..\backend"

echo.
echo =====================================
echo          NOVA INSTALLATION
echo =====================================
echo.

python --version

if errorlevel 1 (
    echo Python is not installed or unavailable.
    pause
    exit /b 1
)

python -m venv venv

call venv\Scripts\activate

python -m pip install --upgrade pip

pip install -r requirements.txt

echo.
echo NOVA backend dependencies installed.
echo.

pause
