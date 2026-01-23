"""
VERIFY ALL REQUIREMENTS
Interactive script to verify all bureaucratic requirements

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
VERIFY EVERY REQUIREMENT
DOCUMENT EVERY SOURCE
TRACK EVERY LOOPHOLE
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    JAN_DATA, JAN_OUTPUT, get_data_path, get_output_path,
    datetime, json, logging, List, Dict,
    setup_logging, load_json, save_json, standard_main
)

from bureaucratic_verification_system import (
    BureaucraticVerificationSystem, RequirementStatus, LoopholeType
)

logger = setup_logging(__name__)

def verify_all_requirements_interactive(system: BureaucraticVerificationSystem):
    """Interactive verification of all requirements"""
    print("="*80)
    print("REQUIREMENT VERIFICATION")
    print("="*80)
    print("\nThis will guide you through verifying each requirement.")
    print("For each requirement, you'll need to:")
    print("  1. Check official sources")
    print("  2. Verify document requirements")
    print("  3. Confirm costs and processing times")
    print("  4. Identify any loopholes")
    print("\nPress Enter to continue, or 'q' to quit...")
    
    all_requirements = list(system.requirements.values())
    all_requirements.extend(system.visas.values())
    all_requirements.extend(system.civil_registry.values())
    
    verified_count = 0
    
    for req in all_requirements:
        if req.status == RequirementStatus.VERIFIED:
            continue
        
        print("\n" + "-"*80)
        print(f"REQUIREMENT: {req.name}")
        print(f"Type: {getattr(req, 'requirement_type', getattr(req, 'visa_type', getattr(req, 'registry_type', 'N/A')))}")
        print(f"Jurisdiction: {getattr(req, 'jurisdiction', getattr(req, 'country', 'N/A'))}")
        print(f"Status: {req.status.value}")
        print(f"\nDescription: {getattr(req, 'description', 'N/A')}")
        
        if hasattr(req, 'required_documents') and req.required_documents:
            print(f"\nRequired Documents:")
            for doc in req.required_documents:
                print(f"  - {doc}")
        
        print(f"\n[V] Verify | [S] Skip | [L] Add Loophole | [Q] Quit")
        action = input("Action: ").strip().lower()
        
        if action == 'q':
            break
        elif action == 's':
            continue
        elif action == 'v':
            notes = input("Verification notes: ").strip()
            verified_by = input("Verified by: ").strip() or "System"
            
            system.verify_requirement(
                getattr(req, 'requirement_id', getattr(req, 'visa_id', getattr(req, 'registry_id', ''))),
                verified_by=verified_by,
                verification_notes=notes,
                status=RequirementStatus.VERIFIED
            )
            verified_count += 1
            print("✓ Verified")
        elif action == 'l':
            print("\nLoophole Types:")
            for i, loop_type in enumerate(LoopholeType, 1):
                print(f"  {i}. {loop_type.value}")
            
            try:
                choice = int(input("Select type (1-7): ")) - 1
                loop_type = list(LoopholeType)[choice]
                description = input("Description: ").strip()
                legal_status = input("Legal status (Legal/Gray/Illegal): ").strip()
                risk = float(input("Risk level (0.0-1.0): ") or "0.5")
                effectiveness = float(input("Effectiveness (0.0-1.0): ") or "0.5")
                
                loop_id = f"{getattr(req, 'requirement_id', getattr(req, 'visa_id', getattr(req, 'registry_id', '')))}_loophole_{datetime.now().strftime('%Y%m%d%H%M%S')}"
                
                system.add_loophole(
                    loophole_id=loop_id,
                    requirement_id=getattr(req, 'requirement_id', getattr(req, 'visa_id', getattr(req, 'registry_id', ''))),
                    loophole_type=loop_type,
                    description=description,
                    legal_status=legal_status,
                    risk_level=risk,
                    effectiveness=effectiveness
                )
                print("✓ Loophole added")
            except (ValueError, IndexError):
                print("Invalid input, skipping...")
    
    print(f"\n\nVerified {verified_count} requirements")
    print("Verification complete!")


def main():
    """Main function"""
    system = BureaucraticVerificationSystem()
    
    print("="*80)
    print("VERIFY ALL REQUIREMENTS")
    print("="*80)
    
    # Show current status
    report = system.generate_verification_report()
    system.print_report(report)
    
    print("\n" + "="*80)
    print("Starting interactive verification...")
    print("="*80)
    
    verify_all_requirements_interactive(system)
    
    # Generate final report
    final_report = system.generate_verification_report()
    report_file = get_output_path("final_verification_report.json")
    save_json(final_report, report_file)
    
    print(f"\nFinal report saved to: {report_file}")

if __name__ == "__main__":
    standard_main(main, script_name="verify_all_requirements.py")
