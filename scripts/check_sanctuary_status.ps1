# CHECK SANCTUARY STATUS
# Quick status check of all Sanctuary services

Write-Host "=== SANCTUARY STATUS CHECK ===" -ForegroundColor Cyan
Write-Host ""

$allGood = $true

# Check Backend API
Write-Host "[1/4] Checking Backend API..." -ForegroundColor Yellow
try {
    $response = Invoke-WebRequest -Uri "http://localhost:8000/api/public/world-history/status" -TimeoutSec 3 -ErrorAction Stop
    if ($response.StatusCode -eq 200) {
        Write-Host "  Backend API: RUNNING" -ForegroundColor Green
        $status = $response.Content | ConvertFrom-Json
        Write-Host "  Status: $($status.status)" -ForegroundColor Gray
    }
} catch {
    Write-Host "  Backend API: NOT RUNNING" -ForegroundColor Red
    Write-Host "  Run: .\scripts\start_sanctuary.ps1" -ForegroundColor Yellow
    $allGood = $false
}
Write-Host ""

# Check Sanctuary Protocol
Write-Host "[2/4] Checking Sanctuary Protocol..." -ForegroundColor Yellow
$protocolScript = "S:\JAN\scripts\sanctuary_protocol.py"
if (Test-Path $protocolScript) {
    Write-Host "  Sanctuary Protocol: AVAILABLE" -ForegroundColor Green
} else {
    Write-Host "  Sanctuary Protocol: NOT FOUND" -ForegroundColor Red
    $allGood = $false
}
Write-Host ""

# Check Sanctuary Guardian
Write-Host "[3/4] Checking Sanctuary Guardian..." -ForegroundColor Yellow
$guardianScript = "S:\JAN\jan-studio\backend\sanctuary_guardian.py"
if (Test-Path $guardianScript) {
    Write-Host "  Sanctuary Guardian: AVAILABLE" -ForegroundColor Green
} else {
    Write-Host "  Sanctuary Guardian: NOT FOUND" -ForegroundColor Red
    $allGood = $false
}
Write-Host ""

# Check Security Tools
Write-Host "[4/4] Checking Security..." -ForegroundColor Yellow
$securityGood = $false

# Check Firewall
$fwStatus = Get-NetFirewallProfile | Where-Object { $_.Enabled -eq $true }
if ($fwStatus) {
    Write-Host "  Windows Firewall: ACTIVE" -ForegroundColor Green
    $securityGood = $true
} else {
    Write-Host "  Windows Firewall: INACTIVE" -ForegroundColor Yellow
}

# Check VPN
if (Test-Path "C:\Program Files\Surfshark") {
    Write-Host "  Surfshark VPN: INSTALLED" -ForegroundColor Green
    $securityGood = $true
} else {
    Write-Host "  Surfshark VPN: NOT FOUND" -ForegroundColor Yellow
}

Write-Host ""

# Summary
Write-Host "=== SUMMARY ===" -ForegroundColor Cyan
Write-Host ""

if ($allGood) {
    Write-Host "Status: ALL SYSTEMS OPERATIONAL" -ForegroundColor Green
    Write-Host ""
    Write-Host "Access Points:" -ForegroundColor Yellow
    Write-Host "  - API: http://localhost:8000/api/public/world-history/status" -ForegroundColor White
    Write-Host "  - Sanctuary: http://localhost:8000/api/heritage/sanctuary/status" -ForegroundColor White
    Write-Host ""
    Write-Host "The Sanctuary is ready to serve the people" -ForegroundColor Green
} else {
    Write-Host "Status: SOME SYSTEMS NEED ATTENTION" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Next Steps:" -ForegroundColor Yellow
    Write-Host "  1. Run: .\scripts\start_sanctuary.ps1" -ForegroundColor White
    Write-Host "  2. Check logs for errors" -ForegroundColor White
    Write-Host "  3. Verify all dependencies are installed" -ForegroundColor White
}

Write-Host ""
Write-Host "SPRAGITSO - Our Father's Royal Seal" -ForegroundColor Cyan
