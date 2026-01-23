"""
Format Delegation API Endpoints

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN

API endpoints for delegating content generation by format
"""

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from datetime import datetime

from scripture_scheduler_2026 import generate_2026_scripture_schedule, ScriptureScheduler

router = APIRouter(prefix="/api/format-delegation", tags=["format-delegation"])


class FormatDelegationRequest(BaseModel):
    """Request model for format-based delegation"""
    format_type: str = Field(..., description="Format to delegate: 'text_short', 'text_long', 'video', 'audio', 'image'")
    entities: Optional[List[str]] = Field(
        default=None,
        description="Entities to include. If None, includes all."
    )
    limit: Optional[int] = Field(
        default=None,
        description="Limit number of posts. If None, returns all matching posts."
    )


@router.get("/formats")
async def list_formats():
    """List all available formats and their definitions"""
    scheduler = ScriptureScheduler()
    return {
        "formats": scheduler.FORMAT_DEFINITIONS,
        "entity_preferences": scheduler.ENTITY_FORMAT_PREFERENCES
    }


@router.get("/by-format/{format_type}")
async def get_posts_by_format(
    format_type: str,
    entities: Optional[List[str]] = Query(default=None),
    limit: Optional[int] = Query(default=None, ge=1)
):
    """
    Get all posts filtered by format type
    
    Format types: text_short, text_long, video, audio, image
    """
    valid_formats = ['text_short', 'text_long', 'video', 'audio', 'image']
    if format_type not in valid_formats:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid format. Must be one of: {valid_formats}"
        )
    
    # Generate schedule
    schedule = generate_2026_scripture_schedule(entities=entities)
    
    # Filter by format
    filtered_posts = []
    for post_dict in schedule['all_posts']:
        # Check if format matches
        primary_format = post_dict.get('format_notes', {}).get('primary_format')
        formats = post_dict.get('formats', [])
        
        if primary_format == format_type or format_type in formats:
            filtered_posts.append(post_dict)
    
    # Apply limit
    if limit:
        filtered_posts = filtered_posts[:limit]
    
    return {
        "format": format_type,
        "total_posts": len(filtered_posts),
        "posts": filtered_posts
    }


@router.get("/delegation-queue/{format_type}")
async def get_delegation_queue(
    format_type: str,
    entities: Optional[List[str]] = Query(default=None),
    agent: Optional[str] = Query(default=None, description="Filter by required agent: WRITER, ARTIST, PUBLISHER, Audio Pipeline")
):
    """
    Get posts ready for delegation to specific format agents
    
    Returns posts with delegation instructions for the specified format
    """
    valid_formats = ['text_short', 'text_long', 'video', 'audio', 'image']
    if format_type not in valid_formats:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid format. Must be one of: {valid_formats}"
        )
    
    # Generate schedule
    schedule = generate_2026_scripture_schedule(entities=entities)
    
    # Filter by format and delegation readiness
    delegation_queue = []
    for post_dict in schedule['all_posts']:
        format_notes = post_dict.get('format_notes', {})
        primary_format = format_notes.get('primary_format')
        formats = post_dict.get('formats', [])
        delegation_ready = post_dict.get('delegation_ready', False)
        
        # Check if format matches and is delegation ready
        if (primary_format == format_type or format_type in formats) and delegation_ready:
            # Filter by agent if specified
            if agent:
                required_agents = format_notes.get('delegation_agents', {}).get('required', [])
                if agent not in required_agents:
                    continue
            
            delegation_queue.append({
                "post": post_dict,
                "delegation_info": {
                    "format": format_type,
                    "required_agents": format_notes.get('delegation_agents', {}).get('required', []),
                    "format_requirements": format_notes.get('format_requirements', {}),
                    "entity_preferences": format_notes.get('entity_preferences', '')
                }
            })
    
    return {
        "format": format_type,
        "agent_filter": agent,
        "queue_length": len(delegation_queue),
        "delegation_queue": delegation_queue
    }


@router.get("/entity-formats/{entity}")
async def get_entity_format_distribution(entity: str):
    """Get format distribution for a specific entity"""
    scheduler = ScriptureScheduler()
    
    if entity not in scheduler.ENTITIES:
        raise HTTPException(
            status_code=404,
            detail=f"Entity not found. Valid entities: {scheduler.ENTITIES}"
        )
    
    prefs = scheduler.ENTITY_FORMAT_PREFERENCES.get(entity, {})
    
    return {
        "entity": entity,
        "format_preferences": prefs,
        "format_definitions": {
            fmt: scheduler.FORMAT_DEFINITIONS.get(fmt, {})
            for fmt in prefs.get('primary', []) + prefs.get('secondary', [])
        }
    }


@router.get("/summary")
async def get_format_summary(entities: Optional[List[str]] = Query(default=None)):
    """Get summary of format distribution across all posts"""
    schedule = generate_2026_scripture_schedule(entities=entities)
    
    format_counts = {
        'text_short': 0,
        'text_long': 0,
        'video': 0,
        'audio': 0,
        'image': 0
    }
    
    entity_format_counts = {}
    
    for post_dict in schedule['all_posts']:
        primary_format = post_dict.get('format_notes', {}).get('primary_format', 'text_short')
        entity = post_dict.get('metadata', {}).get('brand', 'unknown')
        
        if primary_format in format_counts:
            format_counts[primary_format] += 1
        
        if entity not in entity_format_counts:
            entity_format_counts[entity] = {
                'text_short': 0,
                'text_long': 0,
                'video': 0,
                'audio': 0,
                'image': 0
            }
        
        if primary_format in entity_format_counts[entity]:
            entity_format_counts[entity][primary_format] += 1
    
    return {
        "total_posts": schedule['summary']['total_posts'],
        "format_distribution": format_counts,
        "entity_format_distribution": entity_format_counts,
        "format_percentages": {
            fmt: round((count / schedule['summary']['total_posts']) * 100, 2)
            for fmt, count in format_counts.items()
        }
    }
