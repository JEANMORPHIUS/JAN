"""VOLUME DISCOVERY & UTILIZATION SYSTEM
Discover all volumes/disks on computer and utilize them

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
DISCOVER ALL VOLUMES
Utilize available storage
Optimize resource allocation

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

import sys
import subprocess
import json
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass, field, asdict
from typing import List, Optional, Dict, Any

sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    setup_logging, standard_main, load_json, save_json
)

logger = setup_logging(__name__)

@dataclass
class VolumeInfo:
    """Volume/disk information"""
    volume_id: str
    drive_letter: Optional[str] = None
    label: Optional[str] = None
    file_system: Optional[str] = None
    size_gb: float = 0.0
    free_space_gb: float = 0.0
    used_space_gb: float = 0.0
    usage_percent: float = 0.0
    disk_number: Optional[int] = None
    disk_model: Optional[str] = None
    disk_type: Optional[str] = None  # SSD, HDD, Removable, etc.
    health_status: Optional[str] = None
    partition_style: Optional[str] = None
    interface_type: Optional[str] = None
    discovered_at: str = field(default_factory=lambda: datetime.now().isoformat())

@dataclass
class VolumeUtilization:
    """Volume utilization plan"""
    volume_id: str
    drive_letter: str
    recommended_use: str  # backup, archive, workspace, media, etc.
    priority: int = 5  # 1-10, higher = more important
    utilization_actions: List[str] = field(default_factory=list)
    notes: str = ""

class VolumeDiscoverySystem:
    """
    Volume Discovery & Utilization System
    Discover all volumes and suggest utilization strategies
    """
    
    def __init__(self, user_id: str = "jan", data_dir: Path = None):
        self.user_id = user_id
        self.data_dir = data_dir or Path(__file__).parent.parent / "data" / "volume_discovery"
        self.data_dir.mkdir(parents=True, exist_ok=True)
        
        self.volumes_file = self.data_dir / f"{user_id}_volumes.json"
        self.utilizations_file = self.data_dir / f"{user_id}_utilizations.json"
        
        self.volumes: List[VolumeInfo] = []
        self.utilizations: List[VolumeUtilization] = []
        
        self._load_data()
    
    def _load_data(self):
        """Load volume data"""
        if self.volumes_file.exists():
            try:
                data = load_json(self.volumes_file)
                self.volumes = [VolumeInfo(**item) for item in data.get("volumes", [])]
            except Exception as e:
                logger.warning(f"Error loading volumes: {e}")
                self.volumes = []
        else:
            self.volumes = []
        
        if self.utilizations_file.exists():
            try:
                data = load_json(self.utilizations_file)
                self.utilizations = [VolumeUtilization(**item) for item in data.get("utilizations", [])]
            except Exception as e:
                logger.warning(f"Error loading utilizations: {e}")
                self.utilizations = []
        else:
            self.utilizations = []
    
    def _save_data(self):
        """Save volume data"""
        try:
            save_json(
                {"volumes": [asdict(vol) for vol in self.volumes]},
                self.volumes_file
            )
            save_json(
                {"utilizations": [asdict(util) for util in self.utilizations]},
                self.utilizations_file
            )
        except Exception as e:
            logger.error(f"Error saving volume data: {e}")
    
    def discover_volumes(self) -> List[VolumeInfo]:
        """Discover all volumes on the system"""
        logger.info("Discovering all volumes on system...")
        
        volumes = []
        
        try:
            # Get all volumes with drive letters
            ps_command = """
            $volumes = Get-Volume | Where-Object { $_.DriveLetter -ne $null }
            $result = @()
            foreach ($vol in $volumes) {
                $disk = Get-Disk -Number $vol.DiskNumber -ErrorAction SilentlyContinue
                $partition = Get-Partition -DiskNumber $vol.DiskNumber -PartitionNumber $vol.PartitionNumber -ErrorAction SilentlyContinue
                
                $obj = @{
                    DriveLetter = [string]$vol.DriveLetter
                    Label = $vol.FileSystemLabel
                    FileSystem = $vol.FileSystemType
                    Size = $vol.Size
                    SizeRemaining = $vol.SizeRemaining
                    HealthStatus = $vol.HealthStatus
                    DiskNumber = $vol.DiskNumber
                    DiskModel = if ($disk) { $disk.Model } else { $null }
                    DiskType = if ($disk) { $disk.MediaType } else { $null }
                    PartitionStyle = if ($disk) { $disk.PartitionStyle } else { $null }
                    InterfaceType = if ($disk) { $disk.BusType } else { $null }
                }
                $result += $obj
            }
            $result | ConvertTo-Json -Depth 10
            """
            
            result = subprocess.run(
                ["powershell", "-Command", ps_command],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode == 0 and result.stdout.strip():
                output = result.stdout.strip()
                # Clean output
                lines = output.split('\n')
                json_lines = []
                in_json = False
                for line in lines:
                    if line.strip().startswith('[') or line.strip().startswith('{'):
                        in_json = True
                    if in_json:
                        json_lines.append(line)
                
                if json_lines:
                    output = '\n'.join(json_lines)
                    volumes_data = json.loads(output)
                    if not isinstance(volumes_data, list):
                        volumes_data = [volumes_data]
                    
                    for vol_data in volumes_data:
                        drive_letter = vol_data.get("DriveLetter")
                        if drive_letter and isinstance(drive_letter, str) and len(drive_letter) > 0:
                            drive_letter = drive_letter[0] if len(drive_letter) > 0 else None
                        
                        size_gb = round(vol_data.get("Size", 0) / (1024**3), 2) if vol_data.get("Size") else 0.0
                        free_gb = round(vol_data.get("SizeRemaining", 0) / (1024**3), 2) if vol_data.get("SizeRemaining") else 0.0
                        used_gb = round(size_gb - free_gb, 2)
                        usage_percent = round((used_gb / size_gb * 100) if size_gb > 0 else 0, 2)
                        
                        volume_id = f"vol_{drive_letter or 'unknown'}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
                        
                        volume = VolumeInfo(
                            volume_id=volume_id,
                            drive_letter=drive_letter,
                            label=vol_data.get("Label"),
                            file_system=vol_data.get("FileSystem"),
                            size_gb=size_gb,
                            free_space_gb=free_gb,
                            used_space_gb=used_gb,
                            usage_percent=usage_percent,
                            disk_number=vol_data.get("DiskNumber"),
                            disk_model=vol_data.get("DiskModel"),
                            disk_type=vol_data.get("DiskType"),
                            health_status=vol_data.get("HealthStatus"),
                            partition_style=vol_data.get("PartitionStyle"),
                            interface_type=vol_data.get("InterfaceType")
                        )
                        
                        volumes.append(volume)
                        logger.info(f"Discovered volume: {drive_letter}: ({size_gb} GB, {free_gb} GB free)")
            
        except json.JSONDecodeError as e:
            logger.error(f"Error parsing PowerShell output: {e}")
        except subprocess.TimeoutExpired:
            logger.error("PowerShell command timed out")
        except Exception as e:
            logger.error(f"Error discovering volumes: {e}")
        
        return volumes
    
    def analyze_utilization(self, volume: VolumeInfo) -> VolumeUtilization:
        """Analyze volume and suggest utilization"""
        drive_letter = volume.drive_letter or "Unknown"
        
        # Determine recommended use based on volume properties
        recommended_use = "general"
        priority = 5
        actions = []
        notes = ""
        
        # Large free space (>500GB) - good for backups/archives
        if volume.free_space_gb > 500:
            recommended_use = "backup_archive"
            priority = 8
            actions = [
                f"Create backup directory structure on {drive_letter}:",
                f"  - {drive_letter}:\\Backups\\System",
                f"  - {drive_letter}:\\Backups\\Projects",
                f"  - {drive_letter}:\\Archives",
                f"Set up automated backup scripts",
                f"Configure backup schedule"
            ]
            notes = f"Large capacity ({volume.size_gb} GB) with {volume.free_space_gb} GB free - ideal for backups and archives"
        
        # SSD with good health - workspace/active projects
        elif volume.disk_type and "ssd" in str(volume.disk_type).lower():
            recommended_use = "workspace_active"
            priority = 9
            actions = [
                f"Use {drive_letter}: for active projects",
                f"Create workspace directories",
                f"Move frequently accessed files here",
                f"Configure development tools to use this drive"
            ]
            notes = f"SSD drive - fast access, ideal for active workspace"
        
        # Removable drive - portable workspace
        elif volume.disk_type and "removable" in str(volume.disk_type).lower():
            recommended_use = "portable_workspace"
            priority = 7
            actions = [
                f"Use {drive_letter}: for portable projects",
                f"Create portable workspace structure",
                f"Sync with cloud storage",
                f"Keep portable tools and data here"
            ]
            notes = "Removable drive - portable workspace"
        
        # System drive (C:) - keep system only
        elif drive_letter.upper() == "C":
            recommended_use = "system_only"
            priority = 10
            actions = [
                "Keep system files only",
                "Move user data to other drives",
                "Keep free space >20% for system health",
                "Regular cleanup and optimization"
            ]
            notes = "System drive - keep minimal, optimize regularly"
        
        # Medium capacity (100-500GB) - project storage
        elif 100 <= volume.size_gb <= 500:
            recommended_use = "project_storage"
            priority = 6
            actions = [
                f"Use {drive_letter}: for project storage",
                f"Create project directory structure",
                f"Organize by project type",
                f"Regular archive old projects"
            ]
            notes = f"Medium capacity ({volume.size_gb} GB) - good for project storage"
        
        # Small capacity (<100GB) - utilities/tools
        elif volume.size_gb < 100:
            recommended_use = "utilities_tools"
            priority = 4
            actions = [
                f"Use {drive_letter}: for utilities and tools",
                f"Portable applications",
                f"Temporary workspace",
                f"Quick access tools"
            ]
            notes = f"Small capacity ({volume.size_gb} GB) - utilities and tools"
        
        # High usage (>80%) - needs cleanup
        if volume.usage_percent > 80:
            actions.append(f"[WARNING] {volume.usage_percent}% used - cleanup needed")
            priority = max(priority, 8)
            notes += f" High usage ({volume.usage_percent}%) - consider cleanup or migration"
        
        return VolumeUtilization(
            volume_id=volume.volume_id,
            drive_letter=drive_letter,
            recommended_use=recommended_use,
            priority=priority,
            utilization_actions=actions,
            notes=notes
        )
    
    def discover_and_utilize(self) -> Dict[str, Any]:
        """Discover volumes and create utilization plans"""
        logger.info("Discovering volumes and creating utilization plans...")
        
        # Discover volumes
        discovered_volumes = self.discover_volumes()
        
        # Update or add volumes
        for new_vol in discovered_volumes:
            existing = next((v for v in self.volumes if v.drive_letter == new_vol.drive_letter), None)
            if existing:
                # Update existing
                existing.size_gb = new_vol.size_gb
                existing.free_space_gb = new_vol.free_space_gb
                existing.used_space_gb = new_vol.used_space_gb
                existing.usage_percent = new_vol.usage_percent
                existing.health_status = new_vol.health_status
                existing.discovered_at = datetime.now().isoformat()
                logger.info(f"Updated volume: {existing.drive_letter}:")
            else:
                # Add new
                self.volumes.append(new_vol)
                logger.info(f"Added new volume: {new_vol.drive_letter}:")
        
        # Create utilization plans
        self.utilizations = []
        for volume in self.volumes:
            utilization = self.analyze_utilization(volume)
            self.utilizations.append(utilization)
        
        # Sort by priority
        self.utilizations.sort(key=lambda x: x.priority, reverse=True)
        
        self._save_data()
        
        return {
            "volumes_discovered": len(discovered_volumes),
            "total_volumes": len(self.volumes),
            "utilizations_created": len(self.utilizations)
        }


def main():
    """Main function"""
    system = VolumeDiscoverySystem(user_id="jan")
    
    print("\n" + "="*80)
    print("VOLUME DISCOVERY & UTILIZATION SYSTEM")
    print("="*80)
    print("\nDiscovering all volumes on system...")
    
    result = system.discover_and_utilize()
    
    print("\n" + "-"*80)
    print("DISCOVERY COMPLETE")
    print("-"*80)
    print(f"\nVolumes Discovered: {result['volumes_discovered']}")
    print(f"Total Volumes: {result['total_volumes']}")
    print(f"Utilization Plans: {result['utilizations_created']}")
    
    if system.volumes:
        print("\n" + "-"*80)
        print("DISCOVERED VOLUMES:")
        print("-"*80)
        for vol in system.volumes:
            print(f"\n  {vol.drive_letter}: ({vol.label or 'No Label'})")
            print(f"    Size: {vol.size_gb} GB")
            print(f"    Free: {vol.free_space_gb} GB ({100 - vol.usage_percent:.1f}%)")
            print(f"    Used: {vol.used_space_gb} GB ({vol.usage_percent:.1f}%)")
            print(f"    Type: {vol.disk_type or 'Unknown'}")
            print(f"    Model: {vol.disk_model or 'Unknown'}")
            print(f"    Health: {vol.health_status or 'Unknown'}")
    
    if system.utilizations:
        print("\n" + "-"*80)
        print("UTILIZATION RECOMMENDATIONS:")
        print("-"*80)
        for util in system.utilizations:
            print(f"\n  {util.drive_letter}: - {util.recommended_use.replace('_', ' ').title()} (Priority: {util.priority})")
            print(f"    {util.notes}")
            if util.utilization_actions:
                print("    Actions:")
                for action in util.utilization_actions:
                    print(f"      - {action}")
    
    print("\n" + "="*80)
    print("Volume discovery and utilization complete.")
    print("="*80)
    
    logger.info(f"Volume discovery complete: {result['total_volumes']} volumes, {result['utilizations_created']} utilization plans")

if __name__ == "__main__":
    standard_main(main, script_name="volume_discovery_utilization.py")
