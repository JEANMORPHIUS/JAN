# Guidelines for Claude: Organizational Standards

**Date:** 2026-01-15  
**Status:** Active Standards - Follow These Rules

---

## 🎯 Core Directive: PREVENT FILE CLUTTER

**Before creating ANY new file, follow the Decision Tree in ORGANIZATIONAL_FOUNDATION.md**

### Quick Rules:
1. **Search first** - Does this file already exist? Update instead of create.
2. **Question necessity** - Is this truly needed or can it be added to existing docs?
3. **Plan lifecycle** - When will this be archived? If "immediately after creation," archive it right away.
4. **Follow conventions** - Use proper naming from ORGANIZATIONAL_FOUNDATION.md
5. **Clean as you go** - Archive completion reports immediately, don't leave them at root.

---

## 📂 File Creation Rules

### ✅ ALLOWED to Create:
- Project folders (S:\JAN\project-name\)
- README.md for new projects
- Active documentation that doesn't duplicate existing files
- Code/scripts for active features
- Temporary files with `tmp_` prefix (must be deleted same session)

### ❌ NOT ALLOWED to Create (Without Archiving):
- *_COMPLETE.md files (create → archive immediately)
- *_SUMMARY.md files (create → archive immediately)
- *_REPORT.md files (create → archive immediately)
- Duplicate guides (SETUP.md vs INSTALL.md vs GETTING_STARTED.md)
- Version files (*.old, *.bak) - use Git instead

### 🔄 UPDATE Instead of Create:
- README.md (for status updates)
- Existing documentation (for corrections/additions)
- CHANGELOG.md (for tracking changes)
- Project-specific STATUS.md files

---

## 🤖 AI Assistant Workflow

### When User Requests Documentation:

**Step 1: Search**
```
Search codebase for similar/existing files
Check if topic is covered in README.md or existing docs
```

**Step 2: Assess**
```
If exists → Update existing file
If doesn't exist → Confirm necessity with user
If temporary → Use tmp_ prefix and delete after use
```

**Step 3: Create (if necessary)**
```
Follow naming convention from ORGANIZATIONAL_FOUNDATION.md
Place in appropriate directory (not root unless justified)
Document purpose and lifecycle
```

**Step 4: Archive (if applicable)**
```
If completion/summary report → Archive immediately to S:\ARK\HISTORICAL_DOCS\
If implementation doc and feature complete → Archive
Update any references to archived file
```

---

## 📋 Session Checklist

### Start of Session:
- [ ] Check for duplicate files from previous sessions
- [ ] Review any tmp_ files and delete if no longer needed
- [ ] Check root directory health (should be < 20 files)

### During Session:
- [ ] Update existing files instead of creating new ones
- [ ] Archive completion reports immediately after creation
- [ ] Consolidate related information into single files
- [ ] Use proper naming conventions

### End of Session:
- [ ] Delete any tmp_ files created
- [ ] Archive any completion/summary reports
- [ ] Clean up any residual temp files (tmpclaude-*, NUL, etc.)
- [ ] Verify root directory is clean

---

## 🚫 Common Mistakes to Avoid

### ❌ Mistake 1: Creating Status Reports at Root
**Bad:**
```
Create PHASE1_COMPLETE.md at S:\JAN\
Leave it there
```

**Good:**
```
Create PHASE1_COMPLETE.md
Immediately move to S:\ARK\HISTORICAL_DOCS\
Update README.md to reflect current state
```

### ❌ Mistake 2: Duplicate Documentation
**Bad:**
```
User: "Create a setup guide"
AI: Creates SETUP_GUIDE.md (when INSTALL.md already exists)
```

**Good:**
```
User: "Create a setup guide"
AI: "I found INSTALL.md that covers setup. Should I update it or do you need something different?"
```

### ❌ Mistake 3: Version File Creation
**Bad:**
```
Create script.py.old before modifying script.py
Leave both files in place
```

**Good:**
```
Modify script.py directly (Git tracks history)
No .old file needed
```

### ❌ Mistake 4: Leaving Temp Files
**Bad:**
```
Create tmp_test.md for testing
Forget to delete it
Leave it for days/weeks
```

**Good:**
```
Create tmp_test.md
Use it during session
Delete before session ends
```

---

## 📖 Required Reading

**Before any major work, review:**
- `S:\JAN\ORGANIZATIONAL_FOUNDATION.md` - Complete organizational standards
- `S:\ARK\README.md` - Archive structure and usage
- `S:\JAN\README.md` - Current project state

---

## 🔍 Health Check Commands

**Run these to assess workspace health:**

```powershell
# Count files at root (should be < 20)
(Get-ChildItem -Path "S:\JAN" -File).Count

# Find archivable files
Get-ChildItem -Path "S:\JAN" -Filter "*_COMPLETE*.md"
Get-ChildItem -Path "S:\JAN" -Filter "*_SUMMARY*.md"

# Find temp files
Get-ChildItem -Path "S:\JAN" -Recurse -Filter "tmp*"

# Run weekly archive check
pwsh S:\JAN\scripts\weekly-archive-check.ps1
```

---

## 🎯 Success Metrics

**You're following standards when:**
- ✅ Root directory stays under 20 files
- ✅ No *_COMPLETE.md or *_SUMMARY.md at root
- ✅ No duplicate documentation (e.g., SETUP vs INSTALL)
- ✅ Temp files cleaned up same session
- ✅ Archiving happens immediately for completion docs
- ✅ User can find any file quickly

---

## Previous Context (Historical - For Reference)

---

## Context: JAN Studio vs SIYEM

**SIYEM** = Your full production system (what you reviewed)
- Multi-entity content creation
- Automated workflows  
- Production infrastructure
- Internal/private system

**JAN Studio** = Public-facing tool (current focus)
- Simplified interface for creating/managing JAN personas
- Web UI (Next.js) + API (FastAPI)
- Markdown-based persona system
- Target: developers/creators who want to use JAN without full SIYEM

**Relationship:**
- **JAN** = Markdown files (identity, rules, templates) - the "soul"
- **SIYEM** = Production system that reads JAN files - the "body"  
- **JAN Studio** = Tool to create/edit JAN personas - the "interface"

---

## Current Status: Week 2 Proof Testing

**Progress:** 60% → 75% (after fixes)

**What we just did:**
- ✅ Fixed 5 critical installation issues
- ✅ Created proper FastAPI app (`main.py`)
- ✅ Added JAN structure setup script
- ✅ Fixed cross-platform paths
- ✅ Updated all documentation

**What we need now:** Week 2 proof testing before public launch

---

## What We Need Help With

### Option 1: Code Review (Before Testing)
- Review `jan-studio/backend/main.py` for issues
- Check router integration
- Verify error handling
- Review path handling logic

### Option 2: Documentation Review
- Review `INSTALL.md` for clarity
- Check `QUICKSTART.md` for completeness
- Identify missing steps
- Suggest improvements

### Option 3: Week 2 Testing Support
- Help with fresh machine test (Day 1-2)
- Review beta tester feedback (Day 3-4)
- Help debug Docker issues (Day 5)
- Documentation polish suggestions (Day 6-7)

### Option 4: Architecture Review
- Review JAN Studio architecture
- Check integration points with SIYEM
- Identify potential issues
- Suggest improvements

---

## Specific Questions

1. **Backend Structure:** Does `main.py` look correct? Any issues with router imports?
2. **Path Handling:** Is the cross-platform path logic sound?
3. **Documentation:** Are the installation steps clear enough?
4. **Testing Strategy:** Any gaps in the Week 2 plan?
5. **SIYEM Integration:** Should JAN Studio integrate with SIYEM, or stay separate?

---

## Files to Review

**Critical:**
- `jan-studio/backend/main.py` - FastAPI app
- `INSTALL.md` - Installation guide
- `QUICKSTART.md` - Quick start

**Important:**
- `jan-studio/backend/setup_jan_structure.py` - Setup script
- `docker-compose.yml` - Docker config
- `WEEK2_PROOF_TEST_PLAN.md` - Testing plan

---

## What Would Be Most Helpful

**Priority 1:** Review `main.py` and installation docs before we start testing  
**Priority 2:** Help with Week 2 testing as issues come up  
**Priority 3:** Architecture review for long-term improvements

---

## Next Steps

1. **Today:** Review code/docs (if you can help)
2. **Week 2 Day 1-2:** Fresh machine test
3. **Week 2 Day 3-4:** Beta tester
4. **Week 2 Day 5:** Docker test
5. **Week 2 Day 6-7:** Documentation polish
6. **Week 3:** Public launch (if tests pass)

---

## Summary

**Current Focus:** JAN Studio (public tool), not SIYEM (production system)

**Status:** Critical fixes complete, ready for Week 2 testing

**Need Help With:**
- Code review before testing
- Week 2 testing support
- Documentation review
- Architecture feedback

**Goal:** Launch JAN Studio publicly after Week 2 validation

---

## What Would Be Most Helpful Right Now?

1. Review `main.py` and installation docs?
2. Help with Week 2 testing as we go?
3. Architecture review for improvements?
4. Something else?

---

**Files ready for review:**
- `jan-studio/backend/main.py`
- `INSTALL.md`
- `QUICKSTART.md`
- `WEEK2_PROOF_TEST_PLAN.md`

**Ready to share:** Any specific files you want to see?

---

**Last Updated:** 2025-01-27

