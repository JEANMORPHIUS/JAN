"""
UNIFIED API
Single entry point for all services - Heritage, Health, Life Audit

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

STARVE THE EGO, FEED THE SOUL:
Nobody needs anyone. We help everyone help themselves.
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from pathlib import Path
import sys
import logging

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

try:
    from unified_global_access import UnifiedGlobalAccess
    from api_error_handler import heritage_api_error_handler
    UNIFIED_API_AVAILABLE = True
except ImportError as e:
    logging.warning(f"Unified API modules not available: {e}")
    UNIFIED_API_AVAILABLE = False

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/unified", tags=["unified"])


@router.get("/services")
@heritage_api_error_handler
async def get_all_services(
    user_id: Optional[str] = Query("public", description="User identifier")
):
    """
    Get overview of all available services.
    
    Returns:
    - Heritage cleansing and timeline audit
    - Health tracking (any condition)
    - Life audit and personal grid
    - Global Grid connection
    """
    if not UNIFIED_API_AVAILABLE:
        raise HTTPException(status_code=503, detail="Unified API not available")
    
    try:
        access = UnifiedGlobalAccess(user_id=user_id)
        result = access.get_all_services()
        return result
    except Exception as e:
        logger.error(f"Error getting services: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/care-package")
@heritage_api_error_handler
async def get_care_package(
    user_id: Optional[str] = Query("public", description="User identifier")
):
    """
    Get the Care Package - everything someone needs to get started.
    
    Philosophy: Starve the Ego, Feed the Soul
    - Empowerment, not dependency
    - Self-mastery, not external control
    - Tools, not crutches
    
    Returns:
    - Quick start guides
    - Documentation links
    - Templates
    - Examples
    - API endpoints
    """
    if not UNIFIED_API_AVAILABLE:
        raise HTTPException(status_code=503, detail="Unified API not available")
    
    try:
        access = UnifiedGlobalAccess(user_id=user_id)
        result = access.get_care_package()
        return result
    except Exception as e:
        logger.error(f"Error getting care package: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/status")
@heritage_api_error_handler
async def unified_api_status():
    """
    Get unified API status.
    
    Returns availability and system information.
    """
    return {
        "status": "available" if UNIFIED_API_AVAILABLE else "unavailable",
        "message": "Unified Global Access for all humanity",
        "philosophy": {
            "mission": "THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS",
            "principle": "STARVE THE EGO, FEED THE SOUL",
            "message": "Nobody needs anyone. We help everyone help themselves. This is empowerment, not dependency."
        },
        "available_endpoints": [
            "/api/unified/services",
            "/api/unified/care-package",
            "/api/unified/status"
        ],
        "integrated_services": {
            "heritage": "/api/heritage/*",
            "health": "/api/health/*",
            "life_audit": "Available via Python scripts"
        }
    }
