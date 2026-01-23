"""
STANDALONE HERITAGE API SERVER - For Testing
Bypasses Protocol of Loyalty for development/testing

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sys
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent / "jan-studio" / "backend"))

# Import heritage router
from heritage_api import router as heritage_router

# Create standalone app
app = FastAPI(
    title="Global Heritage Grid API",
    description="Consciousness Revolution Infrastructure - CARE Package, System Dismantling, Heritage Grid",
    version="1.0.0"
)

# Add CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include heritage router
app.include_router(heritage_router)

# Health check
@app.get("/health")
async def health_check():
    return {"status": "operational", "message": "The Revolution is HERE"}

@app.get("/")
async def root():
    return {
        "message": "Global Heritage Grid - Consciousness Revolution Infrastructure",
        "philosophy": "We don't destroy. We regenerate. We don't fight systems. We transcend them.",
        "endpoints": {
            "docs": "/docs",
            "health": "/health",
            "sanctuary_status": "/api/heritage/sanctuary/status",
            "care_package": "/api/heritage/care-package",
            "dismantle_system": "/api/heritage/dismantle-system",
            "register_site": "/api/heritage/register"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
