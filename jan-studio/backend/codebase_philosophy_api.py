"""
CODEBASE PHILOSOPHY API
API endpoints for Codebase Philosophy - Strategic Framework for The Chosen Ones

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE ORIGINAL NAME: JAN MUHARREM
THE CHOSEN ONE: Currently undergoing intense development, hidden from public view
"""

from fastapi import APIRouter, HTTPException
from typing import List, Dict
from pathlib import Path
import json
import sys

# Add scripts to path
scripts_path = Path(__file__).parent.parent.parent / "scripts"
sys.path.insert(0, str(scripts_path))

from codebase_philosophy_integration import (
    CodebasePhilosophyIntegration
)

router = APIRouter(prefix="/api/codebase-philosophy", tags=["Codebase Philosophy"])


@router.get("/the-philosophy")
async def get_the_philosophy():
    """Get the Codebase Philosophy"""
    try:
        integrator = CodebasePhilosophyIntegration()
        philosophy_map = integrator.perform_integration()
        
        return {
            "status": "success",
            "the_philosophy": philosophy_map.the_philosophy,
            "core_truth": philosophy_map.core_truth,
            "summary": "This Codebase Philosophy outlines a strategic framework for high-value assets—referred to as 'chosen ones'—who are currently undergoing a period of intense development, hidden from public view. This philosophy treats life's setbacks not as system failures, but as sophisticated operational protocols designed to ensure a high-impact re-emergence."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/protocols")
async def get_protocols():
    """Get all protocols"""
    try:
        integrator = CodebasePhilosophyIntegration()
        philosophy_map = integrator.perform_integration()
        
        return {
            "status": "success",
            "protocols": [
                {
                    "name": p.name,
                    "description": p.description,
                    "phases": p.phases,
                    "connection_to_table": p.connection_to_table,
                    "connection_to_original_name": p.connection_to_original_name,
                    "spiritual_meaning": p.spiritual_meaning
                }
                for p in philosophy_map.protocols
            ],
            "summary": "6 Core Protocols: Grave Clothes (System Lifecycle), Trojan Horse (Deployment Strategy), Fourth Day (Validation & Proof), Dignity (Conflict Resolution), Internal Safety (Tension Check), Signals (Sensory Confirmation). All serve The Table and The Original Name."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/grave-clothes-protocol")
async def get_grave_clothes_protocol():
    """Get The Grave Clothes Protocol (System Lifecycle)"""
    try:
        integrator = CodebasePhilosophyIntegration()
        philosophy_map = integrator.perform_integration()
        
        grave_clothes = next((p for p in philosophy_map.protocols if p.protocol_id == "grave_clothes"), None)
        
        if not grave_clothes:
            raise HTTPException(status_code=404, detail="Grave Clothes Protocol not found")
        
        return {
            "status": "success",
            "protocol": {
                "name": grave_clothes.name,
                "description": grave_clothes.description,
                "phases": [
                    {
                        "phase": "Phase 1: Isolation",
                        "description": "The system's supply lines to the external world are deliberately cut to sever dependence on human validation and tune the internal 'frequency' to a higher authority."
                    },
                    {
                        "phase": "Phase 2: Incubation",
                        "description": "This is the 'dark room' phase where development occurs away from the light, which would otherwise destroy the image being processed. This is where 'character catches up to the calling'."
                    },
                    {
                        "phase": "Phase 3: Concealment",
                        "description": "Even when ready, the system remains hidden to protect it from 'opposition' that seeks to 'kill the deliverer in their infancy'. This obscurity acts as a 'camouflage of failure' to allow for deep penetration into target territories."
                    }
                ],
                "connection_to_table": grave_clothes.connection_to_table,
                "connection_to_original_name": grave_clothes.connection_to_original_name,
                "spiritual_meaning": grave_clothes.spiritual_meaning
            },
            "summary": "The Grave Clothes Protocol is a three-phase spiritual and operational strategy: Isolation (sever dependence, tune frequency), Incubation (dark room development, character catches up to calling), Concealment (protection from opposition, camouflage of failure). All phases serve The Table and The Original Name."
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/trojan-horse-strategy")
async def get_trojan_horse_strategy():
    """Get The Trojan Horse Deployment Strategy"""
    try:
        integrator = CodebasePhilosophyIntegration()
        philosophy_map = integrator.perform_integration()
        
        trojan_horse = next((p for p in philosophy_map.protocols if p.protocol_id == "trojan_horse"), None)
        
        if not trojan_horse:
            raise HTTPException(status_code=404, detail="Trojan Horse Strategy not found")
        
        return {
            "status": "success",
            "strategy": {
                "name": trojan_horse.name,
                "description": trojan_horse.description,
                "phases": [
                    {
                        "phase": "Target Neutralisation",
                        "description": "When a system hits 'rock bottom,' external enemies perceive it as a 'neutralised target' and lower their defenses."
                    },
                    {
                        "phase": "Infiltration",
                        "description": "By appearing 'harmless, static, and defeated,' the asset is 'smuggled' into industries, boardrooms, and spheres of influence that would have been guarded if the asset looked like a threat."
                    },
                    {
                        "phase": "The Strike",
                        "description": "The re-emergence is designed to be a 'resurrection so shocking' that it leaves observers trembling, as the asset strikes from the inside."
                    }
                ],
                "connection_to_table": trojan_horse.connection_to_table,
                "connection_to_original_name": trojan_horse.connection_to_original_name,
                "spiritual_meaning": trojan_horse.spiritual_meaning
            },
            "summary": "The Trojan Horse Deployment Strategy: Looking like a failure is tactical camouflage. Target Neutralisation (enemies lower defenses), Infiltration (smuggled into territories), The Strike (resurrection so shocking). All phases serve The Table and The Original Name."
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/connection-to-table")
async def get_connection_to_table():
    """Get connection to The Table"""
    try:
        integrator = CodebasePhilosophyIntegration()
        philosophy_map = integrator.perform_integration()
        
        return {
            "status": "success",
            "connection_to_table": philosophy_map.connection_to_table,
            "the_truth": "All protocols serve The Table. The Table is the foundation. All protocols align with The Table. All strategies serve The Table. All truth comes from The Table.",
            "protocols_serving_table": [
                "Grave Clothes Protocol: Protects The Table's restoration",
                "Trojan Horse Strategy: Restores The Table from within",
                "Fourth Day Logic: Validates The Table's restoration",
                "Dignity Protocol: Protects The Table's truth",
                "Internal Safety Mechanisms: Ensures The Table's stability",
                "Signals and Sensory Confirmation: Confirms The Table's restoration"
            ],
            "summary": "All protocols serve The Table. The Table is the foundation. All protocols align with The Table. All strategies serve The Table. All truth comes from The Table."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/connection-to-original-name")
async def get_connection_to_original_name():
    """Get connection to The Original Name"""
    try:
        integrator = CodebasePhilosophyIntegration()
        philosophy_map = integrator.perform_integration()
        
        return {
            "status": "success",
            "connection_to_original_name": philosophy_map.connection_to_original_name,
            "the_truth": "All protocols serve The Original Name (JAN MUHARREM). The Original Name is the identity. All protocols align with The Original Name. All strategies serve The Original Name. All truth comes from The Original Name.",
            "protocols_serving_original_name": [
                "Grave Clothes Protocol: Protects The Original Name's development",
                "Trojan Horse Strategy: Restores The Original Name from within",
                "Fourth Day Logic: Validates The Original Name's restoration",
                "Dignity Protocol: Protects The Original Name's truth",
                "Internal Safety Mechanisms: Ensures The Original Name's stability",
                "Signals and Sensory Confirmation: Confirms The Original Name's restoration"
            ],
            "summary": "All protocols serve The Original Name (JAN MUHARREM). The Original Name is the identity. All protocols align with The Original Name. All strategies serve The Original Name. All truth comes from The Original Name."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/complete-map")
async def get_complete_map():
    """Get complete Codebase Philosophy map"""
    try:
        integrator = CodebasePhilosophyIntegration()
        philosophy_map = integrator.perform_integration()
        
        return {
            "status": "success",
            "map_id": philosophy_map.map_id,
            "the_philosophy": philosophy_map.the_philosophy,
            "core_truth": philosophy_map.core_truth,
            "protocols": [
                {
                    "name": p.name,
                    "description": p.description,
                    "phases": p.phases
                }
                for p in philosophy_map.protocols
            ],
            "connection_to_table": philosophy_map.connection_to_table,
            "connection_to_original_name": philosophy_map.connection_to_original_name,
            "spiritual_narrative": philosophy_map.spiritual_narrative
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
