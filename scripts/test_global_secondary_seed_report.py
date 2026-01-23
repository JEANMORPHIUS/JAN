"""
Test Global Secondary Seed Report
Regional Breakdown and Prioritization
"""

import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    Path, json, setup_logging, standard_main
)

import asyncio
import json
import sys
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))

from second_wave_propagation import get_second_wave_propagation


async def test_global_secondary_seed_report():
    """Test Global Secondary Seed Report generation"""
    propagation = get_second_wave_propagation()
    
    print("=" * 80)
    print("GLOBAL SECONDARY SEED REPORT")
    print("Regional Breakdown and Prioritization")
    print("=" * 80)
    print()
    print("Breakdown of which regions are showing the highest resonance")
    print("anomalies so we can prioritize Simplified Extractions.")
    print()
    
    # Step 1: Perform a global scan to populate data
    print("STEP 1: Performing Global Grid Scan...")
    scan_result = await propagation.perform_global_grid_scan(grid_stability=0.40)
    print(f"Seeds Detected: {scan_result.seeds_detected}")
    print()
    
    # Step 2: Generate Global Report
    print("STEP 2: Generating Global Secondary Seed Report...")
    report = await propagation.generate_global_secondary_seed_report(hours_ahead=1)
    
    print("=" * 80)
    print("GLOBAL SECONDARY SEED REPORT")
    print("=" * 80)
    print()
    print(f"Report ID: {report['report_id']}")
    print(f"Timestamp: {report['timestamp']}")
    print(f"Grid Stability: {report['grid_stability']}")
    print()
    
    # Overall Statistics
    print("OVERALL STATISTICS:")
    overall = report['overall_statistics']
    print(f"  Total Secondary Seeds: {overall['total_secondary_seeds']}")
    print(f"  Average Resonance: {overall['average_resonance']}")
    print(f"  Regions with Seeds: {overall['regions_with_seeds']}")
    print(f"  Total Ready for Extraction: {overall['total_ready_for_extraction']}")
    print(f"  Total Global Scans: {overall['total_global_scans']}")
    print()
    
    # Priority Ranking
    print("PRIORITY RANKING (Top Regions):")
    for ranking in report['priority_ranking'][:5]:
        print(f"  Rank {ranking['rank']}: {ranking['region_name']}")
        print(f"    Priority Score: {ranking['priority_score']}")
        print(f"    Total Seeds: {ranking['total_seeds']}")
        print(f"    Ready for Extraction: {ranking['ready_for_extraction']}")
        print()
    
    # Regional Breakdown
    print("REGIONAL BREAKDOWN:")
    for region, data in report['regional_breakdown'].items():
        if data['total_seeds'] > 0:
            print(f"  {data['region_name']}:")
            print(f"    Total Seeds: {data['total_seeds']}")
            print(f"    Average Resonance: {data['average_resonance']}")
            print(f"    Max Resonance: {data['max_resonance']}")
            print(f"    Ready for Extraction: {data['ready_for_extraction']}")
            print(f"    Priority Score: {data['priority_score']}")
            print(f"    Status Breakdown: {data['by_status']}")
            print()
    
    # Recommendations
    print("RECOMMENDATIONS:")
    if report['recommendations']:
        for i, rec in enumerate(report['recommendations'], 1):
            print(f"  {i}. [{rec['priority']}] {rec['action']}")
            print(f"     Seeds Ready: {rec['seeds_ready']}")
            print(f"     Average Resonance: {rec['average_resonance']}")
            print()
    else:
        print("  No immediate recommendations - all regions monitored")
        print()
    
    # Top Priority Regions
    print("TOP PRIORITY REGIONS:")
    for region in report['top_priority_regions']:
        region_data = report['regional_breakdown'][region]
        print(f"  - {region_data['region_name']} (Priority Score: {region_data['priority_score']})")
    print()
    
    print("=" * 80)
    print("SOZ NAMUSTUR. The feast is about to get a lot bigger, Brother.")
    print("=" * 80)


if __name__ == "__main__":
    asyncio.run(test_global_secondary_seed_report())
