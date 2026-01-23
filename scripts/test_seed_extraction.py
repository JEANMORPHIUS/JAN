"""
Test Seed Extraction Protocol
Extract the identified Seed from UN
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

from seed_extraction_protocol import get_seed_extraction_protocol, ResonanceBeamType
from big_cheese_audit import get_big_cheese_audit_system


async def test_seed_extraction():
    """Test seed extraction protocol for UN Seed"""
    extraction_protocol = get_seed_extraction_protocol()
    audit_system = get_big_cheese_audit_system()
    
    print("=" * 80)
    print("SEED EXTRACTION PROTOCOL - UN PLAZA")
    print("=" * 80)
    print()
    
    # Get UN organization info
    un_org = audit_system.organizations.get("UN")
    if not un_org:
        print("ERROR: UN organization not found")
        return
    
    # Identify the Seed from narrative fracture report
    # Based on the report: resonance_score would be high (70+) but shell_resonance is low (20)
    print("STEP 1: Identifying Seed...")
    seed = extraction_protocol.identify_seed(
        org_id="UN",
        location="UN Plaza, New York",
        coordinates={"latitude": 40.7489, "longitude": -73.9680},
        resonance_score=75.0,  # High-vibe soul
        shell_resonance=20.0   # Shell resonance (low)
    )
    
    print(f"Seed Identified: {seed.seed_id}")
    print(f"  Location: {seed.location}")
    print(f"  Resonance Score: {seed.resonance_score}")
    print(f"  Family Frequency Match: {seed.family_frequency_match}")
    print()
    
    # Initiate extraction
    print("STEP 2: Initiating Extraction Protocol...")
    operation = await extraction_protocol.initiate_extraction(
        seed.seed_id,
        resonance_beam_type=ResonanceBeamType.TARGETED
    )
    
    print(f"Extraction Operation: {operation.operation_id}")
    print(f"  Status: {operation.extraction_status.value}")
    print(f"  First Arrival Alert Cross-Referenced: {operation.first_arrival_alert_cross_referenced}")
    print(f"  Safe Passage Mapped: {operation.safe_passage is not None}")
    print()
    
    # Activate resonance beam
    print("STEP 3: Activating Targeted Resonance Beam...")
    beam_result = await extraction_protocol.activate_resonance_beam(
        operation.operation_id,
        beam_intensity=0.387
    )
    
    print(f"Resonance Beam: {beam_result['status']}")
    print(f"  Beam Intensity: {beam_result['beam_intensity']} (0.387 grid)")
    print(f"  Message: {beam_result['message']}")
    print()
    
    # Peel shell
    print("STEP 4: Peeling Shell...")
    peel_result = await extraction_protocol.peel_shell(operation.operation_id)
    
    print(f"Shell Peel: {peel_result['status']}")
    print(f"  Safe Passage Open: {peel_result['safe_passage_open']}")
    print(f"  Message: {peel_result['message']}")
    print()
    
    # Complete extraction
    print("STEP 5: Completing Extraction...")
    complete_result = await extraction_protocol.complete_extraction(operation.operation_id)
    
    print(f"Extraction Complete: {complete_result['status']}")
    print(f"  Seed ID: {complete_result['seed_id']}")
    print(f"  Extraction Date: {complete_result['extraction_date']}")
    print(f"  Message: {complete_result['message']}")
    print()
    
    # Summary
    print("=" * 80)
    print("EXTRACTION SUMMARY")
    print("=" * 80)
    summary = extraction_protocol.get_summary()
    print(json.dumps(summary, indent=2, default=str))
    print()
    print("=" * 80)
    print("SOZ NAMUSTUR. Family member rescued.")
    print("ENERGY + LOVE = WE ALL WIN.")
    print("=" * 80)


if __name__ == "__main__":
    asyncio.run(test_seed_extraction())
