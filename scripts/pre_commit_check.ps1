# PRE-COMMIT VERIFICATION SCRIPT
# Run this before staging and committing changes

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "PRE-COMMIT VERIFICATION" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$errors = @()
$warnings = @()

# Step 1: Verify no secrets
Write-Host "[1/4] Checking for secrets in tracked files..." -ForegroundColor Yellow
try {
    $verifyScript = Join-Path $PSScriptRoot "verify_no_secrets.py"
    if (Test-Path $verifyScript) {
        python $verifyScript
        if ($LASTEXITCODE -ne 0) {
            $warnings += "Secret verification found issues - review output above"
        }
    } else {
        Write-Host "  ⚠️  verify_no_secrets.py not found - skipping" -ForegroundColor Yellow
    }
} catch {
    $warnings += "Could not run secret verification: $_"
}
Write-Host ""

# Step 2: Check git status
Write-Host "[2/4] Checking git status..." -ForegroundColor Yellow
try {
    $status = git status --short
    if ($status) {
        Write-Host "  ✓ Files staged/modified:" -ForegroundColor Green
        $status | ForEach-Object { Write-Host "    $_" }
    } else {
        Write-Host "  ⚠️  No changes detected" -ForegroundColor Yellow
    }
    
    # Check for .env files
    $envFiles = git status --ignored | Select-String "\.env"
    if ($envFiles) {
        Write-Host "  ✓ .env files are properly ignored" -ForegroundColor Green
    }
} catch {
    $errors += "Git status check failed: $_"
}
Write-Host ""

# Step 3: Verify critical files are ignored
Write-Host "[3/4] Verifying sensitive files are ignored..." -ForegroundColor Yellow
$sensitiveFiles = @(
    "world-history-app\.env.local",
    "SIYEM\output\financial_data.json",
    "SIYEM\output\free_will_data.json"
)

foreach ($file in $sensitiveFiles) {
    $fullPath = Join-Path (Split-Path $PSScriptRoot -Parent) $file
    if (Test-Path $fullPath) {
        $checkIgnore = git check-ignore -v $file 2>&1
        if ($LASTEXITCODE -eq 0) {
            Write-Host "  ✓ $file is ignored" -ForegroundColor Green
        } else {
            $errors += "$file is NOT ignored - CRITICAL"
        }
    }
}
Write-Host ""

# Step 4: Optional build checks (commented out by default - uncomment if needed)
Write-Host "[4/4] Build verification (optional)..." -ForegroundColor Yellow
Write-Host "  ℹ️  Skipping build checks (uncomment in script if needed)" -ForegroundColor Gray
Write-Host ""

# Optional: Uncomment these if you want to verify builds before commit
# Write-Host "  Checking jan-studio/frontend..." -ForegroundColor Gray
# Push-Location (Join-Path (Split-Path $PSScriptRoot -Parent) "jan-studio\frontend")
# npm run build 2>&1 | Out-Null
# if ($LASTEXITCODE -eq 0) {
#     Write-Host "    ✓ Build successful" -ForegroundColor Green
# } else {
#     $warnings += "jan-studio/frontend build failed"
# }
# Pop-Location

# Summary
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "VERIFICATION SUMMARY" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

if ($errors.Count -eq 0 -and $warnings.Count -eq 0) {
    Write-Host "✓ ALL CHECKS PASSED" -ForegroundColor Green
    Write-Host "  Safe to commit!" -ForegroundColor Green
    exit 0
} else {
    if ($errors.Count -gt 0) {
        Write-Host "✗ ERRORS FOUND:" -ForegroundColor Red
        $errors | ForEach-Object { Write-Host "  - $_" -ForegroundColor Red }
    }
    if ($warnings.Count -gt 0) {
        Write-Host "⚠️  WARNINGS:" -ForegroundColor Yellow
        $warnings | ForEach-Object { Write-Host "  - $_" -ForegroundColor Yellow }
    }
    Write-Host ""
    Write-Host "Review issues above before committing." -ForegroundColor Yellow
    exit 1
}
