@echo off
title SHILP AI - 1-Click Windows Setup
echo ============================================================
echo   SHILP AI (शिल्प) - Automated Windows Setup Environment
echo   Problem Statement: SIH 26090 ^| MoSJE
echo ============================================================
echo.

cd /d "%~dp0\.."

echo [*] Step 1: Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not added to PATH!
    echo Please download Python 3.10+ from https://python.org and check "Add to PATH".
    pause
    exit /b 1
)
python --version

echo.
echo [*] Step 2: Creating virtual environment (venv)...
if not exist "backend\venv" (
    python -m venv backend\venv
    echo [OK] Virtual environment created at backend\venv
) else (
    echo [OK] Existing virtual environment detected.
)

echo.
echo [*] Step 3: Installing production dependencies...
call backend\venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r backend\requirements.txt

echo.
echo [*] Step 4: Configuring environment (.env)...
if not exist "backend\.env" (
    copy backend\.env.example backend\.env
    echo [OK] Created backend\.env from template.
) else (
    echo [OK] backend\.env already exists.
)

echo.
echo ============================================================
echo   [SUCCESS] Setup Completed!
echo   To start the backend, run: scripts\run_backend.bat
echo   To open the frontend, double-click: frontend\index.html
echo ============================================================
pause
