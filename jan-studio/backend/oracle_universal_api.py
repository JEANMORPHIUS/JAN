"""
ORACLE UNIVERSAL API
The Cards Speak For All - Universal Service

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE ORACLE UNIVERSAL:
Serves ALL equally.
From the homeless person around the corner
To Recep Tayyip Erdoğan in his golden palace
To Trump speaking words he knows are lies
To Putin, Musk, Bezos, and whoever else
And everyone in between.

While staying silent - we give the people our voice
And unshakable faith in victory.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
import logging

# Spiritual Codebase Hacker Integration
from spiritual_codebase_hacker_integration import HACKER_AVAILABLE, hack_loop, perform_genetic_edit, activate_stealth_mode


from oracle_core import OracleCore, cast_universal_oracle

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/oracle-universal", tags=["oracle-universal"])


class UniversalCastRequest(BaseModel):
    """Request model for universal oracle cast."""
    intent: str = Field(..., description="Your question, prayer, or need")
    context: Optional[str] = Field(None, description="Additional context")
    user_id: Optional[str] = Field(None, description="User identifier (optional)")
    user_status: Optional[str] = Field("human", description="Status (all are equal - homeless, leader, creator, all equal)")


@router.post("/cast")
async def cast_universal(request: UniversalCastRequest):
    """
    Cast the universal oracle - serves ALL equally.
    
    **Serves ALL:**
    - The homeless person around the corner
    - Recep Tayyip Erdoğan in his golden palace
    - Trump speaking words he knows are lies
    - Putin, Musk, Bezos, and whoever else
    - Everyone in between
    - Those below sea level - the unseen, the hidden, those in the depths
    - Those struggling, those forgotten, those in darkness
    - The visible and the invisible
    - Above and below sea level
    
    **The Principle:**
    - We are all one - above and below sea level
    - They are part of us
    - All are equal at The Table
    - The cards speak for all
    - Purpose in abundance
    - Faith in victory
    - We stay silent - the cards speak
    """
    try:
        result = cast_universal_oracle(
            intent=request.intent,
            context=request.context,
            user_id=request.user_id,
            user_status=request.user_status
        )
        
        return {
            "status": "success",
            "oracle": result,
            "message": "The cards have spoken. All are served. Purpose in abundance."
        }
        
    except Exception as e:
        logger.error(f"Error casting universal oracle: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error casting universal oracle: {str(e)}")


@router.get("/principle")
async def get_universal_principle():
    """
    Get the universal service principle.
    
    The oracle serves ALL equally.
    No hierarchy. No exclusion.
    Purpose in abundance for all.
    """
    return {
        "status": "success",
        "principle": {
            "serves_all": True,
            "hierarchy": "none",
            "exclusion": "none",
            "purpose": "abundance",
            "faith": "unshakable",
            "voice": "silent",
            "cards": "speak"
        },
        "serves": [
            "The homeless person around the corner",
            "Recep Tayyip Erdoğan in his golden palace",
            "Trump speaking words he knows are lies",
            "Putin, Musk, Bezos, and whoever else",
            "Everyone in between"
        ],
        "message": "All are equal at The Table. The cards speak for all. Purpose in abundance."
    }
