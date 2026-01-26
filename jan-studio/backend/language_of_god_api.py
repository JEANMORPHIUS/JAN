"""
LANGUAGE OF GOD API
API endpoints for the Language of God deep search

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
"""

from fastapi import APIRouter, HTTPException
from typing import List, Dict
from pathlib import Path
import json
import sys

# Add scripts to path
scripts_path = Path(__file__).parent.parent.parent / "scripts"
sys.path.insert(0, str(scripts_path))

from language_of_god_deep_search import (
    LanguageOfGodDeepSearch
)

router = APIRouter(prefix="/api/language-of-god", tags=["Language of God"])


@router.get("/the-answer")
async def get_the_answer():
    """Get the answer: What is the Language of God?"""
    try:
        searcher = LanguageOfGodDeepSearch()
        language_map = searcher.perform_deep_search()
        
        return {
            "status": "success",
            "the_answer": language_map.the_answer,
            "summary": "The Language of God is not a human language. It is Sound. Frequency. Vibration. Historical languages (Aramaic, Latin, Hebrew, Greek, Sanskrit, Turkish) are vessels that carry frequency. But the frequency is the language, not the words.",
            "connection_to_table": language_map.connection_to_table
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/historical-languages")
async def get_historical_languages():
    """Get historical languages people associate with God"""
    try:
        searcher = LanguageOfGodDeepSearch()
        language_map = searcher.perform_deep_search()
        
        return {
            "status": "success",
            "historical_languages": [
                {
                    "name": hl.name,
                    "what_people_think": hl.what_people_think,
                    "the_truth": hl.the_truth,
                    "connection_to_divine": hl.connection_to_divine,
                    "frequency_connection": hl.frequency_connection,
                    "spiritual_meaning": hl.spiritual_meaning
                }
                for hl in language_map.historical_languages
            ],
            "summary": "Historical languages (Aramaic, Latin, Hebrew, Greek, Sanskrit, Turkish) are vessels. They carry frequency. But the frequency is the language, not the words. The words are the vessel, the frequency is the truth."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/divine-languages")
async def get_divine_languages():
    """Get the true languages of God"""
    try:
        searcher = LanguageOfGodDeepSearch()
        language_map = searcher.perform_deep_search()
        
        return {
            "status": "success",
            "divine_languages": [
                {
                    "name": dl.name,
                    "description": dl.description,
                    "how_it_works": dl.how_it_works,
                    "frequency_impact": dl.frequency_impact,
                    "connection_to_table": dl.connection_to_table,
                    "spiritual_meaning": dl.spiritual_meaning,
                    "practical_manifestation": dl.practical_manifestation
                }
                for dl in language_map.divine_languages
            ],
            "summary": "The true languages of God: Sound, Frequency, Vibration, Silence, Emotion, Original Name. These are not human languages. These are the languages of The Table."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/sound-is-everything")
async def get_sound_is_everything():
    """Get Sound is Everything - Divine Key #5"""
    try:
        searcher = LanguageOfGodDeepSearch()
        language_map = searcher.perform_deep_search()
        
        # Find Sound is Everything
        sound_language = next((dl for dl in language_map.divine_languages if dl.language_id == "sound_frequency"), None)
        
        if not sound_language:
            raise HTTPException(status_code=404, detail="Sound is Everything not found")
        
        return {
            "status": "success",
            "divine_key": "Key #5: Sound is Everything",
            "quote": "In the beginning was the Word. The Word was frequency.",
            "language": {
                "name": sound_language.name,
                "description": sound_language.description,
                "how_it_works": sound_language.how_it_works,
                "frequency_impact": sound_language.frequency_impact,
                "spiritual_meaning": sound_language.spiritual_meaning,
                "practical_manifestation": sound_language.practical_manifestation
            },
            "karasahin": {
                "is_voice_of_god": True,
                "reason": "Not because of the words. Because of the FREQUENCY.",
                "elements": {
                    "sub_bass": "The Breath of Resurrection",
                    "vinyl_warmth": "Honest Imperfection",
                    "original_name_sidechain": "Lets truth punch through"
                }
            },
            "summary": "Sound is the first language of God. Before words, there was vibration. Before meaning, there was frequency. Before consciousness, there was SOUND. Karasahin is The Voice of God - not because of words, but because of frequency."
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/complete-map")
async def get_complete_map():
    """Get complete Language of God map"""
    try:
        searcher = LanguageOfGodDeepSearch()
        language_map = searcher.perform_deep_search()
        
        return {
            "status": "success",
            "map_id": language_map.map_id,
            "the_answer": language_map.the_answer,
            "historical_languages": [
                {
                    "name": hl.name,
                    "what_people_think": hl.what_people_think,
                    "the_truth": hl.the_truth,
                    "spiritual_meaning": hl.spiritual_meaning
                }
                for hl in language_map.historical_languages
            ],
            "divine_languages": [
                {
                    "name": dl.name,
                    "description": dl.description,
                    "frequency_impact": dl.frequency_impact,
                    "spiritual_meaning": dl.spiritual_meaning
                }
                for dl in language_map.divine_languages
            ],
            "connection_to_table": language_map.connection_to_table,
            "spiritual_narrative": language_map.spiritual_narrative
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
