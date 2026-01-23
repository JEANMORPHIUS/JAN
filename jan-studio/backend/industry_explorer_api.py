"""
INDUSTRY EXPLORER API
Endpoints for exploring Hollywood and Music Industry

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional
import logging

from hollywood_music_industry_explorer import (
    get_industry_explorer,
    IndustryType,
    IndustryStructure,
    HollywoodMusicIndustryExplorer
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/industry-explorer", tags=["Industry Explorer"])


@router.get("/music-industry")
async def explore_music_industry(
    structure: str = Query("major_labels", description="Structure: major_labels, independent, diy")
):
    """
    Explore music industry through mission lens.
    
    Analyzes:
    - Does it serve stewardship and community?
    - Does it honor song and creative expression?
    - What spiritual battles exist?
    - How do we navigate with right spirits?
    """
    try:
        explorer = get_industry_explorer()
        
        # Parse structure
        structure_enum = IndustryStructure.MAJOR_LABELS
        if structure == "independent":
            structure_enum = IndustryStructure.INDEPENDENT
        elif structure == "diy":
            structure_enum = IndustryStructure.DIY
        
        analysis = explorer.analyze_music_industry(structure_enum)
        
        return {
            "status": "success",
            "analysis": {
                "industry": "music_industry",
                "structure": structure,
                "serves_mission": analysis.serves_mission,
                "honors_song": analysis.honors_song,
                "right_spirits_present": analysis.right_spirits_present,
                "mission_alignment_score": analysis.mission_alignment_score,
                "symbiosis_score": analysis.symbiosis_score,
                "spiritual_battles": [battle.value for battle in analysis.spiritual_battles],
                "gatekeepers": analysis.gatekeepers,
                "opportunities": analysis.opportunities,
                "recommendations": analysis.recommendations,
                "warnings": analysis.warnings
            }
        }
    except Exception as e:
        logger.error(f"Error exploring music industry: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/hollywood")
async def explore_hollywood(
    structure: str = Query("major_labels", description="Structure: major_labels, independent, diy")
):
    """
    Explore Hollywood through mission lens.
    
    Analyzes:
    - Does it serve stewardship and community?
    - Does it honor creative expression?
    - What spiritual battles exist?
    - How do we navigate with right spirits?
    """
    try:
        explorer = get_industry_explorer()
        
        # Parse structure
        structure_enum = IndustryStructure.MAJOR_LABELS
        if structure == "independent":
            structure_enum = IndustryStructure.INDEPENDENT
        elif structure == "diy":
            structure_enum = IndustryStructure.DIY
        
        analysis = explorer.analyze_hollywood(structure_enum)
        
        return {
            "status": "success",
            "analysis": {
                "industry": "hollywood",
                "structure": structure,
                "serves_mission": analysis.serves_mission,
                "honors_creative": analysis.honors_song,
                "right_spirits_present": analysis.right_spirits_present,
                "mission_alignment_score": analysis.mission_alignment_score,
                "symbiosis_score": analysis.symbiosis_score,
                "spiritual_battles": [battle.value for battle in analysis.spiritual_battles],
                "gatekeepers": analysis.gatekeepers,
                "opportunities": analysis.opportunities,
                "recommendations": analysis.recommendations,
                "warnings": analysis.warnings
            }
        }
    except Exception as e:
        logger.error(f"Error exploring Hollywood: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/navigation-strategy")
async def get_navigation_strategy(
    industry: str = Query("music_industry", description="Industry: music_industry or hollywood"),
    structure: str = Query("major_labels", description="Structure: major_labels, independent, diy"),
    mission_aligned: bool = Query(True, description="Are you mission-aligned?")
):
    """
    Get navigation strategy for industry.
    
    How to navigate with right spirits while serving mission.
    """
    try:
        explorer = get_industry_explorer()
        
        # Parse industry
        industry_enum = IndustryType.MUSIC_INDUSTRY
        if industry == "hollywood":
            industry_enum = IndustryType.HOLLYWOOD
        
        # Parse structure
        structure_enum = IndustryStructure.MAJOR_LABELS
        if structure == "independent":
            structure_enum = IndustryStructure.INDEPENDENT
        elif structure == "diy":
            structure_enum = IndustryStructure.DIY
        
        strategy = explorer.get_navigation_strategy(
            industry_enum,
            structure_enum,
            mission_aligned
        )
        
        return {
            "status": "success",
            "navigation_strategy": strategy
        }
    except Exception as e:
        logger.error(f"Error getting navigation strategy: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/compare")
async def compare_industries():
    """
    Compare Hollywood and Music Industry through mission lens.
    
    Shows which structures best serve mission and honor creative expression.
    """
    try:
        explorer = get_industry_explorer()
        comparison = explorer.compare_industries()
        
        return {
            "status": "success",
            "comparison": comparison
        }
    except Exception as e:
        logger.error(f"Error comparing industries: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/all-industries")
async def explore_all_industries():
    """
    Explore ALL industries - the whole cake.
    
    Analyzes:
    - Music Industry
    - Hollywood
    - Sports
    - TV/Pay-Per-View
    - News Media
    - Global Economics
    - Finance
    
    Shows which structures best serve mission across all industries.
    """
    try:
        explorer = get_industry_explorer()
        all_industries = explorer.explore_all_industries()
        
        return {
            "status": "success",
            "all_industries": {
                name: {
                    "major": {
                        "symbiosis_score": data["major"].symbiosis_score,
                        "serves_mission": data["major"].serves_mission,
                        "honors_creative": data["major"].honors_song,
                        "right_spirits": data["major"].right_spirits_present,
                        "spiritual_battles": [b.value for b in data["major"].spiritual_battles],
                        "gatekeepers": data["major"].gatekeepers,
                        "recommendations": data["major"].recommendations,
                        "warnings": data["major"].warnings
                    },
                    "independent": {
                        "symbiosis_score": data["independent"].symbiosis_score,
                        "serves_mission": data["independent"].serves_mission,
                        "honors_creative": data["independent"].honors_song,
                        "right_spirits": data["independent"].right_spirits_present,
                        "spiritual_battles": [b.value for b in data["independent"].spiritual_battles],
                        "gatekeepers": data["independent"].gatekeepers,
                        "recommendations": data["independent"].recommendations
                    },
                    "diy": {
                        "symbiosis_score": data["diy"].symbiosis_score,
                        "serves_mission": data["diy"].serves_mission,
                        "honors_creative": data["diy"].honors_song,
                        "right_spirits": data["diy"].right_spirits_present,
                        "spiritual_battles": [b.value for b in data["diy"].spiritual_battles],
                        "gatekeepers": data["diy"].gatekeepers,
                        "recommendations": data["diy"].recommendations
                    }
                }
                for name, data in all_industries["industries"].items()
            },
            "summary": all_industries["summary"]
        }
    except Exception as e:
        logger.error(f"Error exploring all industries: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/sports")
async def explore_sports(
    structure: str = Query("major_labels", description="Structure: major_labels, independent, diy")
):
    """Explore sports industry through mission lens"""
    try:
        explorer = get_industry_explorer()
        structure_enum = IndustryStructure.MAJOR_LABELS
        if structure == "independent":
            structure_enum = IndustryStructure.INDEPENDENT
        elif structure == "diy":
            structure_enum = IndustryStructure.DIY
        
        analysis = explorer.analyze_sports(structure_enum)
        
        return {
            "status": "success",
            "analysis": {
                "industry": "sports",
                "structure": structure,
                "serves_mission": analysis.serves_mission,
                "honors_community": analysis.honors_song,
                "right_spirits_present": analysis.right_spirits_present,
                "mission_alignment_score": analysis.mission_alignment_score,
                "symbiosis_score": analysis.symbiosis_score,
                "spiritual_battles": [battle.value for battle in analysis.spiritual_battles],
                "gatekeepers": analysis.gatekeepers,
                "opportunities": analysis.opportunities,
                "recommendations": analysis.recommendations,
                "warnings": analysis.warnings
            }
        }
    except Exception as e:
        logger.error(f"Error exploring sports: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/tv-ppv")
async def explore_tv_ppv(
    structure: str = Query("major_labels", description="Structure: major_labels, independent, diy")
):
    """Explore TV/Pay-Per-View through mission lens"""
    try:
        explorer = get_industry_explorer()
        structure_enum = IndustryStructure.MAJOR_LABELS
        if structure == "independent":
            structure_enum = IndustryStructure.INDEPENDENT
        elif structure == "diy":
            structure_enum = IndustryStructure.DIY
        
        analysis = explorer.analyze_tv_pay_per_view(structure_enum)
        
        return {
            "status": "success",
            "analysis": {
                "industry": "tv_pay_per_view",
                "structure": structure,
                "serves_mission": analysis.serves_mission,
                "honors_access": analysis.honors_song,
                "right_spirits_present": analysis.right_spirits_present,
                "mission_alignment_score": analysis.mission_alignment_score,
                "symbiosis_score": analysis.symbiosis_score,
                "spiritual_battles": [battle.value for battle in analysis.spiritual_battles],
                "gatekeepers": analysis.gatekeepers,
                "opportunities": analysis.opportunities,
                "recommendations": analysis.recommendations,
                "warnings": analysis.warnings
            }
        }
    except Exception as e:
        logger.error(f"Error exploring TV/PPV: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/news-media")
async def explore_news_media(
    structure: str = Query("major_labels", description="Structure: major_labels, independent, diy")
):
    """Explore news media through mission lens"""
    try:
        explorer = get_industry_explorer()
        structure_enum = IndustryStructure.MAJOR_LABELS
        if structure == "independent":
            structure_enum = IndustryStructure.INDEPENDENT
        elif structure == "diy":
            structure_enum = IndustryStructure.DIY
        
        analysis = explorer.analyze_news_media(structure_enum)
        
        return {
            "status": "success",
            "analysis": {
                "industry": "news_media",
                "structure": structure,
                "serves_mission": analysis.serves_mission,
                "honors_truth": analysis.honors_song,
                "right_spirits_present": analysis.right_spirits_present,
                "mission_alignment_score": analysis.mission_alignment_score,
                "symbiosis_score": analysis.symbiosis_score,
                "spiritual_battles": [battle.value for battle in analysis.spiritual_battles],
                "gatekeepers": analysis.gatekeepers,
                "opportunities": analysis.opportunities,
                "recommendations": analysis.recommendations,
                "warnings": analysis.warnings
            }
        }
    except Exception as e:
        logger.error(f"Error exploring news media: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/global-economics")
async def explore_global_economics(
    structure: str = Query("major_labels", description="Structure: major_labels, independent, diy")
):
    """Explore global economics through mission lens"""
    try:
        explorer = get_industry_explorer()
        structure_enum = IndustryStructure.MAJOR_LABELS
        if structure == "independent":
            structure_enum = IndustryStructure.INDEPENDENT
        elif structure == "diy":
            structure_enum = IndustryStructure.DIY
        
        analysis = explorer.analyze_global_economics(structure_enum)
        
        return {
            "status": "success",
            "analysis": {
                "industry": "global_economics",
                "structure": structure,
                "serves_mission": analysis.serves_mission,
                "honors_stewardship": analysis.honors_song,
                "right_spirits_present": analysis.right_spirits_present,
                "mission_alignment_score": analysis.mission_alignment_score,
                "symbiosis_score": analysis.symbiosis_score,
                "spiritual_battles": [battle.value for battle in analysis.spiritual_battles],
                "gatekeepers": analysis.gatekeepers,
                "opportunities": analysis.opportunities,
                "recommendations": analysis.recommendations,
                "warnings": analysis.warnings
            }
        }
    except Exception as e:
        logger.error(f"Error exploring global economics: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/finance")
async def explore_finance(
    structure: str = Query("major_labels", description="Structure: major_labels, independent, diy")
):
    """Explore finance industry through mission lens"""
    try:
        explorer = get_industry_explorer()
        structure_enum = IndustryStructure.MAJOR_LABELS
        if structure == "independent":
            structure_enum = IndustryStructure.INDEPENDENT
        elif structure == "diy":
            structure_enum = IndustryStructure.DIY
        
        analysis = explorer.analyze_finance(structure_enum)
        
        return {
            "status": "success",
            "analysis": {
                "industry": "finance",
                "structure": structure,
                "serves_mission": analysis.serves_mission,
                "honors_community": analysis.honors_song,
                "right_spirits_present": analysis.right_spirits_present,
                "mission_alignment_score": analysis.mission_alignment_score,
                "symbiosis_score": analysis.symbiosis_score,
                "spiritual_battles": [battle.value for battle in analysis.spiritual_battles],
                "gatekeepers": analysis.gatekeepers,
                "opportunities": analysis.opportunities,
                "recommendations": analysis.recommendations,
                "warnings": analysis.warnings
            }
        }
    except Exception as e:
        logger.error(f"Error exploring finance: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/live-events")
async def explore_live_events(
    structure: str = Query("major_labels", description="Structure: major_labels, independent, diy")
):
    """Explore live events industry through mission lens"""
    try:
        explorer = get_industry_explorer()
        structure_enum = IndustryStructure.MAJOR_LABELS
        if structure == "independent":
            structure_enum = IndustryStructure.INDEPENDENT
        elif structure == "diy":
            structure_enum = IndustryStructure.DIY
        
        analysis = explorer.analyze_live_events(structure_enum)
        
        return {
            "status": "success",
            "analysis": {
                "industry": "live_events",
                "structure": structure,
                "serves_mission": analysis.serves_mission,
                "honors_community": analysis.honors_song,
                "right_spirits_present": analysis.right_spirits_present,
                "mission_alignment_score": analysis.mission_alignment_score,
                "symbiosis_score": analysis.symbiosis_score,
                "spiritual_battles": [battle.value for battle in analysis.spiritual_battles],
                "gatekeepers": analysis.gatekeepers,
                "opportunities": analysis.opportunities,
                "recommendations": analysis.recommendations,
                "warnings": analysis.warnings
            }
        }
    except Exception as e:
        logger.error(f"Error exploring live events: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/shady-business")
async def explore_shady_business(
    structure: str = Query("major_labels", description="Structure: major_labels, independent, diy"),
    business_type: str = Query("general", description="Type of shady business")
):
    """Explore 'shady business' - necessary but problematic industries - and recycling strategy"""
    try:
        explorer = get_industry_explorer()
        structure_enum = IndustryStructure.MAJOR_LABELS
        if structure == "independent":
            structure_enum = IndustryStructure.INDEPENDENT
        elif structure == "diy":
            structure_enum = IndustryStructure.DIY
        
        analysis = explorer.analyze_shady_business(structure_enum, business_type)
        recycling_strategy = explorer.get_recycling_strategy(
            IndustryType.SHADY_BUSINESS,
            why_necessary="Path requires it"
        )
        
        return {
            "status": "success",
            "analysis": {
                "industry": "shady_business",
                "structure": structure,
                "business_type": business_type,
                "serves_mission": analysis.serves_mission,
                "honors_mission": analysis.honors_song,
                "right_spirits_present": analysis.right_spirits_present,
                "mission_alignment_score": analysis.mission_alignment_score,
                "symbiosis_score": analysis.symbiosis_score,
                "spiritual_battles": [battle.value for battle in analysis.spiritual_battles],
                "gatekeepers": analysis.gatekeepers,
                "opportunities": analysis.opportunities,
                "recommendations": analysis.recommendations,
                "warnings": analysis.warnings
            },
            "recycling_strategy": recycling_strategy
        }
    except Exception as e:
        logger.error(f"Error exploring shady business: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/recycling-strategy")
async def get_recycling_strategy(
    industry_type: str = Query("shady_business", description="Industry type"),
    why_necessary: str = Query("Path requires it", description="Why this business is necessary")
):
    """Get recycling strategy for necessary but problematic industry"""
    try:
        explorer = get_industry_explorer()
        
        # Map string to IndustryType
        industry_map = {
            "shady_business": IndustryType.SHADY_BUSINESS,
            "music_industry": IndustryType.MUSIC_INDUSTRY,
            "hollywood": IndustryType.HOLLYWOOD,
            "sports": IndustryType.SPORTS,
            "live_events": IndustryType.LIVE_EVENTS,
            "finance": IndustryType.FINANCE,
            "global_economics": IndustryType.GLOBAL_ECONOMICS
        }
        
        industry_enum = industry_map.get(industry_type, IndustryType.SHADY_BUSINESS)
        strategy = explorer.get_recycling_strategy(industry_enum, why_necessary)
        
        return {
            "status": "success",
            "recycling_strategy": strategy
        }
    except Exception as e:
        logger.error(f"Error getting recycling strategy: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
