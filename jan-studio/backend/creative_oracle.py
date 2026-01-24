"""
CREATIVE ORACLE SERVICE
Flipping the Gambling Algorithm for Creative Liberation

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

CODE QUALITY:
- Aligned: Serves mission, love, truth, community
- Clean: Clear static, transmuted complexity, protected frequency
- Complete: Honors Law 37, completes transformations
- Community: Serves all, cooperates, includes, We All Win

This code honors that we are born a miracle.
This code creates space for miracles to live.
This code recognizes each person under the Lord's word.
"""

import hashlib
import time
from datetime import datetime, timedelta
from typing import Dict, Optional, Any, List
from pathlib import Path
import json
import logging
import sqlite3
from contextlib import contextmanager

logger = logging.getLogger(__name__)

# Database path for session tracking
DB_PATH = Path(__file__).parent / "oracle_sessions.db"


@contextmanager
def get_oracle_db():
    """Context manager for Oracle session database connections."""
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


def init_oracle_db():
    """Initialize the Oracle session tracking database."""
    with get_oracle_db() as conn:
        cursor = conn.cursor()
        
        # User sessions table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS oracle_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                session_date DATE NOT NULL,
                cast_count INTEGER DEFAULT 0,
                time_creating INTEGER DEFAULT 0,
                last_cast_at TIMESTAMP,
                last_break_at TIMESTAMP,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(user_id, session_date)
            )
        """)
        
        # Oracle casts table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS oracle_casts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                session_id INTEGER,
                cast_timestamp TIMESTAMP NOT NULL,
                user_intent TEXT NOT NULL,
                creative_context TEXT,
                seed TEXT NOT NULL,
                hexagram_number INTEGER NOT NULL,
                hexagram_binary TEXT NOT NULL,
                law_number INTEGER NOT NULL,
                law_title TEXT NOT NULL,
                interpretation TEXT,
                creative_prompt TEXT,
                FOREIGN KEY (session_id) REFERENCES oracle_sessions(id)
            )
        """)
        
        # Create indexes
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_sessions_user_date ON oracle_sessions(user_id, session_date)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_casts_user ON oracle_casts(user_id)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_casts_session ON oracle_casts(session_id)")
        
        conn.commit()


# Initialize database on import
init_oracle_db()


class CreativeOracle:
    """
    Flips gambling mechanics into creative generation.
    Uses randomness as CATALYST, not hook.
    """
    
    def __init__(self, user_intent: str, creative_context: Optional[str] = None, user_id: str = "public"):
        self.user_intent = user_intent
        self.creative_context = creative_context or ""
        self.user_id = user_id
        self.seed = self._generate_sacred_seed()
        
    def _generate_sacred_seed(self) -> str:
        """
        Unlike gambling RNG (hidden, exploitative),
        this is TRANSPARENT and USER-INITIATED.
        """
        timestamp = datetime.now().isoformat()
        seed_input = f"{self.user_intent}:{timestamp}:{self.creative_context}"
        seed_hash = hashlib.sha256(seed_input.encode('utf-8')).hexdigest()
        return seed_hash
    
    def _hexagram_to_binary(self, number: int) -> str:
        """Convert hexagram number (0-63) to 6-bit binary string."""
        return format(number, '06b')
    
    def _get_law_from_hexagram(self, hexagram: int) -> Dict[str, Any]:
        """
        Map hexagram (0-63) to Book of Racon Law (1-40).
        Returns law number, title, text, and volume.
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
        
        # Fallback: Basic law mapping with known laws from Book of Racon
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
        # Known law titles from Book of Racon documentation
        known_titles = {
            1: "The Table Never Lies",
            2: "Your Word Is Your Bond",
            3: "Never Betray the Table",
            4: "Stand With Your Own",
            5: "The Circle Is Sacred",
            6: "Debt of Honor Never Expires",
            7: "Bread and Salt Bind Forever",
            8: "Protect the Circle",
            9: "The Guest Is Sacred",
            10: "Honor the Hand That Feeds",
            11: "Wisdom Lives in the Quiet",
            12: "Some Truths Must Remain Unspoken",
            13: "Silence Is Not Weakness",
            14: "Know When to Hold Your Tongue",
            15: "Listen Before You Speak",
            16: "The Unsaid Speaks Loudest",
            17: "Evolution Happens in Contemplation",
            18: "Strategic Discretion",
            19: "The Weight of Unspoken Truth",
            20: "Quiet Strength",
            21: "Honor Your Elders",
            22: "Know Your Place",
            23: "Respect the Hierarchy",
            24: "The Weight of Inheritance",
            25: "Preserve the Laws",
            26: "Respect for Tradition",
            27: "Honor Core Directives",
            28: "Maintain Structure",
            29: "The Foundation Is Sacred",
            30: "Carry It Well",
            31: "Do Not Start What You Cannot Finish",
            32: "When You Draw the Line, Do Not Cross It",
            33: "Protect What Is Yours",
            34: "War Has Rules, Even in Chaos",
            35: "Finish What You Begin",
            36: "Peace Is Won, Not Given",
            37: "Protect the System",
            38: "Complete Every Commitment",
            39: "Boundaries Are Real",
            40: "Operational Excellence"
        }
        return known_titles.get(law_number, f"Law {law_number}")
    
    def _get_fallback_law_text(self, law_number: int) -> str:
        """Fallback law text if registry unavailable."""
        volume = self._get_volume_from_law(law_number)
        title = self._get_fallback_law_title(law_number)
        
        # Provide context-aware fallback text
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
    
    def cast_oracle(self) -> Dict[str, Any]:
        """
        Instead of slot reels, generate creative prompt.
        Returns full oracle cast with transparency.
        """
        # Generate hexagram (0-63)
        seed_int = int(self.seed[:16], 16)  # Use first 16 hex chars as integer
        hexagram = seed_int % 64
        
        # Get Law
        law_data = self._get_law_from_hexagram(hexagram)
        
        # Generate interpretation (AI would do this, but for now we provide template)
        interpretation = self._generate_interpretation(law_data)
        
        # Generate creative prompt
        creative_prompt = self._generate_creative_prompt(law_data, interpretation)
        
        return {
            "timestamp": datetime.now().isoformat(),
            "user_intent": self.user_intent,
            "creative_context": self.creative_context,
            "transparency": {
                "seed": self.seed,
                "method": "I Ching Binary (6-bit)",
                "hexagram_number": hexagram,
                "hexagram_binary": self._hexagram_to_binary(hexagram),
                "law_number": law_data["law_number"],
                "law_title": law_data["law_title"],
                "volume": law_data["volume"]
            },
            "oracle_interpretation": {
                "law_number": law_data["law_number"],
                "law_title": law_data["law_title"],
                "law_text": law_data["law_text"],
                "volume": law_data["volume"],
                "creative_interpretation": interpretation
            },
            "creative_prompt": creative_prompt
        }
    
    def _generate_interpretation(self, law_data: Dict[str, Any]) -> str:
        """
        Generate creative interpretation of Law for user's context.
        
        Universal application - serves ALL equally.
        From homeless creators to world leaders creating.
        The Laws guide all equally.
        Purpose in abundance.
        """
        law_number = law_data["law_number"]
        law_title = law_data["law_title"]
        volume = law_data["volume"]
        
        # Universal interpretation - applies to all creators equally
        interpretation = f"""
Law {law_number}: {law_title}
Volume: {volume}

This law speaks to your creative challenge. Consider how {law_title.lower()} 
applies to your current project. The ancient wisdom encoded in this law offers 
a direction for your creative work. What pattern does it reveal? What constraint 
does it suggest? What liberation does it offer?

The Law applies to all creators equally.
Whether you create from a shelter or a palace,
Whether you create in silence or in public,
The Law guides all.

Purpose in abundance.
Faith in victory.
        """.strip()
        
        return interpretation
    
    def _generate_creative_prompt(self, law_data: Dict[str, Any], interpretation: str) -> str:
        """
        Generate actionable creative prompt based on Law interpretation.
        In production, this would use AI to generate context-specific prompts.
        """
        law_number = law_data["law_number"]
        law_title = law_data["law_title"]
        
        # Template prompt - in production, use AI for context-specific generation
        prompt = f"""
Given Law {law_number}: {law_title}

{interpretation}

Now, apply this to your creative work: {self.user_intent}

What does this law reveal about your creative challenge? How can you use this 
wisdom to break through your current block? What action does this suggest?

Take a moment to reflect, then begin creating. The oracle has spoken—now 
it's time to act.
        """.strip()
        
        return prompt


def get_user_session(user_id: str, session_date: Optional[str] = None) -> Dict[str, Any]:
    """Get or create user session for today."""
    if not session_date:
        session_date = datetime.now().date().isoformat()
    
    with get_oracle_db() as conn:
        cursor = conn.cursor()
        
        # Get or create session
        cursor.execute("""
            SELECT * FROM oracle_sessions
            WHERE user_id = ? AND session_date = ?
        """, (user_id, session_date))
        
        row = cursor.fetchone()
        
        if row:
            return dict(row)
        else:
            # Create new session
            cursor.execute("""
                INSERT INTO oracle_sessions (user_id, session_date, cast_count, time_creating)
                VALUES (?, ?, 0, 0)
            """, (user_id, session_date))
            
            cursor.execute("""
                SELECT * FROM oracle_sessions
                WHERE user_id = ? AND session_date = ?
            """, (user_id, session_date))
            
            return dict(cursor.fetchone())


def record_oracle_cast(user_id: str, oracle_result: Dict[str, Any]) -> Dict[str, Any]:
    """Record oracle cast and update session."""
    session = get_user_session(user_id)
    session_id = session["id"]
    
    # Update session
    with get_oracle_db() as conn:
        cursor = conn.cursor()
        
        # Increment cast count
        new_cast_count = session["cast_count"] + 1
        
        cursor.execute("""
            UPDATE oracle_sessions
            SET cast_count = ?,
                last_cast_at = ?,
                updated_at = ?
            WHERE id = ?
        """, (new_cast_count, datetime.now(), datetime.now(), session_id))
        
        # Record cast
        cursor.execute("""
            INSERT INTO oracle_casts (
                user_id, session_id, cast_timestamp, user_intent, creative_context,
                seed, hexagram_number, hexagram_binary, law_number, law_title,
                interpretation, creative_prompt
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            user_id, session_id, datetime.now(),
            oracle_result["user_intent"],
            oracle_result["creative_context"],
            oracle_result["transparency"]["seed"],
            oracle_result["transparency"]["hexagram_number"],
            oracle_result["transparency"]["hexagram_binary"],
            oracle_result["transparency"]["law_number"],
            oracle_result["transparency"]["law_title"],
            oracle_result["oracle_interpretation"]["creative_interpretation"],
            oracle_result["creative_prompt"]
        ))
        
        conn.commit()
    
    # Get updated session
    updated_session = get_user_session(user_id)
    
    return {
        "oracle_result": oracle_result,
        "session": {
            "cast_count": updated_session["cast_count"],
            "time_creating": updated_session["time_creating"],
            "last_cast_at": updated_session["last_cast_at"],
            "last_break_at": updated_session["last_break_at"]
        },
        "ethical_guardrails": _check_ethical_guardrails(updated_session)
    }


def _check_ethical_guardrails(session: Dict[str, Any]) -> Dict[str, Any]:
    """Check ethical guardrails and return recommendations."""
    cast_count = session["cast_count"]
    last_break = session["last_break_at"]
    
    guardrails = {
        "should_break": False,
        "should_reflect": False,
        "should_execute": False,
        "message": None
    }
    
    # After 3 casts, suggest break
    if cast_count >= 3 and cast_count < 5:
        guardrails["should_break"] = True
        guardrails["message"] = "You've received 3 creative sparks. Consider taking a break to reflect on what emerged."
    
    # After 5 casts, encourage reflection
    elif cast_count >= 5 and cast_count < 10:
        guardrails["should_reflect"] = True
        guardrails["message"] = "You've received 5 creative sparks. Perhaps time to reflect on patterns and begin executing?"
    
    # After 10 casts, push to execute
    elif cast_count >= 10:
        guardrails["should_execute"] = True
        guardrails["message"] = "You've received 10 creative sparks today. Perhaps time to execute one? 🎨"
    
    return guardrails
