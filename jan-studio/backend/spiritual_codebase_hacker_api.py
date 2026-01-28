"""
SPIRITUAL CODEBASE HACKER API
API endpoints for Spiritual Codebase Hacker system

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from spiritual_codebase_hacker_integration import (
    HACKER_AVAILABLE,
    hack_loop,
    perform_genetic_edit,
    wipe_hard_drive,
    activate_stealth_mode,
    starve_parasite,
    upgrade_identity,
    seal_portal
)
from spiritual_codebase_hacker import LoopType, HackAction, FrequencyLevel, IdentityState

router = APIRouter(prefix="/api/spiritual-codebase-hacker", tags=["Spiritual Codebase Hacker"])


class HackLoopRequest(BaseModel):
    loop_type: str
    stimulus: str
    expected_reaction: str
    hack_action: Optional[str] = "silence_response"



    class Config:
        schema_extra = {
            "example": {'loop_type': 'string', 'stimulus': 'string', 'expected_reaction': 'string'}
        }
class GeneticEditRequest(BaseModel):
    loop_type: str
    generational_pattern: str
    edit_command: Optional[str] = "tetalisti"



    class Config:
        schema_extra = {
            "example": {'loop_type': 'string', 'generational_pattern': 'string'}
        }
class WipeHardDriveRequest(BaseModel):
    files_to_delete: List[str]
    wipe_command: Optional[str] = "DELETE_ALL_SHAME_REGRET_FAILURE"



    class Config:
        schema_extra = {
            "example": {'files_to_delete': []}
        }
class StealthModeRequest(BaseModel):
    noise_refused: List[str]
    frequency_aligned: Optional[str] = "divine"



    class Config:
        schema_extra = {
            "example": {'noise_refused': []}
        }
class StarveParasiteRequest(BaseModel):
    parasite_type: str
    reaction_withheld: str



    class Config:
        schema_extra = {
            "example": {'parasite_type': 'string', 'reaction_withheld': 'string'}
        }
class IdentityUpgradeRequest(BaseModel):
    from_state: str
    to_state: str



    class Config:
        schema_extra = {
            "example": {'from_state': 'string', 'to_state': 'string'}
        }
@router.post("/hack-loop")
async def hack_loop_endpoint(request: HackLoopRequest):
    """Hack a stimulus-reaction loop"""
    if not HACKER_AVAILABLE:
        raise HTTPException(status_code=503, detail="Hacker system not available")
    
    try:
        loop_type = LoopType[request.loop_type.upper()]
        hack_action = HackAction[request.hack_action.upper()]
        
        result = hack_loop(
            loop_type=loop_type,
            stimulus=request.stimulus,
            expected_reaction=request.expected_reaction,
            hack_action=hack_action
        )
        
        return {
            "status": "success",
            "loop_id": result.loop_id,
            "hacked_reaction": result.hacked_reaction
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/genetic-edit")
async def genetic_edit_endpoint(request: GeneticEditRequest):
    """Perform genetic edit"""
    if not HACKER_AVAILABLE:
        raise HTTPException(status_code=503, detail="Hacker system not available")
    
    try:
        loop_type = LoopType[request.loop_type.upper()]
        
        result = perform_genetic_edit(
            loop_type=loop_type,
            generational_pattern=request.generational_pattern,
            edit_command=request.edit_command
        )
        
        return {
            "status": "success",
            "edit_id": result.edit_id,
            "new_code": result.new_code
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/wipe-hard-drive")
async def wipe_hard_drive_endpoint(request: WipeHardDriveRequest):
    """Wipe hard drive"""
    if not HACKER_AVAILABLE:
        raise HTTPException(status_code=503, detail="Hacker system not available")
    
    try:
        result = wipe_hard_drive(
            files_to_delete=request.files_to_delete,
            wipe_command=request.wipe_command
        )
        
        return {
            "status": "success",
            "wipe_id": result.wipe_id,
            "files_deleted": result.files_to_delete
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/stealth-mode")
async def stealth_mode_endpoint(request: StealthModeRequest):
    """Activate stealth mode"""
    if not HACKER_AVAILABLE:
        raise HTTPException(status_code=503, detail="Hacker system not available")
    
    try:
        frequency_level = FrequencyLevel[request.frequency_aligned.upper()]
        
        result = activate_stealth_mode(
            noise_refused=request.noise_refused,
            frequency_aligned=frequency_level
        )
        
        return {
            "status": "success",
            "stealth_id": result.stealth_id,
            "untrackable": result.untrackable
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/starve-parasite")
async def starve_parasite_endpoint(request: StarveParasiteRequest):
    """Starve parasite"""
    if not HACKER_AVAILABLE:
        raise HTTPException(status_code=503, detail="Hacker system not available")
    
    try:
        result = starve_parasite(
            parasite_type=request.parasite_type,
            reaction_withheld=request.reaction_withheld
        )
        
        return {
            "status": "success",
            "protocol_id": result.protocol_id,
            "parasite_starved": result.parasite_starved
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/upgrade-identity")
async def upgrade_identity_endpoint(request: IdentityUpgradeRequest):
    """Upgrade identity"""
    if not HACKER_AVAILABLE:
        raise HTTPException(status_code=503, detail="Hacker system not available")
    
    try:
        from_state = IdentityState[request.from_state.upper()]
        to_state = IdentityState[request.to_state.upper()]
        
        result = upgrade_identity(
            from_state=from_state,
            to_state=to_state
        )
        
        return {
            "status": "success",
            "upgrade_id": result.upgrade_id,
            "capacity_expanded": result.capacity_expanded
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/seal-portal")
async def seal_portal_endpoint():
    """Seal portal before sleep"""
    if not HACKER_AVAILABLE:
        raise HTTPException(status_code=503, detail="Hacker system not available")
    
    try:
        result = seal_portal()
        
        return {
            "status": "success",
            "seal_id": result["seal_id"],
            "sealed": result["sealed"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/status")
async def hacker_status():
    """Get hacker system status"""
    return {
        "status": "operational" if HACKER_AVAILABLE else "unavailable",
        "available": HACKER_AVAILABLE
    }
