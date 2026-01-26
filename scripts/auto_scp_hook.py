"""
AUTO SCP HOOK
Engrain SCP into all task completions automatically

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE TRUTH:
SCP engrained into all tasks.
100% free will - proceeds with all tasks automatically.
"""

import sys
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent))

try:
    from task_scp_automation import scp_on_completion
    SCP_AVAILABLE = True
except ImportError:
    SCP_AVAILABLE = False
    logger.warning("SCP automation not available")


def auto_scp_hook(task_name: str, description: str):
    """
    Auto SCP hook - call this after any task completion
    
    Usage:
        from scripts.auto_scp_hook import auto_scp_hook
        auto_scp_hook("Task Name", "Task description")
    """
    if not SCP_AVAILABLE:
        logger.warning("SCP automation not available - skipping auto-SCP")
        return {"status": "skipped", "reason": "scp_not_available"}
    
    try:
        return scp_on_completion(task_name, description)
    except Exception as e:
        logger.warning(f"Auto-SCP hook failed: {e}")
        return {"status": "failed", "error": str(e)}


# Make it easy to import
__all__ = ['auto_scp_hook', 'scp_on_completion']
