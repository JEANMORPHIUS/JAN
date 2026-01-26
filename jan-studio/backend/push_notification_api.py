"""PUSH NOTIFICATION API
API endpoints for push notifications

NO DILLY DALLY - Real-time updates

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Query, HTTPException
from typing import Optional, List
import logging
import json

from push_notification_system import (
    get_push_system,
    NotificationType,
    NotificationPriority
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/push", tags=["Push Notifications"])


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """
    WebSocket endpoint for real-time push notifications.
    
    NO DILLY DALLY - Immediate updates.
    """
    push_system = get_push_system()
    await push_system.connect(websocket)
    
    try:
        while True:
            # Keep connection alive and listen for client messages
            data = await websocket.receive_text()
            try:
                message = json.loads(data)
                # Handle client messages if needed
                if message.get("type") == "ping":
                    await push_system.send_personal_message(websocket, {"type": "pong"})
            except json.JSONDecodeError:
                pass
    except WebSocketDisconnect:
        await push_system.disconnect(websocket)
    except Exception as e:
        logger.error(f"WebSocket error: {e}")
        await push_system.disconnect(websocket)


@router.post("/notify")
async def push_notification(
    notification_type: str,
    priority: str,
    title: str,
    message: str,
    data: Optional[dict] = None,
    action_url: Optional[str] = None
):
    """Manually push a notification"""
    try:
        push_system = get_push_system()
        
        try:
            type_enum = NotificationType(notification_type.lower())
            priority_enum = NotificationPriority(priority.lower())
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"Invalid type or priority: {e}")
        
        notification = await push_system.push_notification(
            type_enum,
            priority_enum,
            title,
            message,
            data,
            action_url
        )
        
        return {
            "status": "success",
            "notification_id": notification.notification_id,
            "message": "Notification pushed"
        }
    except Exception as e:
        logger.error(f"Error pushing notification: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/notifications")
async def get_notifications(
    notification_type: Optional[str] = Query(None, description="Filter by type"),
    unread_only: bool = Query(False, description="Only unread notifications"),
    limit: Optional[int] = Query(None, description="Limit results")
):
    """Get notifications"""
    try:
        push_system = get_push_system()
        
        type_enum = None
        if notification_type:
            try:
                type_enum = NotificationType(notification_type.lower())
            except ValueError:
                raise HTTPException(status_code=400, detail=f"Invalid notification type: {notification_type}")
        
        notifications = push_system.get_notifications(type_enum, unread_only, limit)
        
        return {
            "status": "success",
            "total": len(notifications),
            "notifications": [
                {
                    "id": n.notification_id,
                    "type": n.type.value,
                    "priority": n.priority.value,
                    "title": n.title,
                    "message": n.message,
                    "data": n.data,
                    "timestamp": n.timestamp.isoformat(),
                    "read": n.read,
                    "action_url": n.action_url
                }
                for n in notifications
            ]
        }
    except Exception as e:
        logger.error(f"Error getting notifications: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.post("/notifications/{notification_id}/read")
async def mark_notification_read(notification_id: str):
    """Mark notification as read"""
    try:
        push_system = get_push_system()
        push_system.mark_read(notification_id)
        
        return {
            "status": "success",
            "message": "Notification marked as read"
        }
    except Exception as e:
        logger.error(f"Error marking notification as read: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/status")
async def get_push_status():
    """Get push system status"""
    try:
        push_system = get_push_system()
        
        return {
            "status": "active",
            "active_connections": len(push_system.active_connections),
            "total_notifications": len(push_system.notifications),
            "unread_notifications": len([n for n in push_system.notifications.values() if not n.read]),
            "message": "NO DILLY DALLY - Push system active"
        }
    except Exception as e:
        logger.error(f"Error getting push status: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
