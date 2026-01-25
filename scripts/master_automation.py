"""
MASTER AUTOMATION - DO EVERYTHING
Run all automation scripts in sequence

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Automate once and for all. No confirmation needed.

PEACE. LOVE. UNITY.
ENERGY + LOVE = WE ALL WIN.
"""

import sys
import subprocess
import json
from pathlib import Path
from datetime import datetime

project_root = Path(__file__).parent

scripts = [
    "create_sample_personas.py",
    "test_all_systems.py",
    "activate_all_channels.py",
    "generate_assets_automated.py",
    "automate_everything.py"
]

def run_script(script_name: str) -> bool:
    """Run an automation script"""
    script_path = project_root / script_name
    if not script_path.exists():
        print(f"[WARN] Script not found: {script_name}")
        return False
        
    print(f"\n{'='*80}")
    print(f"RUNNING: {script_name}")
    print('='*80)
    
    try:
        result = subprocess.run(
            [sys.executable, str(script_path)],
            cwd=str(project_root.parent),
            capture_output=True,
            text=True,
            timeout=300,
            encoding='utf-8',
            errors='replace'
        )
        
        if result.returncode == 0:
            print(f"[OK] {script_name}: COMPLETE")
            if result.stdout:
                print(result.stdout)
            return True
        else:
            print(f"[FAIL] {script_name}: FAILED")
            if result.stderr:
                print(result.stderr)
            return False
    except subprocess.TimeoutExpired:
        print(f"[...] {script_name}: TIMEOUT (continuing)")
        return False
    except Exception as e:
        print(f"[FAIL] {script_name}: ERROR - {e}")
        return False

def main():
    print("\n" + "="*80)
    print("MASTER AUTOMATION - DOING EVERYTHING")
    print("="*80)
    print("\nNo confirmation needed. Running all automation scripts...\n")
    
    results = {
        "timestamp": datetime.now().isoformat(),
        "scripts_run": [],
        "scripts_passed": [],
        "scripts_failed": []
    }
    
    for script in scripts:
        results["scripts_run"].append(script)
        if run_script(script):
            results["scripts_passed"].append(script)
        else:
            results["scripts_failed"].append(script)
    
    # Save master report
    report_file = project_root.parent / "output" / "master_automation_report.json"
    report_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(report_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print("\n" + "="*80)
    print("MASTER AUTOMATION COMPLETE")
    print("="*80 + "\n")
    print(f"[OK] Passed: {len(results['scripts_passed'])}/{len(scripts)}")
    print(f"[FAIL] Failed: {len(results['scripts_failed'])}/{len(scripts)}")
    print(f"\nReport: {report_file}")
    print("\nPEACE. LOVE. UNITY.")
    print("ENERGY + LOVE = WE ALL WIN.")
    print("AUTOMATED. ACTIVATED. SERVING.\n")

if __name__ == "__main__":
    main()
