# Build Script for JAN Ecosystem Mobile App (PowerShell)
# Production build automation

Write-Host "🚀 JAN Ecosystem - Building for Production" -ForegroundColor Cyan
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
Write-Host ""

# Check if EAS CLI is installed
try {
    $null = Get-Command eas -ErrorAction Stop
} catch {
    Write-Host "❌ EAS CLI not found. Installing..." -ForegroundColor Yellow
    npm install -g eas-cli
}

# Check if logged in
Write-Host "🔐 Checking EAS authentication..." -ForegroundColor Yellow
$whoami = eas whoami 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "⚠️  Not logged in. Please run: eas login" -ForegroundColor Red
    exit 1
}

# Select platform
Write-Host ""
Write-Host "Select platform:"
Write-Host "1) iOS"
Write-Host "2) Android"
Write-Host "3) Both"
$choice = Read-Host "Enter choice (1-3)"

switch ($choice) {
    "1" {
        Write-Host ""
        Write-Host "📱 Building for iOS..." -ForegroundColor Green
        eas build --platform ios --profile production
    }
    "2" {
        Write-Host ""
        Write-Host "🤖 Building for Android..." -ForegroundColor Green
        eas build --platform android --profile production
    }
    "3" {
        Write-Host ""
        Write-Host "📱 Building for iOS..." -ForegroundColor Green
        eas build --platform ios --profile production
        Write-Host ""
        Write-Host "🤖 Building for Android..." -ForegroundColor Green
        eas build --platform android --profile production
    }
    default {
        Write-Host "❌ Invalid choice" -ForegroundColor Red
        exit 1
    }
}

Write-Host ""
Write-Host "✅ Build complete!" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:"
Write-Host "1. Download builds from EAS dashboard"
Write-Host "2. Test builds on devices"
Write-Host "3. Submit to app stores: eas submit"
