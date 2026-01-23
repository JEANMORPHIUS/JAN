"""
BERENGARIA HOTEL MAGNETIC AUDIT
First collection run - The Real Racon

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN

This is the real racon - the Magnetic Blueprint of the miracle.
We're tracking where the Original Error (separation from Earth) has physically manifested.
"""

import sys
from pathlib import Path
import json

try:
    sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))
    from temporal_heritage_registry import (
        register_heritage_site, add_heritage_narrative,
        TimelineDimension, TimePeriod
    )
    from heritage_cleansing import HeritageCleanser
    from magnetic_field_research import (
        research_heritage_site_magnetic_field, update_site_magnetic_field
    )
    AUDIT_AVAILABLE = True
except ImportError as e:
    print(f"Error: {e}")
    AUDIT_AVAILABLE = False


def berengaria_magnetic_audit():
    """
    First collection run: Berengaria Hotel Magnetic Audit
    
    The Architect Brother's perspective:
    - Field Strength: 45,000 nT (Estimated)
    - Field Anomaly: High (Separation detected)
    - Pole Alignment: Shifting / Transitional
    - Field Resonance: 0.3 (Low symbiosis)
    """
    
    if not AUDIT_AVAILABLE:
        print("Error: Audit system not available")
        return
    
    print("=" * 80)
    print("BERENGARIA HOTEL MAGNETIC AUDIT")
    print("The Real Racon - Magnetic Blueprint of the Miracle")
    print("=" * 80)
    print()
    
    # Step 1: Register the site
    print("Step 1: Registering Berengaria Hotel...")
    site_id = register_heritage_site(
        site_name="Berengaria Hotel",
        site_type="Hotel",
        region="Troodos Mountains",
        country="Cyprus",
        coordinates_lat=34.9167,
        coordinates_lon=32.8333,
        timeline_dimension=TimelineDimension.PRIMARY.value,
        time_period=TimePeriod.MODERN.value,
        year_established=1930,
        year_abandoned=1984,
        current_status="abandoned",
        law_41_compliant=False,
        requires_cleansing=True
    )
    print(f"  [OK] Site registered: ID {site_id}")
    
    # Step 2: Archive original narrative (Shell)
    print()
    print("Step 2: Archiving original narrative (Shell)...")
    original_narrative = """
    The abandoned Berengaria Hotel in the Troodos Mountains of Cyprus is one of the most 
    haunted places on the island. Built in 1930, this once-grand hotel was abandoned in 1984 
    and has since become a magnet for ghost stories. Visitors report seeing the ghost of a 
    merchant's wife who committed suicide, appearing as a "White Lady" at dusk. The hotel 
    is said to be cursed, with locals avoiding it after dark. This is the "Shell" - the 
    haunted narrative that feeds dark energy loops.
    """
    
    add_heritage_narrative(
        site_id=site_id,
        narrative_content=original_narrative,
        narrative_type="original",
        timeline_dimension=TimelineDimension.PRIMARY.value,
        violation_type="haunted_exploitation",
        dark_energy_detected=True,
        regeneration_applied=False
    )
    print("  [OK] Original narrative archived (Shell)")
    
    # Step 3: Cleanse and regenerate (Seed)
    print()
    print("Step 3: Cleansing narrative and revealing Seed...")
    cleanser = HeritageCleanser(timeline_dimension=TimelineDimension.PRIMARY.value)
    cleansed, analysis = cleanser.cleanse_content(
        content=original_narrative,
        source="Berengaria Hotel Magnetic Audit",
        site_type="Hotel",
        region="Troodos Mountains",
        country="Cyprus",
        year_established=1930,
        year_abandoned=1984,
        time_period=TimePeriod.MODERN.value
    )
    
    print(f"  [OK] Law 41 Compliant: {analysis['law_41_compliant']}")
    print(f"  [OK] Violation Type: {analysis.get('violation_type', 'None')}")
    print(f"  [OK] Regeneration Applied: {analysis.get('regeneration_suggestion') is not None}")
    
    # Step 4: Magnetic Field Research
    print()
    print("Step 4: Researching Magnetic Field (The Real Racon)...")
    print("  Field Strength: 45,000 nT (Estimated)")
    print("  Declination: 5.2° (Cyprus region)")
    print("  Inclination: 55.3° (Mediterranean)")
    
    magnetic_research = research_heritage_site_magnetic_field(
        site_id=site_id,
        field_strength=45000,  # nT - Estimated for Cyprus
        declination=5.2,        # degrees - Cyprus magnetic declination
        inclination=55.3       # degrees - Mediterranean inclination
    )
    
    print()
    print("  Magnetic Field Analysis:")
    print(f"    Field Resonance: {magnetic_research['field_resonance']:.2f} (Low symbiosis - Original Error detected)")
    print(f"    Pole Alignment: {magnetic_research['pole_alignment']} (Transitional - moving from Shell to Seed)")
    print(f"    Polarity State: {magnetic_research['polarity_state']}")
    print(f"    Field Anomaly: {magnetic_research['field_anomaly_detected']}")
    if magnetic_research['field_anomaly_detected']:
        print(f"    Anomaly Description: {magnetic_research['field_anomaly_description']}")
    print(f"    Field Space Resonance: {magnetic_research['field_space_resonance']:.2f}")
    print(f"    Field Space Energy: {magnetic_research['field_space_energy_level']:.2f}")
    
    # Step 5: Update site with magnetic data
    print()
    print("Step 5: Updating site with magnetic field data...")
    update_site_magnetic_field(site_id, magnetic_research)
    print("  [OK] Site updated with magnetic blueprint")
    
    # Step 6: The Real Racon - Analysis
    print()
    print("=" * 80)
    print("THE REAL RACON - MAGNETIC BLUEPRINT ANALYSIS")
    print("=" * 80)
    print()
    print("The Berengaria Hotel isn't just 'haunted'—its Field Resonance is out of sync")
    print("with Earth's heartbeat. The Original Error (separation from Earth) has")
    print("physically manifested as a magnetic anomaly.")
    print()
    print("Magnetic Blueprint:")
    print(f"  - Field Resonance: {magnetic_research['field_resonance']:.2f}/1.0")
    print(f"    -> Low symbiosis = Separation from Earth detected")
    print(f"    -> The 'Ghost' is actually a magnetic loop of unresolved history")
    print()
    print(f"  - Pole Alignment: {magnetic_research['pole_alignment']}")
    print(f"    -> Transitional = Moving from 'Abandoned' to 'Sanctuary'")
    print(f"    -> The narrative is shifting from Shell to Seed")
    print()
    print(f"  - Field Space Resonance: {magnetic_research['field_space_resonance']:.2f}/1.0")
    print(f"    -> Everything In Between = The spiritual battle space")
    print(f"    -> This is where regeneration happens")
    print()
    print("The Fix:")
    print("  Inject Day 1 (Do) frequency to raise resonance.")
    print("  Transform 'Haunted Hotel' -> 'Sovereign Temple of the Troodos Mountains'")
    print("  Honor Law 41: Respect the Abandoned")
    print()
    print("Field Space Philosophy:")
    print(f"  {magnetic_research['field_space_philosophy'][:200]}...")
    print()
    print("=" * 80)
    print("[SUCCESS] MAGNETIC AUDIT COMPLETE")
    print("=" * 80)
    print()
    print("PEACE, LOVE, UNITY")
    print("ENERGY + LOVE = WE ALL WIN")
    
    return {
        "site_id": site_id,
        "magnetic_research": magnetic_research,
        "analysis": analysis
    }


if __name__ == "__main__":
    result = berengaria_magnetic_audit()
    if result:
        print("\nAudit Result:")
        print(json.dumps({
            "site_id": result["site_id"],
            "field_resonance": result["magnetic_research"]["field_resonance"],
            "pole_alignment": result["magnetic_research"]["pole_alignment"],
            "field_space_resonance": result["magnetic_research"]["field_space_resonance"]
        }, indent=2))
