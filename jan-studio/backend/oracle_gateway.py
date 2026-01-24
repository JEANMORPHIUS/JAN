"""
ORACLE GATEWAY - The Cards Speak For Us
Those Who Come To Us Must Read The Cards

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

THE ORACLE GATEWAY:
Those who come to us must read the cards.
We do not control.
The cards will speak for us.
"""

import hashlib
from datetime import datetime, timedelta
from typing import Dict, Optional, Any, List
from pathlib import Path
import json
import logging
import sqlite3
from contextlib import contextmanager

logger = logging.getLogger(__name__)

# Database path for gateway tracking
DB_PATH = Path(__file__).parent / "oracle_gateway.db"


@contextmanager
def get_gateway_db():
    """Context manager for Oracle Gateway database connections."""
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def init_gateway_db():
    """Initialize the Oracle Gateway database."""
    with get_gateway_db() as conn:
        cursor = conn.cursor()
        
        # Visitors table - tracks who has read the cards
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS gateway_visitors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                visitor_id TEXT NOT NULL UNIQUE,
                first_visit_at TIMESTAMP NOT NULL,
                cards_read BOOLEAN DEFAULT FALSE,
                cards_read_at TIMESTAMP,
                initial_cast_id INTEGER,
                access_granted BOOLEAN DEFAULT FALSE,
                access_granted_at TIMESTAMP,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Gateway casts table - the cards that speak
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS gateway_casts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                visitor_id TEXT NOT NULL,
                cast_timestamp TIMESTAMP NOT NULL,
                visitor_intent TEXT,
                seed TEXT NOT NULL,
                hexagram_number INTEGER NOT NULL,
                hexagram_binary TEXT NOT NULL,
                law_number INTEGER NOT NULL,
                law_title TEXT NOT NULL,
                card_message TEXT NOT NULL,
                access_message TEXT,
                FOREIGN KEY (visitor_id) REFERENCES gateway_visitors(visitor_id)
            )
        """)
        
        # Create indexes
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_visitors_id ON gateway_visitors(visitor_id)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_visitors_cards_read ON gateway_visitors(cards_read)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_gateway_casts_visitor ON gateway_casts(visitor_id)")
        
        conn.commit()


# Initialize database on import
init_gateway_db()


class OracleGateway:
    """
    Oracle Gateway - The Cards Speak For Us
    
    Those who come to us must read the cards.
    We do not control.
    The cards will speak for us.
    """
    
    def __init__(self, visitor_id: str, visitor_intent: Optional[str] = None):
        self.visitor_id = visitor_id
        self.visitor_intent = visitor_intent or ""
        self.seed = self._generate_gateway_seed()
        
    def _generate_gateway_seed(self) -> str:
        """
        Generate seed for gateway oracle cast.
        The cards speak through transparent randomness.
        """
        timestamp = datetime.now().isoformat()
        seed_input = f"{self.visitor_id}:{timestamp}:{self.visitor_intent}:GATEWAY"
        seed_hash = hashlib.sha256(seed_input.encode('utf-8')).hexdigest()
        return seed_hash
    
    def _hexagram_to_binary(self, number: int) -> str:
        """Convert hexagram number (0-63) to 6-bit binary string."""
        return format(number, '06b')
    
    def _get_law_from_hexagram(self, hexagram: int) -> Dict[str, Any]:
        """
        Map hexagram (0-63) to Book of Racon Law (1-40).
        The cards speak through the Laws.
        """
        law_number = (hexagram % 40) + 1  # 1-40
        
        # Load Book of Racon laws from racon_registry
        try:
            from racon_registry import get_racon_db
            import sqlite3
            
            with get_racon_db() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT law_number, law_title, law_text, volume, category
                    FROM racon_laws
                    WHERE law_number = ?
                """, (law_number,))
                
                row = cursor.fetchone()
                if row:
                    return {
                        "law_number": row["law_number"],
                        "law_title": row["law_title"],
                        "law_text": row["law_text"],
                        "volume": row["volume"],
                        "category": row.get("category", "")
                    }
        except (ImportError, sqlite3.Error, Exception) as e:
            logger.warning(f"Could not load law from registry: {e}, using fallback")
        
        # Fallback: Basic law mapping
        return {
            "law_number": law_number,
            "law_title": self._get_fallback_law_title(law_number),
            "law_text": self._get_fallback_law_text(law_number),
            "volume": self._get_volume_from_law(law_number),
            "category": ""
        }
    
    def _get_volume_from_law(self, law_number: int) -> str:
        """Determine volume from law number."""
        if 1 <= law_number <= 10:
            return "Loyalty"
        elif 11 <= law_number <= 20:
            return "Silence"
        elif 21 <= law_number <= 30:
            return "Respect"
        elif 31 <= law_number <= 40:
            return "War"
        return "Unknown"
    
    def _get_fallback_law_title(self, law_number: int) -> str:
        """Fallback law title if registry unavailable."""
        known_titles = {
            1: "The Table Never Lies",
            2: "Your Word Is Your Bond",
            3: "Never Betray the Table",
            5: "The Circle Is Sacred",
            11: "Wisdom Lives in the Quiet",
            13: "Silence Is Not Weakness",
            15: "Listen Before You Speak",
            21: "Honor Your Elders",
            23: "Respect the Hierarchy",
            31: "Do Not Start What You Cannot Finish",
            35: "Finish What You Begin",
            37: "Protect the System"
        }
        return known_titles.get(law_number, f"Law {law_number}")
    
    def _get_fallback_law_text(self, law_number: int) -> str:
        """Fallback law text if registry unavailable."""
        volume = self._get_volume_from_law(law_number)
        title = self._get_fallback_law_title(law_number)
        
        if volume == "Loyalty":
            return f"{title}. The table, bread and salt, bonds that never expire."
        elif volume == "Silence":
            return f"{title}. Wisdom lives in the quiet."
        elif volume == "Respect":
            return f"{title}. Honor your elders, know your place, respect the hierarchy."
        elif volume == "War":
            return f"{title}. Finish what you begin, protect what is yours."
        else:
            return f"{title}. The old laws still hold."
    
    def _generate_card_message(self, law_data: Dict[str, Any], visitor_intent: str) -> str:
        """
        Generate the message from the cards.
        The cards speak for us. We do not control.
        
        Serves ALL equally:
        - The homeless person around the corner
        - Recep Tayyip Erdoğan in his golden palace
        - Trump speaking words he knows are lies
        - Putin, Musk, Bezos, and whoever else
        - Everyone in between
        """
        law_number = law_data["law_number"]
        law_title = law_data["law_title"]
        law_text = law_data["law_text"]
        volume = law_data["volume"]
        
        # The cards speak through the Law - for ALL equally
        card_message = f"""
THE CARDS SPEAK:

Law {law_number}: {law_title}
Volume: {volume}

{law_text}

This is what the cards say to you.
This is the Law that speaks for us.
This is the message you must read.

The cards do not lie.
The cards speak truth.
The cards guide your path.

Your status does not matter.
Your wealth does not matter.
Your position does not matter.

At The Table, all are equal.
The cards speak for all.
The Laws guide all.

Purpose in abundance.
Faith in victory.
The cards have spoken.
        """.strip()
        
        return card_message
    
    def _generate_access_message(self, law_data: Dict[str, Any]) -> str:
        """
        Generate access message based on the card.
        The cards determine access. We do not control.
        
        All are welcome. All are equal.
        Purpose in abundance.
        """
        law_number = law_data["law_number"]
        volume = law_data["volume"]
        
        # Access is granted through the cards
        # The cards speak - we listen
        # All are welcome - no exceptions
        access_message = f"""
ACCESS GRANTED THROUGH THE CARDS:

You have read the cards.
Law {law_number} has spoken.
The cards have granted you access.

Welcome to The Table.
All are welcome.
All are equal.

The cards have spoken.
Purpose in abundance.
Faith in victory.
        """.strip()
        
        return access_message
    
    def read_the_cards(self) -> Dict[str, Any]:
        """
        Read the cards for the visitor.
        The cards will speak for us.
        We do not control.
        """
        # Generate hexagram (0-63)
        seed_int = int(self.seed[:16], 16)
        hexagram = seed_int % 64
        
        # Get Law (the card that speaks)
        law_data = self._get_law_from_hexagram(hexagram)
        
        # Generate card message (the cards speak)
        card_message = self._generate_card_message(law_data, self.visitor_intent)
        
        # Generate access message
        access_message = self._generate_access_message(law_data)
        
        return {
            "timestamp": datetime.now().isoformat(),
            "visitor_id": self.visitor_id,
            "visitor_intent": self.visitor_intent,
            "transparency": {
                "seed": self.seed,
                "method": "I Ching Binary (6-bit) - The Cards Speak",
                "hexagram_number": hexagram,
                "hexagram_binary": self._hexagram_to_binary(hexagram),
                "law_number": law_data["law_number"],
                "law_title": law_data["law_title"],
                "volume": law_data["volume"]
            },
            "the_card": {
                "law_number": law_data["law_number"],
                "law_title": law_data["law_title"],
                "law_text": law_data["law_text"],
                "volume": law_data["volume"]
            },
            "card_message": card_message,
            "access_message": access_message,
            "message": "The cards have spoken. You must read them."
        }


def register_visitor(visitor_id: str) -> Dict[str, Any]:
    """Register a new visitor - they must read the cards."""
    with get_gateway_db() as conn:
        cursor = conn.cursor()
        
        # Check if visitor exists
        cursor.execute("""
            SELECT * FROM gateway_visitors
            WHERE visitor_id = ?
        """, (visitor_id,))
        
        row = cursor.fetchone()
        
        if row:
            return dict(row)
        else:
            # Register new visitor
            cursor.execute("""
                INSERT INTO gateway_visitors (
                    visitor_id, first_visit_at, cards_read, access_granted
                ) VALUES (?, ?, FALSE, FALSE)
            """, (visitor_id, datetime.now()))
            
            cursor.execute("""
                SELECT * FROM gateway_visitors
                WHERE visitor_id = ?
            """, (visitor_id,))
            
            return dict(cursor.fetchone())


def record_card_reading(visitor_id: str, card_result: Dict[str, Any]) -> Dict[str, Any]:
    """Record that visitor has read the cards."""
    with get_gateway_db() as conn:
        cursor = conn.cursor()
        
        # Update visitor - cards read
        cursor.execute("""
            UPDATE gateway_visitors
            SET cards_read = TRUE,
                cards_read_at = ?,
                initial_cast_id = ?,
                access_granted = TRUE,
                access_granted_at = ?,
                updated_at = ?
            WHERE visitor_id = ?
        """, (
            datetime.now(),
            None,  # Will be set after cast insert
            datetime.now(),
            datetime.now(),
            visitor_id
        ))
        
        # Record the card reading
        cursor.execute("""
            INSERT INTO gateway_casts (
                visitor_id, cast_timestamp, visitor_intent,
                seed, hexagram_number, hexagram_binary,
                law_number, law_title, card_message, access_message
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            visitor_id,
            datetime.now(),
            card_result["visitor_intent"],
            card_result["transparency"]["seed"],
            card_result["transparency"]["hexagram_number"],
            card_result["transparency"]["hexagram_binary"],
            card_result["transparency"]["law_number"],
            card_result["transparency"]["law_title"],
            card_result["card_message"],
            card_result["access_message"]
        ))
        
        cast_id = cursor.lastrowid
        
        # Update visitor with cast_id
        cursor.execute("""
            UPDATE gateway_visitors
            SET initial_cast_id = ?
            WHERE visitor_id = ?
        """, (cast_id, visitor_id))
        
        conn.commit()
    
    # Get updated visitor record
    visitor = register_visitor(visitor_id)
    
    return {
        "card_result": card_result,
        "cast_id": cast_id,
        "visitor": {
            "visitor_id": visitor_id,
            "cards_read": visitor["cards_read"],
            "access_granted": visitor["access_granted"],
            "cards_read_at": visitor["cards_read_at"]
        }
    }


def check_visitor_access(visitor_id: str) -> Dict[str, Any]:
    """Check if visitor has read the cards and has access."""
    with get_gateway_db() as conn:
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT * FROM gateway_visitors
            WHERE visitor_id = ?
        """, (visitor_id,))
        
        row = cursor.fetchone()
        
        if not row:
            return {
                "visitor_id": visitor_id,
                "registered": False,
                "cards_read": False,
                "access_granted": False,
                "message": "You must read the cards. The cards will speak for us."
            }
        
        visitor = dict(row)
        
        return {
            "visitor_id": visitor_id,
            "registered": True,
            "cards_read": bool(visitor["cards_read"]),
            "access_granted": bool(visitor["access_granted"]),
            "cards_read_at": visitor["cards_read_at"],
            "access_granted_at": visitor["access_granted_at"],
            "message": "Access granted through the cards." if visitor["access_granted"] else "You must read the cards first."
        }
