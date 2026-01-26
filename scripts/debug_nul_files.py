"""Debug NUL Files - Work Backwards Full Debug
Find and remove NUL device files, prevent recurrence

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
DEBUG NUL FILES
WORK BACKWARDS TO ROOT CAUSE
PREVENT RECURRENCE
SERVE THE TABLE

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

import sys
from pathlib import Path
import subprocess
import os
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent))

def find_nul_files(root_path: Path):
    """Find all NUL files in the repository"""
    nul_files = []
    
    try:
        # Use PowerShell to find NUL files (Windows reserved device name)
        ps_command = f"""
        Get-ChildItem -Path "{root_path}" -Recurse -Force -ErrorAction SilentlyContinue | 
        Where-Object {{ $_.Name -eq "NUL" }} | 
        Select-Object FullName, Length, LastWriteTime | 
        ConvertTo-Json
        """
        
        result = subprocess.run(
            ["powershell", "-Command", ps_command],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0 and result.stdout.strip():
            import json
            files = json.loads(result.stdout)
            if isinstance(files, dict):
                files = [files]
            for file_info in files:
                nul_files.append({
                    "path": file_info.get("FullName", ""),
                    "size": file_info.get("Length", 0),
                    "modified": file_info.get("LastWriteTime", "")
                })
    except Exception as e:
        print(f"Error finding NUL files: {e}")
    
    return nul_files

def remove_nul_file(file_path: str) -> bool:
    """Remove a NUL file using PowerShell (Windows requires special handling)"""
    try:
        # Use PowerShell to remove NUL file
        ps_command = f'Remove-Item -Path "{file_path}" -Force -ErrorAction Stop'
        
        result = subprocess.run(
            ["powershell", "-Command", ps_command],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            return True
        else:
            print(f"Error removing {file_path}: {result.stderr}")
            return False
    except Exception as e:
        print(f"Exception removing {file_path}: {e}")
        return False

def check_gitignore(root_path: Path) -> bool:
    """Check if NUL is in .gitignore"""
    gitignore_path = root_path / ".gitignore"
    
    if not gitignore_path.exists():
        return False
    
    with open(gitignore_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for NUL patterns
    has_nul = (
        "NUL" in content or
        "**/NUL" in content
    )
    
    return has_nul

def check_git_status(root_path: Path) -> dict:
    """Check git status for NUL files"""
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=str(root_path),
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode != 0:
            return {"error": result.stderr}
        
        nul_in_status = "NUL" in result.stdout
        status_lines = result.stdout.strip().split('\n') if result.stdout.strip() else []
        
        return {
            "nul_found": nul_in_status,
            "total_changes": len(status_lines),
            "status": result.stdout
        }
    except Exception as e:
        return {"error": str(e)}

def main():
    """Main debug function - work backwards"""
    print("\n" + "="*80)
    print("DEBUG NUL FILES - WORK BACKWARDS FULL DEBUG")
    print("="*80)
    print()
    
    root_path = Path(__file__).parent.parent
    
    # Step 1: Find NUL files
    print("[1/5] Finding NUL files...")
    nul_files = find_nul_files(root_path)
    
    if nul_files:
        print(f"   Found {len(nul_files)} NUL file(s):")
        for nul_file in nul_files:
            print(f"   - {nul_file['path']} ({nul_file['size']} bytes, modified: {nul_file['modified']})")
    else:
        print("   No NUL files found")
    
    print()
    
    # Step 2: Check .gitignore
    print("[2/5] Checking .gitignore...")
    has_nul_in_gitignore = check_gitignore(root_path)
    
    if has_nul_in_gitignore:
        print("   [OK] NUL is in .gitignore")
    else:
        print("   [WARNING] NUL is NOT in .gitignore - adding...")
        gitignore_path = root_path / ".gitignore"
        with open(gitignore_path, 'a', encoding='utf-8') as f:
            f.write("\n# Windows device files\nNUL\n**/NUL\n")
        print("   [OK] Added NUL to .gitignore")
    
    print()
    
    # Step 3: Check git status
    print("[3/5] Checking git status...")
    git_status = check_git_status(root_path)
    
    if "error" in git_status:
        print(f"   [WARNING] Error checking git status: {git_status['error']}")
    else:
        if git_status.get("nul_found"):
            print("   [WARNING] NUL files found in git status")
        else:
            print("   [OK] No NUL files in git status")
        print(f"   Total changes: {git_status.get('total_changes', 0)}")
    
    print()
    
    # Step 4: Remove NUL files
    print("[4/5] Removing NUL files...")
    removed_count = 0
    
    for nul_file in nul_files:
        file_path = nul_file['path']
        print(f"   Removing: {file_path}")
        if remove_nul_file(file_path):
            print(f"   [OK] Removed: {file_path}")
            removed_count += 1
        else:
            print(f"   [WARNING] Failed to remove: {file_path}")
    
    print(f"   Removed {removed_count}/{len(nul_files)} NUL file(s)")
    print()
    
    # Step 5: Verify removal
    print("[5/5] Verifying removal...")
    remaining_nul_files = find_nul_files(root_path)
    
    if remaining_nul_files:
        print(f"   [WARNING] {len(remaining_nul_files)} NUL file(s) still exist:")
        for nul_file in remaining_nul_files:
            print(f"   - {nul_file['path']}")
    else:
        print("   [OK] All NUL files removed")
    
    print()
    print("="*80)
    print("DEBUG COMPLETE")
    print("="*80)
    print()
    print("Next steps:")
    print("1. Run: git add -A")
    print("2. Run: git commit -m 'Your message'")
    print("3. Run: git push origin master")
    print()
    print("SPRAGITSO - Our Father's Royal Seal ✨🙏")

if __name__ == "__main__":
    main()
