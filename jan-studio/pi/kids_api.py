"""
Kids-Friendly API for Raspberry Pi

Simplified API endpoints for kid-friendly interface.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Dict, Any
import os
from local_ai_service import get_tinyllama

app = FastAPI(title="JAN Studio Kids", version="1.0.0-kids")

# CORS for local network access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static files
STATIC_DIR = os.path.join(os.path.dirname(__file__), "frontend-kids")


class GenerationRequest(BaseModel):
    prompt: str
    max_length: int = 512
    temperature: float = 0.7


class GenerationResponse(BaseModel):
    content: str
    success: bool = True


@app.get("/")
async def root():
    """Serve kids-friendly frontend."""
    index_path = os.path.join(STATIC_DIR, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"message": "JAN Studio Kids API", "status": "running"}


@app.post("/api/generate", response_model=GenerationResponse)
async def generate_content(request: GenerationRequest):
    """Generate kid-friendly content."""
    try:
        tinyllama = get_tinyllama()
        
        # Make prompt more kid-friendly
        kid_prompt = f"Write a fun and exciting story for kids. {request.prompt} Make it appropriate for children ages 10-16. Keep it positive and engaging."
        
        content = tinyllama.generate(
            prompt=kid_prompt,
            max_length=request.max_length,
            temperature=request.temperature
        )
        
        # Clean up content for kids
        content = content.strip()
        if not content:
            content = "I'm still learning! Please try again with a different prompt."
        
        return GenerationResponse(
            content=content,
            success=True
        )
    except Exception as e:
        return GenerationResponse(
            content=f"Oops! Something went wrong: {str(e)}. Please try again!",
            success=False
        )


@app.get("/api/health")
async def health_check():
    """Health check for kids interface."""
    return {
        "status": "ready",
        "message": "Ready to create amazing stories!"
    }


# Mount static files
if os.path.exists(STATIC_DIR):
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        workers=1,
        log_level="info"
    )

