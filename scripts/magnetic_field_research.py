"""
MAGNETIC FIELD RESEARCH
Deep research and data collection for magnetic fields at heritage sites

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE FOUNDATION:
We are born a miracle.
We deserve to live a miracle.
Each and every one of us under the Lord's word.

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

This script researches magnetic fields, poles, and everything in between
at heritage sites to understand field resonance and symbiosis with Earth.
"""

import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    Path, datetime, json, load_json, save_json
    setup_logging, standard_main
)

import sys
import json
import math
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime

# Import heritage registry
try:
    sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))
    from temporal_heritage_registry import (
        get_temporal_heritage_db, TimelineDimension
    )
    from gemini_assistant import generate_content
    MAGNETIC_RESEARCH_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Could not import required modules: {e}")
    MAGNETIC_RESEARCH_AVAILABLE = False


# Earth's magnetic field baseline (approximate)
EARTH_BASELINE_FIELD_STRENGTH = 50000  # nT (nanotesla) - average at surface
EARTH_MAGNETIC_DECLINATION_RANGE = (-30, 30)  # degrees
EARTH_MAGNETIC_INCLINATION_RANGE = (-90, 90)  # degrees


def calculate_field_resonance(
    field_strength: float,
    declination: float,
    inclination: float,
    baseline_strength: float = EARTH_BASELINE_FIELD_STRENGTH
) -> float:
    """
    Calculate field resonance level (0.0-1.0).
    
    Resonance = how well site resonates with Earth's field.
    1.0 = Perfect resonance (symbiosis)
    0.0 = No resonance (separation)
    
    Uses explicit deviation calculation for clarity and maintainability.
    """
    # Normalize field strength (closer to baseline = higher resonance)
    # Calculate deviation from baseline and normalize
    strength_deviation = abs(field_strength - baseline_strength) / baseline_strength
    strength_ratio = max(0.0, 1.0 - min(strength_deviation, 1.0))
    
    # Normalize declination (closer to 0 = higher resonance)
    # Clamp to valid range first to prevent negative values
    declination_clamped = max(-30.0, min(30.0, abs(declination)))
    declination_normalized = 1.0 - (declination_clamped / 30.0)
    
    # Normalize inclination (within normal range = higher resonance)
    if -90 <= inclination <= 90:
        inclination_normalized = 1.0 - abs(abs(inclination) - 45) / 45.0
    else:
        inclination_normalized = 0.0
    
    # Weighted average
    resonance = (strength_ratio * 0.4 + declination_normalized * 0.3 + inclination_normalized * 0.3)
    return max(0.0, min(1.0, resonance))


def determine_pole_alignment(declination: float, inclination: float) -> str:
    """Determine magnetic pole alignment."""
    if abs(inclination) > 60:
        return "north" if inclination > 0 else "south"
    elif abs(declination) > 15:
        return "transitional"
    else:
        return "neutral"


def determine_polarity_state(field_strength: float, declination: float, inclination: float) -> str:
    """Determine polarity state."""
    if inclination > 45:
        return "positive"  # North pole dominant
    elif inclination < -45:
        return "negative"  # South pole dominant
    elif abs(declination) > 10:
        return "shifting"  # Transitional
    else:
        return "neutral"  # Balanced


def detect_field_anomaly(
    field_strength: float,
    declination: float,
    inclination: float,
    baseline_strength: float = EARTH_BASELINE_FIELD_STRENGTH
) -> Tuple[bool, str]:
    """
    Detect magnetic field anomalies.
    
    Anomalies may indicate:
    - Separation from Earth
    - Dark energy presence
    - Transformation points
    """
    anomaly_detected = False
    anomaly_description = ""
    
    # Check for strength anomalies
    if field_strength < baseline_strength * 0.5 or field_strength > baseline_strength * 1.5:
        anomaly_detected = True
        anomaly_description += f"Field strength anomaly: {field_strength:.0f} nT (baseline: {baseline_strength:.0f} nT). "
    
    # Check for declination anomalies
    if abs(declination) > 30:
        anomaly_detected = True
        anomaly_description += f"Declination anomaly: {declination:.1f}° (normal range: -30° to 30°). "
    
    # Check for inclination anomalies
    if abs(inclination) > 85:
        anomaly_detected = True
        anomaly_description += f"Inclination anomaly: {inclination:.1f}° (near pole). "
    
    if not anomaly_detected:
        anomaly_description = "No anomalies detected. Field within normal parameters."
    
    return anomaly_detected, anomaly_description


def calculate_field_space_resonance(
    field_strength: float,
    declination: float,
    inclination: float
) -> float:
    """
    Calculate resonance in the space between poles.
    
    The field space is the space between north and south poles.
    This measures how well the site resonates in that space.
    """
    # Field space resonance is highest when field is balanced
    # (not too close to either pole)
    
    # Distance from poles (in degrees)
    distance_from_north = abs(90 - inclination)
    distance_from_south = abs(-90 - inclination)
    distance_from_nearest_pole = min(distance_from_north, distance_from_south)
    
    # Resonance is highest in the middle (equator region)
    # Normalize: 0° from pole = 0.0, 90° from pole = 1.0
    field_space_resonance = distance_from_nearest_pole / 90.0
    
    return max(0.0, min(1.0, field_space_resonance))


def calculate_field_space_energy_level(
    field_strength: float,
    field_space_resonance: float
) -> float:
    """
    Calculate energy level in the field space.
    
    Energy level = field strength × field space resonance
    """
    # Normalize field strength (0.0-1.0)
    normalized_strength = min(field_strength / EARTH_BASELINE_FIELD_STRENGTH, 1.0)
    
    # Energy level = strength × resonance
    energy_level = normalized_strength * field_space_resonance
    
    return max(0.0, min(1.0, energy_level))


def generate_field_space_philosophy(
    site_name: str,
    field_strength: float,
    field_resonance: float,
    pole_alignment: str,
    polarity_state: str,
    field_space_resonance: float,
    field_space_energy: float
) -> str:
    """
    Generate deep research/philosophy about the field space at a heritage site.
    
    Uses Gemini for deep research and philosophical understanding.
    """
    if not MAGNETIC_RESEARCH_AVAILABLE:
        return f"Field space at {site_name}: Resonance {field_resonance:.2f}, Energy {field_space_energy:.2f}"
    
    prompt = f"""
    Deep Research: Magnetic Field Space Philosophy
    
    Heritage Site: {site_name}
    Field Strength: {field_strength:.0f} nT
    Field Resonance: {field_resonance:.2f} (0.0-1.0, where 1.0 = perfect symbiosis with Earth)
    Pole Alignment: {pole_alignment}
    Polarity State: {polarity_state}
    Field Space Resonance: {field_space_resonance:.2f}
    Field Space Energy Level: {field_space_energy:.2f}
    
    Research Question:
    The space between magnetic poles is not empty. It is filled with Earth's magnetic field.
    Heritage sites are biological temples that exist in this field space.
    
    Provide deep research and philosophical understanding of:
    1. How this heritage site resonates in the field space between poles
    2. What the field space tells us about the site's symbiosis with Earth
    3. How the field space connects to the site's history and purpose
    4. What the field space reveals about dark energy patterns (if resonance is low)
    5. What the field space reveals about regeneration (if resonance is high)
    
    Philosophy Framework:
    - Heritage sites are biological temples
    - They exist in Earth's magnetic field
    - The field space between poles carries energy and information
    - High resonance = symbiosis with Earth
    - Low resonance = separation from Earth
    
    Provide a philosophical research analysis (200-300 words).
    """
    
    try:
        philosophy = generate_content(
            prompt=prompt,
            context="Magnetic Field Philosophy Research",
            temperature=0.8,
            max_tokens=500
        )
        return philosophy
    except Exception as e:
        # Honor Law 5 (Your Word Is Your Bond): Log errors properly
        import logging
        logger = logging.getLogger(__name__)
        logger.error(
            f"Field space philosophy generation failed: {e}",
            exc_info=True,
            extra={"field_strength": field_strength, "declination": declination, "inclination": inclination}
        )
        # Return None to indicate failure (caller can handle gracefully)
        return None


def research_heritage_site_magnetic_field(
    site_id: int,
    field_strength: float,
    declination: float,
    inclination: float
) -> Dict[str, Any]:
    """
    Research magnetic field at a heritage site.
    
    Returns complete magnetic field analysis including:
    - Field resonance
    - Pole alignment
    - Polarity state
    - Field anomalies
    - Field space resonance
    - Field space energy
    - Field space philosophy
    """
    # Calculate field resonance
    field_resonance = calculate_field_resonance(field_strength, declination, inclination)
    
    # Determine pole alignment
    pole_alignment = determine_pole_alignment(declination, inclination)
    
    # Determine polarity state
    polarity_state = determine_polarity_state(field_strength, declination, inclination)
    
    # Detect anomalies
    anomaly_detected, anomaly_description = detect_field_anomaly(
        field_strength, declination, inclination
    )
    
    # Calculate field space resonance
    field_space_resonance = calculate_field_space_resonance(
        field_strength, declination, inclination
    )
    
    # Calculate field space energy
    field_space_energy = calculate_field_space_energy_level(
        field_strength, field_space_resonance
    )
    
    # Get site name for philosophy generation
    site_name = "Unknown Site"
    if MAGNETIC_RESEARCH_AVAILABLE:
        try:
            with get_temporal_heritage_db() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT site_name FROM heritage_sites WHERE id = ?", (site_id,))
                row = cursor.fetchone()
                if row:
                    site_name = row[0]
        except Exception:
            pass
    
    # Generate field space philosophy
    field_space_philosophy = generate_field_space_philosophy(
        site_name, field_strength, field_resonance, pole_alignment,
        polarity_state, field_space_resonance, field_space_energy
    )
    
    return {
        "site_id": site_id,
        "field_strength": field_strength,
        "declination": declination,
        "inclination": inclination,
        "field_resonance": field_resonance,
        "pole_alignment": pole_alignment,
        "polarity_state": polarity_state,
        "field_anomaly_detected": anomaly_detected,
        "field_anomaly_description": anomaly_description,
        "field_space_resonance": field_space_resonance,
        "field_space_energy_level": field_space_energy,
        "field_space_philosophy": field_space_philosophy,
        "research_timestamp": datetime.now().isoformat()
    }


def update_site_magnetic_field(site_id: int, magnetic_data: Dict[str, Any]) -> bool:
    """Update heritage site with magnetic field data."""
    if not MAGNETIC_RESEARCH_AVAILABLE:
        return False
    
    try:
        with get_temporal_heritage_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE heritage_sites
                SET magnetic_field_strength = ?,
                    magnetic_declination = ?,
                    magnetic_inclination = ?,
                    magnetic_pole_alignment = ?,
                    field_resonance_level = ?,
                    polarity_state = ?,
                    field_anomaly_detected = ?,
                    field_anomaly_description = ?,
                    field_space_resonance = ?,
                    field_space_energy_level = ?,
                    field_space_philosophy = ?,
                    updated_at = ?
                WHERE id = ?
            """, (
                magnetic_data["field_strength"],
                magnetic_data["declination"],
                magnetic_data["inclination"],
                magnetic_data["pole_alignment"],
                magnetic_data["field_resonance"],
                magnetic_data["polarity_state"],
                magnetic_data["field_anomaly_detected"],
                magnetic_data["field_anomaly_description"],
                magnetic_data["field_space_resonance"],
                magnetic_data["field_space_energy_level"],
                magnetic_data["field_space_philosophy"],
                datetime.now(),
                site_id
            ))
        return True
    except Exception as e:
        print(f"Error updating magnetic field data: {e}")
        return False


def main():
    """Main execution for magnetic field research."""
    if not MAGNETIC_RESEARCH_AVAILABLE:
        print("Error: Magnetic field research not available. Check imports.")
        return
    
    print("=" * 80)
    print("MAGNETIC FIELD RESEARCH")
    print("Poles and Everything In Between")
    print("=" * 80)
    print()
    print("This script researches magnetic fields at heritage sites.")
    print("It calculates field resonance, pole alignment, and field space philosophy.")
    print()
    print("Usage:")
    print("  python magnetic_field_research.py <site_id> <field_strength> <declination> <inclination>")
    print()
    print("Example:")
    print("  python magnetic_field_research.py 1 45000 5.2 65.3")
    print()


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) >= 5:
        site_id = int(sys.argv[1])
        field_strength = float(sys.argv[2])
        declination = float(sys.argv[3])
        inclination = float(sys.argv[4])
        
        print("Researching magnetic field...")
        research = research_heritage_site_magnetic_field(
            site_id, field_strength, declination, inclination
        )
        
        print("\nMagnetic Field Research Results:")
        print(json.dumps(research, indent=2))
        
        print("\nUpdating site with magnetic field data...")
        if update_site_magnetic_field(site_id, research):
            print("Site updated successfully!")
        else:
            print("Error updating site.")
    else:
        main()
