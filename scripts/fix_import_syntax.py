"""
Fix import syntax errors in scripts
Fixes missing commas in utils imports
"""

import re
from pathlib import Path

scripts_dir = Path(__file__).parent

# Pattern to find the problematic import
pattern = r'from utils import \(\s*([^)]+?)\s*setup_logging, standard_main\s*\)'

# Find all Python files
for script_file in scripts_dir.glob("*.py"):
    try:
        content = script_file.read_text(encoding='utf-8')
        
        # Check if it has the problematic pattern
        if 'setup_logging, standard_main' in content and 'from utils import' in content:
            # Look for the specific pattern with missing comma
            match = re.search(r'from utils import \(\s*([^)]+?)\s+setup_logging, standard_main\s*\)', content, re.MULTILINE)
            if match:
                # Check if there's a missing comma before setup_logging
                before_setup = match.group(1)
                if not before_setup.rstrip().endswith(',') and before_setup.strip():
                    # Fix it
                    fixed = re.sub(
                        r'(from utils import \(\s*[^)]+?)(\s+setup_logging, standard_main\s*\))',
                        r'\1,\2',
                        content,
                        flags=re.MULTILINE
                    )
                    script_file.write_text(fixed, encoding='utf-8')
                    print(f"Fixed: {script_file.name}")
    except Exception as e:
        print(f"Error processing {script_file.name}: {e}")

print("Done!")
