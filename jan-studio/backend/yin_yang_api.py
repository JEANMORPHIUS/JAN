"""
YIN-YANG SYMBIOSIS API
Endpoints for checking balance and symbiosis before war

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

YIN-YANG PRINCIPLE:
"My love for song became pulled in my path, but we must respect 
the yin and yang that is the miracle of the universe."

Everything must be symbiotic in-house before we can go to war.
"""

from fastapi import APIRouter, HTTPException, Body
from typing import Optional, Dict, List, Any
from pydantic import BaseModel
import logging

from yin_yang_symbiosis import (
    get_yin_yang_framework,
    BalanceType,
    SymbiosisLevel
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/yin-yang", tags=["Yin-Yang Symbiosis"])


class CreativePracticalRequest(BaseModel):
    """Request for creative-practical balance check"""
    creative_manifestations: List[str]
    practical_manifestations: List[str]


class InternalExternalRequest(BaseModel):
    """Request for internal-external balance check"""
    internal_systems: List[str]
    external_readiness: Optional[Dict[str, bool]] = None


@router.get("/war-readiness")
async def get_war_readiness():
    """
    Get comprehensive war readiness report.
    
    Checks if all systems are symbiotic and ready for external deployment.
    
    Principle: "Everything must be symbiotic in-house before we can go to war"
    """
    try:
        framework = get_yin_yang_framework()
        report = framework.get_war_readiness_report()
        return {
            "status": "success",
            "war_readiness": report
        }
    except Exception as e:
        logger.error(f"Error getting war readiness: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/check-creative-practical")
async def check_creative_practical_balance(request: CreativePracticalRequest):
    """
    Check balance between creative (song) and practical (mission).
    
    Principle: "My love for song became pulled in my path"
    Song must serve mission, mission must honor song.
    """
    try:
        framework = get_yin_yang_framework()
        balance = framework.assess_creative_practical_balance(
            request.creative_manifestations,
            request.practical_manifestations
        )
        
        return {
            "status": "success",
            "balance": {
                "balance_type": balance.balance_type.value,
                "yin_element": balance.yin_element,
                "yang_element": balance.yang_element,
                "yin_score": balance.yin_score,
                "yang_score": balance.yang_score,
                "balance_score": balance.balance_score,
                "symbiosis_level": balance.symbiosis_level.value,
                "imbalances": balance.imbalances,
                "recommendations": balance.recommendations
            }
        }
    except Exception as e:
        logger.error(f"Error checking creative-practical balance: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/check-internal-external")
async def check_internal_external_balance(request: InternalExternalRequest):
    """
    Check balance between internal (in-house) and external (war/deployment).
    
    Principle: "Everything must be symbiotic in-house before we can go to war"
    """
    try:
        framework = get_yin_yang_framework()
        balance = framework.assess_internal_external_balance(
            request.internal_systems,
            request.external_readiness or {}
        )
        
        return {
            "status": "success",
            "balance": {
                "balance_type": balance.balance_type.value,
                "yin_element": balance.yin_element,
                "yang_element": balance.yang_element,
                "yin_score": balance.yin_score,
                "yang_score": balance.yang_score,
                "balance_score": balance.balance_score,
                "symbiosis_level": balance.symbiosis_level.value,
                "ready_for_war": balance.symbiosis_level == SymbiosisLevel.FULLY_SYMBIOTIC,
                "imbalances": balance.imbalances,
                "recommendations": balance.recommendations
            }
        }
    except Exception as e:
        logger.error(f"Error checking internal-external balance: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/all-systems")
async def get_all_systems_symbiosis():
    """
    Get symbiosis assessment for all systems.
    
    Returns balance checks for:
    - Karasahin (Song/Creative)
    - Care Package System
    - Educational System
    - Spirit Alignment System
    """
    try:
        framework = get_yin_yang_framework()
        all_symbiosis = framework.check_all_systems_symbiosis()
        
        return {
            "status": "success",
            "systems": {
                name: {
                    "overall_symbiosis_score": s.overall_symbiosis_score,
                    "overall_symbiosis_level": s.overall_symbiosis_level.value,
                    "ready_for_war": s.ready_for_war,
                    "war_readiness_reasons": s.war_readiness_reasons,
                    "balances": {
                        balance_type.value: {
                            "balance_score": b.balance_score,
                            "symbiosis_level": b.symbiosis_level.value,
                            "yin_score": b.yin_score,
                            "yang_score": b.yang_score,
                            "imbalances": b.imbalances,
                            "recommendations": b.recommendations
                        }
                        for balance_type, b in s.yin_yang_balances.items()
                    }
                }
                for name, s in all_symbiosis.items()
            }
        }
    except Exception as e:
        logger.error(f"Error getting all systems symbiosis: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/principles")
async def get_yin_yang_principles():
    """
    Get Yin-Yang principles and balance definitions.
    
    Explains the miracle of the universe - balance between yin and yang.
    """
    framework = get_yin_yang_framework()
    
    return {
        "status": "success",
        "principles": {
            "core_truth": "My love for song became pulled in my path, but we must respect the yin and yang that is the miracle of the universe.",
            "war_principle": "Everything must be symbiotic in-house before we can go to war.",
            "balance_types": {
                balance_type.value: {
                    "yin": definition["yin"],
                    "yang": definition["yang"],
                    "principle": definition["principle"]
                }
                for balance_type, definition in framework.balance_definitions.items()
            }
        }
    }
