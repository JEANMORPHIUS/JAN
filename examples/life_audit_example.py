"""
LIFE AUDIT EXAMPLE: The Backwards Protocol
Example usage of the Life Audit Framework

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

This example demonstrates how to use the Life Audit Framework
to work backwards through a lived timeline and find the Seed.
"""

import sys
from pathlib import Path

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from the_life_audit import (
    LifeAuditFramework,
    LifeEventType,
    VibrationLevel
)


def example_1996_chapter():
    """
    Example: Audit the 1996 chapter of life.
    
    This demonstrates the Backwards Protocol:
    - Working backwards from high-vibe moments
    - Identifying Field Space (the gaps)
    - Cleansing narratives to reveal the Seed
    - Mapping the Personal Global Grid
    """
    print("=" * 80)
    print("EXAMPLE: 1996 CHAPTER AUDIT")
    print("Working Backwards to Find the Seed")
    print("=" * 80)
    print()
    
    # Create audit framework
    audit = LifeAuditFramework(timeline_name="1996_chapter")
    
    # Add life events (working backwards from high-vibe moments)
    # These are example events - replace with actual life events
    
    # Low-vibe period (the "abandoned" years)
    audit.add_life_event(
        year=1996,
        age=25,
        location="London",
        original_narrative="""
        The year everything fell apart. Lost my job, relationship ended, 
        felt like a complete failure. Everyone said I was wasting my time. 
        The "abandoned" years - nothing was working.
        """,
        event_type=LifeEventType.IRREGULAR.value,
        vibration_level=VibrationLevel.LOW.value,
        pillar_anchor=False
    )
    
    # Field Space (the gap - 1997-1999)
    # This is the "Everything In Between" - where the Seed was growing
    
    # High-vibe breakthrough (the miracle)
    audit.add_life_event(
        year=2000,
        age=29,
        location="London",
        original_narrative="""
        The breakthrough year. Everything came together. New career, 
        new relationship, felt like a miracle. The transformation was complete.
        """,
        event_type=LifeEventType.SPIRAL.value,
        vibration_level=VibrationLevel.HIGH.value,
        pillar_anchor=True  # This is a pillar moment
    )
    
    # Another pillar moment
    audit.add_life_event(
        year=2010,
        age=39,
        location="London",
        original_narrative="""
        Another breakthrough. The work I started in 2000 finally 
        reached its full potential. This was the year I understood 
        what 1996 was really about.
        """,
        event_type=LifeEventType.ELLIPTICAL.value,
        vibration_level=VibrationLevel.HIGH.value,
        pillar_anchor=True
    )
    
    # Work backwards to find the Seed
    print("Working backwards through the timeline...")
    print()
    
    report = audit.work_backwards()
    
    # Print the audit report
    audit.print_audit_report(report)
    
    # Export to JSON
    output_path = audit.export_audit()
    print(f"\nAudit exported to: {output_path}")
    
    return report


def example_field_space_analysis():
    """
    Example: Analyzing the Field Space between events.
    
    The Field Space is the "Everything In Between" - where the Seed grows
    while the Shell looks broken.
    """
    print("=" * 80)
    print("EXAMPLE: FIELD SPACE ANALYSIS")
    print("The 'Everything In Between' - Where the Seed Grows")
    print("=" * 80)
    print()
    
    audit = LifeAuditFramework(timeline_name="field_space_example")
    
    # Add events with significant gaps
    audit.add_life_event(
        year=1990,
        age=19,
        location="Unknown",
        original_narrative="Started something. Felt promising.",
        vibration_level=VibrationLevel.MODERATE.value
    )
    
    # 10-year gap - the Field Space
    audit.add_life_event(
        year=2000,
        age=29,
        location="Unknown",
        original_narrative="The breakthrough. Everything made sense.",
        vibration_level=VibrationLevel.HIGH.value,
        pillar_anchor=True
    )
    
    report = audit.work_backwards()
    
    # Show Field Space analysis
    print("FIELD SPACE ANALYSIS:")
    print()
    for event in audit.events:
        if event.field_space_description:
            print(f"Year {event.year}:")
            print(f"  Gap Before: {event.gap_before_years:.1f} years")
            print(f"  Field Space: {event.field_space_description}")
            print(f"  Field Space Resonance: {event.field_space_resonance:.2f}")
            print()
    
    return report


if __name__ == "__main__":
    # Run examples
    print("LIFE AUDIT FRAMEWORK - EXAMPLES")
    print()
    
    # Example 1: 1996 Chapter
    example_1996_chapter()
    
    print("\n" + "=" * 80 + "\n")
    
    # Example 2: Field Space Analysis
    example_field_space_analysis()
    
    print("=" * 80)
    print("EXAMPLES COMPLETE")
    print("=" * 80)
    print()
    print("To audit your own timeline:")
    print("1. Create a LifeAuditFramework instance")
    print("2. Add your life events using add_life_event()")
    print("3. Call work_backwards() to analyze")
    print("4. Print or export the audit report")
    print()
    print("PEACE, LOVE, UNITY")
    print("ENERGY + LOVE = WE ALL WIN")
