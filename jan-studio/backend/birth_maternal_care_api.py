"""
BIRTH/MATERNAL CARE SYSTEM API
Midwifery, doulas, home birth, reproductive autonomy

Birth is sacred. Every person deserves safety, choice, and compassionate support.
"""

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

class BirthSetting(str, Enum):
    HOME = "home"
    BIRTH_CENTER = "birth_center"
    HOSPITAL = "hospital"

class SupportType(str, Enum):
    PRENATAL = "prenatal"
    BIRTH = "birth"
    POSTPARTUM = "postpartum"
    LACTATION = "lactation"

# ============================================================================
# MODELS
# ============================================================================

class Midwife(BaseModel):
    midwife_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    certification: str
    years_experience: int
    on_call: bool = True
    base_rate: float = 0.0  # Covered by universal system
    created_date: datetime = Field(default_factory=datetime.now)

class Doula(BaseModel):
    doula_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    services: List[SupportType]
    on_call: bool = True
    stipend: float = 0.0  # Covered by universal system
    created_date: datetime = Field(default_factory=datetime.now)

class BirthPlan(BaseModel):
    plan_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    person_id: str
    person_name: str
    due_date: date
    birth_setting: BirthSetting
    midwife_id: Optional[str] = None
    doula_id: Optional[str] = None
    pain_preferences: List[str]
    autonomy_statement: str
    created_date: datetime = Field(default_factory=datetime.now)

class BirthCenter(BaseModel):
    center_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    location: str
    suites_available: int
    free_of_charge: bool = True
    has_midwives_on_site: bool = True
    created_date: datetime = Field(default_factory=datetime.now)

class PostpartumSupport(BaseModel):
    support_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    person_id: str
    visits_count: int
    lactation_support: bool = True
    mental_health_support: bool = True
    cost_to_family: float = 0.0
    created_date: datetime = Field(default_factory=datetime.now)

# ============================================================================
# STORAGE
# ============================================================================

midwives_db: Dict[str, Midwife] = {}
doulas_db: Dict[str, Doula] = {}
birth_plans_db: Dict[str, BirthPlan] = {}
birth_centers_db: Dict[str, BirthCenter] = {}
postpartum_db: Dict[str, PostpartumSupport] = {}

# ============================================================================
# ENDPOINTS
# ============================================================================

@router.post("/birth/midwife/register")
async def register_midwife(midwife: Midwife):
    """
    Register a midwife into the universal maternal care system.
    """
    midwife.base_rate = 0.0
    midwives_db[midwife.midwife_id] = midwife

    return {
        "success": True,
        "midwife_id": midwife.midwife_id,
        "name": midwife.name,
        "certification": midwife.certification,
        "message": f"Midwife registered: {midwife.name}",
        "one_truth": "Birth is sacred and deserves skilled, loving care."
    }

@router.post("/birth/doula/register")
async def register_doula(doula: Doula):
    """
    Register a doula for prenatal, birth, and postpartum support.
    """
    doula.stipend = 0.0
    doulas_db[doula.doula_id] = doula

    return {
        "success": True,
        "doula_id": doula.doula_id,
        "name": doula.name,
        "services": doula.services,
        "message": f"Doula registered: {doula.name}",
        "one_truth": "No one should birth alone."
    }

@router.post("/birth/plan/create")
async def create_birth_plan(plan: BirthPlan):
    """
    Create a personalized birth plan honoring autonomy and choice.
    """
    birth_plans_db[plan.plan_id] = plan

    return {
        "success": True,
        "plan_id": plan.plan_id,
        "person_name": plan.person_name,
        "birth_setting": plan.birth_setting,
        "message": "Birth plan created",
        "one_truth": "Reproductive autonomy is a human right."
    }

@router.post("/birth/center/register")
async def register_birth_center(center: BirthCenter):
    """
    Register a community birth center.
    """
    center.free_of_charge = True
    birth_centers_db[center.center_id] = center

    return {
        "success": True,
        "center_id": center.center_id,
        "name": center.name,
        "location": center.location,
        "suites_available": center.suites_available,
        "message": "Birth center registered",
        "one_truth": "Every community deserves a safe place to bring life."
    }

@router.post("/birth/postpartum/support")
async def create_postpartum_support(support: PostpartumSupport):
    """
    Create postpartum care and recovery supports.
    """
    support.cost_to_family = 0.0
    postpartum_db[support.support_id] = support

    return {
        "success": True,
        "support_id": support.support_id,
        "visits_count": support.visits_count,
        "lactation_support": support.lactation_support,
        "mental_health_support": support.mental_health_support,
        "message": "Postpartum support created",
        "one_truth": "Care after birth is as sacred as birth itself."
    }
