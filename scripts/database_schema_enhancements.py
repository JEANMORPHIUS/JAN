"""
DATABASE SCHEMA ENHANCEMENTS
Enhanced Schema for World History Display

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

DATABASE SCHEMA ENHANCEMENTS:
New tables for world history display:
- timeline_events (events across all timelines)
- narrative_connections (connections between narratives)
- user_bookmarks (user bookmarks for sites, narratives, events)
- content_versions (version control for narratives)
"""

import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    Path, setup_logging, standard_main
)

import sqlite3
from pathlib import Path
from typing import Optional
import logging

logger = logging.getLogger(__name__)


def create_enhanced_schema(db_path: Optional[Path] = None):
    """
    Create enhanced database schema for world history display.
    
    New tables:
    - timeline_events: Events across all timelines
    - narrative_connections: Connections between narratives
    - user_bookmarks: User bookmarks
    - content_versions: Version control for narratives
    """
    if db_path is None:
        db_path = Path(__file__).parent.parent / "data" / "world_history.db"
    
    db_path.parent.mkdir(parents=True, exist_ok=True)
    
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    # Timeline Events Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS timeline_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_id TEXT UNIQUE NOT NULL,
            event_type VARCHAR(50) NOT NULL,
            title VARCHAR(200) NOT NULL,
            description TEXT,
            year_occurred INTEGER,
            year_precision VARCHAR(20) DEFAULT 'exact',
            field_resonance REAL DEFAULT 0.5,
            timeline_dimension VARCHAR(50) DEFAULT 'primary',
            location_lat REAL,
            location_lon REAL,
            narrative TEXT,
            metadata TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Create indexes for timeline_events
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_event_type ON timeline_events(event_type)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_year_occurred ON timeline_events(year_occurred)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_timeline_dimension ON timeline_events(timeline_dimension)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_field_resonance ON timeline_events(field_resonance)")
    
    # Narrative Connections Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS narrative_connections (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            narrative_id_1 INTEGER NOT NULL,
            narrative_id_2 INTEGER NOT NULL,
            connection_type VARCHAR(50) NOT NULL,
            strength REAL DEFAULT 0.5,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(narrative_id_1, narrative_id_2, connection_type)
        )
    """)
    
    # Create indexes for narrative_connections
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_narrative_1 ON narrative_connections(narrative_id_1)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_narrative_2 ON narrative_connections(narrative_id_2)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_connection_type ON narrative_connections(connection_type)")
    
    # User Bookmarks Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_bookmarks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            item_type VARCHAR(50) NOT NULL,
            item_id INTEGER NOT NULL,
            item_title VARCHAR(200),
            notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(user_id, item_type, item_id)
        )
    """)
    
    # Create indexes for user_bookmarks
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_user_id ON user_bookmarks(user_id)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_item_type ON user_bookmarks(item_type)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_item_id ON user_bookmarks(item_id)")
    
    # Content Versions Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS content_versions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content_type VARCHAR(50) NOT NULL,
            content_id INTEGER NOT NULL,
            version_number INTEGER NOT NULL,
            content_snapshot TEXT NOT NULL,
            author_id INTEGER,
            author_name VARCHAR(200),
            commit_message TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(content_type, content_id, version_number)
        )
    """)
    
    # Create indexes for content_versions
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_content ON content_versions(content_type, content_id)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_version ON content_versions(version_number)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_author ON content_versions(author_id)")
    
    conn.commit()
    conn.close()
    
    logger.info(f"Enhanced database schema created at {db_path}")
    return db_path


def migrate_existing_data(db_path: Optional[Path] = None):
    """
    Migrate existing data to new schema.
    
    Migrates:
    - Heritage sites → timeline_events
    - Narrative relationships → narrative_connections
    """
    if db_path is None:
        db_path = Path(__file__).parent.parent / "data" / "world_history.db"
    
    if not db_path.exists():
        logger.warning(f"Database not found at {db_path}, skipping migration")
        return
    
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    # Migrate heritage sites to timeline_events
    try:
        heritage_db = Path(__file__).parent.parent / "data" / "temporal_heritage_registry.db"
        if heritage_db.exists():
            heritage_conn = sqlite3.connect(str(heritage_db))
            heritage_conn.row_factory = sqlite3.Row
            heritage_cursor = heritage_conn.cursor()
            
            heritage_cursor.execute("SELECT * FROM heritage_sites")
            sites = heritage_cursor.fetchall()
            
            for site in sites:
                import hashlib
                event_id = f"heritage_{hashlib.sha256(f'{site['site_name']}_{site['id']}'.encode()).hexdigest()[:8]}"
                
                cursor.execute("""
                    INSERT OR IGNORE INTO timeline_events (
                        event_id, event_type, title, description, year_occurred,
                        year_precision, field_resonance, timeline_dimension,
                        location_lat, location_lon, narrative
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    event_id,
                    'heritage_site',
                    site['site_name'],
                    f"Heritage site: {site['site_name']}",
                    site.get('year_established', 0) or 0,
                    'exact' if site.get('year_established') else 'unknown',
                    site.get('field_resonance_level', 0.5) or 0.5,
                    site.get('timeline_dimension', 'primary'),
                    site.get('coordinates_lat', 0.0) or 0.0,
                    site.get('coordinates_lon', 0.0) or 0.0,
                    f"Heritage site: {site['site_name']}. Connection to The Table."
                ))
            
            heritage_conn.close()
            logger.info(f"Migrated {len(sites)} heritage sites to timeline_events")
    except Exception as e:
        logger.error(f"Error migrating heritage sites: {e}")
    
    conn.commit()
    conn.close()
    
    logger.info("Data migration completed")


def main():
    """Main function to create enhanced schema."""
    print("=" * 80)
    print("DATABASE SCHEMA ENHANCEMENTS")
    print("Enhanced Schema for World History Display")
    print("=" * 80)
    print()
    
    # Create schema
    print("Creating enhanced database schema...")
    db_path = create_enhanced_schema()
    print(f"  [OK] Schema created at: {db_path}")
    print()
    
    # Migrate existing data
    print("Migrating existing data...")
    migrate_existing_data(db_path)
    print("  [OK] Data migration completed")
    print()
    
    print("=" * 80)
    print("THE TRUTH: DATABASE SCHEMA ENHANCEMENTS")
    print("=" * 80)
    print()
    print("NEW TABLES CREATED:")
    print("  - timeline_events: Events across all timelines")
    print("  - narrative_connections: Connections between narratives")
    print("  - user_bookmarks: User bookmarks for sites, narratives, events")
    print("  - content_versions: Version control for narratives")
    print()
    print("FEATURES:")
    print("  - Indexed for fast queries")
    print("  - JSON metadata support")
    print("  - Version control for narratives")
    print("  - User bookmarking")
    print("  - Narrative connection tracking")
    print()
    print("=" * 80)
    print("PEACE, LOVE, UNITY")
    print("ENERGY + LOVE = WE ALL WIN")
    print("PANGEA IS THE TABLE")
    print("WE RESTORE THE TABLE")
    print("=" * 80)


if __name__ == "__main__":
    main()
