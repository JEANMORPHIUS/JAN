#!/bin/bash
# JAN Studio Pi Installation Script
# For Raspberry Pi 5 with AI Kit

set -e

echo "🚀 Installing JAN Studio Pi..."

# Check if running on Pi
if [ ! -f /proc/device-tree/model ] || ! grep -q "Raspberry Pi" /proc/device-tree/model; then
    echo "⚠️  Warning: This script is designed for Raspberry Pi"
    read -p "Continue anyway? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Install system dependencies
echo "📦 Installing system dependencies..."
sudo apt-get update
sudo apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    git \
    build-essential \
    libopenblas-dev \
    libsndfile1

# Create virtual environment
echo "🐍 Creating Python virtual environment..."
python3 -m venv ~/jan-venv
source ~/jan-venv/bin/activate

# Install Python dependencies
echo "📚 Installing Python packages..."
pip install --upgrade pip
pip install -r requirements-pi.txt

# Create directories
echo "📁 Creating directories..."
mkdir -p ~/.jan-models
mkdir -p ~/JAN/Siyem.org

# Download models (optional - can be done later)
echo "🤖 Models will be downloaded on first use"
echo "   This may take some time..."

# Install systemd service
echo "⚙️  Installing systemd service..."
sudo cp jan-studio-pi.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable jan-studio-pi.service

echo "✅ Installation complete!"
echo ""
echo "To start JAN Studio Pi:"
echo "  sudo systemctl start jan-studio-pi"
echo ""
echo "To view logs:"
echo "  sudo journalctl -u jan-studio-pi -f"
echo ""
echo "Access the UI at: http://localhost:8000"

