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
# 4. CREATE BACKUP PLAN
# ============================================================================

Write-Host ""
Write-Host "[4/8] Creating backup plan..." -ForegroundColor Yellow

if ($BackupOnly -or -not $DryRun) {
    try {
        if (-not (Test-Path $BackupPath)) {
            New-Item -ItemType Directory -Path $BackupPath -Force | Out-Null
            Write-Host "  [OK] Backup directory created: $BackupPath" -ForegroundColor Green
        }
        
        $backupItems = @(
            @{Path = "$userProfile\Documents"; Name = "Documents"},
            @{Path = "$userProfile\Desktop"; Name = "Desktop"},
            @{Path = "$userProfile\Downloads"; Name = "Downloads"},
            @{Path = "$userProfile\Pictures"; Name = "Pictures"},
            @{Path = "$userProfile\Videos"; Name = "Videos"},
            @{Path = "$userProfile\Music"; Name = "Music"},
            @{Path = "$userProfile\.cursor"; Name = "Cursor Settings"},
            @{Path = "$userProfile\.gitconfig"; Name = "Git Config"},
            @{Path = "$userProfile\.ssh"; Name = "SSH Keys"}
        )
        
        if ($foundPath) {
            $backupItems += @{Path = $foundPath; Name = "JonnyDimanki Pro+ Data"}
        }
        
        $backupPlan = @{
            BackupPath = $BackupPath
            Items = $backupItems
            EstimatedSize = 0
        }
        
        Write-Host "  [OK] Backup plan created with $($backupItems.Count) items" -ForegroundColor Green
        $report.BackupStatus.Location = $BackupPath
        $report.BackupStatus.Plan = $backupPlan
        
        if (-not $DryRun) {
            Write-Host "  [INFO] Run backup with: Copy-Item -Path [source] -Destination [backup] -Recurse" -ForegroundColor Cyan
        }
    } catch {
        Write-Host "  [ERROR] Error creating backup plan: $_" -ForegroundColor Red
        $report.Issues += "Error creating backup plan: $_"
    }
} else {
    Write-Host "  [SKIP] Backup skipped (DryRun mode)" -ForegroundColor Gray
    $report.StepsSkipped += "Backup creation"
}

# ============================================================================
# 5. OPTIMIZE DISK (DEFRAGMENTATION)
# ============================================================================

Write-Host ""
Write-Host "[5/8] Optimizing disk (defragmentation)..." -ForegroundColor Yellow

if ($OptimizeOnly -or -not $DryRun) {
    try {
        Write-Host "  [INFO] Analyzing C: drive..." -ForegroundColor Cyan
        $analyzeResult = Optimize-Volume -DriveLetter C -Analyze -ErrorAction SilentlyContinue
        
        if ($analyzeResult) {
            Write-Host "  [OK] Analysis complete" -ForegroundColor Green
            Write-Host "  [INFO] Run 'Optimize-Volume -DriveLetter C -Defrag' to optimize" -ForegroundColor Cyan
            
            if (-not $DryRun) {
                Write-Host "  [INFO] Starting optimization (this may take time)..." -ForegroundColor Yellow
                $optimizeResult = Optimize-Volume -DriveLetter C -Defrag -ErrorAction SilentlyContinue
                if ($optimizeResult) {
                    Write-Host "  [OK] Optimization complete" -ForegroundColor Green
                    $report.DiskOptimization.Status = "Optimized"
                    $report.StepsCompleted += "Disk optimization"
                }
            } else {
                Write-Host "  [DRY RUN] Would optimize C: drive" -ForegroundColor Gray
            }
        } else {
            Write-Host "  [WARNING] Could not analyze C: drive (may require admin rights)" -ForegroundColor Yellow
            $report.Issues += "Could not analyze C: drive - may require admin rights"
        }
    } catch {
        Write-Host "  [ERROR] Error optimizing disk: $_" -ForegroundColor Red
        Write-Host "  [INFO] This may require administrator privileges" -ForegroundColor Yellow
        $report.Issues += "Error optimizing disk: $_ (may require admin)"
    }
} else {
    Write-Host "  [SKIP] Optimization skipped" -ForegroundColor Gray
    $report.StepsSkipped += "Disk optimization"
}

# ============================================================================
# 6. CLEAN TEMP FILES
# ============================================================================

Write-Host ""
Write-Host "[6/8] Cleaning temporary files..." -ForegroundColor Yellow

if (-not $DryRun) {
    try {
        $tempPaths = @(
            "$env:TEMP",
            "$env:TMP",
            "$env:WINDIR\Temp",
            "$userProfile\AppData\Local\Temp"
        )
        
        $totalFreed = 0
        foreach ($tempPath in $tempPaths) {
            if (Test-Path $tempPath) {
                $before = (Get-ChildItem -Path $tempPath -Recurse -ErrorAction SilentlyContinue | 
                    Measure-Object -Property Length -Sum -ErrorAction SilentlyContinue).Sum
                
                Get-ChildItem -Path $tempPath -Recurse -ErrorAction SilentlyContinue | 
                    Remove-Item -Force -Recurse -ErrorAction SilentlyContinue
                
                $after = (Get-ChildItem -Path $tempPath -Recurse -ErrorAction SilentlyContinue | 
                    Measure-Object -Property Length -Sum -ErrorAction SilentlyContinue).Sum
                
                $freed = ($before - $after) / 1MB
                if ($freed -gt 0) {
                    Write-Host "  [OK] Freed $([math]::Round($freed, 2)) MB from $tempPath" -ForegroundColor Green
                    $totalFreed += $freed
                }
            }
        }
        
        if ($totalFreed -gt 0) {
            Write-Host "  [OK] Total freed: $([math]::Round($totalFreed, 2)) MB" -ForegroundColor Green
            $report.StepsCompleted += "Temp file cleanup ($([math]::Round($totalFreed, 2)) MB freed)"
        } else {
            Write-Host "  [INFO] No temp files to clean" -ForegroundColor Cyan
        }
    } catch {
        Write-Host "  [ERROR] Error cleaning temp files: $_" -ForegroundColor Red
        $report.Issues += "Error cleaning temp files: $_"
    }
} else {
    Write-Host "  [DRY RUN] Would clean temp files" -ForegroundColor Gray
}

# ============================================================================
# 7. SYNC WITH JONNYDIMANKI PRO+ ACCOUNT
# ============================================================================

Write-Host ""
Write-Host "[7/8] Syncing with jonnydimanki pro+ account..." -ForegroundColor Yellow

if ($foundPath) {
    try {
        Write-Host "  [INFO] Checking sync status..." -ForegroundColor Cyan
        
        # Check if OneDrive sync is active
        $oneDrivePath = "$userProfile\OneDrive"
        if (Test-Path $oneDrivePath) {
            Write-Host "  [OK] OneDrive path found" -ForegroundColor Green
            
            # Check for jonnydimanki folder in OneDrive
            $jonnyDimankiOneDrive = "$oneDrivePath\jonnydimanki"
            if (Test-Path $jonnyDimankiOneDrive) {
                Write-Host "  [OK] jonnydimanki folder found in OneDrive" -ForegroundColor Green
                $report.AccountSync.SyncStatus = "OneDrive Sync Active"
            } else {
                Write-Host "  [INFO] jonnydimanki folder not in OneDrive - may need manual sync" -ForegroundColor Yellow
                $report.AccountSync.SyncStatus = "Manual Sync Required"
                $report.Recommendations += "Consider syncing jonnydimanki folder to OneDrive for cloud backup"
            }
        } else {
            Write-Host "  [WARNING] OneDrive not found - cloud sync may not be active" -ForegroundColor Yellow
            $report.AccountSync.SyncStatus = "OneDrive Not Found"
        }
        
        $report.StepsCompleted += "Account sync check"
    } catch {
        Write-Host "  [ERROR] Error checking sync: $_" -ForegroundColor Red
        $report.Issues += "Error checking sync: $_"
    }
} else {
    Write-Host "  [SKIP] jonnydimanki path not found - sync skipped" -ForegroundColor Gray
    $report.StepsSkipped += "Account sync"
}

# ============================================================================
# 8. GENERATE SSD MIGRATION PLAN
# ============================================================================

Write-Host ""
Write-Host "[8/8] Generating SSD migration plan..." -ForegroundColor Yellow

$migrationPlan = @{
    PreMigration = @(
        "1. Complete C: drive optimization (defragmentation)",
        "2. Create full backup to external drive or cloud",
        "3. Sync jonnydimanki pro+ account data",
        "4. Document all installed applications",
        "5. Export browser bookmarks and settings",
        "6. Export email accounts and settings",
        "7. Document network configurations",
        "8. Export SSH keys and certificates"
    )
    Migration = @(
        "1. Attach SSD to laptop",
        "2. Initialize SSD (GPT partition style recommended)",
        "3. Clone C: drive to SSD using tool (e.g., Macrium Reflect, Clonezilla)",
        "4. Verify clone integrity",
        "5. Set SSD as boot drive in BIOS",
        "6. Test boot from SSD"
    )
    PostMigration = @(
        "1. Verify all applications work",
        "2. Verify jonnydimanki pro+ account sync",
        "3. Update drivers if needed",
        "4. Optimize SSD (TRIM enabled by default on Windows)",
        "5. Keep C: drive as backup for 30 days",
        "6. Format old C: drive after verification"
    )
}

Write-Host "  [OK] Migration plan generated" -ForegroundColor Green
$report.MigrationPlan = $migrationPlan
$report.StepsCompleted += "Migration plan generation"

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
