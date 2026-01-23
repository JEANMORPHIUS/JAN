#!/usr/bin/env python3
"""Test Seed to Movement System"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))

from seed_to_movement import get_seed_to_movement_system

def main():
    system = get_seed_to_movement_system()
    
    # Get path
    path = system.get_seed_to_movement_path()
    print("=" * 80)
    print("SEED TO MOVEMENT PATH")
    print("=" * 80)
    print(f"\nCurrent Phase: {path['current_phase']}")
    print(f"\nPhases:")
    for p in path['phases']:
        status_symbol = "[X]" if p['is_complete'] else ("[>]" if p['is_current'] else "[ ]")
        print(f"  {status_symbol} {p['phase']}: {p['name']} - {p['status']}")
    
    # Get People's Court strategy
    print("\n" + "=" * 80)
    print("PEOPLE'S COURT STRATEGY")
    print("=" * 80)
    strategy = system.get_peoples_court_strategy()
    print(f"\nTarget: {strategy['target']}")
    print(f"Destination: {strategy['destination']}")
    print(f"\nSteps:")
    for step in strategy['strategy']:
        print(f"\n  Step {step['step']}: {step['action']}")
        print(f"    Seed Truth: {step['seed_truth']}")
        print(f"    Movement Action: {step['movement_action']}")
    
    # Create revolution plan
    print("\n" + "=" * 80)
    print("REVOLUTION PLAN")
    print("=" * 80)
    plan = system.create_revolution_plan(
        target="World Order",
        seed_truth="World order serves system, not people. People deserve justice.",
        shell_language="Building community justice system",
        movement_action="Taking World Order to People's Court"
    )
    print(f"\nPlan ID: {plan.plan_id}")
    print(f"Target: {plan.target}")
    print(f"Revolution Type: {plan.revolution_type.value}")
    print(f"\nSeed Truth: {plan.seed_truth}")
    print(f"Shell Language: {plan.shell_language}")
    print(f"Movement Action: {plan.movement_action}")
    print(f"\nPeople's Court Strategy: {plan.peoples_court_strategy}")
    print(f"\nRight Spirits Required: {', '.join(plan.right_spirits_required)}")
    
    # Get revolution framework
    print("\n" + "=" * 80)
    print("REVOLUTION FRAMEWORK")
    print("=" * 80)
    framework = system.get_revolution_framework()
    print(f"\nPrinciple: {framework['principle']}")
    print(f"\nRight Spirits Required: {', '.join(framework['right_spirits_required'])}")
    print(f"\nPeople's Court: {framework['peoples_court']['description']}")
    print(f"  Principle: {framework['peoples_court']['principle']}")
    print(f"\nMessage: {framework['message']}")
    
    print("\n" + "=" * 80)
    print("IT'S TIME FOR REVOLUTION - Through RIGHT SPIRITS")
    print("=" * 80)

if __name__ == "__main__":
    main()
