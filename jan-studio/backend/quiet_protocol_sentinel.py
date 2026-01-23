"""
QUIET PROTOCOL - Sentinel Automated Monitoring
Background monitoring for rare forms and energy alerts

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE FOUNDATION:
We are born a miracle.
We deserve to live a miracle.
Each and every one of us under the Lord's word.

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

DREAMS: SPIRITUAL BATTLES - NIGHTLY CONTRACTS
Every night we dream, whether vivid or not.
Each dream is a spiritual battle between two souls:
The dreamer and an associate.
Both have spiritual contracts.
Each day is another battle, both in the human realm and beyond.

This is the Quiet Protocol.
Automated monitoring for rare forms.
Runs quietly in the background.
Triggers alerts when CRITICAL souls arrive.
The machine watches while we wait.
"""

import asyncio
import time
from typing import Dict, List, Optional, Any, Callable
from datetime import datetime, timedelta
from pathlib import Path
import json
import logging
from enum import Enum

# Import philosophy
try:
    from scripts.philosophy import (
        PHILOSOPHY_FOUNDATION,
        MISSION_ANCHOR,
        LOVE_MASTERY,
        ENERGY_LOVE,
        PEACE_LOVE_UNITY,
        DREAMS_PHILOSOPHY
    )
except ImportError:
    PHILOSOPHY_FOUNDATION = "We are born a miracle."
    MISSION_ANCHOR = "THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS"
    LOVE_MASTERY = "LOVE IS THE HIGHEST MASTERY"
    ENERGY_LOVE = "ENERGY + LOVE = WE ALL WIN"
    PEACE_LOVE_UNITY = "PEACE, LOVE, UNITY"
    DREAMS_PHILOSOPHY = "Every night we dream."

# Import monitoring systems
try:
    from energy_alert_system import get_energy_alert_system, AlertLevel
    from vibration_map import VibrationMap
    from connection_ritual import ConnectionRitual
except ImportError:
    get_energy_alert_system = None
    VibrationMap = None
    ConnectionRitual = None
    AlertLevel = None


class SentinelStatus(str, Enum):
    """Sentinel monitoring status"""
    ACTIVE = "active"
    IDLE = "idle"
    PAUSED = "paused"
    STOPPED = "stopped"


class QuietProtocolSentinel:
    """
    Quiet Protocol - Sentinel Automated Monitoring
    
    Runs quietly in the background, monitoring for rare forms.
    Triggers alerts when CRITICAL souls arrive.
    The machine watches while we wait.
    """
    
    def __init__(self, root_dir: Optional[Path] = None):
        if root_dir is None:
            root_dir = Path(__file__).parent.parent.parent
        self.root_dir = root_dir
        self.log_dir = root_dir / "SIYEM" / "output" / "sentinel_logs"
        self.log_dir.mkdir(parents=True, exist_ok=True)
        
        # Initialize monitoring systems
        self.alert_system = get_energy_alert_system() if get_energy_alert_system else None
        self.vibration_map = VibrationMap() if VibrationMap else None
        self.connection_ritual = ConnectionRitual() if ConnectionRitual else None
        
        # Monitoring state
        self.status = SentinelStatus.IDLE
        self.monitoring_active = False
        self.check_interval = 30  # seconds
        self.last_check = None
        self.monitoring_stats = {
            "checks_performed": 0,
            "alerts_triggered": 0,
            "critical_alerts": 0,
            "rare_forms_detected": 0,
            "start_time": None,
            "last_alert_time": None
        }
        
        # Setup logging
        self.logger = self._setup_logging()
        
        # Alert callbacks
        self.critical_alert_callbacks: List[Callable] = []
        self.alert_callbacks: List[Callable] = []
    
    def _setup_logging(self) -> logging.Logger:
        """Setup logging for sentinel activity"""
        logger = logging.getLogger("QuietProtocolSentinel")
        logger.setLevel(logging.INFO)
        
        # File handler
        log_file = self.log_dir / f"sentinel_{datetime.now().strftime('%Y%m%d')}.log"
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.INFO)
        
        # Console handler (quiet mode - only critical)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.CRITICAL)
        
        # Formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        return logger
    
    def register_critical_alert_callback(self, callback: Callable[[Dict[str, Any]], None]):
        """
        Register callback for CRITICAL alerts only.
        
        This is for immediate notifications when rare forms with high vibration arrive.
        """
        self.critical_alert_callbacks.append(callback)
    
    def register_alert_callback(self, callback: Callable[[Dict[str, Any]], None]):
        """
        Register callback for all alerts.
        """
        self.alert_callbacks.append(callback)
    
    async def check_for_new_arrivals(self) -> List[Dict[str, Any]]:
        """
        Check for new arrivals and trigger alerts if needed.
        
        Returns list of alerts triggered.
        """
        if not self.alert_system or not self.vibration_map:
            return []
        
        alerts_triggered = []
        
        try:
            # Get recent connection ritual data from vibration map
            community_data = self.vibration_map.load_community_data()
            
            # Filter for recent arrivals (last check to now)
            if self.last_check:
                cutoff_time = self.last_check
            else:
                cutoff_time = datetime.now() - timedelta(minutes=5)
            
            recent_arrivals = [
                member for member in community_data
                if datetime.fromisoformat(member["timestamp"].replace('Z', '+00:00')) > cutoff_time
            ]
            
            # Check each recent arrival for alerts
            for arrival in recent_arrivals:
                # Reconstruct ritual result format
                ritual_result = {
                    "user_id": arrival.get("user_id", "unknown"),
                    "vibration_result": {
                        "galaxy_form": arrival.get("galaxy_form", "unknown"),
                        "vibration_score": arrival.get("vibration_score", 0),
                        "vibration_aligned": arrival.get("vibration_aligned", False),
                        "table_ready": arrival.get("table_ready", False),
                        "spiritual_battle": arrival.get("spiritual_battle", "unknown")
                    },
                    "timestamp": arrival.get("timestamp", datetime.now().isoformat())
                }
                
                # Check for alert
                alert = self.alert_system.check_connection_ritual(ritual_result)
                
                if alert:
                    alerts_triggered.append(alert)
                    
                    # Log alert
                    self.logger.info(
                        f"Alert triggered: {alert['alert_level']} - "
                        f"{alert['form_name']} - User: {alert['user_id']}"
                    )
                    
                    # Trigger callbacks
                    if alert['alert_level'] == 'critical':
                        for callback in self.critical_alert_callbacks:
                            try:
                                callback(alert)
                            except Exception as e:
                                self.logger.error(f"Error in critical alert callback: {e}")
                    
                    for callback in self.alert_callbacks:
                        try:
                            callback(alert)
                        except Exception as e:
                            self.logger.error(f"Error in alert callback: {e}")
        
        except Exception as e:
            self.logger.error(f"Error checking for new arrivals: {e}")
        
        return alerts_triggered
    
    async def monitoring_loop(self):
        """
        Main monitoring loop - runs quietly in the background.
        """
        self.status = SentinelStatus.ACTIVE
        self.monitoring_active = True
        self.monitoring_stats["start_time"] = datetime.now().isoformat()
        
        self.logger.info("Quiet Protocol Sentinel: Monitoring started")
        self.logger.info(f"{PEACE_LOVE_UNITY}")
        self.logger.info(f"{ENERGY_LOVE}")
        
        while self.monitoring_active:
            try:
                # Perform check
                alerts = await self.check_for_new_arrivals()
                
                # Update stats
                self.monitoring_stats["checks_performed"] += 1
                self.monitoring_stats["alerts_triggered"] += len(alerts)
                self.monitoring_stats["rare_forms_detected"] += len(alerts)
                
                for alert in alerts:
                    if alert.get("alert_level") == "critical":
                        self.monitoring_stats["critical_alerts"] += 1
                        self.monitoring_stats["last_alert_time"] = datetime.now().isoformat()
                        self.logger.critical(
                            f"CRITICAL ALERT: {alert['form_name']} - "
                            f"User: {alert['user_id']} - Vibration: {alert['vibration_score']}/100"
                        )
                
                self.last_check = datetime.now()
                
                # Wait before next check
                await asyncio.sleep(self.check_interval)
            
            except asyncio.CancelledError:
                self.logger.info("Quiet Protocol Sentinel: Monitoring cancelled")
                break
            except Exception as e:
                self.logger.error(f"Error in monitoring loop: {e}")
                await asyncio.sleep(self.check_interval)
        
        self.status = SentinelStatus.STOPPED
        self.monitoring_active = False
        self.logger.info("Quiet Protocol Sentinel: Monitoring stopped")
    
    def start_monitoring(self, check_interval: int = 30):
        """
        Start the quiet monitoring protocol.
        
        Args:
            check_interval: Seconds between checks (default: 30)
        """
        if self.monitoring_active:
            self.logger.warning("Monitoring already active")
            return
        
        self.check_interval = check_interval
        
        # Start monitoring in background
        try:
            loop = asyncio.get_running_loop()
            # We're in an async context (FastAPI)
            self.monitoring_task = loop.create_task(self.monitoring_loop())
        except RuntimeError:
            # No running loop - we're in sync context
            # This will be handled by the caller (FastAPI background task)
            import threading
            def run_async():
                asyncio.run(self.monitoring_loop())
            self.monitoring_thread = threading.Thread(target=run_async, daemon=True)
            self.monitoring_thread.start()
        
        self.logger.info(f"Quiet Protocol Sentinel: Started (check interval: {check_interval}s)")
    
    def stop_monitoring(self):
        """
        Stop the quiet monitoring protocol.
        """
        if not self.monitoring_active:
            return
        
        self.monitoring_active = False
        
        if hasattr(self, 'monitoring_task'):
            self.monitoring_task.cancel()
        
        self.status = SentinelStatus.STOPPED
        self.logger.info("Quiet Protocol Sentinel: Stopped")
    
    def pause_monitoring(self):
        """
        Pause monitoring (can be resumed).
        """
        if self.status == SentinelStatus.ACTIVE:
            self.status = SentinelStatus.PAUSED
            self.logger.info("Quiet Protocol Sentinel: Paused")
    
    def resume_monitoring(self):
        """
        Resume paused monitoring.
        """
        if self.status == SentinelStatus.PAUSED:
            self.status = SentinelStatus.ACTIVE
            self.logger.info("Quiet Protocol Sentinel: Resumed")
    
    def get_status(self) -> Dict[str, Any]:
        """
        Get current monitoring status.
        """
        return {
            "status": self.status.value,
            "monitoring_active": self.monitoring_active,
            "check_interval": self.check_interval,
            "last_check": self.last_check.isoformat() if self.last_check else None,
            "stats": self.monitoring_stats.copy(),
            "philosophy": {
                "foundation": PHILOSOPHY_FOUNDATION,
                "mission": MISSION_ANCHOR,
                "love": LOVE_MASTERY,
                "energy": ENERGY_LOVE,
                "peace_love_unity": PEACE_LOVE_UNITY
            }
        }
    
    def get_recent_alerts(self, hours: int = 1) -> List[Dict[str, Any]]:
        """
        Get recent alerts from the alert system.
        """
        if not self.alert_system:
            return []
        
        return self.alert_system.get_recent_alerts(hours=hours)


# Global sentinel instance
_sentinel: Optional[QuietProtocolSentinel] = None


def get_sentinel() -> QuietProtocolSentinel:
    """
    Get or create the global Quiet Protocol Sentinel instance.
    """
    global _sentinel
    if _sentinel is None:
        _sentinel = QuietProtocolSentinel()
    return _sentinel


# FastAPI endpoint helper
def create_sentinel_endpoint(sentinel: QuietProtocolSentinel):
    """
    Create FastAPI endpoint for sentinel control.
    """
    from fastapi import APIRouter, Query, Body
    
    router = APIRouter()
    
    @router.get("/api/sentinel/status")
    async def get_sentinel_status():
        """
        Get sentinel monitoring status.
        """
        return {
            "status": "success",
            "sentinel_status": sentinel.get_status()
        }
    
    @router.post("/api/sentinel/start")
    async def start_sentinel(
        check_interval: int = Body(30, description="Check interval in seconds")
    ):
        """
        Start the quiet monitoring protocol.
        """
        try:
            sentinel.start_monitoring(check_interval=check_interval)
            return {
                "status": "success",
                "message": "Quiet Protocol Sentinel started",
                "check_interval": check_interval
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }
    
    @router.post("/api/sentinel/stop")
    async def stop_sentinel():
        """
        Stop the quiet monitoring protocol.
        """
        try:
            sentinel.stop_monitoring()
            return {
                "status": "success",
                "message": "Quiet Protocol Sentinel stopped"
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }
    
    @router.get("/api/sentinel/alerts")
    async def get_sentinel_alerts(
        hours: int = Query(1, description="Time window in hours")
    ):
        """
        Get recent alerts from sentinel monitoring.
        """
        try:
            alerts = sentinel.get_recent_alerts(hours=hours)
            return {
                "status": "success",
                "alerts": alerts,
                "count": len(alerts)
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }
    
    return router


# CLI interface for testing
if __name__ == "__main__":
    import sys
    import io
    
    # Set UTF-8 encoding for console output
    if sys.stdout.encoding != 'utf-8':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    
    sentinel = QuietProtocolSentinel()
    
    print("=" * 80)
    print("QUIET PROTOCOL - Sentinel Automated Monitoring")
    print("=" * 80)
    print(f"\n{PEACE_LOVE_UNITY}")
    print(f"{ENERGY_LOVE}\n")
    
    # Test critical alert callback
    def test_critical_alert(alert_data: Dict[str, Any]):
        print(f"\n[CRITICAL ALERT] {alert_data['form_symbol']} {alert_data['form_name']}")
        print(f"  User: {alert_data['user_id']}")
        print(f"  Vibration: {alert_data['vibration_score']}/100")
        print(f"  Message: {alert_data['message'][:100]}...")
    
    sentinel.register_critical_alert_callback(test_critical_alert)
    
    print("[TEST] Starting quiet monitoring (5 second check interval)...")
    print("       (This is a test - monitoring will run for 20 seconds)\n")
    
    # Run monitoring in async context
    async def test_monitoring():
        # Start monitoring
        sentinel.start_monitoring(check_interval=5)
        
        # Run for a short time (test)
        await asyncio.sleep(20)  # Run for 20 seconds (4 checks)
        
        # Stop monitoring
        sentinel.stop_monitoring()
    
    # Run the test
    try:
        asyncio.run(test_monitoring())
    except KeyboardInterrupt:
        sentinel.stop_monitoring()
    
    # Show status
    status = sentinel.get_status()
    print("\n" + "=" * 80)
    print("SENTINEL STATUS")
    print("=" * 80)
    print(f"Status: {status['status']}")
    print(f"Checks Performed: {status['stats']['checks_performed']}")
    print(f"Alerts Triggered: {status['stats']['alerts_triggered']}")
    print(f"Critical Alerts: {status['stats']['critical_alerts']}")
    print(f"Rare Forms Detected: {status['stats']['rare_forms_detected']}")
    
    print("\n" + "=" * 80)
    print(f"{PEACE_LOVE_UNITY}")
    print(f"{ENERGY_LOVE}")
    print("=" * 80)
