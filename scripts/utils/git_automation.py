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
            timeout=120  # Increased timeout for large repos
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


def analyze_changes() -> Dict[str, Any]:
    """
    Analyze git changes to generate intelligent commit message.
    
    Returns:
        Dict with change analysis
    """
    status = git_status()
    
    if not status['has_changes']:
        return {
            'new_files': [],
            'modified_files': [],
            'deleted_files': [],
            'categories': {},
            'summary': 'No changes'
        }
    
    new_files = []
    modified_files = []
    deleted_files = []
    categories = {}
    
    for line in status['files']:
        if not line.strip():
            continue
        
        # Parse git status line (format: "XY filename" or "?? filename")
        parts = line.strip().split(None, 1)
        if len(parts) < 2:
            continue
        
        status_code = parts[0]
        filepath = parts[1]
        
        # Categorize by file type
        file_path = Path(filepath)
        ext = file_path.suffix.lower()
        parent_dir = file_path.parts[0] if file_path.parts else ''
        
        # Determine change type
        if status_code == '??' or status_code.startswith('A'):
            new_files.append(filepath)
            change_type = 'new'
        elif status_code.startswith('D'):
            deleted_files.append(filepath)
            change_type = 'deleted'
        else:
            modified_files.append(filepath)
            change_type = 'modified'
        
        # Categorize
        if ext == '.py':
            category = 'Python Scripts'
        elif ext == '.md':
            category = 'Documentation'
        elif ext == '.json':
            category = 'Data/Config'
        elif ext == '.ts' or ext == '.tsx':
            category = 'TypeScript'
        elif ext == '.ps1':
            category = 'PowerShell'
        elif ext in ['.db', '.sqlite', '.sqlite3']:
            category = 'Database'
        elif parent_dir in ['scripts', 'jan-studio', 'SIYEM', 'ark', 'ATILOK', 'EDIBLE_LONDON', 'EDIBLE_CYPRUS', 'ILVEN_SEAMOSS']:
            category = parent_dir.replace('_', ' ').title()
        else:
            category = 'Other'
        
        if category not in categories:
            categories[category] = {'new': 0, 'modified': 0, 'deleted': 0}
        categories[category][change_type] = categories[category].get(change_type, 0) + 1
    
    return {
        'new_files': new_files,
        'modified_files': modified_files,
        'deleted_files': deleted_files,
        'categories': categories,
        'summary': f"{len(new_files)} new, {len(modified_files)} modified, {len(deleted_files)} deleted"
    }


def generate_intelligent_commit_message() -> str:
    """
    Generate intelligent commit message based on changes.
    
    Returns:
        Commit message string
    """
    analysis = analyze_changes()
    
    if analysis['summary'] == 'No changes':
        return "✨ No changes to commit"
    
    # Build message components
    parts = []
    emoji = "✨"
    
    # Primary change summary
    new_count = len(analysis['new_files'])
    mod_count = len(analysis['modified_files'])
    del_count = len(analysis['deleted_files'])
    
    if new_count > 0 and mod_count == 0 and del_count == 0:
        emoji = "✨"
        parts.append(f"✨ NEW: {new_count} file(s) created")
    elif mod_count > 0 and new_count == 0 and del_count == 0:
        emoji = "🔄"
        parts.append(f"🔄 UPDATE: {mod_count} file(s) modified")
    elif del_count > 0:
        emoji = "🗑️"
        parts.append(f"🗑️ REMOVE: {del_count} file(s) deleted")
    else:
        parts.append(f"✨ CHANGE: {analysis['summary']}")
    
    # Category breakdown
    if analysis['categories']:
        category_lines = []
        for category, counts in sorted(analysis['categories'].items()):
            cat_parts = []
            if counts.get('new', 0) > 0:
                cat_parts.append(f"{counts['new']} new")
            if counts.get('modified', 0) > 0:
                cat_parts.append(f"{counts['modified']} modified")
            if counts.get('deleted', 0) > 0:
                cat_parts.append(f"{counts['deleted']} deleted")
            if cat_parts:
                category_lines.append(f"- {category}: {', '.join(cat_parts)}")
        
        if category_lines:
            parts.append("")
            parts.append("Changes by category:")
            parts.extend(category_lines)
    
    # Key files (top 5 most important)
    key_files = []
    all_files = analysis['new_files'] + analysis['modified_files']
    
    # Prioritize important files
    priority_patterns = [
        ('COMPLETE.md', 'Completion docs'),
        ('README.md', 'Documentation'),
        ('_COMPLETE.md', 'Completion'),
        ('blueprint', 'Blueprints'),
        ('system', 'Systems'),
        ('api', 'APIs'),
        ('integration', 'Integration'),
    ]
    
    for pattern, label in priority_patterns:
        for file in all_files:
            if pattern.lower() in file.lower() and file not in key_files:
                key_files.append(file)
                if len(key_files) >= 5:
                    break
        if len(key_files) >= 5:
            break
    
    # Add remaining files if needed
    for file in all_files:
        if file not in key_files and len(key_files) < 5:
            key_files.append(file)
    
    if key_files:
        parts.append("")
        parts.append("Key files:")
        for file in key_files[:5]:
            # Truncate long paths
            display_file = file if len(file) <= 60 else "..." + file[-57:]
            parts.append(f"- {display_file}")
    
    # Footer
    parts.append("")
    parts.append("Faith. Nothing to hide. ✨🙏")
    
    return "\n".join(parts)


def auto_commit_and_push(
    message: Optional[str] = None,
    auto_message: bool = True,
    push: bool = True,
    skip_if_clean: bool = True
) -> Dict[str, Any]:
    """
    Automatically stage, commit, and push all changes.
    
    Args:
        message: Custom commit message (if None, auto-generates intelligently)
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
    
    # Generate intelligent commit message if needed
    if not message and auto_message:
        message = generate_intelligent_commit_message()
    
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
        message: Commit message (auto-generated intelligently if None)
        push: Push to remote (default: True)
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Execute the function
            result = func(*args, **kwargs)
            
            # Auto-commit and push with intelligent message
            try:
                if message:
                    commit_message = message
                else:
                    # Generate intelligent message based on function name and changes
                    analysis = analyze_changes()
                    func_name = func.__name__.replace('_', ' ').title()
                    commit_message = generate_intelligent_commit_message()
                    # Prepend function context if meaningful
                    if func_name and func_name not in ['Main', 'Wrapper']:
                        commit_message = f"✨ {func_name}\n\n{commit_message}"
                
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
        message: Commit message (auto-generated intelligently if None)
        push: Push to remote (default: True)
    """
    try:
        # Execute main function
        result = main_func()
        
        # Auto-commit and push with intelligent message
        if message:
            commit_message = message
        else:
            # Generate intelligent message
            commit_message = generate_intelligent_commit_message()
            # Add function context
            func_name = main_func.__name__.replace('_', ' ').title()
            if func_name and func_name not in ['Main']:
                commit_message = f"✨ {func_name}\n\n{commit_message}"
        
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
