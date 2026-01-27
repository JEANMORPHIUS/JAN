"""
GIT AUTOMATION - AUTO STAGE, COMMIT, PUSH
Everything we build should be shared

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X.

FAITH: NOTHING TO HIDE
Everything we build should be shared.
"""

import subprocess
import logging
from pathlib import Path
from typing import Optional, List, Dict, Any
from datetime import datetime
from functools import wraps

logger = logging.getLogger(__name__)


def get_git_root(path: Path = None) -> Optional[Path]:
    """
    Find the git repository root directory.
    
    Args:
        path: Starting path (defaults to current directory)
    
    Returns:
        Path to git root or None if not in a git repo
    """
    if path is None:
        path = Path.cwd()
    
    path = Path(path).resolve()
    
    # Check if we're in a git repo
    for parent in [path] + list(path.parents):
        if (parent / '.git').exists():
            return parent
    
    return None


def run_git_command(command: List[str], cwd: Optional[Path] = None, check: bool = True) -> Dict[str, Any]:
    """
    Run a git command and return the result.
    
    Args:
        command: Git command as list (e.g., ['git', 'add', '.'])
        cwd: Working directory (defaults to git root)
        check: Raise exception on error (default: True)
    
    Returns:
        Dict with 'success', 'stdout', 'stderr', 'returncode'
    """
    git_root = get_git_root(cwd) if cwd else get_git_root()
    
    if not git_root:
        logger.warning("Not in a git repository - skipping git operations")
        return {
            'success': False,
            'stdout': '',
            'stderr': 'Not in a git repository',
            'returncode': -1
        }
    
    try:
        result = subprocess.run(
            command,
            cwd=git_root,
            capture_output=True,
            text=True,
            check=check,
            timeout=30
        )
        
        return {
            'success': result.returncode == 0,
            'stdout': result.stdout.strip(),
            'stderr': result.stderr.strip(),
            'returncode': result.returncode
        }
    except subprocess.TimeoutExpired:
        logger.error(f"Git command timed out: {' '.join(command)}")
        return {
            'success': False,
            'stdout': '',
            'stderr': 'Command timed out',
            'returncode': -1
        }
    except subprocess.CalledProcessError as e:
        logger.error(f"Git command failed: {' '.join(command)} - {e}")
        return {
            'success': False,
            'stdout': e.stdout.strip() if e.stdout else '',
            'stderr': e.stderr.strip() if e.stderr else str(e),
            'returncode': e.returncode
        }
    except Exception as e:
        logger.error(f"Error running git command: {' '.join(command)} - {e}")
        return {
            'success': False,
            'stdout': '',
            'stderr': str(e),
            'returncode': -1
        }


def git_status() -> Dict[str, Any]:
    """
    Get git status.
    
    Returns:
        Dict with status information
    """
    result = run_git_command(['git', 'status', '--porcelain'], check=False)
    
    if not result['success']:
        return {'has_changes': False, 'files': []}
    
    lines = result['stdout'].strip().split('\n') if result['stdout'] else []
    files = [line for line in lines if line.strip()]
    
    return {
        'has_changes': len(files) > 0,
        'files': files,
        'count': len(files)
    }


def git_stage_all() -> bool:
    """
    Stage all changes (git add .).
    
    Returns:
        True if successful
    """
    result = run_git_command(['git', 'add', '.'])
    
    if result['success']:
        logger.info("✅ All changes staged")
    else:
        logger.warning(f"⚠️ Failed to stage changes: {result['stderr']}")
    
    return result['success']


def git_commit(message: str, allow_empty: bool = False) -> bool:
    """
    Commit staged changes.
    
    Args:
        message: Commit message
        allow_empty: Allow empty commits (default: False)
    
    Returns:
        True if successful
    """
    cmd = ['git', 'commit', '-m', message]
    if allow_empty:
        cmd.append('--allow-empty')
    
    result = run_git_command(cmd, check=False)
    
    if result['success']:
        logger.info(f"✅ Committed: {message}")
    elif 'nothing to commit' in result['stderr'].lower():
        logger.info("ℹ️ Nothing to commit (working tree clean)")
        return True  # Not an error - just nothing to commit
    else:
        logger.warning(f"⚠️ Failed to commit: {result['stderr']}")
    
    return result['success'] or 'nothing to commit' in result['stderr'].lower()


def git_push(branch: Optional[str] = None, force: bool = False) -> bool:
    """
    Push commits to remote.
    
    Args:
        branch: Branch to push (defaults to current branch)
        force: Force push (default: False)
    
    Returns:
        True if successful
    """
    # Get current branch if not specified
    if not branch:
        result = run_git_command(['git', 'branch', '--show-current'], check=False)
        if result['success']:
            branch = result['stdout'].strip()
        else:
            logger.warning("Could not determine current branch")
            return False
    
    cmd = ['git', 'push']
    if force:
        cmd.append('--force')
    cmd.extend(['origin', branch])
    
    result = run_git_command(cmd, check=False)
    
    if result['success']:
        logger.info(f"✅ Pushed to origin/{branch}")
    else:
        logger.warning(f"⚠️ Failed to push: {result['stderr']}")
    
    return result['success']


def auto_commit_and_push(
    message: Optional[str] = None,
    auto_message: bool = True,
    push: bool = True,
    skip_if_clean: bool = True
) -> Dict[str, Any]:
    """
    Automatically stage, commit, and push all changes.
    
    Args:
        message: Custom commit message (if None, auto-generates)
        auto_message: Auto-generate message if None (default: True)
        push: Push to remote after commit (default: True)
        skip_if_clean: Skip if working tree is clean (default: True)
    
    Returns:
        Dict with operation results
    """
    git_root = get_git_root()
    
    if not git_root:
        return {
            'success': False,
            'message': 'Not in a git repository',
            'staged': False,
            'committed': False,
            'pushed': False
        }
    
    # Check status
    status = git_status()
    
    if skip_if_clean and not status['has_changes']:
        logger.info("ℹ️ Working tree clean - nothing to commit")
        return {
            'success': True,
            'message': 'Working tree clean',
            'staged': False,
            'committed': False,
            'pushed': False
        }
    
    # Generate commit message if needed
    if not message and auto_message:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"✨ Auto-commit: {timestamp}\n\nAll changes staged, committed, and shared.\n\nFaith. Nothing to hide. ✨🙏"
    
    results = {
        'success': True,
        'message': message,
        'staged': False,
        'committed': False,
        'pushed': False,
        'files_changed': status['count']
    }
    
    # Stage all changes
    if status['has_changes']:
        results['staged'] = git_stage_all()
        if not results['staged']:
            results['success'] = False
            return results
    
    # Commit
    results['committed'] = git_commit(message or "Auto-commit")
    if not results['committed']:
        results['success'] = False
        return results
    
    # Push
    if push and results['committed']:
        results['pushed'] = git_push()
        if not results['pushed']:
            results['success'] = False
    
    return results


def auto_share_decorator(message: Optional[str] = None, push: bool = True):
    """
    Decorator to automatically commit and push after function execution.
    
    Usage:
        @auto_share_decorator(message="Custom message")
        def my_function():
            # ... do work ...
            pass
    
    Args:
        message: Commit message (auto-generated if None)
        push: Push to remote (default: True)
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Execute the function
            result = func(*args, **kwargs)
            
            # Auto-commit and push
            try:
                commit_message = message or f"✨ Auto-commit: {func.__name__}\n\nAll changes from {func.__name__} shared.\n\nFaith. Nothing to hide. ✨🙏"
                auto_commit_and_push(message=commit_message, push=push)
            except Exception as e:
                logger.warning(f"Auto-commit failed after {func.__name__}: {e}")
            
            return result
        return wrapper
    return decorator


def standard_main_with_auto_share(
    main_func,
    message: Optional[str] = None,
    push: bool = True
):
    """
    Wrapper for standard_main pattern that auto-commits and pushes.
    
    Usage:
        if __name__ == "__main__":
            standard_main_with_auto_share(main, message="Custom message")
    
    Args:
        main_func: Main function to execute
        message: Commit message (auto-generated if None)
        push: Push to remote (default: True)
    """
    try:
        # Execute main function
        result = main_func()
        
        # Auto-commit and push
        commit_message = message or f"✨ Auto-commit: {main_func.__name__}\n\nAll changes from {main_func.__name__} shared.\n\nFaith. Nothing to hide. ✨🙏"
        auto_commit_and_push(message=commit_message, push=push)
        
        return result
    except Exception as e:
        logger.error(f"Error in {main_func.__name__}: {e}")
        raise


# Convenience function for scripts
def share_everything(message: Optional[str] = None, push: bool = True) -> Dict[str, Any]:
    """
    Convenience function: Stage, commit, and push everything.
    
    Usage in scripts:
        from scripts.utils.git_automation import share_everything
        
        # ... do work ...
        
        share_everything(message="Custom message")
    
    Args:
        message: Commit message (auto-generated if None)
        push: Push to remote (default: True)
    
    Returns:
        Dict with operation results
    """
    return auto_commit_and_push(message=message, push=push)
