# --- JAN MUHARREM Ecosystem NotebookLM Sync ---
# Captures the complete current ecosystem state for NotebookLM ingestion
# Updated: 2026-01-18 - Reflects current JAN/SIYEM/Homeostasis Sentinel ecosystem
# Local sync only - everything stays on S: drive for NotebookLM

$date = Get-Date -Format "yyyyMMdd_HHmm"
$janRoot = "S:\JAN"
$targetRoot = "S:\JAN\NotebookLM_Sync"
$target = "$targetRoot\$date"
$enableCloudUpload = $false  # Set to $true if you want cloud backup
$bucket = "gs://siyem-archive"

Write-Host "=== JAN MUHARREM ECOSYSTEM SYNC ===" -ForegroundColor Cyan
Write-Host "Date: $date" -ForegroundColor Cyan
Write-Host ""

New-Item -ItemType Directory -Force -Path $target | Out-Null
New-Item -ItemType Directory -Force -Path "$target\Mission" | Out-Null
New-Item -ItemType Directory -Force -Path "$target\Book_Of_Racon" | Out-Null
New-Item -ItemType Directory -Force -Path "$target\Homeostasis_Sentinel" | Out-Null
New-Item -ItemType Directory -Force -Path "$target\Earth_Alignment" | Out-Null
New-Item -ItemType Directory -Force -Path "$target\Entity_Structures" | Out-Null
New-Item -ItemType Directory -Force -Path "$target\Status_Documents" | Out-Null
New-Item -ItemType Directory -Force -Path "$target\Core_Documentation" | Out-Null

$copiedFiles = @()
$missingFiles = @()

# ===================================================================
# 1. MISSION DOCUMENTS (Core Identity)
# ===================================================================
Write-Host "📋 Syncing Mission Documents..." -ForegroundColor Green

$missionFiles = @(
    "$janRoot\MISSION_SEED.md",
    "$janRoot\MISSION_SHELL.md",
    "$janRoot\STEWARDSHIP_AND_COMMUNITY.md"
)

foreach ($file in $missionFiles) {
    if (Test-Path $file) {
        $name = Split-Path $file -Leaf
        Copy-Item $file -Destination "$target\Mission\$name" -Force
        $copiedFiles += "Mission/$name"
        Write-Host "  ✅ $name" -ForegroundColor Gray
    } else {
        $missingFiles += $file
        Write-Host "  ⚠️  Missing: $file" -ForegroundColor Yellow
    }
}

# ===================================================================
# 2. BOOK OF RACON (Foundational Philosophy)
# ===================================================================
Write-Host "📜 Syncing Book of Racon..." -ForegroundColor Green

$raconFiles = @(
    "$janRoot\docs\BOOK-OF-RACON.md",
    "$janRoot\THE_BOOK_OF_RACON.md"
)

foreach ($file in $raconFiles) {
    if (Test-Path $file) {
        $name = Split-Path $file -Leaf
        Copy-Item $file -Destination "$target\Book_Of_Racon\$name" -Force
        $copiedFiles += "Book_Of_Racon/$name"
        Write-Host "  ✅ $name" -ForegroundColor Gray
    } else {
        $missingFiles += $file
        Write-Host "  ⚠️  Missing: $file" -ForegroundColor Yellow
    }
}

# ===================================================================
# 3. HOMEOSTASIS SENTINEL (Biological Tracking)
# ===================================================================
Write-Host "🔬 Syncing Homeostasis Sentinel..." -ForegroundColor Green

$homeostasisRoot = "$janRoot\homeostasis-sentinel"
$homeostasisFiles = @(
    "$homeostasisRoot\Obsidian_Vault\2026-01-16_DAY4.md",
    "$homeostasisRoot\Obsidian_Vault\2026-01-16_DAY4_TRUTH.md",
    "$homeostasisRoot\Obsidian_Vault\2026-01-15_DAY3.md",
    "$homeostasisRoot\Obsidian_Vault\2026-01-15_DAY2.md",
    "$homeostasisRoot\Obsidian_Vault\2026-01-14_DAY1.md",
    "$janRoot\HYBRID_PROTOCOL_LOG.md",
    "$homeostasisRoot\MEDICATION_ADHERENCE_TRACKER.md",
    "$homeostasisRoot\BLOOD_PRESSURE_TRACKING.md",
    "$homeostasisRoot\CONTINUOUS_LOOP_PROTOCOL.md",
    "$homeostasisRoot\LOOP_EARTH_ALIGNMENT.md"
)

# Get latest daily log
$latestDailyLog = Get-ChildItem "$homeostasisRoot\Obsidian_Vault" -Filter "2026-01-*.md" -ErrorAction SilentlyContinue | 
    Sort-Object LastWriteTime -Descending | Select-Object -First 1

if ($latestDailyLog) {
    Copy-Item $latestDailyLog.FullName -Destination "$target\Homeostasis_Sentinel\LATEST_DAILY_LOG.md" -Force
    $copiedFiles += "Homeostasis_Sentinel/LATEST_DAILY_LOG.md (from $($latestDailyLog.Name))"
    Write-Host "  ✅ Latest Daily Log: $($latestDailyLog.Name)" -ForegroundColor Gray
}

foreach ($file in $homeostasisFiles) {
    if (Test-Path $file) {
        $name = Split-Path $file -Leaf
        Copy-Item $file -Destination "$target\Homeostasis_Sentinel\$name" -Force
        $copiedFiles += "Homeostasis_Sentinel/$name"
        Write-Host "  ✅ $name" -ForegroundColor Gray
    } else {
        $missingFiles += $file
    }
}

# ===================================================================
# 4. ENTITY STRUCTURES (Siyem.org Entities)
# ===================================================================
Write-Host "👥 Syncing Entity Structures..." -ForegroundColor Green

$entityRoot = "$janRoot\Siyem.org"
$entities = @("jean_mahram", "jk", "pierre_pressure", "uncle_ray_ramiz", "siyem_media")

foreach ($entity in $entities) {
    $entityPath = "$entityRoot\$entity"
    if (Test-Path $entityPath) {
        $entityDir = "$target\Entity_Structures\$entity"
        New-Item -ItemType Directory -Force -Path $entityDir | Out-Null
        
        $entityFiles = @(
            "$entityPath\profile.md",
            "$entityPath\creative_rules.md"
        )
        
        foreach ($file in $entityFiles) {
            if (Test-Path $file) {
                $name = Split-Path $file -Leaf
                Copy-Item $file -Destination "$entityDir\$name" -Force
                $copiedFiles += "Entity_Structures/$entity/$name"
            }
        }
        Write-Host "  ✅ $entity" -ForegroundColor Gray
    }
}

# ===================================================================
# 5. STATUS & COMPLETION DOCUMENTS (Current State)
# ===================================================================
Write-Host "📊 Syncing Status Documents..." -ForegroundColor Green

$statusFiles = @(
    "$janRoot\CHANNEL_INTEGRATION_STRATEGY.md",
    "$janRoot\INTEGRATED_STEWARDSHIP_ARCHITECTURE.md",
    "$janRoot\THE_ORIGINAL_ERROR_AND_SYMBIOISIS.md",
    "$janRoot\FOUNDATIONAL_INTEGRATION_SEALED.md",
    "$janRoot\READINESS_WHEN_PEOPLE_COME_CALLING.md",
    "$janRoot\KNOWLEDGE_OVER_BELIEF.md",
    "$janRoot\THE_LAW_OF_THIS_LAND.md",
    "$janRoot\README.md"
)

foreach ($file in $statusFiles) {
    if (Test-Path $file) {
        $name = Split-Path $file -Leaf
        Copy-Item $file -Destination "$target\Status_Documents\$name" -Force
        $copiedFiles += "Status_Documents/$name"
        Write-Host "  ✅ $name" -ForegroundColor Gray
    } else {
        $missingFiles += $file
    }
}

# ===================================================================
# 6. EARTH ALIGNMENT DOCUMENTS (Symbiotic Relationship)
# ===================================================================
Write-Host "🌍 Syncing Earth Alignment Documents..." -ForegroundColor Green

$earthFiles = @(
    "$janRoot\THE_ORIGINAL_ERROR_AND_SYMBIOISIS.md",
    "$homeostasisRoot\LOOP_EARTH_ALIGNMENT.md"
)

foreach ($file in $earthFiles) {
    if (Test-Path $file) {
        $name = Split-Path $file -Leaf
        Copy-Item $file -Destination "$target\Earth_Alignment\$name" -Force
        $copiedFiles += "Earth_Alignment/$name"
        Write-Host "  ✅ $name" -ForegroundColor Gray
    } else {
        $missingFiles += $file
    }
}

# ===================================================================
# 7. CORE DOCUMENTATION (JAN/SIYEM Architecture)
# ===================================================================
Write-Host "🏗️  Syncing Core Documentation..." -ForegroundColor Green

$coreFiles = @(
    "$janRoot\README.md"
)

foreach ($file in $coreFiles) {
    if (Test-Path $file) {
        $name = Split-Path $file -Leaf
        Copy-Item $file -Destination "$target\Core_Documentation\$name" -Force
        $copiedFiles += "Core_Documentation/$name"
        Write-Host "  ✅ $name" -ForegroundColor Gray
    }
}

# ===================================================================
# 8. BUILD COMPREHENSIVE COMBINED_REFERENCE.md
# ===================================================================
Write-Host "🧠 Building COMBINED_REFERENCE.md..." -ForegroundColor Green

$combined = "$target\COMBINED_REFERENCE.md"
$sections = @()

# Mission Section
$sections += "# MISSION & IDENTITY`n`n"
$missionSeed = "$target\Mission\MISSION_SEED.md"
$missionShell = "$target\Mission\MISSION_SHELL.md"
if (Test-Path $missionSeed) { $sections += (Get-Content $missionSeed -Raw) + "`n---`n" }
if (Test-Path $missionShell) { $sections += (Get-Content $missionShell -Raw) + "`n---`n" }

# Book of Racon Section
$sections += "`n# THE BOOK OF RACON`n`n"
$raconFile = "$target\Book_Of_Racon\BOOK-OF-RACON.md"
if (-not (Test-Path $raconFile)) { $raconFile = "$target\Book_Of_Racon\THE_BOOK_OF_RACON.md" }
if (Test-Path $raconFile) { $sections += (Get-Content $raconFile -Raw) + "`n---`n" }

# Homeostasis Sentinel Section
$sections += "`n# HOMEOSTASIS SENTINEL`n`n"
$latestLog = "$target\Homeostasis_Sentinel\LATEST_DAILY_LOG.md"
$hybridLog = "$target\Homeostasis_Sentinel\HYBRID_PROTOCOL_LOG.md"
$loopProtocol = "$target\Homeostasis_Sentinel\CONTINUOUS_LOOP_PROTOCOL.md"
if (Test-Path $latestLog) { $sections += "## Latest Daily Log`n`n" + (Get-Content $latestLog -Raw) + "`n---`n" }
if (Test-Path $hybridLog) { $sections += "## Hybrid Protocol Log`n`n" + (Get-Content $hybridLog -Raw) + "`n---`n" }
if (Test-Path $loopProtocol) { $sections += "## Continuous Loop Protocol`n`n" + (Get-Content $loopProtocol -Raw) + "`n---`n" }

# Earth Alignment Section
$sections += "`n# EARTH ALIGNMENT - THE SYMBIOTIC RELATIONSHIP`n`n"
$originalError = "$target\Earth_Alignment\THE_ORIGINAL_ERROR_AND_SYMBIOISIS.md"
$loopEarth = "$target\Earth_Alignment\LOOP_EARTH_ALIGNMENT.md"
if (Test-Path $originalError) { $sections += "## The Original Error and Symbiosis`n`n" + (Get-Content $originalError -Raw) + "`n---`n" }
if (Test-Path $loopEarth) { $sections += "## Loop-Earth Alignment`n`n" + (Get-Content $loopEarth -Raw) + "`n---`n" }

# Entity Structures Section
$sections += "`n# ENTITY STRUCTURES`n`n"
$entityDir = "$target\Entity_Structures"
if (Test-Path $entityDir) {
    $entities = Get-ChildItem $entityDir -Directory
    foreach ($entity in $entities) {
        $profile = "$($entity.FullName)\profile.md"
        $rules = "$($entity.FullName)\creative_rules.md"
        if (Test-Path $profile) { 
            $sections += "## $($entity.Name) - Profile`n`n" + (Get-Content $profile -Raw) + "`n---`n" 
        }
        if (Test-Path $rules) { 
            $sections += "## $($entity.Name) - Creative Rules`n`n" + (Get-Content $rules -Raw) + "`n---`n" 
        }
    }
}

# Status Documents Section
$sections += "`n# STATUS & STRATEGY`n`n"
$statusDir = "$target\Status_Documents"
if (Test-Path $statusDir) {
    $statusDocs = Get-ChildItem $statusDir -Filter "*.md"
    foreach ($doc in $statusDocs) {
        $sections += "## $($doc.BaseName)`n`n" + (Get-Content $doc.FullName -Raw) + "`n---`n"
    }
}

$sections -join "`n" | Out-File -FilePath $combined -Encoding utf8
Write-Host "  ✅ COMBINED_REFERENCE.md built ($([math]::Round((Get-Item $combined).Length/1KB, 2)) KB)" -ForegroundColor Gray

# ===================================================================
# 9. CREATE SYNC INDEX
# ===================================================================
$index = "$target\SYNC_INDEX.md"
$indexContent = @"
# JAN MUHARREM Ecosystem Sync Index
**Sync Date:** $date
**Ecosystem:** JAN + SIYEM + Homeostasis Sentinel

## Files Synced: $($copiedFiles.Count)

### Mission Documents
$(if ($copiedFiles | Where-Object { $_ -like "Mission/*" }) { ($copiedFiles | Where-Object { $_ -like "Mission/*" }) -join "`n" } else { "None" })

### Book of Racon
$(if ($copiedFiles | Where-Object { $_ -like "Book_Of_Racon/*" }) { ($copiedFiles | Where-Object { $_ -like "Book_Of_Racon/*" }) -join "`n" } else { "None" })

### Homeostasis Sentinel
$(if ($copiedFiles | Where-Object { $_ -like "Homeostasis_Sentinel/*" }) { ($copiedFiles | Where-Object { $_ -like "Homeostasis_Sentinel/*" }) -join "`n" } else { "None" })

### Entity Structures
$(if ($copiedFiles | Where-Object { $_ -like "Entity_Structures/*" }) { ($copiedFiles | Where-Object { $_ -like "Entity_Structures/*" }) -join "`n" } else { "None" })

### Status Documents
$(if ($copiedFiles | Where-Object { $_ -like "Status_Documents/*" }) { ($copiedFiles | Where-Object { $_ -like "Status_Documents/*" }) -join "`n" } else { "None" })

### Earth Alignment
$(if ($copiedFiles | Where-Object { $_ -like "Earth_Alignment/*" }) { ($copiedFiles | Where-Object { $_ -like "Earth_Alignment/*" }) -join "`n" } else { "None" })

### Core Documentation
$(if ($copiedFiles | Where-Object { $_ -like "Core_Documentation/*" }) { ($copiedFiles | Where-Object { $_ -like "Core_Documentation/*" }) -join "`n" } else { "None" })

## Missing Files: $($missingFiles.Count)
$(if ($missingFiles.Count -gt 0) { $missingFiles -join "`n" } else { "None" })

---
**Generated by:** notebooklm_sync.ps1
**Date:** $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")
"@

$indexContent | Out-File -FilePath $index -Encoding utf8
$copiedFiles += "SYNC_INDEX.md"

# ===================================================================
# 10. OPTIONAL CLOUD UPLOAD (Backup/Sharing)
# ===================================================================
if ($enableCloudUpload -and (Get-Command gcloud -ErrorAction SilentlyContinue)) {
    Write-Host "☁️  Uploading to Google Cloud Storage (optional backup)..." -ForegroundColor Green
    
    $currentAccount = (gcloud config get-value account 2>&1)
    if ($currentAccount -notlike "*siyemfilm@gmail.com*") {
        Write-Host "  Switching to siyemfilm@gmail.com for bucket access..." -ForegroundColor Gray
        gcloud config set account siyemfilm@gmail.com 2>&1 | Out-Null
    }
    
    $uploadResult = gcloud storage cp "$target\*" "$bucket/syncs/$date/" --recursive 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  ✅ Synced to Cloud Bucket: $bucket/syncs/$date" -ForegroundColor Cyan
    } else {
        Write-Host "  ⚠️  Cloud upload failed (continuing anyway):" -ForegroundColor Yellow
        Write-Host $uploadResult -ForegroundColor Yellow
    }
} else {
    if ($enableCloudUpload) {
        Write-Host "⚠️  Cloud upload enabled but gcloud not available - skipping" -ForegroundColor Yellow
    }
    # Cloud upload disabled by default - local sync only
}

# ===================================================================
# 11. SUMMARY
# ===================================================================
Write-Host ""
Write-Host "=== SYNC COMPLETE ===" -ForegroundColor Green
Write-Host "📁 Files synced: $($copiedFiles.Count)" -ForegroundColor Cyan
Write-Host "📦 Target: $target" -ForegroundColor Cyan
Write-Host "📚 COMBINED_REFERENCE.md: $([math]::Round((Get-Item $combined).Length/1KB, 2)) KB" -ForegroundColor Cyan
if ($missingFiles.Count -gt 0) {
    Write-Host "⚠️  Missing files: $($missingFiles.Count)" -ForegroundColor Yellow
}
Write-Host ""
Write-Host "📚 NotebookLM ready to ingest from: $target" -ForegroundColor Green
Write-Host "💡 To enable cloud backup, set `$enableCloudUpload = `$true in the script`n" -ForegroundColor Gray
