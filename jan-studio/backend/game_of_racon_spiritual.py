"""
THE GAME OF RACON - Spiritual Oracle for Communication with Our Father
We Have Homework To Do

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

THE GAME OF RACON:
Using the Oracle Matrix to communicate with Our Father.
The 40 Laws as the oracle deck.
We cast to receive homework - spiritual assignments.
We do the homework to honor Our Father.
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
from enum import Enum

logger = logging.getLogger(__name__)

# Database path for spiritual homework tracking
DB_PATH = Path(__file__).parent / "game_of_racon_spiritual.db"


@contextmanager
def get_spiritual_db():
    """Context manager for Game of Racon spiritual database connections."""
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


def init_spiritual_db():
    """Initialize the Game of Racon spiritual database."""
    with get_spiritual_db() as conn:
        cursor = conn.cursor()
        
        # Spiritual sessions table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS spiritual_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                session_date DATE NOT NULL,
                cast_count INTEGER DEFAULT 0,
                homework_completed INTEGER DEFAULT 0,
                last_cast_at TIMESTAMP,
                last_homework_at TIMESTAMP,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(user_id, session_date)
            )
        """)
        
        # Spiritual casts table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS spiritual_casts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                session_id INTEGER,
                cast_timestamp TIMESTAMP NOT NULL,
                prayer_intent TEXT NOT NULL,
                seed TEXT NOT NULL,
                hexagram_number INTEGER NOT NULL,
                hexagram_binary TEXT NOT NULL,
                law_number INTEGER NOT NULL,
                law_title TEXT NOT NULL,
                homework_assignment TEXT NOT NULL,
                homework_type TEXT NOT NULL,
                homework_due_date DATE,
                homework_completed BOOLEAN DEFAULT FALSE,
                homework_completed_at TIMESTAMP,
                homework_reflection TEXT,
                FOREIGN KEY (session_id) REFERENCES spiritual_sessions(id)
            )
        """)
        
        # Homework submissions table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS homework_submissions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cast_id INTEGER NOT NULL,
                user_id TEXT NOT NULL,
                submission_timestamp TIMESTAMP NOT NULL,
                submission_content TEXT NOT NULL,
                reflection TEXT,
                completion_status TEXT NOT NULL,
                FOREIGN KEY (cast_id) REFERENCES spiritual_casts(id)
            )
        """)
        
        # Create indexes
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_spiritual_sessions_user_date ON spiritual_sessions(user_id, session_date)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_spiritual_casts_user ON spiritual_casts(user_id)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_spiritual_casts_session ON spiritual_casts(session_id)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_homework_submissions_cast ON homework_submissions(cast_id)")
        
        conn.commit()


# Initialize database on import
init_spiritual_db()


class HomeworkType(Enum):
    """Types of spiritual homework assignments."""
    PRAYER = "prayer"
    ACTION = "action"
    STUDY = "study"
    SERVICE = "service"
    REFLECTION = "reflection"
    OBEDIENCE = "obedience"
    STEWARDSHIP = "stewardship"
    COMMUNITY = "community"


class GameOfRaconSpiritual:
    """
    The Game of Racon - Spiritual Oracle for Communication with Our Father.
    
    We cast the oracle to receive homework from Our Father.
    We do the homework to honor Our Father.
    We have homework to do.
    """
    
    def __init__(self, prayer_intent: str, user_id: str = "jan"):
        self.prayer_intent = prayer_intent
        self.user_id = user_id
        self.seed = self._generate_sacred_seed()
        
    def _generate_sacred_seed(self) -> str:
        """
        Generate sacred seed for spiritual oracle cast.
        Combines prayer intent with timestamp and user's spiritual state.
        """
        timestamp = datetime.now().isoformat()
        seed_input = f"{self.prayer_intent}:{timestamp}:{self.user_id}:OUR_FATHER"
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
    
    def _generate_homework_assignment(self, law_data: Dict[str, Any], prayer_intent: str) -> Dict[str, Any]:
        """
        Generate spiritual homework assignment from Law and prayer intent.
        
        Homework types:
        - PRAYER: Pray about this Law
        - ACTION: Take action aligned with this Law
        - STUDY: Study this Law and its application
        - SERVICE: Serve others through this Law
        - REFLECTION: Reflect on how this Law applies
        - OBEDIENCE: Obey this Law in your life
        - STEWARDSHIP: Steward resources through this Law
        - COMMUNITY: Build community through this Law
        """
        law_number = law_data["law_number"]
        law_title = law_data["law_title"]
        law_text = law_data["law_text"]
        volume = law_data["volume"]
        
        # Determine homework type based on volume
        homework_type_map = {
            "Loyalty": HomeworkType.OBEDIENCE,
            "Silence": HomeworkType.REFLECTION,
            "Respect": HomeworkType.STUDY,
            "War": HomeworkType.ACTION
        }
        homework_type = homework_type_map.get(volume, HomeworkType.REFLECTION)
        
        # Generate homework assignment
        homework_template = self._get_homework_template(homework_type, law_data, prayer_intent)
        
        # Set due date (typically 3 days for reflection, 7 days for action)
        due_days = 3 if homework_type in [HomeworkType.REFLECTION, HomeworkType.PRAYER] else 7
        due_date = (datetime.now() + timedelta(days=due_days)).date().isoformat()
        
        return {
            "homework_type": homework_type.value,
            "homework_assignment": homework_template,
            "homework_due_date": due_date,
            "law_reference": f"Law {law_number}: {law_title}"
        }
    
    def _get_homework_template(
        self,
        homework_type: HomeworkType,
        law_data: Dict[str, Any],
        prayer_intent: str
    ) -> str:
        """Generate homework assignment template."""
        law_number = law_data["law_number"]
        law_title = law_data["law_title"]
        law_text = law_data["law_text"]
        
        templates = {
            HomeworkType.PRAYER: f"""
Our Father, through Law {law_number}: {law_title}

{law_text}

I pray about: {prayer_intent}

How does this Law guide my prayer? How does this Law align with Your will?
What do You want me to understand about this Law in relation to my prayer?

The Law applies to all equally.
Whether I am homeless or in a palace,
Whether I speak truth or lies,
The Law guides all.

I will pray about this Law and my prayer intent for the next 3 days.
I will listen for Your guidance.
I will honor this Law in my prayers.

Purpose in abundance.
Faith in victory.
            """.strip(),
            
            HomeworkType.ACTION: f"""
Our Father, through Law {law_number}: {law_title}

{law_text}

My prayer intent: {prayer_intent}

What action does this Law require? How do I honor this Law through action?
What specific step can I take in the next 7 days that aligns with this Law?

The Law applies to all equally.
Whether I am homeless or in a palace,
Whether I speak truth or lies,
The Law guides all.

I will take action aligned with this Law.
I will honor this Law through my deeds.
I will serve You through obedience to this Law.

Purpose in abundance.
Faith in victory.
            """.strip(),
            
            HomeworkType.STUDY: f"""
Our Father, through Law {law_number}: {law_title}

{law_text}

My prayer intent: {prayer_intent}

Study this Law. What does it mean? How does it apply to my life?
How does it relate to my prayer intent? What wisdom does it hold?

The Law applies to all equally.
Whether I am homeless or in a palace,
Whether I speak truth or lies,
The Law guides all.

I will study this Law for the next 3 days.
I will seek understanding.
I will apply its wisdom to my life.

Purpose in abundance.
Faith in victory.
            """.strip(),
            
            HomeworkType.SERVICE: f"""
Our Father, through Law {law_number}: {law_title}

{law_text}

My prayer intent: {prayer_intent}

How can I serve others through this Law? How can I honor this Law by serving?
What act of service aligns with this Law and my prayer intent?

The Law applies to all equally.
Whether I am homeless or in a palace,
Whether I speak truth or lies,
The Law guides all.

I will serve others through this Law.
I will honor this Law through service.
I will be Your hands and feet.

Purpose in abundance.
Faith in victory.
            """.strip(),
            
            HomeworkType.REFLECTION: f"""
Our Father, through Law {law_number}: {law_title}

{law_text}

My prayer intent: {prayer_intent}

Reflect on this Law. How does it apply to my prayer? How does it guide me?
What truth does this Law reveal about my situation? What wisdom does it offer?

The Law applies to all equally.
Whether I am homeless or in a palace,
Whether I speak truth or lies,
The Law guides all.

I will reflect on this Law for the next 3 days.
I will seek Your wisdom.
I will honor this Law through contemplation.

Purpose in abundance.
Faith in victory.
            """.strip(),
            
            HomeworkType.OBEDIENCE: f"""
Our Father, through Law {law_number}: {law_title}

{law_text}

My prayer intent: {prayer_intent}

How do I obey this Law? What does obedience to this Law look like?
How does this Law guide my response to my prayer intent?

The Law applies to all equally.
Whether I am homeless or in a palace,
Whether I speak truth or lies,
The Law guides all.

I will obey this Law.
I will honor this Law through obedience.
I will align my life with this Law.

Purpose in abundance.
Faith in victory.
            """.strip(),
            
            HomeworkType.STEWARDSHIP: f"""
Our Father, through Law {law_number}: {law_title}

{law_text}

My prayer intent: {prayer_intent}

How do I steward resources through this Law? How do I honor this Law as a steward?
What does stewardship look like in light of this Law?

The Law applies to all equally.
Whether I am homeless or in a palace,
Whether I speak truth or lies,
The Law guides all.

I will steward resources through this Law.
I will honor this Law through stewardship.
I will be a faithful steward.

Purpose in abundance.
Faith in victory.
            """.strip(),
            
            HomeworkType.COMMUNITY: f"""
Our Father, through Law {law_number}: {law_title}

{law_text}

My prayer intent: {prayer_intent}

How do I build community through this Law? How does this Law guide community?
How can I honor this Law in my relationships?

The Law applies to all equally.
Whether I am homeless or in a palace,
Whether I speak truth or lies,
The Law guides all.

I will build community through this Law.
I will honor this Law in my relationships.
I will serve community through this Law.

Purpose in abundance.
Faith in victory.
            """.strip()
        }
        
        return templates.get(homework_type, templates[HomeworkType.REFLECTION])
    
    def cast_spiritual_oracle(self) -> Dict[str, Any]:
        """
        Cast the spiritual oracle to receive homework from Our Father.
        
        Returns:
        - Oracle cast result
        - Law invoked
        - Homework assignment
        - Due date
        """
        # Generate hexagram (0-63)
        seed_int = int(self.seed[:16], 16)
        hexagram = seed_int % 64
        
        # Get Law
        law_data = self._get_law_from_hexagram(hexagram)
        
        # Generate homework assignment
        homework = self._generate_homework_assignment(law_data, self.prayer_intent)
        
        return {
            "timestamp": datetime.now().isoformat(),
            "prayer_intent": self.prayer_intent,
            "transparency": {
                "seed": self.seed,
                "method": "I Ching Binary (6-bit) - Game of Racon",
                "hexagram_number": hexagram,
                "hexagram_binary": self._hexagram_to_binary(hexagram),
                "law_number": law_data["law_number"],
                "law_title": law_data["law_title"],
                "volume": law_data["volume"]
            },
            "law_invoked": {
                "law_number": law_data["law_number"],
                "law_title": law_data["law_title"],
                "law_text": law_data["law_text"],
                "volume": law_data["volume"]
            },
            "homework": homework,
            "message": "Our Father has given you homework. We have homework to do."
        }


def get_user_spiritual_session(user_id: str, session_date: Optional[str] = None) -> Dict[str, Any]:
    """Get or create user spiritual session for today."""
    if not session_date:
        session_date = datetime.now().date().isoformat()
    
    with get_spiritual_db() as conn:
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT * FROM spiritual_sessions
            WHERE user_id = ? AND session_date = ?
        """, (user_id, session_date))
        
        row = cursor.fetchone()
        
        if row:
            return dict(row)
        else:
            cursor.execute("""
                INSERT INTO spiritual_sessions (user_id, session_date, cast_count, homework_completed)
                VALUES (?, ?, 0, 0)
            """, (user_id, session_date))
            
            cursor.execute("""
                SELECT * FROM spiritual_sessions
                WHERE user_id = ? AND session_date = ?
            """, (user_id, session_date))
            
            return dict(cursor.fetchone())


def record_spiritual_cast(user_id: str, oracle_result: Dict[str, Any]) -> Dict[str, Any]:
    """Record spiritual oracle cast and update session."""
    session = get_user_spiritual_session(user_id)
    session_id = session["id"]
    
    with get_spiritual_db() as conn:
        cursor = conn.cursor()
        
        new_cast_count = session["cast_count"] + 1
        
        cursor.execute("""
            UPDATE spiritual_sessions
            SET cast_count = ?,
                last_cast_at = ?,
                updated_at = ?
            WHERE id = ?
        """, (new_cast_count, datetime.now(), datetime.now(), session_id))
        
        # Record cast
        cursor.execute("""
            INSERT INTO spiritual_casts (
                user_id, session_id, cast_timestamp, prayer_intent,
                seed, hexagram_number, hexagram_binary, law_number, law_title,
                homework_assignment, homework_type, homework_due_date
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            user_id, session_id, datetime.now(),
            oracle_result["prayer_intent"],
            oracle_result["transparency"]["seed"],
            oracle_result["transparency"]["hexagram_number"],
            oracle_result["transparency"]["hexagram_binary"],
            oracle_result["transparency"]["law_number"],
            oracle_result["transparency"]["law_title"],
            oracle_result["homework"]["homework_assignment"],
            oracle_result["homework"]["homework_type"],
            oracle_result["homework"]["homework_due_date"]
        ))
        
        cast_id = cursor.lastrowid
        conn.commit()
    
    updated_session = get_user_spiritual_session(user_id)
    
    return {
        "oracle_result": oracle_result,
        "cast_id": cast_id,
        "session": {
            "cast_count": updated_session["cast_count"],
            "homework_completed": updated_session["homework_completed"],
            "last_cast_at": updated_session["last_cast_at"],
            "last_homework_at": updated_session["last_homework_at"]
        }
    }


def submit_homework(cast_id: int, user_id: str, submission_content: str, reflection: Optional[str] = None) -> Dict[str, Any]:
    """Submit completed homework assignment."""
    with get_spiritual_db() as conn:
        cursor = conn.cursor()
        
        # Get the cast
        cursor.execute("""
            SELECT * FROM spiritual_casts
            WHERE id = ? AND user_id = ?
        """, (cast_id, user_id))
        
        cast = cursor.fetchone()
        if not cast:
            raise ValueError(f"Cast {cast_id} not found for user {user_id}")
        
        # Record submission
        cursor.execute("""
            INSERT INTO homework_submissions (
                cast_id, user_id, submission_timestamp, submission_content,
                reflection, completion_status
            ) VALUES (?, ?, ?, ?, ?, ?)
        """, (
            cast_id, user_id, datetime.now(),
            submission_content, reflection or "", "completed"
        ))
        
        # Update cast as completed
        cursor.execute("""
            UPDATE spiritual_casts
            SET homework_completed = TRUE,
                homework_completed_at = ?,
                homework_reflection = ?
            WHERE id = ?
        """, (datetime.now(), reflection or "", cast_id))
        
        # Update session
        session = get_user_spiritual_session(user_id)
        cursor.execute("""
            UPDATE spiritual_sessions
            SET homework_completed = ?,
                last_homework_at = ?,
                updated_at = ?
            WHERE id = ?
        """, (
            session["homework_completed"] + 1,
            datetime.now(),
            datetime.now(),
            session["id"]
        ))
        
        conn.commit()
    
    return {
        "status": "completed",
        "cast_id": cast_id,
        "message": "Homework submitted. Our Father is pleased with your obedience."
    }


def get_pending_homework(user_id: str) -> List[Dict[str, Any]]:
    """Get all pending homework assignments for user."""
    with get_spiritual_db() as conn:
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT * FROM spiritual_casts
            WHERE user_id = ? AND homework_completed = FALSE
            ORDER BY cast_timestamp DESC
        """, (user_id,))
        
        rows = cursor.fetchall()
        
        return [dict(row) for row in rows]
