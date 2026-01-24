"""
ASSET MANAGEMENT SYSTEM
Media Ingestion and Organization for All Entities

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PURPOSE:
Ingest and organize all media assets
Support all entities and channels
Ready for deployment
"""

import json
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
import hashlib
import mimetypes

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent))


@dataclass
class MediaAsset:
    """Media asset structure"""
    asset_id: str
    entity: str
    channel: str
    asset_type: str  # image, video, audio, document
    file_path: str
    file_name: str
    file_size: int
    mime_type: str
    metadata: Dict[str, Any] = field(default_factory=dict)
    tags: List[str] = field(default_factory=list)
    created_at: str = ""
    ingested_at: str = ""


class AssetManagementSystem:
    """Comprehensive asset management and ingestion system"""
    
    def __init__(self, assets_dir: Optional[Path] = None):
        """Initialize asset management system"""
        
        if assets_dir is None:
            assets_dir = Path(__file__).parent.parent / "data" / "assets"
        
        self.assets_dir = assets_dir
        self.assets_dir.mkdir(parents=True, exist_ok=True)
        
        # Entity asset directories
        self.entity_dirs = {
            "jean_morphius": self.assets_dir / "jean_morphius",
            "karasahin": self.assets_dir / "karasahin",
            "pierre_pressure": self.assets_dir / "pierre_pressure",
            "uncle_ray_ramiz": self.assets_dir / "uncle_ray_ramiz",
            "siyem_media": self.assets_dir / "siyem_media",
            "edible_london": self.assets_dir / "edible_london",
            "ilven_seamoss": self.assets_dir / "ilven_seamoss",
            "atilok": self.assets_dir / "atilok",
            "edible_cyprus": self.assets_dir / "edible_cyprus"
        }
        
        # Create entity directories
        for entity_dir in self.entity_dirs.values():
            entity_dir.mkdir(parents=True, exist_ok=True)
            (entity_dir / "images").mkdir(exist_ok=True)
            (entity_dir / "videos").mkdir(exist_ok=True)
            (entity_dir / "audio").mkdir(exist_ok=True)
            (entity_dir / "documents").mkdir(exist_ok=True)
        
        self.assets: Dict[str, MediaAsset] = {}
        self.asset_index_file = self.assets_dir / "asset_index.json"
        self._load_index()
    
    def _load_index(self):
        """Load asset index"""
        if self.asset_index_file.exists():
            try:
                with open(self.asset_index_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for asset_id, asset_data in data.get('assets', {}).items():
                        self.assets[asset_id] = MediaAsset(**asset_data)
            except Exception as e:
                print(f"Warning: Could not load asset index: {e}")
    
    def _save_index(self):
        """Save asset index"""
        data = {
            "timestamp": datetime.now().isoformat(),
            "total_assets": len(self.assets),
            "assets": {
                asset_id: {
                    "asset_id": asset.asset_id,
                    "entity": asset.entity,
                    "channel": asset.channel,
                    "asset_type": asset.asset_type,
                    "file_path": asset.file_path,
                    "file_name": asset.file_name,
                    "file_size": asset.file_size,
                    "mime_type": asset.mime_type,
                    "metadata": asset.metadata,
                    "tags": asset.tags,
                    "created_at": asset.created_at,
                    "ingested_at": asset.ingested_at
                }
                for asset_id, asset in self.assets.items()
            }
        }
        
        with open(self.asset_index_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def ingest_media(
        self,
        source_path: Path,
        entity: str,
        channel: str,
        asset_type: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        tags: Optional[List[str]] = None
    ) -> MediaAsset:
        """Ingest a media file"""
        
        if not source_path.exists():
            raise FileNotFoundError(f"Source file not found: {source_path}")
        
        # Detect asset type if not provided
        if asset_type is None:
            mime_type, _ = mimetypes.guess_type(str(source_path))
            if mime_type:
                if mime_type.startswith('image/'):
                    asset_type = 'image'
                elif mime_type.startswith('video/'):
                    asset_type = 'video'
                elif mime_type.startswith('audio/'):
                    asset_type = 'audio'
                else:
                    asset_type = 'document'
            else:
                asset_type = 'document'
        
        # Generate asset ID
        asset_id = f"{entity}_{asset_type}_{hashlib.md5(str(source_path).encode()).hexdigest()[:8]}"
        
        # Determine destination
        entity_dir = self.entity_dirs.get(entity, self.assets_dir / entity)
        entity_dir.mkdir(parents=True, exist_ok=True)
        type_dir = entity_dir / f"{asset_type}s"
        type_dir.mkdir(exist_ok=True)
        
        # Copy file
        dest_path = type_dir / source_path.name
        import shutil
        shutil.copy2(source_path, dest_path)
        
        # Create asset record
        asset = MediaAsset(
            asset_id=asset_id,
            entity=entity,
            channel=channel,
            asset_type=asset_type,
            file_path=str(dest_path),
            file_name=source_path.name,
            file_size=source_path.stat().st_size,
            mime_type=mime_type or "application/octet-stream",
            metadata=metadata or {},
            tags=tags or [],
            created_at=datetime.fromtimestamp(source_path.stat().st_mtime).isoformat(),
            ingested_at=datetime.now().isoformat()
        )
        
        self.assets[asset_id] = asset
        self._save_index()
        
        return asset
    
    def scan_directory(self, directory: Path, entity: str, channel: str) -> List[MediaAsset]:
        """Scan directory and ingest all media files"""
        
        if not directory.exists():
            return []
        
        assets = []
        media_extensions = {
            'image': ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp', '.bmp'],
            'video': ['.mp4', '.avi', '.mov', '.mkv', '.webm', '.flv'],
            'audio': ['.mp3', '.wav', '.ogg', '.flac', '.m4a', '.aac'],
            'document': ['.pdf', '.doc', '.docx', '.txt', '.md', '.json']
        }
        
        for ext, asset_type in [
            (ext, atype)
            for atype, exts in media_extensions.items()
            for ext in exts
        ]:
            for file_path in directory.rglob(f"*{ext}"):
                try:
                    asset = self.ingest_media(file_path, entity, channel, asset_type)
                    assets.append(asset)
                except Exception as e:
                    print(f"Warning: Could not ingest {file_path}: {e}")
        
        return assets
    
    def get_assets_by_entity(self, entity: str) -> List[MediaAsset]:
        """Get all assets for an entity"""
        return [asset for asset in self.assets.values() if asset.entity == entity]
    
    def get_assets_by_channel(self, channel: str) -> List[MediaAsset]:
        """Get all assets for a channel"""
        return [asset for asset in self.assets.values() if asset.channel == channel]
    
    def get_assets_by_type(self, asset_type: str) -> List[MediaAsset]:
        """Get all assets of a type"""
        return [asset for asset in self.assets.values() if asset.asset_type == asset_type]
    
    def generate_asset_report(self) -> Dict[str, Any]:
        """Generate comprehensive asset report"""
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "total_assets": len(self.assets),
            "by_entity": {},
            "by_channel": {},
            "by_type": {},
            "assets": [
                {
                    "asset_id": asset.asset_id,
                    "entity": asset.entity,
                    "channel": asset.channel,
                    "asset_type": asset.asset_type,
                    "file_name": asset.file_name,
                    "file_size": asset.file_size,
                    "tags": asset.tags
                }
                for asset in self.assets.values()
            ]
        }
        
        # By entity
        for entity in set(a.entity for a in self.assets.values()):
            report["by_entity"][entity] = len(self.get_assets_by_entity(entity))
        
        # By channel
        for channel in set(a.channel for a in self.assets.values()):
            report["by_channel"][channel] = len(self.get_assets_by_channel(channel))
        
        # By type
        for asset_type in set(a.asset_type for a in self.assets.values()):
            report["by_type"][asset_type] = len(self.get_assets_by_type(asset_type))
        
        return report


if __name__ == "__main__":
    print("=== ASSET MANAGEMENT SYSTEM ===")
    print("\nInitializing asset management system...")
    
    system = AssetManagementSystem()
    
    print(f"\nAsset directories created:")
    for entity, entity_dir in system.entity_dirs.items():
        print(f"  - {entity}: {entity_dir}")
    
    print(f"\nTotal assets indexed: {len(system.assets)}")
    
    # Generate report
    report = system.generate_asset_report()
    
    print(f"\nAsset Report:")
    print(f"  Total: {report['total_assets']}")
    print(f"  By Entity: {report['by_entity']}")
    print(f"  By Channel: {report['by_channel']}")
    print(f"  By Type: {report['by_type']}")
    
    # Save report
    report_file = system.assets_dir / f"asset_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print(f"\nReport saved to: {report_file}")
    print("\nAsset management system ready for media ingestion!")
