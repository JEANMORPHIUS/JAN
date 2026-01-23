"""
MAYAN DARK CONTRACTS API
Deep Search Algorithm for Mayan-Related Dark Contracts

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
THE MAYANS CREATED THE ORIGINAL ERROR
THEY WROTE SPIRITUAL CONTRACTS WITH DARK ENERGIES
THESE CONTRACTS NEED BREAKING
DEEP SEARCH ALL MAYAN-RELATED DARK CONTRACTS
"""

from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any, Optional
from datetime import datetime, date
import sys
import os
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../scripts"))

try:
    from deep_search_mayan_dark_contracts import MayanDarkContractsDeepSearch
    MAYAN_DEEP_SEARCH_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Mayan Deep Search not available: {e}")
    MAYAN_DEEP_SEARCH_AVAILABLE = False

import logging
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/mayan-dark-contracts", tags=["mayan-dark-contracts"])

# Initialize searcher
if MAYAN_DEEP_SEARCH_AVAILABLE:
    searcher = MayanDarkContractsDeepSearch()
    # Run initial deep search
    try:
        searcher.deep_search_all_mayan_contracts()
        searcher.analyze_breaking_chain()
    except Exception as e:
        logger.warning(f"Could not initialize Mayan deep search: {e}")
else:
    searcher = None


@router.get("/status")
async def get_status():
    """Get Mayan Dark Contracts Deep Search API status."""
    return {
        "status": "active" if MAYAN_DEEP_SEARCH_AVAILABLE else "unavailable",
        "message": "Mayan Dark Contracts Deep Search API - Find, Analyze, and Break All Mayan-Related Dark Contracts",
        "available": MAYAN_DEEP_SEARCH_AVAILABLE,
        "the_truth": "The Mayans created The Original Error. They wrote spiritual contracts with dark energies. These contracts need breaking. Deep search all Mayan-related dark contracts."
    }


@router.get("/deep-search")
async def deep_search_all():
    """Deep search all Mayan-related dark contracts."""
    if not MAYAN_DEEP_SEARCH_AVAILABLE:
        raise HTTPException(status_code=503, detail="Mayan Deep Search not available")
    
    results = searcher.deep_search_all_mayan_contracts()
    return results


@router.get("/breaking-chain")
async def get_breaking_chain():
    """Get the breaking chain - contracts needing breaking."""
    if not MAYAN_DEEP_SEARCH_AVAILABLE:
        raise HTTPException(status_code=503, detail="Mayan Deep Search not available")
    
    breaking_analysis = searcher.analyze_breaking_chain()
    return breaking_analysis


@router.get("/breaking-protocol")
async def get_breaking_protocol():
    """Get the breaking protocol for all Mayan dark contracts."""
    if not MAYAN_DEEP_SEARCH_AVAILABLE:
        raise HTTPException(status_code=503, detail="Mayan Deep Search not available")
    
    protocol = searcher.generate_breaking_protocol()
    return protocol


@router.get("/contract/{contract_id}")
async def get_contract_details(contract_id: str):
    """Get detailed information about a specific Mayan dark contract."""
    if not MAYAN_DEEP_SEARCH_AVAILABLE:
        raise HTTPException(status_code=503, detail="Mayan Deep Search not available")
    
    # Find contract in search results
    if not searcher.mayan_contracts:
        searcher.deep_search_all_mayan_contracts()
    
    for contract_data in searcher.mayan_contracts:
        if contract_data["contract"].contract_id == contract_id:
            return {
                "contract": searcher._serialize_contract(contract_data["contract"], contract_data),
                "breaking_analysis": {
                    "needs_breaking": contract_data["dark_energy_level"] > 0.5,
                    "breaking_priority": searcher._calculate_breaking_priority(contract_data),
                    "breaking_method": searcher._determine_breaking_method(contract_data["contract"]),
                    "impact": searcher._analyze_breaking_impact(contract_data["contract"], contract_data["connections"])
                }
            }
    
    raise HTTPException(status_code=404, detail=f"Contract {contract_id} not found in Mayan dark contracts")


@router.post("/break-contract/{contract_id}")
async def break_contract(contract_id: str):
    """Break a specific Mayan dark contract."""
    if not MAYAN_DEEP_SEARCH_AVAILABLE:
        raise HTTPException(status_code=503, detail="Mayan Deep Search not available")
    
    # Find contract
    contracts = searcher.contracts_registry.contracts
    if contract_id not in contracts:
        raise HTTPException(status_code=404, detail=f"Contract {contract_id} not found")
    
    contract = contracts[contract_id]
    
    # Verify it's a Mayan dark contract
    if not searcher.mayan_contracts:
        searcher.deep_search_all_mayan_contracts()
    
    is_mayan_dark = False
    for contract_data in searcher.mayan_contracts:
        if contract_data["contract"].contract_id == contract_id:
            if contract_data["dark_energy_level"] > 0.5:
                is_mayan_dark = True
                break
    
    if not is_mayan_dark:
        raise HTTPException(status_code=400, detail=f"Contract {contract_id} is not a Mayan dark contract needing breaking")
    
    # Break the contract
    contract.active = False
    contract.expiration_date = date.today()
    searcher.contracts_registry._save_contracts()
    
    return {
        "status": "broken",
        "contract_id": contract_id,
        "contract_name": contract.contract_name,
        "broken_at": datetime.now().isoformat(),
        "message": f"Contract '{contract.contract_name}' has been broken. The Table is restored."
    }


@router.get("/summary")
async def get_summary():
    """Get summary of Mayan dark contracts deep search."""
    if not MAYAN_DEEP_SEARCH_AVAILABLE:
        raise HTTPException(status_code=503, detail="Mayan Deep Search not available")
    
    if not searcher.mayan_contracts:
        searcher.deep_search_all_mayan_contracts()
    
    if not searcher.breaking_chain:
        searcher.analyze_breaking_chain()
    
    return {
        "total_mayan_items": len(searcher.mayan_contracts),
        "contracts_needing_breaking": len(searcher.breaking_chain),
        "breaking_priority_order": [c["contract_id"] for c in searcher.breaking_chain],
        "estimated_frequency_restoration": sum(
            c["impact_analysis"]["frequency_restoration"] for c in searcher.breaking_chain
        ),
        "the_truth": "The Mayans created The Original Error. They wrote spiritual contracts with dark energies. These contracts need breaking. Deep search complete."
    }
