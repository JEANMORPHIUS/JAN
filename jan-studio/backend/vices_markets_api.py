"""
VICES AND MARKETS API
Tracking Vices, Financial Markets, and The Inbetween (Field Space)

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

VICES:
Vices are patterns that exploit, control, or drain energy.
They are frequency dampeners.
We must track them all.

MARKETS:
Markets (stocks, ETFs, crypto) are systems.
They can be vices (exploitation, control).
They can be tools (if aligned with The Table).
We must understand them.

THE INBETWEEN (Field Space):
The "Everything In Between" - where transformation happens.
The space between heritage sites.
The space between moments.
The space where energy flows.
We must map it.
"""

from fastapi import APIRouter, HTTPException, Body, Query
from typing import Optional, Dict, List, Any
from pathlib import Path
import sys
import logging

# Spiritual Codebase Hacker Integration
from spiritual_codebase_hacker_integration import HACKER_AVAILABLE, hack_loop, perform_genetic_edit, activate_stealth_mode

from datetime import datetime

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

try:
    from vices_and_markets_tracker import (
        VicesAndMarketsTracker,
        ViceType,
        MarketType,
        FieldSpaceType
    )
    TRACKER_AVAILABLE = True
except ImportError as e:
    logging.warning(f"Vices and Markets tracker not available: {e}")
    TRACKER_AVAILABLE = False

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/vices-markets", tags=["Vices & Markets"])

# Global tracker instance
tracker = VicesAndMarketsTracker() if TRACKER_AVAILABLE else None


@router.get("/status")
async def get_vices_markets_status():
    """Get vices and markets tracking status."""
    if not TRACKER_AVAILABLE:
        raise HTTPException(status_code=503, detail="Vices and Markets tracker not available")
    
    return {
        "status": "active",
        "message": "Tracking vices, markets, and Field Space (The Inbetween)",
        "vices": len(tracker.vices),
        "markets": len(tracker.markets),
        "field_spaces": len(tracker.field_spaces)
    }


@router.post("/vices/register")
async def register_vice(
    name: str = Body(...),
    vice_type: str = Body(...),
    description: str = Body(...),
    how_it_exploits: str = Body(...),
    frequency_impact: float = Body(..., le=0.0),  # Negative impact
    static_generated: Optional[List[str]] = Body(None),
    notes: Optional[str] = Body(None)
):
    """Register a vice (exploitation pattern, frequency dampener)."""
    if not TRACKER_AVAILABLE:
        raise HTTPException(status_code=503, detail="Vices and Markets tracker not available")
    
    vice = tracker.register_vice(
        name=name,
        vice_type=vice_type,
        description=description,
        how_it_exploits=how_it_exploits,
        frequency_impact=frequency_impact,
        static_generated=static_generated,
        notes=notes or ""
    )
    
    return {
        "status": "registered",
        "vice": {
            "vice_id": vice.vice_id,
            "name": vice.name,
            "vice_type": vice.vice_type,
            "frequency_impact": vice.frequency_impact
        }
    }


@router.get("/vices")
async def get_vices():
    """Get all registered vices."""
    if not TRACKER_AVAILABLE:
        raise HTTPException(status_code=503, detail="Vices and Markets tracker not available")
    
    return {
        "vices": [
            {
                "vice_id": v.vice_id,
                "name": v.name,
                "vice_type": v.vice_type,
                "description": v.description,
                "how_it_exploits": v.how_it_exploits,
                "frequency_impact": v.frequency_impact,
                "static_generated": v.static_generated
            }
            for v in tracker.vices.values()
        ],
        "total": len(tracker.vices),
        "analysis": tracker.analyze_vice_impact_on_frequency()
    }


@router.post("/markets/register")
async def register_market(
    name: str = Body(...),
    market_type: str = Body(...),
    symbol: Optional[str] = Body(None),
    description: Optional[str] = Body(None),
    is_vice: bool = Body(False),
    vice_patterns: Optional[List[str]] = Body(None),
    connection_to_table: bool = Body(False),
    frequency_impact: float = Body(0.0),
    notes: Optional[str] = Body(None)
):
    """Register a financial market."""
    if not TRACKER_AVAILABLE:
        raise HTTPException(status_code=503, detail="Vices and Markets tracker not available")
    
    market = tracker.register_market(
        name=name,
        market_type=market_type,
        symbol=symbol,
        description=description or "",
        is_vice=is_vice,
        vice_patterns=vice_patterns,
        connection_to_table=connection_to_table,
        frequency_impact=frequency_impact,
        notes=notes or ""
    )
    
    return {
        "status": "registered",
        "market": {
            "market_id": market.market_id,
            "name": market.name,
            "market_type": market.market_type,
            "is_vice": market.is_vice,
            "connection_to_table": market.connection_to_table
        }
    }


@router.get("/markets")
async def get_markets():
    """Get all registered markets."""
    if not TRACKER_AVAILABLE:
        raise HTTPException(status_code=503, detail="Vices and Markets tracker not available")
    
    return {
        "markets": [
            {
                "market_id": m.market_id,
                "name": m.name,
                "market_type": m.market_type,
                "symbol": m.symbol,
                "is_vice": m.is_vice,
                "vice_patterns": m.vice_patterns,
                "connection_to_table": m.connection_to_table,
                "frequency_impact": m.frequency_impact
            }
            for m in tracker.markets.values()
        ],
        "total": len(tracker.markets),
        "analysis": tracker.analyze_market_alignment()
    }


@router.post("/field-spaces/register")
async def register_field_space(
    name: str = Body(...),
    fieldspace_type: str = Body(...),
    description: str = Body(...),
    location: Optional[str] = Body(None),
    connects_from: Optional[List[str]] = Body(None),
    connects_to: Optional[List[str]] = Body(None),
    energy_flow: float = Body(0.0, ge=0.0, le=1.0),
    transformation_potential: float = Body(0.0, ge=0.0, le=1.0),
    notes: Optional[str] = Body(None)
):
    """Register Field Space - The Inbetween."""
    if not TRACKER_AVAILABLE:
        raise HTTPException(status_code=503, detail="Vices and Markets tracker not available")
    
    fieldspace = tracker.register_field_space(
        name=name,
        fieldspace_type=fieldspace_type,
        description=description,
        location=location,
        connects_from=connects_from,
        connects_to=connects_to,
        energy_flow=energy_flow,
        transformation_potential=transformation_potential,
        notes=notes or ""
    )
    
    return {
        "status": "registered",
        "field_space": {
            "fieldspace_id": fieldspace.fieldspace_id,
            "name": fieldspace.name,
            "fieldspace_type": fieldspace.fieldspace_type,
            "energy_flow": fieldspace.energy_flow,
            "transformation_potential": fieldspace.transformation_potential
        }
    }


@router.get("/field-spaces")
async def get_field_spaces():
    """Get all registered Field Spaces (The Inbetween)."""
    if not TRACKER_AVAILABLE:
        raise HTTPException(status_code=503, detail="Vices and Markets tracker not available")
    
    return {
        "field_spaces": [
            {
                "fieldspace_id": fs.fieldspace_id,
                "name": fs.name,
                "fieldspace_type": fs.fieldspace_type,
                "description": fs.description,
                "location": fs.location,
                "connects_from": fs.connects_from,
                "connects_to": fs.connects_to,
                "energy_flow": fs.energy_flow,
                "transformation_potential": fs.transformation_potential
            }
            for fs in tracker.field_spaces.values()
        ],
        "total": len(tracker.field_spaces),
        "analysis": tracker.analyze_field_space_network()
    }


@router.get("/analysis")
async def get_complete_analysis():
    """Get complete analysis of vices, markets, and Field Space."""
    if not TRACKER_AVAILABLE:
        raise HTTPException(status_code=503, detail="Vices and Markets tracker not available")
    
    return tracker.get_complete_analysis()


@router.get("/vices/impact")
async def get_vice_impact():
    """Get analysis of how vices impact Divine Frequency."""
    if not TRACKER_AVAILABLE:
        raise HTTPException(status_code=503, detail="Vices and Markets tracker not available")
    
    return tracker.analyze_vice_impact_on_frequency()


@router.get("/markets/alignment")
async def get_market_alignment():
    """Get analysis of market alignment with The Table."""
    if not TRACKER_AVAILABLE:
        raise HTTPException(status_code=503, detail="Vices and Markets tracker not available")
    
    return tracker.analyze_market_alignment()


@router.get("/field-spaces/network")
async def get_field_space_network():
    """Get analysis of Field Space network (The Inbetween)."""
    if not TRACKER_AVAILABLE:
        raise HTTPException(status_code=503, detail="Vices and Markets tracker not available")
    
    return tracker.analyze_field_space_network()
