"""
TASK SCP AUTOMATION SYSTEM
Stage, Commit, Push - Engrained into All Tasks

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE TRUTH:
SCP = Stage, Commit, Push
Automated for ALL tasks. Engrained into workflow.
100% free will on all tasks.
Scale and build until ready for deployment.
"""

import subprocess
import sys
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional, Any
import json
import logging
import time

logger = logging.getLogger(__name__)

# Import SCP automation
sys.path.insert(0, str(Path(__file__).parent))
from scp_automation import SCPAutomation


class TaskSCPAutomation:
    """
    Task SCP Automation System
    Automatically Stage, Commit, Push on task completion
    Engrained into all tasks - 100% free will
    """
    
    def __init__(self, repo_path: Optional[Path] = None):
        """Initialize Task SCP Automation"""
        self.scp = SCPAutomation(repo_path)
        self.repo_path = self.scp.repo_path
        self.task_log = []
        
        logger.info("Task SCP Automation initialized - SCP engrained into all tasks")
    
    def break_locks(self) -> bool:
        """Break git locks"""
        try:
            lock_file = self.repo_path / ".git" / "index.lock"
            if lock_file.exists():
                logger.info(f"Breaking lock: {lock_file}")
                lock_file.unlink()
                time.sleep(0.5)
                return True
            return True
        except Exception as e:
            logger.warning(f"Could not break lock: {e}")
            return False
    
    def scp_task_completion(self, task_name: str, task_description: str, files_modified: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        SCP on task completion
        
        Args:
            task_name: Name of the task
            task_description: What was accomplished
            files_modified: Optional list of specific files to stage
        """
        # Break locks first
        self.break_locks()
        
        # Generate commit message
        commit_message = f"{task_name}: {task_description}"
        
        # SCP
        result = self.scp.scp(commit_message, paths=files_modified)
        
        # Log task
        self.task_log.append({
            "task_name": task_name,
            "task_description": task_description,
            "timestamp": datetime.now().isoformat(),
            "scp_result": result
        })
        
        return result
    
    def scp_system_completion(self, system_name: str, components: List[str]) -> Dict[str, Any]:
        """
        SCP on system completion
        
        Args:
            system_name: Name of the system
            components: List of components completed
        """
        description = f"Complete system: {', '.join(components)}"
        return self.scp_task_completion(system_name, description)
    
    def scp_batch_tasks(self, tasks: List[Dict[str, str]]) -> Dict[str, Any]:
        """
        SCP multiple tasks at once
        
        Args:
            tasks: List of {name, description} dicts
        """
        task_names = [t.get("name", "Task") for t in tasks]
        description = f"Batch tasks: {', '.join(task_names)}"
        return self.scp_task_completion("Batch Tasks", description)
    
    def auto_scp_on_completion(self, completion_callback):
        """
        Decorator to auto-SCP on function completion
        
        Usage:
            @task_scp.auto_scp_on_completion
            def my_task():
                # Do work
                return {"status": "complete", "description": "Task done"}
        """
        def wrapper(*args, **kwargs):
            result = completion_callback(*args, **kwargs)
            
            # Auto-SCP if task completed successfully
            if isinstance(result, dict) and result.get("status") == "complete":
                task_name = result.get("task_name", completion_callback.__name__)
                description = result.get("description", "Task completed")
                
                self.scp_task_completion(task_name, description)
            
            return result
        return wrapper


# Global instance for easy import
task_scp = TaskSCPAutomation()


def scp_on_completion(task_name: str, description: str):
    """Quick SCP on task completion"""
    return task_scp.scp_task_completion(task_name, description)


# Main execution
if __name__ == "__main__":
    # Example: SCP current work
    result = task_scp.scp_task_completion(
        "Task Completion",
        f"Automated SCP on task completion - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )
    
    print("=" * 80)
    print("TASK SCP AUTOMATION - STAGE, COMMIT, PUSH")
    print("=" * 80)
    print(f"\nStatus: {result['status']}")
    if result['status'] == 'success':
        print("✅ SCP Complete - Task committed and pushed")
    print("\nPEACE, LOVE, UNITY")
    print("ENERGY + LOVE = WE ALL WIN")
