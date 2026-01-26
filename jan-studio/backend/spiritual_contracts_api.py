"""SPIRITUAL CONTRACTS API
API endpoints for spiritual contracts registry

Deep search and integration of ALL spiritual contracts.

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
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

from fastapi import APIRouter, HTTPException, Body, Query
from typing import Optional, Dict, Any, List
import logging

# Spiritual Codebase Hacker Integration
from spiritual_codebase_hacker_integration import HACKER_AVAILABLE, hack_loop, perform_genetic_edit, activate_stealth_mode


from spiritual_contracts_registry import (
    get_spiritual_contracts_registry,
    ContractType,
    ContractStatus
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/spiritual-contracts", tags=["Spiritual Contracts"])


@router.get("/all")
async def get_all_contracts(
    contract_type: Optional[str] = Query(None, description="Filter by contract type"),
    status: Optional[str] = Query(None, description="Filter by status"),
    party: Optional[str] = Query(None, description="Filter by party")
):
    """
    Get all spiritual contracts.
    
    Deep search across all systems.
    """
    try:
        registry = get_spiritual_contracts_registry()
        
        contracts = registry.get_all_contracts()
        
        # Filter by type
        if contract_type:
            try:
                type_enum = ContractType(contract_type.lower())
                contracts = [c for c in contracts if c.contract_type == type_enum]
            except ValueError:
                raise HTTPException(status_code=400, detail=f"Invalid contract type: {contract_type}")
        
        # Filter by status
        if status:
            try:
                status_enum = ContractStatus(status.lower())
                contracts = [c for c in contracts if c.status == status_enum]
            except ValueError:
                raise HTTPException(status_code=400, detail=f"Invalid status: {status}")
        
        # Filter by party
        if party:
            contracts = registry.get_contracts_by_party(party)
        
        return {
            "status": "success",
            "total_contracts": len(contracts),
            "contracts": [
                {
                    "contract_id": c.contract_id,
                    "contract_type": c.contract_type.value,
                    "parties": c.parties,
                    "dreamer": c.dreamer,
                    "associate": c.associate,
                    "status": c.status.value,
                    "negative_energy": c.negative_energy,
                    "positive_energy": c.positive_energy,
                    "alignment_score": c.alignment_score,
                    "mission_aligned": c.mission_aligned,
                    "cleaned": c.cleaned,
                    "system_source": c.system_source,
                    "related_contracts": c.related_contracts
                }
                for c in contracts
            ]
        }
    except Exception as e:
        logger.error(f"Error getting contracts: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/summary")
async def get_contracts_summary():
    """Get summary of all spiritual contracts"""
    try:
        registry = get_spiritual_contracts_registry()
        summary = registry.get_system_summary()
        
        return {
            "status": "success",
            "summary": summary
        }
    except Exception as e:
        logger.error(f"Error getting summary: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/network/{contract_id}")
async def get_contract_network(contract_id: str):
    """
    Get the network of contracts connected to a specific contract.
    
    Ties together all related contracts.
    """
    try:
        registry = get_spiritual_contracts_registry()
        network = registry.get_contract_network(contract_id)
        
        return {
            "status": "success",
            "network": network
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(f"Error getting contract network: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/register")
async def register_contract(
    contract_type: str = Body(..., description="Contract type"),
    parties: List[str] = Body(..., description="Parties to the contract"),
    dreamer: Optional[str] = Body(None, description="Dreamer (for dream battles)"),
    associate: Optional[str] = Body(None, description="Associate (for dream battles)"),
    system_source: str = Body("", description="System source"),
    metadata: Optional[Dict[str, Any]] = Body(None, description="Additional metadata")
):
    """Register a new spiritual contract"""
    try:
        registry = get_spiritual_contracts_registry()
        
        try:
            type_enum = ContractType(contract_type.lower())
        except ValueError:
            raise HTTPException(status_code=400, detail=f"Invalid contract type: {contract_type}")
        
        contract = registry.register_contract(
            contract_type=type_enum,
            parties=parties,
            dreamer=dreamer,
            associate=associate,
            system_source=system_source,
            metadata=metadata
        )
        
        return {
            "status": "success",
            "contract": {
                "contract_id": contract.contract_id,
                "contract_type": contract.contract_type.value,
                "parties": contract.parties,
                "status": contract.status.value
            }
        }
    except Exception as e:
        logger.error(f"Error registering contract: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/link")
async def link_contracts(
    contract_id1: str = Body(..., description="First contract ID"),
    contract_id2: str = Body(..., description="Second contract ID")
):
    """Link two contracts together"""
    try:
        registry = get_spiritual_contracts_registry()
        registry.link_contracts(contract_id1, contract_id2)
        
        return {
            "status": "success",
            "message": f"Linked contracts: {contract_id1} <-> {contract_id2}"
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(f"Error linking contracts: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/clean/{contract_id}")
async def clean_contract(
    contract_id: str,
    cleaning_method: str = Body(..., description="Cleaning method"),
    cleaned_by: str = Body("RAMIZ", description="Who cleaned the contract")
):
    """
    Clean a spiritual contract.
    
    RAMIZ leads dirty money cleaning, but all contracts can be cleaned.
    """
    try:
        registry = get_spiritual_contracts_registry()
        contract = registry.clean_contract(contract_id, cleaning_method, cleaned_by)
        
        return {
            "status": "success",
            "message": f"[{cleaned_by}] Contract cleaned",
            "contract": {
                "contract_id": contract.contract_id,
                "status": contract.status.value,
                "cleaned": contract.cleaned,
                "negative_energy": contract.negative_energy
            }
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(f"Error cleaning contract: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/integrate/dirty-money")
async def integrate_dirty_money_contract(
    transaction_id: str = Body(..., description="Transaction ID"),
    spiritual_contract_data: Dict[str, Any] = Body(..., description="Spiritual contract data")
):
    """Integrate spiritual contract from dirty money cleaning system"""
    try:
        registry = get_spiritual_contracts_registry()
        contract = registry.integrate_from_dirty_money_cleaning(transaction_id, spiritual_contract_data)
        
        return {
            "status": "success",
            "message": "[RAMIZ] Dirty money contract integrated",
            "contract": {
                "contract_id": contract.contract_id,
                "contract_type": contract.contract_type.value,
                "cleaning_required": contract.cleaning_required
            }
        }
    except Exception as e:
        logger.error(f"Error integrating dirty money contract: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/integrate/spirit-alignment")
async def integrate_spirit_alignment_contract(
    spirit1_id: str = Body(..., description="First spirit ID"),
    spirit2_id: str = Body(..., description="Second spirit ID"),
    alignment_data: Dict[str, Any] = Body(..., description="Alignment data")
):
    """Integrate spiritual contract from spirit alignment system"""
    try:
        registry = get_spiritual_contracts_registry()
        contract = registry.integrate_from_spirit_alignment(spirit1_id, spirit2_id, alignment_data)
        
        return {
            "status": "success",
            "message": "Spirit alignment contract integrated",
            "contract": {
                "contract_id": contract.contract_id,
                "contract_type": contract.contract_type.value,
                "alignment_score": contract.alignment_score
            }
        }
    except Exception as e:
        logger.error(f"Error integrating spirit alignment contract: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/integrate/dream-battle")
async def integrate_dream_battle(
    dreamer: str = Body(..., description="Dreamer"),
    associate: str = Body(..., description="Associate"),
    dream_data: Dict[str, Any] = Body(..., description="Dream battle data")
):
    """
    Integrate spiritual contract from dream battle.
    
    "Every night we dream, whether vivid or not. Each dream is a spiritual battle 
    between two souls: The dreamer and an associate. Both have spiritual contracts."
    """
    try:
        registry = get_spiritual_contracts_registry()
        contract = registry.integrate_dream_battle(dreamer, associate, dream_data)
        
        return {
            "status": "success",
            "message": "Dream battle contract integrated",
            "contract": {
                "contract_id": contract.contract_id,
                "contract_type": contract.contract_type.value,
                "dreamer": contract.dreamer,
                "associate": contract.associate,
                "status": contract.status.value
            }
        }
    except Exception as e:
        logger.error(f"Error integrating dream battle contract: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/integrate/daily-battle")
async def integrate_daily_battle(
    party1: str = Body(..., description="First party"),
    party2: str = Body(..., description="Second party"),
    battle_data: Dict[str, Any] = Body(..., description="Battle data")
):
    """
    Integrate spiritual contract from daily battle.
    
    "Each day is another battle, both in the human realm and beyond."
    """
    try:
        registry = get_spiritual_contracts_registry()
        contract = registry.integrate_daily_battle(party1, party2, battle_data)
        
        return {
            "status": "success",
            "message": "Daily battle contract integrated",
            "contract": {
                "contract_id": contract.contract_id,
                "contract_type": contract.contract_type.value,
                "parties": contract.parties,
                "status": contract.status.value
            }
        }
    except Exception as e:
        logger.error(f"Error integrating daily battle contract: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
