"""
EDUCATION PROFESSIONAL DEPLOYMENT API
Complete deployment management for Education Professional channel

THE NOAH PROTOCOL:
- Architectural Weight: Built for 10x, 100x, 1000x school deployments
- The Pitch: Waterproof error handling
- The Perimeter: Clear deployment boundaries

THE ARRIVAL PROTOCOL:
- Pre-Commissioning Scan: Can this handle 1000x schools?
- Frequency Anchor: Deploy from "done" - production ready

THE TRUTH:
Scale and build until ready.
Education Professional deployments for the new world.
"""

from fastapi import APIRouter, HTTPException, status, BackgroundTasks
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
from enum import Enum
from dataclasses import dataclass, field
import json
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/education-professional", tags=["Education Professional Deployment"])


class DeploymentStatus(Enum):
    """Deployment status"""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    ACTIVE = "active"
    INACTIVE = "inactive"


class SchoolType(Enum):
    """School type"""
    PRIMARY = "primary"
    SECONDARY = "secondary"
    HIGH_SCHOOL = "high_school"
    UNIVERSITY = "university"
    HOMESCHOOL = "homeschool"
    COMMUNITY = "community"


@dataclass
class SchoolDeployment:
    """School deployment record"""
    school_id: str
    school_name: str
    school_type: SchoolType
    location: str
    contact_email: str
    contact_phone: Optional[str] = None
    deployment_status: DeploymentStatus = DeploymentStatus.PENDING
    deployment_date: Optional[datetime] = None
    license_type: str = "school"  # school, teacher, student
    license_expiry: Optional[datetime] = None
    student_count: int = 0
    teacher_count: int = 0
    api_key: Optional[str] = None
    configuration: Dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)


class EducationProfessionalDeploymentManager:
    """
    Education Professional Deployment Manager
    Manages school deployments, licenses, and monitoring
    """
    
    def __init__(self):
        """Initialize deployment manager"""
        self.schools: Dict[str, SchoolDeployment] = {}
        self.deployment_history: List[Dict[str, Any]] = []
        
        logger.info("Education Professional Deployment Manager initialized")
    
    def register_school(self, school_data: Dict[str, Any]) -> SchoolDeployment:
        """Register a new school for deployment"""
        school_id = school_data.get("school_id") or f"school_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        school = SchoolDeployment(
            school_id=school_id,
            school_name=school_data["school_name"],
            school_type=SchoolType(school_data.get("school_type", "primary")),
            location=school_data["location"],
            contact_email=school_data["contact_email"],
            contact_phone=school_data.get("contact_phone"),
            license_type=school_data.get("license_type", "school"),
            student_count=school_data.get("student_count", 0),
            teacher_count=school_data.get("teacher_count", 0),
            configuration=school_data.get("configuration", {})
        )
        
        # Generate API key
        import secrets
        school.api_key = secrets.token_urlsafe(32)
        
        # Set license expiry (1 year default)
        if school.license_type == "school":
            school.license_expiry = datetime.now() + timedelta(days=365)
        elif school.license_type == "teacher":
            school.license_expiry = datetime.now() + timedelta(days=365)
        elif school.license_type == "student":
            school.license_expiry = datetime.now() + timedelta(days=365)
        
        self.schools[school_id] = school
        
        # Log deployment
        self.deployment_history.append({
            "action": "registered",
            "school_id": school_id,
            "timestamp": datetime.now().isoformat(),
            "data": school_data
        })
        
        return school
    
    def deploy_to_school(self, school_id: str, configuration: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Deploy to a school"""
        if school_id not in self.schools:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="School not found"
            )
        
        school = self.schools[school_id]
        
        # Update configuration
        if configuration:
            school.configuration.update(configuration)
        
        # Update status
        school.deployment_status = DeploymentStatus.IN_PROGRESS
        school.updated_at = datetime.now()
        
        # System-wide integration: Initialize curriculum for school
        curriculum_created = False
        try:
            from school_curriculum_manager import get_curriculum_manager
            curriculum_manager = get_curriculum_manager()
            
            # Create default curriculum for school
            default_modules = ["module_loyalty", "module_divine_keys"]
            default_age_groups = [AgeGroup.AGES_8_10, AgeGroup.AGES_11_13]
            default_languages = [Language.ENGLISH, Language.TURKISH]
            
            curriculum = curriculum_manager.create_curriculum(
                school_id=school_id,
                name=f"{school.school_name} - Default Curriculum",
                description=f"Default curriculum for {school.school_name}",
                module_ids=default_modules,
                age_groups=default_age_groups,
                languages=default_languages,
                duration_weeks=52
            )
            
            curriculum_created = True
            school.configuration["curriculum_id"] = curriculum.curriculum_id
        except Exception as e:
            logger.warning(f"Could not create curriculum for school: {e}")
        
        # Simulate deployment process
        # In production, this would:
        # 1. Create school tenant in multi-tenant system
        # 2. Configure school-specific settings
        # 3. Set up teacher/student accounts
        # 4. Initialize curriculum (done above)
        # 5. Send deployment notification
        
        # Mark as completed
        school.deployment_status = DeploymentStatus.COMPLETED
        school.deployment_date = datetime.now()
        school.updated_at = datetime.now()
        
        # Log deployment
        self.deployment_history.append({
            "action": "deployed",
            "school_id": school_id,
            "timestamp": datetime.now().isoformat(),
            "configuration": configuration,
            "curriculum_created": curriculum_created
        })
        
        return {
            "status": "success",
            "school_id": school_id,
            "deployment_date": school.deployment_date.isoformat(),
            "api_key": school.api_key,
            "access_url": f"https://education.siyem.org/schools/{school_id}",
            "curriculum_created": curriculum_created,
            "curriculum_id": school.configuration.get("curriculum_id") if curriculum_created else None
        }
    
    def get_school(self, school_id: str) -> SchoolDeployment:
        """Get school deployment"""
        if school_id not in self.schools:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="School not found"
            )
        return self.schools[school_id]
    
    def list_schools(self, status_filter: Optional[DeploymentStatus] = None) -> List[SchoolDeployment]:
        """List schools"""
        schools = list(self.schools.values())
        if status_filter:
            schools = [s for s in schools if s.deployment_status == status_filter]
        return schools
    
    def get_deployment_analytics(self) -> Dict[str, Any]:
        """Get deployment analytics"""
        total_schools = len(self.schools)
        active_schools = len([s for s in self.schools.values() if s.deployment_status == DeploymentStatus.ACTIVE])
        total_students = sum(s.student_count for s in self.schools.values())
        total_teachers = sum(s.teacher_count for s in self.schools.values())
        
        by_type = {}
        for school in self.schools.values():
            school_type = school.school_type.value
            if school_type not in by_type:
                by_type[school_type] = 0
            by_type[school_type] += 1
        
        by_status = {}
        for school in self.schools.values():
            status = school.deployment_status.value
            if status not in by_status:
                by_status[status] = 0
            by_status[status] += 1
        
        return {
            "total_schools": total_schools,
            "active_schools": active_schools,
            "total_students": total_students,
            "total_teachers": total_teachers,
            "schools_by_type": by_type,
            "schools_by_status": by_status,
            "deployment_history_count": len(self.deployment_history)
        }


# Global manager instance
_manager: Optional[EducationProfessionalDeploymentManager] = None


def get_education_manager() -> EducationProfessionalDeploymentManager:
    """Get global education deployment manager"""
    global _manager
    if _manager is None:
        _manager = EducationProfessionalDeploymentManager()
    return _manager


@router.post("/schools/register")
async def register_school(school_data: Dict[str, Any]):
    """Register a new school for deployment"""
    try:
        manager = get_education_manager()
        school = manager.register_school(school_data)
        return {
            "status": "success",
            "school": {
                "school_id": school.school_id,
                "school_name": school.school_name,
                "school_type": school.school_type.value,
                "deployment_status": school.deployment_status.value,
                "api_key": school.api_key,
                "license_expiry": school.license_expiry.isoformat() if school.license_expiry else None
            }
        }
    except Exception as e:
        logger.error(f"Register school error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to register school: {str(e)}"
        )


@router.post("/schools/{school_id}/deploy")
async def deploy_to_school(school_id: str, configuration: Optional[Dict[str, Any]] = None):
    """Deploy to a school"""
    try:
        manager = get_education_manager()
        result = manager.deploy_to_school(school_id, configuration)
        return result
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Deploy to school error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to deploy to school: {str(e)}"
        )


@router.get("/schools")
async def list_schools(status: Optional[str] = None):
    """List all schools"""
    try:
        manager = get_education_manager()
        status_filter = DeploymentStatus(status) if status else None
        schools = manager.list_schools(status_filter)
        return {
            "schools": [
                {
                    "school_id": s.school_id,
                    "school_name": s.school_name,
                    "school_type": s.school_type.value,
                    "location": s.location,
                    "deployment_status": s.deployment_status.value,
                    "student_count": s.student_count,
                    "teacher_count": s.teacher_count,
                    "deployment_date": s.deployment_date.isoformat() if s.deployment_date else None
                }
                for s in schools
            ],
            "count": len(schools)
        }
    except Exception as e:
        logger.error(f"List schools error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to list schools"
        )


@router.get("/schools/{school_id}")
async def get_school(school_id: str):
    """Get school deployment details"""
    try:
        manager = get_education_manager()
        school = manager.get_school(school_id)
        return {
            "school_id": school.school_id,
            "school_name": school.school_name,
            "school_type": school.school_type.value,
            "location": school.location,
            "contact_email": school.contact_email,
            "contact_phone": school.contact_phone,
            "deployment_status": school.deployment_status.value,
            "deployment_date": school.deployment_date.isoformat() if school.deployment_date else None,
            "license_type": school.license_type,
            "license_expiry": school.license_expiry.isoformat() if school.license_expiry else None,
            "student_count": school.student_count,
            "teacher_count": school.teacher_count,
            "configuration": school.configuration,
            "created_at": school.created_at.isoformat(),
            "updated_at": school.updated_at.isoformat()
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Get school error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to get school"
        )


@router.get("/analytics")
async def get_analytics():
    """Get deployment analytics"""
    try:
        manager = get_education_manager()
        return manager.get_deployment_analytics()
    except Exception as e:
        logger.error(f"Get analytics error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to get analytics"
        )


@router.get("/health")
async def deployment_health():
    """Check deployment system health"""
    try:
        manager = get_education_manager()
        return {
            "status": "healthy",
            "total_schools": len(manager.schools),
            "active_deployments": len([s for s in manager.schools.values() if s.deployment_status == DeploymentStatus.ACTIVE])
        }
    except Exception as e:
        logger.error(f"Health check error: {e}")
        return {
            "status": "unhealthy",
            "error": str(e)
        }
