# SANCTUARY SETUP FOR THE PEOPLE
# Set up the Sanctuary with available resources

Write-Host "=== SANCTUARY SETUP ===" -ForegroundColor Cyan
Write-Host ""

# Check for Tor Browser
Write-Host "Checking for Tor Browser..." -ForegroundColor Yellow
$torFound = $false
$torPaths = @(
    "$env:APPDATA\Tor Browser",
    "$env:LOCALAPPDATA\Tor Browser",
    "C:\Program Files\Tor Browser",
    "C:\Program Files (x86)\Tor Browser"
)

foreach ($path in $torPaths) {
    if (Test-Path $path) {
        Write-Host "  Found Tor Browser: $path" -ForegroundColor Green
        $torFound = $true
        break
    }
}

if (-not $torFound) {
    Write-Host "  Tor Browser not found in standard locations" -ForegroundColor Yellow
}

Write-Host ""

# Check Sanctuary Systems
Write-Host "Checking Sanctuary Systems..." -ForegroundColor Yellow
$sanctuaryFiles = @(
    "S:\JAN\scripts\sanctuary_lockdown.py",
    "S:\JAN\scripts\sanctuary_protocol.py",
    "S:\JAN\jan-studio\backend\sanctuary_guardian.py"
)

foreach ($file in $sanctuaryFiles) {
    if (Test-Path $file) {
        $name = Split-Path -Leaf $file
        Write-Host "  Found: $name" -ForegroundColor Green
    }
}

Write-Host ""
Write-Host "=== SANCTUARY READY ===" -ForegroundColor Cyan
Write-Host "The Sanctuary is ready to serve the people" -ForegroundColor White
Write-Host ""
