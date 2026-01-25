#!/bin/bash
# Build Script for JAN Ecosystem Mobile App
# Production build automation

set -e

echo "🚀 JAN Ecosystem - Building for Production"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Check if EAS CLI is installed
if ! command -v eas &> /dev/null; then
    echo "❌ EAS CLI not found. Installing..."
    npm install -g eas-cli
fi

# Check if logged in
echo "🔐 Checking EAS authentication..."
if ! eas whoami &> /dev/null; then
    echo "⚠️  Not logged in. Please run: eas login"
    exit 1
fi

# Select platform
echo ""
echo "Select platform:"
echo "1) iOS"
echo "2) Android"
echo "3) Both"
read -p "Enter choice (1-3): " choice

case $choice in
    1)
        echo ""
        echo "📱 Building for iOS..."
        eas build --platform ios --profile production
        ;;
    2)
        echo ""
        echo "🤖 Building for Android..."
        eas build --platform android --profile production
        ;;
    3)
        echo ""
        echo "📱 Building for iOS..."
        eas build --platform ios --profile production
        echo ""
        echo "🤖 Building for Android..."
        eas build --platform android --profile production
        ;;
    *)
        echo "❌ Invalid choice"
        exit 1
        ;;
esac

echo ""
echo "✅ Build complete!"
echo ""
echo "Next steps:"
echo "1. Download builds from EAS dashboard"
echo "2. Test builds on devices"
echo "3. Submit to app stores: eas submit"
