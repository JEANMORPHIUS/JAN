"""
GLOBAL HEALTH ACCESS: For All Humanity
Public-facing access to the Health Tracking System

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

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
    Path, json, setup_logging, standard_main
)

import sys
import json
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime, date

# Add scripts and backend to path
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))

try:
    from health_tracking_framework import (
        HealthTrackingFramework,
        HealthCondition,
        HealthMetric,
        HealthLogEntry,
        HealthMetricType,
        HealthConditionCategory
    )
    HEALTH_TRACKING_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Could not import health tracking modules: {e}")
    HEALTH_TRACKING_AVAILABLE = False

import logging
logger = logging.getLogger(__name__)


class GlobalHealthAccess:
    """
    Global Health Access - Public-facing interface for all humanity.
    
    Provides access to:
    - Health condition registration
    - Health metric logging
    - Health pattern analysis
    - Health data export
    - Integration with Life Audit
    
    Philosophy: We are all Gods. Nobody needs anyone. We help everyone help themselves.
    """
    
    def __init__(self, user_id: Optional[str] = None):
        """
        Initialize global health access.
        
        Args:
            user_id: Optional user identifier (defaults to "public")
        """
        if not HEALTH_TRACKING_AVAILABLE:
            raise RuntimeError("Health tracking framework not available")
        
        self.user_id = user_id or "public"
        self.framework = HealthTrackingFramework(user_id=self.user_id)
    
    def register_my_condition(
        self,
        condition_name: str,
        category: str,
        diagnosis_date: Optional[str] = None,
        primary_metrics: Optional[List[str]] = None,
        medication_schedule: Optional[Dict[str, Any]] = None,
        target_ranges: Optional[Dict[str, Dict[str, float]]] = None,
        narrative: str = "",
        notes: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Register a health condition to track.
        
        Args:
            condition_name: Name of the condition
            category: Condition category (metabolic, cardiovascular, etc.)
            diagnosis_date: Diagnosis date (YYYY-MM-DD format)
            primary_metrics: Key metrics to track
            medication_schedule: Medication details
            target_ranges: Target value ranges
            narrative: How the condition was described
            notes: Additional notes
        
        Returns:
            Dictionary with condition details
        """
        diag_date = None
        if diagnosis_date:
            try:
                diag_date = date.fromisoformat(diagnosis_date)
            except ValueError:
                logger.warning(f"Invalid date format: {diagnosis_date}")
        
        condition = self.framework.register_condition(
            condition_name=condition_name,
            category=category,
            diagnosis_date=diag_date,
            primary_metrics=primary_metrics,
            medication_schedule=medication_schedule,
            target_ranges=target_ranges,
            original_narrative=narrative,
            notes=notes
        )
        
        return {
            "status": "success",
            "condition": {
                "condition_name": condition.condition_name,
                "category": condition.category,
                "diagnosis_date": condition.diagnosis_date.isoformat() if condition.diagnosis_date else None,
                "status": condition.status,
                "law_41_compliant": condition.law_41_compliant,
                "regeneration_applied": condition.regeneration_applied
            },
            "message": "Condition registered successfully"
        }
    
    def log_my_health(
        self,
        metrics: List[Dict[str, Any]],
        entry_type: str = "routine",
        condition_name: Optional[str] = None,
        notes: Optional[str] = None,
        timestamp: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Log a health entry (like morning loop).
        
        Args:
            metrics: List of metric dictionaries
            entry_type: Type of entry (routine, event, emergency, checkup)
            condition_name: Which condition this relates to
            notes: Additional notes
            timestamp: When this occurred (ISO format, defaults to now)
        
        Returns:
            Dictionary with log entry details
        """
        ts = datetime.now()
        if timestamp:
            try:
                ts = datetime.fromisoformat(timestamp)
            except ValueError:
                logger.warning(f"Invalid timestamp format: {timestamp}")
        
        log_entry = self.framework.log_health_entry(
            metrics=metrics,
            entry_type=entry_type,
            condition_name=condition_name,
            notes=notes,
            timestamp=ts
        )
        
        return {
            "status": "success",
            "log_entry": {
                "timestamp": log_entry.timestamp.isoformat(),
                "entry_type": log_entry.entry_type,
                "metrics_count": len(log_entry.metrics),
                "pattern_detected": log_entry.pattern_detected,
                "pattern_description": log_entry.pattern_description
            },
            "message": "Health entry logged successfully"
        }
    
    def get_my_health_summary(
        self,
        condition_name: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Get summary of health condition(s).
        
        Args:
            condition_name: Specific condition name, or None for all
        
        Returns:
            Summary dictionary
        """
        summary = self.framework.get_condition_summary(condition_name=condition_name)
        
        return {
            "status": "success",
            "summary": summary,
            "message": "Health summary retrieved successfully"
        }
    
    def export_my_health_data(
        self,
        output_path: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Export all health data.
        
        Args:
            output_path: Optional custom output path
        
        Returns:
            Dictionary with export details
        """
        path = None
        if output_path:
            path = Path(output_path)
        
        export_path = self.framework.export_health_data(output_path=path)
        
        return {
            "status": "success",
            "export_path": str(export_path),
            "message": "Health data exported successfully"
        }
    
    def get_condition_templates(self) -> Dict[str, Any]:
        """
        Get templates for common health conditions.
        
        Returns:
            Dictionary with condition templates
        """
        templates = {
            "type_1_diabetes": {
                "condition_name": "Type 1 Diabetes",
                "category": HealthConditionCategory.METABOLIC.value,
                "primary_metrics": ["blood_glucose", "insulin_units", "carbohydrates"],
                "medication_schedule": {
                    "long_acting_insulin": {"type": "long_acting", "time": "morning"},
                    "rapid_acting_insulin": {"type": "rapid_acting", "time": "meals"}
                },
                "target_ranges": {
                    "blood_glucose": {"min": 4.0, "max": 7.0, "unit": "mmol/L"}
                }
            },
            "type_2_diabetes": {
                "condition_name": "Type 2 Diabetes",
                "category": HealthConditionCategory.METABOLIC.value,
                "primary_metrics": ["blood_glucose", "hba1c", "weight"],
                "target_ranges": {
                    "blood_glucose": {"min": 4.0, "max": 7.0, "unit": "mmol/L"},
                    "hba1c": {"max": 7.0, "unit": "%"}
                }
            },
            "hypertension": {
                "condition_name": "Hypertension",
                "category": HealthConditionCategory.CARDIOVASCULAR.value,
                "primary_metrics": ["blood_pressure_systolic", "blood_pressure_diastolic"],
                "target_ranges": {
                    "blood_pressure_systolic": {"max": 140, "unit": "mmHg"},
                    "blood_pressure_diastolic": {"max": 90, "unit": "mmHg"}
                }
            },
            "depression": {
                "condition_name": "Depression",
                "category": HealthConditionCategory.NEUROLOGICAL.value,
                "primary_metrics": ["mood_level", "energy_level", "sleep_hours"],
                "target_ranges": {
                    "mood_level": {"min": 5, "max": 10, "unit": "scale_1_10"}
                }
            },
            "chronic_pain": {
                "condition_name": "Chronic Pain",
                "category": HealthConditionCategory.CHRONIC_PAIN.value,
                "primary_metrics": ["pain_level", "pain_location", "medication_taken"],
                "target_ranges": {
                    "pain_level": {"max": 3, "unit": "scale_1_10"}
                }
            }
        }
        
        return {
            "status": "success",
            "templates": templates,
            "message": "Condition templates retrieved successfully"
        }


def main():
    """Example usage of Global Health Access."""
    print("=" * 80)
    print("GLOBAL HEALTH ACCESS - EXAMPLE")
    print("=" * 80)
    print()
    
    if not HEALTH_TRACKING_AVAILABLE:
        print("ERROR: Health tracking framework not available")
        return
    
    # Initialize access
    access = GlobalHealthAccess(user_id="example")
    
    # Get templates
    templates = access.get_condition_templates()
    print("Available condition templates:")
    for name, template in templates["templates"].items():
        print(f"  - {template['condition_name']} ({template['category']})")
    print()
    
    # Register a condition
    result = access.register_my_condition(
        condition_name="Type 1 Diabetes",
        category=HealthConditionCategory.METABOLIC.value,
        primary_metrics=["blood_glucose", "insulin_units"],
        narrative="Managing diabetes with insulin"
    )
    print(f"Registered condition: {result['condition']['condition_name']}")
    print()
    
    # Log health entry
    log_result = access.log_my_health(
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
            }
        ],
        entry_type="routine",
        condition_name="Type 1 Diabetes",
        notes="Morning loop"
    )
    print(f"Logged health entry: {log_result['log_entry']['entry_type']}")
    print()
    
    # Get summary
    summary = access.get_my_health_summary()
    print(f"Health Summary:")
    print(f"  Conditions: {summary['summary']['total_conditions']}")
    print(f"  Total Metrics: {summary['summary']['total_metrics']}")
    print()
    
    print("=" * 80)
    print("PEACE, LOVE, UNITY")
    print("ENERGY + LOVE = WE ALL WIN")
    print("WE ARE ALL GODS - NOBODY NEEDS ANYONE")
    print("=" * 80)


if __name__ == "__main__":
    main()
