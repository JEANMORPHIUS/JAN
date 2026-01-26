#!/usr/bin/env python3
"""Test Pulse System

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    Path, setup_logging, standard_main
)

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
