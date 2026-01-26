"""
CLOUD SEEDING ANALYSIS API
100% Complete - Debunk and Utilization Analysis

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE TRUTH:
TRUTH HEALS, LIES HARM
What is denied persists. What is acknowledged can heal.
"""

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime
import sys
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))
from cloud_seeding_analysis import CloudSeedingAnalysisSystem

router = APIRouter(prefix="/api/cloud-seeding", tags=["Cloud Seeding"])

# Initialize analysis system
analysis_system = CloudSeedingAnalysisSystem()


# ============================================================================
# MODELS
# ============================================================================

class CloudSeedingClaimResponse(BaseModel):
    """Response model for cloud seeding claim"""
    claim_id: str
    claim_text: str
    claim_type: str
    debunked: bool
    evidence: List[str]
    refutation_points: List[str]
    truth_statement: Optional[str]
    debunk_status: str


class CloudSeedingOperationResponse(BaseModel):
    """Response model for cloud seeding operation"""
    operation_id: str
    name: str
    location: str
    start_date: str
    end_date: Optional[str]
    operation_type: str
    purpose: str
    effectiveness: Optional[float]
    materials_used: List[str]
    scale: Optional[str]
    transparency: str
    community_control: bool
    weaponized: bool
    weaponization_status: str
    truth: str


# ============================================================================
# ENDPOINTS
# ============================================================================

@router.get("/")
async def get_cloud_seeding_overview():
    """Get complete cloud seeding analysis overview"""
    analysis = analysis_system.generate_complete_analysis()
    return {
        "status": "complete",
        "message": "100% Complete - All lies debunked, all truth restored, all utilization examined",
        "summary": analysis["summary"],
        "truth_declaration": analysis["truth_declaration"],
        "timestamp": datetime.now().isoformat()
    }


@router.get("/claims")
async def get_all_claims():
    """Get all cloud seeding claims (debunked and verified)"""
    return analysis_system.get_all_debunked_claims()


@router.get("/claims/{claim_id}")
async def get_claim(claim_id: str):
    """Get specific claim details"""
    result = analysis_system.debunk_claim(claim_id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result


@router.get("/operations")
async def get_all_operations():
    """Get all cloud seeding operations"""
    return {
        "total_operations": len(analysis_system.operations),
        "operations": [
            {
                "operation_id": op.operation_id,
                "name": op.name,
                "location": op.location,
                "operation_type": op.operation_type,
                "weaponized": op.weaponized,
                "transparency": op.transparency
            }
            for op in analysis_system.operations.values()
        ]
    }


@router.get("/operations/weaponized")
async def get_weaponized_operations():
    """Get all weaponized cloud seeding operations"""
    return analysis_system.get_weaponized_operations()


@router.get("/operations/{operation_id}")
async def get_operation(operation_id: str):
    """Get specific operation details"""
    result = analysis_system.get_operation_details(operation_id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result


@router.get("/utilizations")
async def get_all_utilizations():
    """Get all cloud seeding utilizations by country"""
    return {
        "total_utilizations": len(analysis_system.utilizations),
        "utilizations": [
            {
                "country": util.country,
                "program_name": util.program_name,
                "status": util.status,
                "purpose": util.purpose,
                "community_control": util.community_control,
                "transparency": util.transparency
            }
            for util in analysis_system.utilizations.values()
        ]
    }


@router.get("/utilizations/{country}")
async def get_utilization(country: str):
    """Get cloud seeding utilization for specific country"""
    result = analysis_system.analyze_utilization(country)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result


@router.get("/healing-pathway")
async def get_healing_pathway():
    """Get healing pathway for cloud seeding technology"""
    return analysis_system.identify_healing_pathway()


@router.get("/analysis/complete")
async def get_complete_analysis():
    """Get complete cloud seeding analysis"""
    return analysis_system.generate_complete_analysis()


@router.post("/analysis/save")
async def save_analysis():
    """Save current analysis to JSON file"""
    filepath = analysis_system.save_analysis()
    return {
        "status": "saved",
        "filepath": filepath,
        "message": "Analysis saved successfully",
        "timestamp": datetime.now().isoformat()
    }


@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "cloud_seeding_analysis",
        "claims_total": len(analysis_system.claims),
        "operations_total": len(analysis_system.operations),
        "utilizations_total": len(analysis_system.utilizations),
        "timestamp": datetime.now().isoformat()
    }
