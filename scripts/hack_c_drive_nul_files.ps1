# HACK ALL C: DRIVE NUL FILES
# Finds and attempts to remove ALL NUL files on C: drive
# WARNING: This is aggressive - use with caution!

param(
    [switch]$Force,
    [switch]$DryRun
)

Write-Host "=== HACKING ALL C: DRIVE NUL FILES ===" -ForegroundColor Cyan
Write-Host ""

if ($DryRun) {
    Write-Host "🔍 DRY RUN MODE - No files will be deleted" -ForegroundColor Yellow
    Write-Host ""
}

# Find all NUL files on C: drive
Write-Host "[1/3] Scanning for NUL files on C: drive..." -ForegroundColor Yellow
Write-Host "This may take a while..." -ForegroundColor Gray

$nulFiles = @()

# Scan C:\ root
Write-Host "  Scanning C:\..." -ForegroundColor DarkGray
$rootNul = Get-ChildItem -Path "C:\" -Filter "NUL" -Force -ErrorAction SilentlyContinue
if ($rootNul) {
    $nulFiles += $rootNul
}

# Scan user profile (most common location)
Write-Host "  Scanning C:\Users\janmu..." -ForegroundColor DarkGray
$userNul = Get-ChildItem -Path "C:\Users\janmu" -Filter "NUL" -Recurse -Force -ErrorAction SilentlyContinue
if ($userNul) {
    $nulFiles += $userNul
}

Write-Host ""
Write-Host "Found $($nulFiles.Count) NUL file(s)" -ForegroundColor $(if ($nulFiles.Count -gt 0) { "Yellow" } else { "Green" })
Write-Host ""

if ($nulFiles.Count -eq 0) {
    Write-Host "No NUL files found! You're clean!" -ForegroundColor Green
    exit 0
}

# Show what we found
Write-Host "[2/3] NUL Files Found:" -ForegroundColor Yellow
$nulFiles | ForEach-Object {
    Write-Host "  - $($_.FullName) ($($_.Length) bytes)" -ForegroundColor Gray
}
Write-Host ""

if ($DryRun) {
    Write-Host "DRY RUN: Would attempt to remove $($nulFiles.Count) file(s)" -ForegroundColor Yellow
    exit 0
}

# Attempt removal using the hack script
Write-Host "[3/3] Attempting to remove NUL files..." -ForegroundColor Yellow
Write-Host ""

$removed = 0
$failed = 0

foreach ($nulFile in $nulFiles) {
    $nulPath = $nulFile.FullName
    Write-Host "Processing: $nulPath" -ForegroundColor Cyan
    
    # Try multiple methods
    $success = $false
    
    # Method 1: \\?\ prefix
    try {
        $rawPath = "\\?\$nulPath"
        $result = cmd /c "del /F /Q `"$rawPath`" 2>&1"
        if ($LASTEXITCODE -eq 0) {
            Write-Host "  ✓ Removed using \\?\ prefix" -ForegroundColor Green
            $removed++
            $success = $true
            continue
        }
    } catch {}
    
    # Method 2: .NET DeleteFile
    try {
        $rawPath = "\\?\$nulPath"
        [System.IO.File]::Delete($rawPath)
        Write-Host "  ✓ Removed using .NET method" -ForegroundColor Green
        $removed++
        $success = $true
        continue
    } catch {}
    
    # Method 3: Win32 API (if Force)
    if ($Force) {
        try {
            $rawPath = "\\?\$nulPath"
            Add-Type -TypeDefinition @"
                using System;
                using System.Runtime.InteropServices;
                public class Win32 {
                    [DllImport("kernel32.dll", SetLastError=true, CharSet=CharSet.Auto)]
                    public static extern bool DeleteFile(string lpFileName);
                }
"@ -ErrorAction SilentlyContinue
            $result = [Win32]::DeleteFile($rawPath)
            if ($result) {
                Write-Host "  ✓ Removed using Win32 API" -ForegroundColor Green
                $removed++
                $success = $true
                continue
            }
        } catch {}
    }
    
    if (-not $success) {
        Write-Host "  ✗ Failed to remove" -ForegroundColor Red
        $failed++
    }
    
    Write-Host ""
}

Write-Host "=== RESULTS ===" -ForegroundColor Cyan
Write-Host "Removed: $removed / $($nulFiles.Count)" -ForegroundColor $(if ($removed -eq $nulFiles.Count) { "Green" } else { "Yellow" })
Write-Host "Failed: $failed / $($nulFiles.Count)" -ForegroundColor $(if ($failed -eq 0) { "Green" } else { "Red" })
Write-Host ""

if ($failed -gt 0) {
    Write-Host "Some NUL files could not be removed." -ForegroundColor Yellow
    Write-Host "They may be phantom entries or locked by the system." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Try:" -ForegroundColor White
    Write-Host "1. Run as Administrator" -ForegroundColor Gray
    Write-Host "2. Boot into Safe Mode and try again" -ForegroundColor Gray
    Write-Host "3. Use: .\scripts\hack_nul_files.ps1 -CDrive -Force" -ForegroundColor Gray
    Write-Host ""
}

Write-Host "SPRAGITSO - Our Father's Royal Seal" -ForegroundColor Cyan
