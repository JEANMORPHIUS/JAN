"""
Rate Limiting Middleware for JAN Studio
Applies rate limiting to specific endpoints.

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity
"""

from fastapi import Request, status
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
import logging

logger = logging.getLogger(__name__)

# Rate limiting will be applied via slowapi in main.py
# This middleware can be used for additional rate limiting logic if needed

class RateLimitMiddleware(BaseHTTPMiddleware):
    """Additional rate limiting middleware if needed"""
    
    async def dispatch(self, request: Request, call_next):
        # Rate limiting is primarily handled by slowapi in main.py
        # This middleware can add additional logic if needed
        response = await call_next(request)
        return response
