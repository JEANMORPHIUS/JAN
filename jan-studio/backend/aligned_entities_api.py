"""
ALIGNED ENTITIES API
Real-World Entities Across All Industries in Alignment with The Table

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

ALIGNED ENTITIES:
Real-world entities (companies, organizations, people) that are in alignment with The Table.
They serve unity, truth, connection.
They don't exploit.
They support restoration.
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
    from aligned_entities_tracker import (
        AlignedEntitiesTracker,
        IndustryType,
        AlignmentLevel,
        EntityType
    )
    TRACKER_AVAILABLE = True
except ImportError as e:
    logging.warning(f"Aligned Entities tracker not available: {e}")
    TRACKER_AVAILABLE = False

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/aligned-entities", tags=["Aligned Entities"])

# Global tracker instance
tracker = AlignedEntitiesTracker() if TRACKER_AVAILABLE else None


@router.get("/status")
async def get_aligned_entities_status():
    """Get aligned entities tracking status."""
    if not TRACKER_AVAILABLE:
        raise HTTPException(status_code=503, detail="Aligned Entities tracker not available")
    
    return {
        "status": "active",
        "message": "Tracking real-world entities aligned with The Table across all industries",
        "total_entities": len(tracker.entities),
        "industries_tracked": len(set(e.industry for e in tracker.entities.values()))
    }


@router.post("/register")
async def register_aligned_entity(
    name: str = Body(...),
    entity_type: str = Body(...),
    industry: str = Body(...),
    description: str = Body(...),
    alignment_score: float = Body(..., ge=0.0, le=1.0),
    how_they_align: Optional[List[str]] = Body(None),
    supports_restoration: bool = Body(False),
    heritage_connections: Optional[List[str]] = Body(None),
    field_space_connections: Optional[List[str]] = Body(None),
    frequency_contribution: float = Body(0.0, ge=0.0),
    website: Optional[str] = Body(None),
    location: Optional[str] = Body(None),
    notes: Optional[str] = Body(None)
):
    """Register an aligned entity."""
    if not TRACKER_AVAILABLE:
        raise HTTPException(status_code=503, detail="Aligned Entities tracker not available")
    
    entity = tracker.register_entity(
        name=name,
        entity_type=entity_type,
        industry=industry,
        description=description,
        alignment_score=alignment_score,
        how_they_align=how_they_align,
        supports_restoration=supports_restoration,
        heritage_connections=heritage_connections,
        field_space_connections=field_space_connections,
        frequency_contribution=frequency_contribution,
        website=website,
        location=location,
        notes=notes or ""
    )
    
    return {
        "status": "registered",
        "entity": {
            "entity_id": entity.entity_id,
            "name": entity.name,
            "industry": entity.industry,
            "alignment_score": entity.alignment_score,
            "alignment_level": entity.alignment_level
        }
    }


@router.get("/entities")
async def get_all_entities():
    """Get all aligned entities."""
    if not TRACKER_AVAILABLE:
        raise HTTPException(status_code=503, detail="Aligned Entities tracker not available")
    
    return {
        "entities": [
            {
                "entity_id": e.entity_id,
                "name": e.name,
                "entity_type": e.entity_type,
                "industry": e.industry,
                "description": e.description,
                "alignment_score": e.alignment_score,
                "alignment_level": e.alignment_level,
                "how_they_align": e.how_they_align,
                "supports_restoration": e.supports_restoration,
                "frequency_contribution": e.frequency_contribution,
                "website": e.website,
                "location": e.location
            }
            for e in tracker.entities.values()
        ],
        "total": len(tracker.entities)
    }


@router.get("/entities/industry/{industry}")
async def get_entities_by_industry(industry: str):
    """Get all entities in a specific industry."""
    if not TRACKER_AVAILABLE:
        raise HTTPException(status_code=503, detail="Aligned Entities tracker not available")
    
    entities = tracker.get_entities_by_industry(industry)
    
    return {
        "industry": industry,
        "entities": [
            {
                "entity_id": e.entity_id,
                "name": e.name,
                "entity_type": e.entity_type,
                "alignment_score": e.alignment_score,
                "alignment_level": e.alignment_level,
                "frequency_contribution": e.frequency_contribution
            }
            for e in entities
        ],
        "total": len(entities)
    }


@router.get("/entities/alignment/{alignment_level}")
async def get_entities_by_alignment(alignment_level: str):
    """Get all entities at a specific alignment level."""
    if not TRACKER_AVAILABLE:
        raise HTTPException(status_code=503, detail="Aligned Entities tracker not available")
    
    entities = tracker.get_entities_by_alignment_level(alignment_level)
    
    return {
        "alignment_level": alignment_level,
        "entities": [
            {
                "entity_id": e.entity_id,
                "name": e.name,
                "industry": e.industry,
                "alignment_score": e.alignment_score,
                "frequency_contribution": e.frequency_contribution
            }
            for e in entities
        ],
        "total": len(entities)
    }


@router.get("/entities/top")
async def get_top_aligned_entities(limit: int = Query(10, ge=1, le=100)):
    """Get top aligned entities by alignment score."""
    if not TRACKER_AVAILABLE:
        raise HTTPException(status_code=503, detail="Aligned Entities tracker not available")
    
    top_entities = tracker.get_top_aligned_entities(limit)
    
    return {
        "entities": [
            {
                "entity_id": e.entity_id,
                "name": e.name,
                "industry": e.industry,
                "alignment_score": e.alignment_score,
                "alignment_level": e.alignment_level,
                "frequency_contribution": e.frequency_contribution,
                "supports_restoration": e.supports_restoration
            }
            for e in top_entities
        ],
        "total": len(top_entities)
    }


@router.get("/summary")
async def get_alignment_summary():
    """Get summary of alignment across all entities."""
    if not TRACKER_AVAILABLE:
        raise HTTPException(status_code=503, detail="Aligned Entities tracker not available")
    
    return tracker.get_alignment_summary()


@router.get("/industry-analysis")
async def get_industry_analysis():
    """Get analysis of alignment by industry."""
    if not TRACKER_AVAILABLE:
        raise HTTPException(status_code=503, detail="Aligned Entities tracker not available")
    
    industry_analysis = tracker.analyze_industry_alignment()
    
    return {
        "industry_analysis": {
            industry: {
                "total_entities": ia.total_entities,
                "perfect_alignment": ia.perfect_alignment,
                "high_alignment": ia.high_alignment,
                "moderate_alignment": ia.moderate_alignment,
                "average_alignment_score": ia.average_alignment_score,
                "top_entities": ia.top_entities
            }
            for industry, ia in industry_analysis.items()
        }
    }


@router.get("/complete-analysis")
async def get_complete_analysis():
    """Get complete analysis of aligned entities."""
    if not TRACKER_AVAILABLE:
        raise HTTPException(status_code=503, detail="Aligned Entities tracker not available")
    
    return tracker.get_complete_analysis()
