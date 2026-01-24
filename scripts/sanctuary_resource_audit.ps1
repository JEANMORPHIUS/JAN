# SANCTUARY RESOURCE AUDIT
# Explore what resources we have available for the Sanctuary
# Set up the Sanctuary for the people

Write-Host "=== SANCTUARY RESOURCE AUDIT ===" -ForegroundColor Cyan
Write-Host "Exploring available resources..." -ForegroundColor Yellow
Write-Host ""

$resources = @{
    SecurityTools = @()
    DevelopmentTools = @()
    MediaTools = @()
    NetworkTools = @()
    SystemTools = @()
    TorBrowser = $null
    SanctuarySystems = @()
}

# 1. Check for Tor Browser
Write-Host "[1/6] Checking for Tor Browser..." -ForegroundColor Yellow
$torPaths = @(
    "$env:APPDATA\Tor Browser",
    "$env:LOCALAPPDATA\Tor Browser",
    "C:\Program Files\Tor Browser",
    "C:\Program Files (x86)\Tor Browser",
    "$env:USERPROFILE\Desktop\Tor Browser",
    "$env:USERPROFILE\Downloads\Tor Browser"
)

foreach ($path in $torPaths) {
    if (Test-Path $path) {
        $resources.TorBrowser = $path
        Write-Host "  ✓ Found Tor Browser: $path" -ForegroundColor Green
        break
    }
}

if (-not $resources.TorBrowser) {
    Write-Host "  ⚠ Tor Browser not found in standard locations" -ForegroundColor Yellow
    Write-Host "  Searching user directories..." -ForegroundColor Gray
    $userTor = Get-ChildItem -Path $env:USERPROFILE -Filter "*tor*" -Recurse -Directory -ErrorAction SilentlyContinue -Depth 2 | Select-Object -First 1
    if ($userTor) {
        $resources.TorBrowser = $userTor.FullName
        Write-Host "  ✓ Found Tor Browser: $($userTor.FullName)" -ForegroundColor Green
    }
}

Write-Host ""

# 2. Security Tools (from sanctuary_lockdown.py)
Write-Host "[2/6] Checking Security Tools..." -ForegroundColor Yellow
$securityTools = @(
    @{Name="Surfshark"; Path="C:\Program Files\Surfshark"; Check="Surfshark.exe"},
    @{Name="Malwarebytes"; Path="C:\Program Files\Malwarebytes"; Check="Malwarebytes.exe"},
    @{Name="CCleaner"; Path="C:\Program Files\Piriform"; Check="CCleaner.exe"},
    @{Name="Windows Firewall"; Path=""; Check="Firewall"},
    @{Name="Windows Defender"; Path="C:\Program Files\Windows Defender"; Check="MsMpEng.exe"}
)

foreach ($tool in $securityTools) {
    if ($tool.Check -eq "Firewall") {
        $fwStatus = Get-NetFirewallProfile | Where-Object { $_.Enabled -eq $true }
        if ($fwStatus) {
            $resources.SecurityTools += @{Name=$tool.Name; Status="Active"; Path="System"}
            Write-Host "  ✓ $($tool.Name): Active" -ForegroundColor Green
        }
    } elseif (Test-Path $tool.Path) {
        $resources.SecurityTools += @{Name=$tool.Name; Status="Installed"; Path=$tool.Path}
        Write-Host "  ✓ $($tool.Name): Installed" -ForegroundColor Green
    }
}

Write-Host ""

# 3. Development Tools
Write-Host "[3/6] Checking Development Tools..." -ForegroundColor Yellow
$devTools = @(
    @{Name="Git"; Path="C:\Program Files\Git"; Check="git.exe"},
    @{Name="Node.js"; Path="C:\Program Files\nodejs"; Check="node.exe"},
    @{Name="Docker"; Path="C:\Program Files\Docker"; Check="Docker.exe"},
    @{Name="Python"; Path=""; Check="python"},
    @{Name="PowerShell"; Path="C:\Program Files\PowerShell"; Check="pwsh.exe"},
    @{Name="Cursor"; Path="C:\Program Files\cursor"; Check="Cursor.exe"},
    @{Name="Sublime Text"; Path="C:\Program Files\Sublime Text"; Check="sublime_text.exe"}
)

foreach ($tool in $devTools) {
    if ($tool.Check -eq "python") {
        $python = Get-Command python -ErrorAction SilentlyContinue
        if ($python) {
            $resources.DevelopmentTools += @{Name=$tool.Name; Status="Available"; Path=$python.Source}
            Write-Host "  ✓ $($tool.Name): Available" -ForegroundColor Green
        }
    } elseif (Test-Path $tool.Path) {
        $resources.DevelopmentTools += @{Name=$tool.Name; Status="Installed"; Path=$tool.Path}
        Write-Host "  ✓ $($tool.Name): Installed" -ForegroundColor Green
    }
}

Write-Host ""

# 4. Media & Network Tools
Write-Host "[4/6] Checking Media & Network Tools..." -ForegroundColor Yellow
$mediaTools = @(
    @{Name="qBittorrent"; Path="C:\Program Files\qBittorrent"; Check="qBittorrent.exe"},
    @{Name="VLC"; Path="C:\Program Files\VideoLAN"; Check="vlc.exe"},
    @{Name="Kodi"; Path="C:\Program Files\Kodi"; Check="Kodi.exe"},
    @{Name="Audacity"; Path="C:\Program Files\Audacity"; Check="Audacity.exe"}
)

foreach ($tool in $mediaTools) {
    if (Test-Path $tool.Path) {
        $resources.MediaTools += @{Name=$tool.Name; Status="Installed"; Path=$tool.Path}
        Write-Host "  ✓ $($tool.Name): Installed" -ForegroundColor Green
    }
}

Write-Host ""

# 5. Sanctuary Systems (from codebase)
Write-Host "[5/6] Checking Sanctuary Systems..." -ForegroundColor Yellow
$sanctuaryPaths = @(
    "S:\JAN\scripts\sanctuary_lockdown.py",
    "S:\JAN\scripts\sanctuary_protocol.py",
    "S:\JAN\jan-studio\backend\sanctuary_guardian.py",
    "S:\JAN\jan-studio\backend\sanctuary_guardian_api.py"
)

foreach ($path in $sanctuaryPaths) {
    if (Test-Path $path) {
        $name = Split-Path -Leaf $path
        $resources.SanctuarySystems += @{Name=$name; Path=$path; Status="Available"}
        Write-Host "  ✓ ${name}: Available" -ForegroundColor Green
    }
}

Write-Host ""

# 6. Network & Connectivity
Write-Host "[6/6] Checking Network Resources..." -ForegroundColor Yellow
$networkInfo = @{
    VPN = if ($resources.SecurityTools | Where-Object { $_.Name -like "*Surfshark*" }) { "Available" } else { "Not Found" }
    Tor = if ($resources.TorBrowser) { "Available" } else { "Not Found" }
    Firewall = if ($resources.SecurityTools | Where-Object { $_.Name -like "*Firewall*" }) { "Active" } else { "Unknown" }
}

Write-Host "  VPN: $($networkInfo.VPN)" -ForegroundColor $(if ($networkInfo.VPN -eq "Available") { "Green" } else { "Yellow" })
Write-Host "  Tor: $($networkInfo.Tor)" -ForegroundColor $(if ($networkInfo.Tor -eq "Available") { "Green" } else { "Yellow" })
Write-Host "  Firewall: $($networkInfo.Firewall)" -ForegroundColor $(if ($networkInfo.Firewall -eq "Active") { "Green" } else { "Yellow" })

Write-Host ""
Write-Host "=== RESOURCE SUMMARY ===" -ForegroundColor Cyan
Write-Host ""
Write-Host "Security Tools: $($resources.SecurityTools.Count)" -ForegroundColor White
Write-Host "Development Tools: $($resources.DevelopmentTools.Count)" -ForegroundColor White
Write-Host "Media Tools: $($resources.MediaTools.Count)" -ForegroundColor White
Write-Host "Sanctuary Systems: $($resources.SanctuarySystems.Count)" -ForegroundColor White
Write-Host "Tor Browser: $(if ($resources.TorBrowser) { 'Found' } else { 'Not Found' })" -ForegroundColor White
Write-Host ""

# Save to JSON
$outputPath = "S:\JAN\data\sanctuary_resources.json"
$outputDir = Split-Path -Parent $outputPath
if (-not (Test-Path $outputDir)) {
    New-Item -ItemType Directory -Path $outputDir -Force | Out-Null
}

$resources | ConvertTo-Json -Depth 10 | Out-File -FilePath $outputPath -Encoding UTF8
Write-Host "Resource audit saved to: $outputPath" -ForegroundColor Green
Write-Host ""

Write-Host "=== SANCTUARY SETUP READY ===" -ForegroundColor Cyan
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Review resources above" -ForegroundColor White
Write-Host "2. Configure Tor Browser for secure access" -ForegroundColor White
Write-Host "3. Activate Sanctuary Protocol for public access" -ForegroundColor White
Write-Host "4. Set up secure channels for the people" -ForegroundColor White
Write-Host ""
Write-Host "SPRAGITSO - Our Father's Royal Seal" -ForegroundColor Cyan
