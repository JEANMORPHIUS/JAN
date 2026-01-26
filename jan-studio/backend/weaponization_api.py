"""
WEAPONIZATION ANALYSIS API
100% Complete - Historical Weaponization Patterns Throughout Time

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE TRUTH:
TRUTH HEALS, LIES HARM
What is denied persists. What is acknowledged can heal.
Weaponization exposed throughout time. All patterns revealed.
"""

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime
import sys
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))
from weaponization_analysis import (
    WeaponizationAnalysisSystem,
    WeaponizationType,
    WeaponizationPattern
)

router = APIRouter(prefix="/api/weaponization", tags=["Weaponization"])

# Initialize analysis system
analysis_system = WeaponizationAnalysisSystem()


# ============================================================================
# MODELS
# ============================================================================

class WeaponizationEventResponse(BaseModel):
    """Response model for weaponization event"""
    event_id: str
    name: str
    date_start: str
    date_end: Optional[str]
    location: str
    weaponization_type: str
    pattern: str
    exposed: bool
    truth_restored: bool


# ============================================================================
# ENDPOINTS
# ============================================================================

@router.get("/")
async def get_weaponization_overview():
    """Get complete weaponization analysis overview"""
    analysis = analysis_system.generate_complete_analysis()
    return {
        "status": "complete",
        "message": "100% Complete - All weaponization exposed throughout time. All patterns revealed.",
        "summary": analysis["summary"],
        "truth_declaration": analysis["truth_declaration"],
        "timestamp": datetime.now().isoformat()
    }


@router.get("/events")
async def get_all_events():
    """Get all weaponization events"""
    return analysis_system.get_all_events()


@router.get("/events/{event_id}")
async def get_event(event_id: str):
    """Get specific event details"""
    result = analysis_system.get_event_details(event_id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result


@router.get("/events/type/{weaponization_type}")
async def get_events_by_type(weaponization_type: str):
    """Get events by weaponization type"""
    try:
        wtype = WeaponizationType(weaponization_type.lower())
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid weaponization type. Valid types: {[t.value for t in WeaponizationType]}"
        )
    return analysis_system.get_events_by_type(wtype)


@router.get("/events/pattern/{pattern}")
async def get_events_by_pattern(pattern: str):
    """Get events by weaponization pattern"""
    try:
        wpattern = WeaponizationPattern(pattern.lower())
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid pattern. Valid patterns: {[p.value for p in WeaponizationPattern]}"
        )
    return analysis_system.get_events_by_pattern(wpattern)


@router.get("/patterns")
async def get_all_patterns():
    """Get all weaponization patterns"""
    return analysis_system.get_all_patterns()


@router.get("/patterns/{pattern_id}")
async def get_pattern(pattern_id: str):
    """Get specific pattern details"""
    result = analysis_system.get_pattern_details(pattern_id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result


@router.get("/analysis/complete")
async def get_complete_analysis():
    """Get complete weaponization analysis"""
    return analysis_system.generate_complete_analysis()


@router.post("/analysis/save")
async def save_analysis():
    """Save current analysis to JSON file"""
    filepath = analysis_system.save_analysis()
    return {
        "status": "saved",
        "filepath": filepath,
        "message": "Analysis saved successfully",
        "timestamp": datetime.now().isoformat()
    }


@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "weaponization_analysis",
        "events_total": len(analysis_system.events),
        "patterns_total": len(analysis_system.patterns),
        "timestamp": datetime.now().isoformat()
    }
