@echo off
title SHILP AI - Automated System Verification
cd /d "%~dp0\..\backend"
echo ============================================================
echo   Running SHILP AI Full Test Suite & Developer Sandboxes
echo ============================================================
echo.

if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
)

echo [*] Testing Anikeat's Database Sandbox...
python sandboxes\test_anikeat_db.py
if %errorlevel% neq 0 ( echo [FAIL] Anikeat's Sandbox Failed! & pause & exit /b 1 )

echo.
echo [*] Testing Kartik's AI & Speech Sandbox...
python sandboxes\test_kartik_ai.py
if %errorlevel% neq 0 ( echo [FAIL] Kartik's Sandbox Failed! & pause & exit /b 1 )

echo.
echo [*] Testing Ishaan's Pricing Sandbox...
python sandboxes\test_ishaan_pricing.py
if %errorlevel% neq 0 ( echo [FAIL] Ishaan's Sandbox Failed! & pause & exit /b 1 )

echo.
echo [*] Testing Jatin's 5-Channel & Document Sandbox...
python sandboxes\test_jatin_channels.py
if %errorlevel% neq 0 ( echo [FAIL] Jatin's Sandbox Failed! & pause & exit /b 1 )

echo.
echo [*] Running Master 11-Point End-to-End Verification...
python tests\test_e2e_suite.py
if %errorlevel% neq 0 ( echo [FAIL] Master E2E Suite Failed! & pause & exit /b 1 )

echo.
echo ============================================================
echo   [SUCCESS] ALL INDIVIDUAL & MASTER E2E TESTS PASSED 100%!
echo ============================================================
pause
