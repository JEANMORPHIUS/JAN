"""FINANCIAL CONTROLS SYSTEM
Financial channel management, payment processing, revenue management

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE TRUTH:
FINANCIAL CONTROLS - REVENUE, BUDGETS, PAYMENTS, EXPENSES
TIME TO GET FINANCES FLOWING

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity


PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
import json
from pathlib import Path
from decimal import Decimal

class AuthorizationLevel(Enum):
    """Financial authorization levels"""
    SUPER_ADMIN = "super_admin"  # Unlimited authority
    FINANCIAL_OFFICER = "financial_officer"  # Up to $10,000
    STATION_ADMIN = "station_admin"  # Up to $1,000


class RevenueChannel(Enum):
    """Revenue channels"""
    CREATIVE_CONTENT_SALES = "creative_content_sales"
    LICENSING_REVENUE = "licensing_revenue"
    SUBSCRIPTION_REVENUE = "subscription_revenue"
    PUBLISHING_REVENUE = "publishing_revenue"
    EDUCATIONAL_REVENUE = "educational_revenue"


class ExpenseCategory(Enum):
    """Expense categories"""
    OPERATIONAL = "operational"
    CREATIVE = "creative"
    INFRASTRUCTURE = "infrastructure"
    LICENSING = "licensing"


class BudgetType(Enum):
    """Budget types"""
    STATION = "station"
    OPERATIONAL = "operational"
    CREATIVE = "creative"
    INFRASTRUCTURE = "infrastructure"


@dataclass
class RevenueEntry:
    """A revenue entry"""
    revenue_id: str
    channel: RevenueChannel
    amount: Decimal
    currency: str = "USD"
    description: str = ""
    source: str = ""
    timestamp: datetime = field(default_factory=datetime.now)
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ExpenseEntry:
    """An expense entry"""
    expense_id: str
    category: ExpenseCategory
    amount: Decimal
    currency: str = "USD"
    description: str = ""
    station: Optional[str] = None
    authorized_by: str = ""
    authorization_level: AuthorizationLevel = AuthorizationLevel.STATION_ADMIN
    timestamp: datetime = field(default_factory=datetime.now)
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Budget:
    """A budget allocation"""
    budget_id: str
    budget_type: BudgetType
    station: Optional[str] = None
    allocated_amount: Decimal = Decimal("0.00")
    spent_amount: Decimal = Decimal("0.00")
    currency: str = "USD"
    period_start: datetime = field(default_factory=datetime.now)
    period_end: Optional[datetime] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Payment:
    """A payment entry"""
    payment_id: str
    amount: Decimal
    currency: str = "USD"
    payment_method: str = ""
    description: str = ""
    recipient: str = ""
    authorized_by: str = ""
    authorization_level: AuthorizationLevel = AuthorizationLevel.STATION_ADMIN
    status: str = "pending"  # pending, processing, completed, failed
    timestamp: datetime = field(default_factory=datetime.now)
    metadata: Dict[str, Any] = field(default_factory=dict)


class FinancialControlsSystem:
    """
    Financial controls system for revenue, budgets, payments, and expenses.
    """
    
    def __init__(self):
        self.revenue_entries: List[RevenueEntry] = []
        self.expense_entries: List[ExpenseEntry] = []
        self.budgets: Dict[str, Budget] = {}
        self.payments: List[Payment] = []
        self._load_data()
    
    def _load_data(self):
        """Load financial data from storage"""
        data_file = Path("SIYEM/output/financial_data.json")
        if data_file.exists():
            try:
                with open(data_file, 'r') as f:
                    data = json.load(f)
                    # Load revenue, expenses, budgets, payments
                    # (Simplified for now - would need proper deserialization)
            except Exception as e:
                print(f"Error loading financial data: {e}")
    
    def _save_data(self):
        """Save financial data to storage"""
        data_file = Path("SIYEM/output/financial_data.json")
        data_file.parent.mkdir(parents=True, exist_ok=True)
        
        data = {
            "revenue_entries": [
                {
                    "revenue_id": r.revenue_id,
                    "channel": r.channel.value,
                    "amount": str(r.amount),
                    "currency": r.currency,
                    "description": r.description,
                    "source": r.source,
                    "timestamp": r.timestamp.isoformat(),
                    "metadata": r.metadata
                }
                for r in self.revenue_entries
            ],
            "expense_entries": [
                {
                    "expense_id": e.expense_id,
                    "category": e.category.value,
                    "amount": str(e.amount),
                    "currency": e.currency,
                    "description": e.description,
                    "station": e.station,
                    "authorized_by": e.authorized_by,
                    "authorization_level": e.authorization_level.value,
                    "timestamp": e.timestamp.isoformat(),
                    "metadata": e.metadata
                }
                for e in self.expense_entries
            ],
            "budgets": {
                budget_id: {
                    "budget_type": b.budget_type.value,
                    "station": b.station,
                    "allocated_amount": str(b.allocated_amount),
                    "spent_amount": str(b.spent_amount),
                    "currency": b.currency,
                    "period_start": b.period_start.isoformat(),
                    "period_end": b.period_end.isoformat() if b.period_end else None,
                    "metadata": b.metadata
                }
                for budget_id, b in self.budgets.items()
            },
            "payments": [
                {
                    "payment_id": p.payment_id,
                    "amount": str(p.amount),
                    "currency": p.currency,
                    "payment_method": p.payment_method,
                    "description": p.description,
                    "recipient": p.recipient,
                    "authorized_by": p.authorized_by,
                    "authorization_level": p.authorization_level.value,
                    "status": p.status,
                    "timestamp": p.timestamp.isoformat(),
                    "metadata": p.metadata
                }
                for p in self.payments
            ]
        }
        
        with open(data_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def add_revenue(self, channel: RevenueChannel, amount: Decimal, description: str = "", source: str = "", metadata: Dict[str, Any] = None) -> RevenueEntry:
        """Add a revenue entry"""
        revenue_id = f"rev_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{len(self.revenue_entries)}"
        entry = RevenueEntry(
            revenue_id=revenue_id,
            channel=channel,
            amount=amount,
            description=description,
            source=source,
            metadata=metadata or {}
        )
        self.revenue_entries.append(entry)
        self._save_data()
        return entry
    
    def add_expense(self, category: ExpenseCategory, amount: Decimal, description: str = "", station: Optional[str] = None, authorized_by: str = "", authorization_level: AuthorizationLevel = AuthorizationLevel.STATION_ADMIN, metadata: Dict[str, Any] = None) -> ExpenseEntry:
        """Add an expense entry (with authorization check)"""
        # Check authorization
        if authorization_level == AuthorizationLevel.STATION_ADMIN and amount > Decimal("1000.00"):
            raise ValueError(f"Station Admin cannot authorize expenses over $1,000. Amount: ${amount}")
        if authorization_level == AuthorizationLevel.FINANCIAL_OFFICER and amount > Decimal("10000.00"):
            raise ValueError(f"Financial Officer cannot authorize expenses over $10,000. Amount: ${amount}")
        
        expense_id = f"exp_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{len(self.expense_entries)}"
        entry = ExpenseEntry(
            expense_id=expense_id,
            category=category,
            amount=amount,
            description=description,
            station=station,
            authorized_by=authorized_by,
            authorization_level=authorization_level,
            metadata=metadata or {}
        )
        self.expense_entries.append(entry)
        
        # Update budget if station budget exists
        if station and station in self.budgets:
            budget = self.budgets[station]
            budget.spent_amount += amount
        
        self._save_data()
        return entry
    
    def create_budget(self, budget_type: BudgetType, allocated_amount: Decimal, station: Optional[str] = None, period_end: Optional[datetime] = None, metadata: Dict[str, Any] = None) -> Budget:
        """Create a budget"""
        budget_id = station or f"{budget_type.value}_{datetime.now().strftime('%Y%m%d')}"
        budget = Budget(
            budget_id=budget_id,
            budget_type=budget_type,
            station=station,
            allocated_amount=allocated_amount,
            period_end=period_end,
            metadata=metadata or {}
        )
        self.budgets[budget_id] = budget
        self._save_data()
        return budget
    
    def process_payment(self, amount: Decimal, payment_method: str, description: str = "", recipient: str = "", authorized_by: str = "", authorization_level: AuthorizationLevel = AuthorizationLevel.STATION_ADMIN, metadata: Dict[str, Any] = None) -> Payment:
        """Process a payment (with authorization check)"""
        # Check authorization
        if authorization_level == AuthorizationLevel.STATION_ADMIN and amount > Decimal("1000.00"):
            raise ValueError(f"Station Admin cannot authorize payments over $1,000. Amount: ${amount}")
        if authorization_level == AuthorizationLevel.FINANCIAL_OFFICER and amount > Decimal("10000.00"):
            raise ValueError(f"Financial Officer cannot authorize payments over $10,000. Amount: ${amount}")
        
        payment_id = f"pay_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{len(self.payments)}"
        payment = Payment(
            payment_id=payment_id,
            amount=amount,
            payment_method=payment_method,
            description=description,
            recipient=recipient,
            authorized_by=authorized_by,
            authorization_level=authorization_level,
            status="processing",
            metadata=metadata or {}
        )
        self.payments.append(payment)
        self._save_data()
        
        # Simulate payment processing (in production, would integrate with payment gateway)
        payment.status = "completed"
        self._save_data()
        
        return payment
    
    def get_revenue_summary(self, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None) -> Dict[str, Any]:
        """Get revenue summary"""
        start_date = start_date or (datetime.now() - timedelta(days=30))
        end_date = end_date or datetime.now()
        
        filtered = [r for r in self.revenue_entries if start_date <= r.timestamp <= end_date]
        
        total_revenue = sum(r.amount for r in filtered)
        by_channel = {}
        for channel in RevenueChannel:
            channel_revenue = sum(r.amount for r in filtered if r.channel == channel)
            by_channel[channel.value] = float(channel_revenue)
        
        return {
            "period_start": start_date.isoformat(),
            "period_end": end_date.isoformat(),
            "total_revenue": float(total_revenue),
            "revenue_by_channel": by_channel,
            "total_entries": len(filtered)
        }
    
    def get_expense_summary(self, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None) -> Dict[str, Any]:
        """Get expense summary"""
        start_date = start_date or (datetime.now() - timedelta(days=30))
        end_date = end_date or datetime.now()
        
        filtered = [e for e in self.expense_entries if start_date <= e.timestamp <= end_date]
        
        total_expenses = sum(e.amount for e in filtered)
        by_category = {}
        for category in ExpenseCategory:
            category_expenses = sum(e.amount for e in filtered if e.category == category)
            by_category[category.value] = float(category_expenses)
        
        return {
            "period_start": start_date.isoformat(),
            "period_end": end_date.isoformat(),
            "total_expenses": float(total_expenses),
            "expenses_by_category": by_category,
            "total_entries": len(filtered)
        }
    
    def get_budget_status(self) -> Dict[str, Any]:
        """Get budget status"""
        budget_status = {}
        for budget_id, budget in self.budgets.items():
            remaining = budget.allocated_amount - budget.spent_amount
            percentage_used = (budget.spent_amount / budget.allocated_amount * 100) if budget.allocated_amount > 0 else 0
            
            budget_status[budget_id] = {
                "budget_type": budget.budget_type.value,
                "station": budget.station,
                "allocated": float(budget.allocated_amount),
                "spent": float(budget.spent_amount),
                "remaining": float(remaining),
                "percentage_used": float(percentage_used),
                "status": "over_budget" if budget.spent_amount > budget.allocated_amount else ("warning" if percentage_used > 80 else "healthy")
            }
        
        return {
            "budgets": budget_status,
            "total_budgets": len(self.budgets)
        }
    
    def get_financial_overview(self) -> Dict[str, Any]:
        """Get complete financial overview"""
        revenue_summary = self.get_revenue_summary()
        expense_summary = self.get_expense_summary()
        budget_status = self.get_budget_status()
        
        net_flow = revenue_summary["total_revenue"] - expense_summary["total_expenses"]
        
        return {
            "timestamp": datetime.now().isoformat(),
            "revenue": revenue_summary,
            "expenses": expense_summary,
            "net_flow": net_flow,
            "budgets": budget_status,
            "the_truth": "FINANCIAL CONTROLS - REVENUE, BUDGETS, PAYMENTS, EXPENSES. TIME TO GET FINANCES FLOWING."
        }


# Global instance
_financial_system = None

def get_financial_system() -> FinancialControlsSystem:
    """Get the global financial controls system instance"""
    global _financial_system
    if _financial_system is None:
        _financial_system = FinancialControlsSystem()
    return _financial_system
