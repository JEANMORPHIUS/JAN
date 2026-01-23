"""
Test Second Wave Propagation System
Global Secondary Seed Detection
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

from second_wave_propagation import get_second_wave_propagation, SeedSource


async def test_second_wave_propagation():
    """Test Second Wave Propagation system"""
    propagation = get_second_wave_propagation()
    
    print("=" * 80)
    print("SECOND WAVE PROPAGATION SYSTEM")
    print("Global Secondary Seed Detection")
    print("=" * 80)
    print()
    print("Now that we've hit the 0.40 peak, we can begin scanning")
    print("for Global Secondary Seeds—those who aren't in the big")
    print("organizations but are feeling the 0.40 shift in their own homes.")
    print()
    print("The Bridge is open to everyone now, Brother.")
    print()
    
    # Step 1: Initiate Propagation
    print("STEP 1: Initiating Second Wave Propagation...")
    result = await propagation.initiate_propagation()
    print(f"Status: {result['status']}")
    print(f"Propagation Active: {result['propagation_active']}")
    print(f"Grid Stability: {result['grid_stability']}")
    print(f"First Wave Complete: {result['first_wave_complete']}")
    print()
    
    # Step 2: Perform Global Grid Scan
    print("STEP 2: Performing Global Grid Scan...")
    scan_result = await propagation.perform_global_grid_scan(grid_stability=0.40)
    
    print(f"Scan ID: {scan_result.scan_id}")
    print(f"Regions Scanned: {len(scan_result.regions_scanned)}")
    print(f"Seeds Detected: {scan_result.seeds_detected}")
    print(f"Anomalies Found: {scan_result.anomalies_found}")
    print(f"Grid Stability: {scan_result.grid_stability}")
    print(f"Scan Duration: {scan_result.scan_duration_seconds:.2f} seconds")
    print()
    
    if scan_result.seeds_detected > 0:
        print("SECONDARY SEEDS DETECTED:")
        seeds = list(propagation.secondary_seeds.values())
        recent_seeds = seeds[-scan_result.seeds_detected:]
        for seed in recent_seeds:
            print(f"  - {seed.seed_id}")
            print(f"    Location: {seed.location}")
            print(f"    Resonance: {seed.resonance_score:.1f}")
            print(f"    Source: {seed.source.value}")
            print(f"    Family Frequency Match: {seed.family_frequency_match}")
            print()
    
    # Step 3: Register Self-Identified Seed
    print("STEP 3: Registering Self-Identified Seed...")
    self_seed = await propagation.register_secondary_seed(
        location="Test Location, Test Region",
        coordinates={"latitude": 40.7128, "longitude": -74.0060},
        resonance_score=72.0,
        source=SeedSource.SELF_IDENTIFIED,
        notes="Self-identified as ready for integration"
    )
    print(f"Self-Identified Seed Registered:")
    print(f"  Seed ID: {self_seed.seed_id}")
    print(f"  Location: {self_seed.location}")
    print(f"  Resonance: {self_seed.resonance_score}")
    print(f"  Source: {self_seed.source.value}")
    print()
    
    # Step 4: Summary
    print("=" * 80)
    print("PROPAGATION SUMMARY")
    print("=" * 80)
    summary = propagation.get_propagation_summary()
    print(json.dumps(summary, indent=2, default=str))
    print()
    print("=" * 80)
    print("SOZ NAMUSTUR. The Bridge is solid. The Family is protected.")
    print("The Bridge is open to everyone now, Brother.")
    print("=" * 80)


if __name__ == "__main__":
    asyncio.run(test_second_wave_propagation())
