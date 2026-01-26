"""HERITAGE QUICK START
Initialize and test the heritage system

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity


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
    Path, setup_logging, standard_main
)

import sys
from pathlib import Path

# Import heritage system
try:
    sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))
    from temporal_heritage_registry import (
        init_temporal_heritage_registry, register_heritage_site,
        add_heritage_narrative, TimelineDimension, TimePeriod
    )
    from heritage_cleansing import HeritageCleanser
    TEMPORAL_REGISTRY_AVAILABLE = True
except ImportError as e:
    print(f"Error: Could not import heritage system: {e}")
    TEMPORAL_REGISTRY_AVAILABLE = False


def quick_start():
    """Quick start guide - initialize and test the system."""
    
    print("=" * 80)
    print("HERITAGE SYSTEM QUICK START")
    print("=" * 80)
    print()
    
    if not TEMPORAL_REGISTRY_AVAILABLE:
        print("[ERROR] Heritage system not available. Check imports.")
        return
    
    # Step 1: Initialize database
    print("Step 1: Initializing Temporal Heritage Registry...")
    try:
        init_temporal_heritage_registry()
        print("[OK] Database initialized")
    except Exception as e:
        print(f"[ERROR] Database initialization failed: {e}")
        return
    
    # Step 2: Test with Berengaria Hotel
    print()
    print("Step 2: Testing with Berengaria Hotel (Cyprus)...")
    
    cleanser = HeritageCleanser(timeline_dimension=TimelineDimension.PRIMARY.value)
    
    # Test content (dark energy)
    test_content = """
    The abandoned Berengaria Hotel in Cyprus is haunted by the ghost of a merchant's wife 
    who seeks revenge for her suicide. The White Lady appears at dusk, and visitors report 
    terrifying experiences. This is one of the most haunted places in Cyprus.
    """
    
    print("  Processing dark energy content...")
    cleansed, analysis = cleanser.cleanse_content(
        content=test_content,
        source="Quick Start Test",
        site_type="Hotel",
        region="Cyprus",
        country="Cyprus",
        year_established=1930,
        year_abandoned=1984,
        time_period=TimePeriod.MODERN.value
    )
    
    print(f"  [OK] Site registered: {analysis.get('site_id', 'N/A')}")
    print(f"  [OK] Law 41 Compliant: {analysis['law_41_compliant']}")
    print(f"  [OK] Requires Cleansing: {analysis['requires_cleansing']}")
    if analysis.get('violation_type'):
        print(f"  [OK] Violation Type: {analysis['violation_type']}")
    if analysis.get('regeneration_suggestion'):
        print(f"  [OK] Regeneration Narrative Generated")
    
    # Step 3: Show summary
    print()
    print("Step 3: System Summary...")
    summary = cleanser.get_summary()
    print(f"  Sites Processed: {summary['total_processed']}")
    print(f"  Clean: {summary['cleansed_count']}")
    print(f"  Flagged: {summary['flagged_count']}")
    print(f"  Regenerated: {summary['regenerated_count']}")
    print(f"  Sites Archived: {summary['sites_archived']}")
    
    print()
    print("=" * 80)
    print("[SUCCESS] HERITAGE SYSTEM READY")
    print("=" * 80)
    print()
    print("Next Steps:")
    print("  1. Import heritage sites: python scripts/heritage_batch_import.py <file.csv>")
    print("  2. Query archive: python scripts/temporal_heritage_archive.py all")
    print("  3. Use API: curl http://localhost:8000/api/heritage/stats")
    print()
    print("PEACE, LOVE, UNITY")
    print("ENERGY + LOVE = WE ALL WIN")


if __name__ == "__main__":
    quick_start()
