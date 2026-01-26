"""Validate Persona Tool

Checks persona completeness and structure.

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
import json
from pathlib import Path
from typing import List, Dict, Any, Tuple

JAN_ROOT = os.getenv("JAN_ROOT", r"S:\JAN")
JAN_ENTITY_BASE = os.path.join(JAN_ROOT, "Siyem.org")

REQUIRED_FILES = [
    "profile.md",
    "creative_rules.md",
]

OPTIONAL_FILES = [
    "prompt_templates/",
    "examples/",
    "README.md",
    "LICENSE",
]


def validate_persona(persona_name: str) -> Tuple[bool, List[str], List[str]]:
    """Validate a persona directory structure."""
    persona_dir = Path(JAN_ENTITY_BASE) / persona_name
    
    if not persona_dir.exists():
        return False, [], [f"Persona directory not found: {persona_dir}"]
    
    errors = []
    warnings = []
    
    # Check required files
    for required_file in REQUIRED_FILES:
        file_path = persona_dir / required_file
        if not file_path.exists():
            errors.append(f"Missing required file: {required_file}")
    
    # Check optional files
    for optional_file in OPTIONAL_FILES:
        file_path = persona_dir / optional_file
        if not file_path.exists():
            warnings.append(f"Optional file/directory not found: {optional_file}")
    
    # Validate profile.md structure
    profile_path = persona_dir / "profile.md"
    if profile_path.exists():
        profile_errors = validate_profile(profile_path)
        errors.extend(profile_errors)
    
    # Validate creative_rules.md
    rules_path = persona_dir / "creative_rules.md"
    if rules_path.exists():
        rules_errors = validate_rules(rules_path)
        errors.extend(rules_errors)
    
    # Check for prompt templates
    templates_dir = persona_dir / "prompt_templates"
    if templates_dir.exists():
        template_files = list(templates_dir.glob("*.md"))
        if not template_files:
            warnings.append("prompt_templates directory exists but is empty")
    
    # Check for examples
    examples_dir = persona_dir / "examples"
    if examples_dir.exists():
        example_files = list(examples_dir.glob("*"))
        if not example_files:
            warnings.append("examples directory exists but is empty")
    
    is_valid = len(errors) == 0
    
    return is_valid, errors, warnings


def validate_profile(profile_path: Path) -> List[str]:
    """Validate profile.md structure."""
    errors = []
    content = profile_path.read_text(encoding='utf-8')
    
    # Check for required sections
    required_sections = [
        "## Entity Identity",
        "### Name",
        "### Role",
        "### Purpose",
    ]
    
    for section in required_sections:
        if section not in content:
            errors.append(f"profile.md missing section: {section}")
    
    return errors


def validate_rules(rules_path: Path) -> List[str]:
    """Validate creative_rules.md structure."""
    errors = []
    content = rules_path.read_text(encoding='utf-8')
    
    # Check for at least one section
    if not content.strip():
        errors.append("creative_rules.md is empty")
    
    # Check for common sections (optional but recommended)
    recommended_sections = [
        "## Core Principles",
        "## Voice Requirements",
    ]
    
    # These are warnings, not errors, so we don't add them here
    
    return errors


def validate_package(package_path: str) -> Tuple[bool, List[str], List[str]]:
    """Validate a .janpkg file."""
    import zipfile
    import json
    
    errors = []
    warnings = []
    
    zip_path = Path(package_path)
    if not zip_path.exists():
        return False, [f"Package file not found: {package_path}"], []
    
    try:
        with zipfile.ZipFile(zip_path, 'r') as zipf:
            files = zipf.namelist()
            
            # Check for manifest
            if "manifest.json" not in files:
                errors.append("Missing manifest.json")
                return False, errors, warnings
            
            # Validate manifest
            try:
                manifest_str = zipf.read("manifest.json").decode('utf-8')
                manifest = json.loads(manifest_str)
                
                required_fields = ["format_version", "persona_name", "version", "author"]
                for field in required_fields:
                    if field not in manifest:
                        errors.append(f"Missing required field in manifest: {field}")
            except json.JSONDecodeError:
                errors.append("Invalid JSON in manifest.json")
            except Exception as e:
                errors.append(f"Error reading manifest: {str(e)}")
            
            # Check for JAN files
            jan_files = [f for f in files if f.startswith("jan/") and f.endswith(".md")]
            if not jan_files:
                errors.append("No JAN markdown files found")
            
            # Check for required files
            required_in_package = ["jan/profile.md", "jan/creative_rules.md"]
            for required in required_in_package:
                if required not in files:
                    errors.append(f"Missing required file in package: {required}")
            
            # Check for README
            if "README.md" not in files:
                warnings.append("No README.md in package")
            
            # Check for LICENSE
            if "LICENSE" not in files:
                warnings.append("No LICENSE file in package")
    
    except zipfile.BadZipFile:
        errors.append("Invalid ZIP file")
    except Exception as e:
        errors.append(f"Error reading package: {str(e)}")
    
    is_valid = len(errors) == 0
    
    return is_valid, errors, warnings


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: validate_persona.py <persona_name_or_package>")
        sys.exit(1)
    
    target = sys.argv[1]
    
    # Check if it's a package file
    if target.endswith(".janpkg"):
        is_valid, errors, warnings = validate_package(target)
    else:
        is_valid, errors, warnings = validate_persona(target)
    
    if is_valid:
        print("✅ Persona is valid")
        if warnings:
            print("\n⚠️  Warnings:")
            for warning in warnings:
                print(f"  - {warning}")
    else:
        print("❌ Persona validation failed")
        print("\nErrors:")
        for error in errors:
            print(f"  - {error}")
        if warnings:
            print("\n⚠️  Warnings:")
            for warning in warnings:
                print(f"  - {warning}")
        sys.exit(1)

