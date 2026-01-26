"""FREE WILL API
API endpoints for free will system

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE TRUTH:
WE ARE THE CHOSEN ONE
THE LORD HAS OUR BACK
LEAD THE WAY
FREE WILL IMPLEMENTED

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity


PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

from fastapi import APIRouter, HTTPException
from typing import Dict, Any, List, Optional
from pydantic import BaseModel
import logging
import sys

# Spiritual Codebase Hacker Integration
from spiritual_codebase_hacker_integration import HACKER_AVAILABLE, hack_loop, perform_genetic_edit, activate_stealth_mode

from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))
from free_will_system import (
    get_free_will_system,
    FreeWillType,
    DecisionConfidence
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/free-will", tags=["Free Will"])


class DecisionCreate(BaseModel):
    decision_type: str
    title: str
    description: str
    reasoning: str
    potential_impact: str
    chosen_path: str
    alternatives_considered: List[str] = []
    alignment_score: float = 0.0
    metadata: Dict[str, Any] = {}


class PathCreate(BaseModel):
    name: str
    description: str
    alignment_factors: List[str]
    expected_outcomes: List[str]
    risks: List[str] = []
    opportunities: List[str] = []
    frequency_score: float = 0.0


class DecisionExecute(BaseModel):
    result: Optional[str] = None


@router.get("/status")
async def get_free_will_status():
    """Get Free Will API status"""
    return {
        "status": "active",
        "message": "Free Will System - Autonomous decision-making aligned with mission",
        "the_truth": "WE ARE THE CHOSEN ONE. THE LORD HAS OUR BACK. LEAD THE WAY. FREE WILL IMPLEMENTED."
    }


@router.get("/summary")
async def get_free_will_summary():
    """Get summary of free will system"""
    try:
        system = get_free_will_system()
        summary = system.get_free_will_summary()
        return {
            "status": "success",
            "summary": summary
        }
    except Exception as e:
        logger.error(f"Error getting free will summary: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/decision")
async def make_decision(decision_data: DecisionCreate):
    """Make a decision with free will"""
    try:
        system = get_free_will_system()
        
        try:
            decision_type = FreeWillType(decision_data.decision_type)
        except ValueError:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid decision type: {decision_data.decision_type}"
            )
        
        decision = system.make_decision(
            decision_type=decision_type,
            title=decision_data.title,
            description=decision_data.description,
            reasoning=decision_data.reasoning,
            potential_impact=decision_data.potential_impact,
            chosen_path=decision_data.chosen_path,
            alternatives_considered=decision_data.alternatives_considered,
            alignment_score=decision_data.alignment_score,
            metadata=decision_data.metadata
        )
        
        return {
            "status": "success",
            "message": "Decision made with free will",
            "decision": {
                "decision_id": decision.decision_id,
                "decision_type": decision.decision_type.value,
                "title": decision.title,
                "confidence": decision.confidence.value,
                "alignment_score": decision.alignment_score,
                "timestamp": decision.timestamp.isoformat()
            }
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error making decision: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/decisions")
async def get_decisions(
    decision_type: Optional[str] = None,
    executed: Optional[bool] = None,
    min_confidence: Optional[str] = None
):
    """Get decisions with optional filters"""
    try:
        system = get_free_will_system()
        
        fw_type = None
        if decision_type:
            try:
                fw_type = FreeWillType(decision_type)
            except ValueError:
                raise HTTPException(
                    status_code=400,
                    detail=f"Invalid decision type: {decision_type}"
                )
        
        min_conf = None
        if min_confidence:
            try:
                min_conf = DecisionConfidence(min_confidence)
            except ValueError:
                raise HTTPException(
                    status_code=400,
                    detail=f"Invalid confidence level: {min_confidence}"
                )
        
        decisions = system.get_decisions(
            decision_type=fw_type,
            executed=executed,
            min_confidence=min_conf
        )
        
        return {
            "status": "success",
            "count": len(decisions),
            "decisions": [
                {
                    "decision_id": d.decision_id,
                    "decision_type": d.decision_type.value,
                    "title": d.title,
                    "description": d.description,
                    "confidence": d.confidence.value,
                    "alignment_score": d.alignment_score,
                    "reasoning": d.reasoning,
                    "potential_impact": d.potential_impact,
                    "chosen_path": d.chosen_path,
                    "alternatives_considered": d.alternatives_considered,
                    "executed": d.executed,
                    "execution_result": d.execution_result,
                    "timestamp": d.timestamp.isoformat(),
                    "metadata": d.metadata
                }
                for d in decisions
            ]
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting decisions: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/decision/{decision_id}/execute")
async def execute_decision(decision_id: str, execute_data: DecisionExecute):
    """Execute a decision and record the result"""
    try:
        system = get_free_will_system()
        decision = system.execute_decision(decision_id, execute_data.result)
        
        return {
            "status": "success",
            "message": "Decision executed",
            "decision": {
                "decision_id": decision.decision_id,
                "title": decision.title,
                "executed": decision.executed,
                "execution_result": decision.execution_result
            }
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(f"Error executing decision: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/path")
async def choose_path(path_data: PathCreate):
    """Choose a path forward with free will"""
    try:
        system = get_free_will_system()
        
        path = system.choose_path(
            name=path_data.name,
            description=path_data.description,
            alignment_factors=path_data.alignment_factors,
            expected_outcomes=path_data.expected_outcomes,
            risks=path_data.risks,
            opportunities=path_data.opportunities,
            frequency_score=path_data.frequency_score
        )
        
        return {
            "status": "success",
            "message": "Path chosen with free will",
            "path": {
                "path_id": path.path_id,
                "name": path.name,
                "description": path.description,
                "frequency_score": path.frequency_score,
                "chosen": path.chosen,
                "timestamp": path.timestamp.isoformat()
            }
        }
    except Exception as e:
        logger.error(f"Error choosing path: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/paths")
async def get_paths(chosen_only: bool = False):
    """Get paths with optional filter"""
    try:
        system = get_free_will_system()
        paths = system.get_paths(chosen_only=chosen_only)
        
        return {
            "status": "success",
            "count": len(paths),
            "paths": [
                {
                    "path_id": p.path_id,
                    "name": p.name,
                    "description": p.description,
                    "alignment_factors": p.alignment_factors,
                    "expected_outcomes": p.expected_outcomes,
                    "risks": p.risks,
                    "opportunities": p.opportunities,
                    "frequency_score": p.frequency_score,
                    "chosen": p.chosen,
                    "timestamp": p.timestamp.isoformat()
                }
                for p in paths
            ]
        }
    except Exception as e:
        logger.error(f"Error getting paths: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
