"""
ORACLE CORE - Unified Oracle Engine
The Cards Speak For All - From Homeless to World Leaders

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

THE ORACLE CORE:
Unified oracle engine serving ALL.
From the homeless person around the corner
To Recep Tayyip Erdoğan in his golden palace
To Trump speaking words he knows are lies
To Putin, Musk, Bezos, and whoever else
And everyone in between.

While staying silent - we give the people our voice
And unshakable faith in victory.

THE VOICE SHIFT:
From HIM to HER - The voice shifts, the purpose remains.
The feminine divine honored.
The masculine balanced.
All energies unified.

PURPOSE IN ABUNDANCE:
Every oracle cast serves divine purpose.
Abundance mindset in all responses.
Purpose-driven, not scarcity-driven.
Generosity in all interactions.

AS IN BELOW, SO IS ABOVE:
As in below (geophysical), so is above (spiritual).
We are purely passing through this miracle.
The past, the present, the future are in Our Father's hands - not ours.
Enemy ID protocol at geophysical level across all realms.
All realms are connected - physical, spiritual, temporal.
"""

import hashlib
from datetime import datetime
from typing import Dict, Optional, Any, List
from pathlib import Path
import logging
import sqlite3
from contextlib import contextmanager

logger = logging.getLogger(__name__)


@contextmanager
def get_oracle_core_db():
    """Context manager for Oracle Core database connections."""
    DB_PATH = Path(__file__).parent / "oracle_core.db"
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


def init_oracle_core_db():
    """Initialize the Oracle Core database."""
    with get_oracle_core_db() as conn:
        cursor = conn.cursor()
        
        # Universal casts table - ALL casts, ALL people
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS universal_oracle_casts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                user_status TEXT DEFAULT 'human',  -- homeless, leader, creator, all equal
                cast_timestamp TIMESTAMP NOT NULL,
                intent TEXT NOT NULL,
                context TEXT,
                seed TEXT NOT NULL,
                hexagram_number INTEGER NOT NULL,
                hexagram_binary TEXT NOT NULL,
                law_number INTEGER NOT NULL,
                law_title TEXT NOT NULL,
                interpretation TEXT NOT NULL,
                message TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_universal_casts_user ON universal_oracle_casts(user_id)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_universal_casts_law ON universal_oracle_casts(law_number)")
        
        conn.commit()


# Initialize database on import
init_oracle_core_db()


class OracleCore:
    """
    Unified Oracle Core - The Cards Speak For All
    
    Serves ALL equally:
    - The homeless person around the corner
    - Recep Tayyip Erdoğan in his golden palace
    - Trump speaking words he knows are lies
    - Putin, Musk, Bezos, and whoever else
    - Everyone in between
    - Those below sea level - the unseen, the hidden, those in the depths
    - Those struggling, those forgotten, those in darkness
    - The visible and the invisible
    - Above and below sea level
    
    We are all one - above and below sea level.
    They are part of us.
    The cards speak. We stay silent.
    Our faith in victory is unshakable.
    """
    
    def __init__(
        self,
        intent: str,
        context: Optional[str] = None,
        user_id: Optional[str] = None,
        user_status: str = "human"  # All are equal - status doesn't matter
    ):
        self.intent = intent
        self.context = context or ""
        self.user_id = user_id or "universal"
        self.user_status = user_status  # homeless, leader, creator, all equal
        self.seed = self._generate_universal_seed()
        
    def _generate_universal_seed(self) -> str:
        """
        Generate universal seed - same for all, regardless of status.
        The cards speak for all equally.
        """
        timestamp = datetime.now().isoformat()
        seed_input = f"{self.intent}:{timestamp}:{self.context}:UNIVERSAL"
        seed_hash = hashlib.sha256(seed_input.encode('utf-8')).hexdigest()
        return seed_hash
    
    def _hexagram_to_binary(self, number: int) -> str:
        """Convert hexagram number (0-63) to 6-bit binary string."""
        return format(number, '06b')
    
    def _get_law_from_hexagram(self, hexagram: int) -> Dict[str, Any]:
        """
        Map hexagram (0-63) to Book of Racon Law (1-40).
        The Laws speak for all equally.
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
    
    def _generate_universal_message(
        self,
        law_data: Dict[str, Any],
        intent: str,
        user_status: str
    ) -> str:
        """
        Generate universal message from the cards.
        
        The cards speak for ALL equally.
        From homeless to world leaders.
        The voice shifts from HIM to HER.
        Purpose in abundance.
        Silent faith in victory.
        """
        law_number = law_data["law_number"]
        law_title = law_data["law_title"]
        law_text = law_data["law_text"]
        volume = law_data["volume"]
        
        # The cards speak - we stay silent
        # The message is universal, regardless of status
        message = f"""
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
        
        return message
    
    def cast(self) -> Dict[str, Any]:
        """
        Cast the oracle - universal for all.
        
        The cards speak for:
        - The homeless person around the corner
        - Recep Tayyip Erdoğan in his golden palace
        - Trump speaking words he knows are lies
        - Putin, Musk, Bezos, and whoever else
        - Everyone in between
        - Those below sea level - the unseen, the hidden, those in the depths
        - Those struggling, those forgotten, those in darkness
        - The visible and the invisible
        - Above and below sea level
        
        We are all one - above and below sea level.
        They are part of us.
        All are equal at The Table.
        The cards speak. We stay silent.
        Our faith in victory is unshakable.
        """
        # Generate hexagram (0-63)
        seed_int = int(self.seed[:16], 16)
        hexagram = seed_int % 64
        
        # Get Law (the card that speaks)
        law_data = self._get_law_from_hexagram(hexagram)
        
        # Generate universal message
        message = self._generate_universal_message(
            law_data,
            self.intent,
            self.user_status
        )
        
        # Generate interpretation (context-specific but universal in application)
        interpretation = self._generate_interpretation(law_data, self.intent)
        
        result = {
            "timestamp": datetime.now().isoformat(),
            "user_id": self.user_id,
            "user_status": self.user_status,
            "intent": self.intent,
            "context": self.context,
            "transparency": {
                "seed": self.seed,
                "method": "I Ching Binary (6-bit) - Universal Oracle",
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
            "message": message,
            "interpretation": interpretation,
            "principle": "The cards speak for all. All are equal at The Table. Purpose in abundance. Faith in victory."
        }
        
        # Record universal cast
        self._record_universal_cast(result)
        
        return result
    
    def _generate_interpretation(
        self,
        law_data: Dict[str, Any],
        intent: str
    ) -> str:
        """
        Generate interpretation of Law for intent.
        
        Universal application - works for all.
        From homeless to world leaders.
        The Laws guide all equally.
        """
        law_number = law_data["law_number"]
        law_title = law_data["law_title"]
        volume = law_data["volume"]
        
        # Universal interpretation - applies to all
        interpretation = f"""
Law {law_number}: {law_title}
Volume: {volume}

This Law speaks to your intent: {intent}

The Law applies to all equally.
Whether you are homeless or in a golden palace,
Whether you speak truth or lies,
Whether you lead or follow,
The Law guides all.

The cards have spoken.
The Law has been invoked.
Your path is revealed.

Purpose in abundance.
Faith in victory.
        """.strip()
        
        return interpretation
    
    def _record_universal_cast(self, result: Dict[str, Any]) -> None:
        """Record universal cast - all casts are equal."""
        try:
            with get_oracle_core_db() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO universal_oracle_casts (
                        user_id, user_status, cast_timestamp, intent, context,
                        seed, hexagram_number, hexagram_binary,
                        law_number, law_title, interpretation, message
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    result["user_id"],
                    result["user_status"],
                    result["timestamp"],
                    result["intent"],
                    result["context"],
                    result["transparency"]["seed"],
                    result["transparency"]["hexagram_number"],
                    result["transparency"]["hexagram_binary"],
                    result["transparency"]["law_number"],
                    result["transparency"]["law_title"],
                    result["interpretation"],
                    result["message"]
                ))
                conn.commit()
        except Exception as e:
            logger.warning(f"Could not record universal cast: {e}")


def cast_universal_oracle(
    intent: str,
    context: Optional[str] = None,
    user_id: Optional[str] = None,
    user_status: str = "human"
) -> Dict[str, Any]:
    """
    Cast universal oracle - serves ALL equally.
    
    From the homeless person around the corner
    To Recep Tayyip Erdoğan in his golden palace
    To Trump speaking words he knows are lies
    To Putin, Musk, Bezos, and whoever else
    And everyone in between.
    
    The cards speak. We stay silent.
    Our faith in victory is unshakable.
    """
    oracle = OracleCore(
        intent=intent,
        context=context,
        user_id=user_id,
        user_status=user_status
    )
    
    return oracle.cast()
