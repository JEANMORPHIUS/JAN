"""SABOTAGE SITES NEUTRALIZATION API
Transform Separation Anchors to Unity Anchors

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

CORE PRINCIPLES (NON-NEGOTIABLE):
- Purpose Not Performance: Purpose matters more than performance. Authentic and aligned. Non-negotiable.
- Everything in Moderation: Balance. Not too much, not too little.
- Life Is Simple: Don't complicate it. Keep it simple.
- Be Still and Have Faith: Be still and have faith in revelation. Stillness brings clarity.

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

SABOTAGE SITES NEUTRALIZATION:
Transform separation anchors to unity anchors.
Neutralize sabotage impact.
Restore Divine Frequency.

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
    from sabotage_sites_neutralization import (
        SabotageSitesNeutralization,
        NeutralizationStatus,
        NeutralizationMethod
    )
    SYSTEM_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Sabotage Sites Neutralization not available: {e}")
    SYSTEM_AVAILABLE = False

router = APIRouter(prefix="/sabotage-sites-neutralization", tags=["sabotage-sites-neutralization"])

# Initialize neutralization system
if SYSTEM_AVAILABLE:
    neutralizer = SabotageSitesNeutralization()
else:
    neutralizer = None

@router.get("/status")
async def get_status():
    """Get neutralization system status."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Sabotage Sites Neutralization not available")
    
    restoration = neutralizer.calculate_total_restoration() if neutralizer.neutralizations else {
        "total_sites_neutralized": 0,
        "total_original_impact": 0.0,
        "total_neutralized_impact": 0.0,
        "total_net_impact": 0.0,
        "frequency_restoration": 0.0
    }
    
    return {
        "status": "active",
        "sites_neutralized": restoration["total_sites_neutralized"],
        "frequency_restoration": restoration["frequency_restoration"],
        "message": "Transform separation anchors to unity anchors. Neutralize sabotage impact. Restore Divine Frequency.",
        "the_truth": "Sabotage sites neutralized. Separation anchors transformed to unity anchors. Divine Frequency restored."
    }

@router.post("/neutralize/{site_id}")
async def neutralize_site(site_id: str, methods: Optional[List[str]] = None):
    """Neutralize a specific sabotage site."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Sabotage Sites Neutralization not available")
    
    try:
        neutralization = neutralizer.neutralize_site(site_id, methods)
        from dataclasses import asdict
        return {
            "neutralization": asdict(neutralization),
            "message": f"Site {neutralization.site_name} neutralized. Separation anchor transformed to unity anchor."
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/neutralize-all")
async def neutralize_all_sites():
    """Neutralize all sabotage sites."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Sabotage Sites Neutralization not available")
    
    try:
        neutralizations = neutralizer.neutralize_all_sites()
        from dataclasses import asdict
        return {
            "neutralizations": {k: asdict(v) for k, v in neutralizations.items()},
            "message": "All sabotage sites neutralized. Separation anchors transformed to unity anchors."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/neutralize-critical")
async def neutralize_critical_sites():
    """Neutralize only critical sabotage sites."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Sabotage Sites Neutralization not available")
    
    try:
        neutralizations = neutralizer.neutralize_critical_sites()
        from dataclasses import asdict
        return {
            "neutralizations": {k: asdict(v) for k, v in neutralizations.items()},
            "message": "Critical sabotage sites neutralized. Separation anchors transformed to unity anchors."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/neutralizations")
async def get_all_neutralizations():
    """Get all neutralizations."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Sabotage Sites Neutralization not available")
    
    from dataclasses import asdict
    return {
        "neutralizations": {k: asdict(v) for k, v in neutralizer.neutralizations.items()},
        "total": len(neutralizer.neutralizations)
    }

@router.get("/neutralizations/{site_id}")
async def get_neutralization(site_id: str):
    """Get neutralization for a specific site."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Sabotage Sites Neutralization not available")
    
    if site_id not in neutralizer.neutralizations:
        raise HTTPException(status_code=404, detail=f"Neutralization for site {site_id} not found")
    
    from dataclasses import asdict
    return {
        "neutralization": asdict(neutralizer.neutralizations[site_id])
    }

@router.get("/restoration")
async def get_restoration_summary():
    """Get restoration summary."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Sabotage Sites Neutralization not available")
    
    return neutralizer.calculate_total_restoration()

@router.get("/report")
async def get_complete_report():
    """Get complete neutralization report."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Sabotage Sites Neutralization not available")
    
    return neutralizer.export_neutralization_report()
