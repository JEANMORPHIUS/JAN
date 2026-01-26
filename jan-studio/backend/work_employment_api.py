"""WORK/EMPLOYMENT SYSTEM API
4-day week, worker cooperatives, universal basic income, job guarantee

Work is for human dignity, not exploitation. Everyone deserves meaningful work,
fair pay, and time to live.

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

class EmploymentType(str, Enum):
    COOPERATIVE = "cooperative"
    PUBLIC_SERVICE = "public_service"
    COMMUNITY_ENTERPRISE = "community_enterprise"
    CARE_WORK = "care_work"
    EDUCATION = "education"
    RESTORATION = "restoration"

class ScheduleType(str, Enum):
    FOUR_DAY_WEEK = "four_day_week"
    FLEXIBLE = "flexible"
    SEASONAL = "seasonal"
    PART_TIME = "part_time"

# ============================================================================
# MODELS
# ============================================================================

class WorkerProfile(BaseModel):
    worker_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    primary_skills: List[str]
    desired_employment: EmploymentType
    desired_hours_per_week: int = 32  # 4-day week baseline
    preferred_schedule: ScheduleType = ScheduleType.FOUR_DAY_WEEK
    current_wage: Optional[float] = None
    living_wage_floor: float = 25.0
    union_member: bool = True
    enrolled_date: datetime = Field(default_factory=datetime.now)

class WorkerCooperative(BaseModel):
    coop_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    sector: str
    community_name: str
    member_count: int = 0
    governance_model: str = "one_member_one_vote"
    profit_share_percent: float = 100.0
    four_day_week: bool = True
    created_date: datetime = Field(default_factory=datetime.now)

class JobGuaranteePlacement(BaseModel):
    placement_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    worker_id: str
    project_name: str
    role_title: str
    employment_type: EmploymentType
    hourly_wage: float = 25.0
    hours_per_week: int = 32
    start_date: datetime = Field(default_factory=datetime.now)
    benefits_included: bool = True

class UniversalBasicIncome(BaseModel):
    ubi_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    person_id: str
    person_name: str
    monthly_base: float = 2000.0
    supplemental_income: float = 0.0
    total_monthly: float = 2000.0
    no_work_requirement: bool = True
    no_means_test: bool = True
    enrolled_date: datetime = Field(default_factory=datetime.now)

class WorkSchedulePolicy(BaseModel):
    policy_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    organization_name: str
    standard_week_hours: int = 32
    minimum_paid_time_off_days: int = 30
    max_overtime_hours: int = 0
    flexible_schedule: bool = True
    remote_option: bool = True
    created_date: datetime = Field(default_factory=datetime.now)

class WageTransition(BaseModel):
    transition_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    worker_id: str
    previous_wage: float
    new_wage: float
    improvement_percent: float
    transition_date: datetime = Field(default_factory=datetime.now)

class CommunityProject(BaseModel):
    project_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    community_name: str
    purpose: str
    positions_open: int
    living_wage_floor: float = 25.0
    created_date: datetime = Field(default_factory=datetime.now)

# ============================================================================
# STORAGE
# ============================================================================

workers_db: Dict[str, WorkerProfile] = {}
cooperatives_db: Dict[str, WorkerCooperative] = {}
placements_db: Dict[str, JobGuaranteePlacement] = {}
ubi_db: Dict[str, UniversalBasicIncome] = {}
policies_db: Dict[str, WorkSchedulePolicy] = {}
wage_transitions_db: Dict[str, WageTransition] = {}
projects_db: Dict[str, CommunityProject] = {}

# ============================================================================
# ENDPOINTS
# ============================================================================

@router.post("/work/worker/register")
async def register_worker(worker: WorkerProfile):
    """
    Register worker profile for job guarantee or cooperative placement.
    """
    worker.living_wage_floor = max(worker.living_wage_floor, 25.0)
    workers_db[worker.worker_id] = worker

    return {
        "success": True,
        "worker_id": worker.worker_id,
        "name": worker.name,
        "desired_employment": worker.desired_employment,
        "hours_per_week": worker.desired_hours_per_week,
        "living_wage_floor": worker.living_wage_floor,
        "message": f"{worker.name} registered for dignified work",
        "one_truth": "Work should serve life. Dignity is the baseline."
    }

@router.post("/work/cooperative/create")
async def create_cooperative(coop: WorkerCooperative):
    """
    Create a worker cooperative with democratic governance.
    """
    coop.profit_share_percent = 100.0
    coop.four_day_week = True
    cooperatives_db[coop.coop_id] = coop

    return {
        "success": True,
        "coop_id": coop.coop_id,
        "name": coop.name,
        "member_count": coop.member_count,
        "governance_model": coop.governance_model,
        "message": f"Worker cooperative created: {coop.name}",
        "one_truth": "Those who do the work should own the work."
    }

@router.post("/work/job-guarantee/place")
async def place_job_guarantee(placement: JobGuaranteePlacement):
    """
    Place a worker into a guaranteed job with living wage and benefits.
    """
    if placement.hourly_wage < 25.0:
        placement.hourly_wage = 25.0
    placement.benefits_included = True
    placements_db[placement.placement_id] = placement

    return {
        "success": True,
        "placement_id": placement.placement_id,
        "worker_id": placement.worker_id,
        "project_name": placement.project_name,
        "role_title": placement.role_title,
        "hourly_wage": placement.hourly_wage,
        "hours_per_week": placement.hours_per_week,
        "benefits_included": True,
        "message": "Job guarantee placement confirmed",
        "one_truth": "No one should be forced into poverty for lack of work."
    }

@router.post("/work/ubi/enroll")
async def enroll_ubi(ubi: UniversalBasicIncome):
    """
    Enroll a person in universal basic income.
    """
    ubi.no_work_requirement = True
    ubi.no_means_test = True
    ubi.total_monthly = ubi.monthly_base + ubi.supplemental_income
    ubi_db[ubi.ubi_id] = ubi

    return {
        "success": True,
        "ubi_id": ubi.ubi_id,
        "person_name": ubi.person_name,
        "total_monthly": ubi.total_monthly,
        "annual_income": ubi.total_monthly * 12,
        "message": f"UBI enrollment confirmed for {ubi.person_name}",
        "one_truth": "Life is not earned. It is given. So is dignity."
    }

@router.post("/work/policy/create")
async def create_work_policy(policy: WorkSchedulePolicy):
    """
    Create a 4-day week and rest-centered work policy.
    """
    policy.standard_week_hours = min(policy.standard_week_hours, 32)
    policy.minimum_paid_time_off_days = max(policy.minimum_paid_time_off_days, 30)
    policy.max_overtime_hours = 0
    policies_db[policy.policy_id] = policy

    return {
        "success": True,
        "policy_id": policy.policy_id,
        "organization_name": policy.organization_name,
        "standard_week_hours": policy.standard_week_hours,
        "minimum_paid_time_off_days": policy.minimum_paid_time_off_days,
        "message": f"Rest-centered work policy created for {policy.organization_name}",
        "one_truth": "Rest is sacred. Work must honor life."
    }

@router.post("/work/project/create")
async def create_community_project(project: CommunityProject):
    """
    Create a community project that offers living-wage positions.
    """
    project.living_wage_floor = max(project.living_wage_floor, 25.0)
    projects_db[project.project_id] = project

    return {
        "success": True,
        "project_id": project.project_id,
        "name": project.name,
        "community_name": project.community_name,
        "positions_open": project.positions_open,
        "living_wage_floor": project.living_wage_floor,
        "message": f"Community project created: {project.name}",
        "one_truth": "Community care is real work."
    }

@router.post("/work/wage-transition/record")
async def record_wage_transition(transition: WageTransition):
    """
    Record wage improvements during system transition.
    """
    if transition.previous_wage <= 0:
        raise HTTPException(status_code=400, detail="Previous wage must be positive")
    transition.improvement_percent = (
        (transition.new_wage - transition.previous_wage) / transition.previous_wage
    ) * 100
    wage_transitions_db[transition.transition_id] = transition

    return {
        "success": True,
        "transition_id": transition.transition_id,
        "worker_id": transition.worker_id,
        "previous_wage": transition.previous_wage,
        "new_wage": transition.new_wage,
        "improvement_percent": transition.improvement_percent,
        "message": "Wage transition recorded",
        "one_truth": "A rising wage is a rising life."
    }
