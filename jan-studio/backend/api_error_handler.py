"""API ERROR HANDLER
Unified error handling decorator for Heritage API

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

Honors Law 5 (Your Word Is Your Bond) - proper error reporting.

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity


PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

from functools import wraps
from fastapi import HTTPException
from typing import Callable, Any
import logging

logger = logging.getLogger(__name__)


def heritage_api_error_handler(func: Callable) -> Callable:
    """
    Unified error handling decorator for Heritage API endpoints.
    
    Honors Law 5 (Your Word Is Your Bond) - proper error reporting.
    Provides consistent error handling across all API endpoints.
    
    Usage:
        @router.get("/endpoint")
        @heritage_api_error_handler
        async def my_endpoint():
            # Your code here
            return result
    
    Args:
        func: The API endpoint function to wrap
    
    Returns:
        Wrapped function with error handling
    """
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except HTTPException:
            # Re-raise HTTP exceptions (already properly formatted)
            raise
        except ValueError as e:
            # Client error (bad input)
            logger.warning(f"Invalid input in {func.__name__}: {e}")
            raise HTTPException(
                status_code=400,
                detail=f"Invalid input: {str(e)}"
            )
        except KeyError as e:
            # Missing data
            logger.warning(f"Missing data in {func.__name__}: {e}")
            raise HTTPException(
                status_code=404,
                detail=f"Not found: {str(e)}"
            )
        except Exception as e:
            # Server error
            logger.error(
                f"Heritage API error in {func.__name__}: {e}",
                exc_info=True,
                extra={"function": func.__name__, "args": str(args), "kwargs": str(kwargs)}
            )
            raise HTTPException(
                status_code=500,
                detail="Internal server error"
            )
    return wrapper
