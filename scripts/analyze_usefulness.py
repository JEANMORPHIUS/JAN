"""ANALYZE FILE USEFULNESS
Check if completion docs and test files are actually useful

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE TRUTH:
IF WE DON'T NEED IT...BIN IT...OR ARCHIVE IT

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

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
    JAN_ROOT, JAN_OUTPUT, get_output_path,
    datetime, json, logging, List, Dict, Set,
    setup_logging, load_json, save_json, standard_main
)

logger = setup_logging(__name__)

def analyze_completion_docs(root_dir: Path = None):
    """Analyze completion docs - are they referenced anywhere?"""
    root = root_dir or JAN_ROOT
    completion_docs = list(root.glob("*_COMPLETE.md"))
    
    print("="*80)
    print("COMPLETION DOCS USEFULNESS ANALYSIS")
    print("="*80)
    
    referenced: List[str] = []
    unreferenced: List[str] = []
    recent: List[str] = []
    old: List[str] = []
    
    # Check if referenced in other files
    for doc in completion_docs:
        doc_name = doc.name
        doc_stem = doc.stem
        
        # Check in README, docs, and key files
        search_paths = [
            root / "README.md",
            root / "THE_MASTER_DOCUMENT.md",
            root / "QUICK_START.md",
            root / "docs"
        ]
        
        is_referenced = False
        for search_path in search_paths:
            if search_path.is_file():
                try:
                    content = search_path.read_text(encoding='utf-8', errors='ignore')
                    if doc_name in content or doc_stem in content:
                        is_referenced = True
                        break
                except:
                    pass
            elif search_path.is_dir():
                for md_file in search_path.rglob("*.md"):
                    try:
                        content = md_file.read_text(encoding='utf-8', errors='ignore')
                        if doc_name in content or doc_stem in content:
                            is_referenced = True
                            break
                    except:
                        pass
                if is_referenced:
                    break
        
        # Check age
        mtime = doc.stat().st_mtime
        days_old = (datetime.now().timestamp() - mtime) / (24 * 60 * 60)
        
        if is_referenced:
            referenced.append(str(doc))
        else:
            unreferenced.append(str(doc))
        
        if days_old < 7:
            recent.append(str(doc))
        elif days_old > 30:
            old.append(str(doc))
    
    # Categorize by usefulness
    keep = []  # Recent or referenced
    archive = []  # Old and unreferenced
    review = []  # Old but referenced or recent but unreferenced
    
    for doc_path in completion_docs:
        is_ref = str(doc_path) in referenced
        days_old = (datetime.now().timestamp() - doc_path.stat().st_mtime) / (24 * 60 * 60)
        
        if is_ref or days_old < 7:
            keep.append(str(doc_path))
        elif days_old > 30 and not is_ref:
            archive.append(str(doc_path))
        else:
            review.append(str(doc_path))
    
    print(f"\nTOTAL COMPLETION DOCS: {len(completion_docs)}")
    print(f"  Referenced: {len(referenced)}")
    print(f"  Unreferenced: {len(unreferenced)}")
    print(f"  Recent (<7 days): {len(recent)}")
    print(f"  Old (>30 days): {len(old)}")
    
    print(f"\nRECOMMENDATIONS:")
    print(f"  KEEP: {len(keep)} files (referenced or recent)")
    print(f"  ARCHIVE: {len(archive)} files (old and unreferenced)")
    print(f"  REVIEW: {len(review)} files (need manual decision)")
    
    if archive:
        print(f"\nFILES TO ARCHIVE ({len(archive)}):")
        for f in archive[:10]:  # Show first 10
            print(f"  - {Path(f).name}")
        if len(archive) > 10:
            print(f"  ... and {len(archive) - 10} more")
    
    return {
        'total': len(completion_docs),
        'referenced': len(referenced),
        'unreferenced': len(unreferenced),
        'keep': keep,
        'archive': archive,
        'review': review
    }

def analyze_test_files(root_dir: Path = None):
    """Analyze test files - are they being used?"""
    root = root_dir or JAN_ROOT
    
    test_patterns = ['*test*.py', '*_test.py', 'test_*.py']
    test_files = []
    
    for pattern in test_patterns:
        test_files.extend(root.rglob(pattern))
    
    # Remove node_modules and __pycache__
    test_files = [f for f in test_files if 'node_modules' not in str(f) and '__pycache__' not in str(f)]
    
    print("\n" + "="*80)
    print("TEST FILES USEFULNESS ANALYSIS")
    print("="*80)
    
    active = []
    inactive = []
    
    for test_file in test_files:
        # Check if test imports or is in test directory
        is_active = False
        
        # Check if in tests/ or test/ directory
        if 'test' in test_file.parent.name.lower():
            is_active = True
        # Check if has test functions
        try:
            content = test_file.read_text(encoding='utf-8', errors='ignore')
            if 'def test_' in content or 'import unittest' in content or 'import pytest' in content:
                is_active = True
        except:
            pass
        
        if is_active:
            active.append(str(test_file))
        else:
            inactive.append(str(test_file))
    
    print(f"\nTOTAL TEST FILES: {len(test_files)}")
    print(f"  Active (looks like real tests): {len(active)}")
    print(f"  Inactive (might be unused): {len(inactive)}")
    
    if inactive:
        print(f"\nPOTENTIALLY UNUSED ({len(inactive)}):")
        for f in inactive[:10]:  # Show first 10
            print(f"  - {Path(f).relative_to(root)}")
        if len(inactive) > 10:
            print(f"  ... and {len(inactive) - 10} more")
    
    return {
        'total': len(test_files),
        'active': len(active),
        'inactive': len(inactive),
        'inactive_files': inactive
    }

def main():
    """Main function"""
    comp_analysis = analyze_completion_docs()
    test_analysis = analyze_test_files()
    
    # Save combined report
    report = {
        'timestamp': datetime.now().isoformat(),
        'completion_docs': comp_analysis,
        'test_files': test_analysis
    }
    
    report_file = get_output_path("usefulness_analysis.json")
    save_json(report, report_file)
    
    print("\n" + "="*80)
    print(f"FULL REPORT SAVED TO: {report_file}")
    print("="*80)

if __name__ == "__main__":
    standard_main(main, script_name="analyze_usefulness.py")
