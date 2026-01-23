#!/usr/bin/env python3
"""
Test Pulse System
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))

from pulse_system import get_pulse_system

def main():
    pulse = get_pulse_system()
    overview = pulse.get_pulse_overview()
    
    print(f"Pulse System initialized: {overview['overview']['total_systems']} systems")
    print(f"Healthy: {overview['overview']['healthy']}")
    print(f"Total Opportunities: {overview['overview']['total_opportunities']}")
    print(f"Average Frequency: {overview['overview']['avg_frequency']:.2f}")
    
    print("\nSystems:")
    for system_id, system_data in overview['systems'].items():
        print(f"  {system_id}: {system_data['status']} (Frequency: {system_data['frequency_score']:.2f})")

if __name__ == "__main__":
    main()
