"""DIRTY MONEY CLEANING API
API endpoints for cleaning spiritual contracts and repurposing for humanitarian causes

RAMIZ IS THE LEAD FOR THIS.

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

from datetime import datetime

from dirty_money_cleaning import (
    get_dirty_money_cleaning_system,
    MoneySource,
    CleaningStatus,
    HumanitarianCause,
    DirtyMoneyTransaction,
    HumanitarianProject
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/dirty-money-cleaning", tags=["Dirty Money Cleaning"])


@router.post("/identify")
async def identify_dirty_money(
    amount: float = Body(..., description="Amount of dirty money"),
    source: str = Body(..., description="Source of dirty money"),
    source_details: Optional[Dict[str, Any]] = Body(None, description="Additional source details"),
    transaction_id: Optional[str] = Body(None, description="Optional transaction ID")
):
    """
    Identify dirty money and create transaction record.
    
    RAMIZ leads this process.
    """
    try:
        system = get_dirty_money_cleaning_system()
        
        # Parse source
        try:
            source_enum = MoneySource(source.lower())
        except ValueError:
            raise HTTPException(status_code=400, detail=f"Invalid source: {source}")
        
        transaction = system.identify_dirty_money(
            amount=amount,
            source=source_enum,
            source_details=source_details,
            transaction_id=transaction_id
        )
        
        return {
            "status": "success",
            "message": f"[RAMIZ] Dirty money identified",
            "transaction": {
                "transaction_id": transaction.transaction_id,
                "amount": transaction.amount,
                "currency": transaction.currency,
                "source": transaction.source.value,
                "status": transaction.status.value,
                "spiritual_contract": {
                    "contract_type": transaction.spiritual_contract.contract_type if transaction.spiritual_contract else None,
                    "spiritual_residue": transaction.spiritual_contract.spiritual_residue if transaction.spiritual_contract else [],
                    "negative_energy": transaction.spiritual_contract.negative_energy if transaction.spiritual_contract else 0.0,
                    "cleaned_by": transaction.spiritual_contract.cleaned_by if transaction.spiritual_contract else "RAMIZ"
                } if transaction.spiritual_contract else None,
                "cleaned_by": transaction.cleaned_by
            }
        }
    except Exception as e:
        logger.error(f"Error identifying dirty money: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/clean/{transaction_id}")
async def clean_spiritual_contract(
    transaction_id: str,
    cleaning_method: Optional[str] = Body(None, description="Optional custom cleaning method")
):
    """
    Clean the spiritual contract of dirty money.
    
    RAMIZ leads this process.
    """
    try:
        system = get_dirty_money_cleaning_system()
        
        transaction = system.clean_spiritual_contract(
            transaction_id=transaction_id,
            cleaning_method=cleaning_method
        )
        
        return {
            "status": "success",
            "message": f"[RAMIZ] Spiritual contract cleaned",
            "transaction": {
                "transaction_id": transaction.transaction_id,
                "amount": transaction.amount,
                "status": transaction.status.value,
                "cleaning_progress": transaction.cleaning_progress,
                "spiritual_contract": {
                    "cleaned": transaction.spiritual_contract.cleaned if transaction.spiritual_contract else False,
                    "cleaning_date": transaction.spiritual_contract.cleaning_date.isoformat() if transaction.spiritual_contract and transaction.spiritual_contract.cleaning_date else None,
                    "cleaning_method": transaction.spiritual_contract.cleaning_method if transaction.spiritual_contract else None,
                    "negative_energy": transaction.spiritual_contract.negative_energy if transaction.spiritual_contract else 0.0,
                    "cleaned_by": transaction.spiritual_contract.cleaned_by if transaction.spiritual_contract else "RAMIZ"
                } if transaction.spiritual_contract else None,
                "cleaned_by": transaction.cleaned_by
            }
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Error cleaning spiritual contract: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/repurpose/{transaction_id}")
async def repurpose_for_humanitarian_cause(
    transaction_id: str,
    cause: Optional[str] = Body(None, description="Humanitarian cause"),
    humanitarian_project: Optional[str] = Body(None, description="Project name"),
    repurposed_amount: Optional[float] = Body(None, description="Amount to repurpose")
):
    """
    Repurpose cleaned money for humanitarian cause.
    
    RAMIZ leads this process.
    """
    try:
        system = get_dirty_money_cleaning_system()
        
        # Parse cause if provided
        cause_enum = None
        if cause:
            try:
                cause_enum = HumanitarianCause(cause.lower())
            except ValueError:
                raise HTTPException(status_code=400, detail=f"Invalid cause: {cause}")
        
        transaction, project = system.repurpose_for_humanitarian_cause(
            transaction_id=transaction_id,
            cause=cause_enum,
            humanitarian_project=humanitarian_project,
            repurposed_amount=repurposed_amount
        )
        
        return {
            "status": "success",
            "message": f"[RAMIZ] Money repurposed for humanitarian cause",
            "transaction": {
                "transaction_id": transaction.transaction_id,
                "amount": transaction.amount,
                "status": transaction.status.value,
                "repurposed_for": transaction.repurposed_for.value if transaction.repurposed_for else None,
                "repurposed_amount": transaction.repurposed_amount,
                "repurposed_date": transaction.repurposed_date.isoformat() if transaction.repurposed_date else None,
                "humanitarian_project": transaction.humanitarian_project,
                "cleaned_by": transaction.cleaned_by
            },
            "project": {
                "project_id": project.project_id,
                "name": project.name,
                "cause": project.cause.value,
                "description": project.description,
                "funded_amount": project.funded_amount,
                "funded_date": project.funded_date.isoformat(),
                "status": project.status
            }
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Error repurposing money: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/complete/{transaction_id}")
async def complete_cycle(
    transaction_id: str
):
    """
    Complete the full cycle: Identify -> Clean -> Repurpose -> Complete
    
    RAMIZ leads this process.
    """
    try:
        system = get_dirty_money_cleaning_system()
        
        transaction = system.complete_cycle(transaction_id=transaction_id)
        
        return {
            "status": "success",
            "message": f"[RAMIZ] Cycle complete",
            "transaction": {
                "transaction_id": transaction.transaction_id,
                "amount": transaction.amount,
                "status": transaction.status.value,
                "repurposed_for": transaction.repurposed_for.value if transaction.repurposed_for else None,
                "repurposed_amount": transaction.repurposed_amount,
                "humanitarian_project": transaction.humanitarian_project,
                "cleaned_by": transaction.cleaned_by
            }
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Error completing cycle: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/summary")
async def get_system_summary():
    """
    Get summary of dirty money cleaning system.
    
    RAMIZ leads this system.
    """
    try:
        system = get_dirty_money_cleaning_system()
        summary = system.get_system_summary()
        
        return {
            "status": "success",
            "summary": summary,
            "message": "[RAMIZ] System summary - Dirty money cleaning for humanitarian causes"
        }
    except Exception as e:
        logger.error(f"Error getting summary: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/transactions")
async def get_transactions(
    status: Optional[str] = Query(None, description="Filter by status"),
    source: Optional[str] = Query(None, description="Filter by source")
):
    """Get all transactions"""
    try:
        system = get_dirty_money_cleaning_system()
        
        transactions = list(system.transactions.values())
        
        # Filter by status
        if status:
            try:
                status_enum = CleaningStatus(status.lower())
                transactions = [t for t in transactions if t.status == status_enum]
            except ValueError:
                raise HTTPException(status_code=400, detail=f"Invalid status: {status}")
        
        # Filter by source
        if source:
            try:
                source_enum = MoneySource(source.lower())
                transactions = [t for t in transactions if t.source == source_enum]
            except ValueError:
                raise HTTPException(status_code=400, detail=f"Invalid source: {source}")
        
        return {
            "status": "success",
            "transactions": [
                {
                    "transaction_id": t.transaction_id,
                    "amount": t.amount,
                    "currency": t.currency,
                    "source": t.source.value,
                    "status": t.status.value,
                    "cleaning_progress": t.cleaning_progress,
                    "repurposed_for": t.repurposed_for.value if t.repurposed_for else None,
                    "repurposed_amount": t.repurposed_amount,
                    "humanitarian_project": t.humanitarian_project,
                    "cleaned_by": t.cleaned_by
                }
                for t in transactions
            ]
        }
    except Exception as e:
        logger.error(f"Error getting transactions: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/projects")
async def get_projects(
    cause: Optional[str] = Query(None, description="Filter by cause")
):
    """Get all humanitarian projects"""
    try:
        system = get_dirty_money_cleaning_system()
        
        projects = list(system.projects.values())
        
        # Filter by cause
        if cause:
            try:
                cause_enum = HumanitarianCause(cause.lower())
                projects = [p for p in projects if p.cause == cause_enum]
            except ValueError:
                raise HTTPException(status_code=400, detail=f"Invalid cause: {cause}")
        
        return {
            "status": "success",
            "projects": [
                {
                    "project_id": p.project_id,
                    "name": p.name,
                    "cause": p.cause.value,
                    "description": p.description,
                    "funded_amount": p.funded_amount,
                    "currency": p.currency,
                    "funded_date": p.funded_date.isoformat(),
                    "status": p.status,
                    "source_transactions": p.source_transactions,
                    "location": p.location,
                    "beneficiaries": p.beneficiaries
                }
                for p in projects
            ]
        }
    except Exception as e:
        logger.error(f"Error getting projects: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
