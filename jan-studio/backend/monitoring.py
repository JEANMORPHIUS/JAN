"""
MONITORING SYSTEM
Architectural Weight: Built for 10x, 100x, 1000x scale

THE NOAH PROTOCOL:
- The Pitch: Waterproof error handling
- The Perimeter: Clear jurisdiction (monitoring boundaries)
- The Door: Trust the monitoring's buoyancy (auto-recovery)

THE TRUTH:
We build arks, not plastic tables.
"""

from typing import Dict, Any, Optional, List
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
import logging
import asyncio

logger = logging.getLogger(__name__)


class HealthStatus(Enum):
    """Health status"""
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    UNHEALTHY = "unhealthy"
    UNKNOWN = "unknown"


@dataclass
class HealthCheck:
    """Health check result"""
    name: str
    status: HealthStatus
    message: str
    timestamp: datetime = field(default_factory=datetime.now)
    response_time_ms: Optional[float] = None
    details: Dict[str, Any] = field(default_factory=dict)


class MonitoringSystem:
    """
    Monitoring System
    Architectural Weight: Monitors 10x, 100x, 1000x scale systems
    """
    
    def __init__(self):
        """Initialize monitoring system"""
        self.health_checks: Dict[str, HealthCheck] = {}
        self.metrics: Dict[str, List[float]] = {}
        self.alerts: List[Dict[str, Any]] = []
        self.running = False
        
        logger.info("Monitoring system initialized")
    
    async def start(self):
        """Start monitoring system (The Door: Trust the monitoring's buoyancy)"""
        if self.running:
            return
        
        self.running = True
        asyncio.create_task(self._monitoring_loop())
        logger.info("Monitoring system started")
    
    async def stop(self):
        """Stop monitoring system"""
        self.running = False
        logger.info("Monitoring system stopped")
    
    async def _monitoring_loop(self):
        """Monitoring loop (The Pitch: Waterproof error handling)"""
        while self.running:
            try:
                await self.run_health_checks()
                await asyncio.sleep(60)  # Check every minute
            except Exception as e:
                logger.error(f"Monitoring loop error: {e}")
                await asyncio.sleep(60)
    
    async def run_health_checks(self):
        """Run all health checks"""
        # Check database
        await self.check_database()
        
        # Check cache
        await self.check_cache()
        
        # Check queue
        await self.check_queue()
        
        # Check API
        await self.check_api()
    
    async def check_database(self) -> HealthCheck:
        """Check database health"""
        start_time = datetime.now()
        
        try:
            # Try to import and check database
            try:
                from database_pool import get_db_pool
                pool = get_db_pool()
                health = pool.health_check()
                
                status = HealthStatus.HEALTHY if health.get("status") == "healthy" else HealthStatus.UNHEALTHY
                message = f"Database: {health.get('status', 'unknown')}"
                
            except ImportError:
                status = HealthStatus.UNKNOWN
                message = "Database pool not available"
            
            response_time = (datetime.now() - start_time).total_seconds() * 1000
            
            check = HealthCheck(
                name="database",
                status=status,
                message=message,
                response_time_ms=response_time
            )
            
            self.health_checks["database"] = check
            return check
        
        except Exception as e:
            check = HealthCheck(
                name="database",
                status=HealthStatus.UNHEALTHY,
                message=f"Database check failed: {e}",
                response_time_ms=(datetime.now() - start_time).total_seconds() * 1000
            )
            self.health_checks["database"] = check
            return check
    
    async def check_cache(self) -> HealthCheck:
        """Check cache health"""
        start_time = datetime.now()
        
        try:
            from cache_layer import get_cache_layer
            cache = get_cache_layer()
            
            # Test cache
            test_key = "health_check"
            cache.set(test_key, "ok", ttl=60)
            result = cache.get(test_key)
            cache.invalidate(test_key)
            
            status = HealthStatus.HEALTHY if result == "ok" else HealthStatus.UNHEALTHY
            message = "Cache: operational"
            
            response_time = (datetime.now() - start_time).total_seconds() * 1000
            
            check = HealthCheck(
                name="cache",
                status=status,
                message=message,
                response_time_ms=response_time
            )
            
            self.health_checks["cache"] = check
            return check
        
        except Exception as e:
            check = HealthCheck(
                name="cache",
                status=HealthStatus.UNHEALTHY,
                message=f"Cache check failed: {e}",
                response_time_ms=(datetime.now() - start_time).total_seconds() * 1000
            )
            self.health_checks["cache"] = check
            return check
    
    async def check_queue(self) -> HealthCheck:
        """Check queue health"""
        start_time = datetime.now()
        
        try:
            from queue_system import get_queue_system
            queue = get_queue_system()
            stats = queue.get_queue_stats()
            
            # Determine status based on queue size and failures
            if stats["failed"] > stats["completed"] * 0.1:  # More than 10% failure rate
                status = HealthStatus.DEGRADED
            elif stats["queue_size"] > 1000:  # Queue backing up
                status = HealthStatus.DEGRADED
            else:
                status = HealthStatus.HEALTHY
            
            message = f"Queue: {stats['queue_size']} pending, {stats['completed']} completed, {stats['failed']} failed"
            
            response_time = (datetime.now() - start_time).total_seconds() * 1000
            
            check = HealthCheck(
                name="queue",
                status=status,
                message=message,
                response_time_ms=response_time,
                details=stats
            )
            
            self.health_checks["queue"] = check
            return check
        
        except Exception as e:
            check = HealthCheck(
                name="queue",
                status=HealthStatus.UNKNOWN,
                message=f"Queue check failed: {e}",
                response_time_ms=(datetime.now() - start_time).total_seconds() * 1000
            )
            self.health_checks["queue"] = check
            return check
    
    async def check_api(self) -> HealthCheck:
        """Check API health"""
        start_time = datetime.now()
        
        try:
            # Simple API health check
            import aiohttp
            async with aiohttp.ClientSession() as session:
                async with session.get("http://localhost:8000/health", timeout=aiohttp.ClientTimeout(total=5)) as response:
                    status_code = response.status
                    status = HealthStatus.HEALTHY if status_code == 200 else HealthStatus.UNHEALTHY
                    message = f"API: {status_code}"
        except Exception as e:
            status = HealthStatus.UNHEALTHY
            message = f"API check failed: {e}"
        
        response_time = (datetime.now() - start_time).total_seconds() * 1000
        
        check = HealthCheck(
            name="api",
            status=status,
            message=message,
            response_time_ms=response_time
        )
        
        self.health_checks["api"] = check
        return check
    
    def get_health_summary(self) -> Dict[str, Any]:
        """
        Get health summary (The Perimeter: Clear jurisdiction)
        
        Returns:
            Health summary
        """
        healthy = sum(1 for check in self.health_checks.values() if check.status == HealthStatus.HEALTHY)
        degraded = sum(1 for check in self.health_checks.values() if check.status == HealthStatus.DEGRADED)
        unhealthy = sum(1 for check in self.health_checks.values() if check.status == HealthStatus.UNHEALTHY)
        unknown = sum(1 for check in self.health_checks.values() if check.status == HealthStatus.UNKNOWN)
        
        overall_status = HealthStatus.HEALTHY
        if unhealthy > 0:
            overall_status = HealthStatus.UNHEALTHY
        elif degraded > 0:
            overall_status = HealthStatus.DEGRADED
        elif unknown == len(self.health_checks):
            overall_status = HealthStatus.UNKNOWN
        
        return {
            "overall_status": overall_status.value,
            "healthy": healthy,
            "degraded": degraded,
            "unhealthy": unhealthy,
            "unknown": unknown,
            "checks": {
                name: {
                    "status": check.status.value,
                    "message": check.message,
                    "response_time_ms": check.response_time_ms,
                    "timestamp": check.timestamp.isoformat()
                }
                for name, check in self.health_checks.items()
            },
            "timestamp": datetime.now().isoformat()
        }


# Global monitoring instance (The Perimeter: Clear jurisdiction)
_monitoring_system: Optional[MonitoringSystem] = None


def get_monitoring_system() -> MonitoringSystem:
    """
    Get or create monitoring system
    
    Returns:
        MonitoringSystem instance
    """
    global _monitoring_system
    
    if _monitoring_system is None:
        _monitoring_system = MonitoringSystem()
    
    return _monitoring_system
