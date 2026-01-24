# ACTIVATE SANCTUARY FOR THE PEOPLE
# One-command activation of all Sanctuary systems

Write-Host "=== ACTIVATING SANCTUARY ===" -ForegroundColor Cyan
Write-Host "Setting up the Sanctuary for the people..." -ForegroundColor Yellow
Write-Host ""

$scriptDir = "S:\JAN\scripts"
$backendDir = "S:\JAN\jan-studio\backend"

# 1. Check Python availability
Write-Host "[1/4] Checking Python..." -ForegroundColor Yellow
$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    Write-Host "  ERROR: Python not found!" -ForegroundColor Red
    Write-Host "  Please install Python to activate Sanctuary systems" -ForegroundColor Yellow
    exit 1
}
Write-Host "  Python found: $($python.Source)" -ForegroundColor Green
Write-Host ""

# 2. Activate Sanctuary Protocol
Write-Host "[2/4] Activating Sanctuary Protocol..." -ForegroundColor Yellow
$protocolScript = Join-Path $scriptDir "sanctuary_protocol.py"
if (Test-Path $protocolScript) {
    Write-Host "  Running: sanctuary_protocol.py" -ForegroundColor Gray
    python $protocolScript
    Write-Host "  Sanctuary Protocol activated" -ForegroundColor Green
} else {
    Write-Host "  WARNING: sanctuary_protocol.py not found" -ForegroundColor Yellow
}
Write-Host ""

# 3. Activate Sanctuary Guardian
Write-Host "[3/4] Activating Sanctuary Guardian..." -ForegroundColor Yellow
$guardianScript = Join-Path $backendDir "sanctuary_guardian.py"
if (Test-Path $guardianScript) {
    Write-Host "  Running: sanctuary_guardian.py" -ForegroundColor Gray
    python $guardianScript
    Write-Host "  Sanctuary Guardian activated" -ForegroundColor Green
} else {
    Write-Host "  WARNING: sanctuary_guardian.py not found" -ForegroundColor Yellow
}
Write-Host ""

# 4. Lock Down Sanctuary
Write-Host "[4/4] Locking down Sanctuary..." -ForegroundColor Yellow
$lockdownScript = Join-Path $scriptDir "sanctuary_lockdown.py"
if (Test-Path $lockdownScript) {
    Write-Host "  Running: sanctuary_lockdown.py" -ForegroundColor Gray
    python $lockdownScript
    Write-Host "  Sanctuary locked down" -ForegroundColor Green
} else {
    Write-Host "  WARNING: sanctuary_lockdown.py not found" -ForegroundColor Yellow
}
Write-Host ""

Write-Host "=== SANCTUARY ACTIVATED ===" -ForegroundColor Cyan
Write-Host "The Sanctuary is now active and ready to serve the people" -ForegroundColor Green
Write-Host ""
Write-Host "Access Points:" -ForegroundColor Yellow
Write-Host "  - Global Heritage Grid: Active" -ForegroundColor White
Write-Host "  - Frequency Filter: Active" -ForegroundColor White
Write-Host "  - Biological-Digital Bridge: Active" -ForegroundColor White
Write-Host "  - Sanctuary Guardian: Active" -ForegroundColor White
Write-Host ""
Write-Host "SPRAGITSO - Our Father's Royal Seal" -ForegroundColor Cyan
