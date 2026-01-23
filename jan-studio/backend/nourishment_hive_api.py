"""
NOURISHMENT HIVE API
API endpoints for nourishment hive system

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE TRUTH:
IN A BROKEN WORLD HUMANS ARE BROKEN
WHAT THEY CONSUME CREATES ALL THE CHAOS INTERNALLY
SINCE WE'VE WORKED BACKWARDS...LETS WORK FORWARD
CONSIDER ALL POTENTIAL AND BEST CASE SCENARIOS
FOR ALL MANKIND AND THE EARTH
HOW DO WE BEST NOURISH EACH OTHER AS A HIVE
"""

from fastapi import APIRouter, HTTPException
from typing import Dict, Any
import logging
import sys
from pathlib import Path

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

try:
    from nourishment_hive_system import NourishmentHiveSystem
    NOURISHMENT_HIVE_AVAILABLE = True
except ImportError as e:
    NOURISHMENT_HIVE_AVAILABLE = False
    print(f"Warning: Nourishment Hive System not available: {e}")

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/nourishment-hive", tags=["Nourishment Hive"])

# Global instance
_nourishment_system = None

def get_nourishment_system() -> NourishmentHiveSystem:
    """Get the global nourishment hive system instance"""
    global _nourishment_system
    if _nourishment_system is None and NOURISHMENT_HIVE_AVAILABLE:
        _nourishment_system = NourishmentHiveSystem()
    return _nourishment_system


@router.get("/status")
async def get_status():
    """Get Nourishment Hive API status"""
    return {
        "status": "active" if NOURISHMENT_HIVE_AVAILABLE else "unavailable",
        "message": "Nourishment Hive System - Working Forward, Best Case Scenarios",
        "available": NOURISHMENT_HIVE_AVAILABLE,
        "the_truth": "IN A BROKEN WORLD HUMANS ARE BROKEN. WHAT THEY CONSUME CREATES ALL THE CHAOS INTERNALLY. WE NOURISH INSTEAD. WE WORK FORWARD. WE NOURISH EACH OTHER AS A HIVE."
    }


@router.get("/nourishment-plan")
async def get_nourishment_plan():
    """Get comprehensive nourishment plan for the hive"""
    if not NOURISHMENT_HIVE_AVAILABLE:
        raise HTTPException(status_code=503, detail="Nourishment Hive System not available")
    
    try:
        system = get_nourishment_system()
        plan = system.get_nourishment_plan()
        return {
            "status": "success",
            "plan": plan
        }
    except Exception as e:
        logger.error(f"Error getting nourishment plan: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/nourishment-sources")
async def get_nourishment_sources():
    """Get all nourishment sources"""
    if not NOURISHMENT_HIVE_AVAILABLE:
        raise HTTPException(status_code=503, detail="Nourishment Hive System not available")
    
    try:
        system = get_nourishment_system()
        sources = {
            source_id: {
                "name": source.name,
                "type": source.nourishment_type.value,
                "description": source.description,
                "impact": source.impact,
                "accessibility": source.accessibility,
                "sustainability": source.sustainability,
                "hive_benefit": source.hive_benefit,
                "consumption_healing": source.consumption_healing,
                "best_case_scenario": source.best_case_scenario
            }
            for source_id, source in system.nourishment_sources.items()
        }
        return {
            "status": "success",
            "sources": sources
        }
    except Exception as e:
        logger.error(f"Error getting nourishment sources: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/best-case-scenarios")
async def get_best_case_scenarios():
    """Get all best case scenarios"""
    if not NOURISHMENT_HIVE_AVAILABLE:
        raise HTTPException(status_code=503, detail="Nourishment Hive System not available")
    
    try:
        system = get_nourishment_system()
        scenarios = {
            scenario_id: {
                "domain": scenario.domain,
                "vision": scenario.vision,
                "current_state": scenario.current_state,
                "transformation_path": scenario.transformation_path,
                "nourishment_required": scenario.nourishment_required,
                "hive_benefit": scenario.hive_benefit,
                "earth_benefit": scenario.earth_benefit,
                "timeline": scenario.timeline,
                "indicators": scenario.indicators
            }
            for scenario_id, scenario in system.best_case_scenarios.items()
        }
        return {
            "status": "success",
            "scenarios": scenarios
        }
    except Exception as e:
        logger.error(f"Error getting best case scenarios: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/hive-path")
async def get_hive_nourishment_path():
    """Get the path from broken consumption to hive nourishment"""
    if not NOURISHMENT_HIVE_AVAILABLE:
        raise HTTPException(status_code=503, detail="Nourishment Hive System not available")
    
    try:
        system = get_nourishment_system()
        path = system.get_hive_nourishment_path()
        return {
            "status": "success",
            "path": path
        }
    except Exception as e:
        logger.error(f"Error getting hive path: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
