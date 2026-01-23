"""
UNIVERSAL CHILDCARE SYSTEM API
Free childcare for all children 0-5 years, community collectives, worker justice

Every child deserves nurturing care - regardless of parents' economic status.
Childcare is a human right and collective responsibility.

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
"""

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

class AgeGroup(str, Enum):
    INFANT = "infant"              # 0-12 months
    TODDLER = "toddler"            # 1-3 years
    PRESCHOOL = "preschool"        # 3-5 years
    SCHOOL_AGE = "school_age"      # 5-12 years

class CareType(str, Enum):
    FULL_TIME = "full_time"        # Up to 50 hours/week
    PART_TIME = "part_time"        # Flexible hours
    DROP_IN = "drop_in"            # Emergency/hourly
    OVERNIGHT = "overnight"        # Shift workers
    SICK_CHILD = "sick_child"      # Illness care
    SPECIAL_NEEDS = "special_needs"  # Intensive support

class ProgramType(str, Enum):
    NEIGHBORHOOD_HUB = "neighborhood_hub"           # Community center
    FAMILY_SUPPORT_CENTER = "family_support_center" # Drop-in + parent support
    INTERGENERATIONAL = "intergenerational"         # Elder involvement
    COOPERATIVE = "cooperative"                     # Parent-run collective
    HOME_BASED = "home_based"                      # Rural/home network

class WorkerRole(str, Enum):
    LEAD_TEACHER = "lead_teacher"      # $35-45/hour
    TEACHER = "teacher"                # $25-35/hour
    ASSISTANT = "assistant"            # $25-30/hour
    SPECIALIST = "specialist"          # Special needs, infant care
    COORDINATOR = "coordinator"        # Program coordination

# ============================================================================
# MODELS
# ============================================================================

class ChildEnrollment(BaseModel):
    child_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    child_name: str
    age_months: int
    age_group: AgeGroup
    care_type: CareType
    hours_per_week: int
    special_needs: bool = False
    special_needs_description: Optional[str] = None
    enrolled_date: datetime = Field(default_factory=datetime.now)
    cost_to_family: float = 0.0  # Always $0 - FREE
    program_id: str
    meals_included: bool = True
    supplies_included: bool = True

class NeighborhoodHub(BaseModel):
    hub_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    community_name: str
    address: str
    total_capacity: int
    current_enrollment: int = 0
    program_type: ProgramType
    age_groups_served: List[AgeGroup]
    has_outdoor_space: bool = True
    has_intergenerational_program: bool = False
    walking_distance_families: int  # Families within walking distance
    total_staff: int
    staff_child_ratio_infant: str = "1:3"   # Actual ratio
    staff_child_ratio_toddler: str = "1:5"
    staff_child_ratio_preschool: str = "1:8"
    opened_date: datetime = Field(default_factory=datetime.now)
    community_governed: bool = True  # Parent + worker councils

class ChildcareWorker(BaseModel):
    worker_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    role: WorkerRole
    hourly_wage: float  # Minimum $25/hour
    has_benefits: bool = True  # Healthcare, retirement, paid leave
    years_experience: int
    specialized_training: Optional[str] = None  # Infant care, special needs, etc.
    works_at_hub: str  # hub_id
    hired_date: datetime = Field(default_factory=datetime.now)
    previous_wage: Optional[float] = None  # Before universal childcare
    planning_time_hours: int = 10  # Paid planning time per week

class FamilySupport(BaseModel):
    support_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    family_id: str
    support_type: str  # prenatal_ed, postpartum_doula, mental_health, material_support, housing
    description: str
    provided_date: datetime = Field(default_factory=datetime.now)
    cost_to_family: float = 0.0  # FREE
    hub_id: Optional[str] = None

class IntergenerationalProgram(BaseModel):
    program_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    hub_id: str
    elder_volunteers: int = 0
    teen_mentors: int = 0
    grandparent_volunteers: int = 0
    storytelling_sessions_monthly: int = 0
    wisdom_sharing_hours_monthly: int = 0
    cross_age_learning_activities: int = 0
    created_date: datetime = Field(default_factory=datetime.now)

class SystemTransition(BaseModel):
    transition_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    metric: str
    before_value: float
    after_value: float
    improvement_percent: float
    date_recorded: datetime = Field(default_factory=datetime.now)
    description: str

# ============================================================================
# STORAGE
# ============================================================================

enrollments_db: Dict[str, ChildEnrollment] = {}
hubs_db: Dict[str, NeighborhoodHub] = {}
workers_db: Dict[str, ChildcareWorker] = {}
family_support_db: Dict[str, FamilySupport] = {}
intergenerational_db: Dict[str, IntergenerationalProgram] = {}
transitions_db: Dict[str, SystemTransition] = {}

# ============================================================================
# ENDPOINTS
# ============================================================================

@router.post("/childcare/enroll")
async def enroll_child(enrollment: ChildEnrollment):
    """
    Enroll a child in universal free childcare.
    Every child deserves nurturing care - regardless of parents' economic status.
    """
    # Ensure cost is always $0
    enrollment.cost_to_family = 0.0
    enrollment.meals_included = True
    enrollment.supplies_included = True

    enrollments_db[enrollment.child_id] = enrollment

    # Update hub enrollment count
    if enrollment.program_id in hubs_db:
        hubs_db[enrollment.program_id].current_enrollment += 1

    return {
        "success": True,
        "child_id": enrollment.child_id,
        "message": f"{enrollment.child_name} enrolled in free childcare",
        "care_type": enrollment.care_type,
        "hours_per_week": enrollment.hours_per_week,
        "cost_to_family": 0.0,
        "meals_included": True,
        "supplies_included": True,
        "one_truth": "Every child deserves nurturing care. Childcare is a human right."
    }

@router.post("/childcare/hub/create")
async def create_neighborhood_hub(hub: NeighborhoodHub):
    """
    Create a neighborhood childcare hub.
    Walking distance, community-based, democratically governed.
    """
    hubs_db[hub.hub_id] = hub

    return {
        "success": True,
        "hub_id": hub.hub_id,
        "community": hub.community_name,
        "capacity": hub.total_capacity,
        "program_type": hub.program_type,
        "message": f"Neighborhood hub created in {hub.community_name}",
        "one_truth": "Children belong to all of us. We raise them collectively."
    }

@router.post("/childcare/worker/hire")
async def hire_childcare_worker(worker: ChildcareWorker):
    """
    Hire childcare worker with living wage and full benefits.
    Caregivers are skilled professionals, not 'babysitters'.
    """
    # Ensure minimum wage
    if worker.hourly_wage < 25.0:
        worker.hourly_wage = 25.0

    # Ensure benefits
    worker.has_benefits = True

    workers_db[worker.worker_id] = worker

    wage_increase = None
    if worker.previous_wage:
        wage_increase = worker.hourly_wage - worker.previous_wage

    return {
        "success": True,
        "worker_id": worker.worker_id,
        "name": worker.name,
        "role": worker.role,
        "hourly_wage": worker.hourly_wage,
        "has_benefits": True,
        "wage_increase": wage_increase,
        "message": f"{worker.name} hired as {worker.role} at ${worker.hourly_wage}/hour",
        "one_truth": "Childcare workers deserve living wages and respect as professionals."
    }

@router.post("/childcare/support/provide")
async def provide_family_support(support: FamilySupport):
    """
    Provide family support services (prenatal, postpartum, mental health, material support).
    Support parents, don't judge them.
    """
    support.cost_to_family = 0.0  # Always free
    family_support_db[support.support_id] = support

    return {
        "success": True,
        "support_id": support.support_id,
        "family_id": support.family_id,
        "support_type": support.support_type,
        "cost": 0.0,
        "message": f"Family support provided: {support.support_type}",
        "one_truth": "Parents need support, not judgment. We help each other."
    }

@router.post("/childcare/intergenerational/create")
async def create_intergenerational_program(program: IntergenerationalProgram):
    """
    Create intergenerational program connecting elders, teens, and children.
    Wisdom flows from old to young. Community raises children together.
    """
    intergenerational_db[program.program_id] = program

    return {
        "success": True,
        "program_id": program.program_id,
        "hub_id": program.hub_id,
        "elder_volunteers": program.elder_volunteers,
        "teen_mentors": program.teen_mentors,
        "grandparent_volunteers": program.grandparent_volunteers,
        "message": "Intergenerational program created - connecting generations",
        "one_truth": "Elders share wisdom. Youth gain mentorship. Children learn from all ages."
    }

@router.post("/childcare/transition/track")
async def track_system_transition(transition: SystemTransition):
    """
    Track transition from private childcare to universal free system.
    Document the transformation.
    """
    transitions_db[transition.transition_id] = transition

    return {
        "success": True,
        "transition_id": transition.transition_id,
        "metric": transition.metric,
        "before": transition.before_value,
        "after": transition.after_value,
        "improvement": f"{transition.improvement_percent}%",
        "message": f"System transition tracked: {transition.metric}"
    }

@router.get("/childcare/stats")
async def get_childcare_stats():
    """
    Get universal childcare system statistics.
    Track the transformation to collective child-raising.
    """
    total_enrolled = len(enrollments_db)
    total_hubs = len(hubs_db)
    total_workers = len(workers_db)
    total_family_support = len(family_support_db)
    total_intergenerational = len(intergenerational_db)

    # Calculate total capacity
    total_capacity = sum(hub.total_capacity for hub in hubs_db.values())

    # Calculate average worker wage
    avg_wage = sum(w.hourly_wage for w in workers_db.values()) / len(workers_db) if workers_db else 0

    # Calculate children by age group
    age_groups = {
        "infant": len([e for e in enrollments_db.values() if e.age_group == AgeGroup.INFANT]),
        "toddler": len([e for e in enrollments_db.values() if e.age_group == AgeGroup.TODDLER]),
        "preschool": len([e for e in enrollments_db.values() if e.age_group == AgeGroup.PRESCHOOL]),
        "school_age": len([e for e in enrollments_db.values() if e.age_group == AgeGroup.SCHOOL_AGE])
    }

    # Calculate special needs support
    special_needs_children = len([e for e in enrollments_db.values() if e.special_needs])

    return {
        "total_children_enrolled": total_enrolled,
        "total_neighborhood_hubs": total_hubs,
        "total_capacity": total_capacity,
        "total_workers": total_workers,
        "average_worker_wage": round(avg_wage, 2),
        "total_family_support_services": total_family_support,
        "total_intergenerational_programs": total_intergenerational,
        "children_by_age_group": age_groups,
        "special_needs_children": special_needs_children,
        "cost_to_families": 0.0,
        "one_truth": "Every child receives nurturing care. No parent chooses between career and children. Workers earn living wages with dignity."
    }

@router.get("/childcare/worker/wages")
async def get_worker_wage_comparison():
    """
    Compare worker wages before and after universal childcare.
    Document worker justice transformation.
    """
    workers_with_increase = [w for w in workers_db.values() if w.previous_wage is not None]

    if not workers_with_increase:
        return {
            "workers_tracked": 0,
            "message": "No wage comparison data yet"
        }

    total_increase = sum(w.hourly_wage - w.previous_wage for w in workers_with_increase)
    avg_previous = sum(w.previous_wage for w in workers_with_increase) / len(workers_with_increase)
    avg_current = sum(w.hourly_wage for w in workers_with_increase) / len(workers_with_increase)
    avg_increase_percent = ((avg_current - avg_previous) / avg_previous) * 100

    return {
        "workers_tracked": len(workers_with_increase),
        "average_previous_wage": round(avg_previous, 2),
        "average_current_wage": round(avg_current, 2),
        "average_increase": round(avg_current - avg_previous, 2),
        "average_increase_percent": round(avg_increase_percent, 1),
        "total_wage_increase": round(total_increase, 2),
        "all_have_benefits": True,
        "one_truth": "Childcare workers were exploited in poverty wages. Now they earn living wages with dignity and respect."
    }

@router.get("/childcare/wisdom/why-free")
async def why_childcare_should_be_free():
    """
    Explain why childcare should be free.
    The fundamental truths.
    """
    return {
        "one_truth": "Every child deserves nurturing care - regardless of parents' economic status.",
        "core_principle": "Childcare is a human right and collective responsibility.",
        "fundamental_arguments": [
            "Children are society's future. Their care is society's responsibility.",
            "No child chooses their parents' economic status.",
            "Brain development happens 0-5 years (can't be delayed).",
            "Quality early care prevents lifetime problems.",
            "Society benefits from every child reaching potential."
        ],
        "economic_reality": {
            "current_family_spending": "$50+ billion annually",
            "universal_system_cost": "$265 billion annually",
            "economic_return": "$7-13 for every $1 invested",
            "lost_productivity_current": "$57 billion annually",
            "net_positive_timeline": "3-5 years"
        },
        "what_breaks": [
            "Profit-driven childcare corporations",
            "Parent financial strain and stress",
            "Worker poverty and exploitation",
            "Isolated nuclear family pressure",
            "Childcare deserts and access inequality",
            "Market-based approach to human development"
        ],
        "what_replaces": [
            "Community collective care",
            "Neighborhood hubs (walking distance)",
            "Intergenerational programs (elders + children)",
            "Worker cooperatives",
            "Living wages for caregivers ($25+/hour)",
            "Free enrollment for all families"
        ],
        "the_vision": "A world where every child receives nurturing high-quality care, no parent chooses between career and children, childcare workers earn living wages with dignity, communities raise children collectively, and children grow up knowing they belong to everyone."
    }

@router.get("/health")
async def health_check():
    """API health check"""
    return {
        "status": "operational",
        "system": "Universal Childcare System",
        "message": "Every child deserves nurturing care. Childcare is a human right.",
        "endpoints_active": True
    }
