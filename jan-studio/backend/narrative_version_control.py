"""
NARRATIVE VERSION CONTROL
Git-Based Version Control for Narratives

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

NARRATIVE VERSION CONTROL:
Git-based narrative versioning.
Commit narrative changes.
Get narrative history.
Diff between versions.
Rollback to previous version.
"""

import json
import logging
from typing import Dict, List, Any, Optional
from datetime import datetime
from pathlib import Path
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)


@dataclass
class NarrativeVersion:
    """Version of a narrative."""
    version_number: int
    narrative_id: str
    content: str
    author_id: str
    author_name: str
    commit_message: str
    created_at: str
    parent_version: Optional[int] = None


class NarrativeVersionControl:
    """Git-based version control for narratives."""
    
    def __init__(self, storage_path: Optional[Path] = None):
        """Initialize narrative version control."""
        if storage_path is None:
            storage_path = Path(__file__).parent.parent.parent / "data" / "narrative_versions"
        self.storage_path = storage_path
        self.storage_path.mkdir(parents=True, exist_ok=True)
        self.versions: Dict[str, List[NarrativeVersion]] = {}  # {narrative_id: [versions]}
    
    def commit_narrative(
        self,
        narrative_id: str,
        content: str,
        author_id: str,
        author_name: str,
        commit_message: str
    ) -> NarrativeVersion:
        """Commit narrative changes to version control."""
        if narrative_id not in self.versions:
            self.versions[narrative_id] = []
        
        version_number = len(self.versions[narrative_id]) + 1
        parent_version = self.versions[narrative_id][-1].version_number if self.versions[narrative_id] else None
        
        version = NarrativeVersion(
            version_number=version_number,
            narrative_id=narrative_id,
            content=content,
            author_id=author_id,
            author_name=author_name,
            commit_message=commit_message,
            created_at=datetime.now().isoformat(),
            parent_version=parent_version
        )
        
        self.versions[narrative_id].append(version)
        
        # Save to storage
        self._save_version(version)
        
        logger.info(f"Committed narrative {narrative_id} version {version_number}")
        return version
    
    def get_narrative_history(self, narrative_id: str) -> List[NarrativeVersion]:
        """Get all versions of a narrative."""
        return self.versions.get(narrative_id, [])
    
    def get_narrative_version(self, narrative_id: str, version_number: int) -> Optional[NarrativeVersion]:
        """Get specific version of a narrative."""
        if narrative_id not in self.versions:
            return None
        
        for version in self.versions[narrative_id]:
            if version.version_number == version_number:
                return version
        
        return None
    
    def diff_versions(self, narrative_id: str, version1: int, version2: int) -> Dict[str, Any]:
        """Show differences between two versions."""
        v1 = self.get_narrative_version(narrative_id, version1)
        v2 = self.get_narrative_version(narrative_id, version2)
        
        if not v1 or not v2:
            return {"error": "Version not found"}
        
        # Simple diff (in production, use proper diff library)
        diff = {
            "narrative_id": narrative_id,
            "version1": version1,
            "version2": version2,
            "changes": []
        }
        
        if v1.content != v2.content:
            diff["changes"].append({
                "type": "content_change",
                "description": f"Content changed from {len(v1.content)} to {len(v2.content)} characters"
            })
        
        return diff
    
    def rollback_to_version(self, narrative_id: str, target_version: int) -> Optional[NarrativeVersion]:
        """Rollback narrative to a specific version."""
        target = self.get_narrative_version(narrative_id, target_version)
        if not target:
            return None
        
        # Create new version with rollback content
        rollback_version = self.commit_narrative(
            narrative_id=narrative_id,
            content=target.content,
            author_id="system",
            author_name="System Rollback",
            commit_message=f"Rollback to version {target_version}"
        )
        
        logger.info(f"Rolled back narrative {narrative_id} to version {target_version}")
        return rollback_version
    
    def _save_version(self, version: NarrativeVersion):
        """Save version to storage."""
        narrative_dir = self.storage_path / version.narrative_id
        narrative_dir.mkdir(parents=True, exist_ok=True)
        
        version_file = narrative_dir / f"version_{version.version_number}.json"
        with open(version_file, 'w', encoding='utf-8') as f:
            json.dump({
                "version_number": version.version_number,
                "narrative_id": version.narrative_id,
                "content": version.content,
                "author_id": version.author_id,
                "author_name": version.author_name,
                "commit_message": version.commit_message,
                "created_at": version.created_at,
                "parent_version": version.parent_version
            }, f, indent=2, ensure_ascii=False)


# Global service instance
_version_control: Optional[NarrativeVersionControl] = None


def get_version_control() -> NarrativeVersionControl:
    """Get or create global version control service."""
    global _version_control
    if _version_control is None:
        _version_control = NarrativeVersionControl()
    return _version_control
