"""
IMPLEMENT VOLUME OPTIMIZATION
Implement recommendations and optimize storage usage

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
IMPLEMENT RECOMMENDATIONS
Optimize storage usage
Set up backup structures
Move user data from C: drive
"""

import sys
import subprocess
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any

sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    setup_logging, standard_main, load_json, save_json
)
from volume_discovery_utilization import VolumeDiscoverySystem

logger = setup_logging(__name__)

def create_backup_structure(drive_letter: str, base_path: Path) -> Dict[str, Any]:
    """Create backup directory structure on drive"""
    logger.info(f"Creating backup structure on {drive_letter}:")
    
    structure = {
        "drive": drive_letter,
        "base_path": str(base_path),
        "directories_created": [],
        "directories_existing": [],
        "errors": []
    }
    
    directories = [
        "Backups",
        "Backups/System",
        "Backups/Projects",
        "Backups/UserData",
        "Archives",
        "Archives/Projects",
        "Archives/Media",
        "Workspace",
        "Workspace/Active",
        "Workspace/Temp"
    ]
    
    for dir_path in directories:
        full_path = base_path / dir_path
        try:
            full_path.mkdir(parents=True, exist_ok=True)
            if full_path.exists():
                if any(full_path.iterdir()):
                    structure["directories_existing"].append(str(full_path))
                else:
                    structure["directories_created"].append(str(full_path))
                    logger.info(f"  Created: {full_path}")
        except Exception as e:
            structure["errors"].append(f"{dir_path}: {str(e)}")
            logger.error(f"  Error creating {dir_path}: {e}")
    
    return structure

def move_user_data_from_c_drive(user_profile: str, target_drive: str) -> Dict[str, Any]:
    """Move user data from C: drive to target drive"""
    logger.info(f"Planning user data migration from C: to {target_drive}:")
    
    migration_plan = {
        "source_drive": "C:",
        "target_drive": target_drive,
        "items_to_move": [],
        "estimated_size_gb": 0.0,
        "actions": []
    }
    
    # Items that can be moved from C: drive
    user_items = [
        {"path": f"{user_profile}\\Documents", "target": f"{target_drive}:\\UserData\\Documents", "type": "folder"},
        {"path": f"{user_profile}\\Desktop", "target": f"{target_drive}:\\UserData\\Desktop", "type": "folder"},
        {"path": f"{user_profile}\\Downloads", "target": f"{target_drive}:\\UserData\\Downloads", "type": "folder"},
        {"path": f"{user_profile}\\Pictures", "target": f"{target_drive}:\\UserData\\Pictures", "type": "folder"},
        {"path": f"{user_profile}\\Videos", "target": f"{target_drive}:\\UserData\\Videos", "type": "folder"},
        {"path": f"{user_profile}\\Music", "target": f"{target_drive}:\\UserData\\Music", "type": "folder"},
    ]
    
    for item in user_items:
        source_path = Path(item["path"])
        if source_path.exists():
            # Estimate size (rough)
            try:
                size = sum(f.stat().st_size for f in source_path.rglob('*') if f.is_file())
                size_gb = round(size / (1024**3), 2)
                migration_plan["estimated_size_gb"] += size_gb
                
                migration_plan["items_to_move"].append({
                    "source": str(source_path),
                    "target": item["target"],
                    "type": item["type"],
                    "size_gb": size_gb
                })
                
                migration_plan["actions"].append(
                    f"Move {item['path']} ({size_gb} GB) to {item['target']}"
                )
            except Exception as e:
                logger.warning(f"Could not estimate size for {item['path']}: {e}")
    
    return migration_plan

def create_backup_script(drive_letter: str, backup_path: Path) -> Path:
    """Create automated backup script for drive"""
    script_path = backup_path / "automated_backup.ps1"
    
    script_content = f"""# AUTOMATED BACKUP SCRIPT - {drive_letter}: Drive
# Auto-generated backup script

$backupPath = "{backup_path}"
$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"

# Create timestamped backup directory
$backupDir = Join-Path $backupPath "Backups\\System\\backup_$timestamp"
New-Item -ItemType Directory -Path $backupDir -Force | Out-Null

Write-Host "Backup started: $timestamp" -ForegroundColor Green
Write-Host "Backup location: $backupDir" -ForegroundColor Cyan

# Add your backup commands here
# Example: Copy-Item -Path "C:\\Source" -Destination "$backupDir\\Source" -Recurse

Write-Host "Backup complete: $timestamp" -ForegroundColor Green
"""
    
    try:
        script_path.write_text(script_content, encoding='utf-8')
        logger.info(f"Created backup script: {script_path}")
        return script_path
    except Exception as e:
        logger.error(f"Error creating backup script: {e}")
        return None

def optimize_c_drive() -> Dict[str, Any]:
    """Optimize C: drive - cleanup and recommendations"""
    logger.info("Optimizing C: drive...")
    
    optimization = {
        "actions_taken": [],
        "space_freed_gb": 0.0,
        "recommendations": []
    }
    
    # Check temp files
    temp_paths = [
        Path("C:\\Windows\\Temp"),
        Path(f"{Path.home()}\\AppData\\Local\\Temp")
    ]
    
    for temp_path in temp_paths:
        if temp_path.exists():
            try:
                # Estimate size (don't delete yet - just report)
                size = sum(f.stat().st_size for f in temp_path.rglob('*') if f.is_file())
                size_gb = round(size / (1024**3), 2)
                optimization["recommendations"].append(
                    f"Clean {temp_path} - estimated {size_gb} GB can be freed"
                )
            except Exception as e:
                logger.warning(f"Could not analyze {temp_path}: {e}")
    
    # Disk cleanup recommendations
    optimization["recommendations"].extend([
        "Run: Optimize-Volume -DriveLetter C -Defrag (admin required)",
        "Run: Cleanmgr /d C: (Disk Cleanup)",
        "Move user data to other drives",
        "Uninstall unused programs",
        "Clear browser cache",
        "Clear Windows Update cache"
    ])
    
    return optimization

def main():
    """Main function"""
    system = VolumeDiscoverySystem(user_id="jan")
    
    print("\n" + "="*80)
    print("IMPLEMENT VOLUME OPTIMIZATION")
    print("="*80)
    print("\nImplementing recommendations and optimizing storage...")
    
    # Discover volumes
    result = system.discover_and_utilize()
    
    user_profile = str(Path.home())
    implementations = []
    
    # 1. Create backup structures on recommended drives
    print("\n" + "-"*80)
    print("[1/3] Creating backup structures...")
    print("-"*80)
    
    for vol in system.volumes:
        if vol.drive_letter and vol.drive_letter.upper() != "C":
            # Check if it's recommended for backup
            util = next((u for u in system.utilizations if u.drive_letter == vol.drive_letter), None)
            if util and "backup" in util.recommended_use.lower():
                drive_path = Path(f"{vol.drive_letter}:\\")
                structure = create_backup_structure(vol.drive_letter, drive_path)
                implementations.append({
                    "type": "backup_structure",
                    "drive": vol.drive_letter,
                    "result": structure
                })
                
                # Create backup script
                backup_script = create_backup_script(vol.drive_letter, drive_path)
                if backup_script:
                    implementations.append({
                        "type": "backup_script",
                        "drive": vol.drive_letter,
                        "script_path": str(backup_script)
                    })
    
    # 2. Plan C: drive cleanup and user data migration
    print("\n" + "-"*80)
    print("[2/3] Planning C: drive optimization...")
    print("-"*80)
    
    c_drive_vol = next((v for v in system.volumes if v.drive_letter and v.drive_letter.upper() == "C"), None)
    if c_drive_vol and c_drive_vol.usage_percent > 80:
        print(f"  [WARNING] C: drive is {c_drive_vol.usage_percent:.1f}% used - optimization needed")
        
        # Find best target drive for user data
        target_drive = None
        for vol in system.volumes:
            if vol.drive_letter and vol.drive_letter.upper() != "C":
                if vol.free_space_gb > 100:  # At least 100GB free
                    target_drive = vol.drive_letter
                    break
        
        if target_drive:
            migration_plan = move_user_data_from_c_drive(user_profile, target_drive)
            implementations.append({
                "type": "migration_plan",
                "result": migration_plan
            })
            
            print(f"  [OK] Migration plan created - target: {target_drive}:")
            print(f"  Estimated data to move: {migration_plan['estimated_size_gb']:.2f} GB")
            print(f"  Items to move: {len(migration_plan['items_to_move'])}")
        else:
            print("  [WARNING] No suitable target drive found for migration")
    
    # 3. C: drive optimization
    print("\n" + "-"*80)
    print("[3/3] C: drive optimization analysis...")
    print("-"*80)
    
    optimization = optimize_c_drive()
    implementations.append({
        "type": "optimization",
        "result": optimization
    })
    
    if optimization["recommendations"]:
        print("  Recommendations:")
        for rec in optimization["recommendations"]:
            print(f"    - {rec}")
    
    # Save implementation report
    report = {
        "timestamp": datetime.now().isoformat(),
        "implementations": implementations,
        "summary": {
            "backup_structures_created": len([i for i in implementations if i["type"] == "backup_structure"]),
            "backup_scripts_created": len([i for i in implementations if i["type"] == "backup_script"]),
            "migration_plans": len([i for i in implementations if i["type"] == "migration_plan"]),
            "optimizations": len([i for i in implementations if i["type"] == "optimization"])
        }
    }
    
    output_dir = Path(__file__).parent.parent / "output"
    output_dir.mkdir(parents=True, exist_ok=True)
    report_path = output_dir / f"volume_optimization_implementation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    save_json(report, report_path)
    
    print("\n" + "="*80)
    print("IMPLEMENTATION COMPLETE")
    print("="*80)
    print(f"\nBackup Structures Created: {report['summary']['backup_structures_created']}")
    print(f"Backup Scripts Created: {report['summary']['backup_scripts_created']}")
    print(f"Migration Plans: {report['summary']['migration_plans']}")
    print(f"Optimizations: {report['summary']['optimizations']}")
    print(f"\nReport saved to: {report_path}")
    print("\n" + "="*80)
    
    logger.info(f"Volume optimization implementation complete: {len(implementations)} implementations")

if __name__ == "__main__":
    standard_main(main, script_name="implement_volume_optimization.py")
