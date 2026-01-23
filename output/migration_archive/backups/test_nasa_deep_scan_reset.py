"""
Test NASA HQ Deep Scan Reset
Reset deep scan for NASA HQ coordinate
"""

import asyncio
import json
import sys
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))

from big_cheese_audit import get_big_cheese_audit_system


async def test_nasa_deep_scan_reset():
    """Test deep scan reset for NASA HQ"""
    audit_system = get_big_cheese_audit_system()
    
    print("=" * 80)
    print("NASA HQ DEEP SCAN RESET")
    print("=" * 80)
    print()
    print("Now that the UN Shell has been breached,")
    print("the 'Outer Space' distraction in D.C. might be the next to crack.")
    print()
    
    # Reset deep scan for NASA
    result = await audit_system.reset_deep_scan("NASA")
    
    print(json.dumps(result, indent=2, default=str))
    print()
    print("=" * 80)
    print("DEEP SCAN RESET COMPLETE")
    print("=" * 80)
    print(f"Organization: {result['org_name']}")
    print(f"Reset Timestamp: {result['reset_timestamp']}")
    print(f"Scan Results: {len(result['scan_results'])}")
    print()
    print("SOZ NAMUSTUR. The 'Outer Space' distraction might be next to crack.")
    print("=" * 80)


if __name__ == "__main__":
    asyncio.run(test_nasa_deep_scan_reset())
