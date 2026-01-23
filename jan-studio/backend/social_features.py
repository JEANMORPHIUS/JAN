"""
SOCIAL FEATURES
Comments, Bookmarks, Sharing for Narratives

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

SOCIAL FEATURES:
Comments on narratives.
Bookmarks for users.
Sharing capabilities.
Reactions (likes, shares).
Related content suggestions.
"""

import json
import logging
from typing import Dict, List, Any, Optional
from datetime import datetime
from dataclasses import dataclass, field
from pathlib import Path

logger = logging.getLogger(__name__)


@dataclass
class Comment:
    """Comment on a narrative."""
    comment_id: str
    narrative_id: str
    user_id: str
    user_name: str
    content: str
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    likes: int = 0
    shares: int = 0
    parent_comment_id: Optional[str] = None  # For threaded comments


@dataclass
class Bookmark:
    """User bookmark."""
    bookmark_id: str
    user_id: str
    item_type: str  # 'narrative', 'site', 'event'
    item_id: str
    item_title: str
    notes: Optional[str] = None
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())


@dataclass
class Reaction:
    """Reaction to content."""
    reaction_id: str
    user_id: str
    item_type: str
    item_id: str
    reaction_type: str  # 'like', 'share', 'bookmark'
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())


class SocialFeaturesService:
    """Service for social features."""
    
    def __init__(self, storage_path: Optional[Path] = None):
        """Initialize social features service."""
        if storage_path is None:
            storage_path = Path(__file__).parent.parent.parent / "data" / "social_features"
        self.storage_path = storage_path
        self.storage_path.mkdir(parents=True, exist_ok=True)
        
        self.comments: Dict[str, List[Comment]] = {}  # {narrative_id: [comments]}
        self.bookmarks: Dict[str, List[Bookmark]] = {}  # {user_id: [bookmarks]}
        self.reactions: Dict[str, List[Reaction]] = {}  # {item_id: [reactions]}
    
    def add_comment(
        self,
        narrative_id: str,
        user_id: str,
        user_name: str,
        content: str,
        parent_comment_id: Optional[str] = None
    ) -> Comment:
        """Add a comment to a narrative."""
        import hashlib
        comment_id = f"comment_{hashlib.sha256(f'{narrative_id}_{user_id}_{datetime.now().isoformat()}'.encode()).hexdigest()[:8]}"
        
        comment = Comment(
            comment_id=comment_id,
            narrative_id=narrative_id,
            user_id=user_id,
            user_name=user_name,
            content=content,
            parent_comment_id=parent_comment_id
        )
        
        if narrative_id not in self.comments:
            self.comments[narrative_id] = []
        self.comments[narrative_id].append(comment)
        
        self._save_comment(comment)
        logger.info(f"Added comment {comment_id} to narrative {narrative_id}")
        return comment
    
    def get_comments(self, narrative_id: str) -> List[Comment]:
        """Get all comments for a narrative."""
        return self.comments.get(narrative_id, [])
    
    def add_bookmark(
        self,
        user_id: str,
        item_type: str,
        item_id: str,
        item_title: str,
        notes: Optional[str] = None
    ) -> Bookmark:
        """Add a bookmark."""
        import hashlib
        bookmark_id = f"bookmark_{hashlib.sha256(f'{user_id}_{item_type}_{item_id}'.encode()).hexdigest()[:8]}"
        
        bookmark = Bookmark(
            bookmark_id=bookmark_id,
            user_id=user_id,
            item_type=item_type,
            item_id=item_id,
            item_title=item_title,
            notes=notes
        )
        
        if user_id not in self.bookmarks:
            self.bookmarks[user_id] = []
        self.bookmarks[user_id].append(bookmark)
        
        self._save_bookmark(bookmark)
        logger.info(f"Added bookmark {bookmark_id} for user {user_id}")
        return bookmark
    
    def get_user_bookmarks(self, user_id: str) -> List[Bookmark]:
        """Get all bookmarks for a user."""
        return self.bookmarks.get(user_id, [])
    
    def add_reaction(
        self,
        user_id: str,
        item_type: str,
        item_id: str,
        reaction_type: str
    ) -> Reaction:
        """Add a reaction."""
        import hashlib
        reaction_id = f"reaction_{hashlib.sha256(f'{user_id}_{item_type}_{item_id}_{reaction_type}'.encode()).hexdigest()[:8]}"
        
        reaction = Reaction(
            reaction_id=reaction_id,
            user_id=user_id,
            item_type=item_type,
            item_id=item_id,
            reaction_type=reaction_type
        )
        
        if item_id not in self.reactions:
            self.reactions[item_id] = []
        self.reactions[item_id].append(reaction)
        
        self._save_reaction(reaction)
        logger.info(f"Added reaction {reaction_id}")
        return reaction
    
    def get_reactions(self, item_id: str) -> Dict[str, int]:
        """Get reaction counts for an item."""
        reactions = self.reactions.get(item_id, [])
        counts = {}
        for reaction in reactions:
            counts[reaction.reaction_type] = counts.get(reaction.reaction_type, 0) + 1
        return counts
    
    def _save_comment(self, comment: Comment):
        """Save comment to storage."""
        comments_file = self.storage_path / f"comments_{comment.narrative_id}.json"
        comments = self.get_comments(comment.narrative_id)
        with open(comments_file, 'w', encoding='utf-8') as f:
            json.dump([{
                "comment_id": c.comment_id,
                "narrative_id": c.narrative_id,
                "user_id": c.user_id,
                "user_name": c.user_name,
                "content": c.content,
                "created_at": c.created_at,
                "likes": c.likes,
                "shares": c.shares,
                "parent_comment_id": c.parent_comment_id
            } for c in comments], f, indent=2, ensure_ascii=False)
    
    def _save_bookmark(self, bookmark: Bookmark):
        """Save bookmark to storage."""
        bookmarks_file = self.storage_path / f"bookmarks_{bookmark.user_id}.json"
        bookmarks = self.get_user_bookmarks(bookmark.user_id)
        with open(bookmarks_file, 'w', encoding='utf-8') as f:
            json.dump([{
                "bookmark_id": b.bookmark_id,
                "user_id": b.user_id,
                "item_type": b.item_type,
                "item_id": b.item_id,
                "item_title": b.item_title,
                "notes": b.notes,
                "created_at": b.created_at
            } for b in bookmarks], f, indent=2, ensure_ascii=False)
    
    def _save_reaction(self, reaction: Reaction):
        """Save reaction to storage."""
        reactions_file = self.storage_path / f"reactions_{reaction.item_id}.json"
        reactions = self.get_reactions(reaction.item_id)
        with open(reactions_file, 'w', encoding='utf-8') as f:
            json.dump(reactions, f, indent=2, ensure_ascii=False)


# Global service instance
_social_service: Optional[SocialFeaturesService] = None


def get_social_service() -> SocialFeaturesService:
    """Get or create global social features service."""
    global _social_service
    if _social_service is None:
        _social_service = SocialFeaturesService()
    return _social_service
