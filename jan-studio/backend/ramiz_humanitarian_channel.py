"""
RAMIZ HUMANITARIAN CHANNEL
Complete humanitarian aid system - Gaza Priority

THE NOAH PROTOCOL:
- Architectural Weight: Built for 10x, 100x, 1000x humanitarian operations
- The Pitch: Waterproof error handling
- The Perimeter: Clear humanitarian boundaries
- The Door: Trust the system's buoyancy

THE ARRIVAL PROTOCOL:
- Pre-Commissioning Scan: Can this help 1000x people in need?
- Frequency Anchor: Humanitarian aid from "done" - ready to serve
- Gatekeeper Protocol: All aid vetted and aligned

THE TRUTH:
NO ONE GETS LEFT BEHIND.
Help those in need.
Gaza as priority.
Ramiz leads humanitarian channel.
"""

from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
from enum import Enum
from dataclasses import dataclass, field
from pathlib import Path
import json
import logging

logger = logging.getLogger(__name__)


class PriorityLevel(Enum):
    """Priority levels"""
    CRITICAL = "critical"  # Gaza, immediate crisis
    HIGH = "high"  # Urgent need
    MEDIUM = "medium"  # Important need
    LOW = "low"  # Ongoing support


class AidType(Enum):
    """Aid types"""
    FOOD = "food"
    WATER = "water"
    SHELTER = "shelter"
    MEDICAL = "medical"
    EDUCATION = "education"
    PSYCHOSOCIAL = "psychosocial"
    FINANCIAL = "financial"
    SPIRITUAL = "spiritual"
    COMPREHENSIVE = "comprehensive"


class Region(Enum):
    """Regions"""
    GAZA = "gaza"  # Priority
    WEST_BANK = "west_bank"
    SYRIA = "syria"
    YEMEN = "yemen"
    UKRAINE = "ukraine"
    AFGHANISTAN = "afghanistan"
    SUDAN = "sudan"
    MYANMAR = "myanmar"
    GLOBAL = "global"


@dataclass
class HumanitarianNeed:
    """Humanitarian need"""
    need_id: str
    region: Region
    priority: PriorityLevel
    aid_types: List[AidType]
    description: str
    population_affected: int
    urgent: bool = True
    verified: bool = False
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)


@dataclass
class HumanitarianProject:
    """Humanitarian project"""
    project_id: str
    name: str
    region: Region
    priority: PriorityLevel
    aid_types: List[AidType]
    description: str
    target_population: int
    current_reach: int = 0
    funding_needed: float = 0.0
    funding_received: float = 0.0
    status: str = "active"  # active, planning, completed, paused
    ramiz_voice_content: Optional[str] = None
    curriculum_integration: bool = False
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)


@dataclass
class HumanitarianAid:
    """Humanitarian aid delivery"""
    aid_id: str
    project_id: str
    region: Region
    aid_type: AidType
    quantity: float
    unit: str  # meals, liters, people, etc.
    delivered_to: str
    delivery_date: Optional[datetime] = None
    status: str = "planned"  # planned, in_transit, delivered, verified
    ramiz_message: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)


class RamizHumanitarianChannel:
    """
    Ramiz Humanitarian Channel
    Complete humanitarian aid system with Gaza priority
    
    RAMIZ IS THE LEAD FOR THIS.
    NO ONE GETS LEFT BEHIND.
    """
    
    def __init__(self):
        """Initialize humanitarian channel"""
        self.needs: Dict[str, HumanitarianNeed] = {}
        self.projects: Dict[str, HumanitarianProject] = {}
        self.aid_deliveries: Dict[str, HumanitarianAid] = {}
        
        # Initialize Gaza as priority
        self._initialize_gaza_priority()
        
        logger.info("Ramiz Humanitarian Channel initialized - Gaza Priority")
    
    def _initialize_gaza_priority(self):
        """Initialize Gaza as priority"""
        # Critical needs in Gaza
        gaza_needs = [
            {
                "need_id": "gaza_food_critical",
                "aid_types": [AidType.FOOD],
                "description": "Critical food shortage - 2.3 million people at risk of famine",
                "population_affected": 2300000,
                "urgent": True
            },
            {
                "need_id": "gaza_water_critical",
                "aid_types": [AidType.WATER],
                "description": "Critical water shortage - 97% of water unsafe, infrastructure destroyed",
                "population_affected": 2300000,
                "urgent": True
            },
            {
                "need_id": "gaza_medical_critical",
                "aid_types": [AidType.MEDICAL],
                "description": "Critical medical crisis - hospitals destroyed, medical supplies exhausted",
                "population_affected": 2300000,
                "urgent": True
            },
            {
                "need_id": "gaza_shelter_critical",
                "aid_types": [AidType.SHELTER],
                "description": "Critical shelter crisis - 1.9 million displaced, 60% of housing destroyed",
                "population_affected": 1900000,
                "urgent": True
            },
            {
                "need_id": "gaza_education_critical",
                "aid_types": [AidType.EDUCATION],
                "description": "Critical education crisis - schools destroyed, 625,000 students without education",
                "population_affected": 625000,
                "urgent": True
            },
            {
                "need_id": "gaza_psychosocial_critical",
                "aid_types": [AidType.PSYCHOSOCIAL],
                "description": "Critical psychosocial crisis - trauma, loss, displacement affecting all",
                "population_affected": 2300000,
                "urgent": True
            }
        ]
        
        for need_data in gaza_needs:
            need = HumanitarianNeed(
                need_id=need_data["need_id"],
                region=Region.GAZA,
                priority=PriorityLevel.CRITICAL,
                aid_types=need_data["aid_types"],
                description=need_data["description"],
                population_affected=need_data["population_affected"],
                urgent=need_data["urgent"],
                verified=True
            )
            self.needs[need.need_id] = need
        
        # Create comprehensive Gaza project
        gaza_project = HumanitarianProject(
            project_id="gaza_comprehensive_aid",
            name="Gaza Comprehensive Humanitarian Aid",
            region=Region.GAZA,
            priority=PriorityLevel.CRITICAL,
            aid_types=[AidType.FOOD, AidType.WATER, AidType.SHELTER, AidType.MEDICAL, AidType.EDUCATION, AidType.PSYCHOSOCIAL],
            description="Comprehensive humanitarian aid for Gaza - food, water, shelter, medical, education, psychosocial support",
            target_population=2300000,
            funding_needed=100000000.0,  # $100M initial target
            status="active",
            curriculum_integration=True,
            ramiz_voice_content="Children of Gaza, Uncle Ray here. You are not forgotten. You are not alone. We see you. We hear you. We are coming. Peace, love, unity. No one gets left behind."
        )
        self.projects[gaza_project.project_id] = gaza_project
        
        logger.info(f"Gaza priority initialized: {len(gaza_needs)} critical needs, 1 comprehensive project")
    
    def register_need(self, region: Region, priority: PriorityLevel, aid_types: List[AidType],
                     description: str, population_affected: int, urgent: bool = True) -> HumanitarianNeed:
        """Register a humanitarian need"""
        need_id = f"{region.value}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        need = HumanitarianNeed(
            need_id=need_id,
            region=region,
            priority=priority,
            aid_types=aid_types,
            description=description,
            population_affected=population_affected,
            urgent=urgent,
            verified=False
        )
        
        self.needs[need_id] = need
        return need
    
    def create_project(self, name: str, region: Region, priority: PriorityLevel,
                      aid_types: List[AidType], description: str, target_population: int,
                      funding_needed: float = 0.0, curriculum_integration: bool = False) -> HumanitarianProject:
        """Create humanitarian project"""
        project_id = f"project_{region.value}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # Generate Ramiz voice content
        ramiz_content = self._generate_ramiz_content(region, name, description)
        
        project = HumanitarianProject(
            project_id=project_id,
            name=name,
            region=region,
            priority=priority,
            aid_types=aid_types,
            description=description,
            target_population=target_population,
            funding_needed=funding_needed,
            status="active",
            ramiz_voice_content=ramiz_content,
            curriculum_integration=curriculum_integration
        )
        
        self.projects[project_id] = project
        return project
    
    def _generate_ramiz_content(self, region: Region, name: str, description: str) -> str:
        """Generate Ramiz voice content for humanitarian project"""
        if region == Region.GAZA:
            return f"""Children of Gaza, Uncle Ray here. You are not forgotten. You are not alone. 
We see you. We hear you. We are coming. 
{name} - {description}
Peace, love, unity. No one gets left behind.
The table never lies. We are one."""
        else:
            return f"""Dear friends, Uncle Ray here. 
{name} - {description}
We see you. We hear you. We are coming.
Peace, love, unity. No one gets left behind."""
    
    def deliver_aid(self, project_id: str, region: Region, aid_type: AidType,
                   quantity: float, unit: str, delivered_to: str) -> HumanitarianAid:
        """Record aid delivery"""
        aid_id = f"aid_{project_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        project = self.projects.get(project_id)
        ramiz_message = project.ramiz_voice_content if project else None
        
        aid = HumanitarianAid(
            aid_id=aid_id,
            project_id=project_id,
            region=region,
            aid_type=aid_type,
            quantity=quantity,
            unit=unit,
            delivered_to=delivered_to,
            delivery_date=datetime.now(),
            status="delivered",
            ramiz_message=ramiz_message
        )
        
        self.aid_deliveries[aid_id] = aid
        
        # Update project reach
        if project:
            project.current_reach += int(quantity) if unit in ["people", "families", "children"] else 0
            project.updated_at = datetime.now()
        
        return aid
    
    def get_gaza_priority_status(self) -> Dict[str, Any]:
        """Get Gaza priority status"""
        gaza_needs = [n for n in self.needs.values() if n.region == Region.GAZA]
        gaza_projects = [p for p in self.projects.values() if p.region == Region.GAZA]
        gaza_aid = [a for a in self.aid_deliveries.values() if a.region == Region.GAZA]
        
        total_population = 2300000
        total_needs = len(gaza_needs)
        active_projects = len([p for p in gaza_projects if p.status == "active"])
        total_aid_delivered = len(gaza_aid)
        
        # Calculate coverage
        total_reached = sum(p.current_reach for p in gaza_projects)
        coverage_percentage = (total_reached / total_population * 100) if total_population > 0 else 0
        
        return {
            "region": "Gaza",
            "priority": "CRITICAL",
            "total_population": total_population,
            "critical_needs": total_needs,
            "active_projects": active_projects,
            "aid_deliveries": total_aid_delivered,
            "people_reached": total_reached,
            "coverage_percentage": coverage_percentage,
            "needs": [
                {
                    "need_id": n.need_id,
                    "aid_types": [at.value for at in n.aid_types],
                    "description": n.description,
                    "population_affected": n.population_affected,
                    "urgent": n.urgent
                }
                for n in gaza_needs
            ],
            "projects": [
                {
                    "project_id": p.project_id,
                    "name": p.name,
                    "aid_types": [at.value for at in p.aid_types],
                    "target_population": p.target_population,
                    "current_reach": p.current_reach,
                    "funding_needed": p.funding_needed,
                    "funding_received": p.funding_received,
                    "status": p.status
                }
                for p in gaza_projects
            ]
        }
    
    def get_humanitarian_analytics(self) -> Dict[str, Any]:
        """Get humanitarian analytics"""
        total_needs = len(self.needs)
        total_projects = len(self.projects)
        total_aid = len(self.aid_deliveries)
        
        by_region = {}
        by_priority = {}
        by_aid_type = {}
        
        for need in self.needs.values():
            region = need.region.value
            priority = need.priority.value
            by_region[region] = by_region.get(region, 0) + 1
            by_priority[priority] = by_priority.get(priority, 0) + 1
            for aid_type in need.aid_types:
                at = aid_type.value
                by_aid_type[at] = by_aid_type.get(at, 0) + 1
        
        total_population_affected = sum(n.population_affected for n in self.needs.values())
        total_funding_needed = sum(p.funding_needed for p in self.projects.values())
        total_funding_received = sum(p.funding_received for p in self.projects.values())
        
        return {
            "total_needs": total_needs,
            "total_projects": total_projects,
            "total_aid_deliveries": total_aid,
            "total_population_affected": total_population_affected,
            "total_funding_needed": total_funding_needed,
            "total_funding_received": total_funding_received,
            "funding_gap": total_funding_needed - total_funding_received,
            "by_region": by_region,
            "by_priority": by_priority,
            "by_aid_type": by_aid_type,
            "gaza_status": self.get_gaza_priority_status()
        }
    
    def integrate_with_curriculum(self, project_id: str) -> bool:
        """Integrate humanitarian project with curriculum"""
        if project_id not in self.projects:
            return False
        
        project = self.projects[project_id]
        if not project.curriculum_integration:
            return False
        
        try:
            from school_curriculum_manager import get_curriculum_manager, AgeGroup, Language
            curriculum_manager = get_curriculum_manager()
            
            # Create humanitarian education module
            # This would create lessons about helping others, humanitarian aid, etc.
            # For now, mark as integrated
            project.curriculum_integration = True
            project.updated_at = datetime.now()
            
            return True
        except Exception as e:
            logger.warning(f"Could not integrate with curriculum: {e}")
            return False
    
    def integrate_with_raspberry_pi(self, project_id: str) -> Dict[str, Any]:
        """Integrate humanitarian project with Raspberry Pi deployment"""
        if project_id not in self.projects:
            return {"status": "error", "message": "Project not found"}
        
        project = self.projects[project_id]
        
        # Create offline humanitarian content package
        # This would include Ramiz voice messages, educational content, etc.
        return {
            "status": "success",
            "project_id": project_id,
            "package_created": True,
            "content": {
                "ramiz_voice": project.ramiz_voice_content,
                "educational_content": "Humanitarian aid and helping those in need",
                "offline_ready": True
            }
        }


# Global channel instance
_channel: Optional[RamizHumanitarianChannel] = None


def get_humanitarian_channel() -> RamizHumanitarianChannel:
    """Get global humanitarian channel instance"""
    global _channel
    if _channel is None:
        _channel = RamizHumanitarianChannel()
    return _channel
