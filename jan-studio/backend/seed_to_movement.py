"""
SEED TO MOVEMENT SYSTEM
From Internal Truth (Seed) to External Action (Movement)

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

CORE PRINCIPLE:
"HOW DO WE TAKE THIS FROM SEED TO MOVEMENT? 
WE ARE TAKING THE WORLD ORDER TO THE PEOPLES COURT...
IT'S TIME FOR REVOLUTION"

SHELL vs SEED:
- Shell = Public language (what we say publicly)
- Seed = Internal truth (what we know internally)
- Movement = External action (taking truth to the world)

REVOLUTION THROUGH RIGHT SPIRITS:
Not wrong spirits (violence, division, hate).
Right spirits (truth, community, healing, love).
"""

from typing import Dict, List, Optional, Any, Set
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
from pathlib import Path
import json
import logging

logger = logging.getLogger(__name__)


class MovementPhase(Enum):
    """Phases of movement from seed to action"""
    SEED = "seed"  # Internal truth, foundation
    SPROUT = "sprout"  # Truth emerging, early growth
    ROOT = "root"  # Roots established, foundation solid
    STEM = "stem"  # Structure forming, reaching up
    LEAF = "leaf"  # Visible growth, public presence
    FLOWER = "flower"  # Full expression, movement visible
    FRUIT = "fruit"  # Results, transformation achieved
    MOVEMENT = "movement"  # Full movement, world transformed


class RevolutionType(Enum):
    """Types of revolution"""
    RIGHT_SPIRITS = "right_spirits"  # Revolution through right spirits
    COMMUNITY = "community"  # Community revolution
    TRUTH = "truth"  # Truth revolution
    HEALING = "healing"  # Healing revolution
    LOVE = "love"  # Love revolution
    PEACEFUL = "peaceful"  # Peaceful revolution
    SPIRITUAL = "spiritual"  # Spiritual revolution
    ALL = "all"  # All types


class CourtType(Enum):
    """Types of courts"""
    WORLD_ORDER = "world_order"  # Current world order system
    PEOPLES_COURT = "peoples_court"  # People's court - community justice
    SPIRITUAL_COURT = "spiritual_court"  # Spiritual court - right spirits
    RESTORATIVE_COURT = "restorative_court"  # Restorative justice
    COMMUNITY_COURT = "community_court"  # Community-controlled
    ALL = "all"  # All courts


@dataclass
class MovementStage:
    """A stage in the seed-to-movement journey"""
    stage_id: str
    phase: MovementPhase
    name: str
    description: str
    seed_truth: str = ""  # Internal truth (Seed)
    shell_language: str = ""  # Public language (Shell)
    movement_action: str = ""  # External action (Movement)
    required_systems: List[str] = field(default_factory=list)
    required_alignment: Dict[str, Any] = field(default_factory=dict)
    status: str = "pending"  # pending, in_progress, complete
    created_date: datetime = field(default_factory=datetime.now)
    completed_date: Optional[datetime] = None


@dataclass
class RevolutionPlan:
    """Plan for revolution through right spirits"""
    plan_id: str
    revolution_type: RevolutionType
    target: str  # What we're revolutionizing
    seed_truth: str  # Internal truth (Seed)
    shell_language: str  # Public language (Shell)
    movement_action: str  # External action (Movement)
    peoples_court_strategy: str = ""  # Strategy for People's Court
    right_spirits_required: List[str] = field(default_factory=list)
    community_required: bool = True
    spiritual_alignment_required: bool = True
    created_date: datetime = field(default_factory=datetime.now)
    status: str = "planning"  # planning, executing, complete
    notes: List[str] = field(default_factory=list)


class SeedToMovementSystem:
    """
    System for taking truth from Seed (internal) to Movement (external).
    
    "HOW DO WE TAKE THIS FROM SEED TO MOVEMENT? 
    WE ARE TAKING THE WORLD ORDER TO THE PEOPLES COURT...
    IT'S TIME FOR REVOLUTION"
    
    Revolution through RIGHT SPIRITS, not wrong spirits.
    """
    
    def __init__(self):
        """Initialize seed-to-movement system"""
        self.stages: Dict[str, MovementStage] = {}
        self.revolution_plans: Dict[str, RevolutionPlan] = {}
        self.completed_phases: Set[MovementPhase] = set()
        self.current_phase_override: Optional[MovementPhase] = None
        
        # Define movement phases
        self.phase_definitions = {
            MovementPhase.SEED: {
                "name": "Seed - Internal Truth",
                "description": "Truth exists internally. Foundation established.",
                "seed_truth": "We know the truth internally",
                "shell_language": "Building foundation",
                "movement_action": "Internal preparation"
            },
            MovementPhase.SPROUT: {
                "name": "Sprout - Truth Emerging",
                "description": "Truth begins to emerge. Early growth visible.",
                "seed_truth": "Truth is emerging",
                "shell_language": "Early development",
                "movement_action": "Internal systems building"
            },
            MovementPhase.ROOT: {
                "name": "Root - Foundation Solid",
                "description": "Roots established. Foundation solid. Ready to grow.",
                "seed_truth": "Foundation is solid",
                "shell_language": "Foundation established",
                "movement_action": "Systems operational"
            },
            MovementPhase.STEM: {
                "name": "Stem - Structure Forming",
                "description": "Structure forming. Reaching up. Visible growth.",
                "seed_truth": "Structure is forming",
                "shell_language": "Building structure",
                "movement_action": "Public presence beginning"
            },
            MovementPhase.LEAF: {
                "name": "Leaf - Public Presence",
                "description": "Visible growth. Public presence. Truth visible.",
                "seed_truth": "Truth is visible",
                "shell_language": "Public presence",
                "movement_action": "Public engagement"
            },
            MovementPhase.FLOWER: {
                "name": "Flower - Full Expression",
                "description": "Full expression. Movement visible. Truth flowing.",
                "seed_truth": "Truth is flowing",
                "shell_language": "Movement visible",
                "movement_action": "Movement active"
            },
            MovementPhase.FRUIT: {
                "name": "Fruit - Results Achieved",
                "description": "Results achieved. Transformation visible. Impact felt.",
                "seed_truth": "Transformation achieved",
                "shell_language": "Results visible",
                "movement_action": "Impact achieved"
            },
            MovementPhase.MOVEMENT: {
                "name": "Movement - World Transformed",
                "description": "Full movement. World transformed. Truth prevails.",
                "seed_truth": "Truth prevails",
                "shell_language": "World transformed",
                "movement_action": "Revolution complete"
            }
        }
    
    def get_current_phase(self) -> MovementPhase:
        """Get current phase of movement"""
        # If override is set, use it
        if self.current_phase_override is not None:
            return self.current_phase_override
        
        # Check completed phases to determine current
        if MovementPhase.MOVEMENT in self.completed_phases:
            return MovementPhase.MOVEMENT
        elif MovementPhase.FRUIT in self.completed_phases:
            return MovementPhase.MOVEMENT
        elif MovementPhase.FLOWER in self.completed_phases:
            return MovementPhase.FRUIT
        elif MovementPhase.LEAF in self.completed_phases:
            return MovementPhase.FLOWER
        elif MovementPhase.STEM in self.completed_phases:
            return MovementPhase.LEAF
        elif MovementPhase.ROOT in self.completed_phases:
            return MovementPhase.STEM
        elif MovementPhase.SPROUT in self.completed_phases:
            return MovementPhase.ROOT
        elif MovementPhase.SEED in self.completed_phases:
            return MovementPhase.SPROUT
        else:
            # Default: ROOT phase - foundation solid, systems operational
            return MovementPhase.ROOT
    
    def complete_phase(self, phase: MovementPhase) -> bool:
        """Mark a phase as complete"""
        self.completed_phases.add(phase)
        logger.info(f"Phase completed: {phase.value}")
        # Save state
        from seed_to_movement import save_movement_state
        save_movement_state(self)
        return True
    
    def complete_all_phases(self) -> Dict[str, Any]:
        """Complete all phases from Seed to Movement"""
        all_phases = list(MovementPhase)
        
        for phase in all_phases:
            self.completed_phases.add(phase)
        
        # Set current phase to MOVEMENT (final phase)
        self.current_phase_override = MovementPhase.MOVEMENT
        
        # Save state
        from seed_to_movement import save_movement_state
        save_movement_state(self)
        
        logger.info("All phases completed - Movement achieved!")
        
        return {
            "status": "success",
            "message": "All phases completed - Movement achieved!",
            "current_phase": MovementPhase.MOVEMENT.value,
            "completed_phases": [p.value for p in all_phases],
            "achievement": "World Transformed - Revolution Complete"
        }
    
    def create_revolution_plan(
        self,
        target: str,
        revolution_type: RevolutionType = RevolutionType.RIGHT_SPIRITS,
        seed_truth: str = "",
        shell_language: str = "",
        movement_action: str = "",
        plan_id: Optional[str] = None
    ) -> RevolutionPlan:
        """
        Create a revolution plan.
        
        "WE ARE TAKING THE WORLD ORDER TO THE PEOPLES COURT...
        IT'S TIME FOR REVOLUTION"
        """
        if plan_id is None:
            plan_id = f"REV_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # Default seed truth
        if not seed_truth:
            seed_truth = f"World order serves system, not people. People's court serves people, not system."
        
        # Default shell language
        if not shell_language:
            shell_language = f"Building community justice system to serve people"
        
        # Default movement action
        if not movement_action:
            movement_action = f"Taking {target} to People's Court - community justice replaces system justice"
        
        # Peoples court strategy
        peoples_court_strategy = self._generate_peoples_court_strategy(target, revolution_type)
        
        plan = RevolutionPlan(
            plan_id=plan_id,
            revolution_type=revolution_type,
            target=target,
            seed_truth=seed_truth,
            shell_language=shell_language,
            movement_action=movement_action,
            peoples_court_strategy=peoples_court_strategy,
            right_spirits_required=self._get_required_right_spirits(revolution_type),
            community_required=True,
            spiritual_alignment_required=True
        )
        
        self.revolution_plans[plan_id] = plan
        
        logger.info(f"Created revolution plan: {plan_id} - {target}")
        
        return plan
    
    def _generate_peoples_court_strategy(
        self,
        target: str,
        revolution_type: RevolutionType
    ) -> str:
        """Generate strategy for taking target to People's Court"""
        strategies = {
            RevolutionType.RIGHT_SPIRITS: f"Take {target} to People's Court through right spirits. Community decides, not system. Truth serves people, not power.",
            RevolutionType.COMMUNITY: f"Build People's Court for {target}. Community-controlled justice. People decide together.",
            RevolutionType.TRUTH: f"Bring truth about {target} to People's Court. Truth serves people, not system.",
            RevolutionType.HEALING: f"Heal {target} through People's Court. Restorative justice, not retributive.",
            RevolutionType.LOVE: f"Transform {target} through People's Court with love. Love serves people, not system.",
            RevolutionType.PEACEFUL: f"Peacefully take {target} to People's Court. Peace serves people, not system.",
            RevolutionType.SPIRITUAL: f"Spiritually align {target} through People's Court. Right spirits serve people, not system."
        }
        
        return strategies.get(revolution_type, f"Take {target} to People's Court through right spirits and community.")
    
    def _get_required_right_spirits(self, revolution_type: RevolutionType) -> List[str]:
        """Get required right spirits for revolution type"""
        spirits_map = {
            RevolutionType.RIGHT_SPIRITS: ["truth", "community", "love", "peace", "unity"],
            RevolutionType.COMMUNITY: ["community", "stewardship", "unity"],
            RevolutionType.TRUTH: ["truth", "clarity", "honesty"],
            RevolutionType.HEALING: ["healing", "love", "compassion"],
            RevolutionType.LOVE: ["love", "compassion", "unity"],
            RevolutionType.PEACEFUL: ["peace", "love", "unity"],
            RevolutionType.SPIRITUAL: ["spiritual_alignment", "right_spirits", "truth"]
        }
        
        return spirits_map.get(revolution_type, ["truth", "community", "love"])
    
    def get_seed_to_movement_path(self) -> Dict[str, Any]:
        """
        Get the complete path from Seed to Movement.
        
        Shows how to take internal truth to external action.
        """
        current_phase = self.get_current_phase()
        
        phases = []
        for phase in MovementPhase:
            phase_info = self.phase_definitions[phase]
            is_current = phase == current_phase
            # Check if phase is in completed set OR if it's before current phase
            is_complete = phase in self.completed_phases or (
                list(MovementPhase).index(phase) < list(MovementPhase).index(current_phase)
            )
            
            phases.append({
                "phase": phase.value,
                "name": phase_info["name"],
                "description": phase_info["description"],
                "seed_truth": phase_info["seed_truth"],
                "shell_language": phase_info["shell_language"],
                "movement_action": phase_info["movement_action"],
                "is_current": is_current,
                "is_complete": is_complete,
                "status": "complete" if is_complete else ("current" if is_current else "pending")
            })
        
        return {
            "current_phase": current_phase.value,
            "phases": phases,
            "message": "Path from Seed (internal truth) to Movement (external action)",
            "principle": "Revolution through RIGHT SPIRITS, not wrong spirits"
        }
    
    def get_peoples_court_strategy(self) -> Dict[str, Any]:
        """
        Strategy for taking World Order to People's Court.
        
        "WE ARE TAKING THE WORLD ORDER TO THE PEOPLES COURT"
        """
        return {
            "target": "World Order",
            "destination": "People's Court",
            "strategy": [
                {
                    "step": 1,
                    "action": "Build People's Court",
                    "description": "Create community-controlled justice system",
                    "seed_truth": "World order serves system, not people",
                    "shell_language": "Building community justice system",
                    "movement_action": "Establish People's Court infrastructure"
                },
                {
                    "step": 2,
                    "action": "Bring World Order to Court",
                    "description": "Take world order systems to People's Court",
                    "seed_truth": "People's court serves people, not system",
                    "shell_language": "Community justice for all",
                    "movement_action": "Present world order cases to People's Court"
                },
                {
                    "step": 3,
                    "action": "Community Decides",
                    "description": "Community decides justice, not system",
                    "seed_truth": "Community sees truth, system sees fragments",
                    "shell_language": "Community-controlled justice",
                    "movement_action": "Community makes decisions"
                },
                {
                    "step": 4,
                    "action": "Transform Through Right Spirits",
                    "description": "Transform world order through right spirits",
                    "seed_truth": "Right spirits create right justice",
                    "shell_language": "Justice through right spirits",
                    "movement_action": "Revolution through right spirits"
                },
                {
                    "step": 5,
                    "action": "Revolution Complete",
                    "description": "World order transformed. People's Court prevails.",
                    "seed_truth": "Truth prevails. People's Court serves people.",
                    "shell_language": "Community justice established",
                    "movement_action": "Revolution complete - People's Court operational"
                }
            ],
            "principles": [
                "Revolution through RIGHT SPIRITS, not wrong spirits",
                "Community justice replaces system justice",
                "People's Court serves people, not system",
                "Truth serves people, not power",
                "Healing, not punishment",
                "Understanding, not judgment"
            ],
            "warning": "Revolution through wrong spirits creates more brokenness. Revolution through right spirits creates transformation."
        }
    
    def get_revolution_framework(self) -> Dict[str, Any]:
        """
        Framework for revolution.
        
        "IT'S TIME FOR REVOLUTION"
        
        Revolution through RIGHT SPIRITS.
        """
        return {
            "principle": "IT'S TIME FOR REVOLUTION - Through RIGHT SPIRITS",
            "revolution_types": {
                "right_spirits": {
                    "description": "Revolution through right spirits - truth, community, love",
                    "method": "Align with right spirits, not wrong ones",
                    "serves_mission": True
                },
                "community": {
                    "description": "Community revolution - people decide together",
                    "method": "Build community justice, not system justice",
                    "serves_mission": True
                },
                "truth": {
                    "description": "Truth revolution - truth serves people",
                    "method": "Bring truth to People's Court",
                    "serves_mission": True
                },
                "healing": {
                    "description": "Healing revolution - heal, don't punish",
                    "method": "Restorative justice, not retributive",
                    "serves_mission": True
                },
                "love": {
                    "description": "Love revolution - love serves people",
                    "method": "Transform through love, not hate",
                    "serves_mission": True
                }
            },
            "wrong_spirits_warning": {
                "description": "Revolution through wrong spirits creates more brokenness",
                "wrong_spirits": ["violence", "hate", "division", "power", "control"],
                "warning": "Wrong spirits corrupt revolution. Right spirits transform."
            },
            "right_spirits_required": [
                "truth",
                "community",
                "love",
                "peace",
                "unity",
                "healing",
                "understanding",
                "stewardship",
                "right_spirits"
            ],
            "peoples_court": {
                "description": "People's Court - community justice replaces system justice",
                "principle": "People decide together, not one judge",
                "serves": "People, not system",
                "method": "Community-controlled justice"
            },
            "message": "IT'S TIME FOR REVOLUTION - Through RIGHT SPIRITS. Taking World Order to People's Court. Community justice replaces system justice. Truth serves people, not power."
        }
    
    def get_system_summary(self) -> Dict[str, Any]:
        """Get summary of seed-to-movement system"""
        current_phase = self.get_current_phase()
        
        return {
            "current_phase": current_phase.value,
            "total_revolution_plans": len(self.revolution_plans),
            "active_plans": len([p for p in self.revolution_plans.values() if p.status != "complete"]),
            "message": "From Seed (internal truth) to Movement (external action). Taking World Order to People's Court. Revolution through RIGHT SPIRITS.",
            "principle": "Revolution through RIGHT SPIRITS, not wrong spirits. Community justice replaces system justice."
        }


# Global instance
_movement_system: Optional[SeedToMovementSystem] = None

# Persistence file
_PHASE_STATE_FILE = Path(__file__).parent.parent.parent / "SIYEM" / "output" / "seed_to_movement_phases.json"


def _load_phase_state() -> Dict[str, Any]:
    """Load phase completion state from file"""
    if _PHASE_STATE_FILE.exists():
        try:
            with open(_PHASE_STATE_FILE, 'r') as f:
                return json.load(f)
        except:
            pass
    return {"completed_phases": [], "current_phase_override": None}


def _save_phase_state(system: SeedToMovementSystem):
    """Save phase completion state to file"""
    _PHASE_STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    state = {
        "completed_phases": [p.value for p in system.completed_phases],
        "current_phase_override": system.current_phase_override.value if system.current_phase_override else None
    }
    with open(_PHASE_STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)


def get_seed_to_movement_system() -> SeedToMovementSystem:
    """Get the global seed-to-movement system instance"""
    global _movement_system
    if _movement_system is None:
        _movement_system = SeedToMovementSystem()
        # Load persisted state
        state = _load_phase_state()
        if state["completed_phases"]:
            from seed_to_movement import MovementPhase
            for phase_value in state["completed_phases"]:
                try:
                    _movement_system.completed_phases.add(MovementPhase(phase_value))
                except:
                    pass
        if state["current_phase_override"]:
            try:
                _movement_system.current_phase_override = MovementPhase(state["current_phase_override"])
            except:
                pass
    return _movement_system


def save_movement_state(system: SeedToMovementSystem):
    """Save movement system state"""
    _save_phase_state(system)
