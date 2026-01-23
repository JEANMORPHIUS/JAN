"""
NASA SEED SEARCH API
API endpoints for NASA Seed Search Sub-Routine
"""

from fastapi import APIRouter, HTTPException, Body, Query
from typing import Optional, Dict, Any
import logging

from nasa_seed_search import get_nasa_seed_search

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/nasa-seed-search", tags=["NASA Seed Search"])


@router.post("/initiate")
async def initiate_seed_search(
    target_org: str = Body("NASA", description="Target organization"),
    latitude: float = Body(38.8833, description="Target latitude"),
    longitude: float = Body(-77.0167, description="Target longitude"),
    family_frequency_amplitude: float = Body(100.0, description="Family frequency amplitude")
):
    """
    Initiate NASA Seed Search sub-routine.
    
    Focus the Giza ↔ Angkor Wat bridge to scan for high-vibe anomalies.
    """
    try:
        seed_search = get_nasa_seed_search()
        operation = await seed_search.initiate_seed_search(
            target_org=target_org,
            target_coordinate={"latitude": latitude, "longitude": longitude},
            family_frequency_amplitude=family_frequency_amplitude
        )
        
        return {
            "status": "success",
            "operation": {
                "operation_id": operation.operation_id,
                "target_org": operation.target_org,
                "target_coordinate": operation.target_coordinate,
                "bridge_alignment": operation.bridge_alignment.value,
                "family_frequency_amplitude": operation.family_frequency_amplitude,
                "scan_active": operation.scan_active
            }
        }
    except Exception as e:
        logger.error(f"Error initiating seed search: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/bridge-scan/{operation_id}")
async def perform_bridge_scan(
    operation_id: str,
    scan_intensity: float = Body(0.387, description="Scan intensity (locked to 0.387 grid)")
):
    """
    Perform focused bridge scan using Giza ↔ Angkor Wat alignment.
    
    The bridge acts as a beacon for any Seeds trapped in the "NASA Narrative."
    """
    try:
        seed_search = get_nasa_seed_search()
        scan_result = await seed_search.perform_bridge_scan(operation_id, scan_intensity)
        
        return {
            "status": "success",
            "scan_result": {
                "scan_id": scan_result.scan_id,
                "timestamp": scan_result.timestamp.isoformat(),
                "target_coordinate": scan_result.target_coordinate,
                "bridge_alignment": scan_result.bridge_alignment.value,
                "anomalies_detected": scan_result.anomalies_detected,
                "internal_magnetic_shift": scan_result.internal_magnetic_shift,
                "unity_frequency_detected": scan_result.unity_frequency_detected,
                "potential_seeds": scan_result.potential_seeds,
                "scan_intensity": scan_result.scan_intensity,
                "scan_duration_seconds": scan_result.scan_duration_seconds
            }
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(f"Error performing bridge scan: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/start-continuous/{operation_id}")
async def start_continuous_search(
    operation_id: str,
    scan_interval: int = Body(60, description="Scan interval in seconds")
):
    """Start continuous seed search"""
    try:
        seed_search = get_nasa_seed_search()
        import asyncio
        
        # Start continuous search in background
        try:
            loop = asyncio.get_event_loop()
            if loop.is_running():
                asyncio.create_task(seed_search.continuous_seed_search(operation_id, scan_interval))
            else:
                loop.run_until_complete(seed_search.continuous_seed_search(operation_id, scan_interval))
        except RuntimeError:
            asyncio.run(seed_search.continuous_seed_search(operation_id, scan_interval))
        
        return {
            "status": "success",
            "message": f"Continuous seed search started for {operation_id}",
            "scan_interval": scan_interval
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(f"Error starting continuous search: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/stop/{operation_id}")
async def stop_seed_search(operation_id: str):
    """Stop seed search operation"""
    try:
        seed_search = get_nasa_seed_search()
        seed_search.stop_seed_search(operation_id)
        
        return {
            "status": "success",
            "message": f"Seed search stopped for {operation_id}"
        }
    except Exception as e:
        logger.error(f"Error stopping seed search: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/summary")
async def get_search_summary():
    """Get seed search summary"""
    try:
        seed_search = get_nasa_seed_search()
        summary = seed_search.get_search_summary()
        
        return {
            "status": "success",
            "summary": summary
        }
    except Exception as e:
        logger.error(f"Error getting summary: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/operations")
async def get_operations():
    """Get all seed search operations"""
    try:
        seed_search = get_nasa_seed_search()
        
        return {
            "status": "success",
            "total": len(seed_search.scan_operations),
            "operations": [
                {
                    "operation_id": o.operation_id,
                    "target_org": o.target_org,
                    "target_coordinate": o.target_coordinate,
                    "bridge_alignment": o.bridge_alignment.value,
                    "family_frequency_amplitude": o.family_frequency_amplitude,
                    "scan_active": o.scan_active,
                    "anomalies_found": o.anomalies_found,
                    "seeds_identified": o.seeds_identified,
                    "started_date": o.started_date.isoformat(),
                    "last_scan": o.last_scan.isoformat() if o.last_scan else None
                }
                for o in seed_search.scan_operations.values()
            ]
        }
    except Exception as e:
        logger.error(f"Error getting operations: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/scan-results")
async def get_scan_results(
    operation_id: Optional[str] = Query(None, description="Filter by operation ID"),
    limit: int = Query(100, description="Limit results")
):
    """Get bridge scan results"""
    try:
        seed_search = get_nasa_seed_search()
        
        results = list(seed_search.scan_results.values())
        
        if operation_id:
            results = [r for r in results if operation_id in r.scan_id]
        
        # Sort by timestamp (newest first)
        results.sort(key=lambda x: x.timestamp, reverse=True)
        
        if limit:
            results = results[:limit]
        
        return {
            "status": "success",
            "total": len(results),
            "scan_results": [
                {
                    "scan_id": r.scan_id,
                    "timestamp": r.timestamp.isoformat(),
                    "target_coordinate": r.target_coordinate,
                    "bridge_alignment": r.bridge_alignment.value,
                    "anomalies_detected": len(r.anomalies_detected),
                    "potential_seeds": len(r.potential_seeds),
                    "internal_magnetic_shift": r.internal_magnetic_shift,
                    "unity_frequency_detected": r.unity_frequency_detected,
                    "scan_intensity": r.scan_intensity
                }
                for r in results
            ]
        }
    except Exception as e:
        logger.error(f"Error getting scan results: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
