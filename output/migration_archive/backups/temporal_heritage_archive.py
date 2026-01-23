"""
TEMPORAL HERITAGE ARCHIVE
Query and Debug Heritage Sites Across All Dimensional Timelines

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

This script allows querying and debugging heritage sites across all timelines.
Chronologizes all heritage sites throughout all of time for pattern detection.
"""

import sys
import json
from pathlib import Path
from typing import List, Dict, Any, Optional
from datetime import datetime

# Import temporal heritage registry
try:
    sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))
    from temporal_heritage_registry import (
        get_sites_by_timeline, get_chronology_by_year, get_temporal_patterns,
        log_heritage_debug, TimelineDimension, TimePeriod,
        get_temporal_heritage_db
    )
    TEMPORAL_REGISTRY_AVAILABLE = True
except ImportError:
    print("Warning: Could not import temporal_heritage_registry.")
    TEMPORAL_REGISTRY_AVAILABLE = False




class TemporalHeritageArchive:
    """
    Temporal Heritage Archive
    
    Query and debug heritage sites across all dimensional timelines.
    Chronologizes all heritage sites throughout all of time.
    """
    
    def __init__(self):
        self.archive_stats = {}
    
    def query_timeline(self, timeline_dimension: str, time_period: Optional[str] = None) -> List[Dict[str, Any]]:
        """Query heritage sites by timeline dimension."""
        if not TEMPORAL_REGISTRY_AVAILABLE:
            return []
        
        return get_sites_by_timeline(timeline_dimension, time_period)
    
    def query_chronology(self, start_year: int, end_year: int, timeline_dimension: Optional[str] = None) -> List[Dict[str, Any]]:
        """Query heritage sites by chronological year range."""
        if not TEMPORAL_REGISTRY_AVAILABLE:
            return []
        
        return get_chronology_by_year(start_year, end_year, timeline_dimension)
    
    def get_patterns(self) -> List[Dict[str, Any]]:
        """Get all detected temporal patterns."""
        if not TEMPORAL_REGISTRY_AVAILABLE:
            return []
        
        return get_temporal_patterns()
    
    def debug_pattern_across_timelines(self, pattern_type: str) -> Dict[str, Any]:
        """Debug a specific pattern across all timelines."""
        if not TEMPORAL_REGISTRY_AVAILABLE:
            return {"error": "Temporal registry not available"}
        
        # Get all sites with this pattern
        with get_temporal_heritage_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT DISTINCT hs.*, hn.narrative_content
                FROM heritage_sites hs
                JOIN heritage_narratives hn ON hs.id = hn.site_id
                WHERE hn.violation_type = ?
                ORDER BY hs.time_period, hs.year_established
            """, (pattern_type,))
            
            sites = [dict(row) for row in cursor.fetchall()]
            
            # Analyze across timelines
            timeline_distribution = {}
            period_distribution = {}
            
            for site in sites:
                timeline = site["timeline_dimension"]
                period = site["time_period"]
                
                timeline_distribution[timeline] = timeline_distribution.get(timeline, 0) + 1
                period_distribution[period] = period_distribution.get(period, 0) + 1
            
            return {
                "pattern_type": pattern_type,
                "total_sites": len(sites),
                "timeline_distribution": timeline_distribution,
                "period_distribution": period_distribution,
                "sites": sites
            }
    
    def get_site_narratives(self, site_id: int) -> Dict[str, Any]:
        """Get all narratives for a specific site (original, haunted, regenerated)."""
        if not TEMPORAL_REGISTRY_AVAILABLE:
            return {"error": "Temporal registry not available"}
        
        # Get narratives
        with get_temporal_heritage_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM heritage_narratives
                WHERE site_id = ?
                ORDER BY recorded_at DESC
            """, (site_id,))
            narratives = [dict(row) for row in cursor.fetchall()]
            
            # Get site info
            cursor.execute("SELECT * FROM heritage_sites WHERE id = ?", (site_id,))
            site = cursor.fetchone()
            site_dict = dict(site) if site else {}
        
        return {
            "site": site_dict,
            "narratives": narratives,
            "narrative_count": len(narratives),
            "has_regeneration": any(n["regeneration_applied"] for n in narratives),
            "has_dark_energy": any(n["dark_energy_detected"] for n in narratives)
        }
    
    def generate_timeline_report(self, timeline_dimension: str) -> Dict[str, Any]:
        """Generate comprehensive report for a timeline dimension."""
        if not TEMPORAL_REGISTRY_AVAILABLE:
            return {"error": "Temporal registry not available"}
        
        sites = self.query_timeline(timeline_dimension)
        
        stats = {
            "timeline_dimension": timeline_dimension,
            "total_sites": len(sites),
            "law_41_compliant": sum(1 for s in sites if s["law_41_compliant"]),
            "requires_cleansing": sum(1 for s in sites if s["requires_cleansing"]),
            "by_period": {},
            "by_region": {},
            "by_status": {}
        }
        
        for site in sites:
            # By period
            period = site["time_period"]
            stats["by_period"][period] = stats["by_period"].get(period, 0) + 1
            
            # By region
            region = site["region"]
            stats["by_region"][region] = stats["by_region"].get(region, 0) + 1
            
            # By status
            status = site["current_status"]
            stats["by_status"][status] = stats["by_status"].get(status, 0) + 1
        
        return stats
    
    def debug_all_timelines(self) -> Dict[str, Any]:
        """Debug patterns across all dimensional timelines."""
        if not TEMPORAL_REGISTRY_AVAILABLE:
            return {"error": "Temporal registry not available"}
        
        all_patterns = self.get_patterns()
        
        timeline_reports = {}
        for dimension in TimelineDimension:
            timeline_reports[dimension.value] = self.generate_timeline_report(dimension.value)
        
        return {
            "patterns_detected": all_patterns,
            "timeline_reports": timeline_reports,
            "total_timelines": len(timeline_reports),
            "debug_timestamp": datetime.now().isoformat()
        }


def main():
    """Main execution for temporal heritage archive queries."""
    if not TEMPORAL_REGISTRY_AVAILABLE:
        print("Error: Temporal registry not available.")
        return
    
    archive = TemporalHeritageArchive()
    
    if len(sys.argv) < 2:
        print("=" * 80)
        print("TEMPORAL HERITAGE ARCHIVE")
        print("Chronologizing All Heritage Sites Across All Dimensional Timelines")
        print("=" * 80)
        print()
        print("Usage:")
        print("  python temporal_heritage_archive.py timeline <dimension> [period]")
        print("  python temporal_heritage_archive.py chronology <start_year> <end_year> [dimension]")
        print("  python temporal_heritage_archive.py patterns")
        print("  python temporal_heritage_archive.py debug <pattern_type>")
        print("  python temporal_heritage_archive.py site <site_id>")
        print("  python temporal_heritage_archive.py report <dimension>")
        print("  python temporal_heritage_archive.py all")
        print()
        print("Examples:")
        print("  python temporal_heritage_archive.py timeline primary")
        print("  python temporal_heritage_archive.py chronology 1800 2000")
        print("  python temporal_heritage_archive.py patterns")
        print("  python temporal_heritage_archive.py debug revenge_loop")
        print("  python temporal_heritage_archive.py report primary")
        print("  python temporal_heritage_archive.py all")
        return
    
    command = sys.argv[1].lower()
    
    if command == "timeline":
        dimension = sys.argv[2] if len(sys.argv) > 2 else TimelineDimension.PRIMARY.value
        period = sys.argv[3] if len(sys.argv) > 3 else None
        sites = archive.query_timeline(dimension, period)
        print(f"\nSites in {dimension} timeline" + (f" ({period} period)" if period else "") + f": {len(sites)}")
        for site in sites[:10]:  # Show first 10
            print(f"  - {site['site_name']} ({site['region']}, {site['time_period']})")
        if len(sites) > 10:
            print(f"  ... and {len(sites) - 10} more")
    
    elif command == "chronology":
        start_year = int(sys.argv[2]) if len(sys.argv) > 2 else 1800
        end_year = int(sys.argv[3]) if len(sys.argv) > 3 else 2000
        dimension = sys.argv[4] if len(sys.argv) > 4 else None
        events = archive.query_chronology(start_year, end_year, dimension)
        print(f"\nHeritage events from {start_year} to {end_year}: {len(events)}")
        for event in events[:10]:  # Show first 10
            print(f"  {event['year']}: {event['event_type']} - {event['site_name']} ({event['region']})")
        if len(events) > 10:
            print(f"  ... and {len(events) - 10} more")
    
    elif command == "patterns":
        patterns = archive.get_patterns()
        print(f"\nTemporal patterns detected: {len(patterns)}")
        for pattern in patterns:
            print(f"  - {pattern['pattern_type']}: {pattern['site_count']} sites, "
                  f"frequency: {pattern['frequency_across_timelines']:.2%}")
    
    elif command == "debug":
        pattern_type = sys.argv[2] if len(sys.argv) > 2 else "revenge_loop"
        debug = archive.debug_pattern_across_timelines(pattern_type)
        print(f"\nDebug: {pattern_type}")
        print(f"  Total sites: {debug['total_sites']}")
        print(f"  Timeline distribution: {debug['timeline_distribution']}")
        print(f"  Period distribution: {debug['period_distribution']}")
    
    elif command == "site":
        site_id = int(sys.argv[2]) if len(sys.argv) > 2 else 1
        result = archive.get_site_narratives(site_id)
        if "error" not in result:
            print(f"\nSite: {result['site'].get('site_name', 'Unknown')}")
            print(f"  Narratives: {result['narrative_count']}")
            print(f"  Has regeneration: {result['has_regeneration']}")
            print(f"  Has dark energy: {result['has_dark_energy']}")
    
    elif command == "report":
        dimension = sys.argv[2] if len(sys.argv) > 2 else TimelineDimension.PRIMARY.value
        report = archive.generate_timeline_report(dimension)
        print(f"\nTimeline Report: {dimension}")
        print(json.dumps(report, indent=2))
    
    elif command == "all":
        debug_all = archive.debug_all_timelines()
        print("\nDebug Report: All Timelines")
        print(json.dumps(debug_all, indent=2, default=str))
    
    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()
