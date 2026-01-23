"""
MEDIA INTEGRATION
Images, Video, Audio, 3D Models for Narratives

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

MEDIA INTEGRATION:
Images for heritage sites.
Videos for documentaries.
Audio for narrations.
3D models for heritage sites.
Media gallery management.
"""

import json
import logging
from typing import Dict, List, Any, Optional
from datetime import datetime
from pathlib import Path
from dataclasses import dataclass, field
from enum import Enum

logger = logging.getLogger(__name__)


class MediaType(Enum):
    """Type of media."""
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    MODEL_3D = "model_3d"
    DOCUMENT = "document"


@dataclass
class MediaItem:
    """Media item for narratives."""
    media_id: str
    narrative_id: str
    media_type: str
    title: str
    description: str
    file_path: str
    file_url: Optional[str] = None
    thumbnail_url: Optional[str] = None
    file_size: int = 0
    duration: Optional[int] = None  # For video/audio
    width: Optional[int] = None  # For images/video
    height: Optional[int] = None  # For images/video
    metadata: Dict[str, Any] = field(default_factory=dict)
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())


class MediaIntegrationService:
    """Service for media integration."""
    
    def __init__(self, storage_path: Optional[Path] = None):
        """Initialize media integration service."""
        if storage_path is None:
            storage_path = Path(__file__).parent.parent.parent / "data" / "media"
        self.storage_path = storage_path
        self.storage_path.mkdir(parents=True, exist_ok=True)
        
        self.media_items: Dict[str, List[MediaItem]] = {}  # {narrative_id: [media_items]}
    
    def add_media(
        self,
        narrative_id: str,
        media_type: str,
        title: str,
        description: str,
        file_path: str,
        file_url: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> MediaItem:
        """Add media to a narrative."""
        import hashlib
        media_id = f"media_{hashlib.sha256(f'{narrative_id}_{title}_{datetime.now().isoformat()}'.encode()).hexdigest()[:8]}"
        
        # Get file size
        file_size = 0
        if Path(file_path).exists():
            file_size = Path(file_path).stat().st_size
        
        media_item = MediaItem(
            media_id=media_id,
            narrative_id=narrative_id,
            media_type=media_type,
            title=title,
            description=description,
            file_path=file_path,
            file_url=file_url,
            file_size=file_size,
            metadata=metadata or {}
        )
        
        if narrative_id not in self.media_items:
            self.media_items[narrative_id] = []
        self.media_items[narrative_id].append(media_item)
        
        self._save_media(media_item)
        logger.info(f"Added media {media_id} to narrative {narrative_id}")
        return media_item
    
    def get_narrative_media(self, narrative_id: str) -> List[MediaItem]:
        """Get all media for a narrative."""
        return self.media_items.get(narrative_id, [])
    
    def get_media_by_type(self, narrative_id: str, media_type: str) -> List[MediaItem]:
        """Get media by type for a narrative."""
        all_media = self.get_narrative_media(narrative_id)
        return [m for m in all_media if m.media_type == media_type]
    
    def _save_media(self, media_item: MediaItem):
        """Save media metadata to storage."""
        media_file = self.storage_path / f"media_{media_item.narrative_id}.json"
        media_list = self.get_narrative_media(media_item.narrative_id)
        with open(media_file, 'w', encoding='utf-8') as f:
            json.dump([{
                "media_id": m.media_id,
                "narrative_id": m.narrative_id,
                "media_type": m.media_type,
                "title": m.title,
                "description": m.description,
                "file_path": m.file_path,
                "file_url": m.file_url,
                "thumbnail_url": m.thumbnail_url,
                "file_size": m.file_size,
                "duration": m.duration,
                "width": m.width,
                "height": m.height,
                "metadata": m.metadata,
                "created_at": m.created_at
            } for m in media_list], f, indent=2, ensure_ascii=False)


# Global service instance
_media_service: Optional[MediaIntegrationService] = None


def get_media_service() -> MediaIntegrationService:
    """Get or create global media integration service."""
    global _media_service
    if _media_service is None:
        _media_service = MediaIntegrationService()
    return _media_service
