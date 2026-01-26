"""Marketplace Database Schema and Operations

SQLite database for JAN persona marketplace.

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

import sqlite3
import os
from pathlib import Path
from typing import Optional, List, Dict, Any
from datetime import datetime
from contextlib import contextmanager

# Database path
DB_PATH = os.getenv("MARKETPLACE_DB", os.path.join(os.path.dirname(__file__), "marketplace.db"))


@contextmanager
def get_db():
    """Context manager for database connections."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def init_database():
    """Initialize the marketplace database with schema."""
    with get_db() as conn:
        cursor = conn.cursor()
        
        # Users table (with authentication fields)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT,
                is_active BOOLEAN DEFAULT TRUE,
                is_admin BOOLEAN DEFAULT FALSE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Personas table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS personas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                author_id INTEGER NOT NULL,
                description TEXT,
                category TEXT,
                downloads INTEGER DEFAULT 0,
                rating REAL DEFAULT 0.0,
                rating_count INTEGER DEFAULT 0,
                version TEXT DEFAULT '1.0.0',
                status TEXT DEFAULT 'pending',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (author_id) REFERENCES users(id)
            )
        """)
        
        # Persona files table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS persona_files (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                persona_id INTEGER NOT NULL,
                file_path TEXT NOT NULL,
                file_content TEXT NOT NULL,
                version TEXT DEFAULT '1.0.0',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (persona_id) REFERENCES personas(id) ON DELETE CASCADE,
                UNIQUE(persona_id, file_path, version)
            )
        """)
        
        # Downloads table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS downloads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                persona_id INTEGER NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id),
                FOREIGN KEY (persona_id) REFERENCES personas(id) ON DELETE CASCADE
            )
        """)
        
        # Ratings table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ratings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                persona_id INTEGER NOT NULL,
                rating INTEGER NOT NULL CHECK (rating >= 1 AND rating <= 5),
                comment TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id),
                FOREIGN KEY (persona_id) REFERENCES personas(id) ON DELETE CASCADE,
                UNIQUE(user_id, persona_id)
            )
        """)
        
        # Auth tokens table (for refresh tokens)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS auth_tokens (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                refresh_token_hash TEXT NOT NULL,
                expires_at TIMESTAMP NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            )
        """)
        
        # Create indexes
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_personas_author ON personas(author_id)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_personas_category ON personas(category)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_personas_status ON personas(status)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_downloads_persona ON downloads(persona_id)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_ratings_persona ON ratings(persona_id)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_auth_tokens_user ON auth_tokens(user_id)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_auth_tokens_hash ON auth_tokens(refresh_token_hash)")
        
        conn.commit()


def get_user_by_username(username: str) -> Optional[Dict[str, Any]]:
    """Get user by username."""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()
        return dict(row) if row else None


def create_user(username: str, email: str) -> int:
    """Create a new user."""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, email) VALUES (?, ?)",
            (username, email)
        )
        return cursor.lastrowid


def get_persona(persona_id: int) -> Optional[Dict[str, Any]]:
    """Get persona by ID."""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT p.*, u.username as author_name
            FROM personas p
            LEFT JOIN users u ON p.author_id = u.id
            WHERE p.id = ?
        """, (persona_id,))
        row = cursor.fetchone()
        return dict(row) if row else None


def list_personas(
    category: Optional[str] = None,
    status: str = "approved",
    limit: int = 50,
    offset: int = 0,
    sort_by: str = "downloads"
) -> List[Dict[str, Any]]:
    """List personas with filters."""
    with get_db() as conn:
        cursor = conn.cursor()
        
        query = """
            SELECT p.*, u.username as author_name
            FROM personas p
            LEFT JOIN users u ON p.author_id = u.id
            WHERE p.status = ?
        """
        params = [status]
        
        if category:
            query += " AND p.category = ?"
            params.append(category)
        
        # Sorting
        valid_sorts = ["downloads", "rating", "created_at", "updated_at"]
        if sort_by in valid_sorts:
            query += f" ORDER BY p.{sort_by} DESC"
        else:
            query += " ORDER BY p.downloads DESC"
        
        query += " LIMIT ? OFFSET ?"
        params.extend([limit, offset])
        
        cursor.execute(query, params)
        return [dict(row) for row in cursor.fetchall()]


def create_persona(
    name: str,
    author_id: int,
    description: str,
    category: Optional[str] = None,
    files: Optional[List[Dict[str, str]]] = None
) -> int:
    """Create a new persona in marketplace."""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO personas (name, author_id, description, category)
            VALUES (?, ?, ?, ?)
        """, (name, author_id, description, category))
        persona_id = cursor.lastrowid
        
        # Add files
        if files:
            for file_data in files:
                cursor.execute("""
                    INSERT INTO persona_files (persona_id, file_path, file_content, version)
                    VALUES (?, ?, ?, ?)
                """, (persona_id, file_data["path"], file_data["content"], "1.0.0"))
        
        return persona_id


def get_persona_files(persona_id: int, version: Optional[str] = None) -> List[Dict[str, Any]]:
    """Get files for a persona."""
    with get_db() as conn:
        cursor = conn.cursor()
        if version:
            cursor.execute("""
                SELECT * FROM persona_files
                WHERE persona_id = ? AND version = ?
            """, (persona_id, version))
        else:
            cursor.execute("""
                SELECT * FROM persona_files
                WHERE persona_id = ?
                ORDER BY created_at DESC
            """, (persona_id,))
        return [dict(row) for row in cursor.fetchall()]


def record_download(user_id: Optional[int], persona_id: int):
    """Record a download."""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO downloads (user_id, persona_id) VALUES (?, ?)
        """, (user_id, persona_id))
        cursor.execute("""
            UPDATE personas SET downloads = downloads + 1 WHERE id = ?
        """, (persona_id,))


def add_rating(user_id: Optional[int], persona_id: int, rating: int, comment: Optional[str] = None):
    """Add or update a rating."""
    with get_db() as conn:
        cursor = conn.cursor()
        
        # Check if rating exists
        cursor.execute("SELECT * FROM ratings WHERE user_id = ? AND persona_id = ?", (user_id, persona_id))
        existing = cursor.fetchone()
        
        if existing:
            # Update existing rating
            cursor.execute("""
                UPDATE ratings SET rating = ?, comment = ? WHERE user_id = ? AND persona_id = ?
            """, (rating, comment, user_id, persona_id))
        else:
            # Insert new rating
            cursor.execute("""
                INSERT INTO ratings (user_id, persona_id, rating, comment)
                VALUES (?, ?, ?, ?)
            """, (user_id, persona_id, rating, comment))
        
        # Update persona rating
        cursor.execute("""
            SELECT AVG(rating) as avg_rating, COUNT(*) as count
            FROM ratings WHERE persona_id = ?
        """, (persona_id,))
        result = cursor.fetchone()
        
        cursor.execute("""
            UPDATE personas
            SET rating = ?, rating_count = ?
            WHERE id = ?
        """, (result["avg_rating"] or 0.0, result["count"] or 0, persona_id))


def get_ratings(persona_id: int) -> List[Dict[str, Any]]:
    """Get all ratings for a persona."""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT r.*, u.username
            FROM ratings r
            LEFT JOIN users u ON r.user_id = u.id
            WHERE r.persona_id = ?
            ORDER BY r.created_at DESC
        """, (persona_id,))
        return [dict(row) for row in cursor.fetchall()]


# ============================================================================
# Authentication Functions
# ============================================================================

def get_user_by_email(email: str) -> Optional[Dict[str, Any]]:
    """Get user by email."""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        row = cursor.fetchone()
        return dict(row) if row else None


def get_user_by_id(user_id: int) -> Optional[Dict[str, Any]]:
    """Get user by ID."""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        row = cursor.fetchone()
        return dict(row) if row else None


def create_user_with_password(username: str, email: str, password_hash: str) -> int:
    """Create a new user with password hash."""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
            (username, email, password_hash)
        )
        return cursor.lastrowid


def store_refresh_token(user_id: int, refresh_token_hash: str, expires_at: datetime) -> int:
    """Store a refresh token hash."""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO auth_tokens (user_id, refresh_token_hash, expires_at) VALUES (?, ?, ?)",
            (user_id, refresh_token_hash, expires_at)
        )
        return cursor.lastrowid


def get_refresh_token(refresh_token_hash: str) -> Optional[Dict[str, Any]]:
    """Get refresh token by hash."""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM auth_tokens WHERE refresh_token_hash = ? AND expires_at > datetime('now')",
            (refresh_token_hash,)
        )
        row = cursor.fetchone()
        return dict(row) if row else None


def delete_refresh_token(refresh_token_hash: str) -> bool:
    """Delete a refresh token."""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM auth_tokens WHERE refresh_token_hash = ?", (refresh_token_hash,))
        return cursor.rowcount > 0


def delete_user_refresh_tokens(user_id: int) -> int:
    """Delete all refresh tokens for a user."""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM auth_tokens WHERE user_id = ?", (user_id,))
        return cursor.rowcount


def list_all_users(limit: int = 50, offset: int = 0) -> List[Dict[str, Any]]:
    """List all users (admin function)."""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, username, email, is_active, is_admin, created_at, updated_at
            FROM users
            ORDER BY created_at DESC
            LIMIT ? OFFSET ?
        """, (limit, offset))
        return [dict(row) for row in cursor.fetchall()]


def update_user_status(user_id: int, is_active: bool) -> bool:
    """Update user active status."""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE users
            SET is_active = ?, updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
        """, (is_active, user_id))
        return cursor.rowcount > 0


# Initialize database on import
init_database()

