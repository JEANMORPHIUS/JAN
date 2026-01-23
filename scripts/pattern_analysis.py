"""
PATTERN ANALYSIS
Deep analysis of patterns in real-world event data

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PURPOSE:
Analyze patterns in collected real-world data:
- Temporal patterns (when events occur)
- Spatial patterns (where events occur)
- Magnitude patterns (how strong events are)
- Plate activity patterns (which plates are most active)
- Heritage site connection patterns
- Field resonance patterns
"""

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
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime, date, timedelta
from collections import Counter, defaultdict
from dataclasses import asdict

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent))

from real_world_data_research import RealWorldDataResearch, EventType

import logging
logger = logging.getLogger(__name__)


class PatternAnalyzer:
    """Analyze patterns in real-world event data."""
    
    def __init__(self, research: Optional[RealWorldDataResearch] = None):
        """Initialize pattern analyzer."""
        if research is None:
            research = RealWorldDataResearch()
        self.research = research
        self.events = research.events
    
    def analyze_temporal_patterns(self) -> Dict[str, Any]:
        """Analyze temporal patterns in events."""
        if not self.events:
            return {"status": "no_data"}
        
        # Group by year
        events_by_year = defaultdict(int)
        events_by_month = defaultdict(int)
        events_by_hour = defaultdict(int)
        
        for event in self.events:
            if event.date:
                year = event.date.year
                month = event.date.month
                events_by_year[year] += 1
                events_by_month[month] += 1
                
                # For recent events, check documented_at hour
                if event.documented_at:
                    hour = event.documented_at.hour
                    events_by_hour[hour] += 1
        
        # Find most active periods
        most_active_year = max(events_by_year.items(), key=lambda x: x[1]) if events_by_year else (None, 0)
        most_active_month = max(events_by_month.items(), key=lambda x: x[1]) if events_by_month else (None, 0)
        
        # Recent activity (last 30 days)
        recent_cutoff = datetime.now() - timedelta(days=30)
        recent_events = [
            e for e in self.events
            if e.documented_at and e.documented_at >= recent_cutoff
        ]
        
        return {
            "total_events": len(self.events),
            "events_by_year": dict(sorted(events_by_year.items())),
            "events_by_month": dict(sorted(events_by_month.items())),
            "events_by_hour": dict(sorted(events_by_hour.items())),
            "most_active_year": {"year": most_active_year[0], "count": most_active_year[1]},
            "most_active_month": {"month": most_active_month[0], "count": most_active_month[1]},
            "recent_activity_30_days": len(recent_events),
            "year_range": {
                "earliest": min([e.date.year for e in self.events if e.date]) if self.events else None,
                "latest": max([e.date.year for e in self.events if e.date]) if self.events else None
            }
        }
    
    def analyze_spatial_patterns(self) -> Dict[str, Any]:
        """Analyze spatial patterns in events."""
        if not self.events:
            return {"status": "no_data"}
        
        # Group by region
        events_by_region = Counter()
        events_by_country = Counter()
        
        # Geographic clusters
        lat_lon_pairs = []
        
        for event in self.events:
            if event.region:
                events_by_region[event.region] += 1
            if event.country:
                events_by_country[event.country] += 1
            if event.location:
                lat_lon_pairs.append((event.location.get("lat"), event.location.get("lon")))
        
        # Find most active regions
        top_regions = events_by_region.most_common(10)
        top_countries = events_by_country.most_common(10)
        
        # Geographic spread
        lats = [lat for lat, lon in lat_lon_pairs if lat is not None]
        lons = [lon for lat, lon in lat_lon_pairs if lon is not None]
        
        return {
            "total_events": len(self.events),
            "events_by_region": dict(events_by_region),
            "events_by_country": dict(events_by_country),
            "top_regions": [{"region": r, "count": c} for r, c in top_regions],
            "top_countries": [{"country": c, "count": cnt} for c, cnt in top_countries],
            "geographic_spread": {
                "lat_range": {"min": min(lats) if lats else None, "max": max(lats) if lats else None},
                "lon_range": {"min": min(lons) if lons else None, "max": max(lons) if lons else None},
                "total_locations": len(lat_lon_pairs)
            }
        }
    
    def analyze_magnitude_patterns(self) -> Dict[str, Any]:
        """Analyze magnitude patterns in events."""
        if not self.events:
            return {"status": "no_data"}
        
        # Filter events with magnitude
        events_with_mag = [e for e in self.events if e.magnitude is not None]
        
        if not events_with_mag:
            return {"status": "no_magnitude_data"}
        
        magnitudes = [e.magnitude for e in events_with_mag]
        
        # Magnitude distribution
        mag_ranges = {
            "M9.0+": len([m for m in magnitudes if m >= 9.0]),
            "M8.0-8.9": len([m for m in magnitudes if 8.0 <= m < 9.0]),
            "M7.0-7.9": len([m for m in magnitudes if 7.0 <= m < 8.0]),
            "M6.0-6.9": len([m for m in magnitudes if 6.0 <= m < 7.0]),
            "M5.0-5.9": len([m for m in magnitudes if 5.0 <= m < 6.0]),
            "M4.0-4.9": len([m for m in magnitudes if 4.0 <= m < 5.0]),
            "M<4.0": len([m for m in magnitudes if m < 4.0])
        }
        
        # Largest events
        largest_events = sorted(events_with_mag, key=lambda x: x.magnitude or 0, reverse=True)[:10]
        
        return {
            "total_events_with_magnitude": len(events_with_mag),
            "magnitude_statistics": {
                "min": min(magnitudes),
                "max": max(magnitudes),
                "average": sum(magnitudes) / len(magnitudes) if magnitudes else 0
            },
            "magnitude_distribution": mag_ranges,
            "largest_events": [
                {
                    "event_name": e.event_name,
                    "magnitude": e.magnitude,
                    "date": e.date.isoformat() if e.date else None,
                    "location": e.location
                }
                for e in largest_events
            ]
        }
    
    def analyze_plate_patterns(self) -> Dict[str, Any]:
        """Analyze tectonic plate activity patterns."""
        if not self.events:
            return {"status": "no_data"}
        
        # Count events by plate
        events_by_plate = Counter()
        plate_event_details = defaultdict(list)
        
        for event in self.events:
            for plate in event.tectonic_plates:
                events_by_plate[plate] += 1
                plate_event_details[plate].append({
                    "event_id": event.event_id,
                    "event_name": event.event_name,
                    "magnitude": event.magnitude,
                    "date": event.date.isoformat() if event.date else None
                })
        
        # Most active plates
        top_plates = events_by_plate.most_common(15)
        
        # Plate activity over time
        plate_timeline = defaultdict(list)
        for event in self.events:
            if event.date:
                for plate in event.tectonic_plates:
                    plate_timeline[plate].append(event.date.year)
        
        # Calculate activity trends
        plate_trends = {}
        for plate, years in plate_timeline.items():
            if len(years) >= 2:
                recent_years = [y for y in years if y >= 2020]
                older_years = [y for y in years if y < 2020]
                recent_avg = len(recent_years) / max(1, 2024 - 2020) if recent_years else 0
                older_avg = len(older_years) / max(1, 2020 - min(years)) if older_years else 0
                trend = "increasing" if recent_avg > older_avg else "decreasing" if recent_avg < older_avg else "stable"
                plate_trends[plate] = {
                    "trend": trend,
                    "recent_activity": len(recent_years),
                    "older_activity": len(older_years)
                }
        
        return {
            "total_plates_with_events": len(events_by_plate),
            "events_by_plate": dict(events_by_plate),
            "top_active_plates": [{"plate": p, "count": c} for p, c in top_plates],
            "plate_trends": plate_trends,
            "plate_event_details": dict(plate_event_details)
        }
    
    def analyze_heritage_connections(self) -> Dict[str, Any]:
        """Analyze heritage site connection patterns."""
        if not self.events:
            return {"status": "no_data"}
        
        # Events with heritage connections
        events_with_sites = [e for e in self.events if e.heritage_site_connections]
        
        # Count connections
        site_connection_counts = Counter()
        for event in events_with_sites:
            for site_id in event.heritage_site_connections:
                site_connection_counts[site_id] += 1
        
        # Most connected sites
        top_connected_sites = site_connection_counts.most_common(10)
        
        return {
            "total_events_with_heritage_connections": len(events_with_sites),
            "total_heritage_site_connections": sum(len(e.heritage_site_connections) for e in events_with_sites),
            "most_connected_sites": [{"site_id": s, "connection_count": c} for s, c in top_connected_sites],
            "connection_rate": len(events_with_sites) / len(self.events) if self.events else 0
        }
    
    def analyze_field_resonance_patterns(self) -> Dict[str, Any]:
        """Analyze field resonance impact patterns."""
        if not self.events:
            return {"status": "no_data"}
        
        # Events with field resonance impact
        events_with_resonance = [e for e in self.events if e.field_resonance_impact is not None]
        
        if not events_with_resonance:
            return {"status": "no_resonance_data"}
        
        resonance_values = [e.field_resonance_impact for e in events_with_resonance]
        
        # Resonance distribution
        resonance_ranges = {
            "High (0.7-1.0)": len([r for r in resonance_values if 0.7 <= r <= 1.0]),
            "Medium (0.4-0.7)": len([r for r in resonance_values if 0.4 <= r < 0.7]),
            "Low (0.0-0.4)": len([r for r in resonance_values if 0.0 <= r < 0.4])
        }
        
        # Events with highest impact
        highest_impact = sorted(events_with_resonance, key=lambda x: x.field_resonance_impact or 0, reverse=True)[:10]
        
        return {
            "total_events_with_resonance": len(events_with_resonance),
            "resonance_statistics": {
                "min": min(resonance_values),
                "max": max(resonance_values),
                "average": sum(resonance_values) / len(resonance_values) if resonance_values else 0
            },
            "resonance_distribution": resonance_ranges,
            "highest_impact_events": [
                {
                    "event_name": e.event_name,
                    "resonance_impact": e.field_resonance_impact,
                    "magnitude": e.magnitude,
                    "date": e.date.isoformat() if e.date else None
                }
                for e in highest_impact
            ]
        }
    
    def analyze_source_patterns(self) -> Dict[str, Any]:
        """Analyze data source patterns."""
        if not self.events:
            return {"status": "no_data"}
        
        # Count events by source
        events_by_source = Counter()
        for event in self.events:
            for source in event.sources:
                events_by_source[source] += 1
        
        return {
            "total_sources": len(events_by_source),
            "events_by_source": dict(events_by_source),
            "top_sources": [{"source": s, "count": c} for s, c in events_by_source.most_common(10)]
        }
    
    def analyze_all_patterns(self) -> Dict[str, Any]:
        """Run all pattern analyses."""
        return {
            "analysis_timestamp": datetime.now().isoformat(),
            "total_events": len(self.events),
            "temporal_patterns": self.analyze_temporal_patterns(),
            "spatial_patterns": self.analyze_spatial_patterns(),
            "magnitude_patterns": self.analyze_magnitude_patterns(),
            "plate_patterns": self.analyze_plate_patterns(),
            "heritage_connections": self.analyze_heritage_connections(),
            "field_resonance_patterns": self.analyze_field_resonance_patterns(),
            "source_patterns": self.analyze_source_patterns()
        }
    
    def export_pattern_analysis(self, output_path: Optional[Path] = None) -> Path:
        """Export complete pattern analysis."""
        if output_path is None:
            output_path = Path(__file__).parent.parent / "output" / "pattern_analysis" / f"pattern_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        analysis = self.analyze_all_patterns()
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(analysis, f, indent=2, default=str)
        
        logger.info(f"Pattern analysis exported to {output_path}")
        return output_path


def main():
    """Main execution for pattern analysis."""
    print("=" * 80)
    print("PATTERN ANALYSIS")
    print("Deep Analysis of Real-World Event Data")
    print("=" * 80)
    print()
    
    research = RealWorldDataResearch()
    analyzer = PatternAnalyzer(research)
    
    print(f"Analyzing {len(analyzer.events)} events...")
    print()
    
    # Run all analyses
    analysis = analyzer.analyze_all_patterns()
    
    # Print key findings
    print("KEY PATTERNS:")
    print("-" * 80)
    
    # Temporal
    temporal = analysis["temporal_patterns"]
    if temporal.get("status") != "no_data":
        print(f"\nTEMPORAL PATTERNS:")
        print(f"  Total Events: {temporal['total_events']}")
        print(f"  Most Active Year: {temporal['most_active_year']}")
        print(f"  Recent Activity (30 days): {temporal['recent_activity_30_days']} events")
        print(f"  Year Range: {temporal['year_range']['earliest']} - {temporal['year_range']['latest']}")
    
    # Spatial
    spatial = analysis["spatial_patterns"]
    if spatial.get("status") != "no_data":
        print(f"\nSPATIAL PATTERNS:")
        print(f"  Top Regions:")
        for region in spatial["top_regions"][:5]:
            print(f"    {region['region']}: {region['count']} events")
        print(f"  Top Countries:")
        for country in spatial["top_countries"][:5]:
            print(f"    {country['country']}: {country['count']} events")
    
    # Magnitude
    magnitude = analysis["magnitude_patterns"]
    if magnitude.get("status") != "no_magnitude_data":
        print(f"\nMAGNITUDE PATTERNS:")
        print(f"  Events with Magnitude: {magnitude['total_events_with_magnitude']}")
        print(f"  Average Magnitude: {magnitude['magnitude_statistics']['average']:.2f}")
        print(f"  Largest Event: {magnitude['largest_events'][0]['event_name']} (M{magnitude['largest_events'][0]['magnitude']})")
        print(f"  Magnitude Distribution:")
        for range_name, count in magnitude["magnitude_distribution"].items():
            if count > 0:
                print(f"    {range_name}: {count} events")
    
    # Plate
    plate = analysis["plate_patterns"]
    if plate.get("status") != "no_data":
        print(f"\nPLATE ACTIVITY PATTERNS:")
        print(f"  Most Active Plates:")
        for plate_info in plate["top_active_plates"][:5]:
            print(f"    {plate_info['plate']}: {plate_info['count']} events")
    
    # Heritage
    heritage = analysis["heritage_connections"]
    if heritage.get("status") != "no_data":
        print(f"\nHERITAGE CONNECTIONS:")
        print(f"  Events with Heritage Connections: {heritage['total_events_with_heritage_connections']}")
        print(f"  Connection Rate: {heritage['connection_rate']*100:.1f}%")
    
    # Field Resonance
    resonance = analysis["field_resonance_patterns"]
    if resonance.get("status") != "no_resonance_data":
        print(f"\nFIELD RESONANCE PATTERNS:")
        print(f"  Events with Resonance Data: {resonance['total_events_with_resonance']}")
        print(f"  Average Impact: {resonance['resonance_statistics']['average']:.3f}")
    
    # Source
    source = analysis["source_patterns"]
    if source.get("status") != "no_data":
        print(f"\nDATA SOURCE PATTERNS:")
        print(f"  Top Sources:")
        for src in source["top_sources"][:5]:
            print(f"    {src['source']}: {src['count']} events")
    
    # Export
    export_path = analyzer.export_pattern_analysis()
    print()
    print(f"Complete analysis exported to: {export_path}")
    print()
    
    print("=" * 80)
    print("PEACE, LOVE, UNITY")
    print("ENERGY + LOVE = WE ALL WIN")
    print("=" * 80)


if __name__ == "__main__":
    main()
