# npm audit fix - Run across all projects
# This script runs npm audit fix in each project directory

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "npm audit fix - All Projects" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$projects = @(
    "admin-dashboard",
    "world-history-app",
    "pi-display",
    "jan-studio\frontend",
    "homeostasis-sentinel",
    "ATILOK"
)

$basePath = "S:\JAN"
$failed = @()
$success = @()

foreach ($project in $projects) {
    $projectPath = Join-Path $basePath $project
    
    if (Test-Path $projectPath) {
        Write-Host "Processing: $project" -ForegroundColor Yellow
        Write-Host "  Path: $projectPath" -ForegroundColor Gray
        
        Push-Location $projectPath
        
        try {
            # First check audit
            Write-Host "  Running npm audit..." -ForegroundColor Gray
            npm audit --json | Out-Null
            
            # Then fix
            Write-Host "  Running npm audit fix..." -ForegroundColor Gray
            npm audit fix
            
            if ($LASTEXITCODE -eq 0) {
                Write-Host "  ✅ Success" -ForegroundColor Green
                $success += $project
            } else {
                Write-Host "  ⚠️  Completed with warnings (exit code: $LASTEXITCODE)" -ForegroundColor Yellow
                $success += $project
            }
        }
        catch {
            Write-Host "  ❌ Failed: $_" -ForegroundColor Red
            $failed += $project
        }
        finally {
            Pop-Location
            Write-Host ""
        }
    } else {
        Write-Host "  ⚠️  Path not found: $projectPath" -ForegroundColor Yellow
        $failed += $project
        Write-Host ""
    }
}

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Summary" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "✅ Successful: $($success.Count)" -ForegroundColor Green
Write-Host "❌ Failed: $($failed.Count)" -ForegroundColor $(if ($failed.Count -gt 0) { "Red" } else { "Green" })

if ($failed.Count -gt 0) {
    Write-Host ""
    Write-Host "Failed projects:" -ForegroundColor Red
    foreach ($f in $failed) {
        Write-Host "  - $f" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "Done!" -ForegroundColor Cyan
