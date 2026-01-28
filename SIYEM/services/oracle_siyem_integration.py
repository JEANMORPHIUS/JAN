"""
ORACLE SIYEM INTEGRATION
Transparent RNG Engine + 40 Laws Interpretation + Anti-Addiction Metrics

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

ORACLE PRINCIPLES:
1. Transparency: User sees exactly how randomness is generated
2. Anti-Addiction: Success = user creates and LEAVES (inverse of platform metrics)
3. 40 Laws Integration: Every cast interprets a Law from Book of Racon
4. Creative Liberation: Flipping gambling algorithms for creative empowerment

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X.
"""

import hashlib
from datetime import datetime, timedelta
from typing import Dict, Optional, Any, List
from pathlib import Path
import logging
import sqlite3
from contextlib import contextmanager
import json

logger = logging.getLogger(__name__)


@contextmanager
def get_oracle_siyem_db():
    """Context manager for Oracle SIYEM database connections."""
    DB_PATH = Path(__file__).parent.parent / "data" / "oracle_siyem.db"
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
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


def init_oracle_siyem_db():
    """Initialize the Oracle SIYEM database."""
    with get_oracle_siyem_db() as conn:
        cursor = conn.cursor()
        
        # Oracle casts table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS oracle_casts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                cast_timestamp TIMESTAMP NOT NULL,
                intent TEXT NOT NULL,
                context TEXT,
                seed TEXT NOT NULL,
                seed_components TEXT NOT NULL,  -- JSON of seed parts
                hexagram_number INTEGER NOT NULL,
                hexagram_binary TEXT NOT NULL,
                law_number INTEGER NOT NULL,
                law_title TEXT NOT NULL,
                law_volume TEXT NOT NULL,
                interpretation TEXT NOT NULL,
                creative_prompt TEXT NOT NULL,
                transparency_data TEXT NOT NULL,  -- Full transparency JSON
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # User sessions table (anti-addiction tracking)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS oracle_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                session_date DATE NOT NULL,
                cast_count INTEGER DEFAULT 0,
                time_creating INTEGER DEFAULT 0,  -- Minutes spent creating
                last_cast_at TIMESTAMP,
                last_break_at TIMESTAMP,
                creative_outputs INTEGER DEFAULT 0,  -- Number of things created
                break_reminders INTEGER DEFAULT 0,
                execution_nudges INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(user_id, session_date)
            )
        """)
        
        # Anti-addiction metrics table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS anti_addiction_metrics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                metric_date DATE NOT NULL,
                casts_today INTEGER DEFAULT 0,
                time_on_platform INTEGER DEFAULT 0,  -- Minutes
                creative_outputs INTEGER DEFAULT 0,
                break_taken BOOLEAN DEFAULT 0,
                execution_triggered BOOLEAN DEFAULT 0,
                success_score REAL DEFAULT 0.0,  -- Higher = more creation, less time
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(user_id, metric_date)
            )
        """)
        
        # 40 Laws registry (if not exists, will be populated from racon_registry)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS racon_laws_cache (
                law_number INTEGER PRIMARY KEY,
                law_title TEXT NOT NULL,
                law_text TEXT NOT NULL,
                volume TEXT NOT NULL,
                category TEXT,
                interpretation_guidance TEXT,
                last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_casts_user ON oracle_casts(user_id)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_casts_law ON oracle_casts(law_number)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_sessions_user_date ON oracle_sessions(user_id, session_date)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_metrics_user_date ON anti_addiction_metrics(user_id, metric_date)")
        
        conn.commit()


# Initialize database on import
init_oracle_siyem_db()


class TransparentRNG:
    """
    Transparent Random Number Generator
    
    Unlike gambling RNG (opaque, exploitative), this is:
    - Fully transparent (user sees seed, method, result)
    - Deterministic (same seed = same result)
    - Verifiable (user can verify the process)
    - User-serving (generates value, not extracts it)
    """
    
    @staticmethod
    def generate_seed(
        user_intent: str,
        timestamp: str,
        context: Optional[str] = None,
        user_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Generate transparent seed with full component visibility.
        
        Returns:
            Dict with seed hash and all components for transparency
        """
        components = {
            "user_intent": user_intent,
            "timestamp": timestamp,
            "context": context or "",
            "user_id": user_id or "public"
        }
        
        # Create seed string from components
        seed_string = f"{user_intent}:{timestamp}:{context or ''}:{user_id or 'public'}"
        seed_hash = hashlib.sha256(seed_string.encode('utf-8')).hexdigest()
        
        return {
            "seed": seed_hash,
            "components": components,
            "method": "SHA-256 hash of concatenated components",
            "verifiable": True
        }
    
    @staticmethod
    def seed_to_hexagram(seed: str) -> Dict[str, Any]:
        """
        Convert seed to I Ching hexagram (0-63).
        
        Uses first 16 hex characters of seed to generate number.
        """
        # Use first 16 hex characters (64 bits of entropy)
        seed_int = int(seed[:16], 16)
        hexagram = seed_int % 64
        
        # Convert to 6-bit binary (I Ching format)
        hexagram_binary = format(hexagram, '06b')
        
        return {
            "hexagram_number": hexagram,
            "hexagram_binary": hexagram_binary,
            "method": "First 16 hex chars of seed → integer → mod 64 → 6-bit binary",
            "transparent": True
        }


class LawsInterpreter:
    """
    40 Laws Interpretation Layer
    
    Maps hexagrams to Book of Racon Laws and provides
    context-specific interpretations for creative work.
    """
    
    def __init__(self):
        self.laws_cache = self._load_laws_cache()
    
    def _load_laws_cache(self) -> Dict[int, Dict[str, Any]]:
        """Load laws from racon_registry or use fallback."""
        cache = {}
        
        # Try to load from racon_registry
        try:
            from racon_registry import get_racon_db
            import sqlite3
            
            with get_racon_db() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT law_number, law_title, law_text, volume, category
                    FROM racon_laws
                """)
                
                for row in cursor.fetchall():
                    cache[row["law_number"]] = {
                        "law_number": row["law_number"],
                        "law_title": row["law_title"],
                        "law_text": row["law_text"],
                        "volume": row["volume"],
                        "category": row.get("category", "")
                    }
        except (ImportError, sqlite3.Error, Exception) as e:
            logger.warning(f"Could not load laws from registry: {e}, using fallback")
        
        # If cache is empty, use fallback
        if not cache:
            cache = self._get_fallback_laws()
        
        # Update cache in database
        self._update_laws_cache(cache)
        
        return cache
    
    def _get_fallback_laws(self) -> Dict[int, Dict[str, Any]]:
        """Fallback laws if registry unavailable."""
        laws = {}
        
        # Volume 1: Loyalty (Laws 1-10)
        laws[1] = {"law_number": 1, "law_title": "The Table Never Lies", "law_text": "The table, bread and salt, bonds that never expire. What is created reflects character and honor.", "volume": "Loyalty", "category": "Truth"}
        laws[2] = {"law_number": 2, "law_title": "Your Word Is Your Bond", "law_text": "Creative commitments are laws, not suggestions. What you promise, you must deliver.", "volume": "Loyalty", "category": "Commitment"}
        laws[3] = {"law_number": 3, "law_title": "Never Betray the Table", "law_text": "Creative collaboration is sacred. What is shared in creation is protected.", "volume": "Loyalty", "category": "Trust"}
        laws[5] = {"law_number": 5, "law_title": "The Circle Is Sacred", "law_text": "Once chosen, loyalty binds forever. Like bread and salt, bonds are eternal.", "volume": "Loyalty", "category": "Loyalty"}
        
        # Volume 2: Silence (Laws 11-20)
        laws[11] = {"law_number": 11, "law_title": "Wisdom Lives in the Quiet", "law_text": "Contemplation produces wisdom. Noise obscures truth. Silence reveals understanding.", "volume": "Silence", "category": "Wisdom"}
        laws[13] = {"law_number": 13, "law_title": "Silence Is Not Weakness", "law_text": "Strategic quiet is powerful. Not speaking can be strength. Discretion is a tool.", "volume": "Silence", "category": "Strategy"}
        laws[15] = {"law_number": 15, "law_title": "Listen Before You Speak", "law_text": "Understand before you change. Wisdom comes from listening. Change requires understanding.", "volume": "Silence", "category": "Understanding"}
        
        # Volume 3: Respect (Laws 21-30)
        laws[21] = {"law_number": 21, "law_title": "Honor Your Elders", "law_text": "Respect for those who came before. Wisdom comes from experience. Tradition is valuable.", "volume": "Respect", "category": "Respect"}
        laws[23] = {"law_number": 23, "law_title": "Respect the Hierarchy", "law_text": "Structure maintains order. Hierarchy is not oppression. Order enables function.", "volume": "Respect", "category": "Structure"}
        
        # Volume 4: War (Laws 31-40)
        laws[31] = {"law_number": 31, "law_title": "Do Not Start What You Cannot Finish", "law_text": "Every expansion is a commitment to completion. Begin only what you can finish.", "volume": "War", "category": "Completion"}
        laws[35] = {"law_number": 35, "law_title": "Finish What You Begin", "law_text": "Every project, every commitment, every creative war must be completed. Completion is non-negotiable.", "volume": "War", "category": "Completion"}
        laws[37] = {"law_number": 37, "law_title": "Protect the System", "law_text": "The ecosystem defends itself. System protection is required. Defense is active.", "volume": "War", "category": "Protection"}
        
        # Fill in missing laws with generic entries
        for i in range(1, 41):
            if i not in laws:
                volume = self._get_volume_from_law(i)
                laws[i] = {
                    "law_number": i,
                    "law_title": f"Law {i}",
                    "law_text": f"Law {i} from {volume}. The old laws still hold.",
                    "volume": volume,
                    "category": "Universal"
                }
        
        return laws
    
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
    
    def _update_laws_cache(self, laws: Dict[int, Dict[str, Any]]):
        """Update laws cache in database."""
        try:
            with get_oracle_siyem_db() as conn:
                cursor = conn.cursor()
                for law_num, law_data in laws.items():
                    cursor.execute("""
                        INSERT OR REPLACE INTO racon_laws_cache
                        (law_number, law_title, law_text, volume, category, last_updated)
                        VALUES (?, ?, ?, ?, ?, ?)
                    """, (
                        law_data["law_number"],
                        law_data["law_title"],
                        law_data["law_text"],
                        law_data["volume"],
                        law_data.get("category", ""),
                        datetime.now()
                    ))
                conn.commit()
        except Exception as e:
            logger.warning(f"Could not update laws cache: {e}")
    
    def hexagram_to_law(self, hexagram: int) -> Dict[str, Any]:
        """
        Map hexagram (0-63) to Book of Racon Law (1-40).
        
        Args:
            hexagram: Hexagram number (0-63)
        
        Returns:
            Dict with law data
        """
        law_number = (hexagram % 40) + 1  # 1-40
        
        if law_number in self.laws_cache:
            return self.laws_cache[law_number].copy()
        else:
            # Fallback
            volume = self._get_volume_from_law(law_number)
            return {
                "law_number": law_number,
                "law_title": f"Law {law_number}",
                "law_text": f"Law {law_number} from {volume}.",
                "volume": volume,
                "category": "Universal"
            }
    
    def interpret_law_for_creativity(
        self,
        law_data: Dict[str, Any],
        user_intent: str,
        context: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Interpret Law for creative context.
        
        Provides actionable creative guidance based on the Law.
        """
        law_number = law_data["law_number"]
        law_title = law_data["law_title"]
        law_text = law_data["law_text"]
        volume = law_data["volume"]
        
        # Generate creative interpretation
        interpretation = f"""
Law {law_number}: {law_title}
Volume: {volume}

{law_text}

**For Your Creative Work:**

This Law speaks to your intent: "{user_intent}"

The Law guides your creative path. It offers wisdom for your current challenge.
Apply this Law's principles to your creative work. Let it shape your approach.

**Creative Prompt:**
How does {law_title} inform your creative process?
What does this Law reveal about your current challenge?
How can you honor this Law in your creative work?
        """.strip()
        
        # Generate actionable creative prompt
        creative_prompt = f"""
Based on Law {law_number}: {law_title}

Your intent: {user_intent}
{context and f"Context: {context}" or ""}

The Law says: {law_text}

**Your Creative Challenge:**
Apply {law_title} to your creative work. How does this Law guide your process?
What creative action does this Law inspire?

**Remember:** The Oracle serves your creativity. Use this guidance to CREATE, then step away to execute.
        """.strip()
        
        return {
            "interpretation": interpretation,
            "creative_prompt": creative_prompt,
            "law_data": law_data
        }


class AntiAddictionMetrics:
    """
    Anti-Addiction Success Metrics
    
    Success = User creates and LEAVES (inverse of platform metrics)
    
    Tracks:
    - Cast count (but encourages breaks)
    - Time creating (not time on platform)
    - Creative outputs (actual work created)
    - Break reminders (healthy practice)
    - Execution nudges (push to create, not consume)
    """
    
    @staticmethod
    def get_user_session(user_id: str) -> Dict[str, Any]:
        """Get or create user session for today."""
        today = datetime.now().date()
        
        with get_oracle_siyem_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM oracle_sessions
                WHERE user_id = ? AND session_date = ?
            """, (user_id, today))
            
            row = cursor.fetchone()
            
            if row:
                return dict(row)
            else:
                # Create new session
                cursor.execute("""
                    INSERT INTO oracle_sessions
                    (user_id, session_date, cast_count, time_creating, last_cast_at, last_break_at)
                    VALUES (?, ?, 0, 0, ?, ?)
                """, (user_id, today, datetime.now(), datetime.now()))
                conn.commit()
                
                return {
                    "id": cursor.lastrowid,
                    "user_id": user_id,
                    "session_date": today.isoformat(),
                    "cast_count": 0,
                    "time_creating": 0,
                    "last_cast_at": datetime.now().isoformat(),
                    "last_break_at": datetime.now().isoformat(),
                    "creative_outputs": 0,
                    "break_reminders": 0,
                    "execution_nudges": 0
                }
    
    @staticmethod
    def record_cast(user_id: str):
        """Record an oracle cast."""
        session = AntiAddictionMetrics.get_user_session(user_id)
        
        with get_oracle_siyem_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE oracle_sessions
                SET cast_count = cast_count + 1,
                    last_cast_at = ?,
                    updated_at = ?
                WHERE id = ?
            """, (datetime.now(), datetime.now(), session["id"]))
            conn.commit()
    
    @staticmethod
    def record_creative_output(user_id: str):
        """Record that user created something (success metric)."""
        session = AntiAddictionMetrics.get_user_session(user_id)
        
        with get_oracle_siyem_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE oracle_sessions
                SET creative_outputs = creative_outputs + 1,
                    updated_at = ?
                WHERE id = ?
            """, (datetime.now(), session["id"]))
            conn.commit()
    
    @staticmethod
    def check_ethical_guardrails(user_id: str) -> Dict[str, Any]:
        """
        Check ethical guardrails and return recommendations.
        
        Returns:
            Dict with guardrail status and recommendations
        """
        session = AntiAddictionMetrics.get_user_session(user_id)
        cast_count = session["cast_count"]
        creative_outputs = session.get("creative_outputs", 0)
        last_break = session.get("last_break_at")
        
        guardrails = {
            "status": "healthy",
            "recommendations": [],
            "break_suggested": False,
            "execution_nudged": False
        }
        
        # After 3 casts: Break prompt
        if cast_count >= 3 and cast_count < 5:
            if not last_break or (datetime.now() - datetime.fromisoformat(last_break.replace('Z', '+00:00').split('+')[0])).seconds > 3600:
                guardrails["status"] = "break_suggested"
                guardrails["break_suggested"] = True
                guardrails["recommendations"].append(
                    "You've cast 3 times. Consider taking a break to reflect on what emerged."
                )
        
        # After 5 casts: Reflection prompt
        if cast_count >= 5 and cast_count < 10:
            guardrails["status"] = "reflection_suggested"
            guardrails["recommendations"].append(
                "You've cast 5 times. Take time to reflect on the patterns. What is the Oracle telling you?"
            )
        
        # After 10 casts: Execution nudge
        if cast_count >= 10:
            guardrails["status"] = "execution_nudged"
            guardrails["execution_nudged"] = True
            guardrails["recommendations"].append(
                "You've cast 10 times. The Oracle has spoken. Now is the time to CREATE. Step away and execute."
            )
        
        # Success metric: More creative outputs than casts = healthy
        if creative_outputs > cast_count:
            guardrails["status"] = "success"
            guardrails["recommendations"].append(
                f"Excellent! You've created {creative_outputs} outputs from {cast_count} casts. This is the goal."
            )
        
        return guardrails
    
    @staticmethod
    def calculate_success_score(user_id: str) -> float:
        """
        Calculate anti-addiction success score.
        
        Higher score = more creation, less time on platform
        Success = user creates and LEAVES
        """
        session = AntiAddictionMetrics.get_user_session(user_id)
        cast_count = session["cast_count"]
        creative_outputs = session.get("creative_outputs", 0)
        time_creating = session.get("time_creating", 0)
        
        if cast_count == 0:
            return 0.0
        
        # Success = (creative_outputs / cast_count) * (1 / (1 + time_creating/60))
        # More outputs per cast = better
        # Less time on platform = better
        output_ratio = creative_outputs / cast_count if cast_count > 0 else 0
        time_penalty = 1 / (1 + time_creating / 60)  # Penalize time on platform
        
        success_score = output_ratio * time_penalty * 100  # Scale to 0-100
        
        return round(success_score, 2)


class OracleSIYEM:
    """
    Oracle SIYEM Integration
    
    Combines:
    - Transparent RNG Engine
    - 40 Laws Interpretation Layer
    - Anti-Addiction Success Metrics
    """
    
    def __init__(self):
        self.rng = TransparentRNG()
        self.laws_interpreter = LawsInterpreter()
        self.metrics = AntiAddictionMetrics()
    
    def cast_oracle(
        self,
        user_intent: str,
        context: Optional[str] = None,
        user_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Cast the Oracle with full transparency and anti-addiction metrics.
        
        Args:
            user_intent: User's creative question or challenge
            context: Current project context
            user_id: User identifier
        
        Returns:
            Complete oracle cast result with transparency data
        """
        user_id = user_id or "public"
        timestamp = datetime.now().isoformat()
        
        # 1. Generate transparent seed
        seed_data = self.rng.generate_seed(user_intent, timestamp, context, user_id)
        
        # 2. Convert seed to hexagram
        hexagram_data = self.rng.seed_to_hexagram(seed_data["seed"])
        
        # 3. Map hexagram to Law
        law_data = self.laws_interpreter.hexagram_to_law(hexagram_data["hexagram_number"])
        
        # 4. Interpret Law for creativity
        interpretation_data = self.laws_interpreter.interpret_law_for_creativity(
            law_data, user_intent, context
        )
        
        # 5. Record cast (anti-addiction tracking)
        self.metrics.record_cast(user_id)
        
        # 6. Check ethical guardrails
        guardrails = self.metrics.check_ethical_guardrails(user_id)
        
        # 7. Build transparency data
        transparency = {
            "seed": seed_data,
            "hexagram": hexagram_data,
            "law_mapping": {
                "hexagram": hexagram_data["hexagram_number"],
                "law_number": law_data["law_number"],
                "method": "hexagram % 40 + 1"
            },
            "verifiable": True,
            "user_can_verify": "User can recreate seed from components and verify hexagram calculation"
        }
        
        # 8. Get session and calculate detailed metrics
        session = self.metrics.get_user_session(user_id)
        success_score = self.metrics.calculate_success_score(user_id)
        
        # 9. Build success metrics
        success_metrics = {
            "success_score": success_score,
            "cast_count": session["cast_count"],
            "creative_outputs": session.get("creative_outputs", 0),
            "time_creating": session.get("time_creating", 0),
            "output_ratio": round(session.get("creative_outputs", 0) / session["cast_count"], 2) if session["cast_count"] > 0 else 0,
            "is_healthy": success_score > 50 and session.get("creative_outputs", 0) > session["cast_count"],
            "interpretation": {
                "score_explanation": "Higher score = more creation, less time on platform",
                "healthy_threshold": 50,
                "goal": "Create more outputs than casts, then step away to execute"
            }
        }
        
        # 10. Build mechanism visualization
        mechanism_visualization = {
            "flow": [
                {
                    "step": 1,
                    "name": "Seed Generation",
                    "input": f"Intent: '{user_intent[:50]}...' + Timestamp + Context",
                    "process": "SHA-256 hash of concatenated components",
                    "output": f"Seed: {seed_data['seed'][:16]}..."
                },
                {
                    "step": 2,
                    "name": "Hexagram Calculation",
                    "input": f"Seed: {seed_data['seed'][:16]}...",
                    "process": "First 16 hex chars → integer → mod 64 → 6-bit binary",
                    "output": f"Hexagram {hexagram_data['hexagram_number']} ({hexagram_data['hexagram_binary']})"
                },
                {
                    "step": 3,
                    "name": "Law Mapping",
                    "input": f"Hexagram: {hexagram_data['hexagram_number']}",
                    "process": "hexagram % 40 + 1",
                    "output": f"Law {law_data['law_number']}: {law_data['law_title']}"
                },
                {
                    "step": 4,
                    "name": "Law Interpretation",
                    "input": f"Law {law_data['law_number']} + User Intent",
                    "process": "Context-specific creative guidance",
                    "output": "Creative prompt generated"
                }
            ],
            "verification_steps": [
                "1. Recreate seed: SHA-256(user_intent:timestamp:context:user_id)",
                "2. Verify hexagram: int(seed[:16], 16) % 64",
                "3. Verify law: hexagram % 40 + 1",
                "4. All steps are deterministic and verifiable"
            ],
            "transparency_level": "full"
        }
        
        # 11. Build result
        result = {
            "timestamp": timestamp,
            "user_id": user_id,
            "user_intent": user_intent,
            "creative_context": context or "",
            "transparency": transparency,
            "mechanism_visualization": mechanism_visualization,
            "oracle_interpretation": {
                "law": law_data,
                "interpretation": interpretation_data["interpretation"],
                "creative_prompt": interpretation_data["creative_prompt"]
            },
            "ethical_guardrails": guardrails,
            "session": session,
            "success_metrics": success_metrics,
            "success_score": success_score
        }
        
        # 9. Record cast in database
        self._record_cast(result)
        
        return result
    
    def _record_cast(self, result: Dict[str, Any]):
        """Record oracle cast in database."""
        try:
            with get_oracle_siyem_db() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO oracle_casts (
                        user_id, cast_timestamp, intent, context,
                        seed, seed_components, hexagram_number, hexagram_binary,
                        law_number, law_title, law_volume,
                        interpretation, creative_prompt, transparency_data
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    result["user_id"],
                    result["timestamp"],
                    result["user_intent"],
                    result["creative_context"],
                    result["transparency"]["seed"]["seed"],
                    json.dumps(result["transparency"]["seed"]["components"]),
                    result["transparency"]["hexagram"]["hexagram_number"],
                    result["transparency"]["hexagram"]["hexagram_binary"],
                    result["transparency"]["law_mapping"]["law_number"],
                    result["oracle_interpretation"]["law"]["law_title"],
                    result["oracle_interpretation"]["law"]["volume"],
                    result["oracle_interpretation"]["interpretation"],
                    result["oracle_interpretation"]["creative_prompt"],
                    json.dumps(result["transparency"])
                ))
                conn.commit()
        except Exception as e:
            logger.warning(f"Could not record oracle cast: {e}")


# Convenience function
def cast_siyem_oracle(
    user_intent: str,
    context: Optional[str] = None,
    user_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Cast SIYEM Oracle - convenience function.
    
    Args:
        user_intent: User's creative question or challenge
        context: Current project context
        user_id: User identifier
    
    Returns:
        Complete oracle cast result
    """
    oracle = OracleSIYEM()
    return oracle.cast_oracle(user_intent, context, user_id)
