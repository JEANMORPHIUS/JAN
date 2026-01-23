# C: DRIVE CLEANUP AND OPTIMIZATION
# Review, Clean, and Optimize C: Drive Scripts
#
# DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
# Spiritual Alignment Over Mechanical Productivity
#
# THE MISSION:
# - Review C: drive scripts for residue
# - Remove what we don't need
# - Optimize what we have
# - Build on what works
#
# PEACE, LOVE, UNITY

param(
    [switch]$DryRun,
    [switch]$UpdateNavigationScripts,
    [switch]$RemoveDenyScripts
)

$ErrorActionPreference = "Continue"
$userProfile = $env:USERPROFILE
$report = @{
    Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    ScriptsFound = @()
    ScriptsUpdated = @()
    ScriptsRemoved = @()
    Recommendations = @()
    Issues = @()
}

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   C: DRIVE SCRIPT CLEANUP & OPTIMIZE" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# ============================================================================
# 1. REVIEW USER SCRIPTS
# ============================================================================

Write-Host "[1/5] Reviewing User Scripts..." -ForegroundColor Yellow

$userScripts = @(
    @{Path = "$userProfile\cd_core.ps1"; Type = "Navigation"; Status = "Review"}
    @{Path = "$userProfile\cd_prod.ps1"; Type = "Navigation"; Status = "Review"}
    @{Path = "$userProfile\cd_pub.ps1"; Type = "Navigation"; Status = "Review"}
    @{Path = "$userProfile\OneDrive\Documents\Microsoft.PowerShell_profile.ps1"; Type = "Profile"; Status = "Review"}
)

foreach ($script in $userScripts) {
    if (Test-Path $script.Path) {
        $file = Get-Item $script.Path
        $scriptInfo = @{
            Path = $script.Path
            Type = $script.Type
            Size = $file.Length
            LastModified = $file.LastWriteTime
            Content = Get-Content $script.Path -Raw -ErrorAction SilentlyContinue
        }
        
        $report.ScriptsFound += $scriptInfo
        
        Write-Host "  [FOUND] $($script.Path)" -ForegroundColor Green
        Write-Host "    Type: $($script.Type)" -ForegroundColor Gray
        Write-Host "    Size: $($scriptInfo.Size) bytes" -ForegroundColor Gray
        Write-Host "    Modified: $($scriptInfo.LastModified)" -ForegroundColor Gray
        
        # Check for D: drive references
        if ($scriptInfo.Content -match "D:\\SIYEM") {
            Write-Host "    [ISSUE] References D:\SIYEM (should be S:\SIYEM?)" -ForegroundColor Yellow
            $report.Issues += @{
                Script = $script.Path
                Issue = "References D:\SIYEM instead of S:\SIYEM"
                Recommendation = "Update to S:\SIYEM for consistency"
            }
        }
    } else {
        Write-Host "  [NOT FOUND] $($script.Path)" -ForegroundColor DarkGray
    }
}

Write-Host ""

# ============================================================================
# 2. REVIEW DENY SCRIPTS
# ============================================================================

Write-Host "[2/5] Reviewing Deny Scripts..." -ForegroundColor Yellow

$denyScripts = @(
    "$userProfile\.sbx-denybin\scp.bat"
    "$userProfile\.sbx-denybin\ssh.bat"
)

foreach ($scriptPath in $denyScripts) {
    if (Test-Path $scriptPath) {
        $file = Get-Item $scriptPath
        $content = Get-Content $scriptPath -Raw
        
        Write-Host "  [FOUND] $scriptPath" -ForegroundColor Green
        Write-Host "    Content: $($content.Trim())" -ForegroundColor Gray
        
        if ($content -match "exit /b 1") {
            Write-Host "    [INFO] Deny script (intentional block)" -ForegroundColor Cyan
            $report.Recommendations += @{
                Action = "Review"
                Script = $scriptPath
                Reason = "Deny script - verify if still needed for security"
            }
        }
    }
}

Write-Host ""

# ============================================================================
# 3. UPDATE NAVIGATION SCRIPTS (if requested)
# ============================================================================

if ($UpdateNavigationScripts) {
    Write-Host "[3/5] Updating Navigation Scripts..." -ForegroundColor Yellow
    
    $navigationUpdates = @{
        "$userProfile\cd_core.ps1" = "Set-Location S:\SIYEM\00_CORE"
        "$userProfile\cd_prod.ps1" = "Set-Location S:\SIYEM\03_PRODUCTION"
        "$userProfile\cd_pub.ps1" = "Set-Location S:\SIYEM\05_PUBLISHING"
    }
    
    foreach ($scriptPath in $navigationUpdates.Keys) {
        if (Test-Path $scriptPath) {
            $newContent = $navigationUpdates[$scriptPath]
            
            if ($DryRun) {
                Write-Host "  [DRY RUN] Would update: $scriptPath" -ForegroundColor Cyan
                Write-Host "    New content: $newContent" -ForegroundColor Gray
            } else {
                try {
                    Set-Content -Path $scriptPath -Value $newContent -Encoding UTF8
                    Write-Host "  [UPDATED] $scriptPath" -ForegroundColor Green
                    $report.ScriptsUpdated += @{
                        Path = $scriptPath
                        Action = "Updated to S:\SIYEM"
                        NewContent = $newContent
                    }
                } catch {
                    Write-Host "  [ERROR] Failed to update $scriptPath : $_" -ForegroundColor Red
                    $report.Issues += @{
                        Script = $scriptPath
                        Issue = "Failed to update"
                        Error = $_.Exception.Message
                    }
                }
            }
        }
    }
} else {
    Write-Host "[3/5] Skipping Navigation Script Updates (use -UpdateNavigationScripts to enable)" -ForegroundColor DarkGray
}

Write-Host ""

# ============================================================================
# 4. REMOVE DENY SCRIPTS (if requested)
# ============================================================================

if ($RemoveDenyScripts) {
    Write-Host "[4/5] Removing Deny Scripts..." -ForegroundColor Yellow
    
    foreach ($scriptPath in $denyScripts) {
        if (Test-Path $scriptPath) {
            if ($DryRun) {
                Write-Host "  [DRY RUN] Would remove: $scriptPath" -ForegroundColor Cyan
            } else {
                try {
                    Remove-Item -Path $scriptPath -Force
                    Write-Host "  [REMOVED] $scriptPath" -ForegroundColor Green
                    $report.ScriptsRemoved += @{
                        Path = $scriptPath
                        Reason = "Deny script - removed as requested"
                    }
                } catch {
                    Write-Host "  [ERROR] Failed to remove $scriptPath : $_" -ForegroundColor Red
                    $report.Issues += @{
                        Script = $scriptPath
                        Issue = "Failed to remove"
                        Error = $_.Exception.Message
                    }
                }
            }
        }
    }
} else {
    Write-Host "[4/5] Skipping Deny Script Removal (use -RemoveDenyScripts to enable)" -ForegroundColor DarkGray
}

Write-Host ""

# ============================================================================
# 5. SCAN FOR OTHER RESIDUE
# ============================================================================

Write-Host "[5/5] Scanning for Other Residue..." -ForegroundColor Yellow

# Check for temp scripts
$tempPatterns = @("*.tmp", "*.bak", "*.old", "*~")
$tempScripts = @()

foreach ($pattern in $tempPatterns) {
    $found = Get-ChildItem -Path $userProfile -Filter "*$pattern" -Recurse -Depth 2 -ErrorAction SilentlyContinue | 
             Where-Object { $_.Extension -in @('.ps1', '.bat', '.sh', '.py') }
    $tempScripts += $found
}

if ($tempScripts) {
    Write-Host "  [FOUND] Temporary script files:" -ForegroundColor Yellow
    foreach ($temp in $tempScripts) {
        Write-Host "    - $($temp.FullName)" -ForegroundColor Gray
        $report.Recommendations += @{
            Action = "Review/Remove"
            Script = $temp.FullName
            Reason = "Temporary script file"
        }
    }
} else {
    Write-Host "  [OK] No temporary script files found" -ForegroundColor Green
}

# Check for orphaned scripts (scripts that reference non-existent paths)
Write-Host "  Checking for orphaned scripts..." -ForegroundColor Gray
foreach ($scriptInfo in $report.ScriptsFound) {
    if ($scriptInfo.Content) {
        # Check for path references
        if ($scriptInfo.Content -match "Set-Location\s+['`"]?([^'`"]+)['`"]?") {
            $referencedPath = $matches[1]
            if (-not (Test-Path $referencedPath)) {
                Write-Host "    [ORPHANED] $($scriptInfo.Path) references non-existent: $referencedPath" -ForegroundColor Yellow
                $report.Issues += @{
                    Script = $scriptInfo.Path
                    Issue = "References non-existent path"
                    Path = $referencedPath
                }
            }
        }
    }
}

Write-Host ""

# ============================================================================
# SUMMARY REPORT
# ============================================================================

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   SUMMARY REPORT" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "Scripts Found: $($report.ScriptsFound.Count)" -ForegroundColor Cyan
Write-Host "Scripts Updated: $($report.ScriptsUpdated.Count)" -ForegroundColor $(if ($report.ScriptsUpdated.Count -gt 0) { "Green" } else { "Gray" })
Write-Host "Scripts Removed: $($report.ScriptsRemoved.Count)" -ForegroundColor $(if ($report.ScriptsRemoved.Count -gt 0) { "Green" } else { "Gray" })
Write-Host "Issues Found: $($report.Issues.Count)" -ForegroundColor $(if ($report.Issues.Count -gt 0) { "Yellow" } else { "Green" })
Write-Host "Recommendations: $($report.Recommendations.Count)" -ForegroundColor Cyan

if ($report.Issues.Count -gt 0) {
    Write-Host ""
    Write-Host "ISSUES:" -ForegroundColor Yellow
    foreach ($issue in $report.Issues) {
        Write-Host "  - $($issue.Script): $($issue.Issue)" -ForegroundColor Yellow
    }
}

if ($report.Recommendations.Count -gt 0) {
    Write-Host ""
    Write-Host "RECOMMENDATIONS:" -ForegroundColor Cyan
    foreach ($rec in $report.Recommendations) {
        Write-Host "  [$($rec.Action)] $($rec.Script)" -ForegroundColor Cyan
        Write-Host "    Reason: $($rec.Reason)" -ForegroundColor Gray
    }
}

# Save report
$reportPath = "S:\JAN\output\c_drive_cleanup_report_$(Get-Date -Format 'yyyyMMdd_HHmmss').json"
$reportDir = Split-Path $reportPath -Parent
if (-not (Test-Path $reportDir)) {
    New-Item -ItemType Directory -Path $reportDir -Force | Out-Null
}

$report | ConvertTo-Json -Depth 10 | Set-Content -Path $reportPath
Write-Host ""
Write-Host "Full report saved to: $reportPath" -ForegroundColor Green

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
if ($DryRun) {
    Write-Host "   DRY RUN COMPLETE" -ForegroundColor Cyan
    Write-Host "   Run without -DryRun to apply changes" -ForegroundColor Yellow
} else {
    Write-Host "   CLEANUP COMPLETE" -ForegroundColor Cyan
}
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "PEACE, LOVE, UNITY" -ForegroundColor Green
Write-Host "ENERGY + LOVE = WE ALL WIN" -ForegroundColor Green
