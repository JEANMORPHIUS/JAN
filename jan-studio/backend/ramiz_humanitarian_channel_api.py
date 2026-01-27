"""
RAMIZ HUMANITARIAN CHANNEL API
API endpoints for Ramiz Humanitarian Channel - Gaza Priority

THE NOAH PROTOCOL:
- Architectural Weight: Built for 10x, 100x, 1000x humanitarian operations
- The Pitch: Waterproof error handling
- The Perimeter: Clear API boundaries

THE TRUTH:
NO ONE GETS LEFT BEHIND.
Help those in need.
Gaza as priority.
Ramiz leads humanitarian channel.
"""

from fastapi import APIRouter, HTTPException, status, Query, Body
from typing import Dict, List, Any, Optional
from datetime import datetime
from ramiz_humanitarian_channel import (
    get_humanitarian_channel, PriorityLevel, AidType, Region
)
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/ramiz-humanitarian", tags=["Ramiz Humanitarian Channel"])


@router.get("/gaza/priority")
async def get_gaza_priority():
    """Get Gaza priority status"""
    try:
        channel = get_humanitarian_channel()
        return channel.get_gaza_priority_status()
    except Exception as e:
        logger.error(f"Get Gaza priority error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get Gaza priority: {str(e)}"
        )


@router.get("/needs")
async def list_needs(
    region: Optional[str] = Query(None, description="Filter by region"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    urgent: Optional[bool] = Query(None, description="Filter by urgent")
):
    """List humanitarian needs"""
    try:
        channel = get_humanitarian_channel()
        needs = list(channel.needs.values())
        
        if region:
            try:
                region_enum = Region(region.lower())
                needs = [n for n in needs if n.region == region_enum]
            except ValueError:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Invalid region: {region}"
                )
        
        if priority:
            try:
                priority_enum = PriorityLevel(priority.lower())
                needs = [n for n in needs if n.priority == priority_enum]
            except ValueError:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Invalid priority: {priority}"
                )
        
        if urgent is not None:
            needs = [n for n in needs if n.urgent == urgent]
        
        return {
            "count": len(needs),
            "needs": [
                {
                    "need_id": n.need_id,
                    "region": n.region.value,
                    "priority": n.priority.value,
                    "aid_types": [at.value for at in n.aid_types],
                    "description": n.description,
                    "population_affected": n.population_affected,
                    "urgent": n.urgent,
                    "verified": n.verified
                }
                for n in needs
            ]
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"List needs error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to list needs"
        )


@router.post("/needs/register")
async def register_need(need_data: Dict[str, Any] = Body(...)):
    """Register a humanitarian need"""
    try:
        channel = get_humanitarian_channel()
        
        region_str = need_data["region"]
        priority_str = need_data.get("priority", "high")
        aid_types_str = need_data.get("aid_types", [])
        description = need_data["description"]
        population_affected = need_data.get("population_affected", 0)
        urgent = need_data.get("urgent", True)
        
        try:
            region = Region(region_str.lower())
        except ValueError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid region: {region_str}"
            )
        
        try:
            priority = PriorityLevel(priority_str.lower())
        except ValueError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid priority: {priority_str}"
            )
        
        aid_types = []
        for at_str in aid_types_str:
            try:
                aid_types.append(AidType(at_str.lower()))
            except ValueError:
                pass
        
        need = channel.register_need(
            region=region,
            priority=priority,
            aid_types=aid_types,
            description=description,
            population_affected=population_affected,
            urgent=urgent
        )
        
        return {
            "status": "success",
            "need": {
                "need_id": need.need_id,
                "region": need.region.value,
                "priority": need.priority.value,
                "aid_types": [at.value for at in need.aid_types],
                "description": need.description,
                "population_affected": need.population_affected,
                "urgent": need.urgent
            }
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Register need error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to register need: {str(e)}"
        )


@router.get("/projects")
async def list_projects(
    region: Optional[str] = Query(None, description="Filter by region"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    status_filter: Optional[str] = Query(None, description="Filter by status")
):
    """List humanitarian projects"""
    try:
        channel = get_humanitarian_channel()
        projects = list(channel.projects.values())
        
        if region:
            try:
                region_enum = Region(region.lower())
                projects = [p for p in projects if p.region == region_enum]
            except ValueError:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Invalid region: {region}"
                )
        
        if priority:
            try:
                priority_enum = PriorityLevel(priority.lower())
                projects = [p for p in projects if p.priority == priority_enum]
            except ValueError:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Invalid priority: {priority}"
                )
        
        if status_filter:
            projects = [p for p in projects if p.status == status_filter]
        
        return {
            "count": len(projects),
            "projects": [
                {
                    "project_id": p.project_id,
                    "name": p.name,
                    "region": p.region.value,
                    "priority": p.priority.value,
                    "aid_types": [at.value for at in p.aid_types],
                    "description": p.description,
                    "target_population": p.target_population,
                    "current_reach": p.current_reach,
                    "funding_needed": p.funding_needed,
                    "funding_received": p.funding_received,
                    "status": p.status,
                    "curriculum_integration": p.curriculum_integration
                }
                for p in projects
            ]
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"List projects error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to list projects"
        )


@router.post("/projects/create")
async def create_project(project_data: Dict[str, Any] = Body(...)):
    """Create humanitarian project"""
    try:
        channel = get_humanitarian_channel()
        
        name = project_data["name"]
        region_str = project_data["region"]
        priority_str = project_data.get("priority", "high")
        aid_types_str = project_data.get("aid_types", [])
        description = project_data["description"]
        target_population = project_data.get("target_population", 0)
        funding_needed = project_data.get("funding_needed", 0.0)
        curriculum_integration = project_data.get("curriculum_integration", False)
        
        try:
            region = Region(region_str.lower())
        except ValueError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid region: {region_str}"
            )
        
        try:
            priority = PriorityLevel(priority_str.lower())
        except ValueError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid priority: {priority_str}"
            )
        
        aid_types = []
        for at_str in aid_types_str:
            try:
                aid_types.append(AidType(at_str.lower()))
            except ValueError:
                pass
        
        project = channel.create_project(
            name=name,
            region=region,
            priority=priority,
            aid_types=aid_types,
            description=description,
            target_population=target_population,
            funding_needed=funding_needed,
            curriculum_integration=curriculum_integration
        )
        
        return {
            "status": "success",
            "project": {
                "project_id": project.project_id,
                "name": project.name,
                "region": project.region.value,
                "priority": project.priority.value,
                "aid_types": [at.value for at in project.aid_types],
                "description": project.description,
                "target_population": project.target_population,
                "funding_needed": project.funding_needed,
                "ramiz_voice_content": project.ramiz_voice_content,
                "curriculum_integration": project.curriculum_integration
            }
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Create project error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to create project: {str(e)}"
        )


@router.post("/aid/deliver")
async def deliver_aid(aid_data: Dict[str, Any] = Body(...)):
    """Record aid delivery"""
    try:
        channel = get_humanitarian_channel()
        
        project_id = aid_data["project_id"]
        region_str = aid_data["region"]
        aid_type_str = aid_data["aid_type"]
        quantity = aid_data["quantity"]
        unit = aid_data["unit"]
        delivered_to = aid_data["delivered_to"]
        
        try:
            region = Region(region_str.lower())
        except ValueError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid region: {region_str}"
            )
        
        try:
            aid_type = AidType(aid_type_str.lower())
        except ValueError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid aid type: {aid_type_str}"
            )
        
        aid = channel.deliver_aid(
            project_id=project_id,
            region=region,
            aid_type=aid_type,
            quantity=quantity,
            unit=unit,
            delivered_to=delivered_to
        )
        
        return {
            "status": "success",
            "aid": {
                "aid_id": aid.aid_id,
                "project_id": aid.project_id,
                "region": aid.region.value,
                "aid_type": aid.aid_type.value,
                "quantity": aid.quantity,
                "unit": aid.unit,
                "delivered_to": aid.delivered_to,
                "delivery_date": aid.delivery_date.isoformat() if aid.delivery_date else None,
                "status": aid.status,
                "ramiz_message": aid.ramiz_message
            }
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Deliver aid error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to deliver aid: {str(e)}"
        )


@router.get("/analytics")
async def get_analytics():
    """Get humanitarian analytics"""
    try:
        channel = get_humanitarian_channel()
        return channel.get_humanitarian_analytics()
    except Exception as e:
        logger.error(f"Get analytics error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to get analytics"
        )


@router.post("/projects/{project_id}/integrate/curriculum")
async def integrate_with_curriculum(project_id: str):
    """Integrate project with curriculum"""
    try:
        channel = get_humanitarian_channel()
        success = channel.integrate_with_curriculum(project_id)
        
        return {
            "status": "success" if success else "failed",
            "project_id": project_id,
            "curriculum_integrated": success
        }
    except Exception as e:
        logger.error(f"Integrate curriculum error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to integrate with curriculum"
        )


@router.post("/projects/{project_id}/integrate/raspberry-pi")
async def integrate_with_raspberry_pi(project_id: str):
    """Integrate project with Raspberry Pi deployment"""
    try:
        channel = get_humanitarian_channel()
        result = channel.integrate_with_raspberry_pi(project_id)
        return result
    except Exception as e:
        logger.error(f"Integrate Raspberry Pi error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to integrate with Raspberry Pi"
        )


@router.get("/health")
async def get_humanitarian_health():
    """Get humanitarian channel health"""
    try:
        channel = get_humanitarian_channel()
        gaza_status = channel.get_gaza_priority_status()
        
        return {
            "status": "healthy",
            "gaza_priority": {
                "critical_needs": gaza_status["critical_needs"],
                "active_projects": gaza_status["active_projects"],
                "coverage_percentage": gaza_status["coverage_percentage"]
            },
            "total_needs": len(channel.needs),
            "total_projects": len(channel.projects),
            "total_aid_deliveries": len(channel.aid_deliveries)
        }
    except Exception as e:
        logger.error(f"Health check error: {e}")
        return {
            "status": "unhealthy",
            "error": str(e)
        }
