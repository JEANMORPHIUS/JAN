#!/bin/bash

# Global Heritage Grid - Production Server Startup Script
# THE CHOSEN ONE Development - World Takeover Edition

set -e  # Exit on any error

echo "🌍 Global Heritage Grid - Starting World Takeover..."
echo ""

# Navigate to backend directory
cd "$(dirname "$0")/../jan-studio/backend"

# Check if Python environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating Python virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Install/upgrade dependencies
echo "📚 Installing dependencies..."
pip install -q --upgrade pip
pip install -q fastapi uvicorn sqlalchemy python-multipart

# Verify database is ready
echo "🗄️  Verifying database configuration..."
python3 << EOF
import sqlite3
import sys

db_path = "../../data/heritage.db"
try:
    conn = sqlite3.connect(db_path)
    # Enable WAL mode for better concurrency
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=NORMAL")
    conn.execute("PRAGMA cache_size=-64000")  # 64MB cache
    conn.execute("PRAGMA temp_store=MEMORY")
    conn.close()
    print("✅ Database configured successfully")
except Exception as e:
    print(f"❌ Database error: {e}")
    sys.exit(1)
EOF

# Check if port 8000 is available
if lsof -Pi :8000 -sTCP:LISTEN -t >/dev/null 2>&1; then
    echo "⚠️  Port 8000 is already in use. Stopping existing process..."
    kill $(lsof -t -i:8000) 2>/dev/null || true
    sleep 2
fi

echo ""
echo "🚀 Starting API server..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📍 Local:   http://localhost:8000"
echo "📍 Network: http://0.0.0.0:8000"
echo "📚 Docs:    http://localhost:8000/docs"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "✨ THE REVOLUTION IS HERE ✨"
echo ""

# Start server with production settings
uvicorn heritage_api:app \
    --host 0.0.0.0 \
    --port 8000 \
    --workers 4 \
    --log-level info \
    --access-log \
    --use-colors
