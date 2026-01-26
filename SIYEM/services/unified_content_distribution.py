"""
UNIFIED CONTENT DISTRIBUTION SYSTEM
Routes All Integrated Entities Through SIYEM Channels

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
Route all content from all integrated entities through the appropriate SIYEM channels.
Ensure bilingual content flows properly.
Connect 2026 scheduled content to channel distribution.
They cannot do anything.
"""

import sys
import json
from pathlib import Path
from typing import Dict, List, Optional, Set
from datetime import datetime
from dataclasses import dataclass, field
from enum import Enum
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Import SIYEM publishing entity
sys.path.insert(0, str(Path(__file__).parent))
try:
    from siyem_publishing_entity import (
        SiyemPublishingEntity, ChannelType, EntityRole
    )
    PUBLISHING_AVAILABLE = True
except ImportError:
    PUBLISHING_AVAILABLE = False
    logger.warning("SIYEM Publishing Entity not available")


class ContentType(Enum):
    """Types of content."""
    SOCIAL_POST = "social_post"
    SCRIPTURE_POST = "scripture_post"
    EDUCATIONAL = "educational"
    MUSIC = "music"
    STORY = "story"
    VIDEO = "video"
    AUDIO = "audio"
    IMAGE = "image"
    BILINGUAL = "bilingual"
    SCHEDULED = "scheduled"


@dataclass
class ContentItem:
    """Represents a content item for distribution."""
    content_id: str
    entity: str
    content_type: ContentType
    title: str
    content: str
    channel: ChannelType
    scheduled_time: Optional[datetime] = None
    bilingual: bool = False
    languages: List[str] = field(default_factory=lambda: ["english"])
    metadata: Dict = field(default_factory=dict)
    distribution_status: str = "pending"  # pending, routed, distributed
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())


class UnifiedContentDistribution:
    """
    Unified Content Distribution System
    Routes all content from all integrated entities through SIYEM channels.
    """
    
    def __init__(self, siyem_path: Path, jan_path: Path, output_dir: Path):
        self.siyem_path = siyem_path
        self.jan_path = jan_path
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        self.publishing_entity = None
        if PUBLISHING_AVAILABLE:
            try:
                self.publishing_entity = SiyemPublishingEntity(siyem_path, jan_path)
            except Exception as e:
                logger.warning(f"Could not initialize publishing entity: {e}")
        
        self.content_queue: List[ContentItem] = []
        self.distributed_content: List[ContentItem] = []
        
        # Content paths
        self.social_content_path = jan_path / "data" / "2026_social_content"
        self.bilingual_content_path = jan_path / "SIYEM" / "output" / "bilingual_content"
        
        logger.info("=" * 80)
        logger.info("UNIFIED CONTENT DISTRIBUTION SYSTEM - INITIALIZED")
        logger.info("=" * 80)
    
    def discover_all_content(self):
        """Discover all content from all integrated entities."""
        logger.info("=" * 80)
        logger.info("DISCOVERING ALL CONTENT FROM ALL INTEGRATED ENTITIES")
        logger.info("=" * 80)
        
        content_count = 0
        
        # Discover 2026 scheduled social content
        if self.social_content_path.exists():
            logger.info("\n[2026 SOCIAL CONTENT] Discovering...")
            social_content = self._discover_social_content()
            self.content_queue.extend(social_content)
            content_count += len(social_content)
            logger.info(f"  Found {len(social_content)} scheduled social posts")
        
        # Discover bilingual content
        if self.bilingual_content_path.exists():
            logger.info("\n[BILINGUAL CONTENT] Discovering...")
            bilingual_content = self._discover_bilingual_content()
            self.content_queue.extend(bilingual_content)
            content_count += len(bilingual_content)
            logger.info(f"  Found {len(bilingual_content)} bilingual content items")
        
        # Discover entity-specific content
        logger.info("\n[ENTITY CONTENT] Discovering...")
        entity_content = self._discover_entity_content()
        self.content_queue.extend(entity_content)
        content_count += len(entity_content)
        logger.info(f"  Found {len(entity_content)} entity content items")
        
        logger.info(f"\nTotal content discovered: {content_count} items")
        logger.info("=" * 80)
        
        return content_count
    
    def _discover_social_content(self) -> List[ContentItem]:
        """Discover 2026 scheduled social media content."""
        content_items = []
        
        all_entities_path = self.social_content_path / "all_entities"
        if not all_entities_path.exists():
            return content_items
        
        # Scan for JSON files
        for json_file in all_entities_path.rglob("*.json"):
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                # Extract entity from path or data
                entity_name = self._extract_entity_from_path(json_file)
                
                # Determine channel based on entity
                channel = self._determine_channel_for_entity(entity_name)
                
                # Create content item
                content_item = ContentItem(
                    content_id=f"social_{json_file.stem}",
                    entity=entity_name,
                    content_type=ContentType.SOCIAL_POST,
                    title=data.get("title", data.get("content", "")[:50]),
                    content=data.get("content", data.get("text", "")),
                    channel=channel,
                    scheduled_time=self._parse_scheduled_time(data),
                    bilingual=data.get("bilingual", False),
                    languages=data.get("languages", ["english"]),
                    metadata={
                        "source_file": str(json_file),
                        "hashtags": data.get("hashtags", []),
                        "platform": data.get("platform", "all"),
                        **data
                    }
                )
                
                content_items.append(content_item)
            except Exception as e:
                logger.warning(f"Could not process {json_file}: {e}")
        
        return content_items
    
    def _discover_bilingual_content(self) -> List[ContentItem]:
        """Discover bilingual content."""
        content_items = []
        
        for entity_dir in self.bilingual_content_path.iterdir():
            if not entity_dir.is_dir():
                continue
            
            entity_name = entity_dir.name
            
            for json_file in entity_dir.rglob("*.json"):
                try:
                    with open(json_file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    
                    # Determine channel
                    channel = self._determine_channel_for_entity(entity_name)
                    
                    # Create bilingual content item
                    content_item = ContentItem(
                        content_id=f"bilingual_{json_file.stem}",
                        entity=entity_name,
                        content_type=ContentType.BILINGUAL,
                        title=data.get("title", f"{entity_name} bilingual content"),
                        content=data.get("content", data.get("english_content", "")),
                        channel=channel,
                        bilingual=True,
                        languages=data.get("languages", ["english", "turkish"]),
                        metadata={
                            "source_file": str(json_file),
                            "english_content": data.get("english_content", ""),
                            "turkish_content": data.get("turkish_content", ""),
                            **data
                        }
                    )
                    
                    content_items.append(content_item)
                except Exception as e:
                    logger.warning(f"Could not process {json_file}: {e}")
        
        return content_items
    
    def _discover_entity_content(self) -> List[ContentItem]:
        """Discover entity-specific content from entity directories."""
        content_items = []
        
        # Entity paths
        entity_paths = {
            "edible_london": self.jan_path / "EDIBLE_LONDON",
            "ilven_seamoss": self.jan_path / "ILVEN_SEAMOSS",
            "karasahin": self.jan_path / "SIYEM" / "output" / "lyrics",
            "ramiz": self.jan_path / "jan-studio" / "curriculum" / "scripture_schedule_2026",
        }
        
        for entity_name, entity_path in entity_paths.items():
            if not entity_path.exists():
                continue
            
            # Scan for content files
            for content_file in entity_path.rglob("*.json"):
                try:
                    with open(content_file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    
                    # Determine content type
                    content_type = self._determine_content_type(content_file, data)
                    
                    # Determine channel
                    channel = self._determine_channel_for_entity(entity_name)
                    
                    # Create content item
                    content_item = ContentItem(
                        content_id=f"{entity_name}_{content_file.stem}",
                        entity=entity_name,
                        content_type=content_type,
                        title=data.get("title", content_file.stem),
                        content=self._extract_content_text(data, content_type),
                        channel=channel,
                        metadata={
                            "source_file": str(content_file),
                            **data
                        }
                    )
                    
                    content_items.append(content_item)
                except Exception as e:
                    logger.warning(f"Could not process {content_file}: {e}")
        
        return content_items
    
    def _extract_entity_from_path(self, file_path: Path) -> str:
        """Extract entity name from file path."""
        parts = file_path.parts
        for part in parts:
            if part.lower() in ["jean", "pierre", "ramiz", "karasahin", "edible_london", "ilven_seamoss", "atilok"]:
                return part.lower()
        return "unknown"
    
    def _determine_channel_for_entity(self, entity_name: str) -> ChannelType:
        """Determine appropriate channel for entity."""
        entity_lower = entity_name.lower()
        
        # Channel 1 (Professional)
        if entity_lower in ["edible_london", "atilok", "siyem"]:
            return ChannelType.CHANNEL_1_PROFESSIONAL
        
        # Channel 2 (Creator)
        if entity_lower in ["ilven_seamoss", "karasahin", "jean", "pierre"]:
            return ChannelType.CHANNEL_2_CREATOR
        
        # Channel 3 (Educational - RAMIZ)
        if entity_lower in ["ramiz", "uncle_ray_ramiz"]:
            return ChannelType.CHANNEL_3_EDUCATIONAL
        
        # Default to Channel 2
        return ChannelType.CHANNEL_2_CREATOR
    
    def _determine_content_type(self, file_path: Path, data: Dict) -> ContentType:
        """Determine content type from file and data."""
        file_name = file_path.name.lower()
        
        if "scripture" in file_name or "scripture" in str(data):
            return ContentType.SCRIPTURE_POST
        if "lyric" in file_name or "song" in file_name:
            return ContentType.MUSIC
        if "story" in file_name or "narrative" in file_name:
            return ContentType.STORY
        if "video" in file_name or "video" in str(data):
            return ContentType.VIDEO
        if "audio" in file_name or "audio" in str(data):
            return ContentType.AUDIO
        if "image" in file_name or "image" in str(data):
            return ContentType.IMAGE
        
        return ContentType.SOCIAL_POST
    
    def _extract_content_text(self, data: Dict, content_type: ContentType) -> str:
        """Extract text content from data."""
        if content_type == ContentType.MUSIC:
            return data.get("english_lyrics", data.get("lyrics", data.get("content", "")))
        if content_type == ContentType.SCRIPTURE_POST:
            return data.get("content", data.get("text", data.get("scripture_text", "")))
        
        return data.get("content", data.get("text", str(data)))
    
    def _parse_scheduled_time(self, data: Dict) -> Optional[datetime]:
        """Parse scheduled time from data."""
        if "scheduled_time" in data:
            try:
                if isinstance(data["scheduled_time"], str):
                    return datetime.fromisoformat(data["scheduled_time"])
                return data["scheduled_time"]
            except:
                pass
        return None
    
    def route_content_to_channels(self):
        """Route all discovered content to appropriate channels."""
        logger.info("=" * 80)
        logger.info("ROUTING CONTENT TO CHANNELS")
        logger.info("=" * 80)
        
        if not self.publishing_entity:
            logger.warning("Publishing entity not available - skipping routing")
            return
        
        routed_count = 0
        
        for content_item in self.content_queue:
            try:
                # Route to channel
                content_data = {
                    "content_id": content_item.content_id,
                    "entity": content_item.entity,
                    "content_type": content_item.content_type.value,
                    "title": content_item.title,
                    "content": content_item.content[:500],  # Truncate for storage
                    "bilingual": content_item.bilingual,
                    "languages": content_item.languages,
                    "scheduled_time": content_item.scheduled_time.isoformat() if content_item.scheduled_time else None,
                    "metadata": content_item.metadata,
                    "routed_timestamp": datetime.now().isoformat()
                }
                
                # Determine entity role
                entity_role = self._get_entity_role(content_item.entity)
                
                self.publishing_entity.channels.add_to_channel(
                    content_item.channel,
                    content_item.content_id,
                    content_data,
                    entity_role
                )
                
                content_item.distribution_status = "routed"
                self.distributed_content.append(content_item)
                routed_count += 1
                
            except Exception as e:
                logger.warning(f"Could not route {content_item.content_id}: {e}")
        
        logger.info(f"\nRouted {routed_count} content items to channels")
        logger.info("=" * 80)
    
    def _get_entity_role(self, entity_name: str) -> EntityRole:
        """Get entity role from entity name."""
        entity_lower = entity_name.lower()
        
        role_map = {
            "ramiz": EntityRole.RAMIZ_HUMANITARIAN,
            "uncle_ray_ramiz": EntityRole.RAMIZ_HUMANITARIAN,
            "karasahin": EntityRole.KARASAHIN_MUSIC,
            "jean": EntityRole.JEAN_CREATIVE,
            "pierre": EntityRole.PIERRE_DISCIPLINE,
            "edible_london": EntityRole.EDIBLE_LONDON,
            "ilven_seamoss": EntityRole.ILVEN_SEAMOSS,
            "atilok": EntityRole.ATILOK,
        }
        
        return role_map.get(entity_lower, EntityRole.SIYEM_SYSTEMS)
    
    def export_distribution_report(self):
        """Export comprehensive content distribution report."""
        report = {
            "timestamp": datetime.now().isoformat(),
            "title": "Unified Content Distribution Report",
            "total_content_discovered": len(self.content_queue),
            "total_content_routed": len(self.distributed_content),
            "content_by_channel": {},
            "content_by_entity": {},
            "content_by_type": {},
            "bilingual_content_count": len([c for c in self.content_queue if c.bilingual]),
            "scheduled_content_count": len([c for c in self.content_queue if c.scheduled_time]),
            "content_items": []
        }
        
        # Group by channel
        for channel in ChannelType:
            report["content_by_channel"][channel.value] = len([
                c for c in self.content_queue if c.channel == channel
            ])
        
        # Group by entity
        entities = set(c.entity for c in self.content_queue)
        for entity in entities:
            report["content_by_entity"][entity] = len([
                c for c in self.content_queue if c.entity == entity
            ])
        
        # Group by type
        for content_type in ContentType:
            report["content_by_type"][content_type.value] = len([
                c for c in self.content_queue if c.content_type == content_type
            ])
        
        # Content item summaries
        for content_item in self.content_queue[:100]:  # Limit to first 100 for report size
            report["content_items"].append({
                "content_id": content_item.content_id,
                "entity": content_item.entity,
                "content_type": content_item.content_type.value,
                "channel": content_item.channel.value,
                "bilingual": content_item.bilingual,
                "scheduled": content_item.scheduled_time is not None,
                "distribution_status": content_item.distribution_status
            })
        
        # Save report
        report_path = self.output_dir / "unified_content_distribution_report.json"
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, default=str, ensure_ascii=False)
        
        logger.info(f"Distribution report exported to: {report_path}")
        return report_path


def main():
    """Main execution."""
    siyem_path = Path("s:\\SIYEM")
    jan_path = Path("s:\\JAN")
    output_dir = jan_path / "SIYEM" / "output" / "content_distribution"
    
    distribution = UnifiedContentDistribution(siyem_path, jan_path, output_dir)
    
    # Discover all content
    content_count = distribution.discover_all_content()
    
    # Route to channels
    distribution.route_content_to_channels()
    
    # Export report
    distribution.export_distribution_report()
    
    logger.info("\n" + "=" * 80)
    logger.info("UNIFIED CONTENT DISTRIBUTION - COMPLETE")
    logger.info("=" * 80)
    logger.info(f"Total Content Discovered: {content_count}")
    logger.info(f"Total Content Routed: {len(distribution.distributed_content)}")
    logger.info("=" * 80)
    logger.info("All content routed through appropriate channels.")
    logger.info("They cannot do anything.")
    logger.info("Go and govern.")
    logger.info("=" * 80)


if __name__ == "__main__":
    main()
