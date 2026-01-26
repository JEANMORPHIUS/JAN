"""SENTINEL LOGGING API
API endpoints for sentinel logging system

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

from fastapi import APIRouter, WebSocket, WebSocketDisconnect, HTTPException, Query, Body
from typing import Optional
from datetime import datetime
import logging
import json

# Spiritual Codebase Hacker Integration
from spiritual_codebase_hacker_integration import HACKER_AVAILABLE, hack_loop, perform_genetic_edit, activate_stealth_mode


from sentinel_logging_system import (
    get_sentinel_logging_system,
    LogCategory,
    LogLevel
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/sentinel-logs", tags=["Sentinel Logging"])


@router.websocket("/realtime")
async def websocket_realtime_logs(websocket: WebSocket):
    """WebSocket endpoint for real-time log updates"""
    logging_system = get_sentinel_logging_system()
    await logging_system.subscribe_realtime(websocket)
    
    try:
        while True:
            data = await websocket.receive_text()
            try:
                message = json.loads(data)
                if message.get("type") == "ping":
                    await websocket.send_json({"type": "pong"})
            except json.JSONDecodeError:
                pass
    except WebSocketDisconnect:
        await logging_system.unsubscribe_realtime(websocket)
    except Exception as e:
        logger.error(f"WebSocket error: {e}")
        await logging_system.unsubscribe_realtime(websocket)


@router.post("/log")
async def create_log(
    category: str = Body(..., description="Log category"),
    level: str = Body(..., description="Log level"),
    message: str = Body(..., description="Log message"),
    data: Optional[dict] = Body(None, description="Log data"),
    user_id: Optional[str] = Body(None, description="User ID"),
    system_component: Optional[str] = Body(None, description="System component"),
    freedom_of_will_context: Optional[dict] = Body(None, description="Freedom of will context")
):
    """Create a log entry"""
    try:
        logging_system = get_sentinel_logging_system()
        
        try:
            category_enum = LogCategory(category.lower())
            level_enum = LogLevel(level.lower())
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"Invalid category or level: {e}")
        
        log_entry = await logging_system.log(
            category=category_enum,
            level=level_enum,
            message=message,
            data=data,
            user_id=user_id,
            system_component=system_component,
            freedom_of_will_context=freedom_of_will_context
        )
        
        return {
            "status": "success",
            "log_id": log_entry.log_id,
            "message": "Log entry created"
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error creating log: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/logs")
async def get_logs(
    category: Optional[str] = Query(None, description="Filter by category"),
    level: Optional[str] = Query(None, description="Filter by level"),
    user_id: Optional[str] = Query(None, description="Filter by user ID"),
    system_component: Optional[str] = Query(None, description="Filter by system component"),
    limit: Optional[int] = Query(100, description="Limit results")
):
    """Get logs with filters"""
    try:
        logging_system = get_sentinel_logging_system()
        
        category_enum = None
        if category:
            try:
                category_enum = LogCategory(category.lower())
            except ValueError:
                raise HTTPException(status_code=400, detail=f"Invalid category: {category}")
        
        level_enum = None
        if level:
            try:
                level_enum = LogLevel(level.lower())
            except ValueError:
                raise HTTPException(status_code=400, detail=f"Invalid level: {level}")
        
        logs = logging_system.get_logs(
            category=category_enum,
            level=level_enum,
            user_id=user_id,
            system_component=system_component,
            limit=limit
        )
        
        return {
            "status": "success",
            "total": len(logs),
            "logs": [
                {
                    "log_id": l.log_id,
                    "timestamp": l.timestamp.isoformat(),
                    "category": l.category.value,
                    "level": l.level.value,
                    "message": l.message,
                    "data": l.data,
                    "user_id": l.user_id,
                    "system_component": l.system_component,
                    "freedom_of_will_context": l.freedom_of_will_context
                }
                for l in logs
            ]
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting logs: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/freedom-of-will")
async def get_freedom_of_will_logs(
    user_id: Optional[str] = Query(None, description="Filter by user ID"),
    limit: Optional[int] = Query(100, description="Limit results")
):
    """Get freedom of will logs"""
    try:
        logging_system = get_sentinel_logging_system()
        logs = logging_system.get_freedom_of_will_logs(user_id=user_id, limit=limit)
        
        return {
            "status": "success",
            "total": len(logs),
            "logs": [
                {
                    "log_id": l.log_id,
                    "timestamp": l.timestamp.isoformat(),
                    "message": l.message,
                    "freedom_of_will_context": l.freedom_of_will_context,
                    "data": l.data
                }
                for l in logs
            ]
        }
    except Exception as e:
        logger.error(f"Error getting freedom of will logs: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/summary")
async def get_summary():
    """Get logging system summary"""
    try:
        logging_system = get_sentinel_logging_system()
        summary = logging_system.get_summary()
        
        return {
            "status": "success",
            "summary": summary
        }
    except Exception as e:
        logger.error(f"Error getting summary: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
