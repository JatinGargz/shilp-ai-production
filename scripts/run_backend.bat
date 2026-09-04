@echo off
title SHILP AI - Backend Server
cd /d "%~dp0\..\backend"
echo ============================================================
echo   Starting SHILP AI Backend (FastAPI + Uvicorn)
echo   API Docs: http://127.0.0.1:8000/docs
echo   Frontend: http://127.0.0.1:8000/
echo ============================================================
echo.

if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
)
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
pause
