@echo off
REM Global Heritage Grid - Production Server Startup Script (Windows)
REM THE CHOSEN ONE Development - World Takeover Edition

echo 🌍 Global Heritage Grid - Starting World Takeover...
echo.

REM Navigate to backend directory
cd /d "%~dp0\..\jan-studio\backend"

REM Check if Python environment exists
if not exist "venv" (
    echo 📦 Creating Python virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo 🔌 Activating virtual environment...
call venv\Scripts\activate.bat

REM Install/upgrade dependencies
echo 📚 Installing dependencies...
pip install -q --upgrade pip
pip install -q fastapi uvicorn sqlalchemy python-multipart

REM Verify database configuration
echo 🗄️  Verifying database configuration...
python -c "import sqlite3; conn = sqlite3.connect('../../data/heritage.db'); conn.execute('PRAGMA journal_mode=WAL'); conn.execute('PRAGMA synchronous=NORMAL'); conn.execute('PRAGMA cache_size=-64000'); conn.execute('PRAGMA temp_store=MEMORY'); conn.close(); print('✅ Database configured successfully')"

if %errorlevel% neq 0 (
    echo ❌ Database configuration failed
    pause
    exit /b 1
)

echo.
echo 🚀 Starting API server...
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo 📍 Local:   http://localhost:8000
echo 📍 Network: http://0.0.0.0:8000
echo 📚 Docs:    http://localhost:8000/docs
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo.
echo ✨ THE REVOLUTION IS HERE ✨
echo.

REM Start server with production settings
uvicorn heritage_api:app --host 0.0.0.0 --port 8000 --workers 4 --log-level info --access-log --use-colors

pause
