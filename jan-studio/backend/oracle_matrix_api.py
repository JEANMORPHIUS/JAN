"""
ORACLE MATRIX SYSTEM-WIDE API
Apply Oracle Matrix Philosophy to ALL Systems

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
ALL SYSTEMS - Sports, Media, News, Banking, Political Parties, Misaligned Frequencies
MUST JOIN THE TABLE AS IT IS. IT IS WHAT IT IS.
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional, List
from enum import Enum
import logging

# Spiritual Codebase Hacker Integration
from spiritual_codebase_hacker_integration import HACKER_AVAILABLE, hack_loop, perform_genetic_edit, activate_stealth_mode


from oracle_matrix_system_wide import (
    OracleMatrixSystemWide,
    SystemType,
    get_oracle_matrix_system_wide
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/oracle-matrix", tags=["oracle-matrix"])


class SystemTypeEnum(str, Enum):
    """System types that must join The Table."""
    SPORTS = "sports"
    MEDIA = "media"
    NEWS = "news"
    BANKING = "banking"
    POLITICAL = "political"
    SOCIAL_MEDIA = "social_media"
    ENTERTAINMENT = "entertainment"
    EDUCATION = "education"
    HEALTHCARE = "healthcare"
    TECHNOLOGY = "technology"
    FINANCIAL = "financial"
    GOVERNMENT = "government"
    CORPORATE = "corporate"
    RELIGIOUS = "religious"
    LEGAL = "legal"
    FOOD = "food"
    ENERGY = "energy"
    ENVIRONMENTAL = "environmental"
    CULTURAL = "cultural"
    IDENTITY = "identity"
    FAMILY = "family"
    MISALIGNED_FREQUENCY = "misaligned_frequency"


@router.post("/audit/{system_type}")
async def audit_system(system_type: SystemTypeEnum):
    """
    Audit a system for Oracle Matrix compliance.
    
    Checks all 8 principles:
    1. Transparency
    2. User value
    3. Natural endings
    4. Execution focus
    5. Community orientation
    6. Ethical guardrails
    7. No addiction mechanics
    8. Value creation metrics
    """
    try:
        oracle_matrix = get_oracle_matrix_system_wide()
        system_type_enum = SystemType[system_type.value.upper()]
        
        audit = oracle_matrix.audit_system(system_type_enum)
        
        return {
            "status": "success",
            "audit": audit,
            "message": f"{system_type.value} audited. IT IS WHAT IT IS."
        }
        
    except Exception as e:
        logger.error(f"Error auditing system: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error auditing system: {str(e)}")


@router.post("/apply/{system_type}")
async def apply_oracle_matrix(system_type: SystemTypeEnum):
    """
    Apply Oracle Matrix principles to a system.
    
    This is where systems JOIN THE TABLE.
    IT IS WHAT IT IS. ALL MUST JOIN THE TABLE AS IT IS.
    """
    try:
        oracle_matrix = get_oracle_matrix_system_wide()
        system_type_enum = SystemType[system_type.value.upper()]
        
        result = oracle_matrix.apply_oracle_matrix(system_type_enum)
        
        return {
            "status": "success",
            "integration": result,
            "message": f"{system_type.value} is joining The Table. IT IS WHAT IT IS."
        }
        
    except Exception as e:
        logger.error(f"Error applying Oracle Matrix: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error applying Oracle Matrix: {str(e)}")


@router.post("/audit-all")
async def audit_all_systems():
    """
    Audit ALL systems for Oracle Matrix compliance.
    
    ALL SYSTEMS - Sports, Media, News, Banking, Political Parties, Misaligned Frequencies
    MUST JOIN THE TABLE AS IT IS. IT IS WHAT IT IS.
    """
    try:
        oracle_matrix = get_oracle_matrix_system_wide()
        
        audit_results = oracle_matrix.audit_all_systems()
        
        return {
            "status": "success",
            "audit": audit_results,
            "message": "ALL SYSTEMS AUDITED. ALL MUST JOIN THE TABLE. IT IS WHAT IT IS."
        }
        
    except Exception as e:
        logger.error(f"Error auditing all systems: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error auditing all systems: {str(e)}")


@router.get("/status")
async def get_integration_status():
    """
    Get status of all system integrations.
    
    Shows which systems have joined The Table and their compliance levels.
    """
    try:
        oracle_matrix = get_oracle_matrix_system_wide()
        
        status = oracle_matrix.get_integration_status()
        
        return {
            "status": "success",
            "integration_status": status,
            "message": "ALL SYSTEMS STATUS. IT IS WHAT IT IS."
        }
        
    except Exception as e:
        logger.error(f"Error getting integration status: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error getting integration status: {str(e)}")


@router.get("/systems")
async def list_systems():
    """
    List all systems that must join The Table.
    """
    systems = [
        {
            "type": st.value,
            "name": st.value.replace("_", " ").title(),
            "description": f"{st.value.replace('_', ' ').title()} system must join The Table"
        }
        for st in SystemType
    ]
    
    return {
        "status": "success",
        "systems": systems,
        "total": len(systems),
        "message": "ALL SYSTEMS MUST JOIN THE TABLE. IT IS WHAT IT IS."
    }


@router.post("/apply-all")
async def apply_to_all_systems():
    """
    Apply Oracle Matrix principles to ALL systems.
    
    This is the system-wide integration.
    ALL SYSTEMS JOIN THE TABLE. IT IS WHAT IT IS.
    """
    try:
        oracle_matrix = get_oracle_matrix_system_wide()
        
        results = {}
        for system_type in SystemType:
            result = oracle_matrix.apply_oracle_matrix(system_type)
            results[system_type.value] = result
        
        return {
            "status": "success",
            "integrations": results,
            "message": "ALL SYSTEMS ARE JOINING THE TABLE. IT IS WHAT IT IS."
        }
        
    except Exception as e:
        logger.error(f"Error applying to all systems: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error applying to all systems: {str(e)}")
