"""Content Population API Endpoints

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN

API endpoints for auto-populating content using AI services

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity


PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

from fastapi import APIRouter, HTTPException, Query, Body
from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
import asyncio

# Spiritual Codebase Hacker Integration
from spiritual_codebase_hacker_integration import HACKER_AVAILABLE, hack_loop, perform_genetic_edit, activate_stealth_mode


from content_auto_populator import ContentAutoPopulator

router = APIRouter(prefix="/api/content-population", tags=["content-population"])


class PopulationRequest(BaseModel):
    """Request model for populating content"""
    schedule: Dict = Field(..., description="Schedule dictionary with posts to populate")
    limit: Optional[int] = Field(default=None, description="Limit number of posts to populate")
    base_url: Optional[str] = Field(default="http://localhost:8000", description="Base URL for AI services")



    class Config:
        schema_extra = {
            "example": {'schedule': {}, 'limit': 10}
        }
class SinglePostRequest(BaseModel):
    """Request model for populating a single post"""
    post: Dict = Field(..., description="Post dictionary to populate")
    base_url: Optional[str] = Field(default="http://localhost:8000", description="Base URL for AI services")



    class Config:
        schema_extra = {
            "example": {'post': {}}
        }
@router.post("/populate-schedule", summary="Auto-populate entire schedule")
async def populate_schedule(request: PopulationRequest):
    """
    Auto-populate all posts in a schedule with content in assigned formats
    Uses AI services (WRITER, ARTIST, PUBLISHER, Audio Pipeline) aligned with entity voices
    """
    try:
        populator = ContentAutoPopulator(base_url=request.base_url)
        
        populated_schedule = await populator.populate_schedule(
            request.schedule,
            limit=request.limit
        )
        
        await populator.close()
        
        return {
            "success": True,
            "schedule": populated_schedule,
            "total_populated": populated_schedule.get('total_populated', 0),
            "message": f"Successfully populated {populated_schedule.get('total_populated', 0)} posts"
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error populating schedule: {str(e)}")


@router.post("/populate-post", summary="Auto-populate single post")
async def populate_post(request: SinglePostRequest):
    """
    Auto-populate a single post with content in assigned format
    """
    try:
        populator = ContentAutoPopulator(base_url=request.base_url)
        
        populated_post = await populator.populate_post(request.post)
        
        await populator.close()
        
        return {
            "success": True,
            "post": populated_post,
            "content_populated": populated_post.get('content_populated', False),
            "message": "Post populated successfully" if populated_post.get('content_populated') else "Post population completed with errors"
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error populating post: {str(e)}")


@router.post("/populate-by-format/{format_type}", summary="Populate posts by format type")
async def populate_by_format(
    format_type: str,
    schedule: Dict = Body(..., description="Schedule dictionary"),
    limit: Optional[int] = Body(default=None),
    base_url: Optional[str] = Body(default="http://localhost:8000")
):
    """
    Populate only posts with a specific format type
    """
    valid_formats = ['text_short', 'text_long', 'video', 'audio', 'image']
    if format_type not in valid_formats:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid format. Must be one of: {valid_formats}"
        )
    
    try:
        # Filter posts by format
        all_posts = schedule.get('all_posts', [])
        filtered_posts = [
            post for post in all_posts
            if post.get('format_notes', {}).get('primary_format') == format_type
        ]
        
        if limit:
            filtered_posts = filtered_posts[:limit]
        
        # Create filtered schedule
        filtered_schedule = {
            'all_posts': filtered_posts,
            'summary': schedule.get('summary', {})
        }
        
        populator = ContentAutoPopulator(base_url=base_url)
        populated_schedule = await populator.populate_schedule(filtered_schedule)
        await populator.close()
        
        return {
            "success": True,
            "format": format_type,
            "total_populated": populated_schedule.get('total_populated', 0),
            "posts": populated_schedule.get('all_posts', [])
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error populating by format: {str(e)}")


@router.post("/populate-by-entity/{entity}", summary="Populate posts by entity")
async def populate_by_entity(
    entity: str,
    schedule: Dict = Body(..., description="Schedule dictionary"),
    limit: Optional[int] = Body(default=None),
    base_url: Optional[str] = Body(default="http://localhost:8000")
):
    """
    Populate only posts for a specific entity
    """
    try:
        # Filter posts by entity
        all_posts = schedule.get('all_posts', [])
        filtered_posts = [
            post for post in all_posts
            if post.get('metadata', {}).get('brand') == entity
        ]
        
        if limit:
            filtered_posts = filtered_posts[:limit]
        
        # Create filtered schedule
        filtered_schedule = {
            'all_posts': filtered_posts,
            'summary': schedule.get('summary', {})
        }
        
        populator = ContentAutoPopulator(base_url=base_url)
        populated_schedule = await populator.populate_schedule(filtered_schedule)
        await populator.close()
        
        return {
            "success": True,
            "entity": entity,
            "total_populated": populated_schedule.get('total_populated', 0),
            "posts": populated_schedule.get('all_posts', [])
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error populating by entity: {str(e)}")


@router.get("/status", summary="Get population status")
async def get_population_status(schedule: Dict = Body(..., description="Schedule dictionary")):
    """
    Get status of content population for a schedule
    """
    all_posts = schedule.get('all_posts', [])
    
    total = len(all_posts)
    populated = len([p for p in all_posts if p.get('content_populated')])
    errors = len([p for p in all_posts if p.get('content_population_error')])
    
    format_breakdown = {}
    for post in all_posts:
        format_type = post.get('format_notes', {}).get('primary_format', 'unknown')
        if format_type not in format_breakdown:
            format_breakdown[format_type] = {'total': 0, 'populated': 0, 'errors': 0}
        
        format_breakdown[format_type]['total'] += 1
        if post.get('content_populated'):
            format_breakdown[format_type]['populated'] += 1
        if post.get('content_population_error'):
            format_breakdown[format_type]['errors'] += 1
    
    return {
        "total_posts": total,
        "populated": populated,
        "errors": errors,
        "pending": total - populated - errors,
        "completion_percentage": round((populated / total * 100) if total > 0 else 0, 2),
        "format_breakdown": format_breakdown
    }
