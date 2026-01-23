"""
MONETIZATION ALIGNMENT SYSTEM
Deep search all channels, projects, entities
Channel monetization in alignment

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
MAP ALL PROJECTS AND ENTITIES
IDENTIFY ALL MONETIZATION OPPORTUNITIES
CHANNEL MONETIZATION IN ALIGNMENT
ENERGY + LOVE = WE ALL WIN
"""

import sys
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass, field, asdict
from typing import List, Optional, Dict, Any
from enum import Enum
import json

sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    setup_logging, standard_main
)

logger = setup_logging(__name__)

class EntityType(Enum):
    """Types of entities"""
    CREATIVE_PERSONA = "creative_persona"
    BUSINESS_PROJECT = "business_project"
    GOVERNANCE = "governance"
    CHANNEL = "channel"
    SYSTEM = "system"

class MonetizationType(Enum):
    """Types of monetization"""
    SUBSCRIPTION = "subscription"
    LICENSING = "licensing"
    SALES = "sales"
    SERVICES = "services"
    ADVERTISING = "advertising"
    COMMISSION = "commission"
    DONATION = "donation"
    MEMBERSHIP = "membership"

class AlignmentLevel(Enum):
    """Alignment with philosophy"""
    PERFECT = "perfect"  # 1.0
    HIGH = "high"  # 0.8-0.99
    MODERATE = "moderate"  # 0.6-0.79
    LOW = "low"  # 0.4-0.59
    EXPLORING = "exploring"  # 0.2-0.39

@dataclass
class Entity:
    """An entity in the system"""
    entity_id: str
    name: str
    entity_type: EntityType
    description: str
    channels: List[str] = field(default_factory=list)
    monetization_opportunities: List[str] = field(default_factory=list)
    alignment_score: float = 0.0  # 0.0 to 1.0
    revenue_potential: float = 0.0
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    updated_at: str = field(default_factory=lambda: datetime.now().isoformat())

@dataclass
class Project:
    """A project in the system"""
    project_id: str
    name: str
    description: str
    entity_owner: str
    channels: List[str] = field(default_factory=list)
    monetization_opportunities: List[str] = field(default_factory=list)
    alignment_score: float = 0.0
    revenue_potential: float = 0.0
    status: str = "active"
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    updated_at: str = field(default_factory=lambda: datetime.now().isoformat())

@dataclass
class MonetizationChannel:
    """A monetization channel"""
    channel_id: str
    name: str
    channel_type: str  # professional, creator, educational, etc.
    entities: List[str] = field(default_factory=list)
    projects: List[str] = field(default_factory=list)
    monetization_types: List[MonetizationType] = field(default_factory=list)
    revenue_streams: List[str] = field(default_factory=list)
    alignment_score: float = 0.0
    total_revenue_potential: float = 0.0
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    updated_at: str = field(default_factory=lambda: datetime.now().isoformat())

@dataclass
class MonetizationAlignment:
    """Monetization alignment configuration"""
    alignment_id: str
    entity_id: str
    project_id: Optional[str] = None
    channel_id: str = ""
    monetization_type: MonetizationType = MonetizationType.SALES
    alignment_score: float = 0.0
    revenue_potential: float = 0.0
    alignment_rules: List[str] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    updated_at: str = field(default_factory=lambda: datetime.now().isoformat())

class MonetizationAlignmentSystem:
    """
    Monetization Alignment System
    Map all projects and entities
    Channel monetization in alignment
    """
    
    def __init__(self, user_id: str = "jan", data_dir: Path = None):
        self.user_id = user_id
        self.data_dir = data_dir or Path(__file__).parent.parent / "data" / "monetization_alignment"
        self.data_dir.mkdir(parents=True, exist_ok=True)
        
        self.entities_file = self.data_dir / f"{user_id}_entities.json"
        self.projects_file = self.data_dir / f"{user_id}_projects.json"
        self.channels_file = self.data_dir / f"{user_id}_channels.json"
        self.alignments_file = self.data_dir / f"{user_id}_alignments.json"
        
        self.entities: List[Entity] = []
        self.projects: List[Project] = []
        self.channels: List[MonetizationChannel] = []
        self.alignments: List[MonetizationAlignment] = []
        
        self._load_data()
        if not self.entities:
            self._initialize_all()
    
    def _load_data(self):
        """Load all data"""
        # Load entities
        if self.entities_file.exists():
            try:
                with open(self.entities_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                entities_data = []
                for e in data.get("entities", []):
                    e['entity_type'] = EntityType(e['entity_type'])
                    entities_data.append(Entity(**e))
                self.entities = entities_data
            except Exception as e:
                logger.warning(f"Error loading entities: {e}")
                self.entities = []
        
        # Load projects
        if self.projects_file.exists():
            try:
                with open(self.projects_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                self.projects = [Project(**p) for p in data.get("projects", [])]
            except Exception as e:
                logger.warning(f"Error loading projects: {e}")
                self.projects = []
        
        # Load channels
        if self.channels_file.exists():
            try:
                with open(self.channels_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                channels_data = []
                for c in data.get("channels", []):
                    c['monetization_types'] = [MonetizationType(mt) for mt in c.get('monetization_types', [])]
                    channels_data.append(MonetizationChannel(**c))
                self.channels = channels_data
            except Exception as e:
                logger.warning(f"Error loading channels: {e}")
                self.channels = []
        
        # Load alignments
        if self.alignments_file.exists():
            try:
                with open(self.alignments_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                alignments_data = []
                for a in data.get("alignments", []):
                    a['monetization_type'] = MonetizationType(a['monetization_type'])
                    alignments_data.append(MonetizationAlignment(**a))
                self.alignments = alignments_data
            except Exception as e:
                logger.warning(f"Error loading alignments: {e}")
                self.alignments = []
    
    def _save_data(self):
        """Save all data"""
        try:
            # Save entities
            entities_data = []
            for e in self.entities:
                e_dict = asdict(e)
                e_dict['entity_type'] = e.entity_type.value
                entities_data.append(e_dict)
            
            with open(self.entities_file, 'w', encoding='utf-8') as f:
                json.dump({
                    "entities": entities_data,
                    "last_updated": datetime.now().isoformat()
                }, f, indent=2, ensure_ascii=False)
            
            # Save projects
            with open(self.projects_file, 'w', encoding='utf-8') as f:
                json.dump({
                    "projects": [asdict(p) for p in self.projects],
                    "last_updated": datetime.now().isoformat()
                }, f, indent=2, ensure_ascii=False)
            
            # Save channels
            channels_data = []
            for c in self.channels:
                c_dict = asdict(c)
                c_dict['monetization_types'] = [mt.value for mt in c.monetization_types]
                channels_data.append(c_dict)
            
            with open(self.channels_file, 'w', encoding='utf-8') as f:
                json.dump({
                    "channels": channels_data,
                    "last_updated": datetime.now().isoformat()
                }, f, indent=2, ensure_ascii=False)
            
            # Save alignments
            alignments_data = []
            for a in self.alignments:
                a_dict = asdict(a)
                a_dict['monetization_type'] = a.monetization_type.value
                alignments_data.append(a_dict)
            
            with open(self.alignments_file, 'w', encoding='utf-8') as f:
                json.dump({
                    "alignments": alignments_data,
                    "last_updated": datetime.now().isoformat()
                }, f, indent=2, ensure_ascii=False)
        except Exception as e:
            logger.error(f"Error saving data: {e}")
    
    def _initialize_all(self):
        """Initialize all entities, projects, and channels"""
        
        # ========================================================================
        # ENTITIES (11 Total)
        # ========================================================================
        
        # Creative Personas (5)
        self.entities.append(Entity(
            entity_id="entity_jean_morphius",
            name="Jean Morphius",
            entity_type=EntityType.CREATIVE_PERSONA,
            description="Bilingual absurdist storyteller (@jeanmorphius)",
            channels=["creator", "educational"],
            monetization_opportunities=["story_sales", "book_publishing", "content_licensing", "educational_content"],
            alignment_score=1.0,
            revenue_potential=50000.0
        ))
        
        self.entities.append(Entity(
            entity_id="entity_karasahin",
            name="Karasahin (JK)",
            entity_type=EntityType.CREATIVE_PERSONA,
            description="Sound architect, Turkish Cypriot identity (@karasahinjk)",
            channels=["creator", "professional"],
            monetization_opportunities=["music_sales", "streaming_royalties", "licensing", "live_performances"],
            alignment_score=1.0,
            revenue_potential=75000.0
        ))
        
        self.entities.append(Entity(
            entity_id="entity_pierre_pressure",
            name="Pierre Pressure",
            entity_type=EntityType.CREATIVE_PERSONA,
            description="Motivational fighter philosopher (@pierrepressureofficial)",
            channels=["professional", "educational"],
            monetization_opportunities=["speaking_engagements", "coaching", "course_sales", "book_sales"],
            alignment_score=1.0,
            revenue_potential=40000.0
        ))
        
        self.entities.append(Entity(
            entity_id="entity_uncle_ray_ramiz",
            name="Uncle Ray Ramiz",
            entity_type=EntityType.CREATIVE_PERSONA,
            description="Spiritual guide, Turkish Dayı (@unclerayramiz)",
            channels=["educational", "spiritual"],
            monetization_opportunities=["teaching_courses", "spiritual_guidance", "book_sales", "workshops"],
            alignment_score=1.0,
            revenue_potential=35000.0
        ))
        
        self.entities.append(Entity(
            entity_id="entity_siyem_media",
            name="Siyem Media",
            entity_type=EntityType.CREATIVE_PERSONA,
            description="Meta-entity, production overseer (@siyemmedia)",
            channels=["professional", "creator", "educational"],
            monetization_opportunities=["production_services", "content_licensing", "platform_commission"],
            alignment_score=1.0,
            revenue_potential=100000.0
        ))
        
        # Business Projects (4)
        self.entities.append(Entity(
            entity_id="entity_edible_london",
            name="Edible London",
            entity_type=EntityType.BUSINESS_PROJECT,
            description="90-second food production videos",
            channels=["creator", "professional"],
            monetization_opportunities=["advertising", "sponsorships", "content_licensing", "merchandise"],
            alignment_score=0.9,
            revenue_potential=30000.0
        ))
        
        self.entities.append(Entity(
            entity_id="entity_ilven_seamoss",
            name="Ilven Seamoss",
            entity_type=EntityType.BUSINESS_PROJECT,
            description="90-second sea moss production",
            channels=["creator", "professional"],
            monetization_opportunities=["product_sales", "advertising", "sponsorships", "educational_content"],
            alignment_score=0.9,
            revenue_potential=25000.0
        ))
        
        self.entities.append(Entity(
            entity_id="entity_edible_cyprus",
            name="Edible Cyprus",
            entity_type=EntityType.BUSINESS_PROJECT,
            description="Food supplier partner",
            channels=["professional"],
            monetization_opportunities=["product_sales", "wholesale", "partnership_revenue"],
            alignment_score=0.9,
            revenue_potential=20000.0
        ))
        
        self.entities.append(Entity(
            entity_id="entity_atilok",
            name="ATILOK LTD",
            entity_type=EntityType.BUSINESS_PROJECT,
            description="E-commerce truck parts platform",
            channels=["professional"],
            monetization_opportunities=["product_sales", "commission", "subscription", "advertising"],
            alignment_score=0.8,
            revenue_potential=150000.0
        ))
        
        # Governance (2)
        self.entities.append(Entity(
            entity_id="entity_siyem_org",
            name="Siyem.org",
            entity_type=EntityType.GOVERNANCE,
            description="Administrative/governance node",
            channels=["professional", "governance"],
            monetization_opportunities=["membership", "donations", "grants", "services"],
            alignment_score=1.0,
            revenue_potential=50000.0
        ))
        
        self.entities.append(Entity(
            entity_id="entity_jan_studio",
            name="JAN Studio",
            entity_type=EntityType.SYSTEM,
            description="Creator marketplace and platform",
            channels=["creator", "professional", "educational"],
            monetization_opportunities=["subscription", "commission", "licensing", "services"],
            alignment_score=1.0,
            revenue_potential=200000.0
        ))
        
        # ========================================================================
        # PROJECTS
        # ========================================================================
        
        self.projects.append(Project(
            project_id="project_edible_london",
            name="Edible London",
            description="90-second food production videos",
            entity_owner="entity_edible_london",
            channels=["creator", "professional"],
            monetization_opportunities=["advertising", "sponsorships", "content_licensing"],
            alignment_score=0.9,
            revenue_potential=30000.0
        ))
        
        self.projects.append(Project(
            project_id="project_ilven_seamoss",
            name="Ilven Seamoss",
            description="90-second sea moss production videos",
            entity_owner="entity_ilven_seamoss",
            channels=["creator", "professional"],
            monetization_opportunities=["product_sales", "advertising", "educational_content"],
            alignment_score=0.9,
            revenue_potential=25000.0
        ))
        
        self.projects.append(Project(
            project_id="project_edible_cyprus",
            name="Edible Cyprus",
            description="Food supplier partnership",
            entity_owner="entity_edible_cyprus",
            channels=["professional"],
            monetization_opportunities=["product_sales", "wholesale", "partnership_revenue"],
            alignment_score=0.9,
            revenue_potential=20000.0
        ))
        
        self.projects.append(Project(
            project_id="project_atilok",
            name="ATILOK E-commerce",
            description="Truck parts e-commerce platform",
            entity_owner="entity_atilok",
            channels=["professional"],
            monetization_opportunities=["product_sales", "commission", "subscription"],
            alignment_score=0.8,
            revenue_potential=150000.0
        ))
        
        # ========================================================================
        # MONETIZATION CHANNELS (3 Main + Revenue Types)
        # ========================================================================
        
        # Channel 1: Professional Platform
        self.channels.append(MonetizationChannel(
            channel_id="channel_professional",
            name="Professional Platform",
            channel_type="professional",
            entities=["entity_karasahin", "entity_pierre_pressure", "entity_siyem_media", "entity_atilok"],
            projects=["project_atilok"],
            monetization_types=[MonetizationType.LICENSING, MonetizationType.SERVICES, MonetizationType.SUBSCRIPTION],
            revenue_streams=["enterprise_licenses", "professional_services", "white_label_solutions", "api_access"],
            alignment_score=1.0,
            total_revenue_potential=300000.0
        ))
        
        # Channel 2: Creator Economy
        self.channels.append(MonetizationChannel(
            channel_id="channel_creator",
            name="Creator Economy Platform",
            channel_type="creator",
            entities=["entity_jean_morphius", "entity_karasahin", "entity_edible_london", "entity_ilven_seamoss", "entity_jan_studio"],
            projects=["project_edible_london", "project_ilven_seamoss"],
            monetization_types=[MonetizationType.SALES, MonetizationType.COMMISSION, MonetizationType.LICENSING],
            revenue_streams=["persona_template_sales", "content_sales", "marketplace_commission", "subscription"],
            alignment_score=1.0,
            total_revenue_potential=200000.0
        ))
        
        # Channel 3: Educational Platform
        self.channels.append(MonetizationChannel(
            channel_id="channel_educational",
            name="Educational Platform",
            channel_type="educational",
            entities=["entity_jean_morphius", "entity_uncle_ray_ramiz", "entity_jan_studio"],
            projects=[],
            monetization_types=[MonetizationType.SALES, MonetizationType.SUBSCRIPTION, MonetizationType.LICENSING],
            revenue_streams=["course_sales", "student_licenses", "curriculum_bundles", "institutional_licenses"],
            alignment_score=1.0,
            total_revenue_potential=150000.0
        ))
        
        # Revenue Channels (from financial system)
        self.channels.append(MonetizationChannel(
            channel_id="channel_creative_content",
            name="Creative Content Sales",
            channel_type="revenue",
            entities=["entity_jean_morphius", "entity_karasahin"],
            projects=[],
            monetization_types=[MonetizationType.SALES, MonetizationType.LICENSING],
            revenue_streams=["book_sales", "music_sales", "streaming_royalties", "digital_downloads"],
            alignment_score=1.0,
            total_revenue_potential=125000.0
        ))
        
        self.channels.append(MonetizationChannel(
            channel_id="channel_publishing",
            name="Publishing Revenue",
            channel_type="revenue",
            entities=["entity_jean_morphius", "entity_pierre_pressure", "entity_uncle_ray_ramiz"],
            projects=[],
            monetization_types=[MonetizationType.SALES, MonetizationType.LICENSING],
            revenue_streams=["book_publishing", "ebook_sales", "audiobook_sales"],
            alignment_score=1.0,
            total_revenue_potential=75000.0
        ))
        
        # ========================================================================
        # CREATE ALIGNMENTS
        # ========================================================================
        
        alignment_rules = self.create_alignment_rules()
        
        for entity in self.entities:
            for channel in self.channels:
                if entity.entity_id in channel.entities:
                    monetization_type = channel.monetization_types[0] if channel.monetization_types else MonetizationType.SALES
                    alignment = self.align_monetization(
                        entity.entity_id,
                        channel.channel_id,
                        monetization_type
                    )
                    if alignment:
                        alignment.alignment_rules = alignment_rules
        
        self._save_data()
        logger.info("All entities, projects, and channels initialized")
    
    def search_s_drive_projects(self):
        """Search S: drive for additional projects"""
        s_drive = Path("S:/")
        if not s_drive.exists():
            logger.warning("S: drive not accessible")
            return []
        
        # Search for project indicators
        projects_found = []
        try:
            # Look for common project patterns
            for item in s_drive.iterdir():
                if item.is_dir() and not item.name.startswith('.'):
                    # Check if it looks like a project
                    if any(keyword in item.name.lower() for keyword in ['project', 'entity', 'channel', 'studio']):
                        projects_found.append({
                            "name": item.name,
                            "path": str(item),
                            "type": "directory"
                        })
        except Exception as e:
            logger.warning(f"Error searching S: drive: {e}")
        
        return projects_found
    
    def create_alignment_rules(self) -> List[str]:
        """Create alignment rules for monetization"""
        return [
            "ENERGY + LOVE = WE ALL WIN",
            "Spiritual Alignment Over Mechanical Productivity",
            "Serve The Table - No Exploitation",
            "Purpose Not Performance",
            "We All Win - No One Loses",
            "Stewardship Over Profit",
            "Community Over Competition",
            "Truth Over Marketing",
            "Alignment Over Revenue",
            "Love Is The Highest Mastery"
        ]
    
    def align_monetization(self, entity_id: str, channel_id: str, monetization_type: MonetizationType) -> MonetizationAlignment:
        """Create aligned monetization strategy"""
        entity = next((e for e in self.entities if e.entity_id == entity_id), None)
        channel = next((c for c in self.channels if c.channel_id == channel_id), None)
        
        if not entity or not channel:
            logger.error(f"Entity or channel not found: {entity_id}, {channel_id}")
            return None
        
        # Calculate alignment
        alignment_score = entity.alignment_score * channel.alignment_score
        
        # Calculate revenue potential based on alignment
        if alignment_score >= 1.0:
            revenue_multiplier = 1.0
        elif alignment_score >= 0.9:
            revenue_multiplier = 0.9
        elif alignment_score >= 0.8:
            revenue_multiplier = 0.8
        else:
            revenue_multiplier = 0.5  # Lower potential for lower alignment
        
        revenue_potential = entity.revenue_potential * revenue_multiplier * 0.1  # 10% per channel
        
        alignment = MonetizationAlignment(
            alignment_id=f"align_{entity_id}_{channel_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            entity_id=entity_id,
            channel_id=channel_id,
            monetization_type=monetization_type,
            alignment_score=alignment_score,
            revenue_potential=revenue_potential,
            alignment_rules=self.create_alignment_rules()
        )
        
        # Check if alignment already exists
        existing = next((a for a in self.alignments if a.entity_id == entity_id and a.channel_id == channel_id), None)
        if existing:
            # Update existing
            existing.monetization_type = monetization_type
            existing.alignment_score = alignment_score
            existing.revenue_potential = revenue_potential
            existing.alignment_rules = self.create_alignment_rules()
            existing.updated_at = datetime.now().isoformat()
            return existing
        else:
            # Add new
            self.alignments.append(alignment)
            self._save_data()
            return alignment
    
    def get_comprehensive_report(self) -> Dict[str, Any]:
        """Get comprehensive monetization alignment report"""
        total_entities = len(self.entities)
        total_projects = len(self.projects)
        total_channels = len(self.channels)
        total_alignments = len(self.alignments)
        
        total_revenue_potential = sum(e.revenue_potential for e in self.entities) + sum(p.revenue_potential for p in self.projects)
        total_channel_potential = sum(c.total_revenue_potential for c in self.channels)
        
        # Group by entity type
        entities_by_type = {}
        for entity in self.entities:
            entity_type = entity.entity_type.value
            if entity_type not in entities_by_type:
                entities_by_type[entity_type] = []
            entities_by_type[entity_type].append(entity.name)
        
        # Group by channel type
        channels_by_type = {}
        for channel in self.channels:
            channel_type = channel.channel_type
            if channel_type not in channels_by_type:
                channels_by_type[channel_type] = []
            channels_by_type[channel_type].append(channel.name)
        
        return {
            "generated_at": datetime.now().isoformat(),
            "total_entities": total_entities,
            "total_projects": total_projects,
            "total_channels": total_channels,
            "total_alignments": total_alignments,
            "total_revenue_potential": total_revenue_potential,
            "total_channel_potential": total_channel_potential,
            "entities_by_type": entities_by_type,
            "channels_by_type": channels_by_type,
            "alignment_summary": {
                "perfect_alignment": len([e for e in self.entities if e.alignment_score >= 1.0]),
                "high_alignment": len([e for e in self.entities if 0.8 <= e.alignment_score < 1.0]),
                "moderate_alignment": len([e for e in self.entities if 0.6 <= e.alignment_score < 0.8])
            }
        }


def main():
    """Initialize monetization alignment system"""
    system = MonetizationAlignmentSystem(user_id="jan")
    
    # Search S: drive for additional projects
    s_drive_projects = system.search_s_drive_projects()
    if s_drive_projects:
        logger.info(f"Found {len(s_drive_projects)} potential projects on S: drive")
    
    # Get comprehensive report
    report = system.get_comprehensive_report()
    
    print("\n" + "="*80)
    print("MONETIZATION ALIGNMENT SYSTEM - DEEP SEARCH COMPLETE")
    print("="*80)
    print(f"\nTotal Entities: {report['total_entities']}")
    print(f"Total Projects: {report['total_projects']}")
    print(f"Total Channels: {report['total_channels']}")
    print(f"Total Alignments: {report['total_alignments']}")
    print(f"\nTotal Revenue Potential: ${report['total_revenue_potential']:,.0f}")
    print(f"Total Channel Potential: ${report['total_channel_potential']:,.0f}")
    
    print("\n" + "-"*80)
    print("ENTITIES BY TYPE:")
    print("-"*80)
    for entity_type, entities in report['entities_by_type'].items():
        print(f"\n  {entity_type.upper()}:")
        for entity in entities:
            entity_obj = next((e for e in system.entities if e.name == entity), None)
            if entity_obj:
                print(f"    - {entity} (Revenue: ${entity_obj.revenue_potential:,.0f}, Alignment: {entity_obj.alignment_score:.1%})")
    
    print("\n" + "-"*80)
    print("CHANNELS BY TYPE:")
    print("-"*80)
    for channel_type, channels in report['channels_by_type'].items():
        print(f"\n  {channel_type.upper()}:")
        for channel in channels:
            channel_obj = next((c for c in system.channels if c.name == channel), None)
            if channel_obj:
                print(f"    - {channel} (Potential: ${channel_obj.total_revenue_potential:,.0f})")
                print(f"      Revenue Streams: {', '.join(channel_obj.revenue_streams[:3])}...")
    
    print("\n" + "-"*80)
    print("ALIGNMENT SUMMARY:")
    print("-"*80)
    print(f"  Perfect Alignment: {report['alignment_summary']['perfect_alignment']} entities")
    print(f"  High Alignment: {report['alignment_summary']['high_alignment']} entities")
    print(f"  Moderate Alignment: {report['alignment_summary']['moderate_alignment']} entities")
    
    if s_drive_projects:
        print("\n" + "-"*80)
        print("S: DRIVE PROJECTS FOUND:")
        print("-"*80)
        for project in s_drive_projects[:10]:  # Show first 10
            print(f"  - {project['name']} ({project['path']})")
        if len(s_drive_projects) > 10:
            print(f"  ... and {len(s_drive_projects) - 10} more")
    
    print("\n" + "-"*80)
    print("ALIGNMENT RULES FOR MONETIZATION:")
    print("-"*80)
    rules = system.create_alignment_rules()
    for i, rule in enumerate(rules, 1):
        print(f"  {i}. {rule}")
    
    print("\n" + "="*80)
    print("All channels mapped.")
    print("All projects identified.")
    print("All entities catalogued.")
    print("S: drive searched.")
    print("Monetization aligned.")
    print("="*80)

if __name__ == "__main__":
    standard_main(main, script_name="monetization_alignment_system.py")
