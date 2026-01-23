"""
REVENUE AUTOMATION
Automatic revenue tracking and reporting

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE TRUTH:
REVENUE AUTOMATION - AUTOMATIC TRACKING AND REPORTING
TIME TO GET FINANCES FLOWING
"""

from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
from decimal import Decimal
import json
from pathlib import Path
from financial_controls_system import get_financial_system, RevenueChannel
from pulse_system import get_pulse_system

class RevenueAutomation:
    """
    Automatic revenue tracking and reporting.
    Integrates with Financial Controls and Pulse systems.
    """
    
    def __init__(self):
        self.financial_system = get_financial_system()
        self.pulse_system = get_pulse_system()
    
    def track_revenue_from_source(self, source: str, amount: Decimal, channel: RevenueChannel, description: str = "", metadata: Dict[str, Any] = None):
        """Automatically track revenue from a source"""
        entry = self.financial_system.add_revenue(
            channel=channel,
            amount=amount,
            description=description,
            source=source,
            metadata=metadata or {}
        )
        
        # Update Pulse system with revenue data
        self.pulse_system.update_system_pulse(
            "financial_controls",
            metrics={
                "last_revenue": float(amount),
                "revenue_channel": channel.value,
                "total_revenue": float(self.financial_system.get_revenue_summary()["total_revenue"])
            }
        )
        
        return entry
    
    def generate_daily_revenue_report(self) -> Dict[str, Any]:
        """Generate daily revenue report"""
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        tomorrow = today + timedelta(days=1)
        
        summary = self.financial_system.get_revenue_summary(start_date=today, end_date=tomorrow)
        
        return {
            "report_date": today.isoformat(),
            "report_type": "daily",
            "revenue": summary,
            "generated_at": datetime.now().isoformat()
        }
    
    def generate_weekly_revenue_report(self) -> Dict[str, Any]:
        """Generate weekly revenue report"""
        today = datetime.now()
        week_start = today - timedelta(days=today.weekday())
        week_start = week_start.replace(hour=0, minute=0, second=0, microsecond=0)
        
        summary = self.financial_system.get_revenue_summary(start_date=week_start, end_date=today)
        
        return {
            "report_date": week_start.isoformat(),
            "report_type": "weekly",
            "revenue": summary,
            "generated_at": datetime.now().isoformat()
        }
    
    def generate_monthly_revenue_report(self) -> Dict[str, Any]:
        """Generate monthly revenue report"""
        today = datetime.now()
        month_start = today.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        
        summary = self.financial_system.get_revenue_summary(start_date=month_start, end_date=today)
        
        return {
            "report_date": month_start.isoformat(),
            "report_type": "monthly",
            "revenue": summary,
            "generated_at": datetime.now().isoformat()
        }
    
    def save_revenue_report(self, report: Dict[str, Any], report_type: str = "daily"):
        """Save revenue report to file"""
        reports_dir = Path("SIYEM/output/revenue_reports")
        reports_dir.mkdir(parents=True, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = reports_dir / f"{report_type}_revenue_report_{timestamp}.json"
        
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        return report_file


# Global instance
_revenue_automation = None

def get_revenue_automation() -> RevenueAutomation:
    """Get the global revenue automation instance"""
    global _revenue_automation
    if _revenue_automation is None:
        _revenue_automation = RevenueAutomation()
    return _revenue_automation
