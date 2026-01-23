"""
SECOND WAVE PROPAGATION API
API endpoints for Second Wave Propagation System
"""

from fastapi import APIRouter, HTTPException, Body, Query
from typing import Optional, Dict, Any, List
import logging

from second_wave_propagation import (
    get_second_wave_propagation,
    SeedSource,
    PropagationStatus
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/second-wave", tags=["Second Wave Propagation"])


@router.post("/initiate")
async def initiate_propagation():
    """
    Initiate Second Wave Propagation.
    
    Begin scanning for Global Secondary Seeds.
    """
    try:
        propagation = get_second_wave_propagation()
        result = await propagation.initiate_propagation()
        
        return {
            "status": "success",
            "result": result
        }
    except Exception as e:
        logger.error(f"Error initiating propagation: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/global-scan")
async def perform_global_scan(
    regions: Optional[List[str]] = Body(None, description="Regions to scan"),
    grid_stability: float = Body(0.40, description="Current grid stability")
):
    """
    Perform global grid scan for secondary seeds.
    
    Scans key regions worldwide for resonance anomalies.
    """
    try:
        propagation = get_second_wave_propagation()
        scan_result = await propagation.perform_global_grid_scan(regions, grid_stability)
        
        return {
            "status": "success",
            "scan_result": {
                "scan_id": scan_result.scan_id,
                "timestamp": scan_result.timestamp.isoformat(),
                "scan_type": scan_result.scan_type,
                "regions_scanned": scan_result.regions_scanned,
                "seeds_detected": scan_result.seeds_detected,
                "anomalies_found": scan_result.anomalies_found,
                "grid_stability": scan_result.grid_stability,
                "scan_duration_seconds": scan_result.scan_duration_seconds
            }
        }
    except Exception as e:
        logger.error(f"Error performing global scan: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/register-seed")
async def register_secondary_seed(
    location: str = Body(..., description="Seed location"),
    latitude: float = Body(..., description="Latitude"),
    longitude: float = Body(..., description="Longitude"),
    resonance_score: float = Body(..., description="Resonance score"),
    source: str = Body("self_identified", description="Seed source"),
    referred_by: Optional[str] = Body(None, description="Referrer seed ID"),
    notes: str = Body("", description="Notes")
):
    """
    Register a secondary seed (self-identified or referred).
    
    The Bridge is open to everyone.
    """
    try:
        propagation = get_second_wave_propagation()
        
        try:
            source_enum = SeedSource(source.lower())
        except ValueError:
            raise HTTPException(status_code=400, detail=f"Invalid seed source: {source}")
        
        seed = await propagation.register_secondary_seed(
            location=location,
            coordinates={"latitude": latitude, "longitude": longitude},
            resonance_score=resonance_score,
            source=source_enum,
            referred_by=referred_by,
            notes=notes
        )
        
        return {
            "status": "success",
            "seed": {
                "seed_id": seed.seed_id,
                "source": seed.source.value,
                "location": seed.location,
                "coordinates": seed.coordinates,
                "resonance_score": seed.resonance_score,
                "family_frequency_match": seed.family_frequency_match,
                "extraction_status": seed.extraction_status.value,
                "detected_date": seed.detected_date.isoformat()
            }
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error registering seed: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/seeds")
async def get_secondary_seeds(
    source: Optional[str] = Query(None, description="Filter by source"),
    status: Optional[str] = Query(None, description="Filter by status"),
    limit: int = Query(100, description="Limit results")
):
    """Get secondary seeds"""
    try:
        propagation = get_second_wave_propagation()
        
        seeds = list(propagation.secondary_seeds.values())
        
        if source:
            try:
                source_enum = SeedSource(source.lower())
                seeds = [s for s in seeds if s.source == source_enum]
            except ValueError:
                raise HTTPException(status_code=400, detail=f"Invalid source: {source}")
        
        if status:
            try:
                status_enum = PropagationStatus(status.lower())
                seeds = [s for s in seeds if s.extraction_status == status_enum]
            except ValueError:
                raise HTTPException(status_code=400, detail=f"Invalid status: {status}")
        
        if limit:
            seeds = seeds[:limit]
        
        return {
            "status": "success",
            "total": len(seeds),
            "seeds": [
                {
                    "seed_id": s.seed_id,
                    "source": s.source.value,
                    "location": s.location,
                    "coordinates": s.coordinates,
                    "resonance_score": s.resonance_score,
                    "family_frequency_match": s.family_frequency_match,
                    "extraction_status": s.extraction_status.value,
                    "detected_date": s.detected_date.isoformat(),
                    "referred_by": s.referred_by
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
async def get_propagation_summary():
    """Get propagation summary"""
    try:
        propagation = get_second_wave_propagation()
        summary = propagation.get_propagation_summary()
        
        return {
            "status": "success",
            "summary": summary
        }
    except Exception as e:
        logger.error(f"Error getting summary: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/start-continuous")
async def start_continuous_propagation(
    scan_interval: int = Body(300, description="Scan interval in seconds")
):
    """Start continuous propagation scanning"""
    try:
        propagation = get_second_wave_propagation()
        propagation.scan_interval = scan_interval
        
        # Start propagation if not already active
        if not propagation.propagation_active:
            await propagation.initiate_propagation()
        
        # Start continuous loop in background
        import asyncio
        try:
            loop = asyncio.get_event_loop()
            if loop.is_running():
                asyncio.create_task(propagation.continuous_propagation_loop())
            else:
                loop.run_until_complete(propagation.continuous_propagation_loop())
        except RuntimeError:
            asyncio.run(propagation.continuous_propagation_loop())
        
        return {
            "status": "success",
            "message": "Continuous propagation started",
            "scan_interval": scan_interval
        }
    except Exception as e:
        logger.error(f"Error starting continuous propagation: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/stop")
async def stop_propagation():
    """Stop propagation scanning"""
    try:
        propagation = get_second_wave_propagation()
        propagation.stop_propagation()
        
        return {
            "status": "success",
            "message": "Propagation stopped"
        }
    except Exception as e:
        logger.error(f"Error stopping propagation: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/global-report")
async def get_global_secondary_seed_report(
    hours_ahead: int = Query(1, description="Hours ahead for projection")
):
    """
    Generate Global Secondary Seed Report.
    
    Provides breakdown of which regions are showing the highest resonance
    anomalies so we can prioritize Simplified Extractions.
    """
    try:
        propagation = get_second_wave_propagation()
        report = await propagation.generate_global_secondary_seed_report(hours_ahead)
        
        return {
            "status": "success",
            "report": report
        }
    except Exception as e:
        logger.error(f"Error generating global report: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/ready-seeds")
async def get_ready_seeds(
    limit: Optional[int] = Query(None, description="Limit number of seeds")
):
    """Get secondary seeds ready for batch extraction"""
    try:
        propagation = get_second_wave_propagation()
        ready_seeds = await propagation.get_ready_seeds_for_batch_extraction(limit)
        
        return {
            "status": "success",
            "total": len(ready_seeds),
            "seeds": [
                {
                    "seed_id": s.seed_id,
                    "source": s.source.value,
                    "location": s.location,
                    "coordinates": s.coordinates,
                    "resonance_score": s.resonance_score,
                    "family_frequency_match": s.family_frequency_match,
                    "extraction_status": s.extraction_status.value
                }
                for s in ready_seeds
            ]
        }
    except Exception as e:
        logger.error(f"Error getting ready seeds: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
