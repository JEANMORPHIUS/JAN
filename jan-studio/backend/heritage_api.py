"""
HERITAGE API
REST API endpoints for temporal heritage archive

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional, List, Dict
from pydantic import BaseModel
from datetime import datetime
from pathlib import Path

from temporal_heritage_registry import (
    get_sites_by_timeline, get_chronology_by_year, get_temporal_patterns,
    register_heritage_site, add_heritage_narrative,
    TimelineDimension, TimePeriod, get_temporal_heritage_db
)
from api_error_handler import heritage_api_error_handler
import logging
import sys

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/heritage", tags=["heritage"])


class HeritageSiteCreate(BaseModel):
    site_name: str
    site_type: str
    region: str
    country: Optional[str] = None
    coordinates_lat: Optional[float] = None
    coordinates_lon: Optional[float] = None
    timeline_dimension: str = TimelineDimension.PRIMARY.value
    time_period: str = TimePeriod.MODERN.value
    year_established: Optional[int] = None
    year_abandoned: Optional[int] = None
    current_status: str = "unknown"
    narrative_content: Optional[str] = None


@router.get("/timeline/{dimension}")
@heritage_api_error_handler
async def get_timeline_sites(
    dimension: str,
    period: Optional[str] = Query(None, description="Time period filter"),
    limit: int = Query(100, ge=1, le=1000, description="Results per page"),
    offset: int = Query(0, ge=0, description="Results offset")
):
    """
    Get heritage sites for a timeline dimension with pagination.
    
    Performance: Prevents loading entire dataset into memory.
    Honors Law 37: Finish What You Begin - complete pagination support.
    """
    with get_temporal_heritage_db() as conn:
        cursor = conn.cursor()
        
        # Build query with filters
        query = "SELECT * FROM heritage_sites WHERE timeline_dimension = ?"
        params = [dimension]
        
        if period:
            query += " AND time_period = ?"
            params.append(period)
        
        # Count total (for pagination metadata)
        count_query = query.replace("SELECT *", "SELECT COUNT(*)")
        cursor.execute(count_query, params)
        total_count = cursor.fetchone()[0]
        
        # Get paginated results
        query += " ORDER BY year_established DESC LIMIT ? OFFSET ?"
        params.extend([limit, offset])
        cursor.execute(query, params)
        sites = [dict(row) for row in cursor.fetchall()]
        
        return {
            "timeline_dimension": dimension,
            "time_period": period,
            "sites": sites,
            "count": len(sites),
            "total_count": total_count,
            "limit": limit,
            "offset": offset,
            "has_more": (offset + len(sites)) < total_count
        }


@router.get("/chronology")
@heritage_api_error_handler
async def get_chronology(
    start_year: int = Query(..., description="Start year"),
    end_year: int = Query(..., description="End year"),
    dimension: Optional[str] = Query(None, description="Timeline dimension filter")
):
    """Get heritage events within a year range."""
    events = get_chronology_by_year(start_year, end_year, dimension)
    return {"start_year": start_year, "end_year": end_year, "events": events, "count": len(events)}


@router.get("/patterns")
@heritage_api_error_handler
async def get_patterns():
    """Get all detected temporal patterns."""
    patterns = get_temporal_patterns()
    return {"patterns": patterns, "count": len(patterns)}


@router.get("/site/{site_id}")
@heritage_api_error_handler
async def get_site_details(site_id: int):
    """
    Get complete site details with narratives in single optimized query.
    
    Performance: Eliminates N+1 query pattern using LEFT JOIN.
    Honors Law 37: Finish What You Begin - complete data in one transaction.
    """
    with get_temporal_heritage_db() as conn:
        cursor = conn.cursor()
        
        # Single query with LEFT JOIN to get site + narratives
        cursor.execute("""
            SELECT 
                hs.id as site_id,
                hs.site_name,
                hs.site_type,
                hs.region,
                hs.country,
                hs.coordinates_lat,
                hs.coordinates_lon,
                hs.timeline_dimension,
                hs.time_period,
                hs.year_established,
                hs.year_abandoned,
                hs.current_status,
                hs.law_41_compliant,
                hs.requires_cleansing,
                hs.magnetic_field_strength,
                hs.magnetic_declination,
                hs.magnetic_inclination,
                hs.magnetic_pole_alignment,
                hs.field_resonance_level,
                hs.polarity_state,
                hs.field_anomaly_detected,
                hs.field_anomaly_description,
                hs.field_space_resonance,
                hs.field_space_energy_level,
                hs.field_space_philosophy,
                hs.temporal_hash,
                hs.created_at,
                hs.updated_at,
                hn.id as narrative_id,
                hn.narrative_type,
                hn.narrative_content,
                hn.violation_type,
                hn.dark_energy_detected,
                hn.regeneration_applied,
                hn.narrative_hash,
                hn.recorded_at
            FROM heritage_sites hs
            LEFT JOIN heritage_narratives hn ON hs.id = hn.site_id
            WHERE hs.id = ?
            ORDER BY hn.recorded_at DESC
        """, (site_id,))
        
        rows = cursor.fetchall()
        if not rows:
            raise HTTPException(status_code=404, detail="Site not found")
        
        # Build site dict from first row (all rows have same site data)
        first_row = rows[0]
        site = {
            'id': first_row['site_id'],
            'site_name': first_row['site_name'],
            'site_type': first_row['site_type'],
            'region': first_row['region'],
            'country': first_row['country'],
            'coordinates_lat': first_row['coordinates_lat'],
            'coordinates_lon': first_row['coordinates_lon'],
            'timeline_dimension': first_row['timeline_dimension'],
            'time_period': first_row['time_period'],
            'year_established': first_row['year_established'],
            'year_abandoned': first_row['year_abandoned'],
            'current_status': first_row['current_status'],
            'law_41_compliant': bool(first_row['law_41_compliant']),
            'requires_cleansing': bool(first_row['requires_cleansing']),
            'magnetic_field_strength': first_row['magnetic_field_strength'],
            'magnetic_declination': first_row['magnetic_declination'],
            'magnetic_inclination': first_row['magnetic_inclination'],
            'magnetic_pole_alignment': first_row['magnetic_pole_alignment'],
            'field_resonance_level': first_row['field_resonance_level'],
            'polarity_state': first_row['polarity_state'],
            'field_anomaly_detected': bool(first_row['field_anomaly_detected']),
            'field_anomaly_description': first_row['field_anomaly_description'],
            'field_space_resonance': first_row['field_space_resonance'],
            'field_space_energy_level': first_row['field_space_energy_level'],
            'field_space_philosophy': first_row['field_space_philosophy'],
            'temporal_hash': first_row['temporal_hash'],
            'created_at': first_row['created_at'],
            'updated_at': first_row['updated_at']
        }
        
        # Build narratives list (exclude rows where narrative_id is None)
        narratives = []
        for row in rows:
            if row['narrative_id'] is not None:
                narratives.append({
                    'id': row['narrative_id'],
                    'narrative_type': row['narrative_type'],
                    'narrative_content': row['narrative_content'],
                    'violation_type': row['violation_type'],
                    'dark_energy_detected': bool(row['dark_energy_detected']),
                    'regeneration_applied': bool(row['regeneration_applied']),
                    'narrative_hash': row['narrative_hash'],
                    'recorded_at': row['recorded_at']
                })
        
        return {
            "site": site,
            "narratives": narratives,
            "narrative_count": len(narratives)
        }


@router.post("/site")
@heritage_api_error_handler
async def create_heritage_site(site_data: HeritageSiteCreate):
    """Register a new heritage site."""
    # Validate coordinates if provided
    if site_data.coordinates_lat is not None:
        if not -90 <= site_data.coordinates_lat <= 90:
            raise ValueError(f"Latitude must be between -90 and 90, got {site_data.coordinates_lat}")
    if site_data.coordinates_lon is not None:
        if not -180 <= site_data.coordinates_lon <= 180:
            raise ValueError(f"Longitude must be between -180 and 180, got {site_data.coordinates_lon}")
    
    site_id = register_heritage_site(
        site_name=site_data.site_name,
        site_type=site_data.site_type,
        region=site_data.region,
        country=site_data.country,
        coordinates_lat=site_data.coordinates_lat,
        coordinates_lon=site_data.coordinates_lon,
        timeline_dimension=site_data.timeline_dimension,
        time_period=site_data.time_period,
        year_established=site_data.year_established,
        year_abandoned=site_data.year_abandoned,
        current_status=site_data.current_status
    )
    
    # If narrative provided, archive it
    if site_data.narrative_content:
        add_heritage_narrative(
            site_id=site_id,
            narrative_content=site_data.narrative_content,
            narrative_type="original",
            timeline_dimension=site_data.timeline_dimension
        )
    
    return {"site_id": site_id, "status": "created"}


@router.get("/search")
@heritage_api_error_handler
async def search_heritage(
    q: str = Query(..., description="Search query"),
    dimension: Optional[str] = Query(None, description="Timeline dimension filter"),
    period: Optional[str] = Query(None, description="Time period filter")
):
    """Search heritage sites by name, region, or type."""
    with get_temporal_heritage_db() as conn:
        cursor = conn.cursor()
        
        query = """
            SELECT * FROM heritage_sites
            WHERE (site_name LIKE ? OR region LIKE ? OR site_type LIKE ?)
        """
        params = [f"%{q}%", f"%{q}%", f"%{q}%"]
        
        if dimension:
            query += " AND timeline_dimension = ?"
            params.append(dimension)
        
        if period:
            query += " AND time_period = ?"
            params.append(period)
        
        query += " ORDER BY site_name"
        
        cursor.execute(query, params)
        sites = [dict(row) for row in cursor.fetchall()]
        
        return {"query": q, "sites": sites, "count": len(sites)}


@router.get("/stats")
@heritage_api_error_handler
async def get_heritage_stats():
    """Get statistics about the heritage archive."""
    with get_temporal_heritage_db() as conn:
        cursor = conn.cursor()
        
        # Total sites
        cursor.execute("SELECT COUNT(*) FROM heritage_sites")
        total_sites = cursor.fetchone()[0]
        
        # Sites by timeline
        cursor.execute("""
            SELECT timeline_dimension, COUNT(*) as count
            FROM heritage_sites
            GROUP BY timeline_dimension
        """)
        by_timeline = {row[0]: row[1] for row in cursor.fetchall()}
        
        # Sites by period
        cursor.execute("""
            SELECT time_period, COUNT(*) as count
            FROM heritage_sites
            GROUP BY time_period
        """)
        by_period = {row[0]: row[1] for row in cursor.fetchall()}
        
        # Law 41 compliance
        cursor.execute("SELECT COUNT(*) FROM heritage_sites WHERE law_41_compliant = 1")
        compliant = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM heritage_sites WHERE requires_cleansing = 1")
        requires_cleansing = cursor.fetchone()[0]
        
        # Total narratives
        cursor.execute("SELECT COUNT(*) FROM heritage_narratives")
        total_narratives = cursor.fetchone()[0]
        
        return {
            "total_sites": total_sites,
            "by_timeline": by_timeline,
            "by_period": by_period,
            "law_41_compliant": compliant,
            "requires_cleansing": requires_cleansing,
            "total_narratives": total_narratives,
            "timestamp": datetime.now().isoformat()
        }


@router.post("/cleanse")
@heritage_api_error_handler
async def cleanse_narrative(narrative: str, context: Optional[Dict] = None):
    """
    Public API: Cleanse any narrative through Law 41 (Heritage focus).

    For all humanity - anyone can cleanse their story, memory, or content.
    Strips away Dark Energy. Reveals the Seed.

    Note: For comprehensive dark energy detection across ALL life aspects,
    use /care-package endpoint.
    """
    try:
        sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))
        from heritage_cleansing import HeritageCleanser

        cleanser = HeritageCleanser(timeline_dimension=TimelineDimension.PRIMARY.value)

        cleansed, analysis = cleanser.cleanse_content(
            content=narrative,
            source=context.get("source", "Visitor Content") if context else "Visitor Content",
            site_type=context.get("site_type", "Heritage Property") if context else "Heritage Property",
            region=context.get("region") if context else None,
            country=context.get("country") if context else None,
            time_period=TimePeriod.MODERN.value
        )

        return {
            "status": "cleansed",
            "original": narrative,
            "cleansed": cleansed,
            "analysis": analysis,
            "sanctuary_message": "Your content has been cleansed through Law 41. Dark Energy filtered. Seed revealed."
        }
    except Exception as e:
        logger.error(f"Error cleansing narrative: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error cleansing narrative: {str(e)}")


@router.post("/care-package")
@heritage_api_error_handler
async def care_package_cleanse(
    narrative: str,
    life_aspect: Optional[str] = None,
    context: Optional[Dict] = None
):
    """
    CARE PACKAGE: Comprehensive Dark Energy Detection & Regeneration.

    Detects and cleanses Dark Energy across ALL life aspects:
    - Heritage & Historical
    - Health & Medical
    - Relationship & Connection
    - Financial & Abundance
    - Career & Purpose
    - Identity & Self-Concept
    - Family & Ancestral
    - Spiritual & Faith
    - Digital & Social Media
    - Body & Physical
    - News & Media Consumption
    - Education & Learning
    - Political & Community
    - Environmental & Nature
    - Crisis & Trauma

    For ALL Humanity. Nobody needs anyone. We help everyone help themselves.

    Request body:
    {
        "narrative": "Your narrative/story/content to cleanse",
        "life_aspect": "health|relationship|financial|etc (optional)",
        "context": {
            "source": "Optional source identifier",
            "user_id": "Optional user ID for tracking"
        }
    }

    Returns:
    {
        "status": "cleansed",
        "dark_energy_detected": true/false,
        "categories_found": ["category1", "category2"],
        "severity_score": 0.75,
        "law_41_compliant": false,
        "regenerated_narrative": "Cleansed narrative with Seed revealed",
        "original_narrative": "Your original input",
        "care_package_message": "Your narrative has been cleansed..."
    }
    """
    try:
        sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))
        from care_package_framework import CarePackageFramework

        # Initialize CARE Package
        care = CarePackageFramework()

        # Start session
        user_id = context.get("user_id", "anonymous") if context else "anonymous"
        session = care.start_session(user_id=user_id)

        # Detect dark energy
        detection = care.detect_dark_energy(
            content=narrative,
            source=context.get("source", "API Request") if context else "API Request",
            life_aspect=life_aspect
        )

        # Regenerate if needed
        regenerated_narrative = None
        if detection.regeneration_required:
            regenerated_narrative = care.regenerate_narrative(detection)

        # Complete session
        session_report = care.complete_session()

        return {
            "status": "analyzed",
            "dark_energy_detected": detection.dark_energy_detected,
            "categories_found": detection.categories_detected,
            "patterns_found": detection.patterns_found,
            "severity_score": detection.severity_score,
            "law_41_compliant": detection.law_41_compliant,
            "violation_type": detection.violation_type,
            "regeneration_required": detection.regeneration_required,
            "regenerated_narrative": regenerated_narrative,
            "original_narrative": narrative,
            "session_summary": session_report,
            "care_package_message": (
                "Your narrative has been analyzed through the CARE Package. "
                f"{'Dark Energy detected and cleansed. Seed revealed.' if detection.regeneration_required else 'No Dark Energy detected. Your narrative radiates clean energy.'}"
            ),
            "sanctuary_access": "The Sanctuary is open. All humanity is welcome.",
            "sovereignty_reminder": "Nobody needs anyone. We help everyone help themselves. You are sovereign."
        }
    except Exception as e:
        logger.error(f"Error in CARE Package analysis: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error in CARE Package: {str(e)}")


@router.get("/sanctuary/status")
@heritage_api_error_handler
async def get_sanctuary_status():
    """
    Get Sanctuary status for all humanity.

    Public API showing the Sanctuary is open and accessible.
    Includes CARE Package availability for comprehensive dark energy cleansing.
    """
    try:
        sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))
        from grid_sync_analysis import analyze_grid_sync
        from care_package_framework import CarePackageFramework

        # Get Grid status
        grid_analysis = analyze_grid_sync()
        grid_stability = grid_analysis.get("grid_metrics", {}).get("grid_stability", 0.387)
        avg_resonance = 0.78  # Default high resonance

        # Try to get average field resonance from grid metrics
        try:
            pillars = grid_analysis.get("pillars", [])
            if pillars:
                resonances = [p.get("field_resonance", 0.0) for p in pillars]
                avg_resonance = sum(resonances) / len(resonances) if resonances else 0.78
        except Exception:
            pass

        # Get CARE Package stats
        care = CarePackageFramework()
        care_stats = care.get_statistics()

        return {
            "sanctuary_status": "OPEN",
            "grid_stability": grid_stability,
            "field_resonance": avg_resonance,
            "message": "The Sanctuary is open. All humanity is welcome.",

            "care_package": {
                "status": "ACTIVE",
                "description": "Comprehensive Dark Energy Detection & Regeneration",
                "total_narratives_cleansed": care_stats.get("total_narratives_cleansed", 0),
                "life_aspects_covered": 16,
                "categories": [
                    "Heritage & Historical",
                    "Health & Medical",
                    "Relationship & Connection",
                    "Financial & Abundance",
                    "Career & Purpose",
                    "Identity & Self-Concept",
                    "Family & Ancestral",
                    "Spiritual & Faith",
                    "Digital & Social Media",
                    "Body & Physical",
                    "News & Media Consumption",
                    "Education & Learning",
                    "Political & Community",
                    "Environmental & Nature",
                    "Age & Limitation",
                    "Crisis & Trauma"
                ],
                "philosophy": "Nobody needs anyone. We help everyone help themselves.",
                "endpoint": "/api/heritage/care-package"
            },

            "access_points": [
                "CARE Package - Comprehensive dark energy cleansing across ALL life aspects",
                "Heritage Cleansing Protocol - Cleanses heritage/historical narratives through Law 41",
                "Life Audit Framework - Reverse-engineer your own timeline",
                "Health Tracking - Universal health condition tracking & empowerment",
                "Global Grid Resonance - Connect with the 7 pillars",
                "Field Space Analysis - Find your 'Everything In Between'",
                "Temporal Archive - Access heritage across all timelines",
                "REST API - Programmatic access for all",
                "Export Channels - All formats available (JSON, CSV, Markdown, HTML, GeoJSON)"
            ],

            "principles": {
                "sovereignty": "We are all Gods. You are sovereign.",
                "empowerment": "Nobody needs anyone. We help everyone help themselves.",
                "stewardship": "This is stewardship and community with the right spirits.",
                "love": "Love is the highest mastery.",
                "unity": "Energy + Love = We All Win",
                "motto": "Peace, Love, Unity"
            },

            "for_everyone": True,
            "free_access": True,
            "no_gatekeepers": True,
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        logger.error(f"Error getting sanctuary status: {e}", exc_info=True)
        return {
            "sanctuary_status": "OPEN",
            "message": "The Sanctuary is open. All humanity is welcome.",
            "care_package_status": "ACTIVE",
            "error": str(e)
        }
