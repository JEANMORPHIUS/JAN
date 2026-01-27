"""
RAMIZ HUMANITARIAN SUPPLY CHAIN API
API endpoints for supply chain management

THE TRUTH:
NO ONE GETS LEFT BEHIND.
Gaza as priority.
Supply chain is critical for humanitarian aid.
"""

from fastapi import APIRouter, HTTPException, status, Query, Body
from typing import Dict, List, Any, Optional
from datetime import datetime
from ramiz_humanitarian_supply_chain import (
    get_humanitarian_supply_chain, SupplyType, SupplyStatus
)
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/ramiz-humanitarian/supply-chain", tags=["Ramiz Humanitarian Supply Chain"])


@router.post("/orders/create")
async def create_order(order_data: Dict[str, Any] = Body(...)):
    """Create supply order"""
    try:
        supply_chain = get_humanitarian_supply_chain()
        
        project_id = order_data["project_id"]
        supply_type_str = order_data["supply_type"]
        quantity = order_data["quantity"]
        unit = order_data["unit"]
        priority = order_data.get("priority", "high")
        supplier = order_data.get("supplier")
        cost = order_data.get("cost", 0.0)
        currency = order_data.get("currency", "USD")
        expected_delivery = None
        if order_data.get("expected_delivery"):
            expected_delivery = datetime.fromisoformat(order_data["expected_delivery"])
        notes = order_data.get("notes", "")
        
        try:
            supply_type = SupplyType(supply_type_str.lower())
        except ValueError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid supply type: {supply_type_str}"
            )
        
        order = supply_chain.create_order(
            project_id=project_id,
            supply_type=supply_type,
            quantity=quantity,
            unit=unit,
            priority=priority,
            supplier=supplier,
            cost=cost,
            currency=currency,
            expected_delivery=expected_delivery,
            notes=notes
        )
        
        return {
            "status": "success",
            "order": {
                "order_id": order.order_id,
                "project_id": order.project_id,
                "supply_type": order.supply_type.value,
                "quantity": order.quantity,
                "unit": order.unit,
                "priority": order.priority,
                "status": order.status.value
            }
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Create order error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to create order: {str(e)}"
        )


@router.post("/deliveries/track")
async def track_delivery(delivery_data: Dict[str, Any] = Body(...)):
    """Track supply delivery"""
    try:
        supply_chain = get_humanitarian_supply_chain()
        
        order_id = delivery_data["order_id"]
        location = delivery_data["location"]
        tracking_number = delivery_data.get("tracking_number")
        estimated_arrival = None
        if delivery_data.get("estimated_arrival"):
            estimated_arrival = datetime.fromisoformat(delivery_data["estimated_arrival"])
        current_location = delivery_data.get("current_location")
        
        delivery = supply_chain.track_delivery(
            order_id=order_id,
            location=location,
            tracking_number=tracking_number,
            estimated_arrival=estimated_arrival,
            current_location=current_location
        )
        
        return {
            "status": "success",
            "delivery": {
                "delivery_id": delivery.delivery_id,
                "order_id": delivery.order_id,
                "location": delivery.location,
                "status": delivery.status.value,
                "tracking_number": delivery.tracking_number
            }
        }
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
    except Exception as e:
        logger.error(f"Track delivery error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to track delivery: {str(e)}"
        )


@router.post("/orders/{order_id}/received")
async def mark_received(order_id: str, delivery_id: Optional[str] = Query(None)):
    """Mark supply as received"""
    try:
        supply_chain = get_humanitarian_supply_chain()
        success = supply_chain.mark_received(order_id, delivery_id)
        
        if not success:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Order not found"
            )
        
        return {"status": "success", "order_id": order_id}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Mark received error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to mark as received"
        )


@router.post("/orders/{order_id}/distributed")
async def mark_distributed(order_id: str):
    """Mark supply as distributed"""
    try:
        supply_chain = get_humanitarian_supply_chain()
        success = supply_chain.mark_distributed(order_id)
        
        if not success:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Order not found"
            )
        
        return {"status": "success", "order_id": order_id}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Mark distributed error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to mark as distributed"
        )


@router.get("/gaza/status")
async def get_gaza_supply_status():
    """Get Gaza supply status"""
    try:
        supply_chain = get_humanitarian_supply_chain()
        return supply_chain.get_gaza_supply_status()
    except Exception as e:
        logger.error(f"Get Gaza supply status error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to get Gaza supply status"
        )


@router.get("/analytics")
async def get_supply_analytics():
    """Get supply chain analytics"""
    try:
        supply_chain = get_humanitarian_supply_chain()
        return supply_chain.get_supply_analytics()
    except Exception as e:
        logger.error(f"Get supply analytics error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to get supply analytics"
        )
