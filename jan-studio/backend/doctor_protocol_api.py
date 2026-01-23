"""
DOCTOR PROTOCOL API
API endpoints for doctor protocol system
"""

from fastapi import APIRouter, HTTPException, Body, Query
from typing import Optional, Dict, Any, List
from datetime import date
import logging

from doctor_protocol import (
    get_doctor_protocol_system,
    ProtocolType,
    ProtocolStatus
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/doctor-protocol", tags=["Doctor Protocol"])


@router.post("/insulin-protocol")
async def create_insulin_protocol(
    insulin_type: str = Body(..., description="Insulin type (Humalog, Degludec, etc.)"),
    correction_factor: Optional[float] = Body(None, description="Units per mmol/L above target"),
    carb_ratio: Optional[float] = Body(None, description="Units per gram of carbs"),
    target_min: float = Body(4.0, description="Target glucose minimum"),
    target_max: float = Body(10.0, description="Target glucose maximum"),
    doctor_name: Optional[str] = Body(None, description="Doctor name"),
    notes: str = Body("", description="Notes")
):
    """Create an insulin dosing protocol"""
    try:
        system = get_doctor_protocol_system()
        
        protocol = system.create_insulin_protocol(
            insulin_type=insulin_type,
            correction_factor=correction_factor,
            carb_ratio=carb_ratio,
            target_range={"min": target_min, "max": target_max},
            doctor_name=doctor_name,
            notes=notes
        )
        
        return {
            "status": "success",
            "protocol": {
                "protocol_id": protocol.protocol_id,
                "insulin_type": protocol.insulin_type,
                "correction_factor": protocol.correction_factor,
                "carb_ratio": protocol.carb_ratio,
                "target_range": protocol.target_range,
                "doctor_name": protocol.doctor_name
            }
        }
    except Exception as e:
        logger.error(f"Error creating insulin protocol: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/carb-protocol")
async def create_carb_counting_protocol(
    carb_ratio: float = Body(..., description="Units insulin per gram of carbs"),
    fiber_adjustment: bool = Body(False, description="Adjust for fiber"),
    protein_adjustment: bool = Body(False, description="Adjust for protein"),
    doctor_name: Optional[str] = Body(None, description="Doctor name"),
    notes: str = Body("", description="Notes")
):
    """Create a carbohydrate counting protocol"""
    try:
        system = get_doctor_protocol_system()
        
        protocol = system.create_carb_counting_protocol(
            carb_ratio=carb_ratio,
            fiber_adjustment=fiber_adjustment,
            protein_adjustment=protein_adjustment,
            doctor_name=doctor_name,
            notes=notes
        )
        
        return {
            "status": "success",
            "protocol": {
                "protocol_id": protocol.protocol_id,
                "carb_ratio": protocol.carb_ratio,
                "fiber_adjustment": protocol.fiber_adjustment,
                "protein_adjustment": protocol.protein_adjustment,
                "doctor_name": protocol.doctor_name
            }
        }
    except Exception as e:
        logger.error(f"Error creating carb protocol: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/calculate-insulin")
async def calculate_insulin_dose(
    current_glucose: float = Body(..., description="Current blood glucose (mmol/L)"),
    carbs: float = Body(0.0, description="Carbohydrates (grams)"),
    insulin_type: str = Body("Humalog", description="Insulin type")
):
    """Calculate insulin dose based on active protocols"""
    try:
        system = get_doctor_protocol_system()
        calculation = system.calculate_insulin_dose(current_glucose, carbs, insulin_type)
        
        return {
            "status": "success",
            "calculation": calculation
        }
    except Exception as e:
        logger.error(f"Error calculating insulin dose: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/active-protocols")
async def get_active_protocols():
    """Get all active protocols"""
    try:
        system = get_doctor_protocol_system()
        protocols = system.get_active_protocols()
        
        return {
            "status": "success",
            "protocols": protocols
        }
    except Exception as e:
        logger.error(f"Error getting active protocols: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/summary")
async def get_system_summary():
    """Get summary of doctor protocol system"""
    try:
        system = get_doctor_protocol_system()
        summary = system.get_system_summary()
        
        return {
            "status": "success",
            "summary": summary
        }
    except Exception as e:
        logger.error(f"Error getting summary: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/sync")
async def sync_protocols():
    """Sync protocols across systems"""
    try:
        system = get_doctor_protocol_system()
        result = await system.sync_protocols()
        
        return {
            "status": "success",
            "result": result
        }
    except Exception as e:
        logger.error(f"Error syncing protocols: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/educational-resources")
async def get_educational_resources(
    topic: Optional[str] = Query(None, description="Topic: insulin_management, carb_counting, blood_glucose_monitoring")
):
    """Get educational resources"""
    try:
        system = get_doctor_protocol_system()
        resources = system.get_educational_resources(topic)
        
        return {
            "status": "success",
            "resources": resources
        }
    except Exception as e:
        logger.error(f"Error getting educational resources: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
