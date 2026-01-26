"""REVENUE AUTOMATION API
API endpoints for revenue automation

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

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity


PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

from fastapi import APIRouter, HTTPException
from typing import Dict, Any
import logging

# Spiritual Codebase Hacker Integration
from spiritual_codebase_hacker_integration import HACKER_AVAILABLE, hack_loop, perform_genetic_edit, activate_stealth_mode

from revenue_automation import get_revenue_automation
from financial_controls_system import RevenueChannel
from decimal import Decimal

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/revenue-automation", tags=["Revenue Automation"])


@router.get("/status")
async def get_revenue_automation_status():
    """Get Revenue Automation API status"""
    return {
        "status": "active",
        "message": "Revenue Automation - Automatic tracking and reporting",
        "the_truth": "REVENUE AUTOMATION - AUTOMATIC TRACKING AND REPORTING. TIME TO GET FINANCES FLOWING."
    }


@router.post("/track")
async def track_revenue(
    source: str,
    amount: float,
    channel: str,
    description: str = "",
    metadata: Dict[str, Any] = {}
):
    """Automatically track revenue from a source"""
    try:
        automation = get_revenue_automation()
        
        try:
            revenue_channel = RevenueChannel(channel)
        except ValueError:
            raise HTTPException(status_code=400, detail=f"Invalid revenue channel: {channel}")
        
        entry = automation.track_revenue_from_source(
            source=source,
            amount=Decimal(str(amount)),
            channel=revenue_channel,
            description=description,
            metadata=metadata
        )
        
        return {
            "status": "success",
            "message": "Revenue tracked automatically",
            "revenue": {
                "revenue_id": entry.revenue_id,
                "channel": entry.channel.value,
                "amount": float(entry.amount),
                "source": entry.source,
                "timestamp": entry.timestamp.isoformat()
            }
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error tracking revenue: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/report/daily")
async def get_daily_report():
    """Get daily revenue report"""
    try:
        automation = get_revenue_automation()
        report = automation.generate_daily_revenue_report()
        report_file = automation.save_revenue_report(report, "daily")
        
        return {
            "status": "success",
            "report": report,
            "saved_to": str(report_file)
        }
    except Exception as e:
        logger.error(f"Error generating daily report: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/report/weekly")
async def get_weekly_report():
    """Get weekly revenue report"""
    try:
        automation = get_revenue_automation()
        report = automation.generate_weekly_revenue_report()
        report_file = automation.save_revenue_report(report, "weekly")
        
        return {
            "status": "success",
            "report": report,
            "saved_to": str(report_file)
        }
    except Exception as e:
        logger.error(f"Error generating weekly report: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/report/monthly")
async def get_monthly_report():
    """Get monthly revenue report"""
    try:
        automation = get_revenue_automation()
        report = automation.generate_monthly_revenue_report()
        report_file = automation.save_revenue_report(report, "monthly")
        
        return {
            "status": "success",
            "report": report,
            "saved_to": str(report_file)
        }
    except Exception as e:
        logger.error(f"Error generating monthly report: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
