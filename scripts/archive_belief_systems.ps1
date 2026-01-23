# Archive Belief Systems Script
# Moves belief-based documentation to archive

$archivePath = "S:\ARK\HISTORICAL_DOCS"
$sourcePath = "S:\JAN"

# Ensure archive directory exists
if (-not (Test-Path $archivePath)) {
    New-Item -ItemType Directory -Path $archivePath -Force | Out-Null
    Write-Host "Created archive directory: $archivePath" -ForegroundColor Green
}

# Files to archive (belief-based documentation)
$filesToArchive = @(
    "BELIEF_AUDIT_REPORT.md"
)

foreach ($file in $filesToArchive) {
    $sourceFile = Join-Path $sourcePath $file
    if (Test-Path $sourceFile) {
        $destFile = Join-Path $archivePath $file
        Move-Item -Path $sourceFile -Destination $destFile -Force
        Write-Host "Archived: $file -> $archivePath" -ForegroundColor Yellow
    } else {
        Write-Host "File not found: $file" -ForegroundColor Red
    }
}

Write-Host "`nBelief systems archiving complete." -ForegroundColor Green
Write-Host "All belief-based documentation moved to archive." -ForegroundColor Green
Write-Host "Replaced with KNOWLEDGE_OVER_BELIEF.md" -ForegroundColor Green
