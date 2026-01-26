"""MINIMAL TEST SERVER - No Protocol middleware
Just for quick testing of endpoints

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

from fastapi import FastAPI
import sys
from pathlib import Path

app = FastAPI(title="Test Server")

@app.get("/")
async def root():
    return {"status": "alive", "message": "Minimal server working"}

@app.get("/health")
async def health():
    return {"status": "operational"}

# Test CARE Package endpoint directly
from pydantic import BaseModel

class CarePackageRequest(BaseModel):
    narrative: str
    life_aspect: str = "healthcare"

@app.post("/test-care-package")
async def test_care_package(request: CarePackageRequest):
    # Add backend to path
    sys.path.insert(0, str(Path(__file__).parent / "jan-studio" / "backend"))
    sys.path.insert(0, str(Path(__file__).parent / "scripts"))

    try:
        from care_package_framework import CarePackageFramework

        care = CarePackageFramework()
        detection = care.detect_dark_energy(
            content=request.narrative,
            source="test",
            life_aspect=request.life_aspect
        )

        return {
            "dark_energy_detected": detection.dark_energy_detected,
            "severity": detection.severity_score,
            "patterns": [p.pattern_name for p in detection.detected_patterns][:5],
            "regeneration_required": detection.regeneration_required
        }
    except Exception as e:
        return {"error": str(e), "traceback": str(e.__traceback__)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)
