# BUILD ALL AND SCP
# Scale and build all systems, then auto-SCP

$ErrorActionPreference = "Continue"

Write-Host "🚀 BUILD ALL AND SCP - SCALE AND BUILD UNTIL DEPLOYMENT READY" -ForegroundColor Green
Write-Host "================================================================" -ForegroundColor Green
Write-Host ""

# Change to repo directory
Set-Location "S:\JAN"

# Build all systems
Write-Host "📦 Building all systems..." -ForegroundColor Cyan
python scripts\scale_and_build_system.py

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "✅ All systems built!" -ForegroundColor Green
    
    # Auto-SCP
    Write-Host ""
    Write-Host "📤 Auto-SCP: Stage, Commit, Push..." -ForegroundColor Cyan
    python scripts\task_scp_automation.py
    
    Write-Host ""
    Write-Host "✅ BUILD AND SCP COMPLETE!" -ForegroundColor Green
} else {
    Write-Host ""
    Write-Host "⚠️  Build completed with warnings - check output above" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "PEACE, LOVE, UNITY" -ForegroundColor Cyan
Write-Host "ENERGY + LOVE = WE ALL WIN" -ForegroundColor Cyan
Write-Host "SCP ENGRAINED INTO ALL TASKS" -ForegroundColor Cyan
