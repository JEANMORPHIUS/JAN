"""
Direct test of CARE Package Framework
No API server needed
"""

import sys
from pathlib import Path

# Add paths
sys.path.insert(0, str(Path(__file__).parent / "scripts"))
sys.path.insert(0, str(Path(__file__).parent / "jan-studio" / "backend"))

from care_package_framework import CarePackageFramework
import json

def test_care_package():
    print("="*70)
    print("CARE PACKAGE DIRECT TEST")
    print("="*70)

    care = CarePackageFramework()

    # Test 1: Healthcare dark energy
    print("\n[TEST 1] Healthcare Dark Energy Detection")
    print("-"*70)
    narrative1 = "I am battling terminal cancer and the doctors say there is no hope for recovery. This disease will kill me."

    detection1 = care.detect_dark_energy(
        content=narrative1,
        source="test",
        life_aspect="healthcare"
    )

    print(f"Narrative: {narrative1}")
    print(f"\nDark Energy Detected: {detection1.dark_energy_detected}")
    print(f"Severity Score: {detection1.severity_score:.2f}")
    print(f"Regeneration Required: {detection1.regeneration_required}")
    print(f"\nDetected Patterns ({len(detection1.detected_patterns)}):")
    for i, pattern in enumerate(detection1.detected_patterns[:5], 1):
        print(f"  {i}. {pattern.pattern_name} (severity: {pattern.severity})")

    if detection1.regeneration_required:
        print("\nRegenerating narrative...")
        regenerated1 = care.regenerate_narrative(detection1)
        print(f"Regenerated: {regenerated1[:200]}...")

    # Test 2: Financial dark energy
    print("\n\n[TEST 2] Financial Dark Energy Detection")
    print("-"*70)
    narrative2 = "I am drowning in debt and will never be free. I am a financial failure trapped in this system."

    detection2 = care.detect_dark_energy(
        content=narrative2,
        source="test",
        life_aspect="financial"
    )

    print(f"Narrative: {narrative2}")
    print(f"\nDark Energy Detected: {detection2.dark_energy_detected}")
    print(f"Severity Score: {detection2.severity_score:.2f}")
    print(f"Regeneration Required: {detection2.regeneration_required}")
    print(f"\nDetected Patterns ({len(detection2.detected_patterns)}):")
    for i, pattern in enumerate(detection2.detected_patterns[:5], 1):
        print(f"  {i}. {pattern.pattern_name} (severity: {pattern.severity})")

    if detection2.regeneration_required:
        print("\nRegenerating narrative...")
        regenerated2 = care.regenerate_narrative(detection2)
        print(f"Regenerated: {regenerated2[:200]}...")

    # Test 3: Clean narrative (no dark energy)
    print("\n\n[TEST 3] Clean Narrative (No Dark Energy)")
    print("-"*70)
    narrative3 = "I am learning to steward my health temple through conscious choices and holistic practices."

    detection3 = care.detect_dark_energy(
        content=narrative3,
        source="test",
        life_aspect="healthcare"
    )

    print(f"Narrative: {narrative3}")
    print(f"\nDark Energy Detected: {detection3.dark_energy_detected}")
    print(f"Severity Score: {detection3.severity_score:.2f}")
    print(f"Regeneration Required: {detection3.regeneration_required}")

    print("\n" + "="*70)
    print("CARE PACKAGE TEST COMPLETE")
    print("="*70)

if __name__ == "__main__":
    test_care_package()
