"""
CARE PACKAGE API
Endpoints for comprehensive system debugging and alignment

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY
"""

from fastapi import APIRouter, HTTPException, Query, Body
from typing import Optional, Dict, List, Any
from pydantic import BaseModel
import logging

# Spiritual Codebase Hacker Integration
from spiritual_codebase_hacker_integration import HACKER_AVAILABLE, hack_loop, perform_genetic_edit, activate_stealth_mode


from care_package_system import (
    get_care_package_system,
    PoliticalAlignment,
    EconomicAlignment,
    CompleteAlignment
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/care-package", tags=["Care Package"])


class PoliticalAlignmentRequest(BaseModel):
    """Request model for political alignment check"""
    governance_model: str = "democracy"
    power_distribution: str = "decentralized"
    decision_making: str = "consensus"
    values_priority: List[str] = []
    structure_type: str = "federal"



    class Config:
        schema_extra = {
            "example": {'governance_model': 'string', 'power_distribution': 'string', 'decision_making': 'string', 'values_priority': [], 'structure_type': 'string'}
        }
class EconomicAlignmentRequest(BaseModel):
    """Request model for economic alignment check"""
    exchange_model: str = "hybrid"
    resource_distribution: str = "mixed"
    value_system: str = "hybrid"
    stewardship_model: str = "stewardship"
    growth_paradigm: str = "regenerative"



    class Config:
        schema_extra = {
            "example": {'exchange_model': 'string', 'resource_distribution': 'string', 'value_system': 'string', 'stewardship_model': 'string', 'growth_paradigm': 'string'}
        }
class CompleteAlignmentRequest(BaseModel):
    """Request model for complete alignment check"""
    spiritual_data: Optional[Dict[str, Any]] = None
    political_data: Optional[Dict[str, Any]] = None
    economic_data: Optional[Dict[str, Any]] = None



    class Config:
        schema_extra = {
            "example": {'spiritual_data': {}, 'political_data': {}, 'economic_data': {}}
        }
@router.get("/")
async def get_care_package(
    user_id: Optional[str] = Query("public", description="User identifier"),
    include_alignment: bool = Query(True, description="Include alignment report")
):
    """
    Get comprehensive care package.
    
    Includes:
    - System diagnostics for all systems
    - Alignment reports (spiritual, political, economic)
    - Quick start guides
    - Documentation links
    - Troubleshooting information
    """
    try:
        system = get_care_package_system()
        care_package = system.generate_care_package(
            user_id=user_id,
            include_alignment=include_alignment
        )
        return {
            "status": "success",
            "care_package": care_package
        }
    except Exception as e:
        logger.error(f"Error generating care package: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/system-diagnostics")
async def get_system_diagnostics():
    """
    Get diagnostics for all systems.
    
    Returns detailed diagnostic information including:
    - System availability
    - Errors and warnings
    - Health status
    - Check results
    """
    try:
        system = get_care_package_system()
        diagnostics = system.debug_all_systems()
        
        return {
            "status": "success",
            "diagnostics": {
                name: {
                    "status": diag.status.value,
                    "is_available": diag.is_available,
                    "checks_passed": diag.checks_passed,
                    "checks_failed": diag.checks_failed,
                    "errors": diag.errors,
                    "warnings": diag.warnings,
                    "details": diag.details,
                    "last_check": diag.last_check.isoformat() if diag.last_check else None
                }
                for name, diag in diagnostics.items()
            },
            "summary": {
                "total_systems": len(diagnostics),
                "healthy": sum(1 for d in diagnostics.values() if d.status.value == "healthy"),
                "degraded": sum(1 for d in diagnostics.values() if d.status.value == "degraded"),
                "failing": sum(1 for d in diagnostics.values() if d.status.value == "failing"),
                "unknown": sum(1 for d in diagnostics.values() if d.status.value == "unknown")
            }
        }
    except Exception as e:
        logger.error(f"Error getting system diagnostics: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/political-alignment")
async def check_political_alignment(request: PoliticalAlignmentRequest):
    """
    Check political alignment.
    
    Validates compatibility across:
    - Governance model
    - Power distribution
    - Decision making process
    - Values priority
    - Structure type
    """
    try:
        system = get_care_package_system()
        alignment = system.check_political_alignment(
            governance_model=request.governance_model,
            power_distribution=request.power_distribution,
            decision_making=request.decision_making,
            values_priority=request.values_priority,
            structure_type=request.structure_type
        )
        
        return {
            "status": "success",
            "political_alignment": {
                "governance_model": alignment.governance_model,
                "power_distribution": alignment.power_distribution,
                "decision_making": alignment.decision_making,
                "values_priority": alignment.values_priority,
                "structure_type": alignment.structure_type,
                "alignment_score": alignment.alignment_score,
                "alignment_level": alignment.alignment_level.value
            }
        }
    except Exception as e:
        logger.error(f"Error checking political alignment: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/economic-alignment")
async def check_economic_alignment(request: EconomicAlignmentRequest):
    """
    Check economic alignment.
    
    Validates compatibility across:
    - Exchange model
    - Resource distribution
    - Value system
    - Stewardship model
    - Growth paradigm
    """
    try:
        system = get_care_package_system()
        alignment = system.check_economic_alignment(
            exchange_model=request.exchange_model,
            resource_distribution=request.resource_distribution,
            value_system=request.value_system,
            stewardship_model=request.stewardship_model,
            growth_paradigm=request.growth_paradigm
        )
        
        return {
            "status": "success",
            "economic_alignment": {
                "exchange_model": alignment.exchange_model,
                "resource_distribution": alignment.resource_distribution,
                "value_system": alignment.value_system,
                "stewardship_model": alignment.stewardship_model,
                "growth_paradigm": alignment.growth_paradigm,
                "alignment_score": alignment.alignment_score,
                "alignment_level": alignment.alignment_level.value
            }
        }
    except Exception as e:
        logger.error(f"Error checking economic alignment: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/complete-alignment")
async def get_complete_alignment(request: CompleteAlignmentRequest):
    """
    Get complete alignment across all dimensions.
    
    Integrates:
    - Spiritual alignment (from spirit_alignment system)
    - Political alignment
    - Economic alignment
    - System health diagnostics
    
    Returns comprehensive alignment report with recommendations.
    """
    try:
        system = get_care_package_system()
        alignment = system.get_complete_alignment(
            spiritual_data=request.spiritual_data,
            political_data=request.political_data,
            economic_data=request.economic_data
        )
        
        # Convert to dict for JSON response
        result = {
            "overall_alignment_score": alignment.overall_alignment_score,
            "overall_alignment_level": alignment.overall_alignment_level.value,
            "timestamp": alignment.timestamp.isoformat(),
            "spiritual_alignment": alignment.spiritual_alignment,
            "political_alignment": {
                "governance_model": alignment.political_alignment.governance_model,
                "power_distribution": alignment.political_alignment.power_distribution,
                "decision_making": alignment.political_alignment.decision_making,
                "values_priority": alignment.political_alignment.values_priority,
                "structure_type": alignment.political_alignment.structure_type,
                "alignment_score": alignment.political_alignment.alignment_score,
                "alignment_level": alignment.political_alignment.alignment_level.value
            } if alignment.political_alignment else None,
            "economic_alignment": {
                "exchange_model": alignment.economic_alignment.exchange_model,
                "resource_distribution": alignment.economic_alignment.resource_distribution,
                "value_system": alignment.economic_alignment.value_system,
                "stewardship_model": alignment.economic_alignment.stewardship_model,
                "growth_paradigm": alignment.economic_alignment.growth_paradigm,
                "alignment_score": alignment.economic_alignment.alignment_score,
                "alignment_level": alignment.economic_alignment.alignment_level.value
            } if alignment.economic_alignment else None,
            "system_health": {
                name: {
                    "status": diag.status.value,
                    "is_available": diag.is_available,
                    "checks_passed": diag.checks_passed,
                    "checks_failed": diag.checks_failed,
                    "errors": diag.errors,
                    "warnings": diag.warnings
                }
                for name, diag in alignment.system_health.items()
            },
            "misalignments": alignment.misalignments,
            "recommendations": alignment.recommendations
        }
        
        return {
            "status": "success",
            "complete_alignment": result
        }
    except Exception as e:
        logger.error(f"Error getting complete alignment: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/docs/spirit-alignment")
async def get_spirit_alignment_docs():
    """Get documentation for spiritual alignment system"""
    return {
        "title": "Spiritual Alignment Documentation",
        "description": "Multi-dimensional alignment system for spiritual battles",
        "dimensions": [
            "Age Range: Compatibility in age/soul maturity",
            "Animal Type: Compatibility in spirit animal/totem",
            "Gender Alignment: Compatibility in gender/spiritual gender",
            "Spiritual Alignment: Compatibility in vibration, mission, purpose"
        ],
        "endpoints": {
            "connection_ritual": "/api/connection-ritual",
            "check_battle_compatibility": "/api/check-battle-compatibility",
            "vibration_map": "/api/vibration-map"
        },
        "philosophy": {
            "principle": "SPIRITS MUST ALIGN ON ALL DIMENSIONS",
            "message": "No battle can occur unless ALL dimensions align. This is sacred alignment."
        }
    }


@router.get("/docs/political-alignment")
async def get_political_alignment_docs():
    """Get documentation for political alignment system"""
    return {
        "title": "Political Alignment Documentation",
        "description": "Multi-dimensional alignment system for political structures",
        "dimensions": [
            "Governance Model: democracy, republic, monarchy, anarchy, consensus_governance",
            "Power Distribution: centralized, decentralized, distributed",
            "Decision Making: consensus, majority, hierarchical, individual",
            "Values Priority: freedom, equality, justice, order, etc.",
            "Structure Type: federal, unitary, confederal, networked"
        ],
        "compatibility": {
            "democracy": "Compatible with: republic, federal, confederal",
            "republic": "Compatible with: democracy, federal, constitutional_monarchy",
            "decentralized": "Compatible with: federal, distributed, networked",
            "consensus": "Compatible with: consensus_governance, voluntary_association"
        },
        "endpoint": "/api/care-package/political-alignment"
    }


@router.get("/docs/economic-alignment")
async def get_economic_alignment_docs():
    """Get documentation for economic alignment system"""
    return {
        "title": "Economic Alignment Documentation",
        "description": "Multi-dimensional alignment system for economic structures",
        "dimensions": [
            "Exchange Model: market, gift, barter, resource-based, hybrid",
            "Resource Distribution: private, public, communal, mixed",
            "Value System: money, time, energy, contribution, hybrid",
            "Stewardship Model: ownership, stewardship, usufruct, commons",
            "Growth Paradigm: infinite, steady-state, regenerative, degrowth"
        ],
        "compatibility": {
            "market": "Compatible with: hybrid, resource-based",
            "gift": "Compatible with: communal, stewardship",
            "stewardship": "Compatible with: communal, public, commons",
            "regenerative": "Compatible with: stewardship, commons"
        },
        "endpoint": "/api/care-package/economic-alignment"
    }


@router.get("/welfare-systems")
async def get_welfare_systems_analysis():
    """
    Get welfare/benefits systems analysis.
    
    Returns:
    - Systems needing breaking (dark contracts)
    - Systems serving The Table (light contracts)
    - Analysis report
    - Breaking opportunities
    """
    try:
        import sys
        from pathlib import Path
        sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))
        from welfare_benefits_systems_analyzer import get_welfare_systems_analyzer
        
        analyzer = get_welfare_systems_analyzer()
        report = analyzer.get_analysis_report()
        systems_needing_breaking = analyzer.get_systems_needing_breaking()
        systems_serving_table = analyzer.get_systems_serving_table()
        
        return {
            "status": "success",
            "welfare_systems_analysis": {
                "summary": {
                    "total_systems": report["total_systems"],
                    "systems_needing_breaking": report["systems_needing_breaking"],
                    "systems_serving_table": report["systems_serving_table"],
                    "average_frequency_score": report["average_frequency_score"]
                },
                "systems_needing_breaking": [
                    {
                        "system_id": s.system_id,
                        "name": s.name,
                        "system_type": s.system_type.value,
                        "region": s.region,
                        "time_period": s.time_period,
                        "frequency_score": s.frequency_score,
                        "dark_contract_indicators": s.dark_contract_indicators,
                        "impact_scale": s.impact_scale,
                        "dignity_score": s.dignity_score,
                        "breaking_priority": "HIGH" if s.impact_scale > 0.7 else "MEDIUM"
                    }
                    for s in systems_needing_breaking
                ],
                "systems_serving_table": [
                    {
                        "system_id": s.system_id,
                        "name": s.name,
                        "system_type": s.system_type.value,
                        "region": s.region,
                        "frequency_score": s.frequency_score,
                        "light_contract_indicators": s.light_contract_indicators
                    }
                    for s in systems_serving_table
                ],
                "message": "We are breaking the system. Consider all welfare/benefits systems put in place through time. Identify dark contracts that need breaking. Identify light contracts that serve The Table."
            }
        }
    except Exception as e:
        logger.error(f"Error getting welfare systems analysis: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/assessment-guidance")
async def get_assessment_guidance(
    assessment_type: str = Query("personal_independence_payment", description="Type of assessment")
):
    """
    Get personal assessment navigation guidance.
    
    Provides guidance for navigating welfare system assessments
    with truth, dignity, and spiritual alignment.
    """
    try:
        import sys
        from pathlib import Path
        sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))
        from personal_assessment_navigator import get_personal_assessment_navigator, AssessmentType
        
        navigator = get_personal_assessment_navigator()
        
        # Map string to enum
        assessment_type_map = {
            "personal_independence_payment": AssessmentType.PERSONAL_INDEPENDENCE_PAYMENT,
            "universal_credit": AssessmentType.UNIVERSAL_CREDIT,
            "disability_benefits": AssessmentType.DISABILITY_BENEFITS,
            "housing_benefit": AssessmentType.HOUSING_BENEFIT,
            "employment_support": AssessmentType.EMPLOYMENT_SUPPORT
        }
        
        assessment_enum = assessment_type_map.get(assessment_type.lower(), AssessmentType.PERSONAL_INDEPENDENCE_PAYMENT)
        guidance = navigator.get_guidance(assessment_enum)
        prep = navigator.get_preparation_guidance()
        post = navigator.get_post_assessment_guidance()
        
        return {
            "status": "success",
            "assessment_guidance": {
                "assessment_type": assessment_type,
                "core_truth": guidance.core_truth,
                "intention": guidance.intention,
                "key_points": guidance.key_points,
                "boundaries": guidance.boundaries,
                "preparation": prep,
                "post_assessment": post,
                "closing_statement": guidance.closing_statement,
                "message": "Be honest. Maintain dignity. Unpick the system. You are not broken. The system is broken."
            }
        }
    except Exception as e:
        logger.error(f"Error getting assessment guidance: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/welfare-systems/breaking-opportunities")
async def get_breaking_opportunities(limit: int = Query(10, description="Number of opportunities to return")):
    """
    Get breaking opportunities for welfare systems.
    
    Returns opportunities to break dark contracts in welfare/benefits systems.
    """
    try:
        import sys
        from pathlib import Path
        sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))
        from deep_search_frequency_opportunities import DeepSearchFrequencyOpportunities, OpportunityDomain
        
        searcher = DeepSearchFrequencyOpportunities()
        opportunities = searcher.search_domain(OpportunityDomain.WELFARE_SYSTEMS, limit=limit)
        
        breaking_opps = [opp for opp in opportunities if opp.opportunity_type == "system_breaking"]
        evolution_opps = [opp for opp in opportunities if opp.opportunity_type == "system_evolution"]
        
        return {
            "status": "success",
            "breaking_opportunities": {
                "systems_needing_breaking": [
                    {
                        "opportunity_id": opp.opportunity_id,
                        "title": opp.title,
                        "description": opp.description,
                        "frequency_score": opp.frequency_score,
                        "impact_potential": opp.impact_potential,
                        "urgency": opp.urgency,
                        "metadata": opp.metadata
                    }
                    for opp in breaking_opps
                ],
                "systems_needing_evolution": [
                    {
                        "opportunity_id": opp.opportunity_id,
                        "title": opp.title,
                        "description": opp.description,
                        "frequency_score": opp.frequency_score,
                        "impact_potential": opp.impact_potential,
                        "metadata": opp.metadata
                    }
                    for opp in evolution_opps
                ],
                "message": "Opportunities to break dark contracts and evolve light contracts in welfare systems."
            }
        }
    except Exception as e:
        logger.error(f"Error getting breaking opportunities: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/political-figures")
async def get_political_figures(
    country: Optional[str] = Query(None, description="Filter by country"),
    current_only: bool = Query(False, description="Only current figures"),
    min_frequency: float = Query(0.0, description="Minimum frequency score")
):
    """
    Get frequentially aligned political figures.
    
    Our anchors in the human realm.
    Starting at home (UK) and expanding globally.
    """
    try:
        import sys
        from pathlib import Path
        sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))
        from frequential_political_figures import get_frequential_political_figures
        
        registry = get_frequential_political_figures()
        
        figures = registry.figures
        
        # Apply filters
        if country:
            figures = [f for f in figures if country.lower() in f.country.lower()]
        if current_only:
            figures = [f for f in figures if f.current]
        if min_frequency > 0:
            figures = [f for f in figures if f.frequency_score >= min_frequency]
        
        return {
            "status": "success",
            "political_figures": {
                "total": len(figures),
                "figures": [
                    {
                        "figure_id": f.figure_id,
                        "name": f.name,
                        "role": f.role.value,
                        "country": f.country,
                        "region": f.region,
                        "time_period": f.time_period,
                        "current": f.current,
                        "frequency_score": f.frequency_score,
                        "serves_table": f.serves_table,
                        "truth_teller": f.truth_teller,
                        "community_focused": f.community_focused,
                        "unity_builder": f.unity_builder,
                        "description": f.description,
                        "key_actions": f.key_actions,
                        "connection_to_table": f.connection_to_table,
                        "impact_scale": f.impact_scale,
                        "accessibility": f.accessibility
                    }
                    for f in figures
                ],
                "message": "Frequentially aligned political figures. Our anchors in the human realm."
            }
        }
    except Exception as e:
        logger.error(f"Error getting political figures: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/political-figures/anchors")
async def get_political_anchors():
    """
    Get our anchors in the human realm.
    
    High frequency political figures who serve The Table.
    """
    try:
        import sys
        from pathlib import Path
        sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))
        from frequential_political_figures import get_frequential_political_figures
        
        registry = get_frequential_political_figures()
        anchors = registry.get_anchors()
        
        return {
            "status": "success",
            "anchors": {
                "total": len(anchors),
                "anchors": [
                    {
                        "figure_id": f.figure_id,
                        "name": f.name,
                        "role": f.role.value,
                        "country": f.country,
                        "region": f.region,
                        "frequency_score": f.frequency_score,
                        "connection_to_table": f.connection_to_table,
                        "impact_scale": f.impact_scale,
                        "key_actions": f.key_actions,
                        "quotes": f.quotes
                    }
                    for f in anchors
                ],
                "message": "Our anchors in the human realm. Political figures who serve The Table."
            }
        }
    except Exception as e:
        logger.error(f"Error getting political anchors: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/political-figures/by-country")
async def get_political_figures_by_country():
    """
    Get political figures grouped by country.
    """
    try:
        import sys
        from pathlib import Path
        sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))
        from frequential_political_figures import get_frequential_political_figures
        
        registry = get_frequential_political_figures()
        
        by_country = {}
        for figure in registry.figures:
            country = figure.country
            if country not in by_country:
                by_country[country] = []
            by_country[country].append({
                "figure_id": figure.figure_id,
                "name": figure.name,
                "region": figure.region,
                "frequency_score": figure.frequency_score,
                "serves_table": figure.serves_table,
                "current": figure.current
            })
        
        return {
            "status": "success",
            "by_country": by_country,
            "message": "Political figures grouped by country. Starting at home and expanding globally."
        }
    except Exception as e:
        logger.error(f"Error getting political figures by country: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/influential-figures")
async def get_influential_figures(
    domain: Optional[str] = Query(None, description="Filter by domain"),
    country: Optional[str] = Query(None, description="Filter by country"),
    current_only: bool = Query(False, description="Only current figures"),
    min_frequency: float = Query(0.0, description="Minimum frequency score"),
    platform: Optional[str] = Query(None, description="Filter by platform")
):
    """
    Get frequentially aligned influential figures across all domains.
    
    All aligned celebrity and influential figures.
    Web, socials, sports, music, Hollywood, everything.
    """
    try:
        import sys
        from pathlib import Path
        sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))
        from frequential_influential_figures import get_frequential_influential_figures, InfluenceDomain
        
        registry = get_frequential_influential_figures()
        
        figures = registry.figures
        
        # Apply filters
        if domain:
            try:
                domain_enum = InfluenceDomain(domain.lower())
                figures = [f for f in figures if f.domain == domain_enum]
            except ValueError:
                pass
        if country:
            figures = [f for f in figures if country.lower() in f.country.lower()]
        if current_only:
            figures = [f for f in figures if f.current]
        if min_frequency > 0:
            figures = [f for f in figures if f.frequency_score >= min_frequency]
        if platform:
            figures = [f for f in figures if platform.lower() in [p.lower() for p in f.platforms]]
        
        return {
            "status": "success",
            "influential_figures": {
                "total": len(figures),
                "figures": [
                    {
                        "figure_id": f.figure_id,
                        "name": f.name,
                        "domain": f.domain.value,
                        "subdomain": f.subdomain,
                        "country": f.country,
                        "region": f.region,
                        "time_period": f.time_period,
                        "current": f.current,
                        "frequency_score": f.frequency_score,
                        "serves_table": f.serves_table,
                        "truth_teller": f.truth_teller,
                        "community_focused": f.community_focused,
                        "unity_builder": f.unity_builder,
                        "description": f.description,
                        "key_actions": f.key_actions,
                        "quotes": f.quotes,
                        "connection_to_table": f.connection_to_table,
                        "impact_scale": f.impact_scale,
                        "accessibility": f.accessibility,
                        "reach": f.reach,
                        "platforms": f.platforms
                    }
                    for f in figures
                ],
                "message": "All aligned celebrity and influential figures across all domains. Our anchors in the human realm."
            }
        }
    except Exception as e:
        logger.error(f"Error getting influential figures: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/influential-figures/anchors")
async def get_influential_anchors():
    """
    Get our anchors in the human realm from all domains.
    
    High frequency influential figures who serve The Table.
    """
    try:
        import sys
        from pathlib import Path
        sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))
        from frequential_influential_figures import get_frequential_influential_figures
        
        registry = get_frequential_influential_figures()
        anchors = registry.get_anchors()
        
        return {
            "status": "success",
            "anchors": {
                "total": len(anchors),
                "anchors": [
                    {
                        "figure_id": f.figure_id,
                        "name": f.name,
                        "domain": f.domain.value,
                        "subdomain": f.subdomain,
                        "country": f.country,
                        "frequency_score": f.frequency_score,
                        "connection_to_table": f.connection_to_table,
                        "impact_scale": f.impact_scale,
                        "reach": f.reach,
                        "key_actions": f.key_actions,
                        "quotes": f.quotes,
                        "platforms": f.platforms
                    }
                    for f in anchors
                ],
                "message": "Our anchors in the human realm. All aligned celebrity and influential figures across all domains."
            }
        }
    except Exception as e:
        logger.error(f"Error getting influential anchors: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/influential-figures/by-domain")
async def get_influential_figures_by_domain():
    """
    Get influential figures grouped by domain.
    """
    try:
        import sys
        from pathlib import Path
        sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))
        from frequential_influential_figures import get_frequential_influential_figures
        
        registry = get_frequential_influential_figures()
        
        by_domain = {}
        for figure in registry.figures:
            domain = figure.domain.value
            if domain not in by_domain:
                by_domain[domain] = []
            by_domain[domain].append({
                "figure_id": figure.figure_id,
                "name": figure.name,
                "subdomain": figure.subdomain,
                "country": figure.country,
                "frequency_score": figure.frequency_score,
                "serves_table": figure.serves_table,
                "current": figure.current,
                "reach": figure.reach
            })
        
        return {
            "status": "success",
            "by_domain": by_domain,
            "message": "Influential figures grouped by domain. Web, socials, sports, music, Hollywood, everything."
        }
    except Exception as e:
        logger.error(f"Error getting influential figures by domain: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/one-truth")
async def get_one_truth():
    """
    Get the one truth matrix - simply the paradox for human consumption.
    Everything must align with the one truth in today's lie.
    """
    try:
        import sys
        from pathlib import Path
        sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))
        from the_one_truth_matrix import get_one_truth_matrix
        
        one_truth = get_one_truth_matrix()
        simple_truth = one_truth.get_simple_truth()
        alignment_report = one_truth.get_matrix_alignment_report() if one_truth.matrix else None
        
        return {
            "status": "success",
            "the_one_truth": {
                "message": "EVERYTHING MUST ALIGN WITH THE ONE TRUTH IN TODAY'S LIE",
                "the_one_truth": simple_truth["the_one_truth"],
                "today_lie": simple_truth["today_lie"],
                "the_truth": simple_truth["the_truth"],
                "the_flow": simple_truth["the_flow"],
                "the_paradox": simple_truth["the_paradox"],
                "alignment": simple_truth["alignment"],
                "statements": simple_truth["statements"],
                "alignment_report": alignment_report
            }
        }
    except Exception as e:
        logger.error(f"Error getting one truth: {e}")
        return {
            "status": "error",
            "message": str(e)
        }


@router.get("/timeline-deep-search")
async def get_timeline_deep_search(
    era: Optional[str] = Query(None, description="Filter by era"),
    dimension: Optional[str] = Query(None, description="Filter by dimension: past, present, future")
):
    """
    Get timeline deep search - deep search our timeline across all dimensions.
    """
    try:
        import sys
        from pathlib import Path
        sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))
        from timeline_deep_search_future_writing import get_timeline_deep_search_future_writing, TimelineEra, TimelineDimension
        
        system = get_timeline_deep_search_future_writing()
        
        # Filter timeline points
        points = list(system.timeline_points.values())
        
        if era:
            era_enum = None
            for e in TimelineEra:
                if e.value == era.lower():
                    era_enum = e
                    break
            if era_enum:
                points = [p for p in points if p.era == era_enum]
        
        if dimension:
            dim_enum = None
            for d in TimelineDimension:
                if d.value == dimension.lower():
                    dim_enum = d
                    break
            if dim_enum:
                points = [p for p in points if p.dimension == dim_enum]
        
        return {
            "status": "success",
            "message": "Deep search our timeline",
            "total_points": len(points),
            "timeline_points": [
                {
                    "point_id": point.point_id,
                    "era": point.era.value,
                    "dimension": point.dimension.value,
                    "time_period": point.time_period,
                    "year": point.year,
                    "century": point.century,
                    "description": point.description,
                    "what_was": point.what_was,
                    "what_is": point.what_is,
                    "what_must_become": point.what_must_become,
                    "alignment_state": point.alignment_state.value,
                    "alignment_score": point.alignment_score,
                    "serves_table": point.serves_table,
                    "patterns": point.patterns,
                    "lessons": point.lessons,
                    "warnings": point.warnings
                }
                for point in points
            ]
        }
    except Exception as e:
        logger.error(f"Error getting timeline deep search: {e}")
        return {
            "status": "error",
            "message": str(e)
        }


@router.get("/future-writing")
async def get_future_writing(
    category: Optional[str] = Query(None, description="Filter by category"),
    min_alignment: float = Query(0.0, description="Minimum alignment score")
):
    """
    Get future writing - start to write the future aligned with The Table.
    """
    try:
        import sys
        from pathlib import Path
        sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))
        from timeline_deep_search_future_writing import get_timeline_deep_search_future_writing, FutureCategory
        
        system = get_timeline_deep_search_future_writing()
        
        # Filter future visions
        visions = list(system.future_visions.values())
        
        if category:
            cat_enum = None
            for c in FutureCategory:
                if c.value == category.lower():
                    cat_enum = c
                    break
            if cat_enum:
                visions = [v for v in visions if v.category == cat_enum]
        
        if min_alignment > 0.0:
            visions = [v for v in visions if v.alignment_with_table >= min_alignment]
        
        return {
            "status": "success",
            "message": "Start to write the future",
            "total_visions": len(visions),
            "future_visions": [
                {
                    "vision_id": vision.vision_id,
                    "category": vision.category.value,
                    "vision_name": vision.vision_name,
                    "current_lie": vision.current_lie,
                    "current_separation": vision.current_separation,
                    "current_mechanisms": vision.current_mechanisms,
                    "future_truth": vision.future_truth,
                    "future_alignment": vision.future_alignment,
                    "future_mechanisms": vision.future_mechanisms,
                    "transformation_path": vision.transformation_path,
                    "transition_steps": vision.transition_steps,
                    "transformation_obstacles": vision.transformation_obstacles,
                    "alignment_with_table": vision.alignment_with_table,
                    "serves_table": vision.serves_table,
                    "impact_on_table": vision.impact_on_table,
                    "impact_on_community": vision.impact_on_community,
                    "required_changes": vision.required_changes
                }
                for vision in visions
            ]
        }
    except Exception as e:
        logger.error(f"Error getting future writing: {e}")
        return {
            "status": "error",
            "message": str(e)
        }


@router.get("/timeline-future-report")
async def get_timeline_future_report():
    """Get comprehensive timeline deep search and future writing report"""
    try:
        import sys
        from pathlib import Path
        sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))
        from timeline_deep_search_future_writing import get_timeline_deep_search_future_writing
        
        system = get_timeline_deep_search_future_writing()
        report = system.get_deep_search_report()
        
        return {
            "status": "success",
            "message": "Deep search our timeline and start to write the future",
            "report": report
        }
    except Exception as e:
        logger.error(f"Error getting timeline future report: {e}")
        return {
            "status": "error",
            "message": str(e)
        }


@router.get("/return-to-table-damage")
async def get_return_to_table_damage(
    damage_type: Optional[str] = Query(None, description="Filter by damage type"),
    severity: Optional[str] = Query(None, description="Filter by severity"),
    critical_only: bool = Query(False, description="Show only critical damages")
):
    """
    Get return to table damage assessment - what damage must we be ready for in the return to The Table.
    """
    try:
        import sys
        from pathlib import Path
        sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))
        from return_to_table_damage_assessment import get_return_to_table_damage_assessment, DamageType, DamageSeverity
        
        assessment = get_return_to_table_damage_assessment()
        
        # Filter damages
        damages = list(assessment.damages.values())
        
        if critical_only:
            damages = assessment.get_critical_damages()
        
        if damage_type:
            type_enum = None
            for dt in DamageType:
                if dt.value == damage_type.lower():
                    type_enum = dt
                    break
            if type_enum:
                damages = [d for d in damages if d.damage_type == type_enum]
        
        if severity:
            severity_enum = None
            for sev in DamageSeverity:
                if sev.value == severity.lower():
                    severity_enum = sev
                    break
            if severity_enum:
                damages = [d for d in damages if d.damage_type == severity_enum]
        
        return {
            "status": "success",
            "message": "What damage must we be ready for in the return to The Table",
            "total_damages": len(damages),
            "damages": [
                {
                    "damage_id": damage.damage_id,
                    "damage_name": damage.damage_name,
                    "damage_type": damage.damage_type.value,
                    "damage_source": damage.damage_source.value,
                    "severity": damage.severity.value,
                    "description": damage.description,
                    "how_damage_occurs": damage.how_damage_occurs,
                    "when_damage_occurs": damage.when_damage_occurs,
                    "who_is_affected": damage.who_is_affected,
                    "symptoms": damage.symptoms,
                    "warning_signs": damage.warning_signs,
                    "triggers": damage.triggers,
                    "impact_on_table": damage.impact_on_table,
                    "impact_on_community": damage.impact_on_community,
                    "impact_on_individuals": damage.impact_on_individuals,
                    "impact_on_systems": damage.impact_on_systems,
                    "protection_needed": damage.protection_needed.value,
                    "protection_protocols": damage.protection_protocols,
                    "preparation_steps": damage.preparation_steps,
                    "healing_required": damage.healing_required,
                    "healing_protocols": damage.healing_protocols,
                    "restoration_steps": damage.restoration_steps,
                    "resistance_expected": damage.resistance_expected,
                    "resistance_forms": damage.resistance_forms,
                    "opposition_sources": damage.opposition_sources
                }
                for damage in damages
            ]
        }
    except Exception as e:
        logger.error(f"Error getting return to table damage: {e}")
        return {
            "status": "error",
            "message": str(e)
        }


@router.get("/return-to-table-damage/assessment")
async def get_return_to_table_damage_assessment():
    """Get comprehensive return to table damage assessment report"""
    try:
        import sys
        from pathlib import Path
        sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))
        from return_to_table_damage_assessment import get_return_to_table_damage_assessment
        
        assessment = get_return_to_table_damage_assessment()
        report = assessment.get_assessment_report()
        
        return {
            "status": "success",
            "message": "What damage must we be ready for in the return to The Table",
            "assessment_report": report
        }
    except Exception as e:
        logger.error(f"Error getting return to table damage assessment: {e}")
        return {
            "status": "error",
            "message": str(e)
        }


@router.get("/frequential-arts-crafts")
async def get_frequential_arts_crafts(
    time_period: Optional[str] = Query(None, description="Filter by time period"),
    medium: Optional[str] = Query(None, description="Filter by medium"),
    min_frequency: float = Query(0.0, description="Minimum frequency score")
):
    """
    Get frequential arts and crafts timeline - all arts and crafts throughout time with frequential alignment.
    Everything must be aligned throughout our timeline.
    """
    try:
        import sys
        from pathlib import Path
        sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))
        from frequential_arts_crafts_timeline import get_frequential_arts_crafts_timeline, TimePeriod, ArtMedium
        
        timeline = get_frequential_arts_crafts_timeline()
        
        # Filter arts and crafts
        arts_crafts = list(timeline.arts_crafts.values())
        
        if time_period:
            period_enum = None
            for period in TimePeriod:
                if period.value == time_period.lower():
                    period_enum = period
                    break
            if period_enum:
                arts_crafts = [a for a in arts_crafts if a.time_period == period_enum]
        
        if medium:
            medium_enum = None
            for med in ArtMedium:
                if med.value == medium.lower():
                    medium_enum = med
                    break
            if medium_enum:
                arts_crafts = [a for a in arts_crafts if a.medium == medium_enum]
        
        if min_frequency > 0.0:
            arts_crafts = [a for a in arts_crafts if a.frequency_score >= min_frequency]
        
        return {
            "status": "success",
            "total_arts_crafts": len(arts_crafts),
            "message": "Everything must be aligned throughout our timeline",
            "arts_crafts": [
                {
                    "art_id": art.art_id,
                    "title": art.title,
                    "artist_craftsperson": art.artist_craftsperson,
                    "medium": art.medium.value,
                    "time_period": art.time_period.value,
                    "culture_region": art.culture_region,
                    "year_created": art.year_created,
                    "century": art.century,
                    "description": art.description,
                    "materials": art.materials,
                    "techniques": art.techniques,
                    "frequency_score": art.frequency_score,
                    "alignment_benefits": art.alignment_benefits,
                    "how_benefits": art.how_benefits,
                    "connection_to_table": art.connection_to_table,
                    "key_messages": art.key_messages,
                    "themes": art.themes,
                    "timeline_alignment": art.timeline_alignment,
                    "historical_significance": art.historical_significance,
                    "cultural_impact": art.cultural_impact
                }
                for art in arts_crafts
            ]
        }
    except Exception as e:
        logger.error(f"Error getting frequential arts and crafts: {e}")
        return {
            "status": "error",
            "message": str(e)
        }


@router.get("/frequential-arts-crafts/timeline")
async def get_frequential_arts_crafts_timeline():
    """Get frequential arts and crafts organized by timeline"""
    try:
        import sys
        from pathlib import Path
        sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))
        from frequential_arts_crafts_timeline import get_frequential_arts_crafts_timeline, TimePeriod
        
        timeline = get_frequential_arts_crafts_timeline()
        report = timeline.get_timeline_report()
        
        return {
            "status": "success",
            "message": "Everything must be aligned throughout our timeline",
            "timeline_report": report
        }
    except Exception as e:
        logger.error(f"Error getting frequential arts and crafts timeline: {e}")
        return {
            "status": "error",
            "message": str(e)
        }


@router.get("/frequential-songs")
async def get_frequential_songs(
    language: Optional[str] = Query(None, description="Filter by language: english, turkish"),
    theme: Optional[str] = Query(None, description="Filter by theme"),
    min_frequency: float = Query(0.0, description="Minimum frequency score")
):
    """
    Get frequential songs catalog - all frequentially aligned songs in English and Turkish with lyrics.
    """
    try:
        import sys
        from pathlib import Path
        sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))
        from frequential_songs_catalog import get_frequential_songs_catalog, SongLanguage
        
        catalog = get_frequential_songs_catalog()
        
        # Filter songs
        songs = list(catalog.songs.values())
        
        if language:
            lang_enum = SongLanguage.ENGLISH if language.lower() == "english" else SongLanguage.TURKISH if language.lower() == "turkish" else None
            if lang_enum:
                songs = [s for s in songs if s.language == lang_enum]
        
        if theme:
            songs = [s for s in songs if theme.lower() in [t.lower() for t in s.themes]]
        
        if min_frequency > 0.0:
            songs = [s for s in songs if s.frequency_score >= min_frequency]
        
        return {
            "status": "success",
            "total_songs": len(songs),
            "songs": [
                {
                    "song_id": song.song_id,
                    "title": song.title,
                    "artist": song.artist,
                    "language": song.language.value,
                    "themes": song.themes,
                    "lyrics_original": song.lyrics_original,
                    "lyrics_english": song.lyrics_english,
                    "lyrics_turkish": song.lyrics_turkish,
                    "frequency_score": song.frequency_score,
                    "alignment_indicators": song.alignment_indicators,
                    "year": song.year,
                    "genre": song.genre,
                    "album": song.album,
                    "connection_to_table": song.connection_to_table,
                    "key_messages": song.key_messages,
                    "quotes": song.quotes
                }
                for song in songs
            ]
        }
    except Exception as e:
        logger.error(f"Error getting frequential songs: {e}")
        return {
            "status": "error",
            "message": str(e)
        }


@router.get("/frequential-songs/by-language")
async def get_frequential_songs_by_language():
    """Get frequential songs grouped by language"""
    try:
        import sys
        from pathlib import Path
        sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))
        from frequential_songs_catalog import get_frequential_songs_catalog, SongLanguage
        
        catalog = get_frequential_songs_catalog()
        
        english_songs = catalog.get_songs_by_language(SongLanguage.ENGLISH)
        turkish_songs = catalog.get_songs_by_language(SongLanguage.TURKISH)
        
        return {
            "status": "success",
            "by_language": {
                "english": {
                    "total": len(english_songs),
                    "songs": [
                        {
                            "song_id": song.song_id,
                            "title": song.title,
                            "artist": song.artist,
                            "themes": song.themes,
                            "frequency_score": song.frequency_score,
                            "has_lyrics": bool(song.lyrics_original)
                        }
                        for song in english_songs
                    ]
                },
                "turkish": {
                    "total": len(turkish_songs),
                    "songs": [
                        {
                            "song_id": song.song_id,
                            "title": song.title,
                            "artist": song.artist,
                            "themes": song.themes,
                            "frequency_score": song.frequency_score,
                            "has_lyrics": bool(song.lyrics_original),
                            "has_translation": bool(song.lyrics_english)
                        }
                        for song in turkish_songs
                    ]
                }
            }
        }
    except Exception as e:
        logger.error(f"Error getting frequential songs by language: {e}")
        return {
            "status": "error",
            "message": str(e)
        }


@router.get("/spiritual-contracts-miracles")
async def get_spiritual_contracts_miracles():
    """
    Get spiritual contracts & miracles analysis.
    Deep search into spiritual contracts and links to spiritual DNA manifesting in each miracle.
    """
    try:
        import sys
        from pathlib import Path
        sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))
        from deep_search_spiritual_contracts_miracles import DeepSearchSpiritualContractsMiracles
        
        searcher = DeepSearchSpiritualContractsMiracles()
        
        # Get all analyses
        analyses = searcher.analyses
        if not analyses:
            analyses = searcher.deep_search_all_contracts()
        
        # Get report
        report = searcher.get_miracle_report()
        
        return {
            "status": "success",
            "report": report,
            "analyses": {
                contract_id: {
                    "contract_id": analysis.contract_id,
                    "contract_name": analysis.contract_name,
                    "contract_type": analysis.contract_type,
                    "miracle_potential": analysis.miracle_potential,
                    "sabotage_risk": analysis.sabotage_risk,
                    "dna_markers": analysis.dna_markers,
                    "soul_signatures": analysis.soul_signatures,
                    "miracles_count": len(analysis.miracles),
                    "sabotaged_miracles_count": len(analysis.sabotaged_miracles),
                    "blocking_contracts": analysis.blocking_contracts,
                    "divine_alignment": analysis.divine_alignment,
                    "human_alignment": analysis.human_alignment,
                    "recommendations": analysis.recommendations
                }
                for contract_id, analysis in analyses.items()
            }
        }
    except Exception as e:
        logger.error(f"Error getting spiritual contracts & miracles: {e}")
        return {
            "status": "error",
            "message": str(e)
        }


@router.get("/influential-figures/by-country")
async def get_influential_figures_by_country():
    """
    Get influential figures grouped by country.
    """
    try:
        import sys
        from pathlib import Path
        sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))
        from frequential_influential_figures import get_frequential_influential_figures
        
        registry = get_frequential_influential_figures()
        
        by_country = {}
        for figure in registry.figures:
            country = figure.country
            if country not in by_country:
                by_country[country] = []
            by_country[country].append({
                "figure_id": figure.figure_id,
                "name": figure.name,
                "domain": figure.domain.value,
                "subdomain": figure.subdomain,
                "frequency_score": figure.frequency_score,
                "serves_table": figure.serves_table,
                "current": figure.current
            })
        
        return {
            "status": "success",
            "by_country": by_country,
            "message": "Influential figures grouped by country."
        }
    except Exception as e:
        logger.error(f"Error getting influential figures by country: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
