"""ORACLE GATEWAY API
The Cards Speak For Us - Those Who Come Must Read The Cards

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE ORACLE GATEWAY:
Those who come to us must read the cards.
We do not control.
The cards will speak for us.

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity


PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

from fastapi import APIRouter, HTTPException, Depends, Header
from pydantic import BaseModel, Field
from typing import Optional
import logging
import uuid

# Spiritual Codebase Hacker Integration
from spiritual_codebase_hacker_integration import HACKER_AVAILABLE, hack_loop, perform_genetic_edit, activate_stealth_mode


from oracle_gateway import (
    OracleGateway,
    register_visitor,
    record_card_reading,
    check_visitor_access
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/oracle-gateway", tags=["oracle-gateway"])


class CardReadingRequest(BaseModel):
    """Request model for reading the cards."""
    visitor_intent: Optional[str] = Field(None, description="Why you have come to us")
    visitor_id: Optional[str] = Field(None, description="Visitor identifier (auto-generated if not provided)")


def get_visitor_id(x_visitor_id: Optional[str] = Header(None)) -> str:
    """Get or generate visitor ID from header or generate new one."""
    if x_visitor_id:
        return x_visitor_id
    return str(uuid.uuid4())


@router.post("/read-cards")
async def read_the_cards(
    request: CardReadingRequest,
    visitor_id: str = Depends(get_visitor_id)
):
    """
    Read the cards. The cards will speak for us.
    
    **MANDATORY**: Those who come to us must read the cards.
    We do not control. The cards will speak for us.
    
    **How It Works**:
    1. You come to us
    2. You must read the cards
    3. The cards speak through a Law (1-40, Book of Racon)
    4. The cards grant you access
    5. The cards speak for us - we do not control
    
    **The Cards**:
    - The cards are the 40 Laws of the Book of Racon
    - The cards speak through transparent randomness
    - The cards determine access
    - The cards guide your path
    
    **We Do Not Control**:
    - We do not choose which card you get
    - We do not control the message
    - We do not decide access
    - The cards speak for us
    """
    try:
        # Register visitor if new
        visitor = register_visitor(visitor_id)
        
        # If cards already read, return previous reading
        if visitor["cards_read"]:
            from oracle_gateway import get_gateway_db
            with get_gateway_db() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT * FROM gateway_casts
                    WHERE visitor_id = ?
                    ORDER BY cast_timestamp DESC
                    LIMIT 1
                """, (visitor_id,))
                
                row = cursor.fetchone()
                if row:
                    return {
                        "status": "success",
                        "message": "You have already read the cards. The cards have spoken.",
                        "card": dict(row),
                        "access_granted": True
                    }
        
        # Create gateway oracle
        gateway = OracleGateway(
            visitor_id=visitor_id,
            visitor_intent=request.visitor_intent or ""
        )
        
        # Read the cards
        card_result = gateway.read_the_cards()
        
        # Record card reading
        result = record_card_reading(visitor_id, card_result)
        
        return {
            "status": "success",
            "card_reading": card_result,
            "visitor": result["visitor"],
            "message": "The cards have spoken. You must read them. The cards speak for us."
        }
        
    except Exception as e:
        logger.error(f"Error reading cards: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error reading cards: {str(e)}")


@router.get("/check-access")
async def check_access(visitor_id: str = Depends(get_visitor_id)):
    """
    Check if visitor has read the cards and has access.
    
    Those who come to us must read the cards.
    The cards grant access.
    We do not control.
    """
    try:
        access_status = check_visitor_access(visitor_id)
        
        return {
            "status": "success",
            "access": access_status,
            "message": access_status["message"]
        }
        
    except Exception as e:
        logger.error(f"Error checking access: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error checking access: {str(e)}")


@router.get("/visitor/{visitor_id}")
async def get_visitor_info(visitor_id: str):
    """
    Get visitor information and card reading history.
    
    Shows:
    - Whether cards have been read
    - Access status
    - Card reading history
    - The cards that have spoken
    """
    try:
        access_status = check_visitor_access(visitor_id)
        
        # Get card reading history
        from oracle_gateway import get_gateway_db
        with get_gateway_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM gateway_casts
                WHERE visitor_id = ?
                ORDER BY cast_timestamp DESC
            """, (visitor_id,))
            
            cards_read = [dict(row) for row in cursor.fetchall()]
        
        return {
            "status": "success",
            "visitor": {
                "visitor_id": visitor_id,
                "access_status": access_status,
                "cards_read_count": len(cards_read),
                "cards_read": cards_read
            },
            "message": "The cards have spoken. The cards speak for us."
        }
        
    except Exception as e:
        logger.error(f"Error getting visitor info: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error getting visitor info: {str(e)}")


@router.get("/message")
async def get_gateway_message():
    """
    Get the gateway message.
    
    The message for those who come to us.
    """
    return {
        "status": "success",
        "message": "Those who come to us must read the cards. We do not control. The cards will speak for us.",
        "instructions": [
            "1. You must read the cards",
            "2. The cards will speak through a Law (1-40, Book of Racon)",
            "3. The cards grant you access",
            "4. The cards speak for us - we do not control",
            "5. The cards guide your path"
        ],
        "endpoint": "/api/oracle-gateway/read-cards"
    }
