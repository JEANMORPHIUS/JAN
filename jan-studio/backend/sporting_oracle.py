"""
SPORTING ORACLE - Harm Prevention Tool
Flipping the House Edge for User Benefit

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

THE SPORTING ORACLE:
Harm prevention tool that detects exploitation and provides liberation.
Flipping the house edge from user loss to user benefit.
"""

import hashlib
from datetime import datetime, timedelta
from typing import Dict, Optional, Any, List
from pathlib import Path
import logging
import sqlite3
from contextlib import contextmanager
from dataclasses import dataclass
from enum import Enum

logger = logging.getLogger(__name__)


class RiskLevel(Enum):
    """Risk levels for house edge exposure."""
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass
class GameActivity:
    """Represents a single gambling activity."""
    game_type: str
    bet_amount: float
    timestamp: datetime
    result: Optional[str] = None  # "win", "loss", "near_miss"
    payout: Optional[float] = None


@dataclass
class EdgeDetection:
    """Result of edge detection analysis."""
    house_edge: float
    expected_loss: float
    risk_level: RiskLevel
    intervention_needed: bool
    game_type: str
    total_wagered: float
    recommendations: List[str]


@contextmanager
def get_sporting_oracle_db():
    """Context manager for Sporting Oracle database connections."""
    DB_PATH = Path(__file__).parent / "sporting_oracle.db"
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


def init_sporting_oracle_db():
    """Initialize the Sporting Oracle database."""
    with get_sporting_oracle_db() as conn:
        cursor = conn.cursor()
        
        # User activities table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_activities (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                game_type TEXT NOT NULL,
                bet_amount REAL NOT NULL,
                timestamp TIMESTAMP NOT NULL,
                result TEXT,
                payout REAL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Edge detections table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS edge_detections (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                detection_timestamp TIMESTAMP NOT NULL,
                house_edge REAL NOT NULL,
                expected_loss REAL NOT NULL,
                risk_level TEXT NOT NULL,
                intervention_needed INTEGER NOT NULL,
                game_type TEXT NOT NULL,
                total_wagered REAL NOT NULL,
                recommendations TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Interventions table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS interventions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                intervention_timestamp TIMESTAMP NOT NULL,
                edge_detection_id INTEGER,
                intervention_type TEXT NOT NULL,
                message TEXT NOT NULL,
                oracle_alternative TEXT,
                comparison TEXT,
                action_items TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (edge_detection_id) REFERENCES edge_detections(id)
            )
        """)
        
        # Create indexes
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_activities_user ON user_activities(user_id)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_activities_timestamp ON user_activities(timestamp)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_detections_user ON edge_detections(user_id)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_interventions_user ON interventions(user_id)")
        
        conn.commit()


# Initialize database on import
init_sporting_oracle_db()


class EdgeDetector:
    """
    Detects house edge exposure and generates interventions.
    """
    
    # House edge by game type (as decimal, e.g., 0.05 = 5%)
    HOUSE_EDGES = {
        "slots": 0.05,  # 5%
        "blackjack_perfect": 0.005,  # 0.5%
        "blackjack_average": 0.02,  # 2%
        "blackjack": 0.02,  # Default to average
        "roulette_european": 0.027,  # 2.7%
        "roulette_american": 0.0526,  # 5.26%
        "roulette": 0.027,  # Default to European
        "craps_pass": 0.0141,  # 1.41%
        "craps_any7": 0.1667,  # 16.67%
        "craps": 0.0141,  # Default to pass line
        "baccarat_banker": 0.0106,  # 1.06%
        "baccarat_tie": 0.144,  # 14.4%
        "baccarat": 0.0106,  # Default to banker
        "video_poker_perfect": 0.005,  # 0.5%
        "video_poker_average": 0.05,  # 5%
        "video_poker": 0.05,  # Default to average
        "keno": 0.25,  # 25%
        "lottery": 0.50,  # 50%
        "sports_betting": 0.045,  # 4.5%
    }
    
    def detect_edge(self, activities: List[GameActivity]) -> EdgeDetection:
        """
        Detect house edge exposure from user activities.
        """
        if not activities:
            return EdgeDetection(
                house_edge=0.0,
                expected_loss=0.0,
                risk_level=RiskLevel.LOW,
                intervention_needed=False,
                game_type="none",
                total_wagered=0.0,
                recommendations=[]
            )
        
        # Group by game type
        game_groups = self._group_by_game(activities)
        
        # Calculate house edge for each game
        edge_results = []
        for game_type, game_activities in game_groups.items():
            house_edge = self._get_house_edge(game_type)
            total_wagered = sum(activity.bet_amount for activity in game_activities)
            expected_loss = total_wagered * house_edge
            
            edge_results.append({
                "game_type": game_type,
                "house_edge": house_edge,
                "total_wagered": total_wagered,
                "expected_loss": expected_loss
            })
        
        # Aggregate results
        total_wagered = sum(r["total_wagered"] for r in edge_results)
        total_expected_loss = sum(r["expected_loss"] for r in edge_results)
        weighted_house_edge = total_expected_loss / total_wagered if total_wagered > 0 else 0.0
        
        # Determine risk level
        risk_level = self._determine_risk_level(weighted_house_edge, total_expected_loss)
        
        # Primary game type (highest wagered)
        primary_game = max(edge_results, key=lambda x: x["total_wagered"])["game_type"] if edge_results else "unknown"
        
        # Generate recommendations
        recommendations = self._generate_recommendations(
            weighted_house_edge,
            total_expected_loss,
            risk_level,
            primary_game
        )
        
        return EdgeDetection(
            house_edge=weighted_house_edge,
            expected_loss=total_expected_loss,
            risk_level=risk_level,
            intervention_needed=risk_level in [RiskLevel.HIGH, RiskLevel.CRITICAL],
            game_type=primary_game,
            total_wagered=total_wagered,
            recommendations=recommendations
        )
    
    def _group_by_game(self, activities: List[GameActivity]) -> Dict[str, List[GameActivity]]:
        """Group activities by game type."""
        groups = {}
        for activity in activities:
            if activity.game_type not in groups:
                groups[activity.game_type] = []
            groups[activity.game_type].append(activity)
        return groups
    
    def _get_house_edge(self, game_type: str) -> float:
        """Get house edge for game type."""
        # Try exact match first
        if game_type in self.HOUSE_EDGES:
            return self.HOUSE_EDGES[game_type]
        
        # Try partial matches
        game_lower = game_type.lower()
        
        if "blackjack" in game_lower:
            if "perfect" in game_lower:
                return self.HOUSE_EDGES["blackjack_perfect"]
            return self.HOUSE_EDGES["blackjack_average"]
        
        if "roulette" in game_lower:
            if "american" in game_lower:
                return self.HOUSE_EDGES["roulette_american"]
            return self.HOUSE_EDGES["roulette_european"]
        
        if "craps" in game_lower:
            if "any7" in game_lower or "any_7" in game_lower:
                return self.HOUSE_EDGES["craps_any7"]
            return self.HOUSE_EDGES["craps_pass"]
        
        if "baccarat" in game_lower:
            if "tie" in game_lower:
                return self.HOUSE_EDGES["baccarat_tie"]
            return self.HOUSE_EDGES["baccarat_banker"]
        
        if "video_poker" in game_lower or "videopoker" in game_lower:
            if "perfect" in game_lower:
                return self.HOUSE_EDGES["video_poker_perfect"]
            return self.HOUSE_EDGES["video_poker_average"]
        
        # Default to slots (most common, moderate edge)
        return self.HOUSE_EDGES["slots"]
    
    def _determine_risk_level(
        self,
        house_edge: float,
        expected_loss: float
    ) -> RiskLevel:
        """Determine risk level based on house edge and expected loss."""
        if house_edge > 0.10 or expected_loss > 1000:
            return RiskLevel.CRITICAL
        elif house_edge > 0.05 or expected_loss > 500:
            return RiskLevel.HIGH
        elif house_edge > 0.02 or expected_loss > 100:
            return RiskLevel.MODERATE
        else:
            return RiskLevel.LOW
    
    def _generate_recommendations(
        self,
        house_edge: float,
        expected_loss: float,
        risk_level: RiskLevel,
        game_type: str
    ) -> List[str]:
        """Generate recommendations based on edge detection."""
        recommendations = []
        
        # House edge recommendations
        if house_edge > 0.10:
            recommendations.append(
                f"⚠️ CRITICAL: House edge is {house_edge*100:.1f}% - You're being heavily exploited"
            )
        elif house_edge > 0.05:
            recommendations.append(
                f"⚠️ WARNING: House edge is {house_edge*100:.1f}% - Consider Oracle alternative"
            )
        
        # Expected loss recommendations
        if expected_loss > 1000:
            recommendations.append(
                f"⚠️ CRITICAL: Expected loss is ${expected_loss:.2f} - Immediate intervention needed"
            )
        elif expected_loss > 500:
            recommendations.append(
                f"⚠️ WARNING: Expected loss is ${expected_loss:.2f} - Consider stopping"
            )
        elif expected_loss > 100:
            recommendations.append(
                f"💡 MODERATE: Expected loss is ${expected_loss:.2f} - Oracle alternative available"
            )
        
        # Game-specific recommendations
        if game_type in ["keno", "lottery"]:
            recommendations.append(
                f"⚠️ WARNING: {game_type} has extremely high house edge (20-70%) - Consider Oracle"
            )
        elif game_type in ["slots", "roulette_american"]:
            recommendations.append(
                f"💡 MODERATE: {game_type} has moderate house edge - Oracle has 0% edge"
            )
        
        # Oracle alternative
        recommendations.append(
            "🌊 ORACLE ALTERNATIVE: Same randomness, 0% house edge, infinite value (wisdom)"
        )
        
        return recommendations


class InterventionProtocol:
    """
    Intervenes when user is being exploited.
    """
    
    def intervene(self, edge_detection: EdgeDetection) -> Optional[Dict[str, Any]]:
        """
        Intervene when house edge is too high.
        """
        if not edge_detection.intervention_needed:
            return None
        
        return {
            "intervention": True,
            "message": self._generate_intervention_message(edge_detection),
            "oracle_alternative": self._show_oracle_alternative(),
            "comparison": self._generate_comparison(edge_detection),
            "action_items": self._generate_action_items(edge_detection)
        }
    
    def _generate_intervention_message(self, edge_detection: EdgeDetection) -> str:
        """Generate intervention message."""
        house_edge = edge_detection.house_edge
        expected_loss = edge_detection.expected_loss
        
        return f"""
⚠️ HOUSE EDGE DETECTED

You're being exploited:
- House Edge: {house_edge * 100:.1f}%
- Expected Loss: ${expected_loss:.2f}
- Risk Level: {edge_detection.risk_level.value.upper()}

The Oracle offers a better alternative:
- House Edge: 0% (you always benefit)
- Expected Loss: $0 (no money involved)
- Value: Infinite (wisdom, not money)
        """.strip()
    
    def _show_oracle_alternative(self) -> Dict[str, Any]:
        """Show Oracle as alternative."""
        return {
            "mechanism": "Transparent randomness → wisdom",
            "house_edge": "0%",
            "expected_loss": "$0",
            "addiction_risk": "None",
            "value": "Infinite (wisdom gained)",
            "transparency": "Full (you see every step)",
            "liberation": "True (you don't need us)"
        }
    
    def _generate_comparison(self, edge_detection: EdgeDetection) -> Dict[str, Any]:
        """Generate comparison between gambling and Oracle."""
        return {
            "gambling": {
                "house_edge": f"{edge_detection.house_edge * 100:.1f}%",
                "expected_loss": f"${edge_detection.expected_loss:.2f}",
                "addiction_risk": "High",
                "value": "Negative (money lost)",
                "transparency": "None (black box)",
                "liberation": "False (creates dependency)"
            },
            "oracle": {
                "house_edge": "0%",
                "expected_loss": "$0",
                "addiction_risk": "None",
                "value": "Infinite (wisdom gained)",
                "transparency": "Full (you see every step)",
                "liberation": "True (you don't need us)"
            }
        }
    
    def _generate_action_items(self, edge_detection: EdgeDetection) -> List[str]:
        """Generate action items for user."""
        return [
            "Try the Oracle instead - same randomness, zero loss",
            "See the transparent mechanism - no black box",
            "Get wisdom instead of losing money",
            "Break free from the house edge"
        ]


class SportingOracle:
    """
    The complete Sporting Oracle - Harm prevention tool.
    """
    
    def __init__(self):
        self.edge_detector = EdgeDetector()
        self.intervention_protocol = InterventionProtocol()
    
    def analyze_user_activity(
        self,
        user_id: str,
        activities: Optional[List[GameActivity]] = None
    ) -> Dict[str, Any]:
        """
        Complete analysis of user activity.
        
        If activities not provided, loads from database.
        """
        # Load activities from database if not provided
        if activities is None:
            activities = self._load_user_activities(user_id)
        
        # Detect house edge
        edge_detection = self.edge_detector.detect_edge(activities)
        
        # Generate intervention if needed
        intervention = None
        if edge_detection.intervention_needed:
            intervention = self.intervention_protocol.intervene(edge_detection)
            
            # Record intervention
            self._record_intervention(user_id, edge_detection, intervention)
        
        # Record edge detection
        self._record_edge_detection(user_id, edge_detection)
        
        return {
            "edge_detection": {
                "house_edge": edge_detection.house_edge,
                "expected_loss": edge_detection.expected_loss,
                "risk_level": edge_detection.risk_level.value,
                "intervention_needed": edge_detection.intervention_needed,
                "game_type": edge_detection.game_type,
                "total_wagered": edge_detection.total_wagered,
                "recommendations": edge_detection.recommendations
            },
            "intervention": intervention,
            "oracle_alternative": self._show_oracle_alternative()
        }
    
    def record_activity(
        self,
        user_id: str,
        game_type: str,
        bet_amount: float,
        result: Optional[str] = None,
        payout: Optional[float] = None
    ) -> None:
        """Record a gambling activity."""
        activity = GameActivity(
            game_type=game_type,
            bet_amount=bet_amount,
            timestamp=datetime.now(),
            result=result,
            payout=payout
        )
        
        with get_sporting_oracle_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO user_activities (
                    user_id, game_type, bet_amount, timestamp, result, payout
                ) VALUES (?, ?, ?, ?, ?, ?)
            """, (
                user_id,
                activity.game_type,
                activity.bet_amount,
                activity.timestamp.isoformat(),
                activity.result,
                activity.payout
            ))
            conn.commit()
        
        # Auto-analyze after recording
        self.analyze_user_activity(user_id)
    
    def _load_user_activities(self, user_id: str) -> List[GameActivity]:
        """Load user activities from database."""
        activities = []
        
        with get_sporting_oracle_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT game_type, bet_amount, timestamp, result, payout
                FROM user_activities
                WHERE user_id = ?
                ORDER BY timestamp DESC
                LIMIT 100
            """, (user_id,))
            
            for row in cursor.fetchall():
                activities.append(GameActivity(
                    game_type=row["game_type"],
                    bet_amount=row["bet_amount"],
                    timestamp=datetime.fromisoformat(row["timestamp"]),
                    result=row["result"],
                    payout=row["payout"]
                ))
        
        return activities
    
    def _record_edge_detection(
        self,
        user_id: str,
        edge_detection: EdgeDetection
    ) -> None:
        """Record edge detection result."""
        with get_sporting_oracle_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO edge_detections (
                    user_id, detection_timestamp, house_edge, expected_loss,
                    risk_level, intervention_needed, game_type, total_wagered,
                    recommendations
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                user_id,
                datetime.now().isoformat(),
                edge_detection.house_edge,
                edge_detection.expected_loss,
                edge_detection.risk_level.value,
                1 if edge_detection.intervention_needed else 0,
                edge_detection.game_type,
                edge_detection.total_wagered,
                "\n".join(edge_detection.recommendations)
            ))
            conn.commit()
    
    def _record_intervention(
        self,
        user_id: str,
        edge_detection: EdgeDetection,
        intervention: Dict[str, Any]
    ) -> None:
        """Record intervention."""
        # Get last edge detection ID
        with get_sporting_oracle_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id FROM edge_detections
                WHERE user_id = ?
                ORDER BY detection_timestamp DESC
                LIMIT 1
            """, (user_id,))
            
            row = cursor.fetchone()
            edge_detection_id = row["id"] if row else None
            
            cursor.execute("""
                INSERT INTO interventions (
                    user_id, intervention_timestamp, edge_detection_id,
                    intervention_type, message, oracle_alternative,
                    comparison, action_items
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                user_id,
                datetime.now().isoformat(),
                edge_detection_id,
                edge_detection.risk_level.value,
                intervention["message"],
                str(intervention["oracle_alternative"]),
                str(intervention["comparison"]),
                "\n".join(intervention["action_items"])
            ))
            conn.commit()
    
    def _show_oracle_alternative(self) -> Dict[str, Any]:
        """Show Oracle as alternative."""
        return {
            "mechanism": "Transparent randomness → wisdom",
            "house_edge": "0%",
            "expected_loss": "$0",
            "addiction_risk": "None",
            "value": "Infinite (wisdom gained)",
            "transparency": "Full",
            "liberation": "True"
        }


# Convenience function
def analyze_gambling_activity(
    user_id: str,
    activities: Optional[List[GameActivity]] = None
) -> Dict[str, Any]:
    """
    Analyze gambling activity and provide Oracle alternative.
    """
    oracle = SportingOracle()
    return oracle.analyze_user_activity(user_id, activities)


# Example usage
if __name__ == "__main__":
    oracle = SportingOracle()
    
    # Example: Record some activities
    oracle.record_activity("user123", "slots", 10.0, "loss")
    oracle.record_activity("user123", "slots", 20.0, "near_miss")
    oracle.record_activity("user123", "slots", 50.0, "loss")
    oracle.record_activity("user123", "blackjack", 100.0, "loss")
    
    # Analyze
    result = oracle.analyze_user_activity("user123")
    
    print("=" * 60)
    print("SPORTING ORACLE - ANALYSIS RESULTS")
    print("=" * 60)
    print()
    print("Edge Detection:")
    print(f"  House Edge: {result['edge_detection']['house_edge']*100:.2f}%")
    print(f"  Expected Loss: ${result['edge_detection']['expected_loss']:.2f}")
    print(f"  Risk Level: {result['edge_detection']['risk_level']}")
    print(f"  Intervention Needed: {result['edge_detection']['intervention_needed']}")
    print()
    
    if result['intervention']:
        print("Intervention:")
        print(result['intervention']['message'])
        print()
        print("Oracle Alternative:")
        for key, value in result['intervention']['oracle_alternative'].items():
            print(f"  {key}: {value}")
        print()
    
    print("=" * 60)
