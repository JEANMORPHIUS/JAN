"""HERITAGE IMPORT EVERYTHING
Import all available heritage data into all timelines

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

Import EVERYTHING - all heritage data into all relevant timelines.

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
    Path, datetime, json, load_json, save_json
    setup_logging, standard_main
)

import sys
import json
import csv
from pathlib import Path
from typing import List, Dict, Any, Optional
from datetime import datetime

try:
    sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))
    from temporal_heritage_registry import (
        register_heritage_site, add_heritage_narrative,
        TimelineDimension, TimePeriod, get_sites_by_timeline
    )
    from heritage_cleansing import HeritageCleanser
    from heritage_audit_framework import HeritageAuditFramework, HeritageSiteProfile
    from magnetic_field_research import (
        research_heritage_site_magnetic_field, update_site_magnetic_field
    )
    from logging_config import get_logger
    IMPORT_AVAILABLE = True
except ImportError as e:
    print(f"Error: {e}")
    IMPORT_AVAILABLE = False

logger = get_logger(__name__) if IMPORT_AVAILABLE else None


class HeritageImportEverything:
    """
    Import all available heritage data into all timelines.
    
    Sources:
    - CSV files in examples/
    - JSON files in examples/
    - Output exports (if any)
    - Any heritage data files found
    """
    
    def __init__(self):
        if not IMPORT_AVAILABLE:
            raise RuntimeError("Import system not available - check imports")
        
        self.base_dir = Path(__file__).parent.parent
        self.examples_dir = self.base_dir / "examples"
        self.output_dir = self.base_dir / "output"
        self.scripts_dir = self.base_dir / "scripts"
        
        self.cleansers = {}  # Cache cleansers by timeline
        self.import_stats = {
            "total_imported": 0,
            "by_timeline": {},
            "by_source": {},
            "errors": []
        }
    
    def find_all_heritage_files(self) -> Dict[str, List[Path]]:
        """Find all heritage data files in the codebase."""
        files = {
            "csv": [],
            "json": [],
            "other": []
        }
        
        # Search examples directory
        if self.examples_dir.exists():
            for csv_file in self.examples_dir.glob("**/*.csv"):
                if "heritage" in csv_file.name.lower() or "site" in csv_file.name.lower():
                    files["csv"].append(csv_file)
            
            for json_file in self.examples_dir.glob("**/*.json"):
                if "heritage" in json_file.name.lower() or "site" in json_file.name.lower():
                    files["json"].append(json_file)
        
        # Search output/exports for exported data
        exports_dir = self.output_dir / "exports"
        if exports_dir.exists():
            for json_file in exports_dir.glob("heritage_sites*.json"):
                files["json"].append(json_file)
        
        return files
    
    def get_cleanser(self, timeline_dimension: str) -> HeritageCleanser:
        """Get or create cleanser for timeline dimension."""
        if timeline_dimension not in self.cleansers:
            self.cleansers[timeline_dimension] = HeritageCleanser(timeline_dimension=timeline_dimension)
        return self.cleansers[timeline_dimension]
    
    def import_from_csv(self, csv_path: Path, timeline_dimension: str = TimelineDimension.PRIMARY.value) -> List[Dict[str, Any]]:
        """Import heritage sites from CSV file."""
        results = []
        
        try:
            with open(csv_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                cleanser = self.get_cleanser(timeline_dimension)
                
                for row in reader:
                    try:
                        # Register site
                        site_id = register_heritage_site(
                            site_name=row.get('site_name', 'Unknown'),
                            site_type=row.get('site_type', 'Heritage Property'),
                            region=row.get('region', 'Unknown'),
                            country=row.get('country', 'Unknown'),
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
                                source=row.get('source', f'CSV Import: {csv_path.name}'),
                                site_type=row.get('site_type', 'Heritage Property'),
                                region=row.get('region', 'Unknown'),
                                country=row.get('country', 'Unknown'),
                                year_established=int(row['year_established']) if row.get('year_established') else None,
                                year_abandoned=int(row['year_abandoned']) if row.get('year_abandoned') else None,
                                time_period=row.get('time_period', TimePeriod.MODERN.value)
                            )
                        
                        results.append({
                            "site_id": site_id,
                            "site_name": row.get('site_name'),
                            "status": "imported"
                        })
                        
                        self.import_stats["total_imported"] += 1
                        self.import_stats["by_timeline"][timeline_dimension] = \
                            self.import_stats["by_timeline"].get(timeline_dimension, 0) + 1
                        self.import_stats["by_source"][str(csv_path)] = \
                            self.import_stats["by_source"].get(str(csv_path), 0) + 1
                    
                    except Exception as e:
                        error_msg = f"Error importing site from {csv_path.name}: {e}"
                        self.import_stats["errors"].append(error_msg)
                        if logger:
                            logger.error(error_msg, exc_info=True)
        
        except Exception as e:
            error_msg = f"Error reading CSV file {csv_path}: {e}"
            self.import_stats["errors"].append(error_msg)
            if logger:
                logger.error(error_msg, exc_info=True)
        
        return results
    
    def import_from_json(self, json_path: Path, timeline_dimension: str = TimelineDimension.PRIMARY.value) -> List[Dict[str, Any]]:
        """Import heritage sites from JSON file."""
        results = []
        
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
                # Handle different JSON structures
                if isinstance(data, list):
                    sites = data
                elif isinstance(data, dict):
                    sites = data.get('sites', [])
                    if not sites and 'data' in data:
                        sites = data.get('data', [])
                else:
                    sites = []
                
                cleanser = self.get_cleanser(timeline_dimension)
                
                for site_data in sites:
                    try:
                        # Handle both dict and object formats
                        if isinstance(site_data, dict):
                            site_dict = site_data
                        else:
                            site_dict = site_data.__dict__ if hasattr(site_data, '__dict__') else {}
                        
                        # Register site
                        site_id = register_heritage_site(
                            site_name=site_dict.get('site_name', 'Unknown'),
                            site_type=site_dict.get('site_type', 'Heritage Property'),
                            region=site_dict.get('region', 'Unknown'),
                            country=site_dict.get('country', 'Unknown'),
                            coordinates_lat=site_dict.get('coordinates_lat'),
                            coordinates_lon=site_dict.get('coordinates_lon'),
                            timeline_dimension=timeline_dimension,
                            time_period=site_dict.get('time_period', TimePeriod.MODERN.value),
                            year_established=site_dict.get('year_established'),
                            year_abandoned=site_dict.get('year_abandoned'),
                            current_status=site_dict.get('current_status', 'unknown'),
                            law_41_compliant=site_dict.get('law_41_compliant', False),
                            requires_cleansing=bool(site_dict.get('narrative_content') or site_dict.get('requires_cleansing', False))
                        )
                        
                        # If narrative provided, cleanse and archive
                        narrative_content = site_dict.get('narrative_content') or \
                                          (site_dict.get('narratives', [{}])[0].get('narrative_content') if site_dict.get('narratives') else None)
                        
                        if narrative_content:
                            cleansed, analysis = cleanser.cleanse_content(
                                content=narrative_content,
                                source=site_dict.get('source', f'JSON Import: {json_path.name}'),
                                site_type=site_dict.get('site_type', 'Heritage Property'),
                                region=site_dict.get('region', 'Unknown'),
                                country=site_dict.get('country', 'Unknown'),
                                year_established=site_dict.get('year_established'),
                                year_abandoned=site_dict.get('year_abandoned'),
                                time_period=site_dict.get('time_period', TimePeriod.MODERN.value)
                            )
                        
                        # Import magnetic field data if available
                        if site_dict.get('magnetic_field_strength'):
                            try:
                                magnetic_research = research_heritage_site_magnetic_field(
                                    site_id=site_id,
                                    field_strength=site_dict.get('magnetic_field_strength'),
                                    declination=site_dict.get('magnetic_declination', 0.0),
                                    inclination=site_dict.get('magnetic_inclination', 45.0)
                                )
                                update_site_magnetic_field(site_id, magnetic_research)
                            except Exception as e:
                                if logger:
                                    logger.warning(f"Could not import magnetic field data for site {site_id}: {e}")
                        
                        results.append({
                            "site_id": site_id,
                            "site_name": site_dict.get('site_name'),
                            "status": "imported"
                        })
                        
                        self.import_stats["total_imported"] += 1
                        self.import_stats["by_timeline"][timeline_dimension] = \
                            self.import_stats["by_timeline"].get(timeline_dimension, 0) + 1
                        self.import_stats["by_source"][str(json_path)] = \
                            self.import_stats["by_source"].get(str(json_path), 0) + 1
                    
                    except Exception as e:
                        error_msg = f"Error importing site from {json_path.name}: {e}"
                        self.import_stats["errors"].append(error_msg)
                        if logger:
                            logger.error(error_msg, exc_info=True)
        
        except Exception as e:
            error_msg = f"Error reading JSON file {json_path}: {e}"
            self.import_stats["errors"].append(error_msg)
            if logger:
                logger.error(error_msg, exc_info=True)
        
        return results
    
    def import_to_all_timelines(self, files: Dict[str, List[Path]], 
                                primary_only: bool = False) -> Dict[str, Any]:
        """
        Import all files to all timelines.
        
        Args:
            files: Dictionary of file paths by type
            primary_only: If True, only import to PRIMARY timeline
        """
        print("=" * 80)
        print("HERITAGE IMPORT EVERYTHING")
        print("Importing All Available Data to All Timelines")
        print("=" * 80)
        print()
        
        timelines = [TimelineDimension.PRIMARY.value] if primary_only else \
                   [d.value for d in TimelineDimension]
        
        all_results = {}
        
        # Import CSV files
        if files["csv"]:
            print(f"Found {len(files['csv'])} CSV file(s)")
            for csv_file in files["csv"]:
                print(f"  Importing: {csv_file.name}")
                for timeline in timelines:
                    print(f"    -> Timeline: {timeline}")
                    results = self.import_from_csv(csv_file, timeline)
                    all_results[f"{csv_file.name}_{timeline}"] = results
                    print(f"      [OK] Imported {len(results)} sites")
                print()
        
        # Import JSON files
        if files["json"]:
            print(f"Found {len(files['json'])} JSON file(s)")
            for json_file in files["json"]:
                print(f"  Importing: {json_file.name}")
                for timeline in timelines:
                    print(f"    -> Timeline: {timeline}")
                    results = self.import_from_json(json_file, timeline)
                    all_results[f"{json_file.name}_{timeline}"] = results
                    print(f"      [OK] Imported {len(results)} sites")
                print()
        
        # Summary
        print("=" * 80)
        print("IMPORT SUMMARY")
        print("=" * 80)
        print(f"Total Sites Imported: {self.import_stats['total_imported']}")
        print(f"By Timeline:")
        for timeline, count in self.import_stats["by_timeline"].items():
            print(f"  {timeline}: {count}")
        print(f"By Source:")
        for source, count in self.import_stats["by_source"].items():
            print(f"  {Path(source).name}: {count}")
        
        if self.import_stats["errors"]:
            print(f"\nErrors: {len(self.import_stats['errors'])}")
            for error in self.import_stats["errors"][:10]:  # Show first 10
                print(f"  - {error}")
        
        return {
            "results": all_results,
            "stats": self.import_stats
        }
    
    def import_everything(self, primary_only: bool = False) -> Dict[str, Any]:
        """
        Main import function - find and import everything.
        
        Args:
            primary_only: If True, only import to PRIMARY timeline
        """
        # Find all heritage files
        print("Searching for heritage data files...")
        files = self.find_all_heritage_files()
        
        total_files = len(files["csv"]) + len(files["json"])
        print(f"Found {total_files} heritage data file(s)")
        print(f"  CSV: {len(files['csv'])}")
        print(f"  JSON: {len(files['json'])}")
        print()
        
        if total_files == 0:
            print("No heritage data files found.")
            print("Looking in:")
            print(f"  - {self.examples_dir}")
            print(f"  - {self.output_dir / 'exports'}")
            print()
            print("To import data:")
            print("  1. Place CSV/JSON files in examples/ directory")
            print("  2. Or use: python scripts/heritage_batch_import.py <file>")
            return {"error": "No files found"}
        
        # Import to all timelines
        return self.import_to_all_timelines(files, primary_only=primary_only)


def main():
    """Main execution for importing everything."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Import all heritage data to all timelines')
    parser.add_argument('--primary-only', action='store_true',
                       help='Only import to PRIMARY timeline (faster)')
    parser.add_argument('--file', type=Path, help='Specific file to import')
    parser.add_argument('--timeline', default=None,
                       choices=[d.value for d in TimelineDimension],
                       help='Specific timeline to import to')
    
    args = parser.parse_args()
    
    if not IMPORT_AVAILABLE:
        print("Error: Import system not available")
        return
    
    importer = HeritageImportEverything()
    
    if args.file:
        # Import specific file
        if not args.file.exists():
            print(f"Error: File not found: {args.file}")
            return
        
        timeline = args.timeline or TimelineDimension.PRIMARY.value
        
        if args.file.suffix.lower() == '.csv':
            results = importer.import_from_csv(args.file, timeline)
        elif args.file.suffix.lower() == '.json':
            results = importer.import_from_json(args.file, timeline)
        else:
            print(f"Error: Unsupported file format: {args.file.suffix}")
            return
        
        print(f"Imported {len(results)} sites from {args.file.name}")
    else:
        # Import everything
        results = importer.import_everything(primary_only=args.primary_only)
    
    print()
    print("=" * 80)
    print("PEACE, LOVE, UNITY")
    print("ENERGY + LOVE = WE ALL WIN")
    print("=" * 80)


if __name__ == "__main__":
    main()
