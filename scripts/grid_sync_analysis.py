"""
GRID SYNC ANALYSIS
Energy Flow Between Global Grid Pillars

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

This script analyzes energy flow between the three pillars of the Global Grid:
- Berengaria Hotel (Cyprus)
- Alhambra Palace (Spain)
- Stonehenge (England)

The Grid Sync reveals how energy flows through the field space between sites.
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
import math
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime

try:
    sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))
    from temporal_heritage_registry import get_temporal_heritage_db, TimelineDimension
    GRID_SYNC_AVAILABLE = True
except ImportError as e:
    print(f"Error: {e}")
    GRID_SYNC_AVAILABLE = False


def calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Calculate distance between two coordinates in kilometers (Haversine formula)."""
    R = 6371  # Earth's radius in km
    
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    
    return R * c


# Configuration constants for energy decay
ENERGY_DECAY_MODEL = "exponential"  # Options: "exponential", "inverse_square", "modified_inverse"
ENERGY_DECAY_CONSTANT = 0.0002  # Tuned for ~5% remaining at 5000km (exponential model)


def calculate_field_space_connection(
    site1_resonance: float,
    site1_field_space: float,
    site2_resonance: float,
    site2_field_space: float,
    distance_km: float,
    decay_model: str = ENERGY_DECAY_MODEL
) -> Dict[str, Any]:
    """
    Calculate energy flow connection between two sites through field space.
    
    Energy decay follows exponential model (Earth's magnetic field behavior):
    E(d) = E₀ × e^(-λd)
    
    Where:
    - E₀ = initial connection strength
    - λ = decay constant (0.0002 for heritage grid)
    - d = distance in kilometers
    
    The connection flows through the "Everything In Between" - the field space.
    Uses physically accurate energy decay models.
    
    Args:
        site1_resonance: Field resonance of first site (0.0-1.0)
        site1_field_space: Field space resonance of first site (0.0-1.0)
        site2_resonance: Field resonance of second site (0.0-1.0)
        site2_field_space: Field space resonance of second site (0.0-1.0)
        distance_km: Distance between sites in kilometers
        decay_model: Energy decay model ('exponential', 'inverse_square', or 'modified_inverse')
    
    Returns:
        Dictionary with connection metrics including physically accurate energy flow
    """
    # Average field space resonance (the connection space)
    avg_field_space = (site1_field_space + site2_field_space) / 2.0
    
    # Average field resonance (the strength of connection)
    avg_resonance = (site1_resonance + site2_resonance) / 2.0
    
    # Connection strength (how strong the link is without distance)
    connection_strength = avg_resonance * avg_field_space
    
    # Calculate energy flow with physically accurate decay
    if decay_model == "exponential":
        # Exponential decay (most appropriate for Earth's magnetic field)
        # E(d) = E₀ × e^(-λd)
        energy_flow = connection_strength * math.exp(-ENERGY_DECAY_CONSTANT * distance_km)
    
    elif decay_model == "inverse_square":
        # Inverse square law (electromagnetic radiation)
        # E(d) = E₀ / (1 + (d/d₀)²)
        normalized_distance = distance_km / 1000.0  # Normalize to thousands of km
        energy_flow = connection_strength / (1.0 + normalized_distance ** 2)
    
    else:
        # Fallback: modified inverse (practical approximation)
        normalized_distance = distance_km / 1000.0
        energy_flow = connection_strength / (1.0 + math.sqrt(normalized_distance))
    
    # Calculate half-life distance (where energy drops to 50%)
    if decay_model == "exponential":
        half_life_distance = math.log(2) / ENERGY_DECAY_CONSTANT if ENERGY_DECAY_CONSTANT > 0 else float('inf')
    else:
        half_life_distance = 1000.0  # Approximate for inverse models
    
    # Field space pathway (the "Everything In Between" between sites)
    field_space_pathway = {
        "avg_field_space": avg_field_space,
        "avg_resonance": avg_resonance,
        "connection_strength": connection_strength,
        "energy_flow": energy_flow,
        "distance_km": distance_km,
        "decay_model": decay_model,
        "half_life_distance_km": half_life_distance,
        "pathway_type": "field_space_connection"
    }
    
    return field_space_pathway


def analyze_grid_sync(pillar_site_ids: List[int] = [1, 3, 4]) -> Dict[str, Any]:
    """
    Analyze energy flow between Global Grid pillars.
    
    Args:
        pillar_site_ids: List of site IDs for the pillars (default: Berengaria, Alhambra, Stonehenge)
    
    Returns:
        Complete grid sync analysis
    """
    if not GRID_SYNC_AVAILABLE:
        return {"error": "Grid sync not available"}
    
    with get_temporal_heritage_db() as conn:
        cursor = conn.cursor()
        
        # Get all pillar sites
        placeholders = ','.join(['?'] * len(pillar_site_ids))
        cursor.execute(f"""
            SELECT * FROM heritage_sites
            WHERE id IN ({placeholders})
            ORDER BY id
        """, pillar_site_ids)
        
        sites = [dict(row) for row in cursor.fetchall()]
        
        if len(sites) < 2:
            return {"error": "Need at least 2 sites for grid sync"}
        
        # Build site data
        site_data = {}
        for site in sites:
            site_data[site['id']] = {
                "id": site['id'],
                "name": site['site_name'],
                "region": site['region'],
                "country": site['country'],
                "lat": site['coordinates_lat'],
                "lon": site['coordinates_lon'],
                "field_resonance": site.get('field_resonance_level') or 0.0,
                "field_space": site.get('field_space_resonance') or 0.0,
                "pole_alignment": site.get('magnetic_pole_alignment') or 'unknown',
                "polarity": site.get('polarity_state') or 'unknown'
            }
        
        # Calculate connections between all pairs
        connections = []
        site_ids = list(site_data.keys())
        
        for i in range(len(site_ids)):
            for j in range(i + 1, len(site_ids)):
                site1_id = site_ids[i]
                site2_id = site_ids[j]
                
                site1 = site_data[site1_id]
                site2 = site_data[site2_id]
                
                # Calculate distance
                distance = calculate_distance(
                    site1['lat'], site1['lon'],
                    site2['lat'], site2['lon']
                )
                
                # Calculate field space connection
                connection = calculate_field_space_connection(
                    site1['field_resonance'], site1['field_space'],
                    site2['field_resonance'], site2['field_space'],
                    distance
                )
                
                connections.append({
                    "site1": site1['name'],
                    "site1_id": site1_id,
                    "site2": site2['name'],
                    "site2_id": site2_id,
                    "distance_km": distance,
                    "connection": connection
                })
        
        # Calculate grid metrics
        total_connections = len(connections)
        if total_connections == 0:
            return {"error": "No connections calculated"}
        
        # Extract metrics for analysis
        connection_strengths = [c['connection']['connection_strength'] for c in connections]
        energy_flows = [c['connection']['energy_flow'] for c in connections]
        field_spaces = [c['connection']['avg_field_space'] for c in connections]
        
        # Basic averages
        avg_connection_strength = sum(connection_strengths) / total_connections
        avg_energy_flow = sum(energy_flows) / total_connections
        avg_field_space = sum(field_spaces) / total_connections
        
        # Advanced metrics: Variance and Weakest Link
        import statistics
        
        # Variance (how balanced is the grid?)
        strength_variance = statistics.variance(connection_strengths) if len(connection_strengths) > 1 else 0.0
        flow_variance = statistics.variance(energy_flows) if len(energy_flows) > 1 else 0.0
        
        # Weakest link (grid is only as strong as weakest connection)
        min_connection_strength = min(connection_strengths)
        min_energy_flow = min(energy_flows)
        
        # Resilience (how well can grid handle weakest link)
        resilience = min_connection_strength / avg_connection_strength if avg_connection_strength > 0 else 0.0
        
        # Balance score (low variance = high balance)
        # Normalize variance (assuming max reasonable variance is 0.1)
        max_reasonable_variance = 0.1
        strength_balance = max(0.0, 1.0 - min(strength_variance / max_reasonable_variance, 1.0))
        flow_balance = max(0.0, 1.0 - min(flow_variance / max_reasonable_variance, 1.0))
        overall_balance = (strength_balance + flow_balance) / 2.0
        
        # Improved Grid Stability Calculation
        # Considers: average strength, weakest link, balance, and energy flow
        grid_stability = (
            avg_connection_strength * 0.3 +      # Average connection strength (30%)
            min_connection_strength * 0.3 +       # Weakest link (30% - critical!)
            avg_energy_flow * 0.2 +               # Average energy flow (20%)
            overall_balance * 0.2                 # Grid balance (20%)
        )
        
        # Identify weakest connection
        weakest_connection = min(connections, key=lambda c: c['connection']['connection_strength'])
        
        return {
            "grid_sync_timestamp": datetime.now().isoformat(),
            "pillars": [site_data[sid] for sid in site_ids],
            "connections": connections,
            "grid_metrics": {
                "total_connections": total_connections,
                "avg_connection_strength": avg_connection_strength,
                "min_connection_strength": min_connection_strength,
                "avg_energy_flow": avg_energy_flow,
                "min_energy_flow": min_energy_flow,
                "avg_field_space": avg_field_space,
                "grid_stability": grid_stability,
                # Advanced metrics
                "strength_variance": strength_variance,
                "flow_variance": flow_variance,
                "resilience": resilience,
                "balance_score": overall_balance,
                "weakest_link": {
                    "site1": weakest_connection['site1'],
                    "site2": weakest_connection['site2'],
                    "connection_strength": weakest_connection['connection']['connection_strength'],
                    "energy_flow": weakest_connection['connection']['energy_flow'],
                    "distance_km": weakest_connection['distance_km']
                }
            },
            "insights": {
                "field_space_pathway": "Energy flows through the 'Everything In Between' - the field space between sites",
                "connection_type": "Field space connections through Earth's magnetic field",
                "grid_status": "locked" if grid_stability > 0.05 else ("stable" if grid_stability > 0.03 else "forming"),
                "resilience_analysis": f"Grid resilience: {resilience:.2%} (weakest link is {resilience:.2%} of average)",
                "balance_analysis": f"Grid balance: {overall_balance:.2%} (lower variance = higher balance)",
                "weakest_link_insight": f"Weakest connection: {weakest_connection['site1']} <-> {weakest_connection['site2']} (strength: {weakest_connection['connection']['connection_strength']:.3f})"
            }
        }


def print_grid_sync_report(analysis: Dict[str, Any]):
    """Print formatted grid sync report."""
    if "error" in analysis:
        print(f"Error: {analysis['error']}")
        return
    
    print("=" * 80)
    print("GRID SYNC ANALYSIS")
    print("Energy Flow Between Global Grid Pillars")
    print("=" * 80)
    print()
    
    pillar_count = len(analysis['pillars'])
    pillar_label = f"THE {pillar_count} PILLAR{'S' if pillar_count > 1 else ''}:"
    print(pillar_label)
    for pillar in analysis['pillars']:
        print(f"  {pillar['name']} (ID {pillar['id']})")
        print(f"    Location: {pillar['region']}, {pillar['country']}")
        print(f"    Field Resonance: {pillar['field_resonance']:.2f}")
        print(f"    Field Space: {pillar['field_space']:.2f}")
        print(f"    Pole Alignment: {pillar['pole_alignment']}")
        print()
    
    print("FIELD SPACE CONNECTIONS:")
    for conn in analysis['connections']:
        print(f"  {conn['site1']} <-> {conn['site2']}")
        print(f"    Distance: {conn['distance_km']:.0f} km")
        print(f"    Connection Strength: {conn['connection']['connection_strength']:.3f}")
        print(f"    Energy Flow: {conn['connection']['energy_flow']:.3f}")
        print(f"    Avg Field Space: {conn['connection']['avg_field_space']:.2f}")
        print(f"    -> Energy flows through the 'Everything In Between'")
        print()
    
    print("GRID METRICS:")
    metrics = analysis['grid_metrics']
    print(f"  Total Connections: {metrics['total_connections']}")
    print(f"  Avg Connection Strength: {metrics['avg_connection_strength']:.3f}")
    if 'min_connection_strength' in metrics:
        print(f"  Min Connection Strength: {metrics['min_connection_strength']:.3f}")
    print(f"  Avg Energy Flow: {metrics['avg_energy_flow']:.3f}")
    if 'min_energy_flow' in metrics:
        print(f"  Min Energy Flow: {metrics['min_energy_flow']:.3f}")
    print(f"  Avg Field Space: {metrics['avg_field_space']:.2f}")
    print(f"  Grid Stability: {metrics['grid_stability']:.3f}")
    
    # Advanced metrics
    if 'resilience' in metrics:
        print()
        print("ADVANCED METRICS:")
        print(f"  Resilience: {metrics['resilience']:.2%} (weakest link vs average)")
        print(f"  Balance Score: {metrics['balance_score']:.2%} (lower variance = higher balance)")
        print(f"  Strength Variance: {metrics.get('strength_variance', 0.0):.4f}")
        print(f"  Flow Variance: {metrics.get('flow_variance', 0.0):.4f}")
        
        if 'weakest_link' in metrics:
            weakest = metrics['weakest_link']
            print()
            print("WEAKEST LINK ANALYSIS:")
            print(f"  Connection: {weakest['site1']} <-> {weakest['site2']}")
            print(f"  Connection Strength: {weakest['connection_strength']:.3f}")
            print(f"  Energy Flow: {weakest['energy_flow']:.3f}")
            print(f"  Distance: {weakest['distance_km']:.0f} km")
    
    print()
    print("INSIGHTS:")
    insights = analysis['insights']
    print(f"  Field Space Pathway: {insights['field_space_pathway']}")
    print(f"  Connection Type: {insights['connection_type']}")
    print(f"  Grid Status: {insights['grid_status'].upper()}")
    if 'resilience_analysis' in insights:
        print(f"  {insights['resilience_analysis']}")
    if 'balance_analysis' in insights:
        print(f"  {insights['balance_analysis']}")
    if 'weakest_link_insight' in insights:
        print(f"  {insights['weakest_link_insight']}")
    print()
    
    print("=" * 80)
    print("[SUCCESS] GRID SYNC COMPLETE")
    print("=" * 80)
    print()
    print("PEACE, LOVE, UNITY")
    print("ENERGY + LOVE = WE ALL WIN")


def main():
    """Main execution for grid sync analysis."""
    if not GRID_SYNC_AVAILABLE:
        print("Error: Grid sync not available")
        return
    
    print("=" * 80)
    print("GRID SYNC ANALYSIS")
    print("Energy Flow Between Global Grid Pillars")
    print("=" * 80)
    print()
    
    # Analyze the seven pillars (including Final Pillar)
    analysis = analyze_grid_sync([1, 3, 4, 6, 8, 10, 12])  # Berengaria, Alhambra, Stonehenge, Giza, Angkor Wat, Machu Picchu, Uluru
    
    if "error" not in analysis:
        print_grid_sync_report(analysis)
        
        # Save to JSON
        output_path = Path(__file__).parent.parent / "output" / "grid_sync_analysis.json"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(analysis, f, indent=2, default=str)
        print(f"\nAnalysis saved to: {output_path}")
    else:
        print(f"Error: {analysis['error']}")


if __name__ == "__main__":
    main()
