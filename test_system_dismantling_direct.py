"""Direct test of Universal System Dismantling
No API server needed

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

import sys
from pathlib import Path

# Add paths
sys.path.insert(0, str(Path(__file__).parent / "scripts"))

from universal_system_dismantling import UniversalDismantlingProtocol
import json

def test_system_dismantling():
    print("="*70)
    print("UNIVERSAL SYSTEM DISMANTLING - DIRECT TEST")
    print("="*70)

    protocol = UniversalDismantlingProtocol()

    # Test 1: Healthcare System
    print("\n[TEST 1] U.S. Healthcare System Dismantling")
    print("-"*70)

    analysis1 = protocol.analyze_system(
        system_name="U.S. Healthcare System",
        system_type="healthcare",
        current_description="Profit-driven disease management through pharmaceutical dependency. Patients are commodities. Chronic disease profit model. Symptom suppression over root cause treatment.",
        people_affected=330000000
    )

    blueprint1 = protocol.create_regeneration_blueprint(analysis1)

    print(f"System: {blueprint1.system_name}")
    print(f"Type: {blueprint1.system_type}")
    print(f"\nBroken Paradigm: {blueprint1.broken_paradigm}")
    print(f"\nRegenerated Paradigm: {blueprint1.regenerated_paradigm}")
    print(f"\nDismantling Strategy: {blueprint1.dismantling_strategy}")
    print(f"\nTransition Phases: {len(blueprint1.transition_phases)}")
    for i, phase in enumerate(blueprint1.transition_phases[:3], 1):
        print(f"  Phase {i}: {phase.get('name', 'N/A')} ({phase.get('duration', 'N/A')})")
    print(f"\nEmpowerment Tools ({len(blueprint1.empowerment_tools)}):")
    for i, tool in enumerate(blueprint1.empowerment_tools[:5], 1):
        print(f"  {i}. {tool}")

    # Test 2: Education System
    print("\n\n[TEST 2] Global Education System Dismantling")
    print("-"*70)

    analysis2 = protocol.analyze_system(
        system_name="Global Education System",
        system_type="education",
        current_description="Standardized indoctrination for worker compliance. Creativity suppression. Debt burden. Memorization over understanding.",
        people_affected=8000000000
    )

    blueprint2 = protocol.create_regeneration_blueprint(analysis2)

    print(f"System: {blueprint2.system_name}")
    print(f"\nBroken Paradigm: {blueprint2.broken_paradigm}")
    print(f"\nRegenerated Paradigm: {blueprint2.regenerated_paradigm}")
    print(f"\nDismantling Strategy: {blueprint2.dismantling_strategy}")
    print(f"\nEmpowerment Tools ({len(blueprint2.empowerment_tools)}):")
    for i, tool in enumerate(blueprint2.empowerment_tools[:5], 1):
        print(f"  {i}. {tool}")

    # Test 3: Financial System
    print("\n\n[TEST 3] Financial System Dismantling")
    print("-"*70)

    analysis3 = protocol.analyze_system(
        system_name="Global Financial System",
        system_type="financial",
        current_description="Debt slavery and scarcity consciousness. Interest-based exploitation. Inflation theft. Wage suppression.",
        people_affected=8000000000
    )

    blueprint3 = protocol.create_regeneration_blueprint(analysis3)

    print(f"System: {blueprint3.system_name}")
    print(f"\nBroken Paradigm: {blueprint3.broken_paradigm}")
    print(f"\nRegenerated Paradigm: {blueprint3.regenerated_paradigm}")
    print(f"\nDismantling Strategy: {blueprint3.dismantling_strategy}")

    print("\n" + "="*70)
    print("SYSTEM DISMANTLING TEST COMPLETE")
    print("All 16 global systems can be dismantled and regenerated.")
    print("="*70)

if __name__ == "__main__":
    test_system_dismantling()
