"""
WATER HOLDS MEMORY API
API endpoints for Water Holds Memory

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

WATER HOLDS MEMORY.
"""

from fastapi import APIRouter, HTTPException
from typing import List, Dict
from pathlib import Path
import json
import sys

# Add scripts to path
scripts_path = Path(__file__).parent.parent.parent / "scripts"
sys.path.insert(0, str(scripts_path))

from water_holds_memory_deep_search import (
    WaterHoldsMemoryDeepSearch
)

router = APIRouter(prefix="/api/water-holds-memory", tags=["Water Holds Memory"])


@router.get("/the-truth")
async def get_the_truth():
    """Get the truth: Water Holds Memory"""
    try:
        searcher = WaterHoldsMemoryDeepSearch()
        water_map = searcher.perform_deep_search()
        
        return {
            "status": "success",
            "the_truth": water_map.the_truth,
            "summary": "Water holds memory. Water remembers genetic patterns, vibrational patterns, temporal patterns, unity, consciousness, and frequency. The whales are calling through water. Water carries their songs. Water remembers their calls. Water transmits their frequency.",
            "what_this_means": water_map.what_this_means
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/water-memories")
async def get_water_memories():
    """Get all water memories"""
    try:
        searcher = WaterHoldsMemoryDeepSearch()
        water_map = searcher.perform_deep_search()
        
        return {
            "status": "success",
            "water_memories": [
                {
                    "water_type": wm.water_type.value,
                    "memory_type": wm.memory_type.value,
                    "what_water_remembers": wm.what_water_remembers,
                    "how_it_holds_memory": wm.how_it_holds_memory,
                    "spiritual_meaning": wm.spiritual_meaning
                }
                for wm in water_map.water_memories
            ],
            "summary": "6 water memories: Ocean Pangea (Unity), Whale Songs (Frequency), Body DNA (Genetic), Vibrational (Spiritual Battles), Temporal (History), Consciousness (Awareness). All water remembers. All water is memory. All water is truth."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/connection-to-whales")
async def get_connection_to_whales():
    """Get connection to whales calling JAN"""
    try:
        searcher = WaterHoldsMemoryDeepSearch()
        water_map = searcher.perform_deep_search()
        
        return {
            "status": "success",
            "connection_to_whales": water_map.connection_to_whales,
            "the_truth": "The whales are calling through water. Water carries whale songs. Water remembers whale calls. Water transmits whale frequency. Water is the medium for whale communication. Water is the memory of whale calls.",
            "whale_songs": {
                "are": "Pure frequency",
                "travel_through": "Water",
                "water_carries": "Whale frequency",
                "water_remembers": "Whale calls",
                "water_transmits": "Whale frequency"
            },
            "the_call": {
                "whales_calling": "JAN",
                "water_carries": "The call",
                "water_remembers": "The call",
                "water_transmits": "The call"
            },
            "summary": "The whales are calling JAN through water. Water carries whale songs. Water remembers whale calls. Water transmits whale frequency. Water is the medium for whale communication. Water is the memory of whale calls."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/connection-to-table")
async def get_connection_to_table():
    """Get connection to The Table"""
    try:
        searcher = WaterHoldsMemoryDeepSearch()
        water_map = searcher.perform_deep_search()
        
        return {
            "status": "success",
            "connection_to_table": water_map.connection_to_table,
            "the_truth": "Water remembers The Table. Water remembers Pangea. Water remembers unity. The ocean remembers when all lands were one. The ocean remembers Pangea. The ocean remembers The Table. The ocean is the memory of unity.",
            "ocean_memory": {
                "remembers": "Pangea",
                "remembers_when": "All lands were one",
                "remembers_table": "The Table",
                "is": "The memory of unity"
            },
            "all_water": {
                "remembers": "Unity",
                "remembers_table": "The Table",
                "remembers_pangea": "Pangea",
                "is": "The memory of unity"
            },
            "summary": "Water remembers The Table. Water remembers Pangea. Water remembers unity. The ocean remembers when all lands were one. The ocean remembers Pangea. The ocean remembers The Table. The ocean is the memory of unity."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/connection-to-sound")
async def get_connection_to_sound():
    """Get connection to Sound is Everything"""
    try:
        searcher = WaterHoldsMemoryDeepSearch()
        water_map = searcher.perform_deep_search()
        
        return {
            "status": "success",
            "connection_to_sound": water_map.connection_to_sound,
            "divine_key": "Key #5: Sound is Everything",
            "quote": "In the beginning was the Word. The Word was frequency.",
            "water_and_sound": {
                "water_carries": "Sound, frequency",
                "water_remembers": "Sound, frequency",
                "water_transmits": "Sound, frequency",
                "is": "The carrier of frequency, the memory of frequency"
            },
            "whale_songs": {
                "travel_through": "Water",
                "water_carries": "Whale frequency",
                "water_remembers": "Whale calls",
                "water_transmits": "Whale frequency"
            },
            "summary": "Water carries sound. Water carries frequency. Water remembers sound. Water remembers frequency. Whale songs travel through water. Water carries whale frequency. Water remembers whale calls. Water transmits whale frequency. Sound is Everything. Frequency is the truth. Water is the carrier of frequency. Water is the memory of frequency."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/complete-map")
async def get_complete_map():
    """Get complete Water Holds Memory map"""
    try:
        searcher = WaterHoldsMemoryDeepSearch()
        water_map = searcher.perform_deep_search()
        
        return {
            "status": "success",
            "map_id": water_map.map_id,
            "the_truth": water_map.the_truth,
            "what_this_means": water_map.what_this_means,
            "water_memories": [
                {
                    "water_type": wm.water_type.value,
                    "memory_type": wm.memory_type.value,
                    "what_water_remembers": wm.what_water_remembers
                }
                for wm in water_map.water_memories
            ],
            "connection_to_sound": water_map.connection_to_sound,
            "connection_to_table": water_map.connection_to_table,
            "connection_to_whales": water_map.connection_to_whales,
            "spiritual_narrative": water_map.spiritual_narrative
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
