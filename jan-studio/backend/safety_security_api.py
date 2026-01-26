"""SAFETY/SECURITY SYSTEM API
Community safety teams, crisis intervention, restorative justice

Safety is relational, not coercive. Communities protect each other.

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

class ResponseType(str, Enum):
    CRISIS_INTERVENTION = "crisis_intervention"
    PEER_MEDIATION = "peer_mediation"
    MENTAL_HEALTH = "mental_health"
    HOUSING_SUPPORT = "housing_support"
    SUBSTANCE_SUPPORT = "substance_support"
    DOMESTIC_SUPPORT = "domestic_support"

class HarmType(str, Enum):
    CONFLICT = "conflict"
    VIOLENCE = "violence"
    CRISIS = "crisis"
    THEFT = "theft"
    NEGLECT = "neglect"

# ============================================================================
# MODELS
# ============================================================================

class SafetyTeam(BaseModel):
    team_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    community_name: str
    members_count: int
    trained_in: List[str]
    available_24_7: bool = True
    unarmed: bool = True
    created_date: datetime = Field(default_factory=datetime.now)

class CrisisCall(BaseModel):
    call_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    person_id: str
    location: str
    response_type: ResponseType
    severity_level: int = 3  # 1-5
    response_time_minutes: Optional[int] = None
    resolved: bool = False
    call_time: datetime = Field(default_factory=datetime.now)

class RestorativeCircle(BaseModel):
    circle_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    incident_id: str
    participants_count: int
    agreements: List[str]
    completion_date: Optional[datetime] = None
    created_date: datetime = Field(default_factory=datetime.now)

class CommunityAgreement(BaseModel):
    agreement_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    community_name: str
    principles: List[str]
    created_date: datetime = Field(default_factory=datetime.now)

class IncidentReport(BaseModel):
    incident_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    description: str
    harm_type: HarmType
    referred_team_id: Optional[str] = None
    resolved: bool = False
    reported_date: datetime = Field(default_factory=datetime.now)

# ============================================================================
# STORAGE
# ============================================================================

teams_db: Dict[str, SafetyTeam] = {}
crisis_calls_db: Dict[str, CrisisCall] = {}
restorative_circles_db: Dict[str, RestorativeCircle] = {}
agreements_db: Dict[str, CommunityAgreement] = {}
incidents_db: Dict[str, IncidentReport] = {}

# ============================================================================
# ENDPOINTS
# ============================================================================

@router.post("/safety/team/create")
async def create_safety_team(team: SafetyTeam):
    """
    Create a community safety team (non-police, unarmed).
    """
    team.unarmed = True
    teams_db[team.team_id] = team

    return {
        "success": True,
        "team_id": team.team_id,
        "community_name": team.community_name,
        "members_count": team.members_count,
        "message": "Community safety team created",
        "one_truth": "Safety grows from relationship, not fear."
    }

@router.post("/safety/crisis/log")
async def log_crisis(call: CrisisCall):
    """
    Log a crisis call for community response.
    """
    crisis_calls_db[call.call_id] = call

    return {
        "success": True,
        "call_id": call.call_id,
        "response_type": call.response_type,
        "severity_level": call.severity_level,
        "resolved": call.resolved,
        "message": "Crisis call logged",
        "one_truth": "We show up for each other in crisis."
    }

@router.post("/safety/incident/report")
async def report_incident(incident: IncidentReport):
    """
    Report harm or conflict for restorative response.
    """
    incidents_db[incident.incident_id] = incident

    return {
        "success": True,
        "incident_id": incident.incident_id,
        "harm_type": incident.harm_type,
        "resolved": incident.resolved,
        "message": "Incident reported for restorative action",
        "one_truth": "Accountability restores, it does not destroy."
    }

@router.post("/safety/restorative-circle/create")
async def create_restorative_circle(circle: RestorativeCircle):
    """
    Create a restorative circle for healing and accountability.
    """
    restorative_circles_db[circle.circle_id] = circle

    return {
        "success": True,
        "circle_id": circle.circle_id,
        "incident_id": circle.incident_id,
        "participants_count": circle.participants_count,
        "message": "Restorative circle created",
        "one_truth": "Healing requires truth, listening, and repair."
    }

@router.post("/safety/agreement/create")
async def create_community_agreement(agreement: CommunityAgreement):
    """
    Create community safety principles and agreements.
    """
    agreements_db[agreement.agreement_id] = agreement

    return {
        "success": True,
        "agreement_id": agreement.agreement_id,
        "community_name": agreement.community_name,
        "principles_count": len(agreement.principles),
        "message": "Community agreement created",
        "one_truth": "Our agreements are how we care for each other."
    }
