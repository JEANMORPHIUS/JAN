#!/usr/bin/env python3
"""VERIFY NO SECRETS IN TRACKED FILES
Check for sensitive data before committing

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE TRUTH:
PROTECT SENSITIVE DATA
NO SECRETS IN REPO
SAFE TO COMMIT

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity


PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    Path, setup_logging, standard_main
)

import subprocess
import re
from pathlib import Path

def check_tracked_files():
    """Check tracked files for sensitive patterns"""
    print("=" * 80)
    print("VERIFY NO SECRETS IN TRACKED FILES")
    print("PROTECT SENSITIVE DATA")
    print("=" * 80)
    print()
    
    # Get tracked files
    try:
        result = subprocess.run(
            ["git", "ls-files"],
            capture_output=True,
            text=True,
            cwd=Path(__file__).parent.parent
        )
        tracked_files = result.stdout.strip().split('\n')
    except Exception as e:
        print(f"Error getting tracked files: {e}")
        return
    
    # Sensitive patterns
    sensitive_patterns = [
        r'pk\.eyJ[0-9A-Za-z_-]+',  # Mapbox tokens
        r'sk_live_[0-9A-Za-z]+',  # Stripe live keys
        r'sk_test_[0-9A-Za-z]+',  # Stripe test keys
        r'AIza[0-9A-Za-z_-]+',  # Google API keys
        r'AKIA[0-9A-Z]{16}',  # AWS access keys
        r'password\s*[:=]\s*["\']?[^"\'\s]+',  # Passwords
        r'api[_-]?key\s*[:=]\s*["\']?[^"\'\s]+',  # API keys
        r'secret\s*[:=]\s*["\']?[^"\'\s]+',  # Secrets
        r'token\s*[:=]\s*["\']?[^"\'\s]+',  # Tokens
    ]
    
    issues = []
    
    for file_path in tracked_files:
        if not file_path:
            continue
        
        # Skip binary files and large files
        if any(file_path.endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.gif', '.pdf', '.zip', '.exe']):
            continue
        
        file_full_path = Path(__file__).parent.parent / file_path
        
        if not file_full_path.exists():
            continue
        
        try:
            # Read file (limit size)
            if file_full_path.stat().st_size > 1_000_000:  # 1MB limit
                continue
            
            content = file_full_path.read_text(encoding='utf-8', errors='ignore')
            
            for pattern in sensitive_patterns:
                matches = re.finditer(pattern, content, re.IGNORECASE)
                for match in matches:
                    # Check if it's in a comment or example
                    line_start = content.rfind('\n', 0, match.start()) + 1
                    line = content[line_start:content.find('\n', match.end())]
                    
                    # Skip if it's clearly an example or comment
                    if any(indicator in line.lower() for indicator in ['example', 'placeholder', 'your_', 'replace', '//', '#']):
                        continue
                    
                    issues.append({
                        "file": file_path,
                        "pattern": pattern,
                        "match": match.group()[:20] + "..." if len(match.group()) > 20 else match.group(),
                        "line": line.strip()[:100]
                    })
        except Exception as e:
            # Skip files that can't be read
            continue
    
    if issues:
        print("[WARNING] POTENTIAL SECRETS FOUND:")
        print("-" * 80)
        for issue in issues:
            print(f"File: {issue['file']}")
            print(f"Pattern: {issue['pattern']}")
            print(f"Match: {issue['match']}")
            print(f"Line: {issue['line']}")
            print()
        print("=" * 80)
        print("[WARNING] REVIEW THESE FILES BEFORE COMMITTING")
        print("=" * 80)
    else:
        print("[OK] NO SECRETS FOUND IN TRACKED FILES")
        print("=" * 80)
        print("SAFE TO COMMIT")
        print("=" * 80)
    
    # Check ignored files
    print()
    print("CHECKING IGNORED FILES:")
    print("-" * 80)
    
    sensitive_files = [
        "world-history-app/.env.local",
        "SIYEM/output/financial_data.json",
        "SIYEM/output/free_will_data.json"
    ]
    
    for file_path in sensitive_files:
        try:
            result = subprocess.run(
                ["git", "check-ignore", "-v", file_path],
                capture_output=True,
                text=True,
                cwd=Path(__file__).parent.parent
            )
            if result.returncode == 0:
                print(f"[OK] {file_path} - IGNORED ({result.stdout.strip()})")
            else:
                print(f"[WARNING] {file_path} - NOT IGNORED (NEEDS ATTENTION)")
        except Exception:
            print(f"⚠️ {file_path} - COULD NOT VERIFY")

if __name__ == "__main__":
    check_tracked_files()
