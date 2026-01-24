# Quick script to remove S: drive NUL files
$nulFiles = @("S:\JAN\NUL", "S:\JAN\jan-studio\NUL")
Write-Host "Attempting to remove S: drive NUL files..." -ForegroundColor Yellow
Write-Host ""
foreach ($nulPath in $nulFiles) {
    Write-Host "Trying: $nulPath" -ForegroundColor Cyan
    $rawPath = "\\?\$nulPath"
    $result = cmd /c "del /F /Q `"$rawPath`""
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  Success!" -ForegroundColor Green
    } else {
        Write-Host "  Failed - trying .NET method..." -ForegroundColor Yellow
        try {
            [System.IO.File]::Delete($rawPath)
            Write-Host "  Success with .NET method!" -ForegroundColor Green
        } catch {
            Write-Host "  Failed: $($_.Exception.Message)" -ForegroundColor Red
        }
    }
    Write-Host ""
}
Write-Host "Done!" -ForegroundColor Cyan
