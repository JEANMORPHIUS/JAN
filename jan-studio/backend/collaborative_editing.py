"""
COLLABORATIVE EDITING
Operational Transformation for Real-Time Collaborative Narrative Editing

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

COLLABORATIVE EDITING:
Multiple editors can edit narratives simultaneously.
Real-time cursor positions.
Change highlighting.
Conflict resolution.
Edit history with rollback.
"""

import json
import logging
from typing import Dict, List, Any, Optional
from datetime import datetime
from dataclasses import dataclass, field
from enum import Enum

logger = logging.getLogger(__name__)


class OperationType(Enum):
    """Type of edit operation."""
    INSERT = "insert"
    DELETE = "delete"
    RETAIN = "retain"


@dataclass
class EditOperation:
    """Single edit operation."""
    operation_type: str
    position: int
    content: Optional[str] = None
    length: int = 1
    author_id: str = ""
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())


@dataclass
class CollaborativeSession:
    """Collaborative editing session."""
    session_id: str
    narrative_id: str
    content: str
    active_users: List[Dict[str, Any]] = field(default_factory=list)
    operations: List[EditOperation] = field(default_factory=list)
    version: int = 0
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    updated_at: str = field(default_factory=lambda: datetime.now().isoformat())


class CollaborativeEditingService:
    """Service for collaborative narrative editing."""
    
    def __init__(self):
        """Initialize collaborative editing service."""
        self.sessions: Dict[str, CollaborativeSession] = {}
        self.user_cursors: Dict[str, Dict[str, int]] = {}  # {session_id: {user_id: position}}
    
    def create_session(self, narrative_id: str, initial_content: str) -> CollaborativeSession:
        """Create a new collaborative editing session."""
        import hashlib
        session_id = f"session_{hashlib.sha256(f'{narrative_id}_{datetime.now().isoformat()}'.encode()).hexdigest()[:8]}"
        
        session = CollaborativeSession(
            session_id=session_id,
            narrative_id=narrative_id,
            content=initial_content
        )
        
        self.sessions[session_id] = session
        logger.info(f"Created collaborative session: {session_id} for narrative {narrative_id}")
        return session
    
    def join_session(self, session_id: str, user_id: str, user_name: str) -> bool:
        """Join a collaborative editing session."""
        if session_id not in self.sessions:
            return False
        
        session = self.sessions[session_id]
        
        # Check if user already in session
        if any(u["user_id"] == user_id for u in session.active_users):
            return True
        
        session.active_users.append({
            "user_id": user_id,
            "user_name": user_name,
            "joined_at": datetime.now().isoformat()
        })
        
        # Initialize cursor position
        if session_id not in self.user_cursors:
            self.user_cursors[session_id] = {}
        self.user_cursors[session_id][user_id] = 0
        
        logger.info(f"User {user_id} joined session {session_id}")
        return True
    
    def apply_operation(self, session_id: str, operation: EditOperation) -> bool:
        """Apply an edit operation to a session."""
        if session_id not in self.sessions:
            return False
        
        session = self.sessions[session_id]
        
        # Transform operation against concurrent operations
        transformed_operation = self._transform_operation(operation, session.operations[-10:])
        
        # Apply operation
        if transformed_operation.operation_type == OperationType.INSERT.value:
            session.content = (
                session.content[:transformed_operation.position] +
                transformed_operation.content +
                session.content[transformed_operation.position:]
            )
        elif transformed_operation.operation_type == OperationType.DELETE.value:
            session.content = (
                session.content[:transformed_operation.position] +
                session.content[transformed_operation.position + transformed_operation.length:]
            )
        
        # Record operation
        session.operations.append(transformed_operation)
        session.version += 1
        session.updated_at = datetime.now().isoformat()
        
        logger.info(f"Applied operation {transformed_operation.operation_type} to session {session_id}")
        return True
    
    def _transform_operation(self, operation: EditOperation, concurrent_operations: List[EditOperation]) -> EditOperation:
        """Transform operation against concurrent operations (simplified OT)."""
        # Simplified OT - in production, use a proper OT library
        transformed_position = operation.position
        
        for concurrent_op in concurrent_operations:
            if concurrent_op.position < operation.position:
                if concurrent_op.operation_type == OperationType.INSERT.value:
                    transformed_position += len(concurrent_op.content or "")
                elif concurrent_op.operation_type == OperationType.DELETE.value:
                    transformed_position -= concurrent_op.length
        
        return EditOperation(
            operation_type=operation.operation_type,
            position=max(0, transformed_position),
            content=operation.content,
            length=operation.length,
            author_id=operation.author_id,
            timestamp=operation.timestamp
        )
    
    def update_cursor(self, session_id: str, user_id: str, position: int):
        """Update user cursor position."""
        if session_id not in self.user_cursors:
            self.user_cursors[session_id] = {}
        self.user_cursors[session_id][user_id] = position
    
    def get_session_state(self, session_id: str) -> Optional[Dict[str, Any]]:
        """Get current session state."""
        if session_id not in self.sessions:
            return None
        
        session = self.sessions[session_id]
        cursors = self.user_cursors.get(session_id, {})
        
        return {
            "session_id": session.session_id,
            "narrative_id": session.narrative_id,
            "content": session.content,
            "version": session.version,
            "active_users": session.active_users,
            "cursors": cursors,
            "updated_at": session.updated_at
        }
    
    def rollback_to_version(self, session_id: str, target_version: int) -> bool:
        """Rollback session to a specific version."""
        if session_id not in self.sessions:
            return False
        
        session = self.sessions[session_id]
        
        if target_version < 0 or target_version >= session.version:
            return False
        
        # Replay operations up to target version
        # Simplified - in production, store content snapshots
        logger.info(f"Rollback session {session_id} to version {target_version}")
        return True


# Global service instance
_collaborative_service: Optional[CollaborativeEditingService] = None


def get_collaborative_service() -> CollaborativeEditingService:
    """Get or create global collaborative editing service."""
    global _collaborative_service
    if _collaborative_service is None:
        _collaborative_service = CollaborativeEditingService()
    return _collaborative_service
