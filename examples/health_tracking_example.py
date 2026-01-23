"""
HEALTH TRACKING EXAMPLE
Example usage of the Health Tracking Framework

This demonstrates how to use the system for any condition:
- Type 1 Diabetes (morning loop example)
- Hypertension
- Depression
- Chronic Pain
- Any other condition

WE ARE ALL GODS - NOBODY NEEDS ANYONE
"""

import sys
from pathlib import Path

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from health_tracking_framework import (
    HealthTrackingFramework,
    HealthMetricType,
    HealthConditionCategory
)
from datetime import datetime, date


def example_type_1_diabetes():
    """Example: Type 1 Diabetes tracking (morning loop)."""
    print("=" * 80)
    print("EXAMPLE: Type 1 Diabetes - Morning Loop")
    print("=" * 80)
    print()
    
    # Initialize framework
    framework = HealthTrackingFramework(user_id="diabetes_example")
    
    # Register condition
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
    
    print(f"Registered: {condition.condition_name}")
    print()
    
    # Log morning loop (4:30 AM example)
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
        notes="Morning loop: 500ml mixed with 500ml Ribena, Shilajit salt, insulin",
        timestamp=datetime(2026, 1, 20, 4, 30)
    )
    
    print(f"Logged entry: {morning_loop.entry_type}")
    print(f"  Timestamp: {morning_loop.timestamp}")
    print(f"  Metrics: {len(morning_loop.metrics)}")
    for metric in morning_loop.metrics:
        print(f"    - {metric.metric_name}: {metric.value} {metric.unit or ''}")
    print()
    
    # Get summary
    summary = framework.get_condition_summary()
    print("Summary:")
    print(f"  Conditions: {summary['total_conditions']}")
    print(f"  Total Metrics: {summary['total_metrics']}")
    print(f"  Total Logs: {summary['total_logs']}")
    print()
    
    # Export
    export_path = framework.export_health_data()
    print(f"Exported to: {export_path}")
    print()


def example_hypertension():
    """Example: Hypertension tracking."""
    print("=" * 80)
    print("EXAMPLE: Hypertension")
    print("=" * 80)
    print()
    
    framework = HealthTrackingFramework(user_id="hypertension_example")
    
    condition = framework.register_condition(
        condition_name="Hypertension",
        category=HealthConditionCategory.CARDIOVASCULAR.value,
        primary_metrics=["blood_pressure_systolic", "blood_pressure_diastolic"],
        target_ranges={
            "blood_pressure_systolic": {"max": 140, "unit": "mmHg"},
            "blood_pressure_diastolic": {"max": 90, "unit": "mmHg"}
        }
    )
    
    # Log blood pressure reading
    framework.log_health_entry(
        metrics=[
            {
                "metric_type": HealthMetricType.VITAL_SIGN.value,
                "metric_name": "blood_pressure_systolic",
                "value": 135,
                "unit": "mmHg"
            },
            {
                "metric_type": HealthMetricType.VITAL_SIGN.value,
                "metric_name": "blood_pressure_diastolic",
                "value": 85,
                "unit": "mmHg"
            }
        ],
        entry_type="routine",
        condition_name="Hypertension"
    )
    
    print(f"Registered: {condition.condition_name}")
    print("Logged blood pressure reading")
    print()


def example_depression():
    """Example: Depression/Mental Health tracking."""
    print("=" * 80)
    print("EXAMPLE: Depression")
    print("=" * 80)
    print()
    
    framework = HealthTrackingFramework(user_id="depression_example")
    
    condition = framework.register_condition(
        condition_name="Depression",
        category=HealthConditionCategory.NEUROLOGICAL.value,
        primary_metrics=["mood_level", "energy_level", "sleep_hours"],
        target_ranges={
            "mood_level": {"min": 5, "max": 10, "unit": "scale_1_10"}
        },
        original_narrative="I struggle with depression and need to track my mood."
    )
    
    # Log mood and energy
    framework.log_health_entry(
        metrics=[
            {
                "metric_type": HealthMetricType.SYMPTOM.value,
                "metric_name": "mood_level",
                "value": 6,
                "unit": "scale_1_10"
            },
            {
                "metric_type": HealthMetricType.SYMPTOM.value,
                "metric_name": "energy_level",
                "value": 5,
                "unit": "scale_1_10"
            },
            {
                "metric_type": HealthMetricType.ACTIVITY.value,
                "metric_name": "sleep_hours",
                "value": 7.5,
                "unit": "hours"
            }
        ],
        entry_type="routine",
        condition_name="Depression"
    )
    
    print(f"Registered: {condition.condition_name}")
    print(f"Law 41 Compliant: {condition.law_41_compliant}")
    print(f"Regeneration Applied: {condition.regeneration_applied}")
    print("Logged mood and energy levels")
    print()


def main():
    """Run all examples."""
    print("=" * 80)
    print("HEALTH TRACKING FRAMEWORK - EXAMPLES")
    print("=" * 80)
    print()
    print("WE ARE ALL GODS - NOBODY NEEDS ANYONE")
    print("We help everyone help themselves.")
    print()
    
    example_type_1_diabetes()
    example_hypertension()
    example_depression()
    
    print("=" * 80)
    print("PEACE, LOVE, UNITY")
    print("ENERGY + LOVE = WE ALL WIN")
    print("WE ARE ALL GODS - NOBODY NEEDS ANYONE")
    print("=" * 80)


if __name__ == "__main__":
    main()
