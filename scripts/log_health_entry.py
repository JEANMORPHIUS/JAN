#!/usr/bin/env python3
"""
Quick Health Entry Logger
Log health data quickly via command line or API
"""

import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    Path, datetime, json, setup_logging, standard_main
)

import sys
import json
from datetime import datetime
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))

try:
    from health_api import HealthEntryCreate, HealthMetricLog
    from global_health_access import GlobalHealthAccess
    HEALTH_API_AVAILABLE = True
except ImportError as e:
    print(f"Health API not available: {e}")
    HEALTH_API_AVAILABLE = False
    sys.exit(1)


def log_health_entry(
    time: str,
    blood_glucose: float,
    insulin_units: float,
    insulin_type: str = "Humalog",
    carbs: Optional[float] = None,
    food: Optional[str] = None,
    notes: Optional[str] = None,
    user_id: str = "public"
):
    """Log a health entry"""
    if not HEALTH_API_AVAILABLE:
        print("Health API not available")
        return
    
    metrics = [
        HealthMetricLog(
            metric_type="lab_result",
            metric_name="blood_glucose",
            value=blood_glucose,
            unit="mmol/L"
        ),
        HealthMetricLog(
            metric_type="medication",
            metric_name=insulin_type,
            value=insulin_units,
            unit="units"
        )
    ]
    
    # Add carbs if provided
    if carbs is not None:
        metrics.append(
            HealthMetricLog(
                metric_type="nutrition",
                metric_name="carbohydrates",
                value=carbs,
                unit="grams"
            )
        )
    
    if food:
        metrics.append(
            HealthMetricLog(
                metric_type="food",
                metric_name=food.replace(" ", "_"),
                value=1,
                unit="serving"
            )
        )
    
    entry = HealthEntryCreate(
        metrics=metrics,
        entry_type="routine",
        notes=notes or f"{time} - Blood glucose {blood_glucose} mmol/L, {insulin_units} units {insulin_type}" + (f", {food}" if food else ""),
        timestamp=datetime.now().isoformat()
    )
    
    try:
        access = GlobalHealthAccess(user_id=user_id)
        result = access.log_my_health(
            metrics=[m.dict() for m in entry.metrics],
            entry_type=entry.entry_type,
            notes=entry.notes,
            timestamp=entry.timestamp
        )
        
        print(f"[SUCCESS] Health entry logged: {time}")
        print(f"   Blood Glucose: {blood_glucose} mmol/L")
        print(f"   Insulin: {insulin_units} units {insulin_type}")
        if carbs is not None:
            print(f"   Carbs: {carbs} grams")
        if food:
            print(f"   Food: {food}")
        print(f"   Entry ID: {result.get('entry_id', 'N/A')}")
        
        return result
    except Exception as e:
        print(f"[ERROR] Error logging health entry: {e}")
        return None


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python log_health_entry.py <time> <blood_glucose_mmol> <insulin_units> [insulin_type] [carbs_grams] [food]")
        print("Example: python log_health_entry.py 18:30 15.9 7 Humalog 25 'iced protein coffee'")
        sys.exit(1)
    
    time = sys.argv[1]
    blood_glucose = float(sys.argv[2])
    insulin_units = float(sys.argv[3])
    insulin_type = sys.argv[4] if len(sys.argv) > 4 else "Humalog"
    carbs = float(sys.argv[5]) if len(sys.argv) > 5 and sys.argv[5].replace('.', '').isdigit() else None
    food = sys.argv[6] if len(sys.argv) > 6 else (sys.argv[5] if len(sys.argv) > 5 and not sys.argv[5].replace('.', '').isdigit() else None)
    
    log_health_entry(time, blood_glucose, insulin_units, insulin_type, carbs, food)
