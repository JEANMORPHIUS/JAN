"""DEATH/END-OF-LIFE SYSTEM API
Natural burial, death doulas, right to die, dignity

Death is part of life. Everyone deserves care, choice, and dignity at the end.

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

# Spiritual Codebase Hacker Integration
from spiritual_codebase_hacker_integration import HACKER_AVAILABLE, hack_loop, perform_genetic_edit, activate_stealth_mode


router = APIRouter()

# ============================================================================
# ENUMS
# ============================================================================

class CareOption(str, Enum):
    HOSPICE = "hospice"
    HOME = "home"
    COMMUNITY_CENTER = "community_center"

class RequestStatus(str, Enum):
    SUBMITTED = "submitted"
    REVIEWING = "reviewing"
    APPROVED = "approved"
    DENIED = "denied"

# ============================================================================
# MODELS
# ============================================================================

class EndOfLifePlan(BaseModel):
    plan_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    person_id: str
    person_name: str
    care_option: CareOption
    advance_directives: List[str]
    pain_management_preferences: List[str]
    do_not_resuscitate: bool = False
    chosen_doula_id: Optional[str] = None
    created_date: datetime = Field(default_factory=datetime.now)

class DeathDoula(BaseModel):
    doula_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    training: str
    available: bool = True
    sliding_scale: bool = True
    cost_to_family: float = 0.0
    created_date: datetime = Field(default_factory=datetime.now)

class NaturalBurialSite(BaseModel):
    site_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    location: str
    capacity: int
    native_plants_restoration: bool = True
    cost_to_family: float = 0.0
    created_date: datetime = Field(default_factory=datetime.now)

class LegacyArchive(BaseModel):
    archive_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    person_id: str
    message: str
    media_links: List[str]
    shared_with_family: bool = True
    created_date: datetime = Field(default_factory=datetime.now)

class AssistedDyingRequest(BaseModel):
    request_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    person_id: str
    person_name: str
    eligibility_confirmed: bool = False
    waiting_period_days: int = 0
    status: RequestStatus = RequestStatus.SUBMITTED
    submitted_date: datetime = Field(default_factory=datetime.now)

# ============================================================================
# STORAGE
# ============================================================================

plans_db: Dict[str, EndOfLifePlan] = {}
doulas_db: Dict[str, DeathDoula] = {}
burial_sites_db: Dict[str, NaturalBurialSite] = {}
archives_db: Dict[str, LegacyArchive] = {}
assisted_requests_db: Dict[str, AssistedDyingRequest] = {}

# ============================================================================
# ENDPOINTS
# ============================================================================


    class Config:
        schema_extra = {
            "example": {'request_id': 1, 'person_id': 1, 'person_name': 'jan', 'eligibility_confirmed': True, 'waiting_period_days': 1, 'status': 'string', 'submitted_date': 'string', 'plans_db': {}, 'doulas_db': {}, 'burial_sites_db': {}, 'archives_db': {}, 'assisted_requests_db': {}}
        }
@router.post("/death/plan/create")
async def create_end_of_life_plan(plan: EndOfLifePlan):
    """
    Create an end-of-life care plan.
    """
    plans_db[plan.plan_id] = plan

    return {
        "success": True,
        "plan_id": plan.plan_id,
        "person_name": plan.person_name,
        "care_option": plan.care_option,
        "do_not_resuscitate": plan.do_not_resuscitate,
        "message": "End-of-life plan created",
        "one_truth": "Dignity at the end is a human right."
    }

@router.post("/death/doula/register")
async def register_death_doula(doula: DeathDoula):
    """
    Register a death doula for end-of-life support.
    """
    doula.cost_to_family = 0.0
    doulas_db[doula.doula_id] = doula

    return {
        "success": True,
        "doula_id": doula.doula_id,
        "name": doula.name,
        "training": doula.training,
        "message": f"Death doula registered: {doula.name}",
        "one_truth": "No one should die alone or in fear."
    }

@router.post("/death/burial-site/register")
async def register_burial_site(site: NaturalBurialSite):
    """
    Register a natural burial site.
    """
    site.cost_to_family = 0.0
    burial_sites_db[site.site_id] = site

    return {
        "success": True,
        "site_id": site.site_id,
        "name": site.name,
        "location": site.location,
        "capacity": site.capacity,
        "message": "Natural burial site registered",
        "one_truth": "We return to the earth in peace."
    }

@router.post("/death/legacy/archive")
async def create_legacy_archive(archive: LegacyArchive):
    """
    Preserve a legacy message and memories.
    """
    archives_db[archive.archive_id] = archive

    return {
        "success": True,
        "archive_id": archive.archive_id,
        "person_id": archive.person_id,
        "shared_with_family": archive.shared_with_family,
        "message": "Legacy archive created",
        "one_truth": "Love outlives the body."
    }

@router.post("/death/assisted-request/submit")
async def submit_assisted_request(request: AssistedDyingRequest):
    """
    Submit a request for assisted dying (subject to safeguards).
    """
    request.status = RequestStatus.SUBMITTED
    assisted_requests_db[request.request_id] = request

    return {
        "success": True,
        "request_id": request.request_id,
        "person_name": request.person_name,
        "status": request.status,
        "message": "Assisted dying request submitted for review",
        "one_truth": "Compassion honors choice with care and safeguards."
    }
