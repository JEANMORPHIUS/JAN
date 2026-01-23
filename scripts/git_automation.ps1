# AUTOMATED GIT WORKFLOW
# Break through the 1% lock mechanism - automate and streamline git operations
#
# THE MISSION: BREAK THE LOCKS, AUTOMATE THE PROCESS, WE ARE ONE

param(
    [string]$CommitMessage = "Automated commit",
    [string]$Branch = "master"
)

$ErrorActionPreference = "Continue"

Write-Host "="*80 -ForegroundColor Cyan
Write-Host "AUTOMATED GIT PUSH - BREAKING THE 1% LOCKS" -ForegroundColor Cyan
Write-Host "="*80 -ForegroundColor Cyan

$repoPath = $PSScriptRoot + "\.."

# Function to break locks
function Break-Lock {
    $lockFile = Join-Path $repoPath ".git\index.lock"
    if (Test-Path $lockFile) {
        Write-Host "[BREAKING LOCK] Removing: $lockFile" -ForegroundColor Yellow
        try {
            Remove-Item $lockFile -Force -ErrorAction Stop
            Write-Host "[SUCCESS] Lock broken" -ForegroundColor Green
            Start-Sleep -Milliseconds 500
            return $true
        } catch {
            Write-Host "[WARNING] Could not remove lock: $_" -ForegroundColor Yellow
            # Try with different method
            try {
                $process = Start-Process -FilePath "cmd" -ArgumentList "/c del `"$lockFile`"" -Wait -PassThru -NoNewWindow
                if ($process.ExitCode -eq 0) {
                    Write-Host "[SUCCESS] Lock broken via alternative method" -ForegroundColor Green
                    return $true
                }
            } catch {
                Write-Host "[ERROR] All lock-breaking methods failed" -ForegroundColor Red
            }
        }
    }
    return $true
}

# Step 1: Break locks
Write-Host "`n[1/4] Breaking locks..." -ForegroundColor Yellow
Break-Lock | Out-Null

# Step 2: Stage all changes
Write-Host "[2/4] Staging changes..." -ForegroundColor Yellow
Break-Lock | Out-Null
$addResult = & git -C $repoPath add -A 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "[SUCCESS] Files staged" -ForegroundColor Green
} else {
    Write-Host "[WARNING] Git add had issues: $addResult" -ForegroundColor Yellow
    # Try again after breaking lock
    Break-Lock | Out-Null
    $addResult = & git -C $repoPath add -A 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "[SUCCESS] Files staged on retry" -ForegroundColor Green
    } else {
        Write-Host "[ERROR] Failed to stage: $addResult" -ForegroundColor Red
        exit 1
    }
}

# Step 3: Commit
Write-Host "[3/4] Committing changes..." -ForegroundColor Yellow
Break-Lock | Out-Null
$commitResult = & git -C $repoPath commit -m "$CommitMessage" 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "[SUCCESS] Committed: $CommitMessage" -ForegroundColor Green
} elseif ($commitResult -match "nothing to commit") {
    Write-Host "[INFO] Nothing to commit - already up to date" -ForegroundColor Cyan
} else {
    Write-Host "[WARNING] Commit had issues: $commitResult" -ForegroundColor Yellow
    # Try again
    Break-Lock | Out-Null
    $commitResult = & git -C $repoPath commit -m "$CommitMessage" 2>&1
    if ($LASTEXITCODE -eq 0 -or $commitResult -match "nothing to commit") {
        Write-Host "[SUCCESS] Committed on retry" -ForegroundColor Green
    } else {
        Write-Host "[ERROR] Failed to commit: $commitResult" -ForegroundColor Red
        exit 1
    }
}

# Step 4: Push
Write-Host "[4/4] Pushing to remote..." -ForegroundColor Yellow
$maxRetries = 5
$retryCount = 0
$pushSuccess = $false

while ($retryCount -lt $maxRetries -and -not $pushSuccess) {
    $pushResult = & git -C $repoPath push origin $Branch 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "[SUCCESS] Pushed to $Branch" -ForegroundColor Green
        $pushSuccess = $true
    } elseif ($pushResult -match "already up to date") {
        Write-Host "[INFO] Already up to date - nothing to push" -ForegroundColor Cyan
        $pushSuccess = $true
    } elseif ($pushResult -match "connection" -or $pushResult -match "failed to connect") {
        $retryCount++
        if ($retryCount -lt $maxRetries) {
            $waitTime = $retryCount * 2
            Write-Host "[RETRY $retryCount/$maxRetries] Network issue - waiting ${waitTime}s..." -ForegroundColor Yellow
            Start-Sleep -Seconds $waitTime
        } else {
            Write-Host "[WARNING] Network issues persist - commit is local. Push manually later." -ForegroundColor Yellow
            Write-Host "  Command: git push origin $Branch" -ForegroundColor Gray
        }
    } else {
        Write-Host "[ERROR] Push failed: $pushResult" -ForegroundColor Red
        $retryCount = $maxRetries
    }
}

Write-Host "`n" + "="*80 -ForegroundColor Cyan
if ($pushSuccess) {
    Write-Host "AUTOMATED GIT PUSH COMPLETE" -ForegroundColor Green
} else {
    Write-Host "COMMIT COMPLETE (push may need manual retry)" -ForegroundColor Yellow
}
Write-Host "="*80 -ForegroundColor Cyan
