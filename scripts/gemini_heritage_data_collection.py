"""GEMINI HERITAGE DATA COLLECTION
Prepare Gemini for heritage site data import and collection

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

This script prepares Gemini for collecting heritage site data including:
- Site metadata
- Historical narratives
- Magnetic field data
- Deep research and philosophy

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
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime

# Import Gemini and heritage system
try:
    sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))
    from gemini_assistant import generate_content
    from temporal_heritage_registry import (
        register_heritage_site, add_heritage_narrative,
        TimelineDimension, TimePeriod
    )
    from heritage_cleansing import HeritageCleanser
    from magnetic_field_research import research_heritage_site_magnetic_field, update_site_magnetic_field
    GEMINI_HERITAGE_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Could not import required modules: {e}")
    GEMINI_HERITAGE_AVAILABLE = False


def prepare_gemini_for_heritage_collection() -> str:
    """
    Prepare Gemini with context for heritage site data collection.
    
    Returns the prepared context prompt.
    """
    context = """
HERITAGE SITE DATA COLLECTION PROTOCOL

You are collecting data for the Temporal Heritage Archive - a system that chronologizes
all heritage sites throughout all of time across all dimensional timelines for debugging
historical patterns.

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN

DATA COLLECTION REQUIREMENTS:

1. SITE METADATA:
   - site_name: Name of heritage site
   - site_type: Type (Hotel, Palace, Castle, Temple, etc.)
   - region: Region/State
   - country: Country
   - coordinates_lat: Latitude (if available)
   - coordinates_lon: Longitude (if available)
   - time_period: ancient, medieval, renaissance, enlightenment, industrial, modern, contemporary, future
   - year_established: Year established (if known)
   - year_abandoned: Year abandoned (if applicable)
   - current_status: abandoned, active, ruins, etc.

2. HISTORICAL NARRATIVE:
   - narrative_content: Original historical narrative about the site
   - source: Source of the narrative
   - Note: Narrative will be automatically cleansed through Law 41 (Respect the Abandoned)

3. MAGNETIC FIELD DATA (if available):
   - magnetic_field_strength: Field strength in nT (nanotesla)
   - magnetic_declination: Declination in degrees
   - magnetic_inclination: Inclination in degrees
   - Note: If not available, we can estimate or research

4. DEEP RESEARCH:
   - Research the site's history
   - Research magnetic field data (if available)
   - Research field space philosophy
   - Connect to symbiosis with Earth

OUTPUT FORMAT:
Provide data in JSON format with all available fields.
"""
    return context


def collect_heritage_site_data(
    site_query: str,
    include_magnetic_field: bool = True,
    timeline_dimension: str = TimelineDimension.PRIMARY.value if GEMINI_HERITAGE_AVAILABLE else "primary"
) -> Dict[str, Any]:
    """
    Use Gemini to collect heritage site data.
    
    Args:
        site_query: Query about the heritage site (name, location, etc.)
        include_magnetic_field: Whether to research magnetic field data
        timeline_dimension: Timeline dimension for the site
    
    Returns:
        Complete heritage site data dictionary
    """
    if not GEMINI_HERITAGE_AVAILABLE:
        return {"error": "Gemini heritage collection not available"}
    
    context = prepare_gemini_for_heritage_collection()
    
    prompt = f"""
Collect comprehensive data for this heritage site: {site_query}

Please provide:
1. Complete site metadata (name, type, region, country, coordinates, time period, years, status)
2. Historical narrative about the site (original narrative - will be cleansed automatically)
3. Source information for the data
4. Any available magnetic field data (field strength, declination, inclination)
5. Deep research notes about the site's connection to Earth and symbiosis

Format the response as JSON with these fields:
{{
    "site_name": "...",
    "site_type": "...",
    "region": "...",
    "country": "...",
    "coordinates_lat": ...,
    "coordinates_lon": ...,
    "time_period": "...",
    "year_established": ...,
    "year_abandoned": ...,
    "current_status": "...",
    "narrative_content": "...",
    "source": "...",
    "magnetic_field_strength": ...,
    "magnetic_declination": ...,
    "magnetic_inclination": ...,
    "research_notes": "..."
}}
"""
    
    try:
        response = generate_content(
            prompt=prompt,
            context=context,
            temperature=0.7,
            max_tokens=2000
        )
        
        # Try to parse JSON from response
        # Gemini might return JSON wrapped in markdown or text
        json_start = response.find('{')
        json_end = response.rfind('}') + 1
        
        if json_start >= 0 and json_end > json_start:
            json_str = response[json_start:json_end]
            data = json.loads(json_str)
        else:
            # If no JSON found, create structured data from text
            data = {
                "site_name": site_query,
                "narrative_content": response,
                "source": "Gemini Collection",
                "research_notes": response
            }
        
        # Add collection metadata
        data["collected_by"] = "Gemini"
        data["collection_timestamp"] = datetime.now().isoformat()
        data["timeline_dimension"] = timeline_dimension
        
        return data
        
    except Exception as e:
        return {"error": f"Error collecting data: {e}", "query": site_query}


def import_gemini_collected_data(
    collected_data: Dict[str, Any],
    auto_cleanse: bool = True,
    auto_research_magnetic: bool = True
) -> Dict[str, Any]:
    """
    Import Gemini-collected data into the heritage archive.
    
    Args:
        collected_data: Data collected by Gemini
        auto_cleanse: Whether to automatically cleanse narratives
        auto_research_magnetic: Whether to research magnetic field if not provided
    
    Returns:
        Import result with site_id and status
    """
    if not GEMINI_HERITAGE_AVAILABLE:
        return {"error": "Gemini heritage import not available"}
    
    try:
        # Register site
        site_id = register_heritage_site(
            site_name=collected_data.get("site_name", "Unknown"),
            site_type=collected_data.get("site_type", "Heritage Property"),
            region=collected_data.get("region", "Unknown"),
            country=collected_data.get("country"),
            coordinates_lat=collected_data.get("coordinates_lat"),
            coordinates_lon=collected_data.get("coordinates_lon"),
            timeline_dimension=collected_data.get("timeline_dimension", TimelineDimension.PRIMARY.value),
            time_period=collected_data.get("time_period", TimePeriod.MODERN.value),
            year_established=collected_data.get("year_established"),
            year_abandoned=collected_data.get("year_abandoned"),
            current_status=collected_data.get("current_status", "unknown")
        )
        
        # Archive narrative
        narrative_content = collected_data.get("narrative_content", "")
        if narrative_content:
            if auto_cleanse:
                # Cleanse narrative
                cleanser = HeritageCleanser(
                    timeline_dimension=collected_data.get("timeline_dimension", TimelineDimension.PRIMARY.value)
                )
                cleansed, analysis = cleanser.cleanse_content(
                    content=narrative_content,
                    source=collected_data.get("source", "Gemini Collection"),
                    site_type=collected_data.get("site_type", "Heritage Property"),
                    region=collected_data.get("region", "Unknown"),
                    country=collected_data.get("country"),
                    year_established=collected_data.get("year_established"),
                    year_abandoned=collected_data.get("year_abandoned"),
                    time_period=collected_data.get("time_period", TimePeriod.MODERN.value)
                )
                
                # Archive original
                add_heritage_narrative(
                    site_id=site_id,
                    narrative_content=narrative_content,
                    narrative_type="original",
                    timeline_dimension=collected_data.get("timeline_dimension", TimelineDimension.PRIMARY.value)
                )
                
                # Archive cleansed
                if analysis.get("regeneration_suggestion"):
                    add_heritage_narrative(
                        site_id=site_id,
                        narrative_content=cleansed,
                        narrative_type="regenerated",
                        timeline_dimension=collected_data.get("timeline_dimension", TimelineDimension.PRIMARY.value),
                        regeneration_applied=True
                    )
            else:
                # Archive without cleansing
                add_heritage_narrative(
                    site_id=site_id,
                    narrative_content=narrative_content,
                    narrative_type="original",
                    timeline_dimension=collected_data.get("timeline_dimension", TimelineDimension.PRIMARY.value)
                )
        
        # Research magnetic field
        if auto_research_magnetic:
            field_strength = collected_data.get("magnetic_field_strength")
            declination = collected_data.get("magnetic_declination")
            inclination = collected_data.get("magnetic_inclination")
            
            # If magnetic data provided, research it
            if field_strength and declination is not None and inclination is not None:
                magnetic_research = research_heritage_site_magnetic_field(
                    site_id, field_strength, declination, inclination
                )
                update_site_magnetic_field(site_id, magnetic_research)
        
        return {
            "site_id": site_id,
            "status": "imported",
            "auto_cleansed": auto_cleanse,
            "magnetic_researched": auto_research_magnetic
        }
        
    except Exception as e:
        return {"error": f"Error importing data: {e}"}


def collect_and_import_heritage_site(
    site_query: str,
    auto_cleanse: bool = True,
    auto_research_magnetic: bool = True,
    timeline_dimension: str = TimelineDimension.PRIMARY.value if GEMINI_HERITAGE_AVAILABLE else "primary"
) -> Dict[str, Any]:
    """
    Complete workflow: Collect data with Gemini and import into archive.
    
    Args:
        site_query: Query about the heritage site
        auto_cleanse: Whether to automatically cleanse narratives
        auto_research_magnetic: Whether to research magnetic field
        timeline_dimension: Timeline dimension for the site
    
    Returns:
        Complete result with collection and import status
    """
    print(f"Collecting data for: {site_query}")
    collected_data = collect_heritage_site_data(
        site_query, include_magnetic_field=auto_research_magnetic, timeline_dimension=timeline_dimension
    )
    
    if "error" in collected_data:
        return collected_data
    
    print(f"Importing data into archive...")
    import_result = import_gemini_collected_data(
        collected_data, auto_cleanse=auto_cleanse, auto_research_magnetic=auto_research_magnetic
    )
    
    return {
        "collection": collected_data,
        "import": import_result,
        "status": "complete" if "error" not in import_result else "error"
    }


def main():
    """Main execution for Gemini heritage data collection."""
    if not GEMINI_HERITAGE_AVAILABLE:
        print("Error: Gemini heritage collection not available. Check imports and API key.")
        return
    
    print("=" * 80)
    print("GEMINI HERITAGE DATA COLLECTION")
    print("Poles and Everything In Between")
    print("=" * 80)
    print()
    print("This script uses Gemini to collect heritage site data including:")
    print("  - Site metadata")
    print("  - Historical narratives")
    print("  - Magnetic field data")
    print("  - Deep research and philosophy")
    print()
    print("Usage:")
    print("  python gemini_heritage_data_collection.py <site_query>")
    print()
    print("Example:")
    print("  python gemini_heritage_data_collection.py 'Berengaria Hotel Cyprus'")
    print()
    
    import sys
    if len(sys.argv) > 1:
        site_query = " ".join(sys.argv[1:])
        result = collect_and_import_heritage_site(site_query)
        print("\nCollection and Import Result:")
        print(json.dumps(result, indent=2, default=str))


if __name__ == "__main__":
    main()
