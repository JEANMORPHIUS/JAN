"""FINANCIAL CONTROLS API
API endpoints for financial controls system

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

from fastapi import APIRouter, HTTPException, Query, Body
from typing import Dict, Any, Optional, List
from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal
import logging
from financial_controls_system import (
    get_financial_system,
    RevenueChannel,
    ExpenseCategory,
    BudgetType,
    AuthorizationLevel
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/financial", tags=["Financial Controls"])

# Request models
class RevenueCreate(BaseModel):
    channel: str
    amount: float
    currency: str = "USD"
    description: str = ""
    source: str = ""
    metadata: Dict[str, Any] = {}

class ExpenseCreate(BaseModel):
    category: str
    amount: float
    currency: str = "USD"
    description: str = ""
    station: Optional[str] = None
    authorized_by: str = ""
    authorization_level: str = "station_admin"
    metadata: Dict[str, Any] = {}

class BudgetCreate(BaseModel):
    budget_type: str
    allocated_amount: float
    station: Optional[str] = None
    period_end: Optional[str] = None
    metadata: Dict[str, Any] = {}

class PaymentCreate(BaseModel):
    amount: float
    currency: str = "USD"
    payment_method: str = ""
    description: str = ""
    recipient: str = ""
    authorized_by: str = ""
    authorization_level: str = "station_admin"
    metadata: Dict[str, Any] = {}


@router.get("/status")
async def get_financial_status():
    """Get Financial Controls API status"""
    return {
        "status": "active",
        "message": "Financial Controls - Revenue, Budgets, Payments, Expenses",
        "the_truth": "FINANCIAL CONTROLS - REVENUE, BUDGETS, PAYMENTS, EXPENSES. TIME TO GET FINANCES FLOWING."
    }


@router.get("/overview")
async def get_financial_overview():
    """Get complete financial overview"""
    try:
        system = get_financial_system()
        overview = system.get_financial_overview()
        return {
            "status": "success",
            "overview": overview
        }
    except Exception as e:
        logger.error(f"Error getting financial overview: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/revenue")
async def add_revenue(revenue: RevenueCreate):
    """Add a revenue entry"""
    try:
        system = get_financial_system()
        
        try:
            channel = RevenueChannel(revenue.channel)
        except ValueError:
            raise HTTPException(status_code=400, detail=f"Invalid revenue channel: {revenue.channel}")
        
        entry = system.add_revenue(
            channel=channel,
            amount=Decimal(str(revenue.amount)),
            description=revenue.description,
            source=revenue.source,
            metadata=revenue.metadata
        )
        
        return {
            "status": "success",
            "message": "Revenue entry added",
            "revenue": {
                "revenue_id": entry.revenue_id,
                "channel": entry.channel.value,
                "amount": float(entry.amount),
                "currency": entry.currency,
                "description": entry.description,
                "timestamp": entry.timestamp.isoformat()
            }
        }
    except Exception as e:
        logger.error(f"Error adding revenue: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/revenue")
async def get_revenue(
    start_date: Optional[str] = Query(None),
    end_date: Optional[str] = Query(None)
):
    """Get revenue summary"""
    try:
        system = get_financial_system()
        
        start = datetime.fromisoformat(start_date) if start_date else None
        end = datetime.fromisoformat(end_date) if end_date else None
        
        summary = system.get_revenue_summary(start_date=start, end_date=end)
        
        return {
            "status": "success",
            "revenue": summary
        }
    except Exception as e:
        logger.error(f"Error getting revenue: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/expenses")
async def add_expense(expense: ExpenseCreate):
    """Add an expense entry"""
    try:
        system = get_financial_system()
        
        try:
            category = ExpenseCategory(expense.category)
            auth_level = AuthorizationLevel(expense.authorization_level)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"Invalid parameter: {str(e)}")
        
        try:
            entry = system.add_expense(
                category=category,
                amount=Decimal(str(expense.amount)),
                description=expense.description,
                station=expense.station,
                authorized_by=expense.authorized_by,
                authorization_level=auth_level,
                metadata=expense.metadata
            )
            
            return {
                "status": "success",
                "message": "Expense entry added",
                "expense": {
                    "expense_id": entry.expense_id,
                    "category": entry.category.value,
                    "amount": float(entry.amount),
                    "currency": entry.currency,
                    "description": entry.description,
                    "timestamp": entry.timestamp.isoformat()
                }
            }
        except ValueError as e:
            raise HTTPException(status_code=403, detail=f"Authorization error: {str(e)}")
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error adding expense: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/expenses")
async def get_expenses(
    start_date: Optional[str] = Query(None),
    end_date: Optional[str] = Query(None)
):
    """Get expense summary"""
    try:
        system = get_financial_system()
        
        start = datetime.fromisoformat(start_date) if start_date else None
        end = datetime.fromisoformat(end_date) if end_date else None
        
        summary = system.get_expense_summary(start_date=start, end_date=end)
        
        return {
            "status": "success",
            "expenses": summary
        }
    except Exception as e:
        logger.error(f"Error getting expenses: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/budgets")
async def create_budget(budget: BudgetCreate):
    """Create a budget"""
    try:
        system = get_financial_system()
        
        try:
            budget_type = BudgetType(budget.budget_type)
        except ValueError:
            raise HTTPException(status_code=400, detail=f"Invalid budget type: {budget.budget_type}")
        
        period_end = datetime.fromisoformat(budget.period_end) if budget.period_end else None
        
        budget_obj = system.create_budget(
            budget_type=budget_type,
            allocated_amount=Decimal(str(budget.allocated_amount)),
            station=budget.station,
            period_end=period_end,
            metadata=budget.metadata
        )
        
        return {
            "status": "success",
            "message": "Budget created",
            "budget": {
                "budget_id": budget_obj.budget_id,
                "budget_type": budget_obj.budget_type.value,
                "allocated_amount": float(budget_obj.allocated_amount),
                "spent_amount": float(budget_obj.spent_amount),
                "currency": budget_obj.currency
            }
        }
    except Exception as e:
        logger.error(f"Error creating budget: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/budgets")
async def get_budgets():
    """Get budget status"""
    try:
        system = get_financial_system()
        status = system.get_budget_status()
        
        return {
            "status": "success",
            "budgets": status
        }
    except Exception as e:
        logger.error(f"Error getting budgets: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/payments")
async def process_payment(payment: PaymentCreate):
    """Process a payment"""
    try:
        system = get_financial_system()
        
        try:
            auth_level = AuthorizationLevel(payment.authorization_level)
        except ValueError:
            raise HTTPException(status_code=400, detail=f"Invalid authorization level: {payment.authorization_level}")
        
        try:
            payment_obj = system.process_payment(
                amount=Decimal(str(payment.amount)),
                payment_method=payment.payment_method,
                description=payment.description,
                recipient=payment.recipient,
                authorized_by=payment.authorized_by,
                authorization_level=auth_level,
                metadata=payment.metadata
            )
            
            return {
                "status": "success",
                "message": "Payment processed",
                "payment": {
                    "payment_id": payment_obj.payment_id,
                    "amount": float(payment_obj.amount),
                    "currency": payment_obj.currency,
                    "status": payment_obj.status,
                    "timestamp": payment_obj.timestamp.isoformat()
                }
            }
        except ValueError as e:
            raise HTTPException(status_code=403, detail=f"Authorization error: {str(e)}")
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error processing payment: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/payments")
async def get_payments():
    """Get payment history"""
    try:
        system = get_financial_system()
        
        payments = [
            {
                "payment_id": p.payment_id,
                "amount": float(p.amount),
                "currency": p.currency,
                "payment_method": p.payment_method,
                "description": p.description,
                "recipient": p.recipient,
                "status": p.status,
                "timestamp": p.timestamp.isoformat()
            }
            for p in system.payments
        ]
        
        return {
            "status": "success",
            "payments": payments,
            "total": len(payments)
        }
    except Exception as e:
        logger.error(f"Error getting payments: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
