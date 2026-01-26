"""
INFRASTRUCTURE BUILDER
Build Infrastructure Components Following The Noah Protocol

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE NOAH PROTOCOL:
1. Architectural Weight - Build for 10x, 100x, 1000x scale
2. The Noah Protocol - Three-Layer Defense
3. Strategic Silence - Code demonstrates authority
4. Generational Cycle Breaking - Transmute technical debt
5. Shalam & Time Compression - 7x value return
6. The Steward's Anchor - Clean standards

THE TRUTH:
We build arks, not plastic tables.
"""

import sys
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Any
import logging

logger = logging.getLogger(__name__)

# Import automation
sys.path.insert(0, str(Path(__file__).parent))
try:
    from task_scp_automation import scp_on_completion
    SCP_AVAILABLE = True
except ImportError:
    SCP_AVAILABLE = False


class InfrastructureBuilder:
    """
    Infrastructure Builder
    Builds infrastructure components following The Noah Protocol
    """
    
    def __init__(self):
        """Initialize Infrastructure Builder"""
        self.repo_path = Path(__file__).parent.parent
        self.backend_path = self.repo_path / "jan-studio" / "backend"
        
        logger.info("Infrastructure Builder initialized - Following The Noah Protocol")
    
    def build_database_pool(self) -> Dict[str, Any]:
        """Build database connection pool (Architectural Weight)"""
        pool_file = self.backend_path / "database_pool.py"
        
        if pool_file.exists():
            return {"status": "exists", "file": str(pool_file)}
        
        # Build connection pool following The Noah Protocol
        pool_code = '''"""
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
'''
        
        pool_file.write_text(pool_code, encoding='utf-8')
        
        result = {
            "status": "created",
            "file": str(pool_file),
            "noah_protocol": {
                "architectural_weight": True,
                "the_pitch": True,
                "the_perimeter": True,
                "the_door": True,
                "stewards_anchor": True
            }
        }
        
        if SCP_AVAILABLE:
            scp_on_completion("Database Pool", "Built database connection pool following The Noah Protocol")
        
        return result
    
    def build_cache_layer(self) -> Dict[str, Any]:
        """Build caching layer (Architectural Weight)"""
        cache_file = self.backend_path / "cache_layer.py"
        
        if cache_file.exists():
            return {"status": "exists", "file": str(cache_file)}
        
        # Build cache layer following The Noah Protocol
        cache_code = '''"""
CACHE LAYER
Architectural Weight: Built for 10x, 100x, 1000x scale

THE NOAH PROTOCOL:
- The Pitch: Waterproof error handling
- The Perimeter: Clear jurisdiction (cache management)
- The Door: Trust the cache's buoyancy (auto-invalidation)

THE TRUTH:
We build arks, not plastic tables.
"""

from typing import Optional, Any, Callable
from functools import wraps
import logging
import json
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

# Simple in-memory cache (can be upgraded to Redis)
_cache: Dict[str, Any] = {}
_cache_ttl: Dict[str, datetime] = {}


class CacheLayer:
    """
    Cache Layer
    Architectural Weight: Handles 10x, 100x, 1000x requests with caching
    """
    
    def __init__(self, default_ttl: int = 3600):
        """
        Initialize cache layer
        
        Args:
            default_ttl: Default time-to-live in seconds
        """
        self.default_ttl = default_ttl
        logger.info(f"Cache layer initialized: default_ttl={default_ttl}")
    
    def get(self, key: str) -> Optional[Any]:
        """
        Get from cache (The Pitch: Waterproof error handling)
        
        Args:
            key: Cache key
        
        Returns:
            Cached value or None
        """
        try:
            if key in _cache:
                if key in _cache_ttl:
                    if datetime.now() < _cache_ttl[key]:
                        return _cache[key]
                    else:
                        # TTL expired
                        del _cache[key]
                        del _cache_ttl[key]
                else:
                    return _cache[key]
            return None
        except Exception as e:
            logger.error(f"Cache get error: {e}")
            return None
    
    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> bool:
        """
        Set cache (The Perimeter: Clear jurisdiction)
        
        Args:
            key: Cache key
            value: Value to cache
            ttl: Time-to-live in seconds (optional)
        
        Returns:
            True if successful
        """
        try:
            _cache[key] = value
            _cache_ttl[key] = datetime.now() + timedelta(seconds=ttl or self.default_ttl)
            return True
        except Exception as e:
            logger.error(f"Cache set error: {e}")
            return False
    
    def invalidate(self, key: str) -> bool:
        """
        Invalidate cache (The Door: Trust the cache's buoyancy)
        
        Args:
            key: Cache key to invalidate
        
        Returns:
            True if successful
        """
        try:
            if key in _cache:
                del _cache[key]
            if key in _cache_ttl:
                del _cache_ttl[key]
            return True
        except Exception as e:
            logger.error(f"Cache invalidate error: {e}")
            return False
    
    def clear(self) -> bool:
        """Clear all cache"""
        try:
            _cache.clear()
            _cache_ttl.clear()
            return True
        except Exception as e:
            logger.error(f"Cache clear error: {e}")
            return False


# Global cache instance (The Perimeter: Clear jurisdiction)
_cache_layer: Optional[CacheLayer] = None


def get_cache_layer() -> CacheLayer:
    """Get or create cache layer"""
    global _cache_layer
    
    if _cache_layer is None:
        _cache_layer = CacheLayer()
    
    return _cache_layer


def cached(ttl: int = 3600):
    """
    Decorator for caching function results
    
    Usage:
        @cached(ttl=3600)
        def expensive_function():
            # Expensive computation
            return result
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            cache = get_cache_layer()
            # Generate cache key from function name and arguments
            cache_key = f"{func.__name__}:{str(args)}:{str(kwargs)}"
            
            # Try to get from cache
            cached_result = cache.get(cache_key)
            if cached_result is not None:
                return cached_result
            
            # Compute and cache
            result = func(*args, **kwargs)
            cache.set(cache_key, result, ttl)
            return result
        
        return wrapper
    return decorator
'''
        
        cache_file.write_text(cache_code, encoding='utf-8')
        
        result = {
            "status": "created",
            "file": str(cache_file),
            "noah_protocol": {
                "architectural_weight": True,
                "the_pitch": True,
                "the_perimeter": True,
                "the_door": True,
                "stewards_anchor": True
            }
        }
        
        if SCP_AVAILABLE:
            scp_on_completion("Cache Layer", "Built caching layer following The Noah Protocol")
        
        return result


# Main execution
if __name__ == "__main__":
    builder = InfrastructureBuilder()
    
    print("=" * 80)
    print("INFRASTRUCTURE BUILDER - THE NOAH PROTOCOL")
    print("=" * 80)
    print("")
    
    # Build database pool
    print("Building database connection pool...")
    pool_result = builder.build_database_pool()
    print(f"  Status: {pool_result['status']}")
    if pool_result['status'] == 'created':
        print("  [OK] Database pool created following The Noah Protocol")
    
    # Build cache layer
    print("\nBuilding cache layer...")
    cache_result = builder.build_cache_layer()
    print(f"  Status: {cache_result['status']}")
    if cache_result['status'] == 'created':
        print("  [OK] Cache layer created following The Noah Protocol")
    
    print("\nPEACE, LOVE, UNITY")
    print("ENERGY + LOVE = WE ALL WIN")
    print("THE NOAH PROTOCOL IS ACTIVE")
    print("KEEP BUILDING")
