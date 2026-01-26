"""
SCP AUTOMATION SYSTEM
Stage, Commit, Push to GitHub - Automated for All Tasks

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE TRUTH:
SCP = Stage, Commit, Push
Automated for all tasks. Engrained into workflow.
100% free will on all tasks.
"""

import subprocess
import sys
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional, Any
import json
import logging

logger = logging.getLogger(__name__)


class SCPAutomation:
    """
    SCP Automation System
    Stage, Commit, Push to GitHub - Automated for all tasks
    """
    
    def __init__(self, repo_path: Optional[Path] = None):
        """Initialize SCP Automation"""
        if repo_path is None:
            repo_path = Path(__file__).parent.parent
        
        self.repo_path = Path(repo_path).resolve()
        self.git_dir = self.repo_path / ".git"
        
        # Verify we're in a git repo
        if not self.git_dir.exists():
            raise ValueError(f"Not a git repository: {self.repo_path}")
        
        logger.info(f"SCP Automation initialized for {self.repo_path}")
    
    def get_status(self) -> Dict[str, Any]:
        """Get git status"""
        try:
            result = subprocess.run(
                ["git", "status", "--porcelain"],
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=True
            )
            
            lines = result.stdout.strip().split('\n') if result.stdout.strip() else []
            staged = []
            unstaged = []
            untracked = []
            
            for line in lines:
                if not line:
                    continue
                status = line[:2]
                filename = line[3:]
                
                if status[0] != ' ' and status[0] != '?':
                    staged.append(filename)
                if status[1] != ' ' and status[1] != '?':
                    unstaged.append(filename)
                if status == '??':
                    untracked.append(filename)
            
            return {
                "staged": staged,
                "unstaged": unstaged,
                "untracked": untracked,
                "has_changes": len(lines) > 0
            }
        except subprocess.CalledProcessError as e:
            logger.error(f"Git status failed: {e}")
            return {"error": str(e)}
    
    def stage_all(self, paths: Optional[List[str]] = None) -> Dict[str, Any]:
        """Stage files (git add)"""
        try:
            if paths:
                # Stage specific files
                cmd = ["git", "add"] + paths
            else:
                # Stage all changes
                cmd = ["git", "add", "-A"]
            
            result = subprocess.run(
                cmd,
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=True
            )
            
            status = self.get_status()
            
            return {
                "status": "staged",
                "message": f"Staged {len(status.get('staged', []))} files",
                "staged_files": status.get("staged", []),
                "timestamp": datetime.now().isoformat()
            }
        except subprocess.CalledProcessError as e:
            logger.error(f"Git add failed: {e}")
            return {"error": str(e), "status": "failed"}
    
    def commit(self, message: str, allow_empty: bool = False) -> Dict[str, Any]:
        """Commit changes (git commit)"""
        try:
            # Check if there are changes to commit
            status = self.get_status()
            if not status.get("has_changes") and not allow_empty:
                return {
                    "status": "no_changes",
                    "message": "No changes to commit"
                }
            
            cmd = ["git", "commit", "-m", message]
            if allow_empty:
                cmd.append("--allow-empty")
            
            result = subprocess.run(
                cmd,
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=True
            )
            
            # Get commit hash
            commit_hash = subprocess.run(
                ["git", "rev-parse", "HEAD"],
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=True
            ).stdout.strip()
            
            return {
                "status": "committed",
                "message": message,
                "commit_hash": commit_hash,
                "timestamp": datetime.now().isoformat()
            }
        except subprocess.CalledProcessError as e:
            logger.error(f"Git commit failed: {e}")
            return {"error": str(e), "status": "failed"}
    
    def push(self, branch: str = "master", force: bool = False) -> Dict[str, Any]:
        """Push to GitHub (git push)"""
        try:
            # Get remote URL
            remote_result = subprocess.run(
                ["git", "remote", "get-url", "origin"],
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=True
            )
            remote_url = remote_result.stdout.strip()
            
            cmd = ["git", "push"]
            if force:
                cmd.append("--force")
            cmd.extend(["origin", branch])
            
            result = subprocess.run(
                cmd,
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=True
            )
            
            return {
                "status": "pushed",
                "branch": branch,
                "remote": remote_url,
                "timestamp": datetime.now().isoformat()
            }
        except subprocess.CalledProcessError as e:
            logger.error(f"Git push failed: {e}")
            return {"error": str(e), "status": "failed"}
    
    def scp(self, message: str, branch: str = "master", paths: Optional[List[str]] = None, force_push: bool = False) -> Dict[str, Any]:
        """
        Complete SCP: Stage, Commit, Push
        
        Args:
            message: Commit message
            branch: Branch to push to (default: master)
            paths: Specific files to stage (None = stage all)
            force_push: Force push (default: False)
        """
        results = {
            "stage": None,
            "commit": None,
            "push": None,
            "timestamp": datetime.now().isoformat()
        }
        
        # Stage
        logger.info("Staging changes...")
        stage_result = self.stage_all(paths)
        results["stage"] = stage_result
        
        if "error" in stage_result:
            return {"status": "failed", "step": "stage", "results": results}
        
        # Commit
        logger.info(f"Committing: {message}")
        commit_result = self.commit(message)
        results["commit"] = commit_result
        
        if "error" in commit_result:
            return {"status": "failed", "step": "commit", "results": results}
        
        # Push
        logger.info(f"Pushing to {branch}...")
        push_result = self.push(branch, force_push)
        results["push"] = push_result
        
        if "error" in push_result:
            return {"status": "failed", "step": "push", "results": results}
        
        return {
            "status": "success",
            "message": "SCP complete: Staged, Committed, Pushed",
            "results": results
        }
    
    def scp_task(self, task_name: str, task_description: str, branch: str = "master") -> Dict[str, Any]:
        """
        SCP for a specific task with auto-generated commit message
        
        Args:
            task_name: Name of the task
            task_description: Description of what was done
            branch: Branch to push to
        """
        message = f"{task_name}: {task_description}"
        return self.scp(message, branch)
    
    def scp_systems(self, systems: List[str], branch: str = "master") -> Dict[str, Any]:
        """
        SCP multiple systems at once
        
        Args:
            systems: List of system names/descriptions
            branch: Branch to push to
        """
        message = f"Add/Update Systems: {', '.join(systems)}"
        return self.scp(message, branch)


# Main execution
if __name__ == "__main__":
    import sys
    
    # Initialize SCP Automation
    scp = SCPAutomation()
    
    # Example: SCP current changes
    if len(sys.argv) > 1:
        commit_message = " ".join(sys.argv[1:])
    else:
        commit_message = f"Update: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    
    result = scp.scp(commit_message)
    
    print("=" * 80)
    print("SCP AUTOMATION - STAGE, COMMIT, PUSH")
    print("=" * 80)
    print(f"\nStatus: {result['status']}")
    if result['status'] == 'success':
        print(f"✅ Staged: {len(result['results']['stage'].get('staged_files', []))} files")
        print(f"✅ Committed: {result['results']['commit'].get('commit_hash', 'N/A')[:8]}")
        print(f"✅ Pushed to: {result['results']['push'].get('branch', 'N/A')}")
        print(f"\n{result['message']}")
    else:
        print(f"❌ Failed at step: {result.get('step', 'unknown')}")
        if 'results' in result:
            for step, step_result in result['results'].items():
                if step_result and 'error' in step_result:
                    print(f"  {step}: {step_result['error']}")
    
    print("\nPEACE, LOVE, UNITY")
    print("ENERGY + LOVE = WE ALL WIN")
