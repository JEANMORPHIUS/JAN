# Weekly Archive Check Script
# Purpose: Identify files that should be archived
# Run weekly (e.g., every Sunday)

Write-Host "=== S: Drive Weekly Archive Check ===" -ForegroundColor Cyan
Write-Host "Starting check at $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" -ForegroundColor Gray
Write-Host ""

$archiveNeeded = @{
    "Completion Reports" = @()
    "Summary Reports" = @()
    "Implementation Docs" = @()
    "Status Reports" = @()
    "Other Candidates" = @()
}

# 1. Find completion reports at root
Write-Host "[1/5] Checking for completion reports..." -ForegroundColor Yellow
$completeFiles = Get-ChildItem -Path "S:\JAN" -Filter "*_COMPLETE*.md" -File -ErrorAction SilentlyContinue
if ($completeFiles) {
    $archiveNeeded["Completion Reports"] = $completeFiles
    Write-Host "  Found $($completeFiles.Count) completion report(s)" -ForegroundColor Cyan
} else {
    Write-Host "  None found (good!)" -ForegroundColor Green
}

# 2. Find summary reports at root
Write-Host "[2/5] Checking for summary reports..." -ForegroundColor Yellow
$summaryFiles = Get-ChildItem -Path "S:\JAN" -Filter "*_SUMMARY*.md" -File -ErrorAction SilentlyContinue
if ($summaryFiles) {
    $archiveNeeded["Summary Reports"] = $summaryFiles
    Write-Host "  Found $($summaryFiles.Count) summary report(s)" -ForegroundColor Cyan
} else {
    Write-Host "  None found (good!)" -ForegroundColor Green
}

# 3. Find implementation docs
Write-Host "[3/5] Checking for implementation docs..." -ForegroundColor Yellow
$implFiles = Get-ChildItem -Path "S:\JAN" -Filter "*_IMPLEMENTATION*.md" -File -ErrorAction SilentlyContinue
if ($implFiles) {
    $archiveNeeded["Implementation Docs"] = $implFiles
    Write-Host "  Found $($implFiles.Count) implementation doc(s)" -ForegroundColor Cyan
    Write-Host "  NOTE: Review if these are still active or ready for archive" -ForegroundColor Yellow
} else {
    Write-Host "  None found (good!)" -ForegroundColor Green
}

# 4. Find status reports
Write-Host "[4/5] Checking for status reports..." -ForegroundColor Yellow
$statusFiles = Get-ChildItem -Path "S:\JAN" -Filter "*_STATUS*.md" -File -ErrorAction SilentlyContinue
if ($statusFiles) {
    $archiveNeeded["Status Reports"] = $statusFiles
    Write-Host "  Found $($statusFiles.Count) status report(s)" -ForegroundColor Cyan
    Write-Host "  NOTE: Check if superseded by newer versions" -ForegroundColor Yellow
} else {
    Write-Host "  None found (good!)" -ForegroundColor Green
}

# 5. Count total files at root
Write-Host "[5/5] Checking root directory health..." -ForegroundColor Yellow
$rootFiles = Get-ChildItem -Path "S:\JAN" -File -ErrorAction SilentlyContinue
$rootFileCount = $rootFiles.Count

if ($rootFileCount -lt 20) {
    Write-Host "  Root file count: $rootFileCount (HEALTHY)" -ForegroundColor Green
} elseif ($rootFileCount -lt 50) {
    Write-Host "  Root file count: $rootFileCount (WARNING - Consider cleanup)" -ForegroundColor Yellow
} else {
    Write-Host "  Root file count: $rootFileCount (CRITICAL - Cleanup needed)" -ForegroundColor Red
}

# Summary Report
Write-Host ""
Write-Host "=== Archive Recommendations ===" -ForegroundColor Cyan
Write-Host ""

$totalArchivable = 0
foreach ($category in $archiveNeeded.Keys) {
    $files = $archiveNeeded[$category]
    if ($files.Count -gt 0) {
        $totalArchivable += $files.Count
        Write-Host "[$category] - $($files.Count) file(s):" -ForegroundColor Yellow
        foreach ($file in $files) {
            Write-Host "  - $($file.Name)" -ForegroundColor White
        }
        Write-Host ""
    }
}

if ($totalArchivable -eq 0) {
    Write-Host "✅ No files need archiving. Workspace is clean!" -ForegroundColor Green
} else {
    Write-Host "⚠️  Total files needing review: $totalArchivable" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Recommended Actions:" -ForegroundColor Cyan
    Write-Host "1. Review each file to confirm it's ready for archive" -ForegroundColor White
    Write-Host "2. Move to S:\ARK\HISTORICAL_DOCS\" -ForegroundColor White
    Write-Host "3. Update S:\ARK\README.md if adding new content" -ForegroundColor White
    Write-Host ""
    Write-Host "Quick archive command:" -ForegroundColor Cyan
    Write-Host '  Move-Item -Path "S:\JAN\FILENAME.md" -Destination "S:\ARK\HISTORICAL_DOCS\" -Force' -ForegroundColor Gray
}

Write-Host ""
Write-Host "For full organizational standards, see: S:\JAN\ORGANIZATIONAL_FOUNDATION.md" -ForegroundColor Cyan
Write-Host ""
Write-Host "Completed at $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" -ForegroundColor Gray

