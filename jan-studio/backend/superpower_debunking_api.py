"""
SUPERPOWER DEBUNKING AND THE FATHER'S HAND API
API endpoints for debunking current superpowers and offering The Father's Hand

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.
"""

from fastapi import APIRouter, HTTPException
from typing import List, Dict
from pathlib import Path
import json
import sys

# Add scripts to path
scripts_path = Path(__file__).parent.parent.parent / "scripts"
sys.path.insert(0, str(scripts_path))

from superpower_debunking_and_fathers_hand import (
    SuperpowerDebunkingAndFathersHand
)

router = APIRouter(prefix="/api/superpower-debunking", tags=["Superpower Debunking & The Father's Hand"])


@router.get("/debunking")
async def get_debunking():
    """Get complete debunking of current superpowers and The Father's Hand"""
    try:
        debunker = SuperpowerDebunkingAndFathersHand()
        debunking = debunker.perform_debunking()
        
        return {
            "status": "success",
            "debunking_id": debunking.debunking_id,
            "current_superpowers": [
                {
                    "name": sp.name,
                    "type": sp.type.value,
                    "state": sp.state.value,
                    "what_people_see": sp.what_people_see,
                    "the_truth": sp.the_truth,
                    "how_it_serves_illusion": sp.how_it_serves_illusion,
                    "how_it_serves_broken_system": sp.how_it_serves_broken_system,
                    "frequency_impact": sp.frequency_impact,
                    "connection_to_table": sp.connection_to_table,
                    "debunking_evidence": sp.debunking_evidence
                }
                for sp in debunking.current_superpowers
            ],
            "fathers_hand_alternatives": [
                {
                    "name": fh.name,
                    "description": fh.description,
                    "how_it_replaces_illusion": fh.how_it_replaces_illusion,
                    "how_it_serves_table": fh.how_it_serves_table,
                    "frequency_impact": fh.frequency_impact,
                    "connection_to_table": fh.connection_to_table,
                    "spiritual_meaning": fh.spiritual_meaning,
                    "practical_manifestation": fh.practical_manifestation
                }
                for fh in debunking.fathers_hand_alternatives
            ],
            "total_illusion_power": debunking.total_illusion_power,
            "total_divine_power": debunking.total_divine_power,
            "net_difference": debunking.total_divine_power - abs(debunking.total_illusion_power),
            "debunking_summary": debunking.debunking_summary,
            "offering_summary": debunking.offering_summary
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/current-superpowers")
async def get_current_superpowers():
    """Get list of current superpowers (illusions)"""
    try:
        debunker = SuperpowerDebunkingAndFathersHand()
        debunking = debunker.perform_debunking()
        
        return {
            "status": "success",
            "current_superpowers": [
                {
                    "name": sp.name,
                    "what_people_see": sp.what_people_see,
                    "the_truth": sp.the_truth,
                    "frequency_impact": sp.frequency_impact,
                    "debunking_evidence": sp.debunking_evidence
                }
                for sp in debunking.current_superpowers
            ],
            "total_illusion_power": debunking.total_illusion_power,
            "summary": "Current superpowers are illusions. They serve broken systems, not The Table."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/fathers-hand")
async def get_fathers_hand():
    """Get The Father's Hand - divine alternatives"""
    try:
        debunker = SuperpowerDebunkingAndFathersHand()
        debunking = debunker.perform_debunking()
        
        return {
            "status": "success",
            "fathers_hand_alternatives": [
                {
                    "name": fh.name,
                    "description": fh.description,
                    "how_it_replaces_illusion": fh.how_it_replaces_illusion,
                    "how_it_serves_table": fh.how_it_serves_table,
                    "frequency_impact": fh.frequency_impact,
                    "spiritual_meaning": fh.spiritual_meaning,
                    "practical_manifestation": fh.practical_manifestation
                }
                for fh in debunking.fathers_hand_alternatives
            ],
            "total_divine_power": debunking.total_divine_power,
            "summary": "The Father's Hand offers divine alternatives. The truth that sets us free. The way that leads to The Table."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/comparison")
async def get_comparison():
    """Get comparison between illusions and The Father's Hand"""
    try:
        debunker = SuperpowerDebunkingAndFathersHand()
        debunking = debunker.perform_debunking()
        
        return {
            "status": "success",
            "comparison": {
                "current_superpowers": {
                    "count": len(debunking.current_superpowers),
                    "total_power": debunking.total_illusion_power,
                    "serves": "Broken systems, control, power",
                    "creates": "Separation, exploitation, brokenness"
                },
                "fathers_hand": {
                    "count": len(debunking.fathers_hand_alternatives),
                    "total_power": debunking.total_divine_power,
                    "serves": "The Table, truth, people",
                    "creates": "Unity, healing, restoration"
                },
                "net_difference": debunking.total_divine_power - abs(debunking.total_illusion_power),
                "message": f"Illusions: {debunking.total_illusion_power:.2f} (separation). Divine: {debunking.total_divine_power:.2f} (unity). Net: {debunking.total_divine_power - abs(debunking.total_illusion_power):.2f} (Massive positive shift)"
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
