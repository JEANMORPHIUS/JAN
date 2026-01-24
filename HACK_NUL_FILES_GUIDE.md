# HACK NUL FILES - Complete Guide

**Date:** 2026-01-24  
**Status:** 🔥 NAUGHTY MODE ACTIVATED

---

## The Problem

NUL files are Windows reserved device names (like `/dev/null` in Unix). When you accidentally create a file named "NUL" (usually from redirecting output like `> NUL` or `2>NUL`), Windows treats it as a special device file, making it **extremely difficult to remove** using normal methods.

### Where They Are

- **S: Drive:** `S:\JAN\NUL`, `S:\JAN\jan-studio\NUL`
- **C: Drive:** `C:\NUL`, `C:\Users\janmu\NUL`, and **TONS** in `.bun` cache directories

---

## The Hacks

### Script 1: `hack_nul_files.ps1`

**Basic usage:**
```powershell
# S: drive (default)
.\scripts\hack_nul_files.ps1

# C: drive
.\scripts\hack_nul_files.ps1 -CDrive

# With force (tries nuclear options)
.\scripts\hack_nul_files.ps1 -CDrive -Force
```

**What it tries (8 methods):**

1. **`\\?\` prefix** - Bypasses Windows path normalization
   ```powershell
   cmd /c "del /F /Q `"\\?\C:\NUL`""
   ```

2. **Subst virtual drive** - Creates virtual drive, deletes from there
   ```powershell
   subst Z: C:\
   del /F /Q Z:\NUL
   subst Z: /D
   ```

3. **Robocopy mirror** - Mirrors empty directory over the parent
   ```powershell
   robocopy $emptyDir $parentDir /MIR
   ```

4. **Fsutil** - Uses Windows file system utilities
   ```powershell
   fsutil file setzerodata offset=0 length=0 "C:\NUL"
   ```

5. **.NET DeleteFile** - Direct .NET API call
   ```powershell
   [System.IO.File]::Delete("\\?\C:\NUL")
   ```

6. **Takeown + Icacls** - Nuclear option (requires admin)
   ```powershell
   takeown /F C:\NUL
   icacls C:\NUL /grant "${env:USERNAME}:F"
   del /F /Q C:\NUL
   ```

7. **Win32 API** - Direct Win32 DeleteFile call
   ```powershell
   [Win32]::DeleteFile("\\?\C:\NUL")
   ```

8. **8.3 short path** - Uses old DOS 8.3 filename format
   ```powershell
   $shortPath = $fs.GetFile("C:\NUL").ShortPath
   del /F /Q $shortPath
   ```

### Script 2: `hack_c_drive_nul_files.ps1`

**Finds and removes ALL NUL files on C: drive:**

```powershell
# Dry run (see what would be deleted)
.\scripts\hack_c_drive_nul_files.ps1 -DryRun

# Actually remove them
.\scripts\hack_c_drive_nul_files.ps1

# With force (tries Win32 API)
.\scripts\hack_c_drive_nul_files.ps1 -Force
```

---

## Manual Hacks (If Scripts Fail)

### Method 1: Boot into Safe Mode
1. Boot into Windows Safe Mode
2. Try: `cmd /c "del /F /Q \\?\C:\NUL"`

### Method 2: Linux Live USB
1. Boot from Linux live USB
2. Mount C: drive
3. Delete NUL files directly (Linux doesn't care about Windows device names)

### Method 3: Use Junction Points
```powershell
# Create junction point to "trap" the NUL file
mklink /J C:\nul_trap C:\temp
# Then delete the junction
rmdir C:\nul_trap
```

### Method 4: Use PowerShell with Raw Paths
```powershell
# Get file handle and delete
$rawPath = "\\?\C:\NUL"
Remove-Item -LiteralPath $rawPath -Force
```

### Method 5: Use Process Monitor
1. Download Process Monitor (Sysinternals)
2. Find what process is locking the NUL file
3. Kill the process
4. Delete the file

---

## Why This Happens

NUL files are created when:
- Scripts redirect output: `> NUL` or `2>NUL`
- Programs accidentally create files named "NUL"
- Copy operations go wrong
- Git operations on Windows

**Prevention:**
- Use `$null` in PowerShell instead of `> NUL`
- Use `Out-Null` in PowerShell
- Use `/dev/null` equivalents in cross-platform scripts
- Add `NUL` to `.gitignore` (already done ✅)

---

## Current Status

- ✅ NUL is in `.gitignore` (git will ignore them)
- ⚠️  NUL files still exist as phantom entries
- ✅ Git operations work (they're ignored)
- 🔥 Ready to hack them away!

---

## Quick Commands

```powershell
# Find all NUL files
Get-ChildItem -Path "C:\" -Filter "NUL" -Recurse -Force -ErrorAction SilentlyContinue

# Try to remove one
cmd /c "del /F /Q `"\\?\C:\NUL`""

# Use the hack script
.\scripts\hack_nul_files.ps1 -CDrive -Force
```

---

**SPRAGITSO - Our Father's Royal Seal** ✨🙏

**Naughty mode: ACTIVATED** 🔥
