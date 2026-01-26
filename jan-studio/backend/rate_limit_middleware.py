"""Rate Limiting Middleware for JAN Studio
Applies rate limiting to specific endpoints.

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

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
