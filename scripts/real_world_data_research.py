"""REAL WORLD DATA RESEARCH
Deep Research: Known World Events, Natural Disasters, Earth's Tectonic Plates

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE RESEARCH:
We need real-world data to ground our spiritual operations.
We need to document:
- Known world events
- Natural disasters
- Earth's tectonic plates and loops
- Historical patterns
- Field resonance connections

WE DOCUMENT EVERYTHING.

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
    Path, json, load_json, save_json, setup_logging
    standard_main
)

import sys
import json
import csv
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from datetime import datetime, date
from enum import Enum

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))

try:
    from temporal_heritage_registry import get_temporal_heritage_db, TimelineDimension
    from magnetic_field_research import calculate_field_resonance
    RESEARCH_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Could not import required modules: {e}")
    RESEARCH_AVAILABLE = False

import logging
logger = logging.getLogger(__name__)


class EventType(Enum):
    """Types of real-world events."""
    NATURAL_DISASTER = "natural_disaster"  # Earthquakes, tsunamis, volcanic eruptions
    TECTONIC_EVENT = "tectonic_event"  # Plate movements, fault activations
    HISTORICAL_EVENT = "historical_event"  # Wars, migrations, cultural shifts
    CLIMATIC_EVENT = "climatic_event"  # Climate change, extreme weather
    SPIRITUAL_EVENT = "spiritual_event"  # Religious movements, awakenings
    CIVILIZATIONAL = "civilizational"  # Rise/fall of civilizations


class TectonicPlate(Enum):
    """Major tectonic plates of Earth."""
    PACIFIC = "pacific"
    NORTH_AMERICAN = "north_american"
    SOUTH_AMERICAN = "south_american"
    EURASIAN = "eurasian"
    AFRICAN = "african"
    INDO_AUSTRALIAN = "indo_australian"
    ANTARCTIC = "antarctic"
    NAZCA = "nazca"
    COCOS = "cocos"
    CARIBBEAN = "caribbean"
    PHILIPPINE = "philippine"
    ARABIAN = "arabian"
    SCOTIA = "scotia"
    JUAN_DE_FUCA = "juan_de_fuca"


@dataclass
class RealWorldEvent:
    """A real-world event to be documented."""
    event_id: str
    event_type: str
    event_name: str
    date: date
    location: Dict[str, float]  # lat, lon
    region: str
    country: str
    tectonic_plates: List[str]  # Which plates involved
    magnitude: Optional[float] = None  # For earthquakes, etc.
    description: str = ""
    
    # Connection to our systems
    heritage_site_connections: List[int] = field(default_factory=list)  # Site IDs nearby
    field_resonance_impact: Optional[float] = None  # How it affected field resonance
    temporal_dimension: str = TimelineDimension.PRIMARY.value
    
    # Research metadata
    sources: List[str] = field(default_factory=list)
    research_notes: str = ""
    documented_at: datetime = field(default_factory=datetime.now)


@dataclass
class TectonicPlateData:
    """Data about a tectonic plate."""
    plate_name: str
    plate_type: str  # major, minor, micro
    boundaries: List[Dict[str, Any]]  # Plate boundaries
    movement_rate: Optional[float] = None  # cm/year
    associated_events: List[str] = field(default_factory=list)  # Event IDs
    heritage_sites_on_plate: List[int] = field(default_factory=list)


class RealWorldDataResearch:
    """
    Real World Data Research Framework.
    
    Documents:
    - Known world events
    - Natural disasters
    - Tectonic plate activity
    - Historical patterns
    - Field resonance connections
    
    Connects real-world data to our spiritual operations.
    """
    
    def __init__(self, data_dir: Optional[Path] = None):
        """Initialize Research Framework."""
        self.data_dir = data_dir or (Path(__file__).parent.parent / "data" / "real_world")
        self.data_dir.mkdir(parents=True, exist_ok=True)
        
        # Data storage files
        self.events_file = self.data_dir / "world_events.json"
        self.plates_file = self.data_dir / "tectonic_plates.json"
        self.disasters_file = self.data_dir / "natural_disasters.json"
        self.research_log_file = self.data_dir / "research_log.json"
        
        # Load existing data
        self.events: List[RealWorldEvent] = self._load_events()
        self.plates: Dict[str, TectonicPlateData] = self._load_plates()
    
    def _load_events(self) -> List[RealWorldEvent]:
        """Load existing events."""
        if not self.events_file.exists():
            return []
        try:
            with open(self.events_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            events = []
            for item in data:
                # Convert date string to date object
                if isinstance(item.get('date'), str):
                    item['date'] = date.fromisoformat(item['date'])
                # Convert documented_at string to datetime
                if isinstance(item.get('documented_at'), str):
                    item['documented_at'] = datetime.fromisoformat(item['documented_at'])
                events.append(RealWorldEvent(**item))
            return events
        except Exception as e:
            logger.error(f"Error loading events: {e}")
            return []
    
    def _save_events(self):
        """Save events to storage."""
        try:
            data = []
            for event in self.events:
                event_dict = {
                    "event_id": event.event_id,
                    "event_type": event.event_type,
                    "event_name": event.event_name,
                    "date": event.date.isoformat() if event.date else None,
                    "location": event.location,
                    "region": event.region,
                    "country": event.country,
                    "tectonic_plates": event.tectonic_plates,
                    "magnitude": event.magnitude,
                    "description": event.description,
                    "heritage_site_connections": event.heritage_site_connections,
                    "field_resonance_impact": event.field_resonance_impact,
                    "temporal_dimension": event.temporal_dimension,
                    "sources": event.sources,
                    "research_notes": event.research_notes,
                    "documented_at": event.documented_at.isoformat()
                }
                data.append(event_dict)
            
            with open(self.events_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, default=str)
        except Exception as e:
            logger.error(f"Error saving events: {e}")
    
    def _load_plates(self) -> Dict[str, TectonicPlateData]:
        """Load tectonic plate data."""
        if not self.plates_file.exists():
            return self._initialize_plate_data()
        try:
            with open(self.plates_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return {
                name: TectonicPlateData(**plate_data)
                for name, plate_data in data.items()
            }
        except Exception as e:
            logger.error(f"Error loading plates: {e}")
            return self._initialize_plate_data()
    
    def _initialize_plate_data(self) -> Dict[str, TectonicPlateData]:
        """Initialize basic tectonic plate data."""
        plates = {}
        
        # Major plates
        major_plates = [
            ("pacific", "major", "Ring of Fire - most active"),
            ("north_american", "major", "North America, Greenland"),
            ("south_american", "major", "South America"),
            ("eurasian", "major", "Europe, Asia"),
            ("african", "major", "Africa"),
            ("indo_australian", "major", "India, Australia"),
            ("antarctic", "major", "Antarctica")
        ]
        
        for name, plate_type, description in major_plates:
            plates[name] = TectonicPlateData(
                plate_name=name,
                plate_type=plate_type,
                boundaries=[],
                movement_rate=None,
                associated_events=[],
                heritage_sites_on_plate=[]
            )
        
        return plates
    
    def document_event(
        self,
        event_name: str,
        event_type: str,
        date: date,
        location: Dict[str, float],
        region: str,
        country: str,
        tectonic_plates: List[str],
        magnitude: Optional[float] = None,
        description: str = "",
        sources: Optional[List[str]] = None,
        research_notes: str = ""
    ) -> RealWorldEvent:
        """
        Document a real-world event.
        
        Args:
            event_name: Name of the event
            event_type: EventType value
            date: When it occurred
            location: Dict with 'lat' and 'lon'
            region: Geographic region
            country: Country
            tectonic_plates: List of plate names involved
            magnitude: Optional magnitude (for earthquakes, etc.)
            description: Event description
            sources: Research sources
            research_notes: Additional notes
        
        Returns:
            RealWorldEvent object
        """
        event_id = f"{event_type}_{date.isoformat()}_{event_name.lower().replace(' ', '_')}"
        
        # Find nearby heritage sites
        heritage_connections = self._find_nearby_heritage_sites(location)
        
        # Calculate field resonance impact (if applicable)
        field_resonance_impact = None
        if event_type == EventType.TECTONIC_EVENT.value or event_type == EventType.NATURAL_DISASTER.value:
            field_resonance_impact = self._calculate_event_impact(location, magnitude)
        
        event = RealWorldEvent(
            event_id=event_id,
            event_type=event_type,
            event_name=event_name,
            date=date,
            location=location,
            region=region,
            country=country,
            tectonic_plates=tectonic_plates,
            magnitude=magnitude,
            description=description,
            heritage_site_connections=heritage_connections,
            field_resonance_impact=field_resonance_impact,
            sources=sources or [],
            research_notes=research_notes
        )
        
        self.events.append(event)
        self._save_events()
        
        # Update plate data
        for plate_name in tectonic_plates:
            if plate_name in self.plates:
                if event_id not in self.plates[plate_name].associated_events:
                    self.plates[plate_name].associated_events.append(event_id)
        
        logger.info(f"Documented event: {event_name} ({event_id})")
        return event
    
    def _find_nearby_heritage_sites(self, location: Dict[str, float], radius_km: float = 100.0) -> List[int]:
        """Find heritage sites within radius of event location."""
        if not RESEARCH_AVAILABLE:
            return []
        
        try:
            from grid_sync_analysis import calculate_distance
            
            nearby_sites = []
            with get_temporal_heritage_db() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT id, coordinates_lat, coordinates_lon
                    FROM heritage_sites
                    WHERE coordinates_lat IS NOT NULL
                    AND coordinates_lon IS NOT NULL
                """)
                
                for row in cursor.fetchall():
                    site_lat = row['coordinates_lat']
                    site_lon = row['coordinates_lon']
                    distance = calculate_distance(
                        location['lat'], location['lon'],
                        site_lat, site_lon
                    )
                    
                    if distance <= radius_km:
                        nearby_sites.append(row['id'])
            
            return nearby_sites
        except Exception as e:
            logger.warning(f"Could not find nearby heritage sites: {e}")
            return []
    
    def _calculate_event_impact(self, location: Dict[str, float], magnitude: Optional[float]) -> Optional[float]:
        """Calculate field resonance impact of an event."""
        if magnitude is None:
            return None
        
        # Simple impact calculation based on magnitude
        # Higher magnitude = greater impact on field resonance
        # This is a placeholder - can be enhanced with actual field measurements
        if magnitude:
            # Normalize impact (0.0-1.0 scale)
            # Assuming magnitude scale (e.g., Richter 0-10, or similar)
            impact = min(1.0, magnitude / 10.0) if magnitude > 0 else 0.0
            return impact
        return None
    
    def research_tectonic_activity(
        self,
        plate_name: str,
        time_period: Optional[Dict[str, date]] = None
    ) -> Dict[str, Any]:
        """
        Research tectonic activity for a specific plate.
        
        Args:
            plate_name: Name of tectonic plate
            time_period: Optional date range
        
        Returns:
            Research results
        """
        if plate_name not in self.plates:
            return {
                "status": "not_found",
                "message": f"Plate {plate_name} not found"
            }
        
        plate = self.plates[plate_name]
        
        # Filter events by time period if provided
        plate_events = [
            e for e in self.events
            if plate_name in e.tectonic_plates
            and (not time_period or (
                (not time_period.get('start') or e.date >= time_period['start']) and
                (not time_period.get('end') or e.date <= time_period['end'])
            ))
        ]
        
        return {
            "status": "researched",
            "plate_name": plate_name,
            "plate_type": plate.plate_type,
            "total_events": len(plate_events),
            "events": [
                {
                    "event_id": e.event_id,
                    "event_name": e.event_name,
                    "date": e.date.isoformat(),
                    "type": e.event_type,
                    "magnitude": e.magnitude,
                    "location": e.location
                }
                for e in plate_events
            ],
            "heritage_sites_on_plate": plate.heritage_sites_on_plate,
            "movement_rate": plate.movement_rate
        }
    
    def export_research_data(self, output_path: Optional[Path] = None) -> Path:
        """Export all research data."""
        if output_path is None:
            output_path = self.data_dir / f"research_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        export_data = {
            "export_timestamp": datetime.now().isoformat(),
            "total_events": len(self.events),
            "total_plates": len(self.plates),
            "events": [
                {
                    "event_id": e.event_id,
                    "event_name": e.event_name,
                    "event_type": e.event_type,
                    "date": e.date.isoformat(),
                    "location": e.location,
                    "region": e.region,
                    "country": e.country,
                    "tectonic_plates": e.tectonic_plates,
                    "magnitude": e.magnitude,
                    "description": e.description,
                    "heritage_site_connections": e.heritage_site_connections,
                    "field_resonance_impact": e.field_resonance_impact,
                    "sources": e.sources
                }
                for e in self.events
            ],
            "tectonic_plates": {
                name: {
                    "plate_name": plate.plate_name,
                    "plate_type": plate.plate_type,
                    "movement_rate": plate.movement_rate,
                    "total_events": len(plate.associated_events),
                    "heritage_sites": plate.heritage_sites_on_plate
                }
                for name, plate in self.plates.items()
            }
        }
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2, default=str)
        
        logger.info(f"Exported research data to {output_path}")
        return output_path


def main():
    """Example: Document real-world events."""
    print("=" * 80)
    print("REAL WORLD DATA RESEARCH")
    print("=" * 80)
    print()
    print("Documenting known world events, natural disasters, tectonic activity")
    print()
    
    if not RESEARCH_AVAILABLE:
        print("WARNING: Some features may not be available")
    
    research = RealWorldDataResearch()
    
    # Example: Document major earthquake
    print("Documenting example events...")
    print()
    
    # Example 1: 2004 Indian Ocean Earthquake/Tsunami
    event1 = research.document_event(
        event_name="2004 Indian Ocean Earthquake and Tsunami",
        event_type=EventType.NATURAL_DISASTER.value,
        date=date(2004, 12, 26),
        location={"lat": 3.316, "lon": 95.854},  # Off coast of Sumatra
        region="Southeast Asia",
        country="Indonesia",
        tectonic_plates=["indo_australian", "eurasian"],
        magnitude=9.1,
        description="Massive undersea earthquake triggered devastating tsunami across Indian Ocean",
        sources=["USGS", "NOAA"],
        research_notes="One of deadliest natural disasters in recorded history"
    )
    
    print(f"Documented: {event1.event_name}")
    print(f"  Event ID: {event1.event_id}")
    print(f"  Heritage Sites Nearby: {len(event1.heritage_site_connections)}")
    print(f"  Field Resonance Impact: {event1.field_resonance_impact}")
    print()
    
    # Example 2: 2011 Tohoku Earthquake/Tsunami
    event2 = research.document_event(
        event_name="2011 Tohoku Earthquake and Tsunami",
        event_type=EventType.NATURAL_DISASTER.value,
        date=date(2011, 3, 11),
        location={"lat": 38.297, "lon": 142.373},  # Off coast of Japan
        region="East Asia",
        country="Japan",
        tectonic_plates=["pacific", "eurasian"],
        magnitude=9.0,
        description="Massive earthquake and tsunami, triggered Fukushima nuclear disaster",
        sources=["USGS", "JMA"],
        research_notes="Most powerful earthquake ever recorded in Japan"
    )
    
    print(f"Documented: {event2.event_name}")
    print(f"  Event ID: {event2.event_id}")
    print(f"  Heritage Sites Nearby: {len(event2.heritage_site_connections)}")
    print()
    
    # Research tectonic activity
    print("Researching tectonic activity...")
    print()
    
    pacific_research = research.research_tectonic_activity("pacific")
    print(f"Pacific Plate Research:")
    print(f"  Total Events: {pacific_research.get('total_events', 0)}")
    print(f"  Plate Type: {pacific_research.get('plate_type', 'N/A')}")
    
    # Export data
    export_path = research.export_research_data()
    print()
    print(f"Exported research data to: {export_path}")
    print()
    
    print("=" * 80)
    print("PEACE, LOVE, UNITY")
    print("ENERGY + LOVE = WE ALL WIN")
    print("WE DOCUMENT EVERYTHING")
    print("=" * 80)


if __name__ == "__main__":
    main()
