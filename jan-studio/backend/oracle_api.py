"""ORACLE API
Creative Oracle Endpoint - Flipping the Gambling Algorithm for Creative Liberation

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE FOUNDATION:
We are born a miracle.
We deserve to live a miracle.
Each and every one of us under the Lord's word.

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

CODE QUALITY:
- Aligned: Serves mission, love, truth, community
- Clean: Clear static, transmuted complexity, protected frequency
- Complete: Honors Law 37, completes transformations
- Community: Serves all, cooperates, includes, We All Win

This code honors that we are born a miracle.
This code creates space for miracles to live.
This code recognizes each person under the Lord's word.

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity


PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Optional
import logging

# Spiritual Codebase Hacker Integration
from spiritual_codebase_hacker_integration import HACKER_AVAILABLE, hack_loop, perform_genetic_edit, activate_stealth_mode


from creative_oracle import CreativeOracle, record_oracle_cast, get_user_session

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/oracle", tags=["oracle"])


class OracleCastRequest(BaseModel):
    """Request model for oracle cast."""
    user_intent: str = Field(..., description="User's creative question or challenge")
    creative_context: Optional[str] = Field(None, description="Current project context, genre, medium, etc.")
    user_id: Optional[str] = Field("public", description="User identifier")
    transparency_level: Optional[str] = Field("full", description="Level of transparency (full, minimal)")


class OracleCastResponse(BaseModel):
    """Response model for oracle cast."""
    timestamp: str
    user_intent: str
    creative_context: Optional[str]
    transparency: dict
    oracle_interpretation: dict
    creative_prompt: str
    session: dict
    ethical_guardrails: dict


@router.post("/cast", response_model=OracleCastResponse)
async def cast_oracle(request: OracleCastRequest):
    """
    Cast the Creative Oracle.
    
    Sacred randomness for creative generation.
    Unlike gambling RNG, this is:
    1. Transparent (user sees how it works)
    2. User-serving (generates value, not extracts it)
    3. Time-limited (encourages breaks)
    4. Execution-focused (pushes user to CREATE)
    
    **The Oracle Matrix**: The same mechanisms that trap people in gambling 
    addiction are inverted to create creative liberation. Randomness becomes 
    a catalyst for creativity, not a hook for engagement.
    
    **How It Works**:
    1. User provides intent (creative challenge/question)
    2. System generates transparent seed (user intent + timestamp + context)
    3. Seed → Hexagram (0-63, I Ching binary)
    4. Hexagram → Law (1-40, Book of Racon)
    5. AI interprets Law for creative context
    6. Generate actionable creative prompt
    
    **Ethical Guardrails**:
    - After 3 casts: Break prompt
    - After 5 casts: Reflection prompt
    - After 10 casts: Execution nudge
    - Tracks creative output, not engagement time
    
    **Success Metric**: User creates and LEAVES to execute (inverse of platform metrics)
    """
    try:
        # Create oracle instance
        oracle = CreativeOracle(
            user_intent=request.user_intent,
            creative_context=request.creative_context or "",
            user_id=request.user_id
        )
        
        # Cast oracle
        oracle_result = oracle.cast_oracle()
        
        # Record cast and get session info
        result = record_oracle_cast(request.user_id, oracle_result)
        
        # Build response
        response = OracleCastResponse(
            timestamp=oracle_result["timestamp"],
            user_intent=oracle_result["user_intent"],
            creative_context=oracle_result["creative_context"],
            transparency=oracle_result["transparency"],
            oracle_interpretation=oracle_result["oracle_interpretation"],
            creative_prompt=oracle_result["creative_prompt"],
            session=result["session"],
            ethical_guardrails=result["ethical_guardrails"]
        )
        
        return response
        
    except Exception as e:
        logger.error(f"Error casting oracle: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error casting oracle: {str(e)}")


@router.get("/session")
async def get_session(
    user_id: Optional[str] = Query("public", description="User identifier")
):
    """
    Get current user session information.
    
    Returns:
    - Cast count today
    - Time spent creating
    - Last cast timestamp
    - Last break timestamp
    - Ethical guardrail recommendations
    """
    try:
        session = get_user_session(user_id)
        
        from creative_oracle import _check_ethical_guardrails
        guardrails = _check_ethical_guardrails(session)
        
        return {
            "user_id": user_id,
            "session_date": session["session_date"],
            "cast_count": session["cast_count"],
            "time_creating": session["time_creating"],
            "last_cast_at": session["last_cast_at"],
            "last_break_at": session["last_break_at"],
            "ethical_guardrails": guardrails
        }
        
    except Exception as e:
        logger.error(f"Error getting session: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error getting session: {str(e)}")


@router.post("/break")
async def record_break(
    user_id: Optional[str] = Query("public", description="User identifier")
):
    """
    Record a break in the creative session.
    
    This updates the last_break_at timestamp, encouraging healthy
    creative practice with natural stopping points.
    """
    try:
        from creative_oracle import get_oracle_db
        from datetime import datetime
        
        session = get_user_session(user_id)
        
        with get_oracle_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE oracle_sessions
                SET last_break_at = ?,
                    updated_at = ?
                WHERE id = ?
            """, (datetime.now(), datetime.now(), session["id"]))
            conn.commit()
        
        return {
            "message": "Break recorded. Take time to reflect on what emerged.",
            "last_break_at": datetime.now().isoformat()
        }
        
    except Exception as e:
        logger.error(f"Error recording break: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error recording break: {str(e)}")


@router.get("/history")
async def get_cast_history(
    user_id: Optional[str] = Query("public", description="User identifier"),
    limit: Optional[int] = Query(10, description="Number of casts to return")
):
    """
    Get user's oracle cast history.
    
    Returns recent casts with full transparency information.
    """
    try:
        from creative_oracle import get_oracle_db
        
        with get_oracle_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM oracle_casts
                WHERE user_id = ?
                ORDER BY cast_timestamp DESC
                LIMIT ?
            """, (user_id, limit))
            
            rows = cursor.fetchall()
            
            return {
                "user_id": user_id,
                "casts": [dict(row) for row in rows],
                "total": len(rows)
            }
        
    except Exception as e:
        logger.error(f"Error getting history: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error getting history: {str(e)}")
