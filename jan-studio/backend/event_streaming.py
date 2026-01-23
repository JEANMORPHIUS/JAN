"""
EVENT STREAMING ARCHITECTURE
Redis Pub/Sub for Event Streaming

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

EVENT STREAMING:
Redis Pub/Sub for event streaming to all channels.
Publishes events when data changes.
Subscribers listen for updates and broadcast to WebSocket clients.
"""

import json
import logging
from datetime import datetime
from typing import Dict, Any, Optional, List
from enum import Enum

logger = logging.getLogger(__name__)

# Try to import redis, but make it optional
try:
    import redis
    REDIS_AVAILABLE = True
except ImportError:
    REDIS_AVAILABLE = False
    logger.warning("Redis not available. Event streaming will use in-memory fallback.")


class EventType(Enum):
    """Type of event."""
    TIMELINE_EVENT_ADDED = "timeline_event_added"
    TIMELINE_EVENT_UPDATED = "timeline_event_updated"
    HERITAGE_SITE_ADDED = "heritage_site_added"
    HERITAGE_SITE_UPDATED = "heritage_site_updated"
    NARRATIVE_ADDED = "narrative_added"
    NARRATIVE_UPDATED = "narrative_updated"
    FREQUENCY_UPDATED = "frequency_updated"
    RESTORATION_PROGRESS = "restoration_progress"


class EventStreamingService:
    """Service for event streaming using Redis Pub/Sub."""
    
    def __init__(self, redis_url: Optional[str] = None):
        """Initialize event streaming service."""
        self.redis_url = redis_url or "redis://localhost:6379"
        self.redis_client: Optional[redis.Redis] = None
        self.pubsub: Optional[redis.client.PubSub] = None
        self.in_memory_events: List[Dict[str, Any]] = []  # Fallback if Redis unavailable
        
        if REDIS_AVAILABLE:
            try:
                self.redis_client = redis.from_url(self.redis_url, decode_responses=True)
                self.pubsub = self.redis_client.pubsub()
                logger.info("Event streaming service initialized with Redis")
            except Exception as e:
                logger.warning(f"Failed to connect to Redis: {e}. Using in-memory fallback.")
                REDIS_AVAILABLE = False
    
    def publish_event(self, event_type: EventType, event_data: Dict[str, Any]):
        """
        Publish event to Redis Pub/Sub.
        
        If Redis is unavailable, stores event in memory.
        """
        event = {
            "type": event_type.value,
            "data": event_data,
            "timestamp": datetime.now().isoformat()
        }
        
        if REDIS_AVAILABLE and self.redis_client:
            try:
                self.redis_client.publish(
                    'world-history-events',
                    json.dumps(event)
                )
                logger.info(f"Published event: {event_type.value}")
            except Exception as e:
                logger.error(f"Error publishing event: {e}")
                # Fallback to in-memory
                self.in_memory_events.append(event)
        else:
            # In-memory fallback
            self.in_memory_events.append(event)
            logger.info(f"Stored event in memory (Redis unavailable): {event_type.value}")
    
    def subscribe_to_events(self, callback):
        """
        Subscribe to events from Redis Pub/Sub.
        
        callback: Function to call when event is received
        """
        if REDIS_AVAILABLE and self.pubsub:
            try:
                self.pubsub.subscribe('world-history-events')
                
                for message in self.pubsub.listen():
                    if message['type'] == 'message':
                        try:
                            event = json.loads(message['data'])
                            callback(event)
                        except json.JSONDecodeError as e:
                            logger.error(f"Error decoding event: {e}")
            except Exception as e:
                logger.error(f"Error subscribing to events: {e}")
        else:
            logger.warning("Redis not available. Cannot subscribe to events.")
    
    def get_recent_events(self, limit: int = 100) -> List[Dict[str, Any]]:
        """Get recent events (from in-memory fallback if Redis unavailable)."""
        if self.in_memory_events:
            return self.in_memory_events[-limit:]
        return []
    
    def broadcast_to_websocket_clients(self, event: Dict[str, Any], websocket_clients: List):
        """
        Broadcast event to WebSocket clients.
        
        This would be called by the WebSocket handler when an event is received.
        """
        for client in websocket_clients:
            try:
                client.send_json(event)
            except Exception as e:
                logger.error(f"Error broadcasting to WebSocket client: {e}")


# Global event streaming service instance
_event_streaming_service: Optional[EventStreamingService] = None


def get_event_streaming_service() -> EventStreamingService:
    """Get or create global event streaming service instance."""
    global _event_streaming_service
    if _event_streaming_service is None:
        _event_streaming_service = EventStreamingService()
    return _event_streaming_service


def publish_timeline_event(event_data: Dict[str, Any], is_new: bool = True):
    """Publish timeline event."""
    service = get_event_streaming_service()
    event_type = EventType.TIMELINE_EVENT_ADDED if is_new else EventType.TIMELINE_EVENT_UPDATED
    service.publish_event(event_type, event_data)


def publish_frequency_update(frequency_data: Dict[str, Any]):
    """Publish Divine Frequency update."""
    service = get_event_streaming_service()
    service.publish_event(EventType.FREQUENCY_UPDATED, frequency_data)


def publish_restoration_progress(progress_data: Dict[str, Any]):
    """Publish restoration progress update."""
    service = get_event_streaming_service()
    service.publish_event(EventType.RESTORATION_PROGRESS, progress_data)
