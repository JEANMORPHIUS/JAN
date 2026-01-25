"""
CREATE SAMPLE PERSONAS - AUTOMATED
Create sample personas for testing and demonstration

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Create personas. Enable content generation.

PEACE. LOVE. UNITY.
"""

import sys
import requests
import json
from pathlib import Path
from datetime import datetime

project_root = Path(__file__).parent.parent
backend_url = "http://localhost:8000"

personas = [
    {
        "name": "storyteller",
        "description": "Creative storytelling persona for narratives and fiction"
    },
    {
        "name": "educator",
        "description": "Educational content creator for teaching and learning"
    },
    {
        "name": "motivator",
        "description": "Motivational content generator for inspiration"
    },
    {
        "name": "technical-writer",
        "description": "Technical documentation and explanation specialist"
    },
    {
        "name": "poet",
        "description": "Poetry and lyrical content creator"
    }
]

def create_persona(persona_data: dict) -> bool:
    """Create a persona via API"""
    try:
        response = requests.post(
            f"{backend_url}/api/jan/personas",
            json={"name": persona_data["name"]},
            timeout=10
        )
        return response.status_code in [200, 201]
    except:
        return False

def main():
    print("\n" + "="*80)
    print("CREATING SAMPLE PERSONAS")
    print("="*80 + "\n")
    
    created = []
    failed = []
    
    for persona in personas:
        print(f"[...] Creating: {persona['name']}")
        if create_persona(persona):
            print(f"[OK] Created: {persona['name']}")
            created.append(persona['name'])
        else:
            print(f"[FAIL] Failed: {persona['name']}")
            failed.append(persona['name'])
    
    # Save report
    report = {
        "timestamp": datetime.now().isoformat(),
        "created": created,
        "failed": failed,
        "total": len(personas)
    }
    
    report_file = project_root / "output" / "persona_creation_report.json"
    report_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    print("\n" + "="*80)
    print("PERSONA CREATION COMPLETE")
    print("="*80 + "\n")
    print(f"[OK] Created: {len(created)} personas")
    if failed:
        print(f"[FAIL] Failed: {len(failed)} personas")
    print(f"\nReport: {report_file}\n")

if __name__ == "__main__":
    main()
