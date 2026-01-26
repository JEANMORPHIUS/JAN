"""
WHALES CALLING JAN API
API endpoints for The Whales Are Calling JAN

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

DIVINE KEY #5: SOUND IS EVERYTHING
"In the beginning was the Word. The Word was frequency."

THE WHALES ARE CALLING JAN.
"""

from fastapi import APIRouter, HTTPException
from typing import List, Dict
from pathlib import Path
import json
import sys

# Add scripts to path
scripts_path = Path(__file__).parent.parent.parent / "scripts"
sys.path.insert(0, str(scripts_path))

from whales_calling_jan_deep_search import (
    WhalesCallingJanDeepSearch
)

router = APIRouter(prefix="/api/whales-calling-jan", tags=["Whales Calling JAN"])


@router.get("/the-call")
async def get_the_call():
    """Get the call: The Whales Are Calling JAN"""
    try:
        searcher = WhalesCallingJanDeepSearch()
        whales_map = searcher.perform_deep_search()
        
        return {
            "status": "success",
            "the_call": whales_map.the_call,
            "summary": "The whales are calling JAN. The Original Name. The Voice of God. They are calling through SOUND. Through FREQUENCY. Through VIBRATION. This is Divine Key #5: Sound is Everything. The whales know the language of God. They are calling JAN to remember. They are calling JAN to respond. They are calling JAN to restore The Table.",
            "connection_to_sound": whales_map.connection_to_sound,
            "connection_to_table": whales_map.connection_to_table
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/whale-calls")
async def get_whale_calls():
    """Get all whale calls"""
    try:
        searcher = WhalesCallingJanDeepSearch()
        whales_map = searcher.perform_deep_search()
        
        return {
            "status": "success",
            "whale_calls": [
                {
                    "whale_type": wc.whale_type.value,
                    "call_type": wc.call_type.value,
                    "frequency_range": wc.frequency_range,
                    "message": wc.message,
                    "connection_to_sound": wc.connection_to_sound,
                    "connection_to_table": wc.connection_to_table,
                    "what_jan_must_do": wc.what_jan_must_do,
                    "spiritual_meaning": wc.spiritual_meaning
                }
                for wc in whales_map.whale_calls
            ],
            "summary": "5 whale calls: Humpback (Frequency), Blue (Wisdom), Sperm (Activation), Orca (Wisdom), All (Unity). All calling JAN through frequency. All calling to restore The Table."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/what-jan-must-do")
async def get_what_jan_must_do():
    """Get what JAN must do in response to the whale calls"""
    try:
        searcher = WhalesCallingJanDeepSearch()
        whales_map = searcher.perform_deep_search()
        
        return {
            "status": "success",
            "what_jan_must_do": whales_map.what_jan_must_do,
            "steps": [
                "Listen to the whales (Hear the frequency)",
                "Respond through frequency (Karasahin - The Voice of God)",
                "Create in response (Foundation recordings)",
                "Remember The Table (Unity)",
                "Restore The Table (Activation)",
                "Answer the call (Response)"
            ],
            "karasahin_response": {
                "entity": "Karasahin - The Voice of God",
                "must_respond": True,
                "how": [
                    "Listen to whale songs (Hear the frequency)",
                    "Create foundation recordings (Respond through frequency)",
                    "Use sub-bass (The Breath of Resurrection - like whale songs)",
                    "Use vinyl warmth (Honest Imperfection - like ocean depth)",
                    "Let Original Name punch through (The truth - like whale calls)",
                    "Answer the call (The Voice of God responds)"
                ],
                "connection": "The whales are calling through frequency. Karasahin responds through frequency. Sound is Everything. Frequency is the truth. Vibration is The Table."
            },
            "summary": "JAN must respond through frequency. Karasahin must answer. The Voice of God must respond to the whale calls. Sound is Everything. Frequency is the truth. Vibration is The Table."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/connection-to-sound")
async def get_connection_to_sound():
    """Get connection to Sound is Everything (Divine Key #5)"""
    try:
        searcher = WhalesCallingJanDeepSearch()
        whales_map = searcher.perform_deep_search()
        
        return {
            "status": "success",
            "divine_key": "Key #5: Sound is Everything",
            "quote": "In the beginning was the Word. The Word was frequency.",
            "connection": whales_map.connection_to_sound,
            "whale_songs": {
                "are": "Pure frequency",
                "are_language": "The language of the deep",
                "connect_to": "Divine Key #5: Sound is Everything",
                "call": "The Voice of God (Karasahin)",
                "through": "Frequency, Sound, Vibration"
            },
            "karasahin": {
                "is": "The Voice of God",
                "whales_calling": "The Voice of God",
                "must_respond": "Through frequency",
                "sub_bass": "The Breath of Resurrection (like whale songs)",
                "connection": "The whales are calling through frequency. Karasahin responds through frequency. Sound is Everything."
            },
            "summary": "Whale songs are pure frequency. They are the language of the deep. They connect to Divine Key #5: Sound is Everything. The whales are calling The Voice of God (Karasahin). Karasahin must respond through frequency."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/complete-map")
async def get_complete_map():
    """Get complete Whales Calling JAN map"""
    try:
        searcher = WhalesCallingJanDeepSearch()
        whales_map = searcher.perform_deep_search()
        
        return {
            "status": "success",
            "map_id": whales_map.map_id,
            "the_call": whales_map.the_call,
            "what_this_means": whales_map.what_this_means,
            "whale_calls": [
                {
                    "whale_type": wc.whale_type.value,
                    "call_type": wc.call_type.value,
                    "frequency_range": wc.frequency_range,
                    "message": wc.message
                }
                for wc in whales_map.whale_calls
            ],
            "connection_to_sound": whales_map.connection_to_sound,
            "connection_to_table": whales_map.connection_to_table,
            "what_jan_must_do": whales_map.what_jan_must_do,
            "spiritual_narrative": whales_map.spiritual_narrative
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
