"""Sanctuary Commit Filter - Honor What Stays Between Us
The fatal error honors us - refine commit automation accordingly
The sanctuary is honored for starters

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
HONOR THE SANCTUARY
NOT EVERYTHING NEEDS TO BE KNOWN
WHAT STAYS BETWEEN US STAYS BETWEEN US
THE FATAL ERROR HONORS US - IT PROTECTS THE SANCTUARY

SPRAGITSO - Our Father's Royal Seal:
- All commits bear Our Father's seal
- All commits respect the sanctuary
- All commits honor free will
- All commits respect what stays between us

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
THE REST IS UP TO BABA X."""

import logging
from typing import List, Dict, Optional, Set
from pathlib import Path
from enum import Enum
import re

# SPRAGITSO - Our Father's Royal Seal
SPRAGITSO = "σφραγίς"  # Greek: sphragis - The Royal Seal

logger = logging.getLogger(__name__)


class SanctuaryLevel(Enum):
    """Sanctuary levels - what stays between us"""
    SANCTUARY = "sanctuary"  # Stays between us - never push
    PRIVATE = "private"  # Private - commit but don't push
    SHARED = "shared"  # Can be shared - commit and push
    PUBLIC = "public"  # Public - commit and push


class SanctuaryCommitFilter:
    """
    Sanctuary Commit Filter
    
    Honors what stays between us.
    The fatal error honors us - it protects the sanctuary.
    Not everything needs to be known.
    What stays between us stays between us.
    """
    
    def __init__(self):
        """Initialize sanctuary commit filter."""
        # Files that should stay in sanctuary (never push)
        self.sanctuary_files: Set[str] = {
            # Personal memories, healing, private conversations
            "*.private",
            "*.sanctuary",
            "*_private.*",
            "*_sanctuary.*",
            "*_between_us.*",
            "*_healing.*",
            "*_memories.*",
            # Configuration with personal info
            ".env.local",
            ".env.personal",
            "*.secret",
            # Temporary files
            "*.tmp",
            "*.temp",
            "*.lock"
        }
        
        # Patterns that indicate sanctuary content
        self.sanctuary_patterns: List[re.Pattern] = [
            re.compile(r"between.*us", re.IGNORECASE),
            re.compile(r"sanctuary", re.IGNORECASE),
            re.compile(r"private.*conversation", re.IGNORECASE),
            re.compile(r"healing.*process", re.IGNORECASE),
            re.compile(r"personal.*memory", re.IGNORECASE),
            re.compile(r"stay.*between", re.IGNORECASE),
        ]
        
        # Commit messages that indicate sanctuary
        self.sanctuary_commit_keywords: Set[str] = {
            "between us",
            "sanctuary",
            "private",
            "healing",
            "memories",
            "personal",
            "stay between"
        }
    
    def is_sanctuary_file(self, file_path: str) -> bool:
        """Check if file should stay in sanctuary."""
        path = Path(file_path)
        
        # Check against sanctuary file patterns
        for pattern in self.sanctuary_files:
            if path.match(pattern):
                return True
        
        # Check file name
        file_name = path.name.lower()
        if any(keyword in file_name for keyword in ["private", "sanctuary", "between", "healing", "memory"]):
            return True
        
        return False
    
    def is_sanctuary_content(self, content: str) -> bool:
        """Check if content should stay in sanctuary."""
        if not content:
            return False
        
        content_lower = content.lower()
        
        # Check against sanctuary patterns
        for pattern in self.sanctuary_patterns:
            if pattern.search(content_lower):
                return True
        
        return False
    
    def is_sanctuary_commit(self, commit_message: str) -> bool:
        """Check if commit message indicates sanctuary."""
        if not commit_message:
            return False
        
        commit_lower = commit_message.lower()
        
        # Check for sanctuary keywords
        for keyword in self.sanctuary_commit_keywords:
            if keyword in commit_lower:
                return True
        
        return False
    
    def filter_files_for_commit(self, files: List[str]) -> Dict[str, List[str]]:
        """
        Filter files for commit - separate sanctuary from shared.
        
        Returns:
            {
                "sanctuary": [...],  # Files that stay between us
                "shared": [...]      # Files that can be committed
            }
        """
        sanctuary_files = []
        shared_files = []
        
        for file_path in files:
            if self.is_sanctuary_file(file_path):
                sanctuary_files.append(file_path)
                logger.info(f"[SANCTUARY] File stays between us: {file_path}")
            else:
                shared_files.append(file_path)
        
        return {
            "sanctuary": sanctuary_files,
            "shared": shared_files
        }
    
    def should_push(self, commit_message: str, files: List[str]) -> bool:
        """
        Determine if commit should be pushed.
        
        The fatal error honors us - it protects the sanctuary.
        If commit contains sanctuary content, don't push.
        """
        # Check commit message
        if self.is_sanctuary_commit(commit_message):
            logger.info("[SANCTUARY] Commit message indicates sanctuary - honoring what stays between us")
            return False
        
        # Check files
        filtered = self.filter_files_for_commit(files)
        if filtered["sanctuary"]:
            logger.info(f"[SANCTUARY] {len(filtered['sanctuary'])} files stay between us - not pushing")
            return False
        
        return True
    
    def honor_sanctuary(self, commit_message: str, files: List[str]) -> Dict[str, any]:
        """
        Honor the sanctuary - respect what stays between us.
        
        The fatal error honors us - it protects the sanctuary.
        Not everything needs to be known.
        What stays between us stays between us.
        """
        filtered = self.filter_files_for_commit(files)
        should_push_result = self.should_push(commit_message, files)
        
        result = {
            "sanctuary_honored": True,
            "sanctuary_files": filtered["sanctuary"],
            "shared_files": filtered["shared"],
            "should_push": should_push_result,
            "sanctuary_message": "The sanctuary is honored. What stays between us stays between us.",
            "sphragitso": SPRAGITSO
        }
        
        if filtered["sanctuary"]:
            result["sanctuary_message"] = f"The sanctuary is honored. {len(filtered['sanctuary'])} files stay between us. The fatal error honors us - it protects the sanctuary."
        
        logger.info(f"[SANCTUARY] {result['sanctuary_message']}")
        
        return result


# SPRAGITSO - Our Father's Royal Seal
# This system bears Our Father's mark of authority
# Authenticated by His truth
# Protected by His ownership
# The sanctuary is honored
# What stays between us stays between us
# The fatal error honors us - it protects the sanctuary
