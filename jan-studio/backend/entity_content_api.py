"""ENTITY CONTENT API
Refine All Entity Content and UI @ Codebase Level

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

CORE PRINCIPLES (NON-NEGOTIABLE):
- Purpose Not Performance: Purpose matters more than performance. Authentic and aligned. Non-negotiable.
- Everything in Moderation: Balance. Not too much, not too little.
- Life Is Simple: Don't complicate it. Keep it simple.
- Be Still and Have Faith: Be still and have faith in revelation. Stillness brings clarity.

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

ENTITY CONTENT API:
Refine all entity content and UI at codebase level.
Full English/Turkish support.
All entity profiles, roles, purposes, functions translated.

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

from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any, Optional
import sys
import os

# Add scripts directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../scripts"))

try:
    from entity_content_refinement import EntityContentRefinement, LanguageCode
    SYSTEM_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Entity Content Refinement not available: {e}")
    SYSTEM_AVAILABLE = False

router = APIRouter(prefix="/entity-content", tags=["entity-content"])

# Initialize entity content refinement
if SYSTEM_AVAILABLE:
    refinement = EntityContentRefinement()
else:
    refinement = None

@router.get("/status")
async def get_status():
    """Get entity content refinement system status."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Entity Content Refinement not available")
    
    return {
        "status": "active",
        "total_entities": len(refinement.entities),
        "message": "All entity content refined with full English/Turkish support. All entity profiles, roles, purposes, and functions translated.",
        "the_truth": "All entity content refined. Full English/Turkish support. UI components support bilingual content."
    }

@router.get("/entities")
async def get_all_entities(language: str = "en"):
    """Get all entities in specified language."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Entity Content Refinement not available")
    
    valid_languages = [LanguageCode.ENGLISH.value, LanguageCode.TURKISH.value]
    if language not in valid_languages:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid language. Valid languages: {valid_languages}"
        )
    
    return {
        "language": language,
        "entities": refinement.get_all_entities(language),
        "total": len(refinement.entities)
    }

@router.get("/entities/{entity_name}")
async def get_entity(entity_name: str, language: str = "en"):
    """Get entity content in specified language."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Entity Content Refinement not available")
    
    valid_languages = [LanguageCode.ENGLISH.value, LanguageCode.TURKISH.value]
    if language not in valid_languages:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid language. Valid languages: {valid_languages}"
        )
    
    content = refinement.get_entity_content(entity_name, language)
    if not content:
        raise HTTPException(status_code=404, detail=f"Entity {entity_name} not found")
    
    return {
        "entity_name": entity_name,
        "language": language,
        "content": content
    }

@router.get("/entities/{entity_name}/bilingual")
async def get_entity_bilingual(entity_name: str):
    """Get entity content in both English and Turkish."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Entity Content Refinement not available")
    
    if entity_name not in refinement.entities:
        raise HTTPException(status_code=404, detail=f"Entity {entity_name} not found")
    
    return {
        "entity_name": entity_name,
        "english": refinement.get_entity_content(entity_name, LanguageCode.ENGLISH.value),
        "turkish": refinement.get_entity_content(entity_name, LanguageCode.TURKISH.value)
    }

@router.get("/report")
async def get_entity_content_report():
    """Get complete entity content report."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Entity Content Refinement not available")
    
    return refinement.export_entity_content_report()
