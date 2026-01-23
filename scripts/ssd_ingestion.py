"""
SSD INGESTION SYSTEM
Ingest and integrate SSD information into the system

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
INGEST SSD INFORMATION
Integrate SSD data into system
Track SSD status and alignment
"""

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
class SSDInfo:
    """SSD information"""
    ssd_id: str
    model: str
    serial_number: Optional[str] = None
    capacity_gb: float = 0.0
    partition_style: Optional[str] = None
    file_system: Optional[str] = None
    health_status: Optional[str] = None
    drive_letter: Optional[str] = None
    interface_type: Optional[str] = None  # SATA, NVMe, etc.
    firmware_version: Optional[str] = None
    temperature: Optional[float] = None
    wear_level: Optional[float] = None  # Percentage
    ingested_at: str = field(default_factory=lambda: datetime.now().isoformat())
    source: str = "powershell"  # powershell, wmi, etc.

@dataclass
class SSDIngestion:
    """SSD ingestion record"""
    ingestion_id: str
    timestamp: str
    ssd_count: int = 0
    ssds: List[SSDInfo] = field(default_factory=list)
    ingestion_method: str = "powershell"
    status: str = "completed"
    notes: str = ""
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())

class SSDIngestionSystem:
    """
    SSD Ingestion System
    Ingest and integrate SSD information into the system
    """
    
    def __init__(self, user_id: str = "jan", data_dir: Path = None):
        self.user_id = user_id
        self.data_dir = data_dir or Path(__file__).parent.parent / "data" / "ssd_ingestion"
        self.data_dir.mkdir(parents=True, exist_ok=True)
        
        self.ssds_file = self.data_dir / f"{user_id}_ssds.json"
        self.ingestions_file = self.data_dir / f"{user_id}_ingestions.json"
        
        self.ssds: List[SSDInfo] = []
        self.ingestions: List[SSDIngestion] = []
        
        self._load_data()
    
    def _load_data(self):
        """Load SSD data"""
        if self.ssds_file.exists():
            try:
                data = load_json(self.ssds_file)
                self.ssds = [SSDInfo(**item) for item in data.get("ssds", [])]
            except Exception as e:
                logger.warning(f"Error loading SSDs: {e}")
                self.ssds = []
        else:
            self.ssds = []
        
        if self.ingestions_file.exists():
            try:
                data = load_json(self.ingestions_file)
                self.ingestions = [SSDIngestion(**item) for item in data.get("ingestions", [])]
            except Exception as e:
                logger.warning(f"Error loading ingestions: {e}")
                self.ingestions = []
        else:
            self.ingestions = []
    
    def _save_data(self):
        """Save SSD data"""
        try:
            save_json(
                {"ssds": [asdict(ssd) for ssd in self.ssds]},
                self.ssds_file
            )
            save_json(
                {"ingestions": [asdict(ing) for ing in self.ingestions]},
                self.ingestions_file
            )
        except Exception as e:
            logger.error(f"Error saving SSD data: {e}")
    
    def ingest_from_powershell(self) -> List[SSDInfo]:
        """Ingest SSD information using PowerShell"""
        logger.info("Ingesting SSD information from PowerShell...")
        
        ssds = []
        
        try:
            # Get all disks - simplified command
            ps_command = """
            $disks = Get-Disk
            $result = @()
            foreach ($disk in $disks) {
                $volumes = Get-Volume -DiskNumber $disk.Number -ErrorAction SilentlyContinue
                $volume = $volumes | Where-Object { $_.DriveLetter -ne $null } | Select-Object -First 1
                
                $obj = @{
                    Number = $disk.Number
                    Model = $disk.Model
                    SerialNumber = $disk.SerialNumber
                    Size = $disk.Size
                    PartitionStyle = $disk.PartitionStyle
                    MediaType = $disk.MediaType
                    BusType = $disk.BusType
                    FirmwareVersion = $disk.FirmwareVersion
                    HealthStatus = $disk.HealthStatus
                    DriveLetter = if ($volume) { [string]$volume.DriveLetter } else { $null }
                    FileSystem = if ($volume) { $volume.FileSystemType } else { $null }
                    Health = if ($volume) { $volume.HealthStatus } else { $null }
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
                # Remove any PowerShell warnings/errors from output
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
                    disks_data = json.loads(output)
                    if not isinstance(disks_data, list):
                        disks_data = [disks_data]
                    
                    for disk_data in disks_data:
                        # Check if it's an SSD (MediaType = SSD or BusType = NVMe) or include all disks
                        media_type = str(disk_data.get("MediaType", "")).lower()
                        bus_type = str(disk_data.get("BusType", "")).lower()
                        model = str(disk_data.get("Model", "")).lower()
                        
                        is_ssd = (
                            "ssd" in media_type or
                            "nvme" in bus_type or
                            "nvme" in model or
                            disk_data.get("Number") == 0  # Include disk 0 (C: drive)
                        )
                        
                        if is_ssd:
                            ssd_id = f"ssd_{disk_data.get('Number', 'unknown')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
                            
                            drive_letter = disk_data.get("DriveLetter")
                            if drive_letter and isinstance(drive_letter, str) and len(drive_letter) > 0:
                                drive_letter = drive_letter[0] if len(drive_letter) > 0 else None
                            
                            ssd = SSDInfo(
                                ssd_id=ssd_id,
                                model=disk_data.get("Model", "Unknown"),
                                serial_number=disk_data.get("SerialNumber"),
                                capacity_gb=round(disk_data.get("Size", 0) / (1024**3), 2) if disk_data.get("Size") else 0.0,
                                partition_style=disk_data.get("PartitionStyle"),
                                file_system=disk_data.get("FileSystem"),
                                health_status=disk_data.get("Health") or disk_data.get("HealthStatus"),
                                drive_letter=drive_letter,
                                interface_type=disk_data.get("BusType"),
                                firmware_version=disk_data.get("FirmwareVersion")
                            )
                            
                            ssds.append(ssd)
                            logger.info(f"Ingested SSD: {ssd.model} ({ssd.capacity_gb} GB) - Drive: {ssd.drive_letter or 'N/A'}")
                else:
                    logger.warning("No JSON data found in PowerShell output")
            else:
                logger.warning(f"PowerShell command failed or returned no output. Return code: {result.returncode}")
                if result.stderr:
                    logger.warning(f"PowerShell stderr: {result.stderr[:200]}")
            
        except json.JSONDecodeError as e:
            logger.error(f"Error parsing PowerShell output: {e}")
            logger.debug(f"Output was: {result.stdout[:500] if 'result' in locals() else 'N/A'}")
        except subprocess.TimeoutExpired:
            logger.error("PowerShell command timed out")
        except Exception as e:
            logger.error(f"Error ingesting from PowerShell: {e}")
        
        return ssds
    
    def ingest(self, method: str = "powershell") -> SSDIngestion:
        """Ingest SSD information"""
        ingestion_id = f"ingestion_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        logger.info(f"Starting SSD ingestion: {ingestion_id}")
        
        ssds = []
        if method == "powershell":
            ssds = self.ingest_from_powershell()
        else:
            logger.warning(f"Unknown ingestion method: {method}")
        
        # Update or add SSDs
        for new_ssd in ssds:
            # Check if SSD already exists (by serial number or model)
            existing = None
            if new_ssd.serial_number:
                existing = next((s for s in self.ssds if s.serial_number == new_ssd.serial_number), None)
            if not existing:
                existing = next((s for s in self.ssds if s.model == new_ssd.model and s.capacity_gb == new_ssd.capacity_gb), None)
            
            if existing:
                # Update existing
                existing.model = new_ssd.model
                existing.capacity_gb = new_ssd.capacity_gb
                existing.partition_style = new_ssd.partition_style
                existing.file_system = new_ssd.file_system
                existing.health_status = new_ssd.health_status
                existing.drive_letter = new_ssd.drive_letter
                existing.interface_type = new_ssd.interface_type
                existing.firmware_version = new_ssd.firmware_version
                existing.ingested_at = datetime.now().isoformat()
                logger.info(f"Updated existing SSD: {existing.model}")
            else:
                # Add new
                self.ssds.append(new_ssd)
                logger.info(f"Added new SSD: {new_ssd.model}")
        
        # Create ingestion record
        ingestion = SSDIngestion(
            ingestion_id=ingestion_id,
            timestamp=datetime.now().isoformat(),
            ssd_count=len(ssds),
            ssds=ssds,
            ingestion_method=method,
            status="completed",
            notes=f"Ingested {len(ssds)} SSD(s)"
        )
        
        self.ingestions.append(ingestion)
        self._save_data()
        
        logger.info(f"SSD ingestion complete: {len(ssds)} SSD(s) ingested")
        
        return ingestion
    
    def get_ssds(self) -> List[SSDInfo]:
        """Get all ingested SSDs"""
        return self.ssds
    
    def get_ssd_by_drive_letter(self, drive_letter: str) -> Optional[SSDInfo]:
        """Get SSD by drive letter"""
        return next((s for s in self.ssds if s.drive_letter == drive_letter.upper()), None)
    
    def get_report(self) -> Dict[str, Any]:
        """Get ingestion report"""
        return {
            "total_ssds": len(self.ssds),
            "total_ingestions": len(self.ingestions),
            "ssds": [asdict(ssd) for ssd in self.ssds],
            "latest_ingestion": asdict(self.ingestions[-1]) if self.ingestions else None
        }


def main():
    """Main function"""
    system = SSDIngestionSystem(user_id="jan")
    
    print("\n" + "="*80)
    print("SSD INGESTION SYSTEM")
    print("="*80)
    print("\nIngesting SSD information...")
    
    ingestion = system.ingest(method="powershell")
    
    print("\n" + "-"*80)
    print("INGESTION COMPLETE")
    print("-"*80)
    print(f"\nSSDs Ingested: {ingestion.ssd_count}")
    print(f"Ingestion ID: {ingestion.ingestion_id}")
    print(f"Status: {ingestion.status}")
    
    ssds = system.get_ssds()
    if ssds:
        print("\n" + "-"*80)
        print("INGESTED SSDs:")
        print("-"*80)
        for ssd in ssds:
            print(f"\n  Model: {ssd.model}")
            print(f"  Capacity: {ssd.capacity_gb} GB")
            print(f"  Drive Letter: {ssd.drive_letter or 'N/A'}")
            print(f"  Partition Style: {ssd.partition_style or 'N/A'}")
            print(f"  File System: {ssd.file_system or 'N/A'}")
            print(f"  Health: {ssd.health_status or 'N/A'}")
            print(f"  Interface: {ssd.interface_type or 'N/A'}")
            if ssd.serial_number:
                print(f"  Serial: {ssd.serial_number}")
    
    report = system.get_report()
    print("\n" + "="*80)
    print(f"Total SSDs in system: {report['total_ssds']}")
    print(f"Total ingestions: {report['total_ingestions']}")
    print("="*80)
    
    logger.info(f"SSD ingestion complete: {ingestion.ssd_count} SSD(s) ingested")

if __name__ == "__main__":
    standard_main(main, script_name="ssd_ingestion.py")
