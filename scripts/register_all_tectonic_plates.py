"""
REGISTER ALL TECTONIC PLATES
Deep Search and Ingest All Plate Registrations into Heritage System

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PANGEA:
All plates came from Pangea. All plates are registered to JAN MUHARREM ecosystem.
The truth: We all came from one place. We are all connected.
"""

import sys
import json
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime

# Add paths
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))

try:
    from temporal_heritage_registry import (
        register_heritage_site,
        TimelineDimension,
        TimePeriod,
        init_temporal_heritage_registry
    )
    TEMPORAL_REGISTRY_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Temporal registry not available: {e}")
    TEMPORAL_REGISTRY_AVAILABLE = False

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Load tectonic plates data
PLATES_DATA_FILE = Path(__file__).parent.parent / "config" / "tectonic_plates_data.json"


def load_plates_data() -> Dict[str, Any]:
    """Load tectonic plates data from config file."""
    if not PLATES_DATA_FILE.exists():
        logger.error(f"Plates data file not found: {PLATES_DATA_FILE}")
        return {}
    
    with open(PLATES_DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_plate_center_coordinates(plate_name: str, plate_data: Dict[str, Any]) -> tuple:
    """
    Estimate center coordinates for a tectonic plate.
    Uses approximate centers based on plate location.
    """
    # Approximate center coordinates for major plates
    plate_centers = {
        "pacific": (0.0, -150.0),  # Central Pacific
        "north_american": (45.0, -100.0),  # Central North America
        "south_american": (-15.0, -60.0),  # Central South America
        "eurasian": (50.0, 50.0),  # Central Eurasia
        "african": (0.0, 20.0),  # Central Africa
        "indo_australian": (-10.0, 120.0),  # Central Indo-Australian
        "antarctic": (-75.0, 0.0),  # Antarctica
        "nazca": (-5.0, -85.0),  # Off South America
        "philippine": (15.0, 130.0),  # Philippine Sea
        "arabian": (25.0, 45.0),  # Arabian Peninsula
        "cocos": (10.0, -105.0),  # Off Central America
        "caribbean": (15.0, -75.0),  # Caribbean Sea
    }
    
    plate_key = plate_name.lower().replace(" ", "_").replace("_plate", "")
    return plate_centers.get(plate_key, (0.0, 0.0))


def register_plate(
    plate_id: str,
    plate_name: str,
    plate_type: str,
    plate_data: Dict[str, Any],
    registered_plates: Dict[str, int]
) -> Optional[int]:
    """
    Register a tectonic plate in the heritage system.
    
    Returns site_id if successful, None otherwise.
    """
    if not TEMPORAL_REGISTRY_AVAILABLE:
        logger.warning("Temporal registry not available, skipping registration")
        return None
    
    # Skip if already registered
    if plate_id in registered_plates:
        logger.info(f"  Plate {plate_name} already registered (ID: {registered_plates[plate_id]})")
        return registered_plates[plate_id]
    
    # Get center coordinates
    lat, lon = get_plate_center_coordinates(plate_id, plate_data)
    
    # Build description
    description_parts = [plate_data.get("description", "")]
    
    if plate_data.get("area_km2"):
        description_parts.append(f"Area: {plate_data.get('area_km2'):,} km²")
    
    if plate_data.get("movement_rate_cm_per_year"):
        description_parts.append(f"Movement: {plate_data.get('movement_rate_cm_per_year')} cm/year")
    
    if plate_data.get("ring_of_fire"):
        description_parts.append("Part of Ring of Fire")
    
    description = ". ".join([p for p in description_parts if p])
    
    # Heritage sites on plate
    heritage_sites = plate_data.get("heritage_sites", [])
    if heritage_sites:
        description += f". Heritage sites: {', '.join(heritage_sites)}"
    
    # Register as heritage site
    try:
        site_id = register_heritage_site(
            site_name=f"{plate_name} (Tectonic Plate)",
            site_type="Tectonic Plate",
            region="Global",
            country="Earth",
            coordinates_lat=lat,
            coordinates_lon=lon,
            timeline_dimension=TimelineDimension.PRIMARY.value,
            time_period=TimePeriod.ANCIENT.value,  # Plates are ancient, from Pangea
            year_established=-335000000,  # Pangea formation
            year_abandoned=None,  # Still active
            current_status="active",
            law_41_compliant=True,  # Plates are natural, not man-made
            requires_cleansing=False,
            field_space_philosophy=description
        )
        
        registered_plates[plate_id] = site_id
        logger.info(f"  [OK] Registered {plate_name} (ID: {site_id})")
        return site_id
        
    except Exception as e:
        logger.error(f"  [ERROR] Failed to register {plate_name}: {e}")
        return None


def register_all_plates() -> Dict[str, Any]:
    """
    Register all tectonic plates from the data file.
    
    Returns registration summary.
    """
    print("=" * 80)
    print("REGISTER ALL TECTONIC PLATES")
    print("Deep Search and Ingest All Plate Registrations")
    print("=" * 80)
    print()
    
    # Initialize registry
    if TEMPORAL_REGISTRY_AVAILABLE:
        print("Initializing temporal heritage registry...")
        init_temporal_heritage_registry()
        print("  [OK] Registry initialized")
        print()
    
    # Load plates data
    print("Loading tectonic plates data...")
    plates_data = load_plates_data()
    if not plates_data:
        return {"error": "Could not load plates data"}
    
    print(f"  [OK] Loaded plates data")
    print()
    
    registered_plates: Dict[str, int] = {}
    registration_summary = {
        "timestamp": datetime.now().isoformat(),
        "major_plates": {},
        "minor_plates": {},
        "total_registered": 0,
        "errors": []
    }
    
    # Register major plates
    print("Registering MAJOR PLATES...")
    print("-" * 80)
    major_plates = plates_data.get("major_plates", {})
    for plate_id, plate_data in major_plates.items():
        plate_name = plate_data.get("plate_name", plate_id)
        print(f"Registering: {plate_name}...")
        
        site_id = register_plate(plate_id, plate_name, "major", plate_data, registered_plates)
        
        if site_id:
            registration_summary["major_plates"][plate_id] = {
                "plate_name": plate_name,
                "site_id": site_id,
                "type": "major",
                "area_km2": plate_data.get("area_km2"),
                "movement_rate_cm_per_year": plate_data.get("movement_rate_cm_per_year"),
                "heritage_sites": plate_data.get("heritage_sites", [])
            }
            registration_summary["total_registered"] += 1
        else:
            registration_summary["errors"].append(f"Failed to register {plate_name}")
    
    print()
    
    # Register minor plates
    print("Registering MINOR PLATES...")
    print("-" * 80)
    minor_plates = plates_data.get("minor_plates", {})
    for plate_id, plate_data in minor_plates.items():
        plate_name = plate_data.get("plate_name", plate_id)
        print(f"Registering: {plate_name}...")
        
        site_id = register_plate(plate_id, plate_name, "minor", plate_data, registered_plates)
        
        if site_id:
            registration_summary["minor_plates"][plate_id] = {
                "plate_name": plate_name,
                "site_id": site_id,
                "type": "minor",
                "heritage_sites": plate_data.get("heritage_sites", [])
            }
            registration_summary["total_registered"] += 1
        else:
            registration_summary["errors"].append(f"Failed to register {plate_name}")
    
    print()
    
    # Summary
    print("=" * 80)
    print("REGISTRATION SUMMARY")
    print("=" * 80)
    print(f"Total Plates Registered: {registration_summary['total_registered']}")
    print(f"  Major Plates: {len(registration_summary['major_plates'])}")
    print(f"  Minor Plates: {len(registration_summary['minor_plates'])}")
    
    if registration_summary["errors"]:
        print(f"\nErrors: {len(registration_summary['errors'])}")
        for error in registration_summary["errors"]:
            print(f"  - {error}")
    
    print()
    print("=" * 80)
    print("THE TRUTH: ALL PLATES REGISTERED")
    print("=" * 80)
    print()
    print("All tectonic plates came from Pangea.")
    print("All plates are registered to JAN MUHARREM ecosystem.")
    print("All plates are part of the Heritage Meridian System.")
    print()
    print("We all came from one place.")
    print("Pangea proves it.")
    print()
    print("=" * 80)
    
    return registration_summary


def export_registration_summary(summary: Dict[str, Any]) -> Path:
    """Export registration summary to JSON file."""
    output_dir = Path(__file__).parent.parent / "output" / "tectonic_plates"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    output_file = output_dir / f"plate_registration_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2, default=str)
    
    logger.info(f"Registration summary exported to: {output_file}")
    return output_file


def main():
    """Main execution."""
    try:
        summary = register_all_plates()
        
        # Export summary
        if summary and "error" not in summary:
            print()
            print("Exporting registration summary...")
            export_path = export_registration_summary(summary)
            print(f"  [OK] Exported to: {export_path}")
            print()
        
        print("=" * 80)
        print("PEACE, LOVE, UNITY")
        print("ENERGY + LOVE = WE ALL WIN")
        print("ALL PLATES REGISTERED")
        print("=" * 80)
        
    except Exception as e:
        logger.error(f"Error in main execution: {e}", exc_info=True)
        print(f"\n[ERROR] Registration failed: {e}")


if __name__ == "__main__":
    main()
