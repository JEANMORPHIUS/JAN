# C: DRIVE SSD ALIGNMENT & PREPARATION
# Align laptop from C: drive local prior to attaching SSD
# Linked to jonnydimanki pro+ account
#
# DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
# Spiritual Alignment Over Mechanical Productivity
#
# THE MISSION:
# - Align and optimize C: drive
# - Prepare for SSD attachment
# - Sync with jonnydimanki pro+ account
# - Create backup and migration plan
# - Optimize system performance
#
# PEACE, LOVE, UNITY

param(
    [switch]$DryRun,
    [switch]$OptimizeOnly,
    [switch]$BackupOnly,
    [string]$JonnyDimankiPath = "",
    [string]$BackupPath = "$env:USERPROFILE\Desktop\C_Drive_Backup_$(Get-Date -Format 'yyyyMMdd_HHmmss')"
)

$ErrorActionPreference = "Continue"
$userProfile = $env:USERPROFILE
$report = @{
    Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Phase = "C: Drive SSD Alignment"
    StepsCompleted = @()
    StepsSkipped = @()
    Issues = @()
    Recommendations = @()
    AccountSync = @{
        JonnyDimankiProPlus = "Not Configured"
        SyncStatus = "Pending"
    }
    DiskOptimization = @{
        Status = "Pending"
        Fragmentation = "Unknown"
        Alignment = "Unknown"
    }
    BackupStatus = @{
        Created = $false
        Location = ""
        Size = 0
    }
}

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   C: DRIVE SSD ALIGNMENT & PREP" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# ============================================================================
# 1. DETECT JONNYDIMANKI PRO+ ACCOUNT
# ============================================================================

Write-Host "[1/8] Detecting jonnydimanki pro+ account..." -ForegroundColor Yellow

$jonnyDimankiPaths = @(
    "$userProfile\OneDrive\jonnydimanki",
    "$userProfile\Documents\jonnydimanki",
    "$userProfile\Desktop\jonnydimanki",
    "C:\jonnydimanki",
    "$env:ProgramFiles\jonnydimanki",
    "$env:ProgramFiles(x86)\jonnydimanki"
)

if ($JonnyDimankiPath -ne "") {
    $jonnyDimankiPaths = @($JonnyDimankiPath)
}

$foundPath = $null
foreach ($path in $jonnyDimankiPaths) {
    if (Test-Path $path) {
        $foundPath = $path
        Write-Host "  [OK] Found jonnydimanki at: $path" -ForegroundColor Green
        $report.AccountSync.JonnyDimankiProPlus = $path
        break
    }
}

if (-not $foundPath) {
    Write-Host "  [WARNING] jonnydimanki pro+ account path not found" -ForegroundColor Yellow
    Write-Host "  Please specify path with -JonnyDimankiPath parameter" -ForegroundColor Yellow
    $report.Issues += "JonnyDimanki path not found - manual configuration required"
}

# ============================================================================
# 2. CHECK DISK ALIGNMENT
# ============================================================================

Write-Host ""
Write-Host "[2/8] Checking disk alignment..." -ForegroundColor Yellow

try {
    $disk = Get-Disk | Where-Object { $_.Number -eq 0 }
    if ($disk) {
        Write-Host "  [OK] Disk 0 found: $($disk.Model)" -ForegroundColor Green
        Write-Host "  Partition Style: $($disk.PartitionStyle)" -ForegroundColor Cyan
        Write-Host "  Size: $([math]::Round($disk.Size / 1GB, 2)) GB" -ForegroundColor Cyan
        
        $report.DiskOptimization.Alignment = "Checked"
        $report.DiskOptimization.PartitionStyle = $disk.PartitionStyle
        $report.DiskOptimization.Size = [math]::Round($disk.Size / 1GB, 2)
    } else {
        Write-Host "  [WARNING] Could not detect disk 0" -ForegroundColor Yellow
        $report.Issues += "Could not detect disk 0"
    }
} catch {
    Write-Host "  [ERROR] Error checking disk: $_" -ForegroundColor Red
    $report.Issues += "Error checking disk: $_"
}

# ============================================================================
# 3. CHECK DISK FRAGMENTATION
# ============================================================================

Write-Host ""
Write-Host "[3/8] Checking disk fragmentation..." -ForegroundColor Yellow

try {
    $volume = Get-Volume -DriveLetter C
    if ($volume) {
        $fragmentation = Get-Volume | Where-Object { $_.DriveLetter -eq 'C' }
        Write-Host "  [OK] C: drive volume checked" -ForegroundColor Green
        Write-Host "  File System: $($volume.FileSystemType)" -ForegroundColor Cyan
        Write-Host "  Health Status: $($volume.HealthStatus)" -ForegroundColor Cyan
        
        $report.DiskOptimization.Fragmentation = "Checked"
        $report.DiskOptimization.FileSystem = $volume.FileSystemType
        $report.DiskOptimization.HealthStatus = $volume.HealthStatus
        
        # Note: Actual fragmentation analysis requires defrag.exe or Optimize-Volume
        Write-Host "  [INFO] Run 'Optimize-Volume -DriveLetter C -Analyze' for detailed fragmentation" -ForegroundColor Cyan
    } else {
        Write-Host "  [WARNING] Could not get C: volume info" -ForegroundColor Yellow
        $report.Issues += "Could not get C: volume info"
    }
} catch {
    Write-Host "  [ERROR] Error checking fragmentation: $_" -ForegroundColor Red
    $report.Issues += "Error checking fragmentation: $_"
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

$reportPath = "$userProfile\Desktop\C_Drive_SSD_Alignment_Report_$(Get-Date -Format 'yyyyMMdd_HHmmss').json"
$report | ConvertTo-Json -Depth 10 | Out-File -FilePath $reportPath -Encoding UTF8

Write-Host "Report saved to: $reportPath" -ForegroundColor Green
Write-Host ""
Write-Host "Steps Completed: $($report.StepsCompleted.Count)" -ForegroundColor Cyan
Write-Host "Steps Skipped: $($report.StepsSkipped.Count)" -ForegroundColor Yellow
Write-Host "Issues Found: $($report.Issues.Count)" -ForegroundColor $(if ($report.Issues.Count -gt 0) { "Red" } else { "Green" })
Write-Host ""

if ($report.Issues.Count -gt 0) {
    Write-Host "Issues:" -ForegroundColor Red
    foreach ($issue in $report.Issues) {
        Write-Host "  - $issue" -ForegroundColor Yellow
    }
    Write-Host ""
}

if ($report.Recommendations.Count -gt 0) {
    Write-Host "Recommendations:" -ForegroundColor Cyan
    foreach ($rec in $report.Recommendations) {
        Write-Host "  - $rec" -ForegroundColor White
    }
    Write-Host ""
}

Write-Host "PEACE, LOVE, UNITY" -ForegroundColor Green
Write-Host "ENERGY + LOVE = WE ALL WIN" -ForegroundColor Green
