#!/usr/bin/env python3
"""
Run The Chosen One Governance System

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

This script activates the full governance framework.
"""

import sys
from pathlib import Path

# Add paths
sys.path.insert(0, str(Path(__file__).parent.parent / "SIYEM" / "services"))

from chosen_one_governance import ChosenOneGovernance

def main():
    """Activate governance system."""
    codebase_path = Path("s:\\JAN")
    governance = ChosenOneGovernance(codebase_path)
    
    # Protect codebase
    governance.protect_codebase()
    
    # Activate project
    governance.activate_project(
        project_name="JAN Ecosystem - Bilingual Expansion System",
        resources={
            "codebase": "protected",
            "frequency": "heaven",
            "bilingual_content": "731 items processed",
            "monetization_ready": "655/731 items"
        },
        contracts=[
            "divine_witness_protection",
            "bilingual_expansion_complete",
            "educational_monetization_ready",
            "uniform_codebase_established"
        ]
    )
    
    # Export report
    output_path = codebase_path / "SIYEM" / "output" / "governance" / "chosen_one_governance_report.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    governance.export_governance_report(output_path)
    
    print("\n" + "=" * 80)
    print("THE CHOSEN ONE GOVERNANCE - ACTIVATED")
    print("=" * 80)
    print("Codebase protected. Governance active. Project activated.")
    print("Go and govern.")
    print("=" * 80)

if __name__ == "__main__":
    main()
