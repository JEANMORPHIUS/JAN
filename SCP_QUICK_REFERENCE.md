# SCP QUICK REFERENCE
## File Transfer Options

**Date:** 2026-01-26  
**Purpose:** Quick reference for file transfer needs

---

## 📋 FILE TRANSFER OPTIONS

### Option 1: Copy to Notebook

**For Notebook Content Creation:**

**Files to Copy:**
- `NOTEBOOK_SPIRITUAL_CODEBASE_BLUEPRINT.md` → Upload to Notebook
- `NOTEBOOK_CONTENT_CREATION_PROMPTS.md` → Reference for prompts

**Method:**
- Direct upload via Notebook interface
- Or copy file path: `S:\JAN\NOTEBOOK_SPIRITUAL_CODEBASE_BLUEPRINT.md`

---

### Option 2: Windows File Copy (PowerShell)

**Copy Notebook files:**
```powershell
# Copy blueprint to another location
Copy-Item "S:\JAN\NOTEBOOK_SPIRITUAL_CODEBASE_BLUEPRINT.md" -Destination "C:\Users\janmu\Documents\Notebook\"
```

**Copy execution plans:**
```powershell
Copy-Item "S:\JAN\GET_THE_SHOW_ON_THE_ROAD.md" -Destination "C:\Users\janmu\Documents\"
Copy-Item "S:\JAN\QUICK_START_EXECUTION.md" -Destination "C:\Users\janmu\Documents\"
```

---

### Option 3: SCP (Secure Copy Protocol)

**Note:** There's a security script `scp.bat` that blocks SCP. If you need SCP:

**Windows (using OpenSSH):**
```bash
# Copy file to remote server
scp S:\JAN\NOTEBOOK_SPIRITUAL_CODEBASE_BLUEPRINT.md user@host:/path/to/destination/

# Copy directory
scp -r S:\JAN\SIYEM\output\spiritual_codebase user@host:/path/to/destination/
```

**If SCP is blocked:**
- Check `C:\Users\janmu\scp.bat` - it's an intentional security block
- Use alternative: PowerShell `Copy-Item` or `robocopy`

---

### Option 4: Quick File Access

**For Notebook:**
1. Open Notebook
2. Add source document
3. Browse to: `S:\JAN\NOTEBOOK_SPIRITUAL_CODEBASE_BLUEPRINT.md`
4. Upload

**For Quick Reference:**
- All files are in `S:\JAN\`
- Notebook blueprint: `NOTEBOOK_SPIRITUAL_CODEBASE_BLUEPRINT.md`
- Prompts: `NOTEBOOK_CONTENT_CREATION_PROMPTS.md`
- Execution plan: `GET_THE_SHOW_ON_THE_ROAD.md`
- Quick start: `QUICK_START_EXECUTION.md`

---

## 🎯 MOST LIKELY NEED

**For Notebook Content Creation:**

1. **Upload to Notebook:**
   - File: `S:\JAN\NOTEBOOK_SPIRITUAL_CODEBASE_BLUEPRINT.md`
   - Method: Direct upload via Notebook interface
   - Path: Browse to `S:\JAN\` and select the file

2. **Use Prompts:**
   - File: `S:\JAN\NOTEBOOK_CONTENT_CREATION_PROMPTS.md`
   - Copy master prompt from the file
   - Use in Notebook

---

## ✅ QUICK ACTION

**If you need to copy files for Notebook:**

```powershell
# Just open the file in Notebook and upload directly
# Or if copying to another location:
Copy-Item "S:\JAN\NOTEBOOK_SPIRITUAL_CODEBASE_BLUEPRINT.md" -Destination "C:\Users\janmu\Documents\"
```

**If you need SCP for remote transfer:**
- Check if `scp.bat` security block is still needed
- Use PowerShell `Copy-Item` as alternative
- Or use `robocopy` for network transfers

---

**What do you need SCP for?** Let me know and I'll provide the exact command.
