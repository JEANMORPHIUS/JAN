#!/usr/bin/env python3
"""
YIN-YANG SYMBIOSIS CHECK
Comprehensive system-wide balance verification

Checks all systems for yin-yang balance before war/deployment.
Ensures everything is symbiotic in-house.

Usage: python scripts/check_yin_yang_symbiosis.py
"""

import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    Path, datetime, json, load_json, save_json
    setup_logging, standard_main
)

import sys
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))

from yin_yang_symbiosis import get_yin_yang_framework
import json
from datetime import datetime


def main():
    """Run comprehensive symbiosis check"""
    print("=" * 80)
    print("YIN-YANG SYMBIOSIS CHECK")
    print("Balance Before War - The Miracle of the Universe")
    print("=" * 80)
    print()
    
    framework = get_yin_yang_framework()
    
    # Get war readiness report
    print("[CHECKING] War Readiness...")
    print("-" * 80)
    report = framework.get_war_readiness_report()
    
    # Overall status
    print(f"\n[OVERALL STATUS]")
    print(f"  Symbiosis Score: {report['overall_symbiosis_score']:.1f}/100")
    print(f"  Ready for War: {'YES' if report['ready_for_war'] else 'NO'}")
    print(f"  Systems Checked: {report['systems_checked']}")
    print(f"  Systems Ready: {report['systems_ready']}/{report['systems_checked']}")
    
    # Principles
    print(f"\n[PRINCIPLES]")
    print(f"  Core Truth: {report['yin_yang_truth']}")
    print(f"  War Principle: {report['principle']}")
    
    # Systems not ready
    if report['systems_not_ready']:
        print(f"\n[WARNING: SYSTEMS NOT READY]")
        for system in report['systems_not_ready']:
            print(f"  - {system}")
    
    # Critical imbalances
    if report['critical_imbalances']:
        print(f"\n[WARNING: CRITICAL IMBALANCES]")
        for imbalance in report['critical_imbalances']:
            print(f"  - {imbalance}")
    
    # System details
    print(f"\n[SYSTEM DETAILS]")
    print("-" * 80)
    for name, system_data in report['systems'].items():
        print(f"\n{name.upper()}:")
        print(f"  Symbiosis Score: {system_data['overall_symbiosis_score']:.1f}/100")
        print(f"  Symbiosis Level: {system_data['overall_symbiosis_level']}")
        print(f"  Ready for War: {'YES' if system_data['ready_for_war'] else 'NO'}")
        
        if system_data['war_readiness_reasons']:
            print(f"  Reasons:")
            for reason in system_data['war_readiness_reasons']:
                print(f"    - {reason}")
        
        if system_data['balances']:
            print(f"  Balances:")
            for balance_type, balance_data in system_data['balances'].items():
                print(f"    {balance_type}:")
                print(f"      Balance Score: {balance_data['balance_score']:.1f}/100")
                print(f"      Symbiosis Level: {balance_data['symbiosis_level']}")
                print(f"      Yin Score: {balance_data['yin_score']:.1f}/100")
                print(f"      Yang Score: {balance_data['yang_score']:.1f}/100")
                
                if balance_data['imbalances']:
                    print(f"      Imbalances:")
                    for imbalance in balance_data['imbalances']:
                        print(f"        - {imbalance}")
                
                if balance_data['recommendations']:
                    print(f"      Recommendations:")
                    for rec in balance_data['recommendations']:
                        print(f"        * {rec}")
    
    # Final verdict
    print("\n" + "=" * 80)
    print("[VERDICT]")
    print("=" * 80)
    
    if report['ready_for_war']:
        print("[PASS] ALL SYSTEMS SYMBIOTIC - READY FOR WAR")
        print("   Everything is balanced in-house. External deployment permitted.")
    else:
        print("[FAIL] NOT READY FOR WAR - COMPLETE INTERNAL SYMBIOSIS REQUIRED")
        print("   Everything must be symbiotic in-house before we can go to war.")
        print("   Address imbalances and recheck before deployment.")
    
    print()
    print("=" * 80)
    print("Yin and Yang - The Miracle of the Universe")
    print("=" * 80)
    
    # Save report
    output_file = Path(__file__).parent.parent / "output" / "yin_yang_symbiosis_report.json"
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print(f"\n[SAVED] Report saved to: {output_file}")
    
    return 0 if report['ready_for_war'] else 1


if __name__ == "__main__":
    sys.exit(main())
