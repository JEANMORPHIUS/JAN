"""EXECUTE SYSTEM CLEANUP
Archive or Delete Unnecessary Files

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE TRUTH:
IF WE DON'T NEED IT...BIN IT...OR ARCHIVE IT

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
    JAN_ROOT, JAN_ARCHIVE, get_archive_path,
    datetime, json, shutil, logging, List, Dict,
    setup_logging, standard_main
)

logger = setup_logging(__name__)

class CleanupExecutor:
    """Execute cleanup operations"""
    
    def __init__(self, root_dir: Path = None):
        self.root_dir = root_dir or JAN_ROOT
        self.archive_dir = get_archive_path()
        self.archive_dir.mkdir(exist_ok=True)
        
        # Create archive subdirectories
        (self.archive_dir / "duplicates").mkdir(exist_ok=True)
        (self.archive_dir / "old_outputs").mkdir(exist_ok=True)
        (self.archive_dir / "completion_docs").mkdir(exist_ok=True)
        (self.archive_dir / "backups").mkdir(exist_ok=True)
        (self.archive_dir / "test_files").mkdir(exist_ok=True)
    
    def archive_file(self, file_path: Path, category: str) -> bool:
        """Archive a file to ARCHIVE directory"""
        try:
            if not file_path.exists():
                return False
            
            # Create category directory
            category_dir = self.archive_dir / category
            category_dir.mkdir(exist_ok=True)
            
            # Preserve directory structure in archive
            rel_path = file_path.relative_to(self.root_dir)
            archive_path = category_dir / rel_path
            archive_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Move file
            shutil.move(str(file_path), str(archive_path))
            print(f"  [OK] Archived: {file_path.name} -> {archive_path}")
            return True
        except Exception as e:
            print(f"  [ERROR] Error archiving {file_path}: {e}")
            return False
    
    def delete_file(self, file_path: Path) -> bool:
        """Delete a file"""
        try:
            if not file_path.exists():
                return False
            
            file_path.unlink()
            print(f"  [OK] Deleted: {file_path}")
            return True
        except Exception as e:
            print(f"  [ERROR] Error deleting {file_path}: {e}")
            return False
    
    def execute_cleanup(self, report_file: str = "output/system_cleanup_report.json", dry_run: bool = True):
        """Execute cleanup based on report"""
        print("="*80)
        print("EXECUTING SYSTEM CLEANUP")
        print(f"Mode: {'DRY RUN' if dry_run else 'LIVE'}")
        print("="*80 + "\n")
        
        # Load report
        report_path = self.root_dir / report_file
        if not report_path.exists():
            print(f"Error: Report file not found: {report_path}")
            return
        
        with open(report_path, 'r') as f:
            report = json.load(f)
        
        archived = 0
        deleted = 0
        
        # Archive duplicates
        if report.get('duplicates'):
            print(f"\n[ARCHIVING DUPLICATES] {len(report['duplicates'])} files")
            for dup in report['duplicates'][:50]:  # Limit to first 50
                file_path = Path(dup['file'])
                if not dry_run:
                    if self.archive_file(file_path, 'duplicates'):
                        archived += 1
                else:
                    print(f"  [DRY RUN] Would archive: {file_path}")
        
        # Archive old outputs
        if report.get('old_outputs'):
            print(f"\n[ARCHIVING OLD OUTPUTS] {len(report['old_outputs'])} files")
            for old in report['old_outputs'][:100]:  # Limit to first 100
                file_path = Path(old['file'])
                if not dry_run:
                    if self.archive_file(file_path, 'old_outputs'):
                        archived += 1
                else:
                    print(f"  [DRY RUN] Would archive: {file_path}")
        
        # Archive completion docs (review first)
        if report.get('completion_docs'):
            print(f"\n[REVIEWING COMPLETION DOCS] {len(report['completion_docs'])} files")
            print("  Note: Completion docs need manual review before archiving")
            # Don't auto-archive these - need review
        
        # Delete backup files
        if report.get('backup_files'):
            print(f"\n[DELETING BACKUP FILES] {len(report['backup_files'])} files")
            for backup in report['backup_files']:
                file_path = Path(backup['file'])
                if not dry_run:
                    if self.delete_file(file_path):
                        deleted += 1
                else:
                    print(f"  [DRY RUN] Would delete: {file_path}")
        
        # Summary
        print("\n" + "="*80)
        print("CLEANUP SUMMARY")
        print("="*80)
        if not dry_run:
            print(f"  Archived: {archived} files")
            print(f"  Deleted: {deleted} files")
            print(f"  Archive location: {self.archive_dir}")
        else:
            print("  DRY RUN - No files were modified")
            print("  Run with dry_run=False to execute")
        print("="*80)


def main():
    """Main function"""
    import sys
    
    dry_run = '--execute' not in sys.argv
    
    executor = CleanupExecutor()
    executor.execute_cleanup(dry_run=dry_run)
    
    if dry_run:
        print("\nTo execute cleanup, run:")
        print("  python scripts/execute_cleanup.py --execute")

if __name__ == "__main__":
    standard_main(main, script_name="execute_cleanup.py")
