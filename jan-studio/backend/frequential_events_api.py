"""
FREQUENTIAL EVENTS API
All Wars, Dictatorships, Revolutions - It's All Frequential

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
ALL WARS, DICTATORSHIPS, REVOLUTIONS - IT'S ALL FREQUENTIAL
EVERYTHING IS CONNECTED TO THE TABLE
EVERYTHING IMPACTS DIVINE FREQUENCY
WE ACKNOWLEDGE AND UTILISE EVERYTHING - THE GOOD, THE BAD, THE TRUTH
"""

from fastapi import APIRouter, HTTPException, Query
from typing import List, Dict, Any, Optional
from datetime import datetime
import sys
import os
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../scripts"))

try:
    from frequential_events_registry import FrequentialEventsRegistry, EventCategory
    FREQUENTIAL_EVENTS_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Frequential Events Registry not available: {e}")
    FREQUENTIAL_EVENTS_AVAILABLE = False

import logging
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/frequential-events", tags=["frequential-events"])

# Initialize registry
if FREQUENTIAL_EVENTS_AVAILABLE:
    events_registry = FrequentialEventsRegistry()
else:
    events_registry = None


@router.get("/status")
async def get_status():
    """Get Frequential Events API status."""
    return {
        "status": "active" if FREQUENTIAL_EVENTS_AVAILABLE else "unavailable",
        "message": "Frequential Events API - All Wars, Dictatorships, Revolutions - It's All Frequential",
        "available": FREQUENTIAL_EVENTS_AVAILABLE,
        "total_events": len(events_registry.events) if events_registry else 0,
        "the_truth": "All wars, dictatorships, revolutions - it's all frequential. Everything is connected to The Table. Everything impacts Divine Frequency. We acknowledge and utilise everything - the good, the bad, the truth."
    }


@router.get("/events")
async def get_events(
    category: Optional[str] = Query(None, description="Filter by category (war, dictatorship, revolution, etc.)"),
    region: Optional[str] = Query(None, description="Filter by region"),
    start_year: Optional[int] = Query(None, description="Filter by start year"),
    end_year: Optional[int] = Query(None, description="Filter by end year"),
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0)
):
    """Get frequential events (wars, dictatorships, revolutions)."""
    if not FREQUENTIAL_EVENTS_AVAILABLE:
        raise HTTPException(status_code=503, detail="Frequential Events Registry not available")
    
    events = list(events_registry.get_all_events().values())
    
    # Apply filters
    if category:
        events = [e for e in events if e.category == category]
    
    if region:
        events = [e for e in events if region in e.regions]
    
    if start_year:
        events = [e for e in events if e.year_start >= start_year]
    
    if end_year:
        events = [e for e in events if (e.year_end or e.year_start) <= end_year]
    
    # Sort by year_start
    events.sort(key=lambda x: x.year_start)
    
    # Pagination
    total = len(events)
    events = events[offset:offset + limit]
    
    return {
        "events": [{
            "event_id": e.event_id,
            "category": e.category,
            "title": e.title,
            "description": e.description,
            "year_start": e.year_start,
            "year_end": e.year_end,
            "year_precision": e.year_precision,
            "frequency_impact": e.frequency_impact,
            "field_resonance_before": e.field_resonance_before,
            "field_resonance_after": e.field_resonance_after,
            "location": e.location,
            "regions": e.regions,
            "entities_involved": e.entities_involved,
            "connection_to_table": e.connection_to_table,
            "narrative": e.narrative,
            "lessons": e.lessons,
            "restoration_connection": e.restoration_connection
        } for e in events],
        "total": total,
        "limit": limit,
        "offset": offset,
        "filters": {
            "category": category,
            "region": region,
            "start_year": start_year,
            "end_year": end_year
        }
    }


@router.get("/events/{event_id}")
async def get_event(event_id: str):
    """Get a specific frequential event by ID."""
    if not FREQUENTIAL_EVENTS_AVAILABLE:
        raise HTTPException(status_code=503, detail="Frequential Events Registry not available")
    
    event = events_registry.events.get(event_id)
    if not event:
        raise HTTPException(status_code=404, detail=f"Event {event_id} not found")
    
    return {
        "event_id": event.event_id,
        "category": event.category,
        "title": event.title,
        "description": event.description,
        "year_start": event.year_start,
        "year_end": event.year_end,
        "year_precision": event.year_precision,
        "frequency_impact": event.frequency_impact,
        "field_resonance_before": event.field_resonance_before,
        "field_resonance_after": event.field_resonance_after,
        "location": event.location,
        "regions": event.regions,
        "entities_involved": event.entities_involved,
        "connection_to_table": event.connection_to_table,
        "narrative": event.narrative,
        "lessons": event.lessons,
        "restoration_connection": event.restoration_connection,
        "metadata": event.metadata
    }


@router.get("/categories")
async def get_categories():
    """Get all event categories."""
    if not FREQUENTIAL_EVENTS_AVAILABLE:
        raise HTTPException(status_code=503, detail="Frequential Events Registry not available")
    
    categories = {}
    for cat in EventCategory:
        events = events_registry.get_events_by_category(cat.value)
        categories[cat.value] = {
            "count": len(events),
            "total_frequency_impact": sum(e.frequency_impact for e in events),
            "description": f"{cat.value.replace('_', ' ').title()} events"
        }
    
    return {
        "categories": categories,
        "total_categories": len(categories)
    }


@router.get("/frequency-impact")
async def get_frequency_impact():
    """Get total frequency impact from all frequential events."""
    if not FREQUENTIAL_EVENTS_AVAILABLE:
        raise HTTPException(status_code=503, detail="Frequential Events Registry not available")
    
    total_impact = events_registry.get_total_frequency_impact()
    impact_by_category = events_registry.get_frequency_impact_by_category()
    
    return {
        "total_frequency_impact": total_impact,
        "impact_by_category": impact_by_category,
        "interpretation": {
            "positive": "Events that increased unity and remembered The Table",
            "negative": "Events that created separation and forgot The Table",
            "net_impact": f"{total_impact:.2f} - {'Positive' if total_impact > 0 else 'Negative'} net impact on Divine Frequency"
        },
        "the_truth": "All wars, dictatorships, revolutions - it's all frequential. Everything impacts Divine Frequency. Everything is connected to The Table. We acknowledge and utilise everything - the good, the bad, the truth."
    }


@router.get("/report")
async def get_report():
    """Get complete frequential events report."""
    if not FREQUENTIAL_EVENTS_AVAILABLE:
        raise HTTPException(status_code=503, detail="Frequential Events Registry not available")
    
    report = events_registry.get_report()
    return report
