"""
HERITAGE BATCH IMPORT
Import heritage sites from CSV/JSON files into temporal registry

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity
"""

import sys
import json
import csv
from pathlib import Path
from typing import List, Dict, Any
import argparse

# Import temporal heritage registry
try:
    sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))
    from temporal_heritage_registry import (
        register_heritage_site, add_heritage_narrative,
        TimelineDimension, TimePeriod
    )
    from heritage_cleansing import HeritageCleanser
    TEMPORAL_REGISTRY_AVAILABLE = True
except ImportError:
    print("Warning: Could not import temporal_heritage_registry.")
    TEMPORAL_REGISTRY_AVAILABLE = False


def import_from_csv(csv_path: Path, timeline_dimension: str = TimelineDimension.PRIMARY.value) -> List[Dict[str, Any]]:
    """Import heritage sites from CSV file."""
    if not TEMPORAL_REGISTRY_AVAILABLE:
        return []
    
    results = []
    cleanser = HeritageCleanser(timeline_dimension=timeline_dimension)
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Map CSV columns to registry fields
            site_id = register_heritage_site(
                site_name=row.get('site_name', 'Unknown'),
                site_type=row.get('site_type', 'Heritage Property'),
                region=row.get('region', 'Unknown'),
                country=row.get('country'),
                coordinates_lat=float(row['coordinates_lat']) if row.get('coordinates_lat') else None,
                coordinates_lon=float(row['coordinates_lon']) if row.get('coordinates_lon') else None,
                timeline_dimension=timeline_dimension,
                time_period=row.get('time_period', TimePeriod.MODERN.value),
                year_established=int(row['year_established']) if row.get('year_established') else None,
                year_abandoned=int(row['year_abandoned']) if row.get('year_abandoned') else None,
                current_status=row.get('current_status', 'unknown'),
                law_41_compliant=False,
                requires_cleansing=bool(row.get('narrative_content', ''))
            )
            
            # If narrative provided, cleanse and archive
            if row.get('narrative_content'):
                cleansed, analysis = cleanser.cleanse_content(
                    content=row['narrative_content'],
                    source=row.get('source', 'CSV Import'),
                    site_type=row.get('site_type', 'Heritage Property'),
                    region=row.get('region', 'Unknown'),
                    country=row.get('country'),
                    year_established=int(row['year_established']) if row.get('year_established') else None,
                    year_abandoned=int(row['year_abandoned']) if row.get('year_abandoned') else None,
                    time_period=row.get('time_period', TimePeriod.MODERN.value)
                )
                results.append({
                    "site_id": site_id,
                    "site_name": row.get('site_name'),
                    "status": "imported_and_cleansed",
                    "analysis": analysis
                })
            else:
                results.append({
                    "site_id": site_id,
                    "site_name": row.get('site_name'),
                    "status": "imported"
                })
    
    return results


def import_from_json(json_path: Path, timeline_dimension: str = TimelineDimension.PRIMARY.value) -> List[Dict[str, Any]]:
    """Import heritage sites from JSON file."""
    if not TEMPORAL_REGISTRY_AVAILABLE:
        return []
    
    results = []
    cleanser = HeritageCleanser(timeline_dimension=timeline_dimension)
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        sites = data if isinstance(data, list) else data.get('sites', [])
        
        for site_data in sites:
            site_id = register_heritage_site(
                site_name=site_data.get('site_name', 'Unknown'),
                site_type=site_data.get('site_type', 'Heritage Property'),
                region=site_data.get('region', 'Unknown'),
                country=site_data.get('country'),
                coordinates_lat=site_data.get('coordinates_lat'),
                coordinates_lon=site_data.get('coordinates_lon'),
                timeline_dimension=timeline_dimension,
                time_period=site_data.get('time_period', TimePeriod.MODERN.value),
                year_established=site_data.get('year_established'),
                year_abandoned=site_data.get('year_abandoned'),
                current_status=site_data.get('current_status', 'unknown'),
                law_41_compliant=False,
                requires_cleansing=bool(site_data.get('narrative_content'))
            )
            
            # If narrative provided, cleanse and archive
            if site_data.get('narrative_content'):
                cleansed, analysis = cleanser.cleanse_content(
                    content=site_data['narrative_content'],
                    source=site_data.get('source', 'JSON Import'),
                    site_type=site_data.get('site_type', 'Heritage Property'),
                    region=site_data.get('region', 'Unknown'),
                    country=site_data.get('country'),
                    year_established=site_data.get('year_established'),
                    year_abandoned=site_data.get('year_abandoned'),
                    time_period=site_data.get('time_period', TimePeriod.MODERN.value)
                )
                results.append({
                    "site_id": site_id,
                    "site_name": site_data.get('site_name'),
                    "status": "imported_and_cleansed",
                    "analysis": analysis
                })
            else:
                results.append({
                    "site_id": site_id,
                    "site_name": site_data.get('site_name'),
                    "status": "imported"
                })
    
    return results


def main():
    """Main execution for batch import."""
    parser = argparse.ArgumentParser(description='Import heritage sites from CSV/JSON')
    parser.add_argument('file', type=Path, help='CSV or JSON file to import')
    parser.add_argument('--timeline', default=TimelineDimension.PRIMARY.value,
                       choices=[d.value for d in TimelineDimension],
                       help='Timeline dimension')
    parser.add_argument('--output', type=Path, help='Output results to JSON file')
    
    args = parser.parse_args()
    
    if not args.file.exists():
        print(f"Error: File not found: {args.file}")
        return
    
    print(f"Importing from {args.file}...")
    
    if args.file.suffix.lower() == '.csv':
        results = import_from_csv(args.file, args.timeline)
    elif args.file.suffix.lower() == '.json':
        results = import_from_json(args.file, args.timeline)
    else:
        print(f"Error: Unsupported file format: {args.file.suffix}")
        return
    
    print(f"Imported {len(results)} sites")
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2)
        print(f"Results saved to {args.output}")
    else:
        print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
