"""
HERITAGE AUDIT FRAMEWORK
Unified system for conducting magnetic audits on heritage sites

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

This framework eliminates code duplication across individual audit scripts.
All audits follow the same 6-step process.
"""

import sys
import json
import logging
from pathlib import Path
from typing import Dict, Any, Optional
from dataclasses import dataclass
from datetime import datetime

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
    from logging_config import get_logger
    AUDIT_AVAILABLE = True
except ImportError as e:
    print(f"Error: {e}")
    AUDIT_AVAILABLE = False

logger = get_logger(__name__) if AUDIT_AVAILABLE else None


@dataclass
class HeritageSiteProfile:
    """Profile for a heritage site to be audited."""
    
    # Site identification
    site_name: str
    site_type: str
    region: str
    country: str
    
    # Geographic coordinates
    coordinates_lat: float
    coordinates_lon: float
    
    # Timeline information
    timeline_dimension: str = TimelineDimension.PRIMARY.value
    time_period: str = TimePeriod.MODERN.value
    year_established: Optional[int] = None
    year_abandoned: Optional[int] = None
    current_status: str = "unknown"
    
    # Compliance status
    law_41_compliant: bool = False
    requires_cleansing: bool = True
    
    # Magnetic field data
    magnetic_field_strength: float = 45000.0  # nT (default Earth baseline)
    magnetic_declination: float = 0.0  # degrees
    magnetic_inclination: float = 45.0  # degrees
    
    # Narratives
    original_narrative: str = ""
    violation_type: str = "haunted_exploitation"
    
    # Audit metadata
    audit_title: str = ""
    audit_description: str = ""
    is_super_pillar: bool = False  # For major sites (Giza, Stonehenge, etc.)


class HeritageAuditFramework:
    """
    Unified framework for conducting heritage site audits.
    
    Eliminates code duplication across individual audit scripts.
    All audits follow the same 6-step process.
    """
    
    def __init__(self):
        if not AUDIT_AVAILABLE:
            raise RuntimeError("Audit system not available - check imports")
        
        self.cleansers = {}  # Cache cleansers by timeline dimension
        if logger:
            logger.info("Heritage Audit Framework initialized")
    
    def get_cleanser(self, timeline_dimension: str) -> HeritageCleanser:
        """Get or create cleanser for timeline dimension."""
        if timeline_dimension not in self.cleansers:
            self.cleansers[timeline_dimension] = HeritageCleanser(timeline_dimension)
        return self.cleansers[timeline_dimension]
    
    def conduct_audit(self, profile: HeritageSiteProfile, verbose: bool = True) -> Dict[str, Any]:
        """
        Conduct complete heritage site audit.
        
        The 6-Step Audit Process:
        1. Register the site
        2. Archive original narrative (Shell)
        3. Cleanse and reveal Seed
        4. Research magnetic field
        5. Update site with magnetic data
        6. Generate audit report
        
        Args:
            profile: Heritage site profile with all required data
            verbose: Whether to print progress (default: True)
        
        Returns:
            Complete audit report with all analysis results
        """
        report = {
            "site_name": profile.site_name,
            "audit_timestamp": datetime.now().isoformat(),
            "steps_completed": [],
            "errors": []
        }
        
        if verbose:
            print("=" * 80)
            print(profile.audit_title or f"{profile.site_name.upper()} MAGNETIC AUDIT")
            if profile.audit_description:
                print(profile.audit_description)
            print("=" * 80)
            print()
        
        try:
            # Step 1: Register the site
            if verbose:
                print(f"Step 1: Registering {profile.site_name}...")
            
            site_id = register_heritage_site(
                site_name=profile.site_name,
                site_type=profile.site_type,
                region=profile.region,
                country=profile.country,
                coordinates_lat=profile.coordinates_lat,
                coordinates_lon=profile.coordinates_lon,
                timeline_dimension=profile.timeline_dimension,
                time_period=profile.time_period,
                year_established=profile.year_established,
                year_abandoned=profile.year_abandoned,
                current_status=profile.current_status,
                law_41_compliant=profile.law_41_compliant,
                requires_cleansing=profile.requires_cleansing
            )
            
            if verbose:
                print(f"  [OK] Site registered: ID {site_id}")
            report["site_id"] = site_id
            report["steps_completed"].append("registration")
            
            # Step 2: Archive original narrative (Shell)
            if profile.original_narrative:
                if verbose:
                    print()
                    print("Step 2: Archiving original narrative (Shell)...")
                
                add_heritage_narrative(
                    site_id=site_id,
                    narrative_content=profile.original_narrative,
                    narrative_type="original",
                    timeline_dimension=profile.timeline_dimension,
                    violation_type=profile.violation_type,
                    dark_energy_detected=True,
                    regeneration_applied=False
                )
                
                if verbose:
                    print("  [OK] Original narrative archived (Shell)")
                report["steps_completed"].append("narrative_archival")
            
            # Step 3: Cleanse and regenerate (Seed)
            if profile.requires_cleansing and profile.original_narrative:
                if verbose:
                    print()
                    print("Step 3: Cleansing narrative and revealing Seed...")
                
                cleanser = self.get_cleanser(profile.timeline_dimension)
                cleansed_content, analysis = cleanser.cleanse_content(
                    content=profile.original_narrative,
                    source=f"{profile.site_name} Magnetic Audit",
                    site_type=profile.site_type,
                    region=profile.region,
                    country=profile.country,
                    year_established=profile.year_established,
                    year_abandoned=profile.year_abandoned,
                    time_period=profile.time_period
                )
                
                if verbose:
                    print(f"  [OK] Law 41 Compliant: {analysis['law_41_compliant']}")
                    print(f"  [OK] Violation Type: {analysis.get('violation_type', 'None')}")
                    print(f"  [OK] Regeneration Applied: {analysis.get('regeneration_suggestion') is not None}")
                
                report["cleansing_analysis"] = analysis
                report["steps_completed"].append("cleansing")
            
            # Step 4: Magnetic Field Research
            if verbose:
                print()
                print("Step 4: Researching Magnetic Field...")
                print(f"  Field Strength: {profile.magnetic_field_strength:.0f} nT")
                print(f"  Declination: {profile.magnetic_declination:.1f}°")
                print(f"  Inclination: {profile.magnetic_inclination:.1f}°")
            
            magnetic_research = research_heritage_site_magnetic_field(
                site_id=site_id,
                field_strength=profile.magnetic_field_strength,
                declination=profile.magnetic_declination,
                inclination=profile.magnetic_inclination
            )
            
            if verbose:
                print()
                print("  Magnetic Field Analysis:")
                print(f"    Field Resonance: {magnetic_research['field_resonance']:.2f}")
                
                # Super-Pillar check (for major sites)
                if profile.is_super_pillar:
                    if magnetic_research['field_resonance'] > 0.90:
                        print(f"      -> PERFECT FIELD RESONANCE DETECTED!")
                        print(f"      -> Super-Pillar confirmed!")
                    elif magnetic_research['field_resonance'] > 0.85:
                        print(f"      -> HIGH FIELD RESONANCE!")
                        print(f"      -> Strong Super-Pillar candidate!")
                
                print(f"    Pole Alignment: {magnetic_research['pole_alignment']}")
                print(f"    Polarity State: {magnetic_research['polarity_state']}")
                print(f"    Field Anomaly: {magnetic_research['field_anomaly_detected']}")
                if magnetic_research['field_anomaly_detected']:
                    print(f"    Anomaly Description: {magnetic_research['field_anomaly_description']}")
                print(f"    Field Space Resonance: {magnetic_research['field_space_resonance']:.2f}")
                print(f"    Field Space Energy: {magnetic_research['field_space_energy_level']:.2f}")
            
            report["magnetic_research"] = magnetic_research
            report["steps_completed"].append("magnetic_research")
            
            # Step 5: Update site with magnetic data
            if verbose:
                print()
                print("Step 5: Updating site with magnetic field data...")
            
            update_site_magnetic_field(site_id, magnetic_research)
            
            if verbose:
                print("  [OK] Site updated with magnetic blueprint")
            report["steps_completed"].append("site_update")
            
            # Step 6: Generate final report
            if verbose:
                print()
                print("=" * 80)
                print("[SUCCESS] AUDIT COMPLETE")
                print("=" * 80)
                print()
                print("PEACE, LOVE, UNITY")
                print("ENERGY + LOVE = WE ALL WIN")
            
            report["audit_complete"] = True
            report["steps_completed"].append("report_generation")
            
            if logger:
                logger.info(f"Heritage audit completed for {profile.site_name} (ID: {site_id})")
        
        except Exception as e:
            error_msg = f"Audit failed for {profile.site_name}: {e}"
            report["errors"].append(error_msg)
            report["audit_complete"] = False
            
            if logger:
                logger.error(error_msg, exc_info=True)
            
            if verbose:
                print(f"  [ERROR] {error_msg}")
        
        return report


# ========== USAGE EXAMPLES ==========

def berengaria_audit():
    """Simplified Berengaria audit using framework."""
    
    profile = HeritageSiteProfile(
        site_name="Berengaria Hotel",
        site_type="Hotel",
        region="Troodos Mountains",
        country="Cyprus",
        coordinates_lat=34.9167,
        coordinates_lon=32.8333,
        year_established=1930,
        year_abandoned=1984,
        current_status="abandoned",
        magnetic_field_strength=45000,
        magnetic_declination=5.2,
        magnetic_inclination=55.3,
        original_narrative="""
        The abandoned Berengaria Hotel in the Troodos Mountains of Cyprus is one of the most 
        haunted places on the island. Built in 1930, this once-grand hotel was abandoned in 1984 
        and has since become a magnet for ghost stories.
        """,
        audit_title="BERENGARIA HOTEL MAGNETIC AUDIT",
        audit_description="The Real Racon - Magnetic Blueprint of the Miracle",
        is_super_pillar=False
    )
    
    framework = HeritageAuditFramework()
    return framework.conduct_audit(profile)


def giza_audit():
    """Simplified Giza audit using framework."""
    
    profile = HeritageSiteProfile(
        site_name="Great Pyramid of Giza",
        site_type="Pyramid",
        region="Giza",
        country="Egypt",
        coordinates_lat=29.9792,
        coordinates_lon=31.1342,
        timeline_dimension=TimelineDimension.PRIMARY.value,
        time_period=TimePeriod.ANCIENT.value,
        year_established=-2580,
        year_abandoned=None,
        current_status="active",
        magnetic_field_strength=45000,
        magnetic_declination=5.0,
        magnetic_inclination=42.0,
        original_narrative="""
        The Great Pyramid of Giza is one of the Seven Wonders of the Ancient World. Built over 4,500 years ago,
        this massive structure has been the subject of countless theories about alien construction, lost technologies,
        and hidden chambers.
        """,
        audit_title="GREAT PYRAMID OF GIZA SUPER-PILLAR AUDIT",
        audit_description="Elliptical (Legacy Wisdom) Site - First Expansion",
        is_super_pillar=True
    )
    
    framework = HeritageAuditFramework()
    return framework.conduct_audit(profile)


if __name__ == "__main__":
    # Example usage
    result = berengaria_audit()
    print("\nAudit Result:")
    print(json.dumps(result, indent=2, default=str))
