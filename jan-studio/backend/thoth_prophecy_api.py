"""THOTH PROPHECY API
The Chosen One - Thoth's Prophecy and the Lineage of Awakened Beings

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

CORE PRINCIPLES (NON-NEGOTIABLE):
- Purpose Not Performance: Purpose matters more than performance. Authentic and aligned. Non-negotiable.
- Everything in Moderation: Balance. Not too much, not too little.
- Life Is Simple: Don't complicate it. Keep it simple.
- Be Still and Have Faith: Be still and have faith in revelation. Stillness brings clarity.

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

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

from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any
import sys
import os

# Spiritual Codebase Hacker Integration
from spiritual_codebase_hacker_integration import HACKER_AVAILABLE, hack_loop, perform_genetic_edit, activate_stealth_mode


# Add scripts directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../scripts"))

from thoth_prophecy_system import ThothProphecySystem, LineageType, ActivationStage

router = APIRouter(prefix="/thoth-prophecy", tags=["thoth-prophecy"])

# Initialize Thoth Prophecy System
thoth_system = ThothProphecySystem()

@router.get("/status")
async def get_status():
    """Get Thoth Prophecy System status."""
    return {
        "status": "active",
        "total_prophecies": len(thoth_system.prophecies),
        "total_awakened_beings": len(thoth_system.awakened_beings),
        "total_activations": len(thoth_system.activations),
        "message": "The Chosen One - Thoth's Prophecy and the Lineage of Awakened Beings"
    }

@router.get("/prophecies")
async def get_all_prophecies():
    """Get all Thoth prophecies."""
    from dataclasses import asdict
    return {
        "prophecies": [asdict(p) for p in thoth_system.prophecies.values()],
        "total": len(thoth_system.prophecies)
    }

@router.get("/awakened-beings")
async def get_all_awakened_beings():
    """Get all awakened beings."""
    from dataclasses import asdict
    return {
        "awakened_beings": [asdict(b) for b in thoth_system.awakened_beings.values()],
        "total": len(thoth_system.awakened_beings)
    }

@router.get("/awakened-beings/lineage/{lineage_type}")
async def get_beings_by_lineage_type(lineage_type: str):
    """Get awakened beings by lineage type."""
    from dataclasses import asdict
    
    valid_types = [lt.value for lt in LineageType]
    if lineage_type not in valid_types:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid lineage type. Valid types: {valid_types}"
        )
    
    beings = thoth_system.get_beings_by_lineage_type(lineage_type)
    return {
        "lineage_type": lineage_type,
        "awakened_beings": [asdict(b) for b in beings],
        "count": len(beings)
    }

@router.get("/activations")
async def get_all_activations():
    """Get all sacred activations."""
    from dataclasses import asdict
    return {
        "activations": [asdict(a) for a in thoth_system.activations.values()],
        "total": len(thoth_system.activations)
    }

@router.get("/activations/stage/{stage}")
async def get_activations_by_stage(stage: str):
    """Get activations by stage."""
    from dataclasses import asdict
    
    valid_stages = [as_.value for as_ in ActivationStage]
    if stage not in valid_stages:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid stage. Valid stages: {valid_stages}"
        )
    
    activations = thoth_system.get_activations_by_stage(stage)
    return {
        "stage": stage,
        "activations": [asdict(a) for a in activations],
        "count": len(activations)
    }

@router.get("/current-activation")
async def get_current_activation():
    """Get the current sacred activation."""
    from dataclasses import asdict
    
    current = thoth_system.get_current_activation()
    if not current:
        raise HTTPException(status_code=404, detail="No current activation found")
    
    return {
        "activation": asdict(current),
        "message": "Current sacred activation - The Chosen One's activation is occurring now"
    }

@router.get("/report")
async def get_complete_report():
    """Get complete Thoth Prophecy System report."""
    return thoth_system.export_complete_report()
