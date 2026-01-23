# C: DRIVE SSD ALIGNMENT & PREPARATION
# Simplified script - runnable from S: drive
# Align laptop from C: drive local prior to attaching SSD
# Linked to jonnydimanki pro+ account
#
# DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
# Spiritual Alignment Over Mechanical Productivity
#
# THE MISSION:
# - Check C: drive alignment
# - Detect jonnydimanki pro+ account
# - Generate migration plan
#
# PEACE, LOVE, UNITY

param(
    [switch]$DryRun
)

$ErrorActionPreference = "Continue"
$userProfile = $env:USERPROFILE
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$outputDir = Join-Path $scriptDir "..\output"
if (-not (Test-Path $outputDir)) { New-Item -ItemType Directory -Path $outputDir -Force | Out-Null }

$report = @{
    Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Phase = "C: Drive SSD Alignment"
    JonnyDimankiPath = ""
    DiskInfo = @{}
    MigrationPlan = @()
}

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   C: DRIVE SSD ALIGNMENT & PREP" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# ============================================================================
# 1. DETECT JONNYDIMANKI PRO+ ACCOUNT
# ============================================================================

Write-Host "[1/3] Detecting jonnydimanki pro+ account..." -ForegroundColor Yellow

$jonnyDimankiPaths = @(
    "$userProfile\OneDrive\jonnydimanki",
    "$userProfile\Documents\jonnydimanki",
    "$userProfile\Desktop\jonnydimanki",
    "C:\jonnydimanki"
)

$foundPath = $null
foreach ($path in $jonnyDimankiPaths) {
    if (Test-Path $path) {
        $foundPath = $path
        Write-Host "  [OK] Found: $path" -ForegroundColor Green
        $report.JonnyDimankiPath = $path
        break
    }
}

if (-not $foundPath) {
    Write-Host "  [INFO] jonnydimanki path not found (will need manual setup)" -ForegroundColor Yellow
}

# ============================================================================
# 2. CHECK C: DRIVE INFO
# ============================================================================

Write-Host ""
Write-Host "[2/3] Checking C: drive..." -ForegroundColor Yellow

try {
    $disk = Get-Disk | Where-Object { $_.Number -eq 0 } -ErrorAction SilentlyContinue
    $volume = Get-Volume -DriveLetter C -ErrorAction SilentlyContinue
    
    if ($disk) {
        Write-Host "  [OK] Disk: $($disk.Model)" -ForegroundColor Green
        Write-Host "  Partition: $($disk.PartitionStyle)" -ForegroundColor Cyan
        Write-Host "  Size: $([math]::Round($disk.Size / 1GB, 2)) GB" -ForegroundColor Cyan
        
        $report.DiskInfo = @{
            Model = $disk.Model
            PartitionStyle = $disk.PartitionStyle
            SizeGB = [math]::Round($disk.Size / 1GB, 2)
            FileSystem = if ($volume) { $volume.FileSystemType } else { "Unknown" }
            Health = if ($volume) { $volume.HealthStatus } else { "Unknown" }
        }
    } else {
        Write-Host "  [WARNING] Could not detect disk (may need admin)" -ForegroundColor Yellow
    }
} catch {
    Write-Host "  [INFO] Disk check skipped: $_" -ForegroundColor Yellow
}

# ============================================================================
# 3. GENERATE SSD MIGRATION PLAN
# ============================================================================

Write-Host ""
Write-Host "[3/3] Generating SSD migration plan..." -ForegroundColor Yellow

$report.MigrationPlan = @(
    "PRE-MIGRATION:",
    "  1. Run: Optimize-Volume -DriveLetter C -Defrag (admin required)",
    "  2. Backup critical folders to external drive",
    "  3. Sync jonnydimanki pro+ account to OneDrive/cloud",
    "  4. Export browser bookmarks, email accounts, SSH keys",
    "",
    "MIGRATION:",
    "  1. Attach SSD to laptop",
    "  2. Initialize SSD (GPT partition style)",
    "  3. Clone C: drive using Macrium Reflect or Clonezilla",
    "  4. Set SSD as boot drive in BIOS",
    "  5. Test boot from SSD",
    "",
    "POST-MIGRATION:",
    "  1. Verify all applications work",
    "  2. Verify jonnydimanki pro+ sync",
    "  3. Keep old C: drive as backup (30 days)",
    "  4. Format old C: drive after verification"
)

Write-Host "  [OK] Migration plan generated" -ForegroundColor Green

# ============================================================================
# GENERATE REPORT
# ============================================================================

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   ALIGNMENT COMPLETE" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$reportPath = Join-Path $outputDir "C_Drive_SSD_Alignment_Report_$(Get-Date -Format 'yyyyMMdd_HHmmss').json"
$report | ConvertTo-Json -Depth 10 | Out-File -FilePath $reportPath -Encoding UTF8

Write-Host "Report saved to: $reportPath" -ForegroundColor Green
Write-Host ""
Write-Host "JonnyDimanki Path: $($report.JonnyDimankiPath)" -ForegroundColor Cyan
if ($report.DiskInfo.Count -gt 0) {
    Write-Host "Disk: $($report.DiskInfo.Model) - $($report.DiskInfo.SizeGB) GB" -ForegroundColor Cyan
}
Write-Host ""
Write-Host "Migration Plan:" -ForegroundColor Yellow
$report.MigrationPlan | ForEach-Object { Write-Host "  $_" -ForegroundColor White }
Write-Host ""
Write-Host "PEACE, LOVE, UNITY" -ForegroundColor Green
Write-Host "ENERGY + LOVE = WE ALL WIN" -ForegroundColor Green
