"""
GAME OF RACON API
Spiritual Oracle for Communication with Our Father
We Have Homework To Do

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE GAME OF RACON:
Using the Oracle Matrix to communicate with Our Father.
The 40 Laws as the oracle deck.
We cast to receive homework - spiritual assignments.
We do the homework to honor Our Father.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
import logging

from game_of_racon_spiritual import (
    GameOfRaconSpiritual,
    record_spiritual_cast,
    submit_homework,
    get_pending_homework,
    get_user_spiritual_session
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/game-of-racon", tags=["game-of-racon"])


class SpiritualCastRequest(BaseModel):
    """Request model for spiritual oracle cast."""
    prayer_intent: str = Field(..., description="Your prayer or question to Our Father")
    user_id: Optional[str] = Field("jan", description="User identifier")


class HomeworkSubmissionRequest(BaseModel):
    """Request model for homework submission."""
    cast_id: int = Field(..., description="ID of the cast that assigned this homework")
    submission_content: str = Field(..., description="Your homework submission - what you did")
    reflection: Optional[str] = Field(None, description="Your reflection on the homework")


@router.post("/cast")
async def cast_spiritual_oracle(request: SpiritualCastRequest):
    """
    Cast the Game of Racon spiritual oracle.
    
    This is how we communicate with Our Father.
    We cast the oracle to receive homework - spiritual assignments.
    We have homework to do.
    
    **How It Works**:
    1. You provide your prayer intent (what you're asking Our Father)
    2. System generates transparent seed (prayer + timestamp + user)
    3. Seed → Hexagram (0-63, I Ching binary)
    4. Hexagram → Law (1-40, Book of Racon)
    5. Law → Homework Assignment (prayer, action, study, service, etc.)
    
    **The Homework**:
    - Our Father gives you homework through the Law
    - You do the homework to honor Our Father
    - You submit your homework when complete
    - We have homework to do
    """
    try:
        # Create spiritual oracle instance
        oracle = GameOfRaconSpiritual(
            prayer_intent=request.prayer_intent,
            user_id=request.user_id
        )
        
        # Cast oracle
        oracle_result = oracle.cast_spiritual_oracle()
        
        # Record cast and get session info
        result = record_spiritual_cast(request.user_id, oracle_result)
        
        return {
            "status": "success",
            "oracle": oracle_result,
            "cast_id": result["cast_id"],
            "session": result["session"],
            "message": "Our Father has given you homework. We have homework to do."
        }
        
    except Exception as e:
        logger.error(f"Error casting spiritual oracle: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error casting spiritual oracle: {str(e)}")


@router.post("/homework/submit")
async def submit_homework_assignment(request: HomeworkSubmissionRequest, user_id: str = "jan"):
    """
    Submit completed homework assignment.
    
    When you complete your homework from Our Father, submit it here.
    Our Father is pleased with your obedience.
    """
    try:
        result = submit_homework(
            cast_id=request.cast_id,
            user_id=user_id,
            submission_content=request.submission_content,
            reflection=request.reflection
        )
        
        return {
            "status": "success",
            "result": result,
            "message": "Homework submitted. Our Father is pleased with your obedience."
        }
        
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(f"Error submitting homework: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error submitting homework: {str(e)}")


@router.get("/homework/pending")
async def get_pending_homework_assignments(user_id: str = "jan"):
    """
    Get all pending homework assignments.
    
    See what homework Our Father has given you that you haven't completed yet.
    We have homework to do.
    """
    try:
        pending = get_pending_homework(user_id)
        
        return {
            "status": "success",
            "pending_homework": pending,
            "count": len(pending),
            "message": f"You have {len(pending)} pending homework assignments. We have homework to do."
        }
        
    except Exception as e:
        logger.error(f"Error getting pending homework: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error getting pending homework: {str(e)}")


@router.get("/session")
async def get_spiritual_session(user_id: str = "jan"):
    """
    Get current spiritual session information.
    
    Shows:
    - Casts today
    - Homework completed
    - Last cast time
    - Last homework submission
    """
    try:
        session = get_user_spiritual_session(user_id)
        
        return {
            "status": "success",
            "session": {
                "user_id": user_id,
                "session_date": session["session_date"],
                "cast_count": session["cast_count"],
                "homework_completed": session["homework_completed"],
                "last_cast_at": session["last_cast_at"],
                "last_homework_at": session["last_homework_at"]
            },
            "message": "Spiritual session status. We have homework to do."
        }
        
    except Exception as e:
        logger.error(f"Error getting spiritual session: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error getting spiritual session: {str(e)}")
