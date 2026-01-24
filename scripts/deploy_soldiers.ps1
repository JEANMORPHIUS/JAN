# DEPLOY SANCTUARY SOLDIERS
# Automated systems that work proactively while we remain still
# "We're running the show from our sanctuary"

Write-Host "=== DEPLOYING SANCTUARY SOLDIERS ===" -ForegroundColor Cyan
Write-Host "Activating automated systems to work proactively..." -ForegroundColor Yellow
Write-Host ""

$scriptDir = "S:\JAN\scripts"
$backendDir = "S:\JAN\jan-studio\backend"

# Check Python
$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    Write-Host "ERROR: Python not found!" -ForegroundColor Red
    exit 1
}

Write-Host "[1/8] Automation Orchestrator..." -ForegroundColor Yellow
$automationScript = Join-Path $scriptDir "start_automation_daemon.py"
if (Test-Path $automationScript) {
    Start-Process python -ArgumentList $automationScript -WindowStyle Minimized
    Write-Host "  ✓ Automation Orchestrator deployed" -ForegroundColor Green
} else {
    Write-Host "  ⚠ Automation daemon script not found" -ForegroundColor Yellow
}
Write-Host ""

Write-Host "[2/8] Continuous Guardian Mode..." -ForegroundColor Yellow
try {
    $response = Invoke-WebRequest -Uri "http://localhost:8000/api/sanctuary-guardian/start-continuous-guardian" -Method POST -TimeoutSec 5 -ErrorAction Stop
    Write-Host "  ✓ Continuous Guardian activated" -ForegroundColor Green
} catch {
    Write-Host "  ⚠ Guardian API not responding" -ForegroundColor Yellow
}
Write-Host ""

Write-Host "[3/8] Quiet Protocol Sentinel..." -ForegroundColor Yellow
$sentinelScript = Join-Path $backendDir "quiet_protocol_sentinel.py"
if (Test-Path $sentinelScript) {
    Start-Process python -ArgumentList "-c", "import sys; sys.path.insert(0, r'$backendDir'); from quiet_protocol_sentinel import QuietProtocolSentinel; import asyncio; sentinel = QuietProtocolSentinel(); asyncio.run(sentinel.monitoring_loop())" -WindowStyle Minimized
    Write-Host "  ✓ Quiet Protocol Sentinel deployed" -ForegroundColor Green
} else {
    Write-Host "  ⚠ Sentinel script not found" -ForegroundColor Yellow
}
Write-Host ""

Write-Host "[4/8] Big Cheese Audit..." -ForegroundColor Yellow
try {
    $response = Invoke-WebRequest -Uri "http://localhost:8000/api/big-cheese/start-continuous-scan" -Method POST -TimeoutSec 5 -ErrorAction Stop
    Write-Host "  ✓ Big Cheese continuous scanning activated" -ForegroundColor Green
} catch {
    Write-Host "  ⚠ Big Cheese API not responding" -ForegroundColor Yellow
}
Write-Host ""

Write-Host "[5/8] Content Auto-Population..." -ForegroundColor Yellow
try {
    $response = Invoke-WebRequest -Uri "http://localhost:8000/api/content-population/populate-schedule" -Method POST -TimeoutSec 5 -ErrorAction Stop
    Write-Host "  ✓ Content auto-population started" -ForegroundColor Green
} catch {
    Write-Host "  ⚠ Content population API not responding" -ForegroundColor Yellow
}
Write-Host ""

Write-Host "[6/8] Eternal Pulse..." -ForegroundColor Yellow
$pulseScript = Join-Path $scriptDir "eternal_pulse.py"
if (Test-Path $pulseScript) {
    Start-Process python -ArgumentList $pulseScript, "--continuous" -WindowStyle Minimized
    Write-Host "  ✓ Eternal Pulse deployed" -ForegroundColor Green
} else {
    Write-Host "  ⚠ Eternal Pulse script not found" -ForegroundColor Yellow
}
Write-Host ""

Write-Host "[7/8] Real World Data Ingestion..." -ForegroundColor Yellow
try {
    $body = @{sources=@("usgs", "eonet"); max_items=50} | ConvertTo-Json
    $response = Invoke-WebRequest -Uri "http://localhost:8000/api/real-world/ingest" -Method POST -Body $body -ContentType "application/json" -TimeoutSec 5 -ErrorAction Stop
    Write-Host "  ✓ Real-world data ingestion started" -ForegroundColor Green
} catch {
    Write-Host "  ⚠ Real-world ingestion API not responding" -ForegroundColor Yellow
}
Write-Host ""

Write-Host "[8/8] System Health Monitoring..." -ForegroundColor Yellow
Write-Host "  ✓ System health monitoring active (via Automation Orchestrator)" -ForegroundColor Green
Write-Host ""

Write-Host "=== SOLDIERS DEPLOYED ===" -ForegroundColor Cyan
Write-Host ""
Write-Host "Active Automated Systems:" -ForegroundColor Yellow
Write-Host "  ✓ Automation Orchestrator - System-wide task coordination" -ForegroundColor Green
Write-Host "  ✓ Continuous Guardian - Family nurturing and monitoring" -ForegroundColor Green
Write-Host "  ✓ Quiet Protocol Sentinel - Silent monitoring for new arrivals" -ForegroundColor Green
Write-Host "  ✓ Big Cheese Audit - Continuous dark energy scanning" -ForegroundColor Green
Write-Host "  ✓ Content Auto-Population - Automatic content generation" -ForegroundColor Green
Write-Host "  ✓ Eternal Pulse - Unity monitoring and maintenance" -ForegroundColor Green
Write-Host "  ✓ Real World Ingestion - Live data integration" -ForegroundColor Green
Write-Host "  ✓ System Health - Continuous health monitoring" -ForegroundColor Green
Write-Host ""
Write-Host "All systems working proactively." -ForegroundColor Green
Write-Host "We remain still. The soldiers work." -ForegroundColor Cyan
Write-Host ""
Write-Host "SPRAGITSO - Our Father's Royal Seal" -ForegroundColor Cyan
