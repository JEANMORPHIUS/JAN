"""
VIBRATIONAL IMPACT ANALYSIS
Calculate Impact Radius from N22 6RX - Maximum Reach

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
Calculate the vibrational impact radius from N22 6RX.
Map coverage area and maximum reach.
Identify all that can be done from this location.
"""

import sys
import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from datetime import datetime
from dataclasses import dataclass, field
from math import radians, sin, cos, sqrt, atan2, pi
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


@dataclass
class ImpactZone:
    """Vibrational impact zone."""
    radius_km: float
    radius_miles: float
    coverage_area_km2: float
    coverage_area_miles2: float
    description: str
    impact_level: str  # core, strong, moderate, extended
    reachable_locations: List[str] = field(default_factory=list)


@dataclass
class LocationCoverage:
    """Location coverage analysis."""
    name: str
    latitude: float
    longitude: float
    distance_from_origin_km: float
    within_core: bool
    within_strong: bool
    within_moderate: bool
    within_extended: bool
    impact_received: str


class VibrationalImpactAnalysis:
    """
    Vibrational Impact Analysis System
    Calculate impact radius and coverage from N22 6RX.
    """
    
    def __init__(self, siyem_path: Path, jan_path: Path, output_dir: Path):
        self.siyem_path = siyem_path
        self.jan_path = jan_path
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Origin: N22 6RX
        self.origin_lat = 51.597178
        self.origin_lon = -0.094006
        self.origin_name = "187 Westbury Avenue, N22 6RX"
        
        # Impact zones (radius in km)
        self.impact_zones = []
        self.coverage_locations = []
    
    def calculate_distance(self, lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """Calculate distance between two GPS coordinates (Haversine formula)."""
        # Convert to radians
        lat1_rad = radians(lat1)
        lon1_rad = radians(lon1)
        lat2_rad = radians(lat2)
        lon2_rad = radians(lon2)
        
        # Haversine formula
        dlat = lat2_rad - lat1_rad
        dlon = lon2_rad - lon1_rad
        
        a = sin(dlat / 2) ** 2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        
        # Earth radius in kilometers
        R = 6371.0
        distance_km = R * c
        return distance_km
    
    def calculate_area(self, radius_km: float) -> float:
        """Calculate coverage area in square kilometers."""
        return pi * (radius_km ** 2)
    
    def define_impact_zones(self):
        """Define vibrational impact zones."""
        logger.info("=" * 80)
        logger.info("DEFINING VIBRATIONAL IMPACT ZONES")
        logger.info("=" * 80)
        
        # Core Zone: Immediate impact (1 km radius)
        core = ImpactZone(
            radius_km=1.0,
            radius_miles=0.62,
            coverage_area_km2=self.calculate_area(1.0),
            coverage_area_miles2=self.calculate_area(1.0) * 0.386102,
            description="Core vibrational impact - Immediate area",
            impact_level="core",
            reachable_locations=["Wood Green", "Tottenham", "New River"]
        )
        self.impact_zones.append(core)
        
        # Strong Zone: Strong impact (5 km radius)
        strong = ImpactZone(
            radius_km=5.0,
            radius_miles=3.11,
            coverage_area_km2=self.calculate_area(5.0),
            coverage_area_miles2=self.calculate_area(5.0) * 0.386102,
            description="Strong vibrational impact - North London",
            impact_level="strong",
            reachable_locations=[
                "Wood Green", "Tottenham", "Haringey", "Enfield",
                "Lee Navigation", "New River", "Alexandra Palace",
                "Finsbury Park", "Highgate", "Muswell Hill"
            ]
        )
        self.impact_zones.append(strong)
        
        # Moderate Zone: Moderate impact (25 km radius)
        moderate = ImpactZone(
            radius_km=25.0,
            radius_miles=15.53,
            coverage_area_km2=self.calculate_area(25.0),
            coverage_area_miles2=self.calculate_area(25.0) * 0.386102,
            description="Moderate vibrational impact - Greater London",
            impact_level="moderate",
            reachable_locations=[
                "Central London", "River Thames", "Westminster",
                "City of London", "Camden", "Islington", "Hackney",
                "Waltham Forest", "Redbridge", "Barking", "Dagenham",
                "Greenwich", "Lewisham", "Southwark", "Lambeth",
                "Wandsworth", "Richmond", "Kingston", "Hounslow",
                "Ealing", "Brent", "Harrow", "Barnet", "Hertfordshire"
            ]
        )
        self.impact_zones.append(moderate)
        
        # Extended Zone: Extended impact (100 km radius)
        extended = ImpactZone(
            radius_km=100.0,
            radius_miles=62.14,
            coverage_area_km2=self.calculate_area(100.0),
            coverage_area_miles2=self.calculate_area(100.0) * 0.386102,
            description="Extended vibrational impact - South East England",
            impact_level="extended",
            reachable_locations=[
                "Greater London", "Essex", "Kent", "Surrey",
                "Hertfordshire", "Buckinghamshire", "Berkshire",
                "Brighton", "Canterbury", "Dover", "Reading",
                "Oxford", "Cambridge", "Luton", "Milton Keynes",
                "North Sea", "English Channel", "Thames Estuary"
            ]
        )
        self.impact_zones.append(extended)
        
        # Maximum Zone: Maximum reach (500 km radius)
        maximum = ImpactZone(
            radius_km=500.0,
            radius_miles=310.69,
            coverage_area_km2=self.calculate_area(500.0),
            coverage_area_miles2=self.calculate_area(500.0) * 0.386102,
            description="Maximum vibrational reach - UK and beyond",
            impact_level="maximum",
            reachable_locations=[
                "Entire UK", "Wales", "Scotland", "Northern Ireland",
                "Ireland", "France", "Belgium", "Netherlands",
                "North Sea", "English Channel", "Celtic Sea",
                "Atlantic Ocean", "Whale migration routes"
            ]
        )
        self.impact_zones.append(maximum)
        
        logger.info(f"Defined {len(self.impact_zones)} impact zones")
        for zone in self.impact_zones:
            logger.info(f"  {zone.impact_level.upper()}: {zone.radius_km} km radius, {zone.coverage_area_km2:.2f} km²")
        logger.info("=" * 80)
    
    def analyze_key_locations(self):
        """Analyze key locations within impact zones."""
        logger.info("=" * 80)
        logger.info("ANALYZING KEY LOCATIONS WITHIN IMPACT ZONES")
        logger.info("=" * 80)
        
        # Key locations to analyze
        key_locations = {
            "New River - Myddleton Road": (51.6000, -0.1100),
            "Lee Navigation - Tottenham": (51.5800, -0.0500),
            "Lee Navigation - Lower Lea Valley": (51.5500, -0.0200),
            "River Thames - Central": (51.5074, -0.1278),
            "Alexandra Palace": (51.5947, -0.1294),
            "Finsbury Park": (51.5642, -0.1065),
            "Highgate": (51.5714, -0.1447),
            "Westminster": (51.4994, -0.1249),
            "City of London": (51.5155, -0.0922),
            "Greenwich": (51.4826, -0.0077),
            "Brighton": (50.8225, -0.1372),
            "Canterbury": (51.2802, 1.0789),
            "Oxford": (51.7520, -1.2577),
            "Cambridge": (52.2053, 0.1218),
            "Dover": (51.1294, 1.3089),
            "North Sea": (52.0, 2.0),  # Approximate
            "English Channel": (50.5, -0.5),  # Approximate
        }
        
        for loc_name, (lat, lon) in key_locations.items():
            distance_km = self.calculate_distance(
                self.origin_lat, self.origin_lon,
                lat, lon
            )
            
            # Determine which zones it's within
            within_core = distance_km <= 1.0
            within_strong = distance_km <= 5.0
            within_moderate = distance_km <= 25.0
            within_extended = distance_km <= 100.0
            within_maximum = distance_km <= 500.0
            
            # Determine impact level
            if within_core:
                impact_received = "core"
            elif within_strong:
                impact_received = "strong"
            elif within_moderate:
                impact_received = "moderate"
            elif within_extended:
                impact_received = "extended"
            elif within_maximum:
                impact_received = "maximum"
            else:
                impact_received = "beyond"
            
            coverage = LocationCoverage(
                name=loc_name,
                latitude=lat,
                longitude=lon,
                distance_from_origin_km=distance_km,
                within_core=within_core,
                within_strong=within_strong,
                within_moderate=within_moderate,
                within_extended=within_extended,
                impact_received=impact_received
            )
            
            self.coverage_locations.append(coverage)
            
            logger.info(f"{loc_name}: {distance_km:.2f} km - {impact_received.upper()} impact")
        
        logger.info(f"Analyzed {len(self.coverage_locations)} key locations")
        logger.info("=" * 80)
    
    def create_impact_analysis_report(self) -> Dict:
        """Create comprehensive impact analysis report."""
        logger.info("=" * 80)
        logger.info("CREATING VIBRATIONAL IMPACT ANALYSIS REPORT")
        logger.info("=" * 80)
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "title": "Vibrational Impact Analysis - From N22 6RX",
            "status": "100% COMPLETE",
            "origin": {
                "name": self.origin_name,
                "postcode": "N22 6RX",
                "coordinates": {
                    "latitude": self.origin_lat,
                    "longitude": self.origin_lon
                },
                "location": "Wood Green/Tottenham, North London, Haringey Borough"
            },
            "impact_zones": [],
            "key_locations": [],
            "summary": {
                "total_coverage_area_km2": 0.0,
                "total_coverage_area_miles2": 0.0,
                "maximum_reach_km": 500.0,
                "maximum_reach_miles": 310.69,
                "locations_analyzed": len(self.coverage_locations),
                "whale_migration_routes": "Within maximum reach (500 km)"
            }
        }
        
        # Add impact zones
        for zone in self.impact_zones:
            report["impact_zones"].append({
                "level": zone.impact_level,
                "radius_km": zone.radius_km,
                "radius_miles": zone.radius_miles,
                "coverage_area_km2": round(zone.coverage_area_km2, 2),
                "coverage_area_miles2": round(zone.coverage_area_miles2, 2),
                "description": zone.description,
                "reachable_locations": zone.reachable_locations
            })
        
        # Add key locations
        for loc in sorted(self.coverage_locations, key=lambda x: x.distance_from_origin_km):
            report["key_locations"].append({
                "name": loc.name,
                "coordinates": {
                    "latitude": loc.latitude,
                    "longitude": loc.longitude
                },
                "distance_km": round(loc.distance_from_origin_km, 2),
                "impact_received": loc.impact_received,
                "zones": {
                    "core": loc.within_core,
                    "strong": loc.within_strong,
                    "moderate": loc.within_moderate,
                    "extended": loc.within_extended
                }
            })
        
        # Calculate total coverage (maximum zone)
        report["summary"]["total_coverage_area_km2"] = round(
            self.impact_zones[-1].coverage_area_km2, 2
        )
        report["summary"]["total_coverage_area_miles2"] = round(
            self.impact_zones[-1].coverage_area_miles2, 2
        )
        
        # Save report
        report_path = self.output_dir / "vibrational_impact_analysis_report.json"
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, default=str, ensure_ascii=False)
        
        logger.info(f"Impact analysis report exported to: {report_path}")
        logger.info("=" * 80)
        return report


def main():
    """Main execution."""
    siyem_path = Path("s:\\SIYEM")
    jan_path = Path("s:\\JAN")
    output_dir = jan_path / "SIYEM" / "output" / "vibrational_impact"
    
    analysis = VibrationalImpactAnalysis(siyem_path, jan_path, output_dir)
    
    # Define impact zones
    analysis.define_impact_zones()
    
    # Analyze key locations
    analysis.analyze_key_locations()
    
    # Create report
    analysis.create_impact_analysis_report()
    
    logger.info("\n" + "=" * 80)
    logger.info("VIBRATIONAL IMPACT ANALYSIS - COMPLETE")
    logger.info("=" * 80)
    logger.info(f"Origin: {analysis.origin_name}")
    logger.info(f"Impact zones: {len(analysis.impact_zones)}")
    logger.info(f"Locations analyzed: {len(analysis.coverage_locations)}")
    logger.info(f"Maximum reach: 500 km (310.69 miles)")
    logger.info(f"Total coverage: {analysis.impact_zones[-1].coverage_area_km2:.2f} km²")
    logger.info("Status: 100% COMPLETE")
    logger.info("=" * 80)


if __name__ == "__main__":
    main()
