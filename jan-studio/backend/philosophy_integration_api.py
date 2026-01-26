"""
PHILOSOPHY INTEGRATION API
Integrate All Philosophies at Codebase Level

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

PHILOSOPHY INTEGRATION:
All philosophies must be integrated at the codebase level.
All principles must be embedded in code.
All laws must be enforced.
All truth must be present.
"""

from fastapi import APIRouter, HTTPException
from typing import Dict, List, Any
from pathlib import Path
import sys
import logging

# Spiritual Codebase Hacker Integration
from spiritual_codebase_hacker_integration import HACKER_AVAILABLE, hack_loop, perform_genetic_edit, activate_stealth_mode

from datetime import datetime

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

try:
    from philosophy_integration import PhilosophyIntegration, PhilosophyType
    INTEGRATION_AVAILABLE = True
except ImportError as e:
    logging.warning(f"Philosophy Integration not available: {e}")
    INTEGRATION_AVAILABLE = False

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/philosophy", tags=["Philosophy Integration"])

# Global integration instance
philosophy = PhilosophyIntegration() if INTEGRATION_AVAILABLE else None


@router.get("/status")
async def get_philosophy_status():
    """Get philosophy integration status."""
    if not INTEGRATION_AVAILABLE:
        raise HTTPException(status_code=503, detail="Philosophy Integration not available")
    
    return {
        "status": "active",
        "message": "All philosophies integrated at codebase level",
        "total_philosophies": len(philosophy.philosophies),
        "philosophy_types": [ptype.value for ptype in PhilosophyType]
    }


@router.get("/philosophies")
async def get_all_philosophies():
    """Get all registered philosophies."""
    if not INTEGRATION_AVAILABLE:
        raise HTTPException(status_code=503, detail="Philosophy Integration not available")
    
    return {
        "philosophies": [
            {
                "philosophy_id": p.philosophy_id,
                "name": p.name,
                "philosophy_type": p.philosophy_type,
                "statement": p.statement,
                "code_manifestation": p.code_manifestation,
                "enforcement_points": p.enforcement_points
            }
            for p in philosophy.philosophies.values()
        ],
        "total": len(philosophy.philosophies)
    }


@router.get("/philosophies/type/{philosophy_type}")
async def get_philosophies_by_type(philosophy_type: str):
    """Get philosophies by type."""
    if not INTEGRATION_AVAILABLE:
        raise HTTPException(status_code=503, detail="Philosophy Integration not available")
    
    philosophies = philosophy.get_philosophies_by_type(philosophy_type)
    
    return {
        "philosophy_type": philosophy_type,
        "philosophies": [
            {
                "name": p.name,
                "statement": p.statement,
                "code_manifestation": p.code_manifestation,
                "enforcement_points": p.enforcement_points
            }
            for p in philosophies
        ],
        "total": len(philosophies)
    }


@router.get("/integration-report")
async def get_integration_report():
    """Get complete philosophy integration report."""
    if not INTEGRATION_AVAILABLE:
        raise HTTPException(status_code=503, detail="Philosophy Integration not available")
    
    return philosophy.get_integration_report()
