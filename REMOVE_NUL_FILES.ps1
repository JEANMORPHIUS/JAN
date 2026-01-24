# Remove NUL Files - Windows Device Files
# NUL is a reserved Windows device name - requires special handling

Write-Host "=== REMOVING NUL FILES ===" -ForegroundColor Cyan
Write-Host ""

# Method 1: Try using cmd /c del (handles device names better)
Write-Host "Attempting to remove NUL files using cmd..." -ForegroundColor Yellow

$nulPaths = @(
    "S:\JAN\NUL",
    "S:\JAN\jan-studio\NUL"
)

foreach ($nulPath in $nulPaths) {
    Write-Host "  Attempting: $nulPath" -ForegroundColor Gray
    
    # Use cmd to delete (handles device names)
    $result = cmd /c "del /F /Q `"$nulPath`" 2>&1"
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  [OK] Removed: $nulPath" -ForegroundColor Green
    } else {
        Write-Host "  [INFO] File may not exist or is already removed: $nulPath" -ForegroundColor Yellow
    }
}

Write-Host ""
Write-Host "=== VERIFICATION ===" -ForegroundColor Cyan

# Check if NUL files still exist
$remaining = Get-ChildItem -Path "S:\JAN" -Recurse -Force -ErrorAction SilentlyContinue | Where-Object { $_.Name -eq "NUL" }

if ($remaining) {
    Write-Host "[WARNING] NUL files still exist:" -ForegroundColor Yellow
    foreach ($file in $remaining) {
        Write-Host "  - $($file.FullName)" -ForegroundColor Gray
    }
    Write-Host ""
    Write-Host "These are Windows device files. They may be phantom entries." -ForegroundColor Yellow
    Write-Host "Git will ignore them if NUL is in .gitignore (which it is)." -ForegroundColor Yellow
} else {
    Write-Host "[OK] No NUL files found" -ForegroundColor Green
}

Write-Host ""
Write-Host "=== NEXT STEPS ===" -ForegroundColor Cyan
Write-Host "1. NUL files are in .gitignore - git will ignore them" -ForegroundColor White
Write-Host "2. Run: git add -A" -ForegroundColor White
Write-Host "3. Run: git commit -m 'Your message'" -ForegroundColor White
Write-Host "4. Run: git push origin master" -ForegroundColor White
Write-Host ""
Write-Host "SPRAGITSO - Our Father's Royal Seal" -ForegroundColor Cyan
