"""
DEPLOYMENT DASHBOARD API
Real-time deployment status, analytics, and management

THE NOAH PROTOCOL:
- Architectural Weight: Built for comprehensive dashboards
- The Pitch: Waterproof error handling
- The Perimeter: Clear dashboard boundaries

THE TRUTH:
Scale and build until ready.
Deployment dashboards for the new world.
"""

from fastapi import APIRouter, HTTPException, status
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/deployment-dashboard", tags=["Deployment Dashboard"])


@router.get("/overview")
async def get_dashboard_overview():
    """Get complete dashboard overview"""
    try:
        # Get Raspberry Pi stats
        from raspberry_pi_deployment_api import get_deployment_manager
        pi_manager = get_deployment_manager()
        pi_deployments = pi_manager.list_deployments()
        pi_health = await pi_manager.deployment_health()
        
        # Get Education Professional stats
        from education_professional_deployment_api import get_education_manager
        edu_manager = get_education_manager()
        edu_schools = edu_manager.list_schools()
        edu_analytics = edu_manager.get_deployment_analytics()
        edu_health = await edu_manager.deployment_health()
        
        # Get Automation stats
        from deployment_automation import get_automation
        automation = get_automation()
        automation_stats = automation.get_automation_stats()
        automation_tasks = automation.list_tasks()
        
        return {
            "timestamp": datetime.now().isoformat(),
            "raspberry_pi": {
                "deployments": len(pi_deployments),
                "health": pi_health,
                "recent": pi_deployments[:5] if pi_deployments else []
            },
            "education_professional": {
                "schools": len(edu_schools),
                "analytics": edu_analytics,
                "health": edu_health,
                "recent": [
                    {
                        "school_id": s.school_id,
                        "school_name": s.school_name,
                        "status": s.deployment_status.value
                    }
                    for s in edu_schools[:5]
                ]
            },
            "automation": {
                "stats": automation_stats,
                "recent_tasks": [
                    {
                        "task_id": t.task_id,
                        "channel": t.channel.value,
                        "status": t.status.value,
                        "created_at": t.created_at.isoformat()
                    }
                    for t in automation_tasks[:10]
                ]
            }
        }
    except Exception as e:
        logger.error(f"Dashboard overview error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get dashboard overview: {str(e)}"
        )


@router.get("/analytics")
async def get_deployment_analytics():
    """Get deployment analytics"""
    try:
        from raspberry_pi_deployment_api import get_deployment_manager
        from education_professional_deployment_api import get_education_manager
        from deployment_automation import get_automation
        
        pi_manager = get_deployment_manager()
        edu_manager = get_education_manager()
        automation = get_automation()
        
        # Calculate metrics
        pi_deployments = pi_manager.list_deployments()
        edu_schools = edu_manager.list_schools()
        automation_tasks = automation.list_tasks()
        
        # Time-based analytics
        now = datetime.now()
        last_24h = now - timedelta(hours=24)
        last_7d = now - timedelta(days=7)
        last_30d = now - timedelta(days=30)
        
        pi_recent_24h = [d for d in pi_deployments if datetime.fromisoformat(d["created_at"]) > last_24h]
        pi_recent_7d = [d for d in pi_deployments if datetime.fromisoformat(d["created_at"]) > last_7d]
        pi_recent_30d = [d for d in pi_deployments if datetime.fromisoformat(d["created_at"]) > last_30d]
        
        edu_recent_24h = [s for s in edu_schools if s.created_at > last_24h]
        edu_recent_7d = [s for s in edu_schools if s.created_at > last_7d]
        edu_recent_30d = [s for s in edu_schools if s.created_at > last_30d]
        
        return {
            "timestamp": datetime.now().isoformat(),
            "raspberry_pi": {
                "total": len(pi_deployments),
                "last_24h": len(pi_recent_24h),
                "last_7d": len(pi_recent_7d),
                "last_30d": len(pi_recent_30d)
            },
            "education_professional": {
                "total_schools": len(edu_schools),
                "total_students": sum(s.student_count for s in edu_schools),
                "total_teachers": sum(s.teacher_count for s in edu_schools),
                "last_24h": len(edu_recent_24h),
                "last_7d": len(edu_recent_7d),
                "last_30d": len(edu_recent_30d)
            },
            "automation": {
                "total_tasks": len(automation_tasks),
                "completed": len([t for t in automation_tasks if t.status.value == "completed"]),
                "failed": len([t for t in automation_tasks if t.status.value == "failed"]),
                "in_progress": len([t for t in automation_tasks if t.status.value in ["building", "testing", "deploying"]])
            }
        }
    except Exception as e:
        logger.error(f"Analytics error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get analytics: {str(e)}"
        )


@router.get("/health")
async def get_deployment_health():
    """Get deployment system health"""
    try:
        from raspberry_pi_deployment_api import get_deployment_manager
        from education_professional_deployment_api import get_education_manager
        
        pi_manager = get_deployment_manager()
        edu_manager = get_education_manager()
        
        pi_health = await pi_manager.deployment_health()
        edu_health = await edu_manager.deployment_health()
        
        overall_healthy = (
            pi_health.get("status") == "healthy" and
            edu_health.get("status") == "healthy"
        )
        
        return {
            "timestamp": datetime.now().isoformat(),
            "overall_healthy": overall_healthy,
            "raspberry_pi": pi_health,
            "education_professional": edu_health
        }
    except Exception as e:
        logger.error(f"Health check error: {e}")
        return {
            "timestamp": datetime.now().isoformat(),
            "overall_healthy": False,
            "error": str(e)
        }
