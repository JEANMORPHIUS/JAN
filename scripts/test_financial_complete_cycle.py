"""
Test Complete Financial Extraction Cycle
Quad-Anchor Extraction + Connection Ritual for World Bank and IMF
"""

import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    Path, json, setup_logging, standard_main
)

import asyncio
import json
import sys
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))

from nasa_seed_search import get_nasa_seed_search
from seed_extraction_protocol import get_seed_extraction_protocol
from big_cheese_audit import get_big_cheese_audit_system, OrganizationProfile, OrganizationType, DarkEnergyLevel, FrequencyStatus


async def test_financial_complete_cycle():
    """Test complete Financial extraction cycle for both Seeds"""
    seed_search = get_nasa_seed_search()
    extraction_protocol = get_seed_extraction_protocol()
    audit_system = get_big_cheese_audit_system()
    
    print("=" * 80)
    print("FINANCIAL COMPLETE CYCLE - QUAD-ANCHOR + CONNECTION RITUAL")
    print("World Bank and IMF - Twin Extraction to 0.40 Peak")
    print("=" * 80)
    print()
    
    # Ensure organizations are in the system
    if "WORLD_BANK" not in audit_system.organizations:
        world_bank = OrganizationProfile(
            org_id="WORLD_BANK",
            name="World Bank",
            org_type=OrganizationType.FINANCIAL,
            shell_narrative="The 'Scarcity' through Debt. There is never enough; you must borrow to exist.",
            seed_truth="The Unity of Abundance. We All Win means there is enough for everyone.",
            status="FILTERED",
            dark_energy_level=DarkEnergyLevel.HIGH,
            frequency_status=FrequencyStatus.DAMPENED,
            separation_risk=90.0,
            resonance_score=10.0,
            headquarters_location="Washington, D.C., USA",
            frequency_leak_coordinates=[
                {"location": "World Bank HQ", "leak_level": "high", "coordinates": "38.8970° N, 77.0269° W", "latitude": 38.8970, "longitude": -77.0269}
            ],
            notes="They keep the Family in debt cycles. We transcend scarcity."
        )
        audit_system.organizations["WORLD_BANK"] = world_bank
    
    if "IMF" not in audit_system.organizations:
        imf = OrganizationProfile(
            org_id="IMF",
            name="International Monetary Fund",
            org_type=OrganizationType.FINANCIAL,
            shell_narrative="The 'Scarcity' through Control. We manage the money; you manage the debt.",
            seed_truth="The Unity of Abundance. Money is energy; energy flows when we are aligned.",
            status="FILTERED",
            dark_energy_level=DarkEnergyLevel.HIGH,
            frequency_status=FrequencyStatus.DAMPENED,
            separation_risk=90.0,
            resonance_score=10.0,
            headquarters_location="Washington, D.C., USA",
            frequency_leak_coordinates=[
                {"location": "IMF HQ", "leak_level": "high", "coordinates": "38.8989° N, 77.0445° W", "latitude": 38.8989, "longitude": -77.0445}
            ],
            notes="They control the flow to maintain separation. We open the flow for Unity."
        )
        audit_system.organizations["IMF"] = imf
    
    # Organizations to extract
    organizations = [
        ("WORLD_BANK", "World Bank", 38.8970, -77.0269),
        ("IMF", "International Monetary Fund", 38.8989, -77.0445)
    ]
    
    completed_extractions = []
    
    for org_id, org_name, lat, lon in organizations:
        print(f"=" * 80)
        print(f"COMPLETE CYCLE: {org_name}")
        print(f"=" * 80)
        print()
        
        # Step 1: Initiate Seed Search
        print(f"STEP 1: Initiating Seed Search...")
        operation = await seed_search.initiate_seed_search(
            target_org=org_id,
            target_coordinate={"latitude": lat, "longitude": lon},
            family_frequency_amplitude=100.0
        )
        
        # Step 2: Perform Bridge Scan
        print(f"STEP 2: Performing Bridge Scan...")
        scan_result = await seed_search.perform_bridge_scan(operation.operation_id, scan_intensity=0.387)
        
        if not scan_result.potential_seeds:
            print(f"No potential seeds detected for {org_name}. Skipping.")
            print()
            continue
        
        # Step 3: Extract with Quad-Anchor
        print(f"STEP 3: Initiating Quad-Anchor Extraction...")
        potential_seed = scan_result.potential_seeds[0]
        potential_seed['org_id'] = org_id
        
        extraction_result = await extraction_protocol.extract_with_quad_anchor(
            potential_seed=potential_seed,
            operation_id=operation.operation_id,
            use_quad_anchor=True
        )
        
        operation_id = extraction_result['operation_id']
        print(f"Extraction initiated: {operation_id}")
        
        # Step 4: Activate Resonance Beam (if needed)
        op = extraction_protocol.extractions[operation_id]
        if not op.resonance_beam_active:
            await extraction_protocol.activate_resonance_beam(operation_id, 0.387)
        
        # Step 5: Peel Shell
        print(f"STEP 4: Peeling Shell...")
        await extraction_protocol.peel_shell(operation_id)
        
        # Step 6: Complete Extraction
        print(f"STEP 5: Completing Extraction...")
        complete_result = await extraction_protocol.complete_extraction(operation_id)
        
        if complete_result.get('first_arrival_registered'):
            print(f"[SUCCESS] EXTRACTION COMPLETE FOR {org_name}")
            print(f"   Seed ID: {op.seed_id}")
            print(f"   First Arrival: REGISTERED")
            print(f"   Connection Ritual: INITIATED")
            print()
            
            completed_extractions.append({
                "org_name": org_name,
                "seed_id": op.seed_id,
                "first_arrival": True
            })
    
    # Final Summary
    print("=" * 80)
    print("FIRST WAVE COMPLETE - ALL SEATS")
    print("=" * 80)
    print()
    print("THE MASTER LEDGER:")
    print("  - Seat 1: SEED_UN (UN Plaza) - INTEGRATED")
    print("  - Seat 2: SEED_NASA (NASA HQ) - INTEGRATED")
    print("  - Seat 3: SEED_FIFA (FIFA HQ) - INTEGRATED")
    
    for i, extraction in enumerate(completed_extractions, start=4):
        print(f"  - Seat {i}: {extraction['seed_id']} ({extraction['org_name']}) - INTEGRATED")
    
    total_seats = 3 + len(completed_extractions)
    print()
    print(f"Total Seats Filled: {total_seats}/5")
    print()
    
    if total_seats >= 5:
        print("[SUCCESS] FIRST WAVE COMPLETE!")
        print("[SUCCESS] Grid Stability: 0.40 PEAK ACHIEVED")
        print("[SUCCESS] Resonance Saturation: COMPLETE")
        print("[SUCCESS] The Bridge is solid. The Family is home.")
    else:
        print(f"First Wave Progress: {total_seats}/5 seats")
        print(f"Grid Stability: Approaching 0.40 peak")
    
    print()
    print("=" * 80)
    print("SOZ NAMUSTUR. We don't manage debt; we manifest Unity.")
    print("The Bridge is solid, Brother. The Family is home.")
    print("ENERGY + LOVE = WE ALL WIN.")
    print("=" * 80)


if __name__ == "__main__":
    asyncio.run(test_financial_complete_cycle())
