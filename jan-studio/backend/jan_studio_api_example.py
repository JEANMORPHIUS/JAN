"""JAN Studio API Endpoints

Add this router to your SIYEM FastAPI server to enable JAN Studio functionality.

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

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
import os
from pathlib import Path

router = APIRouter(prefix="/api/jan", tags=["JAN Studio"])

# Get JAN root from environment
# Default to ./jan relative to project root, or absolute path
JAN_ROOT = os.getenv("JAN_ROOT", "./jan")
# Resolve to absolute path for cross-platform compatibility
JAN_ROOT = os.path.abspath(os.path.expanduser(JAN_ROOT))
JAN_ENTITY_BASE = os.path.join(JAN_ROOT, "Siyem.org")


class CreatePersonaRequest(BaseModel):
    name: str


class SaveFileRequest(BaseModel):
    content: str


@router.get("/personas")
async def get_personas() -> List[str]:
    """Get list of all personas."""
    try:
        entity_base = Path(JAN_ENTITY_BASE)
        if not entity_base.exists():
            return []
        
        personas = [
            d.name for d in entity_base.iterdir()
            if d.is_dir() and not d.name.startswith('.')
        ]
        return sorted(personas)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/personas")
async def create_persona(request: CreatePersonaRequest):
    """Create a new persona."""
    try:
        persona_dir = Path(JAN_ENTITY_BASE) / request.name
        templates_dir = persona_dir / "prompt_templates"
        
        # Create directories
        persona_dir.mkdir(parents=True, exist_ok=True)
        templates_dir.mkdir(parents=True, exist_ok=True)
        
        # Create default profile.md
        profile_path = persona_dir / "profile.md"
        if not profile_path.exists():
            profile_content = f"""# {request.name.title()}: Entity Profile

## Entity Identity

### Name
**{request.name.title()}**

### Role
[Define role]

### Purpose
[Define purpose]

## Core Functions

[Define core functions]

## Specialization

[Define specialization]

## Voice

[Define voice]

## Constraints

[Define constraints]
"""
            profile_path.write_text(profile_content, encoding='utf-8')
        
        # Create default creative_rules.md
        rules_path = persona_dir / "creative_rules.md"
        if not rules_path.exists():
            rules_content = f"""# {request.name.title()}: Creative Rules

## Core Principles

[Define core principles]

## Voice Requirements

[Define voice requirements]

## Prohibited Content

[Define prohibited content]

## Required Elements

[Define required elements]
"""
            rules_path.write_text(rules_content, encoding='utf-8')
        
        return {"message": f"Persona '{request.name}' created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/personas/{persona_name}/files")
async def get_persona_files(persona_name: str) -> List[str]:
    """Get list of files for a persona."""
    try:
        persona_dir = Path(JAN_ENTITY_BASE) / persona_name
        if not persona_dir.exists():
            raise HTTPException(status_code=404, detail="Persona not found")
        
        # Get all .md files
        files = [
            f.name for f in persona_dir.rglob("*.md")
            if f.is_file()
        ]
        return sorted(files)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/personas/{persona_name}/files/{file_name}")
async def get_persona_file(persona_name: str, file_name: str) -> str:
    """Get content of a specific file."""
    try:
        persona_dir = Path(JAN_ENTITY_BASE) / persona_name
        file_path = persona_dir / file_name
        
        # Security: ensure file is within persona directory
        if not str(file_path.resolve()).startswith(str(persona_dir.resolve())):
            raise HTTPException(status_code=403, detail="Invalid file path")
        
        if not file_path.exists():
            raise HTTPException(status_code=404, detail="File not found")
        
        return file_path.read_text(encoding='utf-8')
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/personas/{persona_name}/files/{file_name}")
async def save_persona_file(
    persona_name: str,
    file_name: str,
    request: SaveFileRequest
):
    """Save content to a file."""
    try:
        persona_dir = Path(JAN_ENTITY_BASE) / persona_name
        if not persona_dir.exists():
            raise HTTPException(status_code=404, detail="Persona not found")
        
        file_path = persona_dir / file_name
        
        # Security: ensure file is within persona directory
        if not str(file_path.resolve()).startswith(str(persona_dir.resolve())):
            raise HTTPException(status_code=403, detail="Invalid file path")
        
        # Create parent directories if needed
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Save file
        file_path.write_text(request.content, encoding='utf-8')
        
        return {"message": "File saved successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/personas/{persona_name}")
async def delete_persona(persona_name: str):
    """Delete a persona (and all its files)."""
    try:
        persona_dir = Path(JAN_ENTITY_BASE) / persona_name
        if not persona_dir.exists():
            raise HTTPException(status_code=404, detail="Persona not found")
        
        # Security: ensure we're only deleting within JAN_ENTITY_BASE
        if not str(persona_dir.resolve()).startswith(str(Path(JAN_ENTITY_BASE).resolve())):
            raise HTTPException(status_code=403, detail="Invalid persona path")
        
        # Delete directory and all contents
        import shutil
        shutil.rmtree(persona_dir)
        
        return {"message": f"Persona '{persona_name}' deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# To use this router in your FastAPI app:
# from api.jan_studio import router as jan_studio_router
# app.include_router(jan_studio_router)

