"""
MONITORING API
API endpoints for monitoring, alerts, and dashboards

THE NOAH PROTOCOL:
- Architectural Weight: Built for 10x, 100x, 1000x scale
- The Pitch: Waterproof error handling
- The Perimeter: Clear API boundaries

THE TRUTH:
Scale and build until ready.
Monitoring APIs for the new world.
"""

from fastapi import APIRouter, HTTPException, Query, status
from typing import Optional, List
from datetime import datetime, timedelta
from monitoring_enhancements import (
    get_monitoring, AlertLevel, MonitoringEnhancements
)
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/monitoring", tags=["Monitoring"])


@router.get("/dashboard")
async def get_dashboard():
    """Get monitoring dashboard data"""
    try:
        monitoring = get_monitoring()
        return monitoring.get_dashboard_data()
    except Exception as e:
        logger.error(f"Dashboard error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to get dashboard data"
        )


@router.get("/alerts")
async def get_alerts(
    level: Optional[str] = Query(None, description="Filter by alert level"),
    component: Optional[str] = Query(None, description="Filter by component"),
    since_hours: Optional[int] = Query(None, description="Hours ago to start from"),
    limit: int = Query(100, description="Maximum number of alerts")
):
    """Get alerts with optional filters"""
    try:
        monitoring = get_monitoring()
        
        alert_level = None
        if level:
            try:
                alert_level = AlertLevel(level.lower())
            except ValueError:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Invalid alert level: {level}"
                )
        
        since = None
        if since_hours:
            since = datetime.now() - timedelta(hours=since_hours)
        
        alerts = monitoring.get_alerts(
            level=alert_level,
            component=component,
            since=since,
            limit=limit
        )
        
        return {
            "timestamp": datetime.now().isoformat(),
            "count": len(alerts),
            "alerts": alerts
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Get alerts error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to get alerts"
        )


@router.get("/metrics")
async def get_metrics(
    name: Optional[str] = Query(None, description="Specific metric name"),
    since_hours: Optional[int] = Query(None, description="Hours ago to start from")
):
    """Get metrics"""
    try:
        monitoring = get_monitoring()
        
        since = None
        if since_hours:
            since = datetime.now() - timedelta(hours=since_hours)
        
        metrics = monitoring.get_metrics(name=name, since=since)
        
        return {
            "timestamp": datetime.now().isoformat(),
            "metrics": metrics
        }
    except Exception as e:
        logger.error(f"Get metrics error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to get metrics"
        )


@router.get("/health")
async def get_health():
    """Run health checks and return status"""
    try:
        monitoring = get_monitoring()
        health = monitoring.run_health_checks()
        return health
    except Exception as e:
        logger.error(f"Health check error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to run health checks"
        )


@router.post("/thresholds/{metric_name}")
async def set_threshold(
    metric_name: str,
    min_value: Optional[float] = None,
    max_value: Optional[float] = None
):
    """Set threshold for a metric"""
    try:
        monitoring = get_monitoring()
        monitoring.set_threshold(metric_name, min_value, max_value)
        return {
            "status": "success",
            "message": f"Threshold set for {metric_name}",
            "threshold": {
                "min": min_value,
                "max": max_value
            }
        }
    except Exception as e:
        logger.error(f"Set threshold error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to set threshold"
        )


@router.get("/thresholds")
async def get_thresholds():
    """Get all thresholds"""
    try:
        monitoring = get_monitoring()
        return {
            "timestamp": datetime.now().isoformat(),
            "thresholds": monitoring.thresholds
        }
    except Exception as e:
        logger.error(f"Get thresholds error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to get thresholds"
        )
