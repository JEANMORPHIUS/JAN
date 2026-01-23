"""
HUMANITARIAN PROJECTS REGISTRY
Aligned Humanitarian, Animal Sanctuary, and God's Work Projects

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

INTEGRATED INTO CARE PACKAGE SYSTEM
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class ProjectType(Enum):
    """Types of projects"""
    HUMANITARIAN = "humanitarian"  # Humanitarian aid projects
    ANIMAL_SANCTUARY = "animal_sanctuary"  # Animal rescue and sanctuary
    GODS_WORK = "gods_work"  # Faith-based humanitarian projects
    ALL = "all"  # All project types


class AlignmentLevel(Enum):
    """Alignment with mission"""
    FULLY_ALIGNED = "fully_aligned"  # Fully aligned with mission
    HIGHLY_ALIGNED = "highly_aligned"  # Highly aligned
    MODERATELY_ALIGNED = "moderately_aligned"  # Moderately aligned
    PARTIALLY_ALIGNED = "partially_aligned"  # Partially aligned
    UNKNOWN = "unknown"  # Unknown alignment


@dataclass
class HumanitarianProject:
    """A humanitarian, animal sanctuary, or God's work project"""
    project_id: str
    project_type: ProjectType
    name: str
    organization: str
    description: str
    location: str
    mission_alignment: AlignmentLevel
    alignment_score: float = 0.0  # 0-100
    website: Optional[str] = None
    contact_info: Optional[Dict[str, str]] = None
    focus_areas: List[str] = field(default_factory=list)
    impact_metrics: Dict[str, Any] = field(default_factory=dict)
    funding_needs: Optional[Dict[str, Any]] = None
    how_to_help: List[str] = field(default_factory=list)
    created_date: datetime = field(default_factory=datetime.now)
    last_verified: Optional[datetime] = None
    notes: str = ""
    active: bool = True


class HumanitarianProjectsRegistry:
    """
    Registry of aligned humanitarian, animal sanctuary, and God's work projects.
    
    Integrated from deep web search for global projects aligned with:
    - Stewardship and community
    - Right spirits
    - Love as highest mastery
    - Energy + Love = We All Win
    """
    
    def __init__(self):
        """Initialize humanitarian projects registry"""
        self.projects: Dict[str, HumanitarianProject] = {}
        self.data_dir = Path(__file__).parent.parent.parent / "SIYEM" / "output" / "humanitarian_projects"
        self.data_dir.mkdir(parents=True, exist_ok=True)
        
        # Load projects from web search results
        self._load_web_search_projects()
    
    def _load_web_search_projects(self):
        """Load projects from deep web search results"""
        
        # HUMANITARIAN PROJECTS
        humanitarian_projects = [
            {
                "project_id": "UNICEF_2026",
                "project_type": ProjectType.HUMANITARIAN,
                "name": "UNICEF Humanitarian Action for Children 2026",
                "organization": "UNICEF",
                "description": "Reaching 73 million children across 133 countries with $7.66 billion appeal. Focus on hyper-prioritization, strengthening child rights, resilience of systems, working through national governments and local partners.",
                "location": "Global - 133 countries",
                "mission_alignment": AlignmentLevel.FULLY_ALIGNED,
                "alignment_score": 95.0,
                "website": "https://www.unicef.org",
                "focus_areas": ["nutrition", "education", "protection", "health", "WASH"],
                "impact_metrics": {
                    "target_children": 73000000,
                    "countries": 133,
                    "budget": 7660000000
                },
                "how_to_help": [
                    "Donate through UNICEF website",
                    "Volunteer in local chapters",
                    "Advocate for child rights",
                    "Support local partnerships"
                ]
            },
            {
                "project_id": "SAVE_CHILDREN_2026",
                "project_type": ProjectType.HUMANITARIAN,
                "name": "Save the Children Humanitarian Plan 2026",
                "organization": "Save the Children",
                "description": "Reforming Aid, Renewing Hope - Reaching 17.8 million people (10.1 million children) in 45 countries. Focus on shifting power to local actors, efficiency, and principled action.",
                "location": "Global - 45 countries",
                "mission_alignment": AlignmentLevel.FULLY_ALIGNED,
                "alignment_score": 95.0,
                "website": "https://www.savethechildren.net",
                "focus_areas": ["local leadership", "flexible funding", "anticipatory action", "gender-based violence prevention", "psychosocial support"],
                "impact_metrics": {
                    "target_people": 17800000,
                    "target_children": 10100000,
                    "countries": 45,
                    "budget": 687900000
                },
                "how_to_help": [
                    "Support local community-led organizations",
                    "Advocate for flexible funding",
                    "Volunteer in affected communities",
                    "Donate to Save the Children"
                ]
            },
            {
                "project_id": "HAITI_HNRP_2026",
                "project_type": ProjectType.HUMANITARIAN,
                "name": "Haiti Humanitarian Response Plan 2026",
                "organization": "UN OCHA",
                "description": "$880 million budget to assist 4.2 million vulnerable people. Focus on urgent multi-sector interventions, stabilizing households, strengthening essential services.",
                "location": "Haiti",
                "mission_alignment": AlignmentLevel.HIGHLY_ALIGNED,
                "alignment_score": 90.0,
                "website": "https://haiti.un.org",
                "focus_areas": ["multi-sector interventions", "household stabilization", "essential services", "displaced people integration"],
                "impact_metrics": {
                    "target_people": 4200000,
                    "budget": 880000000
                },
                "how_to_help": [
                    "Support UN OCHA Haiti response",
                    "Donate to Haiti relief funds",
                    "Advocate for humanitarian access",
                    "Support local Haitian organizations"
                ]
            }
        ]
        
        # ANIMAL SANCTUARY PROJECTS
        animal_sanctuary_projects = [
            {
                "project_id": "SHELDRICK_WILDLIFE_TRUST",
                "project_type": ProjectType.ANIMAL_SANCTUARY,
                "name": "Sheldrick Wildlife Trust",
                "organization": "Sheldrick Wildlife Trust",
                "description": "Rescuing orphaned elephants and rhinos from poaching and human-wildlife conflict. Operates nursery, rehabilitation, rewilding, and anti-poaching programs in partnership with Kenya Wildlife Service.",
                "location": "Kenya",
                "mission_alignment": AlignmentLevel.FULLY_ALIGNED,
                "alignment_score": 95.0,
                "website": "https://www.sheldrickwildlifetrust.org",
                "focus_areas": ["elephant rescue", "rhino rescue", "rehabilitation", "rewilding", "anti-poaching"],
                "impact_metrics": {
                    "animals_rescued": "hundreds",
                    "rewilding_success_rate": "high"
                },
                "how_to_help": [
                    "Adopt an orphan",
                    "Donate to rescue operations",
                    "Support anti-poaching efforts",
                    "Volunteer at sanctuary"
                ]
            },
            {
                "project_id": "CHIMFUNSHI_WILDLIFE",
                "project_type": ProjectType.ANIMAL_SANCTUARY,
                "name": "Chimfunshi Wildlife Orphanage",
                "organization": "Chimfunshi Wildlife Orphanage",
                "description": "One of the world's oldest and largest chimpanzee sanctuaries, founded in 1983. Focus on rescue, rehabilitation, semi-free-range care, research, and education.",
                "location": "Zambia",
                "mission_alignment": AlignmentLevel.FULLY_ALIGNED,
                "alignment_score": 95.0,
                "website": "https://www.chimfunshi.org",
                "focus_areas": ["chimpanzee rescue", "rehabilitation", "semi-free-range care", "research", "education"],
                "impact_metrics": {
                    "years_operating": 40,
                    "chimpanzees_cared_for": "hundreds"
                },
                "how_to_help": [
                    "Donate to sanctuary operations",
                    "Support research programs",
                    "Volunteer at sanctuary",
                    "Sponsor a chimpanzee"
                ]
            },
            {
                "project_id": "TSAVO_WEST_RHINO",
                "project_type": ProjectType.ANIMAL_SANCTUARY,
                "name": "Tsavo West Rhino Sanctuary",
                "organization": "Kenya Wildlife Service",
                "description": "740,000 acres sanctuary formalized in 2025, enhancing rhino protection with expanded range and ranger capacity.",
                "location": "Kenya - Tsavo West",
                "mission_alignment": AlignmentLevel.HIGHLY_ALIGNED,
                "alignment_score": 90.0,
                "website": "https://www.kws.go.ke",
                "focus_areas": ["rhino protection", "habitat expansion", "ranger capacity"],
                "impact_metrics": {
                    "area_acres": 740000,
                    "established": 2025
                },
                "how_to_help": [
                    "Support Kenya Wildlife Service",
                    "Donate to rhino protection",
                    "Advocate for wildlife conservation",
                    "Support ranger programs"
                ]
            },
            {
                "project_id": "BONORONG_WILDLIFE",
                "project_type": ProjectType.ANIMAL_SANCTUARY,
                "name": "Bonorong Wildlife Sanctuary",
                "organization": "Bonorong Wildlife Sanctuary",
                "description": "Handles nearly 20,000 animal rescues annually. Recently expanded with $4 million Wildlife Hospital & Rehab Facility. Focused on education and preventative programs alongside rescue.",
                "location": "Tasmania, Australia",
                "mission_alignment": AlignmentLevel.FULLY_ALIGNED,
                "alignment_score": 95.0,
                "website": "https://www.bonorong.com.au",
                "focus_areas": ["animal rescue", "wildlife hospital", "rehabilitation", "education", "preventative programs"],
                "impact_metrics": {
                    "rescues_annually": 20000,
                    "facility_expansion": 4000000
                },
                "how_to_help": [
                    "Donate to wildlife hospital",
                    "Volunteer at sanctuary",
                    "Support education programs",
                    "Adopt an animal"
                ]
            }
        ]
        
        # GOD'S WORK PROJECTS
        gods_work_projects = [
            {
                "project_id": "GODS_WORK_INTERNATIONAL",
                "project_type": ProjectType.GODS_WORK,
                "name": "God's Work International",
                "organization": "God's Work International",
                "description": "Hygiene and period-poverty programs for girls, mentorship for both girls and boys, supporting elderly populations with essentials like food, medical support, and dignified social connection.",
                "location": "Kenya - Murang'a County",
                "mission_alignment": AlignmentLevel.FULLY_ALIGNED,
                "alignment_score": 100.0,
                "website": "https://godsworkinternational.org",
                "focus_areas": ["hygiene programs", "period-poverty", "mentorship", "elderly care", "dignity"],
                "impact_metrics": {
                    "schools": 56,
                    "girls_reached": 1140,
                    "boys_reached": 400,
                    "founded": 2023
                },
                "how_to_help": [
                    "Donate to programs",
                    "Support mentorship initiatives",
                    "Volunteer in Kenya",
                    "Sponsor a school program"
                ]
            },
            {
                "project_id": "CHURCH_WOMEN_CHILDREN_HEALTH",
                "project_type": ProjectType.GODS_WORK,
                "name": "Church-Led Global Initiative for Women & Children's Health",
                "organization": "The Church of Jesus Christ of Latter-day Saints",
                "description": "21.2 million children and mothers received vitamins; 1.87 million children screened and treated for malnutrition; nearly 2 million health workers and caregivers trained. $55.8 million investment.",
                "location": "Global - 12 countries (Bangladesh, Kenya, Nepal, Philippines, Zambia, etc.)",
                "mission_alignment": AlignmentLevel.FULLY_ALIGNED,
                "alignment_score": 95.0,
                "website": "https://www.churchofjesuschrist.org",
                "focus_areas": ["maternal health", "child nutrition", "health worker training", "vitamin distribution"],
                "impact_metrics": {
                    "children_mothers_reached": 21200000,
                    "children_screened": 1870000,
                    "health_workers_trained": 2000000,
                    "investment": 55800000,
                    "countries": 12
                },
                "how_to_help": [
                    "Support church humanitarian efforts",
                    "Donate to global health initiatives",
                    "Volunteer in health programs",
                    "Advocate for maternal and child health"
                ]
            },
            {
                "project_id": "GOD_SAID_GO_MISSIONS",
                "project_type": ProjectType.GODS_WORK,
                "name": "Centro Médico Vida Plena",
                "organization": "God Said Go Missions",
                "description": "Launching in 2026 in Escuintla, Guatemala. Aiming for sustainable healthcare access and village ministry support.",
                "location": "Guatemala - Escuintla",
                "mission_alignment": AlignmentLevel.FULLY_ALIGNED,
                "alignment_score": 95.0,
                "website": "https://godsaidgo.org",
                "focus_areas": ["sustainable healthcare", "village ministry", "community health"],
                "impact_metrics": {
                    "launch_year": 2026,
                    "location": "Escuintla, Guatemala"
                },
                "how_to_help": [
                    "Support mission launch",
                    "Donate to healthcare center",
                    "Volunteer in Guatemala",
                    "Support village ministry"
                ]
            },
            {
                "project_id": "EPISCOPAL_RELIEF_DEVELOPMENT",
                "project_type": ProjectType.GODS_WORK,
                "name": "Episcopal Relief & Development Toolkits",
                "organization": "Episcopal Relief & Development",
                "description": "Four toolkits launched in August 2025: Early Childhood Development, Women & Girls, Climate Resilience, and Disaster Response. Includes sermon starters, action templates, and equity-oriented study materials.",
                "location": "Global",
                "mission_alignment": AlignmentLevel.HIGHLY_ALIGNED,
                "alignment_score": 90.0,
                "website": "https://www.episcopalrelief.org",
                "focus_areas": ["early childhood development", "women and girls", "climate resilience", "disaster response"],
                "impact_metrics": {
                    "toolkits": 4,
                    "launched": "August 2025"
                },
                "how_to_help": [
                    "Use toolkits in faith communities",
                    "Support Episcopal Relief & Development",
                    "Advocate for equity-oriented action",
                    "Share resources with communities"
                ]
            }
        ]
        
        # Register all projects
        all_projects = humanitarian_projects + animal_sanctuary_projects + gods_work_projects
        
        for project_data in all_projects:
            project = HumanitarianProject(**project_data)
            self.projects[project.project_id] = project
        
        logger.info(f"Loaded {len(self.projects)} humanitarian projects from web search")
    
    def get_projects(
        self,
        project_type: Optional[ProjectType] = None,
        alignment_level: Optional[AlignmentLevel] = None,
        active_only: bool = True
    ) -> List[HumanitarianProject]:
        """Get projects with filters"""
        projects = list(self.projects.values())
        
        if project_type and project_type != ProjectType.ALL:
            projects = [p for p in projects if p.project_type == project_type]
        
        if alignment_level:
            projects = [p for p in projects if p.mission_alignment == alignment_level]
        
        if active_only:
            projects = [p for p in projects if p.active]
        
        return sorted(projects, key=lambda x: x.alignment_score, reverse=True)
    
    def get_project(self, project_id: str) -> Optional[HumanitarianProject]:
        """Get a specific project"""
        return self.projects.get(project_id)
    
    def register_project(self, project: HumanitarianProject):
        """Register a new project"""
        self.projects[project.project_id] = project
        logger.info(f"Registered project: {project.name}")
    
    def get_summary(self) -> Dict[str, Any]:
        """Get registry summary"""
        total = len(self.projects)
        by_type = {
            ProjectType.HUMANITARIAN.value: len([p for p in self.projects.values() if p.project_type == ProjectType.HUMANITARIAN]),
            ProjectType.ANIMAL_SANCTUARY.value: len([p for p in self.projects.values() if p.project_type == ProjectType.ANIMAL_SANCTUARY]),
            ProjectType.GODS_WORK.value: len([p for p in self.projects.values() if p.project_type == ProjectType.GODS_WORK])
        }
        
        fully_aligned = len([p for p in self.projects.values() if p.mission_alignment == AlignmentLevel.FULLY_ALIGNED])
        
        return {
            "total_projects": total,
            "by_type": by_type,
            "fully_aligned": fully_aligned,
            "message": "Humanitarian, animal sanctuary, and God's work projects integrated into care package system"
        }


# Global instance
_registry: Optional[HumanitarianProjectsRegistry] = None


def get_humanitarian_projects_registry() -> HumanitarianProjectsRegistry:
    """Get the global humanitarian projects registry instance"""
    global _registry
    if _registry is None:
        _registry = HumanitarianProjectsRegistry()
    return _registry
