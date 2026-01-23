"""
HERITAGE MERIDIAN SCAN
Mapping the Original Unity and Tracing the Man-Made Rifts

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

This script performs the Heritage Meridian Scan to:
1. Map the Original Unity (how cultures were connected before borders)
2. Identify the Man-Made Rifts (how modern systems broke connections)
3. Trace the Seven Pillars and ancient meridians
4. Map the Pangea Memory connection
5. Analyze Greenwich Time vs Ancient Meridians
6. Prepare the 13 Seats for activation
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
from dataclasses import dataclass, asdict

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent))

import logging
logger = logging.getLogger(__name__)


@dataclass
class MeridianConnection:
    """Represents a connection between two heritage sites along an ancient meridian."""
    site_a: str
    site_b: str
    distance_km: float
    bearing_degrees: float
    meridian_type: str  # "primary", "equatorial", "bridge", etc.
    original_function: str
    modern_distortion: str
    resonance_strength: float


@dataclass
class RiftAnalysis:
    """Analysis of a man-made rift that broke the Original Unity."""
    rift_id: str
    rift_name: str
    original_link: str
    man_made_rift: str
    consequence: str
    healing: str
    affected_sites: List[str]
    severity: float  # 0.0 to 1.0


class HeritageMeridianScan:
    """
    The Heritage Meridian Scan system.
    
    Bypasses all modern geopolitical overlays to reveal the Original Unity
    that existed before the rifts were weaponized.
    """
    
    def __init__(self, data_path: Optional[Path] = None):
        """Initialize the Heritage Meridian Scan system."""
        if data_path is None:
            data_path = Path(__file__).parent.parent / "data" / "heritage_meridian" / "heritage_meridian_data.json"
        
        self.data_path = data_path
        self.data = self._load_data()
        
        # Extract components
        self.seven_pillars = self.data.get("the_seven_pillars", {}).get("pillars", [])
        self.ancient_meridians = self.data.get("ancient_meridian_system", {}).get("primary_meridians", [])
        self.rifts = self.data.get("the_rifts", {}).get("rifts", [])
        self.thirteen_seats = self.data.get("the_13_seats", {}).get("seats", [])
        self.pangea_memory = self.data.get("pangea_memory", {})
        self.peak_0_40 = self.data.get("the_0_40_peak", {})
    
    def _load_data(self) -> Dict[str, Any]:
        """Load the Heritage Meridian data."""
        try:
            with open(self.data_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"Heritage Meridian data not found at {self.data_path}")
            return {}
        except json.JSONDecodeError as e:
            logger.error(f"Error parsing Heritage Meridian data: {e}")
            return {}
    
    def haversine_distance(self, lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """
        Calculate the great circle distance between two points on Earth.
        Returns distance in kilometers.
        """
        R = 6371  # Earth's radius in kilometers
        
        # Convert to radians
        lat1_rad = math.radians(lat1)
        lon1_rad = math.radians(lon1)
        lat2_rad = math.radians(lat2)
        lon2_rad = math.radians(lon2)
        
        # Haversine formula
        dlat = lat2_rad - lat1_rad
        dlon = lon2_rad - lon1_rad
        
        a = math.sin(dlat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon/2)**2
        c = 2 * math.asin(math.sqrt(a))
        
        return R * c
    
    def calculate_bearing(self, lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """
        Calculate the bearing (direction) from point 1 to point 2.
        Returns bearing in degrees (0-360).
        """
        lat1_rad = math.radians(lat1)
        lon1_rad = math.radians(lon1)
        lat2_rad = math.radians(lat2)
        lon2_rad = math.radians(lon2)
        
        dlon = lon2_rad - lon1_rad
        
        y = math.sin(dlon) * math.cos(lat2_rad)
        x = math.cos(lat1_rad) * math.sin(lat2_rad) - math.sin(lat1_rad) * math.cos(lat2_rad) * math.cos(dlon)
        
        bearing = math.atan2(y, x)
        bearing_degrees = math.degrees(bearing)
        
        # Normalize to 0-360
        return (bearing_degrees + 360) % 360
    
    def map_meridian_connections(self) -> List[MeridianConnection]:
        """
        Map all meridian connections between the Seven Pillars.
        Returns a list of MeridianConnection objects.
        """
        connections = []
        
        # Create a site lookup
        site_lookup = {pillar["pillar_id"]: pillar for pillar in self.seven_pillars}
        
        # Map connections based on meridian_connections in each pillar
        for pillar in self.seven_pillars:
            pillar_id = pillar["pillar_id"]
            coords_a = pillar["coordinates"]
            
            # Get meridian connections for this pillar
            meridian_connections = pillar.get("meridian_connections", [])
            
            for connected_site_name in meridian_connections:
                # Find the connected pillar
                connected_pillar = None
                for p in self.seven_pillars:
                    if p["name"].lower().replace(" ", "_") == connected_site_name.lower() or \
                       p["pillar_id"] == connected_site_name:
                        connected_pillar = p
                        break
                
                if connected_pillar:
                    coords_b = connected_pillar["coordinates"]
                    
                    # Calculate distance and bearing
                    distance = self.haversine_distance(
                        coords_a["lat"], coords_a["lon"],
                        coords_b["lat"], coords_b["lon"]
                    )
                    
                    bearing = self.calculate_bearing(
                        coords_a["lat"], coords_a["lon"],
                        coords_b["lat"], coords_b["lon"]
                    )
                    
                    # Determine meridian type
                    meridian_type = self._determine_meridian_type(pillar, connected_pillar)
                    
                    # Create connection
                    connection = MeridianConnection(
                        site_a=pillar["name"],
                        site_b=connected_pillar["name"],
                        distance_km=distance,
                        bearing_degrees=bearing,
                        meridian_type=meridian_type,
                        original_function=f"Ancient meridian connecting {pillar['name']} to {connected_pillar['name']}",
                        modern_distortion="Disconnected by borders, time zones, and institutional control",
                        resonance_strength=(pillar.get("field_resonance", 0.5) + connected_pillar.get("field_resonance", 0.5)) / 2
                    )
                    
                    connections.append(connection)
        
        # Remove duplicates (A->B and B->A)
        unique_connections = []
        seen_pairs = set()
        for conn in connections:
            pair = tuple(sorted([conn.site_a, conn.site_b]))
            if pair not in seen_pairs:
                seen_pairs.add(pair)
                unique_connections.append(conn)
        
        return unique_connections
    
    def _determine_meridian_type(self, pillar_a: Dict, pillar_b: Dict) -> str:
        """Determine the type of meridian connection between two pillars."""
        names = {pillar_a["name"].lower(), pillar_b["name"].lower()}
        
        # Primary circuit
        if {"great pyramid of giza", "stonehenge", "angkor wat"}.issubset(names) or \
           {"giza", "stonehenge", "angkor"}.issubset(names):
            return "primary_circuit"
        
        # Equatorial line
        if any("equator" in p.get("ancient_name", "").lower() for p in [pillar_a, pillar_b]):
            return "equatorial"
        
        # Mediterranean bridge
        if any("mediterranean" in p.get("ancient_name", "").lower() for p in [pillar_a, pillar_b]):
            return "mediterranean_bridge"
        
        # Default
        return "ancient_meridian"
    
    def analyze_rifts(self) -> List[RiftAnalysis]:
        """
        Analyze the man-made rifts that broke the Original Unity.
        Returns a list of RiftAnalysis objects.
        """
        rift_analyses = []
        
        for rift_data in self.rifts:
            # Determine affected sites
            affected_sites = self._find_affected_sites(rift_data)
            
            # Calculate severity (based on number of affected sites and type)
            severity = self._calculate_rift_severity(rift_data, affected_sites)
            
            rift_analysis = RiftAnalysis(
                rift_id=rift_data.get("rift_id", ""),
                rift_name=rift_data.get("name", ""),
                original_link=rift_data.get("original_link", ""),
                man_made_rift=rift_data.get("man_made_rift", ""),
                consequence=rift_data.get("consequence", ""),
                healing=rift_data.get("healing", ""),
                affected_sites=affected_sites,
                severity=severity
            )
            
            rift_analyses.append(rift_analysis)
        
        return rift_analyses
    
    def _find_affected_sites(self, rift_data: Dict) -> List[str]:
        """Find heritage sites affected by a specific rift."""
        affected = []
        rift_name = rift_data.get("name", "").lower()
        
        # Map rifts to affected sites
        if "tectonic" in rift_name or "border" in rift_name:
            # All sites are affected by border logic
            affected = [p["name"] for p in self.seven_pillars]
        elif "time" in rift_name or "meridian" in rift_name:
            # Sites that were part of the ancient meridian system
            affected = [p["name"] for p in self.seven_pillars if "meridian" in p.get("original_function", "").lower()]
        elif "institutional" in rift_name:
            # All Seven Pillars are affected
            affected = [p["name"] for p in self.seven_pillars]
        elif "language" in rift_name or "tribalism" in rift_name:
            # All sites are affected
            affected = [p["name"] for p in self.seven_pillars]
        elif "heritage" in rift_name or "erasure" in rift_name:
            # All sites are affected
            affected = [p["name"] for p in self.seven_pillars]
        
        return affected
    
    def _calculate_rift_severity(self, rift_data: Dict, affected_sites: List[str]) -> float:
        """Calculate the severity of a rift (0.0 to 1.0)."""
        # Base severity on number of affected sites
        base_severity = min(len(affected_sites) / len(self.seven_pillars), 1.0)
        
        # Adjust based on rift type
        rift_name = rift_data.get("name", "").lower()
        if "heritage" in rift_name or "erasure" in rift_name:
            base_severity = 1.0  # Heritage erasure affects everything
        elif "institutional" in rift_name:
            base_severity = 0.9  # Institutional control is severe
        elif "time" in rift_name:
            base_severity = 0.8  # Time meridian affects all sites
        
        return base_severity
    
    def calculate_global_resonance_network(self) -> Dict[str, Any]:
        """
        Calculate the global resonance network connecting all Seven Pillars.
        Returns analysis of the network's current state vs Original Unity.
        """
        connections = self.map_meridian_connections()
        
        # Calculate total network distance
        total_distance = sum(conn.distance_km for conn in connections)
        
        # Calculate average resonance
        avg_resonance = sum(conn.resonance_strength for conn in connections) / len(connections) if connections else 0.0
        
        # Identify strongest connections
        strongest_connections = sorted(connections, key=lambda x: x.resonance_strength, reverse=True)[:3]
        
        # Identify weakest connections (most disrupted)
        weakest_connections = sorted(connections, key=lambda x: x.resonance_strength)[:3]
        
        return {
            "total_connections": len(connections),
            "total_network_distance_km": total_distance,
            "average_resonance": avg_resonance,
            "network_health": "fragmented" if avg_resonance < 0.7 else "stable" if avg_resonance < 0.9 else "strong",
            "strongest_connections": [
                {
                    "from": conn.site_a,
                    "to": conn.site_b,
                    "resonance": conn.resonance_strength,
                    "distance_km": conn.distance_km
                }
                for conn in strongest_connections
            ],
            "weakest_connections": [
                {
                    "from": conn.site_a,
                    "to": conn.site_b,
                    "resonance": conn.resonance_strength,
                    "distance_km": conn.distance_km,
                    "issue": "Disrupted by modern rifts"
                }
                for conn in weakest_connections
            ],
            "original_unity_state": "All sites were connected in a unified network",
            "current_state": f"Network is {avg_resonance:.1%} of original unity",
            "healing_required": "Reconnect the meridian network through the 13 Seats"
        }
    
    def prepare_13_seats_activation(self) -> Dict[str, Any]:
        """
        Prepare the activation protocol for the 13 Seats.
        Returns the activation sequence and resonance map.
        """
        # Sort seats by resonance (if available) or by strategic importance
        activation_sequence = []
        
        for seat in self.thirteen_seats:
            # Find corresponding pillar if exists
            pillar_resonance = 0.0
            for pillar in self.seven_pillars:
                if abs(pillar["coordinates"]["lat"] - seat["coordinates"]["lat"]) < 0.1 and \
                   abs(pillar["coordinates"]["lon"] - seat["coordinates"]["lon"]) < 0.1:
                    pillar_resonance = pillar.get("field_resonance", 0.0)
                    break
            
            activation_sequence.append({
                "seat_id": seat["seat_id"],
                "name": seat["name"],
                "coordinates": seat["coordinates"],
                "function": seat["function"],
                "resonance": pillar_resonance,
                "activation_order": len(activation_sequence) + 1
            })
        
        # Calculate network coverage
        total_seats = len(activation_sequence)
        central_seat = next((s for s in activation_sequence if "central" in s["name"].lower()), None)
        
        return {
            "total_seats": total_seats,
            "central_anchor": central_seat,
            "activation_sequence": activation_sequence,
            "activation_protocol": "Sequential activation starting with the Central Anchor, then radiating outward to the 12 primary seats",
            "expected_result": "Unified field reconnecting the Family to their True Heritage",
            "resonance_peak": self.peak_0_40.get("frequency", 0.40),
            "healing_frequency": "The 0.40 Peak will anchor into each rift to fuse the memory back into unity"
        }
    
    def generate_scan_report(self, output_path: Optional[Path] = None) -> Path:
        """
        Generate a complete Heritage Meridian Scan report.
        Returns the path to the generated report.
        """
        if output_path is None:
            output_path = Path(__file__).parent.parent / "output" / "heritage_meridian" / f"meridian_scan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Perform all analyses
        meridian_connections = self.map_meridian_connections()
        rift_analyses = self.analyze_rifts()
        resonance_network = self.calculate_global_resonance_network()
        seats_activation = self.prepare_13_seats_activation()
        
        # Compile report
        report = {
            "scan_timestamp": datetime.now().isoformat(),
            "mission": "Heritage Meridian Scan: Mapping the Original Unity and Tracing the Man-Made Rifts",
            "the_truth": {
                "pangea_memory": self.pangea_memory.get("truth", ""),
                "original_unity": "All cultures were once connected through the Ancient Meridian System",
                "the_rift": "Man-made systems (borders, time zones, institutions) broke the connection",
                "the_healing": "The 13 Seats and the 0.40 Peak will reconnect the Family"
            },
            "seven_pillars": self.seven_pillars,
            "meridian_connections": [
                {
                    "from": conn.site_a,
                    "to": conn.site_b,
                    "distance_km": round(conn.distance_km, 2),
                    "bearing_degrees": round(conn.bearing_degrees, 2),
                    "meridian_type": conn.meridian_type,
                    "resonance_strength": round(conn.resonance_strength, 3),
                    "original_function": conn.original_function,
                    "modern_distortion": conn.modern_distortion
                }
                for conn in meridian_connections
            ],
            "the_rifts": [
                {
                    "rift_id": rift.rift_id,
                    "rift_name": rift.rift_name,
                    "original_link": rift.original_link,
                    "man_made_rift": rift.man_made_rift,
                    "consequence": rift.consequence,
                    "healing": rift.healing,
                    "affected_sites": rift.affected_sites,
                    "severity": round(rift.severity, 3)
                }
                for rift in rift_analyses
            ],
            "global_resonance_network": resonance_network,
            "thirteen_seats": {
                "description": "The 13 Seats are the activation points for the Great Relinking",
                "activation_protocol": seats_activation,
                "seats": self.thirteen_seats
            },
            "the_0_40_peak": self.peak_0_40,
            "healing_protocol": {
                "step_1": "Activate the 13 Seats in sequence",
                "step_2": "Anchor the 0.40 Peak into each rift",
                "step_3": "Reconnect the meridian network",
                "step_4": "Restore the Pangea Memory",
                "expected_result": "The Family reconnected to their True Heritage. The Earth brought back to itself."
            }
        }
        
        # Write report
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, default=str)
        
        logger.info(f"Heritage Meridian Scan report generated: {output_path}")
        return output_path
    
    def print_scan_summary(self):
        """Print a summary of the Heritage Meridian Scan."""
        print("=" * 80)
        print("HERITAGE MERIDIAN SCAN")
        print("Mapping the Original Unity and Tracing the Man-Made Rifts")
        print("=" * 80)
        print()
        
        print("THE SEVEN PILLARS:")
        print("-" * 80)
        for i, pillar in enumerate(self.seven_pillars, 1):
            print(f"{i}. {pillar['name']} ({pillar['country']})")
            print(f"   Ancient Name: {pillar.get('ancient_name', 'N/A')}")
            print(f"   Field Resonance: {pillar.get('field_resonance', 0.0):.2f}")
            print(f"   Original Function: {pillar.get('original_function', 'N/A')}")
            print(f"   Modern Distortion: {pillar.get('modern_distortion', 'N/A')}")
            print()
        
        print("=" * 80)
        print("MERIDIAN CONNECTIONS:")
        print("-" * 80)
        connections = self.map_meridian_connections()
        for conn in connections[:5]:  # Show first 5
            print(f"{conn.site_a} <-> {conn.site_b}")
            print(f"   Distance: {conn.distance_km:.0f} km")
            print(f"   Resonance: {conn.resonance_strength:.2f}")
            print(f"   Type: {conn.meridian_type}")
            print()
        
        print("=" * 80)
        print("THE RIFTS:")
        print("-" * 80)
        rifts = self.analyze_rifts()
        for rift in rifts:
            print(f"{rift.rift_name}")
            print(f"   Original Link: {rift.original_link}")
            print(f"   Man-Made Rift: {rift.man_made_rift}")
            print(f"   Severity: {rift.severity:.1%}")
            print(f"   Healing: {rift.healing}")
            print()
        
        print("=" * 80)
        print("GLOBAL RESONANCE NETWORK:")
        print("-" * 80)
        network = self.calculate_global_resonance_network()
        print(f"Total Connections: {network['total_connections']}")
        print(f"Network Distance: {network['total_network_distance_km']:.0f} km")
        print(f"Average Resonance: {network['average_resonance']:.1%}")
        print(f"Network Health: {network['network_health'].upper()}")
        print(f"Current State: {network['current_state']}")
        print()
        
        print("=" * 80)
        print("THE 13 SEATS:")
        print("-" * 80)
        seats = self.prepare_13_seats_activation()
        print(f"Total Seats: {seats['total_seats']}")
        print(f"Central Anchor: {seats['central_anchor']['name'] if seats['central_anchor'] else 'N/A'}")
        print(f"Activation Protocol: {seats['activation_protocol']}")
        print()
        
        print("=" * 80)
        print("THE TRUTH:")
        print("=" * 80)
        print()
        print(self.pangea_memory.get("truth", ""))
        print()
        print("The Family was never truly separated—only the memory was stolen.")
        print("We are relinking the memory.")
        print("We are restoring the unity.")
        print("We are bringing the Earth back to itself.")
        print()
        print("=" * 80)
        print("PEACE. LOVE. UNITY.")
        print("ENERGY + LOVE = WE ALL WIN")
        print("=" * 80)


def main():
    """Main execution for Heritage Meridian Scan."""
    print("=" * 80)
    print("HERITAGE MERIDIAN SCAN")
    print("Operation Pangea Resonance")
    print("=" * 80)
    print()
    
    # Initialize scan
    scan = HeritageMeridianScan()
    
    # Print summary
    scan.print_scan_summary()
    
    # Generate full report
    print()
    print("Generating full scan report...")
    report_path = scan.generate_scan_report()
    print(f"  [OK] Report generated: {report_path}")
    print()
    
    print("=" * 80)
    print("SCAN COMPLETE")
    print("=" * 80)
    print()
    print("The blueprint is ready.")
    print("The Heritage Meridian Scan is complete.")
    print("The 13 Seats are prepared for activation.")
    print()
    print("PEACE. LOVE. UNITY.")
    print("ENERGY + LOVE = WE ALL WIN")
    print("=" * 80)


if __name__ == "__main__":
    main()
