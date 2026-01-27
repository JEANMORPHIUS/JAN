"""
GEOPOLITICAL ANALYSIS ENGINE
Analyzing "Today and the Future" by Evaluating "Reality of the Field"

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

THE GEOPOLITICAL ANALYSIS ENGINE:
Monitors the "new generation" of global conflict through asymmetric warfare.
Evaluates "reality of the field" rather than "selling dreams."
Applies the Cengiz Han principle of sovereignty.
"""

from datetime import datetime
from typing import Dict, List, Optional, Any
from pathlib import Path
import logging
import sqlite3
from contextlib import contextmanager
from dataclasses import dataclass
from enum import Enum

logger = logging.getLogger(__name__)


class ConflictType(Enum):
    """Types of conflict being monitored."""
    ASYMMETRIC_WARFARE = "asymmetric_warfare"
    BORDER_DISPUTE = "border_dispute"
    TERRITORIAL_CLAIM = "territorial_claim"
    HOSTILE_MAPPING = "hostile_mapping"
    HELP_SEEKING_PARADOX = "help_seeking_paradox"
    STRATEGIC_LOYALTY_ISSUE = "strategic_loyalty_issue"


class RiskLevel(Enum):
    """Risk levels for geopolitical events."""
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass
class BorderEvent:
    """Represents a border-related event."""
    region: str
    border_point: str
    event_type: str
    timestamp: datetime
    description: str
    control_status: Optional[str] = None
    shift_speed: Optional[str] = None  # "rapid", "moderate", "slow"


@dataclass
class HostileMapping:
    """Represents a hostile mapping incident."""
    source: str
    target_territory: str
    claimed_by: str
    document_type: str  # "textbook", "official_map", "state_map"
    timestamp: datetime
    description: str
    barrier_level: str  # "definitive", "moderate", "minor"


@dataclass
class HelpSeekingParadox:
    """Represents a help-seeking paradox incident."""
    entity: str
    region: str
    hostile_label: str  # "murderer", "enemy", etc.
    aid_requested: str
    timestamp: datetime
    description: str
    paradox_level: str  # "high", "moderate", "low"


@dataclass
class StrategicLoyalty:
    """Represents a strategic loyalty assessment."""
    entity: str
    relationship_type: str  # "loyal_friend", "stone_thrower", "neutral"
    shared_resources: List[str]
    common_path: bool
    timestamp: datetime
    assessment: str


@contextmanager
def get_geopolitical_db():
    """Context manager for Geopolitical Analysis database connections."""
    DB_PATH = Path(__file__).parent / "geopolitical_analysis.db"
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


def init_geopolitical_db():
    """Initialize the Geopolitical Analysis database."""
    with get_geopolitical_db() as conn:
        cursor = conn.cursor()
        
        # Border events table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS border_events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                region TEXT NOT NULL,
                border_point TEXT NOT NULL,
                event_type TEXT NOT NULL,
                timestamp TIMESTAMP NOT NULL,
                description TEXT NOT NULL,
                control_status TEXT,
                shift_speed TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Hostile mappings table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS hostile_mappings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source TEXT NOT NULL,
                target_territory TEXT NOT NULL,
                claimed_by TEXT NOT NULL,
                document_type TEXT NOT NULL,
                timestamp TIMESTAMP NOT NULL,
                description TEXT NOT NULL,
                barrier_level TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Help-seeking paradoxes table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS help_seeking_paradoxes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                entity TEXT NOT NULL,
                region TEXT NOT NULL,
                hostile_label TEXT NOT NULL,
                aid_requested TEXT NOT NULL,
                timestamp TIMESTAMP NOT NULL,
                description TEXT NOT NULL,
                paradox_level TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Strategic loyalty assessments table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS strategic_loyalty (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                entity TEXT NOT NULL,
                relationship_type TEXT NOT NULL,
                shared_resources TEXT,
                common_path INTEGER NOT NULL,
                timestamp TIMESTAMP NOT NULL,
                assessment TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Analysis results table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS analysis_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                analysis_timestamp TIMESTAMP NOT NULL,
                region TEXT NOT NULL,
                conflict_type TEXT NOT NULL,
                risk_level TEXT NOT NULL,
                findings TEXT NOT NULL,
                recommendations TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Create indexes
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_border_events_region ON border_events(region)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_border_events_timestamp ON border_events(timestamp)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_hostile_mappings_territory ON hostile_mappings(target_territory)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_analysis_results_region ON analysis_results(region)")
        
        conn.commit()


# Initialize database on import
init_geopolitical_db()


class GeopoliticalAnalysisEngine:
    """
    Geopolitical Analysis Engine
    
    Monitors the "new generation" of global conflict through asymmetric warfare.
    Evaluates "reality of the field" rather than "selling dreams."
    """
    
    # Regions being monitored (15+ regions mentioned)
    MONITORED_REGIONS = [
        "Syria",
        "Iran",
        "Ukraine",
        "Gaza",
        "Iraq",
        "Libya",
        "Yemen",
        "Afghanistan",
        "Lebanon",
        "Cyprus",
        "Greece",
        "Armenia",
        "Azerbaijan",
        "Russia",
        "Turkey"
    ]
    
    # Strategic border points
    STRATEGIC_BORDER_POINTS = [
        "Rabia border crossing",
        "Fishabur passage",
        "Hatay",
        "Other strategic points"
    ]
    
    def __init__(self):
        self.analysis_timestamp = datetime.now()
    
    def analyze_border_dynamics(self, region: str, timeframe_days: int = 30) -> Dict[str, Any]:
        """
        Evaluate border dynamics and control of strategic points.
        Track how quickly field conditions shift.
        """
        with get_geopolitical_db() as conn:
            cursor = conn.cursor()
            cutoff_date = datetime.now().timestamp() - (timeframe_days * 24 * 3600)
            
            cursor.execute("""
                SELECT * FROM border_events
                WHERE region = ? AND timestamp >= ?
                ORDER BY timestamp DESC
            """, (region, cutoff_date))
            
            events = [dict(row) for row in cursor.fetchall()]
        
        # Analyze shift speed
        rapid_shifts = [e for e in events if e.get("shift_speed") == "rapid"]
        moderate_shifts = [e for e in events if e.get("shift_speed") == "moderate"]
        
        # Assess risk
        risk_level = self._assess_border_risk(events, rapid_shifts)
        
        return {
            "region": region,
            "timeframe_days": timeframe_days,
            "total_events": len(events),
            "rapid_shifts": len(rapid_shifts),
            "moderate_shifts": len(moderate_shifts),
            "events": events,
            "risk_level": risk_level.value,
            "assessment": self._generate_border_assessment(events, rapid_shifts, risk_level)
        }
    
    def detect_hostile_mapping(self, target_territory: str) -> List[Dict[str, Any]]:
        """
        Flag any data, textbooks, or official state maps that include
        target territory within foreign borders.
        
        These maps are a definitive barrier to established relations.
        """
        with get_geopolitical_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM hostile_mappings
                WHERE target_territory = ?
                ORDER BY timestamp DESC
            """, (target_territory,))
            
            mappings = [dict(row) for row in cursor.fetchall()]
        
        # Assess barrier level
        definitive_barriers = [m for m in mappings if m["barrier_level"] == "definitive"]
        
        return {
            "target_territory": target_territory,
            "total_mappings": len(mappings),
            "definitive_barriers": len(definitive_barriers),
            "mappings": mappings,
            "barrier_assessment": self._assess_mapping_barrier(definitive_barriers)
        }
    
    def analyze_help_seeking_paradox(self, region: str) -> Dict[str, Any]:
        """
        Identify instances where entities label a state as 'murderer' or 'enemy'
        while simultaneously requesting humanitarian aid, border openings, or protection.
        """
        with get_geopolitical_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM help_seeking_paradoxes
                WHERE region = ?
                ORDER BY timestamp DESC
            """, (region,))
            
            paradoxes = [dict(row) for row in cursor.fetchall()]
        
        # Assess paradox level
        high_paradoxes = [p for p in paradoxes if p["paradox_level"] == "high"]
        
        return {
            "region": region,
            "total_paradoxes": len(paradoxes),
            "high_paradoxes": len(high_paradoxes),
            "paradoxes": paradoxes,
            "assessment": self._assess_paradox_severity(high_paradoxes)
        }
    
    def assess_strategic_loyalty(self, entity: str) -> Dict[str, Any]:
        """
        Differentiate between 'loyal friends' who walk a common path
        and those who 'throw stones' while benefiting from shared resources.
        """
        with get_geopolitical_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM strategic_loyalty
                WHERE entity = ?
                ORDER BY timestamp DESC
                LIMIT 1
            """, (entity,))
            
            row = cursor.fetchone()
            if not row:
                return {
                    "entity": entity,
                    "status": "no_assessment",
                    "message": "No loyalty assessment found for this entity"
                }
            
            loyalty = dict(row)
        
        return {
            "entity": entity,
            "relationship_type": loyalty["relationship_type"],
            "common_path": bool(loyalty["common_path"]),
            "shared_resources": loyalty["shared_resources"].split(",") if loyalty["shared_resources"] else [],
            "assessment": loyalty["assessment"],
            "recommendation": self._generate_loyalty_recommendation(loyalty)
        }
    
    def record_border_event(
        self,
        region: str,
        border_point: str,
        event_type: str,
        description: str,
        control_status: Optional[str] = None,
        shift_speed: Optional[str] = None
    ) -> None:
        """Record a border event."""
        event = BorderEvent(
            region=region,
            border_point=border_point,
            event_type=event_type,
            timestamp=datetime.now(),
            description=description,
            control_status=control_status,
            shift_speed=shift_speed
        )
        
        with get_geopolitical_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO border_events (
                    region, border_point, event_type, timestamp,
                    description, control_status, shift_speed
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                event.region,
                event.border_point,
                event.event_type,
                event.timestamp.isoformat(),
                event.description,
                event.control_status,
                event.shift_speed
            ))
            conn.commit()
    
    def record_hostile_mapping(
        self,
        source: str,
        target_territory: str,
        claimed_by: str,
        document_type: str,
        description: str,
        barrier_level: str = "definitive"
    ) -> None:
        """Record a hostile mapping incident."""
        mapping = HostileMapping(
            source=source,
            target_territory=target_territory,
            claimed_by=claimed_by,
            document_type=document_type,
            timestamp=datetime.now(),
            description=description,
            barrier_level=barrier_level
        )
        
        with get_geopolitical_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO hostile_mappings (
                    source, target_territory, claimed_by, document_type,
                    timestamp, description, barrier_level
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                mapping.source,
                mapping.target_territory,
                mapping.claimed_by,
                mapping.document_type,
                mapping.timestamp.isoformat(),
                mapping.description,
                mapping.barrier_level
            ))
            conn.commit()
    
    def record_help_seeking_paradox(
        self,
        entity: str,
        region: str,
        hostile_label: str,
        aid_requested: str,
        description: str,
        paradox_level: str = "high"
    ) -> None:
        """Record a help-seeking paradox incident."""
        paradox = HelpSeekingParadox(
            entity=entity,
            region=region,
            hostile_label=hostile_label,
            aid_requested=aid_requested,
            timestamp=datetime.now(),
            description=description,
            paradox_level=paradox_level
        )
        
        with get_geopolitical_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO help_seeking_paradoxes (
                    entity, region, hostile_label, aid_requested,
                    timestamp, description, paradox_level
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                paradox.entity,
                paradox.region,
                paradox.hostile_label,
                paradox.aid_requested,
                paradox.timestamp.isoformat(),
                paradox.description,
                paradox.paradox_level
            ))
            conn.commit()
    
    def record_strategic_loyalty(
        self,
        entity: str,
        relationship_type: str,
        shared_resources: List[str],
        common_path: bool,
        assessment: str
    ) -> None:
        """Record a strategic loyalty assessment."""
        loyalty = StrategicLoyalty(
            entity=entity,
            relationship_type=relationship_type,
            shared_resources=shared_resources,
            common_path=common_path,
            timestamp=datetime.now(),
            assessment=assessment
        )
        
        with get_geopolitical_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO strategic_loyalty (
                    entity, relationship_type, shared_resources,
                    common_path, timestamp, assessment
                ) VALUES (?, ?, ?, ?, ?, ?)
            """, (
                loyalty.entity,
                loyalty.relationship_type,
                ",".join(loyalty.shared_resources),
                1 if loyalty.common_path else 0,
                loyalty.timestamp.isoformat(),
                loyalty.assessment
            ))
            conn.commit()
    
    def generate_comprehensive_analysis(self, region: str) -> Dict[str, Any]:
        """
        Generate comprehensive analysis for a region.
        Applies the Cengiz Han principle of sovereignty.
        """
        border_analysis = self.analyze_border_dynamics(region)
        hostile_mappings = self.detect_hostile_mapping(region)
        paradox_analysis = self.analyze_help_seeking_paradox(region)
        
        # Overall risk assessment
        risk_factors = []
        if border_analysis["risk_level"] in ["high", "critical"]:
            risk_factors.append("border_instability")
        if hostile_mappings["definitive_barriers"] > 0:
            risk_factors.append("hostile_mapping")
        if paradox_analysis["high_paradoxes"] > 0:
            risk_factors.append("help_seeking_paradox")
        
        overall_risk = self._calculate_overall_risk(risk_factors)
        
        # Generate recommendations based on Cengiz Han principle
        recommendations = self._generate_sovereignty_recommendations(
            region, border_analysis, hostile_mappings, paradox_analysis
        )
        
        # Store analysis result
        self._store_analysis_result(region, overall_risk, risk_factors, recommendations)
        
        return {
            "region": region,
            "analysis_timestamp": self.analysis_timestamp.isoformat(),
            "overall_risk": overall_risk.value,
            "risk_factors": risk_factors,
            "border_analysis": border_analysis,
            "hostile_mappings": hostile_mappings,
            "paradox_analysis": paradox_analysis,
            "recommendations": recommendations,
            "sovereignty_principle": "Cengiz Han: Personal items may be gifted, but not a single pebble of national land is negotiable"
        }
    
    def _assess_border_risk(
        self,
        events: List[Dict],
        rapid_shifts: List[Dict]
    ) -> RiskLevel:
        """Assess risk level based on border events."""
        if len(rapid_shifts) > 5:
            return RiskLevel.CRITICAL
        elif len(rapid_shifts) > 2 or len(events) > 10:
            return RiskLevel.HIGH
        elif len(events) > 5:
            return RiskLevel.MODERATE
        else:
            return RiskLevel.LOW
    
    def _generate_border_assessment(
        self,
        events: List[Dict],
        rapid_shifts: List[Dict],
        risk_level: RiskLevel
    ) -> str:
        """Generate border assessment."""
        if risk_level == RiskLevel.CRITICAL:
            return f"CRITICAL: {len(rapid_shifts)} rapid shifts detected. Field conditions changing extremely quickly."
        elif risk_level == RiskLevel.HIGH:
            return f"HIGH: {len(rapid_shifts)} rapid shifts. Border dynamics unstable."
        elif risk_level == RiskLevel.MODERATE:
            return f"MODERATE: {len(events)} events detected. Monitor closely."
        else:
            return f"LOW: {len(events)} events. Border dynamics relatively stable."
    
    def _assess_mapping_barrier(self, definitive_barriers: List[Dict]) -> str:
        """Assess barrier level from hostile mappings."""
        if len(definitive_barriers) > 0:
            return f"DEFINITIVE BARRIER: {len(definitive_barriers)} hostile mappings detected. These are definitive barriers to established relations."
        else:
            return "No definitive barriers detected."
    
    def _assess_paradox_severity(self, high_paradoxes: List[Dict]) -> str:
        """Assess severity of help-seeking paradoxes."""
        if len(high_paradoxes) > 0:
            return f"HIGH PARADOX: {len(high_paradoxes)} instances of entities labeling state as enemy while requesting aid."
        else:
            return "No high-level paradoxes detected."
    
    def _generate_loyalty_recommendation(self, loyalty: Dict) -> str:
        """Generate recommendation based on loyalty assessment."""
        if loyalty["relationship_type"] == "loyal_friend" and loyalty["common_path"]:
            return "Maintain relationship. Entity walks common path."
        elif loyalty["relationship_type"] == "stone_thrower":
            return "CAUTION: Entity throws stones while benefiting from shared resources. Reassess relationship."
        else:
            return "Monitor relationship. Assess alignment with common path."
    
    def _calculate_overall_risk(self, risk_factors: List[str]) -> RiskLevel:
        """Calculate overall risk level."""
        if len(risk_factors) >= 3:
            return RiskLevel.CRITICAL
        elif len(risk_factors) == 2:
            return RiskLevel.HIGH
        elif len(risk_factors) == 1:
            return RiskLevel.MODERATE
        else:
            return RiskLevel.LOW
    
    def _generate_sovereignty_recommendations(
        self,
        region: str,
        border_analysis: Dict,
        hostile_mappings: Dict,
        paradox_analysis: Dict
    ) -> List[str]:
        """Generate recommendations based on Cengiz Han principle."""
        recommendations = []
        
        # Border recommendations
        if border_analysis["risk_level"] in ["high", "critical"]:
            recommendations.append(
                f"Monitor {region} border dynamics closely. Rapid shifts indicate instability."
            )
        
        # Hostile mapping recommendations
        if hostile_mappings["definitive_barriers"] > 0:
            recommendations.append(
                "DEFINITIVE BARRIER: Hostile mappings detected. These are barriers to relations. "
                "Apply Cengiz Han principle: Not a single pebble of national land is negotiable."
            )
        
        # Paradox recommendations
        if paradox_analysis["high_paradoxes"] > 0:
            recommendations.append(
                "Help-seeking paradox detected. Entity labels state as enemy while requesting aid. "
                "Assess whether aid serves national interest or enables exploitation."
            )
        
        # Sovereignty principle
        recommendations.append(
            "Cengiz Han Principle: Personal items or resources may be gifted to maintain peace, "
            "but not a single pebble of national land or millet (nation) territory is negotiable."
        )
        
        return recommendations
    
    def _store_analysis_result(
        self,
        region: str,
        risk_level: RiskLevel,
        risk_factors: List[str],
        recommendations: List[str]
    ) -> None:
        """Store analysis result in database."""
        with get_geopolitical_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO analysis_results (
                    analysis_timestamp, region, conflict_type,
                    risk_level, findings, recommendations
                ) VALUES (?, ?, ?, ?, ?, ?)
            """, (
                self.analysis_timestamp.isoformat(),
                region,
                "comprehensive",
                risk_level.value,
                ", ".join(risk_factors),
                "\n".join(recommendations)
            ))
            conn.commit()


# Convenience function
def analyze_region(region: str) -> Dict[str, Any]:
    """
    Analyze a region comprehensively.
    """
    engine = GeopoliticalAnalysisEngine()
    return engine.generate_comprehensive_analysis(region)


# Example usage
if __name__ == "__main__":
    engine = GeopoliticalAnalysisEngine()
    
    # Example: Record a hostile mapping
    engine.record_hostile_mapping(
        source="Foreign State Textbook",
        target_territory="Hatay",
        claimed_by="Foreign State",
        document_type="textbook",
        description="Textbook includes Hatay within foreign borders",
        barrier_level="definitive"
    )
    
    # Example: Record a help-seeking paradox
    engine.record_help_seeking_paradox(
        entity="Entity X",
        region="Gaza",
        hostile_label="enemy",
        aid_requested="humanitarian aid, border opening",
        description="Entity labels state as enemy while requesting aid",
        paradox_level="high"
    )
    
    # Analyze region
    analysis = engine.generate_comprehensive_analysis("Gaza")
    
    print("=" * 60)
    print("GEOPOLITICAL ANALYSIS - COMPREHENSIVE")
    print("=" * 60)
    print()
    print(f"Region: {analysis['region']}")
    print(f"Overall Risk: {analysis['overall_risk']}")
    print(f"Risk Factors: {', '.join(analysis['risk_factors'])}")
    print()
    print("Recommendations:")
    for rec in analysis['recommendations']:
        print(f"  • {rec}")
    print()
    print("Sovereignty Principle:")
    print(f"  {analysis['sovereignty_principle']}")
    print("=" * 60)
