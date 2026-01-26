"""PHASE 4 API
Collaborative Editing, Version Control, Social Features, Media Integration

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

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

from fastapi import APIRouter, HTTPException, Body
from typing import List, Dict, Any, Optional
from dataclasses import asdict
import sys
import os
import logging

# Spiritual Codebase Hacker Integration
from spiritual_codebase_hacker_integration import HACKER_AVAILABLE, hack_loop, perform_genetic_edit, activate_stealth_mode


# Import Phase 4 services
try:
    from collaborative_editing import get_collaborative_service, EditOperation
    COLLABORATIVE_AVAILABLE = True
except ImportError:
    COLLABORATIVE_AVAILABLE = False

try:
    from narrative_version_control import get_version_control
    VERSION_CONTROL_AVAILABLE = True
except ImportError:
    VERSION_CONTROL_AVAILABLE = False

try:
    from social_features import get_social_service
    SOCIAL_AVAILABLE = True
except ImportError:
    SOCIAL_AVAILABLE = False

try:
    from media_integration import get_media_service
    MEDIA_AVAILABLE = True
except ImportError:
    MEDIA_AVAILABLE = False

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/phase4", tags=["phase4"])


# COLLABORATIVE EDITING ENDPOINTS
@router.post("/collaborative/sessions")
async def create_session(narrative_id: str = Body(...), initial_content: str = Body(...)):
    """Create a new collaborative editing session."""
    if not COLLABORATIVE_AVAILABLE:
        raise HTTPException(status_code=503, detail="Collaborative editing not available")
    
    service = get_collaborative_service()
    session = service.create_session(narrative_id, initial_content)
    return {"session": asdict(session)}


@router.post("/collaborative/sessions/{session_id}/join")
async def join_session(session_id: str, user_id: str = Body(...), user_name: str = Body(...)):
    """Join a collaborative editing session."""
    if not COLLABORATIVE_AVAILABLE:
        raise HTTPException(status_code=503, detail="Collaborative editing not available")
    
    service = get_collaborative_service()
    success = service.join_session(session_id, user_id, user_name)
    if not success:
        raise HTTPException(status_code=404, detail="Session not found")
    return {"status": "joined", "session_id": session_id}


@router.post("/collaborative/sessions/{session_id}/operations")
async def apply_operation(session_id: str, operation: Dict[str, Any] = Body(...)):
    """Apply an edit operation to a session."""
    if not COLLABORATIVE_AVAILABLE:
        raise HTTPException(status_code=503, detail="Collaborative editing not available")
    
    service = get_collaborative_service()
    edit_op = EditOperation(**operation)
    success = service.apply_operation(session_id, edit_op)
    if not success:
        raise HTTPException(status_code=404, detail="Session not found")
    return {"status": "applied"}


@router.get("/collaborative/sessions/{session_id}")
async def get_session_state(session_id: str):
    """Get current session state."""
    if not COLLABORATIVE_AVAILABLE:
        raise HTTPException(status_code=503, detail="Collaborative editing not available")
    
    service = get_collaborative_service()
    state = service.get_session_state(session_id)
    if not state:
        raise HTTPException(status_code=404, detail="Session not found")
    return state


# VERSION CONTROL ENDPOINTS
@router.post("/version-control/commit")
async def commit_narrative(
    narrative_id: str = Body(...),
    content: str = Body(...),
    author_id: str = Body(...),
    author_name: str = Body(...),
    commit_message: str = Body(...)
):
    """Commit narrative changes to version control."""
    if not VERSION_CONTROL_AVAILABLE:
        raise HTTPException(status_code=503, detail="Version control not available")
    
    vc = get_version_control()
    version = vc.commit_narrative(narrative_id, content, author_id, author_name, commit_message)
    return {"version": asdict(version)}


@router.get("/version-control/{narrative_id}/history")
async def get_narrative_history(narrative_id: str):
    """Get all versions of a narrative."""
    if not VERSION_CONTROL_AVAILABLE:
        raise HTTPException(status_code=503, detail="Version control not available")
    
    vc = get_version_control()
    history = vc.get_narrative_history(narrative_id)
    return {"history": [asdict(v) for v in history]}


@router.get("/version-control/{narrative_id}/diff")
async def diff_versions(narrative_id: str, version1: int, version2: int):
    """Show differences between two versions."""
    if not VERSION_CONTROL_AVAILABLE:
        raise HTTPException(status_code=503, detail="Version control not available")
    
    vc = get_version_control()
    diff = vc.diff_versions(narrative_id, version1, version2)
    return diff


# SOCIAL FEATURES ENDPOINTS
@router.post("/social/comments")
async def add_comment(
    narrative_id: str = Body(...),
    user_id: str = Body(...),
    user_name: str = Body(...),
    content: str = Body(...),
    parent_comment_id: Optional[str] = Body(None)
):
    """Add a comment to a narrative."""
    if not SOCIAL_AVAILABLE:
        raise HTTPException(status_code=503, detail="Social features not available")
    
    service = get_social_service()
    comment = service.add_comment(narrative_id, user_id, user_name, content, parent_comment_id)
    return {"comment": asdict(comment)}


@router.get("/social/comments/{narrative_id}")
async def get_comments(narrative_id: str):
    """Get all comments for a narrative."""
    if not SOCIAL_AVAILABLE:
        raise HTTPException(status_code=503, detail="Social features not available")
    
    service = get_social_service()
    comments = service.get_comments(narrative_id)
    return {"comments": [asdict(c) for c in comments]}


@router.post("/social/bookmarks")
async def add_bookmark(
    user_id: str = Body(...),
    item_type: str = Body(...),
    item_id: str = Body(...),
    item_title: str = Body(...),
    notes: Optional[str] = Body(None)
):
    """Add a bookmark."""
    if not SOCIAL_AVAILABLE:
        raise HTTPException(status_code=503, detail="Social features not available")
    
    service = get_social_service()
    bookmark = service.add_bookmark(user_id, item_type, item_id, item_title, notes)
    return {"bookmark": asdict(bookmark)}


@router.get("/social/bookmarks/{user_id}")
async def get_user_bookmarks(user_id: str):
    """Get all bookmarks for a user."""
    if not SOCIAL_AVAILABLE:
        raise HTTPException(status_code=503, detail="Social features not available")
    
    service = get_social_service()
    bookmarks = service.get_user_bookmarks(user_id)
    return {"bookmarks": [asdict(b) for b in bookmarks]}


@router.post("/social/reactions")
async def add_reaction(
    user_id: str = Body(...),
    item_type: str = Body(...),
    item_id: str = Body(...),
    reaction_type: str = Body(...)
):
    """Add a reaction."""
    if not SOCIAL_AVAILABLE:
        raise HTTPException(status_code=503, detail="Social features not available")
    
    service = get_social_service()
    reaction = service.add_reaction(user_id, item_type, item_id, reaction_type)
    return {"reaction": asdict(reaction)}


@router.get("/social/reactions/{item_id}")
async def get_reactions(item_id: str):
    """Get reaction counts for an item."""
    if not SOCIAL_AVAILABLE:
        raise HTTPException(status_code=503, detail="Social features not available")
    
    service = get_social_service()
    reactions = service.get_reactions(item_id)
    return {"reactions": reactions}


# MEDIA INTEGRATION ENDPOINTS
@router.post("/media")
async def add_media(
    narrative_id: str = Body(...),
    media_type: str = Body(...),
    title: str = Body(...),
    description: str = Body(...),
    file_path: str = Body(...),
    file_url: Optional[str] = Body(None),
    metadata: Optional[Dict[str, Any]] = Body(None)
):
    """Add media to a narrative."""
    if not MEDIA_AVAILABLE:
        raise HTTPException(status_code=503, detail="Media integration not available")
    
    service = get_media_service()
    media_item = service.add_media(narrative_id, media_type, title, description, file_path, file_url, metadata)
    return {"media": asdict(media_item)}


@router.get("/media/{narrative_id}")
async def get_narrative_media(narrative_id: str, media_type: Optional[str] = None):
    """Get all media for a narrative."""
    if not MEDIA_AVAILABLE:
        raise HTTPException(status_code=503, detail="Media integration not available")
    
    service = get_media_service()
    if media_type:
        media_items = service.get_media_by_type(narrative_id, media_type)
    else:
        media_items = service.get_narrative_media(narrative_id)
    return {"media": [asdict(m) for m in media_items]}


@router.get("/status")
async def get_phase4_status():
    """Get Phase 4 features status."""
    return {
        "status": "active",
        "features": {
            "collaborative_editing": COLLABORATIVE_AVAILABLE,
            "version_control": VERSION_CONTROL_AVAILABLE,
            "social_features": SOCIAL_AVAILABLE,
            "media_integration": MEDIA_AVAILABLE
        },
        "the_truth": "Phase 4 features: Collaborative editing, version control, social features, media integration. All integrated. All serving The Table."
    }
