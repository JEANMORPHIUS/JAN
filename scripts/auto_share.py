"""
AUTO-SHARE - Python Script
Automatically stage, commit, and push all changes

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
import argparse
from pathlib import Path

# Add repo root to path
repo_root = Path(__file__).parent.parent
sys.path.insert(0, str(repo_root))

from scripts.utils.git_automation import auto_commit_and_push


def main():
    """Main function for auto-share script."""
    parser = argparse.ArgumentParser(description='Auto-share: Stage, commit, and push all changes')
    parser.add_argument(
        '-m', '--message',
        type=str,
        default=None,
        help='Custom commit message (auto-generated if not provided)'
    )
    parser.add_argument(
        '--no-push',
        action='store_true',
        help='Commit but do not push'
    )
    
    args = parser.parse_args()
    
    result = auto_commit_and_push(
        message=args.message,
        auto_message=True,
        push=not args.no_push,
        skip_if_clean=True
    )
    
    if result['success']:
        if result['files_changed'] > 0:
            print(f"\n[SUCCESS] Auto-shared {result['files_changed']} file(s)")
        else:
            print("\n[INFO] Working tree clean - nothing to share")
        sys.exit(0)
    else:
        error_msg = result.get('message', 'Unknown error')
        print(f"\n[WARNING] Auto-share failed: {error_msg}")
        sys.exit(1)


if __name__ == "__main__":
    main()
