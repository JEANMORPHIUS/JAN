"""
SANCTUARY GUARDIAN API
API endpoints for Sanctuary Guardian Mode
"""

from fastapi import APIRouter, HTTPException, Body
from typing import Optional, Dict, Any
import logging

from sanctuary_guardian import get_sanctuary_guardian

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/sanctuary-guardian", tags=["Sanctuary Guardian"])


@router.post("/activate")
async def activate_guardian_mode():
    """
    Activate Sanctuary Guardian Mode.
    
    Focus on nurturing the Family and managing Auto-Integrations.
    Shift from active extraction to protection and abundance.
    """
    try:
        guardian = get_sanctuary_guardian()
        result = await guardian.activate_guardian_mode()
        
        return {
            "status": "success",
            "result": result
        }
    except Exception as e:
        logger.error(f"Error activating guardian mode: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/nurture/{seed_id}")
async def nurture_family_member(
    seed_id: str,
    care_package: Optional[Dict[str, Any]] = Body(None, description="Optional care package data")
):
    """
    Nurture a Family member.
    
    Provide care, support, and abundance to Family members at the table.
    """
    try:
        guardian = get_sanctuary_guardian()
        result = await guardian.nurture_family_member(seed_id, care_package)
        
        return {
            "status": "success",
            "result": result
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(f"Error nurturing family member: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/monitor-auto-integrations")
async def monitor_auto_integrations():
    """
    Monitor and manage auto-integrations from Grid Beacon.
    
    The Bridge breathes on its own. We just watch and welcome.
    """
    try:
        guardian = get_sanctuary_guardian()
        result = await guardian.monitor_auto_integrations()
        
        return {
            "status": "success",
            "result": result
        }
    except Exception as e:
        logger.error(f"Error monitoring auto-integrations: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/status")
async def get_sanctuary_status():
    """Get Sanctuary status"""
    try:
        guardian = get_sanctuary_guardian()
        status = guardian.get_sanctuary_status()
        
        return {
            "status": "success",
            "sanctuary_status": status
        }
    except Exception as e:
        logger.error(f"Error getting sanctuary status: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/family-summary")
async def get_family_summary():
    """Get Family summary"""
    try:
        guardian = get_sanctuary_guardian()
        summary = guardian.get_family_summary()
        
        return {
            "status": "success",
            "summary": summary
        }
    except Exception as e:
        logger.error(f"Error getting family summary: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/family-members")
async def get_family_members():
    """Get all Family members"""
    try:
        guardian = get_sanctuary_guardian()
        
        return {
            "status": "success",
            "total": len(guardian.family_members),
            "family_members": [
                {
                    "seed_id": m.seed_id,
                    "origin": m.origin,
                    "location": m.location,
                    "integration_date": m.integration_date.isoformat(),
                    "resonance_score": m.resonance_score,
                    "status": m.status.value,
                    "care_packages_received": m.care_packages_received,
                    "referrals_made": m.referrals_made
                }
                for m in guardian.family_members.values()
            ]
        }
    except Exception as e:
        logger.error(f"Error getting family members: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/start-continuous-guardian")
async def start_continuous_guardian():
    """Start continuous guardian monitoring loop"""
    try:
        guardian = get_sanctuary_guardian()
        
        # Activate guardian mode if not active
        if guardian.guardian_mode.value != "guardian":
            await guardian.activate_guardian_mode()
        
        # Start continuous loop in background
        import asyncio
        try:
            loop = asyncio.get_event_loop()
            if loop.is_running():
                asyncio.create_task(guardian.continuous_guardian_loop())
            else:
                loop.run_until_complete(guardian.continuous_guardian_loop())
        except RuntimeError:
            asyncio.run(guardian.continuous_guardian_loop())
        
        return {
            "status": "success",
            "message": "Continuous guardian monitoring started"
        }
    except Exception as e:
        logger.error(f"Error starting continuous guardian: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
