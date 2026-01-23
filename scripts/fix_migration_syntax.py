"""
Fix syntax errors in migrated scripts
Fixes missing commas in import statements
"""

import sys
import re
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from utils import JAN_SCRIPTS, setup_logging, standard_main

logger = setup_logging(__name__)

def fix_import_syntax(script_path: Path) -> bool:
    """Fix missing commas in utils import statements"""
    try:
        with open(script_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Fix pattern: line without comma followed by line starting with identifier
        # Pattern: from utils import (\n    item1\n    item2)
        pattern = r'(from utils import\s*\([^)]*?)\n(\s+)([a-zA-Z_][a-zA-Z0-9_]*)\s*\n(\s+)([a-zA-Z_][a-zA-Z0-9_]*)'
        
        def fix_match(m):
            before = m.group(1)
            indent1 = m.group(2)
            item1 = m.group(3)
            indent2 = m.group(4)
            item2 = m.group(5)
            
            # Check if item1 doesn't end with comma
            if not item1.rstrip().endswith(','):
                return f"{before}\n{indent1}{item1},\n{indent2}{item2}"
            return m.group(0)
        
        content = re.sub(pattern, fix_match, content, flags=re.MULTILINE)
        
        if content != original:
            with open(script_path, 'w', encoding='utf-8') as f:
                f.write(content)
            logger.info(f"Fixed: {script_path.name}")
            return True
        
        return False
        
    except Exception as e:
        logger.error(f"Error fixing {script_path}: {e}")
        return False

def main():
    """Main function"""
    fixed = 0
    scripts = list(JAN_SCRIPTS.glob("*.py"))
    scripts = [s for s in scripts if s.parent == JAN_SCRIPTS and s.name != __file__]
    
    for script in scripts:
        if fix_import_syntax(script):
            fixed += 1
    
    print(f"Fixed {fixed} scripts")

if __name__ == "__main__":
    standard_main(main, script_name="fix_migration_syntax.py")
