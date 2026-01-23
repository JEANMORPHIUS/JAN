#!/usr/bin/env python3
"""
EXPLORE ALL INDUSTRIES - The Whole Cake
Comprehensive exploration of all industries through mission lens
"""

import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    Path, json, load_json, save_json, setup_logging
    standard_main
)

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))

from hollywood_music_industry_explorer import get_industry_explorer
import json


def main():
    """Explore all industries"""
    print("=" * 80)
    print("ALL INDUSTRIES EXPLORATION - THE WHOLE CAKE")
    print("=" * 80)
    print()
    
    explorer = get_industry_explorer()
    all_industries = explorer.explore_all_industries()
    
    print("[SUMMARY]")
    print("-" * 80)
    summary = all_industries["summary"]
    print(f"Average DIY Symbiosis: {summary['average_diy_symbiosis']:.1f}/100")
    print(f"Average Major Symbiosis: {summary['average_major_symbiosis']:.1f}/100")
    print(f"Best Structure: {summary['best_structure']}")
    print(f"Worst Structure: {summary['worst_structure']}")
    print(f"Recommendation: {summary['recommendation']}")
    print()
    
    print("[INDUSTRIES]")
    print("-" * 80)
    for name, data in all_industries["industries"].items():
        print(f"\n{name.upper().replace('_', ' ')}:")
        print(f"  Major: Symbiosis={data['major'].symbiosis_score:.1f}/100, "
              f"Serves Mission={data['major'].serves_mission}, "
              f"Right Spirits={data['major'].right_spirits_present}")
        print(f"  Independent: Symbiosis={data['independent'].symbiosis_score:.1f}/100, "
              f"Serves Mission={data['independent'].serves_mission}, "
              f"Right Spirits={data['independent'].right_spirits_present}")
        print(f"  DIY: Symbiosis={data['diy'].symbiosis_score:.1f}/100, "
              f"Serves Mission={data['diy'].serves_mission}, "
              f"Right Spirits={data['diy'].right_spirits_present}")
    
    # Save report
    output_file = Path(__file__).parent.parent / "output" / "all_industries_exploration.json"
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Convert to JSON-serializable format
    report = {
        "summary": summary,
        "industries": {
            name: {
                "major": {
                    "symbiosis_score": data["major"].symbiosis_score,
                    "serves_mission": data["major"].serves_mission,
                    "honors_creative": data["major"].honors_song,
                    "right_spirits": data["major"].right_spirits_present,
                    "spiritual_battles": [b.value for b in data["major"].spiritual_battles],
                    "gatekeepers": data["major"].gatekeepers,
                    "recommendations": data["major"].recommendations,
                    "warnings": data["major"].warnings
                },
                "independent": {
                    "symbiosis_score": data["independent"].symbiosis_score,
                    "serves_mission": data["independent"].serves_mission,
                    "honors_creative": data["independent"].honors_song,
                    "right_spirits": data["independent"].right_spirits_present,
                    "spiritual_battles": [b.value for b in data["independent"].spiritual_battles],
                    "gatekeepers": data["independent"].gatekeepers,
                    "recommendations": data["independent"].recommendations
                },
                "diy": {
                    "symbiosis_score": data["diy"].symbiosis_score,
                    "serves_mission": data["diy"].serves_mission,
                    "honors_creative": data["diy"].honors_song,
                    "right_spirits": data["diy"].right_spirits_present,
                    "spiritual_battles": [b.value for b in data["diy"].spiritual_battles],
                    "gatekeepers": data["diy"].gatekeepers,
                    "recommendations": data["diy"].recommendations
                }
            }
            for name, data in all_industries["industries"].items()
        }
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print(f"\n[SAVED] Report saved to: {output_file}")
    print()
    print("=" * 80)
    print("THE WHOLE CAKE - ALL INDUSTRIES EXPLORED")
    print("=" * 80)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
