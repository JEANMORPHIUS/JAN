"""
Test Narrative Fracture Report
Generate UN Plaza narrative fracture report
"""

import asyncio
import json
import sys
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))

from big_cheese_audit import get_big_cheese_audit_system


async def test_narrative_fracture_report():
    """Test narrative fracture report generation"""
    system = get_big_cheese_audit_system()
    
    print("=" * 80)
    print("UN PLAZA NARRATIVE FRACTURE REPORT")
    print("=" * 80)
    print()
    
    # Generate report for UN
    report = await system.generate_narrative_fracture_report("UN", include_seeds=True)
    
    print(json.dumps(report, indent=2, default=str))
    print()
    print("=" * 80)
    print("REPORT SUMMARY")
    print("=" * 80)
    print(f"Organization: {report['organization']['name']}")
    print(f"Law 41 Pressure: {report['law_41_pressure']['pressure_level']}%")
    print(f"Severity: {report['law_41_pressure']['severity']}")
    print(f"Narrative Cracks: {len(report['narrative_cracks'])}")
    print(f"Seeds Found: {len(report['seeds_found'])}")
    print()
    print("NARRATIVE CRACKS:")
    for crack in report['narrative_cracks']:
        print(f"  - {crack['fracture_type']}: {crack['description']}")
        print(f"    Severity: {crack['severity']}")
        print(f"    Location: {crack['location']}")
    print()
    print("SHELL ANALYSIS:")
    print(f"  Shell Narrative: {report['shell_analysis']['shell_narrative']}")
    print(f"  Seed Truth: {report['shell_analysis']['seed_truth']}")
    print(f"  Narrative Gap: {report['shell_analysis']['narrative_gap']}")
    print(f"  Thinnest Point: {report['shell_analysis']['thinnest_point']}")
    print()
    print("=" * 80)
    print("SOZ NAMUSTUR. The cracks are showing, twin.")
    print("=" * 80)


if __name__ == "__main__":
    asyncio.run(test_narrative_fracture_report())
