"""
MONITORING ENHANCEMENTS
Advanced monitoring, alerting, and real-time dashboards

THE NOAH PROTOCOL:
- Architectural Weight: Built for 10x, 100x, 1000x scale
- The Pitch: Waterproof error handling
- The Perimeter: Clear monitoring boundaries

THE ARRIVAL PROTOCOL:
- Pre-Commissioning Scan: Can monitoring handle 1000x load?
- Frequency Anchor: Monitor from "done" - production ready

THE TRUTH:
Scale and build until ready.
Advanced monitoring for the new world.
"""

import asyncio
from typing import Dict, List, Any, Optional, Callable
from datetime import datetime, timedelta
from collections import deque
from enum import Enum
import logging
import json
from pathlib import Path

logger = logging.getLogger(__name__)


class AlertLevel(Enum):
    """Alert severity levels"""
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"


class Alert:
    """Alert object"""
    def __init__(self, level: AlertLevel, message: str, component: str, 
                 metadata: Optional[Dict[str, Any]] = None):
        self.level = level
        self.message = message
        self.component = component
        self.metadata = metadata or {}
        self.timestamp = datetime.now()
        self.id = f"{component}_{self.timestamp.isoformat()}"
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert alert to dictionary"""
        return {
            "id": self.id,
            "level": self.level.value,
            "message": self.message,
            "component": self.component,
            "metadata": self.metadata,
            "timestamp": self.timestamp.isoformat()
        }


class MonitoringEnhancements:
    """
    Enhanced Monitoring System
    Real-time alerts, performance metrics, health dashboards
    """
    
    def __init__(self, max_alerts: int = 1000, max_metrics: int = 10000):
        """Initialize enhanced monitoring"""
        self.alerts: deque = deque(maxlen=max_alerts)
        self.metrics: Dict[str, deque] = {}
        self.alert_handlers: List[Callable] = []
        self.health_checks: Dict[str, Callable] = {}
        self.thresholds: Dict[str, Dict[str, float]] = {}
        
        logger.info("Monitoring Enhancements initialized")
    
    def add_alert(self, level: AlertLevel, message: str, component: str,
                  metadata: Optional[Dict[str, Any]] = None):
        """Add an alert"""
        alert = Alert(level, message, component, metadata)
        self.alerts.append(alert)
        
        # Trigger alert handlers
        for handler in self.alert_handlers:
            try:
                handler(alert)
            except Exception as e:
                logger.error(f"Alert handler error: {e}")
        
        logger.log(
            logging.INFO if level == AlertLevel.INFO else
            logging.WARNING if level == AlertLevel.WARNING else
            logging.ERROR if level == AlertLevel.ERROR else
            logging.CRITICAL,
            f"[{component}] {message}"
        )
    
    def register_alert_handler(self, handler: Callable):
        """Register an alert handler"""
        self.alert_handlers.append(handler)
    
    def add_metric(self, name: str, value: float, max_values: int = 1000):
        """Add a metric value"""
        if name not in self.metrics:
            self.metrics[name] = deque(maxlen=max_values)
        
        self.metrics[name].append({
            "value": value,
            "timestamp": datetime.now().isoformat()
        })
        
        # Check thresholds
        if name in self.thresholds:
            thresholds = self.thresholds[name]
            if "max" in thresholds and value > thresholds["max"]:
                self.add_alert(
                    AlertLevel.WARNING,
                    f"Metric {name} exceeded max threshold: {value} > {thresholds['max']}",
                    "monitoring",
                    {"metric": name, "value": value, "threshold": thresholds["max"]}
                )
            if "min" in thresholds and value < thresholds["min"]:
                self.add_alert(
                    AlertLevel.WARNING,
                    f"Metric {name} below min threshold: {value} < {thresholds['min']}",
                    "monitoring",
                    {"metric": name, "value": value, "threshold": thresholds["min"]}
                )
    
    def set_threshold(self, metric_name: str, min_value: Optional[float] = None,
                     max_value: Optional[float] = None):
        """Set threshold for a metric"""
        if metric_name not in self.thresholds:
            self.thresholds[metric_name] = {}
        
        if min_value is not None:
            self.thresholds[metric_name]["min"] = min_value
        if max_value is not None:
            self.thresholds[metric_name]["max"] = max_value
    
    def register_health_check(self, name: str, check_func: Callable):
        """Register a health check"""
        self.health_checks[name] = check_func
    
    def run_health_checks(self) -> Dict[str, Any]:
        """Run all health checks"""
        results = {
            "timestamp": datetime.now().isoformat(),
            "checks": {},
            "overall_healthy": True
        }
        
        for name, check_func in self.health_checks.items():
            try:
                result = check_func()
                if isinstance(result, dict):
                    results["checks"][name] = result
                else:
                    results["checks"][name] = {"healthy": bool(result)}
                
                if not results["checks"][name].get("healthy", False):
                    results["overall_healthy"] = False
                    self.add_alert(
                        AlertLevel.ERROR,
                        f"Health check failed: {name}",
                        "health_check",
                        {"check": name, "result": results["checks"][name]}
                    )
            except Exception as e:
                results["checks"][name] = {"healthy": False, "error": str(e)}
                results["overall_healthy"] = False
                self.add_alert(
                    AlertLevel.CRITICAL,
                    f"Health check error: {name} - {str(e)}",
                    "health_check",
                    {"check": name, "error": str(e)}
                )
        
        return results
    
    def get_alerts(self, level: Optional[AlertLevel] = None,
                   component: Optional[str] = None,
                   since: Optional[datetime] = None,
                   limit: int = 100) -> List[Dict[str, Any]]:
        """Get alerts with filters"""
        filtered = list(self.alerts)
        
        if level:
            filtered = [a for a in filtered if a.level == level]
        
        if component:
            filtered = [a for a in filtered if a.component == component]
        
        if since:
            filtered = [a for a in filtered if a.timestamp >= since]
        
        # Sort by timestamp (newest first)
        filtered.sort(key=lambda a: a.timestamp, reverse=True)
        
        return [a.to_dict() for a in filtered[:limit]]
    
    def get_metrics(self, name: Optional[str] = None,
                   since: Optional[datetime] = None) -> Dict[str, Any]:
        """Get metrics"""
        if name:
            if name not in self.metrics:
                return {}
            
            metrics = list(self.metrics[name])
            if since:
                metrics = [m for m in metrics if datetime.fromisoformat(m["timestamp"]) >= since]
            
            if not metrics:
                return {}
            
            values = [m["value"] for m in metrics]
            return {
                "name": name,
                "count": len(metrics),
                "min": min(values),
                "max": max(values),
                "avg": sum(values) / len(values),
                "latest": values[-1],
                "data": metrics[-100:]  # Last 100 points
            }
        
        # All metrics
        result = {}
        for metric_name in self.metrics:
            result[metric_name] = self.get_metrics(metric_name, since)
        
        return result
    
    def get_dashboard_data(self) -> Dict[str, Any]:
        """Get dashboard data"""
        # Recent alerts (last hour)
        since = datetime.now() - timedelta(hours=1)
        recent_alerts = self.get_alerts(since=since, limit=50)
        
        # Alert counts by level
        alert_counts = {
            "info": len([a for a in recent_alerts if a["level"] == "info"]),
            "warning": len([a for a in recent_alerts if a["level"] == "warning"]),
            "error": len([a for a in recent_alerts if a["level"] == "error"]),
            "critical": len([a for a in recent_alerts if a["level"] == "critical"])
        }
        
        # Health checks
        health = self.run_health_checks()
        
        # Key metrics (last hour)
        metrics = self.get_metrics(since=since)
        
        return {
            "timestamp": datetime.now().isoformat(),
            "alerts": {
                "recent": recent_alerts,
                "counts": alert_counts,
                "total": len(self.alerts)
            },
            "health": health,
            "metrics": metrics,
            "thresholds": self.thresholds
        }


# Global monitoring instance
_monitoring: Optional[MonitoringEnhancements] = None


def get_monitoring() -> MonitoringEnhancements:
    """Get global monitoring instance"""
    global _monitoring
    if _monitoring is None:
        _monitoring = MonitoringEnhancements()
    return _monitoring
