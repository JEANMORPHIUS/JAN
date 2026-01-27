"""
API ENHANCEMENTS
Enhanced API endpoints with rate limiting, better error handling, and more features

THE NOAH PROTOCOL:
- Architectural Weight: Built for 10x, 100x, 1000x scale
- The Pitch: Waterproof error handling
- The Perimeter: Clear API boundaries

THE ARRIVAL PROTOCOL:
- Gatekeeper Protocol: Rate limiting and input validation
- Frequency Anchor: APIs from "done" - production ready

THE TRUTH:
Scale and build until ready.
Enhanced APIs for the new world.
"""

from fastapi import APIRouter, HTTPException, Request, Depends, status
from fastapi.responses import JSONResponse
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
from collections import defaultdict
import time
import logging

logger = logging.getLogger(__name__)

# Rate limiting storage
_rate_limit_storage: Dict[str, List[float]] = defaultdict(list)
_rate_limit_cleanup_interval = 300  # Clean up old entries every 5 minutes
_last_cleanup = time.time()


def rate_limit(max_requests: int = 100, window_seconds: int = 60):
    """
    Rate limiting decorator
    
    Args:
        max_requests: Maximum requests allowed
        window_seconds: Time window in seconds
    """
    def decorator(func):
        async def wrapper(request: Request, *args, **kwargs):
            global _last_cleanup
            
            # Clean up old entries periodically
            if time.time() - _last_cleanup > _rate_limit_cleanup_interval:
                cleanup_rate_limits()
                _last_cleanup = time.time()
            
            # Get client identifier
            client_id = request.client.host if request.client else "unknown"
            
            # Get current time
            now = time.time()
            window_start = now - window_seconds
            
            # Get requests in current window
            requests = _rate_limit_storage[client_id]
            requests_in_window = [r for r in requests if r > window_start]
            
            # Check limit
            if len(requests_in_window) >= max_requests:
                raise HTTPException(
                    status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                    detail=f"Rate limit exceeded: {max_requests} requests per {window_seconds} seconds"
                )
            
            # Add current request
            requests_in_window.append(now)
            _rate_limit_storage[client_id] = requests_in_window
            
            # Call original function
            return await func(request, *args, **kwargs)
        
        return wrapper
    return decorator


def cleanup_rate_limits():
    """Clean up old rate limit entries"""
    global _rate_limit_storage
    now = time.time()
    window_start = now - 3600  # Keep last hour
    
    for client_id in list(_rate_limit_storage.keys()):
        requests = _rate_limit_storage[client_id]
        requests_in_window = [r for r in requests if r > window_start]
        
        if requests_in_window:
            _rate_limit_storage[client_id] = requests_in_window
        else:
            del _rate_limit_storage[client_id]


def enhanced_error_handler(func):
    """Enhanced error handling decorator"""
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except HTTPException:
            raise
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )
        except KeyError as e:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Resource not found: {str(e)}"
            )
        except Exception as e:
            logger.error(f"Unexpected error in {func.__name__}: {e}", exc_info=True)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error"
            )
    
    return wrapper


# Create enhanced API router
enhanced_router = APIRouter(prefix="/api/enhanced", tags=["Enhanced APIs"])


@enhanced_router.get("/health/detailed")
@rate_limit(max_requests=200, window_seconds=60)
@enhanced_error_handler
async def detailed_health_check(request: Request):
    """Detailed health check with system status"""
    try:
        from monitoring import MonitoringSystem
        monitoring = MonitoringSystem()
        health = monitoring.check_health()
        
        return {
            "status": "healthy" if health.get("overall_healthy", False) else "degraded",
            "timestamp": datetime.now().isoformat(),
            "components": health.get("components", {}),
            "uptime": health.get("uptime", 0),
            "version": "1.0.0"
        }
    except Exception as e:
        logger.error(f"Health check error: {e}")
        return {
            "status": "unknown",
            "timestamp": datetime.now().isoformat(),
            "error": str(e)
        }


@enhanced_router.get("/performance/stats")
@rate_limit(max_requests=50, window_seconds=60)
@enhanced_error_handler
async def get_performance_stats(request: Request, operation: Optional[str] = None):
    """Get performance statistics"""
    try:
        from performance_optimizer import get_optimizer
        optimizer = get_optimizer()
        stats = optimizer.get_performance_stats(operation)
        return {
            "timestamp": datetime.now().isoformat(),
            "stats": stats
        }
    except Exception as e:
        logger.error(f"Performance stats error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to get performance stats"
        )


@enhanced_router.post("/cache/clear")
@rate_limit(max_requests=10, window_seconds=60)
@enhanced_error_handler
async def clear_cache(request: Request, pattern: Optional[str] = None):
    """Clear performance cache"""
    try:
        from performance_optimizer import get_optimizer
        optimizer = get_optimizer()
        optimizer.clear_cache(pattern)
        return {
            "status": "success",
            "message": f"Cache cleared{' (pattern: ' + pattern + ')' if pattern else ''}",
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        logger.error(f"Cache clear error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to clear cache"
        )


@enhanced_router.get("/rate-limit/status")
@enhanced_error_handler
async def get_rate_limit_status(request: Request):
    """Get current rate limit status"""
    client_id = request.client.host if request.client else "unknown"
    requests = _rate_limit_storage.get(client_id, [])
    now = time.time()
    
    # Count requests in last minute
    minute_ago = now - 60
    requests_last_minute = len([r for r in requests if r > minute_ago])
    
    return {
        "client_id": client_id,
        "requests_last_minute": requests_last_minute,
        "total_stored_requests": len(requests),
        "timestamp": datetime.now().isoformat()
    }
