"""JAN Templates API Endpoints

Template management for JAN Studio - allows saving and reusing persona configurations.

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
from typing import List, Dict, Any, Optional
import os
import json

# Spiritual Codebase Hacker Integration
from spiritual_codebase_hacker_integration import HACKER_AVAILABLE, hack_loop, perform_genetic_edit, activate_stealth_mode

from pathlib import Path
from datetime import datetime

router = APIRouter(prefix="/api/templates", tags=["JAN Templates"])

# Get JAN root from environment
# Default to ./jan relative to project root, or absolute path
JAN_ROOT = os.getenv("JAN_ROOT", "./jan")
# Resolve to absolute path for cross-platform compatibility
JAN_ROOT = os.path.abspath(os.path.expanduser(JAN_ROOT))
TEMPLATES_DIR = os.path.join(JAN_ROOT, "templates")
JAN_ENTITY_BASE = os.path.join(JAN_ROOT, "Siyem.org")


class CreateTemplateRequest(BaseModel):
    template_name: str
    persona_data: Dict[str, Any]
    description: Optional[str] = None
    category: Optional[str] = None


class TemplateMetadata(BaseModel):
    name: str
    description: Optional[str] = None
    category: Optional[str] = None
    created_at: str
    file_count: int
    persona_name: Optional[str] = None


class InstantiateTemplateRequest(BaseModel):
    template_name: str
    persona_name: str
    overwrite: bool = False


# Ensure templates directory exists
Path(TEMPLATES_DIR).mkdir(parents=True, exist_ok=True)


def get_template_path(template_name: str) -> Path:
    """Get path to template file."""
    return Path(TEMPLATES_DIR) / f"{template_name}.json"


def validate_template_name(name: str) -> bool:
    """Validate template name format."""
    return bool(name and name.replace('_', '').replace('-', '').isalnum() and name.islower())


@router.post("/create")
async def create_template(request: CreateTemplateRequest):
    """Create a new template from persona data."""
    try:
        # Validate template name
        if not validate_template_name(request.template_name):
            raise HTTPException(
                status_code=400,
                detail="Template name must be lowercase alphanumeric with hyphens/underscores only"
            )
        
        # Check if template already exists
        template_path = get_template_path(request.template_name)
        if template_path.exists():
            raise HTTPException(status_code=409, detail="Template already exists")
        
        # Create template structure
        template_data = {
            "name": request.template_name,
            "description": request.description,
            "category": request.category,
            "created_at": datetime.now().isoformat(),
            "persona_data": request.persona_data,
        }
        
        # Save template
        template_path.write_text(json.dumps(template_data, indent=2), encoding='utf-8')
        
        return {
            "message": f"Template '{request.template_name}' created successfully",
            "template_name": request.template_name
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/list")
async def list_templates() -> List[TemplateMetadata]:
    """List all available templates with metadata."""
    try:
        templates_dir = Path(TEMPLATES_DIR)
        if not templates_dir.exists():
            return []
        
        templates = []
        for template_file in templates_dir.glob("*.json"):
            try:
                template_data = json.loads(template_file.read_text(encoding='utf-8'))
                persona_data = template_data.get("persona_data", {})
                files = persona_data.get("files", {})
                
                templates.append(TemplateMetadata(
                    name=template_data.get("name", template_file.stem),
                    description=template_data.get("description"),
                    category=template_data.get("category"),
                    created_at=template_data.get("created_at", ""),
                    file_count=len(files),
                    persona_name=persona_data.get("name")
                ))
            except Exception as e:
                # Skip invalid templates
                continue
        
        return sorted(templates, key=lambda x: x.name)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{template_name}")
async def get_template(template_name: str) -> Dict[str, Any]:
    """Get template structure (JAN files)."""
    try:
        template_path = get_template_path(template_name)
        if not template_path.exists():
            raise HTTPException(status_code=404, detail="Template not found")
        
        template_data = json.loads(template_path.read_text(encoding='utf-8'))
        return template_data
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/instantiate")
async def instantiate_template(request: InstantiateTemplateRequest):
    """Create a persona from a template."""
    try:
        # Get template
        template_path = get_template_path(request.template_name)
        if not template_path.exists():
            raise HTTPException(status_code=404, detail="Template not found")
        
        template_data = json.loads(template_path.read_text(encoding='utf-8'))
        persona_data = template_data.get("persona_data", {})
        
        # Check if persona already exists
        persona_dir = Path(JAN_ENTITY_BASE) / request.persona_name
        if persona_dir.exists() and not request.overwrite:
            raise HTTPException(
                status_code=409,
                detail=f"Persona '{request.persona_name}' already exists. Use overwrite=true to replace."
            )
        
        # Create persona directory
        persona_dir.mkdir(parents=True, exist_ok=True)
        templates_dir = persona_dir / "prompt_templates"
        templates_dir.mkdir(parents=True, exist_ok=True)
        
        # Create files from template
        files = persona_data.get("files", {})
        created_files = []
        
        for file_path, content in files.items():
            file_full_path = persona_dir / file_path
            file_full_path.parent.mkdir(parents=True, exist_ok=True)
            file_full_path.write_text(content, encoding='utf-8')
            created_files.append(file_path)
        
        return {
            "message": f"Persona '{request.persona_name}' created from template '{request.template_name}'",
            "persona_name": request.persona_name,
            "template_name": request.template_name,
            "files_created": created_files
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{template_name}")
async def delete_template(template_name: str):
    """Delete a template."""
    try:
        template_path = get_template_path(template_name)
        if not template_path.exists():
            raise HTTPException(status_code=404, detail="Template not found")
        
        template_path.unlink()
        
        return {"message": f"Template '{template_name}' deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/save-from-persona")
async def save_persona_as_template(persona_name: str, template_name: str, description: Optional[str] = None):
    """Save an existing persona as a template."""
    try:
        # Validate template name
        if not validate_template_name(template_name):
            raise HTTPException(
                status_code=400,
                detail="Template name must be lowercase alphanumeric with hyphens/underscores only"
            )
        
        # Check if template already exists
        template_path = get_template_path(template_name)
        if template_path.exists():
            raise HTTPException(status_code=409, detail="Template already exists")
        
        # Load persona files
        persona_dir = Path(JAN_ENTITY_BASE) / persona_name
        if not persona_dir.exists():
            raise HTTPException(status_code=404, detail="Persona not found")
        
        # Read all .md files
        files = {}
        for md_file in persona_dir.rglob("*.md"):
            relative_path = md_file.relative_to(persona_dir)
            files[str(relative_path)] = md_file.read_text(encoding='utf-8')
        
        # Create template
        template_data = {
            "name": template_name,
            "description": description or f"Template based on persona '{persona_name}'",
            "category": None,
            "created_at": datetime.now().isoformat(),
            "persona_data": {
                "name": persona_name,
                "files": files
            }
        }
        
        # Save template
        template_path.write_text(json.dumps(template_data, indent=2), encoding='utf-8')
        
        return {
            "message": f"Template '{template_name}' created from persona '{persona_name}'",
            "template_name": template_name,
            "files_included": len(files)
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

