"""Google Calendar Export Service

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN

This service provides Google Calendar export functionality for social media posts
and content scheduling, honoring the sacred weight of time and alignment.

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity


PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

import json
import os
from datetime import datetime, timedelta, timezone
from typing import List, Dict, Optional, Any
from dataclasses import dataclass, asdict
import base64
from urllib.parse import urlencode

try:
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import Flow
    from google.auth.transport.requests import Request
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
    GOOGLE_API_AVAILABLE = True
except ImportError:
    GOOGLE_API_AVAILABLE = False
    print("Warning: Google API libraries not installed. iCal export will still work.")


@dataclass
class CalendarEvent:
    """Represents a calendar event for export"""
    title: str
    description: str
    start_datetime: datetime
    end_datetime: Optional[datetime] = None
    location: Optional[str] = None
    url: Optional[str] = None
    platform: Optional[str] = None  # e.g., 'Instagram', 'Twitter', 'Facebook'
    hashtags: Optional[List[str]] = None
    metadata: Optional[Dict[str, Any]] = None


class ICalExporter:
    """
    Exports events to iCal format (.ics files)
    Universal format that works with Google Calendar, Apple Calendar, Outlook, etc.
    """
    
    @staticmethod
    def escape_text(text: str) -> str:
        """Escape special characters for iCal format"""
        if not text:
            return ""
        text = text.replace("\\", "\\\\")
        text = text.replace(",", "\\,")
        text = text.replace(";", "\\;")
        text = text.replace("\n", "\\n")
        return text
    
    @staticmethod
    def format_datetime(dt: datetime) -> str:
        """Format datetime for iCal (UTC format)"""
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.strftime("%Y%m%dT%H%M%SZ")
    
    @staticmethod
    def generate_uid(event: CalendarEvent, index: int = 0) -> str:
        """Generate a unique identifier for the event"""
        timestamp = int(datetime.now().timestamp())
        return f"jan-studio-{timestamp}-{index}@siyem.org"
    
    @classmethod
    def export_events(cls, events: List[CalendarEvent], calendar_name: str = "JAN Studio Posts") -> str:
        """
        Export a list of events to iCal format
        
        Args:
            events: List of CalendarEvent objects
            calendar_name: Name for the calendar
            
        Returns:
            iCal formatted string
        """
        lines = [
            "BEGIN:VCALENDAR",
            "VERSION:2.0",
            "PRODID:-//JAN Studio//SIYEM//EN",
            f"X-WR-CALNAME:{cls.escape_text(calendar_name)}",
            "CALSCALE:GREGORIAN",
            "METHOD:PUBLISH",
        ]
        
        for index, event in enumerate(events):
            lines.extend(cls._format_event(event, index))
        
        lines.append("END:VCALENDAR")
        
        return "\r\n".join(lines)
    
    @classmethod
    def _format_event(cls, event: CalendarEvent, index: int) -> List[str]:
        """Format a single event for iCal"""
        lines = [
            "BEGIN:VEVENT",
            f"UID:{cls.generate_uid(event, index)}",
            f"DTSTART:{cls.format_datetime(event.start_datetime)}",
        ]
        
        # End time (default to 1 hour if not specified)
        if event.end_datetime:
            lines.append(f"DTEND:{cls.format_datetime(event.end_datetime)}")
        else:
            end_time = event.start_datetime + timedelta(hours=1)
            lines.append(f"DTEND:{cls.format_datetime(end_time)}")
        
        # Title
        lines.append(f"SUMMARY:{cls.escape_text(event.title)}")
        
        # Description
        desc_parts = [event.description]
        if event.platform:
            desc_parts.append(f"\nPlatform: {event.platform}")
        if event.hashtags:
            desc_parts.append(f"\nHashtags: {', '.join(event.hashtags)}")
        if event.url:
            desc_parts.append(f"\nURL: {event.url}")
        if event.metadata:
            desc_parts.append(f"\nMetadata: {json.dumps(event.metadata)}")
        
        lines.append(f"DESCRIPTION:{cls.escape_text('\n'.join(desc_parts))}")
        
        # Location
        if event.location:
            lines.append(f"LOCATION:{cls.escape_text(event.location)}")
        
        # URL
        if event.url:
            lines.append(f"URL:{event.url}")
        
        # Created and modified timestamps
        now = datetime.now(timezone.utc)
        lines.append(f"DTSTAMP:{cls.format_datetime(now)}")
        lines.append(f"CREATED:{cls.format_datetime(now)}")
        lines.append(f"LAST-MODIFIED:{cls.format_datetime(now)}")
        
        # Status
        lines.append("STATUS:CONFIRMED")
        lines.append("SEQUENCE:0")
        lines.append("TRANSP:OPAQUE")
        
        lines.append("END:VEVENT")
        
        return lines
    
    @classmethod
    def save_to_file(cls, events: List[CalendarEvent], filepath: str, calendar_name: str = "JAN Studio Posts") -> str:
        """Export events to an .ics file"""
        ical_content = cls.export_events(events, calendar_name)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(ical_content)
        return filepath


class GoogleCalendarAPIExporter:
    """
    Exports events directly to Google Calendar using the Google Calendar API
    Requires OAuth2 authentication
    """
    
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'  # For desktop apps
    
    def __init__(self, credentials_path: Optional[str] = None):
        """
        Initialize Google Calendar API exporter
        
        Args:
            credentials_path: Path to OAuth2 credentials JSON file
        """
        if not GOOGLE_API_AVAILABLE:
            raise ImportError(
                "Google API libraries not installed. "
                "Install with: pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client"
            )
        
        self.credentials_path = credentials_path or os.getenv(
            'GOOGLE_CREDENTIALS_PATH',
            'google_credentials.json'
        )
        self.token_path = os.getenv('GOOGLE_TOKEN_PATH', 'google_token.json')
        self.service = None
        self.creds = None
    
    def authenticate(self, client_id: Optional[str] = None, client_secret: Optional[str] = None) -> str:
        """
        Authenticate with Google Calendar API
        
        Returns:
            Authorization URL for user to visit
        """
        # Load client credentials
        if client_id and client_secret:
            client_config = {
                "installed": {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                    "token_uri": "https://oauth2.googleapis.com/token",
                    "redirect_uris": [self.REDIRECT_URI]
                }
            }
        else:
            if not os.path.exists(self.credentials_path):
                raise FileNotFoundError(
                    f"Credentials file not found: {self.credentials_path}\n"
                    "Get credentials from: https://console.cloud.google.com/apis/credentials"
                )
            with open(self.credentials_path, 'r') as f:
                client_config = json.load(f)
        
        # Create OAuth flow
        flow = Flow.from_client_config(
            client_config,
            scopes=self.SCOPES,
            redirect_uri=self.REDIRECT_URI
        )
        
        authorization_url, _ = flow.authorization_url(
            access_type='offline',
            include_granted_scopes='true'
        )
        
        return authorization_url
    
    def complete_authentication(self, authorization_code: str, client_id: Optional[str] = None, 
                               client_secret: Optional[str] = None) -> bool:
        """
        Complete OAuth2 authentication with authorization code
        
        Args:
            authorization_code: Code from OAuth callback
            client_id: Optional client ID
            client_secret: Optional client secret
            
        Returns:
            True if authentication successful
        """
        if client_id and client_secret:
            client_config = {
                "installed": {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                    "token_uri": "https://oauth2.googleapis.com/token",
                    "redirect_uris": [self.REDIRECT_URI]
                }
            }
        else:
            with open(self.credentials_path, 'r') as f:
                client_config = json.load(f)
        
        flow = Flow.from_client_config(
            client_config,
            scopes=self.SCOPES,
            redirect_uri=self.REDIRECT_URI
        )
        
        flow.fetch_token(code=authorization_code)
        
        # Save credentials
        self.creds = flow.credentials
        with open(self.token_path, 'w') as token:
            token.write(self.creds.to_json())
        
        # Build service
        self.service = build('calendar', 'v3', credentials=self.creds)
        return True
    
    def load_credentials(self) -> bool:
        """Load saved credentials from token file"""
        if not os.path.exists(self.token_path):
            return False
        
        try:
            self.creds = Credentials.from_authorized_user_file(self.token_path, self.SCOPES)
            
            # Refresh if expired
            if self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
                with open(self.token_path, 'w') as token:
                    token.write(self.creds.to_json())
            
            # Build service
            self.service = build('calendar', 'v3', credentials=self.creds)
            return True
        except Exception as e:
            print(f"Error loading credentials: {e}")
            return False
    
    def create_event(self, event: CalendarEvent, calendar_id: str = 'primary') -> Dict[str, Any]:
        """
        Create a single event in Google Calendar
        
        Args:
            event: CalendarEvent object
            calendar_id: Calendar ID (default: 'primary' for user's primary calendar)
            
        Returns:
            Created event dictionary
        """
        if not self.service:
            if not self.load_credentials():
                raise ValueError("Not authenticated. Call authenticate() first.")
        
        # Build description
        desc_parts = [event.description]
        if event.platform:
            desc_parts.append(f"\nPlatform: {event.platform}")
        if event.hashtags:
            desc_parts.append(f"\nHashtags: {', '.join(event.hashtags)}")
        if event.url:
            desc_parts.append(f"\nURL: {event.url}")
        if event.metadata:
            desc_parts.append(f"\nMetadata: {json.dumps(event.metadata)}")
        
        # Build event body
        event_body = {
            'summary': event.title,
            'description': '\n'.join(desc_parts),
            'start': {
                'dateTime': event.start_datetime.isoformat(),
                'timeZone': str(event.start_datetime.tzinfo) if event.start_datetime.tzinfo else 'UTC',
            },
            'end': {
                'dateTime': (event.end_datetime or event.start_datetime + timedelta(hours=1)).isoformat(),
                'timeZone': str(event.end_datetime.tzinfo) if event.end_datetime.tzinfo else 'UTC',
            },
        }
        
        if event.location:
            event_body['location'] = event.location
        
        if event.url:
            event_body['source'] = {'title': event.title, 'url': event.url}
        
        try:
            created_event = self.service.events().insert(
                calendarId=calendar_id,
                body=event_body
            ).execute()
            return created_event
        except HttpError as error:
            raise Exception(f"An error occurred: {error}")
    
    def create_events_batch(self, events: List[CalendarEvent], calendar_id: str = 'primary') -> List[Dict[str, Any]]:
        """
        Create multiple events in Google Calendar
        
        Args:
            events: List of CalendarEvent objects
            calendar_id: Calendar ID
            
        Returns:
            List of created event dictionaries
        """
        created_events = []
        for event in events:
            try:
                created = self.create_event(event, calendar_id)
                created_events.append(created)
            except Exception as e:
                print(f"Error creating event '{event.title}': {e}")
                # Continue with other events
        return created_events


class CalendarExportService:
    """
    Main service for exporting posts to calendars
    Handles both iCal export and Google Calendar API export
    """
    
    @staticmethod
    def parse_post_to_event(
        post: Dict[str, Any],
        default_time: Optional[datetime] = None,
        default_duration_hours: float = 1.0
    ) -> CalendarEvent:
        """
        Parse a post dictionary into a CalendarEvent
        
        Args:
            post: Dictionary containing post data with keys like:
                - content/text: Post content
                - scheduled_time/datetime/post_time: Scheduled datetime
                - platform/channel: Platform name
                - hashtags/tags: List of hashtags
                - url/link: Post URL
                - title: Post title (optional)
            default_time: Default time if not specified in post
            default_duration_hours: Default duration in hours
            
        Returns:
            CalendarEvent object
        """
        # Extract title
        title = post.get('title') or post.get('content', '')[:50] or 'Social Media Post'
        if len(title) > 100:
            title = title[:97] + "..."
        
        # Extract description/content
        description = post.get('content') or post.get('text') or post.get('description') or title
        
        # Extract scheduled time
        scheduled_time = None
        for key in ['scheduled_time', 'datetime', 'post_time', 'scheduled_at', 'publish_at']:
            if key in post and post[key]:
                time_val = post[key]
                if isinstance(time_val, str):
                    try:
                        scheduled_time = datetime.fromisoformat(time_val.replace('Z', '+00:00'))
                    except:
                        try:
                            scheduled_time = datetime.strptime(time_val, '%Y-%m-%d %H:%M:%S')
                        except:
                            pass
                elif isinstance(time_val, datetime):
                    scheduled_time = time_val
                if scheduled_time:
                    break
        
        if not scheduled_time:
            scheduled_time = default_time or datetime.now(timezone.utc)
        
        # Ensure timezone awareness
        if scheduled_time.tzinfo is None:
            scheduled_time = scheduled_time.replace(tzinfo=timezone.utc)
        
        # Calculate end time
        end_time = scheduled_time + timedelta(hours=default_duration_hours)
        if 'duration' in post:
            try:
                duration = float(post['duration'])
                end_time = scheduled_time + timedelta(hours=duration)
            except:
                pass
        
        # Extract other fields
        platform = post.get('platform') or post.get('channel') or post.get('network')
        location = post.get('location')
        url = post.get('url') or post.get('link') or post.get('permalink')
        
        # Extract hashtags
        hashtags = []
        if 'hashtags' in post:
            hashtags = post['hashtags'] if isinstance(post['hashtags'], list) else [post['hashtags']]
        elif 'tags' in post:
            hashtags = post['tags'] if isinstance(post['tags'], list) else [post['tags']]
        
        # Metadata
        metadata = {k: v for k, v in post.items() 
                   if k not in ['title', 'content', 'text', 'description', 'scheduled_time', 
                               'datetime', 'post_time', 'scheduled_at', 'publish_at', 
                               'platform', 'channel', 'network', 'location', 'url', 'link', 
                               'permalink', 'hashtags', 'tags', 'duration']}
        
        return CalendarEvent(
            title=title,
            description=description,
            start_datetime=scheduled_time,
            end_datetime=end_time,
            location=location,
            url=url,
            platform=platform,
            hashtags=hashtags if hashtags else None,
            metadata=metadata if metadata else None
        )
    
    @staticmethod
    @staticmethod
    def export_to_ical(
        posts: List[Dict[str, Any]],
        calendar_name: str = "JAN Studio Social Posts",
        output_path: Optional[str] = None
    ) -> str:
        """
        Export posts to iCal format
        
        Args:
            posts: List of post dictionaries
            calendar_name: Name for the calendar
            output_path: Optional path to save .ics file
            
        Returns:
            iCal content as string
        """
        events = [
            CalendarExportService.parse_post_to_event(post)
            for post in posts
        ]
        
        ical_content = ICalExporter.export_events(events, calendar_name)
        
        if output_path:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(ical_content)
        
        return ical_content
    
    @staticmethod
    def export_to_google_calendar(
        posts: List[Dict[str, Any]],
        calendar_id: str = 'primary',
        credentials_path: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Export posts directly to Google Calendar via API
        
        Args:
            posts: List of post dictionaries
            calendar_id: Google Calendar ID (default: 'primary')
            credentials_path: Path to OAuth2 credentials
            
        Returns:
            List of created event dictionaries
        """
        exporter = GoogleCalendarAPIExporter(credentials_path)
        
        if not exporter.load_credentials():
            raise ValueError(
                "Not authenticated with Google Calendar. "
                "Call authenticate() and complete_authentication() first, "
                "or save credentials to token file."
            )
        
        events = [
            CalendarExportService.parse_post_to_event(post)
            for post in posts
        ]
        
        return exporter.create_events_batch(events, calendar_id)


# Convenience functions
def export_posts_to_ical(posts: List[Dict[str, Any]], output_file: str = "social_posts.ics") -> str:
    """Quick export function for iCal format"""
    service = CalendarExportService()
    return service.export_to_ical(posts, output_path=output_file)
