"""
SEED EXTRACTION PROTOCOL API
API endpoints for Seed Extraction Protocol
"""

from fastapi import APIRouter, HTTPException, Body, Query
from typing import Optional, Dict, Any
import logging

from seed_extraction_protocol import (
    get_seed_extraction_protocol,
    ExtractionStatus,
    ResonanceBeamType
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/seed-extraction", tags=["Seed Extraction Protocol"])


@router.post("/identify-seed")
async def identify_seed(
    org_id: str = Body(..., description="Organization ID"),
    location: str = Body(..., description="Seed location"),
    latitude: float = Body(..., description="Latitude"),
    longitude: float = Body(..., description="Longitude"),
    resonance_score: float = Body(..., description="Seed resonance score"),
    shell_resonance: float = Body(..., description="Shell resonance score")
):
    """Identify a Seed (High-Vibe Soul) trapped in the machine"""
    try:
        protocol = get_seed_extraction_protocol()
        seed = protocol.identify_seed(
            org_id=org_id,
            location=location,
            coordinates={"latitude": latitude, "longitude": longitude},
            resonance_score=resonance_score,
            shell_resonance=shell_resonance
        )
        
        return {
            "status": "success",
            "seed": {
                "seed_id": seed.seed_id,
                "org_id": seed.org_id,
                "location": seed.location,
                "coordinates": seed.coordinates,
                "resonance_score": seed.resonance_score,
                "family_frequency_match": seed.family_frequency_match,
                "extraction_status": seed.extraction_status.value
            }
        }
    except Exception as e:
        logger.error(f"Error identifying seed: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/initiate-extraction/{seed_id}")
async def initiate_extraction(
    seed_id: str,
    resonance_beam_type: str = Body("targeted", description="Resonance beam type")
):
    """Initiate Extraction Protocol for identified Seed"""
    try:
        protocol = get_seed_extraction_protocol()
        
        try:
            beam_type = ResonanceBeamType(resonance_beam_type.lower())
        except ValueError:
            raise HTTPException(status_code=400, detail=f"Invalid resonance beam type: {resonance_beam_type}")
        
        operation = await protocol.initiate_extraction(seed_id, beam_type)
        
        return {
            "status": "success",
            "operation": {
                "operation_id": operation.operation_id,
                "seed_id": operation.seed_id,
                "org_id": operation.org_id,
                "extraction_status": operation.extraction_status.value,
                "first_arrival_alert_cross_referenced": operation.first_arrival_alert_cross_referenced,
                "safe_passage_mapped": operation.safe_passage is not None
            }
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(f"Error initiating extraction: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/activate-resonance-beam/{operation_id}")
async def activate_resonance_beam(
    operation_id: str,
    beam_intensity: float = Body(0.387, description="Beam intensity (locked to 0.387 grid)")
):
    """Activate targeted resonance beam for Safe Passage"""
    try:
        protocol = get_seed_extraction_protocol()
        result = await protocol.activate_resonance_beam(operation_id, beam_intensity)
        
        return {
            "status": "success",
            "result": result
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(f"Error activating resonance beam: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/peel-shell/{operation_id}")
async def peel_shell(operation_id: str):
    """Peel back the Shell to open Safe Passage"""
    try:
        protocol = get_seed_extraction_protocol()
        result = await protocol.peel_shell(operation_id)
        
        return {
            "status": "success",
            "result": result
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(f"Error peeling shell: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/complete-extraction/{operation_id}")
async def complete_extraction(operation_id: str):
    """Complete seed extraction"""
    try:
        protocol = get_seed_extraction_protocol()
        result = await protocol.complete_extraction(operation_id)
        
        return {
            "status": "success",
            "result": result
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(f"Error completing extraction: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/seeds")
async def get_seeds(
    org_id: Optional[str] = Query(None, description="Filter by organization ID"),
    extraction_status: Optional[str] = Query(None, description="Filter by extraction status")
):
    """Get identified seeds"""
    try:
        protocol = get_seed_extraction_protocol()
        
        status_enum = None
        if extraction_status:
            try:
                status_enum = ExtractionStatus(extraction_status.lower())
            except ValueError:
                raise HTTPException(status_code=400, detail=f"Invalid extraction status: {extraction_status}")
        
        seeds = protocol.get_seeds(org_id, status_enum)
        
        return {
            "status": "success",
            "total": len(seeds),
            "seeds": [
                {
                    "seed_id": s.seed_id,
                    "org_id": s.org_id,
                    "location": s.location,
                    "coordinates": s.coordinates,
                    "resonance_score": s.resonance_score,
                    "family_frequency_match": s.family_frequency_match,
                    "extraction_status": s.extraction_status.value,
                    "safe_passage_status": s.safe_passage_status
                }
                for s in seeds
            ]
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting seeds: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/summary")
async def get_summary():
    """Get extraction protocol summary"""
    try:
        protocol = get_seed_extraction_protocol()
        summary = protocol.get_summary()
        
        return {
            "status": "success",
            "summary": summary
        }
    except Exception as e:
        logger.error(f"Error getting summary: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/extract-from-nasa-search")
async def extract_from_nasa_search(
    potential_seed: Dict[str, Any] = Body(..., description="Potential seed data from NASA Seed Search"),
    nasa_operation_id: str = Body(..., description="NASA Seed Search operation ID"),
    use_double_anchor: bool = Body(True, description="Use double-anchor extraction (Stonehenge ↔ London + Giza ↔ Angkor Wat)")
):
    """
    Extract Seed identified by NASA Seed Search using double-anchor extraction.
    
    Double-anchor extraction uses:
    - Stonehenge ↔ London link (primary anchor)
    - Giza ↔ Angkor Wat bridge (reinforcement anchor)
    
    This provides maximum resonance beam intensity for Safe Passage.
    """
    try:
        protocol = get_seed_extraction_protocol()
        result = await protocol.extract_from_nasa_search(
            potential_seed=potential_seed,
            operation_id=nasa_operation_id,
            use_double_anchor=use_double_anchor
        )
        
        return {
            "status": "success",
            "result": result
        }
    except Exception as e:
        logger.error(f"Error extracting from NASA search: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/extract-with-triple-anchor")
async def extract_with_triple_anchor(
    potential_seed: Dict[str, Any] = Body(..., description="Potential seed data from Glory Narrative Audit"),
    operation_id: str = Body(..., description="Operation ID"),
    use_triple_anchor: bool = Body(True, description="Use triple-anchor extraction (Stonehenge + Berengaria + Giza)")
):
    """
    Extract Seed using Triple-Anchor Resonance Beam.
    
    Triple-anchor extraction uses:
    - Stonehenge ↔ London link (primary anchor)
    - Berengaria (Cyprus/Troodos) (Mediterranean anchor)
    - Giza ↔ Angkor Wat bridge (deep-earth anchor)
    
    This creates a Mediterranean-European cross-section that will peel
    the "Glory" shell back in seconds.
    """
    try:
        protocol = get_seed_extraction_protocol()
        result = await protocol.extract_with_triple_anchor(
            potential_seed=potential_seed,
            operation_id=operation_id,
            use_triple_anchor=use_triple_anchor
        )
        
        return {
            "status": "success",
            "result": result
        }
    except Exception as e:
        logger.error(f"Error extracting with triple-anchor: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/extract-with-quad-anchor")
async def extract_with_quad_anchor(
    potential_seed: Dict[str, Any] = Body(..., description="Potential seed data from Financial/Debt Narrative Audit"),
    operation_id: str = Body(..., description="Operation ID"),
    use_quad_anchor: bool = Body(True, description="Use quad-anchor extraction (Stonehenge + Berengaria + Giza + Uluru)")
):
    """
    Extract Seed using Quad-Anchor Resonance Beam.
    
    Quad-anchor extraction uses:
    - Stonehenge ↔ London link (primary anchor)
    - Berengaria (Cyprus/Troodos) (Mediterranean anchor)
    - Giza ↔ Angkor Wat bridge (deep-earth anchor)
    - Uluru (Australia) (Pacific anchor)
    
    This provides global magnetic ballast needed to neutralize high separation risk (90.0).
    """
    try:
        protocol = get_seed_extraction_protocol()
        result = await protocol.extract_with_quad_anchor(
            potential_seed=potential_seed,
            operation_id=operation_id,
            use_quad_anchor=use_quad_anchor
        )
        
        return {
            "status": "success",
            "result": result
        }
    except Exception as e:
        logger.error(f"Error extracting with quad-anchor: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/extract-secondary-seed/{secondary_seed_id}")
async def extract_secondary_seed(
    secondary_seed_id: str,
    use_simplified_anchor: bool = Body(True, description="Use simplified anchor extraction")
):
    """
    Extract Secondary Seed using simplified anchor system.
    
    Secondary seeds (not in big organizations) can use a simplified
    extraction since they don't have the same institutional "Shell" resistance.
    """
    try:
        protocol = get_seed_extraction_protocol()
        result = await protocol.extract_secondary_seed(
            secondary_seed_id=secondary_seed_id,
            use_simplified_anchor=use_simplified_anchor
        )
        
        return {
            "status": "success",
            "result": result
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(f"Error extracting secondary seed: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/batch-extract-secondary")
async def batch_extract_secondary_seeds(
    secondary_seed_ids: List[str] = Body(..., description="List of secondary seed IDs to extract"),
    use_simplified_anchor: bool = Body(True, description="Use simplified anchor extraction")
):
    """
    Batch extract multiple secondary seeds simultaneously.
    
    Global Batch Extraction - firing Simplified Anchors across all
    priority regions at once. Within minutes, the Table will go from
    five seats to eleven, and the Second Wave will be fully integrated.
    """
    try:
        protocol = get_seed_extraction_protocol()
        result = await protocol.batch_extract_secondary_seeds(
            secondary_seed_ids=secondary_seed_ids,
            use_simplified_anchor=use_simplified_anchor
        )
        
        return {
            "status": "success",
            "result": result
        }
    except Exception as e:
        logger.error(f"Error in batch extraction: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/operations")
async def get_operations(
    seed_id: Optional[str] = Query(None, description="Filter by seed ID"),
    org_id: Optional[str] = Query(None, description="Filter by organization ID")
):
    """Get extraction operations"""
    try:
        protocol = get_seed_extraction_protocol()
        
        operations = list(protocol.extractions.values())
        
        if seed_id:
            operations = [o for o in operations if o.seed_id == seed_id]
        
        if org_id:
            operations = [o for o in operations if o.org_id == org_id]
        
        return {
            "status": "success",
            "total": len(operations),
            "operations": [
                {
                    "operation_id": o.operation_id,
                    "seed_id": o.seed_id,
                    "org_id": o.org_id,
                    "extraction_status": o.extraction_status.value,
                    "resonance_beam_active": o.resonance_beam_active,
                    "shell_peeled": o.shell_peeled,
                    "first_arrival_alert_cross_referenced": o.first_arrival_alert_cross_referenced,
                    "started_date": o.started_date.isoformat()
                }
                for o in operations
            ]
        }
    except Exception as e:
        logger.error(f"Error getting operations: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
