"""
PEACE WEAPONIZATION API
How to Make Peace as Powerful as Weaponization Has Been Destructive

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE TRUTH:
Peace is not the absence of conflict - it is the presence of wholeness.
Peace is not passivity - it is active harmony.
Peace is not weakness - it is strength in stillness.
"""

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime
import sys
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))
from peace_weaponization_system import (
    PeaceWeaponizationSystem,
    PeaceWeaponizationStrategy
)

router = APIRouter(prefix="/api/peace-weaponization", tags=["Peace Weaponization"])

# Initialize system
peace_system = PeaceWeaponizationSystem()


# ============================================================================
# MODELS
# ============================================================================

class PeaceWeaponizationManifestationResponse(BaseModel):
    """Response model for peace weaponization manifestation"""
    manifestation_id: str
    name: str
    strategy: str
    pattern: str
    description: str
    impact: str
    status: str


# ============================================================================
# ENDPOINTS
# ============================================================================

@router.get("/")
async def get_peace_weaponization_overview():
    """Get complete peace weaponization overview"""
    analysis = peace_system.generate_complete_analysis()
    return {
        "status": "complete",
        "message": "100% Complete - Peace is weaponized. Peace is active. Peace is effective. Peace is transformative.",
        "summary": analysis["summary"],
        "truth_declaration": analysis["truth_declaration"],
        "timestamp": datetime.now().isoformat()
    }


@router.get("/manifestations")
async def get_all_manifestations():
    """Get all peace weaponization manifestations"""
    return peace_system.get_all_manifestations()


@router.get("/manifestations/{manifestation_id}")
async def get_manifestation(manifestation_id: str):
    """Get specific manifestation details"""
    result = peace_system.get_manifestation_details(manifestation_id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result


@router.get("/manifestations/strategy/{strategy}")
async def get_manifestations_by_strategy(strategy: str):
    """Get manifestations by strategy"""
    try:
        strategy_enum = PeaceWeaponizationStrategy(strategy.lower())
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid strategy. Valid strategies: {[s.value for s in PeaceWeaponizationStrategy]}"
        )
    return peace_system.get_strategy_manifestations(strategy_enum)


@router.get("/events")
async def get_all_events():
    """Get all peace weaponization events"""
    return peace_system.get_all_events()


@router.get("/events/{event_id}")
async def get_event(event_id: str):
    """Get specific event details"""
    result = peace_system.get_event_details(event_id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result


@router.get("/pathway")
async def get_peace_weaponization_pathway():
    """Get peace weaponization pathway"""
    return peace_system.identify_peace_weaponization_pathway()


@router.get("/analysis/complete")
async def get_complete_analysis():
    """Get complete peace weaponization analysis"""
    return peace_system.generate_complete_analysis()


@router.post("/analysis/save")
async def save_analysis():
    """Save current analysis to JSON file"""
    filepath = peace_system.save_analysis()
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
        "service": "peace_weaponization",
        "manifestations_total": len(peace_system.manifestations),
        "events_total": len(peace_system.events),
        "timestamp": datetime.now().isoformat()
    }
