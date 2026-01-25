"""
BLUEPRINT ORCHESTRATION API
API endpoints for blueprint orchestration system

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY
"""

from fastapi import APIRouter, HTTPException
from typing import Dict, Any, Optional
import logging
from .blueprint_orchestration import (
    get_blueprint_orchestration_system,
    EntityType,
    OrchestrationRole
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/blueprint-orchestration", tags=["Blueprint Orchestration"])


@router.get("/status")
async def get_orchestration_status():
    """Get complete blueprint orchestration status"""
    try:
        system = get_blueprint_orchestration_system()
        status = system.get_orchestration_status()
        return {
            "status": "success",
            "orchestration": status
        }
    except Exception as e:
        logger.error(f"Error getting orchestration status: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/blueprint")
async def get_blueprint_summary():
    """Get blueprint summary"""
    try:
        system = get_blueprint_orchestration_system()
        summary = system.get_blueprint_summary()
        return {
            "status": "success",
            "blueprint": summary
        }
    except Exception as e:
        logger.error(f"Error getting blueprint summary: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/voice")
async def get_voice_status():
    """Get The Voice (Karasahin) status"""
    try:
        system = get_blueprint_orchestration_system()
        voice = system.get_voice_status()
        return {
            "status": "success",
            "voice": voice
        }
    except Exception as e:
        logger.error(f"Error getting voice status: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/revolution")
async def get_revolution_status():
    """Get The Revolution (Turkish People) status"""
    try:
        system = get_blueprint_orchestration_system()
        revolution = system.get_revolution_status()
        return {
            "status": "success",
            "revolution": revolution
        }
    except Exception as e:
        logger.error(f"Error getting revolution status: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/ark")
async def get_ark_status():
    """Get The Ark status"""
    try:
        system = get_blueprint_orchestration_system()
        ark = system.get_ark_status()
        return {
            "status": "success",
            "ark": ark
        }
    except Exception as e:
        logger.error(f"Error getting ark status: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/roles")
async def get_entity_roles():
    """Get all entity roles in orchestration"""
    try:
        system = get_blueprint_orchestration_system()
        roles = system.get_entity_roles_summary()
        return {
            "status": "success",
            "roles": roles
        }
    except Exception as e:
        logger.error(f"Error getting entity roles: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/entity/{entity}")
async def get_entity_orchestration_role(entity: str):
    """Get an entity's role in the orchestration"""
    try:
        entity_type = EntityType(entity.lower())
        system = get_blueprint_orchestration_system()
        role = system.get_entity_orchestration_role(entity_type)
        return {
            "status": "success",
            "entity_role": role
        }
    except ValueError:
        raise HTTPException(status_code=400, detail=f"Invalid entity: {entity}")
    except Exception as e:
        logger.error(f"Error getting entity role: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/entity/{entity}/alignment")
async def check_entity_alignment(entity: str):
    """Check if an entity is aligned with blueprint orchestration"""
    try:
        entity_type = EntityType(entity.lower())
        system = get_blueprint_orchestration_system()
        alignment = system.check_entity_alignment(entity_type)
        return {
            "status": "success",
            "alignment": alignment
        }
    except ValueError:
        raise HTTPException(status_code=400, detail=f"Invalid entity: {entity}")
    except Exception as e:
        logger.error(f"Error checking entity alignment: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
