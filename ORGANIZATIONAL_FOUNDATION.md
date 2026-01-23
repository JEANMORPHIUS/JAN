# Organizational Foundation - S: Drive Standards

**Purpose:** Prevent residual file creation and maintain a clean, organized workspace  
**Created:** 2026-01-15  
**Status:** ACTIVE STANDARD

---

## 🎯 Core Principle

**"Every file has a purpose, a place, and a lifecycle."**

If you can't answer these three questions about a file, it shouldn't be created:
1. **Purpose:** Why does this file exist?
2. **Place:** Where does it belong in the structure?
3. **Lifecycle:** When should it be archived or deleted?

---

## 📂 Directory Structure Standards

### **S:\JAN\** - Multi-Project Workspace

**Purpose:** Development, experiments, integration hub

**Allowed at root:**
- ✅ `README.md` - Primary project documentation
- ✅ `FOR_CLAUDE.md` - AI assistant context
- ✅ `LICENSE` - Licensing information
- ✅ Active project folders (homeostasis-sentinel, jan-studio, etc.)
- ✅ `docs\` - Cross-project documentation
- ✅ `examples\` - Reusable examples
- ✅ `scripts\` - Active automation scripts
- ✅ `docker-compose.yml` - Active infrastructure

**NOT allowed at root:**
- ❌ Completed status reports (*_COMPLETE.md, *_SUMMARY.md)
- ❌ Implementation guides (*_IMPLEMENTATION.md)
- ❌ Old documentation versions (*.md.old, *.bak)
- ❌ Temporary files (tmp*, NUL, etc.)
- ❌ Historical reference docs (move to ARK)

---

### **S:\SIYEM\** - Production Content System

**Structure:** Fixed production pipeline
```
00_CORE/          # System core (scripts, DB, entities)
01_CONCEPT/       # Pre-production planning
02_PREPRODUCTION/ # Scripting, storyboards
03_PRODUCTION/    # Active creation
04_POSTPRODUCTION/# Editing, refinement
05_PUBLISHING/    # Distribution ready content
08_WEB_DEV/       # Web projects
```

**Rules:**
- ✅ Content flows through numbered folders (01 → 05)
- ✅ Entity-specific content in entity subfolders
- ❌ No random files at SIYEM root
- ❌ No archive/legacy content (use ARK)

---

### **S:\ARK\** - Archive Storage

**Purpose:** Centralized historical storage

**Structure:**
```
JAN_ARCHIVE/       # Historical JAN content
SIYEM_ARCHIVE/     # Historical SIYEM content
HISTORICAL_DOCS/   # Completed documentation
```

**Archive triggers:**
- Project completion
- Documentation superseded by new version
- Legacy scripts no longer in use
- Old system backups

---

## 📝 File Naming Conventions

### **Documentation Files**

#### Active Documentation (stays in project)
```
README.md               # Primary project documentation
FOR_CLAUDE.md          # AI assistant context
CONTRIBUTING.md        # Contribution guidelines
LICENSE                # License file
```

#### Status Documents (archive when complete)
```
PROJECT_NAME_STATUS.md      # Active status → Archive when complete
PROJECT_NAME_COMPLETE.md    # Completion report → Archive immediately
PROJECT_NAME_SUMMARY.md     # Summary report → Archive immediately
```

#### Implementation Guides (archive after implementation)
```
FEATURE_IMPLEMENTATION.md   # Active during implementation
                           # → Archive when feature is live
```

#### Reference Documents (keep if active, archive if superseded)
```
API_REFERENCE.md           # Keep if API is active
                          # → Archive if API is deprecated
```

### **Version Control**
**Don't do this:**
- ❌ `README.md.old`
- ❌ `script.py.bak`
- ❌ `docker-compose.yml.backup`

**Do this instead:**
- ✅ Use Git for version control
- ✅ Move old versions to ARK if needed for reference
- ✅ Delete temporary backups after verification

### **Temporary Files**
**Never commit these:**
- ❌ `tmp*` files
- ❌ `NUL` files
- ❌ `tmpclaude-*` directories
- ❌ `__pycache__/` directories
- ❌ `node_modules/` directories

**Cleanup automation:** See `.gitignore` and cleanup scripts

---

## 🔄 Document Lifecycle Management

### **Phase 1: Creation**
**Ask before creating:**
1. Does a file for this purpose already exist? (Update instead of create)
2. Is this a temporary note or permanent documentation?
3. Where in the structure does this belong?

**Naming checklist:**
- [ ] Name clearly describes content
- [ ] Follows naming convention for its category
- [ ] No duplicate/similar files exist
- [ ] Appropriate file extension

### **Phase 2: Active Use**
**Maintenance rules:**
- Update existing files instead of creating new versions
- Keep related information consolidated
- Use headers/sections for organization within files
- Date-stamp updates if tracking changes

### **Phase 3: Completion**
**Archive triggers:**
- Project marked as complete
- Documentation superseded
- Implementation finished
- Feature deprecated

**Archive process:**
1. Move to appropriate ARK subfolder
2. Update any links/references
3. Remove from active directory
4. Document in archive index (ARK README.md)

### **Phase 4: Deletion**
**Only delete:**
- Temporary files after verification
- True duplicates (identical content)
- Failed/abandoned drafts
- System-generated temp files

**Never delete:**
- Historical documentation (archive instead)
- Completed project files (archive instead)
- Working code/scripts (archive if deprecated)

---

## 🚫 Anti-Patterns to Avoid

### **1. Status Report Proliferation**
**Problem:** Creating completion/summary reports at project milestones that pile up

**Bad:**
```
S:\JAN\
├── PHASE1_COMPLETE.md
├── PHASE2_COMPLETE.md
├── INTEGRATION_SUMMARY.md
├── FRONTEND_COMPLETE.md
├── BACKEND_COMPLETE.md
└── FINAL_SUMMARY.md
```

**Good:**
```
S:\JAN\
├── PROJECT_STATUS.md (updated continuously)
└── README.md (reflects current state)

S:\ARK\HISTORICAL_DOCS\
└── [Archive completed reports here]
```

### **2. Guide/Reference Duplication**
**Problem:** Creating multiple guides for similar purposes

**Bad:**
```
SETUP_GUIDE.md
INSTALLATION_GUIDE.md
GETTING_STARTED.md
QUICKSTART.md
INSTALL.md
```

**Good:**
```
README.md (overview with links)
INSTALL.md (detailed installation)
QUICKSTART.md (5-minute start)
```

### **3. Implementation Document Sprawl**
**Problem:** Creating separate docs for every implementation task

**Bad:**
```
FEATURE_A_IMPLEMENTATION.md
FEATURE_B_IMPLEMENTATION.md
FEATURE_C_IMPLEMENTATION.md
BUGFIX_IMPLEMENTATION.md
```

**Good:**
```
CHANGELOG.md (track all changes)
docs/ARCHITECTURE.md (explain structure)
[Move completed implementation docs to ARK]
```

### **4. Temporary File Accumulation**
**Problem:** Leaving temp files, backups, and drafts

**Bad:**
```
script.py
script_backup.py
script_old.py
script_test.py
script_final.py
script_final_v2.py
```

**Good:**
```
script.py (current version)
[Use Git for history]
[Delete temp versions]
```

---

## ✅ Creation Decision Tree

### Before Creating ANY New File:

```
┌─ Does a file for this already exist?
│  ├─ YES → Update existing file
│  └─ NO ↓
│
┌─ Is this temporary (< 1 day)?
│  ├─ YES → Use a temp name (tmp_*) and delete after use
│  └─ NO ↓
│
┌─ Is this documentation or code?
│  ├─ DOCUMENTATION ↓
│  │  ┌─ Is it a status/completion report?
│  │  │  ├─ YES → Create, but plan to archive immediately
│  │  │  └─ NO ↓
│  │  ┌─ Is it active guidance or reference?
│  │  │  ├─ YES → Create in appropriate location
│  │  │  └─ NO → Reconsider if needed
│  │
│  └─ CODE ↓
│     ┌─ Is it part of an existing project?
│     │  ├─ YES → Create in that project's directory
│     │  └─ NO → Create new project folder first
│
└─ Create file with proper naming convention
```

---

## 🤖 AI Assistant Guidelines

### For Claude/Cursor AI:

**When user requests documentation:**
1. **Check if it exists first** - Search codebase before creating
2. **Update instead of create** - If similar doc exists, update it
3. **Ask about lifecycle** - "Should this be permanent or temporary?"
4. **Suggest consolidation** - "This could be added to existing [file]"

**When creating completion reports:**
1. Create the report
2. Immediately suggest archival: "This should be moved to ARK\HISTORICAL_DOCS\"
3. Execute archival in same session if possible

**When working across sessions:**
1. Check for duplicate/similar files from previous sessions
2. Consolidate instead of creating parallel documentation
3. Clean up temp files from previous sessions

**File creation checklist:**
- [ ] Searched for existing similar files
- [ ] Confirmed new file is necessary
- [ ] Used proper naming convention
- [ ] Placed in correct directory
- [ ] Planned lifecycle (active vs. archive)

---

## 🔧 Automation & Tooling

### **Cleanup Scripts**

#### Daily Cleanup (run at end of day)
```powershell
# S:\JAN\scripts\daily-cleanup.ps1

# Remove temp files
Get-ChildItem -Path "S:\JAN" -Recurse -Filter "tmp*" | Remove-Item -Force
Get-ChildItem -Path "S:\JAN" -Recurse -Filter "NUL" | Remove-Item -Force

# Remove tmpclaude directories
Get-ChildItem -Path "S:\" -Filter "tmpclaude-*" -Directory -Recurse | Remove-Item -Recurse -Force

# Report orphaned files
Write-Host "Cleanup complete. Review any remaining .old or .bak files."
```

#### Weekly Archive Check (run weekly)
```powershell
# S:\JAN\scripts\weekly-archive-check.ps1

# Find completion reports at root
$completeFiles = Get-ChildItem -Path "S:\JAN" -Filter "*_COMPLETE*.md" -File
if ($completeFiles) {
    Write-Host "ARCHIVE NEEDED: Found $($completeFiles.Count) completion reports"
    $completeFiles | ForEach-Object { Write-Host "  - $($_.Name)" }
}

# Find summary reports at root
$summaryFiles = Get-ChildItem -Path "S:\JAN" -Filter "*_SUMMARY*.md" -File
if ($summaryFiles) {
    Write-Host "ARCHIVE NEEDED: Found $($summaryFiles.Count) summary reports"
    $summaryFiles | ForEach-Object { Write-Host "  - $($_.Name)" }
}

# Find old implementation docs
$implFiles = Get-ChildItem -Path "S:\JAN" -Filter "*_IMPLEMENTATION*.md" -File
if ($implFiles) {
    Write-Host "REVIEW NEEDED: Found $($implFiles.Count) implementation docs"
    Write-Host "Are these still active or ready for archive?"
    $implFiles | ForEach-Object { Write-Host "  - $($_.Name)" }
}
```

### **Git Ignore Standards**

#### S:\JAN\.gitignore
```gitignore
# Temporary files
tmp*
*.tmp
*.temp
NUL

# Backup files
*.bak
*.old
*.backup
*_backup*

# Claude temp directories
tmpclaude-*/

# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/

# Node
node_modules/
.next/
dist/

# System
.DS_Store
Thumbs.db
*.swp
*.swo

# Logs
*.log
npm-debug.log*
yarn-debug.log*
```

---

## 📋 Project Checklist Templates

### **Starting New Project**

**Before creating any files:**
- [ ] Project name decided
- [ ] Location chosen (S:\JAN\project-name\ or separate?)
- [ ] README.md planned (will be first file)
- [ ] Structure defined (folders needed)
- [ ] Archive plan considered (when will this be archived?)

**Initial files (in order):**
1. `README.md` - Project overview
2. `LICENSE` (if applicable)
3. Core code/content
4. Additional documentation only if needed

### **Ending Project / Feature Completion**

**Before marking complete:**
- [ ] All active code/content finalized
- [ ] README.md updated with final state
- [ ] Completion report created (if needed)
- [ ] Archive location identified (ARK subfolder)
- [ ] References updated (links to new archive location)
- [ ] Files moved to archive
- [ ] Active directory cleaned

---

## 🎓 Training: Recognize Clutter Patterns

### **Pattern 1: The "Complete" Cascade**
**Symptom:** Multiple completion documents
```
FEATURE_COMPLETE.md
PHASE1_COMPLETE.md
INTEGRATION_COMPLETE.md
FRONTEND_COMPLETE.md
```
**Solution:** Create one, archive immediately. Update README.md for current state.

### **Pattern 2: The "Guide" Explosion**
**Symptom:** Overlapping guides
```
SETUP.md
INSTALL.md
GETTING_STARTED.md
QUICKSTART.md
HOW_TO_INSTALL.md
```
**Solution:** Consolidate into README.md + detailed INSTALL.md only.

### **Pattern 3: The "Status" Sprawl**
**Symptom:** Historical status reports at root
```
STATUS_WEEK1.md
STATUS_WEEK2.md
PROGRESS_REPORT.md
```
**Solution:** One STATUS.md updated continuously. Archive old ones.

### **Pattern 4: The "Implementation" Trail**
**Symptom:** Implementation docs for every change
```
ADD_FEATURE_X_IMPLEMENTATION.md
FIX_BUG_Y_IMPLEMENTATION.md
UPDATE_Z_IMPLEMENTATION.md
```
**Solution:** Use CHANGELOG.md. Archive implementation docs after completion.

---

## 📊 Health Metrics

### **Healthy Workspace Indicators**
- ✅ < 20 .md files at S:\JAN root
- ✅ No *_COMPLETE.md or *_SUMMARY.md at root
- ✅ No tmp*, NUL, or *.bak files
- ✅ Clear README.md describes current state
- ✅ Projects in dedicated subdirectories
- ✅ ARK contains historical content

### **Warning Signs**
- ⚠️ > 50 .md files at root
- ⚠️ Multiple completion reports visible
- ⚠️ .old or .bak files present
- ⚠️ tmpclaude-* directories not cleaned
- ⚠️ Duplicate guide names (INSTALL vs SETUP vs QUICKSTART)

### **Critical Issues**
- 🚨 > 100 .md files at root
- 🚨 Completion reports older than 1 week at root
- 🚨 No clear project structure
- 🚨 Active and archived content mixed

---

## 🔄 Weekly Maintenance Routine

### **Every Sunday (or end of week):**

1. **Audit root directory**
   ```powershell
   cd S:\JAN
   Get-ChildItem -File | Measure-Object
   # Should be < 20 files
   ```

2. **Identify archivable docs**
   ```powershell
   Get-ChildItem -Filter "*_COMPLETE*.md"
   Get-ChildItem -Filter "*_SUMMARY*.md"
   # Move to ARK if found
   ```

3. **Clean temp files**
   ```powershell
   Get-ChildItem -Recurse -Filter "tmp*" | Remove-Item -Force
   Get-ChildItem -Recurse -Filter "NUL" | Remove-Item -Force
   ```

4. **Update archive index**
   - Update S:\ARK\README.md if new content archived

5. **Review project status**
   - Are any projects complete? → Archive
   - Are any docs outdated? → Update or archive
   - Are any temp files lingering? → Delete

---

## 📖 Quick Reference

### **When to CREATE:**
- New project → Create project folder + README.md
- New feature → Update existing docs, create only if necessary
- Active guidance → Create if no equivalent exists
- Temporary work → Use tmp_ prefix

### **When to UPDATE:**
- Status changes → Update README.md or STATUS.md
- Feature modifications → Update CHANGELOG.md
- Documentation corrections → Update existing doc
- Reference changes → Update existing reference

### **When to ARCHIVE:**
- Project complete → Move to ARK
- Documentation superseded → Move old version to ARK
- Feature deprecated → Archive implementation docs
- Reports finalized → Archive immediately

### **When to DELETE:**
- Temporary files verified → Delete
- True duplicates → Delete (keep one)
- Failed drafts → Delete
- System temp files → Delete

---

## 🎯 Success Criteria

**You have a solid foundation when:**
- ✅ You can find any file quickly
- ✅ Every file has a clear purpose
- ✅ No confusion about what's current vs. historical
- ✅ Root directories are clean (< 20 files)
- ✅ New files follow conventions automatically
- ✅ Archive process is automatic
- ✅ No duplicate/redundant documentation

---

## 🔗 Related Documents

- `S:\ARK\README.md` - Archive index and guide
- `S:\JAN\README.md` - Project overview
- `S:\JAN\FOR_CLAUDE.md` - AI assistant context
- `S:\SIYEM\README.md` - SIYEM production system

---

**Last Updated:** 2026-01-15  
**Review Frequency:** Quarterly  
**Maintainer:** System administrator

**This is a living document. Update as organizational needs evolve.**

