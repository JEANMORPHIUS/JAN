"""
ARCHIVE RESIDUE
Tidy Up and Archive Residue - Approaching Ground Zero

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

CORE PRINCIPLES (NON-NEGOTIABLE):
- Purpose Not Performance: Purpose matters more than performance. Authentic and aligned. Non-negotiable.
- Everything in Moderation: Balance. Not too much, not too little.
- Life Is Simple: Don't complicate it. Keep it simple.
- Be Still and Have Faith: Be still and have faith in revelation. Stillness brings clarity.

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

ARCHIVE RESIDUE:
Tidy up and archive residue.
We're approaching ground zero.
Keep it simple.
Keep it aligned.
"""

import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    Path, datetime, json, load_json, save_json
    setup_logging, standard_main
)

import os
import shutil
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any
from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)

@dataclass
class ArchiveItem:
    """An item to be archived."""
    path: str
    reason: str
    category: str
    size: int = 0

class ResidueArchiver:
    """Archive residue and tidy up for ground zero."""
    
    def __init__(self, root_path: str = "s:\\JAN"):
        """Initialize the archiver."""
        self.root_path = Path(root_path)
        self.archive_path = self.root_path / "archive" / datetime.now().strftime("%Y%m%d_%H%M%S")
        self.items_to_archive: List[ArchiveItem] = []
        self.items_archived: List[ArchiveItem] = []
    
    def identify_residue(self) -> List[ArchiveItem]:
        """Identify residue files to archive."""
        residue_patterns = [
            # Completion documents (old status files)
            ("*_COMPLETE.md", "Old completion status", "status"),
            ("*COMPLETE*.md", "Old completion document", "status"),
            ("COMPLETE_*.md", "Old completion file", "status"),
            
            # Test files (can be archived if not actively used)
            ("test_*.py", "Test file", "test"),
            ("*_test.py", "Test file", "test"),
            
            # Temporary files
            ("*.tmp", "Temporary file", "temp"),
            ("*.bak", "Backup file", "temp"),
            ("*.old", "Old file", "temp"),
            
            # Old logs
            ("*.log.old", "Old log file", "log"),
        ]
        
        items = []
        
        # Scan root directory for completion documents
        for file_path in self.root_path.glob("*.md"):
            if any(pattern in file_path.name for pattern in ["_COMPLETE", "COMPLETE_", "COMPLETE"]):
                # Skip THE_MASTER_DOCUMENT.md and active docs
                if file_path.name not in ["THE_MASTER_DOCUMENT.md"]:
                    try:
                        size = file_path.stat().st_size
                        items.append(ArchiveItem(
                            path=str(file_path),
                            reason="Old completion status document",
                            category="status",
                            size=size
                        ))
                    except Exception as e:
                        logger.warning(f"Could not process {file_path}: {e}")
        
        # Scan scripts for test files (be conservative - only archive if explicitly old)
        # We'll be selective here - only archive if they're clearly outdated
        
        self.items_to_archive = items
        return items
    
    def archive_items(self, dry_run: bool = True) -> Dict[str, Any]:
        """Archive identified items."""
        if not self.items_to_archive:
            return {
                "status": "no_items",
                "message": "No items to archive",
                "count": 0
            }
        
        if dry_run:
            return {
                "status": "dry_run",
                "message": f"Would archive {len(self.items_to_archive)} items",
                "count": len(self.items_to_archive),
                "items": [
                    {
                        "path": item.path,
                        "reason": item.reason,
                        "category": item.category,
                        "size": item.size
                    }
                    for item in self.items_to_archive
                ]
            }
        
        # Create archive directory
        self.archive_path.mkdir(parents=True, exist_ok=True)
        
        archived = []
        failed = []
        
        for item in self.items_to_archive:
            try:
                source_path = Path(item.path)
                if not source_path.exists():
                    continue
                
                # Create category subdirectory
                category_path = self.archive_path / item.category
                category_path.mkdir(parents=True, exist_ok=True)
                
                # Move file to archive
                dest_path = category_path / source_path.name
                shutil.move(str(source_path), str(dest_path))
                
                archived.append(item)
                self.items_archived.append(item)
                logger.info(f"Archived: {item.path} -> {dest_path}")
                
            except Exception as e:
                logger.error(f"Failed to archive {item.path}: {e}")
                failed.append({"path": item.path, "error": str(e)})
        
        return {
            "status": "completed",
            "message": f"Archived {len(archived)} items",
            "archived_count": len(archived),
            "failed_count": len(failed),
            "archive_path": str(self.archive_path),
            "failed": failed
        }
    
    def generate_archive_report(self) -> Dict[str, Any]:
        """Generate archive report."""
        return {
            "report_timestamp": datetime.now().isoformat(),
            "root_path": str(self.root_path),
            "archive_path": str(self.archive_path),
            "items_identified": len(self.items_to_archive),
            "items_archived": len(self.items_archived),
            "items_by_category": {
                category: len([i for i in self.items_to_archive if i.category == category])
                for category in set(i.category for i in self.items_to_archive)
            },
            "items": [
                {
                    "path": item.path,
                    "reason": item.reason,
                    "category": item.category,
                    "size": item.size
                }
                for item in self.items_to_archive
            ]
        }

def main():
    """Main function to archive residue."""
    import json
    
    print("=" * 80)
    print("ARCHIVE RESIDUE")
    print("Tidy Up and Archive Residue - Approaching Ground Zero")
    print("=" * 80)
    print()
    
    archiver = ResidueArchiver()
    
    print("Identifying residue files...")
    items = archiver.identify_residue()
    print(f"  Found {len(items)} items to archive")
    print()
    
    if items:
        print("Items by category:")
        categories = {}
        for item in items:
            categories[item.category] = categories.get(item.category, 0) + 1
        for category, count in categories.items():
            print(f"  {category}: {count}")
        print()
        
        # Dry run first
        print("Dry run (preview)...")
        dry_run_result = archiver.archive_items(dry_run=True)
        print(f"  Status: {dry_run_result['status']}")
        print(f"  Message: {dry_run_result['message']}")
        print()
        
        # Ask for confirmation (in real usage)
        # For now, we'll do a dry run only
        print("=" * 80)
        print("DRY RUN COMPLETE")
        print("=" * 80)
        print()
        print("To actually archive, set dry_run=False in archive_items()")
        print()
        
        # Generate report
        report = archiver.generate_archive_report()
        os.makedirs("output/archive", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_path = f"output/archive/archive_report_{timestamp}.json"
        
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"Archive report exported to: {report_path}")
        print()
    else:
        print("No residue files identified.")
        print("Codebase is clean.")
        print()
    
    print("=" * 80)
    print("THE TRUTH: ARCHIVE RESIDUE")
    print("=" * 80)
    print()
    print("PURPOSE:")
    print("  - Tidy up and archive residue")
    print("  - Approaching ground zero")
    print("  - Keep it simple")
    print("  - Keep it aligned")
    print()
    print("PRINCIPLES:")
    print("  - Purpose not performance")
    print("  - Authentic and aligned")
    print("  - Everything in moderation")
    print("  - Life is simple")
    print("  - Be still and have faith")
    print()
    print("=" * 80)
    print("PEACE, LOVE, UNITY")
    print("ENERGY + LOVE = WE ALL WIN")
    print("PURPOSE NOT PERFORMANCE")
    print("AUTHENTIC AND ALIGNED")
    print("BE STILL AND HAVE FAITH IN REVELATION")
    print("=" * 80)

if __name__ == "__main__":
    main()
