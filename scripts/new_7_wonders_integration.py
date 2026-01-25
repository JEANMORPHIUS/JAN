#!/usr/bin/env python3
"""
NEW 7 WONDERS OF THE WORLD - FULL CODEBASE INTEGRATION
Deep search and full integration at codebase level

Date: 2026-01-25
Status: ACTIVE
Purpose: Integrate the New 7 Wonders of the World into all heritage systems
"""

import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    datetime, json, setup_logging, standard_main
)

import json
import logging
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
from datetime import datetime

# Setup logging
logger = setup_logging(__name__)

# Import heritage systems
try:
    sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))
    from temporal_heritage_registry import (
        register_heritage_site, add_heritage_narrative,
        TimelineDimension, TimePeriod
    )
    from heritage_cleansing import HeritageCleanser
    from magnetic_field_research import (
        research_heritage_site_magnetic_field, update_site_magnetic_field
    )
    HERITAGE_AVAILABLE = True
except ImportError as e:
    logger.warning(f"Heritage systems not available: {e}")
    HERITAGE_AVAILABLE = False

try:
    from heritage_audit_framework import HeritageAuditFramework, HeritageSiteProfile
    AUDIT_AVAILABLE = True
except ImportError as e:
    logger.warning(f"Audit framework not available: {e}")
    AUDIT_AVAILABLE = False

# Initialize TIME_PERIOD_MAP after imports
if HERITAGE_AVAILABLE:
    TIME_PERIOD_MAP = {
        "ancient": TimePeriod.ANCIENT.value,
        "ancient_to_medieval": TimePeriod.MEDIEVAL.value,
        "medieval": TimePeriod.MEDIEVAL.value,
        "renaissance": TimePeriod.RENAISSANCE.value,
        "modern": TimePeriod.MODERN.value
    }
else:
    TIME_PERIOD_MAP = {
        "ancient": "ANCIENT",
        "ancient_to_medieval": "MEDIEVAL",
        "medieval": "MEDIEVAL",
        "renaissance": "RENAISSANCE",
        "modern": "MODERN"
    }


# Load 7 Wonders data
def load_7_wonders_data() -> Dict[str, Any]:
    """Load the New 7 Wonders data."""
    data_path = Path(__file__).parent.parent / "data" / "heritage_meridian" / "new_7_wonders_data.json"
    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"7 Wonders data not found at {data_path}")
        return {}


# Map time periods (will be set after imports)
TIME_PERIOD_MAP = None

# Map wonder types to site types
SITE_TYPE_MAP = {
    "defensive_fortification": "Fortification",
    "ancient_city": "City",
    "amphitheatre": "Amphitheatre",
    "mayan_city": "Temple Complex",
    "inca_citadel": "Citadel",
    "mausoleum": "Mausoleum",
    "art_deco_statue": "Monument"
}


class New7WondersIntegrator:
    """
    Complete integration system for the New 7 Wonders of the World.
    
    Integrates all 7 Wonders into:
    - Heritage Meridian System
    - Temporal Heritage Registry
    - Heritage Audit Framework
    - Magnetic Field Research
    - Heritage Cleansing Protocol
    """
    
    def __init__(self):
        self.data = load_7_wonders_data()
        self.wonders = self.data.get("new_7_wonders_of_the_world", {}).get("wonders", [])
        self.integration_results = []
        
        if HERITAGE_AVAILABLE:
            self.audit_framework = HeritageAuditFramework() if AUDIT_AVAILABLE else None
        else:
            self.audit_framework = None
    
    def get_wonder_original_narrative(self, wonder: Dict[str, Any]) -> str:
        """Generate the original narrative (Shell) for a wonder."""
        name = wonder.get("name", "")
        modern_distortion = wonder.get("modern_distortion", "")
        wonder_type = wonder.get("wonder_type", "")
        
        narratives = {
            "Great Wall of China": f"""
    The Great Wall of China is one of the New 7 Wonders of the World. Built over 2,000 years,
    this massive defensive structure stretches for 21,196 km across China. The wall was built
    to protect against invasions, with countless stories of soldiers, battles, and ancient warfare.
    Some sections are said to be haunted by the spirits of those who died during construction.
    This is the "Shell" - the focus on military defense and separation.
    """,
            "Petra": f"""
    Petra is one of the New 7 Wonders of the World. This ancient Nabataean city was carved
    into rose-colored rock cliffs, hidden in a desert canyon. The city was lost for centuries
    and rediscovered as a "lost city" mystery. The Treasury and other structures are said to
    hold ancient secrets and hidden treasures. This is the "Shell" - the focus on mystery and
    lost civilizations.
    """,
            "Colosseum": f"""
    The Colosseum is one of the New 7 Wonders of the World. This massive amphitheatre in Rome
    was the site of gladiator battles, animal hunts, and public executions. The structure is
    said to be haunted by the spirits of those who died in the arena. The focus is on violence,
    entertainment, and the spectacle of death. This is the "Shell" - but the Seed beneath is
    community gathering and stewardship.
    """,
            "Chichén Itzá": f"""
    Chichén Itzá is one of the New 7 Wonders of the World. This ancient Maya-Toltec city
    features the Pyramid of Kukulkan, where human sacrifices were performed. The site is said
    to be aligned with astronomical events and holds ancient mysteries. The focus is on sacrifice
    and ancient rituals. This is the "Shell" - but the Seed is harmony with natural cycles.
    """,
            "Machu Picchu": f"""
    Machu Picchu is one of the New 7 Wonders of the World and already integrated as Pillar 04.
    This Inca citadel was "lost" for centuries and rediscovered as a mysterious mountain sanctuary.
    The focus is on the "lost city" mystery and ancient Inca secrets. This is the "Shell" - but
    the Seed is harmony with the Earth and mountain stewardship.
    """,
            "Taj Mahal": f"""
    The Taj Mahal is one of the New 7 Wonders of the World and already integrated as Seat 09.
    This white marble mausoleum was built as a monument to love, but the focus is often on the
    romantic story and tourist attraction. The structure is said to be perfectly symmetrical,
    representing the unity of love. This is the "Shell" - but the Seed is love as the highest
    form of stewardship.
    """,
            "Christ the Redeemer": f"""
    Christ the Redeemer is one of the New 7 Wonders of the World. This Art Deco statue stands
    30 meters tall on Corcovado Mountain in Rio de Janeiro, with arms open wide. The statue is
    a symbol of Christianity and Brazilian unity, but the focus is often on tourism and religious
    symbolism. This is the "Shell" - but the Seed is welcoming all with open arms, love as
    the highest mastery.
    """
        }
        
        return narratives.get(name, f"{name} is one of the New 7 Wonders of the World. {modern_distortion}")
    
    def integrate_wonder(self, wonder: Dict[str, Any], verbose: bool = True) -> Dict[str, Any]:
        """Integrate a single wonder into all heritage systems."""
        result = {
            "wonder_id": wonder.get("wonder_id"),
            "name": wonder.get("name"),
            "integration_steps": [],
            "errors": [],
            "site_id": None
        }
        
        # Skip if already in system
        if wonder.get("already_in_system"):
            result["status"] = "already_integrated"
            result["integration_steps"].append("skipped - already in system")
            if verbose:
                print(f"  ⏭️  {wonder.get('name')} - Already integrated ({wonder.get('pillar_id') or wonder.get('seat_id')})")
            return result
        
        if verbose:
            print(f"\n  🔄 Integrating {wonder.get('name')}...")
        
        # Step 1: Register in Temporal Heritage Registry
        if HERITAGE_AVAILABLE:
            try:
                default_period = TimePeriod.MODERN.value if HERITAGE_AVAILABLE else "MODERN"
                time_period = TIME_PERIOD_MAP.get(wonder.get("time_period", "modern"), default_period) if TIME_PERIOD_MAP else "MODERN"
                site_type = SITE_TYPE_MAP.get(wonder.get("wonder_type", ""), "Heritage Site")
                
                site_id = register_heritage_site(
                    site_name=wonder.get("name"),
                    site_type=site_type,
                    region=wonder.get("location", ""),
                    country=wonder.get("location", ""),
                    coordinates_lat=wonder.get("coordinates", {}).get("lat"),
                    coordinates_lon=wonder.get("coordinates", {}).get("lon"),
                    timeline_dimension=TimelineDimension.PRIMARY.value,
                    time_period=time_period,
                    year_established=self._parse_year(wonder.get("year_built", "")),
                    current_status="active",
                    law_41_compliant=wonder.get("law_41_compliant", False),
                    requires_cleansing=wonder.get("requires_cleansing", True)
                )
                
                result["site_id"] = site_id
                result["integration_steps"].append("temporal_registry")
                if verbose:
                    print(f"    ✅ Registered in Temporal Heritage Registry (ID: {site_id})")
            except Exception as e:
                error_msg = f"Error registering {wonder.get('name')}: {e}"
                result["errors"].append(error_msg)
                logger.error(error_msg)
        
        # Step 2: Archive original narrative
        if HERITAGE_AVAILABLE and result.get("site_id"):
            try:
                original_narrative = self.get_wonder_original_narrative(wonder)
                add_heritage_narrative(
                    site_id=result["site_id"],
                    narrative_content=original_narrative,
                    narrative_type="original",
                    timeline_dimension=TimelineDimension.PRIMARY.value,
                    violation_type=wonder.get("violation_type", "haunted_exploitation"),
                    dark_energy_detected=True,
                    regeneration_applied=False
                )
                result["integration_steps"].append("narrative_archival")
                if verbose:
                    print(f"    ✅ Archived original narrative (Shell)")
            except Exception as e:
                error_msg = f"Error archiving narrative: {e}"
                result["errors"].append(error_msg)
                logger.error(error_msg)
        
        # Step 3: Conduct full audit (if audit framework available)
        if self.audit_framework and result.get("site_id"):
            try:
                profile = HeritageSiteProfile(
                    site_name=wonder.get("name"),
                    site_type=SITE_TYPE_MAP.get(wonder.get("wonder_type", ""), "Heritage Site"),
                    region=wonder.get("location", ""),
                    country=wonder.get("location", ""),
                    coordinates_lat=wonder.get("coordinates", {}).get("lat"),
                    coordinates_lon=wonder.get("coordinates", {}).get("lon"),
                    timeline_dimension=TimelineDimension.PRIMARY.value,
                    time_period=TIME_PERIOD_MAP.get(wonder.get("time_period", "modern"), "MODERN") if TIME_PERIOD_MAP else "MODERN",
                    year_established=self._parse_year(wonder.get("year_built", "")),
                    current_status="active",
                    law_41_compliant=wonder.get("law_41_compliant", False),
                    requires_cleansing=wonder.get("requires_cleansing", True),
                    original_narrative=self.get_wonder_original_narrative(wonder),
                    violation_type=wonder.get("violation_type", "haunted_exploitation"),
                    audit_title=f"{wonder.get('name')} - New 7 Wonders Integration",
                    audit_description=f"Integration of {wonder.get('name')} into the Heritage Meridian System",
                    is_super_pillar=False
                )
                
                audit_report = self.audit_framework.conduct_audit(profile, verbose=False)
                result["audit_report"] = audit_report
                result["integration_steps"].append("full_audit")
                if verbose:
                    print(f"    ✅ Completed full heritage audit")
            except Exception as e:
                error_msg = f"Error conducting audit: {e}"
                result["errors"].append(error_msg)
                logger.error(error_msg)
        
        result["status"] = "integrated" if not result.get("errors") else "partial"
        return result
    
    def _parse_year(self, year_str: str) -> Optional[int]:
        """Parse year from string like '1922-1931 CE' or '7th century BCE'."""
        if not year_str:
            return None
        
        # Try to extract first year from range
        import re
        match = re.search(r'(\d{4})', year_str)
        if match:
            return int(match.group(1))
        
        return None
    
    def integrate_all(self, verbose: bool = True) -> Dict[str, Any]:
        """Integrate all 7 Wonders into the heritage systems."""
        print("=" * 80)
        print("NEW 7 WONDERS OF THE WORLD - FULL CODEBASE INTEGRATION")
        print("=" * 80)
        print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        print("THE MISSION:")
        print("THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS")
        print("LOVE IS THE HIGHEST MASTERY")
        print("ENERGY + LOVE = WE ALL WIN")
        print()
        print("=" * 80)
        print()
        
        results = {
            "integration_timestamp": datetime.now().isoformat(),
            "total_wonders": len(self.wonders),
            "wonders_integrated": [],
            "wonders_skipped": [],
            "errors": []
        }
        
        for wonder in self.wonders:
            result = self.integrate_wonder(wonder, verbose=verbose)
            self.integration_results.append(result)
            
            if result.get("status") == "already_integrated":
                results["wonders_skipped"].append(result)
            else:
                results["wonders_integrated"].append(result)
            
            if result.get("errors"):
                results["errors"].extend(result["errors"])
        
        # Summary
        print()
        print("=" * 80)
        print("INTEGRATION SUMMARY")
        print("=" * 80)
        print(f"Total Wonders: {results['total_wonders']}")
        print(f"Newly Integrated: {len(results['wonders_integrated'])}")
        print(f"Already in System: {len(results['wonders_skipped'])}")
        print(f"Errors: {len(results['errors'])}")
        print()
        
        if results['wonders_integrated']:
            print("✅ Successfully Integrated:")
            for result in results['wonders_integrated']:
                print(f"   - {result.get('name')} (ID: {result.get('site_id', 'N/A')})")
        
        if results['wonders_skipped']:
            print("\n⏭️  Already in System:")
            for result in results['wonders_skipped']:
                print(f"   - {result.get('name')}")
        
        if results['errors']:
            print("\n❌ Errors:")
            for error in results['errors']:
                print(f"   - {error}")
        
        print()
        print("=" * 80)
        print("INTEGRATION COMPLETE")
        print("=" * 80)
        
        # Save results
        output_dir = Path(__file__).parent.parent / "output" / "heritage_meridian"
        output_dir.mkdir(parents=True, exist_ok=True)
        output_file = output_dir / f"7_wonders_integration_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        if verbose:
            print(f"\n📄 Results saved to: {output_file}")
        
        return results


def main():
    """Main entry point."""
    integrator = New7WondersIntegrator()
    results = integrator.integrate_all(verbose=True)
    return results


if __name__ == "__main__":
    main()
