"""
SPIRITUAL LINKAGE API
Link Aligned Individuals to Spiritual Contracts - Add Names - Unpick Old Blueprints

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
HAVE WE INGESTED ALL ALIGNED FACTORS?
LINK THE SPIRITUAL.
ADD THE NAMES TO THE CONTRACTS.
UNPICK THE OLD BLUEPRINTS.
"""

from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any, Optional
import sys
import os
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../scripts"))

try:
    from link_aligned_to_spiritual import AlignedSpiritualLinker
    from spiritual_contracts_registry import SpiritualContractsRegistry
    from historical_aligned_individuals import HistoricalAlignedIndividualsRegistry
    SPIRITUAL_LINKAGE_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Spiritual Linkage not available: {e}")
    SPIRITUAL_LINKAGE_AVAILABLE = False

import logging

# Spiritual Codebase Hacker Integration
from spiritual_codebase_hacker_integration import HACKER_AVAILABLE, hack_loop, perform_genetic_edit, activate_stealth_mode

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/spiritual-linkage", tags=["spiritual-linkage"])

# Initialize linker
if SPIRITUAL_LINKAGE_AVAILABLE:
    linker = AlignedSpiritualLinker()
    # Run initial linkage
    try:
        linker.link_aligned_to_contracts()
        linker.unpick_old_blueprints()
        linker.link_spiritual_elements()
    except Exception as e:
        logger.warning(f"Could not initialize spiritual linkage: {e}")
else:
    linker = None


@router.get("/status")
async def get_status():
    """Get Spiritual Linkage API status."""
    return {
        "status": "active" if SPIRITUAL_LINKAGE_AVAILABLE else "unavailable",
        "message": "Spiritual Linkage API - Link Aligned Individuals to Spiritual Contracts",
        "available": SPIRITUAL_LINKAGE_AVAILABLE,
        "the_truth": "Have we ingested all aligned factors? Link the spiritual. Add the names to the contracts. Unpick the old blueprints."
    }


@router.get("/aligned-factors")
async def get_aligned_factors():
    """Get all aligned factors - what we've ingested."""
    if not SPIRITUAL_LINKAGE_AVAILABLE:
        raise HTTPException(status_code=503, detail="Spiritual Linkage not available")
    
    report = linker.ingest_all_aligned_factors()
    return report


@router.get("/contracts-with-names")
async def get_contracts_with_names():
    """Get all contracts with linked individual names."""
    if not SPIRITUAL_LINKAGE_AVAILABLE:
        raise HTTPException(status_code=503, detail="Spiritual Linkage not available")
    
    contracts = linker.contracts_registry.contracts
    aligned_individuals = linker.aligned_registry.get_all_individuals()
    
    contracts_with_names = []
    for contract in contracts.values():
        if contract.linked_individuals:
            names = []
            for ind_id in contract.linked_individuals:
                if ind_id in aligned_individuals:
                    names.append({
                        "individual_id": ind_id,
                        "name": aligned_individuals[ind_id].name,
                        "category": aligned_individuals[ind_id].category,
                        "alignment_score": aligned_individuals[ind_id].alignment_score
                    })
            
            contracts_with_names.append({
                "contract_id": contract.contract_id,
                "contract_name": contract.contract_name,
                "contract_type": contract.contract_type,
                "linked_names": names,
                "narrative": contract.narrative,
                "connection_to_table": contract.purpose
            })
    
    return {
        "contracts_with_names": contracts_with_names,
        "total": len(contracts_with_names),
        "total_names": sum(len(c["linked_names"]) for c in contracts_with_names)
    }


@router.get("/old-blueprints")
async def get_old_blueprints():
    """Get all old blueprints that were unpicked."""
    if not SPIRITUAL_LINKAGE_AVAILABLE:
        raise HTTPException(status_code=503, detail="Spiritual Linkage not available")
    
    blueprints = linker.unpick_old_blueprints()
    return {
        "old_blueprints": blueprints,
        "total": len(blueprints),
        "needing_breaking": len([b for b in blueprints if b["analysis"]["needs_breaking"]]),
        "needing_restoration": len([b for b in blueprints if b["analysis"]["needs_restoration"]])
    }


@router.get("/complete-linkage")
async def get_complete_linkage():
    """Get complete linkage report - everything connected."""
    if not SPIRITUAL_LINKAGE_AVAILABLE:
        raise HTTPException(status_code=503, detail="Spiritual Linkage not available")
    
    report = linker.get_complete_linkage_report()
    return report


@router.post("/link-individual/{individual_id}")
async def link_individual_to_contracts(individual_id: str):
    """Manually link a specific individual to spiritual contracts."""
    if not SPIRITUAL_LINKAGE_AVAILABLE:
        raise HTTPException(status_code=503, detail="Spiritual Linkage not available")
    
    aligned_individuals = linker.aligned_registry.get_all_individuals()
    if individual_id not in aligned_individuals:
        raise HTTPException(status_code=404, detail=f"Individual {individual_id} not found")
    
    individual = aligned_individuals[individual_id]
    
    # Create entity
    entity_id = f"aligned_{individual_id}"
    try:
        entity = linker.contracts_registry.get_or_create_entity(
            entity_name=individual.name,
            entity_type="ascended_master" if individual.alignment_score >= 0.8 else "spirit_guide",
            description=f"Aligned individual: {individual.journey_description}",
            linked_individuals=[individual_id]
        )
        
        # Link to contracts
        linker._link_individual_to_contracts(individual, entity.entity_id)
        
        return {
            "status": "linked",
            "individual_id": individual_id,
            "name": individual.name,
            "entity_id": entity.entity_id,
            "message": f"Linked {individual.name} to spiritual contracts"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error linking individual: {str(e)}")


@router.get("/individual/{individual_id}/contracts")
async def get_individual_contracts(individual_id: str):
    """Get all contracts linked to a specific individual."""
    if not SPIRITUAL_LINKAGE_AVAILABLE:
        raise HTTPException(status_code=503, detail="Spiritual Linkage not available")
    
    contracts = linker.contracts_registry.contracts
    aligned_individuals = linker.aligned_registry.get_all_individuals()
    
    if individual_id not in aligned_individuals:
        raise HTTPException(status_code=404, detail=f"Individual {individual_id} not found")
    
    individual_contracts = []
    for contract in contracts.values():
        if individual_id in contract.linked_individuals:
            individual_contracts.append({
                "contract_id": contract.contract_id,
                "contract_name": contract.contract_name,
                "contract_type": contract.contract_type,
                "narrative": contract.narrative,
                "connection_to_table": contract.purpose
            })
    
    return {
        "individual_id": individual_id,
        "name": aligned_individuals[individual_id].name,
        "contracts": individual_contracts,
        "total": len(individual_contracts)
    }
