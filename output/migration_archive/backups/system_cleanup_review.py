"""
SYSTEM CLEANUP AND REVIEW
Full System Review - Remove Unnecessary Residue

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
IF WE DON'T NEED IT...BIN IT...OR ARCHIVE IT
CLEAN SYSTEM = CLEAR FREQUENCY
"""

import os
import json
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Set
import hashlib

class SystemCleanupReview:
    """Review system and identify files for cleanup/archival"""
    
    def __init__(self, root_dir: str = "S:\\JAN"):
        self.root_dir = Path(root_dir)
        self.archive_dir = self.root_dir / "ARCHIVE"
        self.to_archive: List[Dict] = []
        self.to_delete: List[Dict] = []
        self.duplicates: List[Dict] = []
        self.old_outputs: List[Dict] = []
        self.unused_files: List[Dict] = []
        
    def find_duplicate_files(self) -> List[Dict]:
        """Find duplicate files by content hash"""
        print("Scanning for duplicate files...")
        file_hashes: Dict[str, List[Path]] = {}
        duplicates = []
        
        # Scan common output directories
        scan_dirs = [
            self.root_dir / "output",
            self.root_dir / "SIYEM" / "output",
        ]
        
        for scan_dir in scan_dirs:
            if not scan_dir.exists():
                continue
                
            for file_path in scan_dir.rglob("*"):
                if file_path.is_file() and file_path.suffix in ['.json', '.csv', '.md', '.txt']:
                    try:
                        with open(file_path, 'rb') as f:
                            file_hash = hashlib.md5(f.read()).hexdigest()
                        
                        if file_hash not in file_hashes:
                            file_hashes[file_hash] = []
                        file_hashes[file_hash].append(file_path)
                    except Exception as e:
                        continue
        
        # Find duplicates
        for file_hash, paths in file_hashes.items():
            if len(paths) > 1:
                # Keep newest, archive/delete others
                paths_sorted = sorted(paths, key=lambda p: p.stat().st_mtime, reverse=True)
                keep = paths_sorted[0]
                for duplicate in paths_sorted[1:]:
                    duplicates.append({
                        'type': 'duplicate',
                        'file': str(duplicate),
                        'keep': str(keep),
                        'size': duplicate.stat().st_size,
                        'modified': datetime.fromtimestamp(duplicate.stat().st_mtime).isoformat()
                    })
        
        self.duplicates = duplicates
        return duplicates
    
    def find_old_outputs(self, days_old: int = 30) -> List[Dict]:
        """Find old output files"""
        print(f"Scanning for files older than {days_old} days...")
        old_files = []
        cutoff_time = datetime.now().timestamp() - (days_old * 24 * 60 * 60)
        
        output_dirs = [
            self.root_dir / "output",
            self.root_dir / "SIYEM" / "output",
        ]
        
        for output_dir in output_dirs:
            if not output_dir.exists():
                continue
                
            for file_path in output_dir.rglob("*"):
                if file_path.is_file():
                    try:
                        mtime = file_path.stat().st_mtime
                        if mtime < cutoff_time:
                            # Check if it's a report/timestamped file
                            if any(indicator in file_path.name.lower() for indicator in ['report', 'log', 'output', 'export']):
                                old_files.append({
                                    'type': 'old_output',
                                    'file': str(file_path),
                                    'size': file_path.stat().st_size,
                                    'modified': datetime.fromtimestamp(mtime).isoformat(),
                                    'days_old': int((datetime.now().timestamp() - mtime) / (24 * 60 * 60))
                                })
                    except Exception:
                        continue
        
        self.old_outputs = old_files
        return old_files
    
    def find_completion_docs(self) -> List[Dict]:
        """Find redundant completion documentation"""
        print("Scanning for completion documentation...")
        completion_files = []
        
        # Look for *_COMPLETE.md files
        for md_file in self.root_dir.rglob("*_COMPLETE.md"):
            try:
                # Check file size and modification date
                stat = md_file.stat()
                completion_files.append({
                    'type': 'completion_doc',
                    'file': str(md_file),
                    'size': stat.st_size,
                    'modified': datetime.fromtimestamp(stat.st_mtime).isoformat(),
                    'days_old': int((datetime.now().timestamp() - stat.st_mtime) / (24 * 60 * 60))
                })
            except Exception:
                continue
        
        return completion_files
    
    def find_test_files(self) -> List[Dict]:
        """Find test files that might be unused"""
        print("Scanning for test files...")
        test_files = []
        
        test_patterns = ['*test*.py', '*_test.py', 'test_*.py']
        
        for pattern in test_patterns:
            for test_file in self.root_dir.rglob(pattern):
                if test_file.is_file():
                    # Skip if in node_modules or __pycache__
                    if 'node_modules' in str(test_file) or '__pycache__' in str(test_file):
                        continue
                    
                    try:
                        stat = test_file.stat()
                        test_files.append({
                            'type': 'test_file',
                            'file': str(test_file),
                            'size': stat.st_size,
                            'modified': datetime.fromtimestamp(stat.st_mtime).isoformat()
                        })
                    except Exception:
                        continue
        
        return test_files
    
    def find_backup_files(self) -> List[Dict]:
        """Find backup files"""
        print("Scanning for backup files...")
        backup_files = []
        
        backup_patterns = ['*backup*', '*bak', '*.bak', '*~', '*.old', '*_old*']
        
        for pattern in backup_patterns:
            for backup_file in self.root_dir.rglob(pattern):
                if backup_file.is_file():
                    # Skip node_modules
                    if 'node_modules' in str(backup_file):
                        continue
                    
                    try:
                        stat = backup_file.stat()
                        backup_files.append({
                            'type': 'backup',
                            'file': str(backup_file),
                            'size': stat.st_size,
                            'modified': datetime.fromtimestamp(stat.st_mtime).isoformat()
                        })
                    except Exception:
                        continue
        
        return backup_files
    
    def find_corrupted_dirs(self) -> List[Dict]:
        """Find potentially corrupted directories"""
        print("Scanning for corrupted directories...")
        corrupted = []
        
        # Known corrupted node_modules
        corrupted_paths = [
            self.root_dir / "homeostasis-sentinel" / "node_modules" / "is-extglob",
            self.root_dir / "homeostasis-sentinel" / "node_modules" / "parent-module",
            self.root_dir / "homeostasis-sentinel" / "node_modules" / "slash",
        ]
        
        for path in corrupted_paths:
            if path.exists():
                corrupted.append({
                    'type': 'corrupted',
                    'path': str(path),
                    'action': 'delete_and_reinstall'
                })
        
        return corrupted
    
    def generate_report(self) -> Dict:
        """Generate cleanup report"""
        print("\n" + "="*80)
        print("SYSTEM CLEANUP REVIEW REPORT")
        print("="*80 + "\n")
        
        duplicates = self.find_duplicate_files()
        old_outputs = self.find_old_outputs()
        completion_docs = self.find_completion_docs()
        test_files = self.find_test_files()
        backup_files = self.find_backup_files()
        corrupted = self.find_corrupted_dirs()
        
        report = {
            'timestamp': datetime.now().isoformat(),
            'summary': {
                'duplicates': len(duplicates),
                'old_outputs': len(old_outputs),
                'completion_docs': len(completion_docs),
                'test_files': len(test_files),
                'backup_files': len(backup_files),
                'corrupted': len(corrupted)
            },
            'duplicates': duplicates[:50],  # Limit to first 50
            'old_outputs': old_outputs[:100],  # Limit to first 100
            'completion_docs': completion_docs,
            'test_files': test_files,
            'backup_files': backup_files,
            'corrupted': corrupted,
            'recommendations': []
        }
        
        # Generate recommendations
        if duplicates:
            report['recommendations'].append({
                'action': 'archive',
                'count': len(duplicates),
                'description': 'Archive duplicate files (keeping newest)'
            })
        
        if old_outputs:
            report['recommendations'].append({
                'action': 'archive',
                'count': len(old_outputs),
                'description': f'Archive {len(old_outputs)} old output files (>30 days)'
            })
        
        if completion_docs:
            report['recommendations'].append({
                'action': 'review',
                'count': len(completion_docs),
                'description': f'Review {len(completion_docs)} completion docs - archive if redundant'
            })
        
        if backup_files:
            report['recommendations'].append({
                'action': 'delete',
                'count': len(backup_files),
                'description': f'Delete {len(backup_files)} backup files'
            })
        
        if corrupted:
            report['recommendations'].append({
                'action': 'delete',
                'count': len(corrupted),
                'description': f'Delete {len(corrupted)} corrupted directories and reinstall'
            })
        
        return report
    
    def print_report(self, report: Dict):
        """Print human-readable report"""
        print(f"\nCLEANUP SUMMARY:")
        print(f"  Duplicates: {report['summary']['duplicates']}")
        print(f"  Old Outputs: {report['summary']['old_outputs']}")
        print(f"  Completion Docs: {report['summary']['completion_docs']}")
        print(f"  Test Files: {report['summary']['test_files']}")
        print(f"  Backup Files: {report['summary']['backup_files']}")
        print(f"  Corrupted: {report['summary']['corrupted']}")
        
        print(f"\nRECOMMENDATIONS:")
        for rec in report['recommendations']:
            print(f"  [{rec['action'].upper()}] {rec['count']} items - {rec['description']}")
        
        if report['duplicates']:
            print(f"\nSAMPLE DUPLICATES (showing first 10):")
            for dup in report['duplicates'][:10]:
                print(f"  - {dup['file']}")
                print(f"    Keep: {dup['keep']}")
        
        if report['old_outputs']:
            print(f"\nSAMPLE OLD OUTPUTS (showing first 10):")
            for old in report['old_outputs'][:10]:
                print(f"  - {old['file']} ({old['days_old']} days old)")
        
        if report['corrupted']:
            print(f"\nCORRUPTED DIRECTORIES:")
            for corr in report['corrupted']:
                print(f"  - {corr['path']} ({corr['action']})")


if __name__ == "__main__":
    print("="*80)
    print("SYSTEM CLEANUP REVIEW")
    print("IF WE DON'T NEED IT...BIN IT...OR ARCHIVE IT")
    print("="*80)
    
    reviewer = SystemCleanupReview()
    report = reviewer.generate_report()
    reviewer.print_report(report)
    
    # Save report
    report_file = Path("output") / "system_cleanup_report.json"
    report_file.parent.mkdir(exist_ok=True)
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n\nFull report saved to: {report_file}")
    print("\n" + "="*80)
    print("REVIEW COMPLETE")
    print("="*80)
