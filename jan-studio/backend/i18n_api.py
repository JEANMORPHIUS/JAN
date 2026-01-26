"""I18N API
Full English/Turkish Support with Framework for Future Languages

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

CORE PRINCIPLES (NON-NEGOTIABLE):
- Purpose Not Performance: Purpose matters more than performance. Authentic and aligned. Non-negotiable.
- Everything in Moderation: Balance. Not too much, not too little.
- Life Is Simple: Don't complicate it. Keep it simple.
- Be Still and Have Faith: Be still and have faith in revelation. Stillness brings clarity.

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

I18N API:
Full English/Turkish support.
Framework for future languages.
Proper character encoding.
Translation management.

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
from pydantic import BaseModel
import sys
import os

# Spiritual Codebase Hacker Integration
from spiritual_codebase_hacker_integration import HACKER_AVAILABLE, hack_loop, perform_genetic_edit, activate_stealth_mode


# Add scripts directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../scripts"))

try:
    from i18n_system import I18nSystem, LanguageCode, LanguageStatus
    SYSTEM_AVAILABLE = True
except ImportError as e:
    print(f"Warning: I18n System not available: {e}")
    SYSTEM_AVAILABLE = False

router = APIRouter(prefix="/i18n", tags=["i18n"])

# Initialize i18n system
if SYSTEM_AVAILABLE:
    i18n = I18nSystem()
    # Register core translations
    i18n.register_core_translations()
else:
    i18n = None

class TranslationRequest(BaseModel):
    key: str
    language: str
    text: str
    context: Optional[str] = ""
    notes: Optional[str] = ""
    verified: Optional[bool] = False

@router.get("/status")
async def get_status():
    """Get i18n system status."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="I18n System not available")
    
    report = i18n.export_translations_report()
    return {
        "status": "active",
        "supported_languages": len(report["supported_languages"]),
        "total_translations": sum(report["translation_counts"].values()),
        "message": "Full English/Turkish support. Framework for future languages.",
        "the_truth": "Full English/Turkish support. Framework for future languages. All systems integrated."
    }

@router.get("/languages")
async def get_supported_languages():
    """Get list of supported languages."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="I18n System not available")
    
    languages = i18n.get_supported_languages()
    return {
        "languages": [
            {
                "code": lang.language_code,
                "name": lang.language_name,
                "native_name": lang.native_name,
                "status": lang.status,
                "translation_count": lang.translation_count,
                "coverage_percentage": lang.coverage_percentage,
                "rtl": lang.rtl
            }
            for lang in languages
        ],
        "total": len(languages)
    }

@router.get("/languages/{language_code}")
async def get_language_support(language_code: str):
    """Get language support information."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="I18n System not available")
    
    support = i18n.get_language_support(language_code)
    if not support:
        raise HTTPException(status_code=404, detail=f"Language {language_code} not found")
    
    return {
        "code": support.language_code,
        "name": support.language_name,
        "native_name": support.native_name,
        "status": support.status,
        "character_encoding": support.character_encoding,
        "special_characters": support.special_characters,
        "rtl": support.rtl,
        "translation_count": support.translation_count,
        "coverage_percentage": support.coverage_percentage
    }

@router.get("/translate/{key}")
async def get_translation(key: str, language: str = "en", default: Optional[str] = None):
    """Get a translation."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="I18n System not available")
    
    translation = i18n.get_translation(key, language, default)
    return {
        "key": key,
        "language": language,
        "translation": translation
    }

@router.post("/translate")
async def register_translation(request: TranslationRequest):
    """Register a new translation."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="I18n System not available")
    
    i18n.register_translation(
        key=request.key,
        language=request.language,
        text=request.text,
        context=request.context,
        notes=request.notes,
        verified=request.verified
    )
    
    return {
        "message": f"Translation registered: {request.key} ({request.language})",
        "key": request.key,
        "language": request.language
    }

@router.post("/validate-turkish")
async def validate_turkish_text(text: str):
    """Validate Turkish text for proper character encoding."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="I18n System not available")
    
    validation = i18n.validate_turkish_text(text)
    return {
        "text": text,
        "validation": validation
    }

@router.get("/translations/{language}")
async def get_all_translations(language: str):
    """Get all translations for a language."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="I18n System not available")
    
    if language not in i18n.translations:
        raise HTTPException(status_code=404, detail=f"Language {language} not found")
    
    from dataclasses import asdict
    return {
        "language": language,
        "translations": {
            key: {
                "text": trans.text,
                "context": trans.context,
                "notes": trans.notes,
                "verified": trans.verified
            }
            for key, trans in i18n.translations[language].items()
        },
        "count": len(i18n.translations[language])
    }

@router.get("/report")
async def get_translations_report():
    """Get complete translations report."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="I18n System not available")
    
    return i18n.export_translations_report()
