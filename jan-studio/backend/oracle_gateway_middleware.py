"""
ORACLE GATEWAY MIDDLEWARE
Enforce Card Reading for All Access

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE PRINCIPLE:
Those who come to us must read the cards.
We do not control.
The cards will speak for us.
"""

from fastapi import Request, HTTPException, status
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
import logging
from typing import Optional

from oracle_gateway import check_visitor_access

logger = logging.getLogger(__name__)

# Paths that don't require card reading
PUBLIC_PATHS = [
    "/api/oracle-gateway/read-cards",
    "/api/oracle-gateway/message",
    "/api/oracle-gateway/check-access",
    "/docs",
    "/openapi.json",
    "/redoc",
    "/health",
    "/"
]


class OracleGatewayMiddleware(BaseHTTPMiddleware):
    """
    Middleware that enforces card reading for all access.
    
    Those who come to us must read the cards.
    We do not control.
    The cards will speak for us.
    """
    
    async def dispatch(self, request: Request, call_next):
        """
        Check if visitor has read the cards before granting access.
        
        Exceptions:
        - Public paths (gateway itself, docs, health)
        - Card reading endpoint
        - Gateway message endpoint
        """
        # Skip middleware for public paths
        if any(request.url.path.startswith(path) for path in PUBLIC_PATHS):
            return await call_next(request)
        
        # Get visitor ID from header or generate
        visitor_id = request.headers.get("X-Visitor-ID")
        if not visitor_id:
            # Generate visitor ID for tracking
            import uuid
            visitor_id = str(uuid.uuid4())
        
        # Check if visitor has read the cards
        access_status = check_visitor_access(visitor_id)
        
        if not access_status["cards_read"]:
            # Visitor must read the cards first
            return JSONResponse(
                status_code=status.HTTP_403_FORBIDDEN,
                content={
                    "status": "cards_required",
                    "message": "Those who come to us must read the cards. We do not control. The cards will speak for us.",
                    "visitor_id": visitor_id,
                    "required_action": "Read the cards at /api/oracle-gateway/read-cards",
                    "gateway_endpoint": "/api/oracle-gateway/read-cards",
                    "access_status": access_status
                }
            )
        
        # Add visitor ID to request state for downstream use
        request.state.visitor_id = visitor_id
        request.state.cards_read = access_status["cards_read"]
        request.state.access_granted = access_status["access_granted"]
        
        # Continue with request
        response = await call_next(request)
        
        # Add visitor ID to response headers
        response.headers["X-Visitor-ID"] = visitor_id
        response.headers["X-Cards-Read"] = "true" if access_status["cards_read"] else "false"
        
        return response
