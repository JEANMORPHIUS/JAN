# START BACKEND SERVER
# Dedicated script to start the backend API server

$backendDir = "S:\JAN\jan-studio\backend"

Write-Host "=== STARTING BACKEND SERVER ===" -ForegroundColor Cyan
Write-Host ""

# Check Python
$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    Write-Host "ERROR: Python not found!" -ForegroundColor Red
    exit 1
}
Write-Host "Python: $($python.Source)" -ForegroundColor Green
Write-Host ""

# Check if port 8000 is in use
Write-Host "Checking port 8000..." -ForegroundColor Yellow
$portInUse = Get-NetTCPConnection -LocalPort 8000 -ErrorAction SilentlyContinue
if ($portInUse) {
    Write-Host "Port 8000 is already in use" -ForegroundColor Yellow
    Write-Host "Killing existing process..." -ForegroundColor Gray
    $process = Get-Process -Id $portInUse.OwningProcess -ErrorAction SilentlyContinue
    if ($process) {
        Stop-Process -Id $process.Id -Force -ErrorAction SilentlyContinue
        Start-Sleep -Seconds 2
        Write-Host "Process killed" -ForegroundColor Green
    }
}
Write-Host ""

# Navigate to backend directory
Set-Location $backendDir
Write-Host "Working directory: $backendDir" -ForegroundColor Gray
Write-Host ""

# Check if main.py exists
if (-not (Test-Path "main.py")) {
    Write-Host "ERROR: main.py not found in $backendDir" -ForegroundColor Red
    exit 1
}

# Start the server
Write-Host "Starting backend server..." -ForegroundColor Yellow
Write-Host "Command: python main.py" -ForegroundColor Gray
Write-Host ""

# Start in a new window so we can see output
Start-Process python -ArgumentList "main.py" -WorkingDirectory $backendDir

Write-Host "Backend server starting..." -ForegroundColor Green
Write-Host "Waiting 10 seconds for initialization..." -ForegroundColor Gray
Start-Sleep -Seconds 10

# Verify it started
Write-Host ""
Write-Host "Verifying server..." -ForegroundColor Yellow
try {
    $response = Invoke-WebRequest -Uri "http://localhost:8000/api/public/world-history/status" -TimeoutSec 5 -ErrorAction Stop
    if ($response.StatusCode -eq 200) {
        Write-Host "Backend server is RUNNING!" -ForegroundColor Green
        Write-Host ""
        Write-Host "Access points:" -ForegroundColor Cyan
        Write-Host "  - API: http://localhost:8000/api/public/world-history/status" -ForegroundColor White
        Write-Host "  - Docs: http://localhost:8000/docs" -ForegroundColor White
    }
} catch {
    Write-Host "WARNING: Server may not have started properly" -ForegroundColor Yellow
    Write-Host "Error: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host ""
    Write-Host "Try:" -ForegroundColor Yellow
    Write-Host "  1. Check if dependencies are installed: pip install -r requirements.txt" -ForegroundColor White
    Write-Host "  2. Check for errors in the server window" -ForegroundColor White
    Write-Host "  3. Try running manually: cd $backendDir && python main.py" -ForegroundColor White
}

Write-Host ""
Write-Host "SPRAGITSO - Our Father's Royal Seal" -ForegroundColor Cyan
