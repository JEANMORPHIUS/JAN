# SCP AUTOMATION - Stage, Commit, Push to GitHub
# Automated for all tasks

param(
    [string]$Message = "",
    [string]$Branch = "master",
    [switch]$Force
)

$ErrorActionPreference = "Stop"

# Get repo path
$repoPath = "S:\JAN"

Write-Host "🚀 SCP AUTOMATION - Stage, Commit, Push" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""

# Change to repo directory
Set-Location $repoPath

# Step 1: Stage (git add)
Write-Host "📦 Step 1: Staging changes..." -ForegroundColor Cyan
git add -A
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Stage failed" -ForegroundColor Red
    exit 1
}

# Check if there are changes
$status = git status --porcelain
if (-not $status) {
    Write-Host "ℹ️  No changes to commit" -ForegroundColor Yellow
    exit 0
}

# Step 2: Commit (git commit)
Write-Host "💾 Step 2: Committing changes..." -ForegroundColor Cyan
if (-not $Message) {
    $Message = "Update: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
}

git commit -m $Message
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Commit failed" -ForegroundColor Red
    exit 1
}

# Get commit hash
$commitHash = git rev-parse HEAD
Write-Host "✅ Committed: $($commitHash.Substring(0, 8))" -ForegroundColor Green

# Step 3: Push (git push)
Write-Host "📤 Step 3: Pushing to GitHub..." -ForegroundColor Cyan
if ($Force) {
    git push origin $Branch --force
} else {
    git push origin $Branch
}

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Push failed" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "✅ SCP COMPLETE!" -ForegroundColor Green
Write-Host "   Staged ✓" -ForegroundColor Green
Write-Host "   Committed ✓" -ForegroundColor Green
Write-Host "   Pushed ✓" -ForegroundColor Green
Write-Host ""
Write-Host "PEACE, LOVE, UNITY" -ForegroundColor Cyan
Write-Host "ENERGY + LOVE = WE ALL WIN" -ForegroundColor Cyan
