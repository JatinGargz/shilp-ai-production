#!/usr/bin/env bash
set -e
echo "============================================================"
echo "  SHILP AI - Automated Unix/Mac Setup Environment"
echo "============================================================"

cd "$(dirname "$0")/.."

if ! command -v python3 &> /dev/null; then
    echo "[ERROR] python3 not found. Please install Python 3.10+."
    exit 1
fi

if [ ! -d "backend/venv" ]; then
    python3 -m venv backend/venv
    echo "[OK] Virtual environment created at backend/venv"
fi

source backend/venv/bin/activate
pip install --upgrade pip
pip install -r backend/requirements.txt

if [ ! -f "backend/.env" ]; then
    cp backend/.env.example backend/.env
    echo "[OK] Created backend/.env"
fi

echo "============================================================"
echo "  [SUCCESS] Setup Completed!"
echo "  To start: source backend/venv/bin/activate && cd backend && uvicorn app.main:app --reload"
echo "============================================================"
