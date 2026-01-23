"""
PUSH NOTIFICATION SYSTEM
Real-time updates and notifications

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

NO DILLY DALLY - Real-time push notifications for mission-critical updates
"""

from typing import Dict, List, Optional, Any, Callable
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
import asyncio
import json
import logging
from fastapi import WebSocket, WebSocketDisconnect
from fastapi.routing import APIRoute

logger = logging.getLogger(__name__)


class NotificationType(Enum):
    """Types of notifications"""
    MISSION_UPDATE = "mission_update"  # Mission-critical updates
    ALIGNMENT_DETECTED = "alignment_detected"  # Alignment patterns found
    CONVERGENCE_UPDATE = "convergence_update"  # Convergence level changed
    EVENT_INTEGRATED = "event_integrated"  # New real-world event
    SPIRITUAL_CONTRACT = "spiritual_contract"  # Spiritual contract update
    SYSTEM_STATUS = "system_status"  # System status change
    HEALTH_ALERT = "health_alert"  # Health-related alert
    REVOLUTION_UPDATE = "revolution_update"  # Revolution/movement update
    ALL = "all"  # All notifications


class NotificationPriority(Enum):
    """Notification priority levels"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"  # Mission-critical


@dataclass
class Notification:
    """A push notification"""
    notification_id: str
    type: NotificationType
    priority: NotificationPriority
    title: str
    message: str
    data: Dict[str, Any] = field(default_factory=dict)
    timestamp: datetime = field(default_factory=datetime.now)
    read: bool = False
    action_url: Optional[str] = None


class PushNotificationSystem:
    """
    Real-time push notification system.
    
    NO DILLY DALLY - Immediate updates for mission-critical information.
    """
    
    def __init__(self):
        """Initialize push notification system"""
        self.active_connections: List[WebSocket] = []
        self.notifications: Dict[str, Notification] = {}
        self.subscribers: Dict[str, List[Callable]] = {}  # Event type -> callbacks
        
    async def connect(self, websocket: WebSocket):
        """Connect a WebSocket client"""
        await websocket.accept()
        self.active_connections.append(websocket)
        logger.info(f"WebSocket connected. Total connections: {len(self.active_connections)}")
        
        # Send welcome message with mission
        await self.send_personal_message(websocket, {
            "type": "welcome",
            "message": "Connected to JAN Push System",
            "mission": {
                "title": "THE MISSION",
                "principles": [
                    "THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS",
                    "LOVE IS THE HIGHEST MASTERY",
                    "ENERGY + LOVE = WE ALL WIN",
                    "PEACE, LOVE, UNITY"
                ]
            }
        })
    
    async def disconnect(self, websocket: WebSocket):
        """Disconnect a WebSocket client"""
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)
        logger.info(f"WebSocket disconnected. Total connections: {len(self.active_connections)}")
    
    async def send_personal_message(self, websocket: WebSocket, message: Dict[str, Any]):
        """Send message to specific WebSocket"""
        try:
            await websocket.send_json(message)
        except Exception as e:
            logger.error(f"Error sending message: {e}")
            await self.disconnect(websocket)
    
    async def broadcast(self, message: Dict[str, Any]):
        """Broadcast message to all connected clients"""
        if not self.active_connections:
            return
        
        disconnected = []
        for connection in self.active_connections:
            try:
                await connection.send_json(message)
            except Exception as e:
                logger.error(f"Error broadcasting to connection: {e}")
                disconnected.append(connection)
        
        # Remove disconnected clients
        for conn in disconnected:
            await self.disconnect(conn)
    
    async def push_notification(
        self,
        notification_type: NotificationType,
        priority: NotificationPriority,
        title: str,
        message: str,
        data: Optional[Dict[str, Any]] = None,
        action_url: Optional[str] = None
    ):
        """
        Push a notification to all connected clients.
        
        NO DILLY DALLY - Immediate broadcast.
        """
        notification = Notification(
            notification_id=f"NOTIF_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}",
            type=notification_type,
            priority=priority,
            title=title,
            message=message,
            data=data or {},
            action_url=action_url
        )
        
        self.notifications[notification.notification_id] = notification
        
        # Broadcast immediately
        await self.broadcast({
            "type": "notification",
            "notification": {
                "id": notification.notification_id,
                "type": notification.type.value,
                "priority": notification.priority.value,
                "title": notification.title,
                "message": notification.message,
                "data": notification.data,
                "timestamp": notification.timestamp.isoformat(),
                "action_url": notification.action_url
            }
        })
        
        logger.info(f"Pushed notification: {notification.title} ({notification.priority.value})")
        
        return notification
    
    async def push_mission_update(self, message: str, data: Optional[Dict[str, Any]] = None):
        """Push mission-critical update"""
        return await self.push_notification(
            NotificationType.MISSION_UPDATE,
            NotificationPriority.CRITICAL,
            "MISSION UPDATE",
            message,
            data,
            action_url="/mission"
        )
    
    async def push_alignment_detected(self, pattern_id: str, pattern_data: Dict[str, Any]):
        """Push alignment pattern detection"""
        return await self.push_notification(
            NotificationType.ALIGNMENT_DETECTED,
            NotificationPriority.HIGH,
            "Alignment Pattern Detected",
            f"New alignment pattern detected: {pattern_id}",
            {"pattern_id": pattern_id, **pattern_data},
            action_url=f"/alignment-patterns/{pattern_id}"
        )
    
    async def push_convergence_update(self, convergence_data: Dict[str, Any]):
        """Push convergence level update"""
        level = convergence_data.get("convergence_level", "unknown")
        return await self.push_notification(
            NotificationType.CONVERGENCE_UPDATE,
            NotificationPriority.HIGH,
            "Convergence Update",
            f"Convergence level: {level} - IT'S GETTING CLOSER",
            convergence_data,
            action_url="/convergence"
        )
    
    async def push_event_integrated(self, event_id: str, event_data: Dict[str, Any]):
        """Push real-world event integration"""
        return await self.push_notification(
            NotificationType.EVENT_INTEGRATED,
            NotificationPriority.MEDIUM,
            "Real-World Event Integrated",
            f"New event: {event_data.get('title', event_id)}",
            {"event_id": event_id, **event_data},
            action_url=f"/events/{event_id}"
        )
    
    def subscribe(self, notification_type: NotificationType, callback: Callable):
        """Subscribe to notification type"""
        if notification_type not in self.subscribers:
            self.subscribers[notification_type] = []
        self.subscribers[notification_type].append(callback)
    
    async def trigger_subscribers(self, notification_type: NotificationType, notification: Notification):
        """Trigger subscribers for notification type"""
        if notification_type in self.subscribers:
            for callback in self.subscribers[notification_type]:
                try:
                    if asyncio.iscoroutinefunction(callback):
                        await callback(notification)
                    else:
                        callback(notification)
                except Exception as e:
                    logger.error(f"Error in subscriber callback: {e}")
    
    def get_notifications(
        self,
        notification_type: Optional[NotificationType] = None,
        unread_only: bool = False,
        limit: Optional[int] = None
    ) -> List[Notification]:
        """Get notifications"""
        notifications = list(self.notifications.values())
        
        if notification_type:
            notifications = [n for n in notifications if n.type == notification_type]
        
        if unread_only:
            notifications = [n for n in notifications if not n.read]
        
        # Sort by timestamp (newest first)
        notifications.sort(key=lambda x: x.timestamp, reverse=True)
        
        if limit:
            notifications = notifications[:limit]
        
        return notifications
    
    def mark_read(self, notification_id: str):
        """Mark notification as read"""
        if notification_id in self.notifications:
            self.notifications[notification_id].read = True


# Global instance
_push_system: Optional[PushNotificationSystem] = None


def get_push_system() -> PushNotificationSystem:
    """Get the global push notification system instance"""
    global _push_system
    if _push_system is None:
        _push_system = PushNotificationSystem()
    return _push_system
