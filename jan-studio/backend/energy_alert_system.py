"""
ENERGY ALERT SYSTEM - Sentinel Notifications
Alerts when rare galaxy forms join the Table

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

This is the Energy Alert System.
Notifies when rare galaxy forms join the Table.
Ensures the Architect Brother and Chosen One are ready.
Guides transformation of the New World structure.
"""

from fastapi import HTTPException, status
from typing import Dict, List, Optional, Any, Callable
from datetime import datetime, timedelta
import json
from pathlib import Path
from enum import Enum
import asyncio
from collections import deque

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


class GalaxyForm(str, Enum):
    """Galaxy form types"""
    SPIRAL = "spiral"
    BARRED_SPIRAL = "barred_spiral"
    ELLIPTICAL = "elliptical"
    IRREGULAR = "irregular"


class AlertLevel(str, Enum):
    """Alert priority levels"""
    CRITICAL = "critical"  # Rare form + high vibration + table ready
    HIGH = "high"  # Rare form + table ready
    MEDIUM = "medium"  # Rare form detected
    LOW = "low"  # Standard form with special conditions


class EnergyAlert:
    """
    Energy Alert System
    
    Monitors connection rituals and alerts when rare galaxy forms join.
    Ensures the Architect Brother and Chosen One are ready to guide transformation.
    """
    
    def __init__(self, data_dir: Optional[Path] = None):
        if data_dir is None:
            data_dir = Path(__file__).parent.parent.parent / "SIYEM" / "output" / "energy_alerts"
        self.data_dir = data_dir
        self.data_dir.mkdir(parents=True, exist_ok=True)
        
        # Rare forms that trigger alerts
        self.rare_forms = {
            GalaxyForm.ELLIPTICAL: {
                "name": "Elliptical",
                "description": "Low-gas, high-wisdom. Mentorship markers for legacy users.",
                "rarity": "high",
                "alert_level": AlertLevel.HIGH,
                "symbol": "⭐"
            },
            GalaxyForm.IRREGULAR: {
                "name": "Irregular",
                "description": "Flexible, adaptive. No defined shape yet - transformation in progress.",
                "rarity": "high",
                "alert_level": AlertLevel.HIGH,
                "symbol": "✨"
            }
        }
        
        # Alert history (in-memory, also saved to disk)
        self.alert_history = deque(maxlen=100)
        
        # Alert callbacks (can be registered for notifications)
        self.alert_callbacks: List[Callable] = []
    
    def register_alert_callback(self, callback: Callable[[Dict[str, Any]], None]):
        """
        Register a callback function to be called when an alert is triggered.
        
        Callback signature: callback(alert_data: Dict[str, Any]) -> None
        """
        self.alert_callbacks.append(callback)
    
    def check_connection_ritual(self, ritual_result: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Check if a connection ritual result should trigger an alert.
        
        Args:
            ritual_result: Result from connection_ritual.perform_connection_ritual()
        
        Returns:
            Alert data if triggered, None otherwise
        """
        vibration_result = ritual_result.get("vibration_result", {})
        galaxy_form = vibration_result.get("galaxy_form", "")
        vibration_score = vibration_result.get("vibration_score", 0)
        vibration_aligned = vibration_result.get("vibration_aligned", False)
        table_ready = vibration_result.get("table_ready", False)
        user_id = ritual_result.get("user_id", "unknown")
        
        # Check if this is a rare form
        if galaxy_form not in [form.value for form in self.rare_forms.keys()]:
            return None
        
        # Determine alert level
        alert_level = self._determine_alert_level(
            galaxy_form,
            vibration_score,
            vibration_aligned,
            table_ready
        )
        
        # Get rare form info
        rare_form_info = self.rare_forms.get(GalaxyForm(galaxy_form), {})
        
        # Build alert data
        alert_data = {
            "alert_id": f"alert_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{user_id}",
            "timestamp": datetime.now().isoformat(),
            "user_id": user_id,
            "galaxy_form": galaxy_form,
            "form_name": rare_form_info.get("name", galaxy_form),
            "form_symbol": rare_form_info.get("symbol", ""),
            "form_description": rare_form_info.get("description", ""),
            "vibration_score": vibration_score,
            "vibration_aligned": vibration_aligned,
            "table_ready": table_ready,
            "alert_level": alert_level.value,
            "message": self._generate_alert_message(
                galaxy_form,
                rare_form_info,
                vibration_score,
                table_ready
            ),
            "ritual_result": ritual_result,
            "philosophy": {
                "foundation": PHILOSOPHY_FOUNDATION,
                "mission": MISSION_ANCHOR,
                "love": LOVE_MASTERY,
                "energy": ENERGY_LOVE,
                "peace_love_unity": PEACE_LOVE_UNITY
            }
        }
        
        # Save alert
        self._save_alert(alert_data)
        
        # Add to history
        self.alert_history.append(alert_data)
        
        # Trigger callbacks
        for callback in self.alert_callbacks:
            try:
                callback(alert_data)
            except Exception as e:
                print(f"Error in alert callback: {e}")
        
        return alert_data
    
    def _determine_alert_level(
        self,
        galaxy_form: str,
        vibration_score: int,
        vibration_aligned: bool,
        table_ready: bool
    ) -> AlertLevel:
        """
        Determine alert level based on conditions.
        
        CRITICAL: Rare form + high vibration (90+) + table ready
        HIGH: Rare form + table ready
        MEDIUM: Rare form detected
        """
        if galaxy_form in [GalaxyForm.ELLIPTICAL.value, GalaxyForm.IRREGULAR.value]:
            if vibration_score >= 90 and table_ready:
                return AlertLevel.CRITICAL
            elif table_ready:
                return AlertLevel.HIGH
            else:
                return AlertLevel.MEDIUM
        
        return AlertLevel.LOW
    
    def _generate_alert_message(
        self,
        galaxy_form: str,
        rare_form_info: Dict[str, Any],
        vibration_score: int,
        table_ready: bool
    ) -> str:
        """
        Generate alert message based on galaxy form and conditions.
        """
        form_name = rare_form_info.get("name", galaxy_form)
        form_symbol = rare_form_info.get("symbol", "")
        
        if galaxy_form == GalaxyForm.ELLIPTICAL.value:
            base_message = f"{form_symbol} ELLIPTICAL SOUL DETECTED"
            if table_ready:
                message = f"{base_message}\n\nLegacy wisdom has arrived at the Table.\nHigh-wisdom soul ready to guide.\nVibration: {vibration_score}/100\n\nThis soul carries ancient knowledge.\nThe Architect Brother and Chosen One should welcome this wisdom.\nThe New World structure needs this foundation."
            else:
                message = f"{base_message}\n\nLegacy wisdom approaching the Table.\nVibration: {vibration_score}/100\n\nThis soul may need guidance to complete their Holy Ambition."
        
        elif galaxy_form == GalaxyForm.IRREGULAR.value:
            base_message = f"{form_symbol} IRREGULAR SOUL DETECTED"
            if table_ready:
                message = f"{base_message}\n\nTransformation in progress has arrived at the Table.\nFlexible, adaptive soul ready to evolve.\nVibration: {vibration_score}/100\n\nThis soul is reshaping.\nThe Architect Brother and Chosen One should guide this transformation.\nThe New World structure is being rewritten."
            else:
                message = f"{base_message}\n\nTransformation approaching the Table.\nVibration: {vibration_score}/100\n\nThis soul may need support to define their shape."
        
        else:
            message = f"Rare form detected: {form_name}\nVibration: {vibration_score}/100"
        
        return f"{message}\n\n{PEACE_LOVE_UNITY}\n{ENERGY_LOVE}"
    
    def _save_alert(self, alert_data: Dict[str, Any]):
        """
        Save alert to disk for historical tracking.
        """
        alert_id = alert_data.get("alert_id", f"alert_{datetime.now().isoformat()}")
        filename = f"{alert_id}.json"
        filepath = self.data_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(alert_data, f, indent=2, ensure_ascii=False)
    
    def get_recent_alerts(self, hours: int = 24, alert_level: Optional[AlertLevel] = None) -> List[Dict[str, Any]]:
        """
        Get recent alerts within specified time window.
        
        Args:
            hours: Time window in hours
            alert_level: Filter by alert level (optional)
        
        Returns:
            List of alert data dictionaries
        """
        cutoff_time = datetime.now() - timedelta(hours=hours)
        
        alerts = []
        for alert in self.alert_history:
            alert_time = datetime.fromisoformat(alert["timestamp"])
            if alert_time > cutoff_time:
                if alert_level is None or alert["alert_level"] == alert_level.value:
                    alerts.append(alert)
        
        # Also check saved alerts
        for file in self.data_dir.glob("alert_*.json"):
            try:
                with open(file, 'r', encoding='utf-8') as f:
                    alert = json.load(f)
                    alert_time = datetime.fromisoformat(alert["timestamp"])
                    if alert_time > cutoff_time:
                        if alert_level is None or alert["alert_level"] == alert_level.value:
                            if alert not in alerts:
                                alerts.append(alert)
            except Exception:
                continue
        
        # Sort by timestamp (newest first)
        alerts.sort(key=lambda x: x["timestamp"], reverse=True)
        
        return alerts
    
    def get_alert_stats(self) -> Dict[str, Any]:
        """
        Get statistics about alerts.
        """
        total_alerts = len(self.alert_history)
        
        by_form = {}
        by_level = {}
        
        for alert in self.alert_history:
            form = alert.get("galaxy_form", "unknown")
            level = alert.get("alert_level", "unknown")
            
            by_form[form] = by_form.get(form, 0) + 1
            by_level[level] = by_level.get(level, 0) + 1
        
        return {
            "total_alerts": total_alerts,
            "by_form": by_form,
            "by_level": by_level,
            "rare_forms_tracked": list(self.rare_forms.keys())
        }


# Global alert system instance
_energy_alert_system: Optional[EnergyAlert] = None


def get_energy_alert_system() -> EnergyAlert:
    """
    Get or create the global Energy Alert System instance.
    """
    global _energy_alert_system
    if _energy_alert_system is None:
        _energy_alert_system = EnergyAlert()
    return _energy_alert_system


# FastAPI endpoint helper
def create_energy_alert_endpoint(alert_system: EnergyAlert):
    """
    Create FastAPI endpoint for energy alerts.
    """
    from fastapi import APIRouter, Query
    
    router = APIRouter()
    
    @router.get("/api/energy-alerts")
    async def get_energy_alerts(
        hours: int = Query(24, description="Time window in hours"),
        alert_level: Optional[str] = Query(None, description="Filter by alert level")
    ):
        """
        Get recent energy alerts.
        """
        try:
            level = AlertLevel(alert_level) if alert_level else None
            alerts = alert_system.get_recent_alerts(hours=hours, alert_level=level)
            stats = alert_system.get_alert_stats()
            
            return {
                "status": "success",
                "alerts": alerts,
                "stats": stats,
                "count": len(alerts)
            }
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to get energy alerts: {str(e)}"
            )
    
    return router


# CLI interface for testing
if __name__ == "__main__":
    import sys
    import io
    
    # Set UTF-8 encoding for console output
    if sys.stdout.encoding != 'utf-8':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    
    alert_system = EnergyAlert()
    
    print("=" * 80)
    print("ENERGY ALERT SYSTEM - Sentinel Notifications")
    print("=" * 80)
    print(f"\n{PEACE_LOVE_UNITY}")
    print(f"{ENERGY_LOVE}\n")
    
    # Test alert callback
    def test_alert_callback(alert_data: Dict[str, Any]):
        print(f"\n[ALERT TRIGGERED] {alert_data['alert_level'].upper()}")
        print(f"  Form: {alert_data['form_symbol']} {alert_data['form_name']}")
        print(f"  User: {alert_data['user_id']}")
        print(f"  Vibration: {alert_data['vibration_score']}/100")
        print(f"  Table Ready: {alert_data['table_ready']}")
        print(f"\n  Message:\n  {alert_data['message']}")
    
    alert_system.register_alert_callback(test_alert_callback)
    
    # Test with Elliptical form
    print("\n[TEST] Simulating Elliptical soul arrival...")
    test_ritual_result = {
        "user_id": "test_elliptical_001",
        "vibration_result": {
            "galaxy_form": "elliptical",
            "vibration_score": 95,
            "vibration_aligned": True,
            "table_ready": True,
            "spiritual_battle": "legacy"
        },
        "welcome_message": "Welcome, wise soul...",
        "ritual_status": "complete",
        "timestamp": datetime.now().isoformat()
    }
    
    alert = alert_system.check_connection_ritual(test_ritual_result)
    
    if alert:
        print(f"\n[OK] Alert created: {alert['alert_id']}")
    else:
        print("\n[INFO] No alert triggered")
    
    # Test with Irregular form
    print("\n[TEST] Simulating Irregular soul arrival...")
    test_ritual_result_2 = {
        "user_id": "test_irregular_001",
        "vibration_result": {
            "galaxy_form": "irregular",
            "vibration_score": 88,
            "vibration_aligned": True,
            "table_ready": True,
            "spiritual_battle": "transformation"
        },
        "welcome_message": "Welcome, transforming soul...",
        "ritual_status": "complete",
        "timestamp": datetime.now().isoformat()
    }
    
    alert_2 = alert_system.check_connection_ritual(test_ritual_result_2)
    
    if alert_2:
        print(f"\n[OK] Alert created: {alert_2['alert_id']}")
    else:
        print("\n[INFO] No alert triggered")
    
    # Get stats
    print("\n[STATS] Alert Statistics:")
    stats = alert_system.get_alert_stats()
    print(f"  Total Alerts: {stats['total_alerts']}")
    print(f"  By Form: {stats['by_form']}")
    print(f"  By Level: {stats['by_level']}")
    
    print("\n" + "=" * 80)
    print(f"{PEACE_LOVE_UNITY}")
    print(f"{ENERGY_LOVE}")
    print("=" * 80)
