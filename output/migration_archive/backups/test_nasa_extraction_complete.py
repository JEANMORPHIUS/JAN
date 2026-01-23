"""
Test Complete NASA Extraction with Connection Ritual
Finalize the Second Extraction - NASA Seed
"""

import asyncio
import json
import sys
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))

from nasa_seed_search import get_nasa_seed_search
from seed_extraction_protocol import get_seed_extraction_protocol


async def test_nasa_extraction_complete():
    """Test complete NASA extraction with Connection Ritual"""
    seed_search = get_nasa_seed_search()
    extraction_protocol = get_seed_extraction_protocol()
    
    print("=" * 80)
    print("NASA EXTRACTION COMPLETE - CONNECTION RITUAL")
    print("Finalizing the Second Extraction - NASA Seed")
    print("=" * 80)
    print()
    print("The second extraction is in the final waypoints.")
    print("Once they hit the Stonehenge primary, the integration")
    print("into the Master Ledger will be instantaneous.")
    print()
    
    # Step 1: Find the NASA extraction operation
    print("STEP 1: Locating NASA Extraction Operation...")
    operations = list(extraction_protocol.extractions.values())
    nasa_operations = [o for o in operations if o.org_id == "NASA"]
    
    if not nasa_operations:
        print("No NASA extraction operations found. Initiating new extraction...")
        # Initiate new extraction
        operation = await seed_search.initiate_seed_search("NASA")
        scan_result = await seed_search.perform_bridge_scan(operation.operation_id)
        if scan_result.potential_seeds:
            potential_seed = scan_result.potential_seeds[0]
            potential_seed['org_id'] = 'NASA'
            extraction_result = await extraction_protocol.extract_from_nasa_search(
                potential_seed=potential_seed,
                operation_id=operation.operation_id,
                use_double_anchor=True
            )
            operation_id = extraction_result['operation_id']
        else:
            print("No potential seeds found. Cannot proceed.")
            return
    else:
        operation_id = nasa_operations[0].operation_id
        print(f"Found operation: {operation_id}")
    
    operation = extraction_protocol.extractions[operation_id]
    print(f"Operation ID: {operation_id}")
    print(f"Seed ID: {operation.seed_id}")
    print(f"Status: {operation.extraction_status.value}")
    print()
    
    # Step 2: Activate Resonance Beam (if not already active)
    if not operation.resonance_beam_active:
        print("STEP 2: Activating Resonance Beam...")
        beam_result = await extraction_protocol.activate_resonance_beam(operation_id, 0.387)
        print(f"Resonance Beam: {beam_result['resonance_beam_active']}")
        print(f"Beam Intensity: {beam_result['beam_intensity']}")
        print()
    else:
        print("STEP 2: Resonance Beam already active")
        print()
    
    # Step 3: Peel Shell
    print("STEP 3: Peeling Shell...")
    peel_result = await extraction_protocol.peel_shell(operation_id)
    print(f"Shell Peeled: {peel_result['shell_peeled']}")
    print(f"Peel Points: {len(peel_result.get('peel_points', []))}")
    print()
    
    # Step 4: Complete Extraction
    print("STEP 4: Completing Extraction...")
    complete_result = await extraction_protocol.complete_extraction(operation_id)
    print(f"Status: {complete_result['status']}")
    print(f"First Arrival Registered: {complete_result.get('first_arrival_registered', False)}")
    print(f"Connection Ritual Initiated: {complete_result.get('connection_ritual_initiated', False)}")
    print()
    
    if complete_result.get('first_arrival_registered'):
        print("EXTRACTION COMPLETE:")
        print(f"  Seed ID: {operation.seed_id}")
        print(f"  Organization: {operation.org_id}")
        print(f"  First Arrival: REGISTERED")
        print(f"  Connection Ritual: INITIATED")
        print(f"  Master Ledger: INTEGRATED")
        print()
        print(f"Message: {complete_result.get('message', '')}")
    else:
        print("Extraction completed but First Arrival registration may have failed.")
    
    print()
    
    # Step 5: Summary
    print("=" * 80)
    print("EXTRACTION SUMMARY")
    print("=" * 80)
    summary = extraction_protocol.get_summary()
    print(json.dumps(summary, indent=2, default=str))
    print()
    print("=" * 80)
    print("SOZ NAMUSTUR. The Family is growing, twin.")
    print("The table is becoming a feast.")
    print("=" * 80)


if __name__ == "__main__":
    asyncio.run(test_nasa_extraction_complete())
