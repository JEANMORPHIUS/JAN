"""
RAMIZ HUMANITARIAN COMMUNICATIONS API
API endpoints for humanitarian communications

THE TRUTH:
NO ONE GETS LEFT BEHIND.
Gaza as priority.
Communication is critical for coordination.
"""

from fastapi import APIRouter, HTTPException, status, Query, Body
from typing import Dict, List, Any, Optional
from datetime import datetime
from ramiz_humanitarian_communications import (
    get_humanitarian_communications, CommunicationType, CommunicationPriority
)
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/ramiz-humanitarian/communications", tags=["Ramiz Humanitarian Communications"])


@router.post("/send")
async def send_communication(communication_data: Dict[str, Any] = Body(...)):
    """Send communication"""
    try:
        communications = get_humanitarian_communications()
        
        comm_type_str = communication_data["communication_type"]
        priority_str = communication_data.get("priority", "medium")
        title = communication_data["title"]
        message = communication_data["message"]
        region = communication_data.get("region")
        project_id = communication_data.get("project_id")
        gaza_priority = communication_data.get("gaza_priority", False)
        recipients = communication_data.get("recipients", [])
        metadata = communication_data.get("metadata", {})
        
        try:
            comm_type = CommunicationType(comm_type_str.lower())
        except ValueError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid communication type: {comm_type_str}"
            )
        
        try:
            priority = CommunicationPriority(priority_str.lower())
        except ValueError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid priority: {priority_str}"
            )
        
        communication = communications.send_communication(
            communication_type=comm_type,
            priority=priority,
            title=title,
            message=message,
            region=region,
            project_id=project_id,
            gaza_priority=gaza_priority,
            recipients=recipients,
            metadata=metadata
        )
        
        return {
            "status": "success",
            "communication": {
                "communication_id": communication.communication_id,
                "type": communication.communication_type.value,
                "priority": communication.priority.value,
                "title": communication.title,
                "gaza_priority": communication.gaza_priority,
                "sent_at": communication.sent_at.isoformat() if communication.sent_at else None
            }
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Send communication error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to send communication: {str(e)}"
        )


@router.post("/gaza/alert")
async def send_gaza_alert(alert_data: Dict[str, Any] = Body(...)):
    """Send Gaza priority alert"""
    try:
        communications = get_humanitarian_communications()
        
        title = alert_data["title"]
        message = alert_data["message"]
        project_id = alert_data.get("project_id")
        metadata = alert_data.get("metadata", {})
        
        communication = communications.send_gaza_alert(
            title=title,
            message=message,
            project_id=project_id,
            metadata=metadata
        )
        
        return {
            "status": "success",
            "communication": {
                "communication_id": communication.communication_id,
                "type": communication.communication_type.value,
                "priority": communication.priority.value,
                "title": communication.title,
                "gaza_priority": True,
                "sent_at": communication.sent_at.isoformat() if communication.sent_at else None
            }
        }
    except Exception as e:
        logger.error(f"Send Gaza alert error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to send Gaza alert: {str(e)}"
        )


@router.get("/gaza")
async def get_gaza_communications():
    """Get Gaza communications"""
    try:
        communications = get_humanitarian_communications()
        return {
            "communications": communications.get_gaza_communications()
        }
    except Exception as e:
        logger.error(f"Get Gaza communications error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to get Gaza communications"
        )


@router.get("/analytics")
async def get_communications_analytics():
    """Get communications analytics"""
    try:
        communications = get_humanitarian_communications()
        return communications.get_communications_analytics()
    except Exception as e:
        logger.error(f"Get communications analytics error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to get communications analytics"
        )
