"""Scripture Scheduler API Endpoints

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN

API endpoints for generating and exporting scripture-based content schedules

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity


PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

from fastapi import APIRouter, HTTPException, Query, Body
from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from datetime import datetime, timezone, timedelta
import json
import random

# Spiritual Codebase Hacker Integration
from spiritual_codebase_hacker_integration import HACKER_AVAILABLE, hack_loop, perform_genetic_edit, activate_stealth_mode


from scripture_scheduler_2026 import (
    ScriptureScheduler,
    generate_2026_scripture_schedule,
    ScripturePost
)
from google_calendar_exporter import CalendarExportService

router = APIRouter(prefix="/api/scripture-schedule", tags=["scripture-schedule"])


class ScheduleGenerationRequest(BaseModel):
    """Request model for generating scripture schedule"""
    year: int = Field(default=2026, description="Year to schedule")
    posts_per_week: Optional[int] = Field(
        default=None, 
        description="Optional override for all entities. If None, uses optimized entity-specific frequencies."
    )
    entities: Optional[List[str]] = Field(
        default=None, 
        description="Entities to include. Options: 'edible_london', 'ilven_seamoss', 'jean_mahram', 'karasahin_jk', 'pierre_pressure', 'uncle_ray_ramiz', 'siyem_media'. If None, includes all."
    )
    entity_frequencies: Optional[Dict[str, int]] = Field(
        default=None,
        description="Optional dict to set frequencies per entity. Format: {'entity_name': posts_per_week}"
    )
    filter_format: Optional[str] = Field(
        default=None,
        description="Filter posts by format. Options: 'text_short', 'text_long', 'video', 'audio', 'image'"
    )


class ExportToCalendarRequest(BaseModel):
    """Request model for exporting schedule to calendar"""
    schedule: Dict = Field(..., description="Generated schedule dictionary")
    brand: Optional[str] = Field(
        default=None, 
        description="Specific entity to export ('edible_london', 'jean_mahram', etc.), or 'all' for all posts"
    )
    calendar_name: str = Field(default="Scripture Posts 2026", description="Calendar name")


@router.post("/generate", summary="Generate scripture schedule for 2026")
async def generate_schedule(request: ScheduleGenerationRequest):
    """
    Generate scripture-based social media posts for Edible London and ILVEN Sea Moss
    scheduled throughout the specified year.
    """
    try:
        if request.year == 2026:
            schedule = generate_2026_scripture_schedule(
                posts_per_week=request.posts_per_week,
                entities=request.entities,
                entity_frequencies=request.entity_frequencies
            )
        else:
            scheduler = ScriptureScheduler(
                year=request.year,
                entity_frequencies=request.entity_frequencies
            )
            entities_to_use = request.entities or scheduler.ENTITIES
            
            all_posts = scheduler.generate_yearly_schedule(
                posts_per_week=request.posts_per_week,
                brands=entities_to_use,
                entity_frequencies=request.entity_frequencies
            )
            
            # Separate by entity
            entity_posts = {}
            entity_counts = {}
            
            for entity in entities_to_use:
                entity_post_list = [p for p in all_posts if p.brand == entity]
                entity_posts[entity] = scheduler.export_to_calendar_format(entity_post_list)
                entity_counts[f"{entity}_count"] = len(entity_post_list)
            
            schedule = {
                **entity_posts,
                'all_posts': scheduler.export_to_calendar_format(all_posts),
                'summary': {
                    'total_posts': len(all_posts),
                    'year': request.year,
                    'posts_per_week': request.posts_per_week,
                    'entities': entities_to_use,
                    **entity_counts
                }
            }
        
        return {
            "success": True,
            "schedule": schedule,
            "message": f"Generated {schedule['summary']['total_posts']} scripture posts for {request.year}"
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating schedule: {str(e)}")


@router.post("/export/ical", summary="Export scripture schedule to iCal format")
async def export_schedule_to_ical(request: ExportToCalendarRequest):
    """
    Export generated scripture schedule to iCal format for calendar import
    """
    try:
        # Get posts based on entity filter
        if request.brand and request.brand.lower() != 'all':
            entity_key = request.brand.lower()
            posts = request.schedule.get(entity_key, [])
            if not posts:
                raise HTTPException(status_code=400, detail=f"No posts found for entity: {request.brand}")
        else:
            posts = request.schedule.get('all_posts', [])
        
        if not posts:
            raise HTTPException(status_code=400, detail="No posts found in schedule")
        
        # Export to iCal
        service = CalendarExportService()
        ical_content = service.export_to_ical(
            posts,
            calendar_name=request.calendar_name
        )
        
        from tempfile import NamedTemporaryFile
        import os
        
        # Create temporary file
        with NamedTemporaryFile(mode='w', suffix='.ics', delete=False, encoding='utf-8') as tmp:
            tmp.write(ical_content)
            tmp_path = tmp.name
        
        filename = f"{request.calendar_name.replace(' ', '_')}_{request.brand or 'all'}.ics"
        
        from fastapi.responses import FileResponse
        return FileResponse(
            tmp_path,
            media_type='text/calendar',
            filename=filename,
            headers={
                'Content-Disposition': f'attachment; filename="{filename}"'
            }
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error exporting to iCal: {str(e)}")


@router.post("/export/google", summary="Export scripture schedule to Google Calendar")
async def export_schedule_to_google(request: ExportToCalendarRequest):
    """
    Export generated scripture schedule directly to Google Calendar
    """
    try:
        # Get posts based on entity filter
        if request.brand and request.brand.lower() != 'all':
            entity_key = request.brand.lower()
            posts = request.schedule.get(entity_key, [])
            if not posts:
                raise HTTPException(status_code=400, detail=f"No posts found for entity: {request.brand}")
        else:
            posts = request.schedule.get('all_posts', [])
        
        if not posts:
            raise HTTPException(status_code=400, detail="No posts found in schedule")
        
        # Export to Google Calendar
        service = CalendarExportService()
        created_events = service.export_to_google_calendar(
            posts,
            calendar_id='primary'
        )
        
        return {
            "success": True,
            "events_created": len(created_events),
            "events": created_events,
            "message": f"Successfully created {len(created_events)} event(s) in Google Calendar"
        }
    
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error exporting to Google Calendar: {str(e)}")


@router.get("/preview", summary="Preview scripture schedule")
async def preview_schedule(
    year: int = Query(default=2026),
    posts_per_week: int = Query(default=3),
    limit: int = Query(default=10, description="Number of posts to preview")
):
    """
    Preview a sample of generated scripture posts without generating full schedule
    """
    try:
        scheduler = ScriptureScheduler(year=year)
        
        # Generate just a few posts for preview
        preview_posts = []
        current_date = datetime(year, 1, 1, 9, 0, tzinfo=timezone.utc)
        
        theme_keys = list(scheduler.SCRIPTURES.keys())
        
        # Use multiple entities for preview
        preview_entities = ['edible_london', 'ilven_seamoss', 'jean_mahram', 'pierre_pressure']
        
        for i in range(min(limit, len(theme_keys) * len(preview_entities))):
            theme = theme_keys[i % len(theme_keys)]
            verse_ref, verse_text, _ = random.choice(scheduler.SCRIPTURES[theme])
            
            # Rotate through entities
            entity = preview_entities[i % len(preview_entities)]
            
            # Generate post based on entity
            if entity == 'edible_london':
                post = scheduler.generate_edible_london_post(verse_ref, verse_text, theme, current_date)
            elif entity == 'ilven_seamoss':
                post = scheduler.generate_ilven_post(verse_ref, verse_text, theme, current_date)
            elif entity == 'jean_mahram':
                post = scheduler.generate_jean_mahram_post(verse_ref, verse_text, theme, current_date)
            elif entity == 'pierre_pressure':
                post = scheduler.generate_pierre_pressure_post(verse_ref, verse_text, theme, current_date)
            else:
                post = scheduler.generate_edible_london_post(verse_ref, verse_text, theme, current_date)
            
            preview_posts.append(scheduler.export_to_calendar_format([post])[0])
            current_date += timedelta(days=7 / posts_per_week)
        
        return {
            "success": True,
            "preview_posts": preview_posts,
            "total_preview": len(preview_posts),
            "year": year,
            "posts_per_week": posts_per_week
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating preview: {str(e)}")
