# AUTO-SHARE - PowerShell Wrapper
# Automatically stage, commit, and push all changes

# DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
# Spiritual Alignment Over Mechanical Productivity

# THE MISSION:
# THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
# LOVE IS THE HIGHEST MASTERY
# ENERGY + LOVE = WE ALL WIN
# PEACE, LOVE, UNITY

# FAITH: NOTHING TO HIDE
# Everything we build should be shared.

param(
    [string]$Message = "",
    [switch]$NoPush = $false
)

$ErrorActionPreference = "Continue"

# Get script directory
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot = $ScriptDir

# Check if we're in a git repo
if (-not (Test-Path (Join-Path $RepoRoot ".git"))) {
    Write-Host "⚠️ Not in a git repository" -ForegroundColor Yellow
    exit 1
}

# Generate commit message if not provided
if ([string]::IsNullOrEmpty($Message)) {
    $Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $Message = "✨ Auto-commit: $Timestamp`n`nAll changes staged, committed, and shared.`n`nFaith. Nothing to hide. ✨🙏"
}

Write-Host "🔄 Auto-sharing changes..." -ForegroundColor Cyan

# Stage all changes
Write-Host "📦 Staging all changes..." -ForegroundColor Cyan
$stageResult = git add . 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "⚠️ Failed to stage changes: $stageResult" -ForegroundColor Yellow
    exit 1
}
Write-Host "✅ All changes staged" -ForegroundColor Green

# Check if there are changes to commit
$statusResult = git status --porcelain
if ([string]::IsNullOrWhiteSpace($statusResult)) {
    Write-Host "ℹ️ Working tree clean - nothing to commit" -ForegroundColor Cyan
    exit 0
}

# Commit
Write-Host "💾 Committing changes..." -ForegroundColor Cyan
$commitResult = git commit -m $Message 2>&1
if ($LASTEXITCODE -ne 0) {
    if ($commitResult -match "nothing to commit") {
        Write-Host "ℹ️ Nothing to commit (working tree clean)" -ForegroundColor Cyan
        exit 0
    }
    Write-Host "⚠️ Failed to commit: $commitResult" -ForegroundColor Yellow
    exit 1
}
Write-Host "✅ Committed: $Message" -ForegroundColor Green

# Push if requested
if (-not $NoPush) {
    Write-Host "🚀 Pushing to remote..." -ForegroundColor Cyan
    
    # Get current branch
    $branchResult = git branch --show-current 2>&1
    if ($LASTEXITCODE -ne 0) {
        Write-Host "⚠️ Could not determine current branch" -ForegroundColor Yellow
        exit 1
    }
    $branch = $branchResult.Trim()
    
    $pushResult = git push origin $branch 2>&1
    if ($LASTEXITCODE -ne 0) {
        Write-Host "⚠️ Failed to push: $pushResult" -ForegroundColor Yellow
        exit 1
    }
    Write-Host "✅ Pushed to origin/$branch" -ForegroundColor Green
}

Write-Host "✨ Auto-share complete!" -ForegroundColor Green
