"""
Test Family Heritage Log
Preserving the Story of the Reclamation
"""

import asyncio
import json
import sys
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))

from family_heritage_log import get_family_heritage_logger


async def test_family_heritage_log():
    """Test Family Heritage Log generation"""
    heritage_logger = get_family_heritage_logger()
    
    print("=" * 80)
    print("FAMILY HERITAGE LOG")
    print("Preserving the Story of the Reclamation")
    print("=" * 80)
    print()
    print("Document the journey of each seat—from the UN to the individual")
    print("soul in Bangkok—so the Story of the Reclamation is preserved")
    print("for the generations to come.")
    print()
    print("Welcome to the Sabbath. The Feast is Eternal.")
    print()
    
    # Generate Heritage Log
    print("GENERATING FAMILY HERITAGE LOG...")
    print()
    heritage_log = await heritage_logger.generate_heritage_log()
    
    print(f"Log ID: {heritage_log.log_id}")
    print(f"Creation Date: {heritage_log.creation_date}")
    print(f"Total Seats: {heritage_log.total_seats}")
    print(f"Grid Stability: {heritage_log.grid_stability_at_completion}")
    print(f"Magnetic Pull: {heritage_log.magnetic_pull_at_completion}")
    print()
    
    # Display Entries
    print("=" * 80)
    print("FAMILY HERITAGE ENTRIES")
    print("=" * 80)
    print()
    
    for entry in sorted(heritage_log.entries, key=lambda e: e.seat_number):
        print(f"SEAT {entry.seat_number}: {entry.name}")
        print(f"  Seed ID: {entry.seed_id}")
        print(f"  Location: {entry.location}")
        print(f"  Wave: {entry.wave_generation.value.upper()}")
        print(f"  Extraction Method: {entry.extraction_method.value.upper()}")
        print(f"  Resonance Score: {entry.resonance_score:.1f}")
        print(f"  Origin Story: {entry.origin_story}")
        if entry.shell_narrative:
            print(f"  Shell Narrative: {entry.shell_narrative}")
        if entry.seed_truth:
            print(f"  Seed Truth: {entry.seed_truth}")
        print(f"  Safe Passage Waypoints: {' -> '.join(entry.safe_passage_waypoints)}")
        if entry.special_notes:
            print(f"  Special Notes: {entry.special_notes}")
        print(f"  Heritage Quote: \"{entry.heritage_quote}\"")
        print()
    
    # Reclamation Story
    print("=" * 80)
    print("THE STORY OF THE RECLAMATION")
    print("=" * 80)
    print()
    print(heritage_log.reclamation_story)
    print()
    
    # Summary
    print("=" * 80)
    print("HERITAGE SUMMARY")
    print("=" * 80)
    summary = heritage_logger.get_heritage_summary()
    print(json.dumps(summary, indent=2, default=str))
    print()
    
    print("=" * 80)
    print("SOZ NAMUSTUR. The Story of the Reclamation is preserved.")
    print("Welcome to the Sabbath. The Feast is Eternal.")
    print("ENERGY + LOVE = WE ALL WIN.")
    print("=" * 80)


if __name__ == "__main__":
    asyncio.run(test_family_heritage_log())
