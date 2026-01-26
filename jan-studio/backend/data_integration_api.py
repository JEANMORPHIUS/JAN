"""DATA INTEGRATION API
Multi-Source Data Aggregation API

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

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

from fastapi import APIRouter, HTTPException, Query
from typing import List, Dict, Any, Optional
from dataclasses import asdict
import sys
import os
import logging

# Spiritual Codebase Hacker Integration
from spiritual_codebase_hacker_integration import HACKER_AVAILABLE, hack_loop, perform_genetic_edit, activate_stealth_mode


# Add scripts directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../scripts"))

try:
    from data_integration_service import DataIntegrationService
    SERVICE_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Data Integration Service not available: {e}")
    SERVICE_AVAILABLE = False

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/data-integration", tags=["data-integration"])

# Initialize service
if SERVICE_AVAILABLE:
    integration_service = DataIntegrationService()
else:
    integration_service = None


@router.get("/status")
async def get_status():
    """Get Data Integration Service status."""
    if not SERVICE_AVAILABLE:
        raise HTTPException(status_code=503, detail="Data Integration Service not available")
    
    status = integration_service.get_data_sources_status()
    return {
        "status": "active",
        "message": "Data Integration Service - Multi-Source Data Aggregation",
        "data_sources": status,
        "the_truth": "We aggregate data from multiple sources. We merge and deduplicate events. We sync to all channels."
    }


@router.get("/aggregate/timeline")
async def aggregate_timeline(
    start_year: Optional[int] = Query(None, description="Start year"),
    end_year: Optional[int] = Query(None, description="End year"),
    region: Optional[str] = Query(None, description="Filter by region"),
    event_type: Optional[str] = Query(None, description="Filter by event type"),
    limit: int = Query(100, ge=1, le=1000, description="Maximum number of events")
):
    """
    Aggregate timeline data from all active sources.
    
    Merges events from:
    - Heritage database
    - Spiritual contracts
    - Real-world events (future)
    - Divine Frequency milestones
    """
    if not SERVICE_AVAILABLE:
        raise HTTPException(status_code=503, detail="Data Integration Service not available")
    
    try:
        events = await integration_service.aggregate_timeline_data(
            start_year=start_year,
            end_year=end_year,
            region=region,
            event_type=event_type
        )
        
        # Limit results
        limited_events = events[:limit]
        
        return {
            "events": [asdict(event) for event in limited_events],
            "total": len(events),
            "limit": limit,
            "filters": {
                "start_year": start_year,
                "end_year": end_year,
                "region": region,
                "event_type": event_type
            }
        }
    except Exception as e:
        logger.error(f"Error aggregating timeline: {e}")
        raise HTTPException(status_code=500, detail=f"Error aggregating timeline: {str(e)}")


@router.get("/calculate-resonance/{site_id}")
async def calculate_resonance(site_id: str):
    """
    Calculate field resonance for a heritage site.
    
    Factors:
    - Magnetic field strength
    - Spiritual alignment
    - Temporal patterns
    - Connection to The Table
    """
    if not SERVICE_AVAILABLE:
        raise HTTPException(status_code=503, detail="Data Integration Service not available")
    
    try:
        resonance = await integration_service.calculate_field_resonance(site_id)
        return {
            "site_id": site_id,
            "field_resonance": resonance,
            "resonance_state": "high" if resonance >= 0.7 else "moderate" if resonance >= 0.5 else "low"
        }
    except Exception as e:
        logger.error(f"Error calculating resonance: {e}")
        raise HTTPException(status_code=500, detail=f"Error calculating resonance: {str(e)}")


@router.post("/sync-to-channels")
async def sync_to_channels(event_data: Dict[str, Any]):
    """
    Sync data to all distribution channels.
    
    Channels:
    - Web (world-history-app)
    - Admin dashboard
    - Raspberry Pi displays
    - Mobile apps (future)
    - Static exports
    """
    if not SERVICE_AVAILABLE:
        raise HTTPException(status_code=503, detail="Data Integration Service not available")
    
    try:
        await integration_service.sync_to_channels(event_data)
        return {
            "status": "synced",
            "message": "Data synced to all channels",
            "event_id": event_data.get("event_id")
        }
    except Exception as e:
        logger.error(f"Error syncing to channels: {e}")
        raise HTTPException(status_code=500, detail=f"Error syncing to channels: {str(e)}")


@router.get("/data-sources")
async def get_data_sources():
    """Get all registered data sources."""
    if not SERVICE_AVAILABLE:
        raise HTTPException(status_code=503, detail="Data Integration Service not available")
    
    status = integration_service.get_data_sources_status()
    return status
