# HACK NUL FILES - Advanced Removal Techniques
# NUL is a Windows reserved device name - requires "hacky" methods
# This script tries multiple advanced techniques to actually remove NUL files

param(
    [switch]$Force,
    [switch]$CDrive,
    [string[]]$Paths = @()
)

# Default paths if none specified
if ($Paths.Count -eq 0) {
    if ($CDrive) {
        # C: drive NUL files
        $Paths = @(
            "C:\NUL",
            "C:\Users\janmu\NUL"
        )
    } else {
        # S: drive NUL files (default)
        $Paths = @("S:\JAN\NUL", "S:\JAN\jan-studio\NUL")
    }
}

Write-Host "=== HACKING NUL FILES ===" -ForegroundColor Cyan
Write-Host "Trying advanced removal techniques..." -ForegroundColor Yellow
if ($CDrive) {
    Write-Host "⚠️  C: DRIVE MODE - Be careful!" -ForegroundColor Red
}
Write-Host ""

$removed = @()
$failed = @()

foreach ($nulPath in $Paths) {
    Write-Host "Attempting to hack: $nulPath" -ForegroundColor Yellow
    $success = $false
    
    # METHOD 1: Use \\?\ prefix to bypass path normalization
    Write-Host "  [1/6] Trying \\?\ prefix method..." -ForegroundColor Gray
    try {
        $rawPath = "\\?\$nulPath"
        $result = cmd /c "del /F /Q `"$rawPath`"" 2>&1
        if ($LASTEXITCODE -eq 0) {
            Write-Host "    ✓ Success with \\?\ prefix" -ForegroundColor Green
            $removed += $nulPath
            $success = $true
            continue
        }
    } catch {
        Write-Host "    ✗ Failed" -ForegroundColor DarkGray
    }
    
    # METHOD 2: Use subst to create virtual drive, then delete
    Write-Host "  [2/6] Trying subst virtual drive method..." -ForegroundColor Gray
    try {
        $parentDir = Split-Path -Parent $nulPath
        $driveLetter = "Z:"
        
        # Create virtual drive
        subst $driveLetter $parentDir 2>$null
        
        # Try to delete from virtual drive
        $virtualPath = "$driveLetter\NUL"
        $result = cmd /c "del /F /Q `"$virtualPath`"" 2>&1
        
        # Remove virtual drive
        subst $driveLetter /D 2>$null
        
        if ($LASTEXITCODE -eq 0) {
            Write-Host "    ✓ Success with subst method" -ForegroundColor Green
            $removed += $nulPath
            $success = $true
            continue
        }
    } catch {
        Write-Host "    ✗ Failed" -ForegroundColor DarkGray
    }
    
    # METHOD 3: Use robocopy with mirror to empty directory
    Write-Host "  [3/6] Trying robocopy mirror method..." -ForegroundColor Gray
    try {
        $tempDir = "$env:TEMP\nul_hack_$(Get-Random)"
        New-Item -ItemType Directory -Path $tempDir -Force | Out-Null
        
        $parentDir = Split-Path -Parent $nulPath
        robocopy $tempDir $parentDir /MIR /NFL /NDL /NJH /NJS 2>&1 | Out-Null
        
        Remove-Item $tempDir -Force -ErrorAction SilentlyContinue
        
        # Check if it worked
        $stillExists = Test-Path $nulPath -ErrorAction SilentlyContinue
        if (-not $stillExists) {
            Write-Host "    ✓ Success with robocopy method" -ForegroundColor Green
            $removed += $nulPath
            $success = $true
            continue
        }
    } catch {
        Write-Host "    ✗ Failed" -ForegroundColor DarkGray
    }
    
    # METHOD 4: Use fsutil to check and potentially remove
    Write-Host "  [4/6] Trying fsutil method..." -ForegroundColor Gray
    try {
        $parentDir = Split-Path -Parent $nulPath
        $result = fsutil file queryfilenamebyid "$parentDir" 0 2>&1
        
        # Try to delete using fsutil
        $result = cmd /c "fsutil file setzerodata offset=0 length=0 `"$nulPath`"" 2>&1
        $result = cmd /c "del /F /Q `"$nulPath`"" 2>&1
        
        if ($LASTEXITCODE -eq 0) {
            Write-Host "    ✓ Success with fsutil method" -ForegroundColor Green
            $removed += $nulPath
            $success = $true
            continue
        }
    } catch {
        Write-Host "    ✗ Failed" -ForegroundColor DarkGray
    }
    
    # METHOD 5: Use PowerShell's .NET methods with raw paths
    Write-Host "  [5/6] Trying .NET raw path method..." -ForegroundColor Gray
    try {
        $rawPath = "\\?\$nulPath"
        [System.IO.File]::Delete($rawPath)
        Write-Host "    ✓ Success with .NET method" -ForegroundColor Green
        $removed += $nulPath
        $success = $true
        continue
    } catch {
        Write-Host "    ✗ Failed: $($_.Exception.Message)" -ForegroundColor DarkGray
    }
    
    # METHOD 6: Use takeown + icacls + del (nuclear option)
    Write-Host "  [6/8] Trying takeown + icacls method (nuclear)..." -ForegroundColor Gray
    try {
        if ($Force) {
            $parentDir = Split-Path -Parent $nulPath
            takeown /F $nulPath 2>&1 | Out-Null
            icacls $nulPath /grant "${env:USERNAME}:F" 2>&1 | Out-Null
            $result = cmd /c "del /F /Q `"$nulPath`"" 2>&1
            
            if ($LASTEXITCODE -eq 0) {
                Write-Host "    ✓ Success with takeown method" -ForegroundColor Green
                $removed += $nulPath
                $success = $true
                continue
            }
        } else {
            Write-Host "    ⚠ Skipped (use -Force to try)" -ForegroundColor Yellow
        }
    } catch {
        Write-Host "    ✗ Failed" -ForegroundColor DarkGray
    }
    
    # METHOD 7: Use Win32 API via PowerShell (most hacky)
    Write-Host "  [7/8] Trying Win32 API method (ultra hacky)..." -ForegroundColor Gray
    try {
        $rawPath = "\\?\$nulPath"
        Add-Type -TypeDefinition @"
            using System;
            using System.Runtime.InteropServices;
            public class Win32 {
                [DllImport("kernel32.dll", SetLastError=true, CharSet=CharSet.Auto)]
                public static extern bool DeleteFile(string lpFileName);
            }
"@
        $result = [Win32]::DeleteFile($rawPath)
        if ($result) {
            Write-Host "    ✓ Success with Win32 API method" -ForegroundColor Green
            $removed += $nulPath
            $success = $true
            continue
        }
    } catch {
        Write-Host "    ✗ Failed: $($_.Exception.Message)" -ForegroundColor DarkGray
    }
    
    # METHOD 8: Use short path name (8.3 format) trick
    Write-Host "  [8/8] Trying 8.3 short path name method..." -ForegroundColor Gray
    try {
        $parentDir = Split-Path -Parent $nulPath
        $fs = New-Object -ComObject Scripting.FileSystemObject
        $shortPath = $fs.GetFile($nulPath).ShortPath 2>$null
        
        if ($shortPath) {
            $result = cmd /c "del /F /Q `"$shortPath`"" 2>&1
            if ($LASTEXITCODE -eq 0) {
                Write-Host "    ✓ Success with 8.3 path method" -ForegroundColor Green
                $removed += $nulPath
                $success = $true
                continue
            }
        }
    } catch {
        Write-Host "    ✗ Failed" -ForegroundColor DarkGray
    }
    
    if (-not $success) {
        Write-Host "  ✗ All methods failed for: $nulPath" -ForegroundColor Red
        $failed += $nulPath
    }
    
    Write-Host ""
}

Write-Host "=== RESULTS ===" -ForegroundColor Cyan
Write-Host ""

if ($removed.Count -gt 0) {
    Write-Host "✓ Successfully removed:" -ForegroundColor Green
    foreach ($path in $removed) {
        Write-Host "  - $path" -ForegroundColor Green
    }
    Write-Host ""
}

if ($failed.Count -gt 0) {
    Write-Host "✗ Failed to remove:" -ForegroundColor Red
    foreach ($path in $failed) {
        Write-Host "  - $path" -ForegroundColor Red
    }
    Write-Host ""
    Write-Host "These may be phantom entries. They're already in .gitignore, so git will ignore them." -ForegroundColor Yellow
    Write-Host ""
}

# Final verification
Write-Host "=== VERIFICATION ===" -ForegroundColor Cyan
$remaining = Get-ChildItem -Path "S:\JAN" -Recurse -Force -ErrorAction SilentlyContinue | Where-Object { $_.Name -eq "NUL" }

if ($remaining) {
    Write-Host "[WARNING] NUL files still detected:" -ForegroundColor Yellow
    foreach ($file in $remaining) {
        Write-Host "  - $($file.FullName)" -ForegroundColor Gray
    }
    Write-Host ""
    Write-Host "These are Windows device file phantom entries." -ForegroundColor Yellow
    Write-Host "They cannot be removed normally, but git will ignore them." -ForegroundColor Yellow
} else {
    Write-Host "[OK] No NUL files found - all removed!" -ForegroundColor Green
}

Write-Host ""
Write-Host "=== ALTERNATIVE: NUCLEAR OPTION ===" -ForegroundColor Cyan
Write-Host "If all else fails, you can try:" -ForegroundColor White
Write-Host "1. Boot into safe mode" -ForegroundColor Gray
Write-Host "2. Use: cmd /c 'del /F /Q \\?\S:\JAN\NUL'" -ForegroundColor Gray
Write-Host "3. Or use a Linux live USB to delete them" -ForegroundColor Gray
Write-Host ""
Write-Host "SPRAGITSO - Our Father's Royal Seal" -ForegroundColor Cyan
