# Remove ALL NUL files from S:\JAN
# Finds and removes all NUL files recursively

Write-Host "=== REMOVING ALL NUL FILES ===" -ForegroundColor Cyan
Write-Host ""

# Find all NUL files
Write-Host "[1/3] Scanning for NUL files..." -ForegroundColor Yellow
$nulFiles = Get-ChildItem -Path "S:\JAN" -Filter "NUL" -Recurse -Force -ErrorAction SilentlyContinue

$count = $nulFiles.Count
Write-Host "Found $count NUL file(s)" -ForegroundColor $(if ($count -gt 0) { "Yellow" } else { "Green" })
Write-Host ""

if ($count -eq 0) {
    Write-Host "No NUL files found! You're clean!" -ForegroundColor Green
    exit 0
}

# Remove them
Write-Host "[2/3] Removing NUL files..." -ForegroundColor Yellow
$removed = 0
$failed = 0

foreach ($nulFile in $nulFiles) {
    $nulPath = $nulFile.FullName
    $rawPath = "\\?\$nulPath"
    
    # Try cmd method first (worked before)
    $result = cmd /c "del /F /Q `"$rawPath`"" 2>&1
    
    if ($LASTEXITCODE -eq 0) {
        $removed++
        if ($removed % 50 -eq 0) {
            Write-Host "  Removed $removed / $count..." -ForegroundColor Gray
        }
    } else {
        # Try .NET method
        try {
            [System.IO.File]::Delete($rawPath)
            $removed++
        } catch {
            $failed++
        }
    }
}

Write-Host ""
Write-Host "[3/3] Results:" -ForegroundColor Yellow
Write-Host "  Removed: $removed / $count" -ForegroundColor $(if ($removed -eq $count) { "Green" } else { "Yellow" })
Write-Host "  Failed: $failed / $count" -ForegroundColor $(if ($failed -eq 0) { "Green" } else { "Red" })
Write-Host ""

if ($failed -gt 0) {
    Write-Host "Some files could not be removed (may be locked or phantom entries)" -ForegroundColor Yellow
}

Write-Host "Done!" -ForegroundColor Cyan
