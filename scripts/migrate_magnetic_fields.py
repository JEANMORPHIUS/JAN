"""
MIGRATE MAGNETIC FIELDS
Add magnetic field columns to existing heritage_sites table

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity
"""

import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    Path, setup_logging, standard_main
)

import sys
from pathlib import Path

try:
    sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))
    from temporal_heritage_registry import get_temporal_heritage_db
    MIGRATION_AVAILABLE = True
except ImportError:
    print("Error: Could not import temporal_heritage_registry")
    MIGRATION_AVAILABLE = False


def migrate_magnetic_fields():
    """Add magnetic field columns to existing heritage_sites table."""
    if not MIGRATION_AVAILABLE:
        return False
    
    try:
        with get_temporal_heritage_db() as conn:
            cursor = conn.cursor()
            
            # Check if columns already exist
            cursor.execute("PRAGMA table_info(heritage_sites)")
            existing_columns = [row[1] for row in cursor.fetchall()]
            
            # Add magnetic field columns if they don't exist
            if 'magnetic_field_strength' not in existing_columns:
                print("Adding magnetic field columns...")
                cursor.execute("""
                    ALTER TABLE heritage_sites
                    ADD COLUMN magnetic_field_strength REAL
                """)
                cursor.execute("""
                    ALTER TABLE heritage_sites
                    ADD COLUMN magnetic_declination REAL
                """)
                cursor.execute("""
                    ALTER TABLE heritage_sites
                    ADD COLUMN magnetic_inclination REAL
                """)
                cursor.execute("""
                    ALTER TABLE heritage_sites
                    ADD COLUMN magnetic_pole_alignment TEXT
                """)
                cursor.execute("""
                    ALTER TABLE heritage_sites
                    ADD COLUMN field_resonance_level REAL
                """)
                cursor.execute("""
                    ALTER TABLE heritage_sites
                    ADD COLUMN polarity_state TEXT
                """)
                cursor.execute("""
                    ALTER TABLE heritage_sites
                    ADD COLUMN field_anomaly_detected BOOLEAN DEFAULT FALSE
                """)
                cursor.execute("""
                    ALTER TABLE heritage_sites
                    ADD COLUMN field_anomaly_description TEXT
                """)
                cursor.execute("""
                    ALTER TABLE heritage_sites
                    ADD COLUMN field_space_resonance REAL
                """)
                cursor.execute("""
                    ALTER TABLE heritage_sites
                    ADD COLUMN field_space_energy_level REAL
                """)
                cursor.execute("""
                    ALTER TABLE heritage_sites
                    ADD COLUMN field_space_philosophy TEXT
                """)
                    conn.commit()
                print("[OK] Magnetic field columns added successfully")
                return True
            else:
                print("[OK] Magnetic field columns already exist")
                return True
                
    except Exception as e:
        print(f"[ERROR] Migration error: {e}")
        return False


if __name__ == "__main__":
    print("=" * 80)
    print("MIGRATE MAGNETIC FIELDS")
    print("=" * 80)
    print()
    migrate_magnetic_fields()
