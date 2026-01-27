"""
PERFORMANCE OPTIMIZER
Advanced performance optimizations for 10x, 100x, 1000x scale

THE NOAH PROTOCOL:
- Architectural Weight: Built for massive scale
- The Pitch: Waterproof error handling
- The Perimeter: Clear performance boundaries

THE ARRIVAL PROTOCOL:
- Pre-Commissioning Scan: Can this handle 1000x load?
- Frequency Anchor: Optimize from "done" - performance ready

THE TRUTH:
Scale and build until ready.
Performance optimization for the new world.
"""

import asyncio
import time
from typing import Dict, List, Any, Optional, Callable
from functools import wraps
from datetime import datetime, timedelta
import logging
from pathlib import Path
import json

logger = logging.getLogger(__name__)


class PerformanceOptimizer:
    """
    Performance Optimizer
    Advanced caching, batching, and async optimizations
    """
    
    def __init__(self):
        """Initialize optimizer"""
        self.cache: Dict[str, Any] = {}
        self.cache_timestamps: Dict[str, datetime] = {}
        self.batch_queues: Dict[str, List[Any]] = {}
        self.batch_timers: Dict[str, float] = {}
        self.performance_metrics: Dict[str, List[float]] = {}
        
        logger.info("Performance Optimizer initialized")
    
    def cache_result(self, key: str, value: Any, ttl_seconds: int = 300):
        """Cache a result with TTL"""
        self.cache[key] = value
        self.cache_timestamps[key] = datetime.now() + timedelta(seconds=ttl_seconds)
    
    def get_cached(self, key: str) -> Optional[Any]:
        """Get cached result if valid"""
        if key not in self.cache:
            return None
        
        if datetime.now() > self.cache_timestamps.get(key, datetime.min):
            # Expired
            del self.cache[key]
            del self.cache_timestamps[key]
            return None
        
        return self.cache[key]
    
    def batch_operation(self, queue_key: str, item: Any, batch_size: int = 10, 
                       batch_timeout: float = 1.0, processor: Optional[Callable] = None):
        """Batch operations for efficiency"""
        if queue_key not in self.batch_queues:
            self.batch_queues[queue_key] = []
            self.batch_timers[queue_key] = time.time()
        
        self.batch_queues[queue_key].append(item)
        
        # Check if batch is ready
        queue = self.batch_queues[queue_key]
        elapsed = time.time() - self.batch_timers[queue_key]
        
        if len(queue) >= batch_size or elapsed >= batch_timeout:
            # Process batch
            batch = queue.copy()
            self.batch_queues[queue_key] = []
            self.batch_timers[queue_key] = time.time()
            
            if processor:
                return processor(batch)
            return batch
        
        return None
    
    def measure_performance(self, operation_name: str, func: Callable):
        """Measure and track performance"""
        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            start = time.time()
            try:
                result = await func(*args, **kwargs)
                elapsed = time.time() - start
                
                if operation_name not in self.performance_metrics:
                    self.performance_metrics[operation_name] = []
                self.performance_metrics[operation_name].append(elapsed)
                
                # Keep only last 100 measurements
                if len(self.performance_metrics[operation_name]) > 100:
                    self.performance_metrics[operation_name] = self.performance_metrics[operation_name][-100:]
                
                return result
            except Exception as e:
                elapsed = time.time() - start
                logger.error(f"Performance measurement error for {operation_name}: {e}")
                raise
        
        @wraps(func)
        def sync_wrapper(*args, **kwargs):
            start = time.time()
            try:
                result = func(*args, **kwargs)
                elapsed = time.time() - start
                
                if operation_name not in self.performance_metrics:
                    self.performance_metrics[operation_name] = []
                self.performance_metrics[operation_name].append(elapsed)
                
                # Keep only last 100 measurements
                if len(self.performance_metrics[operation_name]) > 100:
                    self.performance_metrics[operation_name] = self.performance_metrics[operation_name][-100:]
                
                return result
            except Exception as e:
                elapsed = time.time() - start
                logger.error(f"Performance measurement error for {operation_name}: {e}")
                raise
        
        if asyncio.iscoroutinefunction(func):
            return async_wrapper
        return sync_wrapper
    
    def get_performance_stats(self, operation_name: Optional[str] = None) -> Dict[str, Any]:
        """Get performance statistics"""
        if operation_name:
            if operation_name not in self.performance_metrics:
                return {"error": "Operation not found"}
            
            metrics = self.performance_metrics[operation_name]
            if not metrics:
                return {"error": "No metrics available"}
            
            return {
                "operation": operation_name,
                "count": len(metrics),
                "min": min(metrics),
                "max": max(metrics),
                "avg": sum(metrics) / len(metrics),
                "p50": sorted(metrics)[len(metrics) // 2],
                "p95": sorted(metrics)[int(len(metrics) * 0.95)],
                "p99": sorted(metrics)[int(len(metrics) * 0.99)]
            }
        
        # All operations
        stats = {}
        for op_name in self.performance_metrics:
            metrics = self.performance_metrics[op_name]
            if metrics:
                stats[op_name] = {
                    "count": len(metrics),
                    "avg": sum(metrics) / len(metrics),
                    "min": min(metrics),
                    "max": max(metrics)
                }
        
        return stats
    
    def clear_cache(self, pattern: Optional[str] = None):
        """Clear cache (optionally by pattern)"""
        if pattern:
            keys_to_delete = [k for k in self.cache.keys() if pattern in k]
            for key in keys_to_delete:
                del self.cache[key]
                if key in self.cache_timestamps:
                    del self.cache_timestamps[key]
        else:
            self.cache.clear()
            self.cache_timestamps.clear()


# Global optimizer instance
_optimizer: Optional[PerformanceOptimizer] = None


def get_optimizer() -> PerformanceOptimizer:
    """Get global optimizer instance"""
    global _optimizer
    if _optimizer is None:
        _optimizer = PerformanceOptimizer()
    return _optimizer


def cached(ttl_seconds: int = 300):
    """Decorator for caching function results"""
    def decorator(func: Callable):
        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            optimizer = get_optimizer()
            # Create cache key from function name and arguments
            cache_key = f"{func.__name__}:{str(args)}:{str(kwargs)}"
            
            # Check cache
            cached_result = optimizer.get_cached(cache_key)
            if cached_result is not None:
                return cached_result
            
            # Execute and cache
            result = await func(*args, **kwargs)
            optimizer.cache_result(cache_key, result, ttl_seconds)
            return result
        
        @wraps(func)
        def sync_wrapper(*args, **kwargs):
            optimizer = get_optimizer()
            # Create cache key from function name and arguments
            cache_key = f"{func.__name__}:{str(args)}:{str(kwargs)}"
            
            # Check cache
            cached_result = optimizer.get_cached(cache_key)
            if cached_result is not None:
                return cached_result
            
            # Execute and cache
            result = func(*args, **kwargs)
            optimizer.cache_result(cache_key, result, ttl_seconds)
            return result
        
        if asyncio.iscoroutinefunction(func):
            return async_wrapper
        return sync_wrapper
    
    return decorator


def measure_performance(operation_name: Optional[str] = None):
    """Decorator for measuring performance"""
    def decorator(func: Callable):
        optimizer = get_optimizer()
        op_name = operation_name or func.__name__
        return optimizer.measure_performance(op_name, func)
    
    return decorator
