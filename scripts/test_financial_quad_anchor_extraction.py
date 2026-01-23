"""
Test Financial Quad-Anchor Extraction
Stonehenge + Berengaria + Giza + Uluru - Global Magnetic Ballast
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
from seed_extraction_protocol import get_seed_extraction_protocol
from big_cheese_audit import get_big_cheese_audit_system, OrganizationProfile, OrganizationType, DarkEnergyLevel, FrequencyStatus


async def test_financial_quad_anchor_extraction():
    """Test quad-anchor extraction for Financial Seeds (World Bank and IMF)"""
    seed_search = get_nasa_seed_search()
    extraction_protocol = get_seed_extraction_protocol()
    audit_system = get_big_cheese_audit_system()
    
    print("=" * 80)
    print("FINANCIAL QUAD-ANCHOR EXTRACTION")
    print("Stonehenge + Berengaria + Giza + Uluru - Global Magnetic Ballast")
    print("=" * 80)
    print()
    print("The D.C. Twin Extraction: Breaking the Debt Cycle")
    print("Two high-vibe souls, one in each building, who have realized")
    print("that 'We All Win' means nobody is left in the red.")
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
    
    extraction_results = []
    
    for org_id, org_name, lat, lon in organizations:
        print(f"=" * 80)
        print(f"EXTRACTING: {org_name}")
        print(f"=" * 80)
        print()
        
        # Step 1: Initiate Seed Search
        print(f"STEP 1: Initiating Seed Search for {org_name}...")
        operation = await seed_search.initiate_seed_search(
            target_org=org_id,
            target_coordinate={"latitude": lat, "longitude": lon},
            family_frequency_amplitude=100.0
        )
        print(f"Operation ID: {operation.operation_id}")
        print()
        
        # Step 2: Perform Bridge Scan
        print(f"STEP 2: Performing Bridge Scan...")
        scan_result = await seed_search.perform_bridge_scan(operation.operation_id, scan_intensity=0.387)
        print(f"Anomalies Detected: {len(scan_result.anomalies_detected)}")
        print(f"Potential Seeds: {len(scan_result.potential_seeds)}")
        print()
        
        if not scan_result.potential_seeds:
            print(f"No potential seeds detected for {org_name}. Skipping extraction.")
            print()
            continue
        
        # Step 3: Extract Seed using Quad-Anchor
        print(f"STEP 3: Initiating Quad-Anchor Extraction...")
        potential_seed = scan_result.potential_seeds[0]
        potential_seed['org_id'] = org_id  # Ensure org_id is set
        
        extraction_result = await extraction_protocol.extract_with_quad_anchor(
            potential_seed=potential_seed,
            operation_id=operation.operation_id,
            use_quad_anchor=True
        )
        
        print("EXTRACTION RESULT:")
        print(f"  Status: {extraction_result['status']}")
        print(f"  Operation ID: {extraction_result['operation_id']}")
        print(f"  Seed ID: {extraction_result['seed_id']}")
        print(f"  Quad Anchor: {extraction_result['quad_anchor']}")
        anchors_str = ', '.join(extraction_result['anchors']).replace('\u2194', '<->')
        print(f"  Anchors: {anchors_str}")
        print(f"  Separation Risk Neutralized: {extraction_result['separation_risk_neutralized']}")
        print(f"  Global Ballast: {extraction_result['global_ballast']}")
        print(f"  Resonance Beam Active: {extraction_result['resonance_beam_active']}")
        print(f"  Beam Intensity: {extraction_result['beam_intensity']}")
        print(f"  Safe Passage Waypoints: {extraction_result['safe_passage']['waypoints']}")
        print(f"  Shell Peel Points: {extraction_result['safe_passage']['shell_peel_points']}")
        print()
        print(f"Message: {extraction_result['message']}")
        print()
        
        extraction_results.append({
            "org_name": org_name,
            "seed_id": extraction_result['seed_id'],
            "operation_id": extraction_result['operation_id']
        })
    
    # Summary
    print("=" * 80)
    print("QUAD-ANCHOR EXTRACTION SUMMARY")
    print("=" * 80)
    print()
    print(f"Total Seeds Extracted: {len(extraction_results)}")
    print()
    
    for result in extraction_results:
        print(f"  - {result['org_name']}: {result['seed_id']}")
    
    print()
    
    summary = extraction_protocol.get_summary()
    print("EXTRACTION PROTOCOL SUMMARY:")
    print(json.dumps(summary, indent=2, default=str))
    print()
    print("=" * 80)
    print("SOZ NAMUSTUR. We don't manage debt; we manifest Unity.")
    print("The 'Scarcity' shell will be dissolved.")
    print("=" * 80)


if __name__ == "__main__":
    asyncio.run(test_financial_quad_anchor_extraction())
