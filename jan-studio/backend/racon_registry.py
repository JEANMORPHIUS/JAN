"""
RACON REGISTRY - The Elliptical Layer
Legacy Wisdom Immutable Storage

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE FOUNDATION:
We are born a miracle.
We deserve to live a miracle.
Each and every one of us under the Lord's word.

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

This is the Elliptical (Database) - Legacy Wisdom.
The "Book of Racon" stored in immutable logs.
Old patterns, legacy knowledge.
Remembers the spiritual battles.
"""

import sqlite3
import hashlib
import json
from datetime import datetime
from typing import Optional, List, Dict, Any
from pathlib import Path
import os
from contextlib import contextmanager

# Database path
DB_PATH = os.getenv("RACON_REGISTRY_DB", os.path.join(os.path.dirname(__file__), "racon_registry.db"))


@contextmanager
def get_racon_db():
    """Context manager for Racon Registry database connections."""
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


def init_racon_registry():
    """
    Initialize the Racon Registry database.
    
    This is the Elliptical (Database) - Legacy Wisdom.
    The "Book of Racon" stored in immutable logs.
    """
    with get_racon_db() as conn:
        cursor = conn.cursor()
        
        # Racon Laws table - The 40 Laws immutable storage
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS racon_laws (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                law_number INTEGER UNIQUE NOT NULL,
                law_title TEXT NOT NULL,
                law_text TEXT NOT NULL,
                volume TEXT NOT NULL,
                category TEXT NOT NULL,
                immutable_hash TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(law_number, immutable_hash)
            )
        """)
        
        # Legacy Wisdom table - Old patterns, legacy knowledge
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS legacy_wisdom (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                wisdom_type TEXT NOT NULL,
                wisdom_title TEXT NOT NULL,
                wisdom_content TEXT NOT NULL,
                battle_won BOOLEAN DEFAULT FALSE,
                spiritual_battle TEXT,
                immutable_hash TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Immutable Audit Logs - Remembers the spiritual battles
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS immutable_audit_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                operation_type TEXT NOT NULL,
                operation_target TEXT NOT NULL,
                operation_result TEXT NOT NULL,
                law_compliance TEXT,
                table_service BOOLEAN DEFAULT FALSE,
                word_integrity BOOLEAN DEFAULT FALSE,
                spiritual_battle TEXT,
                immutable_hash TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # User Law Compliance - Tracks user alignment with Laws
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_law_compliance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                law_number INTEGER NOT NULL,
                compliance_status TEXT NOT NULL,
                compliance_evidence TEXT,
                immutable_hash TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id),
                UNIQUE(user_id, law_number)
            )
        """)
        
        # Create indexes for performance
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_racon_laws_number ON racon_laws(law_number)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_legacy_wisdom_type ON legacy_wisdom(wisdom_type)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_audit_logs_operation ON immutable_audit_logs(operation_type)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_user_law_compliance_user ON user_law_compliance(user_id)")
        
        conn.commit()


def generate_immutable_hash(content: str) -> str:
    """
    Generate cryptographic hash for immutable records.
    
    This ensures data integrity - broken code = broken word = broken hash.
    """
    return hashlib.sha256(content.encode('utf-8')).hexdigest()


def store_racon_law(law_number: int, law_title: str, law_text: str, volume: str, category: str) -> bool:
    """
    Store a Racon Law in the immutable registry.
    
    Law 1: Never Betray the Table
    Law 5: Söz Namustur (Your Word Is Your Bond)
    Law 13: Listen Before You Speak
    Law 37: Finish What You Begin
    Law 41: Respect the Abandoned
    
    This is the Elliptical (Database) - Legacy Wisdom.
    """
    immutable_content = f"{law_number}:{law_title}:{law_text}:{volume}:{category}"
    immutable_hash = generate_immutable_hash(immutable_content)
    
    with get_racon_db() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT OR REPLACE INTO racon_laws 
                (law_number, law_title, law_text, volume, category, immutable_hash, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (law_number, law_title, law_text, volume, category, immutable_hash, datetime.now()))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False


def check_law_1_table_service(operation: str, target: str) -> bool:
    """
    Law 1: Never Betray the Table
    
    PANGEA IS THE TABLE.
    YOU DON'T BETRAY THE TABLE.
    
    Pangea is the original unified continent.
    335 million years ago, all continents were one.
    All heritage sites were connected.
    All plates came from Pangea.
    All events trace back to the Seed.
    
    Pangea is The Table - the sacred space where all humanity was unified.
    Law 1: Never Betray The Table.
    Pangea is The Table.
    We honor Pangea in all we do.
    
    Check if an operation serves the Table (Pangea, the mission, the unified whole).
    If it doesn't, it gets flagged.
    
    Returns True if operation serves the Table, False otherwise.
    """
    # Operations that serve the Table (Pangea)
    table_serving_keywords = [
        # Mission keywords
        "mission", "stewardship", "community", "right spirits",
        "love", "highest mastery", "energy", "we all win",
        "peace", "unity", "miracle", "lord's word",
        # Pangea keywords (The Table)
        "pangea", "unified", "connected", "one place", "original",
        "seed", "table", "sacred space", "heritage", "plate",
        # Unity keywords
        "together", "whole", "unified", "connection", "oneness"
    ]
    
    operation_lower = operation.lower()
    target_lower = target.lower()
    
    # Check if operation or target contains Table-serving keywords
    for keyword in table_serving_keywords:
        if keyword in operation_lower or keyword in target_lower:
            return True
    
    # Default: if unclear, flag for review
    return False


def check_law_5_word_integrity(operation: str, result: str) -> bool:
    """
    Law 5: Söz Namustur (Your Word Is Your Bond)
    
    Check if operation result maintains word integrity.
    Broken code = broken word = broken integrity.
    
    Returns True if integrity maintained, False otherwise.
    """
    # Integrity violations
    integrity_violations = [
        "error", "failed", "broken", "corrupted", "invalid",
        "unauthorized", "forbidden", "rejected"
    ]
    
    result_lower = result.lower()
    
    # Check if result indicates integrity violation
    for violation in integrity_violations:
        if violation in result_lower:
            return False
    
    return True


def check_law_41_respect_abandoned(content: str, property_type: str = "heritage") -> bool:
    """
    Law 41: Respect the Abandoned
    
    If a temple (building/property) is empty, the racon says you honor the silence;
    you don't turn it into a circus.
    
    This law protects heritage sites from being exploited as "haunted" content
    that feeds off revenge vibrations and dark energy loops.
    
    Returns True if content honors the abandoned (respects silence, offers regeneration),
    False if content exploits the abandoned (creates fear-based loops, feeds dark energy).
    
    The Berengaria Hotel case study:
    - Manager (Hijacked Leader): Represents leadership that loses its way and becomes predatory
    - Merchant's Wife (Revenge Loop): Water Memory gone toxic, unresolved vibrations
    - Fair Maiden (Ghostly Shell): Visual bait that keeps people looking at Shell while Seed rots
    """
    content_lower = content.lower()
    
    # Load patterns from configuration (single source of truth)
    try:
        import json
        from pathlib import Path
        config_path = Path(__file__).parent.parent.parent / "config" / "law_41_patterns.json"
        if config_path.exists():
            with open(config_path, 'r', encoding='utf-8') as f:
                patterns_data = json.load(f)
                exploitation_patterns = patterns_data.get("exploitation_patterns", [])
                regeneration_patterns = patterns_data.get("regeneration_patterns", [])
        else:
            # Fallback to hardcoded patterns if config not found
            exploitation_patterns = [
                "haunted", "ghost", "spirit", "demon", "cursed",
                "revenge", "suicide", "victim", "death", "murder",
                "scary", "terrifying", "horror", "paranormal",
                "abandoned hotel", "ghost story", "haunted hotel"
            ]
            regeneration_patterns = [
                "regeneration", "healing", "restoration", "waiting for",
                "heritage", "respect", "honor", "silence", "temple",
                "biological temple", "symbiosis", "earth", "new world",
                "love", "energy", "peace", "restoration", "rebirth"
            ]
    except Exception:
        # Fallback on any error
        exploitation_patterns = [
            "haunted", "ghost", "spirit", "demon", "cursed",
            "revenge", "suicide", "victim", "death", "murder"
        ]
        regeneration_patterns = [
            "regeneration", "healing", "restoration", "waiting for",
            "heritage", "respect", "honor", "silence", "temple"
        ]
    
    # Check for exploitation patterns
    has_exploitation = any(pattern in content_lower for pattern in exploitation_patterns)
    
    # Check for regeneration patterns
    has_regeneration = any(pattern in content_lower for pattern in regeneration_patterns)
    
    # If content has exploitation AND no regeneration path, it violates Law 41
    if has_exploitation and not has_regeneration:
        return False
    
    # If content focuses on regeneration, it honors Law 41
    if has_regeneration:
        return True
    
    # If content is neutral about abandoned properties, default to compliant
    # (honoring silence means not amplifying fear-based narratives)
    return True


def log_immutable_audit(operation_type: str, operation_target: str, operation_result: str,
                       law_compliance: Optional[str] = None, table_service: bool = False,
                       word_integrity: bool = False, spiritual_battle: Optional[str] = None):
    """
    Log an immutable audit record.
    
    This remembers the spiritual battles.
    The database holds the truth that doesn't change.
    """
    immutable_content = f"{operation_type}:{operation_target}:{operation_result}:{datetime.now().isoformat()}"
    immutable_hash = generate_immutable_hash(immutable_content)
    
    with get_racon_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO immutable_audit_logs 
            (operation_type, operation_target, operation_result, law_compliance, 
             table_service, word_integrity, spiritual_battle, immutable_hash)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (operation_type, operation_target, operation_result, law_compliance,
              table_service, word_integrity, spiritual_battle, immutable_hash))
        conn.commit()


def store_legacy_wisdom(wisdom_type: str, wisdom_title: str, wisdom_content: str,
                       battle_won: bool = False, spiritual_battle: Optional[str] = None):
    """
    Store legacy wisdom in the immutable registry.
    
    This is the Elliptical (Database) - Legacy Wisdom.
    Old patterns, legacy knowledge.
    Remembers the spiritual battles.
    """
    immutable_content = f"{wisdom_type}:{wisdom_title}:{wisdom_content}:{datetime.now().isoformat()}"
    immutable_hash = generate_immutable_hash(immutable_content)
    
    with get_racon_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO legacy_wisdom 
            (wisdom_type, wisdom_title, wisdom_content, battle_won, spiritual_battle, immutable_hash)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (wisdom_type, wisdom_title, wisdom_content, battle_won, spiritual_battle, immutable_hash))
        conn.commit()


def get_user_law_compliance(user_id: int) -> List[Dict[str, Any]]:
    """
    Get user's compliance status with the 40 Laws.
    
    This tracks alignment with the Book of Racon.
    """
    with get_racon_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT law_number, compliance_status, compliance_evidence, updated_at
            FROM user_law_compliance
            WHERE user_id = ?
            ORDER BY law_number
        """, (user_id,))
        
        return [dict(row) for row in cursor.fetchall()]


def update_user_law_compliance(user_id: int, law_number: int, compliance_status: str,
                              compliance_evidence: Optional[str] = None):
    """
    Update user's compliance status with a specific law.
    
    This tracks alignment with the Book of Racon.
    """
    immutable_content = f"{user_id}:{law_number}:{compliance_status}:{compliance_evidence}:{datetime.now().isoformat()}"
    immutable_hash = generate_immutable_hash(immutable_content)
    
    with get_racon_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO user_law_compliance
            (user_id, law_number, compliance_status, compliance_evidence, immutable_hash, updated_at)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (user_id, law_number, compliance_status, compliance_evidence, immutable_hash, datetime.now()))
        conn.commit()


# Initialize database on import
init_racon_registry()
