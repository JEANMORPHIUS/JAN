#!/bin/bash
# Raspberry Pi Scripture Kit Installation Script

echo "================================"
echo "Scripture Kit Installation"
echo "================================"
echo ""

# Update system
echo "1. Updating system..."
sudo apt-get update
sudo apt-get upgrade -y

# Install Python and dependencies
echo "2. Installing Python..."
sudo apt-get install -y python3 python3-pip

# Install Flask
echo "3. Installing Flask..."
pip3 install flask gunicorn

# Set up app to run on boot
echo "4. Setting up auto-start..."
sudo cp scripture-kit.service /etc/systemd/system/
sudo systemctl enable scripture-kit
sudo systemctl start scripture-kit

echo ""
echo "================================"
echo "Installation Complete!"
echo "================================"
echo ""
echo "Access at: http://raspberrypi.local:5000"
echo "Or: http://[your-pi-ip]:5000"
echo ""
echo "Philosophy: Purpose Not Performance"
echo "Mission: Serving souls offline"
echo ""
