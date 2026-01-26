"""JUDICIAL SYSTEM API
API endpoints for judicial system exploration

Addresses: "WHO ARE WE TO JUDGE RIGHT FROM WRONG WHEN EVERYTHING IS WRONG?"

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity


PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional, Dict, Any
import logging

# Spiritual Codebase Hacker Integration
from spiritual_codebase_hacker_integration import HACKER_AVAILABLE, hack_loop, perform_genetic_edit, activate_stealth_mode


from judicial_system_explorer import (
    get_judicial_system_explorer,
    JudicialStructure
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/judicial-system", tags=["Judicial System"])


@router.get("/judgment-question")
async def explore_judgment_question():
    """
    Explore the core question:
    "WHO ARE WE TO JUDGE RIGHT FROM WRONG WHEN EVERYTHING IS WRONG?"
    
    This is a profound spiritual and philosophical question.
    """
    try:
        explorer = get_judicial_system_explorer()
        exploration = explorer.explore_judgment_question()
        
        return {
            "status": "success",
            "exploration": exploration
        }
    except Exception as e:
        logger.error(f"Error exploring judgment question: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/analyze")
async def analyze_judicial_system(
    structure: str = Query("adversarial", description="Judicial structure: adversarial, inquisitorial, community, restorative, spiritual, diy")
):
    """Analyze judicial system through mission lens"""
    try:
        explorer = get_judicial_system_explorer()
        
        try:
            structure_enum = JudicialStructure(structure.lower())
        except ValueError:
            raise HTTPException(status_code=400, detail=f"Invalid structure: {structure}")
        
        analysis = explorer.analyze_judicial_system(structure_enum)
        
        return {
            "status": "success",
            "analysis": {
                "structure": analysis.structure.value,
                "justice_type": analysis.justice_type.value,
                "judgment_type": analysis.judgment_type.value,
                "serves_mission": analysis.serves_mission,
                "serves_truth": analysis.serves_truth,
                "serves_community": analysis.serves_community,
                "right_spirits_present": analysis.right_spirits_present,
                "mission_alignment_score": analysis.mission_alignment_score,
                "truth_alignment_score": analysis.truth_alignment_score,
                "symbiosis_score": analysis.symbiosis_score,
                "spiritual_battles": analysis.spiritual_battles,
                "gatekeepers": analysis.gatekeepers,
                "opportunities": analysis.opportunities,
                "recommendations": analysis.recommendations,
                "warnings": analysis.warnings,
                "philosophical_insights": analysis.philosophical_insights
            }
        }
    except Exception as e:
        logger.error(f"Error analyzing judicial system: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/find-truth")
async def find_truth_in_broken_systems():
    """
    Find truth when everything seems wrong.
    
    "WHO ARE WE TO JUDGE RIGHT FROM WRONG WHEN EVERYTHING IS WRONG?"
    """
    try:
        explorer = get_judicial_system_explorer()
        paths = explorer.find_truth_in_broken_systems()
        
        return {
            "status": "success",
            "paths": paths
        }
    except Exception as e:
        logger.error(f"Error finding truth: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/navigation-strategy")
async def get_navigation_strategy():
    """
    Navigation strategy for judicial systems.
    
    How to navigate when everything seems wrong.
    """
    try:
        explorer = get_judicial_system_explorer()
        strategy = explorer.get_navigation_strategy()
        
        return {
            "status": "success",
            "strategy": strategy
        }
    except Exception as e:
        logger.error(f"Error getting navigation strategy: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
