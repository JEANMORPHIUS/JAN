"""LEISURE/REST SYSTEM API
Right to rest, free recreation, rest as sacred

Rest is not a reward. It is a human right and a foundation for health.

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
from datetime import datetime, date
from enum import Enum
import uuid

router = APIRouter()

# ============================================================================
# ENUMS
# ============================================================================

class RestType(str, Enum):
    SABBATH = "sabbath"
    RECOVERY = "recovery"
    VACATION = "vacation"
    COMMUNITY_FESTIVAL = "community_festival"

# ============================================================================
# MODELS
# ============================================================================

class RestPolicy(BaseModel):
    policy_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    organization_name: str
    standard_week_hours: int = 32
    minimum_paid_rest_days: int = 30
    sabbath_day: str = "Sunday"
    enforcement_required: bool = True
    created_date: datetime = Field(default_factory=datetime.now)

class RecreationCenter(BaseModel):
    center_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    community_name: str
    facilities: List[str]
    free_access: bool = True
    youth_programs: bool = True
    created_date: datetime = Field(default_factory=datetime.now)

class TimeOffGrant(BaseModel):
    grant_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    person_id: str
    rest_type: RestType
    days_granted: int
    stipend_amount: float = 0.0
    approved: bool = True
    created_date: datetime = Field(default_factory=datetime.now)

class CommunityEvent(BaseModel):
    event_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    rest_type: RestType
    event_date: date
    location: str
    free_entry: bool = True
    attendees_estimate: int = 0

class BurnoutRecoveryPlan(BaseModel):
    plan_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    person_id: str
    recommended_days_off: int
    support_services: List[str]
    created_date: datetime = Field(default_factory=datetime.now)

# ============================================================================
# STORAGE
# ============================================================================

policies_db: Dict[str, RestPolicy] = {}
centers_db: Dict[str, RecreationCenter] = {}
grants_db: Dict[str, TimeOffGrant] = {}
events_db: Dict[str, CommunityEvent] = {}
recovery_db: Dict[str, BurnoutRecoveryPlan] = {}

# ============================================================================
# ENDPOINTS
# ============================================================================

@router.post("/rest/policy/create")
async def create_rest_policy(policy: RestPolicy):
    """
    Create a rest-centered policy for organizations.
    """
    policy.standard_week_hours = min(policy.standard_week_hours, 32)
    policy.minimum_paid_rest_days = max(policy.minimum_paid_rest_days, 30)
    policies_db[policy.policy_id] = policy

    return {
        "success": True,
        "policy_id": policy.policy_id,
        "organization_name": policy.organization_name,
        "standard_week_hours": policy.standard_week_hours,
        "minimum_paid_rest_days": policy.minimum_paid_rest_days,
        "message": "Rest policy created",
        "one_truth": "Rest is sacred and non-negotiable."
    }

@router.post("/rest/center/register")
async def register_recreation_center(center: RecreationCenter):
    """
    Register a free community recreation center.
    """
    center.free_access = True
    centers_db[center.center_id] = center

    return {
        "success": True,
        "center_id": center.center_id,
        "community_name": center.community_name,
        "facilities": center.facilities,
        "message": "Recreation center registered",
        "one_truth": "Joy and play are part of a healthy life."
    }

@router.post("/rest/time-off/grant")
async def grant_time_off(grant: TimeOffGrant):
    """
    Grant paid time off for rest or recovery.
    """
    grant.approved = True
    grants_db[grant.grant_id] = grant

    return {
        "success": True,
        "grant_id": grant.grant_id,
        "person_id": grant.person_id,
        "days_granted": grant.days_granted,
        "rest_type": grant.rest_type,
        "message": "Time off granted",
        "one_truth": "Rest restores the body and the spirit."
    }

@router.post("/rest/event/create")
async def create_community_event(event: CommunityEvent):
    """
    Create a community leisure or celebration event.
    """
    event.free_entry = True
    events_db[event.event_id] = event

    return {
        "success": True,
        "event_id": event.event_id,
        "name": event.name,
        "rest_type": event.rest_type,
        "location": event.location,
        "message": "Community event created",
        "one_truth": "Community joy is community health."
    }

@router.post("/rest/recovery/plan")
async def create_recovery_plan(plan: BurnoutRecoveryPlan):
    """
    Create a burnout recovery plan.
    """
    recovery_db[plan.plan_id] = plan

    return {
        "success": True,
        "plan_id": plan.plan_id,
        "person_id": plan.person_id,
        "recommended_days_off": plan.recommended_days_off,
        "message": "Burnout recovery plan created",
        "one_truth": "Rest is how we return to ourselves."
    }
