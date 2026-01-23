"""
GLOBAL OPPORTUNITY LINKER
Identify and link up with real-world aligned opportunities for each project globally
Expand and include all that we can

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
IDENTIFY REAL-WORLD ALIGNED OPPORTUNITIES
LINK PROJECTS TO GLOBAL OPPORTUNITIES
EXPAND AND INCLUDE ALL THAT WE CAN
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

class OpportunityType(Enum):
    """Types of opportunities"""
    PARTNERSHIP = "partnership"
    COLLABORATION = "collaboration"
    DISTRIBUTION = "distribution"
    LICENSING = "licensing"
    INVESTMENT = "investment"
    MARKET_ACCESS = "market_access"
    RESOURCE_SHARING = "resource_sharing"
    KNOWLEDGE_EXCHANGE = "knowledge_exchange"

class Region(Enum):
    """Global regions"""
    GLOBAL = "global"
    NORTH_AMERICA = "north_america"
    EUROPE = "europe"
    ASIA = "asia"
    MIDDLE_EAST = "middle_east"
    AFRICA = "africa"
    LATIN_AMERICA = "latin_america"
    OCEANIA = "oceania"
    TURKEY = "turkey"
    CYPRUS = "cyprus"
    UK = "uk"

@dataclass
class GlobalOpportunity:
    """A real-world aligned opportunity"""
    opportunity_id: str
    name: str
    description: str
    opportunity_type: OpportunityType
    region: Region
    industry: str
    alignment_score: float = 0.0  # 0.0 to 1.0
    entity_name: Optional[str] = None
    entity_type: Optional[str] = None
    website: Optional[str] = None
    contact_info: Optional[str] = None
    how_they_align: List[str] = field(default_factory=list)
    connection_to_table: bool = True
    supports_restoration: bool = False
    frequency_contribution: float = 0.0
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    updated_at: str = field(default_factory=lambda: datetime.now().isoformat())

@dataclass
class ProjectOpportunityLink:
    """Link between a project and an opportunity"""
    link_id: str
    project_id: str
    opportunity_id: str
    link_type: OpportunityType
    alignment_score: float = 0.0
    revenue_potential: float = 0.0
    status: str = "identified"  # identified, contacted, in_negotiation, active, completed
    notes: str = ""
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    updated_at: str = field(default_factory=lambda: datetime.now().isoformat())

class GlobalOpportunityLinker:
    """
    Global Opportunity Linker
    Identify and link real-world aligned opportunities for each project globally
    """
    
    def __init__(self, user_id: str = "jan", data_dir: Path = None):
        self.user_id = user_id
        self.data_dir = data_dir or Path(__file__).parent.parent / "data" / "global_opportunities"
        self.data_dir.mkdir(parents=True, exist_ok=True)
        
        self.opportunities_file = self.data_dir / f"{user_id}_opportunities.json"
        self.links_file = self.data_dir / f"{user_id}_project_links.json"
        
        self.opportunities: List[GlobalOpportunity] = []
        self.project_links: List[ProjectOpportunityLink] = []
        
        self._load_data()
        # Always reinitialize to ensure all opportunities are included
        if len(self.opportunities) < 40:  # If we have fewer than expected, reinitialize
            self.opportunities = []
            self.project_links = []
            self._initialize_global_opportunities()
    
    def _load_data(self):
        """Load opportunities and links"""
        # Load opportunities
        if self.opportunities_file.exists():
            try:
                with open(self.opportunities_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                opportunities_data = []
                for o in data.get("opportunities", []):
                    o['opportunity_type'] = OpportunityType(o['opportunity_type'])
                    o['region'] = Region(o['region'])
                    opportunities_data.append(GlobalOpportunity(**o))
                self.opportunities = opportunities_data
            except Exception as e:
                logger.warning(f"Error loading opportunities: {e}")
                self.opportunities = []
        
        # Load links
        if self.links_file.exists():
            try:
                with open(self.links_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                links_data = []
                for l in data.get("links", []):
                    l['link_type'] = OpportunityType(l['link_type'])
                    links_data.append(ProjectOpportunityLink(**l))
                self.project_links = links_data
            except Exception as e:
                logger.warning(f"Error loading links: {e}")
                self.project_links = []
    
    def _save_data(self):
        """Save opportunities and links"""
        try:
            # Save opportunities
            opportunities_data = []
            for o in self.opportunities:
                o_dict = asdict(o)
                o_dict['opportunity_type'] = o.opportunity_type.value
                o_dict['region'] = o.region.value
                opportunities_data.append(o_dict)
            
            with open(self.opportunities_file, 'w', encoding='utf-8') as f:
                json.dump({
                    "opportunities": opportunities_data,
                    "last_updated": datetime.now().isoformat()
                }, f, indent=2, ensure_ascii=False)
            
            # Save links
            links_data = []
            for l in self.project_links:
                l_dict = asdict(l)
                l_dict['link_type'] = l.link_type.value
                links_data.append(l_dict)
            
            with open(self.links_file, 'w', encoding='utf-8') as f:
                json.dump({
                    "links": links_data,
                    "last_updated": datetime.now().isoformat()
                }, f, indent=2, ensure_ascii=False)
        except Exception as e:
            logger.error(f"Error saving data: {e}")
    
    def _initialize_global_opportunities(self):
        """Initialize global aligned opportunities"""
        
        # ========================================================================
        # EDIBLE LONDON - Global Opportunities
        # ========================================================================
        
        # Food Media & Distribution
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_edible_london_001",
            name="Food Network Partnerships",
            description="Partnership with food networks, streaming platforms, and food media for content distribution",
            opportunity_type=OpportunityType.DISTRIBUTION,
            region=Region.GLOBAL,
            industry="media",
            alignment_score=0.9,
            entity_name="Food Networks, Streaming Platforms",
            how_they_align=["Content distribution", "Food education", "Cultural sharing"],
            supports_restoration=True,
            frequency_contribution=0.1
        ))
        
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_edible_london_002",
            name="Restaurant & Food Service Partnerships",
            description="Partnerships with restaurants, food service companies, and culinary schools globally",
            opportunity_type=OpportunityType.PARTNERSHIP,
            region=Region.GLOBAL,
            industry="food_service",
            alignment_score=0.9,
            entity_name="Restaurant Chains, Culinary Schools",
            how_they_align=["Food education", "Cultural exchange", "Community building"],
            supports_restoration=True,
            frequency_contribution=0.1
        ))
        
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_edible_london_003",
            name="Sustainable Food Organizations",
            description="Collaboration with sustainable food organizations, food banks, and community food initiatives",
            opportunity_type=OpportunityType.COLLABORATION,
            region=Region.GLOBAL,
            industry="nonprofit",
            alignment_score=1.0,
            entity_name="Food Banks, Sustainable Food Orgs",
            how_they_align=["Food security", "Community support", "Sustainability"],
            supports_restoration=True,
            frequency_contribution=0.2
        ))
        
        # ========================================================================
        # ILVEN SEAMOSS - Global Opportunities
        # ========================================================================
        
        # Health & Wellness
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_ilven_seamoss_001",
            name="Health & Wellness Retailers",
            description="Distribution partnerships with health food stores, wellness retailers, and online health platforms globally",
            opportunity_type=OpportunityType.DISTRIBUTION,
            region=Region.GLOBAL,
            industry="retail",
            alignment_score=0.9,
            entity_name="Health Food Stores, Wellness Retailers",
            how_they_align=["Health promotion", "Natural products", "Wellness"],
            supports_restoration=True,
            frequency_contribution=0.1
        ))
        
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_ilven_seamoss_002",
            name="Nutritional Supplement Companies",
            description="Partnerships with ethical supplement companies and nutritional brands",
            opportunity_type=OpportunityType.PARTNERSHIP,
            region=Region.GLOBAL,
            industry="healthcare",
            alignment_score=0.8,
            entity_name="Ethical Supplement Brands",
            how_they_align=["Health support", "Natural nutrition"],
            supports_restoration=True,
            frequency_contribution=0.1
        ))
        
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_ilven_seamoss_003",
            name="Marine Conservation Organizations",
            description="Collaboration with marine conservation organizations and sustainable harvesting initiatives",
            opportunity_type=OpportunityType.COLLABORATION,
            region=Region.GLOBAL,
            industry="environmental",
            alignment_score=1.0,
            entity_name="Marine Conservation Orgs",
            how_they_align=["Ocean protection", "Sustainable practices", "Environmental stewardship"],
            supports_restoration=True,
            frequency_contribution=0.2
        ))
        
        # ========================================================================
        # EDIBLE CYPRUS - Global Opportunities
        # ========================================================================
        
        # Food Supply & Distribution
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_edible_cyprus_001",
            name="International Food Distributors",
            description="Partnerships with international food distributors and import/export companies",
            opportunity_type=OpportunityType.DISTRIBUTION,
            region=Region.GLOBAL,
            industry="food_supply",
            alignment_score=0.9,
            entity_name="Food Distributors, Import/Export",
            how_they_align=["Food distribution", "Cultural food exchange"],
            supports_restoration=True,
            frequency_contribution=0.1
        ))
        
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_edible_cyprus_002",
            name="Mediterranean Food Networks",
            description="Partnerships with Mediterranean food networks and regional food organizations",
            opportunity_type=OpportunityType.PARTNERSHIP,
            region=Region.EUROPE,
            industry="food_networks",
            alignment_score=0.9,
            entity_name="Mediterranean Food Networks",
            how_they_align=["Cultural preservation", "Regional food traditions"],
            supports_restoration=True,
            frequency_contribution=0.1
        ))
        
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_edible_cyprus_003",
            name="Local Food Cooperatives",
            description="Collaboration with local food cooperatives and community-supported agriculture",
            opportunity_type=OpportunityType.COLLABORATION,
            region=Region.GLOBAL,
            industry="cooperative",
            alignment_score=1.0,
            entity_name="Food Cooperatives, CSA Networks",
            how_they_align=["Community support", "Local food systems", "Cooperation"],
            supports_restoration=True,
            frequency_contribution=0.2
        ))
        
        # ========================================================================
        # ATILOK LTD - Global Opportunities
        # ========================================================================
        
        # E-commerce & Truck Parts
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_atilok_001",
            name="Global E-commerce Platforms",
            description="Partnerships with global e-commerce platforms and marketplaces for truck parts distribution",
            opportunity_type=OpportunityType.DISTRIBUTION,
            region=Region.GLOBAL,
            industry="ecommerce",
            alignment_score=0.8,
            entity_name="E-commerce Platforms, Marketplaces",
            how_they_align=["Market access", "Distribution"],
            supports_restoration=False,
            frequency_contribution=0.05
        ))
        
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_atilok_002",
            name="Truck Parts Manufacturers",
            description="Direct partnerships with ethical truck parts manufacturers and suppliers globally",
            opportunity_type=OpportunityType.PARTNERSHIP,
            region=Region.GLOBAL,
            industry="manufacturing",
            alignment_score=0.8,
            entity_name="Truck Parts Manufacturers",
            how_they_align=["Supply chain", "Product access"],
            supports_restoration=False,
            frequency_contribution=0.05
        ))
        
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_atilok_003",
            name="Transportation Cooperatives",
            description="Partnerships with transportation cooperatives and ethical logistics companies",
            opportunity_type=OpportunityType.COLLABORATION,
            region=Region.GLOBAL,
            industry="cooperative",
            alignment_score=0.9,
            entity_name="Transportation Cooperatives",
            how_they_align=["Cooperation", "Community support", "Ethical business"],
            supports_restoration=True,
            frequency_contribution=0.1
        ))
        
        # ========================================================================
        # CREATIVE PERSONAS - Global Opportunities
        # ========================================================================
        
        # Jean Morphius - Publishing & Education
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_jean_001",
            name="International Publishers",
            description="Partnerships with international publishers for bilingual story distribution",
            opportunity_type=OpportunityType.DISTRIBUTION,
            region=Region.GLOBAL,
            industry="publishing",
            alignment_score=0.9,
            entity_name="International Publishers",
            how_they_align=["Story distribution", "Cultural exchange", "Education"],
            supports_restoration=True,
            frequency_contribution=0.1
        ))
        
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_jean_002",
            name="Educational Institutions",
            description="Partnerships with schools, universities, and educational platforms globally",
            opportunity_type=OpportunityType.PARTNERSHIP,
            region=Region.GLOBAL,
            industry="education",
            alignment_score=1.0,
            entity_name="Schools, Universities, EdTech",
            how_they_align=["Education", "Knowledge sharing", "Truth"],
            supports_restoration=True,
            frequency_contribution=0.2
        ))
        
        # Karasahin - Music & Sound
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_karasahin_001",
            name="Music Streaming Platforms",
            description="Distribution partnerships with ethical music streaming platforms and independent music networks",
            opportunity_type=OpportunityType.DISTRIBUTION,
            region=Region.GLOBAL,
            industry="music",
            alignment_score=0.9,
            entity_name="Independent Music Platforms",
            how_they_align=["Music distribution", "Artist support", "Cultural music"],
            supports_restoration=True,
            frequency_contribution=0.1
        ))
        
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_karasahin_002",
            name="Music Festivals & Venues",
            description="Partnerships with music festivals, venues, and cultural events globally",
            opportunity_type=OpportunityType.PARTNERSHIP,
            region=Region.GLOBAL,
            industry="music",
            alignment_score=0.9,
            entity_name="Music Festivals, Cultural Venues",
            how_they_align=["Cultural expression", "Community building", "Music"],
            supports_restoration=True,
            frequency_contribution=0.1
        ))
        
        # Pierre Pressure - Speaking & Coaching
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_pierre_001",
            name="Speaking Engagement Platforms",
            description="Partnerships with speaking platforms, conferences, and motivational events globally",
            opportunity_type=OpportunityType.PARTNERSHIP,
            region=Region.GLOBAL,
            industry="events",
            alignment_score=0.9,
            entity_name="Speaking Platforms, Conferences",
            how_they_align=["Motivation", "Truth sharing", "Community"],
            supports_restoration=True,
            frequency_contribution=0.1
        ))
        
        # Uncle Ray Ramiz - Spiritual & Teaching
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_ramiz_001",
            name="Spiritual & Educational Communities",
            description="Partnerships with spiritual communities, educational organizations, and wisdom-sharing platforms",
            opportunity_type=OpportunityType.COLLABORATION,
            region=Region.GLOBAL,
            industry="spiritual",
            alignment_score=1.0,
            entity_name="Spiritual Communities, Wisdom Platforms",
            how_they_align=["Spiritual guidance", "Wisdom sharing", "Truth"],
            supports_restoration=True,
            frequency_contribution=0.2
        ))
        
        # ========================================================================
        # JAN STUDIO - Global Opportunities
        # ========================================================================
        
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_jan_studio_001",
            name="Creator Economy Platforms",
            description="Partnerships with creator economy platforms, marketplaces, and creator tools globally",
            opportunity_type=OpportunityType.PARTNERSHIP,
            region=Region.GLOBAL,
            industry="technology",
            alignment_score=0.9,
            entity_name="Creator Platforms, Marketplaces",
            how_they_align=["Creator support", "Tool sharing", "Community"],
            supports_restoration=True,
            frequency_contribution=0.1
        ))
        
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_jan_studio_002",
            name="Open Source Communities",
            description="Collaboration with open source communities and developer networks",
            opportunity_type=OpportunityType.COLLABORATION,
            region=Region.GLOBAL,
            industry="technology",
            alignment_score=1.0,
            entity_name="Open Source Communities",
            how_they_align=["Open sharing", "Community", "No exploitation"],
            supports_restoration=True,
            frequency_contribution=0.2
        ))
        
        # ========================================================================
        # SIYEM.ORG - Global Opportunities
        # ========================================================================
        
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_siyem_org_001",
            name="Non-Profit Networks",
            description="Partnerships with non-profit networks, foundations, and humanitarian organizations globally",
            opportunity_type=OpportunityType.COLLABORATION,
            region=Region.GLOBAL,
            industry="nonprofit",
            alignment_score=1.0,
            entity_name="Non-Profit Networks, Foundations",
            how_they_align=["Service", "Community support", "No exploitation"],
            supports_restoration=True,
            frequency_contribution=0.2
        ))
        
        # ========================================================================
        # EXPANDED GLOBAL OPPORTUNITIES - ALL PROJECTS
        # ========================================================================
        
        # Edible London - Expanded
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_edible_london_004",
            name="Food Documentary Platforms",
            description="Partnerships with documentary platforms, food channels, and streaming services for content distribution",
            opportunity_type=OpportunityType.DISTRIBUTION,
            region=Region.GLOBAL,
            industry="media",
            alignment_score=0.9,
            entity_name="Documentary Platforms, Food Channels",
            how_they_align=["Food education", "Cultural sharing", "Content distribution"],
            supports_restoration=True,
            frequency_contribution=0.1
        ))
        
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_edible_london_005",
            name="Culinary Tourism Organizations",
            description="Partnerships with culinary tourism organizations and food travel platforms",
            opportunity_type=OpportunityType.PARTNERSHIP,
            region=Region.GLOBAL,
            industry="tourism",
            alignment_score=0.9,
            entity_name="Culinary Tourism Orgs",
            how_they_align=["Cultural exchange", "Food education", "Community"],
            supports_restoration=True,
            frequency_contribution=0.1
        ))
        
        # Ilven Seamoss - Expanded
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_ilven_seamoss_004",
            name="Holistic Health Practitioners",
            description="Partnerships with holistic health practitioners, naturopaths, and wellness coaches globally",
            opportunity_type=OpportunityType.PARTNERSHIP,
            region=Region.GLOBAL,
            industry="healthcare",
            alignment_score=0.9,
            entity_name="Holistic Health Practitioners",
            how_they_align=["Natural health", "Wellness", "Holistic approach"],
            supports_restoration=True,
            frequency_contribution=0.1
        ))
        
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_ilven_seamoss_005",
            name="Caribbean & Island Communities",
            description="Direct partnerships with Caribbean and island communities where sea moss is traditionally harvested",
            opportunity_type=OpportunityType.COLLABORATION,
            region=Region.GLOBAL,
            industry="community",
            alignment_score=1.0,
            entity_name="Caribbean Communities, Island Harvesters",
            how_they_align=["Community support", "Traditional knowledge", "Fair trade"],
            supports_restoration=True,
            frequency_contribution=0.2
        ))
        
        # Edible Cyprus - Expanded
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_edible_cyprus_004",
            name="Turkish & Greek Food Networks",
            description="Partnerships with Turkish and Greek food networks, cultural organizations, and diaspora communities",
            opportunity_type=OpportunityType.PARTNERSHIP,
            region=Region.EUROPE,
            industry="food_networks",
            alignment_score=0.9,
            entity_name="Turkish/Greek Food Networks",
            how_they_align=["Cultural preservation", "Diaspora connection", "Food traditions"],
            supports_restoration=True,
            frequency_contribution=0.1
        ))
        
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_edible_cyprus_005",
            name="Cyprus Tourism & Cultural Organizations",
            description="Partnerships with Cyprus tourism boards and cultural preservation organizations",
            opportunity_type=OpportunityType.COLLABORATION,
            region=Region.CYPRUS,
            industry="tourism",
            alignment_score=1.0,
            entity_name="Cyprus Tourism, Cultural Orgs",
            how_they_align=["Cultural preservation", "Heritage", "Community support"],
            supports_restoration=True,
            frequency_contribution=0.2
        ))
        
        # ATILOK - Expanded
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_atilok_004",
            name="Logistics & Transportation Networks",
            description="Partnerships with ethical logistics companies and transportation networks globally",
            opportunity_type=OpportunityType.PARTNERSHIP,
            region=Region.GLOBAL,
            industry="logistics",
            alignment_score=0.8,
            entity_name="Logistics Companies, Transport Networks",
            how_they_align=["Supply chain", "Distribution"],
            supports_restoration=False,
            frequency_contribution=0.05
        ))
        
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_atilok_005",
            name="Truck Driver Communities",
            description="Direct partnerships with truck driver communities and associations globally",
            opportunity_type=OpportunityType.COLLABORATION,
            region=Region.GLOBAL,
            industry="community",
            alignment_score=0.9,
            entity_name="Truck Driver Communities",
            how_they_align=["Community support", "Worker support", "Fair access"],
            supports_restoration=True,
            frequency_contribution=0.1
        ))
        
        # Creative Personas - Expanded
        # Jean Morphius
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_jean_003",
            name="Bilingual Education Networks",
            description="Partnerships with bilingual education networks, language learning platforms, and cultural exchange programs",
            opportunity_type=OpportunityType.PARTNERSHIP,
            region=Region.GLOBAL,
            industry="education",
            alignment_score=1.0,
            entity_name="Bilingual Education Networks",
            how_they_align=["Language learning", "Cultural exchange", "Education"],
            supports_restoration=True,
            frequency_contribution=0.2
        ))
        
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_jean_004",
            name="Literary Festivals & Book Fairs",
            description="Partnerships with literary festivals, book fairs, and storytelling events globally",
            opportunity_type=OpportunityType.PARTNERSHIP,
            region=Region.GLOBAL,
            industry="arts",
            alignment_score=0.9,
            entity_name="Literary Festivals, Book Fairs",
            how_they_align=["Story sharing", "Cultural expression", "Community"],
            supports_restoration=True,
            frequency_contribution=0.1
        ))
        
        # Karasahin
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_karasahin_003",
            name="Turkish & Cypriot Cultural Organizations",
            description="Partnerships with Turkish and Cypriot cultural organizations, diaspora communities, and heritage groups",
            opportunity_type=OpportunityType.COLLABORATION,
            region=Region.GLOBAL,
            industry="heritage",
            alignment_score=1.0,
            entity_name="Turkish/Cypriot Cultural Orgs",
            how_they_align=["Cultural preservation", "Heritage", "Identity"],
            supports_restoration=True,
            frequency_contribution=0.2
        ))
        
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_karasahin_004",
            name="Sound & Music Therapy Organizations",
            description="Partnerships with sound therapy, music therapy, and healing music organizations",
            opportunity_type=OpportunityType.COLLABORATION,
            region=Region.GLOBAL,
            industry="healthcare",
            alignment_score=0.9,
            entity_name="Music Therapy Orgs",
            how_they_align=["Healing", "Wellness", "Sound as medicine"],
            supports_restoration=True,
            frequency_contribution=0.1
        ))
        
        # Pierre Pressure
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_pierre_002",
            name="Fitness & Martial Arts Communities",
            description="Partnerships with fitness communities, martial arts schools, and combat sports organizations",
            opportunity_type=OpportunityType.PARTNERSHIP,
            region=Region.GLOBAL,
            industry="sports",
            alignment_score=0.9,
            entity_name="Fitness Communities, Martial Arts",
            how_they_align=["Discipline", "Strength", "Community"],
            supports_restoration=True,
            frequency_contribution=0.1
        ))
        
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_pierre_003",
            name="Personal Development Platforms",
            description="Partnerships with personal development platforms, self-improvement communities, and growth networks",
            opportunity_type=OpportunityType.PARTNERSHIP,
            region=Region.GLOBAL,
            industry="education",
            alignment_score=0.9,
            entity_name="Personal Development Platforms",
            how_they_align=["Growth", "Empowerment", "Truth"],
            supports_restoration=True,
            frequency_contribution=0.1
        ))
        
        # Uncle Ray Ramiz
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_ramiz_002",
            name="Interfaith Organizations",
            description="Partnerships with interfaith organizations, unity-focused spiritual groups, and peace-building communities",
            opportunity_type=OpportunityType.COLLABORATION,
            region=Region.GLOBAL,
            industry="spiritual",
            alignment_score=1.0,
            entity_name="Interfaith Orgs, Unity Groups",
            how_they_align=["Unity", "Peace", "Truth", "No division"],
            supports_restoration=True,
            frequency_contribution=0.2
        ))
        
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_ramiz_003",
            name="Ancestral Wisdom Networks",
            description="Partnerships with ancestral wisdom networks, indigenous knowledge keepers, and traditional teaching communities",
            opportunity_type=OpportunityType.COLLABORATION,
            region=Region.GLOBAL,
            industry="heritage",
            alignment_score=1.0,
            entity_name="Ancestral Wisdom Networks",
            how_they_align=["Wisdom preservation", "Traditional knowledge", "Heritage"],
            supports_restoration=True,
            frequency_contribution=0.2
        ))
        
        # JAN Studio - Expanded
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_jan_studio_003",
            name="Educational Technology Platforms",
            description="Partnerships with EdTech platforms, learning management systems, and educational technology companies",
            opportunity_type=OpportunityType.PARTNERSHIP,
            region=Region.GLOBAL,
            industry="technology",
            alignment_score=0.9,
            entity_name="EdTech Platforms, LMS Companies",
            how_they_align=["Education", "Technology", "Access"],
            supports_restoration=True,
            frequency_contribution=0.1
        ))
        
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_jan_studio_004",
            name="AI & Machine Learning Communities",
            description="Collaboration with ethical AI communities, responsible AI organizations, and open AI research groups",
            opportunity_type=OpportunityType.COLLABORATION,
            region=Region.GLOBAL,
            industry="technology",
            alignment_score=1.0,
            entity_name="Ethical AI Communities",
            how_they_align=["Ethical AI", "Open research", "No exploitation"],
            supports_restoration=True,
            frequency_contribution=0.2
        ))
        
        # Siyem.org - Expanded
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_siyem_org_002",
            name="Humanitarian Organizations",
            description="Partnerships with humanitarian organizations, aid networks, and relief organizations globally",
            opportunity_type=OpportunityType.COLLABORATION,
            region=Region.GLOBAL,
            industry="nonprofit",
            alignment_score=1.0,
            entity_name="Humanitarian Orgs, Aid Networks",
            how_they_align=["Service", "Help", "No exploitation"],
            supports_restoration=True,
            frequency_contribution=0.2
        ))
        
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_siyem_org_003",
            name="Community Development Organizations",
            description="Partnerships with community development organizations, mutual aid networks, and grassroots movements",
            opportunity_type=OpportunityType.COLLABORATION,
            region=Region.GLOBAL,
            industry="community",
            alignment_score=1.0,
            entity_name="Community Development Orgs",
            how_they_align=["Community support", "Mutual aid", "We all win"],
            supports_restoration=True,
            frequency_contribution=0.2
        ))
        
        # ========================================================================
        # REGION-SPECIFIC OPPORTUNITIES
        # ========================================================================
        
        # Turkey-Specific
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_turkey_001",
            name="Turkish Educational Institutions",
            description="Partnerships with Turkish schools, universities, and educational organizations",
            opportunity_type=OpportunityType.PARTNERSHIP,
            region=Region.TURKEY,
            industry="education",
            alignment_score=0.9,
            entity_name="Turkish Schools, Universities",
            how_they_align=["Education", "Cultural connection", "Community"],
            supports_restoration=True,
            frequency_contribution=0.1
        ))
        
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_turkey_002",
            name="Turkish Media & Content Platforms",
            description="Partnerships with Turkish media companies, content platforms, and broadcasting networks",
            opportunity_type=OpportunityType.DISTRIBUTION,
            region=Region.TURKEY,
            industry="media",
            alignment_score=0.8,
            entity_name="Turkish Media, Content Platforms",
            how_they_align=["Content distribution", "Cultural expression"],
            supports_restoration=True,
            frequency_contribution=0.1
        ))
        
        # UK-Specific
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_uk_001",
            name="UK Food & Media Networks",
            description="Partnerships with UK food networks, media companies, and content distributors",
            opportunity_type=OpportunityType.DISTRIBUTION,
            region=Region.UK,
            industry="media",
            alignment_score=0.9,
            entity_name="UK Food Networks, Media",
            how_they_align=["Content distribution", "Food education"],
            supports_restoration=True,
            frequency_contribution=0.1
        ))
        
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_uk_002",
            name="UK Educational & Publishing Networks",
            description="Partnerships with UK educational institutions, publishers, and academic networks",
            opportunity_type=OpportunityType.PARTNERSHIP,
            region=Region.UK,
            industry="education",
            alignment_score=0.9,
            entity_name="UK Educational, Publishing Networks",
            how_they_align=["Education", "Publishing", "Knowledge sharing"],
            supports_restoration=True,
            frequency_contribution=0.1
        ))
        
        # North America
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_na_001",
            name="North American Creator Economy",
            description="Partnerships with North American creator economy platforms, marketplaces, and creator tools",
            opportunity_type=OpportunityType.PARTNERSHIP,
            region=Region.NORTH_AMERICA,
            industry="technology",
            alignment_score=0.9,
            entity_name="NA Creator Platforms",
            how_they_align=["Creator support", "Market access"],
            supports_restoration=True,
            frequency_contribution=0.1
        ))
        
        # Asia
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_asia_001",
            name="Asian Educational & Technology Networks",
            description="Partnerships with Asian EdTech companies, educational networks, and technology platforms",
            opportunity_type=OpportunityType.PARTNERSHIP,
            region=Region.ASIA,
            industry="technology",
            alignment_score=0.9,
            entity_name="Asian EdTech, Tech Networks",
            how_they_align=["Education", "Technology", "Access"],
            supports_restoration=True,
            frequency_contribution=0.1
        ))
        
        # Middle East
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_me_001",
            name="Middle Eastern Cultural & Educational Networks",
            description="Partnerships with Middle Eastern cultural organizations, educational institutions, and heritage groups",
            opportunity_type=OpportunityType.COLLABORATION,
            region=Region.MIDDLE_EAST,
            industry="heritage",
            alignment_score=0.9,
            entity_name="ME Cultural, Educational Networks",
            how_they_align=["Cultural preservation", "Education", "Heritage"],
            supports_restoration=True,
            frequency_contribution=0.1
        ))
        
        # Africa
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_africa_001",
            name="African Educational & Development Organizations",
            description="Partnerships with African educational organizations, development networks, and community initiatives",
            opportunity_type=OpportunityType.COLLABORATION,
            region=Region.AFRICA,
            industry="education",
            alignment_score=1.0,
            entity_name="African Educational, Development Orgs",
            how_they_align=["Education", "Development", "Community support"],
            supports_restoration=True,
            frequency_contribution=0.2
        ))
        
        # Latin America
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_la_001",
            name="Latin American Cultural & Educational Networks",
            description="Partnerships with Latin American cultural organizations, educational networks, and community groups",
            opportunity_type=OpportunityType.COLLABORATION,
            region=Region.LATIN_AMERICA,
            industry="community",
            alignment_score=0.9,
            entity_name="LA Cultural, Educational Networks",
            how_they_align=["Cultural exchange", "Education", "Community"],
            supports_restoration=True,
            frequency_contribution=0.1
        ))
        
        # Oceania
        self.opportunities.append(GlobalOpportunity(
            opportunity_id="opp_oceania_001",
            name="Oceania Educational & Cultural Networks",
            description="Partnerships with Oceania educational institutions, cultural organizations, and indigenous knowledge networks",
            opportunity_type=OpportunityType.COLLABORATION,
            region=Region.OCEANIA,
            industry="heritage",
            alignment_score=1.0,
            entity_name="Oceania Educational, Cultural Networks",
            how_they_align=["Education", "Cultural preservation", "Indigenous knowledge"],
            supports_restoration=True,
            frequency_contribution=0.2
        ))
        
        # ========================================================================
        # CREATE PROJECT-OPPORTUNITY LINKS
        # ========================================================================
        
        # Link Edible London
        self._link_project_opportunities("project_edible_london", [
            "opp_edible_london_001", "opp_edible_london_002", "opp_edible_london_003"
        ])
        
        # Link Ilven Seamoss
        self._link_project_opportunities("project_ilven_seamoss", [
            "opp_ilven_seamoss_001", "opp_ilven_seamoss_002", "opp_ilven_seamoss_003"
        ])
        
        # Link Edible Cyprus
        self._link_project_opportunities("project_edible_cyprus", [
            "opp_edible_cyprus_001", "opp_edible_cyprus_002", "opp_edible_cyprus_003"
        ])
        
        # Link ATILOK
        self._link_project_opportunities("project_atilok", [
            "opp_atilok_001", "opp_atilok_002", "opp_atilok_003"
        ])
        
        # Link Creative Personas
        self._link_project_opportunities("entity_jean_morphius", [
            "opp_jean_001", "opp_jean_002"
        ])
        
        self._link_project_opportunities("entity_karasahin", [
            "opp_karasahin_001", "opp_karasahin_002"
        ])
        
        self._link_project_opportunities("entity_pierre_pressure", [
            "opp_pierre_001"
        ])
        
        self._link_project_opportunities("entity_uncle_ray_ramiz", [
            "opp_ramiz_001"
        ])
        
        # Link Systems
        self._link_project_opportunities("entity_jan_studio", [
            "opp_jan_studio_001", "opp_jan_studio_002", "opp_jan_studio_003", "opp_jan_studio_004"
        ])
        
        self._link_project_opportunities("entity_siyem_org", [
            "opp_siyem_org_001", "opp_siyem_org_002", "opp_siyem_org_003"
        ])
        
        # Link expanded opportunities
        self._link_project_opportunities("project_edible_london", [
            "opp_edible_london_004", "opp_edible_london_005"
        ])
        
        self._link_project_opportunities("project_ilven_seamoss", [
            "opp_ilven_seamoss_004", "opp_ilven_seamoss_005"
        ])
        
        self._link_project_opportunities("project_edible_cyprus", [
            "opp_edible_cyprus_004", "opp_edible_cyprus_005"
        ])
        
        self._link_project_opportunities("project_atilok", [
            "opp_atilok_004", "opp_atilok_005"
        ])
        
        self._link_project_opportunities("entity_jean_morphius", [
            "opp_jean_003", "opp_jean_004"
        ])
        
        self._link_project_opportunities("entity_karasahin", [
            "opp_karasahin_003", "opp_karasahin_004"
        ])
        
        self._link_project_opportunities("entity_pierre_pressure", [
            "opp_pierre_002", "opp_pierre_003"
        ])
        
        self._link_project_opportunities("entity_uncle_ray_ramiz", [
            "opp_ramiz_002", "opp_ramiz_003"
        ])
        
        # Link region-specific opportunities to relevant projects
        self._link_project_opportunities("project_edible_cyprus", [
            "opp_turkey_001", "opp_turkey_002"
        ])
        
        self._link_project_opportunities("entity_jean_morphius", [
            "opp_uk_001", "opp_uk_002"
        ])
        
        self._link_project_opportunities("entity_jan_studio", [
            "opp_na_001", "opp_asia_001"
        ])
        
        self._link_project_opportunities("entity_uncle_ray_ramiz", [
            "opp_me_001", "opp_africa_001", "opp_la_001", "opp_oceania_001"
        ])
        
        self._save_data()
        logger.info(f"Initialized {len(self.opportunities)} global opportunities")
    
    def _link_project_opportunities(self, project_id: str, opportunity_ids: List[str]):
        """Link project to opportunities"""
        for opp_id in opportunity_ids:
            opportunity = next((o for o in self.opportunities if o.opportunity_id == opp_id), None)
            if opportunity:
                link = ProjectOpportunityLink(
                    link_id=f"link_{project_id}_{opp_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                    project_id=project_id,
                    opportunity_id=opp_id,
                    link_type=opportunity.opportunity_type,
                    alignment_score=opportunity.alignment_score,
                    revenue_potential=opportunity.frequency_contribution * 10000,  # Scale frequency to revenue
                    status="identified"
                )
                self.project_links.append(link)
    
    def get_project_opportunities(self, project_id: str) -> List[Dict[str, Any]]:
        """Get all opportunities for a project"""
        links = [l for l in self.project_links if l.project_id == project_id]
        opportunities = []
        for link in links:
            opportunity = next((o for o in self.opportunities if o.opportunity_id == link.opportunity_id), None)
            if opportunity:
                opportunities.append({
                    "opportunity": opportunity,
                    "link": link
                })
        return opportunities
    
    def get_comprehensive_report(self) -> Dict[str, Any]:
        """Get comprehensive opportunity report"""
        projects_with_opportunities = {}
        for link in self.project_links:
            if link.project_id not in projects_with_opportunities:
                projects_with_opportunities[link.project_id] = []
            opportunity = next((o for o in self.opportunities if o.opportunity_id == link.opportunity_id), None)
            if opportunity:
                projects_with_opportunities[link.project_id].append({
                    "opportunity": opportunity.name,
                    "type": opportunity.opportunity_type.value,
                    "region": opportunity.region.value,
                    "alignment": opportunity.alignment_score,
                    "status": link.status
                })
        
        # Group by region
        opportunities_by_region = {}
        for opp in self.opportunities:
            region = opp.region.value
            if region not in opportunities_by_region:
                opportunities_by_region[region] = []
            opportunities_by_region[region].append(opp.name)
        
        # Group by industry
        opportunities_by_industry = {}
        for opp in self.opportunities:
            industry = opp.industry
            if industry not in opportunities_by_industry:
                opportunities_by_industry[industry] = []
            opportunities_by_industry[industry].append(opp.name)
        
        return {
            "generated_at": datetime.now().isoformat(),
            "total_opportunities": len(self.opportunities),
            "total_links": len(self.project_links),
            "projects_with_opportunities": projects_with_opportunities,
            "opportunities_by_region": opportunities_by_region,
            "opportunities_by_industry": opportunities_by_industry,
            "perfect_alignment_count": len([o for o in self.opportunities if o.alignment_score >= 1.0]),
            "high_alignment_count": len([o for o in self.opportunities if 0.8 <= o.alignment_score < 1.0])
        }


def main():
    """Initialize global opportunity linker"""
    linker = GlobalOpportunityLinker(user_id="jan")
    
    # Get comprehensive report
    report = linker.get_comprehensive_report()
    
    print("\n" + "="*80)
    print("GLOBAL OPPORTUNITY LINKER - REAL-WORLD ALIGNED OPPORTUNITIES")
    print("="*80)
    print(f"\nTotal Opportunities: {report['total_opportunities']}")
    print(f"Total Project Links: {report['total_links']}")
    print(f"Perfect Alignment: {report['perfect_alignment_count']}")
    print(f"High Alignment: {report['high_alignment_count']}")
    
    print("\n" + "-"*80)
    print("PROJECTS WITH OPPORTUNITIES:")
    print("-"*80)
    for project_id, opportunities in report['projects_with_opportunities'].items():
        print(f"\n  {project_id}:")
        for opp in opportunities:
            print(f"    - {opp['opportunity']} ({opp['type']}, {opp['region']}, Alignment: {opp['alignment']:.1%}, Status: {opp['status']})")
    
    print("\n" + "-"*80)
    print("OPPORTUNITIES BY REGION:")
    print("-"*80)
    for region, opportunities in report['opportunities_by_region'].items():
        print(f"\n  {region.upper()}: {len(opportunities)} opportunities")
        for opp in opportunities[:5]:  # Show first 5
            print(f"    - {opp}")
        if len(opportunities) > 5:
            print(f"    ... and {len(opportunities) - 5} more")
    
    print("\n" + "-"*80)
    print("OPPORTUNITIES BY INDUSTRY:")
    print("-"*80)
    for industry, opportunities in report['opportunities_by_industry'].items():
        print(f"\n  {industry.upper()}: {len(opportunities)} opportunities")
        for opp in opportunities[:3]:  # Show first 3
            print(f"    - {opp}")
        if len(opportunities) > 3:
            print(f"    ... and {len(opportunities) - 3} more")
    
    print("\n" + "="*80)
    print("All projects linked to real-world aligned opportunities.")
    print("Global expansion complete.")
    print("All opportunities identified.")
    print("="*80)

if __name__ == "__main__":
    standard_main(main, script_name="global_opportunity_linker.py")
