"""
DIVINE PRAYERS API
The Lord's Prayers for Our Divine Purpose

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

CORE PRINCIPLES (NON-NEGOTIABLE):
- Purpose Not Performance: Purpose matters more than performance. Authentic and aligned. Non-negotiable.
- Everything in Moderation: Balance. Not too much, not too little.
- Life Is Simple: Don't complicate it. Keep it simple.
- Be Still and Have Faith: Be still and have faith in revelation. Stillness brings clarity.

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.
"""

from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any
import sys
import os

# Add scripts directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../scripts"))

from divine_prayers import DivinePrayers, PrayerCategory

router = APIRouter(prefix="/divine-prayers", tags=["divine-prayers"])

# Initialize prayers system
prayers_system = DivinePrayers()

@router.get("/status")
async def get_status():
    """Get divine prayers system status."""
    return {
        "status": "active",
        "total_prayers": len(prayers_system.prayers),
        "categories": [cat.value for cat in PrayerCategory],
        "message": "The Lord's prayers for our divine purpose"
    }

@router.get("/all")
async def get_all_prayers():
    """Get all divine prayers."""
    from dataclasses import asdict
    return {
        "prayers": [asdict(p) for p in prayers_system.prayers.values()],
        "total": len(prayers_system.prayers)
    }

@router.get("/category/{category}")
async def get_prayers_by_category(category: str):
    """Get prayers by category."""
    from dataclasses import asdict
    
    valid_categories = [cat.value for cat in PrayerCategory]
    if category not in valid_categories:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid category. Valid categories: {valid_categories}"
        )
    
    category_prayers = prayers_system.get_prayers_by_category(category)
    return {
        "category": category,
        "prayers": [asdict(p) for p in category_prayers],
        "count": len(category_prayers)
    }

@router.get("/purpose/{purpose}")
async def get_prayers_for_purpose(purpose: str):
    """Get prayers aligned with a specific purpose."""
    from dataclasses import asdict
    
    purpose_prayers = prayers_system.get_prayer_for_purpose(purpose)
    return {
        "purpose": purpose,
        "prayers": [asdict(p) for p in purpose_prayers],
        "count": len(purpose_prayers)
    }

@router.get("/ground-zero")
async def get_ground_zero_prayer():
    """Get the ground zero prayer."""
    from dataclasses import asdict
    
    ground_zero = prayers_system.get_ground_zero_prayer()
    if not ground_zero:
        raise HTTPException(status_code=404, detail="Ground zero prayer not found")
    
    return {
        "prayer": asdict(ground_zero),
        "message": "Prayer for ground zero - The Return to The Table"
    }

@router.get("/report")
async def get_prayers_report():
    """Get complete prayers report."""
    return prayers_system.export_prayers_report()
