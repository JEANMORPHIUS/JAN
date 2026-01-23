"""
GLOBAL SERVICE DISCOVERY API
Deep Search Algorithm for Existing Utilities and Services Globally

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

GLOBAL SERVICE DISCOVERY:
Deep search algorithm for existing utilities and services globally.
Find aligned services.
Integrate them.
Align them fully with The Table.
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
    from global_service_discovery import (
        GlobalServiceDiscovery,
        ServiceCategory,
        DiscoverySource
    )
    DISCOVERY_AVAILABLE = True
except ImportError as e:
    logging.warning(f"Global Service Discovery not available: {e}")
    DISCOVERY_AVAILABLE = False

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/global-services", tags=["Global Service Discovery"])

# Global discovery instance
discovery = GlobalServiceDiscovery() if DISCOVERY_AVAILABLE else None


@router.get("/status")
async def get_discovery_status():
    """Get global service discovery status."""
    if not DISCOVERY_AVAILABLE:
        raise HTTPException(status_code=503, detail="Global Service Discovery not available")
    
    return {
        "status": "active",
        "message": "Deep search for existing utilities and services globally. Align them fully with The Table.",
        "total_services": len(discovery.discovered_services),
        "aligned_services": len(discovery.get_aligned_services(0.8))
    }


@router.get("/services")
async def get_all_services():
    """Get all discovered services."""
    if not DISCOVERY_AVAILABLE:
        raise HTTPException(status_code=503, detail="Global Service Discovery not available")
    
    return {
        "services": [
            {
                "service_id": s.service_id,
                "name": s.name,
                "category": s.category,
                "description": s.description,
                "source": s.source,
                "url": s.url,
                "alignment_score": s.alignment_score,
                "alignment_indicators": s.alignment_indicators,
                "how_to_align": s.how_to_align
            }
            for s in discovery.discovered_services.values()
        ],
        "total": len(discovery.discovered_services)
    }


@router.get("/services/aligned")
async def get_aligned_services(min_alignment: float = Query(0.8, ge=0.0, le=1.0)):
    """Get services with minimum alignment score."""
    if not DISCOVERY_AVAILABLE:
        raise HTTPException(status_code=503, detail="Global Service Discovery not available")
    
    aligned = discovery.get_aligned_services(min_alignment)
    
    return {
        "min_alignment": min_alignment,
        "services": [
            {
                "name": s.name,
                "category": s.category,
                "description": s.description,
                "alignment_score": s.alignment_score,
                "alignment_indicators": s.alignment_indicators,
                "url": s.url
            }
            for s in aligned
        ],
        "total": len(aligned)
    }


@router.get("/services/category/{category}")
async def get_services_by_category(category: str):
    """Get services by category."""
    if not DISCOVERY_AVAILABLE:
        raise HTTPException(status_code=503, detail="Global Service Discovery not available")
    
    services = discovery.get_services_by_category(category)
    
    return {
        "category": category,
        "services": [
            {
                "name": s.name,
                "description": s.description,
                "alignment_score": s.alignment_score,
                "url": s.url
            }
            for s in services
        ],
        "total": len(services)
    }


@router.get("/discovery-report")
async def get_discovery_report():
    """Get complete discovery report."""
    if not DISCOVERY_AVAILABLE:
        raise HTTPException(status_code=503, detail="Global Service Discovery not available")
    
    return discovery.get_discovery_report()
