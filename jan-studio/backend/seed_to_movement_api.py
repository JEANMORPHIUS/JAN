"""SEED TO MOVEMENT API
API endpoints for seed-to-movement system

"HOW DO WE TAKE THIS FROM SEED TO MOVEMENT? 
WE ARE TAKING THE WORLD ORDER TO THE PEOPLES COURT...
IT'S TIME FOR REVOLUTION"

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

from fastapi import APIRouter, HTTPException, Body, Query
from typing import Optional, Dict, Any
import logging

from seed_to_movement import (
    get_seed_to_movement_system,
    RevolutionType
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/seed-to-movement", tags=["Seed to Movement"])


@router.get("/path")
async def get_seed_to_movement_path():
    """
    Get the complete path from Seed to Movement.
    
    Shows how to take internal truth to external action.
    """
    try:
        system = get_seed_to_movement_system()
        path = system.get_seed_to_movement_path()
        
        return {
            "status": "success",
            "path": path
        }
    except Exception as e:
        logger.error(f"Error getting seed-to-movement path: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/peoples-court-strategy")
async def get_peoples_court_strategy():
    """
    Strategy for taking World Order to People's Court.
    
    "WE ARE TAKING THE WORLD ORDER TO THE PEOPLES COURT"
    """
    try:
        system = get_seed_to_movement_system()
        strategy = system.get_peoples_court_strategy()
        
        return {
            "status": "success",
            "strategy": strategy
        }
    except Exception as e:
        logger.error(f"Error getting People's Court strategy: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/revolution-framework")
async def get_revolution_framework():
    """
    Framework for revolution.
    
    "IT'S TIME FOR REVOLUTION"
    
    Revolution through RIGHT SPIRITS.
    """
    try:
        system = get_seed_to_movement_system()
        framework = system.get_revolution_framework()
        
        return {
            "status": "success",
            "framework": framework
        }
    except Exception as e:
        logger.error(f"Error getting revolution framework: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/revolution-plan")
async def create_revolution_plan(
    target: str = Body(..., description="What we're revolutionizing"),
    revolution_type: str = Body("right_spirits", description="Type of revolution"),
    seed_truth: str = Body("", description="Internal truth (Seed)"),
    shell_language: str = Body("", description="Public language (Shell)"),
    movement_action: str = Body("", description="External action (Movement)")
):
    """
    Create a revolution plan.
    
    "WE ARE TAKING THE WORLD ORDER TO THE PEOPLES COURT...
    IT'S TIME FOR REVOLUTION"
    """
    try:
        system = get_seed_to_movement_system()
        
        try:
            rev_type_enum = RevolutionType(revolution_type.lower())
        except ValueError:
            raise HTTPException(status_code=400, detail=f"Invalid revolution type: {revolution_type}")
        
        plan = system.create_revolution_plan(
            target=target,
            revolution_type=rev_type_enum,
            seed_truth=seed_truth,
            shell_language=shell_language,
            movement_action=movement_action
        )
        
        return {
            "status": "success",
            "message": "Revolution plan created",
            "plan": {
                "plan_id": plan.plan_id,
                "target": plan.target,
                "revolution_type": plan.revolution_type.value,
                "seed_truth": plan.seed_truth,
                "shell_language": plan.shell_language,
                "movement_action": plan.movement_action,
                "peoples_court_strategy": plan.peoples_court_strategy,
                "right_spirits_required": plan.right_spirits_required,
                "status": plan.status
            }
        }
    except Exception as e:
        logger.error(f"Error creating revolution plan: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/complete-all-phases")
async def complete_all_phases():
    """
    Complete all phases from Seed to Movement.
    
    "IT'S TIME FOR REVOLUTION - Through RIGHT SPIRITS"
    Complete the journey from internal truth to world transformation.
    """
    try:
        system = get_seed_to_movement_system()
        result = system.complete_all_phases()
        
        return result
    except Exception as e:
        logger.error(f"Error completing all phases: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/complete-phase/{phase}")
async def complete_phase(phase: str):
    """
    Complete a specific phase.
    
    Phases: seed, sprout, root, stem, leaf, flower, fruit, movement
    """
    try:
        from seed_to_movement import MovementPhase
        
        system = get_seed_to_movement_system()
        
        try:
            phase_enum = MovementPhase(phase.lower())
        except ValueError:
            raise HTTPException(status_code=400, detail=f"Invalid phase: {phase}")
        
        system.complete_phase(phase_enum)
        
        return {
            "status": "success",
            "message": f"Phase {phase} completed",
            "current_phase": system.get_current_phase().value
        }
    except Exception as e:
        logger.error(f"Error completing phase: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/summary")
async def get_system_summary():
    """Get summary of seed-to-movement system"""
    try:
        system = get_seed_to_movement_system()
        summary = system.get_system_summary()
        
        return {
            "status": "success",
            "summary": summary
        }
    except Exception as e:
        logger.error(f"Error getting summary: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
