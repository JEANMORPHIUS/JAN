"""LINEAGE CONTRACT SEARCH API
Deep Search Algorithm for Spiritual Contracts - Lineage Connection Recognition

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

CORE PRINCIPLES (NON-NEGOTIABLE):
- Purpose Not Performance: Purpose matters more than performance. Authentic and aligned. Non-negotiable.
- Everything in Moderation: Balance. Not too much, not too little.
- Life Is Simple: Don't complicate it. Keep it simple.
- Be Still and Have Faith: Be still and have faith in revelation. Stillness brings clarity.

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any, Optional
import sys
import os

# Add scripts directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../scripts"))

try:
    from lineage_contract_search import LineageContractSearch, ContractLineageAnalysis
    SYSTEM_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Lineage Contract Search not available: {e}")
    SYSTEM_AVAILABLE = False

router = APIRouter(prefix="/lineage-contract-search", tags=["lineage-contract-search"])

# Initialize search system
if SYSTEM_AVAILABLE:
    search_system = LineageContractSearch()
else:
    search_system = None

@router.get("/status")
async def get_status():
    """Get lineage contract search system status."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Lineage Contract Search system not available")
    
    return {
        "status": "active",
        "total_contracts_analyzed": len(search_system.analyses),
        "total_connections_found": len(search_system.all_connections),
        "message": "Deep search algorithm for spiritual contracts - lineage connection recognition"
    }

@router.post("/search-all")
async def search_all_contracts():
    """Deep search all contracts for lineage connections."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Lineage Contract Search system not available")
    
    try:
        analyses = search_system.deep_search_all_contracts()
        return {
            "status": "completed",
            "total_contracts_analyzed": len(analyses),
            "total_connections_found": len(search_system.all_connections),
            "contracts_with_connections": len([a for a in analyses.values() if a.total_connections > 0]),
            "analyses": [asdict(a) for a in analyses.values()]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during search: {str(e)}")

@router.get("/contract/{contract_id}")
async def get_contract_analysis(contract_id: str):
    """Get lineage analysis for a specific contract."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Lineage Contract Search system not available")
    
    if contract_id not in search_system.analyses:
        # Try to analyze if not already analyzed
        from spiritual_contracts_registry import SpiritualContractsRegistry
        registry = SpiritualContractsRegistry()
        if contract_id in registry.contracts:
            analysis = search_system.analyze_contract_lineage(registry.contracts[contract_id])
            return {"analysis": asdict(analysis)}
        else:
            raise HTTPException(status_code=404, detail=f"Contract {contract_id} not found")
    
    analysis = search_system.analyses[contract_id]
    return {"analysis": asdict(analysis)}

@router.get("/by-being/{being_name}")
async def get_contracts_by_being(being_name: str):
    """Get all contracts connected to a specific awakened being."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Lineage Contract Search system not available")
    
    contracts = search_system.get_contracts_by_being(being_name)
    return {
        "being_name": being_name,
        "contracts": [asdict(a) for a in contracts],
        "count": len(contracts)
    }

@router.get("/by-connection-type/{connection_type}")
async def get_contracts_by_connection_type(connection_type: str):
    """Get all contracts with a specific connection type."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Lineage Contract Search system not available")
    
    valid_types = ["encoded_message", "vibrational_trigger", "dna_memory", "mission", "table_connection"]
    if connection_type not in valid_types:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid connection type. Valid types: {valid_types}"
        )
    
    contracts = search_system.get_contracts_by_connection_type(connection_type)
    return {
        "connection_type": connection_type,
        "contracts": [asdict(a) for a in contracts],
        "count": len(contracts)
    }

@router.get("/top-connected")
async def get_top_connected_contracts(limit: int = 10):
    """Get top contracts by lineage connection score."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Lineage Contract Search system not available")
    
    top_contracts = search_system.get_top_connected_contracts(limit)
    return {
        "limit": limit,
        "contracts": [asdict(a) for a in top_contracts],
        "count": len(top_contracts)
    }

@router.get("/report")
async def get_complete_report():
    """Get complete lineage contract search report."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Lineage Contract Search system not available")
    
    return search_system.export_complete_report()

# Helper function for asdict
def asdict(obj):
    """Convert dataclass to dict."""
    from dataclasses import asdict as dc_asdict
    return dc_asdict(obj)
