"""Unpack Persona Tool

Installs a .janpkg file into the JAN directory structure.

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
import zipfile
import shutil
from pathlib import Path
from typing import Dict, Any

JAN_ROOT = os.getenv("JAN_ROOT", r"S:\JAN")
JAN_ENTITY_BASE = os.path.join(JAN_ROOT, "Siyem.org")


def read_manifest(zip_path: Path) -> Dict[str, Any]:
    """Read manifest.json from package."""
    with zipfile.ZipFile(zip_path, 'r') as zipf:
        manifest_str = zipf.read("manifest.json").decode('utf-8')
        return json.loads(manifest_str)


def validate_package(zip_path: Path) -> tuple[bool, str]:
    """Validate package structure."""
    try:
        with zipfile.ZipFile(zip_path, 'r') as zipf:
            files = zipf.namelist()
            
            # Check for manifest
            if "manifest.json" not in files:
                return False, "Missing manifest.json"
            
            # Read and validate manifest
            manifest_str = zipf.read("manifest.json").decode('utf-8')
            manifest = json.loads(manifest_str)
            
            required_fields = ["format_version", "persona_name", "version", "author"]
            for field in required_fields:
                if field not in manifest:
                    return False, f"Missing required field in manifest: {field}"
            
            # Check for JAN files
            jan_files = [f for f in files if f.startswith("jan/") and f.endswith(".md")]
            if not jan_files:
                return False, "No JAN markdown files found"
            
            return True, "Valid package"
    except zipfile.BadZipFile:
        return False, "Invalid ZIP file"
    except Exception as e:
        return False, f"Error validating package: {str(e)}"


def install_persona(package_path: str, overwrite: bool = False) -> str:
    """Install a .janpkg file."""
    zip_path = Path(package_path)
    
    if not zip_path.exists():
        raise ValueError(f"Package file not found: {package_path}")
    
    # Validate package
    is_valid, message = validate_package(zip_path)
    if not is_valid:
        raise ValueError(f"Invalid package: {message}")
    
    # Read manifest
    manifest = read_manifest(zip_path)
    persona_name = manifest["persona_name"]
    
    # Check if persona already exists
    persona_dir = Path(JAN_ENTITY_BASE) / persona_name
    if persona_dir.exists() and not overwrite:
        raise ValueError(f"Persona '{persona_name}' already exists. Use --overwrite to replace.")
    
    # Create persona directory
    persona_dir.mkdir(parents=True, exist_ok=True)
    
    # Extract files
    with zipfile.ZipFile(zip_path, 'r') as zipf:
        # Extract JAN files
        for file_info in zipf.infolist():
            if file_info.filename.startswith("jan/"):
                # Get relative path within jan/
                relative_path = file_info.filename[4:]  # Remove "jan/" prefix
                target_path = persona_dir / relative_path
                target_path.parent.mkdir(parents=True, exist_ok=True)
                
                # Extract file
                with zipf.open(file_info) as source:
                    target_path.write_bytes(source.read())
        
        # Extract examples
        examples_dir = persona_dir / "examples"
        for file_info in zipf.infolist():
            if file_info.filename.startswith("examples/"):
                relative_path = file_info.filename[10:]  # Remove "examples/" prefix
                target_path = examples_dir / relative_path
                target_path.parent.mkdir(parents=True, exist_ok=True)
                
                with zipf.open(file_info) as source:
                    target_path.write_bytes(source.read())
        
        # Extract README if exists
        if "README.md" in zipf.namelist():
            readme_content = zipf.read("README.md").decode('utf-8')
            (persona_dir / "README.md").write_text(readme_content, encoding='utf-8')
        
        # Extract LICENSE if exists
        if "LICENSE" in zipf.namelist():
            license_content = zipf.read("LICENSE").decode('utf-8')
            (persona_dir / "LICENSE").write_text(license_content, encoding='utf-8')
    
    return persona_name


def list_package_info(package_path: str) -> Dict[str, Any]:
    """List information about a package without installing."""
    zip_path = Path(package_path)
    
    if not zip_path.exists():
        raise ValueError(f"Package file not found: {package_path}")
    
    manifest = read_manifest(zip_path)
    
    with zipfile.ZipFile(zip_path, 'r') as zipf:
        files = zipf.namelist()
        jan_files = [f for f in files if f.startswith("jan/") and f.endswith(".md")]
        example_files = [f for f in files if f.startswith("examples/")]
    
    return {
        "manifest": manifest,
        "jan_file_count": len(jan_files),
        "example_count": len(example_files),
        "total_size": zip_path.stat().st_size
    }


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 3:
        print("Usage: unpack_persona.py <command> <package_path> [--overwrite]")
        print("Commands: install, info")
        sys.exit(1)
    
    command = sys.argv[1]
    package_path = sys.argv[2]
    overwrite = "--overwrite" in sys.argv
    
    try:
        if command == "install":
            persona_name = install_persona(package_path, overwrite)
            print(f"✅ Installed persona: {persona_name}")
        elif command == "info":
            info = list_package_info(package_path)
            manifest = info["manifest"]
            print(f"Persona: {manifest['persona_name']}")
            print(f"Version: {manifest['version']}")
            print(f"Author: {manifest['author']}")
            print(f"Description: {manifest.get('description', 'N/A')}")
            print(f"JAN Files: {info['jan_file_count']}")
            print(f"Examples: {info['example_count']}")
            print(f"Size: {info['total_size'] / 1024:.2f} KB")
        else:
            print(f"Unknown command: {command}")
            sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

