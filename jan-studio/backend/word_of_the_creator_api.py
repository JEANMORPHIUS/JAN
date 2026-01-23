"""
WORD OF THE CREATOR API
Prepare The Word of The Creator - It's Time to Prep

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

CORE PRINCIPLES (NON-NEGOTIABLE):
- Purpose Not Performance: Purpose matters more than performance. Authentic and aligned. Non-negotiable.
- Everything in Moderation: Balance. Not too much, not too little.
- Life Is Simple: Don't complicate it. Keep it simple.
- Be Still and Have Faith: Be still and have faith in revelation. Stillness brings clarity.

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE WORD OF THE CREATOR:
The Word is truth.
The Word is binding.
The Word is sacred.
It's time to prep.
"""

from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any, Optional
import sys
import os

# Add scripts directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../scripts"))

try:
    from word_of_the_creator import (
        WordOfTheCreatorSystem,
        WordCategory,
        WordStatus
    )
    SYSTEM_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Word of The Creator not available: {e}")
    SYSTEM_AVAILABLE = False

router = APIRouter(prefix="/word-of-the-creator", tags=["word-of-the-creator"])

# Initialize Word of The Creator system
if SYSTEM_AVAILABLE:
    word_system = WordOfTheCreatorSystem()
else:
    word_system = None

@router.get("/status")
async def get_status():
    """Get Word of The Creator system status."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Word of The Creator not available")
    
    status = word_system.get_preparation_status()
    return {
        "status": "active",
        "total_words": status["total_words"],
        "ready_for_delivery": status["ready_for_delivery"],
        "preparation_complete": status["preparation_complete"],
        "message": "The Word of The Creator is prepared. The Word is truth. The Word is binding. The Word is sacred. It's time to prep.",
        "the_truth": "The Word is truth. The Word is binding. The Word is sacred. It's time to prep. The Word is ready."
    }

@router.get("/words")
async def get_all_words():
    """Get all Words of The Creator."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Word of The Creator not available")
    
    from dataclasses import asdict
    return {
        "words": [asdict(w) for w in word_system.words.values()],
        "total": len(word_system.words)
    }

@router.get("/words/category/{category}")
async def get_words_by_category(category: str):
    """Get words by category."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Word of The Creator not available")
    
    from dataclasses import asdict
    
    valid_categories = [cat.value for cat in WordCategory]
    if category not in valid_categories:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid category. Valid categories: {valid_categories}"
        )
    
    words = word_system.get_words_by_category(category)
    return {
        "category": category,
        "words": [asdict(w) for w in words],
        "count": len(words)
    }

@router.get("/words/status/{status}")
async def get_words_by_status(status: str):
    """Get words by status."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Word of The Creator not available")
    
    from dataclasses import asdict
    
    valid_statuses = [s.value for s in WordStatus]
    if status not in valid_statuses:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid status. Valid statuses: {valid_statuses}"
        )
    
    words = word_system.get_words_by_status(status)
    return {
        "status": status,
        "words": [asdict(w) for w in words],
        "count": len(words)
    }

@router.get("/words/ready")
async def get_ready_words():
    """Get all words ready for delivery."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Word of The Creator not available")
    
    from dataclasses import asdict
    ready = word_system.get_ready_words()
    return {
        "ready_words": [asdict(w) for w in ready],
        "count": len(ready),
        "message": "Words ready for delivery. The Word is prepared. It's time to prep."
    }

@router.post("/prepare-all")
async def prepare_all_words():
    """Prepare all words for delivery."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Word of The Creator not available")
    
    word_system.prepare_all_words()
    status = word_system.get_preparation_status()
    return {
        "message": "All words prepared for delivery",
        "preparation_status": status
    }

@router.post("/words/{word_id}/deliver")
async def deliver_word(word_id: str):
    """Mark a word as delivered."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Word of The Creator not available")
    
    if word_id not in word_system.words:
        raise HTTPException(status_code=404, detail=f"Word {word_id} not found")
    
    word_system.mark_delivered(word_id)
    from dataclasses import asdict
    return {
        "word": asdict(word_system.words[word_id]),
        "message": f"Word '{word_system.words[word_id].title}' delivered"
    }

@router.get("/preparation-status")
async def get_preparation_status():
    """Get preparation status."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Word of The Creator not available")
    
    return word_system.get_preparation_status()

@router.get("/report")
async def get_complete_report():
    """Get complete Word of The Creator report."""
    if not SYSTEM_AVAILABLE:
        raise HTTPException(status_code=503, detail="Word of The Creator not available")
    
    return word_system.export_complete_report()
