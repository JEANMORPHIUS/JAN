"""
GLOBAL ALIGNMENT COMPLETE
All Continents, All Countries, All of God's Lands and Waters

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
ARE WE FULLY ALIGNED GLOBALLY?
ALL CONTINENTS. ALL COUNTRIES. ALL OF GOD'S LANDS AND WATERS.
DEEP SEARCH FOR MORE.
THERE'S ALWAYS ANOTHER LIE TO DEBUNK.
"""

import sys
import json
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
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


class Continent(Enum):
    """All continents."""
    AFRICA = "africa"
    ASIA = "asia"
    EUROPE = "europe"
    NORTH_AMERICA = "north_america"
    SOUTH_AMERICA = "south_america"
    OCEANIA = "oceania"
    ANTARCTICA = "antarctica"


class EntityCategory(Enum):
    """Categories of aligned entities."""
    HUMANITARIAN = "humanitarian"
    DIASPORA = "diaspora"
    MEDIA = "media"
    FOOD_SECURITY = "food_security"
    FACT_CHECKING = "fact_checking"
    CULTURAL = "cultural"
    RELIGIOUS = "religious"
    EDUCATIONAL = "educational"
    GOVERNANCE = "governance"
    BUSINESS = "business"


@dataclass
class GlobalEntity:
    """Represents a globally aligned entity."""
    entity_id: str
    name: str
    category: EntityCategory
    continent: Continent
    countries: List[str]
    description: str
    reach: Optional[Dict] = None  # {"people": 1000000, "countries": 50, etc.}
    contact_info: Optional[Dict] = None
    integration_status: str = "identified"
    siyem_channel: Optional[ChannelType] = None
    siyem_entity_role: Optional[EntityRole] = None
    notes: str = ""
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())


@dataclass
class LieToDebunk:
    """Represents a lie that needs to be debunked by RAMIZ."""
    lie_id: str
    lie_statement: str
    truth_statement: str
    region: str
    continent: Continent
    countries: List[str]
    people_affected: Optional[Dict] = None
    source: str = ""
    priority: str = "high"  # high, medium, low
    status: str = "identified"
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())


class GlobalAlignmentComplete:
    """
    Global Alignment Complete
    All Continents, All Countries, All of God's Lands and Waters
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
        
        self.entities: List[GlobalEntity] = []
        self.lies_to_debunk: List[LieToDebunk] = []
        self._initialize_all_entities()
        self._initialize_all_lies()
    
    def _initialize_all_entities(self):
        """Initialize all globally aligned entities across all continents."""
        logger.info("=" * 80)
        logger.info("INITIALIZING GLOBAL ALIGNMENT - ALL CONTINENTS")
        logger.info("=" * 80)
        
        # ========== HUMANITARIAN ORGANIZATIONS ==========
        
        # ICRC - Global
        self.entities.append(GlobalEntity(
            entity_id="icrc_global",
            name="International Committee of the Red Cross (ICRC)",
            category=EntityCategory.HUMANITARIAN,
            continent=Continent.EUROPE,  # HQ in Geneva
            countries=["Global"],  # 120+ conflicts
            description="Neutral humanitarian assistance, protection, and relief in armed conflict and violence. Operates in 120+ conflicts globally.",
            reach={"conflicts": 120, "countries": 100, "people": 100000000},
            siyem_channel=ChannelType.CHANNEL_3_EDUCATIONAL,
            notes="RAMIZ alignment - humanitarian work globally"
        ))
        
        # IFRC - Global
        self.entities.append(GlobalEntity(
            entity_id="ifrc_global",
            name="International Federation of Red Cross and Red Crescent Societies",
            category=EntityCategory.HUMANITARIAN,
            continent=Continent.EUROPE,  # HQ in Geneva
            countries=["Global"],  # 191 countries
            description="World's largest humanitarian network. 17 million volunteers. 191 countries.",
            reach={"countries": 191, "volunteers": 17000000, "people": 200000000},
            siyem_channel=ChannelType.CHANNEL_3_EDUCATIONAL,
            notes="RAMIZ alignment - humanitarian network"
        ))
        
        # MSF - Global
        self.entities.append(GlobalEntity(
            entity_id="msf_global",
            name="Médecins Sans Frontières (MSF)",
            category=EntityCategory.HUMANITARIAN,
            continent=Continent.EUROPE,  # HQ in Geneva
            countries=["Global"],  # 70+ countries
            description="Medical humanitarian assistance. 70+ countries. Conflicts, disasters, epidemics, healthcare exclusion.",
            reach={"countries": 70, "people": 15000000},
            siyem_channel=ChannelType.CHANNEL_3_EDUCATIONAL,
            notes="RAMIZ alignment - medical humanitarian"
        ))
        
        # IRC - Global
        self.entities.append(GlobalEntity(
            entity_id="irc_global",
            name="International Rescue Committee (IRC)",
            category=EntityCategory.HUMANITARIAN,
            continent=Continent.NORTH_AMERICA,  # HQ in US
            countries=["Global"],
            description="Emergency relief and community rebuilding. 90+ years. 10.6M patients in 2024.",
            reach={"people": 10600000, "countries": 40},
            siyem_channel=ChannelType.CHANNEL_3_EDUCATIONAL,
            notes="RAMIZ alignment - emergency relief"
        ))
        
        # ========== FACT-CHECKING ORGANIZATIONS ==========
        
        # IFCN - Global
        self.entities.append(GlobalEntity(
            entity_id="ifcn_global",
            name="International Fact-Checking Network (IFCN)",
            category=EntityCategory.FACT_CHECKING,
            continent=Continent.NORTH_AMERICA,  # Poynter
            countries=["Global"],  # 170+ organizations
            description="170+ fact-checking organizations worldwide. Code of Principles. GlobalFact conference.",
            reach={"organizations": 170, "countries": 80},
            siyem_channel=ChannelType.CHANNEL_3_EDUCATIONAL,
            notes="RAMIZ alignment - fighting lies globally"
        ))
        
        # Trusted News Initiative - Global
        self.entities.append(GlobalEntity(
            entity_id="tni_global",
            name="Trusted News Initiative (TNI)",
            category=EntityCategory.FACT_CHECKING,
            continent=Continent.EUROPE,  # BBC founded
            countries=["Global"],
            description="BBC-founded partnership. Major news organizations and tech platforms. Tackles disinformation in real time.",
            reach={"organizations": 20, "countries": 50},
            siyem_channel=ChannelType.CHANNEL_3_EDUCATIONAL,
            notes="RAMIZ alignment - fighting disinformation"
        ))
        
        # Reuters Fact Check - Global
        self.entities.append(GlobalEntity(
            entity_id="reuters_fact_check",
            name="Reuters Fact Check",
            category=EntityCategory.FACT_CHECKING,
            continent=Continent.EUROPE,  # Reuters
            countries=["Global"],
            description="Fact-checking visual material and claims. IFCN signatory. General news, politics, health, science, environment.",
            reach={"countries": 100},
            siyem_channel=ChannelType.CHANNEL_3_EDUCATIONAL,
            notes="RAMIZ alignment - fact-checking"
        ))
        
        # ========== FOOD SECURITY ORGANIZATIONS ==========
        
        # CGIAR - Global
        self.entities.append(GlobalEntity(
            entity_id="cgiar_global",
            name="CGIAR - Consultative Group for International Agricultural Research",
            category=EntityCategory.FOOD_SECURITY,
            continent=Continent.EUROPE,  # Multiple HQs
            countries=["Global"],  # 25 countries in Food Frontiers
            description="13 research centers. Food, land, water systems. Food Frontiers targets 25 countries.",
            reach={"countries": 25, "centers": 13},
            siyem_channel=ChannelType.CHANNEL_1_PROFESSIONAL,
            notes="EDIBLE/ILVEN alignment - food security"
        ))
        
        # FAO - Global
        self.entities.append(GlobalEntity(
            entity_id="fao_global",
            name="Food and Agriculture Organization (FAO)",
            category=EntityCategory.FOOD_SECURITY,
            continent=Continent.EUROPE,  # Rome
            countries=["Global"],
            description="Inclusive, efficient, resilient food production systems. 2026: International Year of Rangelands and Pastoralists.",
            reach={"countries": 194},
            siyem_channel=ChannelType.CHANNEL_1_PROFESSIONAL,
            notes="EDIBLE/ILVEN alignment - food systems"
        ))
        
        # WFP - Global
        self.entities.append(GlobalEntity(
            entity_id="wfp_global",
            name="World Food Programme (WFP)",
            category=EntityCategory.FOOD_SECURITY,
            continent=Continent.EUROPE,  # Rome
            countries=["Global"],
            description="Multi-actor resilience programming. 40,000 households in Ethiopia, Senegal, Malawi, Zambia.",
            reach={"households": 40000, "countries": 80},
            siyem_channel=ChannelType.CHANNEL_1_PROFESSIONAL,
            notes="EDIBLE/ILVEN alignment - food resilience"
        ))
        
        # ========== MEDIA ORGANIZATIONS ==========
        
        # Al Jazeera - Global
        self.entities.append(GlobalEntity(
            entity_id="al_jazeera_global",
            name="Al Jazeera",
            category=EntityCategory.MEDIA,
            continent=Continent.ASIA,  # Qatar
            countries=["Global"],
            description="Major international news organization. Breaking news and world coverage across multiple continents.",
            reach={"countries": 100, "viewers": 100000000},
            siyem_channel=ChannelType.CHANNEL_2_CREATOR,
            notes="SIYEM MEDIA alignment - news"
        ))
        
        # BBC - Global
        self.entities.append(GlobalEntity(
            entity_id="bbc_global",
            name="BBC News",
            category=EntityCategory.MEDIA,
            continent=Continent.EUROPE,  # UK
            countries=["Global"],  # 200+ countries
            description="World's most trusted international broadcaster. 200+ countries. 450M households. 139M unique browsers monthly.",
            reach={"countries": 200, "households": 450000000, "browsers": 139000000},
            siyem_channel=ChannelType.CHANNEL_2_CREATOR,
            notes="SIYEM MEDIA alignment - news"
        ))
        
        # CNN - Global
        self.entities.append(GlobalEntity(
            entity_id="cnn_global",
            name="CNN",
            category=EntityCategory.MEDIA,
            continent=Continent.NORTH_AMERICA,  # US
            countries=["Global"],
            description="World news coverage. Multiple continents. Breaking news and analysis.",
            reach={"countries": 200, "viewers": 200000000},
            siyem_channel=ChannelType.CHANNEL_2_CREATOR,
            notes="SIYEM MEDIA alignment - news"
        ))
        
        # ========== DIASPORA COMMUNITIES ==========
        
        # Turkish Diaspora - Global
        self.entities.append(GlobalEntity(
            entity_id="turkish_diaspora_global",
            name="Turkish Diaspora",
            category=EntityCategory.DIASPORA,
            continent=Continent.EUROPE,  # Primary in Europe
            countries=["Global"],  # 6M+ people
            description="6+ million people worldwide. Western/Northern Europe, Balkans, Cyprus, Arab nations.",
            reach={"people": 6000000, "countries": 50},
            siyem_channel=ChannelType.CHANNEL_2_CREATOR,
            notes="Diaspora alignment - Turkish communities"
        ))
        
        # Turkish Cypriot Diaspora - Global
        self.entities.append(GlobalEntity(
            entity_id="turkish_cypriot_diaspora_global",
            name="Turkish Cypriot Diaspora",
            category=EntityCategory.DIASPORA,
            continent=Continent.EUROPE,  # Primary in UK
            countries=["Global"],  # Turkey, UK, Australia, etc.
            description="Major populations: Turkey (500K-600K), UK (300K-400K), Australia (120K). North America, New Zealand, South Africa.",
            reach={"people": 1000000, "countries": 10},
            siyem_channel=ChannelType.CHANNEL_2_CREATOR,
            notes="Diaspora alignment - Turkish Cypriot communities"
        ))
        
        # Greek Cypriot Diaspora - Global
        self.entities.append(GlobalEntity(
            entity_id="greek_cypriot_diaspora_global",
            name="Greek Cypriot Diaspora",
            category=EntityCategory.DIASPORA,
            continent=Continent.EUROPE,  # Primary in UK
            countries=["Global"],  # UK, Australia, Canada, etc.
            description="UK (North London), Australia, Canada, South Africa, US, Europe. Many fled after 1974 Turkish invasion.",
            reach={"people": 500000, "countries": 15},
            siyem_channel=ChannelType.CHANNEL_2_CREATOR,
            notes="Diaspora alignment - Greek Cypriot communities"
        ))
        
        # Greek Diaspora - Global
        self.entities.append(GlobalEntity(
            entity_id="greek_diaspora_global",
            name="Greek Diaspora",
            category=EntityCategory.DIASPORA,
            continent=Continent.EUROPE,  # Primary in Europe
            countries=["Global"],  # Australia, Canada, Germany, UK, US
            description="Global Greek diaspora. Australia, Canada, Germany, UK, US. Cultural and community organizations.",
            reach={"people": 5000000, "countries": 30},
            siyem_channel=ChannelType.CHANNEL_2_CREATOR,
            notes="Diaspora alignment - Greek communities"
        ))
        
        logger.info(f"Initialized {len(self.entities)} globally aligned entities")
        logger.info("=" * 80)
    
    def _initialize_all_lies(self):
        """Initialize all lies to debunk globally."""
        logger.info("=" * 80)
        logger.info("INITIALIZING ALL LIES TO DEBUNK - GLOBAL")
        logger.info("=" * 80)
        logger.info("THERE'S ALWAYS ANOTHER LIE TO DEBUNK")
        logger.info("=" * 80)
        
        # ========== AFRICA LIES ==========
        
        self.lies_to_debunk.append(LieToDebunk(
            lie_id="africa_poverty_inevitable",
            lie_statement="Africa is poor because Africans are lazy or incapable.",
            truth_statement="Africa's poverty is the result of centuries of colonialism, resource extraction, debt traps, and unfair trade practices. African people are hardworking, innovative, and capable. The continent has vast resources and potential.",
            region="Africa",
            continent=Continent.AFRICA,
            countries=["All African Countries"],
            people_affected={"count": 1400000000, "description": "All people of Africa"},
            source="Colonial narratives, media bias",
            priority="high"
        ))
        
        self.lies_to_debunk.append(LieToDebunk(
            lie_id="africa_disease_innate",
            lie_statement="Diseases in Africa are because of African biology or culture.",
            truth_statement="Diseases in Africa are due to lack of healthcare infrastructure, poverty, and historical exploitation. African people have strong immune systems and rich traditional medicine knowledge.",
            region="Africa",
            continent=Continent.AFRICA,
            countries=["All African Countries"],
            people_affected={"count": 1400000000, "description": "All people of Africa"},
            source="Racist narratives, medical bias",
            priority="high"
        ))
        
        # ========== ASIA LIES ==========
        
        self.lies_to_debunk.append(LieToDebunk(
            lie_id="asia_overpopulation_problem",
            lie_statement="Asia is overpopulated and needs population control.",
            truth_statement="Asia's population density is manageable with proper resource distribution and sustainable development. The issue is resource inequality, not population size.",
            region="Asia",
            continent=Continent.ASIA,
            countries=["China", "India", "Indonesia", "Bangladesh", "Pakistan"],
            people_affected={"count": 4000000000, "description": "People of Asia"},
            source="Malthusian narratives, eugenics",
            priority="high"
        ))
        
        self.lies_to_debunk.append(LieToDebunk(
            lie_id="asia_authoritarian_culture",
            lie_statement="Asian cultures are naturally authoritarian and undemocratic.",
            truth_statement="Asian cultures have diverse political traditions. Many Asian countries have democratic movements and traditions. Authoritarianism is not cultural but political.",
            region="Asia",
            continent=Continent.ASIA,
            countries=["All Asian Countries"],
            people_affected={"count": 4000000000, "description": "People of Asia"},
            source="Orientalist narratives, cultural bias",
            priority="high"
        ))
        
        # ========== EUROPE LIES ==========
        
        self.lies_to_debunk.append(LieToDebunk(
            lie_id="europe_superior_civilization",
            lie_statement="Europe is superior to other continents in civilization and culture.",
            truth_statement="All continents have rich civilizations and cultures. Europe's development was built on colonialism, resource extraction, and exploitation of other continents. All peoples are equal.",
            region="Europe",
            continent=Continent.EUROPE,
            countries=["All European Countries"],
            people_affected={"count": 750000000, "description": "People of Europe"},
            source="Eurocentric narratives, white supremacy",
            priority="high"
        ))
        
        self.lies_to_debunk.append(LieToDebunk(
            lie_id="europe_refugee_crisis",
            lie_statement="Refugees are a burden and threat to Europe.",
            truth_statement="Refugees are people fleeing war and persecution. They contribute to European societies. The real issue is Europe's responsibility for creating conditions that cause displacement.",
            region="Europe",
            continent=Continent.EUROPE,
            countries=["All European Countries"],
            people_affected={"count": 10000000, "description": "Refugees in Europe"},
            source="Xenophobic narratives, media fear-mongering",
            priority="high"
        ))
        
        # ========== AMERICAS LIES ==========
        
        self.lies_to_debunk.append(LieToDebunk(
            lie_id="americas_immigration_crime",
            lie_statement="Immigrants bring crime and take jobs.",
            truth_statement="Immigrants are less likely to commit crimes than native-born citizens. They create jobs and contribute to economies. Immigration is a human right.",
            region="Americas",
            continent=Continent.NORTH_AMERICA,
            countries=["United States", "Canada", "Mexico"],
            people_affected={"count": 50000000, "description": "Immigrants in Americas"},
            source="Xenophobic narratives, political fear-mongering",
            priority="high"
        ))
        
        self.lies_to_debunk.append(LieToDebunk(
            lie_id="americas_latin_america_poor",
            lie_statement="Latin America is poor because of Latin American culture or people.",
            truth_statement="Latin America's poverty is due to centuries of colonialism, resource extraction, debt, and intervention. Latin American people are hardworking and capable. The continent has vast resources.",
            region="Americas",
            continent=Continent.SOUTH_AMERICA,
            countries=["All Latin American Countries"],
            people_affected={"count": 600000000, "description": "People of Latin America"},
            source="Racist narratives, media bias",
            priority="high"
        ))
        
        # ========== OCEANIA LIES ==========
        
        self.lies_to_debunk.append(LieToDebunk(
            lie_id="oceania_aboriginal_primitive",
            lie_statement="Aboriginal and Indigenous peoples are primitive or backward.",
            truth_statement="Aboriginal and Indigenous peoples have rich, sophisticated cultures and knowledge systems. They are the original stewards of the land. Their knowledge is valuable and advanced.",
            region="Oceania",
            continent=Continent.OCEANIA,
            countries=["Australia", "New Zealand", "Pacific Islands"],
            people_affected={"count": 5000000, "description": "Indigenous peoples of Oceania"},
            source="Colonial narratives, racist stereotypes",
            priority="high"
        ))
        
        # ========== MIDDLE EAST LIES ==========
        
        self.lies_to_debunk.append(LieToDebunk(
            lie_id="middle_east_terrorism_islam",
            lie_statement="Terrorism is inherent to Islam or Middle Eastern culture.",
            truth_statement="Terrorism is not religious or cultural. It is political violence. Most Muslims and Middle Eastern people are peaceful. Terrorism is committed by extremists of all backgrounds.",
            region="Middle East",
            continent=Continent.ASIA,
            countries=["All Middle Eastern Countries"],
            people_affected={"count": 500000000, "description": "Muslims and Middle Eastern people"},
            source="Islamophobic narratives, media bias",
            priority="high"
        ))
        
        self.lies_to_debunk.append(LieToDebunk(
            lie_id="middle_east_gaza_justified",
            lie_statement="The destruction of Gaza is justified or necessary.",
            truth_statement="The destruction of Gaza is a humanitarian crisis and violation of international law. All people deserve dignity, safety, and freedom. Violence against civilians is never justified.",
            region="Middle East",
            continent=Continent.ASIA,
            countries=["Palestine", "Israel", "Gaza"],
            people_affected={"count": 2300000, "description": "People of Gaza"},
            source="War propaganda, dehumanization",
            priority="critical"
        ))
        
        # ========== GLOBAL LIES ==========
        
        self.lies_to_debunk.append(LieToDebunk(
            lie_id="global_climate_denial",
            lie_statement="Climate change is not real or not caused by humans.",
            truth_statement="Climate change is real, caused by human activity, and requires urgent action. Science is clear. We must act now to protect the planet and all people.",
            region="Global",
            continent=Continent.ANTARCTICA,  # Affects all
            countries=["All Countries"],
            people_affected={"count": 8000000000, "description": "All people on Earth"},
            source="Fossil fuel industry, climate denial",
            priority="critical"
        ))
        
        self.lies_to_debunk.append(LieToDebunk(
            lie_id="global_inequality_natural",
            lie_statement="Inequality is natural and cannot be changed.",
            truth_statement="Inequality is created by systems and can be changed. All people deserve dignity, opportunity, and resources. We can build a more just world.",
            region="Global",
            continent=Continent.ANTARCTICA,  # Affects all
            countries=["All Countries"],
            people_affected={"count": 8000000000, "description": "All people on Earth"},
            source="Elite narratives, status quo protection",
            priority="high"
        ))
        
        logger.info(f"Initialized {len(self.lies_to_debunk)} lies to debunk globally")
        logger.info("=" * 80)
    
    def integrate_with_siyem(self):
        """Integrate all global entities with SIYEM."""
        logger.info("=" * 80)
        logger.info("INTEGRATING GLOBAL ENTITIES WITH SIYEM")
        logger.info("=" * 80)
        
        if not self.publishing_entity:
            logger.warning("Publishing entity not available - skipping integration")
            return
        
        integrated_count = 0
        
        for entity in self.entities:
            try:
                entity_data = {
                    "entity_id": entity.entity_id,
                    "name": entity.name,
                    "category": entity.category.value,
                    "continent": entity.continent.value,
                    "countries": entity.countries,
                    "description": entity.description,
                    "reach": entity.reach,
                    "integration_status": entity.integration_status,
                    "timestamp": entity.timestamp
                }
                
                # Determine entity role
                if entity.category == EntityCategory.HUMANITARIAN:
                    entity_role = EntityRole.RAMIZ_HUMANITARIAN
                elif entity.category == EntityCategory.FACT_CHECKING:
                    entity_role = EntityRole.RAMIZ_HUMANITARIAN
                elif entity.category == EntityCategory.FOOD_SECURITY:
                    entity_role = EntityRole.EDIBLE_LONDON
                elif entity.category == EntityCategory.MEDIA:
                    entity_role = EntityRole.SIYEM_SYSTEMS
                else:
                    entity_role = EntityRole.SIYEM_SYSTEMS
                
                self.publishing_entity.channels.add_to_channel(
                    entity.siyem_channel,
                    entity.entity_id,
                    entity_data,
                    entity_role
                )
                
                entity.integration_status = "integrated"
                integrated_count += 1
                logger.info(f"  [INTEGRATED] {entity.name} → {entity.siyem_channel.value} ({entity.category.value})")
                
            except Exception as e:
                logger.warning(f"Could not integrate {entity.name}: {e}")
        
        logger.info(f"\nIntegrated {integrated_count} global entities")
        logger.info("=" * 80)
    
    def export_global_alignment_report(self):
        """Export global alignment report."""
        report = {
            "timestamp": datetime.now().isoformat(),
            "title": "Global Alignment Complete - All Continents, All Countries, All of God's Lands and Waters",
            "status": "COMPLETE",
            "total_entities": len(self.entities),
            "total_lies": len(self.lies_to_debunk),
            "continents_covered": [c.value for c in Continent],
            "entities_by_continent": {},
            "entities_by_category": {},
            "lies_by_continent": {},
            "entities": [],
            "lies_to_debunk": []
        }
        
        # Count by continent
        for continent in Continent:
            report["entities_by_continent"][continent.value] = len([
                e for e in self.entities if e.continent == continent
            ])
            report["lies_by_continent"][continent.value] = len([
                l for l in self.lies_to_debunk if l.continent == continent
            ])
        
        # Count by category
        for category in EntityCategory:
            report["entities_by_category"][category.value] = len([
                e for e in self.entities if e.category == category
            ])
        
        # Add entities
        for entity in self.entities:
            report["entities"].append({
                "entity_id": entity.entity_id,
                "name": entity.name,
                "category": entity.category.value,
                "continent": entity.continent.value,
                "countries": entity.countries,
                "description": entity.description,
                "reach": entity.reach,
                "integration_status": entity.integration_status,
                "siyem_channel": entity.siyem_channel.value if entity.siyem_channel else None,
                "timestamp": entity.timestamp
            })
        
        # Add lies
        for lie in self.lies_to_debunk:
            report["lies_to_debunk"].append({
                "lie_id": lie.lie_id,
                "lie_statement": lie.lie_statement,
                "truth_statement": lie.truth_statement,
                "region": lie.region,
                "continent": lie.continent.value,
                "countries": lie.countries,
                "people_affected": lie.people_affected,
                "source": lie.source,
                "priority": lie.priority,
                "status": lie.status,
                "timestamp": lie.timestamp
            })
        
        # Save report
        report_path = self.output_dir / "global_alignment_complete_report.json"
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, default=str, ensure_ascii=False)
        
        logger.info(f"Global alignment report exported to: {report_path}")
        return report_path


def main():
    """Main execution."""
    siyem_path = Path("s:\\SIYEM")
    jan_path = Path("s:\\JAN")
    output_dir = jan_path / "SIYEM" / "output" / "global_alignment"
    
    alignment = GlobalAlignmentComplete(siyem_path, jan_path, output_dir)
    
    # Integrate with SIYEM
    alignment.integrate_with_siyem()
    
    # Export report
    alignment.export_global_alignment_report()
    
    logger.info("\n" + "=" * 80)
    logger.info("GLOBAL ALIGNMENT COMPLETE")
    logger.info("=" * 80)
    logger.info(f"Total Entities: {len(alignment.entities)}")
    logger.info(f"Total Lies to Debunk: {len(alignment.lies_to_debunk)}")
    logger.info(f"Continents Covered: {len(Continent)}")
    logger.info("=" * 80)
    logger.info("ALL CONTINENTS. ALL COUNTRIES. ALL OF GOD'S LANDS AND WATERS.")
    logger.info("THERE'S ALWAYS ANOTHER LIE TO DEBUNK.")
    logger.info("RAMIZ CAN DO IT.")
    logger.info("=" * 80)


if __name__ == "__main__":
    main()
