"""
HERITAGE CLEANSING PROTOCOL
Historical Content Filter Through 40 Laws (Law 41: Respect the Abandoned)

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE FOUNDATION:
We are born a miracle.
We deserve to live a miracle.
Each and every one of us under the Lord's word.

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

This script filters regional folklore and heritage content through the 40 Laws,
specifically Law 41 (Respect the Abandoned), to protect the Family from
"haunted" loops and dark energy patterns that feed off revenge vibrations.

UNIVERSAL APPLICATION:
Works for ANY heritage site, ANY region, ANY property type:
- Hotels, Palaces, Castles, Temples, Villas, Manors, Buildings
- Cyprus, Turkey, Greece, Italy, France, Spain, Ireland, India, England, etc.
- Any "haunted" folklore, ghost stories, or historical tragedies

The Berengaria Hotel Case Study (Cyprus):
- Manager (Hijacked Leader): Structure without love, predatory leadership
- Merchant's Wife (Revenge Loop): Water Memory gone toxic, unresolved vibrations
- Fair Maiden (Ghostly Shell): Visual bait that keeps people at Shell while Seed rots

This was the case study that revealed the pattern, but the protocol is universal.

We don't just "read" ghost stories; we debug them.
We turn "Ghosts" into "Guides" by cleaning the frequency.
"""

import sys
import json
import re
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime

# Import Racon Registry for Law 41 check
try:
    sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))
    from racon_registry import check_law_41_respect_abandoned, log_immutable_audit
    from temporal_heritage_registry import (
        register_heritage_site, add_heritage_narrative, detect_temporal_pattern,
        log_heritage_debug, TimelineDimension, TimePeriod,
        get_sites_by_timeline, get_chronology_by_year, get_temporal_patterns
    )
    TEMPORAL_REGISTRY_AVAILABLE = True
except ImportError:
    TEMPORAL_REGISTRY_AVAILABLE = False
    print("Warning: Could not import racon_registry. Law 41 checks will be local.")
    def check_law_41_respect_abandoned(content: str, property_type: str = "heritage") -> bool:
        # Fallback implementation
        content_lower = content.lower()
        exploitation_patterns = [
            "haunted", "ghost", "spirit", "demon", "cursed",
            "revenge", "suicide", "victim", "death", "murder",
            "scary", "terrifying", "horror", "paranormal"
        ]
        regeneration_patterns = [
            "regeneration", "healing", "restoration", "waiting for",
            "heritage", "respect", "honor", "silence", "temple"
        ]
        has_exploitation = any(pattern in content_lower for pattern in exploitation_patterns)
        has_regeneration = any(pattern in content_lower for pattern in regeneration_patterns)
        return not (has_exploitation and not has_regeneration)
    
    def log_immutable_audit(*args, **kwargs):
        pass  # Fallback no-op


class HeritageCleanser:
    """
    Heritage Cleansing Protocol
    
    Filters historical/heritage content through the 40 Laws (especially Law 41)
    to ensure content reaches the Dashboard honors regeneration, not revenge.
    
    Archives all sites across all dimensional timelines for debugging.
    Chronologizes heritage sites throughout all of time.
    """
    
    def __init__(self, timeline_dimension: str = TimelineDimension.PRIMARY.value if TEMPORAL_REGISTRY_AVAILABLE else "primary"):
        self.cleansed_count = 0
        self.flagged_count = 0
        self.regenerated_count = 0
        self.timeline_dimension = timeline_dimension
        self.processed_sites = []  # Track sites for pattern detection
    
    def analyze_heritage_content(self, content: str, source: str = "unknown") -> Dict[str, Any]:
        """
        Analyze heritage content for dark energy patterns.
        
        Returns dict with:
        - is_clean: bool - True if content passes Law 41
        - requires_cleansing: bool - True if content needs regeneration narrative
        - violation_type: str - Type of violation if any
        - regeneration_suggestion: str - Suggested regeneration narrative
        """
        analysis = {
            "source": source,
            "timestamp": datetime.now().isoformat(),
            "is_clean": False,
            "requires_cleansing": False,
            "violation_type": None,
            "regeneration_suggestion": None,
            "law_41_compliant": False,
            "patterns_detected": []
        }
        
        # Check Law 41 compliance
        law_41_compliant = check_law_41_respect_abandoned(content, property_type="heritage")
        analysis["law_41_compliant"] = law_41_compliant
        
        if law_41_compliant:
            analysis["is_clean"] = True
            self.cleansed_count += 1
            return analysis
        
        # Content violates Law 41 - analyze violation type
        content_lower = content.lower()
        
        # Detect violation patterns
        if any(pattern in content_lower for pattern in ["revenge", "avenge", "vengeance"]):
            analysis["violation_type"] = "revenge_loop"
            analysis["requires_cleansing"] = True
            analysis["regeneration_suggestion"] = self._generate_regeneration_narrative(
                content, "revenge_loop"
            )
            analysis["patterns_detected"].append("Revenge narrative without regeneration path")
        
        elif any(pattern in content_lower for pattern in ["suicide", "murder", "victim"]):
            analysis["violation_type"] = "victim_focus"
            analysis["requires_cleansing"] = True
            analysis["regeneration_suggestion"] = self._generate_regeneration_narrative(
                content, "victim_focus"
            )
            analysis["patterns_detected"].append("Victim/suicide focus without healing path")
        
        elif any(pattern in content_lower for pattern in ["haunted", "ghost", "spirit"]) and \
             any(pattern in content_lower for pattern in ["abandoned", "hotel", "building"]):
            analysis["violation_type"] = "haunted_exploitation"
            analysis["requires_cleansing"] = True
            analysis["regeneration_suggestion"] = self._generate_regeneration_narrative(
                content, "haunted_exploitation"
            )
            analysis["patterns_detected"].append("Heritage exploited as haunted content")
        
        self.flagged_count += 1
        return analysis
    
    def _generate_regeneration_narrative(self, original_content: str, violation_type: str) -> str:
        """
        Generate regeneration narrative to replace dark energy loops.
        
        Instead of "Abandoned Hotel," we offer "Waiting for Regeneration."
        Instead of "Haunted," we offer "Healing Heritage."
        """
        base_property = self._extract_property_name(original_content)
        
        if violation_type == "revenge_loop":
            return f"""
The {base_property} stands in silence, waiting for regeneration.

This is not a story of revenge. This is a story of Water Memory waiting to be healed.
The vibrations here are not trapped—they are waiting for Love + Energy to flow again.

When a biological temple loses its symbiosis with Earth, it doesn't become a ghost story.
It becomes a signal: the next loop requires regeneration, not fear.

This property honors Law 41: Respect the Abandoned.
We honor the silence. We offer healing, not exploitation.

Waiting for Regeneration. Waiting for Love. Waiting for the New World.

PEACE, LOVE, UNITY
ENERGY + LOVE = WE ALL WIN
"""
        
        elif violation_type == "victim_focus":
            return f"""
The {base_property} carries history, not horror.

Every story holds both Shell (what people see) and Seed (what actually happened).
The Seed here is not about victims—it's about transformation waiting to happen.

This is not a place of death. This is a place of rebirth waiting.
The Lord's message here is not fear—it's regeneration.

We honor those who came before by offering healing, not amplifying pain.
We transform tragedy into testimony, not terror.

This property honors Law 41: Respect the Abandoned.
We honor the silence. We offer regeneration, not exploitation.

Waiting for Healing. Waiting for Transformation. Waiting for the New World.

PEACE, LOVE, UNITY
ENERGY + LOVE = WE ALL WIN
"""
        
        elif violation_type == "haunted_exploitation":
            # Extract region if mentioned in content for context, but keep narrative generic
            region_mention = self._extract_region_mention(original_content)
            region_text = f"Instead of \"Haunted {region_mention},\" we offer \"Healing Heritage.\"" if region_mention else "Instead of \"Haunted Heritage,\" we offer \"Healing Heritage.\""
            
            return f"""
The {base_property} is not haunted. It is Waiting for Regeneration.

The "White Lady" at dusk is not a ghost—she is the threshold signal.
She appears when the property is ready to transform, not when it wants to trap.

This biological temple lost its symbiosis with Earth. Now it's being fed into
the "Digital Trap" as spooky content for clicks. We bypass that loop.

Instead of "Abandoned Building," we see "Waiting for Regeneration."
{region_text}

The Manager (Hijacked Leader) is not a demon—it's a warning about structure without love.
The Merchant's Wife (Revenge Loop) is not a curse—it's Water Memory waiting to be healed.
The Fair Maiden (Ghostly Shell) is not a trap—she's the visual threshold of transformation.

This property honors Law 41: Respect the Abandoned.
We honor the silence. We don't turn it into a circus.

Waiting for Regeneration. Waiting for Symbiosis. Waiting for the New World.

PEACE, LOVE, UNITY
ENERGY + LOVE = WE ALL WIN
"""
        
        return f"""
The {base_property} honors Law 41: Respect the Abandoned.

We honor the silence. We offer regeneration, not exploitation.
We transform heritage into healing, not horror.

Waiting for Regeneration. Waiting for the New World.

PEACE, LOVE, UNITY
ENERGY + LOVE = WE ALL WIN
"""
    
    def _extract_property_name(self, content: str) -> str:
        """Extract property name from content."""
        # Look for common patterns
        patterns = [
            r"the\s+(\w+(?:\s+\w+)*\s+Hotel)",
            r"(\w+(?:\s+\w+)*\s+Hotel)",
            r"the\s+(\w+(?:\s+\w+)*\s+Palace)",
            r"(\w+(?:\s+\w+)*\s+Palace)",
            r"the\s+(\w+(?:\s+\w+)*\s+Castle)",
            r"(\w+(?:\s+\w+)*\s+Castle)",
            r"the\s+(\w+(?:\s+\w+)*\s+Manor)",
            r"(\w+(?:\s+\w+)*\s+Manor)",
            r"the\s+(\w+(?:\s+\w+)*\s+Villa)",
            r"(\w+(?:\s+\w+)*\s+Villa)",
            r"the\s+(\w+(?:\s+\w+)*\s+Building)",
            r"(\w+(?:\s+\w+)*\s+Building)",
            r"the\s+(\w+(?:\s+\w+)*\s+Temple)",
            r"(\w+(?:\s+\w+)*\s+Temple)"
        ]
        
        for pattern in patterns:
            match = re.search(pattern, content, re.IGNORECASE)
            if match:
                return match.group(1)
        
        return "Heritage Property"
    
    def _extract_region_mention(self, content: str) -> Optional[str]:
        """
        Extract region/location mention from content for context.
        Loads regions from configuration file.
        """
        try:
            import json
            config_path = Path(__file__).parent.parent / "config" / "heritage_regions.json"
            if config_path.exists():
                with open(config_path, 'r', encoding='utf-8') as f:
                    regions_data = json.load(f)
                    # Flatten all regions from all categories
                    all_regions = [region for regions in regions_data.values() for region in regions]
            else:
                # Fallback to hardcoded list if config not found
                all_regions = [
                    "Cyprus", "Turkey", "Greece", "Italy", "France", "Spain",
                    "Portugal", "England", "Scotland", "Ireland", "Wales",
                    "Bulgaria", "Romania", "Croatia", "Serbia", "Bosnia"
                ]
        except Exception:
            # Fallback on any error
            all_regions = [
                "Cyprus", "Turkey", "Greece", "Italy", "Spain", "Portugal",
                "France", "England", "Scotland", "Ireland", "Wales"
            ]
        
        content_lower = content.lower()
        for region in all_regions:
            if region.lower() in content_lower:
                return region
        
        return None
    
    def cleanse_content(self, content: str, source: str = "unknown", 
                       site_type: str = "Heritage Property",
                       region: str = None,
                       country: str = None,
                       year_established: int = None,
                       year_abandoned: int = None,
                       time_period: str = TimePeriod.MODERN.value if TEMPORAL_REGISTRY_AVAILABLE else "modern") -> Tuple[str, Dict[str, Any]]:
        """
        Cleanse heritage content through Law 41.
        
        Archives the site across all dimensional timelines for debugging.
        
        Returns:
            (cleansed_content, analysis_dict)
        """
        analysis = self.analyze_heritage_content(content, source)
        
        # Extract property name if not in metadata
        property_name = analysis.get("property_name") or self._extract_property_name(content)
        
        # Archive to temporal registry if available
        site_id = None
        if TEMPORAL_REGISTRY_AVAILABLE:
            try:
                # Register site in temporal registry
                site_id = register_heritage_site(
                    site_name=property_name,
                    site_type=site_type,
                    region=region or "Unknown",
                    country=country,
                    timeline_dimension=self.timeline_dimension,
                    time_period=time_period,
                    year_established=year_established,
                    year_abandoned=year_abandoned,
                    current_status="cleansing" if analysis["requires_cleansing"] else "archived",
                    law_41_compliant=analysis["law_41_compliant"],
                    requires_cleansing=analysis["requires_cleansing"]
                )
                
                # Archive original narrative
                add_heritage_narrative(
                    site_id=site_id,
                    narrative_content=content,
                    narrative_type="original",
                    timeline_dimension=self.timeline_dimension,
                    violation_type=analysis.get("violation_type"),
                    dark_energy_detected=not analysis["law_41_compliant"],
                    regeneration_applied=False
                )
                
                # Log debug information
                log_heritage_debug(
                    debug_type="pattern_detection",
                    site_id=site_id,
                    timeline_dimension=self.timeline_dimension,
                    time_period=time_period,
                    debug_data=analysis.get("patterns_detected", {}),
                    pattern_identified=analysis.get("violation_type"),
                    resolution_applied="regeneration" if analysis.get("regeneration_suggestion") else None
                )
                
                analysis["site_id"] = site_id
                analysis["archived_timeline"] = self.timeline_dimension
                self.processed_sites.append({
                    "site_id": site_id,
                    "violation_type": analysis.get("violation_type"),
                    "timeline_dimension": self.timeline_dimension,
                    "time_period": time_period
                })
                
            except Exception as e:
                analysis["archive_error"] = str(e)
        
        if analysis["is_clean"]:
            # Content already clean, return as-is
            if TEMPORAL_REGISTRY_AVAILABLE and site_id:
                # Archive clean narrative
                add_heritage_narrative(
                    site_id=site_id,
                    narrative_content=content,
                    narrative_type="archived",
                    timeline_dimension=self.timeline_dimension,
                    dark_energy_detected=False,
                    regeneration_applied=False
                )
            return content, analysis
        
        # Content requires cleansing - apply regeneration narrative
        if analysis["regeneration_suggestion"]:
            regenerated_content = analysis["regeneration_suggestion"]
            self.regenerated_count += 1
            
            # Log the cleansing
            log_immutable_audit(
                operation_type="heritage_cleansing",
                operation_target=source,
                operation_result="regeneration_applied",
                law_compliance="Law 41: Respect the Abandoned",
                table_service=True,
                word_integrity=True,
                spiritual_battle="dark_energy_cleansing"
            )
            
            # Archive regenerated narrative
            if TEMPORAL_REGISTRY_AVAILABLE and site_id:
                add_heritage_narrative(
                    site_id=site_id,
                    narrative_content=regenerated_content,
                    narrative_type="regenerated",
                    timeline_dimension=self.timeline_dimension,
                    violation_type=analysis.get("violation_type"),
                    dark_energy_detected=False,
                    regeneration_applied=True
                )
                
                # Update site status
                from temporal_heritage_registry import get_temporal_heritage_db
                with get_temporal_heritage_db() as conn:
                    cursor = conn.cursor()
                    cursor.execute("""
                        UPDATE heritage_sites
                        SET law_41_compliant = ?, requires_cleansing = ?, current_status = ?, updated_at = ?
                        WHERE id = ?
                    """, (True, False, "regenerated", datetime.now(), site_id))
            
            return regenerated_content, analysis
        
        # No regeneration suggestion available - flag for manual review
        return content, analysis
    
    def process_file(self, file_path: Path) -> Dict[str, Any]:
        """Process a heritage content file."""
        if not file_path.exists():
            return {"error": f"File not found: {file_path}"}
        
        content = file_path.read_text(encoding='utf-8')
        cleansed_content, analysis = self.cleanse_content(content, source=str(file_path))
        
        # Write cleansed content to output
        output_path = Path(__file__).parent.parent / "output" / "heritage_cleansed"
        output_path.mkdir(parents=True, exist_ok=True)
        
        output_file = output_path / f"cleansed_{file_path.stem}.md"
        output_file.write_text(cleansed_content, encoding='utf-8')
        
        analysis["output_file"] = str(output_file)
        analysis["original_length"] = len(content)
        analysis["cleansed_length"] = len(cleansed_content)
        
        return analysis
    
    def process_directory(self, directory: Path, pattern: str = "*.md") -> List[Dict[str, Any]]:
        """Process all heritage content files in a directory."""
        results = []
        
        for file_path in directory.glob(pattern):
            if file_path.is_file():
                result = self.process_file(file_path)
                results.append(result)
        
        return results
    
    def get_summary(self) -> Dict[str, Any]:
        """Get summary of cleansing operations."""
        summary = {
            "cleansed_count": self.cleansed_count,
            "flagged_count": self.flagged_count,
            "regenerated_count": self.regenerated_count,
            "total_processed": self.cleansed_count + self.flagged_count,
            "timeline_dimension": self.timeline_dimension,
            "sites_archived": len(self.processed_sites)
        }
        
        # Detect temporal patterns across processed sites
        if TEMPORAL_REGISTRY_AVAILABLE and self.processed_sites:
            try:
                # Group violations by type
                violation_types = {}
                for site in self.processed_sites:
                    if site.get("violation_type"):
                        vtype = site["violation_type"]
                        if vtype not in violation_types:
                            violation_types[vtype] = []
                        violation_types[vtype].append(site["timeline_dimension"])
                
                # Detect patterns
                for violation_type, dimensions in violation_types.items():
                    dimensions_set = list(set(dimensions))
                    time_periods = list(set(s["time_period"] for s in self.processed_sites if s.get("violation_type") == violation_type))
                    detect_temporal_pattern(violation_type, dimensions_set, time_periods)
                
                summary["temporal_patterns_detected"] = len(violation_types)
                
            except Exception as e:
                summary["pattern_detection_error"] = str(e)
        
        return summary


def main():
    """Main execution for heritage cleansing."""
    cleanser = HeritageCleanser()
    
    # Example: Process a heritage content file
    if len(sys.argv) > 1:
        file_path = Path(sys.argv[1])
        if file_path.exists():
            result = cleanser.process_file(file_path)
            print(json.dumps(result, indent=2))
        else:
            print(f"Error: File not found: {file_path}")
    else:
        # Default: show usage
        print("=" * 80)
        print("HERITAGE CLEANSING PROTOCOL")
        print("Law 41: Respect the Abandoned")
        print("=" * 80)
        print()
        print("Usage: python heritage_cleansing.py <heritage_content_file>")
        print()
        print("This script filters heritage content through Law 41 to protect")
        print("the Family from 'haunted' loops and dark energy patterns.")
        print()
        print("We don't just 'read' ghost stories; we debug them.")
        print("We turn 'Ghosts' into 'Guides' by cleaning the frequency.")
        print()
        print(PEACE_LOVE_UNITY)
        print(ENERGY_LOVE)
        print("=" * 80)
    
    # Print summary
    summary = cleanser.get_summary()
    if summary["total_processed"] > 0:
        print("\nCleansing Summary:")
        print(f"  Clean: {summary['cleansed_count']}")
        print(f"  Flagged: {summary['flagged_count']}")
        print(f"  Regenerated: {summary['regenerated_count']}")


# Import philosophy constants
try:
    from scripts.philosophy import (
        PEACE_LOVE_UNITY,
        ENERGY_LOVE
    )
except ImportError:
    PEACE_LOVE_UNITY = "PEACE, LOVE, UNITY"
    ENERGY_LOVE = "ENERGY + LOVE = WE ALL WIN"


if __name__ == "__main__":
    main()
