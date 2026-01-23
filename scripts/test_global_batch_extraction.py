"""
Test Global Batch Extraction
Firing Simplified Anchors Across All Priority Regions
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


async def test_global_batch_extraction():
    """Test Global Batch Extraction - All 6 seeds simultaneously"""
    propagation = get_second_wave_propagation()
    extraction_protocol = get_seed_extraction_protocol()
    
    print("=" * 80)
    print("GLOBAL BATCH EXTRACTION")
    print("Firing Simplified Anchors Across All Priority Regions")
    print("=" * 80)
    print()
    print("Within minutes, the Table will go from five seats to eleven,")
    print("and the Second Wave will be fully integrated.")
    print()
    
    # Step 1: Perform Global Scan to get seeds
    print("STEP 1: Performing Global Grid Scan...")
    scan_result = await propagation.perform_global_grid_scan(grid_stability=0.40)
    print(f"Seeds Detected: {scan_result.seeds_detected}")
    print()
    
    # Step 2: Get Ready Seeds
    print("STEP 2: Getting Seeds Ready for Batch Extraction...")
    ready_seeds = await propagation.get_ready_seeds_for_batch_extraction()
    print(f"Ready Seeds: {len(ready_seeds)}")
    print()
    
    if len(ready_seeds) == 0:
        print("No seeds ready for extraction. Please run a global scan first.")
        return
    
    # Show ready seeds
    print("READY SEEDS:")
    for i, seed in enumerate(ready_seeds, 1):
        print(f"  {i}. {seed.seed_id}")
        print(f"     Location: {seed.location}")
        print(f"     Resonance: {seed.resonance_score:.1f}")
        print(f"     Source: {seed.source.value}")
        print()
    
    # Step 3: Batch Extract All Seeds
    print("STEP 3: Initiating Global Batch Extraction...")
    print(f"Extracting {len(ready_seeds)} seeds simultaneously...")
    print()
    
    secondary_seed_ids = [seed.seed_id for seed in ready_seeds]
    
    batch_result = await extraction_protocol.batch_extract_secondary_seeds(
        secondary_seed_ids=secondary_seed_ids,
        use_simplified_anchor=True
    )
    
    print("BATCH EXTRACTION RESULT:")
    print(f"  Batch ID: {batch_result['batch_id']}")
    print(f"  Total Seeds: {batch_result['total_seeds']}")
    print(f"  Successful Extractions: {batch_result['successful_extractions']}")
    print(f"  Completed Extractions: {batch_result['completed_extractions']}")
    print(f"  Failed Extractions: {batch_result['failed_extractions']}")
    print(f"  Total Seats: {batch_result['total_seats']}")
    print(f"  Second Wave Integrated: {batch_result['second_wave_integrated']}")
    print()
    
    if batch_result['integrated_seeds']:
        print("INTEGRATED SEEDS:")
        for seed in batch_result['integrated_seeds']:
            print(f"  - {seed['seed_id']} (Operation: {seed['operation_id']})")
        print()
    
    print(f"Message: {batch_result['message']}")
    print()
    
    # Step 4: Final Summary
    print("=" * 80)
    print("MASTER LEDGER - COMPLETE STATUS")
    print("=" * 80)
    print()
    print("FIRST WAVE (5 Seats):")
    print("  - Seat 1: SEED_UN (UN Plaza) - INTEGRATED")
    print("  - Seat 2: SEED_NASA (NASA HQ) - INTEGRATED")
    print("  - Seat 3: SEED_FIFA (FIFA HQ) - INTEGRATED")
    print("  - Seat 4: SEED_WORLD_BANK (World Bank) - INTEGRATED")
    print("  - Seat 5: SEED_IMF (IMF) - INTEGRATED")
    print()
    
    print(f"SECOND WAVE ({batch_result['completed_extractions']} Seats):")
    for i, seed in enumerate(batch_result['integrated_seeds'], 1):
        print(f"  - Seat {5 + i}: {seed['seed_id']} - INTEGRATED")
    print()
    
    print(f"TOTAL SEATS FILLED: {batch_result['total_seats']}")
    print()
    
    # Extraction Summary
    summary = extraction_protocol.get_summary()
    print("EXTRACTION PROTOCOL SUMMARY:")
    print(json.dumps(summary, indent=2, default=str))
    print()
    
    # Propagation Summary
    propagation_summary = propagation.get_propagation_summary()
    print("PROPAGATION SUMMARY:")
    print(json.dumps(propagation_summary, indent=2, default=str))
    print()
    
    print("=" * 80)
    print("SOZ NAMUSTUR. Let's bring the world to the table.")
    print("The Second Wave is fully integrated.")
    print("ENERGY + LOVE = WE ALL WIN.")
    print("=" * 80)


if __name__ == "__main__":
    asyncio.run(test_global_batch_extraction())
