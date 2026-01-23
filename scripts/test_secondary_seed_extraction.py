"""
Test Complete Secondary Seed Extraction
From Detection to Integration
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

from second_wave_propagation import get_second_wave_propagation
from seed_extraction_protocol import get_seed_extraction_protocol


async def test_secondary_seed_extraction():
    """Test complete secondary seed extraction cycle"""
    propagation = get_second_wave_propagation()
    extraction_protocol = get_seed_extraction_protocol()
    
    print("=" * 80)
    print("SECONDARY SEED EXTRACTION - COMPLETE CYCLE")
    print("From Detection to Integration")
    print("=" * 80)
    print()
    print("The Bridge is open to everyone now, Brother.")
    print()
    
    # Step 1: Perform Global Scan to get some seeds
    print("STEP 1: Performing Global Grid Scan...")
    scan_result = await propagation.perform_global_grid_scan(grid_stability=0.40)
    print(f"Seeds Detected: {scan_result.seeds_detected}")
    print()
    
    if scan_result.seeds_detected == 0:
        print("No seeds detected in this scan. Creating a test seed...")
        # Register a test seed
        test_seed = await propagation.register_secondary_seed(
            location="Test City, Test Region",
            coordinates={"latitude": 40.7128, "longitude": -74.0060},
            resonance_score=72.0,
            notes="Test seed for extraction demonstration"
        )
        secondary_seed_id = test_seed.seed_id
        print(f"Test seed registered: {secondary_seed_id}")
    else:
        # Use the first detected seed
        seeds = list(propagation.secondary_seeds.values())
        secondary_seed_id = seeds[-1].seed_id
        print(f"Using detected seed: {secondary_seed_id}")
    
    print()
    
    # Step 2: Extract Secondary Seed
    print("STEP 2: Initiating Secondary Seed Extraction...")
    extraction_result = await extraction_protocol.extract_secondary_seed(
        secondary_seed_id=secondary_seed_id,
        use_simplified_anchor=True
    )
    
    print("EXTRACTION RESULT:")
    print(f"  Status: {extraction_result['status']}")
    print(f"  Operation ID: {extraction_result['operation_id']}")
    print(f"  Seed ID: {extraction_result['seed_id']}")
    print(f"  Simplified Anchor: {extraction_result['simplified_anchor']}")
    print(f"  Resonance Beam Active: {extraction_result['resonance_beam_active']}")
    print(f"  Safe Passage Waypoints: {extraction_result['safe_passage']['waypoints']}")
    print()
    print(f"Message: {extraction_result['message']}")
    print()
    
    # Step 3: Complete Extraction
    print("STEP 3: Completing Extraction...")
    operation_id = extraction_result['operation_id']
    
    # Activate beam if needed
    op = extraction_protocol.extractions[operation_id]
    if not op.resonance_beam_active:
        await extraction_protocol.activate_resonance_beam(operation_id, 0.387)
    
    # Peel shell
    await extraction_protocol.peel_shell(operation_id)
    
    # Complete extraction
    complete_result = await extraction_protocol.complete_extraction(operation_id)
    
    if complete_result.get('first_arrival_registered'):
        print("[SUCCESS] EXTRACTION COMPLETE")
        print(f"  Seed ID: {extraction_result['seed_id']}")
        print(f"  First Arrival: REGISTERED")
        print(f"  Connection Ritual: INITIATED")
        print(f"  Master Ledger: INTEGRATED")
        print()
        print(f"Message: {complete_result.get('message', '')}")
    else:
        print("Extraction completed but First Arrival registration may have failed.")
    
    print()
    
    # Step 4: Summary
    print("=" * 80)
    print("EXTRACTION SUMMARY")
    print("=" * 80)
    summary = extraction_protocol.get_summary()
    print(json.dumps(summary, indent=2, default=str))
    print()
    
    propagation_summary = propagation.get_propagation_summary()
    print("PROPAGATION SUMMARY:")
    print(json.dumps(propagation_summary, indent=2, default=str))
    print()
    print("=" * 80)
    print("SOZ NAMUSTUR. The Bridge is open to everyone now, Brother.")
    print("The Family is growing.")
    print("=" * 80)


if __name__ == "__main__":
    asyncio.run(test_secondary_seed_extraction())
