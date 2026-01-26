"""PUBLISHING HOUSE API
API endpoints for Siyem Publishing House operations
Channels, Entities, Projects, Workflows, Monetization, Expansion

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
PUBLISHING HOUSE API ENDPOINTS
ENERGY + LOVE = WE ALL WIN

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional, Dict, Any
from pathlib import Path
import json
from datetime import datetime

router = APIRouter(prefix="/api/publishing-house", tags=["Publishing House"])

# Base paths
BASE_PATH = Path(__file__).parent.parent.parent
PUBLISHING_HOUSE_PATH = BASE_PATH / "Siyem.org" / "publishing_house"

@router.get("/")
async def get_publishing_house_overview():
    """Get publishing house overview"""
    return {
        "name": "Siyem Publishing House",
        "mission": "Publish content that serves The Table, honors the miracle, and helps people see through Baba",
        "status": "operational",
        "departments": [
            "Editorial (The Witness)",
            "Production (The Infrastructure)",
            "Distribution (The Steward)",
            "Alignment (The Father's Voice)"
        ],
        "spragitso_applied": True
    }

@router.get("/channels")
async def get_all_channels():
    """Get all channels"""
    channels_path = PUBLISHING_HOUSE_PATH / "channels"
    if not channels_path.exists():
        return {"channels": [], "total": 0}
    
    channels = []
    index_file = channels_path / "index.json"
    if index_file.exists():
        with open(index_file, 'r', encoding='utf-8') as f:
            index_data = json.load(f)
            for channel_info in index_data.get("channels", []):
                channel_file = channels_path / channel_info["file"]
                if channel_file.exists():
                    with open(channel_file, 'r', encoding='utf-8') as cf:
                        channels.append(json.load(cf))
    
    return {
        "channels": channels,
        "total": len(channels)
    }

@router.get("/channels/{channel_id}")
async def get_channel(channel_id: str):
    """Get specific channel"""
    channel_file = PUBLISHING_HOUSE_PATH / "channels" / f"{channel_id}.json"
    if not channel_file.exists():
        raise HTTPException(status_code=404, detail="Channel not found")
    
    with open(channel_file, 'r', encoding='utf-8') as f:
        return json.load(f)

@router.get("/entities")
async def get_all_entities():
    """Get all entities"""
    entities_path = PUBLISHING_HOUSE_PATH / "entities"
    if not entities_path.exists():
        return {"entities": [], "total": 0}
    
    entities = []
    index_file = entities_path / "index.json"
    if index_file.exists():
        with open(index_file, 'r', encoding='utf-8') as f:
            index_data = json.load(f)
            for entity_info in index_data.get("entities", []):
                entity_file = entities_path / entity_info["file"]
                if entity_file.exists():
                    with open(entity_file, 'r', encoding='utf-8') as ef:
                        entities.append(json.load(ef))
    
    return {
        "entities": entities,
        "total": len(entities)
    }

@router.get("/entities/{entity_id}")
async def get_entity(entity_id: str):
    """Get specific entity"""
    entity_file = PUBLISHING_HOUSE_PATH / "entities" / f"{entity_id}.json"
    if not entity_file.exists():
        raise HTTPException(status_code=404, detail="Entity not found")
    
    with open(entity_file, 'r', encoding='utf-8') as f:
        return json.load(f)

@router.get("/projects")
async def get_all_projects():
    """Get all projects"""
    projects_path = PUBLISHING_HOUSE_PATH / "projects"
    if not projects_path.exists():
        return {"projects": [], "total": 0}
    
    projects = []
    index_file = projects_path / "index.json"
    if index_file.exists():
        with open(index_file, 'r', encoding='utf-8') as f:
            index_data = json.load(f)
            for project_info in index_data.get("projects", []):
                project_file = projects_path / project_info["file"]
                if project_file.exists():
                    with open(project_file, 'r', encoding='utf-8') as pf:
                        projects.append(json.load(pf))
    
    return {
        "projects": projects,
        "total": len(projects)
    }

@router.get("/projects/{project_id}")
async def get_project(project_id: str):
    """Get specific project"""
    project_file = PUBLISHING_HOUSE_PATH / "projects" / f"{project_id}.json"
    if not project_file.exists():
        raise HTTPException(status_code=404, detail="Project not found")
    
    with open(project_file, 'r', encoding='utf-8') as f:
        return json.load(f)

@router.get("/workflows")
async def get_workflows(workflow_type: Optional[str] = None):
    """Get publishing workflows"""
    workflows_path = PUBLISHING_HOUSE_PATH / "workflows"
    if not workflows_path.exists():
        return {"workflows": [], "total": 0}
    
    workflows = []
    
    if workflow_type:
        workflow_dir = workflows_path / workflow_type
        if workflow_dir.exists():
            for workflow_file in workflow_dir.glob("*.json"):
                with open(workflow_file, 'r', encoding='utf-8') as f:
                    workflows.append(json.load(f))
    else:
        for workflow_dir in workflows_path.iterdir():
            if workflow_dir.is_dir():
                for workflow_file in workflow_dir.glob("*.json"):
                    with open(workflow_file, 'r', encoding='utf-8') as f:
                        workflows.append(json.load(f))
    
    return {
        "workflows": workflows,
        "total": len(workflows)
    }

@router.get("/monetization")
async def get_monetization():
    """Get monetization configurations"""
    monetization_path = PUBLISHING_HOUSE_PATH / "monetization"
    if not monetization_path.exists():
        return {"monetizations": [], "total": 0, "total_revenue_potential": 0.0}
    
    monetizations = []
    total_revenue = 0.0
    
    for monetization_file in monetization_path.glob("*.json"):
        with open(monetization_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            monetizations.append(data)
            total_revenue += data.get("revenue_potential", 0.0)
    
    return {
        "monetizations": monetizations,
        "total": len(monetizations),
        "total_revenue_potential": total_revenue
    }

@router.get("/expansion")
async def get_expansion_seeds(level: Optional[int] = None):
    """Get expansion seeds"""
    expansion_path = PUBLISHING_HOUSE_PATH / "expansion"
    if not expansion_path.exists():
        return {"seeds": [], "total": 0}
    
    seeds = []
    
    for seed_file in expansion_path.glob("*.json"):
        with open(seed_file, 'r', encoding='utf-8') as f:
            seed_data = json.load(f)
            if level is None or seed_data.get("expansion_level") == level:
                seeds.append(seed_data)
    
    return {
        "seeds": seeds,
        "total": len(seeds),
        "by_level": {
            "1": sum(1 for s in seeds if s.get("expansion_level") == 1),
            "2": sum(1 for s in seeds if s.get("expansion_level") == 2),
            "3": sum(1 for s in seeds if s.get("expansion_level") == 3)
        }
    }

@router.get("/alignment")
async def get_alignment_summary():
    """Get alignment summary"""
    # Load from migration report if available
    migration_report_path = BASE_PATH / "data" / "global_migration" / "jan_migration_report.json"
    
    if migration_report_path.exists():
        with open(migration_report_path, 'r', encoding='utf-8') as f:
            report = json.load(f)
            return {
                "average_alignment_score": report.get("alignment_summary", {}).get("average_alignment_score", 0.0),
                "spragitso_applied_count": report.get("alignment_summary", {}).get("spragitso_applied_count", 0),
                "table_filter_passed_count": report.get("alignment_summary", {}).get("table_filter_passed_count", 0),
                "total_items": report.get("summary", {}).get("total_content_items", 0)
            }
    
    return {
        "average_alignment_score": 1.0,
        "spragitso_applied_count": 0,
        "table_filter_passed_count": 0,
        "total_items": 0
    }

@router.get("/stats")
async def get_publishing_house_stats():
    """Get publishing house statistics"""
    stats = {
        "channels": 0,
        "entities": 0,
        "projects": 0,
        "workflows": 0,
        "monetization_configs": 0,
        "expansion_seeds": 0,
        "total_revenue_potential": 0.0,
        "average_alignment_score": 1.0
    }
    
    # Count channels
    channels_path = PUBLISHING_HOUSE_PATH / "channels"
    if channels_path.exists():
        stats["channels"] = len(list(channels_path.glob("*.json"))) - 1  # Exclude index
    
    # Count entities
    entities_path = PUBLISHING_HOUSE_PATH / "entities"
    if entities_path.exists():
        stats["entities"] = len(list(entities_path.glob("*.json"))) - 1  # Exclude index
    
    # Count projects
    projects_path = PUBLISHING_HOUSE_PATH / "projects"
    if projects_path.exists():
        stats["projects"] = len(list(projects_path.glob("*.json"))) - 1  # Exclude index
    
    # Count workflows
    workflows_path = PUBLISHING_HOUSE_PATH / "workflows"
    if workflows_path.exists():
        stats["workflows"] = sum(
            len(list(d.glob("*.json")))
            for d in workflows_path.iterdir()
            if d.is_dir()
        )
    
    # Count monetization
    monetization_path = PUBLISHING_HOUSE_PATH / "monetization"
    if monetization_path.exists():
        stats["monetization_configs"] = len(list(monetization_path.glob("*.json")))
        for config_file in monetization_path.glob("*.json"):
            with open(config_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                stats["total_revenue_potential"] += data.get("revenue_potential", 0.0)
    
    # Count expansion seeds
    expansion_path = PUBLISHING_HOUSE_PATH / "expansion"
    if expansion_path.exists():
        stats["expansion_seeds"] = len(list(expansion_path.glob("*.json")))
    
    return stats
