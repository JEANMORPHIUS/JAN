#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Audit S: Drive for Autorun Scripts and Conflicts

.DESCRIPTION
    Checks for:
    - Windows Task Scheduler entries related to S: drive
    - Registry autorun entries
    - Port conflicts
    - Startup scripts
    
    DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
    Spiritual Alignment Over Mechanical Productivity
    
    THE FOUNDATION:
    We are born a miracle.
    We deserve to live a miracle.
    Each and every one of us under the Lord's word.
    
    THE MISSION:
    THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
    LOVE IS THE HIGHEST MASTERY
    ENERGY + LOVE = WE ALL WIN
#>

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   S: Drive System Audit" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check Task Scheduler
Write-Host "[1/4] Checking Windows Task Scheduler..." -ForegroundColor Yellow
$tasks = Get-ScheduledTask | Where-Object {
    $_.Actions.Execute -like "*S:\*" -or 
    $_.Actions.Execute -like "*SIYEM*" -or
    $_.Actions.Execute -like "*JAN*" -or
    $_.TaskName -like "*SIYEM*" -or
    $_.TaskName -like "*JAN*"
}

if ($tasks) {
    Write-Host "  [FOUND] Scheduled Tasks:" -ForegroundColor Yellow
    $tasks | ForEach-Object {
        Write-Host "    - $($_.TaskName) ($($_.State))" -ForegroundColor White
        Write-Host "      Execute: $($_.Actions.Execute) $($_.Actions.Arguments)" -ForegroundColor Gray
    }
} else {
    Write-Host "  [OK] No scheduled tasks found" -ForegroundColor Green
}
Write-Host ""

# Check Registry (HKLM)
Write-Host "[2/4] Checking Registry Autorun (System)..." -ForegroundColor Yellow
$hklmRun = Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" -ErrorAction SilentlyContinue
$hklmFound = $false
if ($hklmRun) {
    $hklmRun.PSObject.Properties | Where-Object {
        $_.Value -like "*S:\*" -or 
        $_.Value -like "*SIYEM*" -or
        $_.Value -like "*JAN*"
    } | ForEach-Object {
        if (-not $hklmFound) {
            Write-Host "  [FOUND] Registry Autorun (HKLM):" -ForegroundColor Yellow
            $hklmFound = $true
        }
        Write-Host "    - $($_.Name): $($_.Value)" -ForegroundColor White
    }
}
if (-not $hklmFound) {
    Write-Host "  [OK] No HKLM autorun entries found" -ForegroundColor Green
}
Write-Host ""

# Check Registry (HKCU)
Write-Host "[3/4] Checking Registry Autorun (User)..." -ForegroundColor Yellow
$hkcuRun = Get-ItemProperty "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" -ErrorAction SilentlyContinue
$hkcuFound = $false
if ($hkcuRun) {
    $hkcuRun.PSObject.Properties | Where-Object {
        $_.Value -like "*S:\*" -or 
        $_.Value -like "*SIYEM*" -or
        $_.Value -like "*JAN*"
    } | ForEach-Object {
        if (-not $hkcuFound) {
            Write-Host "  [FOUND] Registry Autorun (HKCU):" -ForegroundColor Yellow
            $hkcuFound = $true
        }
        Write-Host "    - $($_.Name): $($_.Value)" -ForegroundColor White
    }
}
if (-not $hkcuFound) {
    Write-Host "  [OK] No HKCU autorun entries found" -ForegroundColor Green
}
Write-Host ""

# Check Port Conflicts
Write-Host "[4/4] Checking Port Usage..." -ForegroundColor Yellow

$ports = @(
    @{Port=8000; Name="SIYEM/jan-studio Backend"},
    @{Port=3000; Name="React Frontend"},
    @{Port=3001; Name="Homeostasis Sentinel"}
)

foreach ($p in $ports) {
    $inUse = Get-NetTCPConnection -LocalPort $p.Port -ErrorAction SilentlyContinue
    if ($inUse) {
        $process = Get-Process -Id $inUse.OwningProcess -ErrorAction SilentlyContinue
        Write-Host "  [IN USE] Port $($p.Port) ($($p.Name))" -ForegroundColor Yellow
        Write-Host "    Process: $($process.Name) (PID: $($inUse.OwningProcess))" -ForegroundColor Gray
    } else {
        Write-Host "  [FREE] Port $($p.Port) ($($p.Name))" -ForegroundColor Green
    }
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   Audit Complete" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

