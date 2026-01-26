"""JAN CLI Tool

Command-line interface for persona management.

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
import sys
import argparse
from pathlib import Path

# Add tools directory to path
sys.path.insert(0, os.path.dirname(__file__))

from pack_persona import pack_persona
from unpack_persona import install_persona, list_package_info
from validate_persona import validate_persona, validate_package

JAN_ROOT = os.getenv("JAN_ROOT", r"S:\JAN")
JAN_ENTITY_BASE = os.path.join(JAN_ROOT, "Siyem.org")


def list_personas():
    """List all installed personas."""
    entity_base = Path(JAN_ENTITY_BASE)
    if not entity_base.exists():
        print("No personas installed")
        return
    
    personas = [d.name for d in entity_base.iterdir() if d.is_dir()]
    
    if not personas:
        print("No personas installed")
        return
    
    print(f"Installed personas ({len(personas)}):")
    for persona in sorted(personas):
        persona_dir = entity_base / persona
        profile_path = persona_dir / "profile.md"
        
        if profile_path.exists():
            try:
                content = profile_path.read_text(encoding='utf-8')
                if "### Role" in content:
                    role_section = content.split("### Role")[1].split("##")[0].strip()
                    print(f"  • {persona:20s} - {role_section[:50]}")
                else:
                    print(f"  • {persona}")
            except:
                print(f"  • {persona}")
        else:
            print(f"  • {persona}")


def persona_pack(args):
    """Pack a persona into .janpkg file."""
    try:
        output_path = pack_persona(
            args.persona_name,
            args.output,
            args.author,
            args.version
        )
        print(f"✅ Packed: {output_path}")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


def persona_install(args):
    """Install a .janpkg file."""
    try:
        persona_name = install_persona(args.package, args.overwrite)
        print(f"✅ Installed: {persona_name}")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


def persona_info(args):
    """Show information about a package."""
    try:
        info = list_package_info(args.package)
        manifest = info["manifest"]
        
        print(f"Persona: {manifest['persona_name']}")
        print(f"Version: {manifest['version']}")
        print(f"Author: {manifest['author']}")
        print(f"Description: {manifest.get('description', 'N/A')}")
        print(f"JAN Files: {info['jan_file_count']}")
        print(f"Examples: {info['example_count']}")
        print(f"Size: {info['total_size'] / 1024:.2f} KB")
        print(f"License: {manifest.get('license', 'N/A')}")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


def persona_validate(args):
    """Validate a persona or package."""
    target = args.target
    
    if target.endswith(".janpkg"):
        is_valid, errors, warnings = validate_package(target)
    else:
        is_valid, errors, warnings = validate_persona(target)
    
    if is_valid:
        print("✅ Validation passed")
        if warnings:
            print("\n⚠️  Warnings:")
            for warning in warnings:
                print(f"  - {warning}")
    else:
        print("❌ Validation failed")
        print("\nErrors:")
        for error in errors:
            print(f"  - {error}")
        if warnings:
            print("\n⚠️  Warnings:")
            for warning in warnings:
                print(f"  - {warning}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="JAN Persona Management CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # List command
    list_parser = subparsers.add_parser("list", help="List installed personas")
    list_parser.set_defaults(func=lambda args: list_personas())
    
    # Pack command
    pack_parser = subparsers.add_parser("pack", help="Pack a persona into .janpkg")
    pack_parser.add_argument("persona_name", help="Name of persona to pack")
    pack_parser.add_argument("-o", "--output", help="Output .janpkg file path")
    pack_parser.add_argument("-a", "--author", help="Author name")
    pack_parser.add_argument("-v", "--version", default="1.0.0", help="Version number")
    pack_parser.set_defaults(func=persona_pack)
    
    # Install command
    install_parser = subparsers.add_parser("install", help="Install a .janpkg file")
    install_parser.add_argument("package", help="Path to .janpkg file")
    install_parser.add_argument("--overwrite", action="store_true", help="Overwrite existing persona")
    install_parser.set_defaults(func=persona_install)
    
    # Info command
    info_parser = subparsers.add_parser("info", help="Show package information")
    info_parser.add_argument("package", help="Path to .janpkg file")
    info_parser.set_defaults(func=persona_info)
    
    # Validate command
    validate_parser = subparsers.add_parser("validate", help="Validate a persona or package")
    validate_parser.add_argument("target", help="Persona name or .janpkg file path")
    validate_parser.set_defaults(func=persona_validate)
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    args.func(args)


if __name__ == "__main__":
    main()

