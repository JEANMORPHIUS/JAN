# Test backend startup with error capture
cd S:\JAN\jan-studio\backend

Write-Host "=== TESTING BACKEND STARTUP ===" -ForegroundColor Cyan
Write-Host ""

# Try to start and capture output
Write-Host "Starting backend server..." -ForegroundColor Yellow
Write-Host "This will run for 15 seconds to capture any startup errors..." -ForegroundColor Gray
Write-Host ""

$job = Start-Job -ScriptBlock {
    cd S:\JAN\jan-studio\backend
    python main.py 2>&1
}

Start-Sleep -Seconds 15

# Get output
$output = Receive-Job -Job $job
Stop-Job -Job $job
Remove-Job -Job $job

# Display output
$output | Select-Object -First 50

Write-Host ""
Write-Host "=== CHECKING IF SERVER IS RUNNING ===" -ForegroundColor Cyan
try {
    $response = Invoke-WebRequest -Uri "http://localhost:8000/api/public/world-history/status" -TimeoutSec 3 -ErrorAction Stop
    Write-Host "Server is RUNNING!" -ForegroundColor Green
    Write-Host "Status: $($response.StatusCode)" -ForegroundColor Green
} catch {
    Write-Host "Server is NOT running" -ForegroundColor Red
    Write-Host "Error: $($_.Exception.Message)" -ForegroundColor Yellow
}
