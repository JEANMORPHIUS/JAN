"""
Pack Persona Tool

Creates a .janpkg file from a persona directory.
"""

import os
import json
import zipfile
import shutil
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List

JAN_ROOT = os.getenv("JAN_ROOT", r"S:\JAN")
JAN_ENTITY_BASE = os.path.join(JAN_ROOT, "Siyem.org")


def find_jan_files(persona_dir: Path) -> List[Dict[str, str]]:
    """Find all JAN markdown files in persona directory."""
    files = []
    for md_file in persona_dir.rglob("*.md"):
        relative_path = md_file.relative_to(persona_dir)
        files.append({
            "path": str(relative_path),
            "content": md_file.read_text(encoding='utf-8')
        })
    return files


def find_example_files(persona_dir: Path) -> List[Dict[str, str]]:
    """Find example output files."""
    examples_dir = persona_dir / "examples"
    if not examples_dir.exists():
        return []
    
    files = []
    for example_file in examples_dir.rglob("*"):
        if example_file.is_file():
            relative_path = example_file.relative_to(examples_dir)
            try:
                content = example_file.read_text(encoding='utf-8')
                files.append({
                    "path": str(relative_path),
                    "content": content
                })
            except:
                # Skip binary files
                pass
    return files


def create_manifest(persona_name: str, persona_dir: Path, author: str = None, version: str = "1.0.0") -> Dict[str, Any]:
    """Create manifest.json for the package."""
    # Try to read existing profile.md for metadata
    profile_path = persona_dir / "profile.md"
    description = ""
    if profile_path.exists():
        try:
            content = profile_path.read_text(encoding='utf-8')
            # Extract description from profile
            if "### Purpose" in content:
                purpose_section = content.split("### Purpose")[1].split("##")[0]
                description = purpose_section.strip()[:500]  # Limit to 500 chars
        except:
            pass
    
    manifest = {
        "format_version": "1.0",
        "persona_name": persona_name,
        "version": version,
        "author": author or "Unknown",
        "description": description or f"JAN persona: {persona_name}",
        "created_at": datetime.now().isoformat(),
        "jan_files": [],
        "examples": [],
        "license": "CC-BY-4.0",
        "requires": {
            "jan_version": ">=1.0.0"
        }
    }
    
    return manifest


def pack_persona(persona_name: str, output_path: str = None, author: str = None, version: str = "1.0.0") -> str:
    """Pack a persona into a .janpkg file."""
    # Find persona directory
    persona_dir = Path(JAN_ENTITY_BASE) / persona_name
    if not persona_dir.exists():
        raise ValueError(f"Persona directory not found: {persona_dir}")
    
    # Create manifest
    manifest = create_manifest(persona_name, persona_dir, author, version)
    
    # Find all files
    jan_files = find_jan_files(persona_dir)
    example_files = find_example_files(persona_dir)
    
    manifest["jan_files"] = [f["path"] for f in jan_files]
    manifest["examples"] = [f["path"] for f in example_files]
    
    # Determine output path
    if not output_path:
        output_path = f"{persona_name}-v{version}.janpkg"
    
    # Create ZIP file
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Add manifest
        zipf.writestr("manifest.json", json.dumps(manifest, indent=2))
        
        # Add JAN files
        for file_data in jan_files:
            zipf.writestr(f"jan/{file_data['path']}", file_data['content'])
        
        # Add example files
        for file_data in example_files:
            zipf.writestr(f"examples/{file_data['path']}", file_data['content'])
        
        # Add README if exists
        readme_path = persona_dir / "README.md"
        if readme_path.exists():
            zipf.writestr("README.md", readme_path.read_text(encoding='utf-8'))
        
        # Add LICENSE if exists
        license_path = persona_dir / "LICENSE"
        if license_path.exists():
            zipf.writestr("LICENSE", license_path.read_text(encoding='utf-8'))
        else:
            # Add default CC-BY-4.0 license
            default_license = """Creative Commons Attribution 4.0 International License

Copyright (c) {year} {author}

This work is licensed under the Creative Commons Attribution 4.0 International License.
To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/
""".format(year=datetime.now().year, author=manifest["author"])
            zipf.writestr("LICENSE", default_license)
    
    return output_path


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: pack_persona.py <persona_name> [output_path] [--author AUTHOR] [--version VERSION]")
        sys.exit(1)
    
    persona_name = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    # Parse optional arguments
    author = None
    version = "1.0.0"
    for i, arg in enumerate(sys.argv):
        if arg == "--author" and i + 1 < len(sys.argv):
            author = sys.argv[i + 1]
        elif arg == "--version" and i + 1 < len(sys.argv):
            version = sys.argv[i + 1]
    
    try:
        result = pack_persona(persona_name, output_path, author, version)
        print(f"✅ Packed persona: {result}")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

