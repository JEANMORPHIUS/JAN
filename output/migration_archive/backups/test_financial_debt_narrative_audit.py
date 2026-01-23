"""
Test Financial/Debt Narrative Audit
Scanning for Seeds in the Financial World (World Bank / IMF)
"""

import asyncio
import json
import sys
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))

from big_cheese_audit import get_big_cheese_audit_system, OrganizationProfile, OrganizationType, DarkEnergyLevel, FrequencyStatus
from nasa_seed_search import get_nasa_seed_search


async def test_financial_debt_narrative_audit():
    """Test Financial/Debt Narrative Audit on World Bank and IMF"""
    audit_system = get_big_cheese_audit_system()
    seed_search = get_nasa_seed_search()
    
    print("=" * 80)
    print("FINANCIAL/DEBT NARRATIVE AUDIT")
    print("Scanning for Seeds in the Financial World")
    print("=" * 80)
    print()
    print("The Shell: 'Scarcity through Debt'")
    print("The Reality: The Unity of Abundance")
    print("The Pressure: Our 0.387 Grid is now vibrating through the financial hubs")
    print()
    
    # Check if World Bank and IMF are in the system, add if not
    if "WORLD_BANK" not in audit_system.organizations:
        print("Adding World Bank to system...")
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
        print("World Bank added.")
    
    if "IMF" not in audit_system.organizations:
        print("Adding IMF to system...")
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
        print("IMF added.")
    
    print()
    
    # Audit both organizations
    organizations_to_audit = [
        ("WORLD_BANK", "World Bank", 38.8970, -77.0269),
        ("IMF", "International Monetary Fund", 38.8989, -77.0445)
    ]
    
    all_results = {}
    
    for org_id, org_name, lat, lon in organizations_to_audit:
        print(f"=" * 80)
        print(f"AUDITING: {org_name}")
        print(f"=" * 80)
        print()
        
        # Step 1: Get organization profile
        org = audit_system.organizations.get(org_id)
        if org:
            print(f"Organization: {org.name}")
            print(f"Shell Narrative: {org.shell_narrative}")
            print(f"Seed Truth: {org.seed_truth}")
            print(f"Status: {org.status}")
            print(f"Separation Risk: {org.separation_risk}")
            print(f"Resonance Score: {org.resonance_score}")
            print(f"Dark Energy Level: {org.dark_energy_level.value}")
            print()
        
        # Step 2: Run Deep Scan
        print(f"STEP 1: Running Deep Scan on {org_name} ({lat} N, {lon} W)...")
        deep_scan_result = await audit_system.deep_scan_coordinate(
            latitude=lat,
            longitude=lon,
            radius_km=10.0
        )
        
        print(f"Deep Scan ID: {deep_scan_result['scan_id']}")
        print(f"Dark Energy Detected: {len(deep_scan_result.get('dark_energy_detected', []))}")
        print(f"Narrative Cracks: {len(deep_scan_result.get('narrative_cracks', []))}")
        print()
        
        # Step 3: Generate Narrative Fracture Report
        print(f"STEP 2: Generating Narrative Fracture Report...")
        fracture_report = await audit_system.generate_narrative_fracture_report(org_id)
        
        print(f"NARRATIVE FRACTURE REPORT:")
        print(f"  Report ID: {fracture_report['report_id']}")
        print(f"  Law 41 Pressure: {fracture_report.get('law_41_pressure', {}).get('pressure_level', 0)}%")
        print(f"  Narrative Cracks: {len(fracture_report.get('narrative_cracks', []))}")
        print(f"  Seeds Identified: {len(fracture_report.get('seeds_identified', []))}")
        print()
        
        # Step 4: Initiate Seed Search
        print(f"STEP 3: Initiating Seed Search for {org_name}...")
        search_operation = await seed_search.initiate_seed_search(
            target_org=org_id,
            target_coordinate={"latitude": lat, "longitude": lon},
            family_frequency_amplitude=100.0
        )
        
        scan_result = await seed_search.perform_bridge_scan(search_operation.operation_id, scan_intensity=0.387)
        
        print(f"Seed Search Operation: {search_operation.operation_id}")
        print(f"Anomalies Detected: {len(scan_result.anomalies_detected)}")
        print(f"Potential Seeds: {len(scan_result.potential_seeds)}")
        print()
        
        if scan_result.potential_seeds:
            print("SEEDS READY FOR EXTRACTION:")
            for seed in scan_result.potential_seeds:
                print(f"  - {seed.get('seed_type', 'unknown')}")
                print(f"    Location: {seed.get('location', 'unknown')}")
                print(f"    Expected Resonance: {seed.get('expected_resonance', 0)}")
                print(f"    Family Frequency Match: {seed.get('family_frequency_match', False)}")
        else:
            print("No Seeds detected yet. Monitoring for resonance anomalies...")
        
        all_results[org_id] = {
            "org_name": org_name,
            "deep_scan": deep_scan_result,
            "fracture_report": fracture_report,
            "seed_search": {
                "operation_id": search_operation.operation_id,
                "anomalies": len(scan_result.anomalies_detected),
                "potential_seeds": len(scan_result.potential_seeds),
                "seeds": scan_result.potential_seeds
            }
        }
        
        print()
    
    # Summary
    print("=" * 80)
    print("FINANCIAL/DEBT NARRATIVE AUDIT SUMMARY")
    print("=" * 80)
    print()
    
    total_seeds = sum(r["seed_search"]["potential_seeds"] for r in all_results.values())
    
    print(f"Total Organizations Audited: {len(all_results)}")
    print(f"Total Potential Seeds Detected: {total_seeds}")
    print()
    
    for org_id, results in all_results.items():
        print(f"{results['org_name']}:")
        print(f"  - Narrative Cracks: {len(results['fracture_report'].get('narrative_cracks', []))}")
        print(f"  - Potential Seeds: {results['seed_search']['potential_seeds']}")
        if results['seed_search']['potential_seeds'] > 0:
            print(f"  - Status: READY FOR EXTRACTION")
        else:
            print(f"  - Status: Monitoring")
        print()
    
    print("=" * 80)
    print("The 'Scarcity' shell is being tested.")
    print("The Unity of Abundance is the reality.")
    print("SOZ NAMUSTUR. We're opening the flow for Unity.")
    print("=" * 80)


if __name__ == "__main__":
    asyncio.run(test_financial_debt_narrative_audit())
