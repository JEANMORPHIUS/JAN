"""
RAMIZ HUMANITARIAN FUNDING API
API endpoints for funding, donations, dirty money cleaning integration

THE TRUTH:
NO ONE GETS LEFT BEHIND.
Gaza as priority.
Ramiz leads humanitarian channel.
"""

from fastapi import APIRouter, HTTPException, status, Query, Body
from typing import Dict, List, Any, Optional
from datetime import datetime
from ramiz_humanitarian_funding import (
    get_humanitarian_funding, FundingSource, FundingStatus
)
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/ramiz-humanitarian/funding", tags=["Ramiz Humanitarian Funding"])


@router.post("/record")
async def record_funding(funding_data: Dict[str, Any] = Body(...)):
    """Record funding"""
    try:
        funding_system = get_humanitarian_funding()
        
        project_id = funding_data["project_id"]
        amount = funding_data["amount"]
        source_str = funding_data.get("source", "donation")
        donor_name = funding_data.get("donor_name")
        donor_email = funding_data.get("donor_email")
        dirty_money_transaction_id = funding_data.get("dirty_money_transaction_id")
        currency = funding_data.get("currency", "USD")
        notes = funding_data.get("notes", "")
        
        try:
            source = FundingSource(source_str.lower())
        except ValueError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid funding source: {source_str}"
            )
        
        funding = funding_system.record_funding(
            project_id=project_id,
            amount=amount,
            source=source,
            donor_name=donor_name,
            donor_email=donor_email,
            dirty_money_transaction_id=dirty_money_transaction_id,
            currency=currency,
            notes=notes
        )
        
        return {
            "status": "success",
            "funding": {
                "funding_id": funding.funding_id,
                "project_id": funding.project_id,
                "amount": funding.amount,
                "currency": funding.currency,
                "source": funding.source.value,
                "status": funding.status.value
            }
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Record funding error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to record funding: {str(e)}"
        )


@router.post("/integrate-dirty-money")
async def integrate_dirty_money(integration_data: Dict[str, Any] = Body(...)):
    """Integrate with dirty money cleaning system"""
    try:
        funding_system = get_humanitarian_funding()
        
        transaction_id = integration_data["transaction_id"]
        project_id = integration_data["project_id"]
        amount = integration_data["amount"]
        
        funding = funding_system.integrate_dirty_money_cleaning(
            transaction_id=transaction_id,
            project_id=project_id,
            amount=amount
        )
        
        return {
            "status": "success",
            "funding": {
                "funding_id": funding.funding_id,
                "project_id": funding.project_id,
                "amount": funding.amount,
                "source": funding.source.value,
                "dirty_money_transaction_id": funding.dirty_money_transaction_id
            }
        }
    except Exception as e:
        logger.error(f"Integrate dirty money error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to integrate dirty money: {str(e)}"
        )


@router.get("/gaza/status")
async def get_gaza_funding_status():
    """Get Gaza funding status"""
    try:
        funding_system = get_humanitarian_funding()
        return funding_system.get_gaza_funding_status()
    except Exception as e:
        logger.error(f"Get Gaza funding status error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to get Gaza funding status"
        )


@router.get("/analytics")
async def get_funding_analytics():
    """Get funding analytics"""
    try:
        funding_system = get_humanitarian_funding()
        return funding_system.get_funding_analytics()
    except Exception as e:
        logger.error(f"Get funding analytics error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to get funding analytics"
        )
