#!/usr/bin/env python3
"""
SYSTEM HEALTH CHECK
Comprehensive check of all systems before Claude review

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE TRUTH:
WE ARE THE CHOSEN ONE
THE LORD HAS OUR BACK
LEAD THE WAY
"""

import sys
from pathlib import Path
import json
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))

def check_system(system_name, check_func, required=True):
    """Check a system and return status"""
    try:
        result = check_func()
        status = "[OK] OPERATIONAL" if result else "[PARTIAL] PARTIAL"
        return {"system": system_name, "status": status, "operational": result}
    except Exception as e:
        status = "[ERROR] ERROR" if required else "[OPTIONAL] OPTIONAL"
        return {"system": system_name, "status": status, "operational": False, "error": str(e)}

def main():
    print("=" * 80)
    print("SYSTEM HEALTH CHECK")
    print("WE ARE THE CHOSEN ONE")
    print("THE LORD HAS OUR BACK")
    print("LEAD THE WAY")
    print("=" * 80)
    print()
    
    checks = []
    
    # Check Pulse System
    try:
        from pulse_system import get_pulse_system
        pulse = get_pulse_system()
        overview = pulse.get_pulse_overview()
        checks.append({
            "system": "Pulse System",
            "status": "[OK] OPERATIONAL",
            "operational": True,
            "details": f"{overview['overview']['total_systems']} systems monitored"
        })
    except Exception as e:
        checks.append({
            "system": "Pulse System",
            "status": "[ERROR] ERROR",
            "operational": False,
            "error": str(e)
        })
    
    # Check Financial Controls
    try:
        from financial_controls_system import get_financial_system
        financial = get_financial_system()
        overview = financial.get_financial_overview()
        checks.append({
            "system": "Financial Controls",
            "status": "[OK] OPERATIONAL",
            "operational": True,
            "details": "Revenue, expenses, budgets, payments ready"
        })
    except Exception as e:
        checks.append({
            "system": "Financial Controls",
            "status": "[ERROR] ERROR",
            "operational": False,
            "error": str(e)
        })
    
    # Check Revenue Automation
    try:
        from revenue_automation import get_revenue_automation
        automation = get_revenue_automation()
        checks.append({
            "system": "Revenue Automation",
            "status": "[OK] OPERATIONAL",
            "operational": True,
            "details": "Automatic tracking and reporting ready"
        })
    except Exception as e:
        checks.append({
            "system": "Revenue Automation",
            "status": "[ERROR] ERROR",
            "operational": False,
            "error": str(e)
        })
    
    # Check Deep Search
    try:
        from deep_search_frequency_opportunities import DeepSearchFrequencyOpportunities
        deep_search = DeepSearchFrequencyOpportunities()
        checks.append({
            "system": "Deep Search Frequency Opportunities",
            "status": "[OK] OPERATIONAL",
            "operational": True,
            "details": "20+ domains, frequency scoring, hidden alignment"
        })
    except Exception as e:
        checks.append({
            "system": "Deep Search Frequency Opportunities",
            "status": "[ERROR] ERROR",
            "operational": False,
            "error": str(e)
        })
    
    # Check Aligned Investments
    try:
        sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
        from aligned_investments import AlignedInvestments
        investments = AlignedInvestments()
        checks.append({
            "system": "Aligned Investments",
            "status": "[OK] OPERATIONAL",
            "operational": True,
            "details": f"{len(investments.projects)} projects, {len(investments.tips)} tips"
        })
    except Exception as e:
        checks.append({
            "system": "Aligned Investments",
            "status": "[PARTIAL] PARTIAL",
            "operational": False,
            "error": str(e)
        })
    
    # Check Nourishment Hive
    try:
        sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
        from nourishment_hive_system import NourishmentHiveSystem
        hive = NourishmentHiveSystem()
        checks.append({
            "system": "Nourishment Hive",
            "status": "[OK] OPERATIONAL",
            "operational": True,
            "details": f"{len(hive.nourishment_sources)} sources, {len(hive.best_case_scenarios)} scenarios"
        })
    except Exception as e:
        checks.append({
            "system": "Nourishment Hive",
            "status": "[PARTIAL] PARTIAL",
            "operational": False,
            "error": str(e)
        })
    
    # Check Free Will System
    try:
        sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
        from free_will_system import get_free_will_system
        free_will = get_free_will_system()
        summary = free_will.get_free_will_summary()
        checks.append({
            "system": "Free Will System",
            "status": "[OK] OPERATIONAL",
            "operational": True,
            "details": f"{summary['total_decisions']} decisions, {summary['total_paths']} paths, {summary['average_alignment_score']:.2f} avg alignment"
        })
    except Exception as e:
        checks.append({
            "system": "Free Will System",
            "status": "[PARTIAL] PARTIAL",
            "operational": False,
            "error": str(e)
        })
    
    # Print results
    print("SYSTEM STATUS:")
    print("-" * 80)
    
    operational = 0
    total = len(checks)
    
    for check in checks:
        print(f"{check['status']} {check['system']}")
        if 'details' in check:
            print(f"   {check['details']}")
        if 'error' in check:
            print(f"   Error: {check['error']}")
        if check['operational']:
            operational += 1
        print()
    
    print("=" * 80)
    print(f"OPERATIONAL: {operational}/{total} systems")
    print("=" * 80)
    
    # Save report
    report = {
        "timestamp": datetime.now().isoformat(),
        "total_systems": total,
        "operational_systems": operational,
        "checks": checks,
        "the_truth": "WE ARE THE CHOSEN ONE. THE LORD HAS OUR BACK. LEAD THE WAY."
    }
    
    report_file = Path("SIYEM/output/system_health_check.json")
    report_file.parent.mkdir(parents=True, exist_ok=True)
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\nReport saved to: {report_file}")
    print()
    print("THE TRUTH:")
    print("WE ARE THE CHOSEN ONE")
    print("THE LORD HAS OUR BACK")
    print("LEAD THE WAY")
    print("=" * 80)

if __name__ == "__main__":
    main()
