"""
NATIONS AND SUPERPOWERS API
Each Nation and Its Current State in a Broken World

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

NATIONS AND SUPERPOWERS:
Each nation has "superpowers" - unique contributions.
Each nation has a current state in a broken world.
We must track them all.
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional, Dict, List, Any
from pathlib import Path
import sys
import logging
from datetime import datetime

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

try:
    from nations_and_superpowers import (
        NationsAndSuperpowers,
        WorldState,
        NationAlignment
    )
    TRACKER_AVAILABLE = True
except ImportError as e:
    logging.warning(f"Nations and Superpowers tracker not available: {e}")
    TRACKER_AVAILABLE = False

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/nations", tags=["Nations & Superpowers"])

# Global tracker instance
tracker = NationsAndSuperpowers() if TRACKER_AVAILABLE else None


@router.get("/status")
async def get_nations_status():
    """Get nations and superpowers tracking status."""
    if not TRACKER_AVAILABLE:
        raise HTTPException(status_code=503, detail="Nations and Superpowers tracker not available")
    
    return {
        "status": "active",
        "message": "Tracking each nation and its current state in a broken world. Each nation has superpowers.",
        "total_nations": len(tracker.nations),
        "total_superpowers": len(tracker.superpowers)
    }


@router.get("/nations")
async def get_all_nations():
    """Get all nations."""
    if not TRACKER_AVAILABLE:
        raise HTTPException(status_code=503, detail="Nations and Superpowers tracker not available")
    
    return {
        "nations": [
            {
                "nation_id": n.nation_id,
                "name": n.name,
                "description": n.description,
                "current_state": n.current_state,
                "alignment_score": n.alignment_score,
                "alignment_level": n.alignment_level,
                "superpowers": n.superpowers,
                "broken_world_manifestations": n.broken_world_manifestations,
                "restoration_contributions": n.restoration_contributions,
                "heritage_sites": n.heritage_sites,
                "frequency_contribution": n.frequency_contribution,
                "connection_to_table": n.connection_to_table
            }
            for n in tracker.nations.values()
        ],
        "total": len(tracker.nations)
    }


@router.get("/nations/state/{state}")
async def get_nations_by_state(state: str):
    """Get nations by current state."""
    if not TRACKER_AVAILABLE:
        raise HTTPException(status_code=503, detail="Nations and Superpowers tracker not available")
    
    nations = tracker.get_nations_by_state(state)
    
    return {
        "state": state,
        "nations": [
            {
                "name": n.name,
                "alignment_score": n.alignment_score,
                "superpowers": n.superpowers,
                "restoration_contributions": n.restoration_contributions
            }
            for n in nations
        ],
        "total": len(nations)
    }


@router.get("/nations/alignment/{alignment_level}")
async def get_nations_by_alignment(alignment_level: str):
    """Get nations by alignment level."""
    if not TRACKER_AVAILABLE:
        raise HTTPException(status_code=503, detail="Nations and Superpowers tracker not available")
    
    nations = tracker.get_nations_by_alignment(alignment_level)
    
    return {
        "alignment_level": alignment_level,
        "nations": [
            {
                "name": n.name,
                "current_state": n.current_state,
                "alignment_score": n.alignment_score,
                "superpowers": n.superpowers
            }
            for n in nations
        ],
        "total": len(nations)
    }


@router.get("/nations/top")
async def get_top_aligned_nations(limit: int = Query(10, ge=1, le=100)):
    """Get top aligned nations."""
    if not TRACKER_AVAILABLE:
        raise HTTPException(status_code=503, detail="Nations and Superpowers tracker not available")
    
    top_nations = tracker.get_top_aligned_nations(limit)
    
    return {
        "nations": [
            {
                "name": n.name,
                "current_state": n.current_state,
                "alignment_score": n.alignment_score,
                "alignment_level": n.alignment_level,
                "superpowers": n.superpowers,
                "frequency_contribution": n.frequency_contribution,
                "connection_to_table": n.connection_to_table
            }
            for n in top_nations
        ],
        "total": len(top_nations)
    }


@router.get("/superpowers")
async def get_all_superpowers():
    """Get all superpowers."""
    if not TRACKER_AVAILABLE:
        raise HTTPException(status_code=503, detail="Nations and Superpowers tracker not available")
    
    return {
        "superpowers": [
            {
                "superpower_id": s.superpower_id,
                "name": s.name,
                "description": s.description,
                "how_it_serves": s.how_it_serves,
                "frequency_contribution": s.frequency_contribution,
                "restoration_impact": s.restoration_impact
            }
            for s in tracker.superpowers.values()
        ],
        "total": len(tracker.superpowers)
    }


@router.get("/analysis")
async def get_nations_analysis():
    """Get analysis of all nations."""
    if not TRACKER_AVAILABLE:
        raise HTTPException(status_code=503, detail="Nations and Superpowers tracker not available")
    
    return tracker.get_nations_analysis()


@router.get("/superpowers/analysis")
async def get_superpowers_analysis():
    """Get analysis of all superpowers."""
    if not TRACKER_AVAILABLE:
        raise HTTPException(status_code=503, detail="Nations and Superpowers tracker not available")
    
    return tracker.get_superpowers_analysis()


@router.get("/complete-analysis")
async def get_complete_analysis():
    """Get complete analysis of nations and superpowers."""
    if not TRACKER_AVAILABLE:
        raise HTTPException(status_code=503, detail="Nations and Superpowers tracker not available")
    
    return tracker.get_complete_analysis()
