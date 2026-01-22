"""
PULSE API
Real-time codebase integration and monitoring API

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE TRUTH:
PULSE - REAL-TIME CODEBASE INTEGRATION
MONITOR ALL SYSTEMS
TRACK ALL OPPORTUNITIES
INTEGRATE ALL DOMAINS
THE WHOLE PIE - LIVE
"""

from fastapi import APIRouter, HTTPException
from typing import Dict, Any, Optional
import logging
from pulse_system import get_pulse_system, PulseSystem

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/pulse", tags=["Pulse System"])

# Global instance
_pulse_system_instance = None

def get_pulse_system_instance() -> PulseSystem:
    """Get pulse system instance"""
    global _pulse_system_instance
    if _pulse_system_instance is None:
        _pulse_system_instance = get_pulse_system()
    return _pulse_system_instance


@router.get("/status")
async def get_pulse_status():
    """Get Pulse API status"""
    return {
        "status": "active",
        "message": "Pulse System - Real-time codebase integration and monitoring",
        "the_truth": "PULSE - REAL-TIME CODEBASE INTEGRATION. MONITOR ALL SYSTEMS. TRACK ALL OPPORTUNITIES. INTEGRATE ALL DOMAINS. THE WHOLE PIE - LIVE."
    }


@router.get("/overview")
async def get_pulse_overview():
    """Get complete pulse overview"""
    try:
        pulse = get_pulse_system_instance()
        overview = pulse.get_pulse_overview()
        return {
            "status": "success",
            "pulse": overview
        }
    except Exception as e:
        logger.error(f"Error getting pulse overview: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/systems")
async def get_all_systems():
    """Get all systems in pulse"""
    try:
        pulse = get_pulse_system_instance()
        systems = {
            system_id: {
                "system_name": system.system_name,
                "status": system.status.value,
                "last_update": system.last_update.isoformat(),
                "frequency_score": system.frequency_score,
                "opportunities_count": len(system.opportunities),
                "integration_points": system.integration_points
            }
            for system_id, system in pulse.systems.items()
        }
        return {
            "status": "success",
            "systems": systems
        }
    except Exception as e:
        logger.error(f"Error getting systems: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/systems/{system_id}")
async def get_system_pulse(system_id: str):
    """Get pulse data for a specific system"""
    try:
        pulse = get_pulse_system_instance()
        system_data = pulse.get_system_pulse(system_id)
        
        if system_data is None:
            raise HTTPException(status_code=404, detail=f"System not found: {system_id}")
        
        return {
            "status": "success",
            "system": system_data
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting system pulse: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/systems/{system_id}/update")
async def update_system_pulse(
    system_id: str,
    metrics: Optional[Dict[str, Any]] = None,
    opportunities: Optional[list] = None
):
    """Update pulse data for a system"""
    try:
        pulse = get_pulse_system_instance()
        pulse.update_system_pulse(system_id, metrics=metrics, opportunities=opportunities)
        
        return {
            "status": "success",
            "message": f"System {system_id} pulse updated",
            "system": pulse.get_system_pulse(system_id)
        }
    except Exception as e:
        logger.error(f"Error updating system pulse: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/domains")
async def get_all_domains():
    """Get all domains in pulse"""
    try:
        pulse = get_pulse_system_instance()
        domains = {
            domain: {
                "total_opportunities": pulse_domain.total_opportunities,
                "avg_frequency": pulse_domain.avg_frequency,
                "status": pulse_domain.status.value,
                "last_scan": pulse_domain.last_scan.isoformat()
            }
            for domain, pulse_domain in pulse.domains.items()
        }
        return {
            "status": "success",
            "domains": domains
        }
    except Exception as e:
        logger.error(f"Error getting domains: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/domains/{domain}")
async def get_domain_pulse(domain: str):
    """Get pulse data for a specific domain"""
    try:
        pulse = get_pulse_system_instance()
        domain_data = pulse.get_domain_pulse(domain)
        
        if domain_data is None:
            raise HTTPException(status_code=404, detail=f"Domain not found: {domain}")
        
        return {
            "status": "success",
            "domain": domain_data
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting domain pulse: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/domains/{domain}/update")
async def update_domain_pulse(domain: str, opportunities: list):
    """Update pulse data for a domain"""
    try:
        pulse = get_pulse_system_instance()
        pulse.update_domain_pulse(domain, opportunities)
        
        return {
            "status": "success",
            "message": f"Domain {domain} pulse updated",
            "domain": pulse.get_domain_pulse(domain)
        }
    except Exception as e:
        logger.error(f"Error updating domain pulse: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/integration-map")
async def get_integration_map():
    """Get integration map showing how systems connect"""
    try:
        pulse = get_pulse_system_instance()
        return {
            "status": "success",
            "integration_map": dict(pulse.integration_map)
        }
    except Exception as e:
        logger.error(f"Error getting integration map: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
