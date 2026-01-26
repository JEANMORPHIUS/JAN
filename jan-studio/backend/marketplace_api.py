"""Marketplace API Endpoints

API for browsing, submitting, downloading, and rating JAN personas.

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, EmailStr
from typing import Optional, List, Dict, Any
from datetime import datetime
import marketplace_db as db

# Spiritual Codebase Hacker Integration
from spiritual_codebase_hacker_integration import HACKER_AVAILABLE, hack_loop, perform_genetic_edit, activate_stealth_mode


router = APIRouter(prefix="/api/marketplace", tags=["Marketplace"])


class PersonaCreateRequest(BaseModel):
    name: str
    author_username: str
    author_email: str
    description: str
    category: Optional[str] = None
    files: List[Dict[str, str]]  # [{"path": "profile.md", "content": "..."}]


class PersonaResponse(BaseModel):
    id: int
    name: str
    author_name: Optional[str]
    description: Optional[str]
    category: Optional[str]
    downloads: int
    rating: float
    rating_count: int
    version: str
    status: str
    created_at: str
    updated_at: str


class DownloadRequest(BaseModel):
    user_id: Optional[int] = None
    username: Optional[str] = None


class RatingRequest(BaseModel):
    user_id: Optional[int] = None
    username: Optional[str] = None
    rating: int  # 1-5
    comment: Optional[str] = None


@router.get("/personas")
async def browse_personas(
    category: Optional[str] = Query(None, description="Filter by category"),
    status: str = Query("approved", description="Filter by status"),
    limit: int = Query(50, ge=1, le=100),
    offset: int = Query(0, ge=0),
    sort_by: str = Query("downloads", description="Sort by: downloads, rating, created_at, updated_at")
) -> List[PersonaResponse]:
    """Browse available personas in the marketplace."""
    try:
        personas = db.list_personas(
            category=category,
            status=status,
            limit=limit,
            offset=offset,
            sort_by=sort_by
        )
        return [PersonaResponse(**p) for p in personas]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/personas/{persona_id}")
async def get_persona_details(persona_id: int) -> Dict[str, Any]:
    """Get detailed information about a persona."""
    try:
        persona = db.get_persona(persona_id)
        if not persona:
            raise HTTPException(status_code=404, detail="Persona not found")
        
        files = db.get_persona_files(persona_id)
        ratings = db.get_ratings(persona_id)
        
        return {
            "persona": PersonaResponse(**persona),
            "files": files,
            "ratings": ratings
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/personas")
async def submit_persona(request: PersonaCreateRequest) -> Dict[str, Any]:
    """Submit a new persona to the marketplace."""
    try:
        # Get or create user
        user = db.get_user_by_username(request.author_username)
        if not user:
            user_id = db.create_user(request.author_username, request.author_email)
        else:
            user_id = user["id"]
        
        # Check if persona name already exists
        existing = db.list_personas(status="all")
        if any(p["name"] == request.name for p in existing):
            raise HTTPException(status_code=409, detail="Persona name already exists")
        
        # Create persona
        persona_id = db.create_persona(
            name=request.name,
            author_id=user_id,
            description=request.description,
            category=request.category,
            files=request.files
        )
        
        return {
            "message": "Persona submitted successfully",
            "persona_id": persona_id,
            "status": "pending"
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/personas/{persona_id}/download")
async def download_persona(persona_id: int, request: DownloadRequest) -> Dict[str, Any]:
    """Download a persona and record the download."""
    try:
        persona = db.get_persona(persona_id)
        if not persona:
            raise HTTPException(status_code=404, detail="Persona not found")
        
        if persona["status"] != "approved":
            raise HTTPException(status_code=403, detail="Persona not available for download")
        
        # Get user ID if provided
        user_id = request.user_id
        if not user_id and request.username:
            user = db.get_user_by_username(request.username)
            user_id = user["id"] if user else None
        
        # Record download
        db.record_download(user_id, persona_id)
        
        # Get files
        files = db.get_persona_files(persona_id)
        
        return {
            "message": "Download successful",
            "persona": PersonaResponse(**persona),
            "files": files
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/personas/{persona_id}/rate")
async def rate_persona(persona_id: int, request: RatingRequest) -> Dict[str, Any]:
    """Rate a persona."""
    try:
        if request.rating < 1 or request.rating > 5:
            raise HTTPException(status_code=400, detail="Rating must be between 1 and 5")
        
        persona = db.get_persona(persona_id)
        if not persona:
            raise HTTPException(status_code=404, detail="Persona not found")
        
        # Get user ID if provided
        user_id = request.user_id
        if not user_id and request.username:
            user = db.get_user_by_username(request.username)
            user_id = user["id"] if user else None
        
        # Add rating
        db.add_rating(user_id, persona_id, request.rating, request.comment)
        
        # Get updated persona
        updated_persona = db.get_persona(persona_id)
        
        return {
            "message": "Rating submitted successfully",
            "persona": PersonaResponse(**updated_persona)
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/categories")
async def get_categories() -> List[str]:
    """Get list of available categories."""
    try:
        with db.get_db() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT DISTINCT category FROM personas WHERE category IS NOT NULL AND status = 'approved'")
            return [row[0] for row in cursor.fetchall()]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

