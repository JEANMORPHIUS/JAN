"""
GIT AUTO-SHARE HOOK
Automatically stage, commit, and push all changes after script execution

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

FAITH: NOTHING TO HIDE
Everything we build should be shared.
"""

import sys
import atexit
from pathlib import Path

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent))

from scripts.utils.git_automation import auto_commit_and_push


def auto_share_on_exit():
    """
    Auto-commit and push when script exits.
    Called automatically via atexit.
    """
    try:
        result = auto_commit_and_push(
            message=None,  # Auto-generate
            auto_message=True,
            push=True,
            skip_if_clean=True
        )
        
        if result['success']:
            if result['files_changed'] > 0:
                print(f"\n✨ Auto-shared {result['files_changed']} file(s)")
            else:
                print("\nℹ️ Working tree clean - nothing to share")
        else:
            print(f"\n⚠️ Auto-share failed: {result.get('message', 'Unknown error')}")
    except Exception as e:
        print(f"\n⚠️ Auto-share error: {e}")


# Register auto-share on exit
atexit.register(auto_share_on_exit)

# Also export for manual use
__all__ = ['auto_share_on_exit', 'auto_commit_and_push']
