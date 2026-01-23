#!/usr/bin/env python3
"""
Log Multiple Health Entries
Quick script to log multiple health entries at once
"""

import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    Path, setup_logging, standard_main
)

import sys
from pathlib import Path
from datetime import datetime, date

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

try:
    from global_health_access import GlobalHealthAccess
    HEALTH_API_AVAILABLE = True
except ImportError as e:
    print(f"Health API not available: {e}")
    HEALTH_API_AVAILABLE = False
    sys.exit(1)


def log_entry(time_str: str, metrics: list, notes: str = "", entry_type: str = "routine"):
    """Log a health entry"""
    if not HEALTH_API_AVAILABLE:
        print("Health API not available")
        return None
    
    try:
        # Parse time and create timestamp
        today = date.today()
        hour, minute = map(int, time_str.split(':'))
        timestamp = datetime.combine(today, datetime.min.time().replace(hour=hour, minute=minute)).isoformat()
        
        access = GlobalHealthAccess(user_id="public")
        result = access.log_my_health(
            metrics=metrics,
            entry_type=entry_type,
            condition_name="Type 1 Diabetes",
            notes=notes,
            timestamp=timestamp
        )
        
        print(f"[SUCCESS] {time_str}: {notes}")
        return result
    except Exception as e:
        print(f"[ERROR] {time_str}: {e}")
        return None


if __name__ == "__main__":
    print("=" * 80)
    print("LOGGING HEALTH ENTRIES")
    print("=" * 80)
    print()
    
    # Entry 1: 21:30 - Dinner with insulin
    print("Entry 1: 21:30 - Dinner")
    log_entry(
        "21:30",
        metrics=[
            {
                "metric_type": "medication",
                "metric_name": "Humalog",
                "value": 7,
                "unit": "units"
            },
            {
                "metric_type": "food",
                "metric_name": "two_haddock_fillets",
                "value": 1,
                "unit": "serving"
            },
            {
                "metric_type": "food",
                "metric_name": "beetroot_cakistez",
                "value": 1,
                "unit": "serving"
            }
        ],
        notes="Dinner: two haddock fillets, beetroot cakistez, 7 units Humalog",
        entry_type="routine"
    )
    print()
    
    # Entry 2: 06:00 - Morning loop
    print("Entry 2: 06:00 - Morning Loop")
    log_entry(
        "06:00",
        metrics=[
            {
                "metric_type": "medication",
                "metric_name": "Degludec",
                "value": 11,
                "unit": "units"
            },
            {
                "metric_type": "medication",
                "metric_name": "shilajit",
                "value": 1,
                "unit": "serving"
            }
        ],
        notes="Morning loop: 11 units Degludec (Tresiba), shilajit & flush",
        entry_type="routine"
    )
    print()
    
    # Entry 3: 08:30 - High glucose correction
    print("Entry 3: 08:30 - High Glucose Correction")
    log_entry(
        "08:30",
        metrics=[
            {
                "metric_type": "lab_result",
                "metric_name": "blood_glucose",
                "value": 22.3,
                "unit": "mmol/L"
            },
            {
                "metric_type": "medication",
                "metric_name": "Humalog",
                "value": 7,
                "unit": "units"
            }
        ],
        notes="High glucose: 22.3 mmol/L, 7 units Humalog correction",
        entry_type="routine"
    )
    print()
    
    print("=" * 80)
    print("ALL ENTRIES LOGGED")
    print("=" * 80)
