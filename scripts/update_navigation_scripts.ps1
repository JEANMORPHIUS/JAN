# UPDATE NAVIGATION SCRIPTS
# Manually update C: drive navigation scripts to use S:\SIYEM
#
# Run this script as Administrator or with proper permissions
# to update the navigation scripts in your user directory

$ErrorActionPreference = "Stop"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   UPDATE NAVIGATION SCRIPTS" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$userProfile = $env:USERPROFILE

$scripts = @{
    "$userProfile\cd_core.ps1" = "Set-Location S:\SIYEM\00_CORE"
    "$userProfile\cd_prod.ps1" = "Set-Location S:\SIYEM\03_PRODUCTION"
    "$userProfile\cd_pub.ps1" = "Set-Location S:\SIYEM\05_PUBLISHING"
}

$updated = 0
$failed = 0

foreach ($scriptPath in $scripts.Keys) {
    $newContent = $scripts[$scriptPath]
    
    Write-Host "Updating: $scriptPath" -ForegroundColor Yellow
    
    if (-not (Test-Path $scriptPath)) {
        Write-Host "  [SKIP] File not found" -ForegroundColor DarkGray
        continue
    }
    
    try {
        # Check current content
        $currentContent = Get-Content $scriptPath -Raw
        
        if ($currentContent.Trim() -eq $newContent) {
            Write-Host "  [OK] Already up to date" -ForegroundColor Green
            continue
        }
        
        # Backup original
        $backupPath = "$scriptPath.backup"
        Copy-Item -Path $scriptPath -Destination $backupPath -Force
        Write-Host "  [BACKUP] Created: $backupPath" -ForegroundColor Gray
        
        # Update script
        Set-Content -Path $scriptPath -Value $newContent -Encoding UTF8 -Force
        Write-Host "  [UPDATED] $scriptPath" -ForegroundColor Green
        Write-Host "    New content: $newContent" -ForegroundColor Gray
        $updated++
        
    } catch {
        Write-Host "  [ERROR] Failed to update: $_" -ForegroundColor Red
        $failed++
    }
    
    Write-Host ""
}

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   SUMMARY" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Updated: $updated" -ForegroundColor $(if ($updated -gt 0) { "Green" } else { "Gray" })
Write-Host "Failed: $failed" -ForegroundColor $(if ($failed -gt 0) { "Red" } else { "Gray" })
Write-Host ""

if ($updated -gt 0) {
    Write-Host "Navigation scripts updated successfully!" -ForegroundColor Green
    Write-Host "Backups created with .backup extension" -ForegroundColor Gray
}

Write-Host ""
Write-Host "PEACE, LOVE, UNITY" -ForegroundColor Green
