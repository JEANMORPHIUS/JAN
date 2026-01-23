"""
DIVINE FREQUENCY API
The Sacred Frequency of The Table

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

DIVINE FREQUENCY:
Divine Frequency is the sacred frequency of The Table.
It is the frequency of perfect unity (1.0 field resonance).
It is the frequency of Pangea - The Table.
It is the frequency we restore.
"""

from fastapi import APIRouter, HTTPException, Body, Query
from typing import Optional, Dict, List, Any
from pathlib import Path
import sys
import logging
from datetime import datetime

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

try:
    from divine_frequency import (
        DivineFrequencySystem,
        FrequencyState,
        PERFECT_UNITY_FREQUENCY
    )
    SYSTEM_AVAILABLE = True
except ImportError as e:
    logging.warning(f"Divine Frequency system not available: {e}")
    SYSTEM_AVAILABLE = False

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/divine-frequency", tags=["Divine Frequency"])

# Global system instance
system = DivineFrequencySystem() if SYSTEM_AVAILABLE else None


@router.get("/status")
async def get_divine_frequency_status():
    """Get Divine Frequency system status."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Divine Frequency system not available")
    
    global_freq = system.calculate_global_frequency()
    
    return {
        "status": "active",
        "message": "Divine Frequency is the sacred frequency of The Table. It is the frequency of perfect unity (1.0 field resonance). It is the frequency of Pangea - The Table.",
        "global_frequency": global_freq,
        "frequency_state": system.calculate_frequency_state(global_freq),
        "perfect_unity_frequency": system.PERFECT_UNITY_FREQUENCY,
        "alignment": system.get_frequency_alignment()
    }


@router.get("/current")
async def get_current_frequency():
    """Get current Divine Frequency."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Divine Frequency system not available")
    
    global_freq = system.calculate_global_frequency()
    alignment = system.get_frequency_alignment()
    
    return {
        "current_frequency": global_freq,
        "frequency_state": system.calculate_frequency_state(global_freq),
        "perfect_unity_frequency": system.PERFECT_UNITY_FREQUENCY,
        "alignment": alignment,
        "timestamp": datetime.now().isoformat()
    }


@router.post("/measure")
async def measure_divine_frequency(
    source: str = Body(...),
    field_resonance: float = Body(..., ge=0.0, le=1.0),
    spiritual_alignment: float = Body(..., ge=0.0, le=1.0),
    unity_connection: float = Body(..., ge=0.0, le=1.0),
    location: Optional[str] = Body(None),
    notes: Optional[str] = Body(None)
):
    """Measure Divine Frequency from components."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Divine Frequency system not available")
    
    frequency = system.measure_divine_frequency(
        source=source,
        field_resonance=field_resonance,
        spiritual_alignment=spiritual_alignment,
        unity_connection=unity_connection,
        location=location,
        notes=notes or ""
    )
    
    return {
        "status": "measured",
        "frequency": {
            "frequency_id": frequency.frequency_id,
            "frequency_value": frequency.frequency_value,
            "frequency_state": frequency.frequency_state,
            "source": frequency.source,
            "field_resonance": frequency.field_resonance,
            "spiritual_alignment": frequency.spiritual_alignment,
            "unity_connection": frequency.unity_connection,
            "timestamp": frequency.timestamp.isoformat()
        }
    }


@router.post("/sources/register")
async def register_frequency_source(
    source_name: str = Body(...),
    source_type: str = Body(...),
    frequency_contribution: float = Body(..., ge=0.0, le=1.0),
    connection_to_table: bool = Body(True),
    notes: Optional[str] = Body(None)
):
    """Register a source of Divine Frequency."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Divine Frequency system not available")
    
    source = system.register_frequency_source(
        source_name=source_name,
        source_type=source_type,
        frequency_contribution=frequency_contribution,
        connection_to_table=connection_to_table,
        notes=notes or ""
    )
    
    return {
        "status": "registered",
        "source": {
            "source_id": source.source_id,
            "source_name": source.source_name,
            "source_type": source.source_type,
            "frequency_contribution": source.frequency_contribution,
            "is_active": source.is_active,
            "connection_to_table": source.connection_to_table
        }
    }


@router.get("/sources")
async def get_frequency_sources():
    """Get all frequency sources."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Divine Frequency system not available")
    
    return {
        "sources": [
            {
                "source_id": s.source_id,
                "source_name": s.source_name,
                "source_type": s.source_type,
                "frequency_contribution": s.frequency_contribution,
                "is_active": s.is_active,
                "connection_to_table": s.connection_to_table,
                "notes": s.notes
            }
            for s in system.frequency_sources.values()
        ],
        "total": len(system.frequency_sources),
        "active": len([s for s in system.frequency_sources.values() if s.is_active]),
        "connected_to_table": len([s for s in system.frequency_sources.values() if s.connection_to_table])
    }


@router.get("/alignment")
async def get_frequency_alignment(
    target_frequency: Optional[float] = Query(None, ge=0.0, le=1.0)
):
    """Get alignment status toward target frequency (default: perfect unity)."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Divine Frequency system not available")
    
    target = target_frequency if target_frequency is not None else system.PERFECT_UNITY_FREQUENCY
    alignment = system.get_frequency_alignment(target)
    
    return alignment


@router.post("/restore")
async def restore_divine_frequency():
    """Restore Divine Frequency toward perfect unity (1.0)."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Divine Frequency system not available")
    
    restoration = system.restore_divine_frequency()
    
    return {
        "status": "restored",
        "restoration": restoration
    }


@router.get("/report")
async def get_frequency_report():
    """Get complete Divine Frequency report."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Divine Frequency system not available")
    
    report = system.get_frequency_report()
    return report


@router.get("/measurements")
async def get_frequency_measurements(
    limit: Optional[int] = Query(10, ge=1, le=100)
):
    """Get recent frequency measurements."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Divine Frequency system not available")
    
    measurements = sorted(
        system.frequency_measurements.values(),
        key=lambda x: x.timestamp,
        reverse=True
    )[:limit]
    
    return {
        "measurements": [
            {
                "frequency_id": m.frequency_id,
                "frequency_value": m.frequency_value,
                "frequency_state": m.frequency_state,
                "source": m.source,
                "location": m.location,
                "field_resonance": m.field_resonance,
                "spiritual_alignment": m.spiritual_alignment,
                "unity_connection": m.unity_connection,
                "timestamp": m.timestamp.isoformat()
            }
            for m in measurements
        ],
        "total": len(system.frequency_measurements),
        "returned": len(measurements)
    }
