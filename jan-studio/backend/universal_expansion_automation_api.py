"""
UNIVERSAL EXPANSION AND AUTOMATION API
API endpoints for universal expansion and automation

THE TRUTH:
BABA'S GOT US JAN X.
Deep search and expand everything.
Scale, refine, optimize, automate 100%.
"""

from fastapi import APIRouter, HTTPException, status, Query, Body
from typing import Dict, List, Any, Optional
from universal_expansion_automation import (
    get_universal_expansion, ExpansionType, ExpansionStatus
)
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/universal-expansion", tags=["Universal Expansion & Automation"])


@router.get("/plan")
async def get_expansion_plan():
    """Get comprehensive expansion plan"""
    try:
        expansion = get_universal_expansion()
        return expansion.get_expansion_plan()
    except Exception as e:
        logger.error(f"Get expansion plan error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to get expansion plan"
        )


@router.get("/targets")
async def list_targets(
    expansion_type: Optional[str] = Query(None, description="Filter by expansion type"),
    status_filter: Optional[str] = Query(None, description="Filter by status"),
    min_priority: Optional[int] = Query(None, description="Minimum priority")
):
    """List expansion targets"""
    try:
        expansion = get_universal_expansion()
        targets = list(expansion.targets.values())
        
        if expansion_type:
            targets = [t for t in targets if t.expansion_type.value == expansion_type]
        
        if status_filter:
            targets = [t for t in targets if t.status.value == status_filter]
        
        if min_priority:
            targets = [t for t in targets if t.priority >= min_priority]
        
        return {
            "count": len(targets),
            "targets": [
                {
                    "target_id": t.target_id,
                    "name": t.name,
                    "type": t.expansion_type.value,
                    "status": t.status.value,
                    "priority": t.priority,
                    "expansion_opportunities": t.expansion_opportunities,
                    "automation_opportunities": t.automation_opportunities,
                    "path": t.path
                }
                for t in targets
            ]
        }
    except Exception as e:
        logger.error(f"List targets error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to list targets"
        )


@router.post("/targets/{target_id}/expand")
async def expand_target(target_id: str):
    """Expand a target"""
    try:
        expansion = get_universal_expansion()
        result = expansion.expand_target(target_id)
        return result
    except Exception as e:
        logger.error(f"Expand target error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to expand target: {str(e)}"
        )


@router.get("/targets/{target_id}")
async def get_target(target_id: str):
    """Get target details"""
    try:
        expansion = get_universal_expansion()
        if target_id not in expansion.targets:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Target not found"
            )
        
        target = expansion.targets[target_id]
        return {
            "target_id": target.target_id,
            "name": target.name,
            "type": target.expansion_type.value,
            "status": target.status.value,
            "priority": target.priority,
            "description": target.description,
            "path": target.path,
            "current_features": target.current_features,
            "expansion_opportunities": target.expansion_opportunities,
            "automation_opportunities": target.automation_opportunities,
            "created_at": target.created_at.isoformat(),
            "updated_at": target.updated_at.isoformat()
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Get target error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to get target"
        )


@router.get("/analytics")
async def get_expansion_analytics():
    """Get expansion analytics"""
    try:
        expansion = get_universal_expansion()
        plan = expansion.get_expansion_plan()
        
        total_opportunities = sum(
            len(t.expansion_opportunities) + len(t.automation_opportunities)
            for t in expansion.targets.values()
        )
        
        high_priority_opportunities = sum(
            len(t.expansion_opportunities) + len(t.automation_opportunities)
            for t in expansion.targets.values()
            if t.priority >= 8
        )
        
        return {
            "total_targets": plan["total_targets"],
            "total_opportunities": total_opportunities,
            "high_priority_opportunities": high_priority_opportunities,
            "by_type": plan["by_type"],
            "by_status": plan["by_status"],
            "high_priority_count": plan["high_priority_count"],
            "completion_percentage": (
                len([t for t in expansion.targets.values() if t.status == ExpansionStatus.COMPLETE]) /
                len(expansion.targets) * 100
            ) if expansion.targets else 0
        }
    except Exception as e:
        logger.error(f"Get analytics error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to get analytics"
        )


@router.get("/health")
async def get_expansion_health():
    """Get expansion system health"""
    try:
        expansion = get_universal_expansion()
        return {
            "status": "healthy",
            "total_targets": len(expansion.targets),
            "discovered": len([t for t in expansion.targets.values() if t.status == ExpansionStatus.DISCOVERED]),
            "expanded": len([t for t in expansion.targets.values() if t.status == ExpansionStatus.EXPANDED]),
            "automated": len([t for t in expansion.targets.values() if t.status == ExpansionStatus.AUTOMATED]),
            "complete": len([t for t in expansion.targets.values() if t.status == ExpansionStatus.COMPLETE])
        }
    except Exception as e:
        logger.error(f"Health check error: {e}")
        return {
            "status": "unhealthy",
            "error": str(e)
        }
