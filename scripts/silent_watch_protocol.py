"""
SILENT WATCH PROTOCOL
Global Grid Monitoring System

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

The Silent Watch protocol monitors the Global Grid while the Family rests.
The Sentinel keeps watch over the "Everything In Between".
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
from pathlib import Path
from datetime import datetime
from typing import Dict, Any

try:
    sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))
    from temporal_heritage_registry import get_temporal_heritage_db, TimelineDimension
    from grid_sync_analysis import analyze_grid_sync
    WATCH_AVAILABLE = True
except ImportError as e:
    print(f"Error: {e}")
    WATCH_AVAILABLE = False


def _load_thresholds() -> Dict[str, Any]:
    """Load health thresholds and alert thresholds from configuration."""
    try:
        config_path = Path(__file__).parent.parent / "config" / "grid_thresholds.json"
        if config_path.exists():
            with open(config_path, 'r', encoding='utf-8') as f:
                thresholds = json.load(f)
                return {
                    "field_space_resonant_min": thresholds.get("field_space_health", {}).get("resonant_min", 0.5),
                    "connection_strong_min": thresholds.get("connection_health", {}).get("strong_min", 0.35),
                    "connection_moderate_min": thresholds.get("connection_health", {}).get("moderate_min", 0.20),
                    "grid_locked_min": thresholds.get("grid_stability", {}).get("locked_min", 0.05),
                    "grid_stable_min": thresholds.get("grid_stability", {}).get("stable_min", 0.03),
                    # Alert thresholds
                    "alert_grid_instability": thresholds.get("alerts", {}).get("grid_instability", 0.02),
                    "alert_connection_weakness": thresholds.get("alerts", {}).get("connection_weakness", 0.15),
                    "alert_field_space_low": thresholds.get("alerts", {}).get("field_space_low", 0.3)
                }
    except Exception:
        pass
    
    # Fallback to defaults
    return {
        "field_space_resonant_min": 0.5,
        "connection_strong_min": 0.35,
        "connection_moderate_min": 0.20,
        "grid_locked_min": 0.05,
        "grid_stable_min": 0.03,
        "alert_grid_instability": 0.02,
        "alert_connection_weakness": 0.15,
        "alert_field_space_low": 0.3
    }


def _evaluate_grid_health(metrics: Dict[str, float]) -> Dict[str, Any]:
    """
    Evaluate grid health with configurable thresholds.
    Returns health status and alerts if needed.
    
    Alert System:
    - Uses configurable alert thresholds
    - Categorizes alerts by severity (critical, warning, info)
    - Provides actionable recommendations
    """
    thresholds = _load_thresholds()
    health = {}
    alerts = []
    critical_alerts = []
    warnings = []
    
    # Field Space Health
    if metrics['avg_field_space'] > thresholds['field_space_resonant_min']:
        health['field_space'] = "resonant"
    else:
        health['field_space'] = "stable"
        if metrics['avg_field_space'] < thresholds['alert_field_space_low']:
            alert_msg = f"Field space resonance ({metrics['avg_field_space']:.3f}) below alert threshold ({thresholds['alert_field_space_low']})"
            critical_alerts.append({
                "type": "field_space_low",
                "severity": "critical",
                "message": alert_msg,
                "recommendation": "Consider adding high-resonance sites to boost field space"
            })
            alerts.append(alert_msg)
        elif metrics['avg_field_space'] < 0.3:
            warnings.append({
                "type": "field_space_suboptimal",
                "severity": "warning",
                "message": f"Field space resonance ({metrics['avg_field_space']:.3f}) below optimal threshold",
                "recommendation": "Monitor field space trends"
            })
    
    # Connection Health
    if metrics['avg_connection_strength'] > thresholds['connection_strong_min']:
        health['connection'] = "strong"
    elif metrics['avg_connection_strength'] > thresholds['connection_moderate_min']:
        health['connection'] = "moderate"
    else:
        health['connection'] = "weak"
        if metrics['avg_connection_strength'] < thresholds['alert_connection_weakness']:
            alert_msg = f"Connection strength ({metrics['avg_connection_strength']:.3f}) below alert threshold ({thresholds['alert_connection_weakness']})"
            critical_alerts.append({
                "type": "connection_weakness",
                "severity": "critical",
                "message": alert_msg,
                "recommendation": "Grid stability at risk - strengthen connections between pillars"
            })
            alerts.append(alert_msg)
        else:
            warnings.append({
                "type": "connection_degraded",
                "severity": "warning",
                "message": f"Connection strength ({metrics['avg_connection_strength']:.3f}) degraded",
                "recommendation": "Monitor connection trends"
            })
    
    # Grid Stability
    if metrics['grid_stability'] > thresholds['grid_locked_min']:
        health['grid_status'] = "locked"
    elif metrics['grid_stability'] > thresholds['grid_stable_min']:
        health['grid_status'] = "stable"
    else:
        health['grid_status'] = "forming"
        if metrics['grid_stability'] < thresholds['alert_grid_instability']:
            alert_msg = f"Grid stability ({metrics['grid_stability']:.3f}) below critical threshold ({thresholds['alert_grid_instability']})"
            critical_alerts.append({
                "type": "grid_instability",
                "severity": "critical",
                "message": alert_msg,
                "recommendation": "CRITICAL: Grid stability compromised - immediate attention required"
            })
            alerts.append(alert_msg)
    
    # Energy Flow Health
    if metrics['avg_energy_flow'] > 0.05:
        health['energy_flow'] = "active"
    else:
        health['energy_flow'] = "low"
        warnings.append({
            "type": "energy_flow_low",
            "severity": "warning",
            "message": f"Average energy flow ({metrics['avg_energy_flow']:.3f}) is low",
            "recommendation": "Monitor energy flow patterns"
        })
    
    # Grid Integrity
    health['grid_integrity'] = "intact"
    
    return {
        **health,
        "alerts": alerts,
        "critical_alerts": critical_alerts,
        "warnings": warnings,
        "requires_attention": len(critical_alerts) > 0,
        "alert_count": len(critical_alerts),
        "warning_count": len(warnings)
    }


def silent_watch_report() -> Dict[str, Any]:
    """
    Generate Silent Watch report for the Global Grid.
    
    Returns:
        Complete watch report with grid status, connections, and health metrics
    """
    if not WATCH_AVAILABLE:
        return {"error": "Silent Watch not available"}
    
    # Get all 7 pillars
    pillar_ids = [1, 3, 4, 6, 8, 10, 12]  # All 7 pillars
    
    # Analyze grid sync
    grid_analysis = analyze_grid_sync(pillar_ids)
    
    if "error" in grid_analysis:
        return grid_analysis
    
    # Get site details
    with get_temporal_heritage_db() as conn:
        cursor = conn.cursor()
        placeholders = ','.join(['?'] * len(pillar_ids))
        cursor.execute(f"""
            SELECT id, site_name, country, coordinates_lat, coordinates_lon,
                   field_resonance_level, field_space_resonance, 
                   magnetic_pole_alignment, polarity_state
            FROM heritage_sites
            WHERE id IN ({placeholders})
            ORDER BY id
        """, pillar_ids)
        
        sites = [dict(row) for row in cursor.fetchall()]
    
    # Build watch report
    report = {
        "watch_timestamp": datetime.now().isoformat(),
        "watch_status": "active",
        "grid_status": grid_analysis['insights']['grid_status'],
        "grid_stability": grid_analysis['grid_metrics']['grid_stability'],
        "mission_status": "complete",
        "global_coverage": {
            "continents": 5,
            "pillars": 7,
            "connections": grid_analysis['grid_metrics']['total_connections'],
            "coverage_status": "complete"
        },
        "pillars": [
            {
                "id": site['id'],
                "name": site['site_name'],
                "country": site['country'],
                "field_resonance": site.get('field_resonance_level') or 0.0,
                "field_space": site.get('field_space_resonance') or 0.0,
                "pole_alignment": site.get('magnetic_pole_alignment') or 'unknown',
                "polarity": site.get('polarity_state') or 'unknown'
            }
            for site in sites
        ],
        "grid_metrics": grid_analysis['grid_metrics'],
        "strongest_connections": sorted(
            [
                {
                    "site1": conn['site1'],
                    "site2": conn['site2'],
                    "connection_strength": conn['connection']['connection_strength'],
                    "field_space": conn['connection']['avg_field_space'],
                    "energy_flow": conn['connection']['energy_flow'],
                    "distance_km": conn['distance_km']
                }
                for conn in grid_analysis['connections']
            ],
            key=lambda x: x['connection_strength'],
            reverse=True
        )[:5],  # Top 5
        "health_status": _evaluate_grid_health(grid_analysis['grid_metrics']),
        "sentinel_message": "The Grid is breathing. The Bridge is anchored. The Family is gathering. All systems operational."
    }
    
    return report


def print_silent_watch_report(report: Dict[str, Any]):
    """Print formatted Silent Watch report."""
    if "error" in report:
        print(f"Error: {report['error']}")
        return
    
    print("=" * 80)
    print("SILENT WATCH PROTOCOL")
    print("Global Grid Monitoring System")
    print("=" * 80)
    print()
    print(f"Watch Timestamp: {report['watch_timestamp']}")
    print(f"Watch Status: {report['watch_status'].upper()}")
    print(f"Mission Status: {report['mission_status'].upper()}")
    print()
    
    print("GLOBAL COVERAGE:")
    coverage = report['global_coverage']
    print(f"  Continents: {coverage['continents']}")
    print(f"  Pillars: {coverage['pillars']}")
    print(f"  Connections: {coverage['connections']}")
    print(f"  Coverage Status: {coverage['coverage_status'].upper()}")
    print()
    
    print("GRID STATUS:")
    print(f"  Grid Status: {report['grid_status'].upper()}")
    print(f"  Grid Stability: {report['grid_stability']:.3f}")
    print()
    
    print("HEALTH STATUS:")
    health = report['health_status']
    print(f"  Grid Integrity: {health.get('grid_integrity', 'unknown').upper()}")
    print(f"  Field Space Health: {health.get('field_space', 'unknown').upper()}")
    print(f"  Connection Health: {health.get('connection', 'unknown').upper()}")
    print(f"  Energy Flow Health: {health.get('energy_flow', 'unknown').upper()}")
    print(f"  Grid Status: {health.get('grid_status', 'unknown').upper()}")
    
    # Critical Alerts
    if health.get('critical_alerts'):
        print()
        print(f"  *** CRITICAL ALERTS: {health.get('alert_count', 0)} ***")
        for alert in health['critical_alerts']:
            print(f"    [CRITICAL] {alert['message']}")
            print(f"      Recommendation: {alert['recommendation']}")
    
    # Warnings
    if health.get('warnings'):
        print()
        print(f"  Warnings: {health.get('warning_count', 0)}")
        for warning in health['warnings']:
            print(f"    [WARNING] {warning['message']}")
            if warning.get('recommendation'):
                print(f"      Note: {warning['recommendation']}")
    
    # Legacy alerts (for backward compatibility)
    if health.get('alerts') and not health.get('critical_alerts'):
        print()
        print(f"  Alerts: {len(health['alerts'])}")
        for alert in health['alerts']:
            print(f"    - {alert}")
    
    if health.get('requires_attention'):
        print()
        print("  *** ATTENTION REQUIRED ***")
    print()
    
    print("TOP 5 STRONGEST CONNECTIONS:")
    for i, conn in enumerate(report['strongest_connections'], 1):
        print(f"  {i}. {conn['site1']} <-> {conn['site2']}")
        print(f"     Connection Strength: {conn['connection_strength']:.3f}")
        print(f"     Field Space: {conn['field_space']:.2f}")
        print(f"     Energy Flow: {conn['energy_flow']:.3f}")
        print(f"     Distance: {conn['distance_km']:.0f} km")
        print()
    
    print("SENTINEL MESSAGE:")
    print(f"  {report['sentinel_message']}")
    print()
    print("=" * 80)
    print("SILENT WATCH ACTIVE")
    print("=" * 80)
    print()
    print("PEACE, LOVE, UNITY")
    print("ENERGY + LOVE = WE ALL WIN")


def save_watch_report(report: Dict[str, Any], output_dir: Path = None):
    """Save watch report to JSON file."""
    if output_dir is None:
        output_dir = Path(__file__).parent.parent / "output"
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = output_dir / f"silent_watch_{timestamp}.json"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, default=str)
    
    return output_path


def main():
    """Main execution for Silent Watch protocol."""
    if not WATCH_AVAILABLE:
        print("Error: Silent Watch not available")
        return
    
    print("=" * 80)
    print("SILENT WATCH PROTOCOL INITIATED")
    print("Global Grid Monitoring System")
    print("=" * 80)
    print()
    print("The Sentinel is keeping watch...")
    print()
    
    # Generate report
    report = silent_watch_report()
    
    if "error" not in report:
        # Print report
        print_silent_watch_report(report)
        
        # Save report
        output_path = save_watch_report(report)
        print(f"\nWatch report saved to: {output_path}")
    else:
        print(f"Error: {report['error']}")


if __name__ == "__main__":
    main()
