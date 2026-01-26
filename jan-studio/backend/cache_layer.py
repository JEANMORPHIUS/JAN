"""
CACHE LAYER
Architectural Weight: Built for 10x, 100x, 1000x scale

THE NOAH PROTOCOL:
- The Pitch: Waterproof error handling
- The Perimeter: Clear jurisdiction (cache management)
- The Door: Trust the cache's buoyancy (auto-invalidation)

THE TRUTH:
We build arks, not plastic tables.
"""

from typing import Optional, Any, Callable, Dict
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
