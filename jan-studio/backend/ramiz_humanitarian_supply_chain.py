"""
RAMIZ HUMANITARIAN SUPPLY CHAIN
Supply chain management, logistics, delivery tracking

THE NOAH PROTOCOL:
- Architectural Weight: Built for 10x, 100x, 1000x supply operations
- The Pitch: Waterproof error handling
- The Perimeter: Clear supply chain boundaries

THE TRUTH:
NO ONE GETS LEFT BEHIND.
Gaza as priority.
Supply chain is critical for humanitarian aid.
"""

from typing import Dict, List, Any, Optional
from datetime import datetime
from enum import Enum
from dataclasses import dataclass, field
import logging

logger = logging.getLogger(__name__)


class SupplyStatus(Enum):
    """Supply status"""
    ORDERED = "ordered"
    IN_TRANSIT = "in_transit"
    RECEIVED = "received"
    DISTRIBUTED = "distributed"
    DELAYED = "delayed"
    LOST = "lost"


class SupplyType(Enum):
    """Supply types"""
    FOOD = "food"
    WATER = "water"
    MEDICAL = "medical"
    SHELTER = "shelter"
    CLOTHING = "clothing"
    HYGIENE = "hygiene"
    EDUCATION = "education"
    OTHER = "other"


@dataclass
class SupplyOrder:
    """Supply order"""
    order_id: str
    project_id: str
    supply_type: SupplyType
    quantity: float
    unit: str
    priority: str = "high"  # critical, high, medium, low
    supplier: Optional[str] = None
    cost: float = 0.0
    currency: str = "USD"
    status: SupplyStatus = SupplyStatus.ORDERED
    ordered_at: datetime = field(default_factory=datetime.now)
    expected_delivery: Optional[datetime] = None
    received_at: Optional[datetime] = None
    distributed_at: Optional[datetime] = None
    notes: str = ""


@dataclass
class SupplyDelivery:
    """Supply delivery tracking"""
    delivery_id: str
    order_id: str
    location: str
    status: SupplyStatus = SupplyStatus.IN_TRANSIT
    current_location: Optional[str] = None
    estimated_arrival: Optional[datetime] = None
    actual_arrival: Optional[datetime] = None
    tracking_number: Optional[str] = None
    notes: str = ""
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)


class RamizHumanitarianSupplyChain:
    """
    Ramiz Humanitarian Supply Chain
    Manages supply orders, logistics, delivery tracking
    
    Gaza priority for all supply operations.
    """
    
    def __init__(self):
        """Initialize supply chain system"""
        self.orders: Dict[str, SupplyOrder] = {}
        self.deliveries: Dict[str, SupplyDelivery] = {}
        self.gaza_orders: List[str] = []  # order_ids for Gaza priority
        
        logger.info("Ramiz Humanitarian Supply Chain initialized")
    
    def create_order(self, project_id: str, supply_type: SupplyType, quantity: float,
                    unit: str, priority: str = "high", supplier: Optional[str] = None,
                    cost: float = 0.0, currency: str = "USD",
                    expected_delivery: Optional[datetime] = None,
                    notes: str = "") -> SupplyOrder:
        """Create supply order"""
        order_id = f"order_{project_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        order = SupplyOrder(
            order_id=order_id,
            project_id=project_id,
            supply_type=supply_type,
            quantity=quantity,
            unit=unit,
            priority=priority,
            supplier=supplier,
            cost=cost,
            currency=currency,
            status=SupplyStatus.ORDERED,
            expected_delivery=expected_delivery,
            notes=notes
        )
        
        self.orders[order_id] = order
        
        # Track Gaza priority orders
        if project_id == "gaza_comprehensive_aid" or priority == "critical":
            if order_id not in self.gaza_orders:
                self.gaza_orders.append(order_id)
            
            # Send monitoring alert for Gaza supply order
            try:
                from monitoring_enhancements import get_monitoring, AlertLevel
                monitoring = get_monitoring()
                alert_level = AlertLevel.CRITICAL if priority == "critical" else AlertLevel.INFO
                monitoring.add_alert(
                    alert_level,
                    f"Gaza Supply Order: {quantity} {unit} of {supply_type.value} - Priority: {priority}",
                    "ramiz_humanitarian_supply_chain",
                    {
                        "order_id": order_id,
                        "project_id": project_id,
                        "supply_type": supply_type.value,
                        "quantity": quantity,
                        "unit": unit,
                        "priority": priority,
                        "gaza_priority": True
                    }
                )
            except Exception as e:
                logger.warning(f"Could not send monitoring alert: {e}")
        
        logger.info(f"Supply order created: {order_id}, Type: {supply_type.value}, Quantity: {quantity} {unit}")
        
        return order
    
    def track_delivery(self, order_id: str, location: str,
                     tracking_number: Optional[str] = None,
                     estimated_arrival: Optional[datetime] = None,
                     current_location: Optional[str] = None) -> SupplyDelivery:
        """Track supply delivery"""
        if order_id not in self.orders:
            raise ValueError(f"Order not found: {order_id}")
        
        delivery_id = f"delivery_{order_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        delivery = SupplyDelivery(
            delivery_id=delivery_id,
            order_id=order_id,
            location=location,
            status=SupplyStatus.IN_TRANSIT,
            tracking_number=tracking_number,
            estimated_arrival=estimated_arrival,
            current_location=current_location
        )
        
        self.deliveries[delivery_id] = delivery
        
        # Update order status
        order = self.orders[order_id]
        order.status = SupplyStatus.IN_TRANSIT
        
        logger.info(f"Delivery tracking started: {delivery_id}, Order: {order_id}, Location: {location}")
        
        return delivery
    
    def mark_received(self, order_id: str, delivery_id: Optional[str] = None) -> bool:
        """Mark supply as received"""
        if order_id not in self.orders:
            return False
        
        order = self.orders[order_id]
        order.status = SupplyStatus.RECEIVED
        order.received_at = datetime.now()
        
        if delivery_id and delivery_id in self.deliveries:
            delivery = self.deliveries[delivery_id]
            delivery.status = SupplyStatus.RECEIVED
            delivery.actual_arrival = datetime.now()
            delivery.updated_at = datetime.now()
        
        logger.info(f"Supply received: {order_id}")
        
        return True
    
    def mark_distributed(self, order_id: str) -> bool:
        """Mark supply as distributed"""
        if order_id not in self.orders:
            return False
        
        order = self.orders[order_id]
        order.status = SupplyStatus.DISTRIBUTED
        order.distributed_at = datetime.now()
        
        logger.info(f"Supply distributed: {order_id}")
        
        return True
    
    def get_gaza_supply_status(self) -> Dict[str, Any]:
        """Get Gaza supply status"""
        gaza_orders = [o for o in self.orders.values() if o.project_id == "gaza_comprehensive_aid"]
        
        by_type = {}
        by_status = {}
        total_quantity = {}
        total_cost = 0.0
        
        for order in gaza_orders:
            supply_type = order.supply_type.value
            status = order.status.value
            
            by_type[supply_type] = by_type.get(supply_type, 0) + 1
            by_status[status] = by_status.get(status, 0) + 1
            
            if supply_type not in total_quantity:
                total_quantity[supply_type] = 0.0
            total_quantity[supply_type] += order.quantity
            
            total_cost += order.cost
        
        critical_orders = [o for o in gaza_orders if o.priority == "critical"]
        in_transit = [o for o in gaza_orders if o.status == SupplyStatus.IN_TRANSIT]
        received = [o for o in gaza_orders if o.status == SupplyStatus.RECEIVED]
        distributed = [o for o in gaza_orders if o.status == SupplyStatus.DISTRIBUTED]
        
        return {
            "project_id": "gaza_comprehensive_aid",
            "total_orders": len(gaza_orders),
            "critical_orders": len(critical_orders),
            "in_transit": len(in_transit),
            "received": len(received),
            "distributed": len(distributed),
            "by_type": by_type,
            "by_status": by_status,
            "total_quantity": total_quantity,
            "total_cost": total_cost
        }
    
    def get_supply_analytics(self) -> Dict[str, Any]:
        """Get supply chain analytics"""
        total_orders = len(self.orders)
        total_deliveries = len(self.deliveries)
        gaza_orders = len(self.gaza_orders)
        
        by_type = {}
        by_status = {}
        by_priority = {}
        
        for order in self.orders.values():
            supply_type = order.supply_type.value
            status = order.status.value
            priority = order.priority
            
            by_type[supply_type] = by_type.get(supply_type, 0) + 1
            by_status[status] = by_status.get(status, 0) + 1
            by_priority[priority] = by_priority.get(priority, 0) + 1
        
        total_cost = sum(o.cost for o in self.orders.values())
        
        return {
            "total_orders": total_orders,
            "total_deliveries": total_deliveries,
            "gaza_orders": gaza_orders,
            "by_type": by_type,
            "by_status": by_status,
            "by_priority": by_priority,
            "total_cost": total_cost
        }


# Global supply chain instance
_supply_chain: Optional[RamizHumanitarianSupplyChain] = None


def get_humanitarian_supply_chain() -> RamizHumanitarianSupplyChain:
    """Get global humanitarian supply chain instance"""
    global _supply_chain
    if _supply_chain is None:
        _supply_chain = RamizHumanitarianSupplyChain()
    return _supply_chain
