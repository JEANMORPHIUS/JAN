"""
Google Calendar API Endpoints

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN

API endpoints for exporting posts to Google Calendar
"""

from fastapi import APIRouter, HTTPException, Query, Body, File, UploadFile
from fastapi.responses import Response, FileResponse
from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime
import tempfile
import os

from google_calendar_exporter import (
    CalendarExportService,
    ICalExporter,
    GoogleCalendarAPIExporter,
    CalendarEvent
)

router = APIRouter(prefix="/api/calendar", tags=["calendar"])


# Request/Response Models
class PostItem(BaseModel):
    """Individual post item for calendar export"""
    title: Optional[str] = None
    content: str = Field(..., description="Post content/text")
    scheduled_time: Optional[str] = Field(None, description="ISO format datetime string")
    platform: Optional[str] = None
    hashtags: Optional[List[str]] = None
    url: Optional[str] = None
    location: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class ExportToICalRequest(BaseModel):
    """Request model for iCal export"""
    posts: List[PostItem] = Field(..., description="List of posts to export")
    calendar_name: str = Field(default="JAN Studio Social Posts", description="Calendar name")
    output_filename: Optional[str] = Field(default=None, description="Optional output filename")


class GoogleCalendarAuthRequest(BaseModel):
    """Request model for Google Calendar authentication"""
    client_id: Optional[str] = None
    client_secret: Optional[str] = None


class GoogleCalendarAuthCompleteRequest(BaseModel):
    """Request model for completing Google Calendar authentication"""
    authorization_code: str = Field(..., description="OAuth authorization code")
    client_id: Optional[str] = None
    client_secret: Optional[str] = None


class ExportToGoogleCalendarRequest(BaseModel):
    """Request model for Google Calendar API export"""
    posts: List[PostItem] = Field(..., description="List of posts to export")
    calendar_id: str = Field(default="primary", description="Google Calendar ID")


@router.post("/export/ical", summary="Export posts to iCal format")
async def export_to_ical(request: ExportToICalRequest):
    """
    Export posts to iCal format (.ics file)
    Universal format compatible with Google Calendar, Apple Calendar, Outlook, etc.
    
    Returns:
        iCal file download
    """
    try:
        # Convert PostItem to dict
        posts_dict = [post.dict() for post in request.posts]
        
        # Export to iCal
        service = CalendarExportService()
        ical_content = service.export_to_ical(
            posts_dict,
            calendar_name=request.calendar_name
        )
        
        # Generate filename
        filename = request.output_filename or f"jan_studio_posts_{datetime.now().strftime('%Y%m%d_%H%M%S')}.ics"
        if not filename.endswith('.ics'):
            filename += '.ics'
        
        # Create temporary file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.ics', delete=False, encoding='utf-8') as tmp:
            tmp.write(ical_content)
            tmp_path = tmp.name
        
        return FileResponse(
            tmp_path,
            media_type='text/calendar',
            filename=filename,
            headers={
                'Content-Disposition': f'attachment; filename="{filename}"'
            }
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error exporting to iCal: {str(e)}")


@router.post("/export/ical/json", summary="Export posts to iCal format (JSON response)")
async def export_to_ical_json(request: ExportToICalRequest):
    """
    Export posts to iCal format and return as JSON with base64-encoded content
    
    Useful for frontend handling without file download
    """
    try:
        posts_dict = [post.dict() for post in request.posts]
        
        service = CalendarExportService()
        ical_content = service.export_to_ical(
            posts_dict,
            calendar_name=request.calendar_name
        )
        
        filename = request.output_filename or f"jan_studio_posts_{datetime.now().strftime('%Y%m%d_%H%M%S')}.ics"
        if not filename.endswith('.ics'):
            filename += '.ics'
        
        # Base64 encode for JSON response
        import base64
        ical_base64 = base64.b64encode(ical_content.encode('utf-8')).decode('utf-8')
        
        return {
            "success": True,
            "filename": filename,
            "ical_content": ical_content,
            "ical_base64": ical_base64,
            "event_count": len(request.posts),
            "calendar_name": request.calendar_name
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error exporting to iCal: {str(e)}")


@router.post("/google/auth/start", summary="Start Google Calendar OAuth authentication")
async def start_google_calendar_auth(request: GoogleCalendarAuthRequest):
    """
    Start Google Calendar OAuth2 authentication flow
    
    Returns authorization URL that user must visit to grant permissions
    """
    try:
        exporter = GoogleCalendarAPIExporter()
        auth_url = exporter.authenticate(
            client_id=request.client_id,
            client_secret=request.client_secret
        )
        
        return {
            "success": True,
            "authorization_url": auth_url,
            "message": "Visit the authorization URL and paste the authorization code to complete authentication"
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error starting authentication: {str(e)}")


@router.post("/google/auth/complete", summary="Complete Google Calendar OAuth authentication")
async def complete_google_calendar_auth(request: GoogleCalendarAuthCompleteRequest):
    """
    Complete Google Calendar OAuth2 authentication with authorization code
    
    Saves credentials for future use
    """
    try:
        exporter = GoogleCalendarAPIExporter()
        success = exporter.complete_authentication(
            request.authorization_code,
            client_id=request.client_id,
            client_secret=request.client_secret
        )
        
        if success:
            return {
                "success": True,
                "message": "Authentication successful. Credentials saved."
            }
        else:
            raise HTTPException(status_code=400, detail="Authentication failed")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error completing authentication: {str(e)}")


@router.get("/google/auth/status", summary="Check Google Calendar authentication status")
async def check_google_calendar_auth_status():
    """
    Check if user is authenticated with Google Calendar
    """
    try:
        exporter = GoogleCalendarAPIExporter()
        is_authenticated = exporter.load_credentials()
        
        return {
            "authenticated": is_authenticated,
            "message": "Authenticated" if is_authenticated else "Not authenticated. Start auth flow first."
        }
    
    except Exception as e:
        return {
            "authenticated": False,
            "error": str(e)
        }


@router.post("/export/google", summary="Export posts to Google Calendar via API")
async def export_to_google_calendar(request: ExportToGoogleCalendarRequest):
    """
    Export posts directly to Google Calendar using Google Calendar API
    
    Requires authentication (call /google/auth/start and /google/auth/complete first)
    """
    try:
        posts_dict = [post.dict() for post in request.posts]
        
        service = CalendarExportService()
        created_events = service.export_to_google_calendar(
            posts_dict,
            calendar_id=request.calendar_id
        )
        
        return {
            "success": True,
            "events_created": len(created_events),
            "events": created_events,
            "message": f"Successfully created {len(created_events)} event(s) in Google Calendar"
        }
    
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error exporting to Google Calendar: {str(e)}")


@router.get("/google/calendars", summary="List available Google Calendars")
async def list_google_calendars():
    """
    List all available Google Calendars for the authenticated user
    """
    try:
        exporter = GoogleCalendarAPIExporter()
        
        if not exporter.load_credentials():
            raise HTTPException(status_code=401, detail="Not authenticated")
        
        calendar_list = exporter.service.calendarList().list().execute()
        calendars = calendar_list.get('items', [])
        
        return {
            "success": True,
            "calendars": [
                {
                    "id": cal.get('id'),
                    "name": cal.get('summary'),
                    "description": cal.get('description'),
                    "primary": cal.get('primary', False)
                }
                for cal in calendars
            ]
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error listing calendars: {str(e)}")


@router.post("/parse-posts", summary="Parse posts and return calendar events")
async def parse_posts(posts: List[PostItem]):
    """
    Parse posts into calendar events without exporting
    Useful for previewing events before export
    """
    try:
        posts_dict = [post.dict() for post in posts]
        service = CalendarExportService()
        
        events = [
            service.parse_post_to_event(post).__dict__
            for post in posts_dict
        ]
        
        # Convert datetime objects to ISO strings for JSON
        for event in events:
            if event.get('start_datetime'):
                if isinstance(event['start_datetime'], datetime):
                    event['start_datetime'] = event['start_datetime'].isoformat()
            if event.get('end_datetime'):
                if isinstance(event['end_datetime'], datetime):
                    event['end_datetime'] = event['end_datetime'].isoformat()
        
        return {
            "success": True,
            "events": events,
            "count": len(events)
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error parsing posts: {str(e)}")
