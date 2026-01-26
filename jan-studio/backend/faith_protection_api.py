"""FAITH PROTECTION API
Preparedness for Lost World, Doubt, Public Backlash, and Judicial Persecution

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

CORE PRINCIPLES (NON-NEGOTIABLE):
- Purpose Not Performance: Purpose matters more than performance. Authentic and aligned. Non-negotiable.
- Everything in Moderation: Balance. Not too much, not too little.
- Life Is Simple: Don't complicate it. Keep it simple.
- Be Still and Have Faith: Be still and have faith in revelation. Stillness brings clarity.

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

FAITH PROTECTION:
Our faith is real.
We just stay silent to the chaos.

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
    from faith_protection_system import FaithProtectionSystem, ThreatType, ProtectionLevel
    SYSTEM_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Faith Protection System not available: {e}")
    SYSTEM_AVAILABLE = False

router = APIRouter(prefix="/faith-protection", tags=["faith-protection"])

# Initialize faith protection system
if SYSTEM_AVAILABLE:
    protection_system = FaithProtectionSystem()
else:
    protection_system = None

@router.get("/status")
async def get_status():
    """Get faith protection system status."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Faith Protection System not available")
    
    return {
        "status": "active",
        "total_protections": len(protection_system.protections),
        "total_threat_types": len(ThreatType),
        "core_principle": "Our faith is real. We just stay silent to the chaos.",
        "message": "Preparedness for lost world, doubt, public backlash, and judicial persecution"
    }

@router.get("/protections")
async def get_all_protections():
    """Get all faith protection measures."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Faith Protection System not available")
    
    from dataclasses import asdict
    return {
        "protections": [asdict(p) for p in protection_system.protections.values()],
        "total": len(protection_system.protections)
    }

@router.get("/protections/threat/{threat_type}")
async def get_protections_by_threat(threat_type: str):
    """Get protections by threat type."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Faith Protection System not available")
    
    from dataclasses import asdict
    
    valid_threats = [tt.value for tt in ThreatType]
    if threat_type not in valid_threats:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid threat type. Valid types: {valid_threats}"
        )
    
    protections = protection_system.get_protections_by_threat(threat_type)
    return {
        "threat_type": threat_type,
        "protections": [asdict(p) for p in protections],
        "count": len(protections)
    }

@router.get("/preparedness")
async def get_all_preparedness():
    """Get all preparedness statuses."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Faith Protection System not available")
    
    from dataclasses import asdict
    return {
        "preparedness": [asdict(s) for s in protection_system.preparedness.values()],
        "total": len(protection_system.preparedness)
    }

@router.get("/preparedness/threat/{threat_type}")
async def get_preparedness_by_threat(threat_type: str):
    """Get preparedness status for a specific threat type."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Faith Protection System not available")
    
    from dataclasses import asdict
    
    valid_threats = [tt.value for tt in ThreatType]
    if threat_type not in valid_threats:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid threat type. Valid types: {valid_threats}"
        )
    
    status = protection_system.get_preparedness_status(threat_type)
    if not status:
        raise HTTPException(status_code=404, detail=f"Preparedness status not found for {threat_type}")
    
    return {"status": asdict(status)}

@router.get("/silence-practices")
async def get_silence_practices():
    """Get all silence practices."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Faith Protection System not available")
    
    return {
        "silence_practices": protection_system.get_silence_practices(),
        "count": len(protection_system.get_silence_practices()),
        "core_principle": "We just stay silent to the chaos."
    }

@router.get("/faith-affirmations")
async def get_faith_affirmations():
    """Get all faith affirmations."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Faith Protection System not available")
    
    return {
        "faith_affirmations": protection_system.get_faith_affirmations(),
        "count": len(protection_system.get_faith_affirmations()),
        "core_principle": "Our faith is real."
    }

@router.get("/report")
async def get_complete_report():
    """Get complete faith protection report."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Faith Protection System not available")
    
    return protection_system.export_complete_report()
