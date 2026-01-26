"""SENTINEL LOGGING SYSTEM
Real-time logging for freedom of will tracking across S: drive

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

FREEDOM OF WILL:
Every aspect of the sentinel should be loggable with real-time data
for freedom of will tracking across the whole S: drive.

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity


PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field, asdict
from enum import Enum
from datetime import datetime
import json
import logging
from pathlib import Path
import asyncio
from fastapi import WebSocket

logger = logging.getLogger(__name__)


class LogLevel(Enum):
    """Log levels"""
    DEBUG = "debug"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"


class LogCategory(Enum):
    """Log categories for sentinel"""
    SENTINEL_MONITORING = "sentinel_monitoring"
    ENERGY_ALERTS = "energy_alerts"
    VIBRATION_CHECKS = "vibration_checks"
    CONNECTION_RITUALS = "connection_rituals"
    SPIRITUAL_BATTLES = "spiritual_battles"
    SYSTEM_EVENTS = "system_events"
    USER_ACTIONS = "user_actions"
    FREEDOM_OF_WILL = "freedom_of_will"
    ALL = "all"


@dataclass
class SentinelLogEntry:
    """A sentinel log entry"""
    log_id: str
    timestamp: datetime
    category: LogCategory
    level: LogLevel
    message: str
    data: Dict[str, Any] = field(default_factory=dict)
    user_id: Optional[str] = None
    system_component: Optional[str] = None
    freedom_of_will_context: Optional[Dict[str, Any]] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


class SentinelLoggingSystem:
    """
    Comprehensive logging system for sentinel.
    
    Every aspect of the sentinel should be loggable with real-time data
    for freedom of will tracking across the whole S: drive.
    """
    
    def __init__(self, root_dir: Optional[Path] = None):
        """Initialize sentinel logging system"""
        if root_dir is None:
            root_dir = Path(__file__).parent.parent.parent
        
        self.root_dir = root_dir
        self.s_drive_root = root_dir  # S: drive root
        
        # Log directories
        self.log_dir = root_dir / "SIYEM" / "output" / "sentinel_logs"
        self.log_dir.mkdir(parents=True, exist_ok=True)
        
        self.realtime_log_dir = root_dir / "SIYEM" / "output" / "realtime_logs"
        self.realtime_log_dir.mkdir(parents=True, exist_ok=True)
        
        # Log storage
        self.logs: Dict[str, SentinelLogEntry] = {}
        self.realtime_subscribers: List[WebSocket] = []
        
        # Setup file logging
        self._setup_file_logging()
        
        logger.info("Sentinel Logging System initialized")
    
    def _setup_file_logging(self):
        """Setup file-based logging"""
        log_file = self.log_dir / f"sentinel_{datetime.now().strftime('%Y%m%d')}.log"
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    async def log(
        self,
        category: LogCategory,
        level: LogLevel,
        message: str,
        data: Optional[Dict[str, Any]] = None,
        user_id: Optional[str] = None,
        system_component: Optional[str] = None,
        freedom_of_will_context: Optional[Dict[str, Any]] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> SentinelLogEntry:
        """
        Log an entry.
        
        Every aspect of the sentinel should be loggable.
        """
        log_entry = SentinelLogEntry(
            log_id=f"LOG_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}",
            timestamp=datetime.now(),
            category=category,
            level=level,
            message=message,
            data=data or {},
            user_id=user_id,
            system_component=system_component,
            freedom_of_will_context=freedom_of_will_context or {},
            metadata=metadata or {}
        )
        
        # Store log
        self.logs[log_entry.log_id] = log_entry
        
        # Write to file
        await self._write_log_to_file(log_entry)
        
        # Broadcast to real-time subscribers
        await self._broadcast_log(log_entry)
        
        # Log to Python logger
        log_method = getattr(logger, level.value, logger.info)
        log_method(f"[{category.value}] {message}")
        
        return log_entry
    
    async def _write_log_to_file(self, log_entry: SentinelLogEntry):
        """Write log entry to file"""
        try:
            # JSON log file
            json_log_file = self.realtime_log_dir / f"realtime_{datetime.now().strftime('%Y%m%d')}.jsonl"
            
            log_dict = {
                "log_id": log_entry.log_id,
                "timestamp": log_entry.timestamp.isoformat(),
                "category": log_entry.category.value,
                "level": log_entry.level.value,
                "message": log_entry.message,
                "data": log_entry.data,
                "user_id": log_entry.user_id,
                "system_component": log_entry.system_component,
                "freedom_of_will_context": log_entry.freedom_of_will_context,
                "metadata": log_entry.metadata
            }
            
            with open(json_log_file, 'a', encoding='utf-8') as f:
                f.write(json.dumps(log_dict) + '\n')
        except Exception as e:
            logger.error(f"Error writing log to file: {e}")
    
    async def _broadcast_log(self, log_entry: SentinelLogEntry):
        """Broadcast log to real-time subscribers"""
        if not self.realtime_subscribers:
            return
        
        log_dict = {
            "log_id": log_entry.log_id,
            "timestamp": log_entry.timestamp.isoformat(),
            "category": log_entry.category.value,
            "level": log_entry.level.value,
            "message": log_entry.message,
            "data": log_entry.data,
            "user_id": log_entry.user_id,
            "system_component": log_entry.system_component,
            "freedom_of_will_context": log_entry.freedom_of_will_context,
            "metadata": log_entry.metadata
        }
        
        disconnected = []
        for subscriber in self.realtime_subscribers:
            try:
                await subscriber.send_json({
                    "type": "sentinel_log",
                    "log": log_dict
                })
            except Exception as e:
                logger.error(f"Error broadcasting to subscriber: {e}")
                disconnected.append(subscriber)
        
        # Remove disconnected subscribers
        for sub in disconnected:
            if sub in self.realtime_subscribers:
                self.realtime_subscribers.remove(sub)
    
    async def subscribe_realtime(self, websocket: WebSocket):
        """Subscribe to real-time log updates"""
        await websocket.accept()
        self.realtime_subscribers.append(websocket)
        logger.info(f"Real-time log subscriber connected. Total: {len(self.realtime_subscribers)}")
    
    async def unsubscribe_realtime(self, websocket: WebSocket):
        """Unsubscribe from real-time log updates"""
        if websocket in self.realtime_subscribers:
            self.realtime_subscribers.remove(websocket)
        logger.info(f"Real-time log subscriber disconnected. Total: {len(self.realtime_subscribers)}")
    
    def get_logs(
        self,
        category: Optional[LogCategory] = None,
        level: Optional[LogLevel] = None,
        user_id: Optional[str] = None,
        system_component: Optional[str] = None,
        limit: Optional[int] = None,
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None
    ) -> List[SentinelLogEntry]:
        """Get logs with filters"""
        logs = list(self.logs.values())
        
        if category and category != LogCategory.ALL:
            logs = [l for l in logs if l.category == category]
        
        if level:
            logs = [l for l in logs if l.level == level]
        
        if user_id:
            logs = [l for l in logs if l.user_id == user_id]
        
        if system_component:
            logs = [l for l in logs if l.system_component == system_component]
        
        if start_time:
            logs = [l for l in logs if l.timestamp >= start_time]
        
        if end_time:
            logs = [l for l in logs if l.timestamp <= end_time]
        
        # Sort by timestamp (newest first)
        logs.sort(key=lambda x: x.timestamp, reverse=True)
        
        if limit:
            logs = logs[:limit]
        
        return logs
    
    def get_freedom_of_will_logs(
        self,
        user_id: Optional[str] = None,
        limit: Optional[int] = None
    ) -> List[SentinelLogEntry]:
        """Get freedom of will logs"""
        return self.get_logs(
            category=LogCategory.FREEDOM_OF_WILL,
            user_id=user_id,
            limit=limit
        )
    
    def get_summary(self) -> Dict[str, Any]:
        """Get logging system summary"""
        total_logs = len(self.logs)
        by_category = {}
        by_level = {}
        
        for log in self.logs.values():
            cat = log.category.value
            lev = log.level.value
            
            by_category[cat] = by_category.get(cat, 0) + 1
            by_level[lev] = by_level.get(lev, 0) + 1
        
        return {
            "total_logs": total_logs,
            "by_category": by_category,
            "by_level": by_level,
            "realtime_subscribers": len(self.realtime_subscribers),
            "log_directory": str(self.log_dir),
            "realtime_log_directory": str(self.realtime_log_dir),
            "message": "Every aspect of the sentinel is loggable with real-time data for freedom of will tracking across S: drive"
        }


# Global instance
_logging_system: Optional[SentinelLoggingSystem] = None


def get_sentinel_logging_system(root_dir: Optional[Path] = None) -> SentinelLoggingSystem:
    """Get the global sentinel logging system instance"""
    global _logging_system
    if _logging_system is None:
        _logging_system = SentinelLoggingSystem(root_dir)
    return _logging_system
