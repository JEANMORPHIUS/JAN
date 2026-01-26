"""ACTION PLAN TRACKER
Track progress on Harringay Council and Turkish Revolution (The Play) action plans

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity


PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

import sys
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass, field, asdict
from typing import List, Optional, Dict, Any
from enum import Enum
import json

sys.path.insert(0, str(Path(__file__).parent))

from utils import setup_logging, standard_main

logger = setup_logging(__name__)

class ActionStatus(Enum):
    """Action status"""
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    BLOCKED = "blocked"
    CANCELLED = "cancelled"

class ActionPlanType(Enum):
    """Action plan type"""
    HARRINGAY_COUNCIL = "harringay_council"
    TURKISH_REVOLUTION_PLAY = "turkish_revolution_play"

@dataclass
class ActionItem:
    """Individual action item"""
    item_id: str
    title: str
    description: str
    status: str = ActionStatus.NOT_STARTED.value
    assigned_to: Optional[str] = None
    due_date: Optional[str] = None
    completed_date: Optional[str] = None
    notes: str = ""
    dependencies: List[str] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    updated_at: str = field(default_factory=lambda: datetime.now().isoformat())

@dataclass
class ActionPhase:
    """Phase within action plan"""
    phase_id: str
    title: str
    description: str
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    status: str = ActionStatus.NOT_STARTED.value
    actions: List[ActionItem] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())

@dataclass
class ActionPlan:
    """Complete action plan"""
    plan_id: str
    plan_type: str
    title: str
    description: str
    status: str = ActionStatus.NOT_STARTED.value
    phases: List[ActionPhase] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    updated_at: str = field(default_factory=lambda: datetime.now().isoformat())

class ActionPlanTracker:
    """
    Action Plan Tracker
    Track progress on multiple action plans
    """
    
    def __init__(self, user_id: str = "jan", data_dir: Path = None):
        self.user_id = user_id
        self.data_dir = data_dir or Path(__file__).parent.parent / "data" / "action_plans"
        self.data_dir.mkdir(parents=True, exist_ok=True)
        
        self.plans_file = self.data_dir / f"{user_id}_action_plans.json"
        self.plans: List[ActionPlan] = []
        
        self._load_plans()
        self._initialize_default_plans()
    
    def _load_plans(self):
        """Load action plans"""
        if self.plans_file.exists():
            try:
                with open(self.plans_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                plans_data = []
                for plan_dict in data.get("plans", []):
                    # Reconstruct phases and actions
                    phases = []
                    for phase_dict in plan_dict.get("phases", []):
                        actions = [ActionItem(**a) for a in phase_dict.get("actions", [])]
                        phases.append(ActionPhase(
                            phase_id=phase_dict["phase_id"],
                            title=phase_dict["title"],
                            description=phase_dict.get("description", ""),
                            start_date=phase_dict.get("start_date"),
                            end_date=phase_dict.get("end_date"),
                            status=phase_dict.get("status", ActionStatus.NOT_STARTED.value),
                            actions=actions
                        ))
                    plans_data.append(ActionPlan(
                        plan_id=plan_dict["plan_id"],
                        plan_type=plan_dict["plan_type"],
                        title=plan_dict["title"],
                        description=plan_dict.get("description", ""),
                        status=plan_dict.get("status", ActionStatus.NOT_STARTED.value),
                        phases=phases,
                        created_at=plan_dict.get("created_at", datetime.now().isoformat()),
                        updated_at=plan_dict.get("updated_at", datetime.now().isoformat())
                    ))
                self.plans = plans_data
            except Exception as e:
                logger.warning(f"Error loading plans: {e}")
                self.plans = []
        else:
            self.plans = []
    
    def _save_plans(self):
        """Save action plans"""
        try:
            plans_data = []
            for plan in self.plans:
                plan_dict = asdict(plan)
                plan_dict["updated_at"] = datetime.now().isoformat()
                plans_data.append(plan_dict)
            
            with open(self.plans_file, 'w', encoding='utf-8') as f:
                json.dump({
                    "plans": plans_data,
                    "last_updated": datetime.now().isoformat()
                }, f, indent=2, ensure_ascii=False)
        except Exception as e:
            logger.error(f"Error saving plans: {e}")
    
    def _initialize_default_plans(self):
        """Initialize default action plans if they don't exist"""
        if not any(p.plan_type == ActionPlanType.HARRINGAY_COUNCIL.value for p in self.plans):
            self._create_harringay_plan()
        
        if not any(p.plan_type == ActionPlanType.TURKISH_REVOLUTION_PLAY.value for p in self.plans):
            self._create_turkish_revolution_plan()
        
        self._save_plans()
    
    def _create_harringay_plan(self):
        """Create Harringay Council action plan"""
        plan = ActionPlan(
            plan_id="harringay_council_2026",
            plan_type=ActionPlanType.HARRINGAY_COUNCIL.value,
            title="Harringay Council Action Plan",
            description="Local government engagement & community transformation",
            status=ActionStatus.NOT_STARTED.value
        )
        
        # Phase 1: Research & Mapping
        phase1 = ActionPhase(
            phase_id="phase1_research",
            title="Research & Mapping",
            description="Weeks 1-2: Research council structure, map community, identify issues",
            status=ActionStatus.NOT_STARTED.value
        )
        phase1.actions = [
            ActionItem("research_1", "Map council leadership", "Identify key decision-makers"),
            ActionItem("research_2", "Map community organizations", "Identify local groups and activists"),
            ActionItem("research_3", "Identify key issues", "Document housing, education, health, etc."),
            ActionItem("research_4", "Assess alignment", "Where do our systems align with council priorities?")
        ]
        
        # Phase 2: Engagement Strategy
        phase2 = ActionPhase(
            phase_id="phase2_engagement",
            title="Engagement Strategy",
            description="Weeks 3-4: Initial outreach, community engagement, proposal development",
            status=ActionStatus.NOT_STARTED.value
        )
        phase2.actions = [
            ActionItem("engage_1", "Contact council leadership", "Reach out to leader and cabinet"),
            ActionItem("engage_2", "Organize community meeting", "Build local support"),
            ActionItem("engage_3", "Develop proposals", "Housing, childcare, accountability, education"),
            ActionItem("engage_4", "Build partnerships", "Connect with local organizations")
        ]
        
        plan.phases = [phase1, phase2]
        self.plans.append(plan)
    
    def _create_turkish_revolution_plan(self):
        """Create Turkish Revolution (The Play) action plan"""
        plan = ActionPlan(
            plan_id="turkish_revolution_play_2026",
            plan_type=ActionPlanType.TURKISH_REVOLUTION_PLAY.value,
            title="Turkish Revolution (The Play) - Action Plan",
            description="Creative production: Revolution through Right Spirits",
            status=ActionStatus.NOT_STARTED.value
        )
        
        # Phase 1: Concept Development
        phase1 = ActionPhase(
            phase_id="phase1_concept",
            title="Concept Development",
            description="Weeks 1-4: Story, characters, musical integration, cultural authenticity",
            status=ActionStatus.NOT_STARTED.value
        )
        phase1.actions = [
            ActionItem("concept_1", "Define narrative arc", "Structure the story of revolution"),
            ActionItem("concept_2", "Develop characters", "The Voice, Community, System, Bridge"),
            ActionItem("concept_3", "Select Karasahin songs", "Integrate music with narrative"),
            ActionItem("concept_4", "Ensure cultural authenticity", "Turkish Cypriot identity, bilingual")
        ]
        
        # Phase 2: Script Development
        phase2 = ActionPhase(
            phase_id="phase2_script",
            title="Script Development",
            description="Weeks 5-8: Write script, integrate music, develop scenes",
            status=ActionStatus.NOT_STARTED.value
        )
        phase2.actions = [
            ActionItem("script_1", "Write first draft", "Complete full script"),
            ActionItem("script_2", "Develop key scenes", "Opening, acts, climax, resolution"),
            ActionItem("script_3", "Integrate musical moments", "Songs and soundscape"),
            ActionItem("script_4", "Bilingual elements", "Turkish/English dialogue")
        ]
        
        plan.phases = [phase1, phase2]
        self.plans.append(plan)
    
    def update_action_status(self, plan_id: str, phase_id: str, action_id: str, status: str, notes: str = ""):
        """Update action item status"""
        plan = next((p for p in self.plans if p.plan_id == plan_id), None)
        if not plan:
            logger.error(f"Plan not found: {plan_id}")
            return False
        
        phase = next((p for p in plan.phases if p.phase_id == phase_id), None)
        if not phase:
            logger.error(f"Phase not found: {phase_id}")
            return False
        
        action = next((a for a in phase.actions if a.item_id == action_id), None)
        if not action:
            logger.error(f"Action not found: {action_id}")
            return False
        
        action.status = status
        action.notes = notes
        action.updated_at = datetime.now().isoformat()
        
        if status == ActionStatus.COMPLETED.value:
            action.completed_date = datetime.now().isoformat()
        
        self._save_plans()
        logger.info(f"Updated action {action_id} to {status}")
        return True
    
    def get_plan_status(self, plan_id: str) -> Dict[str, Any]:
        """Get status report for a plan"""
        plan = next((p for p in self.plans if p.plan_id == plan_id), None)
        if not plan:
            return {"error": "Plan not found"}
        
        total_actions = sum(len(phase.actions) for phase in plan.phases)
        completed_actions = sum(
            len([a for a in phase.actions if a.status == ActionStatus.COMPLETED.value])
            for phase in plan.phases
        )
        in_progress = sum(
            len([a for a in phase.actions if a.status == ActionStatus.IN_PROGRESS.value])
            for phase in plan.phases
        )
        
        return {
            "plan_id": plan.plan_id,
            "title": plan.title,
            "status": plan.status,
            "total_actions": total_actions,
            "completed_actions": completed_actions,
            "in_progress": in_progress,
            "completion_percentage": (completed_actions / total_actions * 100) if total_actions > 0 else 0,
            "phases": [
                {
                    "phase_id": phase.phase_id,
                    "title": phase.title,
                    "status": phase.status,
                    "actions_count": len(phase.actions),
                    "completed_count": len([a for a in phase.actions if a.status == ActionStatus.COMPLETED.value])
                }
                for phase in plan.phases
            ]
        }
    
    def get_all_plans_summary(self) -> Dict[str, Any]:
        """Get summary of all plans"""
        return {
            "total_plans": len(self.plans),
            "plans": [
                self.get_plan_status(plan.plan_id)
                for plan in self.plans
            ],
            "last_updated": datetime.now().isoformat()
        }


def main():
    """Initialize action plan tracker"""
    tracker = ActionPlanTracker(user_id="jan")
    
    print("\n" + "="*80)
    print("ACTION PLAN TRACKER")
    print("="*80)
    
    summary = tracker.get_all_plans_summary()
    
    print(f"\nTotal Action Plans: {summary['total_plans']}")
    
    for plan_status in summary['plans']:
        print("\n" + "-"*80)
        print(f"Plan: {plan_status['title']}")
        print(f"Status: {plan_status['status']}")
        print(f"Progress: {plan_status['completed_actions']}/{plan_status['total_actions']} actions completed")
        print(f"Completion: {plan_status['completion_percentage']:.1f}%")
        
        for phase in plan_status['phases']:
            print(f"\n  Phase: {phase['title']}")
            print(f"    Status: {phase['status']}")
            print(f"    Progress: {phase['completed_count']}/{phase['actions_count']} actions")
    
    print("\n" + "="*80)
    print("Action plans initialized and ready for tracking.")
    print("="*80)

if __name__ == "__main__":
    standard_main(main, script_name="action_plan_tracker.py")
