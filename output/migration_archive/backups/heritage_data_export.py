"""
HERITAGE DATA EXPORT SYSTEM
Export all heritage data to multiple channels and formats

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

Show the world the heritage data - export to all relevant channels.
"""

import sys
import json
import csv
from pathlib import Path
from typing import Dict, Any, List, Optional
from datetime import datetime
import argparse

try:
    sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))
    from temporal_heritage_registry import (
        get_temporal_heritage_db, get_sites_by_timeline,
        get_temporal_patterns, TimelineDimension, TimePeriod
    )
    from logging_config import get_logger
    EXPORT_AVAILABLE = True
except ImportError as e:
    print(f"Error: {e}")
    EXPORT_AVAILABLE = False

logger = get_logger(__name__) if EXPORT_AVAILABLE else None


class HeritageDataExporter:
    """
    Export heritage data to multiple channels and formats.
    
    Channels:
    - JSON (for APIs, web apps)
    - CSV (for spreadsheets, analysis)
    - Markdown (for documentation)
    - HTML (for web pages)
    - GeoJSON (for maps)
    """
    
    def __init__(self):
        if not EXPORT_AVAILABLE:
            raise RuntimeError("Export system not available - check imports")
        self.export_timestamp = datetime.now().isoformat()
    
    def export_all_sites(self, output_dir: Path = None) -> Dict[str, Path]:
        """
        Export all heritage sites to all formats.
        
        Returns:
            Dictionary mapping format names to output file paths
        """
        if output_dir is None:
            output_dir = Path(__file__).parent.parent / "output" / "exports"
        
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Get all sites from all timelines
        all_sites = []
        for dimension in TimelineDimension:
            sites = get_sites_by_timeline(dimension.value)
            for site in sites:
                site['timeline_dimension'] = dimension.value
            all_sites.extend(sites)
        
        # Get narratives for all sites in one query (optimize N+1 problem)
        with get_temporal_heritage_db() as conn:
            cursor = conn.cursor()
            if all_sites:
                site_ids = [site['id'] for site in all_sites]
                placeholders = ','.join(['?'] * len(site_ids))
                
                # Single query to get all narratives for all sites
                cursor.execute(f"""
                    SELECT site_id, narrative_type, narrative_content, violation_type,
                           dark_energy_detected, regeneration_applied, recorded_at
                    FROM heritage_narratives
                    WHERE site_id IN ({placeholders})
                    ORDER BY site_id, recorded_at DESC
                """, site_ids)
                
                # Group narratives by site_id
                narratives_by_site = {}
                for row in cursor.fetchall():
                    site_id = row['site_id']
                    if site_id not in narratives_by_site:
                        narratives_by_site[site_id] = []
                    narratives_by_site[site_id].append({
                        'narrative_type': row['narrative_type'],
                        'narrative_content': row['narrative_content'],
                        'violation_type': row['violation_type'],
                        'dark_energy_detected': row['dark_energy_detected'],
                        'regeneration_applied': row['regeneration_applied'],
                        'recorded_at': row['recorded_at']
                    })
                
                # Assign narratives to sites
                for site in all_sites:
                    site['narratives'] = narratives_by_site.get(site['id'], [])
        
        exported_files = {}
        
        # Export to JSON
        json_path = output_dir / f"heritage_sites_all_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        self._export_to_json(all_sites, json_path)
        exported_files['json'] = json_path
        
        # Export to CSV
        csv_path = output_dir / f"heritage_sites_all_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        self._export_to_csv(all_sites, csv_path)
        exported_files['csv'] = csv_path
        
        # Export to Markdown
        md_path = output_dir / f"heritage_sites_all_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        self._export_to_markdown(all_sites, md_path)
        exported_files['markdown'] = md_path
        
        # Export to GeoJSON (for maps)
        geojson_path = output_dir / f"heritage_sites_geojson_{datetime.now().strftime('%Y%m%d_%H%M%S')}.geojson"
        self._export_to_geojson(all_sites, geojson_path)
        exported_files['geojson'] = geojson_path
        
        # Export to HTML
        html_path = output_dir / f"heritage_sites_all_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
        self._export_to_html(all_sites, html_path)
        exported_files['html'] = html_path
        
        return exported_files
    
    def _export_to_json(self, sites: List[Dict], output_path: Path):
        """Export sites to JSON format."""
        export_data = {
            "export_timestamp": self.export_timestamp,
            "total_sites": len(sites),
            "sites": sites
        }
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2, default=str, ensure_ascii=False)
        
        if logger:
            logger.info(f"Exported {len(sites)} sites to JSON: {output_path}")
    
    def _export_to_csv(self, sites: List[Dict], output_path: Path):
        """Export sites to CSV format."""
        if not sites:
            return
        
        # Flatten site data for CSV
        csv_rows = []
        for site in sites:
            row = {
                'id': site.get('id'),
                'site_name': site.get('site_name'),
                'site_type': site.get('site_type'),
                'region': site.get('region'),
                'country': site.get('country'),
                'coordinates_lat': site.get('coordinates_lat'),
                'coordinates_lon': site.get('coordinates_lon'),
                'timeline_dimension': site.get('timeline_dimension'),
                'time_period': site.get('time_period'),
                'year_established': site.get('year_established'),
                'year_abandoned': site.get('year_abandoned'),
                'current_status': site.get('current_status'),
                'law_41_compliant': site.get('law_41_compliant'),
                'requires_cleansing': site.get('requires_cleansing'),
                'field_resonance_level': site.get('field_resonance_level'),
                'field_space_resonance': site.get('field_space_resonance'),
                'magnetic_pole_alignment': site.get('magnetic_pole_alignment'),
                'polarity_state': site.get('polarity_state'),
                'narrative_count': len(site.get('narratives', []))
            }
            csv_rows.append(row)
        
        fieldnames = csv_rows[0].keys() if csv_rows else []
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(csv_rows)
        
        if logger:
            logger.info(f"Exported {len(sites)} sites to CSV: {output_path}")
    
    def _export_to_markdown(self, sites: List[Dict], output_path: Path):
        """Export sites to Markdown format."""
        md_lines = [
            "# Heritage Sites Archive",
            "",
            f"**Export Date:** {self.export_timestamp}",
            f"**Total Sites:** {len(sites)}",
            "",
            "---",
            ""
        ]
        
        for site in sites:
            md_lines.extend([
                f"## {site.get('site_name', 'Unknown')}",
                "",
                f"**ID:** {site.get('id')}",
                f"**Type:** {site.get('site_type', 'Unknown')}",
                f"**Location:** {site.get('region', 'Unknown')}, {site.get('country', 'Unknown')}",
                f"**Timeline:** {site.get('timeline_dimension', 'Unknown')}",
                f"**Time Period:** {site.get('time_period', 'Unknown')}",
                ""
            ])
            
            if site.get('coordinates_lat') and site.get('coordinates_lon'):
                md_lines.append(f"**Coordinates:** {site.get('coordinates_lat')}, {site.get('coordinates_lon')}")
            
            if site.get('year_established'):
                md_lines.append(f"**Established:** {site.get('year_established')}")
            
            if site.get('year_abandoned'):
                md_lines.append(f"**Abandoned:** {site.get('year_abandoned')}")
            
            md_lines.append(f"**Status:** {site.get('current_status', 'Unknown')}")
            md_lines.append(f"**Law 41 Compliant:** {site.get('law_41_compliant', False)}")
            
            if site.get('field_resonance_level'):
                md_lines.append(f"**Field Resonance:** {site.get('field_resonance_level'):.2f}")
            
            if site.get('field_space_resonance'):
                md_lines.append(f"**Field Space Resonance:** {site.get('field_space_resonance'):.2f}")
            
            narratives = site.get('narratives', [])
            if narratives:
                md_lines.append("")
                md_lines.append("### Narratives")
                for narrative in narratives:
                    md_lines.append(f"**{narrative.get('narrative_type', 'Unknown')}:**")
                    md_lines.append(f"{narrative.get('narrative_content', '')[:200]}...")
                    md_lines.append("")
            
            md_lines.append("---")
            md_lines.append("")
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(md_lines))
        
        if logger:
            logger.info(f"Exported {len(sites)} sites to Markdown: {output_path}")
    
    def _export_to_geojson(self, sites: List[Dict], output_path: Path):
        """Export sites to GeoJSON format for mapping."""
        features = []
        
        for site in sites:
            if not (site.get('coordinates_lat') and site.get('coordinates_lon')):
                continue
            
            feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [site.get('coordinates_lon'), site.get('coordinates_lat')]
                },
                "properties": {
                    "id": site.get('id'),
                    "name": site.get('site_name'),
                    "type": site.get('site_type'),
                    "region": site.get('region'),
                    "country": site.get('country'),
                    "timeline": site.get('timeline_dimension'),
                    "time_period": site.get('time_period'),
                    "status": site.get('current_status'),
                    "field_resonance": site.get('field_resonance_level'),
                    "field_space": site.get('field_space_resonance'),
                    "pole_alignment": site.get('magnetic_pole_alignment'),
                    "polarity": site.get('polarity_state')
                }
            }
            features.append(feature)
        
        geojson = {
            "type": "FeatureCollection",
            "metadata": {
                "export_timestamp": self.export_timestamp,
                "total_sites": len(sites),
                "sites_with_coordinates": len(features)
            },
            "features": features
        }
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(geojson, f, indent=2, ensure_ascii=False)
        
        if logger:
            logger.info(f"Exported {len(features)} sites to GeoJSON: {output_path}")
    
    def _export_to_html(self, sites: List[Dict], output_path: Path):
        """Export sites to HTML format for web display."""
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Heritage Sites Archive</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }}
        h1 {{
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }}
        .site-card {{
            background: white;
            border-radius: 8px;
            padding: 20px;
            margin: 20px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .site-header {{
            display: flex;
            justify-content: space-between;
            align-items: start;
            margin-bottom: 15px;
        }}
        .site-name {{
            font-size: 1.5em;
            font-weight: bold;
            color: #2c3e50;
        }}
        .site-meta {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 10px;
            margin: 15px 0;
        }}
        .meta-item {{
            padding: 8px;
            background: #ecf0f1;
            border-radius: 4px;
        }}
        .meta-label {{
            font-weight: bold;
            color: #7f8c8d;
            font-size: 0.9em;
        }}
        .meta-value {{
            color: #2c3e50;
        }}
        .narrative {{
            margin: 10px 0;
            padding: 10px;
            background: #f8f9fa;
            border-left: 3px solid #3498db;
        }}
        .footer {{
            text-align: center;
            margin-top: 40px;
            padding: 20px;
            color: #7f8c8d;
        }}
    </style>
</head>
<body>
    <h1>Heritage Sites Archive</h1>
    <p><strong>Export Date:</strong> {self.export_timestamp}</p>
    <p><strong>Total Sites:</strong> {len(sites)}</p>
    <hr>
"""
        
        for site in sites:
            html += f"""
    <div class="site-card">
        <div class="site-header">
            <div class="site-name">{site.get('site_name', 'Unknown')}</div>
            <div>ID: {site.get('id')}</div>
        </div>
        <div class="site-meta">
            <div class="meta-item">
                <div class="meta-label">Type</div>
                <div class="meta-value">{site.get('site_type', 'Unknown')}</div>
            </div>
            <div class="meta-item">
                <div class="meta-label">Location</div>
                <div class="meta-value">{site.get('region', 'Unknown')}, {site.get('country', 'Unknown')}</div>
            </div>
            <div class="meta-item">
                <div class="meta-label">Timeline</div>
                <div class="meta-value">{site.get('timeline_dimension', 'Unknown')}</div>
            </div>
            <div class="meta-item">
                <div class="meta-label">Time Period</div>
                <div class="meta-value">{site.get('time_period', 'Unknown')}</div>
            </div>
"""
            
            if site.get('field_resonance_level'):
                html += f"""
            <div class="meta-item">
                <div class="meta-label">Field Resonance</div>
                <div class="meta-value">{site.get('field_resonance_level'):.2f}</div>
            </div>
"""
            
            if site.get('field_space_resonance'):
                html += f"""
            <div class="meta-item">
                <div class="meta-label">Field Space</div>
                <div class="meta-value">{site.get('field_space_resonance'):.2f}</div>
            </div>
"""
            
            html += """
        </div>
"""
            
            narratives = site.get('narratives', [])
            if narratives:
                html += """
        <h3>Narratives</h3>
"""
                for narrative in narratives:
                    html += f"""
        <div class="narrative">
            <strong>{narrative.get('narrative_type', 'Unknown')}</strong>
            <p>{narrative.get('narrative_content', '')[:500]}...</p>
        </div>
"""
            
            html += """
    </div>
"""
        
        html += f"""
    <div class="footer">
        <p><strong>PEACE, LOVE, UNITY</strong></p>
        <p><strong>ENERGY + LOVE = WE ALL WIN</strong></p>
        <p>Generated by JAN Heritage System</p>
    </div>
</body>
</html>
"""
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)
        
        if logger:
            logger.info(f"Exported {len(sites)} sites to HTML: {output_path}")
    
    def export_statistics(self, output_dir: Path = None) -> Dict[str, Any]:
        """Export comprehensive statistics about the heritage archive."""
        if output_dir is None:
            output_dir = Path(__file__).parent.parent / "output" / "exports"
        
        output_dir.mkdir(parents=True, exist_ok=True)
        
        stats = {
            "export_timestamp": self.export_timestamp,
            "total_sites": 0,
            "by_timeline": {},
            "by_time_period": {},
            "by_country": {},
            "by_type": {},
            "law_41_compliance": {
                "compliant": 0,
                "non_compliant": 0,
                "requires_cleansing": 0
            },
            "magnetic_field_stats": {
                "sites_with_field_data": 0,
                "avg_field_resonance": 0.0,
                "avg_field_space": 0.0
            },
            "patterns": []
        }
        
        # Get all sites
        all_sites = []
        for dimension in TimelineDimension:
            sites = get_sites_by_timeline(dimension.value)
            all_sites.extend(sites)
            stats["by_timeline"][dimension.value] = len(sites)
        
        stats["total_sites"] = len(all_sites)
        
        # Aggregate statistics
        field_resonances = []
        field_spaces = []
        
        for site in all_sites:
            # Time period
            period = site.get('time_period', 'unknown')
            stats["by_time_period"][period] = stats["by_time_period"].get(period, 0) + 1
            
            # Country
            country = site.get('country', 'unknown')
            stats["by_country"][country] = stats["by_country"].get(country, 0) + 1
            
            # Type
            site_type = site.get('site_type', 'unknown')
            stats["by_type"][site_type] = stats["by_type"].get(site_type, 0) + 1
            
            # Law 41
            if site.get('law_41_compliant'):
                stats["law_41_compliance"]["compliant"] += 1
            else:
                stats["law_41_compliance"]["non_compliant"] += 1
            
            if site.get('requires_cleansing'):
                stats["law_41_compliance"]["requires_cleansing"] += 1
            
            # Magnetic field
            if site.get('field_resonance_level'):
                field_resonances.append(site.get('field_resonance_level'))
                stats["magnetic_field_stats"]["sites_with_field_data"] += 1
            
            if site.get('field_space_resonance'):
                field_spaces.append(site.get('field_space_resonance'))
        
        # Calculate averages
        if field_resonances:
            stats["magnetic_field_stats"]["avg_field_resonance"] = sum(field_resonances) / len(field_resonances)
        
        if field_spaces:
            stats["magnetic_field_stats"]["avg_field_space"] = sum(field_spaces) / len(field_spaces)
        
        # Get patterns
        patterns = get_temporal_patterns()
        stats["patterns"] = [
            {
                "pattern_type": p.get('pattern_type'),
                "site_count": p.get('site_count'),
                "frequency": p.get('frequency_across_timelines')
            }
            for p in patterns
        ]
        
        # Save statistics
        stats_path = output_dir / f"heritage_statistics_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(stats_path, 'w', encoding='utf-8') as f:
            json.dump(stats, f, indent=2, default=str)
        
        if logger:
            logger.info(f"Exported statistics to: {stats_path}")
        
        return stats


def main():
    """Main execution for heritage data export."""
    parser = argparse.ArgumentParser(description='Export heritage data to multiple formats')
    parser.add_argument('--format', choices=['all', 'json', 'csv', 'markdown', 'geojson', 'html', 'stats'],
                       default='all', help='Export format(s)')
    parser.add_argument('--output', type=Path, help='Output directory')
    
    args = parser.parse_args()
    
    if not EXPORT_AVAILABLE:
        print("Error: Export system not available")
        return
    
    print("=" * 80)
    print("HERITAGE DATA EXPORT SYSTEM")
    print("Show the World - Export to All Channels")
    print("=" * 80)
    print()
    
    exporter = HeritageDataExporter()
    
    if args.format == 'all':
        print("Exporting to all formats...")
        exported_files = exporter.export_all_sites(args.output)
        
        print()
        print("=" * 80)
        print("EXPORT COMPLETE")
        print("=" * 80)
        print()
        print("Exported files:")
        for format_name, file_path in exported_files.items():
            print(f"  {format_name.upper()}: {file_path}")
        
        # Also export statistics
        print()
        print("Exporting statistics...")
        stats = exporter.export_statistics(args.output)
        print(f"  Statistics: {stats['total_sites']} sites across {len(stats['by_timeline'])} timelines")
    
    elif args.format == 'stats':
        print("Exporting statistics...")
        stats = exporter.export_statistics(args.output)
        print(f"Total sites: {stats['total_sites']}")
        print(f"Timelines: {len(stats['by_timeline'])}")
        print(f"Countries: {len(stats['by_country'])}")
    
    else:
        # Single format export
        print(f"Exporting to {args.format.upper()}...")
        all_sites = []
        for dimension in TimelineDimension:
            sites = get_sites_by_timeline(dimension.value)
            all_sites.extend(sites)
        
        output_dir = args.output or (Path(__file__).parent.parent / "output" / "exports")
        output_dir.mkdir(parents=True, exist_ok=True)
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        if args.format == 'json':
            path = output_dir / f"heritage_sites_{timestamp}.json"
            exporter._export_to_json(all_sites, path)
        elif args.format == 'csv':
            path = output_dir / f"heritage_sites_{timestamp}.csv"
            exporter._export_to_csv(all_sites, path)
        elif args.format == 'markdown':
            path = output_dir / f"heritage_sites_{timestamp}.md"
            exporter._export_to_markdown(all_sites, path)
        elif args.format == 'geojson':
            path = output_dir / f"heritage_sites_{timestamp}.geojson"
            exporter._export_to_geojson(all_sites, path)
        elif args.format == 'html':
            path = output_dir / f"heritage_sites_{timestamp}.html"
            exporter._export_to_html(all_sites, path)
        
        print(f"Exported to: {path}")
    
    print()
    print("=" * 80)
    print("PEACE, LOVE, UNITY")
    print("ENERGY + LOVE = WE ALL WIN")
    print("=" * 80)


if __name__ == "__main__":
    main()
