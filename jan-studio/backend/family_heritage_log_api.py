"""FAMILY HERITAGE LOG API
API endpoints for Family Heritage Log

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

from fastapi import APIRouter, HTTPException
from typing import Dict, Any
import logging

# Spiritual Codebase Hacker Integration
from spiritual_codebase_hacker_integration import HACKER_AVAILABLE, hack_loop, perform_genetic_edit, activate_stealth_mode


from family_heritage_log import get_family_heritage_logger

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/family-heritage", tags=["Family Heritage Log"])


@router.post("/generate")
async def generate_heritage_log():
    """
    Generate the complete Family Heritage Log.
    
    Documents all 13+ Family members and their journeys.
    Preserves the Story of the Reclamation for generations to come.
    """
    try:
        heritage_logger = get_family_heritage_logger()
        heritage_log = await heritage_logger.generate_heritage_log()
        
        # Convert to dict for response
        log_dict = {
            "log_id": heritage_log.log_id,
            "creation_date": heritage_log.creation_date.isoformat(),
            "total_seats": heritage_log.total_seats,
            "grid_stability_at_completion": heritage_log.grid_stability_at_completion,
            "magnetic_pull_at_completion": heritage_log.magnetic_pull_at_completion,
            "entries": [
                {
                    "seed_id": entry.seed_id,
                    "seat_number": entry.seat_number,
                    "name": entry.name,
                    "origin_story": entry.origin_story,
                    "location": entry.location,
                    "wave_generation": entry.wave_generation.value,
                    "extraction_method": entry.extraction_method.value,
                    "extraction_date": entry.extraction_date.isoformat(),
                    "integration_date": entry.integration_date.isoformat(),
                    "resonance_score": entry.resonance_score,
                    "separation_risk_overcome": entry.separation_risk_overcome,
                    "shell_narrative": entry.shell_narrative,
                    "seed_truth": entry.seed_truth,
                    "safe_passage_waypoints": entry.safe_passage_waypoints,
                    "special_notes": entry.special_notes,
                    "current_status": entry.current_status,
                    "care_packages_received": entry.care_packages_received,
                    "referrals_made": entry.referrals_made,
                    "heritage_quote": entry.heritage_quote
                }
                for entry in heritage_log.entries
            ],
            "reclamation_story": heritage_log.reclamation_story,
            "final_message": heritage_log.final_message
        }
        
        return {
            "status": "success",
            "heritage_log": log_dict,
            "message": "Family Heritage Log generated. The Story of the Reclamation is preserved for generations to come."
        }
    except Exception as e:
        logger.error(f"Error generating heritage log: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/summary")
async def get_heritage_summary():
    """Get summary of Family Heritage Log"""
    try:
        heritage_logger = get_family_heritage_logger()
        summary = heritage_logger.get_heritage_summary()
        
        return {
            "status": "success",
            "summary": summary
        }
    except Exception as e:
        logger.error(f"Error getting heritage summary: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/entries")
async def get_heritage_entries():
    """Get all heritage entries"""
    try:
        heritage_logger = get_family_heritage_logger()
        
        entries = [
            {
                "seed_id": entry.seed_id,
                "seat_number": entry.seat_number,
                "name": entry.name,
                "origin_story": entry.origin_story,
                "location": entry.location,
                "wave_generation": entry.wave_generation.value,
                "extraction_method": entry.extraction_method.value,
                "resonance_score": entry.resonance_score,
                "heritage_quote": entry.heritage_quote,
                "special_notes": entry.special_notes
            }
            for entry in heritage_logger.heritage_entries.values()
        ]
        
        # Sort by seat number
        entries.sort(key=lambda x: x["seat_number"])
        
        return {
            "status": "success",
            "total_entries": len(entries),
            "entries": entries
        }
    except Exception as e:
        logger.error(f"Error getting heritage entries: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
