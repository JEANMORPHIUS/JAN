"""
ORACLE SIYEM API
API endpoints for Oracle SIYEM Integration

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

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X.
"""

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Optional
import logging
import sys
from pathlib import Path

# Add SIYEM services to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "SIYEM" / "services"))

from oracle_siyem_integration import (
    OracleSIYEM,
    cast_siyem_oracle,
    AntiAddictionMetrics
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/oracle-siyem", tags=["oracle-siyem"])


class OracleCastRequest(BaseModel):
    """Request model for Oracle SIYEM cast."""
    user_intent: str = Field(..., description="User's creative question or challenge")
    creative_context: Optional[str] = Field(None, description="Current project context, genre, medium, etc.")
    user_id: Optional[str] = Field("public", description="User identifier")


class OracleCastResponse(BaseModel):
    """Response model for Oracle SIYEM cast."""
    timestamp: str
    user_id: str
    user_intent: str
    creative_context: str
    transparency: dict
    mechanism_visualization: dict
    oracle_interpretation: dict
    ethical_guardrails: dict
    session: dict
    success_metrics: dict
    success_score: float


@router.post("/cast", response_model=OracleCastResponse)
async def cast_oracle(request: OracleCastRequest):
    """
    Cast the Oracle SIYEM.
    
    **Transparent RNG Engine:**
    - User sees exactly how randomness is generated
    - Seed components are visible and verifiable
    - Hexagram calculation is transparent
    - Law mapping is clear
    
    **40 Laws Interpretation:**
    - Every cast interprets a Law from Book of Racon
    - Context-specific creative guidance
    - Actionable creative prompts
    
    **Anti-Addiction Success Metrics:**
    - Success = user creates and LEAVES (inverse of platform metrics)
    - Tracks creative outputs, not engagement time
    - Encourages breaks and execution
    - Success score: higher = more creation, less time on platform
    
    **How It Works:**
    1. User provides intent (creative challenge/question)
    2. System generates transparent seed (user intent + timestamp + context)
    3. Seed → Hexagram (0-63, I Ching binary)
    4. Hexagram → Law (1-40, Book of Racon)
    5. AI interprets Law for creative context
    6. Generate actionable creative prompt
    7. Track anti-addiction metrics
    
    **Ethical Guardrails:**
    - After 3 casts: Break prompt
    - After 5 casts: Reflection prompt
    - After 10 casts: Execution nudge
    - Tracks creative output, not engagement time
    """
    try:
        oracle = OracleSIYEM()
        result = oracle.cast_oracle(
            user_intent=request.user_intent,
            context=request.creative_context,
            user_id=request.user_id
        )
        
        response = OracleCastResponse(
            timestamp=result["timestamp"],
            user_id=result["user_id"],
            user_intent=result["user_intent"],
            creative_context=result["creative_context"],
            transparency=result["transparency"],
            mechanism_visualization=result.get("mechanism_visualization", {}),
            oracle_interpretation=result["oracle_interpretation"],
            ethical_guardrails=result["ethical_guardrails"],
            session=result["session"],
            success_metrics=result.get("success_metrics", {}),
            success_score=result["success_score"]
        )
        
        return response
        
    except ValueError as e:
        logger.warning(f"Validation error casting Oracle: {e}")
        raise HTTPException(
            status_code=400,
            detail={
                "error": "Validation Error",
                "message": "The Oracle requires clear intent. Law 1: The Table Never Lies - provide honest, specific guidance.",
                "racon_principle": "Law 1: The Table Never Lies - Your intent must be clear and truthful.",
                "suggestion": "Provide a specific creative question or challenge."
            }
        )
    except Exception as e:
        logger.error(f"Error casting Oracle SIYEM: {e}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail={
                "error": "Oracle Casting Error",
                "message": "The Oracle encountered an unexpected error. Law 37: Finish What You Begin - we will resolve this.",
                "racon_principle": "Law 37: Finish What You Begin - We commit to resolving this issue.",
                "support": "Please try again, or contact support if the issue persists."
            }
        )


@router.get("/session")
async def get_session(
    user_id: Optional[str] = Query("public", description="User identifier")
):
    """
    Get current user session information.
    
    Returns:
    - Cast count today
    - Creative outputs count
    - Time creating (minutes)
    - Last cast timestamp
    - Last break timestamp
    - Ethical guardrail recommendations
    - Success score
    """
    try:
        metrics = AntiAddictionMetrics()
        session = metrics.get_user_session(user_id)
        guardrails = metrics.check_ethical_guardrails(user_id)
        success_score = metrics.calculate_success_score(user_id)
        
        return {
            "user_id": user_id,
            "session": session,
            "ethical_guardrails": guardrails,
            "success_score": success_score
        }
        
    except Exception as e:
        logger.error(f"Error getting session: {e}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail={
                "error": "Session Error",
                "message": "Could not retrieve session data. Law 5: Your Word Is Your Bond - we will restore access.",
                "racon_principle": "Law 5: Your Word Is Your Bond - We commit to maintaining your session data."
            }
        )


@router.post("/record-output")
async def record_creative_output(
    user_id: Optional[str] = Query("public", description="User identifier")
):
    """
    Record that user created something (success metric).
    
    This is the KEY success metric: user creates and LEAVES.
    Higher creative outputs = better success score.
    """
    try:
        metrics = AntiAddictionMetrics()
        metrics.record_creative_output(user_id)
        
        session = metrics.get_user_session(user_id)
        success_score = metrics.calculate_success_score(user_id)
        
        return {
            "message": "Creative output recorded. This is the goal - create and execute.",
            "session": session,
            "success_score": success_score
        }
        
    except Exception as e:
        logger.error(f"Error recording creative output: {e}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail={
                "error": "Recording Error",
                "message": "Could not record your creative output. Law 1: The Table Never Lies - your creation matters and will be recognized.",
                "racon_principle": "Law 1: The Table Never Lies - Your creative work is truth and will be honored."
            }
        )


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
        from datetime import datetime
        from oracle_siyem_integration import get_oracle_siyem_db
        
        session = AntiAddictionMetrics.get_user_session(user_id)
        
        with get_oracle_siyem_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE oracle_sessions
                SET last_break_at = ?,
                    break_reminders = break_reminders + 1,
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
        from oracle_siyem_integration import get_oracle_siyem_db
        import json
        
        with get_oracle_siyem_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM oracle_casts
                WHERE user_id = ?
                ORDER BY cast_timestamp DESC
                LIMIT ?
            """, (user_id, limit))
            
            rows = cursor.fetchall()
            
            casts = []
            for row in rows:
                cast = dict(row)
                # Parse JSON fields
                if cast.get("seed_components"):
                    cast["seed_components"] = json.loads(cast["seed_components"])
                if cast.get("transparency_data"):
                    cast["transparency_data"] = json.loads(cast["transparency_data"])
                casts.append(cast)
            
            return {
                "user_id": user_id,
                "casts": casts,
                "total": len(casts)
            }
        
    except Exception as e:
        logger.error(f"Error getting history: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error getting history: {str(e)}")


@router.get("/metrics")
async def get_metrics(
    user_id: Optional[str] = Query("public", description="User identifier")
):
    """
    Get comprehensive anti-addiction metrics.
    
    Returns:
    - Success score (higher = more creation, less time on platform)
    - Cast count vs creative outputs
    - Time creating vs time on platform
    - Break frequency
    - Execution triggers
    """
    try:
        metrics = AntiAddictionMetrics()
        session = metrics.get_user_session(user_id)
        guardrails = metrics.check_ethical_guardrails(user_id)
        success_score = metrics.calculate_success_score(user_id)
        
        return {
            "user_id": user_id,
            "success_score": success_score,
            "metrics": {
                "cast_count": session["cast_count"],
                "creative_outputs": session.get("creative_outputs", 0),
                "time_creating": session.get("time_creating", 0),
                "break_reminders": session.get("break_reminders", 0),
                "execution_nudges": session.get("execution_nudges", 0)
            },
            "guardrails": guardrails,
            "interpretation": {
                "success_score_explanation": "Higher score = more creation, less time on platform. Success = user creates and LEAVES.",
                "healthy_practice": success_score > 50 and session.get("creative_outputs", 0) > session["cast_count"]
            }
        }
        
    except Exception as e:
        logger.error(f"Error getting metrics: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error getting metrics: {str(e)}")
