"""
RAMIZ HUMANITARIAN FUNDING SYSTEM
Funding tracking, donations, dirty money cleaning integration

THE NOAH PROTOCOL:
- Architectural Weight: Built for 10x, 100x, 1000x funding operations
- The Pitch: Waterproof error handling
- The Perimeter: Clear funding boundaries

THE TRUTH:
NO ONE GETS LEFT BEHIND.
Gaza as priority.
Ramiz leads humanitarian channel.
Dirty money cleaning integrated.
"""

from typing import Dict, List, Any, Optional
from datetime import datetime
from enum import Enum
from dataclasses import dataclass, field
import logging

logger = logging.getLogger(__name__)


class FundingSource(Enum):
    """Funding sources"""
    DONATION = "donation"
    DIRTY_MONEY_CLEANED = "dirty_money_cleaned"  # RAMIZ leads this
    GRANT = "grant"
    CORPORATE_SPONSORSHIP = "corporate_sponsorship"
    GOVERNMENT_FUNDING = "government_funding"
    CROWDFUNDING = "crowdfunding"
    OTHER = "other"


class FundingStatus(Enum):
    """Funding status"""
    PENDING = "pending"
    RECEIVED = "received"
    ALLOCATED = "allocated"
    DISBURSED = "disbursed"
    VERIFIED = "verified"


@dataclass
class Funding:
    """Funding record"""
    funding_id: str
    project_id: str
    amount: float
    currency: str = "USD"
    source: FundingSource = FundingSource.DONATION
    status: FundingStatus = FundingStatus.PENDING
    donor_name: Optional[str] = None
    donor_email: Optional[str] = None
    dirty_money_transaction_id: Optional[str] = None  # If from dirty money cleaning
    notes: str = ""
    created_at: datetime = field(default_factory=datetime.now)
    received_at: Optional[datetime] = None
    allocated_at: Optional[datetime] = None
    disbursed_at: Optional[datetime] = None


class RamizHumanitarianFunding:
    """
    Ramiz Humanitarian Funding System
    Tracks funding, donations, dirty money cleaning integration
    
    RAMIZ IS THE LEAD FOR THIS.
    """
    
    def __init__(self):
        """Initialize funding system"""
        self.fundings: Dict[str, Funding] = {}
        self.project_allocations: Dict[str, float] = {}  # project_id -> allocated amount
        self.gaza_priority_funding: float = 0.0
        
        logger.info("Ramiz Humanitarian Funding System initialized")
    
    def record_funding(self, project_id: str, amount: float, source: FundingSource,
                      donor_name: Optional[str] = None, donor_email: Optional[str] = None,
                      dirty_money_transaction_id: Optional[str] = None,
                      currency: str = "USD", notes: str = "") -> Funding:
        """Record funding"""
        funding_id = f"funding_{project_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        funding = Funding(
            funding_id=funding_id,
            project_id=project_id,
            amount=amount,
            currency=currency,
            source=source,
            status=FundingStatus.RECEIVED,
            donor_name=donor_name,
            donor_email=donor_email,
            dirty_money_transaction_id=dirty_money_transaction_id,
            notes=notes,
            received_at=datetime.now()
        )
        
        self.fundings[funding_id] = funding
        
        # Track Gaza priority funding
        if project_id == "gaza_comprehensive_aid":
            self.gaza_priority_funding += amount
        
        # Update project allocation
        self.project_allocations[project_id] = self.project_allocations.get(project_id, 0.0) + amount
        
        logger.info(f"Funding recorded: {funding_id}, Amount: {amount} {currency}, Project: {project_id}")
        
        return funding
    
    def allocate_funding(self, funding_id: str, project_id: str) -> bool:
        """Allocate funding to project"""
        if funding_id not in self.fundings:
            return False
        
        funding = self.fundings[funding_id]
        funding.status = FundingStatus.ALLOCATED
        funding.allocated_at = datetime.now()
        
        return True
    
    def disburse_funding(self, funding_id: str, amount: float) -> bool:
        """Disburse funding"""
        if funding_id not in self.fundings:
            return False
        
        funding = self.fundings[funding_id]
        funding.status = FundingStatus.DISBURSED
        funding.disbursed_at = datetime.now()
        
        # Update project allocation
        self.project_allocations[funding.project_id] = max(0.0, 
            self.project_allocations.get(funding.project_id, 0.0) - amount)
        
        return True
    
    def integrate_dirty_money_cleaning(self, transaction_id: str, project_id: str,
                                      amount: float) -> Funding:
        """Integrate with dirty money cleaning system"""
        try:
            from dirty_money_cleaning import get_dirty_money_cleaning_system
            
            cleaning_system = get_dirty_money_cleaning_system()
            transaction = cleaning_system.get_transaction(transaction_id)
            
            if transaction and transaction.status.value == "repurposed":
                # Record funding from cleaned dirty money
                funding = self.record_funding(
                    project_id=project_id,
                    amount=amount,
                    source=FundingSource.DIRTY_MONEY_CLEANED,
                    dirty_money_transaction_id=transaction_id,
                    notes=f"From dirty money cleaning: {transaction.source.value}"
                )
                
                logger.info(f"Dirty money cleaning integrated: {transaction_id} -> {project_id}, Amount: {amount}")
                return funding
        except Exception as e:
            logger.warning(f"Could not integrate dirty money cleaning: {e}")
        
        # Fallback: record as regular funding
        return self.record_funding(
            project_id=project_id,
            amount=amount,
            source=FundingSource.DIRTY_MONEY_CLEANED,
            dirty_money_transaction_id=transaction_id,
            notes="Dirty money cleaning integration attempted"
        )
    
    def get_gaza_funding_status(self) -> Dict[str, Any]:
        """Get Gaza funding status"""
        gaza_fundings = [f for f in self.fundings.values() if f.project_id == "gaza_comprehensive_aid"]
        
        total_received = sum(f.amount for f in gaza_fundings if f.status != FundingStatus.PENDING)
        total_allocated = sum(f.amount for f in gaza_fundings if f.status == FundingStatus.ALLOCATED)
        total_disbursed = sum(f.amount for f in gaza_fundings if f.status == FundingStatus.DISBURSED)
        
        by_source = {}
        for f in gaza_fundings:
            source = f.source.value
            by_source[source] = by_source.get(source, 0.0) + f.amount
        
        dirty_money_count = len([f for f in gaza_fundings if f.source == FundingSource.DIRTY_MONEY_CLEANED])
        dirty_money_amount = sum(f.amount for f in gaza_fundings if f.source == FundingSource.DIRTY_MONEY_CLEANED)
        
        return {
            "project_id": "gaza_comprehensive_aid",
            "total_received": total_received,
            "total_allocated": total_allocated,
            "total_disbursed": total_disbursed,
            "pending": total_received - total_allocated - total_disbursed,
            "by_source": by_source,
            "dirty_money_cleaned": {
                "count": dirty_money_count,
                "amount": dirty_money_amount,
                "percentage": (dirty_money_amount / total_received * 100) if total_received > 0 else 0
            },
            "funding_count": len(gaza_fundings)
        }
    
    def get_funding_analytics(self) -> Dict[str, Any]:
        """Get funding analytics"""
        total_funding = sum(f.amount for f in self.fundings.values())
        total_received = sum(f.amount for f in self.fundings.values() if f.status != FundingStatus.PENDING)
        total_allocated = sum(f.amount for f in self.fundings.values() if f.status == FundingStatus.ALLOCATED)
        total_disbursed = sum(f.amount for f in self.fundings.values() if f.status == FundingStatus.DISBURSED)
        
        by_source = {}
        by_status = {}
        by_project = {}
        
        for funding in self.fundings.values():
            source = funding.source.value
            status = funding.status.value
            project = funding.project_id
            
            by_source[source] = by_source.get(source, 0.0) + funding.amount
            by_status[status] = by_status.get(status, 0.0) + funding.amount
            by_project[project] = by_project.get(project, 0.0) + funding.amount
        
        dirty_money_total = sum(f.amount for f in self.fundings.values() 
                               if f.source == FundingSource.DIRTY_MONEY_CLEANED)
        
        return {
            "total_funding": total_funding,
            "total_received": total_received,
            "total_allocated": total_allocated,
            "total_disbursed": total_disbursed,
            "gaza_priority_funding": self.gaza_priority_funding,
            "by_source": by_source,
            "by_status": by_status,
            "by_project": by_project,
            "dirty_money_cleaned": {
                "total": dirty_money_total,
                "percentage": (dirty_money_total / total_received * 100) if total_received > 0 else 0,
                "count": len([f for f in self.fundings.values() if f.source == FundingSource.DIRTY_MONEY_CLEANED])
            },
            "total_donations": len(self.fundings)
        }


# Global funding instance
_funding: Optional[RamizHumanitarianFunding] = None


def get_humanitarian_funding() -> RamizHumanitarianFunding:
    """Get global humanitarian funding instance"""
    global _funding
    if _funding is None:
        _funding = RamizHumanitarianFunding()
    return _funding
