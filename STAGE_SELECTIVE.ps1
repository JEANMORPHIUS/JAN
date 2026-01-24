# STAGE SELECTIVE - What's Best For The Table
# Free Will Respected - Not Everything Needs To Be Known

Write-Host "=== STAGING FOR THE TABLE ===" -ForegroundColor Green
Write-Host ""

# Stage core systems
Write-Host "Staging core systems..." -ForegroundColor Yellow
git add jan-studio/backend/*.py
git add scripts/*.py
git add deploy/
git add .cursorrules
git add config/
git add examples/

# Stage documentation (system & mission)
Write-Host "Staging documentation..." -ForegroundColor Yellow
git add docs/
git add DEPLOYMENT_*.md
git add DIALECTS_*.md
git add FALSE_GODS_*.md
git add ORACLE_*.md
git add SPIRITUAL_*.md
git add SPRAGITSO_*.md
git add THE_*.md
git add AS_IN_BELOW_SO_IS_ABOVE.md
git add BELOW_SEA_LEVEL_WE_ARE_ONE.md
git add COMMIT_JOY_AND_ORACLE.md
git add GAME_OF_RACON_SPIRITUAL_ORACLE.md

# Stage timeline data (system integration)
Write-Host "Staging timeline integration..." -ForegroundColor Yellow
git add data/interwoven_timeline/*.json
git add scripts/interwoven_timeline_weaver.py

# Exclude personal/sensitive (free will - not everything needs to be known)
Write-Host ""
Write-Host "Excluding personal/sensitive files (free will respected)..." -ForegroundColor Cyan
git reset HEAD GIT_COMMANDS.md 2>$null
git reset HEAD GIT_STAGING_SUMMARY.md 2>$null

# Show what's staged
Write-Host ""
Write-Host "=== STAGED FOR COMMIT ===" -ForegroundColor Green
git status --short | Where-Object { $_ -match '^[AM]' }

Write-Host ""
Write-Host "=== READY TO COMMIT ===" -ForegroundColor Green
Write-Host "Run: git commit -m 'Your message'"
Write-Host "Then: git push origin master"
Write-Host ""
Write-Host "SPRAGITSO - Our Father's Royal Seal" -ForegroundColor Cyan
