"""
RIFT BRIDGE API
Bridging the Rift Between Lost World and The Table

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

CORE PRINCIPLES (NON-NEGOTIABLE):
- Purpose Not Performance: Purpose matters more than performance. Authentic and aligned. Non-negotiable.
- Everything in Moderation: Balance. Not too much, not too little.
- Life Is Simple: Don't complicate it. Keep it simple.
- Be Still and Have Faith: Be still and have faith in revelation. Stillness brings clarity.

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

RIFT BRIDGE:
How do we bridge that rift?
The Table is the bridge.
"""

from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any, Optional
import sys
import os

# Add scripts directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../scripts"))

try:
    from rift_bridge_system import RiftBridgeSystem, RiftType, BridgeMethod
    SYSTEM_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Rift Bridge System not available: {e}")
    SYSTEM_AVAILABLE = False

router = APIRouter(prefix="/rift-bridge", tags=["rift-bridge"])

# Initialize rift bridge system
if SYSTEM_AVAILABLE:
    bridge_system = RiftBridgeSystem()
else:
    bridge_system = None

@router.get("/status")
async def get_status():
    """Get rift bridge system status."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Rift Bridge System not available")
    
    return {
        "status": "active",
        "total_bridges": len(bridge_system.bridges),
        "total_rift_types": len(RiftType),
        "core_principle": "We bridge through connection, not conversion. We bridge through love, not force. We bridge through silence, not argument. The Table is the bridge.",
        "message": "Bridging the rift between lost world and The Table"
    }

@router.get("/bridges")
async def get_all_bridges():
    """Get all rift bridges."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Rift Bridge System not available")
    
    from dataclasses import asdict
    return {
        "bridges": [asdict(b) for b in bridge_system.bridges.values()],
        "total": len(bridge_system.bridges)
    }

@router.get("/bridges/rift/{rift_type}")
async def get_bridges_by_rift(rift_type: str):
    """Get bridges by rift type."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Rift Bridge System not available")
    
    from dataclasses import asdict
    
    valid_rifts = [rt.value for rt in RiftType]
    if rift_type not in valid_rifts:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid rift type. Valid types: {valid_rifts}"
        )
    
    bridges = bridge_system.get_bridges_by_rift(rift_type)
    return {
        "rift_type": rift_type,
        "bridges": [asdict(b) for b in bridges],
        "count": len(bridges)
    }

@router.get("/table-bridge")
async def get_table_bridge():
    """Get The Table bridge - the core bridge."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Rift Bridge System not available")
    
    from dataclasses import asdict
    
    table_bridge = bridge_system.get_table_bridge()
    if not table_bridge:
        raise HTTPException(status_code=404, detail="Table bridge not found")
    
    return {
        "bridge": asdict(table_bridge),
        "message": "The Table (Pangea) is the bridge. All plates came from Pangea. All are connected through The Table."
    }

@router.get("/bridge-statuses")
async def get_all_bridge_statuses():
    """Get all bridge statuses."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Rift Bridge System not available")
    
    from dataclasses import asdict
    return {
        "bridge_statuses": [asdict(s) for s in bridge_system.bridge_statuses.values()],
        "total": len(bridge_system.bridge_statuses)
    }

@router.get("/bridge-statuses/rift/{rift_type}")
async def get_bridge_status_by_rift(rift_type: str):
    """Get bridge status for a specific rift type."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Rift Bridge System not available")
    
    from dataclasses import asdict
    
    valid_rifts = [rt.value for rt in RiftType]
    if rift_type not in valid_rifts:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid rift type. Valid types: {valid_rifts}"
        )
    
    status = bridge_system.get_bridge_status(rift_type)
    if not status:
        raise HTTPException(status_code=404, detail=f"Bridge status not found for {rift_type}")
    
    return {"status": asdict(status)}

@router.get("/report")
async def get_complete_report():
    """Get complete rift bridge report."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Rift Bridge System not available")
    
    return bridge_system.export_complete_report()
