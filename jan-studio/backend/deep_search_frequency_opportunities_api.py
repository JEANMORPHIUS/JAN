"""DEEP SEARCH FREQUENCY OPPORTUNITIES API
API endpoints for deep search algorithm across all domains

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE TRUTH:
DEEP SEARCH FOR BEST FREQUENCY OPPORTUNITIES
ACROSS ALL DOMAINS
WEB, SOCIALS, BUSINESS, E-COMMERCE, GLOBAL SUPPLY CHAIN
CRYPTO PROJECTS, TRANSPORT, SERVICES, CORPORATE
HOLLYWOOD, MUSIC, THE WHOLE PIE

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity


PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

from fastapi import APIRouter, HTTPException, Query
from typing import Dict, Any, List, Optional
import logging
import sys
from pathlib import Path

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

try:
    from deep_search_frequency_opportunities import (
        DeepSearchFrequencyOpportunities,
        OpportunityDomain,
        FrequencyOpportunity
    )
    DEEP_SEARCH_AVAILABLE = True
except ImportError as e:
    DEEP_SEARCH_AVAILABLE = False
    print(f"Warning: Deep Search Frequency Opportunities not available: {e}")

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/deep-search", tags=["Deep Search Frequency Opportunities"])

# Global instance
_search_system = None

def get_search_system() -> DeepSearchFrequencyOpportunities:
    """Get the global deep search system instance"""
    global _search_system
    if _search_system is None and DEEP_SEARCH_AVAILABLE:
        _search_system = DeepSearchFrequencyOpportunities()
    return _search_system


@router.get("/status")
async def get_status():
    """Get Deep Search API status"""
    return {
        "status": "active" if DEEP_SEARCH_AVAILABLE else "unavailable",
        "message": "Deep Search Algorithm for Best Frequency Opportunities - The Whole Pie",
        "available": DEEP_SEARCH_AVAILABLE,
        "domains": [domain.value for domain in OpportunityDomain] if DEEP_SEARCH_AVAILABLE else [],
        "the_truth": "DEEP SEARCH FOR BEST FREQUENCY OPPORTUNITIES ACROSS ALL DOMAINS. WEB, SOCIALS, BUSINESS, E-COMMERCE, GLOBAL SUPPLY CHAIN, CRYPTO PROJECTS, TRANSPORT, SERVICES, CORPORATE, HOLLYWOOD, MUSIC, THE WHOLE PIE."
    }


@router.get("/domains")
async def get_domains():
    """Get all available domains"""
    if not DEEP_SEARCH_AVAILABLE:
        raise HTTPException(status_code=503, detail="Deep Search System not available")
    
    domains = [
        {
            "value": domain.value,
            "name": domain.value.replace("_", " ").title(),
            "description": f"Search {domain.value.replace('_', ' ')} domain for frequency opportunities"
        }
        for domain in OpportunityDomain
        if domain != OpportunityDomain.WHOLE_PIE
    ]
    
    return {
        "status": "success",
        "domains": domains
    }


@router.get("/search")
async def search_opportunities(
    domain: Optional[str] = Query(None, description="Domain to search (e.g., 'music', 'web', 'socials')"),
    keywords: Optional[str] = Query(None, description="Comma-separated keywords"),
    limit: int = Query(50, description="Maximum number of results"),
    min_frequency: float = Query(0.0, description="Minimum frequency score (-1.0 to 1.0)")
):
    """Search for frequency opportunities"""
    if not DEEP_SEARCH_AVAILABLE:
        raise HTTPException(status_code=503, detail="Deep Search System not available")
    
    try:
        system = get_search_system()
        
        # Parse keywords
        keyword_list = [k.strip() for k in keywords.split(",")] if keywords else []
        
        # Search
        if domain:
            try:
                domain_enum = OpportunityDomain(domain.lower())
                opportunities = system.search_domain(domain_enum, keyword_list, limit)
            except ValueError:
                raise HTTPException(status_code=400, detail=f"Invalid domain: {domain}")
        else:
            # Search all domains
            all_results = system.search_all_domains(keyword_list, limit // len(OpportunityDomain))
            opportunities = []
            for opps in all_results.values():
                opportunities.extend(opps)
            opportunities.sort(key=lambda x: x.frequency_score, reverse=True)
            opportunities = opportunities[:limit]
        
        # Filter by minimum frequency
        filtered = [opp for opp in opportunities if opp.frequency_score >= min_frequency]
        
        # Convert to dict
        results = [
            {
                "opportunity_id": opp.opportunity_id,
                "domain": opp.domain.value,
                "title": opp.title,
                "description": opp.description,
                "source": opp.source,
                "frequency_score": opp.frequency_score,
                "impact_potential": opp.impact_potential,
                "alignment_factors": opp.alignment_factors,
                "opportunity_type": opp.opportunity_type,
                "accessibility": opp.accessibility,
                "urgency": opp.urgency,
                "keywords": opp.keywords,
                "metadata": opp.metadata,
                "discovered_at": opp.discovered_at,
                "has_hidden_spiritual_alignment": opp.metadata.get("hidden_spiritual_alignment", False),
                "spiritual_implication": opp.metadata.get("spiritual_implication", ""),
                "historical_context": opp.metadata.get("historical_context", "")
            }
            for opp in filtered
        ]
        
        return {
            "status": "success",
            "domain": domain or "all",
            "keywords": keyword_list,
            "total_found": len(results),
            "opportunities": results
        }
    except Exception as e:
        logger.error(f"Error searching opportunities: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/top-opportunities")
async def get_top_opportunities(
    limit: int = Query(50, description="Maximum number of results"),
    min_frequency: float = Query(0.3, description="Minimum frequency score")
):
    """Get top frequency opportunities across all domains"""
    if not DEEP_SEARCH_AVAILABLE:
        raise HTTPException(status_code=503, detail="Deep Search System not available")
    
    try:
        system = get_search_system()
        
        # Search all domains first
        system.search_all_domains(limit_per_domain=limit // len(OpportunityDomain))
        
        # Get top opportunities
        top_opps = system.get_top_opportunities(limit=limit, min_frequency=min_frequency)
        
        results = [
            {
                "opportunity_id": opp.opportunity_id,
                "domain": opp.domain.value,
                "title": opp.title,
                "description": opp.description,
                "source": opp.source,
                "frequency_score": opp.frequency_score,
                "impact_potential": opp.impact_potential,
                "alignment_factors": opp.alignment_factors,
                "opportunity_type": opp.opportunity_type,
                "accessibility": opp.accessibility,
                "urgency": opp.urgency,
                "keywords": opp.keywords
            }
            for opp in top_opps
        ]
        
        return {
            "status": "success",
            "total": len(results),
            "opportunities": results
        }
    except Exception as e:
        logger.error(f"Error getting top opportunities: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/by-domain/{domain}")
async def get_opportunities_by_domain(
    domain: str,
    limit: int = Query(50, description="Maximum number of results")
):
    """Get opportunities for a specific domain"""
    if not DEEP_SEARCH_AVAILABLE:
        raise HTTPException(status_code=503, detail="Deep Search System not available")
    
    try:
        system = get_search_system()
        
        try:
            domain_enum = OpportunityDomain(domain.lower())
        except ValueError:
            raise HTTPException(status_code=400, detail=f"Invalid domain: {domain}")
        
        opportunities = system.search_domain(domain_enum, limit=limit)
        
        results = [
            {
                "opportunity_id": opp.opportunity_id,
                "title": opp.title,
                "description": opp.description,
                "source": opp.source,
                "frequency_score": opp.frequency_score,
                "impact_potential": opp.impact_potential,
                "alignment_factors": opp.alignment_factors,
                "opportunity_type": opp.opportunity_type,
                "accessibility": opp.accessibility,
                "urgency": opp.urgency
            }
            for opp in opportunities
        ]
        
        return {
            "status": "success",
            "domain": domain,
            "total": len(results),
            "opportunities": results
        }
    except Exception as e:
        logger.error(f"Error getting domain opportunities: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
