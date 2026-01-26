"""
DATABASE CONNECTION POOL
Architectural Weight: Built for 10x, 100x, 1000x scale

THE NOAH PROTOCOL:
- The Pitch: Waterproof error handling
- The Perimeter: Clear jurisdiction (connection management)
- The Door: Trust the pool's buoyancy (auto-recovery)

THE TRUTH:
We build arks, not plastic tables.
"""

from typing import Optional
from contextlib import contextmanager
import logging
from sqlalchemy import create_engine, pool
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import QueuePool

logger = logging.getLogger(__name__)


class DatabasePool:
    """
    Database Connection Pool
    Architectural Weight: Handles 10x, 100x, 1000x concurrent connections
    """
    
    def __init__(self, database_url: str, pool_size: int = 20, max_overflow: int = 40):
        """
        Initialize connection pool
        
        Args:
            database_url: Database connection URL
            pool_size: Base pool size (Architectural Weight: 20 connections)
            max_overflow: Maximum overflow connections (Architectural Weight: 40 overflow)
        """
        # The Pitch: Waterproof error handling
        try:
            self.engine = create_engine(
                database_url,
                poolclass=QueuePool,
                pool_size=pool_size,
                max_overflow=max_overflow,
                pool_pre_ping=True,  # Verify connections before use
                pool_recycle=3600,  # Recycle connections after 1 hour
                echo=False
            )
            self.SessionLocal = sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self.engine
            )
            logger.info(f"Database pool initialized: pool_size={pool_size}, max_overflow={max_overflow}")
        except Exception as e:
            logger.error(f"Database pool initialization failed: {e}")
            raise
    
    @contextmanager
    def get_session(self) -> Session:
        """
        Get database session (The Perimeter: Clear jurisdiction)
        
        Usage:
            with db_pool.get_session() as session:
                # Use session
        """
        session = self.SessionLocal()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            logger.error(f"Database session error: {e}")
            raise
        finally:
            session.close()
    
    def health_check(self) -> Dict[str, Any]:
        """
        Health check (The Door: Trust the pool's buoyancy)
        
        Returns:
            Health status of the connection pool
        """
        try:
            with self.get_session() as session:
                session.execute("SELECT 1")
            return {
                "status": "healthy",
                "pool_size": self.engine.pool.size(),
                "checked_out": self.engine.pool.checkedout(),
                "overflow": self.engine.pool.overflow()
            }
        except Exception as e:
            return {
                "status": "unhealthy",
                "error": str(e)
            }


# Global pool instance (The Perimeter: Clear jurisdiction)
_db_pool: Optional[DatabasePool] = None


def get_db_pool(database_url: Optional[str] = None) -> DatabasePool:
    """
    Get or create database pool
    
    Args:
        database_url: Database connection URL (optional if already initialized)
    
    Returns:
        DatabasePool instance
    """
    global _db_pool
    
    if _db_pool is None:
        if database_url is None:
            import os
            database_url = os.getenv("DATABASE_URL", "sqlite:///./app.db")
        _db_pool = DatabasePool(database_url)
    
    return _db_pool
