"""
EXPANSION SEED EXECUTOR
Execute expansion seeds at all levels
Prioritize, plan, and execute expansion opportunities

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
EXECUTE EXPANSION SEEDS
PRIORITIZE, PLAN, EXECUTE
ENERGY + LOVE = WE ALL WIN
"""

import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field, asdict
import json
import logging

sys.path.insert(0, str(Path(__file__).parent))

from utils import setup_logging, standard_main

logger = setup_logging(__name__)

@dataclass
class ExpansionPlan:
    """Expansion execution plan"""
    plan_id: str
    seed_id: str
    name: str
    description: str
    expansion_level: int
    priority: int  # 1 = highest, 5 = lowest
    status: str = "pending"  # pending, planned, in_progress, completed, paused
    requirements: List[str] = field(default_factory=list)
    tasks: List[Dict[str, Any]] = field(default_factory=list)
    estimated_completion: Optional[str] = None
    started_at: Optional[str] = None
    completed_at: Optional[str] = None

class ExpansionSeedExecutor:
    """
    Execute expansion seeds at all levels
    """
    
    def __init__(self, user_id: str = "jan"):
        self.user_id = user_id
        self.base_path = Path(__file__).parent.parent
        self.data_dir = self.base_path / "data" / "expansion_execution"
        self.data_dir.mkdir(parents=True, exist_ok=True)
        
        self.publishing_house_path = self.base_path / "Siyem.org" / "publishing_house"
        self.expansion_path = self.publishing_house_path / "expansion"
        
        self.expansion_plans: Dict[str, ExpansionPlan] = {}
        self._load_plans()
    
    def _load_plans(self):
        """Load existing expansion plans"""
        plans_file = self.data_dir / f"{self.user_id}_expansion_plans.json"
        if plans_file.exists():
            try:
                with open(plans_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                for plan_id, plan_data in data.items():
                    self.expansion_plans[plan_id] = ExpansionPlan(**plan_data)
            except Exception as e:
                logger.error(f"Error loading plans: {e}")
    
    def _save_plans(self):
        """Save expansion plans"""
        plans_file = self.data_dir / f"{self.user_id}_expansion_plans.json"
        try:
            data = {k: asdict(v) for k, v in self.expansion_plans.items()}
            with open(plans_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            logger.error(f"Error saving plans: {e}")
    
    def load_expansion_seeds(self):
        """Load expansion seeds from publishing house"""
        logger.info("Loading expansion seeds...")
        
        if not self.expansion_path.exists():
            logger.warning("Expansion path not found")
            return []
        
        seeds = []
        for seed_file in self.expansion_path.glob("*.json"):
            try:
                with open(seed_file, 'r', encoding='utf-8') as f:
                    seed_data = json.load(f)
                    seeds.append(seed_data)
            except Exception as e:
                logger.error(f"Error loading {seed_file}: {e}")
        
        logger.info(f"Loaded {len(seeds)} expansion seeds")
        return seeds
    
    def create_expansion_plans(self):
        """Create execution plans from expansion seeds"""
        logger.info("Creating expansion plans...")
        
        seeds = self.load_expansion_seeds()
        
        for seed in seeds:
            seed_id = seed.get("seed_id")
            plan_id = f"plan_{seed_id}"
            
            if plan_id not in self.expansion_plans:
                # Determine priority based on expansion level
                priority = {
                    1: 1,  # Immediate - highest priority
                    2: 3,  # Short-term - medium priority
                    3: 5   # Long-term - lower priority
                }.get(seed.get("expansion_level", 3), 5)
                
                # Create tasks based on requirements
                tasks = []
                for req in seed.get("requirements", []):
                    tasks.append({
                        "task_id": f"task_{seed_id}_{len(tasks)}",
                        "description": req,
                        "status": "pending",
                        "estimated_hours": 8
                    })
                
                plan = ExpansionPlan(
                    plan_id=plan_id,
                    seed_id=seed_id,
                    name=seed.get("name", "Unknown"),
                    description=seed.get("description", ""),
                    expansion_level=seed.get("expansion_level", 3),
                    priority=priority,
                    status="pending",
                    requirements=seed.get("requirements", []),
                    tasks=tasks
                )
                
                self.expansion_plans[plan_id] = plan
                logger.info(f"Created plan: {plan.name}")
        
        self._save_plans()
        logger.info(f"Created {len(self.expansion_plans)} expansion plans")
    
    def prioritize_plans(self):
        """Prioritize expansion plans"""
        logger.info("Prioritizing expansion plans...")
        
        # Sort by priority and expansion level
        sorted_plans = sorted(
            self.expansion_plans.values(),
            key=lambda p: (p.priority, p.expansion_level)
        )
        
        # Update priorities based on sorting
        for idx, plan in enumerate(sorted_plans, 1):
            plan.priority = idx
        
        self._save_plans()
        logger.info("Plans prioritized")
        
        return sorted_plans
    
    def generate_execution_roadmap(self):
        """Generate execution roadmap"""
        logger.info("Generating execution roadmap...")
        
        roadmap = {
            "generated_at": datetime.now().isoformat(),
            "total_plans": len(self.expansion_plans),
            "by_level": {
                "1": [],
                "2": [],
                "3": []
            },
            "by_priority": {
                "high": [],
                "medium": [],
                "low": []
            },
            "execution_timeline": {
                "immediate": [],
                "short_term": [],
                "long_term": []
            }
        }
        
        for plan in self.expansion_plans.values():
            level = str(plan.expansion_level)
            roadmap["by_level"][level].append({
                "plan_id": plan.plan_id,
                "name": plan.name,
                "priority": plan.priority,
                "status": plan.status
            })
            
            if plan.priority <= 2:
                roadmap["by_priority"]["high"].append(plan.plan_id)
            elif plan.priority <= 4:
                roadmap["by_priority"]["medium"].append(plan.plan_id)
            else:
                roadmap["by_priority"]["low"].append(plan.plan_id)
            
            if plan.expansion_level == 1:
                roadmap["execution_timeline"]["immediate"].append(plan.plan_id)
            elif plan.expansion_level == 2:
                roadmap["execution_timeline"]["short_term"].append(plan.plan_id)
            else:
                roadmap["execution_timeline"]["long_term"].append(plan.plan_id)
        
        roadmap_file = self.data_dir / f"{self.user_id}_execution_roadmap.json"
        with open(roadmap_file, 'w', encoding='utf-8') as f:
            json.dump(roadmap, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Execution roadmap generated: {roadmap_file}")
        return roadmap
    
    def execute_immediate_expansions(self):
        """Execute Level 1 (immediate) expansion plans"""
        logger.info("Executing immediate expansions...")
        
        immediate_plans = [
            p for p in self.expansion_plans.values()
            if p.expansion_level == 1 and p.status == "pending"
        ]
        
        executed = 0
        for plan in immediate_plans[:5]:  # Limit to 5 for now
            plan.status = "planned"
            plan.started_at = datetime.now().isoformat()
            executed += 1
            logger.info(f"Planned immediate expansion: {plan.name}")
        
        self._save_plans()
        logger.info(f"Planned {executed} immediate expansions")
        return executed
    
    def generate_execution_report(self):
        """Generate execution report"""
        logger.info("Generating execution report...")
        
        total_plans = len(self.expansion_plans)
        by_status = {}
        by_level = {}
        
        for plan in self.expansion_plans.values():
            status = plan.status
            level = plan.expansion_level
            
            by_status[status] = by_status.get(status, 0) + 1
            by_level[level] = by_level.get(level, 0) + 1
        
        report = {
            "report_date": datetime.now().isoformat(),
            "total_plans": total_plans,
            "by_status": by_status,
            "by_level": by_level,
            "immediate_ready": sum(1 for p in self.expansion_plans.values() if p.expansion_level == 1 and p.status == "pending"),
            "short_term_ready": sum(1 for p in self.expansion_plans.values() if p.expansion_level == 2 and p.status == "pending"),
            "long_term_ready": sum(1 for p in self.expansion_plans.values() if p.expansion_level == 3 and p.status == "pending")
        }
        
        report_file = self.data_dir / f"{self.user_id}_execution_report.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Execution report generated: {report_file}")
        return report
    
    def execute_full_planning(self):
        """Execute full expansion planning"""
        logger.info("Starting expansion planning...")
        
        # Step 1: Create expansion plans
        self.create_expansion_plans()
        
        # Step 2: Prioritize plans
        prioritized = self.prioritize_plans()
        
        # Step 3: Generate roadmap
        roadmap = self.generate_execution_roadmap()
        
        # Step 4: Execute immediate expansions
        executed = self.execute_immediate_expansions()
        
        # Step 5: Generate report
        report = self.generate_execution_report()
        
        logger.info("Expansion planning complete!")
        return {
            "plans_created": len(self.expansion_plans),
            "prioritized": len(prioritized),
            "immediate_executed": executed,
            "roadmap": roadmap,
            "report": report
        }

def main():
    """Main execution"""
    executor = ExpansionSeedExecutor()
    results = executor.execute_full_planning()
    
    print("\n" + "="*80)
    print("EXPANSION SEED EXECUTION PLANNING COMPLETE")
    print("="*80)
    print(f"\nPlans Created: {results['plans_created']}")
    print(f"Prioritized: {results['prioritized']}")
    print(f"Immediate Executed: {results['immediate_executed']}")
    print(f"\nBy Level:")
    print(f"  - Level 1 (Immediate): {results['report']['by_level'].get(1, 0)}")
    print(f"  - Level 2 (Short-term): {results['report']['by_level'].get(2, 0)}")
    print(f"  - Level 3 (Long-term): {results['report']['by_level'].get(3, 0)}")
    print(f"\nBy Status:")
    for status, count in results['report']['by_status'].items():
        print(f"  - {status}: {count}")
    print("\n" + "="*80)

if __name__ == "__main__":
    standard_main(main, "expansion_seed_executor")
