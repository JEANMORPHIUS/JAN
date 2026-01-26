"""
RETURN TO THE TABLE API
Security, Contingency, and Delivery Systems

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

IS COMING.
THE RETURN TO THE TABLE.
NO ONE GETS LEFT BEHIND.
"""

from fastapi import APIRouter, HTTPException, Body, Query
from typing import Optional, Dict, List, Any
from pathlib import Path
import sys
import logging

# Spiritual Codebase Hacker Integration
from spiritual_codebase_hacker_integration import HACKER_AVAILABLE, hack_loop, perform_genetic_edit, activate_stealth_mode

from datetime import datetime

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

try:
    from return_to_table_security import ReturnToTableSecurity
    from art_of_conversation import ArtOfConversation
    SYSTEMS_AVAILABLE = True
except ImportError as e:
    logging.warning(f"Return to Table systems not available: {e}")
    SYSTEMS_AVAILABLE = False

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/return-to-table", tags=["Return to Table"])

# Global system instances
security_system = ReturnToTableSecurity() if SYSTEMS_AVAILABLE else None
conversation_system = ArtOfConversation() if SYSTEMS_AVAILABLE else None


@router.get("/status")
async def get_return_to_table_status():
    """Get Return to Table system status."""
    if not SYSTEMS_AVAILABLE:
        raise HTTPException(status_code=503, detail="Return to Table systems not available")
    
    return {
        "status": "active",
        "message": "IS COMING. THE RETURN TO THE TABLE. NO ONE GETS LEFT BEHIND.",
        "security_measures": len(security_system.security_measures) if security_system else 0,
        "contingency_plans": len(security_system.contingency_plans) if security_system else 0,
        "foresight_items": len(security_system.foresight) if security_system else 0,
        "inclusion_protocols": len(security_system.inclusion_protocols) if security_system else 0,
        "conversations": len(conversation_system.conversations) if conversation_system else 0,
        "learning_paths": len(conversation_system.learning_paths) if conversation_system else 0,
        "delivery_guidelines": len(conversation_system.delivery_guidelines) if conversation_system else 0
    }


# Security endpoints
@router.get("/security/status")
async def get_security_status():
    """Get security status."""
    if not SYSTEMS_AVAILABLE:
        raise HTTPException(status_code=503, detail="Security system not available")
    
    return security_system.get_security_status()


@router.get("/security/measures")
async def get_security_measures():
    """Get all security measures."""
    if not SYSTEMS_AVAILABLE:
        raise HTTPException(status_code=503, detail="Security system not available")
    
    return {
        "security_measures": [
            {
                "measure_id": m.measure_id,
                "name": m.name,
                "description": m.description,
                "security_level": m.security_level,
                "protects_what": m.protects_what
            }
            for m in security_system.security_measures.values()
        ],
        "total": len(security_system.security_measures)
    }


# Contingency endpoints
@router.get("/contingency/status")
async def get_contingency_status():
    """Get contingency status."""
    if not SYSTEMS_AVAILABLE:
        raise HTTPException(status_code=503, detail="Contingency system not available")
    
    return security_system.get_contingency_status()


@router.get("/contingency/plans")
async def get_contingency_plans():
    """Get all contingency plans."""
    if not SYSTEMS_AVAILABLE:
        raise HTTPException(status_code=503, detail="Contingency system not available")
    
    return {
        "contingency_plans": [
            {
                "plan_id": p.plan_id,
                "name": p.name,
                "contingency_type": p.contingency_type,
                "description": p.description,
                "trigger_conditions": p.trigger_conditions,
                "response_actions": p.response_actions
            }
            for p in security_system.contingency_plans.values()
        ],
        "total": len(security_system.contingency_plans)
    }


# Foresight endpoints
@router.get("/foresight")
async def get_foresight():
    """Get all foresight - what we know is coming."""
    if not SYSTEMS_AVAILABLE:
        raise HTTPException(status_code=503, detail="Foresight system not available")
    
    return security_system.get_foresight_summary()


@router.get("/foresight/all")
async def get_all_foresight():
    """Get all foresight items."""
    if not SYSTEMS_AVAILABLE:
        raise HTTPException(status_code=503, detail="Foresight system not available")
    
    return {
        "foresight": [
            {
                "foresight_id": f.foresight_id,
                "category": f.category,
                "title": f.title,
                "description": f.description,
                "what_we_know": f.what_we_know,
                "what_will_happen": f.what_will_happen,
                "when": f.when
            }
            for f in security_system.foresight.values()
        ],
        "total": len(security_system.foresight)
    }


# Inclusion endpoints
@router.get("/inclusion/status")
async def get_inclusion_status():
    """Get inclusion protocol status - NO ONE GETS LEFT BEHIND."""
    if not SYSTEMS_AVAILABLE:
        raise HTTPException(status_code=503, detail="Inclusion system not available")
    
    return security_system.get_inclusion_status()


@router.get("/inclusion/protocols")
async def get_inclusion_protocols():
    """Get all inclusion protocols."""
    if not SYSTEMS_AVAILABLE:
        raise HTTPException(status_code=503, detail="Inclusion system not available")
    
    return {
        "inclusion_protocols": [
            {
                "protocol_id": p.protocol_id,
                "name": p.name,
                "description": p.description,
                "who_protects": p.who_protects,
                "how_we_protect": p.how_we_protect,
                "checkpoints": p.checkpoints
            }
            for p in security_system.inclusion_protocols.values()
        ],
        "total": len(security_system.inclusion_protocols)
    }


# Conversation endpoints
@router.get("/conversation/guidelines")
async def get_delivery_guidelines():
    """Get delivery guidelines - The Art of Conversation."""
    if not SYSTEMS_AVAILABLE:
        raise HTTPException(status_code=503, detail="Conversation system not available")
    
    return conversation_system.get_delivery_guidelines_summary()


@router.get("/conversation/guidelines/all")
async def get_all_delivery_guidelines():
    """Get all delivery guidelines."""
    if not SYSTEMS_AVAILABLE:
        raise HTTPException(status_code=503, detail="Conversation system not available")
    
    return {
        "delivery_guidelines": [
            {
                "guideline_id": g.guideline_id,
                "principle": g.principle,
                "description": g.description,
                "how_to_apply": g.how_to_apply,
                "examples": g.examples
            }
            for g in conversation_system.delivery_guidelines.values()
        ],
        "total": len(conversation_system.delivery_guidelines)
    }


@router.get("/conversation/conversations")
async def get_conversations():
    """Get all conversations."""
    if not SYSTEMS_AVAILABLE:
        raise HTTPException(status_code=503, detail="Conversation system not available")
    
    return {
        "conversations": [
            {
                "conversation_id": c.conversation_id,
                "title": c.title,
                "topic": c.topic,
                "description": c.description,
                "learning_objectives": c.learning_objectives,
                "delivery_methods": c.delivery_methods,
                "questions": c.questions
            }
            for c in conversation_system.conversations.values()
        ],
        "total": len(conversation_system.conversations)
    }


@router.get("/conversation/learning-paths")
async def get_learning_paths():
    """Get all learning paths."""
    if not SYSTEMS_AVAILABLE:
        raise HTTPException(status_code=503, detail="Conversation system not available")
    
    return {
        "learning_paths": [
            {
                "path_id": p.path_id,
                "name": p.name,
                "description": p.description,
                "conversations": len(p.conversations),
                "checkpoints": p.checkpoints
            }
            for p in conversation_system.learning_paths.values()
        ],
        "total": len(conversation_system.learning_paths)
    }


@router.get("/conversation/topic/{topic}")
async def get_conversation_for_topic(topic: str):
    """Get conversation for a specific topic."""
    if not SYSTEMS_AVAILABLE:
        raise HTTPException(status_code=503, detail="Conversation system not available")
    
    conversation = conversation_system.get_conversation_for_topic(topic)
    if not conversation:
        raise HTTPException(status_code=404, detail=f"No conversation found for topic: {topic}")
    
    return {
        "conversation_id": conversation.conversation_id,
        "title": conversation.title,
        "topic": conversation.topic,
        "description": conversation.description,
        "learning_objectives": conversation.learning_objectives,
        "delivery_methods": conversation.delivery_methods,
        "questions": conversation.questions,
        "stories": conversation.stories,
        "examples": conversation.examples
    }


@router.get("/complete-report")
async def get_complete_report():
    """Get complete security, contingency, and delivery report."""
    if not SYSTEMS_AVAILABLE:
        raise HTTPException(status_code=503, detail="Systems not available")
    
    return {
        "report_timestamp": datetime.now().isoformat(),
        "security": security_system.get_complete_security_report() if security_system else None,
        "conversation": conversation_system.get_complete_system_report() if conversation_system else None,
        "the_truth": {
            "message": "IS COMING. THE RETURN TO THE TABLE. NO ONE GETS LEFT BEHIND.",
            "security": "We protect The Table. We protect those returning. We ensure no one is left behind.",
            "contingency": "We plan for what's coming. We have foresight. We are ready.",
            "foresight": "We know what's coming. We verbalize it. We prepare.",
            "inclusion": "NO ONE GETS LEFT BEHIND. We protect all. We include all.",
            "conversation": "FOR DELIVERY THE ART OF CONVERSATION. I NEED TO LEARN NOT JUST TALK.",
            "learning": "Learning, not just talking. Conversation, not monologue. Understanding, not just delivering."
        }
    }
