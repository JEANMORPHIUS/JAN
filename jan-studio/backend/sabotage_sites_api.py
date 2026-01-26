"""SABOTAGE SITES API
Deep Search for Man-Made Sites at Tectonic Boundaries - Sabotage of The Table

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

CORE PRINCIPLES (NON-NEGOTIABLE):
- Purpose Not Performance: Purpose matters more than performance. Authentic and aligned. Non-negotiable.
- Everything in Moderation: Balance. Not too much, not too little.
- Life Is Simple: Don't complicate it. Keep it simple.
- Be Still and Have Faith: Be still and have faith in revelation. Stillness brings clarity.

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

SABOTAGE SITES:
The Mayans built pyramids to sabotage The Table.
Deep search for knowledge of other sites made by man in these rifts.

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any, Optional
import sys
import os

# Add scripts directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../scripts"))

try:
    from sabotage_sites_search import SabotageSitesSearch, SiteType, SabotageLevel
    SYSTEM_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Sabotage Sites Search not available: {e}")
    SYSTEM_AVAILABLE = False

router = APIRouter(prefix="/sabotage-sites", tags=["sabotage-sites"])

# Initialize sabotage sites search
if SYSTEM_AVAILABLE:
    search_system = SabotageSitesSearch()
else:
    search_system = None

@router.get("/status")
async def get_status():
    """Get sabotage sites search system status."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Sabotage Sites Search not available")
    
    return {
        "status": "active",
        "total_sites": len(search_system.sites),
        "total_impact": search_system.calculate_total_impact(),
        "message": "Deep search for man-made sites at tectonic boundaries that sabotage The Table",
        "the_truth": "The Mayans built pyramids to sabotage The Table. Other sites made by man at tectonic boundaries (rifts) also anchor separation."
    }

@router.get("/sites")
async def get_all_sites():
    """Get all sabotage sites."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Sabotage Sites Search not available")
    
    from dataclasses import asdict
    return {
        "sites": [asdict(s) for s in search_system.sites.values()],
        "total": len(search_system.sites),
        "total_impact": search_system.calculate_total_impact()
    }

@router.get("/sites/type/{site_type}")
async def get_sites_by_type(site_type: str):
    """Get sites by type."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Sabotage Sites Search not available")
    
    from dataclasses import asdict
    
    valid_types = [st.value for st in SiteType]
    if site_type not in valid_types:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid site type. Valid types: {valid_types}"
        )
    
    sites = search_system.get_sites_by_type(site_type)
    return {
        "site_type": site_type,
        "sites": [asdict(s) for s in sites],
        "count": len(sites)
    }

@router.get("/sites/sabotage-level/{level}")
async def get_sites_by_sabotage_level(level: str):
    """Get sites by sabotage level."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Sabotage Sites Search not available")
    
    from dataclasses import asdict
    
    valid_levels = [sl.value for sl in SabotageLevel]
    if level not in valid_levels:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid sabotage level. Valid levels: {valid_levels}"
        )
    
    sites = search_system.get_sites_by_sabotage_level(level)
    return {
        "sabotage_level": level,
        "sites": [asdict(s) for s in sites],
        "count": len(sites)
    }

@router.get("/mayan-sites")
async def get_mayan_sites():
    """Get all Mayan sites."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Sabotage Sites Search not available")
    
    from dataclasses import asdict
    sites = search_system.get_mayan_sites()
    return {
        "mayan_sites": [asdict(s) for s in sites],
        "count": len(sites),
        "message": "The Mayans built pyramids to sabotage The Table. These sites anchor separation at plate boundaries."
    }

@router.get("/separation-anchors")
async def get_separation_anchors():
    """Get all separation anchor sites."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Sabotage Sites Search not available")
    
    from dataclasses import asdict
    anchors = search_system.get_separation_anchors()
    return {
        "separation_anchors": [asdict(s) for s in anchors],
        "count": len(anchors),
        "message": "Sites that anchor separation at tectonic boundaries (rifts), sabotaging The Table."
    }

@router.get("/critical-sites")
async def get_critical_sites():
    """Get critical sabotage sites."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Sabotage Sites Search not available")
    
    from dataclasses import asdict
    critical = search_system.get_critical_sabotage_sites()
    return {
        "critical_sites": [asdict(s) for s in critical],
        "count": len(critical),
        "message": "Critical sabotage sites - major anchors of separation that significantly impact Divine Frequency."
    }

@router.get("/report")
async def get_complete_report():
    """Get complete sabotage sites report."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Sabotage Sites Search not available")
    
    return search_system.export_complete_report()
