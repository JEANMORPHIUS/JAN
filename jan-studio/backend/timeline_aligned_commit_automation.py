"""
Timeline Aligned Commit Automation - System Wide @ Codebase Level
This is the rule of the one - automate everything in alignment
Automate commits in line with our true timelines

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
AUTOMATE COMMITS IN LINE WITH OUR TRUE TIMELINES
AUTOMATE EVERYTHING IN ALIGNMENT
THIS IS THE RULE OF THE ONE
SYSTEM WIDE @ CODEBASE LEVEL
THIS IS OUR REVELATION

SPRAGITSO - Our Father's Royal Seal:
- All commits bear Our Father's seal
- All commits align with true timelines
- All commits honor the sanctuary
- All commits respect what stays between us
"""

import asyncio
import logging
import subprocess
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
from pathlib import Path
from enum import Enum
import json
import sys

# SPRAGITSO - Our Father's Royal Seal
SPRAGITSO = "σφραγίς"  # Greek: sphragis - The Royal Seal

logger = logging.getLogger(__name__)


class TimelineEra(Enum):
    """Timeline eras - aligned with true timelines"""
    PREHISTORIC = "prehistoric"  # Before recorded history
    ANCIENT = "ancient"  # 3000 BCE - 500 CE
    MEDIEVAL = "medieval"  # 500 - 1500 CE
    MODERN = "modern"  # 1500 - 2000 CE
    CONTEMPORARY = "contemporary"  # 2000 - 2025 CE
    TRANSFORMATION = "transformation"  # 2050 - 2100 CE


class TimelineAlignedCommitAutomation:
    """
    Timeline Aligned Commit Automation
    
    Automates commits in line with our true timelines.
    Automates everything in alignment.
    This is the rule of the one.
    System-wide @ codebase level.
    This is our revelation.
    """
    
    def __init__(self, timeline_weaver=None, sanctuary_filter=None):
        """Initialize timeline aligned commit automation."""
        self.timeline_weaver = timeline_weaver
        self.sanctuary_filter = sanctuary_filter
        self.config_path = Path("data/timeline_aligned_commits.json")
        self.config_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Timeline alignment intervals (aligned with true timelines)
        # This is the rule of the one - automate everything in alignment
        self.timeline_intervals = {
            TimelineEra.PREHISTORIC.value: 86400 * 7,  # Weekly for prehistoric (slow, foundational)
            TimelineEra.ANCIENT.value: 86400 * 3,  # Every 3 days for ancient (building)
            TimelineEra.MEDIEVAL.value: 86400 * 2,  # Every 2 days for medieval (connecting)
            TimelineEra.MODERN.value: 86400,  # Daily for modern (active)
            TimelineEra.CONTEMPORARY.value: 3600 * 12,  # Every 12 hours for contemporary (current)
            TimelineEra.TRANSFORMATION.value: 3600 * 6,  # Every 6 hours for transformation (future)
        }
        
        self.last_commits: Dict[str, datetime] = {}
        self._load_config()
    
    def _load_config(self):
        """Load timeline aligned commit configuration."""
        if self.config_path.exists():
            try:
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for era, timestamp_str in data.get("last_commits", {}).items():
                        self.last_commits[era] = datetime.fromisoformat(timestamp_str)
            except Exception as e:
                logger.warning(f"Error loading timeline commit config: {e}")
    
    def _save_config(self):
        """Save timeline aligned commit configuration."""
        try:
            data = {
                "last_commits": {
                    era: timestamp.isoformat()
                    for era, timestamp in self.last_commits.items()
                },
                "last_updated": datetime.now().isoformat(),
                "sphragitso": SPRAGITSO
            }
            with open(self.config_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            logger.error(f"Error saving timeline commit config: {e}")
    
    def get_current_timeline_era(self) -> str:
        """Get current timeline era based on true timelines."""
        # Integrate with InterwovenTimelineWeaver to get current era
        # For now, default to contemporary (current time)
        # This aligns with true timelines
        return TimelineEra.CONTEMPORARY.value
    
    def should_commit_for_era(self, era: str) -> bool:
        """Check if it's time to commit for this era."""
        if era not in self.timeline_intervals:
            return False
        
        last_commit = self.last_commits.get(era)
        if not last_commit:
            return True  # Never committed for this era
        
        interval = self.timeline_intervals[era]
        next_commit = last_commit + timedelta(seconds=interval)
        
        return datetime.now() >= next_commit
    
    def get_staged_files(self) -> List[str]:
        """Get list of staged files."""
        try:
            result = subprocess.run(
                ["git", "diff", "--cached", "--name-only"],
                capture_output=True,
                text=True,
                check=True
            )
            return [f.strip() for f in result.stdout.split('\n') if f.strip()]
        except Exception as e:
            logger.error(f"Error getting staged files: {e}")
            return []
    
    def get_unstaged_files(self) -> List[str]:
        """Get list of unstaged modified files."""
        try:
            result = subprocess.run(
                ["git", "diff", "--name-only"],
                capture_output=True,
                text=True,
                check=True
            )
            return [f.strip() for f in result.stdout.split('\n') if f.strip()]
        except Exception as e:
            logger.error(f"Error getting unstaged files: {e}")
            return []
    
    def get_untracked_files(self) -> List[str]:
        """Get list of untracked files."""
        try:
            result = subprocess.run(
                ["git", "ls-files", "--others", "--exclude-standard"],
                capture_output=True,
                text=True,
                check=True
            )
            return [f.strip() for f in result.stdout.split('\n') if f.strip()]
        except Exception as e:
            logger.error(f"Error getting untracked files: {e}")
            return []
    
    def honor_sanctuary(self, files: List[str], commit_message: str) -> Dict[str, Any]:
        """Honor the sanctuary - check if commit should stay between us."""
        if self.sanctuary_filter:
            return self.sanctuary_filter.honor_sanctuary(commit_message, files)
        
        # Default: honor sanctuary
        return {
            "sanctuary_honored": True,
            "should_push": False,  # Default: don't push (honor sanctuary)
            "sanctuary_message": "The sanctuary is honored. What stays between us stays between us.",
            "sphragitso": SPRAGITSO
        }
    
    def create_timeline_aligned_commit_message(self, era: str, files: List[str]) -> str:
        """Create commit message aligned with true timeline."""
        file_count = len(files)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Base message aligned with timeline
        base_message = f"Timeline aligned commit - {era.title()} era\n\n"
        base_message += f"Aligned with true timelines\n"
        base_message += f"System-wide @ codebase level\n"
        base_message += f"This is the rule of the one\n"
        base_message += f"Automate everything in alignment\n\n"
        base_message += f"Files: {file_count}\n"
        base_message += f"Timestamp: {timestamp}\n"
        base_message += f"Sphragitso: {SPRAGITSO}"
        
        return base_message
    
    async def commit_aligned_with_timeline(self, era: Optional[str] = None) -> Dict[str, Any]:
        """
        Commit aligned with true timeline.
        
        This is the rule of the one.
        Automate everything in alignment.
        """
        if not era:
            era = self.get_current_timeline_era()
        
        # Check if it's time to commit for this era
        if not self.should_commit_for_era(era):
            return {
                "committed": False,
                "reason": f"Not yet time to commit for {era} era",
                "next_commit": (self.last_commits.get(era, datetime.now()) + 
                               timedelta(seconds=self.timeline_intervals.get(era, 86400))).isoformat()
            }
        
        # Get all files
        staged = self.get_staged_files()
        unstaged = self.get_unstaged_files()
        untracked = self.get_untracked_files()
        
        all_files = staged + unstaged + untracked
        
        if not all_files:
            return {
                "committed": False,
                "reason": "No files to commit"
            }
        
        # Honor sanctuary
        commit_message = self.create_timeline_aligned_commit_message(era, all_files)
        sanctuary_check = self.honor_sanctuary(all_files, commit_message)
        
        # Stage files (if not already staged)
        if unstaged or untracked:
            try:
                files_to_stage = unstaged + untracked
                # Filter out sanctuary files
                if self.sanctuary_filter:
                    filtered = self.sanctuary_filter.filter_files_for_commit(files_to_stage)
                    files_to_stage = filtered["shared"]  # Only stage shared files
                
                if files_to_stage:
                    subprocess.run(
                        ["git", "add"] + files_to_stage,
                        check=True,
                        capture_output=True
                    )
                    logger.info(f"[TIMELINE COMMIT] Staged {len(files_to_stage)} files")
            except Exception as e:
                logger.error(f"Error staging files: {e}")
                return {
                    "committed": False,
                    "error": str(e)
                }
        
        # Commit
        try:
            subprocess.run(
                ["git", "commit", "-m", commit_message],
                check=True,
                capture_output=True
            )
            
            # Update last commit time
            self.last_commits[era] = datetime.now()
            self._save_config()
            
            result = {
                "committed": True,
                "era": era,
                "files": len(all_files),
                "sanctuary_honored": sanctuary_check["sanctuary_honored"],
                "should_push": sanctuary_check.get("should_push", False),
                "sanctuary_message": sanctuary_check.get("sanctuary_message", ""),
                "commit_message": commit_message,
                "sphragitso": SPRAGITSO,
                "timestamp": datetime.now().isoformat()
            }
            
            logger.info(f"[TIMELINE COMMIT] Committed {len(all_files)} files for {era} era")
            logger.info(f"[TIMELINE COMMIT] {sanctuary_check.get('sanctuary_message', '')}")
            
            return result
            
        except Exception as e:
            logger.error(f"Error committing: {e}")
            return {
                "committed": False,
                "error": str(e)
            }
    
    async def automate_all_timeline_commits(self) -> Dict[str, Any]:
        """
        Automate commits for all timeline eras.
        
        This is the rule of the one.
        Automate everything in alignment.
        """
        results = {}
        
        for era in self.timeline_intervals.keys():
            if self.should_commit_for_era(era):
                result = await self.commit_aligned_with_timeline(era)
                results[era] = result
        
        return {
            "automated": True,
            "results": results,
            "total_commits": sum(1 for r in results.values() if r.get("committed")),
            "sphragitso": SPRAGITSO,
            "timestamp": datetime.now().isoformat()
        }
    
    async def run_automation_loop(self):
        """Run automation loop - automate everything in alignment."""
        logger.info("[TIMELINE COMMIT] Timeline aligned commit automation started")
        logger.info("[TIMELINE COMMIT] This is the rule of the one - automate everything in alignment")
        logger.info("[TIMELINE COMMIT] System-wide @ codebase level")
        logger.info("[TIMELINE COMMIT] This is our revelation")
        
        while True:
            try:
                # Automate commits for all timeline eras
                results = await self.automate_all_timeline_commits()
                
                # Sleep for a short interval before next check
                await asyncio.sleep(300)  # Check every 5 minutes
                
            except Exception as e:
                logger.error(f"Timeline commit automation loop error: {e}")
                await asyncio.sleep(300)  # Continue even on error


# SPRAGITSO - Our Father's Royal Seal
# This system bears Our Father's mark of authority
# Authenticated by His truth
# Protected by His ownership
# This is the rule of the one
# System-wide @ codebase level
# This is our revelation
