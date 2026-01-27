"""
RAMIZ HUMANITARIAN VOLUNTEERS API
API endpoints for volunteer coordination

THE TRUTH:
NO ONE GETS LEFT BEHIND.
Gaza as priority.
Volunteers are the heart of humanitarian work.
"""

from fastapi import APIRouter, HTTPException, status, Query, Body
from typing import Dict, List, Any, Optional
from datetime import datetime
from ramiz_humanitarian_volunteers import (
    get_humanitarian_volunteers, VolunteerStatus, VolunteerSkill
)
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/ramiz-humanitarian/volunteers", tags=["Ramiz Humanitarian Volunteers"])


@router.post("/register")
async def register_volunteer(volunteer_data: Dict[str, Any] = Body(...)):
    """Register volunteer"""
    try:
        volunteer_system = get_humanitarian_volunteers()
        
        name = volunteer_data["name"]
        email = volunteer_data["email"]
        phone = volunteer_data.get("phone")
        location = volunteer_data.get("location")
        skills = volunteer_data.get("skills", [])
        languages = volunteer_data.get("languages", [])
        gaza_priority = volunteer_data.get("gaza_priority", False)
        availability_start = None
        availability_end = None
        
        if volunteer_data.get("availability_start"):
            availability_start = datetime.fromisoformat(volunteer_data["availability_start"])
        if volunteer_data.get("availability_end"):
            availability_end = datetime.fromisoformat(volunteer_data["availability_end"])
        
        notes = volunteer_data.get("notes", "")
        
        volunteer = volunteer_system.register_volunteer(
            name=name,
            email=email,
            phone=phone,
            location=location,
            skills=skills,
            languages=languages,
            gaza_priority=gaza_priority,
            availability_start=availability_start,
            availability_end=availability_end,
            notes=notes
        )
        
        return {
            "status": "success",
            "volunteer": {
                "volunteer_id": volunteer.volunteer_id,
                "name": volunteer.name,
                "email": volunteer.email,
                "skills": [s.value for s in volunteer.skills],
                "languages": volunteer.languages,
                "gaza_priority": volunteer.gaza_priority,
                "status": volunteer.status.value
            }
        }
    except Exception as e:
        logger.error(f"Register volunteer error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to register volunteer: {str(e)}"
        )


@router.post("/deploy")
async def deploy_volunteer(deployment_data: Dict[str, Any] = Body(...)):
    """Deploy volunteer"""
    try:
        volunteer_system = get_humanitarian_volunteers()
        
        volunteer_id = deployment_data["volunteer_id"]
        project_id = deployment_data["project_id"]
        role = deployment_data["role"]
        start_date = datetime.fromisoformat(deployment_data["start_date"])
        end_date = None
        if deployment_data.get("end_date"):
            end_date = datetime.fromisoformat(deployment_data["end_date"])
        location = deployment_data.get("location")
        notes = deployment_data.get("notes", "")
        
        deployment = volunteer_system.deploy_volunteer(
            volunteer_id=volunteer_id,
            project_id=project_id,
            role=role,
            start_date=start_date,
            end_date=end_date,
            location=location,
            notes=notes
        )
        
        return {
            "status": "success",
            "deployment": {
                "deployment_id": deployment.deployment_id,
                "volunteer_id": deployment.volunteer_id,
                "project_id": deployment.project_id,
                "role": deployment.role,
                "status": deployment.status.value
            }
        }
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
    except Exception as e:
        logger.error(f"Deploy volunteer error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to deploy volunteer: {str(e)}"
        )


@router.get("/gaza")
async def get_gaza_volunteers():
    """Get Gaza priority volunteers"""
    try:
        volunteer_system = get_humanitarian_volunteers()
        return {
            "volunteers": volunteer_system.get_gaza_volunteers()
        }
    except Exception as e:
        logger.error(f"Get Gaza volunteers error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to get Gaza volunteers"
        )


@router.get("/analytics")
async def get_volunteer_analytics():
    """Get volunteer analytics"""
    try:
        volunteer_system = get_humanitarian_volunteers()
        return volunteer_system.get_volunteer_analytics()
    except Exception as e:
        logger.error(f"Get volunteer analytics error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to get volunteer analytics"
        )
