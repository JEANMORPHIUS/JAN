"""DATABASE CONNECTION POOLING
SQLite connection pool for heritage databases

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

Honors performance while maintaining integrity.

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity


PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

import sqlite3
from contextlib import contextmanager
from threading import Lock
from typing import Generator, List, Optional
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


class DatabasePool:
    """
    SQLite connection pool for heritage databases.
    
    Honors performance while maintaining integrity.
    Reduces connection overhead for better scalability.
    """
    
    def __init__(self, db_path: str, pool_size: int = 5):
        """
        Initialize database connection pool.
        
        Args:
            db_path: Path to SQLite database file
            pool_size: Number of connections to maintain in pool
        """
        self.db_path = db_path
        self.pool_size = pool_size
        self._pool: List[sqlite3.Connection] = []
        self._lock = Lock()
        self._initialize_pool()
        logger.info(f"Database pool initialized: {db_path} (pool_size={pool_size})")
    
    def _initialize_pool(self):
        """Create initial connection pool."""
        for _ in range(self.pool_size):
            conn = self._create_connection()
            self._pool.append(conn)
    
    def _create_connection(self) -> sqlite3.Connection:
        """Create a new database connection."""
        conn = sqlite3.connect(self.db_path, check_same_thread=False)
        conn.row_factory = sqlite3.Row
        # Enable WAL mode for better concurrency
        conn.execute("PRAGMA journal_mode=WAL")
        return conn
    
    @contextmanager
    def get_connection(self) -> Generator[sqlite3.Connection, None, None]:
        """
        Get connection from pool.
        
        Usage:
            with pool.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(...)
                # Auto-commits on exit, auto-rollback on exception
        """
        # Get connection from pool
        with self._lock:
            if not self._pool:
                # Pool exhausted - create temporary connection
                conn = self._create_connection()
                logger.debug("Pool exhausted, created temporary connection")
            else:
                conn = self._pool.pop()
        
        try:
            yield conn
            conn.commit()
        except Exception:
            conn.rollback()
            logger.error("Database transaction rolled back", exc_info=True)
            raise
        finally:
            # Return connection to pool
            with self._lock:
                if len(self._pool) < self.pool_size:
                    self._pool.append(conn)
                else:
                    # Pool is full, close the connection
                    conn.close()
                    logger.debug("Pool full, closed connection")
    
    def close_all(self):
        """Close all connections in pool."""
        with self._lock:
            for conn in self._pool:
                try:
                    conn.close()
                except Exception:
                    pass
            self._pool.clear()
        logger.info("Database pool closed")


# Global pools (initialized on first use)
_heritage_pool: Optional[DatabasePool] = None
_racon_pool: Optional[DatabasePool] = None
_pool_lock = Lock()


def get_heritage_pool(db_path: Optional[str] = None, pool_size: int = 5) -> DatabasePool:
    """
    Get or create heritage database pool.
    
    Args:
        db_path: Path to heritage database (default: from temporal_heritage_registry)
        pool_size: Pool size (default: 5)
    
    Returns:
        DatabasePool instance
    """
    global _heritage_pool
    
    if _heritage_pool is None:
        with _pool_lock:
            if _heritage_pool is None:
                if db_path is None:
                    # Default path from temporal_heritage_registry
                    from pathlib import Path
                    db_path = str(Path(__file__).parent.parent.parent / "temporal_heritage_registry.db")
                _heritage_pool = DatabasePool(db_path, pool_size)
    
    return _heritage_pool


def get_racon_pool(db_path: Optional[str] = None, pool_size: int = 5) -> DatabasePool:
    """
    Get or create racon database pool.
    
    Args:
        db_path: Path to racon database (default: from racon_registry)
        pool_size: Pool size (default: 5)
    
    Returns:
        DatabasePool instance
    """
    global _racon_pool
    
    if _racon_pool is None:
        with _pool_lock:
            if _racon_pool is None:
                if db_path is None:
                    # Default path from racon_registry
                    from pathlib import Path
                    db_path = str(Path(__file__).parent.parent.parent / "racon_registry.db")
                _racon_pool = DatabasePool(db_path, pool_size)
    
    return _racon_pool
