"""UI REFINEMENT API
Refine All UI Components @ Codebase Level

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

CORE PRINCIPLES (NON-NEGOTIABLE):
- Purpose Not Performance: Purpose matters more than performance. Authentic and aligned. Non-negotiable.
- Everything in Moderation: Balance. Not too much, not too little.
- Life Is Simple: Don't complicate it. Keep it simple.
- Be Still and Have Faith: Be still and have faith in revelation. Stillness brings clarity.

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

UI REFINEMENT API:
Refine all UI components at codebase level.
Full English/Turkish support.
Language selection.
Bilingual content display.

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

# Spiritual Codebase Hacker Integration
from spiritual_codebase_hacker_integration import HACKER_AVAILABLE, hack_loop, perform_genetic_edit, activate_stealth_mode


# Add scripts directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../scripts"))

try:
    from ui_refinement import UIRefinement, UIComponentType, LanguageCode
    SYSTEM_AVAILABLE = True
except ImportError as e:
    print(f"Warning: UI Refinement not available: {e}")
    SYSTEM_AVAILABLE = False

router = APIRouter(prefix="/ui-refinement", tags=["ui-refinement"])

# Initialize UI refinement
if SYSTEM_AVAILABLE:
    ui_refinement = UIRefinement()
else:
    ui_refinement = None

@router.get("/status")
async def get_status():
    """Get UI refinement system status."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="UI Refinement not available")
    
    return {
        "status": "active",
        "total_components": len(ui_refinement.components),
        "message": "All UI components refined with full English/Turkish support. Language selection supported. Bilingual content display ready.",
        "the_truth": "All UI components refined. Full English/Turkish support. Language selection. Bilingual content display."
    }

@router.get("/components")
async def get_all_components(language: str = "en"):
    """Get all UI components in specified language."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="UI Refinement not available")
    
    valid_languages = [LanguageCode.ENGLISH.value, LanguageCode.TURKISH.value]
    if language not in valid_languages:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid language. Valid languages: {valid_languages}"
        )
    
    return {
        "language": language,
        "components": {
            key: ui_refinement.get_component_text(key, language)
            for key in ui_refinement.components.keys()
        },
        "total": len(ui_refinement.components)
    }

@router.get("/components/{key}")
async def get_component(key: str, language: str = "en"):
    """Get UI component text in specified language."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="UI Refinement not available")
    
    valid_languages = [LanguageCode.ENGLISH.value, LanguageCode.TURKISH.value]
    if language not in valid_languages:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid language. Valid languages: {valid_languages}"
        )
    
    if key not in ui_refinement.components:
        raise HTTPException(status_code=404, detail=f"Component {key} not found")
    
    return {
        "key": key,
        "language": language,
        "text": ui_refinement.get_component_text(key, language),
        "component_type": ui_refinement.components[key].component_type
    }

@router.get("/components/type/{component_type}")
async def get_components_by_type(component_type: str, language: str = "en"):
    """Get all components of a type in specified language."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="UI Refinement not available")
    
    valid_types = [ct.value for ct in UIComponentType]
    if component_type not in valid_types:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid component type. Valid types: {valid_types}"
        )
    
    valid_languages = [LanguageCode.ENGLISH.value, LanguageCode.TURKISH.value]
    if language not in valid_languages:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid language. Valid languages: {valid_languages}"
        )
    
    components = ui_refinement.get_components_by_type(component_type, language)
    return {
        "component_type": component_type,
        "language": language,
        "components": components,
        "count": len(components)
    }

@router.get("/report")
async def get_ui_refinement_report():
    """Get complete UI refinement report."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="UI Refinement not available")
    
    return ui_refinement.export_ui_refinement_report()
