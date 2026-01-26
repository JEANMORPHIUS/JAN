# Deploy New Systems via SCP
# Cloud Seeding, Weaponization, Peace Weaponization Systems

# Configuration
$server = "user@host"  # CHANGE THIS
$remotePath = "/path/to/jan-studio"  # CHANGE THIS
$localPath = "S:\JAN"

Write-Host "🚀 Deploying New Systems via SCP" -ForegroundColor Green
Write-Host "=================================" -ForegroundColor Green
Write-Host ""

# Check if SCP is available
$scpAvailable = Get-Command scp -ErrorAction SilentlyContinue
if (-not $scpAvailable) {
    Write-Host "❌ SCP not found. Installing OpenSSH..." -ForegroundColor Yellow
    Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0
    Write-Host "✅ OpenSSH installed. Please restart terminal and run again." -ForegroundColor Green
    exit
}

Write-Host "📦 Deploying Scripts..." -ForegroundColor Cyan
# Deploy analysis scripts
scp "$localPath\scripts\cloud_seeding_analysis.py" "${server}:${remotePath}/scripts/"
scp "$localPath\scripts\weaponization_analysis.py" "${server}:${remotePath}/scripts/"
scp "$localPath\scripts\peace_weaponization_system.py" "${server}:${remotePath}/scripts/"

Write-Host "📡 Deploying APIs..." -ForegroundColor Cyan
# Deploy API files
scp "$localPath\jan-studio\backend\cloud_seeding_api.py" "${server}:${remotePath}/backend/"
scp "$localPath\jan-studio\backend\weaponization_api.py" "${server}:${remotePath}/backend/"
scp "$localPath\jan-studio\backend\peace_weaponization_api.py" "${server}:${remotePath}/backend/"

Write-Host "📄 Deploying Updated main.py..." -ForegroundColor Cyan
# Deploy updated main.py
scp "$localPath\jan-studio\backend\main.py" "${server}:${remotePath}/backend/"

Write-Host "📚 Deploying Documentation..." -ForegroundColor Cyan
# Deploy documentation
scp "$localPath\CLOUD_SEEDING_DEBUNK_AND_UTILIZATION_COMPLETE.md" "${server}:${remotePath}/docs/"
scp "$localPath\WEAPONIZATION_EXPOSED_THROUGHOUT_TIME_COMPLETE.md" "${server}:${remotePath}/docs/"
scp "$localPath\WEAPONIZING_PEACE_COMPLETE.md" "${server}:${remotePath}/docs/"

Write-Host "💾 Deploying Analysis Data..." -ForegroundColor Cyan
# Deploy analysis JSON files
scp -r "$localPath\SIYEM\output\cloud_seeding_analysis\*" "${server}:${remotePath}/data/cloud_seeding_analysis/"
scp -r "$localPath\SIYEM\output\weaponization_analysis\*" "${server}:${remotePath}/data/weaponization_analysis/"
scp -r "$localPath\SIYEM\output\peace_weaponization\*" "${server}:${remotePath}/data/peace_weaponization/"

Write-Host ""
Write-Host "✅ Deployment Complete!" -ForegroundColor Green
Write-Host ""
Write-Host "Next Steps:" -ForegroundColor Yellow
Write-Host "1. SSH into server: ssh $server" -ForegroundColor White
Write-Host "2. Restart API service" -ForegroundColor White
Write-Host "3. Verify endpoints:" -ForegroundColor White
Write-Host "   - /api/cloud-seeding/" -ForegroundColor White
Write-Host "   - /api/weaponization/" -ForegroundColor White
Write-Host "   - /api/peace-weaponization/" -ForegroundColor White
