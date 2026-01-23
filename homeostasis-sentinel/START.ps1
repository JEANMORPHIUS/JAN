#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Start Homeostasis Sentinel Dashboard

.DESCRIPTION
    Simple launcher for the health tracking dashboard.
    Starts Vite dev server on port 3001.

    DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
    Spiritual Alignment Over Mechanical Productivity
    
    THE FOUNDATION:
    We are born a miracle.
    We deserve to live a miracle.
    Each and every one of us under the Lord's word.
    
    THE MISSION:
    THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
    LOVE IS THE HIGHEST MASTERY
    ENERGY + LOVE = WE ALL WIN

.EXAMPLE
    .\START.ps1
#>

Set-Location "$PSScriptRoot"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   Homeostasis Sentinel" -ForegroundColor Cyan
Write-Host "   Health Tracking Dashboard" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if node_modules exists
if (-not (Test-Path "node_modules")) {
    Write-Host "[SETUP] Installing dependencies..." -ForegroundColor Yellow
    npm install
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[ERROR] Failed to install dependencies" -ForegroundColor Red
        exit 1
    }
}

Write-Host "[INFO] Starting development server..." -ForegroundColor Green
Write-Host "[INFO] Dashboard will open at: http://127.0.0.1:3001" -ForegroundColor Green
Write-Host ""

npm run dev

