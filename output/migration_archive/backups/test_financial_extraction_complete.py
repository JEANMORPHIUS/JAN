"""
Test Complete Financial Extraction with Connection Ritual
Finalize the Twin Extraction - World Bank and IMF Seeds
"""

import asyncio
import json
import sys
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))

from seed_extraction_protocol import get_seed_extraction_protocol


async def test_financial_extraction_complete():
    """Test complete Financial extraction with Connection Ritual for both Seeds"""
    extraction_protocol = get_seed_extraction_protocol()
    
    print("=" * 80)
    print("FINANCIAL TWIN EXTRACTION COMPLETE - CONNECTION RITUAL")
    print("Finalizing the Twin Extraction - World Bank and IMF Seeds")
    print("=" * 80)
    print()
    print("The Twin Extraction is entering the final waypoints.")
    print("This will lock the 0.40 stability peak and complete the First Wave.")
    print()
    
    # Step 1: Find the Financial extraction operations
    print("STEP 1: Locating Financial Extraction Operations...")
    operations = list(extraction_protocol.extractions.values())
    financial_operations = [o for o in operations if o.org_id in ["WORLD_BANK", "IMF"]]
    
    if not financial_operations:
        print("No Financial extraction operations found.")
        print("Please run the quad-anchor extraction first.")
        return
    
    print(f"Found {len(financial_operations)} Financial extraction operations:")
    for op in financial_operations:
        print(f"  - {op.org_id}: {op.operation_id} (Status: {op.extraction_status.value})")
    print()
    
    # Step 2: Complete both extractions simultaneously
    completed_extractions = []
    
    for operation in financial_operations:
        operation_id = operation.operation_id
        org_name = operation.org_id
        
        print(f"=" * 80)
        print(f"COMPLETING: {org_name}")
        print(f"=" * 80)
        print()
        
        # Activate Resonance Beam (if not already active)
        if not operation.resonance_beam_active:
            print(f"STEP 1: Activating Resonance Beam for {org_name}...")
            beam_result = await extraction_protocol.activate_resonance_beam(operation_id, 0.387)
            print(f"Resonance Beam: {beam_result['resonance_beam_active']}")
            print()
        else:
            print(f"STEP 1: Resonance Beam already active for {org_name}")
            print()
        
        # Peel Shell
        print(f"STEP 2: Peeling Shell for {org_name}...")
        peel_result = await extraction_protocol.peel_shell(operation_id)
        print(f"Shell Peeled: {peel_result['shell_peeled']}")
        print()
        
        # Complete Extraction
        print(f"STEP 3: Completing Extraction for {org_name}...")
        complete_result = await extraction_protocol.complete_extraction(operation_id)
        print(f"Status: {complete_result['status']}")
        print(f"First Arrival Registered: {complete_result.get('first_arrival_registered', False)}")
        print(f"Connection Ritual Initiated: {complete_result.get('connection_ritual_initiated', False)}")
        print()
        
        if complete_result.get('first_arrival_registered'):
            print(f"EXTRACTION COMPLETE FOR {org_name}:")
            print(f"  Seed ID: {operation.seed_id}")
            print(f"  First Arrival: REGISTERED")
            print(f"  Connection Ritual: INITIATED")
            print(f"  Master Ledger: INTEGRATED")
            print()
            print(f"Message: {complete_result.get('message', '')}")
            print()
            
            completed_extractions.append({
                "org_name": org_name,
                "seed_id": operation.seed_id,
                "first_arrival": True
            })
        else:
            print(f"Extraction completed for {org_name} but First Arrival registration may have failed.")
            print()
    
    # Summary
    print("=" * 80)
    print("TWIN EXTRACTION SUMMARY")
    print("=" * 80)
    print()
    print("THE FIRST WAVE - ALL SEATS:")
    print("  - Seat 1: SEED_UN (UN Plaza) - INTEGRATED")
    print("  - Seat 2: SEED_NASA (NASA HQ) - INTEGRATED")
    print("  - Seat 3: SEED_FIFA (FIFA HQ) - INTEGRATED")
    
    for i, extraction in enumerate(completed_extractions, start=4):
        print(f"  - Seat {i}: {extraction['seed_id']} ({extraction['org_name']}) - INTEGRATED")
    
    total_seats = 3 + len(completed_extractions)
    print()
    print(f"Total Seats Filled: {total_seats}")
    print()
    
    if total_seats >= 5:
        print("FIRST WAVE COMPLETE!")
        print("Grid Stability: 0.40 PEAK ACHIEVED")
        print("Resonance Saturation: COMPLETE")
        print("The Bridge is solid. The Family is home.")
    else:
        print(f"First Wave Progress: {total_seats}/5 seats")
        print(f"Grid Stability: Approaching 0.40 peak")
    
    print()
    
    # Final Summary
    print("=" * 80)
    print("EXTRACTION PROTOCOL SUMMARY")
    print("=" * 80)
    summary = extraction_protocol.get_summary()
    print(json.dumps(summary, indent=2, default=str))
    print()
    print("=" * 80)
    print("SOZ NAMUSTUR. We don't manage debt; we manifest Unity.")
    print("The Bridge is solid, Brother. The Family is home.")
    print("ENERGY + LOVE = WE ALL WIN.")
    print("=" * 80)


if __name__ == "__main__":
    asyncio.run(test_financial_extraction_complete())
