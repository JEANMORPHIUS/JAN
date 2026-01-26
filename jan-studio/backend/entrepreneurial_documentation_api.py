"""
ENTREPRENEURIAL DOCUMENTATION API
API endpoints for business documentation framework

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE TRUTH:
Everything must be above board.
All documentation needed for the new world.
"""

from fastapi import APIRouter, HTTPException, Body
from typing import Optional, Dict, List, Any
from pydantic import BaseModel
import logging

from entrepreneurial_documentation_framework import (
    get_entrepreneurial_framework,
    BusinessEntityType,
    DocumentType
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/entrepreneurial", tags=["Entrepreneurial Documentation"])


class DocumentCreateRequest(BaseModel):
    """Document creation request"""
    entity_id: str
    document_type: str
    title: str
    description: str
    file_path: Optional[str] = None
    content: Optional[str] = None
    required: bool = True
    compliance_related: bool = False


@router.get("/blueprints")
async def get_all_blueprints():
    """Get all business blueprints"""
    try:
        framework = get_entrepreneurial_framework()
        blueprints = framework.get_all_blueprints()
        
        return {
            "status": "success",
            "count": len(blueprints),
            "blueprints": {
                entity_id: {
                    "name": blueprint.name,
                    "entity_type": blueprint.entity_type.value,
                    "description": blueprint.description,
                    "mission": blueprint.mission,
                    "legal_structure": blueprint.legal_structure,
                    "registration_number": blueprint.registration_number,
                    "location": blueprint.location,
                    "channels": blueprint.channels,
                    "revenue_streams": blueprint.revenue_streams,
                    "documentation_status": blueprint.documentation_status
                }
                for entity_id, blueprint in blueprints.items()
            }
        }
    except Exception as e:
        logger.error(f"Error getting blueprints: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/blueprints/{entity_id}")
async def get_blueprint(entity_id: str):
    """Get blueprint for specific entity"""
    try:
        framework = get_entrepreneurial_framework()
        blueprint = framework.get_blueprint(entity_id)
        
        if not blueprint:
            raise HTTPException(status_code=404, detail=f"Blueprint not found: {entity_id}")
        
        return {
            "status": "success",
            "blueprint": {
                "entity_id": blueprint.entity_id,
                "name": blueprint.name,
                "entity_type": blueprint.entity_type.value,
                "description": blueprint.description,
                "mission": blueprint.mission,
                "vision": blueprint.vision,
                "legal_structure": blueprint.legal_structure,
                "registration_number": blueprint.registration_number,
                "location": blueprint.location,
                "channels": blueprint.channels,
                "revenue_streams": blueprint.revenue_streams,
                "partnerships": blueprint.partnerships,
                "compliance_requirements": blueprint.compliance_requirements,
                "documentation_status": blueprint.documentation_status
            }
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting blueprint: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/the-ark")
async def get_the_ark_blueprint():
    """Get The Ark - Deluxe Holiday Complex blueprint"""
    try:
        framework = get_entrepreneurial_framework()
        the_ark = framework.get_the_ark_blueprint()
        
        if not the_ark:
            raise HTTPException(status_code=404, detail="The Ark blueprint not found")
        
        return {
            "status": "success",
            "the_ark": {
                "project_id": the_ark.project_id,
                "name": the_ark.name,
                "property_type": the_ark.property_type,
                "location": the_ark.location,
                "capacity": the_ark.capacity,
                "facilities": the_ark.facilities,
                "amenities": the_ark.amenities,
                "target_market": the_ark.target_market,
                "business_model": the_ark.business_model,
                "revenue_streams": the_ark.revenue_streams,
                "legal_requirements": the_ark.legal_requirements,
                "documentation_needed": the_ark.documentation_needed,
                "contracts_needed": the_ark.contracts_needed,
                "compliance_requirements": the_ark.compliance_requirements
            }
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting The Ark blueprint: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/documentation/status")
async def get_documentation_status():
    """Get documentation status for all entities"""
    try:
        framework = get_entrepreneurial_framework()
        status = framework.get_documentation_status()
        
        return {
            "status": "success",
            "report": status
        }
    except Exception as e:
        logger.error(f"Error getting documentation status: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/documentation/checklist")
async def get_documentation_checklist():
    """Get comprehensive documentation checklist"""
    try:
        framework = get_entrepreneurial_framework()
        checklist = framework.generate_documentation_checklist()
        
        return {
            "status": "success",
            "checklist": checklist
        }
    except Exception as e:
        logger.error(f"Error getting checklist: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/documents/create")
async def create_document(request: DocumentCreateRequest):
    """Create business document"""
    try:
        framework = get_entrepreneurial_framework()
        
        document_type = DocumentType(request.document_type)
        
        document = framework.create_document(
            entity_id=request.entity_id,
            document_type=document_type,
            title=request.title,
            description=request.description,
            file_path=request.file_path,
            content=request.content,
            required=request.required,
            compliance_related=request.compliance_related
        )
        
        return {
            "status": "success",
            "message": "Document created",
            "document": {
                "document_id": document.document_id,
                "entity_id": document.entity_id,
                "document_type": document.document_type.value,
                "title": document.title,
                "status": document.status
            }
        }
    except Exception as e:
        logger.error(f"Error creating document: {e}")
        raise HTTPException(status_code=500, detail=str(e))
