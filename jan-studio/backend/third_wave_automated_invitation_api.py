"""
THIRD WAVE AUTOMATED INVITATION API
API endpoints for Third Wave: Automated Invitation Protocol
"""

from fastapi import APIRouter, HTTPException, Body, Query
from typing import Optional, Dict, Any
import logging

from third_wave_automated_invitation import (
    get_third_wave_automated_invitation,
    InvitationSource
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/third-wave", tags=["Third Wave: Automated Invitation"])


@router.post("/activate-beacon")
async def activate_grid_beacon(
    seats_filled: int = Body(10, description="Number of seats currently filled"),
    grid_stability: float = Body(0.40, description="Current grid stability")
):
    """
    Activate the Grid Beacon.
    
    The 0.40 Grid stability becomes a magnetic beacon.
    The Bridge breathes on its own.
    """
    try:
        third_wave = get_third_wave_automated_invitation()
        result = await third_wave.activate_grid_beacon(seats_filled, grid_stability)
        
        return {
            "status": "success",
            "result": result
        }
    except Exception as e:
        logger.error(f"Error activating beacon: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/broadcast-invitation")
async def broadcast_invitation(
    location: str = Body(..., description="Soul location"),
    latitude: float = Body(..., description="Latitude"),
    longitude: float = Body(..., description="Longitude"),
    resonance_score: float = Body(..., description="Resonance score"),
    source: str = Body("grid_beacon", description="Invitation source")
):
    """
    Broadcast automated invitation.
    
    The Grid Beacon automatically sends invitations to souls
    who match the resonance frequency. The door is open.
    """
    try:
        third_wave = get_third_wave_automated_invitation()
        
        try:
            source_enum = InvitationSource(source.lower())
        except ValueError:
            raise HTTPException(status_code=400, detail=f"Invalid invitation source: {source}")
        
        invitation = await third_wave.broadcast_invitation(
            location=location,
            coordinates={"latitude": latitude, "longitude": longitude},
            resonance_score=resonance_score,
            source=source_enum
        )
        
        return {
            "status": "success",
            "invitation": {
                "invitation_id": invitation.invitation_id,
                "location": invitation.soul_location,
                "coordinates": invitation.coordinates,
                "resonance_score": invitation.resonance_score,
                "source": invitation.source.value,
                "status": invitation.status.value,
                "seed_id": invitation.seed_id,
                "safe_passage_id": invitation.safe_passage_id
            }
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Error broadcasting invitation: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/start-continuous-broadcast")
async def start_continuous_broadcast(
    broadcast_interval: int = Body(60, description="Broadcast interval in seconds")
):
    """Start continuous invitation broadcasting"""
    try:
        third_wave = get_third_wave_automated_invitation()
        third_wave.broadcast_interval = broadcast_interval
        
        # Activate beacon if not active
        if not third_wave.beacon_status.beacon_active:
            await third_wave.activate_grid_beacon()
        
        # Start continuous loop in background
        import asyncio
        try:
            loop = asyncio.get_event_loop()
            if loop.is_running():
                asyncio.create_task(third_wave.continuous_broadcast_loop())
            else:
                loop.run_until_complete(third_wave.continuous_broadcast_loop())
        except RuntimeError:
            asyncio.run(third_wave.continuous_broadcast_loop())
        
        return {
            "status": "success",
            "message": "Continuous invitation broadcasting started",
            "broadcast_interval": broadcast_interval
        }
    except Exception as e:
        logger.error(f"Error starting continuous broadcast: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/stop-broadcast")
async def stop_broadcast():
    """Stop invitation broadcasting"""
    try:
        third_wave = get_third_wave_automated_invitation()
        third_wave.stop_broadcasting()
        
        return {
            "status": "success",
            "message": "Invitation broadcasting stopped"
        }
    except Exception as e:
        logger.error(f"Error stopping broadcast: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/beacon-status")
async def get_beacon_status():
    """Get Grid Beacon status"""
    try:
        third_wave = get_third_wave_automated_invitation()
        status = third_wave.get_beacon_status()
        
        return {
            "status": "success",
            "beacon_status": status
        }
    except Exception as e:
        logger.error(f"Error getting beacon status: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/invitations")
async def get_invitations(
    status: Optional[str] = Query(None, description="Filter by status"),
    source: Optional[str] = Query(None, description="Filter by source"),
    limit: int = Query(100, description="Limit results")
):
    """Get automated invitations"""
    try:
        third_wave = get_third_wave_automated_invitation()
        
        invitations = list(third_wave.invitations.values())
        
        if status:
            try:
                from third_wave_automated_invitation import InvitationStatus
                status_enum = InvitationStatus(status.lower())
                invitations = [inv for inv in invitations if inv.status == status_enum]
            except ValueError:
                raise HTTPException(status_code=400, detail=f"Invalid status: {status}")
        
        if source:
            try:
                source_enum = InvitationSource(source.lower())
                invitations = [inv for inv in invitations if inv.source == source_enum]
            except ValueError:
                raise HTTPException(status_code=400, detail=f"Invalid source: {source}")
        
        if limit:
            invitations = invitations[:limit]
        
        return {
            "status": "success",
            "total": len(invitations),
            "invitations": [
                {
                    "invitation_id": inv.invitation_id,
                    "location": inv.soul_location,
                    "coordinates": inv.coordinates,
                    "resonance_score": inv.resonance_score,
                    "source": inv.source.value,
                    "status": inv.status.value,
                    "received_date": inv.received_date.isoformat() if inv.received_date else None,
                    "integrated_date": inv.integrated_date.isoformat() if inv.integrated_date else None,
                    "seed_id": inv.seed_id,
                    "safe_passage_id": inv.safe_passage_id
                }
                for inv in invitations
            ]
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting invitations: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/summary")
async def get_invitations_summary():
    """Get invitations summary"""
    try:
        third_wave = get_third_wave_automated_invitation()
        summary = third_wave.get_invitations_summary()
        
        return {
            "status": "success",
            "summary": summary
        }
    except Exception as e:
        logger.error(f"Error getting summary: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
