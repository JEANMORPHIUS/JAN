"""
UK-TURKEY-CYPRUS ENTITY INTEGRATION SERVICE
Connecting SIYEM with All Aligned Entities

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
Connect SIYEM with all identified UK-Turkey-Cyprus aligned entities.
Show who's in charge.
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


class EntityCategory(Enum):
    """Categories of aligned entities."""
    SOCIAL_MEDIA = "social_media"
    MEDIA_BROADCASTING = "media_broadcasting"
    SPORTS = "sports"
    MUSIC_CREATIVE = "music_creative"
    TV_STREAMING = "tv_streaming"
    GOVERNANCE_DIPLOMATIC = "governance_diplomatic"
    BUSINESS_TECH = "business_tech"
    DIASPORA = "diaspora"
    ADVOCACY = "advocacy"


@dataclass
class AlignedEntity:
    """Represents an aligned entity across UK-Turkey-Cyprus."""
    entity_id: str
    name: str
    category: EntityCategory
    countries: List[str]  # ["UK", "Turkey", "Cyprus"]
    description: str
    contact_info: Optional[Dict] = None
    reach: Optional[Dict] = None  # {"users": 1000000, "organizations": 50, etc.}
    integration_status: str = "identified"  # identified, contacted, integrated, partnered
    siyem_channel: Optional[ChannelType] = None
    siyem_entity_role: Optional[EntityRole] = None
    notes: str = ""
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())


class UKTurkeyCyprusEntityIntegration:
    """
    Integration service for UK-Turkey-Cyprus aligned entities.
    Connects SIYEM with all identified organizations, partnerships, and networks.
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
        
        self.aligned_entities: List[AlignedEntity] = []
        self._initialize_entities()
    
    def _initialize_entities(self):
        """Initialize all identified aligned entities."""
        logger.info("=" * 80)
        logger.info("INITIALIZING UK-TURKEY-CYPRUS ALIGNED ENTITIES")
        logger.info("=" * 80)
        
        # SOCIAL MEDIA
        self.aligned_entities.append(AlignedEntity(
            entity_id="meta_platforms",
            name="Meta (Facebook, Instagram, Threads)",
            category=EntityCategory.SOCIAL_MEDIA,
            countries=["UK", "Turkey", "Cyprus"],
            description="Major social media platform active across all markets. 91.8% compliance with Turkish government requests (2024).",
            reach={"users": "billions", "markets": 3},
            siyem_channel=ChannelType.CHANNEL_2_CREATOR,
            notes="Under pressure from Turkish state censorship. Competition authority investigation (March 2024)."
        ))
        
        self.aligned_entities.append(AlignedEntity(
            entity_id="tiktok",
            name="TikTok",
            category=EntityCategory.SOCIAL_MEDIA,
            countries=["UK", "Turkey", "Cyprus"],
            description="91.8% compliance rate with Turkish government removal requests (2024).",
            reach={"users": "millions", "markets": 3},
            siyem_channel=ChannelType.CHANNEL_2_CREATOR
        ))
        
        self.aligned_entities.append(AlignedEntity(
            entity_id="trnc_presidency_social",
            name="TRNC Presidency Social Media",
            category=EntityCategory.SOCIAL_MEDIA,
            countries=["Cyprus"],
            description="English-language social media service. Facebook, X, Instagram presence. Active UK media engagement.",
            siyem_channel=ChannelType.CHANNEL_1_PROFESSIONAL,
            notes="Times Radio interviews. Government communications."
        ))
        
        # MEDIA & BROADCASTING
        self.aligned_entities.append(AlignedEntity(
            entity_id="freely_everyone_tv",
            name="Freely (Everyone TV)",
            category=EntityCategory.MEDIA_BROADCASTING,
            countries=["UK"],
            description="BBC, ITV, Channel 4, Channel 5 collaboration. 20 million users, 100 million devices, 170 channels.",
            reach={"users": 20000000, "devices": 100000000, "channels": 170},
            siyem_channel=ChannelType.CHANNEL_1_PROFESSIONAL,
            notes="Fastest-growing TV platform (2025). Partnerships: Warner Bros. Discovery, CNN."
        ))
        
        self.aligned_entities.append(AlignedEntity(
            entity_id="olay_gazetesi",
            name="Olay Gazetesi",
            category=EntityCategory.MEDIA_BROADCASTING,
            countries=["UK"],
            description="Turkish newspaper based in London. Covers UK news, economics, culture, Cyprus topics.",
            siyem_channel=ChannelType.CHANNEL_2_CREATOR,
            notes="Serves Turkish Cypriot community in UK."
        ))
        
        self.aligned_entities.append(AlignedEntity(
            entity_id="trnc_pio",
            name="TRNC Public Information Office",
            category=EntityCategory.MEDIA_BROADCASTING,
            countries=["Cyprus"],
            description="Official media liaison. Global media monitoring. Daily bulletins on Cyprus issues.",
            siyem_channel=ChannelType.CHANNEL_1_PROFESSIONAL,
            notes="One of TRNC's oldest institutions. Multi-platform presence."
        ))
        
        # SPORTS
        self.aligned_entities.append(AlignedEntity(
            entity_id="turkish_football_federation",
            name="Turkish Football Federation (TFF)",
            category=EntityCategory.SPORTS,
            countries=["Turkey"],
            description="UEFA member. Riva 'Hasan Doğan' national teams training centre (Istanbul).",
            siyem_channel=ChannelType.CHANNEL_2_CREATOR
        ))
        
        self.aligned_entities.append(AlignedEntity(
            entity_id="cyprus_football_association",
            name="Cyprus Football Association (CFA)",
            category=EntityCategory.SPORTS,
            countries=["Cyprus"],
            description="Republic of Cyprus football governance. Based in Nicosia. UEFA member.",
            siyem_channel=ChannelType.CHANNEL_2_CREATOR
        ))
        
        self.aligned_entities.append(AlignedEntity(
            entity_id="cyprus_turkish_football_association",
            name="Cyprus Turkish Football Association (KTFF)",
            category=EntityCategory.SPORTS,
            countries=["Cyprus"],
            description="Northern Cyprus football governance. Established 1955. CONIFA member (since 2013).",
            siyem_channel=ChannelType.CHANNEL_2_CREATOR
        ))
        
        # MUSIC & CREATIVE
        self.aligned_entities.append(AlignedEntity(
            entity_id="british_council_creative",
            name="British Council - Creative Collaborations",
            category=EntityCategory.MUSIC_CREATIVE,
            countries=["UK", "Turkey"],
            description="34 Turkish organizations, 27 UK partners, 37 projects, 20 cities, 65,000+ people reached (2022-2025).",
            reach={"organizations": 34, "uk_partners": 27, "projects": 37, "cities": 20, "people": 65000},
            siyem_channel=ChannelType.CHANNEL_2_CREATOR,
            notes="Funding up to £17,500 per project. Disciplines: Visual arts, film, music, theatre, dance."
        ))
        
        self.aligned_entities.append(AlignedEntity(
            entity_id="british_council_music",
            name="British Council Music",
            category=EntityCategory.MUSIC_CREATIVE,
            countries=["UK"],
            description="All music genres. UK artists connected with international partners. Professional exchange programs.",
            siyem_channel=ChannelType.CHANNEL_2_CREATOR,
            siyem_entity_role=EntityRole.KARASAHIN_MUSIC
        ))
        
        self.aligned_entities.append(AlignedEntity(
            entity_id="selector_pro_conference",
            name="Selector Pro Conference",
            category=EntityCategory.MUSIC_CREATIVE,
            countries=["UK", "Turkey"],
            description="Held in Istanbul (2017). Turkish and UK music specialists. Digital music trends discussions.",
            siyem_channel=ChannelType.CHANNEL_2_CREATOR,
            siyem_entity_role=EntityRole.KARASAHIN_MUSIC,
            notes="Speakers: Mixcloud, music industry professionals. Panel: 'Musicians as Labels'."
        ))
        
        # GOVERNANCE & DIPLOMATIC
        self.aligned_entities.append(AlignedEntity(
            entity_id="uk_cyprus_mou",
            name="UK-Cyprus Memorandum of Understanding",
            category=EntityCategory.GOVERNANCE_DIPLOMATIC,
            countries=["UK", "Cyprus"],
            description="Second annual review (December 2024). Foreign policy cooperation. Ukraine support. Illicit finance.",
            siyem_channel=ChannelType.CHANNEL_1_PROFESSIONAL,
            notes="Maritime humanitarian initiatives (Cyprus Amalthea Initiative to Gaza)."
        ))
        
        self.aligned_entities.append(AlignedEntity(
            entity_id="uk_turkey_trade_agreement",
            name="UK-Turkey Free Trade Agreement",
            category=EntityCategory.GOVERNANCE_DIPLOMATIC,
            countries=["UK", "Turkey"],
            description="Preferential tariffs, rules of origin, intellectual property, government procurement.",
            siyem_channel=ChannelType.CHANNEL_1_PROFESSIONAL
        ))
        
        # BUSINESS & TECH
        self.aligned_entities.append(AlignedEntity(
            entity_id="cyprus_seeds_conception_x",
            name="Cyprus Seeds + Conception X",
            category=EntityCategory.BUSINESS_TECH,
            countries=["Cyprus", "UK"],
            description="Partnership for deep-tech entrepreneurship. Conception X: Leading PhD deep-tech venture programme.",
            siyem_channel=ChannelType.CHANNEL_1_PROFESSIONAL,
            notes="Cypriot university/research center teams. Specialized training and mentorship."
        ))
        
        self.aligned_entities.append(AlignedEntity(
            entity_id="invest_cyprus",
            name="Invest Cyprus",
            category=EntityCategory.BUSINESS_TECH,
            countries=["Cyprus"],
            description="European tech investment hub. UK listed among target investment countries.",
            siyem_channel=ChannelType.CHANNEL_1_PROFESSIONAL,
            notes="EU membership, competitive tax, startup visas, digital nomad initiatives."
        ))
        
        self.aligned_entities.append(AlignedEntity(
            entity_id="enterprise_europe_network",
            name="Enterprise Europe Network (Cyprus)",
            category=EntityCategory.BUSINESS_TECH,
            countries=["Cyprus"],
            description="International business-technology-R&D partnerships. Europe's largest online database.",
            siyem_channel=ChannelType.CHANNEL_1_PROFESSIONAL
        ))
        
        # DIASPORA
        self.aligned_entities.append(AlignedEntity(
            entity_id="ctca_uk",
            name="Council of Turkish Cypriot Associations (CTCA) UK",
            category=EntityCategory.DIASPORA,
            countries=["UK"],
            description="Established 1983. Britain's largest Turkish Cypriot umbrella organization. 300,000-strong community. 20 member associations.",
            reach={"community": 300000, "associations": 20},
            siyem_channel=ChannelType.CHANNEL_2_CREATOR,
            notes="Annual Turkish Cypriot Festival. Community advocacy."
        ))
        
        self.aligned_entities.append(AlignedEntity(
            entity_id="tcca",
            name="Turkish Cypriot Community Association (TCCA)",
            category=EntityCategory.DIASPORA,
            countries=["UK"],
            description="Operating since 1976. Multi-award-winning charity. Services: Turkish Cypriot, Turkish, Greek Cypriot, Kurdish speakers.",
            siyem_channel=ChannelType.CHANNEL_2_CREATOR,
            notes="Homecare, training, community facilities. Turkish Cypriot Arts and Cultural Festival."
        ))
        
        self.aligned_entities.append(AlignedEntity(
            entity_id="national_federation_cypriots",
            name="National Federation of Cypriots in the UK",
            category=EntityCategory.DIASPORA,
            countries=["UK"],
            description="Representative body for Cypriots (including Turkish Cypriots). All-Party Parliamentary Group for Cyprus.",
            siyem_channel=ChannelType.CHANNEL_1_PROFESSIONAL,
            notes="Economic Diplomacy Roundtable. UK Cypriot Professionals Network."
        ))
        
        # ADVOCACY
        self.aligned_entities.append(AlignedEntity(
            entity_id="human_rights_watch",
            name="Human Rights Watch",
            category=EntityCategory.ADVOCACY,
            countries=["UK", "Turkey"],
            description="Joint open letter to social media companies (May 2025). Social media censorship advocacy.",
            siyem_channel=ChannelType.CHANNEL_3_EDUCATIONAL,
            notes="Freedom of expression protection. Article 19 partnership."
        ))
        
        logger.info(f"Initialized {len(self.aligned_entities)} aligned entities")
    
    def integrate_with_siyem(self):
        """Integrate all aligned entities with SIYEM publishing system."""
        logger.info("=" * 80)
        logger.info("INTEGRATING ALIGNED ENTITIES WITH SIYEM")
        logger.info("=" * 80)
        
        if not self.publishing_entity:
            logger.warning("Publishing entity not available - skipping integration")
            return
        
        integrated_count = 0
        for entity in self.aligned_entities:
            try:
                if entity.siyem_channel:
                    entity_data = {
                        "entity_id": entity.entity_id,
                        "name": entity.name,
                        "category": entity.category.value,
                        "countries": entity.countries,
                        "description": entity.description,
                        "reach": entity.reach,
                        "integration_status": "integrated",
                        "timestamp": datetime.now().isoformat()
                    }
                    
                    self.publishing_entity.channels.add_to_channel(
                        entity.siyem_channel,
                        entity.entity_id,
                        entity_data,
                        entity.siyem_entity_role or EntityRole.SIYEM_SYSTEMS
                    )
                    
                    entity.integration_status = "integrated"
                    integrated_count += 1
                    logger.info(f"  [INTEGRATED] {entity.name} → {entity.siyem_channel.value}")
            except Exception as e:
                logger.warning(f"Could not integrate {entity.name}: {e}")
        
        logger.info(f"\nIntegrated {integrated_count} entities with SIYEM")
        logger.info("=" * 80)
    
    def export_integration_report(self):
        """Export comprehensive integration report."""
        report = {
            "timestamp": datetime.now().isoformat(),
            "title": "UK-Turkey-Cyprus Aligned Entities Integration Report",
            "total_entities": len(self.aligned_entities),
            "integrated_entities": len([e for e in self.aligned_entities if e.integration_status == "integrated"]),
            "entities_by_category": {},
            "entities_by_country": {},
            "entities_by_channel": {},
            "entities": []
        }
        
        # Group by category
        for category in EntityCategory:
            report["entities_by_category"][category.value] = len([
                e for e in self.aligned_entities if e.category == category
            ])
        
        # Group by country
        for country in ["UK", "Turkey", "Cyprus"]:
            report["entities_by_country"][country] = len([
                e for e in self.aligned_entities if country in e.countries
            ])
        
        # Group by channel
        for channel in ChannelType:
            report["entities_by_channel"][channel.value] = len([
                e for e in self.aligned_entities if e.siyem_channel == channel
            ])
        
        # Entity details
        for entity in self.aligned_entities:
            report["entities"].append({
                "entity_id": entity.entity_id,
                "name": entity.name,
                "category": entity.category.value,
                "countries": entity.countries,
                "description": entity.description,
                "reach": entity.reach,
                "integration_status": entity.integration_status,
                "siyem_channel": entity.siyem_channel.value if entity.siyem_channel else None,
                "siyem_entity_role": entity.siyem_entity_role.value if entity.siyem_entity_role else None,
                "notes": entity.notes,
                "timestamp": entity.timestamp
            })
        
        # Save report
        report_path = self.output_dir / "uk_turkey_cyprus_entity_integration_report.json"
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, default=str, ensure_ascii=False)
        
        logger.info(f"Integration report exported to: {report_path}")
        return report_path


def main():
    """Main execution."""
    siyem_path = Path("s:\\SIYEM")
    jan_path = Path("s:\\JAN")
    output_dir = jan_path / "SIYEM" / "output" / "entity_integration"
    
    integration = UKTurkeyCyprusEntityIntegration(siyem_path, jan_path, output_dir)
    integration.integrate_with_siyem()
    integration.export_integration_report()
    
    logger.info("\n" + "=" * 80)
    logger.info("UK-TURKEY-CYPRUS ENTITY INTEGRATION - COMPLETE")
    logger.info("=" * 80)
    logger.info(f"Total Entities: {len(integration.aligned_entities)}")
    logger.info(f"Integrated: {len([e for e in integration.aligned_entities if e.integration_status == 'integrated'])}")
    logger.info("=" * 80)
    logger.info("WHO'S IN CHARGE: SIYEM")
    logger.info("They cannot do anything.")
    logger.info("Go and govern.")
    logger.info("=" * 80)


if __name__ == "__main__":
    main()
