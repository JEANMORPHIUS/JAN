"""
Initialize All Databases
Sets up all database schemas for the complete system

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
We build foundations that serve.

THE MISSION:
Initialize all databases:
- Marketplace database
- Racon registry
- Temporal heritage registry
- World history database
- Scripture kit database

PEACE. LOVE. UNITY.
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / "jan-studio" / "backend"))

def init_marketplace_db():
    """Initialize marketplace database"""
    print("\n[INIT] Initializing Marketplace Database...")
    try:
        from jan_studio.backend.marketplace_db import init_database
        init_database()
        print("[OK] Marketplace database initialized")
        return True
    except ImportError:
        # Try alternative import path
        try:
            import sys
            sys.path.insert(0, str(project_root / "jan-studio" / "backend"))
            from marketplace_db import init_database
            init_database()
            print("[OK] Marketplace database initialized")
            return True
        except Exception as e:
            print(f"[WARN] Marketplace database: {e}")
            return False
    except Exception as e:
        print(f"[WARN] Marketplace database: {e}")
        return False

def init_racon_registry():
    """Initialize Racon registry"""
    print("\n[INIT] Initializing Racon Registry...")
    try:
        from racon_registry import init_racon_registry
        init_racon_registry()
        print("[OK] Racon registry initialized")
        return True
    except Exception as e:
        print(f"[WARN] Racon registry: {e}")
        return False

def init_temporal_heritage():
    """Initialize temporal heritage registry"""
    print("\n[INIT] Initializing Temporal Heritage Registry...")
    try:
        from temporal_heritage_registry import init_temporal_heritage_registry
        init_temporal_heritage_registry()
        print("[OK] Temporal heritage registry initialized")
        return True
    except Exception as e:
        print(f"[WARN] Temporal heritage registry: {e}")
        return False

def init_scripture_kit_db():
    """Initialize scripture kit database"""
    print("\n[INIT] Initializing Scripture Kit Database...")
    try:
        import sqlite3
        db_path = project_root / "data" / "scripture_kit.db"
        db_path.parent.mkdir(parents=True, exist_ok=True)
        
        conn = sqlite3.connect(str(db_path))
        cursor = conn.cursor()
        
        # Users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age_group TEXT,
                language TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Progress table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS progress (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                lesson_id TEXT,
                age_group TEXT,
                language TEXT,
                status TEXT,
                completed_at TIMESTAMP,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """)
        
        # Assessments table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS assessments (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                lesson_id TEXT,
                score INTEGER,
                max_score INTEGER,
                completed_at TIMESTAMP,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """)
        
        conn.commit()
        conn.close()
        print("[OK] Scripture kit database initialized")
        return True
    except Exception as e:
        print(f"[WARN] Scripture kit database: {e}")
        return False

def main():
    """Initialize all databases"""
    print("="*80)
    print("INITIALIZING ALL DATABASES")
    print("JAN/SIYEM Complete System")
    print("="*80)
    
    results = {
        "marketplace": init_marketplace_db(),
        "racon": init_racon_registry(),
        "temporal_heritage": init_temporal_heritage(),
        "scripture_kit": init_scripture_kit_db()
    }
    
    print("\n" + "="*80)
    print("INITIALIZATION COMPLETE")
    print("="*80)
    
    successful = sum(1 for v in results.values() if v)
    total = len(results)
    
    print(f"\nSuccessful: {successful}/{total}")
    for name, success in results.items():
        status = "[OK]" if success else "[FAIL]"
        print(f"  {status} {name}")
    
    print("\n" + "="*80)
    print("PEACE. LOVE. UNITY.")
    print("="*80 + "\n")

if __name__ == "__main__":
    main()
