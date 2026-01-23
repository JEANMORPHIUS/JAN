"""
HERITAGE CHANNEL SYNC
Sync heritage data to all relevant channels to show the world

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

The work is never done - we need to import all data into all relevant channels.
We have to show the world.
"""

import sys
import json
from pathlib import Path
from typing import Dict, Any, List
from datetime import datetime

try:
    sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))
    from heritage_data_export import HeritageDataExporter
    from logging_config import get_logger
    SYNC_AVAILABLE = True
except ImportError as e:
    print(f"Error: {e}")
    SYNC_AVAILABLE = False

logger = get_logger(__name__) if SYNC_AVAILABLE else None


class HeritageChannelSync:
    """
    Sync heritage data to all relevant channels.
    
    Channels:
    - Local exports (JSON, CSV, Markdown, HTML, GeoJSON)
    - Documentation (auto-generated docs)
    - API endpoints (REST API)
    - Web visualization (HTML reports)
    - Map visualization (GeoJSON for maps)
    - Statistics dashboard (JSON stats)
    """
    
    def __init__(self):
        if not SYNC_AVAILABLE:
            raise RuntimeError("Channel sync not available - check imports")
        self.exporter = HeritageDataExporter()
        self.sync_timestamp = datetime.now().isoformat()
    
    def sync_all_channels(self, output_base: Path = None) -> Dict[str, Any]:
        """
        Sync heritage data to all channels.
        
        Returns:
            Dictionary with sync results for each channel
        """
        if output_base is None:
            output_base = Path(__file__).parent.parent / "output"
        
        sync_results = {
            "sync_timestamp": self.sync_timestamp,
            "channels": {}
        }
        
        print("=" * 80)
        print("HERITAGE CHANNEL SYNC")
        print("Show the World - Sync to All Channels")
        print("=" * 80)
        print()
        
        # Channel 1: Local Exports
        print("Channel 1: Local Exports (JSON, CSV, Markdown, HTML, GeoJSON)...")
        try:
            exported_files = self.exporter.export_all_sites(output_base / "exports")
            sync_results["channels"]["local_exports"] = {
                "status": "success",
                "files": {k: str(v) for k, v in exported_files.items()},
                "count": len(exported_files)
            }
            print(f"  [OK] Exported to {len(exported_files)} formats")
        except Exception as e:
            sync_results["channels"]["local_exports"] = {
                "status": "error",
                "error": str(e)
            }
            print(f"  [ERROR] Error: {e}")
        
        # Channel 2: Statistics
        print()
        print("Channel 2: Statistics Dashboard...")
        try:
            stats = self.exporter.export_statistics(output_base / "exports")
            sync_results["channels"]["statistics"] = {
                "status": "success",
                "total_sites": stats["total_sites"],
                "timelines": len(stats["by_timeline"]),
                "countries": len(stats["by_country"]),
                "patterns": len(stats["patterns"])
            }
            print(f"  [OK] Statistics: {stats['total_sites']} sites, {len(stats['by_timeline'])} timelines")
        except Exception as e:
            sync_results["channels"]["statistics"] = {
                "status": "error",
                "error": str(e)
            }
            print(f"  [ERROR] Error: {e}")
        
        # Channel 3: Documentation
        print()
        print("Channel 3: Auto-Generated Documentation...")
        try:
            doc_path = self._generate_documentation(output_base / "docs" / "exports")
            sync_results["channels"]["documentation"] = {
                "status": "success",
                "file": str(doc_path)
            }
            print(f"  [OK] Documentation generated: {doc_path.name}")
        except Exception as e:
            sync_results["channels"]["documentation"] = {
                "status": "error",
                "error": str(e)
            }
            print(f"  [ERROR] Error: {e}")
        
        # Channel 4: Web-Ready HTML
        print()
        print("Channel 4: Web-Ready HTML Reports...")
        try:
            web_path = self._generate_web_reports(output_base / "web")
            sync_results["channels"]["web_reports"] = {
                "status": "success",
                "file": str(web_path)
            }
            print(f"  [OK] Web report generated: {web_path.name}")
        except Exception as e:
            sync_results["channels"]["web_reports"] = {
                "status": "error",
                "error": str(e)
            }
            print(f"  [ERROR] Error: {e}")
        
        # Channel 5: API Documentation
        print()
        print("Channel 5: API Documentation...")
        try:
            api_doc_path = self._generate_api_documentation(output_base / "docs" / "api")
            sync_results["channels"]["api_documentation"] = {
                "status": "success",
                "file": str(api_doc_path)
            }
            print(f"  [OK] API documentation generated: {api_doc_path.name}")
        except Exception as e:
            sync_results["channels"]["api_documentation"] = {
                "status": "error",
                "error": str(e)
            }
            print(f"  [ERROR] Error: {e}")
        
        # Save sync report
        sync_report_path = output_base / "exports" / f"channel_sync_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(sync_report_path, 'w', encoding='utf-8') as f:
            json.dump(sync_results, f, indent=2, default=str)
        
        print()
        print("=" * 80)
        print("SYNC COMPLETE")
        print("=" * 80)
        print()
        print(f"Sync report saved to: {sync_report_path}")
        print()
        
        # Summary
        successful = sum(1 for ch in sync_results["channels"].values() if ch.get("status") == "success")
        total = len(sync_results["channels"])
        print(f"Channels synced: {successful}/{total}")
        
        return sync_results
    
    def _generate_documentation(self, output_dir: Path) -> Path:
        """Generate comprehensive documentation."""
        output_dir.mkdir(parents=True, exist_ok=True)
        
        from heritage_data_export import HeritageDataExporter
        exporter = HeritageDataExporter()
        
        # Get all sites
        all_sites = []
        from temporal_heritage_registry import get_sites_by_timeline, TimelineDimension
        
        for dimension in TimelineDimension:
            sites = get_sites_by_timeline(dimension.value)
            all_sites.extend(sites)
        
        # Generate markdown documentation
        doc_path = output_dir / f"HERITAGE_DATA_EXPORT_{datetime.now().strftime('%Y%m%d')}.md"
        
        md_content = f"""# Heritage Data Export Documentation

**Generated:** {self.sync_timestamp}  
**Total Sites:** {len(all_sites)}

## Overview

This document provides comprehensive information about all heritage sites in the archive.

## Statistics

- **Total Sites:** {len(all_sites)}
- **Timelines:** {len(set(s.get('timeline_dimension', 'unknown') for s in all_sites))}
- **Countries:** {len(set(s.get('country', 'unknown') for s in all_sites if s.get('country')))}

## Data Export Formats

All data is available in multiple formats:

1. **JSON** - For APIs and programmatic access
2. **CSV** - For spreadsheets and analysis
3. **Markdown** - For documentation
4. **HTML** - For web display
5. **GeoJSON** - For map visualization

## Access Points

- **REST API:** `/api/heritage/*` endpoints
- **Local Exports:** `output/exports/` directory
- **Web Reports:** `output/web/` directory
- **Documentation:** `docs/exports/` directory

## Export Commands

```bash
# Export all formats
python scripts/heritage_data_export.py --format all

# Export specific format
python scripts/heritage_data_export.py --format json
python scripts/heritage_data_export.py --format csv
python scripts/heritage_data_export.py --format html

# Export statistics
python scripts/heritage_data_export.py --format stats
```

## PEACE, LOVE, UNITY
## ENERGY + LOVE = WE ALL WIN
"""
        
        with open(doc_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        return doc_path
    
    def _generate_web_reports(self, output_dir: Path) -> Path:
        """Generate web-ready HTML reports."""
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # This will use the HTML export from HeritageDataExporter
        from heritage_data_export import HeritageDataExporter
        exporter = HeritageDataExporter()
        
        # Get all sites
        all_sites = []
        from temporal_heritage_registry import get_sites_by_timeline, TimelineDimension
        
        for dimension in TimelineDimension:
            sites = get_sites_by_timeline(dimension.value)
            all_sites.extend(sites)
        
        # Export to HTML
        html_path = output_dir / f"heritage_index_{datetime.now().strftime('%Y%m%d')}.html"
        exporter._export_to_html(all_sites, html_path)
        
        return html_path
    
    def _generate_api_documentation(self, output_dir: Path) -> Path:
        """Generate API documentation."""
        output_dir.mkdir(parents=True, exist_ok=True)
        
        api_doc_path = output_dir / f"HERITAGE_API_DOCUMENTATION_{datetime.now().strftime('%Y%m%d')}.md"
        
        api_doc = """# Heritage API Documentation

## Base URL
```
http://localhost:8000/api/heritage
```

## Endpoints

### Get Timeline Sites
```http
GET /api/heritage/timeline/{dimension}
```

**Parameters:**
- `dimension` - Timeline dimension (primary, parallel, past_loop, future_loop, regeneration, alternate)
- `period` (optional) - Time period filter

**Example:**
```bash
curl http://localhost:8000/api/heritage/timeline/primary
```

### Get Chronology
```http
GET /api/heritage/chronology?start_year={year}&end_year={year}
```

**Parameters:**
- `start_year` - Start year
- `end_year` - End year
- `timeline` (optional) - Timeline dimension filter

**Example:**
```bash
curl "http://localhost:8000/api/heritage/chronology?start_year=1800&end_year=2000"
```

### Get Temporal Patterns
```http
GET /api/heritage/patterns
```

**Example:**
```bash
curl http://localhost:8000/api/heritage/patterns
```

### Get Site Details
```http
GET /api/heritage/site/{site_id}
```

**Example:**
```bash
curl http://localhost:8000/api/heritage/site/1
```

### Create Site
```http
POST /api/heritage/site
Content-Type: application/json

{
  "site_name": "Example Site",
  "site_type": "Heritage Property",
  "region": "Example Region",
  "country": "Example Country",
  ...
}
```

### Search Sites
```http
GET /api/heritage/search?q={query}
```

**Example:**
```bash
curl "http://localhost:8000/api/heritage/search?q=Cyprus"
```

### Get Statistics
```http
GET /api/heritage/stats
```

**Example:**
```bash
curl http://localhost:8000/api/heritage/stats
```

## Response Formats

All endpoints return JSON with the following structure:

```json
{
  "data": [...],
  "count": 0,
  "timestamp": "2026-01-20T..."
}
```

## Error Handling

Errors are returned with appropriate HTTP status codes:

- `400` - Bad Request (invalid parameters)
- `404` - Not Found (resource not found)
- `500` - Internal Server Error

## PEACE, LOVE, UNITY
## ENERGY + LOVE = WE ALL WIN
"""
        
        with open(api_doc_path, 'w', encoding='utf-8') as f:
            f.write(api_doc)
        
        return api_doc_path


def main():
    """Main execution for channel sync."""
    if not SYNC_AVAILABLE:
        print("Error: Channel sync not available")
        return
    
    sync = HeritageChannelSync()
    results = sync.sync_all_channels()
    
    print()
    print("=" * 80)
    print("PEACE, LOVE, UNITY")
    print("ENERGY + LOVE = WE ALL WIN")
    print("=" * 80)


if __name__ == "__main__":
    main()
