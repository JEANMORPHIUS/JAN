"""
Ensure All Entities Are Accessible as Personas
Creates persona directories for all 11 entities if they don't exist.

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
THE REST IS UP TO BABA X.
"""

import json
import os
from pathlib import Path
from typing import Dict, Any

# Paths
SCRIPT_DIR = Path(__file__).parent.parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
JAN_ROOT = os.getenv("JAN_ROOT", str(PROJECT_ROOT / "jan-studio" / "backend" / "jan"))
JAN_ENTITY_BASE = Path(JAN_ROOT) / "Siyem.org"
ENTITIES_FILE = PROJECT_ROOT / "data" / "monetization_alignment" / "jan_entities.json"

# Entity type descriptions
ENTITY_TYPE_DESCRIPTIONS = {
    "creative_persona": "Creative Persona",
    "business_project": "Business Project",
    "governance": "Governance",
    "system": "System"
}


def load_entities() -> list[Dict[str, Any]]:
    """Load entities from jan_entities.json"""
    if not ENTITIES_FILE.exists():
        print(f"Warning: Entities file not found at {ENTITIES_FILE}")
        return []
    
    with open(ENTITIES_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data.get('entities', [])


def create_persona_directory(entity: Dict[str, Any]) -> bool:
    """Create persona directory and default files for an entity"""
    entity_name = entity.get('name', '')
    if not entity_name:
        return False
    
    # Create persona directory
    persona_dir = JAN_ENTITY_BASE / entity_name
    persona_dir.mkdir(parents=True, exist_ok=True)
    
    # Create profile.md if it doesn't exist
    profile_path = persona_dir / "profile.md"
    if not profile_path.exists():
        entity_type = entity.get('entity_type', '')
        description = entity.get('description', '')
        channels = entity.get('channels', [])
        
        profile_content = f"""# {entity_name}: Entity Profile

## Entity Identity

### Name
**{entity_name}**

### Type
{ENTITY_TYPE_DESCRIPTIONS.get(entity_type, entity_type.title())}

### Description
{description}

### Channels
{', '.join(channels) if channels else 'N/A'}

## Core Functions

[Define core functions based on entity type and channels]

## Specialization

{description}

## Voice

[Define voice characteristics]

## Constraints

[Define constraints and boundaries]

## Monetization Opportunities

{', '.join(entity.get('monetization_opportunities', [])) if entity.get('monetization_opportunities') else 'N/A'}

## Alignment Score

{entity.get('alignment_score', 'N/A')}

## Revenue Potential

${entity.get('revenue_potential', 0):,.0f} if entity.get('revenue_potential') else 'N/A'
"""
        profile_path.write_text(profile_content, encoding='utf-8')
        print(f"[OK] Created profile.md for {entity_name}")
    
    # Create creative_rules.md if it doesn't exist
    rules_path = persona_dir / "creative_rules.md"
    if not rules_path.exists():
        rules_content = f"""# {entity_name}: Creative Rules

## Core Principles

- Align with The One Truth
- Pangea is The Table
- Peace is The Truth
- Purpose not Performance

## Voice Requirements

[Define voice requirements for {entity_name}]

## Prohibited Content

- Content that betrays The Table
- Content that promotes separation over unity
- Content that violates core principles

## Required Elements

- Alignment with entity purpose
- Respect for The Table
- Authentic expression

## Entity-Specific Rules

[Add entity-specific creative rules here]
"""
        rules_path.write_text(rules_content, encoding='utf-8')
        print(f"[OK] Created creative_rules.md for {entity_name}")
    
    return True


def main():
    """Main function to ensure all entities are accessible as personas"""
    print("=" * 60)
    print("ENSURING ALL ENTITIES ARE ACCESSIBLE AS PERSONAS")
    print("=" * 60)
    print(f"\nJAN Entity Base: {JAN_ENTITY_BASE}")
    print(f"Entities File: {ENTITIES_FILE}\n")
    
    # Ensure base directory exists
    JAN_ENTITY_BASE.mkdir(parents=True, exist_ok=True)
    
    # Load entities
    entities = load_entities()
    if not entities:
        print("[ERROR] No entities found. Exiting.")
        return
    
    print(f"Found {len(entities)} entities\n")
    
    # Entity name mappings (entity name -> directory name)
    # Some entities exist with different directory names
    entity_name_mappings = {
        "Jean Morphius": "jean_mahram",
        "Karasahin (JK)": "jk",
        "Pierre Pressure": "pierre_pressure",
        "Uncle Ray Ramiz": "uncle_ray_ramiz",
        "Siyem Media": "siyem_media",
        "Edible London": "edible_london",
        "Ilven Seamoss": "ilven_seamoss",
        "Edible Cyprus": "edible_cyprus",
        "ATILOK LTD": "atilok_ltd",
        "Siyem.org": "siyem_org",
        "JAN Studio": "jan_studio"
    }
    
    # Create personas for each entity
    created = 0
    existing = 0
    
    for entity in entities:
        entity_name = entity.get('name', '')
        # Use mapped directory name if available, otherwise use entity name
        dir_name = entity_name_mappings.get(entity_name, entity_name.lower().replace(' ', '_').replace('(', '').replace(')', ''))
        persona_dir = JAN_ENTITY_BASE / dir_name
        
        if persona_dir.exists():
            print(f"[SKIP] {entity_name} ({dir_name}) - Already exists")
            existing += 1
        else:
            # Update entity name for directory creation
            entity_copy = entity.copy()
            entity_copy['name'] = dir_name
            if create_persona_directory(entity_copy):
                created += 1
                print(f"[OK] {entity_name} ({dir_name}) - Created")
            else:
                print(f"[ERROR] {entity_name} ({dir_name}) - Failed to create")
    
    print("\n" + "=" * 60)
    print(f"SUMMARY: {created} created, {existing} already existed")
    print(f"Total: {len(entities)} entities")
    print("=" * 60)
    
    # List all personas now available
    print("\n[LIST] Available Personas:")
    personas = sorted([d.name for d in JAN_ENTITY_BASE.iterdir() if d.is_dir() and not d.name.startswith('.')])
    for i, persona in enumerate(personas, 1):
        print(f"  {i}. {persona}")
    
    print(f"\n[OK] All entities are now accessible as personas in Creation Centre!")


if __name__ == "__main__":
    main()
