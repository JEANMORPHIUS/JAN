"""Heritage Meridian API
Mobile app endpoints for Heritage Meridian System and 7 Wonders

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity


PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any
import json
from pathlib import Path

router = APIRouter(prefix="/api/heritage-meridian", tags=["heritage-meridian"])

# Load heritage meridian data
HERITAGE_DATA_PATH = Path(__file__).parent.parent.parent / "data" / "heritage_meridian" / "heritage_meridian_data.json"
WONDERS_DATA_PATH = Path(__file__).parent.parent.parent / "data" / "heritage_meridian" / "new_7_wonders_data.json"


def load_heritage_data() -> Dict[str, Any]:
    """Load heritage meridian data."""
    try:
        with open(HERITAGE_DATA_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def load_wonders_data() -> Dict[str, Any]:
    """Load 7 Wonders data."""
    try:
        with open(WONDERS_DATA_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


@router.get("/status")
async def get_status():
    """API status check."""
    return {
        "status": "active",
        "message": "Heritage Meridian API is operational",
        "mission": "THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS"
    }


@router.get("/pillars")
async def get_pillars():
    """Get all Seven Pillars."""
    data = load_heritage_data()
    pillars = data.get("the_seven_pillars", {}).get("pillars", [])
    return {
        "pillars": pillars,
        "total": len(pillars)
    }


@router.get("/pillars/{pillar_id}")
async def get_pillar(pillar_id: str):
    """Get single pillar details."""
    data = load_heritage_data()
    pillars = data.get("the_seven_pillars", {}).get("pillars", [])
    
    pillar = next((p for p in pillars if p.get("pillar_id") == pillar_id), None)
    if not pillar:
        raise HTTPException(status_code=404, detail=f"Pillar {pillar_id} not found")
    
    return pillar


@router.get("/wonders")
async def get_wonders():
    """Get all 7 Wonders."""
    data = load_wonders_data()
    wonders = data.get("new_7_wonders_of_the_world", {}).get("wonders", [])
    return {
        "wonders": wonders,
        "total": len(wonders)
    }


@router.get("/wonders/{wonder_id}")
async def get_wonder(wonder_id: str):
    """Get single wonder details."""
    data = load_wonders_data()
    wonders = data.get("new_7_wonders_of_the_world", {}).get("wonders", [])
    
    wonder = next((w for w in wonders if w.get("wonder_id") == wonder_id), None)
    if not wonder:
        raise HTTPException(status_code=404, detail=f"Wonder {wonder_id} not found")
    
    return wonder


@router.get("/meridians")
async def get_meridians():
    """Get all meridian connections."""
    data = load_heritage_data()
    meridians = data.get("ancient_meridian_system", {}).get("primary_meridians", [])
    return {
        "meridians": meridians,
        "total": len(meridians)
    }


@router.get("/network-health")
async def get_network_health():
    """Get global resonance network health."""
    data = load_heritage_data()
    
    # Calculate network health from pillars
    pillars = data.get("the_seven_pillars", {}).get("pillars", [])
    if not pillars:
        return {
            "health": "unknown",
            "average_resonance": 0.0,
            "total_nodes": 0
        }
    
    total_resonance = sum(p.get("field_resonance", 0.0) for p in pillars)
    average_resonance = total_resonance / len(pillars) if pillars else 0.0
    
    # Determine health status
    if average_resonance >= 0.90:
        health = "excellent"
    elif average_resonance >= 0.80:
        health = "good"
    elif average_resonance >= 0.70:
        health = "moderate"
    else:
        health = "needs_attention"
    
    return {
        "health": health,
        "average_resonance": round(average_resonance, 2),
        "total_nodes": len(pillars),
        "mission": "THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS"
    }


@router.get("/7-wonders/list")
async def get_7_wonders_list():
    """Get all 7 Wonders (alternative endpoint)."""
    return await get_wonders()


@router.get("/7-wonders/{wonder_id}")
async def get_7_wonder(wonder_id: str):
    """Get single wonder (alternative endpoint)."""
    return await get_wonder(wonder_id)


@router.get("/7-wonders/{wonder_id}/resonance")
async def get_wonder_resonance(wonder_id: str):
    """Get wonder's field resonance."""
    wonder = await get_wonder(wonder_id)
    return {
        "wonder_id": wonder_id,
        "resonance": wonder.get("field_resonance", 0.0),
        "field_resonance": wonder.get("field_resonance", 0.0)
    }


@router.get("/7-wonders/{wonder_id}/meridian-connections")
async def get_wonder_meridian_connections(wonder_id: str):
    """Get wonder's meridian connections."""
    wonder = await get_wonder(wonder_id)
    return {
        "wonder_id": wonder_id,
        "connections": wonder.get("meridian_connections", []),
        "meridian_connections": wonder.get("meridian_connections", [])
    }
