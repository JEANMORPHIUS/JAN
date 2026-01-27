"""
SYSTEM WIDE INTEGRATION API
API endpoints for system-wide alignment and integration

THE NOAH PROTOCOL:
- Architectural Weight: Built for comprehensive integration
- The Pitch: Waterproof error handling
- The Perimeter: Clear API boundaries

THE TRUTH:
Scale and build until ready.
System-wide integration APIs for the new world.
"""

from fastapi import APIRouter, HTTPException, status
from typing import Dict, List, Any, Optional
from datetime import datetime
from system_wide_integration import get_system_integration
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/system-integration", tags=["System Wide Integration"])


@router.get("/status")
async def get_integration_status():
    """Get overall system integration status"""
    try:
        integration = get_system_integration()
        status = integration.get_integration_status()
        return status
    except Exception as e:
        logger.error(f"Get integration status error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get integration status: {str(e)}"
        )


@router.get("/systems")
async def list_systems(category: Optional[str] = None):
    """List all systems"""
    try:
        integration = get_system_integration()
        systems = list(integration.systems.values())
        
        if category:
            from system_wide_integration import SystemCategory
            try:
                category_enum = SystemCategory(category.lower())
                systems = [s for s in systems if s.category == category_enum]
            except ValueError:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Invalid category: {category}"
                )
        
        return {
            "count": len(systems),
            "systems": [
                {
                    "system_id": s.system_id,
                    "system_name": s.system_name,
                    "category": s.category.value,
                    "status": s.status.value,
                    "alignment_score": s.alignment_score,
                    "protocols": s.protocols,
                    "integration_points": s.integration_points
                }
                for s in systems
            ]
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"List systems error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to list systems"
        )


@router.get("/systems/{system_id}")
async def get_system(system_id: str):
    """Get system integration details"""
    try:
        integration = get_system_integration()
        system = integration.get_system_integration(system_id)
        
        if not system:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"System not found: {system_id}"
            )
        
        connected = integration.get_connected_systems(system_id)
        compliance = integration.protocol_compliance.get(system_id, {})
        
        return {
            "system_id": system.system_id,
            "system_name": system.system_name,
            "category": system.category.value,
            "status": system.status.value,
            "alignment_score": system.alignment_score,
            "protocols": system.protocols,
            "integration_points": system.integration_points,
            "dependencies": system.dependencies,
            "connected_systems": [
                {
                    "system_id": s.system_id,
                    "system_name": s.system_name,
                    "category": s.category.value
                }
                for s in connected
            ],
            "protocol_compliance": compliance
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Get system error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to get system"
        )


@router.get("/alignment-map")
async def get_alignment_map():
    """Get complete system alignment map"""
    try:
        integration = get_system_integration()
        return integration.get_system_alignment_map()
    except Exception as e:
        logger.error(f"Get alignment map error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to get alignment map"
        )


@router.get("/curriculum/integration")
async def verify_curriculum_integration():
    """Verify curriculum system-wide integration"""
    try:
        integration = get_system_integration()
        return integration.verify_curriculum_integration()
    except Exception as e:
        logger.error(f"Verify curriculum integration error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to verify curriculum integration"
        )


@router.get("/health")
async def get_integration_health():
    """Get integration system health"""
    try:
        integration = get_system_integration()
        status = integration.get_integration_status()
        
        overall_healthy = (
            status["integration_rate"] >= 80.0 and
            status["alignment_rate"] >= 80.0
        )
        
        return {
            "timestamp": datetime.now().isoformat(),
            "status": "healthy" if overall_healthy else "degraded",
            "integration_rate": status["integration_rate"],
            "alignment_rate": status["alignment_rate"],
            "total_systems": status["total_systems"],
            "fully_integrated": status["fully_integrated"],
            "aligned": status["aligned"]
        }
    except Exception as e:
        logger.error(f"Get integration health error: {e}")
        return {
            "timestamp": datetime.now().isoformat(),
            "status": "unhealthy",
            "error": str(e)
        }
