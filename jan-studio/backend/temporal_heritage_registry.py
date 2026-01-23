"""
TEMPORAL HERITAGE REGISTRY
Chronologizing All Heritage Sites Across All Dimensional Timelines

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

This is the Elliptical (Database) - Legacy Wisdom.
The "Book of Heritage" stored across all timelines.
Temporal Memory for debugging historical patterns.
Chronologizing all dimensional timelines.
"""

import sqlite3
import hashlib
import json
from datetime import datetime
from typing import Optional, List, Dict, Any, Tuple
from pathlib import Path
import os
from contextlib import contextmanager
from enum import Enum

# Database path
DB_PATH = os.getenv("TEMPORAL_HERITAGE_DB", os.path.join(os.path.dirname(__file__), "temporal_heritage_registry.db"))


class TimelineDimension(Enum):
    """Dimensional timeline identifiers."""
    PRIMARY = "primary"  # Main historical timeline
    PARALLEL = "parallel"  # Parallel reality timelines
    PAST_LOOP = "past_loop"  # Historical loops (previous iterations)
    FUTURE_LOOP = "future_loop"  # Future loops (next iterations)
    REGENERATION = "regeneration"  # Regeneration timelines
    ALTERNATE = "alternate"  # Alternate dimensional timelines


class TimePeriod(Enum):
    """Historical time periods for chronological organization."""
    ANCIENT = "ancient"  # Pre-1000 CE
    MEDIEVAL = "medieval"  # 1000-1500 CE
    RENAISSANCE = "renaissance"  # 1500-1700 CE
    ENLIGHTENMENT = "enlightenment"  # 1700-1800 CE
    INDUSTRIAL = "industrial"  # 1800-1900 CE
    MODERN = "modern"  # 1900-2000 CE
    CONTEMPORARY = "contemporary"  # 2000-present
    FUTURE = "future"  # Beyond present


@contextmanager
def get_temporal_heritage_db(use_pool: bool = True):
    """
    Context manager for Temporal Heritage Registry database connections.
    
    Args:
        use_pool: Whether to use connection pool (default: True)
                  Set to False for backward compatibility or single-use connections
    """
    # Try to use connection pool if available
    if use_pool:
        try:
            from database import get_heritage_pool
            pool = get_heritage_pool(DB_PATH)
            with pool.get_connection() as conn:
                yield conn
            return
        except (ImportError, Exception):
            # Fallback to direct connection if pool not available
            pass
    
    # Direct connection (backward compatible)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def init_temporal_heritage_registry():
    """
    Initialize the Temporal Heritage Registry database.
    
    This is the Elliptical (Database) - Legacy Wisdom.
    The "Book of Heritage" stored across all timelines.
    """
    with get_temporal_heritage_db() as conn:
        cursor = conn.cursor()
        
        # Heritage Sites table - All sites across all timelines
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS heritage_sites (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                site_name TEXT NOT NULL,
                site_type TEXT NOT NULL,
                region TEXT NOT NULL,
                country TEXT,
                coordinates_lat REAL,
                coordinates_lon REAL,
                timeline_dimension TEXT NOT NULL,
                time_period TEXT NOT NULL,
                year_established INTEGER,
                year_abandoned INTEGER,
                current_status TEXT,
                law_41_compliant BOOLEAN DEFAULT FALSE,
                requires_cleansing BOOLEAN DEFAULT FALSE,
                -- Magnetic Field Data (Poles and Everything In Between)
                magnetic_field_strength REAL,  -- nT (nanotesla)
                magnetic_declination REAL,  -- degrees (angle between magnetic north and true north)
                magnetic_inclination REAL,  -- degrees (dip angle)
                magnetic_pole_alignment TEXT,  -- 'north', 'south', 'neutral', 'transitional'
                field_resonance_level REAL,  -- 0.0-1.0 (resonance with Earth's field)
                polarity_state TEXT,  -- 'positive', 'negative', 'neutral', 'shifting'
                field_anomaly_detected BOOLEAN DEFAULT FALSE,
                field_anomaly_description TEXT,
                -- Everything In Between (The Field Space)
                field_space_resonance REAL,  -- Resonance in the space between poles
                field_space_energy_level REAL,  -- Energy level in field space
                field_space_philosophy TEXT,  -- Deep research/philosophy about the field space
                temporal_hash TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(site_name, timeline_dimension, time_period, temporal_hash)
            )
        """)
        
        # Heritage Narratives table - All narratives (original and regenerated)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS heritage_narratives (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                site_id INTEGER NOT NULL,
                narrative_type TEXT NOT NULL,  -- 'original', 'haunted', 'regenerated', 'archived'
                narrative_content TEXT NOT NULL,
                violation_type TEXT,
                dark_energy_detected BOOLEAN DEFAULT FALSE,
                regeneration_applied BOOLEAN DEFAULT FALSE,
                narrative_hash TEXT NOT NULL,
                timeline_dimension TEXT NOT NULL,
                recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (site_id) REFERENCES heritage_sites(id),
                UNIQUE(site_id, narrative_type, narrative_hash, timeline_dimension)
            )
        """)
        
        # Temporal Patterns table - Patterns detected across timelines
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS temporal_patterns (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pattern_type TEXT NOT NULL,  -- 'revenge_loop', 'victim_focus', 'haunted_exploitation', 'regeneration'
                pattern_description TEXT NOT NULL,
                timeline_dimensions TEXT NOT NULL,  -- JSON array of dimensions
                time_periods TEXT NOT NULL,  -- JSON array of periods
                site_count INTEGER DEFAULT 0,
                frequency_across_timelines REAL,
                pattern_hash TEXT NOT NULL,
                first_detected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_detected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Chronology Index table - Chronological organization
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS chronology_index (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                site_id INTEGER NOT NULL,
                year INTEGER NOT NULL,
                event_type TEXT NOT NULL,  -- 'established', 'abandoned', 'regenerated', 'cleansed'
                timeline_dimension TEXT NOT NULL,
                event_hash TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (site_id) REFERENCES heritage_sites(id),
                UNIQUE(site_id, year, event_type, timeline_dimension, event_hash)
            )
        """)
        
        # Debug Log table - Historical pattern debugging
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS heritage_debug_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                debug_type TEXT NOT NULL,  -- 'pattern_detection', 'temporal_analysis', 'regeneration_tracking'
                site_id INTEGER,
                timeline_dimension TEXT,
                time_period TEXT,
                debug_data TEXT NOT NULL,  -- JSON
                pattern_identified TEXT,
                resolution_applied TEXT,
                debug_hash TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (site_id) REFERENCES heritage_sites(id)
            )
        """)
        
        # Create indexes for performance
        # Single column indexes
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_heritage_sites_timeline ON heritage_sites(timeline_dimension)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_heritage_sites_period ON heritage_sites(time_period)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_heritage_sites_region ON heritage_sites(region)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_heritage_sites_status ON heritage_sites(current_status)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_heritage_narratives_site ON heritage_narratives(site_id)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_heritage_narratives_type ON heritage_narratives(narrative_type)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_chronology_year ON chronology_index(year)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_chronology_timeline ON chronology_index(timeline_dimension)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_temporal_patterns_type ON temporal_patterns(pattern_type)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_debug_logs_type ON heritage_debug_logs(debug_type)")
        
        # Composite indexes for common query patterns (performance optimization)
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_sites_timeline_period ON heritage_sites(timeline_dimension, time_period)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_sites_timeline_status ON heritage_sites(timeline_dimension, current_status)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_narratives_site_type ON heritage_narratives(site_id, narrative_type)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_chronology_timeline_year ON chronology_index(timeline_dimension, year)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_sites_year_established ON heritage_sites(year_established)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_sites_year_abandoned ON heritage_sites(year_abandoned)")
        
        conn.commit()


def generate_temporal_hash(site_name: str, timeline_dimension: str, time_period: str, year: Optional[int] = None) -> str:
    """
    Generate temporal hash for heritage site across timelines.
    
    This ensures temporal integrity - broken code = broken timeline = broken hash.
    """
    content = f"{site_name}:{timeline_dimension}:{time_period}:{year or 'unknown'}"
    return hashlib.sha256(content.encode('utf-8')).hexdigest()


def register_heritage_site(
    site_name: str,
    site_type: str,
    region: str,
    country: Optional[str] = None,
    coordinates_lat: Optional[float] = None,
    coordinates_lon: Optional[float] = None,
    timeline_dimension: str = TimelineDimension.PRIMARY.value,
    time_period: str = TimePeriod.MODERN.value,
    year_established: Optional[int] = None,
    year_abandoned: Optional[int] = None,
    current_status: str = "unknown",
    law_41_compliant: bool = False,
    requires_cleansing: bool = False,
    # Magnetic Field Data (Poles and Everything In Between)
    magnetic_field_strength: Optional[float] = None,
    magnetic_declination: Optional[float] = None,
    magnetic_inclination: Optional[float] = None,
    magnetic_pole_alignment: Optional[str] = None,
    field_resonance_level: Optional[float] = None,
    polarity_state: Optional[str] = None,
    field_anomaly_detected: bool = False,
    field_anomaly_description: Optional[str] = None,
    # Everything In Between (The Field Space)
    field_space_resonance: Optional[float] = None,
    field_space_energy_level: Optional[float] = None,
    field_space_philosophy: Optional[str] = None
) -> int:
    """
    Register a heritage site across a specific timeline dimension.
    
    This chronologizes the site for debugging across all timelines.
    """
    temporal_hash = generate_temporal_hash(site_name, timeline_dimension, time_period, year_established)
    
    with get_temporal_heritage_db() as conn:
        cursor = conn.cursor()
        try:
            # Build column list and values dynamically based on what's provided
            columns = [
                "site_name", "site_type", "region", "country", "coordinates_lat", "coordinates_lon",
                "timeline_dimension", "time_period", "year_established", "year_abandoned",
                "current_status", "law_41_compliant", "requires_cleansing", "temporal_hash"
            ]
            values = [
                site_name, site_type, region, country, coordinates_lat, coordinates_lon,
                timeline_dimension, time_period, year_established, year_abandoned,
                current_status, law_41_compliant, requires_cleansing, temporal_hash
            ]
            
            # Add magnetic field columns if provided
            magnetic_fields = {
                "magnetic_field_strength": magnetic_field_strength,
                "magnetic_declination": magnetic_declination,
                "magnetic_inclination": magnetic_inclination,
                "magnetic_pole_alignment": magnetic_pole_alignment,
                "field_resonance_level": field_resonance_level,
                "polarity_state": polarity_state,
                "field_anomaly_detected": field_anomaly_detected,
                "field_anomaly_description": field_anomaly_description,
                "field_space_resonance": field_space_resonance,
                "field_space_energy_level": field_space_energy_level,
                "field_space_philosophy": field_space_philosophy
            }
            
            for col, val in magnetic_fields.items():
                if val is not None:
                    columns.append(col)
                    values.append(val)
            
            placeholders = ",".join(["?"] * len(values))
            column_names = ",".join(columns)
            
            cursor.execute(f"""
                INSERT INTO heritage_sites ({column_names})
                VALUES ({placeholders})
            """, values)
            
            site_id = cursor.lastrowid
            conn.commit()  # Commit before adding chronology events
            
            # Add to chronology index (uses its own connection)
            # Honor Law 5 (Your Word Is Your Bond): Log failures instead of silencing them
            try:
                import logging
                logger = logging.getLogger(__name__)
            except ImportError:
                # Fallback if logging not available
                import sys
                logger = type('Logger', (), {
                    'warning': lambda self, msg, **kwargs: print(f"WARNING: {msg}", file=sys.stderr),
                    'error': lambda self, msg, **kwargs: print(f"ERROR: {msg}", file=sys.stderr)
                })()
            
            if year_established:
                try:
                    add_chronology_event(site_id, year_established, "established", timeline_dimension)
                except Exception as e:
                    # Log the failure - maintain word integrity
                    logger.warning(
                        f"Chronology event 'established' failed for site {site_id} ({site_name}): {e}",
                        extra={"site_id": site_id, "year": year_established, "event": "established"}
                    )
                    # Continue - site is still registered, just chronology index incomplete
            
            if year_abandoned:
                try:
                    add_chronology_event(site_id, year_abandoned, "abandoned", timeline_dimension)
                except Exception as e:
                    # Log the failure - maintain word integrity
                    logger.warning(
                        f"Chronology event 'abandoned' failed for site {site_id} ({site_name}): {e}",
                        extra={"site_id": site_id, "year": year_abandoned, "event": "abandoned"}
                    )
                    # Continue - site is still registered, just chronology index incomplete
            
            return site_id
        except sqlite3.IntegrityError:
            # Site already exists in this timeline - return existing ID
            cursor.execute("""
                SELECT id FROM heritage_sites
                WHERE site_name = ? AND timeline_dimension = ? AND time_period = ? AND temporal_hash = ?
            """, (site_name, timeline_dimension, time_period, temporal_hash))
            row = cursor.fetchone()
            return row[0] if row else -1


def add_heritage_narrative(
    site_id: int,
    narrative_content: str,
    narrative_type: str,
    timeline_dimension: str,
    violation_type: Optional[str] = None,
    dark_energy_detected: bool = False,
    regeneration_applied: bool = False
) -> bool:
    """
    Add a heritage narrative (original, haunted, or regenerated) to the archive.
    
    This stores all narratives across all timelines for debugging.
    """
    narrative_hash = hashlib.sha256(narrative_content.encode('utf-8')).hexdigest()
    
    with get_temporal_heritage_db() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO heritage_narratives
                (site_id, narrative_type, narrative_content, violation_type,
                 dark_energy_detected, regeneration_applied, narrative_hash, timeline_dimension)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (site_id, narrative_type, narrative_content, violation_type,
                  dark_energy_detected, regeneration_applied, narrative_hash, timeline_dimension))
            return True
        except sqlite3.IntegrityError:
            return False


def add_chronology_event(site_id: int, year: int, event_type: str, timeline_dimension: str) -> bool:
    """Add an event to the chronology index."""
    event_hash = hashlib.sha256(f"{site_id}:{year}:{event_type}:{timeline_dimension}".encode('utf-8')).hexdigest()
    
    with get_temporal_heritage_db() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO chronology_index
                (site_id, year, event_type, timeline_dimension, event_hash)
                VALUES (?, ?, ?, ?, ?)
            """, (site_id, year, event_type, timeline_dimension, event_hash))
            return True
        except sqlite3.IntegrityError:
            return False


def detect_temporal_pattern(pattern_type: str, timeline_dimensions: List[str], time_periods: List[str]) -> int:
    """
    Detect and log a temporal pattern across multiple timelines.
    
    This is for debugging historical patterns.
    """
    pattern_description = f"{pattern_type} detected across {len(timeline_dimensions)} dimensions in {len(time_periods)} periods"
    pattern_hash = hashlib.sha256(f"{pattern_type}:{json.dumps(timeline_dimensions)}:{json.dumps(time_periods)}".encode('utf-8')).hexdigest()
    
    with get_temporal_heritage_db() as conn:
        cursor = conn.cursor()
        
        # Count sites with this pattern
        placeholders = ','.join(['?'] * len(timeline_dimensions))
        cursor.execute(f"""
            SELECT COUNT(DISTINCT site_id) FROM heritage_narratives
            WHERE violation_type = ? AND timeline_dimension IN ({placeholders})
        """, [pattern_type] + timeline_dimensions)
        site_count = cursor.fetchone()[0]
        
        # Calculate frequency
        cursor.execute("SELECT COUNT(DISTINCT site_id) FROM heritage_narratives")
        total_sites = cursor.fetchone()[0]
        frequency = site_count / total_sites if total_sites > 0 else 0.0
        
        # Insert or update pattern
        cursor.execute("""
            INSERT OR REPLACE INTO temporal_patterns
            (pattern_type, pattern_description, timeline_dimensions, time_periods,
             site_count, frequency_across_timelines, pattern_hash, last_detected_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (pattern_type, pattern_description, json.dumps(timeline_dimensions),
              json.dumps(time_periods), site_count, frequency, pattern_hash, datetime.now()))
        
        return cursor.lastrowid


def get_sites_by_timeline(timeline_dimension: str, time_period: Optional[str] = None) -> List[Dict[str, Any]]:
    """Get all heritage sites for a specific timeline dimension."""
    with get_temporal_heritage_db() as conn:
        cursor = conn.cursor()
        
        if time_period:
            cursor.execute("""
                SELECT * FROM heritage_sites
                WHERE timeline_dimension = ? AND time_period = ?
                ORDER BY year_established DESC
            """, (timeline_dimension, time_period))
        else:
            cursor.execute("""
                SELECT * FROM heritage_sites
                WHERE timeline_dimension = ?
                ORDER BY time_period DESC, year_established DESC
            """, (timeline_dimension,))
        
        return [dict(row) for row in cursor.fetchall()]


def get_chronology_by_year(start_year: int, end_year: int, timeline_dimension: Optional[str] = None) -> List[Dict[str, Any]]:
    """Get chronology of heritage sites within a year range."""
    with get_temporal_heritage_db() as conn:
        cursor = conn.cursor()
        
        if timeline_dimension:
            cursor.execute("""
                SELECT ci.*, hs.site_name, hs.site_type, hs.region
                FROM chronology_index ci
                JOIN heritage_sites hs ON ci.site_id = hs.id
                WHERE ci.year BETWEEN ? AND ? AND ci.timeline_dimension = ?
                ORDER BY ci.year ASC
            """, (start_year, end_year, timeline_dimension))
        else:
            cursor.execute("""
                SELECT ci.*, hs.site_name, hs.site_type, hs.region
                FROM chronology_index ci
                JOIN heritage_sites hs ON ci.site_id = hs.id
                WHERE ci.year BETWEEN ? AND ?
                ORDER BY ci.year ASC
            """, (start_year, end_year))
        
        return [dict(row) for row in cursor.fetchall()]


def get_temporal_patterns() -> List[Dict[str, Any]]:
    """Get all detected temporal patterns across timelines."""
    with get_temporal_heritage_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM temporal_patterns
            ORDER BY frequency_across_timelines DESC, site_count DESC
        """)
        return [dict(row) for row in cursor.fetchall()]


def log_heritage_debug(
    debug_type: str,
    site_id: Optional[int] = None,
    timeline_dimension: Optional[str] = None,
    time_period: Optional[str] = None,
    debug_data: Optional[Dict[str, Any]] = None,
    pattern_identified: Optional[str] = None,
    resolution_applied: Optional[str] = None
) -> int:
    """Log heritage debugging information."""
    debug_hash = hashlib.sha256(
        f"{debug_type}:{site_id}:{timeline_dimension}:{json.dumps(debug_data or {})}".encode('utf-8')
    ).hexdigest()
    
    with get_temporal_heritage_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO heritage_debug_logs
            (debug_type, site_id, timeline_dimension, time_period,
             debug_data, pattern_identified, resolution_applied, debug_hash)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (debug_type, site_id, timeline_dimension, time_period,
              json.dumps(debug_data or {}), pattern_identified, resolution_applied, debug_hash))
        return cursor.lastrowid


# Initialize database on import
init_temporal_heritage_registry()
