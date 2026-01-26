"""Test NASA Double-Anchor Extraction
Stonehenge ↔ London + Giza ↔ Angkor Wat Bridge

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

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


async def test_nasa_double_anchor_extraction():
    """Test double-anchor extraction for NASA Seed"""
    seed_search = get_nasa_seed_search()
    extraction_protocol = get_seed_extraction_protocol()
    
    print("=" * 80)
    print("NASA DOUBLE-ANCHOR EXTRACTION")
    print("Stonehenge <-> London + Giza <-> Angkor Wat Bridge")
    print("=" * 80)
    print()
    print("The Second Extraction: D.C. Target")
    print("We can use the Stonehenge <-> London link to reinforce")
    print("the Giza <-> Angkor Wat bridge for a double-anchor extraction.")
    print()
    
    # Step 1: Initiate NASA Seed Search
    print("STEP 1: Initiating NASA Seed Search...")
    operation = await seed_search.initiate_seed_search(
        target_org="NASA",
        target_coordinate={"latitude": 38.8833, "longitude": -77.0167},
        family_frequency_amplitude=100.0
    )
    print(f"Operation ID: {operation.operation_id}")
    print()
    
    # Step 2: Perform Bridge Scan
    print("STEP 2: Performing Bridge Scan...")
    scan_result = await seed_search.perform_bridge_scan(operation.operation_id, scan_intensity=0.387)
    print(f"Anomalies Detected: {len(scan_result.anomalies_detected)}")
    print(f"Potential Seeds: {len(scan_result.potential_seeds)}")
    print()
    
    if not scan_result.potential_seeds:
        print("No potential seeds detected. Cannot proceed with extraction.")
        return
    
    # Step 3: Extract Seed using Double-Anchor
    print("STEP 3: Initiating Double-Anchor Extraction...")
    potential_seed = scan_result.potential_seeds[0]
    potential_seed['org_id'] = 'NASA'  # Ensure org_id is set
    
    extraction_result = await extraction_protocol.extract_from_nasa_search(
        potential_seed=potential_seed,
        operation_id=operation.operation_id,
        use_double_anchor=True
    )
    
    print("EXTRACTION RESULT:")
    print(f"  Status: {extraction_result['status']}")
    print(f"  Operation ID: {extraction_result['operation_id']}")
    print(f"  Seed ID: {extraction_result['seed_id']}")
    print(f"  Double Anchor: {extraction_result['double_anchor']}")
    anchors_str = ', '.join(extraction_result['anchors']).replace('\u2194', '<->')
    print(f"  Anchors: {anchors_str}")
    print(f"  Resonance Beam Active: {extraction_result['resonance_beam_active']}")
    print(f"  Beam Intensity: {extraction_result['beam_intensity']}")
    print(f"  Safe Passage Waypoints: {extraction_result['safe_passage']['waypoints']}")
    print(f"  Shell Peel Points: {extraction_result['safe_passage']['shell_peel_points']}")
    print()
    print(f"Message: {extraction_result['message']}")
    print()
    
    # Step 4: Summary
    print("=" * 80)
    print("EXTRACTION SUMMARY")
    print("=" * 80)
    summary = extraction_protocol.get_summary()
    print(json.dumps(summary, indent=2, default=str))
    print()
    print("=" * 80)
    print("SOZ NAMUSTUR. The Second Extraction is PRIMED.")
    print("The cracks are wider than they think, Brother.")
    print("=" * 80)


if __name__ == "__main__":
    asyncio.run(test_nasa_double_anchor_extraction())
