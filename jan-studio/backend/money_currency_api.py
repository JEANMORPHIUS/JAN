"""MONEY/CURRENCY SYSTEM API
Gift economy, time banking, community currencies, debt jubilee

Money is a tool, not a cage. We design exchange to serve life, not control it.

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity


PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, Dict, List
from datetime import datetime
from enum import Enum
import uuid

router = APIRouter()

# ============================================================================
# ENUMS
# ============================================================================

class CurrencyType(str, Enum):
    COMMUNITY_CREDIT = "community_credit"
    TIME_BANK = "time_bank"
    GIFT_CIRCLE = "gift_circle"
    MUTUAL_AID = "mutual_aid"

class GiftType(str, Enum):
    SERVICE = "service"
    GOODS = "goods"
    TIME = "time"
    CARE = "care"

# ============================================================================
# MODELS
# ============================================================================

class CommunityCurrency(BaseModel):
    currency_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    symbol: str
    region: str
    currency_type: CurrencyType
    issuance_model: str = "community_governed"
    pegged_to_hours: bool = True
    created_date: datetime = Field(default_factory=datetime.now)

class TimeBankAccount(BaseModel):
    account_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    person_id: str
    person_name: str
    hours_balance: float = 0.0
    service_categories: List[str]
    created_date: datetime = Field(default_factory=datetime.now)

class TimeBankEntry(BaseModel):
    entry_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    account_id: str
    hours: float
    description: str
    entry_date: datetime = Field(default_factory=datetime.now)

class GiftContribution(BaseModel):
    gift_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    giver_id: str
    receiver_id: str
    gift_type: GiftType
    description: str
    estimated_value: Optional[float] = None
    gift_date: datetime = Field(default_factory=datetime.now)

class DebtJubileeCase(BaseModel):
    case_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    person_id: str
    person_name: str
    creditor_name: str
    original_debt: float
    forgiven_amount: float
    reason: str
    jubilee_date: datetime = Field(default_factory=datetime.now)

class MutualCreditTransaction(BaseModel):
    transaction_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    from_account_id: str
    to_account_id: str
    amount: float
    memo: str
    transaction_date: datetime = Field(default_factory=datetime.now)

# ============================================================================
# STORAGE
# ============================================================================

currencies_db: Dict[str, CommunityCurrency] = {}
timebank_accounts_db: Dict[str, TimeBankAccount] = {}
timebank_entries_db: Dict[str, TimeBankEntry] = {}
gifts_db: Dict[str, GiftContribution] = {}
debt_jubilee_db: Dict[str, DebtJubileeCase] = {}
mutual_credit_db: Dict[str, MutualCreditTransaction] = {}

# ============================================================================
# ENDPOINTS
# ============================================================================

@router.post("/currency/community/create")
async def create_community_currency(currency: CommunityCurrency):
    """
    Create a community currency or time bank system.
    """
    currency.pegged_to_hours = True
    currencies_db[currency.currency_id] = currency

    return {
        "success": True,
        "currency_id": currency.currency_id,
        "name": currency.name,
        "symbol": currency.symbol,
        "region": currency.region,
        "currency_type": currency.currency_type,
        "message": f"Community currency created: {currency.name}",
        "one_truth": "Exchange should serve people, not profit."
    }

@router.post("/currency/timebank/account/create")
async def create_timebank_account(account: TimeBankAccount):
    """
    Create a time bank account. One hour given = one hour received.
    """
    timebank_accounts_db[account.account_id] = account

    return {
        "success": True,
        "account_id": account.account_id,
        "person_name": account.person_name,
        "hours_balance": account.hours_balance,
        "message": f"Time bank account created for {account.person_name}",
        "one_truth": "Every hour of life has equal value."
    }

@router.post("/currency/timebank/earn")
async def earn_timebank_hours(entry: TimeBankEntry):
    """
    Record earned hours in a time bank.
    """
    if entry.account_id not in timebank_accounts_db:
        raise HTTPException(status_code=404, detail="Time bank account not found")
    timebank_entries_db[entry.entry_id] = entry
    timebank_accounts_db[entry.account_id].hours_balance += entry.hours

    return {
        "success": True,
        "entry_id": entry.entry_id,
        "account_id": entry.account_id,
        "hours_added": entry.hours,
        "new_balance": timebank_accounts_db[entry.account_id].hours_balance,
        "message": "Time bank hours recorded",
        "one_truth": "Giving time is giving life."
    }

@router.post("/currency/timebank/spend")
async def spend_timebank_hours(entry: TimeBankEntry):
    """
    Spend hours from a time bank account.
    """
    if entry.account_id not in timebank_accounts_db:
        raise HTTPException(status_code=404, detail="Time bank account not found")
    account = timebank_accounts_db[entry.account_id]
    if account.hours_balance < entry.hours:
        raise HTTPException(status_code=400, detail="Insufficient hours balance")

    timebank_entries_db[entry.entry_id] = entry
    account.hours_balance -= entry.hours

    return {
        "success": True,
        "entry_id": entry.entry_id,
        "account_id": entry.account_id,
        "hours_spent": entry.hours,
        "new_balance": account.hours_balance,
        "message": "Time bank hours spent",
        "one_truth": "Exchange is mutual care."
    }

@router.post("/currency/gift/record")
async def record_gift(gift: GiftContribution):
    """
    Record a gift contribution in the gift economy.
    """
    gifts_db[gift.gift_id] = gift

    return {
        "success": True,
        "gift_id": gift.gift_id,
        "gift_type": gift.gift_type,
        "description": gift.description,
        "message": "Gift contribution recorded",
        "one_truth": "Generosity is the original wealth."
    }

@router.post("/currency/debt-jubilee/forgive")
async def forgive_debt(case: DebtJubileeCase):
    """
    Forgive debt through jubilee.
    """
    if case.forgiven_amount > case.original_debt:
        case.forgiven_amount = case.original_debt
    debt_jubilee_db[case.case_id] = case

    return {
        "success": True,
        "case_id": case.case_id,
        "person_name": case.person_name,
        "forgiven_amount": case.forgiven_amount,
        "remaining_debt": case.original_debt - case.forgiven_amount,
        "message": "Debt jubilee recorded",
        "one_truth": "Debt should never be a life sentence."
    }

@router.post("/currency/mutual-credit/transfer")
async def transfer_mutual_credit(transaction: MutualCreditTransaction):
    """
    Record a mutual credit transfer between community members.
    """
    if transaction.amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be positive")
    mutual_credit_db[transaction.transaction_id] = transaction

    return {
        "success": True,
        "transaction_id": transaction.transaction_id,
        "from_account_id": transaction.from_account_id,
        "to_account_id": transaction.to_account_id,
        "amount": transaction.amount,
        "memo": transaction.memo,
        "message": "Mutual credit transfer recorded",
        "one_truth": "Value moves when we trust each other."
    }
