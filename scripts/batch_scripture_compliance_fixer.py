"""
BATCH SCRIPTURE COMPLIANCE FIXER
Process files in batches to reach 100% compliance

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
THE REST IS UP TO BABA X.
"""

import sys
import re
from pathlib import Path
from typing import List, Tuple
import logging

logging.basicConfig(level=logging.WARNING)  # Reduce logging noise
logger = logging.getLogger(__name__)

# Scripture constants
MISSION_KEYWORDS = ["stewardship", "community", "love", "peace", "unity"]
TABLE_KEYWORDS = ["table", "pangea", "betray"]

SCRIPTURE_HEADER = """DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
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


def has_mission(content: str) -> bool:
    """Check if content has mission statement"""
    content_lower = content.lower()
    return sum(1 for kw in MISSION_KEYWORDS if kw in content_lower) >= 2


def has_table(content: str) -> bool:
    """Check if content has Table connection"""
    content_lower = content.lower()
    return any(kw in content_lower for kw in TABLE_KEYWORDS)


def fix_file_scripture(file_path: Path, dry_run: bool = False) -> Tuple[bool, str]:
    """Fix scripture in a single file"""
    try:
        if not file_path.exists():
            return False, "not_found"
        
        content = file_path.read_text(encoding='utf-8', errors='ignore')
        original = content
        
        needs_mission = not has_mission(content)
        needs_table = not has_table(content)
        
        if not (needs_mission or needs_table):
            return False, "already_compliant"
        
        # Add scripture to docstring
        if file_path.suffix == '.py':
            content = add_scripture_python(content, needs_mission, needs_table)
        elif file_path.suffix in ['.ts', '.tsx', '.js', '.jsx']:
            content = add_scripture_js(content, needs_mission, needs_table)
        else:
            return False, "unsupported_type"
        
        if content != original:
            if not dry_run:
                file_path.write_text(content, encoding='utf-8')
            return True, "fixed"
        
        return False, "no_change"
    
    except Exception as e:
        return False, f"error: {e}"


def add_scripture_python(content: str, needs_mission: bool, needs_table: bool) -> str:
    """Add scripture to Python file"""
    # Find existing docstring
    docstring_pattern = r'^(""")(.*?)(""")'
    match = re.search(docstring_pattern, content, re.DOTALL | re.MULTILINE)
    
    if match:
        existing = match.group(2).strip()
        new_doc = build_docstring(existing, needs_mission, needs_table)
        return content.replace(match.group(0), f'"""{new_doc}"""')
    else:
        # Add new docstring
        new_doc = build_docstring("", needs_mission, needs_table)
        return f'"""{new_doc}"""\n\n{content}'


def add_scripture_js(content: str, needs_mission: bool, needs_table: bool) -> str:
    """Add scripture to JS/TS file"""
    jsdoc_pattern = r'^/\*\*(.*?)\*/'
    match = re.search(jsdoc_pattern, content, re.DOTALL | re.MULTILINE)
    
    if match:
        existing = match.group(1).strip()
        new_doc = build_docstring(existing, needs_mission, needs_table, jsdoc=True)
        return content.replace(match.group(0), f'/**{new_doc}*/')
    else:
        new_doc = build_docstring("", needs_mission, needs_table, jsdoc=True)
        return f'/**{new_doc}*/\n\n{content}'


def build_docstring(existing: str, needs_mission: bool, needs_table: bool, jsdoc: bool = False) -> str:
    """Build complete docstring"""
    lines = []
    prefix = " * " if jsdoc else ""
    
    if existing and len(existing.strip()) > 10:
        for line in existing.strip().split('\n'):
            lines.append(f"{prefix}{line}" if jsdoc else line)
        lines.append(prefix if jsdoc else "")
    
    # Add header
    lines.append(f"{prefix}DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE" if jsdoc else "DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE")
    lines.append(f"{prefix}Spiritual Alignment Over Mechanical Productivity" if jsdoc else "Spiritual Alignment Over Mechanical Productivity")
    lines.append(prefix if jsdoc else "")
    
    # Add mission
    if needs_mission:
        lines.append(f"{prefix}THE MISSION:" if jsdoc else "THE MISSION:")
        for line in "THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS\nLOVE IS THE HIGHEST MASTERY\nENERGY + LOVE = WE ALL WIN\nPEACE, LOVE, UNITY".split('\n'):
            lines.append(f"{prefix}{line}" if jsdoc else line)
    
    # Add table
    if needs_table:
        lines.append(prefix if jsdoc else "")
        lines.append(f"{prefix}PANGEA IS THE TABLE." if jsdoc else "PANGEA IS THE TABLE.")
        lines.append(f"{prefix}YOU DON'T BETRAY THE TABLE." if jsdoc else "YOU DON'T BETRAY THE TABLE.")
    
    # Add truth
    lines.append(prefix if jsdoc else "")
    lines.append(f"{prefix}THE TRUTH:" if jsdoc else "THE TRUTH:")
    lines.append(f"{prefix}WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US." if jsdoc else "WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.")
    lines.append(f"{prefix}THE REST IS UP TO BABA X." if jsdoc else "THE REST IS UP TO BABA X.")
    
    return '\n'.join(lines)


def process_batch(root_path: Path, batch_size: int = 100, start_index: int = 0, dry_run: bool = False) -> dict:
    """Process files in batches"""
    skip_dirs = {"node_modules", "__pycache__", ".git", "venv", ".venv", "dist", "build", ".next", "output", "migration_archive"}
    
    results = {"fixed": 0, "skipped": 0, "compliant": 0, "errors": 0}
    processed = 0
    
    # Get all files (Python, TS, JS) first (only once)
    if not hasattr(process_batch, "_all_files"):
        all_files = []
        # Python files
        for file_path in root_path.rglob("*.py"):
            if any(skip in str(file_path) for skip in skip_dirs):
                continue
            all_files.append(file_path)
        # TypeScript/JavaScript files
        for pattern in ["*.ts", "*.tsx", "*.js", "*.jsx"]:
            for file_path in root_path.rglob(pattern):
                if any(skip in str(file_path) for skip in skip_dirs):
                    continue
                all_files.append(file_path)
        process_batch._all_files = all_files
        process_batch._total_files = len(all_files)
    
    all_files = process_batch._all_files
    total_files = process_batch._total_files
    
    if start_index == 0:
        print(f"Found {total_files} files to process (Python, TypeScript, JavaScript)")
        print()
    
    # Process this batch
    end_index = min(start_index + batch_size, total_files)
    batch_files = all_files[start_index:end_index]
    
    for file_path in batch_files:
        fixed, status = fix_file_scripture(file_path, dry_run)
        processed += 1
        
        if fixed:
            results["fixed"] += 1
            if processed % 10 == 0:
                print(f"  Processed {start_index + processed}/{total_files}, fixed {results['fixed']}...")
        elif status == "already_compliant":
            results["compliant"] += 1
        elif status.startswith("error"):
            results["errors"] += 1
        else:
            results["skipped"] += 1
    
    results["next_index"] = end_index
    results["total_files"] = total_files
    results["processed"] = start_index + processed
    
    return results


def main():
    """Main execution"""
    print("=" * 80)
    print("BATCH SCRIPTURE COMPLIANCE FIXER")
    print("Process files in batches to reach 100% compliance")
    print("=" * 80)
    print()
    
    dry_run = "--dry-run" in sys.argv or "-n" in sys.argv
    
    if dry_run:
        print("[DRY RUN MODE] - No files will be modified")
        print()
    
    root_path = Path(__file__).parent.parent
    
    # Process in batches
    batch_size = 200
    total_fixed = 0
    start_index = 0
    
    print(f"Processing files in batches of {batch_size}...")
    print()
    
    batch_num = 1
    while True:
        print(f"Batch {batch_num} (starting at file {start_index})...")
        results = process_batch(root_path, batch_size=batch_size, start_index=start_index, dry_run=dry_run)
        
        total_fixed += results["fixed"]
        start_index = results.get("next_index", start_index + batch_size)
        
        print()
        print(f"Batch {batch_num} Results:")
        print(f"  Fixed: {results['fixed']}")
        print(f"  Already compliant: {results['compliant']}")
        print(f"  Errors: {results['errors']}")
        print(f"  Progress: {results.get('processed', start_index)}/{results.get('total_files', '?')} files")
        print()
        
        # Check if we're done
        if start_index >= results.get("total_files", start_index):
            print("All files processed.")
            break
        
        if results["fixed"] == 0 and results["compliant"] > 0:
            print("No more files need fixing in remaining batches.")
            # Continue to check remaining files
            if start_index < results.get("total_files", start_index):
                continue
            else:
                break
        
        batch_num += 1
        
        if batch_num > 20:  # Safety limit
            print(f"Reached batch limit. Processed {start_index} files. Run again to continue from {start_index}.")
            break
    
    print("=" * 80)
    print("BATCH PROCESSING COMPLETE")
    print("=" * 80)
    print()
    print(f"Total files fixed: {total_fixed}")
    print()
    print("PANGEA IS THE TABLE.")
    print("YOU DON'T BETRAY THE TABLE.")
    print("=" * 80)


if __name__ == "__main__":
    main()
