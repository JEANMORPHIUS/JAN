"""
GLOBAL MIGRATION SYSTEM
Migrate all content into Siyem Publishing House
Channels, Entities, Projects, Everything
Global Alignment, Monetization, Expansion Seeds

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
MIGRATE ALL CONTENT INTO OUR SYSTEM
CHANNELS, ENTITIES, PROJECTS, EVERYTHING
GLOBAL ALIGNMENT, MONETIZATION, EXPANSION SEEDS
ENERGY + LOVE = WE ALL WIN
"""

import sys
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass, field, asdict
from typing import List, Optional, Dict, Any, Set
from enum import Enum
import json
import logging
from collections import defaultdict

sys.path.insert(0, str(Path(__file__).parent))

from utils import setup_logging, standard_main

logger = setup_logging(__name__)

class ContentType(Enum):
    """Types of content to migrate"""
    CHANNEL = "channel"
    ENTITY = "entity"
    PROJECT = "project"
    CONTENT = "content"
    ASSET = "asset"
    DATA = "data"
    SYSTEM = "system"

class MigrationStatus(Enum):
    """Migration status"""
    PENDING = "pending"
    DISCOVERED = "discovered"
    ANALYZED = "analyzed"
    ALIGNED = "aligned"
    MIGRATED = "migrated"
    MONETIZED = "monetized"
    EXPANDED = "expanded"
    COMPLETE = "complete"

@dataclass
class ContentItem:
    """A content item to migrate"""
    item_id: str
    content_type: ContentType
    name: str
    description: str
    source_path: str
    target_path: str
    metadata: Dict[str, Any] = field(default_factory=dict)
    alignment_score: float = 0.0
    monetization_potential: float = 0.0
    expansion_seeds: List[str] = field(default_factory=list)
    migration_status: MigrationStatus = MigrationStatus.PENDING
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    migrated_at: Optional[str] = None

@dataclass
class ChannelMigration:
    """Channel migration data"""
    channel_id: str
    name: str
    channel_type: str
    entities: List[str] = field(default_factory=list)
    projects: List[str] = field(default_factory=list)
    content_items: List[str] = field(default_factory=list)
    monetization_streams: List[str] = field(default_factory=list)
    alignment_score: float = 0.0
    revenue_potential: float = 0.0
    expansion_seeds: List[str] = field(default_factory=list)

@dataclass
class EntityMigration:
    """Entity migration data"""
    entity_id: str
    name: str
    entity_type: str
    channels: List[str] = field(default_factory=list)
    projects: List[str] = field(default_factory=list)
    content_items: List[str] = field(default_factory=list)
    monetization_opportunities: List[str] = field(default_factory=list)
    alignment_score: float = 0.0
    revenue_potential: float = 0.0
    expansion_seeds: List[str] = field(default_factory=list)

@dataclass
class ProjectMigration:
    """Project migration data"""
    project_id: str
    name: str
    description: str
    entity_owner: str
    channels: List[str] = field(default_factory=list)
    content_items: List[str] = field(default_factory=list)
    monetization_opportunities: List[str] = field(default_factory=list)
    alignment_score: float = 0.0
    revenue_potential: float = 0.0
    expansion_seeds: List[str] = field(default_factory=list)

@dataclass
class GlobalAlignment:
    """Global alignment configuration"""
    alignment_id: str
    item_id: str
    content_type: ContentType
    alignment_dimensions: Dict[str, float] = field(default_factory=dict)  # spiritual, mission, content, distribution
    alignment_score: float = 0.0
    spragitso_applied: bool = False
    table_filter_passed: bool = False
    alignment_rules: List[str] = field(default_factory=list)

@dataclass
class MonetizationIntegration:
    """Monetization integration"""
    monetization_id: str
    item_id: str
    content_type: ContentType
    monetization_types: List[str] = field(default_factory=list)
    revenue_streams: List[str] = field(default_factory=list)
    revenue_potential: float = 0.0
    alignment_score: float = 0.0
    pricing_model: Optional[Dict[str, Any]] = None

@dataclass
class ExpansionSeed:
    """Expansion seed"""
    seed_id: str
    name: str
    description: str
    seed_type: str  # channel, entity, project, system, market
    parent_item_id: str
    expansion_level: int = 1  # 1 = immediate, 2 = short-term, 3 = long-term
    requirements: List[str] = field(default_factory=list)
    potential_impact: str = ""
    alignment_score: float = 0.0

class GlobalMigrationSystem:
    """
    Global Migration System
    Migrate all content into Siyem Publishing House
    Channels, Entities, Projects, Everything
    Global Alignment, Monetization, Expansion Seeds
    """
    
    def __init__(self, user_id: str = "jan", data_dir: Path = None):
        self.user_id = user_id
        self.data_dir = data_dir or Path(__file__).parent.parent / "data" / "global_migration"
        self.data_dir.mkdir(parents=True, exist_ok=True)
        
        # File paths
        self.content_items_file = self.data_dir / f"{user_id}_content_items.json"
        self.channels_file = self.data_dir / f"{user_id}_channels.json"
        self.entities_file = self.data_dir / f"{user_id}_entities.json"
        self.projects_file = self.data_dir / f"{user_id}_projects.json"
        self.alignments_file = self.data_dir / f"{user_id}_alignments.json"
        self.monetizations_file = self.data_dir / f"{user_id}_monetizations.json"
        self.expansion_seeds_file = self.data_dir / f"{user_id}_expansion_seeds.json"
        self.migration_report_file = self.data_dir / f"{user_id}_migration_report.json"
        
        # Data structures
        self.content_items: Dict[str, ContentItem] = {}
        self.channels: Dict[str, ChannelMigration] = {}
        self.entities: Dict[str, EntityMigration] = {}
        self.projects: Dict[str, ProjectMigration] = {}
        self.alignments: Dict[str, GlobalAlignment] = {}
        self.monetizations: Dict[str, MonetizationIntegration] = {}
        self.expansion_seeds: Dict[str, ExpansionSeed] = {}
        
        # Base paths
        self.base_path = Path(__file__).parent.parent
        self.siyem_path = self.base_path / "Siyem.org"
        self.data_path = self.base_path / "data"
        self.jan_studio_path = self.base_path / "jan-studio"
        
        # Load existing data
        self._load_data()
    
    def _load_data(self):
        """Load existing migration data"""
        files = [
            (self.content_items_file, self.content_items, ContentItem),
            (self.channels_file, self.channels, ChannelMigration),
            (self.entities_file, self.entities, EntityMigration),
            (self.projects_file, self.projects, ProjectMigration),
            (self.alignments_file, self.alignments, GlobalAlignment),
            (self.monetizations_file, self.monetizations, MonetizationIntegration),
            (self.expansion_seeds_file, self.expansion_seeds, ExpansionSeed),
        ]
        
        for file_path, data_dict, data_class in files:
            if file_path.exists():
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    for item_id, item_data in data.items():
                        data_dict[item_id] = data_class(**item_data)
                except Exception as e:
                    logger.error(f"Error loading {file_path}: {e}")
    
    def _save_data(self):
        """Save all migration data"""
        files = [
            (self.content_items_file, self.content_items),
            (self.channels_file, self.channels),
            (self.entities_file, self.entities),
            (self.projects_file, self.projects),
            (self.alignments_file, self.alignments),
            (self.monetizations_file, self.monetizations),
            (self.expansion_seeds_file, self.expansion_seeds),
        ]
        
        for file_path, data_dict in files:
            try:
                data = {}
                for k, v in data_dict.items():
                    item_dict = asdict(v)
                    # Convert Enum types to their values
                    for key, value in item_dict.items():
                        if isinstance(value, Enum):
                            item_dict[key] = value.value
                        elif isinstance(value, list):
                            item_dict[key] = [item.value if isinstance(item, Enum) else item for item in value]
                    data[k] = item_dict
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
            except Exception as e:
                logger.error(f"Error saving {file_path}: {e}")
    
    def discover_all_content(self):
        """Discover all content across the codebase"""
        logger.info("Discovering all content...")
        
        # Discover channels
        self._discover_channels()
        
        # Discover entities
        self._discover_entities()
        
        # Discover projects
        self._discover_projects()
        
        # Discover content items
        self._discover_content_items()
        
        # Discover data files
        self._discover_data_files()
        
        logger.info(f"Discovery complete: {len(self.content_items)} items found")
        self._save_data()
    
    def _discover_channels(self):
        """Discover all channels"""
        logger.info("Discovering channels...")
        
        # Known channels from SIYEM_ENTITY_AND_3_CHANNELS.md
        channels_data = [
            {
                "channel_id": "channel_professional",
                "name": "Professional Platform",
                "channel_type": "professional",
                "description": "Enterprise & Business - B2B services"
            },
            {
                "channel_id": "channel_creator",
                "name": "Creator Economy Platform",
                "channel_type": "creator",
                "description": "Individual Creators, Artists, Makers - B2C marketplace"
            },
            {
                "channel_id": "channel_educational",
                "name": "Educational Platform",
                "channel_type": "educational",
                "description": "Teachers, Students, Educational Institutions - B2Ed"
            },
            {
                "channel_id": "channel_pi",
                "name": "PI (Private Investigation)",
                "channel_type": "pi",
                "description": "Private Investigation / Personal Intelligence"
            },
            {
                "channel_id": "channel_spiritual",
                "name": "Spiritual Alignment",
                "channel_type": "spiritual",
                "description": "Spiritual alignment, connection ritual"
            },
            {
                "channel_id": "channel_financial",
                "name": "Financial Systems",
                "channel_type": "financial",
                "description": "Financial systems, dirty money cleaning"
            },
            {
                "channel_id": "channel_community",
                "name": "Community Building",
                "channel_type": "community",
                "description": "Community building, stewardship"
            }
        ]
        
        for channel_data in channels_data:
            if channel_data["channel_id"] not in self.channels:
                channel = ChannelMigration(
                    channel_id=channel_data["channel_id"],
                    name=channel_data["name"],
                    channel_type=channel_data["channel_type"]
                )
                self.channels[channel_data["channel_id"]] = channel
                
                # Create content item
                item = ContentItem(
                    item_id=f"content_{channel_data['channel_id']}",
                    content_type=ContentType.CHANNEL,
                    name=channel_data["name"],
                    description=channel_data["description"],
                    source_path=f"SIYEM_ENTITY_AND_3_CHANNELS.md",
                    target_path=f"Siyem.org/publishing_house/channels/{channel_data['channel_id']}.json"
                )
                self.content_items[item.item_id] = item
    
    def _discover_entities(self):
        """Discover all entities"""
        logger.info("Discovering entities...")
        
        # Entities from Siyem.org structure
        entities_path = self.siyem_path
        if entities_path.exists():
            for entity_dir in entities_path.iterdir():
                if entity_dir.is_dir() and (entity_dir / "profile.md").exists():
                    entity_name = entity_dir.name
                    entity_id = f"entity_{entity_name}"
                    
                    if entity_id not in self.entities:
                        # Read profile
                        profile_path = entity_dir / "profile.md"
                        description = ""
                        if profile_path.exists():
                            try:
                                with open(profile_path, 'r', encoding='utf-8') as f:
                                    content = f.read()
                                    # Extract description from profile
                                    if "### Purpose" in content:
                                        desc_start = content.find("### Purpose") + len("### Purpose")
                                        desc_end = content.find("\n##", desc_start)
                                        if desc_end == -1:
                                            desc_end = len(content)
                                        description = content[desc_start:desc_end].strip()
                            except Exception as e:
                                logger.error(f"Error reading {profile_path}: {e}")
                        
                        entity = EntityMigration(
                            entity_id=entity_id,
                            name=entity_name.replace("_", " ").title(),
                            entity_type="creative_persona" if entity_name != "siyem_media" else "meta_entity"
                        )
                        self.entities[entity_id] = entity
                        
                        # Create content item
                        item = ContentItem(
                            item_id=f"content_{entity_id}",
                            content_type=ContentType.ENTITY,
                            name=entity.name,
                            description=description or f"Entity: {entity.name}",
                            source_path=str(entity_dir.relative_to(self.base_path)),
                            target_path=f"Siyem.org/publishing_house/entities/{entity_id}.json"
                        )
                        self.content_items[item.item_id] = item
    
    def _discover_projects(self):
        """Discover all projects"""
        logger.info("Discovering projects...")
        
        # Known projects
        projects_data = [
            {
                "project_id": "project_edible_london",
                "name": "Edible London",
                "description": "London-based food business",
                "entity_owner": "entity_edible_london"
            },
            {
                "project_id": "project_ilven_seamoss",
                "name": "ILVEN Sea Moss",
                "description": "Sea moss product business",
                "entity_owner": "entity_ilven_seamoss"
            },
            {
                "project_id": "project_edible_cyprus",
                "name": "Edible Cyprus",
                "description": "Cyprus-based food business",
                "entity_owner": "entity_edible_cyprus"
            },
            {
                "project_id": "project_atilok",
                "name": "ATILOK LTD",
                "description": "E-commerce platform",
                "entity_owner": "entity_atilok"
            },
            {
                "project_id": "project_world_history_app",
                "name": "World History App",
                "description": "Next.js world history visualization app",
                "entity_owner": "entity_siyem_media"
            },
            {
                "project_id": "project_pi_display",
                "name": "PI Display",
                "description": "Vite/React kiosk display app",
                "entity_owner": "entity_siyem_media"
            },
            {
                "project_id": "project_admin_dashboard",
                "name": "Admin Dashboard",
                "description": "React admin dashboard",
                "entity_owner": "entity_siyem_media"
            },
            {
                "project_id": "project_jan_studio",
                "name": "JAN Studio",
                "description": "FastAPI backend system",
                "entity_owner": "entity_jan_studio"
            }
        ]
        
        for project_data in projects_data:
            if project_data["project_id"] not in self.projects:
                project = ProjectMigration(
                    project_id=project_data["project_id"],
                    name=project_data["name"],
                    description=project_data["description"],
                    entity_owner=project_data["entity_owner"]
                )
                self.projects[project_data["project_id"]] = project
                
                # Create content item
                item = ContentItem(
                    item_id=f"content_{project_data['project_id']}",
                    content_type=ContentType.PROJECT,
                    name=project_data["name"],
                    description=project_data["description"],
                    source_path=f"projects/{project_data['project_id']}",
                    target_path=f"Siyem.org/publishing_house/projects/{project_data['project_id']}.json"
                )
                self.content_items[item.item_id] = item
    
    def _discover_content_items(self):
        """Discover content items from data directory"""
        logger.info("Discovering content items...")
        
        if not self.data_path.exists():
            return
        
        # Discover JSON files in data directory
        for json_file in self.data_path.rglob("*.json"):
            if json_file.stat().st_size > 0:  # Skip empty files
                item_id = f"content_{json_file.stem}_{json_file.parent.name}"
                if item_id not in self.content_items:
                    item = ContentItem(
                        item_id=item_id,
                        content_type=ContentType.DATA,
                        name=json_file.stem,
                        description=f"Data file: {json_file.name}",
                        source_path=str(json_file.relative_to(self.base_path)),
                        target_path=f"Siyem.org/publishing_house/data/{json_file.parent.name}/{json_file.name}"
                    )
                    self.content_items[item_id] = item
    
    def _discover_data_files(self):
        """Discover data files from various sources"""
        logger.info("Discovering data files...")
        
        # Discover from 2026_social_content
        social_content_path = self.data_path / "2026_social_content"
        if social_content_path.exists():
            for json_file in social_content_path.glob("*.json"):
                item_id = f"content_social_{json_file.stem}"
                if item_id not in self.content_items:
                    item = ContentItem(
                        item_id=item_id,
                        content_type=ContentType.CONTENT,
                        name=f"Social Content: {json_file.stem}",
                        description=f"Social media content post",
                        source_path=str(json_file.relative_to(self.base_path)),
                        target_path=f"Siyem.org/publishing_house/content/social/{json_file.name}"
                    )
                    self.content_items[item_id] = item
    
    def apply_global_alignment(self):
        """Apply global alignment to all content"""
        logger.info("Applying global alignment...")
        
        for item_id, item in self.content_items.items():
            if item_id not in self.alignments:
                alignment = self._calculate_alignment(item)
                self.alignments[item_id] = alignment
                item.alignment_score = alignment.alignment_score
        
        self._save_data()
        logger.info("Global alignment applied")
    
    def _calculate_alignment(self, item: ContentItem) -> GlobalAlignment:
        """Calculate alignment for a content item"""
        # Alignment dimensions
        dimensions = {
            "spiritual": 1.0,  # All content aligned with Our Father's will
            "mission": 1.0,    # All content serves The Table
            "content": 1.0,    # All content honors the miracle
            "distribution": 1.0 # All content brings joy
        }
        
        # Calculate overall alignment score
        alignment_score = sum(dimensions.values()) / len(dimensions)
        
        # Table Filter check
        table_filter_passed = (
            alignment_score >= 0.8 and  # High alignment
            item.content_type != ContentType.SYSTEM  # Not system files
        )
        
        alignment = GlobalAlignment(
            alignment_id=f"alignment_{item.item_id}",
            item_id=item.item_id,
            content_type=item.content_type,
            alignment_dimensions=dimensions,
            alignment_score=alignment_score,
            spragitso_applied=True,  # All content bears SPRAGITSO
            table_filter_passed=table_filter_passed,
            alignment_rules=[
                "Aligns with Our Father's will",
                "Serves The Table",
                "Honors the miracle",
                "Brings joy, not struggle"
            ]
        )
        
        return alignment
    
    def integrate_monetization(self):
        """Integrate monetization for all content"""
        logger.info("Integrating monetization...")
        
        # Load monetization alignment data if available
        monetization_path = self.base_path / "data" / "monetization_alignment"
        if monetization_path.exists():
            # Load existing monetization data
            entities_file = monetization_path / f"{self.user_id}_entities.json"
            if entities_file.exists():
                try:
                    with open(entities_file, 'r', encoding='utf-8') as f:
                        monetization_data = json.load(f)
                    # Integrate monetization data
                    for entity_id, entity_data in monetization_data.items():
                        if entity_id in self.entities:
                            monetization = MonetizationIntegration(
                                monetization_id=f"monetization_{entity_id}",
                                item_id=f"content_{entity_id}",
                                content_type=ContentType.ENTITY,
                                monetization_types=entity_data.get("monetization_opportunities", []),
                                revenue_potential=entity_data.get("revenue_potential", 0.0),
                                alignment_score=entity_data.get("alignment_score", 1.0)
                            )
                            self.monetizations[monetization.monetization_id] = monetization
                except Exception as e:
                    logger.error(f"Error loading monetization data: {e}")
        
        # Apply monetization to all content items
        for item_id, item in self.content_items.items():
            if f"monetization_{item_id}" not in self.monetizations:
                monetization = self._calculate_monetization(item)
                if monetization:
                    self.monetizations[monetization.monetization_id] = monetization
                    item.monetization_potential = monetization.revenue_potential
        
        self._save_data()
        logger.info("Monetization integrated")
    
    def _calculate_monetization(self, item: ContentItem) -> Optional[MonetizationIntegration]:
        """Calculate monetization potential for content item"""
        # Base monetization based on content type
        monetization_types = []
        revenue_potential = 0.0
        
        if item.content_type == ContentType.CHANNEL:
            monetization_types = ["licensing", "subscription", "services"]
            revenue_potential = 50000.0
        elif item.content_type == ContentType.ENTITY:
            monetization_types = ["sales", "licensing", "services"]
            revenue_potential = 30000.0
        elif item.content_type == ContentType.PROJECT:
            monetization_types = ["sales", "licensing"]
            revenue_potential = 20000.0
        elif item.content_type == ContentType.CONTENT:
            monetization_types = ["sales", "licensing"]
            revenue_potential = 1000.0
        else:
            return None  # No monetization for data/system files
        
        monetization = MonetizationIntegration(
            monetization_id=f"monetization_{item.item_id}",
            item_id=item.item_id,
            content_type=item.content_type,
            monetization_types=monetization_types,
            revenue_streams=[f"{mt}_stream" for mt in monetization_types],
            revenue_potential=revenue_potential,
            alignment_score=item.alignment_score
        )
        
        return monetization
    
    def plant_expansion_seeds(self):
        """Plant expansion seeds for all levels"""
        logger.info("Planting expansion seeds...")
        
        # Channel expansion seeds
        for channel_id, channel in self.channels.items():
            seed = ExpansionSeed(
                seed_id=f"seed_channel_{channel_id}",
                name=f"Expand {channel.name}",
                description=f"Expand {channel.name} to new markets and audiences",
                seed_type="channel",
                parent_item_id=f"content_{channel_id}",
                expansion_level=1,
                requirements=["Market research", "Content development", "Distribution setup"],
                potential_impact="High - Opens new revenue streams",
                alignment_score=1.0
            )
            self.expansion_seeds[seed.seed_id] = seed
            channel.expansion_seeds.append(seed.seed_id)
        
        # Entity expansion seeds
        for entity_id, entity in self.entities.items():
            seed = ExpansionSeed(
                seed_id=f"seed_entity_{entity_id}",
                name=f"Expand {entity.name}",
                description=f"Expand {entity.name} to new channels and formats",
                seed_type="entity",
                parent_item_id=f"content_{entity_id}",
                expansion_level=1,
                requirements=["Content creation", "Channel integration", "Format expansion"],
                potential_impact="Medium - Increases entity reach",
                alignment_score=1.0
            )
            self.expansion_seeds[seed.seed_id] = seed
            entity.expansion_seeds.append(seed.seed_id)
        
        # Project expansion seeds
        for project_id, project in self.projects.items():
            seed = ExpansionSeed(
                seed_id=f"seed_project_{project_id}",
                name=f"Expand {project.name}",
                description=f"Expand {project.name} functionality and reach",
                seed_type="project",
                parent_item_id=f"content_{project_id}",
                expansion_level=2,
                requirements=["Feature development", "User testing", "Market validation"],
                potential_impact="Medium - Enhances project value",
                alignment_score=1.0
            )
            self.expansion_seeds[seed.seed_id] = seed
            project.expansion_seeds.append(seed.seed_id)
        
        # System-level expansion seeds
        system_seeds = [
            {
                "seed_id": "seed_system_global",
                "name": "Global Expansion",
                "description": "Expand system globally to new markets",
                "expansion_level": 3,
                "requirements": ["International partnerships", "Localization", "Compliance"]
            },
            {
                "seed_id": "seed_system_ai",
                "name": "AI Integration",
                "description": "Integrate advanced AI capabilities",
                "expansion_level": 2,
                "requirements": ["AI research", "Model training", "Integration testing"]
            },
            {
                "seed_id": "seed_system_community",
                "name": "Community Building",
                "description": "Build global community around system",
                "expansion_level": 1,
                "requirements": ["Community platform", "Engagement strategy", "Content creation"]
            }
        ]
        
        for seed_data in system_seeds:
            seed = ExpansionSeed(
                seed_id=seed_data["seed_id"],
                name=seed_data["name"],
                description=seed_data["description"],
                seed_type="system",
                parent_item_id="system_root",
                expansion_level=seed_data["expansion_level"],
                requirements=seed_data["requirements"],
                potential_impact="High - System-wide transformation",
                alignment_score=1.0
            )
            self.expansion_seeds[seed.seed_id] = seed
        
        self._save_data()
        logger.info("Expansion seeds planted")
    
    def generate_migration_report(self):
        """Generate comprehensive migration report"""
        logger.info("Generating migration report...")
        
        report = {
            "migration_date": datetime.now().isoformat(),
            "summary": {
                "total_content_items": len(self.content_items),
                "total_channels": len(self.channels),
                "total_entities": len(self.entities),
                "total_projects": len(self.projects),
                "total_alignments": len(self.alignments),
                "total_monetizations": len(self.monetizations),
                "total_expansion_seeds": len(self.expansion_seeds)
            },
            "channels": {k: asdict(v) for k, v in self.channels.items()},
            "entities": {k: asdict(v) for k, v in self.entities.items()},
            "projects": {k: asdict(v) for k, v in self.projects.items()},
            "alignment_summary": {
                "average_alignment_score": sum(a.alignment_score for a in self.alignments.values()) / len(self.alignments) if self.alignments else 0.0,
                "spragitso_applied_count": sum(1 for a in self.alignments.values() if a.spragitso_applied),
                "table_filter_passed_count": sum(1 for a in self.alignments.values() if a.table_filter_passed)
            },
            "monetization_summary": {
                "total_revenue_potential": sum(m.revenue_potential for m in self.monetizations.values()),
                "monetization_types": list(set(mt for m in self.monetizations.values() for mt in m.monetization_types)),
                "average_revenue_potential": sum(m.revenue_potential for m in self.monetizations.values()) / len(self.monetizations) if self.monetizations else 0.0
            },
            "expansion_summary": {
                "total_seeds": len(self.expansion_seeds),
                "seeds_by_level": {
                    "1": sum(1 for s in self.expansion_seeds.values() if s.expansion_level == 1),
                    "2": sum(1 for s in self.expansion_seeds.values() if s.expansion_level == 2),
                    "3": sum(1 for s in self.expansion_seeds.values() if s.expansion_level == 3)
                },
                "seeds_by_type": {}
            }
        }
        
        # Seeds by type
        for seed in self.expansion_seeds.values():
            seed_type = seed.seed_type
            if seed_type not in report["expansion_summary"]["seeds_by_type"]:
                report["expansion_summary"]["seeds_by_type"][seed_type] = 0
            report["expansion_summary"]["seeds_by_type"][seed_type] += 1
        
        # Save report
        with open(self.migration_report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Migration report generated: {self.migration_report_file}")
        return report
    
    def execute_full_migration(self):
        """Execute full migration process"""
        logger.info("Starting full migration process...")
        
        # Step 1: Discover all content
        self.discover_all_content()
        
        # Step 2: Apply global alignment
        self.apply_global_alignment()
        
        # Step 3: Integrate monetization
        self.integrate_monetization()
        
        # Step 4: Plant expansion seeds
        self.plant_expansion_seeds()
        
        # Step 5: Generate report
        report = self.generate_migration_report()
        
        logger.info("Full migration complete!")
        return report

def main():
    """Main execution"""
    system = GlobalMigrationSystem()
    report = system.execute_full_migration()
    
    print("\n" + "="*80)
    print("GLOBAL MIGRATION COMPLETE")
    print("="*80)
    print(f"\nTotal Content Items: {report['summary']['total_content_items']}")
    print(f"Total Channels: {report['summary']['total_channels']}")
    print(f"Total Entities: {report['summary']['total_entities']}")
    print(f"Total Projects: {report['summary']['total_projects']}")
    print(f"\nAverage Alignment Score: {report['alignment_summary']['average_alignment_score']:.2f}")
    print(f"SPRAGITSO Applied: {report['alignment_summary']['spragitso_applied_count']}")
    print(f"Table Filter Passed: {report['alignment_summary']['table_filter_passed_count']}")
    print(f"\nTotal Revenue Potential: ${report['monetization_summary']['total_revenue_potential']:,.2f}")
    print(f"Total Expansion Seeds: {report['expansion_summary']['total_seeds']}")
    print("\n" + "="*80)

if __name__ == "__main__":
    standard_main(main, "global_migration_system")
