"""
Quick T1D Health Entry Logger
Log Type 1 Diabetes entries with multiple insulin types

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity
"""

import sys
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    setup_logging, standard_main
)

from health_tracking_framework import (
    HealthTrackingFramework,
    HealthMetricType,
    HealthConditionCategory
)

logger = setup_logging(__name__)

def log_t1d_entry(
    time: str,
    blood_glucose: float,
    tresiba_units: float = 0.0,
    humalog_units: float = 0.0,
    notes: str = "",
    user_id: str = "jan"
):
    """Log a T1D health entry with both insulin types"""
    
    framework = HealthTrackingFramework(user_id=user_id)
    
    # Ensure Type 1 Diabetes condition is registered
    t1d_condition = None
    for condition in framework.conditions:
        if condition.condition_name == "Type 1 Diabetes":
            t1d_condition = condition
            break
    
    if not t1d_condition:
        t1d_condition = framework.register_condition(
            condition_name="Type 1 Diabetes",
            category=HealthConditionCategory.METABOLIC.value,
            primary_metrics=["blood_glucose", "tresiba", "humalog"],
            medication_schedule={
                "Tresiba": {"type": "long_acting", "units": tresiba_units, "time": "morning"},
                "Humalog": {"type": "rapid_acting", "units": humalog_units, "time": "morning"}
            },
            target_ranges={
                "blood_glucose": {"min": 4.0, "max": 7.0, "unit": "mmol/L"}
            },
            notes="Type 1 Diabetes management"
        )
        logger.info("Registered Type 1 Diabetes condition")
    
    # Parse time to datetime
    try:
        hour, minute = map(int, time.split(':'))
        timestamp = datetime.now().replace(hour=hour, minute=minute, second=0, microsecond=0)
        # If time is in the future (e.g., 07:00 when it's still early), assume previous day
        if timestamp > datetime.now():
            from datetime import timedelta
            timestamp = timestamp - timedelta(days=1)
    except:
        timestamp = datetime.now()
    
    # Build metrics
    metrics = [
        {
            "metric_type": HealthMetricType.LAB_RESULT.value,
            "metric_name": "blood_glucose",
            "value": blood_glucose,
            "unit": "mmol/L"
        }
    ]
    
    if tresiba_units > 0:
        metrics.append({
            "metric_type": HealthMetricType.MEDICATION.value,
            "metric_name": "Tresiba",
            "value": tresiba_units,
            "unit": "units"
        })
    
    if humalog_units > 0:
        metrics.append({
            "metric_type": HealthMetricType.MEDICATION.value,
            "metric_name": "Humalog",
            "value": humalog_units,
            "unit": "units"
        })
    
    # Build notes
    full_notes = f"{time} - BG: {blood_glucose} mmol/L"
    if tresiba_units > 0:
        full_notes += f", {tresiba_units}u Tresiba"
    if humalog_units > 0:
        full_notes += f", {humalog_units}u Humalog"
    if notes:
        full_notes += f" | {notes}"
    
    # Log entry
    entry = framework.log_health_entry(
        metrics=metrics,
        entry_type="routine",
        condition_name="Type 1 Diabetes",
        notes=full_notes,
        timestamp=timestamp
    )
    
    print(f"[SUCCESS] Health entry logged: {time}")
    print(f"   Blood Glucose: {blood_glucose} mmol/L")
    if tresiba_units > 0:
        print(f"   Tresiba: {tresiba_units} units")
    if humalog_units > 0:
        print(f"   Humalog: {humalog_units} units")
    if notes:
        print(f"   Notes: {notes}")
    print(f"   Entry ID: {entry.entry_id if hasattr(entry, 'entry_id') else 'N/A'}")
    
    return entry


def main():
    """Main function - log the current entry"""
    # Log the 07:00 entry
    log_t1d_entry(
        time="07:00",
        blood_glucose=28.8,
        tresiba_units=13.0,
        humalog_units=8.0,
        notes="Morning flush & shilajit, looping with various fluids",
        user_id="jan"
    )
    
    print("\n" + "="*80)
    print("Entry logged successfully!")
    print("="*80)

if __name__ == "__main__":
    standard_main(main, script_name="log_t1d_entry.py")
