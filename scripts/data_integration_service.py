"""
DATA INTEGRATION SERVICE
Multi-Source Data Aggregation for World History

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

DATA INTEGRATION SERVICE:
Aggregates data from multiple sources for world history display:
- Heritage database (temporal heritage registry)
- Real-world events (USGS, NASA, UNESCO)
- Spiritual contracts (spiritual contracts registry)
- Life audits (markdown files)
- Divine Frequency (calculated)
"""

import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    Path, datetime, json, setup_logging, standard_main
)

import sys
import json
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime
from dataclasses import dataclass, field, asdict, fields
from enum import Enum
import logging

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent))

try:
    from temporal_heritage_registry import TemporalHeritageRegistry, get_temporal_heritage_db
    TEMPORAL_HERITAGE_AVAILABLE = True
except ImportError:
    TEMPORAL_HERITAGE_AVAILABLE = False

try:
    from spiritual_contracts_registry import SpiritualContractsRegistry
    SPIRITUAL_CONTRACTS_AVAILABLE = True
except ImportError:
    SPIRITUAL_CONTRACTS_AVAILABLE = False

try:
    from divine_frequency import DivineFrequencySystem
    DIVINE_FREQUENCY_AVAILABLE = True
except ImportError:
    DIVINE_FREQUENCY_AVAILABLE = False

logger = logging.getLogger(__name__)


class DataSourceType(Enum):
    """Type of data source."""
    DATABASE = "database"
    API = "api"
    JSON = "json"
    MARKDOWN = "markdown"
    CALCULATED = "calculated"


@dataclass
class DataSource:
    """Data source configuration."""
    source_id: str
    source_name: str
    source_type: str
    connection_string: Optional[str] = None
    api_endpoint: Optional[str] = None
    file_path: Optional[str] = None
    is_active: bool = True
    last_sync: Optional[str] = None
    sync_interval: int = 3600  # seconds
    notes: str = ""


@dataclass
class AggregatedEvent:
    """Aggregated timeline event from multiple sources."""
    event_id: str
    title: str
    description: str
    year_occurred: int
    year_precision: str
    event_type: str
    field_resonance: float
    location: Dict[str, float]
    timeline_dimension: str
    sources: List[str]  # Source IDs that contributed to this event
    narrative: str
    metadata: Dict[str, Any] = field(default_factory=dict)
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())


class DataIntegrationService:
    """Service for aggregating data from multiple sources."""
    
    def __init__(self):
        """Initialize the data integration service."""
        self.data_sources: Dict[str, DataSource] = {}
        self.heritage_registry = TemporalHeritageRegistry() if TEMPORAL_HERITAGE_AVAILABLE else None
        self.contracts_registry = SpiritualContractsRegistry() if SPIRITUAL_CONTRACTS_AVAILABLE else None
        self.frequency_system = DivineFrequencySystem() if DIVINE_FREQUENCY_AVAILABLE else None
        self._register_data_sources()
    
    def _register_data_sources(self):
        """Register all data sources."""
        # Heritage Database
        if TEMPORAL_HERITAGE_AVAILABLE:
            self._register_source(
                source_id="heritage_db",
                source_name="Temporal Heritage Registry",
                source_type=DataSourceType.DATABASE.value,
                connection_string="temporal_heritage_registry.db",
                notes="Heritage sites across timelines"
            )
        
        # Spiritual Contracts
        if SPIRITUAL_CONTRACTS_AVAILABLE:
            self._register_source(
                source_id="spiritual_contracts",
                source_name="Spiritual Contracts Registry",
                source_type=DataSourceType.JSON.value,
                file_path="config/spiritual_contracts.json",
                notes="Spiritual contracts and battlefields"
            )
        
        # Divine Frequency
        if DIVINE_FREQUENCY_AVAILABLE:
            self._register_source(
                source_id="divine_frequency",
                source_name="Divine Frequency System",
                source_type=DataSourceType.CALCULATED.value,
                notes="Calculated Divine Frequency from field resonance, spiritual alignment, unity connection"
            )
        
        # Real-world events (placeholder for future API integration)
        self._register_source(
            source_id="real_world_events",
            source_name="Real World Events",
            source_type=DataSourceType.API.value,
            api_endpoint="https://api.example.com/events",
            is_active=False,  # Not yet implemented
            notes="USGS earthquakes, NASA data, UNESCO heritage (future integration)"
        )
        
        # Life audits (placeholder for markdown files)
        self._register_source(
            source_id="life_audits",
            source_name="Life Audits",
            source_type=DataSourceType.MARKDOWN.value,
            file_path="data/life_audits/",
            is_active=False,  # Not yet implemented
            notes="Markdown files with life audit data (future integration)"
        )
    
    def _register_source(
        self,
        source_id: str,
        source_name: str,
        source_type: str,
        connection_string: Optional[str] = None,
        api_endpoint: Optional[str] = None,
        file_path: Optional[str] = None,
        is_active: bool = True,
        notes: str = ""
    ):
        """Register a data source."""
        source = DataSource(
            source_id=source_id,
            source_name=source_name,
            source_type=source_type,
            connection_string=connection_string,
            api_endpoint=api_endpoint,
            file_path=file_path,
            is_active=is_active,
            notes=notes
        )
        self.data_sources[source_id] = source
        logger.info(f"Registered data source: {source_name} ({source_type})")
    
    async def aggregate_timeline_data(
        self,
        start_year: Optional[int] = None,
        end_year: Optional[int] = None,
        region: Optional[str] = None,
        event_type: Optional[str] = None
    ) -> List[AggregatedEvent]:
        """
        Aggregate timeline data from all active sources.
        
        Merges events from:
        - Heritage sites (temporal heritage registry)
        - Spiritual events (spiritual contracts)
        - Real-world events (APIs - future)
        - Calculated events (Divine Frequency milestones)
        """
        all_events: List[AggregatedEvent] = []
        
        # Fetch from heritage database
        if self.heritage_registry and "heritage_db" in self.data_sources:
            heritage_events = await self._fetch_heritage_events(start_year, end_year, region)
            all_events.extend(heritage_events)
        
        # Fetch from spiritual contracts
        if self.contracts_registry and "spiritual_contracts" in self.data_sources:
            spiritual_events = await self._fetch_spiritual_events(start_year, end_year)
            all_events.extend(spiritual_events)
        
        # Fetch from real-world APIs (future)
        if "real_world_events" in self.data_sources and self.data_sources["real_world_events"].is_active:
            real_world_events = await self._fetch_real_world_events(start_year, end_year, region)
            all_events.extend(real_world_events)
        
        # Add Divine Frequency milestones
        if self.frequency_system and "divine_frequency" in self.data_sources:
            frequency_events = await self._fetch_frequency_milestones()
            all_events.extend(frequency_events)
        
        # Merge and deduplicate events
        merged_events = self._merge_events(all_events)
        
        # Sort by year
        merged_events.sort(key=lambda e: e.year_occurred)
        
        # Filter by event type if specified
        if event_type:
            merged_events = [e for e in merged_events if e.event_type == event_type]
        
        return merged_events
    
    async def _fetch_heritage_events(
        self,
        start_year: Optional[int],
        end_year: Optional[int],
        region: Optional[str]
    ) -> List[AggregatedEvent]:
        """Fetch events from heritage database."""
        events = []
        
        try:
            with get_temporal_heritage_db() as conn:
                cursor = conn.cursor()
                query = "SELECT * FROM heritage_sites WHERE 1=1"
                params = []
                
                if start_year:
                    query += " AND (year_established >= ? OR year_established IS NULL)"
                    params.append(start_year)
                if end_year:
                    query += " AND (year_established <= ? OR year_established IS NULL)"
                    params.append(end_year)
                if region:
                    query += " AND region = ?"
                    params.append(region)
                
                cursor.execute(query, params)
                sites = cursor.fetchall()
                
                for site in sites:
                    import hashlib
                    event_id = f"heritage_{hashlib.sha256(f'{site['site_name']}_{site.get('id', 0)}'.encode()).hexdigest()[:8]}"
                    
                    event = AggregatedEvent(
                        event_id=event_id,
                        title=site['site_name'],
                        description=f"Heritage site: {site['site_name']}",
                        year_occurred=site.get('year_established', 0) or 0,
                        year_precision="exact" if site.get('year_established') else "unknown",
                        event_type="heritage_site",
                        field_resonance=site.get('field_resonance_level', 0.5) or 0.5,
                        location={
                            "lat": site.get('coordinates_lat', 0.0) or 0.0,
                            "lon": site.get('coordinates_lon', 0.0) or 0.0
                        },
                        timeline_dimension=site.get('timeline_dimension', 'primary'),
                        sources=["heritage_db"],
                        narrative=f"Heritage site: {site['site_name']}. Field resonance: {site.get('field_resonance_level', 0.5)}. Connection to The Table."
                    )
                    events.append(event)
        except Exception as e:
            logger.error(f"Error fetching heritage events: {e}")
        
        return events
    
    async def _fetch_spiritual_events(
        self,
        start_year: Optional[int],
        end_year: Optional[int]
    ) -> List[AggregatedEvent]:
        """Fetch events from spiritual contracts."""
        events = []
        
        try:
            if hasattr(self.contracts_registry, 'contracts'):
                for contract_id, contract in self.contracts_registry.contracts.items():
                    # Extract year from contract if available
                    year = contract.get('year_occurred', 0) or 0
                    
                    if start_year and year < start_year:
                        continue
                    if end_year and year > end_year:
                        continue
                    
                    import hashlib
                    event_id = f"spiritual_{hashlib.sha256(contract_id.encode()).hexdigest()[:8]}"
                    
                    event = AggregatedEvent(
                        event_id=event_id,
                        title=contract.get('title', 'Spiritual Contract'),
                        description=contract.get('description', ''),
                        year_occurred=year,
                        year_precision="exact" if year else "unknown",
                        event_type="spiritual_contract",
                        field_resonance=0.8 if contract.get('dark_energy_detected') else 0.9,
                        location={
                            "lat": contract.get('location', {}).get('lat', 0.0) if isinstance(contract.get('location'), dict) else 0.0,
                            "lon": contract.get('location', {}).get('lon', 0.0) if isinstance(contract.get('location'), dict) else 0.0
                        },
                        timeline_dimension="spiritual",
                        sources=["spiritual_contracts"],
                        narrative=contract.get('narrative', 'Spiritual contract event.')
                    )
                    events.append(event)
        except Exception as e:
            logger.error(f"Error fetching spiritual events: {e}")
        
        return events
    
    async def _fetch_real_world_events(
        self,
        start_year: Optional[int],
        end_year: Optional[int],
        region: Optional[str]
    ) -> List[AggregatedEvent]:
        """Fetch events from real-world APIs (placeholder for future implementation)."""
        # Future implementation: USGS earthquakes, NASA data, UNESCO heritage
        return []
    
    async def _fetch_frequency_milestones(self) -> List[AggregatedEvent]:
        """Fetch Divine Frequency milestones."""
        events = []
        
        try:
            if self.frequency_system:
                # Add key frequency milestones
                milestones = [
                    {
                        "title": "Pangea Forms - Perfect Unity",
                        "year": -335000000,
                        "frequency": 1.0,
                        "narrative": "Pangea forms. Perfect unity. The Table is established. Divine Frequency at 1.0."
                    },
                    {
                        "title": "First Separation - The Original Error",
                        "year": -200000000,
                        "frequency": 0.95,
                        "narrative": "The Original Error begins. Dark energy exploitation. Divine Frequency drops to 0.95."
                    },
                    {
                        "title": "Memory of Unity Persists",
                        "year": 2026,
                        "frequency": 0.78,
                        "narrative": "Memory of unity persists at 0.78. The Table remembers. Restoration begins."
                    }
                ]
                
                for milestone in milestones:
                    import hashlib
                    event_id = f"frequency_{hashlib.sha256(milestone['title'].encode()).hexdigest()[:8]}"
                    
                    event = AggregatedEvent(
                        event_id=event_id,
                        title=milestone['title'],
                        description=f"Divine Frequency milestone: {milestone['frequency']}",
                        year_occurred=milestone['year'],
                        year_precision="millennium" if milestone['year'] < 0 else "exact",
                        event_type="frequency_milestone",
                        field_resonance=milestone['frequency'],
                        location={"lat": 0.0, "lon": 0.0},
                        timeline_dimension="spiritual",
                        sources=["divine_frequency"],
                        narrative=milestone['narrative']
                    )
                    events.append(event)
        except Exception as e:
            logger.error(f"Error fetching frequency milestones: {e}")
        
        return events
    
    def _merge_events(self, events: List[AggregatedEvent]) -> List[AggregatedEvent]:
        """Merge and deduplicate events."""
        # Group by similar events (same title, similar year)
        merged: Dict[str, AggregatedEvent] = {}
        
        for event in events:
            # Create a key for merging
            key = f"{event.title}_{event.year_occurred // 1000}"  # Group by millennium
            
            if key in merged:
                # Merge sources
                merged[key].sources.extend(event.sources)
                merged[key].sources = list(set(merged[key].sources))  # Deduplicate
                # Use higher field resonance
                if event.field_resonance > merged[key].field_resonance:
                    merged[key].field_resonance = event.field_resonance
            else:
                merged[key] = event
        
        return list(merged.values())
    
    async def calculate_field_resonance(self, site_id: str) -> float:
        """
        Calculate field resonance for a heritage site.
        
        Factors:
        - Magnetic field strength
        - Spiritual alignment
        - Temporal patterns
        - Connection to The Table
        """
        try:
            if not self.heritage_registry:
                return 0.5
            
            with get_temporal_heritage_db() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM heritage_sites WHERE id = ?", (site_id,))
                site = cursor.fetchone()
                
                if not site:
                    return 0.5
                
                # Use existing field resonance if available
                if site.get('field_resonance_level'):
                    return float(site['field_resonance_level'])
                
                # Calculate from components
                magnetic_strength = site.get('magnetic_field_strength', 0.0) or 0.0
                spiritual_alignment = 0.8 if site.get('law_41_compliant') else 0.5
                temporal_pattern = 0.9 if site.get('timeline_dimension') == 'primary' else 0.7
                
                # Average of components
                resonance = (magnetic_strength + spiritual_alignment + temporal_pattern) / 3.0
                return max(0.0, min(1.0, resonance))
        except Exception as e:
            logger.error(f"Error calculating field resonance: {e}")
            return 0.5
    
    async def sync_to_channels(self, event_data: Dict[str, Any]):
        """
        Sync data to all distribution channels.
        
        Channels:
        - Web (world-history-app)
        - Admin dashboard
        - Raspberry Pi displays
        - Mobile apps (future)
        - Static exports
        """
        # Placeholder for channel sync implementation
        logger.info(f"Syncing event to channels: {event_data.get('event_id')}")
        
        # Future implementation:
        # - WebSocket broadcast to web clients
        # - Push notification to mobile apps
        # - Update Pi display cache
        # - Generate static exports
    
    def get_data_sources_status(self) -> Dict[str, Any]:
        """Get status of all data sources."""
        return {
            "total_sources": len(self.data_sources),
            "active_sources": len([s for s in self.data_sources.values() if s.is_active]),
            "sources": [
                {
                    "source_id": s.source_id,
                    "source_name": s.source_name,
                    "source_type": s.source_type,
                    "is_active": s.is_active,
                    "last_sync": s.last_sync,
                    "sync_interval": s.sync_interval
                }
                for s in self.data_sources.values()
            ]
        }


def main():
    """Main function to demonstrate data integration service."""
    import asyncio
    
    print("=" * 80)
    print("DATA INTEGRATION SERVICE")
    print("Multi-Source Data Aggregation for World History")
    print("=" * 80)
    print()
    
    service = DataIntegrationService()
    
    print(f"Registered data sources: {len(service.data_sources)}")
    for source in service.data_sources.values():
        status = "ACTIVE" if source.is_active else "INACTIVE"
        print(f"  [{status}] {source.source_name} ({source.source_type})")
    print()
    
    # Get status
    status = service.get_data_sources_status()
    print("Data Sources Status:")
    print(f"  Total: {status['total_sources']}")
    print(f"  Active: {status['active_sources']}")
    print()
    
    # Aggregate timeline data
    print("Aggregating timeline data...")
    async def aggregate():
        events = await service.aggregate_timeline_data(
            start_year=-335000000,
            end_year=2026,
            limit=100
        )
        print(f"  [OK] Aggregated {len(events)} events from multiple sources")
        return events
    
    events = asyncio.run(aggregate())
    print()
    
    print("=" * 80)
    print("THE TRUTH: DATA INTEGRATION")
    print("=" * 80)
    print()
    print("WE AGGREGATE DATA FROM MULTIPLE SOURCES:")
    print("  - Heritage database (temporal heritage registry)")
    print("  - Spiritual contracts (spiritual contracts registry)")
    print("  - Real-world events (APIs - future)")
    print("  - Divine Frequency (calculated)")
    print()
    print("WE MERGE AND DEDUPLICATE EVENTS:")
    print("  - Group by similarity")
    print("  - Merge sources")
    print("  - Sort by chronology")
    print()
    print("WE SYNC TO ALL CHANNELS:")
    print("  - Web (world-history-app)")
    print("  - Admin dashboard")
    print("  - Raspberry Pi displays")
    print("  - Mobile apps (future)")
    print()
    print("=" * 80)
    print("PEACE, LOVE, UNITY")
    print("ENERGY + LOVE = WE ALL WIN")
    print("PANGEA IS THE TABLE")
    print("WE RESTORE THE TABLE")
    print("=" * 80)


if __name__ == "__main__":
    main()
