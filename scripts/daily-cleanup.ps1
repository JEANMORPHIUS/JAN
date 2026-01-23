# Daily Cleanup Script
# Purpose: Remove temporary files and maintain workspace hygiene
# Run at end of day or as needed

Write-Host "=== S: Drive Daily Cleanup ===" -ForegroundColor Cyan
Write-Host "Starting cleanup at $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" -ForegroundColor Gray
Write-Host ""

$cleanupCount = 0

# 1. Remove temp files
Write-Host "[1/4] Removing temporary files..." -ForegroundColor Yellow
$tempPatterns = @("tmp*", "*.tmp", "*.temp", "NUL")
foreach ($pattern in $tempPatterns) {
    $tempFiles = Get-ChildItem -Path "S:\JAN" -Recurse -Filter $pattern -File -ErrorAction SilentlyContinue
    foreach ($file in $tempFiles) {
        Write-Host "  Removing: $($file.FullName)" -ForegroundColor DarkGray
        Remove-Item -Path $file.FullName -Force -ErrorAction SilentlyContinue
        $cleanupCount++
    }
}

# 2. Remove tmpclaude directories
Write-Host "[2/4] Removing tmpclaude directories..." -ForegroundColor Yellow
$tmpclaude = Get-ChildItem -Path "S:\" -Filter "tmpclaude-*" -Directory -ErrorAction SilentlyContinue
foreach ($dir in $tmpclaude) {
    Write-Host "  Removing: $($dir.FullName)" -ForegroundColor DarkGray
    Remove-Item -Path $dir.FullName -Recurse -Force -ErrorAction SilentlyContinue
    $cleanupCount++
}

# 3. Remove backup files
Write-Host "[3/4] Checking for backup files..." -ForegroundColor Yellow
$backupPatterns = @("*.bak", "*.old", "*.backup")
foreach ($pattern in $backupPatterns) {
    $backupFiles = Get-ChildItem -Path "S:\JAN" -Recurse -Filter $pattern -File -ErrorAction SilentlyContinue
    if ($backupFiles) {
        Write-Host "  WARNING: Found backup files (review before deleting):" -ForegroundColor Red
        foreach ($file in $backupFiles) {
            Write-Host "    - $($file.FullName)" -ForegroundColor DarkYellow
        }
    }
}

# 4. Check for archivable files at root
Write-Host "[4/4] Checking for archivable files at root..." -ForegroundColor Yellow
$archivePatterns = @("*_COMPLETE*.md", "*_SUMMARY*.md", "*_REPORT*.md")
$archiveNeeded = @()
foreach ($pattern in $archivePatterns) {
    $files = Get-ChildItem -Path "S:\JAN" -Filter $pattern -File -ErrorAction SilentlyContinue
    if ($files) {
        $archiveNeeded += $files
    }
}

if ($archiveNeeded.Count -gt 0) {
    Write-Host "  INFO: Found $($archiveNeeded.Count) file(s) that may need archiving:" -ForegroundColor Yellow
    foreach ($file in $archiveNeeded) {
        Write-Host "    - $($file.Name)" -ForegroundColor Cyan
    }
    Write-Host "  Consider moving these to S:\ARK\HISTORICAL_DOCS\" -ForegroundColor Cyan
}

# Summary
Write-Host ""
Write-Host "=== Cleanup Complete ===" -ForegroundColor Green
Write-Host "Files removed: $cleanupCount" -ForegroundColor White
if ($archiveNeeded.Count -gt 0) {
    Write-Host "Files needing review: $($archiveNeeded.Count)" -ForegroundColor Yellow
}
Write-Host "Completed at $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" -ForegroundColor Gray
Write-Host ""
Write-Host "For full organizational standards, see: S:\JAN\ORGANIZATIONAL_FOUNDATION.md" -ForegroundColor Cyan

