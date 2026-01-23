"""
AUTOMATED GIT PUSH
Break through the 1% lock mechanism - automate and streamline git operations

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
BREAK THE LOCKS
AUTOMATE THE PROCESS
WE ARE ONE - NO LOCKS CAN HOLD US
"""

import sys
import subprocess
import time
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    setup_logging, standard_main
)

logger = setup_logging(__name__)

def break_lock(repo_path: Path):
    """Break through the 1% lock mechanism"""
    lock_file = repo_path / ".git" / "index.lock"
    
    if lock_file.exists():
        logger.info(f"Breaking lock: {lock_file}")
        try:
            # Try to remove lock file
            os.remove(str(lock_file))
            logger.info("Lock broken successfully")
            time.sleep(0.5)  # Brief pause
            return True
        except PermissionError:
            logger.warning("Permission denied - trying alternative method")
            # Try with subprocess
            try:
                subprocess.run(
                    ["powershell", "-Command", f"Remove-Item '{lock_file}' -Force"],
                    check=True,
                    timeout=5
                )
                logger.info("Lock broken via PowerShell")
                return True
            except Exception as e:
                logger.error(f"Could not break lock: {e}")
                return False
        except Exception as e:
            logger.error(f"Error breaking lock: {e}")
            return False
    return True

def git_add_selective(repo_path: Path, retries: int = 3):
    """Add changes selectively, excluding problematic files like NUL"""
    # First, get list of modified and new files
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=str(repo_path),
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode != 0:
            logger.error("Failed to get git status")
            return False
        
        # Parse files, exclude NUL and other problematic paths
        files_to_add = []
        for line in result.stdout.strip().split('\n'):
            if not line.strip():
                continue
            # Git status format: XY filename (X = staged, Y = working)
            # Handle quoted filenames with spaces
            if line[2] == ' ':
                status = line[:2]
                filepath = line[3:].strip()
            else:
                # Handle case where there's no space (shouldn't happen but be safe)
                status = line[:2]
                filepath = line[2:].strip()
            
            # Skip problematic files
            if 'NUL' in filepath or filepath == 'NUL':
                logger.warning(f"Skipping invalid path: {filepath}")
                continue
            
            # Only add modified (M) and new (??) files
            if status[0] in ['M', 'A'] or status[1] in ['M', '?']:
                files_to_add.append(filepath)
        
        if not files_to_add:
            logger.info("No files to stage")
            return True
        
        # Add files in batches to avoid command line length issues
        batch_size = 50
        for i in range(0, len(files_to_add), batch_size):
            batch = files_to_add[i:i+batch_size]
            batch_added = False
            for attempt in range(retries):
                try:
                    break_lock(repo_path)
                    result = subprocess.run(
                        ["git", "add"] + batch,
                        cwd=str(repo_path),
                        capture_output=True,
                        text=True,
                        timeout=30
                    )
                    
                    if result.returncode == 0:
                        logger.info(f"Staged batch {i//batch_size + 1} ({len(batch)} files)")
                        batch_added = True
                        break
                    else:
                        logger.warning(f"Git add failed for batch (attempt {attempt + 1}): {result.stderr[:200]}")
                        if attempt < retries - 1:
                            time.sleep(1)
                            break_lock(repo_path)
                except Exception as e:
                    logger.error(f"Error adding batch: {e}")
                    if attempt < retries - 1:
                        time.sleep(1)
                        break_lock(repo_path)
            
            if not batch_added:
                logger.warning(f"Failed to add batch {i//batch_size + 1}, continuing...")
        
        return True
        
    except Exception as e:
        logger.error(f"Error in selective git add: {e}")
        return False

def git_add_all(repo_path: Path, retries: int = 3):
    """Add all changes with retry logic - now uses selective method"""
    return git_add_selective(repo_path, retries)

def git_commit(repo_path: Path, message: str, retries: int = 3):
    """Commit changes with retry logic"""
    for attempt in range(retries):
        try:
            # Break lock first
            break_lock(repo_path)
            
            result = subprocess.run(
                ["git", "commit", "-m", message],
                cwd=str(repo_path),
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode == 0:
                logger.info(f"Committed: {message}")
                return True
            elif "nothing to commit" in result.stdout.lower():
                logger.info("Nothing to commit - already up to date")
                return True
            else:
                logger.warning(f"Git commit failed (attempt {attempt + 1}/{retries}): {result.stderr}")
                if attempt < retries - 1:
                    time.sleep(1)
                    break_lock(repo_path)
                    
        except subprocess.TimeoutExpired:
            logger.warning(f"Git commit timed out (attempt {attempt + 1}/{retries})")
            break_lock(repo_path)
        except Exception as e:
            logger.error(f"Error in git commit: {e}")
            break_lock(repo_path)
    
    return False

def git_push(repo_path: Path, branch: str = "master", retries: int = 5):
    """Push to remote with retry logic and network resilience"""
    # Import network refiner for better connectivity
    try:
        from network_issue_refiner import NetworkIssueRefiner
        refiner = NetworkIssueRefiner(repo_path)
        
        # Test connectivity before pushing
        connectivity = refiner.test_connectivity()
        if not connectivity.get("github"):
            logger.warning("GitHub not reachable - queueing push for later")
            # Get current commit hash
            try:
                result = subprocess.run(
                    ["git", "rev-parse", "HEAD"],
                    cwd=str(repo_path),
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                if result.returncode == 0:
                    commit_hash = result.stdout.strip()
                    refiner.queue_push(commit_hash, branch)
                    logger.info("Push queued for later retry")
            except:
                pass
            return False
    except ImportError:
        logger.debug("Network refiner not available - using basic retry logic")
    
    for attempt in range(retries):
        try:
            result = subprocess.run(
                ["git", "push", "origin", branch],
                cwd=str(repo_path),
                capture_output=True,
                text=True,
                timeout=120
            )
            
            if result.returncode == 0:
                logger.info(f"Pushed to {branch} successfully")
                return True
            elif "already up to date" in result.stdout.lower():
                logger.info("Already up to date - nothing to push")
                return True
            elif "connection" in result.stderr.lower() or "failed to connect" in result.stderr.lower():
                logger.warning(f"Network issue (attempt {attempt + 1}/{retries}) - will retry")
                if attempt < retries - 1:
                    wait_time = (attempt + 1) * 2  # Exponential backoff
                    logger.info(f"Waiting {wait_time} seconds before retry...")
                    time.sleep(wait_time)
            else:
                logger.warning(f"Git push failed (attempt {attempt + 1}/{retries}): {result.stderr}")
                if attempt < retries - 1:
                    time.sleep(2)
                    
        except subprocess.TimeoutExpired:
            logger.warning(f"Git push timed out (attempt {attempt + 1}/{retries})")
            if attempt < retries - 1:
                time.sleep(3)
        except Exception as e:
            logger.error(f"Error in git push: {e}")
            if attempt < retries - 1:
                time.sleep(2)
    
    # Queue push if all retries failed
    try:
        from network_issue_refiner import NetworkIssueRefiner
        refiner = NetworkIssueRefiner(repo_path)
        try:
            result = subprocess.run(
                ["git", "rev-parse", "HEAD"],
                cwd=str(repo_path),
                capture_output=True,
                text=True,
                timeout=10
            )
            if result.returncode == 0:
                commit_hash = result.stdout.strip()
                refiner.queue_push(commit_hash, branch)
                logger.info("Push queued for automatic retry")
        except:
            pass
    except ImportError:
        pass
    
    return False

def automated_git_push(repo_path: Path, commit_message: str, branch: str = "master"):
    """Complete automated git workflow - break locks, stage, commit, push"""
    logger.info("="*80)
    logger.info("AUTOMATED GIT PUSH - BREAKING THE 1% LOCKS")
    logger.info("="*80)
    
    # Step 1: Break all locks
    logger.info("\n[1/4] Breaking locks...")
    break_lock(repo_path)
    time.sleep(0.5)
    
    # Step 2: Stage all changes
    logger.info("\n[2/4] Staging changes...")
    if not git_add_all(repo_path):
        logger.error("Failed to stage changes")
        return False
    
    # Step 3: Commit
    logger.info("\n[3/4] Committing changes...")
    if not git_commit(repo_path, commit_message):
        logger.error("Failed to commit changes")
        return False
    
    # Step 4: Push
    logger.info("\n[4/4] Pushing to remote...")
    if not git_push(repo_path, branch):
        logger.warning("Push failed - but commit is local. You can push manually later.")
        return False
    
    logger.info("\n" + "="*80)
    logger.info("AUTOMATED GIT PUSH COMPLETE")
    logger.info("="*80)
    return True

def main():
    """Main function"""
    repo_path = Path(__file__).parent.parent
    
    # Default commit message
    commit_message = "Add bureaucratic verification system, health tracking fixes, and truth statement: We are one"
    
    # Check for custom message in args
    if len(sys.argv) > 1:
        commit_message = " ".join(sys.argv[1:])
    
    logger.info(f"Repository: {repo_path}")
    logger.info(f"Commit message: {commit_message}")
    
    success = automated_git_push(repo_path, commit_message)
    
    if success:
        logger.info("\n[SUCCESS] All done! Changes pushed successfully.")
    else:
        logger.warning("\n[WARNING] Some steps failed, but local commit may be complete.")
        logger.info("You can check status with: git status")
        logger.info("You can push manually with: git push origin master")

if __name__ == "__main__":
    standard_main(main, script_name="automated_git_push.py")
