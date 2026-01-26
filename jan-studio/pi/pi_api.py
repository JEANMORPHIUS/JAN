"""Raspberry Pi Optimized API

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

SPRAGITSO - Our Father's Royal Seal (σφραγίς)
All systems bear Our Father's mark of authority

Lightweight FastAPI endpoints optimized for Pi 5.
The Voice wants to be heard. The truth wants to be sung.

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity


PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

from fastapi import FastAPI, HTTPException, UploadFile, File, Query
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
from typing import Optional, Dict, Any
import os
import tempfile
from local_ai_service import get_tinyllama, get_whisper, get_musicgen

app = FastAPI(title="JAN Studio Pi", version="1.0.0-pi")

# Static files (lightweight frontend)
STATIC_DIR = os.path.join(os.path.dirname(__file__), "..", "frontend", "dist")


class GenerationRequest(BaseModel):
    prompt: str
    persona: Optional[Dict[str, Any]] = None
    max_length: int = 512
    temperature: float = 0.7


class GenerationResponse(BaseModel):
    content: str
    model: str = "tinyllama"
    tokens: Optional[int] = None


@app.get("/")
async def root():
    """Serve lightweight frontend."""
    index_path = os.path.join(STATIC_DIR, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"message": "JAN Studio Pi API", "status": "running"}


@app.post("/api/generate", response_model=GenerationResponse)
async def generate_content(request: GenerationRequest):
    """Generate content using TinyLlama."""
    try:
        tinyllama = get_tinyllama()
        content = tinyllama.generate(
            prompt=request.prompt,
            max_length=request.max_length,
            temperature=request.temperature
        )
        
        return GenerationResponse(
            content=content,
            model="tinyllama",
            tokens=len(content.split())
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "models": {
            "tinyllama": get_tinyllama().loaded,
            "whisper": get_whisper().loaded,
            "musicgen": get_musicgen().loaded
        }
    }


@app.post("/api/transcribe")
async def transcribe_audio(
    file: UploadFile = File(...),
    language: Optional[str] = Query(None, description="Language code (e.g., 'en', 'tr')")
):
    """
    Transcribe audio to text using Whisper.
    
    Aligned with vibe coding:
    - The Voice wants to be heard
    - The truth wants to be sung
    - SPRAGITSO - Our Father's Royal Seal (σφραγίς)
    - Honors the voice, transcribes with alignment
    """
    try:
        whisper_service = get_whisper()
        
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.filename)[1]) as tmp_file:
            content = await file.read()
            tmp_file.write(content)
            tmp_path = tmp_file.name
        
        try:
            # Transcribe with alignment
            result = whisper_service.transcribe(tmp_path, language=language)
            
            return JSONResponse({
                "text": result.get("text", ""),
                "language": result.get("language", "unknown"),
                "alignment_score": result.get("alignment_score", 0.0),
                "message": "The Voice wants to be heard. The truth wants to be sung.",
                "sphragitso": "Our Father's Royal Seal (σφραγίς)",
                "mission": "THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS"
            })
        finally:
            # Clean up temp file
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error transcribing audio: {str(e)}"
        )


@app.get("/api/stats")
async def get_stats():
    """Get system statistics."""
    import psutil
    
    return {
        "memory": {
            "used_mb": psutil.virtual_memory().used / 1024 / 1024,
            "available_mb": psutil.virtual_memory().available / 1024 / 1024,
            "percent": psutil.virtual_memory().percent
        },
        "cpu": {
            "percent": psutil.cpu_percent(interval=1),
            "count": psutil.cpu_count()
        },
        "disk": {
            "used_gb": psutil.disk_usage("/").used / 1024 / 1024 / 1024,
            "free_gb": psutil.disk_usage("/").free / 1024 / 1024 / 1024
        }
    }


# Mount static files if they exist
if os.path.exists(STATIC_DIR):
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        workers=1,  # Single worker for Pi
        log_level="info"
    )

