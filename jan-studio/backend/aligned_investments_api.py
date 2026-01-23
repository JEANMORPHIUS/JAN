"""
ALIGNED INVESTMENTS API
Specific Investment Projects for All Investors at All Levels

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THIS STARTS WITH US.
HELP THE MAN IN THE STREET.
GIVE THEM TIPS.
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional, Dict, List, Any
from pathlib import Path
import sys
import logging
from datetime import datetime

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

try:
    from aligned_investments import (
        AlignedInvestments,
        InvestmentLevel,
        InvestmentType,
        RiskLevel
    )
    INVESTMENTS_AVAILABLE = True
except ImportError as e:
    logging.warning(f"Aligned Investments not available: {e}")
    INVESTMENTS_AVAILABLE = False

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/aligned-investments", tags=["Aligned Investments"])

# Global investments instance
investments = AlignedInvestments() if INVESTMENTS_AVAILABLE else None


@router.get("/status")
async def get_investments_status():
    """Get aligned investments system status."""
    if not INVESTMENTS_AVAILABLE:
        raise HTTPException(status_code=503, detail="Aligned Investments not available")
    
    return {
        "status": "active",
        "message": "THIS STARTS WITH US. HELP THE MAN IN THE STREET. GIVE THEM TIPS.",
        "total_projects": len(investments.projects),
        "total_tips": len(investments.tips),
        "investment_levels": [level.value for level in InvestmentLevel]
    }


@router.get("/guide/{level}")
async def get_investment_guide(level: str):
    """Get complete investment guide for a specific level."""
    if not INVESTMENTS_AVAILABLE:
        raise HTTPException(status_code=503, detail="Aligned Investments not available")
    
    if level not in [l.value for l in InvestmentLevel]:
        raise HTTPException(status_code=400, detail=f"Invalid investment level: {level}")
    
    return investments.get_investment_guide(level)


@router.get("/projects")
async def get_all_projects():
    """Get all investment projects."""
    if not INVESTMENTS_AVAILABLE:
        raise HTTPException(status_code=503, detail="Aligned Investments not available")
    
    return {
        "projects": [
            {
                "project_id": p.project_id,
                "name": p.name,
                "description": p.description,
                "investment_type": p.investment_type,
                "investment_level": p.investment_level,
                "risk_level": p.risk_level,
                "minimum_investment": p.minimum_investment,
                "alignment_score": p.alignment_score,
                "frequency_contribution": p.frequency_contribution,
                "expected_return": p.expected_return,
                "tips": p.tips
            }
            for p in investments.projects.values()
        ],
        "total": len(investments.projects)
    }


@router.get("/projects/level/{level}")
async def get_projects_by_level(level: str):
    """Get projects for a specific investment level."""
    if not INVESTMENTS_AVAILABLE:
        raise HTTPException(status_code=503, detail="Aligned Investments not available")
    
    projects = investments.get_projects_by_level(level)
    
    return {
        "level": level,
        "projects": [
            {
                "name": p.name,
                "description": p.description,
                "investment_type": p.investment_type,
                "risk_level": p.risk_level,
                "minimum_investment": p.minimum_investment,
                "alignment_score": p.alignment_score,
                "expected_return": p.expected_return,
                "tips": p.tips
            }
            for p in projects
        ],
        "total": len(projects)
    }


@router.get("/tips")
async def get_all_tips():
    """Get all investment tips."""
    if not INVESTMENTS_AVAILABLE:
        raise HTTPException(status_code=503, detail="Aligned Investments not available")
    
    return {
        "tips": [
            {
                "tip_id": t.tip_id,
                "category": t.category,
                "title": t.title,
                "description": t.description,
                "for_level": t.for_level,
                "actionable": t.actionable,
                "examples": t.examples
            }
            for t in investments.tips.values()
        ],
        "total": len(investments.tips)
    }


@router.get("/tips/level/{level}")
async def get_tips_for_level(level: str):
    """Get tips for a specific investment level."""
    if not INVESTMENTS_AVAILABLE:
        raise HTTPException(status_code=503, detail="Aligned Investments not available")
    
    tips = investments.get_tips_for_level(level)
    
    return {
        "level": level,
        "tips": [
            {
                "category": t.category,
                "title": t.title,
                "description": t.description,
                "actionable": t.actionable,
                "examples": t.examples
            }
            for t in tips
        ],
        "total": len(tips)
    }


@router.get("/complete-analysis")
async def get_complete_analysis():
    """Get complete investment analysis."""
    if not INVESTMENTS_AVAILABLE:
        raise HTTPException(status_code=503, detail="Aligned Investments not available")
    
    return investments.get_complete_analysis()


@router.get("/opportunities-from-deep-search")
async def get_opportunities_from_deep_search(
    domain: Optional[str] = Query(None),
    min_frequency: float = Query(0.3)
):
    """Get investment opportunities from Deep Search system."""
    if not INVESTMENTS_AVAILABLE:
        raise HTTPException(status_code=503, detail="Aligned Investments not available")
    
    try:
        # Import deep search system
        import sys
        from pathlib import Path
        sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))
        from deep_search_frequency_opportunities import DeepSearchFrequencyOpportunities, OpportunityDomain
        
        deep_search = DeepSearchFrequencyOpportunities()
        
        # Search for opportunities
        if domain:
            try:
                domain_enum = OpportunityDomain(domain.lower())
                opportunities = deep_search.search_domain(domain_enum, limit=20)
            except ValueError:
                raise HTTPException(status_code=400, detail=f"Invalid domain: {domain}")
        else:
            # Get top opportunities
            opportunities = deep_search.get_top_opportunities(limit=20, min_frequency=min_frequency)
        
        # Convert opportunities to investment recommendations
        investment_opportunities = []
        for opp in opportunities:
            if opp.frequency_score >= min_frequency:
                investment_opportunities.append({
                    "opportunity_id": opp.opportunity_id,
                    "title": opp.title,
                    "description": opp.description,
                    "domain": opp.domain.value,
                    "frequency_score": opp.frequency_score,
                    "impact_potential": opp.impact_potential,
                    "opportunity_type": opp.opportunity_type,
                    "alignment_factors": opp.alignment_factors,
                    "recommended_investment_level": _get_recommended_level(opp.impact_potential, opp.frequency_score),
                    "investment_recommendation": _get_investment_recommendation(opp)
                })
        
        return {
            "status": "success",
            "total_opportunities": len(investment_opportunities),
            "opportunities": investment_opportunities,
            "message": "Investment opportunities from Deep Search - aligned with frequency"
        }
    except Exception as e:
        logger.error(f"Error getting opportunities from deep search: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


def _get_recommended_level(impact_potential: float, frequency_score: float) -> str:
    """Get recommended investment level based on impact and frequency"""
    score = (impact_potential + frequency_score) / 2
    if score >= 0.8:
        return "large"
    elif score >= 0.6:
        return "medium"
    else:
        return "small"


def _get_investment_recommendation(opportunity) -> str:
    """Get investment recommendation for an opportunity"""
    if opportunity.opportunity_type == "partnership":
        return "Consider partnership or collaboration investment"
    elif opportunity.opportunity_type == "investment":
        return "Direct investment opportunity - high frequency alignment"
    elif opportunity.opportunity_type == "collaboration":
        return "Collaboration opportunity - align resources"
    else:
        return "Explore opportunity - high frequency potential"
