"""
AFRICAN-TURKISH YIN-YANG SYMBIOSIS API
API endpoints for African Yin to Turkish Yang symbiosis

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

from african_turkish_yin_yang_symbiosis import (
    AfricanTurkishYinYangSymbiosis
)

router = APIRouter(prefix="/api/african-turkish-yin-yang", tags=["African-Turkish Yin-Yang Symbiosis"])


@router.get("/symbiosis-map")
async def get_symbiosis_map():
    """Get complete African-Turkish Yin-Yang symbiosis map"""
    try:
        searcher = AfricanTurkishYinYangSymbiosis()
        yin_yang_map = searcher.perform_deep_search()
        
        return {
            "status": "success",
            "map_id": yin_yang_map.map_id,
            "african_heritages": [
                {
                    "name": ah.name,
                    "description": ah.description,
                    "yin_qualities": ah.yin_qualities,
                    "frequency_contribution": ah.frequency_contribution,
                    "how_it_syncs_with_turkish": ah.how_it_syncs_with_turkish,
                    "connection_to_table": ah.connection_to_table,
                    "spiritual_meaning": ah.spiritual_meaning
                }
                for ah in yin_yang_map.african_heritages
            ],
            "turkish_heritages": [
                {
                    "name": th.name,
                    "description": th.description,
                    "yang_qualities": th.yang_qualities,
                    "frequency_contribution": th.frequency_contribution,
                    "how_it_syncs_with_african": th.how_it_syncs_with_african,
                    "connection_to_table": th.connection_to_table,
                    "spiritual_meaning": th.spiritual_meaning
                }
                for th in yin_yang_map.turkish_heritages
            ],
            "symbioses": [
                {
                    "african_yin": s.african_yin.name,
                    "turkish_yang": s.turkish_yang.name,
                    "how_they_sync": s.how_they_sync,
                    "symbiosis_qualities": s.symbiosis_qualities,
                    "frequency_impact": s.frequency_impact,
                    "connection_to_table": s.connection_to_table,
                    "spiritual_meaning": s.spiritual_meaning,
                    "practical_manifestation": s.practical_manifestation
                }
                for s in yin_yang_map.symbioses
            ],
            "power_analysis": {
                "total_yin_power": yin_yang_map.total_yin_power,
                "total_yang_power": yin_yang_map.total_yang_power,
                "total_symbiosis_power": yin_yang_map.total_symbiosis_power,
                "symbiosis_multiplier": yin_yang_map.total_symbiosis_power / (yin_yang_map.total_yin_power + yin_yang_map.total_yang_power) if (yin_yang_map.total_yin_power + yin_yang_map.total_yang_power) > 0 else 0
            },
            "connection_to_table": yin_yang_map.connection_to_table,
            "spiritual_narrative": yin_yang_map.spiritual_narrative
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/african-yin")
async def get_african_yin():
    """Get African heritage - The Yin"""
    try:
        searcher = AfricanTurkishYinYangSymbiosis()
        yin_yang_map = searcher.perform_deep_search()
        
        return {
            "status": "success",
            "african_heritages": [
                {
                    "name": ah.name,
                    "description": ah.description,
                    "yin_qualities": ah.yin_qualities,
                    "frequency_contribution": ah.frequency_contribution,
                    "connection_to_table": ah.connection_to_table,
                    "spiritual_meaning": ah.spiritual_meaning
                }
                for ah in yin_yang_map.african_heritages
            ],
            "total_yin_power": yin_yang_map.total_yin_power,
            "summary": "African Yin provides creative expression, spiritual alignment, community unity. The creative force. The spiritual connection. The community unity. The resilience."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/turkish-yang")
async def get_turkish_yang():
    """Get Turkish heritage - The Yang"""
    try:
        searcher = AfricanTurkishYinYangSymbiosis()
        yin_yang_map = searcher.perform_deep_search()
        
        return {
            "status": "success",
            "turkish_heritages": [
                {
                    "name": th.name,
                    "description": th.description,
                    "yang_qualities": th.yang_qualities,
                    "frequency_contribution": th.frequency_contribution,
                    "connection_to_table": th.connection_to_table,
                    "spiritual_meaning": th.spiritual_meaning
                }
                for th in yin_yang_map.turkish_heritages
            ],
            "total_yang_power": yin_yang_map.total_yang_power,
            "summary": "Turkish Yang provides structure, organization, practical mission. The practical force. The structural connection. The organizational framework. The mission."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/how-they-sync")
async def get_how_they_sync():
    """Get how African Yin and Turkish Yang sync"""
    try:
        searcher = AfricanTurkishYinYangSymbiosis()
        yin_yang_map = searcher.perform_deep_search()
        
        return {
            "status": "success",
            "symbioses": [
                {
                    "symbiosis_name": f"{s.african_yin.name} + {s.turkish_yang.name}",
                    "how_they_sync": s.how_they_sync,
                    "symbiosis_qualities": s.symbiosis_qualities,
                    "frequency_impact": s.frequency_impact,
                    "spiritual_meaning": s.spiritual_meaning,
                    "practical_manifestation": s.practical_manifestation
                }
                for s in yin_yang_map.symbioses
            ],
            "total_symbiosis_power": yin_yang_map.total_symbiosis_power,
            "summary": "African Yin + Turkish Yang = Perfect symbiosis. The miracle of the universe. The Table. Creative expression + Practical mission. Spiritual alignment + Material systems. Community unity + Structural organization."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/london-communities")
async def get_london_communities():
    """Get London communities - African Yin + Turkish Yang unity"""
    try:
        searcher = AfricanTurkishYinYangSymbiosis()
        yin_yang_map = searcher.perform_deep_search()
        
        # Find London-related symbioses
        london_symbioses = [s for s in yin_yang_map.symbioses if "London" in s.how_they_sync or "London" in s.practical_manifestation]
        
        return {
            "status": "success",
            "london_communities": {
                "total": 8,
                "communities": [
                    "Turkish Cypriot (Cypriot thread)",
                    "Greek Cypriot (Greek thread)",
                    "British Cypriot (Cypriot thread)",
                    "Anti-Zionist Jewish (Jewish thread)",
                    "Turkish (Turkish thread)",
                    "Greek (Greek thread)",
                    "African (Cypriot thread - hospitality) ← The Yin",
                    "All in between (Cypriot thread - inclusion)"
                ],
                "symbiosis": "African community (Yin) + Turkish community (Yang) = London unity. 8 communities. All connected. All serving. All honoring. The Table."
            },
            "symbioses": [
                {
                    "how_they_sync": s.how_they_sync,
                    "practical_manifestation": s.practical_manifestation,
                    "frequency_impact": s.frequency_impact
                }
                for s in london_symbioses
            ],
            "connection_to_table": "8 London communities unified. African Yin + Turkish Yang = Perfect symbiosis. The Table. All serving. All honoring."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
