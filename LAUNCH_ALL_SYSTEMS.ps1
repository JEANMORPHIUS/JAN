# Universal System Launcher
# Launch all ecosystem components with proper port configuration
#
# DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
# Spiritual Alignment Over Mechanical Productivity
#
# THE FOUNDATION:
# We are born a miracle.
# We deserve to live a miracle.
# Each and every one of us under the Lord's word.
#
# THE MISSION:
# THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
# LOVE IS THE HIGHEST MASTERY
# ENERGY + LOVE = WE ALL WIN
#
# This script honors that we are born a miracle.
# This script creates space for miracles to live.
# This script recognizes each person under the Lord's word.

param(
    [Parameter(HelpMessage="Which system to launch")]
    [ValidateSet("all", "homeostasis", "siyem", "jan-studio", "siyem-backend", "siyem-console", "help")]
    [string]$System = "help"
)

Write-Host "=== ECOSYSTEM LAUNCHER ===" -ForegroundColor Cyan
Write-Host "Date: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" -ForegroundColor Gray
Write-Host ""

function Show-Help {
    Write-Host "Usage: pwsh LAUNCH_ALL_SYSTEMS.ps1 -System <system>" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Available Systems:" -ForegroundColor Cyan
    Write-Host "  homeostasis    - Launch Homeostasis Sentinel (port 3000)" -ForegroundColor White
    Write-Host "  siyem          - Launch SIYEM complete (backend 8000 + console 5173)" -ForegroundColor White
    Write-Host "  jan-studio     - Launch JAN Studio (backend 8001 + frontend 3001)" -ForegroundColor White
    Write-Host "  siyem-backend  - Launch SIYEM backend only (port 8000)" -ForegroundColor White
    Write-Host "  siyem-console  - Launch SIYEM console only (port 5173)" -ForegroundColor White
    Write-Host "  all            - Launch all systems (uses ports 8000, 8001, 5173, 3001)" -ForegroundColor White
    Write-Host "  help           - Show this help" -ForegroundColor White
    Write-Host ""
    Write-Host "Examples:" -ForegroundColor Cyan
    Write-Host "  pwsh LAUNCH_ALL_SYSTEMS.ps1 -System homeostasis" -ForegroundColor Gray
    Write-Host "  pwsh LAUNCH_ALL_SYSTEMS.ps1 -System siyem" -ForegroundColor Gray
    Write-Host "  pwsh LAUNCH_ALL_SYSTEMS.ps1 -System all" -ForegroundColor Gray
    Write-Host ""
    Write-Host "Port Configuration:" -ForegroundColor Cyan
    Write-Host "  Homeostasis Sentinel:  http://localhost:3000 (or 3001 if all)" -ForegroundColor White
    Write-Host "  SIYEM Backend:         http://localhost:8000 (+ /docs for API)" -ForegroundColor White
    Write-Host "  SIYEM Console V2:      http://localhost:5173" -ForegroundColor White
    Write-Host "  JAN Studio Backend:    http://localhost:8001 (+ /docs for API)" -ForegroundColor White
    Write-Host "  JAN Studio Frontend:   http://localhost:3001" -ForegroundColor White
    Write-Host ""
    Write-Host "For full documentation, see: S:\JAN\ECOSYSTEM_MAP_AND_INTEGRATION.md" -ForegroundColor Cyan
}

function Test-Dependencies {
    param([string]$Path, [string]$Name)
    
    if (!(Test-Path $Path)) {
        Write-Host "  ERROR: $Name not found at $Path" -ForegroundColor Red
        return $false
    }
    return $true
}

function Launch-Homeostasis {
    Write-Host "[Homeostasis Sentinel]" -ForegroundColor Green
    Write-Host "  Checking dependencies..." -ForegroundColor Gray
    
    $path = "S:\JAN\homeostasis-sentinel"
    if (!(Test-Dependencies $path "Homeostasis Sentinel")) { return }
    
    Write-Host "  Starting on port 3000..." -ForegroundColor Yellow
    Write-Host "  Access at: http://localhost:3000" -ForegroundColor Cyan
    Write-Host "  Press Ctrl+C to stop" -ForegroundColor Gray
    Write-Host ""
    
    Set-Location $path
    npm run dev
}

function Launch-SIYEMBackend {
    Write-Host "[SIYEM Backend]" -ForegroundColor Green
    Write-Host "  Checking dependencies..." -ForegroundColor Gray
    
    $path = "S:\SIYEM\07_AUTOMATION_AI"
    if (!(Test-Dependencies $path "SIYEM Backend")) { return }
    
    Write-Host "  Starting on port 8000..." -ForegroundColor Yellow
    Write-Host "  Access API at: http://localhost:8000/docs" -ForegroundColor Cyan
    Write-Host "  Press Ctrl+C to stop" -ForegroundColor Gray
    Write-Host ""
    
    Set-Location $path
    python -m uvicorn server:app --host 127.0.0.1 --port 8000 --reload
}

function Launch-SIYEMConsole {
    Write-Host "[SIYEM Console V2]" -ForegroundColor Green
    Write-Host "  Checking dependencies..." -ForegroundColor Gray
    
    $path = "S:\SIYEM\08_WEB_DEV\console-v2"
    if (!(Test-Dependencies $path "SIYEM Console V2")) { return }
    
    Write-Host "  Starting on port 5173..." -ForegroundColor Yellow
    Write-Host "  Access at: http://localhost:5173" -ForegroundColor Cyan
    Write-Host "  Press Ctrl+C to stop" -ForegroundColor Gray
    Write-Host ""
    
    Set-Location $path
    npm run dev
}

function Launch-SIYEM {
    Write-Host "[SIYEM Complete System]" -ForegroundColor Green
    Write-Host "  This will open TWO terminals:" -ForegroundColor Yellow
    Write-Host "    1. Backend (port 8000)" -ForegroundColor Gray
    Write-Host "    2. Console V2 (port 5173)" -ForegroundColor Gray
    Write-Host ""
    
    # Start backend in new terminal
    Write-Host "  Launching backend..." -ForegroundColor Yellow
    Start-Process pwsh -ArgumentList "-NoExit", "-Command", "cd S:\SIYEM\07_AUTOMATION_AI; Write-Host 'SIYEM Backend Starting...' -ForegroundColor Cyan; python -m uvicorn server:app --host 127.0.0.1 --port 8000 --reload"
    
    Start-Sleep -Seconds 3
    
    # Start console in new terminal
    Write-Host "  Launching console..." -ForegroundColor Yellow
    Start-Process pwsh -ArgumentList "-NoExit", "-Command", "cd S:\SIYEM\08_WEB_DEV\console-v2; Write-Host 'SIYEM Console V2 Starting...' -ForegroundColor Cyan; npm run dev"
    
    Write-Host ""
    Write-Host "  SIYEM systems launching in separate windows..." -ForegroundColor Green
    Write-Host "  Backend: http://localhost:8000/docs" -ForegroundColor Cyan
    Write-Host "  Console: http://localhost:5173" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "  Close individual terminal windows to stop each service." -ForegroundColor Gray
}

function Launch-JANStudio {
    Write-Host "[JAN Studio]" -ForegroundColor Green
    Write-Host "  This will open TWO terminals:" -ForegroundColor Yellow
    Write-Host "    1. Backend (port 8001)" -ForegroundColor Gray
    Write-Host "    2. Frontend (port 3001)" -ForegroundColor Gray
    Write-Host ""
    
    # Start backend in new terminal
    Write-Host "  Launching backend..." -ForegroundColor Yellow
    Start-Process pwsh -ArgumentList "-NoExit", "-Command", "cd S:\JAN\jan-studio\backend; Write-Host 'JAN Studio Backend Starting...' -ForegroundColor Cyan; python -m uvicorn main:app --host 127.0.0.1 --port 8001 --reload"
    
    Start-Sleep -Seconds 3
    
    # Start frontend in new terminal
    Write-Host "  Launching frontend..." -ForegroundColor Yellow
    Start-Process pwsh -ArgumentList "-NoExit", "-Command", "cd S:\JAN\jan-studio\frontend; Write-Host 'JAN Studio Frontend Starting...' -ForegroundColor Cyan; npm run dev -- --port 3001"
    
    Write-Host ""
    Write-Host "  JAN Studio launching in separate windows..." -ForegroundColor Green
    Write-Host "  Backend: http://localhost:8001/docs" -ForegroundColor Cyan
    Write-Host "  Frontend: http://localhost:3001" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "  Close individual terminal windows to stop each service." -ForegroundColor Gray
}

function Launch-All {
    Write-Host "[ALL SYSTEMS]" -ForegroundColor Green
    Write-Host "  This will launch:" -ForegroundColor Yellow
    Write-Host "    - SIYEM Backend (port 8000)" -ForegroundColor Gray
    Write-Host "    - SIYEM Console (port 5173)" -ForegroundColor Gray
    Write-Host "    - JAN Studio Backend (port 8001)" -ForegroundColor Gray
    Write-Host "    - JAN Studio Frontend (port 3001)" -ForegroundColor Gray
    Write-Host "    - Homeostasis Sentinel (port 3000) - MANUAL START" -ForegroundColor Gray
    Write-Host ""
    Write-Host "  Note: Homeostasis is currently on port 3000." -ForegroundColor Yellow
    Write-Host "        If you need it, start manually after this." -ForegroundColor Yellow
    Write-Host ""
    
    # SIYEM Backend
    Write-Host "  Launching SIYEM Backend..." -ForegroundColor Yellow
    Start-Process pwsh -ArgumentList "-NoExit", "-Command", "cd S:\SIYEM\07_AUTOMATION_AI; Write-Host 'SIYEM Backend (Port 8000)' -ForegroundColor Cyan; python -m uvicorn server:app --host 127.0.0.1 --port 8000 --reload"
    Start-Sleep -Seconds 2
    
    # SIYEM Console
    Write-Host "  Launching SIYEM Console..." -ForegroundColor Yellow
    Start-Process pwsh -ArgumentList "-NoExit", "-Command", "cd S:\SIYEM\08_WEB_DEV\console-v2; Write-Host 'SIYEM Console V2 (Port 5173)' -ForegroundColor Cyan; npm run dev"
    Start-Sleep -Seconds 2
    
    # JAN Studio Backend
    Write-Host "  Launching JAN Studio Backend..." -ForegroundColor Yellow
    Start-Process pwsh -ArgumentList "-NoExit", "-Command", "cd S:\JAN\jan-studio\backend; Write-Host 'JAN Studio Backend (Port 8001)' -ForegroundColor Cyan; python -m uvicorn main:app --host 127.0.0.1 --port 8001 --reload"
    Start-Sleep -Seconds 2
    
    # JAN Studio Frontend
    Write-Host "  Launching JAN Studio Frontend..." -ForegroundColor Yellow
    Start-Process pwsh -ArgumentList "-NoExit", "-Command", "cd S:\JAN\jan-studio\frontend; Write-Host 'JAN Studio Frontend (Port 3001)' -ForegroundColor Cyan; npm run dev -- --port 3001"
    
    Write-Host ""
    Write-Host "  All systems launching..." -ForegroundColor Green
    Write-Host ""
    Write-Host "  Access Points:" -ForegroundColor Cyan
    Write-Host "    SIYEM Backend:    http://localhost:8000/docs" -ForegroundColor White
    Write-Host "    SIYEM Console:    http://localhost:5173" -ForegroundColor White
    Write-Host "    JAN Backend:      http://localhost:8001/docs" -ForegroundColor White
    Write-Host "    JAN Frontend:     http://localhost:3001" -ForegroundColor White
    Write-Host ""
    Write-Host "  To start Homeostasis Sentinel:" -ForegroundColor Yellow
    Write-Host "    cd S:\JAN\homeostasis-sentinel && npm run dev" -ForegroundColor Gray
    Write-Host ""
    Write-Host "  Close individual terminal windows to stop each service." -ForegroundColor Gray
}

# Main execution
switch ($System) {
    "help" { Show-Help }
    "homeostasis" { Launch-Homeostasis }
    "siyem-backend" { Launch-SIYEMBackend }
    "siyem-console" { Launch-SIYEMConsole }
    "siyem" { Launch-SIYEM }
    "jan-studio" { Launch-JANStudio }
    "all" { Launch-All }
    default { Show-Help }
}

