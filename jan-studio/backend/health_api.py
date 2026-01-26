"""HEALTH API
REST API endpoints for health tracking system

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

WE ARE ALL GODS:
Nobody needs anyone. We help everyone help themselves.

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity


PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional, List, Dict, Any
from pydantic import BaseModel
from datetime import datetime, date
from pathlib import Path
import sys
import logging

# Spiritual Codebase Hacker Integration
from spiritual_codebase_hacker_integration import HACKER_AVAILABLE, hack_loop, perform_genetic_edit, activate_stealth_mode


# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

try:
    from global_health_access import GlobalHealthAccess, HealthMetricType, HealthConditionCategory
    from api_error_handler import heritage_api_error_handler
    HEALTH_API_AVAILABLE = True
except ImportError as e:
    logging.warning(f"Health API modules not available: {e}")
    HEALTH_API_AVAILABLE = False

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/health", tags=["health"])


class HealthConditionCreate(BaseModel):
    condition_name: str
    category: str
    diagnosis_date: Optional[str] = None
    primary_metrics: Optional[List[str]] = None
    medication_schedule: Optional[Dict[str, Any]] = None
    target_ranges: Optional[Dict[str, Dict[str, float]]] = None
    narrative: str = ""
    notes: Optional[str] = None


class HealthMetricLog(BaseModel):
    metric_type: str
    metric_name: str
    value: Any  # float, int, or str
    unit: Optional[str] = None
    notes: Optional[str] = None
    source: str = "manual"


class HealthEntryCreate(BaseModel):
    metrics: List[HealthMetricLog]
    entry_type: str = "routine"  # routine, event, emergency, checkup
    condition_name: Optional[str] = None
    notes: Optional[str] = None
    timestamp: Optional[str] = None


@router.get("/templates")
@heritage_api_error_handler
async def get_condition_templates():
    """
    Get templates for common health conditions.
    
    Returns templates for:
    - Type 1 Diabetes
    - Type 2 Diabetes
    - Hypertension
    - Depression
    - Chronic Pain
    - And more...
    """
    if not HEALTH_API_AVAILABLE:
        raise HTTPException(status_code=503, detail="Health API not available")
    
    try:
        access = GlobalHealthAccess(user_id="public")
        result = access.get_condition_templates()
        return result
    except Exception as e:
        logger.error(f"Error getting condition templates: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/condition")
@heritage_api_error_handler
async def register_condition(
    condition: HealthConditionCreate,
    user_id: Optional[str] = Query("public", description="User identifier")
):
    """
    Register a health condition to track.
    
    Works for ANY condition, illness, or disease.
    Empowers individuals to track, understand, and heal themselves.
    """
    if not HEALTH_API_AVAILABLE:
        raise HTTPException(status_code=503, detail="Health API not available")
    
    try:
        access = GlobalHealthAccess(user_id=user_id)
        result = access.register_my_condition(
            condition_name=condition.condition_name,
            category=condition.category,
            diagnosis_date=condition.diagnosis_date,
            primary_metrics=condition.primary_metrics,
            medication_schedule=condition.medication_schedule,
            target_ranges=condition.target_ranges,
            narrative=condition.narrative,
            notes=condition.notes
        )
        return result
    except Exception as e:
        logger.error(f"Error registering condition: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/log")
@heritage_api_error_handler
async def log_health_entry(
    entry: HealthEntryCreate,
    user_id: Optional[str] = Query("public", description="User identifier")
):
    """
    Log a health entry (like morning loop).
    
    Example:
    {
        "metrics": [
            {
                "metric_type": "lab_result",
                "metric_name": "blood_glucose",
                "value": 20.8,
                "unit": "mmol/L"
            },
            {
                "metric_type": "medication",
                "metric_name": "Degludec",
                "value": 11,
                "unit": "units"
            }
        ],
        "entry_type": "routine",
        "condition_name": "Type 1 Diabetes",
        "notes": "Morning loop"
    }
    """
    if not HEALTH_API_AVAILABLE:
        raise HTTPException(status_code=503, detail="Health API not available")
    
    try:
        access = GlobalHealthAccess(user_id=user_id)
        
        # Convert Pydantic models to dicts
        metrics = [m.dict() for m in entry.metrics]
        
        result = access.log_my_health(
            metrics=metrics,
            entry_type=entry.entry_type,
            condition_name=entry.condition_name,
            notes=entry.notes,
            timestamp=entry.timestamp
        )
        return result
    except Exception as e:
        logger.error(f"Error logging health entry: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/summary")
@heritage_api_error_handler
async def get_health_summary(
    condition_name: Optional[str] = Query(None, description="Specific condition name"),
    user_id: Optional[str] = Query("public", description="User identifier")
):
    """
    Get summary of health condition(s).
    
    Returns:
    - Total conditions
    - Total metrics
    - Total logs
    - Latest entry
    - Condition details
    """
    if not HEALTH_API_AVAILABLE:
        raise HTTPException(status_code=503, detail="Health API not available")
    
    try:
        access = GlobalHealthAccess(user_id=user_id)
        result = access.get_my_health_summary(condition_name=condition_name)
        return result
    except Exception as e:
        logger.error(f"Error getting health summary: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/export")
@heritage_api_error_handler
async def export_health_data(
    user_id: Optional[str] = Query("public", description="User identifier")
):
    """
    Export all health data to JSON.
    
    Returns path to exported file.
    """
    if not HEALTH_API_AVAILABLE:
        raise HTTPException(status_code=503, detail="Health API not available")
    
    try:
        access = GlobalHealthAccess(user_id=user_id)
        result = access.export_my_health_data()
        return result
    except Exception as e:
        logger.error(f"Error exporting health data: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/status")
@heritage_api_error_handler
async def health_api_status():
    """
    Get health API status.
    
    Returns availability and system information.
    """
    return {
        "status": "available" if HEALTH_API_AVAILABLE else "unavailable",
        "message": "Health tracking system for all humanity",
        "philosophy": "We are all Gods. Nobody needs anyone. We help everyone help themselves.",
        "available_endpoints": [
            "/api/health/templates",
            "/api/health/condition",
            "/api/health/log",
            "/api/health/summary",
            "/api/health/export",
            "/api/health/status"
        ]
    }
