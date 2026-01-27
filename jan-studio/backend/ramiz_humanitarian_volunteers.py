"""
RAMIZ HUMANITARIAN VOLUNTEER COORDINATION
Volunteer management, coordination, deployment

THE NOAH PROTOCOL:
- Architectural Weight: Built for 10x, 100x, 1000x volunteers
- The Pitch: Waterproof error handling
- The Perimeter: Clear volunteer boundaries

THE TRUTH:
NO ONE GETS LEFT BEHIND.
Gaza as priority.
Volunteers are the heart of humanitarian work.
"""

from typing import Dict, List, Any, Optional
from datetime import datetime
from enum import Enum
from dataclasses import dataclass, field
import logging

logger = logging.getLogger(__name__)


class VolunteerStatus(Enum):
    """Volunteer status"""
    REGISTERED = "registered"
    ACTIVE = "active"
    DEPLOYED = "deployed"
    ON_HOLD = "on_hold"
    INACTIVE = "inactive"


class VolunteerSkill(Enum):
    """Volunteer skills"""
    MEDICAL = "medical"
    LOGISTICS = "logistics"
    EDUCATION = "education"
    PSYCHOSOCIAL = "psychosocial"
    TRANSLATION = "translation"
    ADMINISTRATION = "administration"
    FUNDRAISING = "fundraising"
    COMMUNICATION = "communication"
    CONSTRUCTION = "construction"
    COOKING = "cooking"
    DISTRIBUTION = "distribution"
    OTHER = "other"


class DeploymentStatus(Enum):
    """Deployment status"""
    PLANNED = "planned"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


@dataclass
class Volunteer:
    """Volunteer record"""
    volunteer_id: str
    name: str
    email: str
    phone: Optional[str] = None
    location: Optional[str] = None
    skills: List[VolunteerSkill] = field(default_factory=list)
    languages: List[str] = field(default_factory=list)
    status: VolunteerStatus = VolunteerStatus.REGISTERED
    gaza_priority: bool = False  # Priority for Gaza deployment
    availability_start: Optional[datetime] = None
    availability_end: Optional[datetime] = None
    notes: str = ""
    created_at: datetime = field(default_factory=datetime.now)
    last_active: Optional[datetime] = None


@dataclass
class VolunteerDeployment:
    """Volunteer deployment"""
    deployment_id: str
    project_id: str
    volunteer_id: str
    role: str
    start_date: datetime
    end_date: Optional[datetime] = None
    status: DeploymentStatus = DeploymentStatus.PLANNED
    location: Optional[str] = None
    notes: str = ""
    created_at: datetime = field(default_factory=datetime.now)


class RamizHumanitarianVolunteers:
    """
    Ramiz Humanitarian Volunteer Coordination
    Manages volunteers, deployments, coordination
    
    Volunteers are the heart of humanitarian work.
    """
    
    def __init__(self):
        """Initialize volunteer system"""
        self.volunteers: Dict[str, Volunteer] = {}
        self.deployments: Dict[str, VolunteerDeployment] = {}
        self.gaza_volunteers: List[str] = []  # volunteer_ids for Gaza priority
        
        logger.info("Ramiz Humanitarian Volunteer Coordination initialized")
    
    def register_volunteer(self, name: str, email: str, phone: Optional[str] = None,
                          location: Optional[str] = None, skills: List[str] = None,
                          languages: List[str] = None, gaza_priority: bool = False,
                          availability_start: Optional[datetime] = None,
                          availability_end: Optional[datetime] = None,
                          notes: str = "") -> Volunteer:
        """Register volunteer"""
        volunteer_id = f"volunteer_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # Parse skills
        skill_enums = []
        if skills:
            for skill_str in skills:
                try:
                    skill_enums.append(VolunteerSkill(skill_str.lower()))
                except ValueError:
                    pass
        
        volunteer = Volunteer(
            volunteer_id=volunteer_id,
            name=name,
            email=email,
            phone=phone,
            location=location,
            skills=skill_enums,
            languages=languages or [],
            status=VolunteerStatus.ACTIVE,
            gaza_priority=gaza_priority,
            availability_start=availability_start,
            availability_end=availability_end,
            notes=notes
        )
        
        self.volunteers[volunteer_id] = volunteer
        
        if gaza_priority:
            if volunteer_id not in self.gaza_volunteers:
                self.gaza_volunteers.append(volunteer_id)
        
        logger.info(f"Volunteer registered: {volunteer_id}, Name: {name}, Gaza Priority: {gaza_priority}")
        
        return volunteer
    
    def deploy_volunteer(self, volunteer_id: str, project_id: str, role: str,
                        start_date: datetime, end_date: Optional[datetime] = None,
                        location: Optional[str] = None, notes: str = "") -> VolunteerDeployment:
        """Deploy volunteer"""
        if volunteer_id not in self.volunteers:
            raise ValueError(f"Volunteer not found: {volunteer_id}")
        
        deployment_id = f"deployment_{project_id}_{volunteer_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        deployment = VolunteerDeployment(
            deployment_id=deployment_id,
            project_id=project_id,
            volunteer_id=volunteer_id,
            role=role,
            start_date=start_date,
            end_date=end_date,
            status=DeploymentStatus.IN_PROGRESS,
            location=location,
            notes=notes
        )
        
        self.deployments[deployment_id] = deployment
        
        # Update volunteer status
        volunteer = self.volunteers[volunteer_id]
        volunteer.status = VolunteerStatus.DEPLOYED
        volunteer.last_active = datetime.now()
        
        logger.info(f"Volunteer deployed: {volunteer_id} to {project_id}, Role: {role}")
        
        return deployment
    
    def get_gaza_volunteers(self) -> List[Dict[str, Any]]:
        """Get Gaza priority volunteers"""
        gaza_vols = []
        for vol_id in self.gaza_volunteers:
            if vol_id in self.volunteers:
                vol = self.volunteers[vol_id]
                gaza_vols.append({
                    "volunteer_id": vol.volunteer_id,
                    "name": vol.name,
                    "skills": [s.value for s in vol.skills],
                    "languages": vol.languages,
                    "status": vol.status.value,
                    "location": vol.location,
                    "available": vol.status in [VolunteerStatus.ACTIVE, VolunteerStatus.REGISTERED]
                })
        
        return gaza_vols
    
    def get_volunteer_analytics(self) -> Dict[str, Any]:
        """Get volunteer analytics"""
        total_volunteers = len(self.volunteers)
        active_volunteers = len([v for v in self.volunteers.values() if v.status == VolunteerStatus.ACTIVE])
        deployed_volunteers = len([v for v in self.volunteers.values() if v.status == VolunteerStatus.DEPLOYED])
        gaza_volunteers = len(self.gaza_volunteers)
        
        by_skill = {}
        by_status = {}
        
        for volunteer in self.volunteers.values():
            for skill in volunteer.skills:
                skill_val = skill.value
                by_skill[skill_val] = by_skill.get(skill_val, 0) + 1
            
            status = volunteer.status.value
            by_status[status] = by_status.get(status, 0) + 1
        
        active_deployments = len([d for d in self.deployments.values() 
                                 if d.status == DeploymentStatus.IN_PROGRESS])
        
        return {
            "total_volunteers": total_volunteers,
            "active_volunteers": active_volunteers,
            "deployed_volunteers": deployed_volunteers,
            "gaza_volunteers": gaza_volunteers,
            "active_deployments": active_deployments,
            "by_skill": by_skill,
            "by_status": by_status,
            "total_deployments": len(self.deployments)
        }


# Global volunteer instance
_volunteers: Optional[RamizHumanitarianVolunteers] = None


def get_humanitarian_volunteers() -> RamizHumanitarianVolunteers:
    """Get global humanitarian volunteers instance"""
    global _volunteers
    if _volunteers is None:
        _volunteers = RamizHumanitarianVolunteers()
    return _volunteers
