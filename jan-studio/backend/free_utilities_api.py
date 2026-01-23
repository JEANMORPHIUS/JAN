"""
FREE UTILITIES AS HUMAN RIGHT API
Gas, Electricity, Water, Internet - All Should Be Free

This API provides endpoints for:
1. Universal Basic Energy (UBE) tracking
2. Community Energy Commons management
3. Utility debt forgiveness
4. Free utilities pilot programs
5. System transition tracking (private → public → free)
6. Impact measurement and success stories

Integration with Economic Healing and One Truth Matrix
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Dict
from datetime import datetime
from enum import Enum

router = APIRouter()

# ============================================================================
# MODELS
# ============================================================================

class UtilityType(str, Enum):
    """Types of utilities"""
    ELECTRICITY = "electricity"
    GAS_HEATING = "gas_heating"
    WATER = "water"
    INTERNET = "internet"
    ALL = "all"

class OwnershipModel(str, Enum):
    """Utility ownership models"""
    PRIVATE_MONOPOLY = "private_monopoly"           # Current broken system
    PUBLIC_UTILITY = "public_utility"               # Government-owned
    COMMUNITY_COMMONS = "community_commons"         # Community-owned
    COOPERATIVE = "cooperative"                     # User-owned cooperative
    FREE_UNIVERSAL = "free_universal"               # Free for all (goal)

class UsageTier(str, Enum):
    """Usage tiers for free utilities"""
    BASIC = "basic"                 # 0-100 kWh/month - FREE
    COMFORTABLE = "comfortable"     # 100-200 kWh/month - FREE
    LUXURY = "luxury"              # 200+ kWh/month - Small fee

# ============================================================================
# REQUEST/RESPONSE MODELS
# ============================================================================

class UtilityDebtForgiveness(BaseModel):
    """Forgive utility debt for individuals/communities"""
    forgiveness_id: Optional[str] = None
    person_id: Optional[str] = None
    community_id: Optional[str] = None

    # Debt details
    utility_type: UtilityType
    total_debt: float                   # Total debt amount
    debt_age_months: int                # How long in debt

    # Forgiveness
    amount_forgiven: float
    forgiveness_date: Optional[str] = None
    reason: str = "Basic needs are human rights. Survival should not create debt."

    # Restoration
    service_restored: bool = False
    restoration_date: Optional[str] = None

    created_at: Optional[str] = None

class UniversalBasicEnergy(BaseModel):
    """Track UBE (Universal Basic Energy) allocation"""
    ube_id: Optional[str] = None
    person_id: str

    # Allocation
    monthly_kwh_free: float = 200.0     # Free monthly allocation
    usage_tier: UsageTier = UsageTier.COMFORTABLE

    # Usage tracking
    current_month_usage: float = 0.0
    is_within_free_tier: bool = True
    overage_amount: float = 0.0         # If exceeded free tier

    # Cost savings
    traditional_cost: float = 0.0       # What they would pay in old system
    saved_this_month: float = 0.0       # Savings from free utilities

    # Cumulative impact
    total_saved_lifetime: float = 0.0   # Total saved since joining

    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CommunityEnergyCommons(BaseModel):
    """Community-owned energy system"""
    commons_id: Optional[str] = None
    community_name: str

    # Infrastructure
    has_solar: bool = False
    solar_capacity_kw: float = 0.0
    has_wind: bool = False
    wind_capacity_kw: float = 0.0
    has_geothermal: bool = False
    has_battery_storage: bool = False
    storage_capacity_kwh: float = 0.0

    # Ownership
    ownership_model: OwnershipModel
    total_members: int = 0
    democratic_governance: bool = True

    # Production and usage
    monthly_generation_kwh: float = 0.0
    monthly_consumption_kwh: float = 0.0
    surplus_kwh: float = 0.0            # Surplus shared or sold

    # Financial
    setup_cost: float = 0.0
    monthly_maintenance: float = 0.0
    cost_per_member: float = 0.0        # $0 if fully free

    # Impact
    households_served: int = 0
    people_served: int = 0
    co2_avoided_tons: float = 0.0
    money_saved_community: float = 0.0

    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class FreeUtilitiesPilot(BaseModel):
    """Track pilot programs for free utilities"""
    pilot_id: Optional[str] = None
    location: str
    start_date: str

    # What's included
    free_electricity: bool = False
    free_heating: bool = False
    free_water: bool = False
    free_internet: bool = False

    # Participants
    households: int = 0
    people_served: int = 0

    # Infrastructure
    renewable_percentage: float = 0.0   # % from renewables
    local_generation: bool = False
    community_owned: bool = False

    # Metrics
    cost_per_household_month: float = 0.0
    traditional_cost_avoided: float = 0.0
    total_savings: float = 0.0

    # Impact measurements
    health_improvements: List[str] = []
    educational_improvements: List[str] = []
    economic_improvements: List[str] = []
    environmental_improvements: List[str] = []

    # Satisfaction
    participant_satisfaction: float = 0.0  # 0-100
    would_recommend: float = 0.0           # 0-100

    # Challenges and solutions
    challenges: List[str] = []
    solutions: List[str] = []

    # Status
    is_active: bool = True
    is_successful: bool = False
    completion_date: Optional[str] = None

    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class SystemTransitionTracking(BaseModel):
    """Track transition from private → public → free"""
    region: str
    utility_type: UtilityType

    # Current state
    current_model: OwnershipModel
    target_model: OwnershipModel = OwnershipModel.FREE_UNIVERSAL

    # Transition progress
    transition_percentage: float = 0.0  # 0-100

    # Steps completed
    public_awareness_raised: bool = False
    political_support_secured: bool = False
    pilot_program_successful: bool = False
    funding_secured: bool = False
    infrastructure_built: bool = False
    service_launched: bool = False

    # Impact
    people_with_free_utilities: int = 0
    money_saved_community: float = 0.0
    debt_forgiven: float = 0.0
    disconnections_prevented: int = 0

    # Resistance
    corporate_resistance: List[str] = []
    political_resistance: List[str] = []
    solutions_to_resistance: List[str] = []

    updated_at: Optional[str] = None

# ============================================================================
# IN-MEMORY STORAGE (Replace with database in production)
# ============================================================================

debt_forgiveness: Dict[str, UtilityDebtForgiveness] = {}
ube_accounts: Dict[str, UniversalBasicEnergy] = {}
energy_commons: Dict[str, CommunityEnergyCommons] = {}
pilot_programs: Dict[str, FreeUtilitiesPilot] = {}
transition_tracking: Dict[str, SystemTransitionTracking] = {}

# ============================================================================
# UTILITY DEBT FORGIVENESS ENDPOINTS
# ============================================================================

@router.post("/utilities/debt/forgive")
async def forgive_utility_debt(forgiveness: UtilityDebtForgiveness):
    """
    Forgive utility debt. Basic needs are human rights.
    Survival should not create debt.
    """
    forgiveness_id = f"forgive_{len(debt_forgiveness) + 1}"
    forgiveness.forgiveness_id = forgiveness_id
    forgiveness.forgiveness_date = datetime.now().isoformat()
    forgiveness.service_restored = True
    forgiveness.restoration_date = datetime.now().isoformat()
    forgiveness.created_at = datetime.now().isoformat()

    debt_forgiveness[forgiveness_id] = forgiveness

    return {
        "forgiveness_id": forgiveness_id,
        "utility_type": forgiveness.utility_type,
        "amount_forgiven": forgiveness.amount_forgiven,
        "service_restored": True,
        "message": f"${forgiveness.amount_forgiven:,.2f} utility debt forgiven. Service restored.",
        "truth": "Basic needs are human rights. No one should be in debt for survival.",
        "wisdom": "Debt forgiven. Dignity restored. This is justice.",
        "next_steps": [
            "Service restored immediately",
            "No future shut-offs",
            "Transition to free utilities",
            "Community support available"
        ]
    }

@router.get("/utilities/debt/forgiveness/total")
async def get_total_debt_forgiveness():
    """Get total utility debt forgiven"""
    if not debt_forgiveness:
        return {
            "message": "No debt forgiveness yet",
            "truth": "Start forgiving debt today. Restore dignity."
        }

    total_forgiven = sum(f.amount_forgiven for f in debt_forgiveness.values())
    people_helped = len(set(f.person_id for f in debt_forgiveness.values() if f.person_id))
    communities_helped = len(set(f.community_id for f in debt_forgiveness.values() if f.community_id))

    by_utility = {}
    for f in debt_forgiveness.values():
        utility = f.utility_type
        if utility not in by_utility:
            by_utility[utility] = {"count": 0, "total": 0.0}
        by_utility[utility]["count"] += 1
        by_utility[utility]["total"] += f.amount_forgiven

    return {
        "total_debt_forgiven": total_forgiven,
        "people_helped": people_helped,
        "communities_helped": communities_helped,
        "forgiveness_events": len(debt_forgiveness),
        "by_utility_type": by_utility,
        "message": f"${total_forgiven:,.2f} in utility debt forgiven",
        "truth": "Debt forgiveness restores dignity. Basic needs are rights.",
        "wisdom": f"{people_helped} people freed from utility debt. This is justice."
    }

# ============================================================================
# UNIVERSAL BASIC ENERGY (UBE) ENDPOINTS
# ============================================================================

@router.post("/utilities/ube/create")
async def create_ube_account(ube: UniversalBasicEnergy):
    """Create Universal Basic Energy account for person"""
    ube_id = f"ube_{len(ube_accounts) + 1}"
    ube.ube_id = ube_id
    ube.created_at = datetime.now().isoformat()
    ube.updated_at = datetime.now().isoformat()

    ube_accounts[ube_id] = ube

    return {
        "ube_id": ube_id,
        "person_id": ube.person_id,
        "monthly_kwh_free": ube.monthly_kwh_free,
        "usage_tier": ube.usage_tier,
        "message": "Universal Basic Energy account created",
        "truth": "Energy is a human right. You now have free electricity.",
        "what_this_means": [
            f"{ube.monthly_kwh_free} kWh free every month",
            "No shut-offs ever",
            "No debt accumulation",
            "Basic needs met",
            "Dignity honored"
        ]
    }

@router.post("/utilities/ube/{ube_id}/log-usage")
async def log_ube_usage(
    ube_id: str,
    kwh_used: float,
    traditional_cost: Optional[float] = None
):
    """Log monthly energy usage and calculate savings"""
    if ube_id not in ube_accounts:
        raise HTTPException(status_code=404, detail="UBE account not found")

    ube = ube_accounts[ube_id]
    ube.current_month_usage = kwh_used

    # Determine tier
    if kwh_used <= 100:
        ube.usage_tier = UsageTier.BASIC
        ube.is_within_free_tier = True
        ube.overage_amount = 0.0
    elif kwh_used <= 200:
        ube.usage_tier = UsageTier.COMFORTABLE
        ube.is_within_free_tier = True
        ube.overage_amount = 0.0
    else:
        ube.usage_tier = UsageTier.LUXURY
        ube.is_within_free_tier = False
        ube.overage_amount = kwh_used - 200
        # Small fee for overage: $0.05/kWh (vs $0.15-0.30 traditional)
        # Still 60-80% savings on overage

    # Calculate savings
    if traditional_cost:
        ube.traditional_cost = traditional_cost
        if ube.is_within_free_tier:
            ube.saved_this_month = traditional_cost
        else:
            # Save on first 200 kWh, small fee on overage
            overage_fee = ube.overage_amount * 0.05
            ube.saved_this_month = traditional_cost - overage_fee

        ube.total_saved_lifetime += ube.saved_this_month

    ube.updated_at = datetime.now().isoformat()

    return {
        "ube_id": ube_id,
        "month_usage_kwh": kwh_used,
        "usage_tier": ube.usage_tier,
        "is_free": ube.is_within_free_tier,
        "overage_kwh": ube.overage_amount if not ube.is_within_free_tier else 0.0,
        "saved_this_month": ube.saved_this_month,
        "total_saved_lifetime": ube.total_saved_lifetime,
        "message": "Within free tier. $0 owed." if ube.is_within_free_tier else f"Overage: {ube.overage_amount} kWh. Small fee applies.",
        "truth": "Basic energy is free. Your needs are met.",
        "wisdom": f"You've saved ${ube.total_saved_lifetime:,.2f} since joining UBE."
    }

@router.get("/utilities/ube/stats")
async def get_ube_statistics():
    """Get Universal Basic Energy program statistics"""
    if not ube_accounts:
        return {
            "message": "No UBE accounts yet",
            "truth": "Start Universal Basic Energy today. Free electricity for all."
        }

    total_accounts = len(ube_accounts)
    total_saved = sum(ube.total_saved_lifetime for ube in ube_accounts.values())
    within_free_tier = sum(1 for ube in ube_accounts.values() if ube.is_within_free_tier)

    avg_usage = sum(ube.current_month_usage for ube in ube_accounts.values()) / total_accounts

    return {
        "total_accounts": total_accounts,
        "within_free_tier": within_free_tier,
        "percentage_free": (within_free_tier / total_accounts * 100) if total_accounts > 0 else 0,
        "total_saved_all_users": total_saved,
        "average_monthly_usage_kwh": avg_usage,
        "message": f"{within_free_tier}/{total_accounts} users paying $0 for electricity",
        "truth": "Free basic energy works. People's needs are met.",
        "impact": f"${total_saved:,.2f} saved by the community. This is abundance."
    }

# ============================================================================
# COMMUNITY ENERGY COMMONS ENDPOINTS
# ============================================================================

@router.post("/utilities/commons/create")
async def create_energy_commons(commons: CommunityEnergyCommons):
    """Create community energy commons"""
    commons_id = f"commons_{len(energy_commons) + 1}"
    commons.commons_id = commons_id
    commons.created_at = datetime.now().isoformat()
    commons.updated_at = datetime.now().isoformat()

    energy_commons[commons_id] = commons

    # Calculate renewable capacity
    total_capacity = commons.solar_capacity_kw + commons.wind_capacity_kw
    renewable_sources = []
    if commons.has_solar: renewable_sources.append("solar")
    if commons.has_wind: renewable_sources.append("wind")
    if commons.has_geothermal: renewable_sources.append("geothermal")

    return {
        "commons_id": commons_id,
        "community_name": commons.community_name,
        "ownership_model": commons.ownership_model,
        "total_members": commons.total_members,
        "total_capacity_kw": total_capacity,
        "renewable_sources": renewable_sources,
        "has_storage": commons.has_battery_storage,
        "message": f"Community Energy Commons created for {commons.community_name}",
        "truth": "Community ownership. Democratic control. Energy sovereignty.",
        "next_steps": [
            "Install renewable generation",
            "Connect all members",
            "Share surplus energy",
            "Eliminate energy poverty"
        ]
    }

@router.post("/utilities/commons/{commons_id}/production")
async def log_commons_production(
    commons_id: str,
    generation_kwh: float,
    consumption_kwh: float
):
    """Log monthly production and consumption for energy commons"""
    if commons_id not in energy_commons:
        raise HTTPException(status_code=404, detail="Energy commons not found")

    commons = energy_commons[commons_id]
    commons.monthly_generation_kwh = generation_kwh
    commons.monthly_consumption_kwh = consumption_kwh
    commons.surplus_kwh = max(0, generation_kwh - consumption_kwh)

    # Calculate impact
    if commons.total_members > 0:
        commons.cost_per_member = commons.monthly_maintenance / commons.total_members

    # CO2 avoided (rough estimate: 1 kWh renewable = 0.5 kg CO2 avoided)
    commons.co2_avoided_tons += (generation_kwh * 0.5) / 1000

    # Money saved (assume $0.15/kWh traditional cost)
    monthly_savings = consumption_kwh * 0.15
    commons.money_saved_community += monthly_savings

    commons.updated_at = datetime.now().isoformat()

    is_self_sufficient = generation_kwh >= consumption_kwh

    return {
        "commons_id": commons_id,
        "generation_kwh": generation_kwh,
        "consumption_kwh": consumption_kwh,
        "surplus_kwh": commons.surplus_kwh,
        "self_sufficient": is_self_sufficient,
        "cost_per_member": commons.cost_per_member,
        "co2_avoided_tons": commons.co2_avoided_tons,
        "total_community_savings": commons.money_saved_community,
        "message": "Energy self-sufficient!" if is_self_sufficient else f"Generated {generation_kwh/consumption_kwh*100:.1f}% of needs",
        "truth": "Community energy works. Local generation. Local control. Local benefits.",
        "impact": f"${commons.money_saved_community:,.2f} saved, {commons.co2_avoided_tons:.1f} tons CO2 avoided"
    }

@router.get("/utilities/commons/all")
async def get_all_energy_commons():
    """Get all community energy commons"""
    if not energy_commons:
        return {
            "message": "No energy commons yet",
            "truth": "Start community energy today. Own your power."
        }

    total_communities = len(energy_commons)
    total_members = sum(c.total_members for c in energy_commons.values())
    total_capacity = sum(c.solar_capacity_kw + c.wind_capacity_kw for c in energy_commons.values())
    total_co2_avoided = sum(c.co2_avoided_tons for c in energy_commons.values())
    total_saved = sum(c.money_saved_community for c in energy_commons.values())

    return {
        "total_communities": total_communities,
        "total_members": total_members,
        "total_capacity_kw": total_capacity,
        "total_co2_avoided_tons": total_co2_avoided,
        "total_community_savings": total_saved,
        "communities": list(energy_commons.values()),
        "message": f"{total_communities} communities generating their own power",
        "truth": "Community energy movement growing. Power to the people.",
        "impact": f"{total_members} people served, ${total_saved:,.2f} saved, {total_co2_avoided:.1f} tons CO2 avoided"
    }

# ============================================================================
# PILOT PROGRAMS ENDPOINTS
# ============================================================================

@router.post("/utilities/pilot/create")
async def create_pilot_program(pilot: FreeUtilitiesPilot):
    """Create free utilities pilot program"""
    pilot_id = f"pilot_{len(pilot_programs) + 1}"
    pilot.pilot_id = pilot_id
    pilot.created_at = datetime.now().isoformat()
    pilot.updated_at = datetime.now().isoformat()

    pilot_programs[pilot_id] = pilot

    # Count what's free
    free_utilities = []
    if pilot.free_electricity: free_utilities.append("electricity")
    if pilot.free_heating: free_utilities.append("heating")
    if pilot.free_water: free_utilities.append("water")
    if pilot.free_internet: free_utilities.append("internet")

    return {
        "pilot_id": pilot_id,
        "location": pilot.location,
        "free_utilities": free_utilities,
        "households": pilot.households,
        "people_served": pilot.people_served,
        "message": f"Free utilities pilot launched in {pilot.location}",
        "truth": "Pilot program demonstrating free utilities work. Proof of concept.",
        "next_steps": [
            "Track satisfaction and impact",
            "Document success stories",
            "Measure cost savings",
            "Prepare for scale"
        ]
    }

@router.patch("/utilities/pilot/{pilot_id}/update")
async def update_pilot_program(
    pilot_id: str,
    satisfaction: Optional[float] = None,
    health_improvement: Optional[str] = None,
    challenge: Optional[str] = None,
    solution: Optional[str] = None,
    is_successful: Optional[bool] = None
):
    """Update pilot program with results and learnings"""
    if pilot_id not in pilot_programs:
        raise HTTPException(status_code=404, detail="Pilot program not found")

    pilot = pilot_programs[pilot_id]

    if satisfaction is not None:
        pilot.participant_satisfaction = satisfaction

    if health_improvement:
        pilot.health_improvements.append(health_improvement)

    if challenge:
        pilot.challenges.append(challenge)

    if solution:
        pilot.solutions.append(solution)

    if is_successful is not None:
        pilot.is_successful = is_successful
        if is_successful and pilot.is_active:
            pilot.is_active = False
            pilot.completion_date = datetime.now().isoformat()

    pilot.updated_at = datetime.now().isoformat()

    return {
        "pilot_id": pilot_id,
        "satisfaction": pilot.participant_satisfaction,
        "is_successful": pilot.is_successful,
        "challenges_faced": len(pilot.challenges),
        "solutions_found": len(pilot.solutions),
        "message": "Pilot program successful! Ready to scale." if pilot.is_successful else "Pilot program updated",
        "truth": "Free utilities work. Proof demonstrated." if pilot.is_successful else "Learning and improving.",
        "impact": {
            "health_improvements": len(pilot.health_improvements),
            "educational_improvements": len(pilot.educational_improvements),
            "economic_improvements": len(pilot.economic_improvements)
        }
    }

@router.get("/utilities/pilot/all")
async def get_all_pilots():
    """Get all pilot programs"""
    if not pilot_programs:
        return {
            "message": "No pilot programs yet",
            "truth": "Start a pilot today. Demonstrate free utilities work."
        }

    total_pilots = len(pilot_programs)
    successful_pilots = sum(1 for p in pilot_programs.values() if p.is_successful)
    total_people_served = sum(p.people_served for p in pilot_programs.values())
    avg_satisfaction = sum(p.participant_satisfaction for p in pilot_programs.values()) / total_pilots

    return {
        "total_pilots": total_pilots,
        "successful_pilots": successful_pilots,
        "success_rate": (successful_pilots / total_pilots * 100) if total_pilots > 0 else 0,
        "total_people_served": total_people_served,
        "average_satisfaction": avg_satisfaction,
        "pilots": list(pilot_programs.values()),
        "message": f"{successful_pilots}/{total_pilots} pilots successful",
        "truth": "Free utilities proven to work. Ready to scale.",
        "impact": f"{total_people_served} people experiencing free utilities. Satisfaction: {avg_satisfaction:.1f}%"
    }

# ============================================================================
# SYSTEM TRANSITION TRACKING
# ============================================================================

@router.post("/utilities/transition/track")
async def track_system_transition(transition: SystemTransitionTracking):
    """Track transition from private → public → free utilities"""
    key = f"{transition.region}_{transition.utility_type}"
    transition.updated_at = datetime.now().isoformat()

    transition_tracking[key] = transition

    # Calculate transition percentage based on completed steps
    steps = [
        transition.public_awareness_raised,
        transition.political_support_secured,
        transition.pilot_program_successful,
        transition.funding_secured,
        transition.infrastructure_built,
        transition.service_launched
    ]
    transition.transition_percentage = (sum(steps) / len(steps)) * 100

    return {
        "region": transition.region,
        "utility_type": transition.utility_type,
        "current_model": transition.current_model,
        "target_model": transition.target_model,
        "transition_percentage": transition.transition_percentage,
        "people_with_free_utilities": transition.people_with_free_utilities,
        "money_saved": transition.money_saved_community,
        "debt_forgiven": transition.debt_forgiven,
        "message": f"{transition.transition_percentage:.0f}% transition complete in {transition.region}",
        "truth": "System transition in progress. Private → Public → Free.",
        "wisdom": "The transformation is happening. Keep building."
    }

@router.get("/utilities/transition/global")
async def get_global_transition_status():
    """Get global utilities transition status"""
    if not transition_tracking:
        return {
            "message": "No transition tracking yet",
            "truth": "Start tracking your region's transition today."
        }

    total_people = sum(t.people_with_free_utilities for t in transition_tracking.values())
    total_saved = sum(t.money_saved_community for t in transition_tracking.values())
    total_debt_forgiven = sum(t.debt_forgiven for t in transition_tracking.values())
    avg_transition = sum(t.transition_percentage for t in transition_tracking.values()) / len(transition_tracking)

    by_utility = {}
    for t in transition_tracking.values():
        utility = t.utility_type
        if utility not in by_utility:
            by_utility[utility] = []
        by_utility[utility].append({
            "region": t.region,
            "percentage": t.transition_percentage,
            "people_served": t.people_with_free_utilities
        })

    return {
        "global_status": {
            "regions_tracked": len(transition_tracking),
            "average_transition_percentage": avg_transition,
            "total_people_with_free_utilities": total_people,
            "total_money_saved": total_saved,
            "total_debt_forgiven": total_debt_forgiven
        },
        "by_utility_type": by_utility,
        "message": f"{avg_transition:.1f}% average transition globally",
        "truth": "Global free utilities movement growing. The transformation is happening.",
        "impact": f"{total_people} people with free utilities, ${total_saved:,.2f} saved, ${total_debt_forgiven:,.2f} debt forgiven"
    }

# ============================================================================
# WISDOM AND EDUCATION ENDPOINTS
# ============================================================================

@router.get("/utilities/wisdom/why-free")
async def get_why_utilities_should_be_free():
    """Get comprehensive explanation of why utilities should be free"""
    return {
        "fundamental_truths": [
            "Basic needs are human rights, not commodities for profit",
            "Survival should not require payment",
            "Life is not a subscription service",
            "Energy is abundant (sun, wind, water, Earth)",
            "Scarcity is manufactured for profit",
            "We already paid for infrastructure (tax dollars)",
            "Free system cheaper than current profit-driven system"
        ],
        "current_system_harms": [
            "People freeze in winter (can't afford heating)",
            "People die in summer heat (can't afford cooling)",
            "Children sit in darkness (no light for homework)",
            "Families choose: food or utilities",
            "Debt traps (late fees create more fees)",
            "Disconnection cycles (reconnection fees)",
            "Corporate profits while people suffer"
        ],
        "benefits_of_free": {
            "individual": ["No utility stress", "Money for food/health/education", "Dignity restored", "Survival guaranteed"],
            "family": ["Warm homes", "Light for learning", "Internet for education", "Thriving not just surviving"],
            "community": ["Energy poverty eliminated", "Community ownership", "Democratic control", "Resilience"],
            "society": ["Inequality reduced", "Health improved", "Education accessible", "Environment healing"]
        },
        "how_we_pay": [
            "Eliminate profit extraction ($200B+ saved)",
            "Carbon tax on luxury use",
            "Wealth tax (2% on billionaires)",
            "Corporate taxes",
            "Military budget reallocation",
            "Eliminate wasteful spending (billing, debt collection, marketing)"
        ],
        "truth": "Free utilities are not radical. They are rational. They are inevitable.",
        "wisdom": "The question is not 'Can we afford free utilities?' The question is 'Can we afford not to?'"
    }

@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "operational",
        "system": "Free Utilities as Human Right API",
        "truth": "Basic needs are rights. Utilities should be free.",
        "statistics": {
            "debt_forgiveness_events": len(debt_forgiveness),
            "ube_accounts": len(ube_accounts),
            "energy_commons": len(energy_commons),
            "pilot_programs": len(pilot_programs),
            "transition_regions": len(transition_tracking)
        },
        "wisdom": "System operational. The transformation to free utilities is happening."
    }
