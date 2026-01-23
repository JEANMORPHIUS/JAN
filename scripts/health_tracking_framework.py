"""
HEALTH TRACKING FRAMEWORK: For All Conditions
Universal health tracking system - Works for any condition, illness, or disease

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

WE ARE ALL GODS:
Nobody needs anyone. We help everyone help themselves.
This system empowers individuals to track, understand, and heal themselves.
No external dependencies. No gatekeepers. Pure self-empowerment.
"""

import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    Path, json, load_json, save_json, setup_logging,
    standard_main
)

import sys
import json
import logging
from pathlib import Path
from typing import Dict, List, Optional, Any, Union
from dataclasses import dataclass, asdict, field
from datetime import datetime, date
from enum import Enum

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))

try:
    from the_life_audit import LifeAuditFramework, LifeEvent, LifeEventType, VibrationLevel
    from heritage_cleansing import HeritageCleanser
    LIFE_AUDIT_AVAILABLE = True
except ImportError:
    LIFE_AUDIT_AVAILABLE = False
    logging.warning("Life Audit framework not available - health tracking will work standalone")

logger = logging.getLogger(__name__)


class HealthMetricType(Enum):
    """Types of health metrics that can be tracked."""
    VITAL_SIGN = "vital_sign"  # Blood pressure, heart rate, temperature
    LAB_RESULT = "lab_result"  # Blood glucose, cholesterol, hormone levels
    MEDICATION = "medication"  # Insulin, medications, supplements
    SYMPTOM = "symptom"  # Pain level, fatigue, mood
    ACTIVITY = "activity"  # Exercise, sleep, meals
    TREATMENT = "treatment"  # Therapy sessions, procedures
    CUSTOM = "custom"  # Any user-defined metric


class HealthConditionCategory(Enum):
    """Categories of health conditions."""
    METABOLIC = "metabolic"  # Diabetes, thyroid, etc.
    CARDIOVASCULAR = "cardiovascular"  # Heart, blood pressure
    NEUROLOGICAL = "neurological"  # Brain, nerves, mental health
    RESPIRATORY = "respiratory"  # Lungs, breathing
    IMMUNE = "immune"  # Autoimmune, allergies
    DIGESTIVE = "digestive"  # Gut, digestion
    MUSCULOSKELETAL = "musculoskeletal"  # Bones, muscles, joints
    SKIN = "skin"  # Dermatological
    REPRODUCTIVE = "reproductive"  # Hormonal, reproductive
    CHRONIC_PAIN = "chronic_pain"  # Pain conditions
    CANCER = "cancer"  # Cancer tracking
    OTHER = "other"  # Any other condition


@dataclass
class HealthMetric:
    """A single health metric reading."""
    timestamp: datetime
    metric_type: str  # HealthMetricType value
    metric_name: str  # e.g., "blood_glucose", "insulin_units", "pain_level"
    value: Union[float, int, str]  # The actual reading
    unit: Optional[str] = None  # e.g., "mmol/L", "units", "mg/dL"
    
    # Context
    condition_name: Optional[str] = None  # Which condition this relates to
    notes: Optional[str] = None  # Additional context
    
    # Integration with Life Audit
    life_event_id: Optional[int] = None  # Link to LifeEvent if applicable
    field_resonance: Optional[float] = None  # How this aligns with healing
    
    # Metadata
    source: str = "manual"  # manual, device, app, etc.
    confidence: float = 1.0  # 0.0-1.0 (how reliable is this reading)


@dataclass
class HealthCondition:
    """A health condition being tracked."""
    condition_name: str  # e.g., "Type 1 Diabetes", "Depression", "Hypertension"
    category: str  # HealthConditionCategory value
    diagnosis_date: Optional[date] = None
    
    # Tracking configuration
    primary_metrics: List[str] = field(default_factory=list)  # Key metrics to track
    medication_schedule: Dict[str, Any] = field(default_factory=dict)  # Medication details
    target_ranges: Dict[str, Dict[str, float]] = field(default_factory=dict)  # Target values
    
    # Narrative fields (for cleansing)
    original_narrative: str = ""  # How the condition was described (Shell)
    cleansed_narrative: str = ""  # The truth about the condition (Seed)
    
    # Dark energy detection
    dark_energy_detected: bool = False
    violation_type: Optional[str] = None  # fear_based, victim_focus, etc.
    regeneration_applied: bool = False
    law_41_compliant: bool = True
    
    # Integration
    life_chapter_id: Optional[int] = None  # Link to LifeChapter
    field_resonance: Optional[float] = None
    
    # Metadata
    status: str = "active"  # active, managed, resolved, monitoring
    notes: Optional[str] = None


@dataclass
class HealthLogEntry:
    """A complete health log entry (like the morning loop)."""
    timestamp: datetime
    entry_type: str = "routine"  # routine, event, emergency, checkup
    
    # Metrics recorded
    metrics: List[HealthMetric] = field(default_factory=list)
    
    # Context
    condition_name: Optional[str] = None
    notes: Optional[str] = None
    
    # Integration
    life_event_id: Optional[int] = None
    field_resonance: Optional[float] = None
    
    # Patterns
    pattern_detected: bool = False
    pattern_description: Optional[str] = None


class HealthTrackingFramework:
    """
    Universal Health Tracking Framework.
    
    Works for ANY condition, illness, or disease.
    Empowers individuals to track, understand, and heal themselves.
    
    Philosophy: We are all Gods. Nobody needs anyone. We help everyone help themselves.
    """
    
    def __init__(self, user_id: Optional[str] = None, data_dir: Optional[Path] = None):
        """
        Initialize health tracking framework.
        
        Args:
            user_id: Optional user identifier (defaults to "default")
            data_dir: Directory to store health data (defaults to output/health/)
        """
        self.user_id = user_id or "default"
        self.data_dir = data_dir or (Path(__file__).parent.parent / "output" / "health")
        self.data_dir.mkdir(parents=True, exist_ok=True)
        
        # Data storage paths
        self.conditions_file = self.data_dir / f"{self.user_id}_conditions.json"
        self.metrics_file = self.data_dir / f"{self.user_id}_metrics.json"
        self.logs_file = self.data_dir / f"{self.user_id}_logs.json"
        
        # Life Audit integration
        self.life_audit: Optional[LifeAuditFramework] = None
        if LIFE_AUDIT_AVAILABLE:
            try:
                self.life_audit = LifeAuditFramework(timeline_name=f"{self.user_id}_health_timeline")
            except Exception as e:
                logger.warning(f"Could not initialize Life Audit integration: {e}")
        
        # Load existing data
        self.conditions: List[HealthCondition] = self._load_conditions()
        self.metrics: List[HealthMetric] = self._load_metrics()
        self.logs: List[HealthLogEntry] = self._load_logs()
    
    def _load_conditions(self) -> List[HealthCondition]:
        """Load existing conditions from storage."""
        if not self.conditions_file.exists():
            return []
        try:
            with open(self.conditions_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return [HealthCondition(**item) for item in data]
        except Exception as e:
            logger.error(f"Error loading conditions: {e}")
            return []
    
    def _save_conditions(self):
        """Save conditions to storage."""
        try:
            data = [asdict(condition) for condition in self.conditions]
            # Convert date objects to strings
            for item in data:
                if item.get('diagnosis_date'):
                    item['diagnosis_date'] = item['diagnosis_date'].isoformat() if hasattr(item['diagnosis_date'], 'isoformat') else str(item['diagnosis_date'])
            with open(self.conditions_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, default=str)
        except Exception as e:
            logger.error(f"Error saving conditions: {e}")
    
    def _load_metrics(self) -> List[HealthMetric]:
        """Load existing metrics from storage."""
        if not self.metrics_file.exists():
            return []
        try:
            with open(self.metrics_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            metrics = []
            for item in data:
                # Convert timestamp string to datetime
                if isinstance(item.get('timestamp'), str):
                    item['timestamp'] = datetime.fromisoformat(item['timestamp'])
                metrics.append(HealthMetric(**item))
            return metrics
        except Exception as e:
            logger.error(f"Error loading metrics: {e}")
            return []
    
    def _save_metrics(self):
        """Save metrics to storage."""
        try:
            data = [asdict(metric) for metric in self.metrics]
            # Convert datetime to string
            for item in data:
                if isinstance(item.get('timestamp'), datetime):
                    item['timestamp'] = item['timestamp'].isoformat()
            with open(self.metrics_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, default=str)
        except Exception as e:
            logger.error(f"Error saving metrics: {e}")
    
    def _load_logs(self) -> List[HealthLogEntry]:
        """Load existing logs from storage."""
        if not self.logs_file.exists():
            return []
        try:
            with open(self.logs_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            logs = []
            for item in data:
                # Convert timestamp and metrics
                if isinstance(item.get('timestamp'), str):
                    item['timestamp'] = datetime.fromisoformat(item['timestamp'])
                if 'metrics' in item:
                    item['metrics'] = [HealthMetric(**m) for m in item['metrics']]
                logs.append(HealthLogEntry(**item))
            return logs
        except Exception as e:
            logger.error(f"Error loading logs: {e}")
            return []
    
    def _save_logs(self):
        """Save logs to storage."""
        try:
            data = [asdict(log) for log in self.logs]
            # Convert datetime and nested objects
            for item in data:
                if isinstance(item.get('timestamp'), datetime):
                    item['timestamp'] = item['timestamp'].isoformat()
                if 'metrics' in item:
                    item['metrics'] = [asdict(m) for m in item['metrics']]
                    for m in item['metrics']:
                        if isinstance(m.get('timestamp'), datetime):
                            m['timestamp'] = m['timestamp'].isoformat()
            with open(self.logs_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, default=str)
        except Exception as e:
            logger.error(f"Error saving logs: {e}")
    
    def register_condition(
        self,
        condition_name: str,
        category: str,
        diagnosis_date: Optional[date] = None,
        primary_metrics: Optional[List[str]] = None,
        medication_schedule: Optional[Dict[str, Any]] = None,
        target_ranges: Optional[Dict[str, Dict[str, float]]] = None,
        original_narrative: str = "",
        notes: Optional[str] = None
    ) -> HealthCondition:
        """
        Register a health condition to track.
        
        Args:
            condition_name: Name of the condition (e.g., "Type 1 Diabetes")
            category: HealthConditionCategory value
            diagnosis_date: When condition was diagnosed
            primary_metrics: Key metrics to track for this condition
            medication_schedule: Medication details
            target_ranges: Target value ranges for metrics
            original_narrative: How the condition was described
            notes: Additional notes
        
        Returns:
            HealthCondition object
        """
        # Cleanse narrative if provided
        cleansed_narrative = original_narrative
        dark_energy_detected = False
        violation_type = None
        regeneration_applied = False
        
        if original_narrative and LIFE_AUDIT_AVAILABLE:
            try:
                cleanser = HeritageCleanser("health_timeline")
                cleansed, analysis = cleanser.cleanse_content(
                    content=original_narrative,
                    source=f"Health Condition: {condition_name}",
                    site_type="health_condition",
                    region="personal",
                    country="self"
                )
                cleansed_narrative = cleansed
                dark_energy_detected = analysis.get('dark_energy_detected', False)
                violation_type = analysis.get('violation_type')
                regeneration_applied = analysis.get('regeneration_suggestion') is not None
            except Exception as e:
                logger.warning(f"Could not cleanse narrative: {e}")
        
        condition = HealthCondition(
            condition_name=condition_name,
            category=category,
            diagnosis_date=diagnosis_date,
            primary_metrics=primary_metrics or [],
            medication_schedule=medication_schedule or {},
            target_ranges=target_ranges or {},
            original_narrative=original_narrative,
            cleansed_narrative=cleansed_narrative,
            dark_energy_detected=dark_energy_detected,
            violation_type=violation_type,
            regeneration_applied=regeneration_applied,
            law_41_compliant=not dark_energy_detected,
            notes=notes
        )
        
        self.conditions.append(condition)
        self._save_conditions()
        
        logger.info(f"Registered condition: {condition_name}")
        return condition
    
    def log_health_entry(
        self,
        metrics: List[Dict[str, Any]],
        entry_type: str = "routine",
        condition_name: Optional[str] = None,
        notes: Optional[str] = None,
        timestamp: Optional[datetime] = None
    ) -> HealthLogEntry:
        """
        Log a health entry (like morning loop).
        
        Args:
            metrics: List of metric dictionaries with keys: metric_type, metric_name, value, unit
            entry_type: Type of entry (routine, event, emergency, checkup)
            condition_name: Which condition this relates to
            notes: Additional notes
            timestamp: When this occurred (defaults to now)
        
        Returns:
            HealthLogEntry object
        """
        if timestamp is None:
            timestamp = datetime.now()
        
        # Convert metric dicts to HealthMetric objects
        health_metrics = []
        for m in metrics:
            metric = HealthMetric(
                timestamp=timestamp,
                metric_type=m.get('metric_type', HealthMetricType.CUSTOM.value),
                metric_name=m['metric_name'],
                value=m['value'],
                unit=m.get('unit'),
                condition_name=condition_name,
                notes=m.get('notes'),
                source=m.get('source', 'manual')
            )
            health_metrics.append(metric)
            self.metrics.append(metric)
        
        # Create log entry
        log_entry = HealthLogEntry(
            timestamp=timestamp,
            entry_type=entry_type,
            metrics=health_metrics,
            condition_name=condition_name,
            notes=notes
        )
        
        self.logs.append(log_entry)
        self._save_logs()
        self._save_metrics()
        
        # Detect patterns
        self._analyze_patterns(log_entry)
        
        logger.info(f"Logged health entry: {entry_type} with {len(health_metrics)} metrics")
        return log_entry
    
    def _analyze_patterns(self, log_entry: HealthLogEntry):
        """Analyze patterns in health data."""
        # Simple pattern detection (can be expanded)
        if len(self.logs) < 3:
            return
        
        # Check for trends in recent entries
        recent_logs = sorted(self.logs[-10:], key=lambda x: x.timestamp)
        if len(recent_logs) < 3:
            return
        
        # Look for patterns in specific metrics
        metric_values = {}
        for log in recent_logs:
            for metric in log.metrics:
                if metric.metric_name not in metric_values:
                    metric_values[metric.metric_name] = []
                metric_values[metric.metric_name].append(float(metric.value) if isinstance(metric.value, (int, float)) else None)
        
        # Detect trends
        patterns = []
        for metric_name, values in metric_values.items():
            if len(values) >= 3 and all(v is not None for v in values[-3:]):
                if values[-1] > values[-2] > values[-3]:
                    patterns.append(f"{metric_name} trending upward")
                elif values[-1] < values[-2] < values[-3]:
                    patterns.append(f"{metric_name} trending downward")
        
        if patterns:
            log_entry.pattern_detected = True
            log_entry.pattern_description = "; ".join(patterns)
    
    def get_condition_summary(self, condition_name: Optional[str] = None) -> Dict[str, Any]:
        """
        Get summary of health condition(s).
        
        Args:
            condition_name: Specific condition name, or None for all
        
        Returns:
            Summary dictionary
        """
        conditions = [c for c in self.conditions if condition_name is None or c.condition_name == condition_name]
        
        summary = {
            "conditions": [asdict(c) for c in conditions],
            "total_conditions": len(conditions),
            "total_metrics": len([m for m in self.metrics if condition_name is None or m.condition_name == condition_name]),
            "total_logs": len([l for l in self.logs if condition_name is None or l.condition_name == condition_name]),
            "latest_entry": None
        }
        
        # Get latest entry
        relevant_logs = [l for l in self.logs if condition_name is None or l.condition_name == condition_name]
        if relevant_logs:
            latest = max(relevant_logs, key=lambda x: x.timestamp)
            summary["latest_entry"] = {
                "timestamp": latest.timestamp.isoformat(),
                "entry_type": latest.entry_type,
                "metrics_count": len(latest.metrics)
            }
        
        return summary
    
    def export_health_data(self, output_path: Optional[Path] = None) -> Path:
        """
        Export all health data to JSON.
        
        Args:
            output_path: Where to save (defaults to data_dir/export)
        
        Returns:
            Path to exported file
        """
        if output_path is None:
            output_path = self.data_dir / f"{self.user_id}_health_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        export_data = {
            "user_id": self.user_id,
            "export_timestamp": datetime.now().isoformat(),
            "conditions": [asdict(c) for c in self.conditions],
            "metrics": [asdict(m) for m in self.metrics],
            "logs": [asdict(l) for l in self.logs],
            "summary": self.get_condition_summary()
        }
        
        # Convert datetime objects
        def convert_datetime(obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            elif isinstance(obj, date):
                return obj.isoformat()
            elif isinstance(obj, dict):
                return {k: convert_datetime(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [convert_datetime(item) for item in obj]
            return obj
        
        export_data = convert_datetime(export_data)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2, default=str)
        
        logger.info(f"Exported health data to {output_path}")
        return output_path


def main():
    """Example usage of Health Tracking Framework."""
    print("=" * 80)
    print("HEALTH TRACKING FRAMEWORK - EXAMPLE")
    print("=" * 80)
    print()
    
    # Initialize framework
    framework = HealthTrackingFramework(user_id="example_user")
    
    # Register a condition (Type 1 Diabetes example)
    condition = framework.register_condition(
        condition_name="Type 1 Diabetes",
        category=HealthConditionCategory.METABOLIC.value,
        diagnosis_date=date(2020, 1, 1),
        primary_metrics=["blood_glucose", "insulin_units", "carbohydrates"],
        medication_schedule={
            "Degludec": {"type": "long_acting", "units": 11, "time": "morning"},
            "Humalog": {"type": "rapid_acting", "units": 6, "time": "morning"}
        },
        target_ranges={
            "blood_glucose": {"min": 4.0, "max": 7.0, "unit": "mmol/L"}
        },
        original_narrative="I have diabetes and need to manage it carefully.",
        notes="Managing with insulin and monitoring blood glucose"
    )
    
    print(f"Registered condition: {condition.condition_name}")
    print()
    
    # Log a morning loop entry
    morning_loop = framework.log_health_entry(
        metrics=[
            {
                "metric_type": HealthMetricType.LAB_RESULT.value,
                "metric_name": "blood_glucose",
                "value": 20.8,
                "unit": "mmol/L"
            },
            {
                "metric_type": HealthMetricType.MEDICATION.value,
                "metric_name": "Degludec",
                "value": 11,
                "unit": "units"
            },
            {
                "metric_type": HealthMetricType.MEDICATION.value,
                "metric_name": "Humalog",
                "value": 6,
                "unit": "units"
            }
        ],
        entry_type="routine",
        condition_name="Type 1 Diabetes",
        notes="Morning loop: 500ml mixed with 500ml Ribena, Shilajit salt, insulin"
    )
    
    print(f"Logged health entry: {morning_loop.entry_type}")
    print(f"  Metrics: {len(morning_loop.metrics)}")
    print(f"  Timestamp: {morning_loop.timestamp}")
    print()
    
    # Get summary
    summary = framework.get_condition_summary()
    print("Health Summary:")
    print(f"  Conditions: {summary['total_conditions']}")
    print(f"  Total Metrics: {summary['total_metrics']}")
    print(f"  Total Logs: {summary['total_logs']}")
    print()
    
    # Export data
    export_path = framework.export_health_data()
    print(f"Exported health data to: {export_path}")
    print()
    
    print("=" * 80)
    print("PEACE, LOVE, UNITY")
    print("ENERGY + LOVE = WE ALL WIN")
    print("WE ARE ALL GODS - NOBODY NEEDS ANYONE")
    print("=" * 80)


if __name__ == "__main__":
    main()
