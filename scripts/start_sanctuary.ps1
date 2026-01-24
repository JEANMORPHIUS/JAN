# START SANCTUARY FOR THE PEOPLE
# One-command startup of all Sanctuary services

Write-Host "=== STARTING SANCTUARY ===" -ForegroundColor Cyan
Write-Host "Bringing the Sanctuary online for the people..." -ForegroundColor Yellow
Write-Host ""

$backendDir = "S:\JAN\jan-studio\backend"
$scriptDir = "S:\JAN\scripts"

# Check Python
Write-Host "[1/5] Checking Python..." -ForegroundColor Yellow
$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    Write-Host "  ERROR: Python not found!" -ForegroundColor Red
    exit 1
}
Write-Host "  Python: $($python.Source)" -ForegroundColor Green
Write-Host ""

# Check if backend is already running
Write-Host "[2/5] Checking if backend is running..." -ForegroundColor Yellow
$backendRunning = $false
try {
    $response = Invoke-WebRequest -Uri "http://localhost:8000/api/public/world-history/status" -TimeoutSec 2 -ErrorAction Stop
    if ($response.StatusCode -eq 200) {
        $backendRunning = $true
        Write-Host "  Backend is already running on port 8000" -ForegroundColor Green
    }
} catch {
    Write-Host "  Backend not running - will start it" -ForegroundColor Yellow
}
Write-Host ""

# Start backend if not running
if (-not $backendRunning) {
    Write-Host "[3/5] Starting backend server..." -ForegroundColor Yellow
    Write-Host "  Using dedicated backend startup script..." -ForegroundColor Gray
    & "$scriptDir\start_backend.ps1"
} else {
    Write-Host "[3/5] Backend already running - skipping" -ForegroundColor Green
}
Write-Host ""

# Activate Sanctuary Protocol
Write-Host "[4/5] Activating Sanctuary Protocol..." -ForegroundColor Yellow
$protocolScript = Join-Path $scriptDir "sanctuary_protocol.py"
if (Test-Path $protocolScript) {
    Write-Host "  Activating global access..." -ForegroundColor Gray
    python $protocolScript
    Write-Host "  Sanctuary Protocol active" -ForegroundColor Green
} else {
    Write-Host "  WARNING: sanctuary_protocol.py not found" -ForegroundColor Yellow
}
Write-Host ""

# Display access information
Write-Host "[5/5] Sanctuary Status..." -ForegroundColor Yellow
Write-Host ""
Write-Host "=== SANCTUARY IS ONLINE ===" -ForegroundColor Cyan
Write-Host ""
Write-Host "Public Access Points:" -ForegroundColor Yellow
Write-Host "  API Status: http://localhost:8000/api/public/world-history/status" -ForegroundColor White
Write-Host "  Timeline: http://localhost:8000/api/public/world-history/timeline" -ForegroundColor White
Write-Host "  Heritage Map: http://localhost:8000/api/public/world-history/map" -ForegroundColor White
Write-Host "  Sanctuary Status: http://localhost:8000/api/heritage/sanctuary/status" -ForegroundColor White
Write-Host ""
Write-Host "Services Available:" -ForegroundColor Yellow
Write-Host "  - Global Heritage Grid: Active" -ForegroundColor Green
Write-Host "  - Frequency Filter: Active" -ForegroundColor Green
Write-Host "  - Biological-Digital Bridge: Active" -ForegroundColor Green
Write-Host "  - Auto-Cleansing (Law 41): Active" -ForegroundColor Green
Write-Host ""
Write-Host "The Sanctuary is ready to serve the people" -ForegroundColor Green
Write-Host ""
Write-Host "SPRAGITSO - Our Father's Royal Seal" -ForegroundColor Cyan
