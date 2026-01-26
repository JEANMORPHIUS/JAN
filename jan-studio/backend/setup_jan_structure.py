"""Setup JAN Directory Structure

Creates the required JAN directory structure if it doesn't exist.
Run this script once to initialize your JAN directory.

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
THE REST IS UP TO BABA X."""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get JAN root from environment or use default
JAN_ROOT = os.getenv("JAN_ROOT", "./jan")
JAN_ROOT = Path(JAN_ROOT).resolve()

# Required directories
SIYEM_ORG = JAN_ROOT / "Siyem.org"
TEMPLATES_DIR = JAN_ROOT / "templates"
STYLES_DIR = JAN_ROOT / "styles"

def create_jan_structure():
    """Create JAN directory structure."""
    print(f"Creating JAN structure at: {JAN_ROOT}")
    
    # Create base directories
    SIYEM_ORG.mkdir(parents=True, exist_ok=True)
    TEMPLATES_DIR.mkdir(parents=True, exist_ok=True)
    STYLES_DIR.mkdir(parents=True, exist_ok=True)
    
    # Create example persona
    example_persona = SIYEM_ORG / "example-persona"
    example_persona.mkdir(exist_ok=True)
    
    # Create example profile.md
    profile_path = example_persona / "profile.md"
    if not profile_path.exists():
        profile_content = """# Example Persona: Entity Profile

## Entity Identity

### Name
**Example Persona**

### Role
Example role for demonstration

### Purpose
This is an example persona to help you understand the structure.

## Core Functions

- Content generation
- Template management

## Specialization

General purpose example

## Voice

Friendly and helpful

## Constraints

None (example only)
"""
        profile_path.write_text(profile_content, encoding='utf-8')
    
    # Create example creative_rules.md
    rules_path = example_persona / "creative_rules.md"
    if not rules_path.exists():
        rules_content = """# Example Persona: Creative Rules

## Core Principles

- Be helpful
- Be clear
- Be concise

## Voice Requirements

- Friendly tone
- Professional but approachable

## Prohibited Content

None (example only)

## Required Elements

- Clear structure
- Helpful examples
"""
        rules_path.write_text(rules_content, encoding='utf-8')
    
    # Create prompt_templates directory
    templates_dir = example_persona / "prompt_templates"
    templates_dir.mkdir(exist_ok=True)
    
    # Create example template
    template_path = templates_dir / "example_template.md"
    if not template_path.exists():
        template_content = """# Example Template

This is an example prompt template.

## Usage

Use this template to generate content.

## Parameters

- {task}: The task to perform
- {context}: Additional context
"""
        template_path.write_text(template_content, encoding='utf-8')
    
    print(f"✅ JAN structure created successfully!")
    print(f"   Location: {JAN_ROOT}")
    print(f"   Example persona: {example_persona}")
    print(f"\nYou can now create your own personas in: {SIYEM_ORG}")

if __name__ == "__main__":
    create_jan_structure()

