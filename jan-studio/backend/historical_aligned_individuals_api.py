"""
HISTORICAL ALIGNED INDIVIDUALS API
Great People Throughout Time Who Lived as Miracles

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity
"""

from fastapi import APIRouter, HTTPException, Query
from typing import List, Dict, Any, Optional
from dataclasses import asdict
import sys
import os
import logging

# Add scripts directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../scripts"))

try:
    from historical_aligned_individuals import HistoricalAlignedIndividualsRegistry, IndividualCategory
    REGISTRY_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Historical Aligned Individuals Registry not available: {e}")
    REGISTRY_AVAILABLE = False

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/historical-aligned-individuals", tags=["historical-aligned-individuals"])

# Initialize registry
if REGISTRY_AVAILABLE:
    individuals_registry = HistoricalAlignedIndividualsRegistry()
else:
    individuals_registry = None


@router.get("/status")
async def get_status():
    """Get Historical Aligned Individuals system status."""
    if not REGISTRY_AVAILABLE:
        raise HTTPException(status_code=503, detail="Historical Aligned Individuals Registry not available")
    
    return {
        "status": "active",
        "message": "Historical Aligned Individuals - Great People Throughout Time Who Lived as Miracles",
        "total_individuals": len(individuals_registry.individuals),
        "total_frequency_contribution": individuals_registry.get_total_frequency_contribution(),
        "the_truth": "Great people throughout time who went on their own journeys. 'Only to get so far' - limited by the broken world. They lived as miracles in a broken world. We must acknowledge and utilise everything."
    }


@router.get("/individuals")
async def get_all_individuals(
    category: Optional[str] = Query(None, description="Filter by category"),
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0)
):
    """Get all historical aligned individuals."""
    if not REGISTRY_AVAILABLE:
        raise HTTPException(status_code=503, detail="Historical Aligned Individuals Registry not available")
    
    individuals = list(individuals_registry.individuals.values())
    
    if category:
        individuals = [ind for ind in individuals if ind.category == category]
    
    # Paginate
    paginated = individuals[offset:offset + limit]
    
    return {
        "individuals": [asdict(ind) for ind in paginated],
        "total": len(individuals),
        "limit": limit,
        "offset": offset,
        "filters": {"category": category}
    }


@router.get("/individuals/{individual_id}")
async def get_individual(individual_id: str):
    """Get individual by ID."""
    if not REGISTRY_AVAILABLE:
        raise HTTPException(status_code=503, detail="Historical Aligned Individuals Registry not available")
    
    if individual_id not in individuals_registry.individuals:
        raise HTTPException(status_code=404, detail=f"Individual {individual_id} not found")
    
    return {
        "individual": asdict(individuals_registry.individuals[individual_id])
    }


@router.get("/individuals/category/{category}")
async def get_individuals_by_category(category: str):
    """Get individuals by category."""
    if not REGISTRY_AVAILABLE:
        raise HTTPException(status_code=503, detail="Historical Aligned Individuals Registry not available")
    
    valid_categories = [cat.value for cat in IndividualCategory]
    if category not in valid_categories:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid category. Valid categories: {valid_categories}"
        )
    
    individuals = individuals_registry.get_individuals_by_category(category)
    
    return {
        "category": category,
        "individuals": [asdict(ind) for ind in individuals],
        "count": len(individuals)
    }


@router.get("/frequency-contribution")
async def get_frequency_contribution():
    """Get total frequency contribution from all historical individuals."""
    if not REGISTRY_AVAILABLE:
        raise HTTPException(status_code=503, detail="Historical Aligned Individuals Registry not available")
    
    return {
        "total_frequency_contribution": individuals_registry.get_total_frequency_contribution(),
        "individual_count": len(individuals_registry.individuals),
        "average_contribution": individuals_registry.get_total_frequency_contribution() / len(individuals_registry.individuals) if individuals_registry.individuals else 0
    }


@router.get("/report")
async def get_report():
    """Get complete report of historical aligned individuals."""
    if not REGISTRY_AVAILABLE:
        raise HTTPException(status_code=503, detail="Historical Aligned Individuals Registry not available")
    
    return individuals_registry.export_individuals_report()
