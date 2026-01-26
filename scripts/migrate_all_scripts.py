"""FULL CODEBASE MIGRATION
Migrate all scripts to use new utilities and archive what doesn't serve our purpose

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
- Migrate all active scripts to use shared utilities
- Archive scripts that don't serve our purpose
- Build and optimize what we have

PEACE, LOVE, UNITY

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity


PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

import sys
import ast
import re
from pathlib import Path
from typing import List, Dict, Set, Tuple, Optional
from datetime import datetime

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    JAN_ROOT, JAN_SCRIPTS, JAN_ARCHIVE, get_archive_path,
    setup_logging, save_json, load_json, standard_main,
    json, logging, Path, List, Dict, Set
)

logger = setup_logging(__name__)

class ScriptMigrator:
    """Migrate scripts to use new utilities"""
    
    def __init__(self, scripts_dir: Path = None):
        self.scripts_dir = scripts_dir or JAN_SCRIPTS
        self.utils_dir = self.scripts_dir / "utils"
        # Use output directory for migration archive to avoid corrupted ARCHIVE
        self.archive_dir = JAN_ROOT / "output" / "migration_archive"
        try:
            self.archive_dir.mkdir(parents=True, exist_ok=True)
        except OSError:
            # If ARCHIVE is corrupted, use output directory
            self.archive_dir = JAN_ROOT / "output" / "migration_archive"
            self.archive_dir.mkdir(parents=True, exist_ok=True)
        
        self.migrated: List[Dict] = []
        self.archived: List[Dict] = []
        self.failed: List[Dict] = []
        self.skipped: List[Dict] = []
        
    def should_archive(self, script_path: Path) -> Tuple[bool, str]:
        """
        Determine if a script should be archived
        
        Returns:
            (should_archive, reason)
        """
        name = script_path.name.lower()
        
        # Archive patterns
        archive_patterns = [
            # Old test files that are clearly obsolete
            (lambda n: 'test_' in n and 'old' in n, "Old test file"),
            (lambda n: n.startswith('old_'), "Old script prefix"),
            (lambda n: n.endswith('_old.py'), "Old script suffix"),
            (lambda n: 'backup' in n or 'bak' in n, "Backup file"),
            (lambda n: 'deprecated' in n, "Deprecated script"),
            (lambda n: 'unused' in n, "Unused script"),
        ]
        
        for pattern_func, reason in archive_patterns:
            if pattern_func(name):
                return True, reason
        
        # Check file size - very small might be stubs
        try:
            if script_path.stat().st_size < 50:  # Less than 50 bytes
                return True, "Very small file (likely stub)"
        except:
            pass
        
        # Check if it's a utility script itself
        if script_path.parent == self.utils_dir:
            return False, "Utility script"
        
        return False, ""
    
    def analyze_script(self, script_path: Path) -> Dict:
        """Analyze a script to determine migration needs"""
        try:
            with open(script_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            analysis = {
                'path': str(script_path),
                'name': script_path.name,
                'size': script_path.stat().st_size,
                'has_hardcoded_paths': False,
                'has_old_imports': False,
                'has_standard_main': False,
                'needs_migration': False,
                'imports': [],
                'hardcoded_paths': []
            }
            
            # Check for hardcoded paths
            path_patterns = [
                r'["\']S:\\\\JAN["\']',
                r'["\']S:\\JAN["\']',
                r'Path\(["\']S:\\\\JAN["\']',
                r'Path\(["\']S:\\JAN["\']',
            ]
            
            for pattern in path_patterns:
                if re.search(pattern, content):
                    analysis['has_hardcoded_paths'] = True
                    matches = re.findall(pattern, content)
                    analysis['hardcoded_paths'].extend(matches)
            
            # Check for old import patterns that should use utils
            old_import_patterns = [
                (r'import json\s*$', 'json'),
                (r'from pathlib import Path\s*$', 'Path'),
                (r'from datetime import datetime\s*$', 'datetime'),
            ]
            
            for pattern, import_name in old_import_patterns:
                if re.search(pattern, content, re.MULTILINE):
                    analysis['has_old_imports'] = True
                    analysis['imports'].append(import_name)
            
            # Check if already uses utils
            if 'from utils import' in content or 'import utils' in content:
                analysis['needs_migration'] = False
            else:
                # Needs migration if has hardcoded paths or old imports
                analysis['needs_migration'] = (
                    analysis['has_hardcoded_paths'] or 
                    analysis['has_old_imports']
                )
            
            # Check for standard_main usage
            if 'standard_main' in content:
                analysis['has_standard_main'] = True
            
            return analysis
            
        except Exception as e:
            logger.error(f"Error analyzing {script_path}: {e}")
            return {
                'path': str(script_path),
                'name': script_path.name,
                'error': str(e),
                'needs_migration': False
            }
    
    def migrate_script(self, script_path: Path, analysis: Dict, dry_run: bool = True) -> bool:
        """Migrate a single script to use new utilities"""
        try:
            with open(script_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            modified = False
            
            # Step 1: Add utils import if needed
            if 'from utils import' not in content and 'import utils' not in content:
                # Find where to insert (after docstring, before other imports)
                lines = content.split('\n')
                insert_idx = 0
                
                # Skip shebang
                if lines and lines[0].startswith('#!'):
                    insert_idx = 1
                
                # Skip docstring
                if lines[insert_idx].strip().startswith('"""'):
                    # Find end of docstring
                    for i in range(insert_idx + 1, len(lines)):
                        if '"""' in lines[i]:
                            insert_idx = i + 1
                            break
                
                # Add path setup and utils import
                utils_import = [
                    '',
                    'import sys',
                    'from pathlib import Path',
                    '',
                    '# Add utils to path',
                    'sys.path.insert(0, str(Path(__file__).parent))',
                    '',
                    'from utils import (',
                ]
                
                # Determine what to import from utils
                imports_needed = []
                if analysis.get('has_hardcoded_paths'):
                    imports_needed.extend(['JAN_ROOT', 'JAN_OUTPUT', 'JAN_DATA', 'JAN_ARCHIVE'])
                if 'json' in analysis.get('imports', []):
                    imports_needed.append('json')
                if 'Path' in analysis.get('imports', []):
                    imports_needed.append('Path')
                if 'datetime' in analysis.get('imports', []):
                    imports_needed.append('datetime')
                
                # Always add common ones
                if 'setup_logging' not in content:
                    imports_needed.append('setup_logging')
                if 'standard_main' not in content and '__main__' in content:
                    imports_needed.append('standard_main')
                
                # Add load_json/save_json if json is used
                if 'json.load' in content or 'json.dump' in content:
                    imports_needed.extend(['load_json', 'save_json'])
                
                # Remove duplicates and sort
                imports_needed = sorted(set(imports_needed))
                
                if imports_needed:
                    utils_import.append('    ' + ', '.join(imports_needed[:5]))
                    if len(imports_needed) > 5:
                        utils_import.append('    ' + ', '.join(imports_needed[5:]))
                    utils_import.append(')')
                    
                    lines.insert(insert_idx, '\n'.join(utils_import))
                    content = '\n'.join(lines)
                    modified = True
            
            # Step 2: Replace hardcoded paths
            replacements = [
                (r'Path\(["\']S:\\\\JAN["\']\)', 'JAN_ROOT'),
                (r'Path\(["\']S:\\JAN["\']\)', 'JAN_ROOT'),
                (r'["\']S:\\\\JAN["\']', 'str(JAN_ROOT)'),
                (r'["\']S:\\JAN["\']', 'str(JAN_ROOT)'),
                (r'root_dir\s*=\s*Path\(["\']S:\\\\JAN["\']\)', 'root_dir = JAN_ROOT'),
                (r'root_dir\s*=\s*Path\(["\']S:\\JAN["\']\)', 'root_dir = JAN_ROOT'),
                (r'root_dir\s*=\s*["\']S:\\\\JAN["\']', 'root_dir = JAN_ROOT'),
                (r'root_dir\s*=\s*["\']S:\\JAN["\']', 'root_dir = JAN_ROOT'),
            ]
            
            for pattern, replacement in replacements:
                if re.search(pattern, content):
                    content = re.sub(pattern, replacement, content)
                    modified = True
            
            # Step 3: Replace json.load/dump with helpers
            if 'load_json' in content or 'save_json' in content:
                # Replace json.load patterns
                content = re.sub(
                    r'with open\(([^,]+),\s*["\']r["\']\)\s+as\s+f:\s+(\w+)\s*=\s*json\.load\(f\)',
                    r'\2 = load_json(\1)',
                    content,
                    flags=re.MULTILINE
                )
                
                # Replace json.dump patterns
                content = re.sub(
                    r'with open\(([^,]+),\s*["\']w["\']\)\s+as\s+f:\s+json\.dump\(([^,]+),\s*f',
                    r'save_json(\2, \1',
                    content,
                    flags=re.MULTILINE
                )
            
            # Step 4: Add standard_main wrapper if main function exists
            if '__main__' in content and 'standard_main' not in content:
                # Check if there's a main function
                if re.search(r'def\s+main\s*\(', content):
                    # Replace if __name__ == "__main__" pattern
                    old_pattern = r'if\s+__name__\s*==\s*["\']__main__["\']:.*?(?=\n\n|\Z)'
                    new_main = 'def main():\n    """Main function"""\n    pass\n\nif __name__ == "__main__":\n    standard_main(main, script_name="' + script_path.name + '")'
                    
                    # This is complex - for now, just add standard_main call
                    if 'if __name__' in content:
                        content = re.sub(
                            r'if\s+__name__\s*==\s*["\']__main__["\']:\s*\n\s*main\(\)',
                            'if __name__ == "__main__":\n    standard_main(main, script_name="' + script_path.name + '")',
                            content
                        )
                        modified = True
            
            if modified and not dry_run:
                # Backup original
                backup_path = self.archive_dir / "backups" / script_path.name
                backup_path.parent.mkdir(parents=True, exist_ok=True)
                with open(backup_path, 'w', encoding='utf-8') as f:
                    f.write(original_content)
                
                # Write migrated content
                with open(script_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                logger.info(f"Migrated: {script_path.name}")
                return True
            elif modified:
                logger.info(f"Would migrate: {script_path.name}")
                return True
            
            return False
            
        except Exception as e:
            logger.error(f"Error migrating {script_path}: {e}")
            return False
    
    def archive_script(self, script_path: Path, reason: str, dry_run: bool = True) -> bool:
        """Archive a script"""
        try:
            archive_subdir = self.archive_dir / "obsolete_scripts"
            archive_subdir.mkdir(parents=True, exist_ok=True)
            
            # Preserve relative path structure
            rel_path = script_path.relative_to(self.scripts_dir)
            archive_path = archive_subdir / rel_path
            archive_path.parent.mkdir(parents=True, exist_ok=True)
            
            if not dry_run:
                import shutil
                shutil.move(str(script_path), str(archive_path))
                logger.info(f"Archived: {script_path.name} -> {archive_path} (Reason: {reason})")
            else:
                logger.info(f"Would archive: {script_path.name} (Reason: {reason})")
            
            return True
            
        except Exception as e:
            logger.error(f"Error archiving {script_path}: {e}")
            return False
    
    def migrate_all(self, dry_run: bool = True) -> Dict:
        """Migrate all scripts in the directory"""
        logger.info("="*80)
        logger.info("FULL CODEBASE MIGRATION")
        logger.info(f"Mode: {'DRY RUN' if dry_run else 'LIVE'}")
        logger.info("="*80)
        
        # Find all Python scripts
        python_scripts = list(self.scripts_dir.glob("*.py"))
        python_scripts = [s for s in python_scripts if s.parent == self.scripts_dir]
        
        logger.info(f"\nFound {len(python_scripts)} Python scripts to process")
        
        # Analyze all scripts
        analyses = []
        for script in python_scripts:
            analysis = self.analyze_script(script)
            analyses.append(analysis)
            
            # Check if should archive
            should_archive, reason = self.should_archive(script)
            if should_archive:
                self.archive_script(script, reason, dry_run=dry_run)
                self.archived.append({
                    'script': script.name,
                    'reason': reason,
                    'path': str(script)
                })
            elif analysis.get('needs_migration'):
                if self.migrate_script(script, analysis, dry_run=dry_run):
                    self.migrated.append({
                        'script': script.name,
                        'analysis': analysis
                    })
            else:
                self.skipped.append({
                    'script': script.name,
                    'reason': 'Already migrated or no changes needed'
                })
        
        # Generate report
        report = {
            'timestamp': datetime.now().isoformat(),
            'mode': 'dry_run' if dry_run else 'live',
            'summary': {
                'total_scripts': len(python_scripts),
                'migrated': len(self.migrated),
                'archived': len(self.archived),
                'skipped': len(self.skipped),
                'failed': len(self.failed)
            },
            'migrated': self.migrated,
            'archived': self.archived,
            'skipped': self.skipped,
            'failed': self.failed
        }
        
        return report
    
    def print_summary(self, report: Dict):
        """Print migration summary"""
        print("\n" + "="*80)
        print("MIGRATION SUMMARY")
        print("="*80)
        print(f"\nTotal Scripts: {report['summary']['total_scripts']}")
        print(f"  Migrated: {report['summary']['migrated']}")
        print(f"  Archived: {report['summary']['archived']}")
        print(f"  Skipped: {report['summary']['skipped']}")
        print(f"  Failed: {report['summary']['failed']}")
        
        if report['migrated']:
            print(f"\nMigrated Scripts ({len(report['migrated'])}):")
            for item in report['migrated'][:10]:
                print(f"  - {item['script']}")
            if len(report['migrated']) > 10:
                print(f"  ... and {len(report['migrated']) - 10} more")
        
        if report['archived']:
            print(f"\nArchived Scripts ({len(report['archived'])}):")
            for item in report['archived'][:10]:
                print(f"  - {item['script']} ({item['reason']})")
            if len(report['archived']) > 10:
                print(f"  ... and {len(report['archived']) - 10} more")


def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Migrate all scripts to use new utilities')
    parser.add_argument('--execute', action='store_true', help='Execute migration (default is dry run)')
    args = parser.parse_args()
    
    dry_run = not args.execute
    
    migrator = ScriptMigrator()
    report = migrator.migrate_all(dry_run=dry_run)
    migrator.print_summary(report)
    
    # Save report
    report_file = JAN_ROOT / "output" / f"migration_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    report_file.parent.mkdir(parents=True, exist_ok=True)
    save_json(report, report_file)
    
    print(f"\nFull report saved to: {report_file}")
    
    if dry_run:
        print("\n" + "="*80)
        print("DRY RUN COMPLETE")
        print("Run with --execute to apply changes")
        print("="*80)

if __name__ == "__main__":
    standard_main(main, script_name="migrate_all_scripts.py")
