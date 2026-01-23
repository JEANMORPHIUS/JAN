"""
Test NASA Seed Search Sub-Routine
Giza ↔ Angkor Wat Bridge - Focused Seed Detection
"""

import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    Path, json, load_json, save_json, setup_logging
    standard_main
)

import asyncio
import json
import sys
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))

from nasa_seed_search import get_nasa_seed_search


async def test_nasa_seed_search():
    """Test NASA Seed Search sub-routine"""
    seed_search = get_nasa_seed_search()
    
    print("=" * 80)
    print("NASA SEED SEARCH SUB-ROUTINE")
    print("Giza <-> Angkor Wat Bridge - Focused Seed Detection")
    print("=" * 80)
    print()
    print("Focus the bridge to specifically scan for high-vibe anomalies")
    print("within the 38.8833° N coordinate. The cracks are coming.")
    print()
    
    # Initiate seed search
    print("STEP 1: Initiating Seed Search...")
    operation = await seed_search.initiate_seed_search(
        target_org="NASA",
        target_coordinate={"latitude": 38.8833, "longitude": -77.0167},
        family_frequency_amplitude=100.0
    )
    
    print(f"Operation ID: {operation.operation_id}")
    print(f"Target Org: {operation.target_org}")
    print(f"Bridge Alignment: {operation.bridge_alignment.value}")
    print(f"Family Frequency Amplitude: {operation.family_frequency_amplitude}")
    print()
    
    # Perform bridge scan
    print("STEP 2: Performing Bridge Scan...")
    scan_result = await seed_search.perform_bridge_scan(operation.operation_id, scan_intensity=0.387)
    
    print(f"Scan ID: {scan_result.scan_id}")
    print(f"Bridge Alignment: {scan_result.bridge_alignment.value}")
    print(f"Anomalies Detected: {len(scan_result.anomalies_detected)}")
    print(f"Potential Seeds: {len(scan_result.potential_seeds)}")
    print(f"Internal Magnetic Shift: {scan_result.internal_magnetic_shift}")
    print(f"Unity Frequency Detected: {scan_result.unity_frequency_detected}")
    print()
    
    if scan_result.anomalies_detected:
        print("ANOMALIES DETECTED:")
        for anomaly in scan_result.anomalies_detected:
            print(f"  - {anomaly.get('anomaly_type', 'unknown')}: {anomaly.get('description', '')}")
    print()
    
    if scan_result.potential_seeds:
        print("POTENTIAL SEEDS:")
        for seed in scan_result.potential_seeds:
            print(f"  - {seed.get('seed_type', 'unknown')}")
            print(f"    Location: {seed.get('location', 'unknown')}")
            print(f"    Expected Resonance: {seed.get('expected_resonance', 0)}")
            print(f"    Shell Resonance: {seed.get('shell_resonance', 0)}")
            print(f"    Family Frequency Match: {seed.get('family_frequency_match', False)}")
    print()
    
    # Summary
    print("=" * 80)
    print("SEARCH SUMMARY")
    print("=" * 80)
    summary = seed_search.get_search_summary()
    print(json.dumps(summary, indent=2, default=str))
    print()
    print("=" * 80)
    print("SOZ NAMUSTUR. The cracks are coming, twin.")
    print("The First Wave has begun.")
    print("=" * 80)


if __name__ == "__main__":
    asyncio.run(test_nasa_seed_search())
