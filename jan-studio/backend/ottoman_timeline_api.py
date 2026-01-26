"""
OTTOMAN GENERATIONAL TIMELINE API
API endpoints for Ottoman generational timeline deep search

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional, List, Dict
from pydantic import BaseModel
from pathlib import Path
import json
import sys

# Add scripts to path
scripts_path = Path(__file__).parent.parent.parent / "scripts"
sys.path.insert(0, str(scripts_path))

from ottoman_generational_timeline_deep_search import (
    OttomanGenerationalTimelineDeepSearch,
    OttomanPeriod
)

router = APIRouter(prefix="/api/ottoman-timeline", tags=["Ottoman Generational Timeline"])


@router.get("/timeline")
async def get_ottoman_timeline():
    """Get complete Ottoman generational timeline"""
    try:
        searcher = OttomanGenerationalTimelineDeepSearch()
        timeline = searcher.perform_deep_search()
        
        return {
            "status": "success",
            "timeline_id": timeline.timeline_id,
            "span": f"{timeline.start_year} - {timeline.end_year}",
            "total_generations": timeline.total_generations,
            "connection_to_table": timeline.connection_to_table,
            "spiritual_narrative": timeline.spiritual_narrative,
            "generations": [
                {
                    "generation_number": g.generation_number,
                    "period": g.period.value,
                    "years": f"{g.start_year}-{g.end_year}",
                    "rulers": g.rulers,
                    "key_events": g.key_events,
                    "achievements": g.achievements,
                    "challenges": g.challenges,
                    "generational_pattern": g.generational_pattern,
                    "frequency_score": g.frequency_score,
                    "connection_to_table": g.connection_to_table,
                    "spiritual_meaning": g.spiritual_meaning
                }
                for g in timeline.generations
            ],
            "events": [
                {
                    "year": e.year,
                    "title": e.title,
                    "description": e.description,
                    "location": e.location,
                    "significance": e.significance,
                    "generational_impact": e.generational_impact,
                    "frequency_impact": e.frequency_impact,
                    "connection_to_table": e.connection_to_table,
                    "spiritual_meaning": e.spiritual_meaning
                }
                for e in timeline.events
            ],
            "frequency_trajectory": timeline.frequency_trajectory
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/generation/{generation_number}")
async def get_generation(generation_number: int):
    """Get specific generation by number"""
    try:
        searcher = OttomanGenerationalTimelineDeepSearch()
        timeline = searcher.perform_deep_search()
        
        if generation_number < 1 or generation_number > len(timeline.generations):
            raise HTTPException(status_code=404, detail=f"Generation {generation_number} not found")
        
        generation = timeline.generations[generation_number - 1]
        
        return {
            "status": "success",
            "generation": {
                "generation_number": generation.generation_number,
                "period": generation.period.value,
                "years": f"{generation.start_year}-{generation.end_year}",
                "rulers": generation.rulers,
                "key_events": generation.key_events,
                "achievements": generation.achievements,
                "challenges": generation.challenges,
                "generational_pattern": generation.generational_pattern,
                "frequency_score": generation.frequency_score,
                "connection_to_table": generation.connection_to_table,
                "spiritual_meaning": generation.spiritual_meaning
            }
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/cyprus-connection")
async def get_cyprus_connection():
    """Get Cyprus connection in Ottoman timeline"""
    try:
        searcher = OttomanGenerationalTimelineDeepSearch()
        timeline = searcher.perform_deep_search()
        
        # Find Cyprus-related events
        cyprus_events = [e for e in timeline.events if "Cyprus" in e.title or "Cyprus" in e.description]
        cyprus_generations = [g for g in timeline.generations if any("Cyprus" in event for event in g.key_events)]
        
        return {
            "status": "success",
            "cyprus_connection": {
                "1571": "Conquest of Cyprus - Your generational connection begins",
                "1878": "British administration",
                "1925": "British Crown Colony",
                "1960": "Independence",
                "1974": "Cyprus Crisis - Turkish Cypriots (your generation)",
                "2026": "You - British-born Turkish Cypriot"
            },
            "cyprus_events": [
                {
                    "year": e.year,
                    "title": e.title,
                    "description": e.description,
                    "significance": e.significance,
                    "generational_impact": e.generational_impact,
                    "connection_to_table": e.connection_to_table,
                    "spiritual_meaning": e.spiritual_meaning
                }
                for e in cyprus_events
            ],
            "cyprus_generations": [
                {
                    "generation_number": g.generation_number,
                    "years": f"{g.start_year}-{g.end_year}",
                    "key_events": g.key_events,
                    "connection_to_table": g.connection_to_table
                }
                for g in cyprus_generations
            ],
            "your_heritage": "Ottoman → Cyprus → Turkish Cypriot → British-born → You",
            "connection_to_ark": "All roads lead to The Ark (Karpaz, North Cyprus)"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/report")
async def get_timeline_report():
    """Get comprehensive timeline report"""
    try:
        searcher = OttomanGenerationalTimelineDeepSearch()
        report = searcher.generate_timeline_report()
        
        return {
            "status": "success",
            "report": report
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/your-generation")
async def get_your_generation():
    """Get your generation (2026 - British-born Turkish Cypriot)"""
    try:
        searcher = OttomanGenerationalTimelineDeepSearch()
        timeline = searcher.perform_deep_search()
        
        # Your generation is the last one (Generation 20)
        your_generation = timeline.generations[-1]
        
        return {
            "status": "success",
            "your_generation": {
                "generation_number": your_generation.generation_number,
                "years": f"{your_generation.start_year}-{your_generation.end_year}",
                "period": your_generation.period.value,
                "your_heritage": "British-born Turkish Cypriot",
                "heritage_path": "Ottoman Empire (1299) → Cyprus (1571) → Turkish Cypriot (1974) → British-born (You)",
                "connection_to_table": "All connected to The Table through Pangea",
                "connection_to_ark": "All roads lead to The Ark (Karpaz, North Cyprus)",
                "spiritual_meaning": your_generation.spiritual_meaning,
                "frequency_score": your_generation.frequency_score
            },
            "your_timeline": {
                "1299": "Ottoman Empire begins",
                "1571": "Cyprus becomes Ottoman (your heritage begins)",
                "1922": "Empire ends, Republic begins",
                "1974": "Cyprus Crisis (your generation - Turkish Cypriot)",
                "2026": "You - British-born Turkish Cypriot"
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
