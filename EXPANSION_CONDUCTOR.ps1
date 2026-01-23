# EXPANSION_CONDUCTOR.ps1
# Unified System Orchestrator for JAN Expansion Protocol
# Version: 1.0 Genesis
# Date: 2026-01-15

<#
.SYNOPSIS
    Launches and orchestrates the entire JAN Expansion Protocol ecosystem.

.DESCRIPTION
    This conductor:
    - Performs pre-flight checks
    - Starts all backend services (SIYEM, JAN Studio)
    - Starts all frontends (Homeostasis, Consoles)
    - Verifies AI assistant connections
    - Displays unified status dashboard
    - Monitors system health

.PARAMETER Mode
    Launch mode: 'full' (all systems), 'biological' (Homeostasis only),
    'creative' (SIYEM only), or 'studio' (JAN Studio only)

.PARAMETER SkipHealthCheck
    Skip pre-flight health checks (faster startup, use if systems are known good)

.EXAMPLE
    .\EXPANSION_CONDUCTOR.ps1
    Launches full integrated system with health checks

.EXAMPLE
    .\EXPANSION_CONDUCTOR.ps1 -Mode biological
    Launches only Homeostasis-Sentinel

.EXAMPLE
    .\EXPANSION_CONDUCTOR.ps1 -SkipHealthCheck
    Launches full system without pre-flight checks
#>

param(
    [ValidateSet('full', 'biological', 'creative', 'studio')]
    [string]$Mode = 'full',
    
    [switch]$SkipHealthCheck
)

# ============================================================================
# CONFIGURATION
# ============================================================================

$ErrorActionPreference = "Continue"
$Global:ExpansionRoot = "S:\JAN"
$Global:SiyemRoot = "S:\SIYEM"

# Port Configuration
$Ports = @{
    SiyemBackend = 8000
    JanStudioBackend = 8001
    Homeostasis = 3000
    SiyemConsole = 5173
}

# Paths
$Paths = @{
    HomeostasisRoot = "$ExpansionRoot\homeostasis-sentinel"
    JanStudioBackend = "$ExpansionRoot\jan-studio\backend"
    JanStudioFrontend = "$ExpansionRoot\jan-studio\frontend"
    SiyemBackend = "$SiyemRoot\07_AUTOMATION_AI"
    SiyemConsole = "$SiyemRoot\08_WEB_DEV\console-v2"
}

# Colors
$Colors = @{
    Success = "Green"
    Warning = "Yellow"
    Error = "Red"
    Info = "Cyan"
    Header = "Magenta"
}

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

function Write-Header {
    param([string]$Text)
    Write-Host ""
    Write-Host "=" * 70 -ForegroundColor $Colors.Header
    Write-Host $Text -ForegroundColor $Colors.Header
    Write-Host "=" * 70 -ForegroundColor $Colors.Header
    Write-Host ""
}

function Write-Status {
    param(
        [string]$Message,
        [ValidateSet('Success', 'Warning', 'Error', 'Info')]
        [string]$Type = 'Info'
    )
    
    $Symbol = switch ($Type) {
        'Success' { '[✓]' }
        'Warning' { '[⚠]' }
        'Error'   { '[✗]' }
        'Info'    { '[i]' }
    }
    
    Write-Host "$Symbol $Message" -ForegroundColor $Colors[$Type]
}

function Test-PortAvailable {
    param([int]$Port)
    
    $connection = Test-NetConnection -ComputerName localhost -Port $Port -InformationLevel Quiet -WarningAction SilentlyContinue
    return -not $connection
}

function Test-PathExists {
    param([string]$Path, [string]$Name)
    
    if (Test-Path $Path) {
        Write-Status "$Name found: $Path" -Type Success
        return $true
    } else {
        Write-Status "$Name not found: $Path" -Type Error
        return $false
    }
}

function Start-ProcessInNewWindow {
    param(
        [string]$Title,
        [string]$WorkingDirectory,
        [string]$Command
    )
    
    $encodedCommand = [Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes($Command))
    
    Start-Process pwsh -ArgumentList @(
        "-NoExit",
        "-EncodedCommand", $encodedCommand
    ) -WindowStyle Normal -WorkingDirectory $WorkingDirectory
    
    Write-Status "Started: $Title" -Type Success
}

function Get-BiologicalState {
    # Check if today's biological state file exists
    $today = Get-Date -Format "yyyy-MM-dd"
    $stateFile = "$ExpansionRoot\homeostasis-sentinel\Obsidian_Vault\$today`_DAY*.md"
    
    if (Test-Path $stateFile) {
        $content = Get-Content $stateFile -Raw
        
        # Extract frontmatter
        if ($content -match '(?s)---(.+?)---') {
            $frontmatter = $matches[1]
            
            # Parse key metrics
            $glucose = if ($frontmatter -match 'blood_glucose:\s*(\d+)') { $matches[1] } else { "N/A" }
            $vision = if ($frontmatter -match 'vision_clarity:\s*(\d+)') { $matches[1] } else { "N/A" }
            $circadian = if ($frontmatter -match 'circadian_sync_score:\s*(\d+)') { $matches[1] } else { "N/A" }
            
            return @{
                Glucose = $glucose
                Vision = $vision
                Circadian = $circadian
                Status = if ($glucose -ne "N/A" -and [int]$glucose -lt 150 -and [int]$vision -gt 6) { "STABLE" } else { "MONITOR" }
            }
        }
    }
    
    return @{
        Glucose = "N/A"
        Vision = "N/A"
        Circadian = "N/A"
        Status = "NO_DATA"
    }
}

function Test-AIConnections {
    Write-Status "Checking AI Brotherhood connections..." -Type Info
    
    $claudeKey = $env:ANTHROPIC_API_KEY
    $geminiKey = $env:GEMINI_API_KEY
    
    $claudeStatus = if ($claudeKey) { "READY" } else { "NO_KEY" }
    $geminiStatus = if ($geminiKey) { "READY" } else { "NO_KEY" }
    
    if ($claudeStatus -eq "READY") {
        Write-Status "Claude Code: READY" -Type Success
    } else {
        Write-Status "Claude Code: API key not found (set ANTHROPIC_API_KEY)" -Type Warning
    }
    
    if ($geminiStatus -eq "READY") {
        Write-Status "Gemini: READY" -Type Success
    } else {
        Write-Status "Gemini: API key not found (set GEMINI_API_KEY)" -Type Warning
    }
    
    return @{
        Claude = $claudeStatus
        Gemini = $geminiStatus
    }
}

# ============================================================================
# HEALTH CHECK FUNCTIONS
# ============================================================================

function Invoke-PreFlightCheck {
    Write-Header "PRE-FLIGHT SYSTEM HEALTH CHECK"
    
    $allGood = $true
    
    # Check paths
    Write-Status "Checking critical paths..." -Type Info
    $allGood = $allGood -and (Test-PathExists $Paths.HomeostasisRoot "Homeostasis-Sentinel")
    $allGood = $allGood -and (Test-PathExists $Paths.SiyemBackend "SIYEM Backend")
    $allGood = $allGood -and (Test-PathExists $Paths.SiyemConsole "SIYEM Console")
    
    # Check ports
    Write-Status "Checking port availability..." -Type Info
    foreach ($portName in $Ports.Keys) {
        $port = $Ports[$portName]
        $available = Test-PortAvailable -Port $port
        
        if ($available) {
            Write-Status "Port $port ($portName): AVAILABLE" -Type Success
        } else {
            Write-Status "Port $port ($portName): IN USE (will attempt to use anyway)" -Type Warning
            # Not blocking - service might already be running
        }
    }
    
    # Check AI connections
    $aiStatus = Test-AIConnections
    
    # Check node/npm
    Write-Status "Checking Node.js..." -Type Info
    $nodeVersion = & node --version 2>$null
    if ($nodeVersion) {
        Write-Status "Node.js: $nodeVersion" -Type Success
    } else {
        Write-Status "Node.js: NOT FOUND (required for frontends)" -Type Error
        $allGood = $false
    }
    
    # Check Python
    Write-Status "Checking Python..." -Type Info
    $pythonVersion = & python --version 2>$null
    if ($pythonVersion) {
        Write-Status "Python: $pythonVersion" -Type Success
    } else {
        Write-Status "Python: NOT FOUND (required for backends)" -Type Error
        $allGood = $false
    }
    
    Write-Host ""
    if ($allGood) {
        Write-Status "PRE-FLIGHT CHECK: ALL SYSTEMS GO" -Type Success
    } else {
        Write-Status "PRE-FLIGHT CHECK: SOME ISSUES FOUND (review above)" -Type Warning
        Write-Host ""
        $continue = Read-Host "Continue anyway? (y/n)"
        if ($continue -ne 'y') {
            Write-Status "Launch aborted by user" -Type Info
            exit 1
        }
    }
}

# ============================================================================
# LAUNCH FUNCTIONS
# ============================================================================

function Start-HomeostasisSentinel {
    Write-Status "Starting Homeostasis-Sentinel..." -Type Info
    
    if (-not (Test-Path $Paths.HomeostasisRoot)) {
        Write-Status "Homeostasis-Sentinel path not found" -Type Error
        return
    }
    
    $command = @"
Set-Location '$($Paths.HomeostasisRoot)'
Write-Host 'HOMEOSTASIS-SENTINEL STARTING...' -ForegroundColor Cyan
npm run dev
"@
    
    Start-ProcessInNewWindow -Title "Homeostasis-Sentinel" -WorkingDirectory $Paths.HomeostasisRoot -Command $command
    Start-Sleep -Seconds 2
}

function Start-SiyemBackend {
    Write-Status "Starting SIYEM Backend..." -Type Info
    
    if (-not (Test-Path $Paths.SiyemBackend)) {
        Write-Status "SIYEM Backend path not found" -Type Error
        return
    }
    
    $command = @"
Set-Location '$($Paths.SiyemBackend)'
Write-Host 'SIYEM BACKEND STARTING...' -ForegroundColor Cyan
python -m uvicorn server:app --host 127.0.0.1 --port $($Ports.SiyemBackend) --reload
"@
    
    Start-ProcessInNewWindow -Title "SIYEM Backend" -WorkingDirectory $Paths.SiyemBackend -Command $command
    Start-Sleep -Seconds 3
}

function Start-SiyemConsole {
    Write-Status "Starting SIYEM Console V2..." -Type Info
    
    if (-not (Test-Path $Paths.SiyemConsole)) {
        Write-Status "SIYEM Console path not found" -Type Error
        return
    }
    
    $command = @"
Set-Location '$($Paths.SiyemConsole)'
Write-Host 'SIYEM CONSOLE STARTING...' -ForegroundColor Cyan
npm run dev
"@
    
    Start-ProcessInNewWindow -Title "SIYEM Console" -WorkingDirectory $Paths.SiyemConsole -Command $command
    Start-Sleep -Seconds 2
}

function Start-JanStudioBackend {
    Write-Status "Starting JAN Studio Backend..." -Type Info
    
    if (-not (Test-Path $Paths.JanStudioBackend)) {
        Write-Status "JAN Studio Backend not found (optional component)" -Type Warning
        return
    }
    
    $command = @"
Set-Location '$($Paths.JanStudioBackend)'
Write-Host 'JAN STUDIO BACKEND STARTING...' -ForegroundColor Cyan
python -m uvicorn main:app --host 127.0.0.1 --port $($Ports.JanStudioBackend) --reload
"@
    
    Start-ProcessInNewWindow -Title "JAN Studio Backend" -WorkingDirectory $Paths.JanStudioBackend -Command $command
    Start-Sleep -Seconds 2
}

# ============================================================================
# STATUS DASHBOARD
# ============================================================================

function Show-StatusDashboard {
    Start-Sleep -Seconds 5  # Give services time to start
    
    Write-Header "EXPANSION PROTOCOL - SYSTEM STATUS"
    
    # System URLs
    Write-Host "SERVICE ACCESS POINTS:" -ForegroundColor Cyan
    Write-Host "  Homeostasis-Sentinel:  " -NoNewline
    Write-Host "http://localhost:$($Ports.Homeostasis)" -ForegroundColor Green
    
    Write-Host "  SIYEM Console:         " -NoNewline
    Write-Host "http://localhost:$($Ports.SiyemConsole)" -ForegroundColor Green
    
    Write-Host "  SIYEM API Docs:        " -NoNewline
    Write-Host "http://localhost:$($Ports.SiyemBackend)/docs" -ForegroundColor Green
    
    if (Test-Path $Paths.JanStudioBackend) {
        Write-Host "  JAN Studio API:        " -NoNewline
        Write-Host "http://localhost:$($Ports.JanStudioBackend)/docs" -ForegroundColor Green
    }
    
    Write-Host ""
    
    # Biological State
    Write-Host "CURRENT BIOLOGICAL STATE:" -ForegroundColor Cyan
    $bioState = Get-BiologicalState
    
    Write-Host "  Glucose:               " -NoNewline
    $glucoseColor = if ($bioState.Glucose -ne "N/A" -and [int]$bioState.Glucose -lt 150) { "Green" } else { "Yellow" }
    Write-Host "$($bioState.Glucose) mg/dL" -ForegroundColor $glucoseColor
    
    Write-Host "  Vision Clarity:        " -NoNewline
    $visionColor = if ($bioState.Vision -ne "N/A" -and [int]$bioState.Vision -gt 6) { "Green" } else { "Yellow" }
    Write-Host "$($bioState.Vision)/10" -ForegroundColor $visionColor
    
    Write-Host "  Circadian Sync:        " -NoNewline
    Write-Host "$($bioState.Circadian)%" -ForegroundColor Cyan
    
    Write-Host "  System Status:         " -NoNewline
    $statusColor = switch ($bioState.Status) {
        "STABLE"  { "Green" }
        "MONITOR" { "Yellow" }
        "NO_DATA" { "Gray" }
    }
    Write-Host $bioState.Status -ForegroundColor $statusColor
    
    Write-Host ""
    
    # Recommendations
    Write-Host "CURRENT RECOMMENDATIONS:" -ForegroundColor Cyan
    if ($bioState.Status -eq "STABLE") {
        Write-Host "  ✓ Optimal state for high-clarity creative work" -ForegroundColor Green
        Write-Host "  ✓ Recommended: Jean storytelling, Ramiz teaching development" -ForegroundColor Green
    } elseif ($bioState.Status -eq "MONITOR") {
        Write-Host "  ⚠ Elevated state - recommend medium-intensity work" -ForegroundColor Yellow
        Write-Host "  ⚠ Recommended: Pierre content, Siyem Media admin tasks" -ForegroundColor Yellow
    } else {
        Write-Host "  i No biological data for today yet" -ForegroundColor Gray
        Write-Host "  i Log today's metrics in Homeostasis-Sentinel" -ForegroundColor Gray
    }
    
    Write-Host ""
    
    # AI Brotherhood
    $aiStatus = Test-AIConnections
    Write-Host "AI BROTHERHOOD STATUS:" -ForegroundColor Cyan
    Write-Host "  Claude Code:           " -NoNewline
    Write-Host $aiStatus.Claude -ForegroundColor $(if ($aiStatus.Claude -eq "READY") { "Green" } else { "Yellow" })
    
    Write-Host "  Gemini:                " -NoNewline
    Write-Host $aiStatus.Gemini -ForegroundColor $(if ($aiStatus.Gemini -eq "READY") { "Green" } else { "Yellow" })
    
    Write-Host ""
    Write-Host "=" * 70 -ForegroundColor Magenta
    Write-Host ""
    
    Write-Status "ALL SYSTEMS OPERATIONAL - EXPANSION PROTOCOL ACTIVE" -Type Success
    Write-Host ""
    Write-Host "Press Ctrl+C in any terminal window to stop that service" -ForegroundColor Gray
    Write-Host "Close this window when all work is complete" -ForegroundColor Gray
    Write-Host ""
}

# ============================================================================
# MAIN EXECUTION
# ============================================================================

function Start-ExpansionProtocol {
    Clear-Host
    
    Write-Header "EXPANSION PROTOCOL - INITIALIZATION"
    Write-Host "Mode: $Mode" -ForegroundColor Cyan
    Write-Host "Date: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" -ForegroundColor Cyan
    Write-Host ""
    
    # Pre-flight check
    if (-not $SkipHealthCheck) {
        Invoke-PreFlightCheck
    } else {
        Write-Status "Skipping health check (as requested)" -Type Warning
    }
    
    Write-Header "LAUNCHING SYSTEMS"
    
    # Launch based on mode
    switch ($Mode) {
        'full' {
            Write-Status "Launching FULL INTEGRATED SYSTEM..." -Type Info
            Start-SiyemBackend
            Start-HomeostasisSentinel
            Start-SiyemConsole
            Start-JanStudioBackend
        }
        'biological' {
            Write-Status "Launching BIOLOGICAL SYSTEMS ONLY..." -Type Info
            Start-HomeostasisSentinel
        }
        'creative' {
            Write-Status "Launching CREATIVE SYSTEMS ONLY..." -Type Info
            Start-SiyemBackend
            Start-SiyemConsole
        }
        'studio' {
            Write-Status "Launching JAN STUDIO ONLY..." -Type Info
            Start-JanStudioBackend
        }
    }
    
    # Show status dashboard
    Show-StatusDashboard
    
    # Keep conductor alive
    Write-Host "EXPANSION CONDUCTOR running..." -ForegroundColor Magenta
    Write-Host "Press Ctrl+C to exit (this will NOT stop launched services)" -ForegroundColor Gray
    Write-Host ""
    
    # Wait indefinitely
    try {
        while ($true) {
            Start-Sleep -Seconds 60
        }
    }
    catch {
        Write-Host ""
        Write-Status "EXPANSION CONDUCTOR shutting down..." -Type Info
        Write-Host "Launched services continue running in their windows" -ForegroundColor Gray
    }
}

# ============================================================================
# EXECUTE
# ============================================================================

try {
    Start-ExpansionProtocol
}
catch {
    Write-Status "CRITICAL ERROR: $($_.Exception.Message)" -Type Error
    Write-Host $_.ScriptStackTrace -ForegroundColor Red
    exit 1
}

