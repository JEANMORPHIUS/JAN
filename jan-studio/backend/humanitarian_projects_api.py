"""
HUMANITARIAN PROJECTS API
API endpoints for humanitarian projects registry
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional
import logging

from humanitarian_projects_registry import (
    get_humanitarian_projects_registry,
    ProjectType,
    AlignmentLevel
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/humanitarian-projects", tags=["Humanitarian Projects"])


@router.get("/")
async def get_projects(
    project_type: Optional[str] = Query(None, description="Filter by type: humanitarian, animal_sanctuary, gods_work"),
    alignment_level: Optional[str] = Query(None, description="Filter by alignment: fully_aligned, highly_aligned, etc."),
    active_only: bool = Query(True, description="Only active projects")
):
    """Get humanitarian projects"""
    try:
        registry = get_humanitarian_projects_registry()
        
        type_enum = None
        if project_type:
            try:
                type_enum = ProjectType(project_type.lower())
            except ValueError:
                raise HTTPException(status_code=400, detail=f"Invalid project type: {project_type}")
        
        alignment_enum = None
        if alignment_level:
            try:
                alignment_enum = AlignmentLevel(alignment_level.lower())
            except ValueError:
                raise HTTPException(status_code=400, detail=f"Invalid alignment level: {alignment_level}")
        
        projects = registry.get_projects(type_enum, alignment_enum, active_only)
        
        return {
            "status": "success",
            "total": len(projects),
            "projects": [
                {
                    "project_id": p.project_id,
                    "name": p.name,
                    "organization": p.organization,
                    "project_type": p.project_type.value,
                    "description": p.description,
                    "location": p.location,
                    "mission_alignment": p.mission_alignment.value,
                    "alignment_score": p.alignment_score,
                    "website": p.website,
                    "focus_areas": p.focus_areas,
                    "impact_metrics": p.impact_metrics,
                    "how_to_help": p.how_to_help
                }
                for p in projects
            ]
        }
    except Exception as e:
        logger.error(f"Error getting projects: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/summary")
async def get_summary():
    """Get registry summary"""
    try:
        registry = get_humanitarian_projects_registry()
        summary = registry.get_summary()
        
        return {
            "status": "success",
            "summary": summary
        }
    except Exception as e:
        logger.error(f"Error getting summary: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/{project_id}")
async def get_project(project_id: str):
    """Get a specific project"""
    try:
        registry = get_humanitarian_projects_registry()
        project = registry.get_project(project_id)
        
        if not project:
            raise HTTPException(status_code=404, detail=f"Project not found: {project_id}")
        
        return {
            "status": "success",
            "project": {
                "project_id": project.project_id,
                "name": project.name,
                "organization": project.organization,
                "project_type": project.project_type.value,
                "description": project.description,
                "location": project.location,
                "mission_alignment": project.mission_alignment.value,
                "alignment_score": project.alignment_score,
                "website": project.website,
                "contact_info": project.contact_info,
                "focus_areas": project.focus_areas,
                "impact_metrics": project.impact_metrics,
                "funding_needs": project.funding_needs,
                "how_to_help": project.how_to_help,
                "created_date": project.created_date.isoformat(),
                "last_verified": project.last_verified.isoformat() if project.last_verified else None,
                "active": project.active
            }
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting project: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
