# Google Calendar Export Service

**Mission:** "THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS"  
**Purpose:** Export social media posts to Google Calendar for scheduling and planning

---

## Overview

This service provides two methods for exporting posts to Google Calendar:

1. **iCal Export (.ics files)** - Universal format compatible with all calendar apps
   - Works with Google Calendar, Apple Calendar, Outlook, etc.
   - No authentication required
   - Can be imported manually

2. **Google Calendar API Export** - Direct integration with Google Calendar
   - Creates events directly in your calendar
   - Requires OAuth2 authentication
   - Automatic event creation

---

## Quick Start

### Method 1: iCal Export (Recommended - No Auth Needed)

```python
from google_calendar_exporter import CalendarExportService

# Your posts data
posts = [
    {
        "title": "Morning Motivation",
        "content": "Start your day with purpose! 💪",
        "scheduled_time": "2025-01-28T09:00:00Z",
        "platform": "Instagram",
        "hashtags": ["motivation", "dailyinspiration"]
    },
    {
        "content": "Check out our latest blog post...",
        "scheduled_time": "2025-01-28T14:00:00Z",
        "platform": "Twitter",
        "url": "https://example.com/blog"
    }
]

# Export to iCal
service = CalendarExportService()
ical_content = service.export_to_ical(
    posts,
    calendar_name="My Social Posts"
)

# Save to file
with open("social_posts.ics", "w") as f:
    f.write(ical_content)

# Or use convenience function
from google_calendar_exporter import export_posts_to_ical
export_posts_to_ical(posts, "social_posts.ics")
```

**To use in Google Calendar:**
1. Generate the `.ics` file
2. Open Google Calendar
3. Click the gear icon → Settings
4. Scroll to "Import & Export"
5. Click "Import"
6. Select your `.ics` file
7. Choose which calendar to import to
8. Click "Import"

### Method 2: Google Calendar API (Direct Integration)

**Step 1: Get Google API Credentials**

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing
3. Enable Google Calendar API:
   - Go to "APIs & Services" → "Library"
   - Search for "Google Calendar API"
   - Click "Enable"
4. Create OAuth2 credentials:
   - Go to "APIs & Services" → "Credentials"
   - Click "Create Credentials" → "OAuth client ID"
   - Choose "Desktop app" as application type
   - Download the JSON file
   - Save it as `google_credentials.json` in your project

**Step 2: Authenticate**

```python
from google_calendar_exporter import GoogleCalendarAPIExporter

exporter = GoogleCalendarAPIExporter("google_credentials.json")

# Get authorization URL
auth_url = exporter.authenticate()
print(f"Visit this URL: {auth_url}")

# After visiting URL, you'll get an authorization code
# Paste it here:
auth_code = input("Enter authorization code: ")

# Complete authentication
exporter.complete_authentication(auth_code)
print("Authentication complete! Credentials saved.")
```

**Step 3: Export Posts**

```python
from google_calendar_exporter import CalendarExportService

posts = [
    {
        "content": "Monday motivation post",
        "scheduled_time": "2025-01-28T09:00:00Z",
        "platform": "Instagram"
    }
]

service = CalendarExportService()
created_events = service.export_to_google_calendar(
    posts,
    calendar_id="primary"  # or specific calendar ID
)

print(f"Created {len(created_events)} events in Google Calendar!")
```

---

## API Endpoints

### POST `/api/calendar/export/ical`

Export posts to iCal format (file download).

**Request:**
```json
{
  "posts": [
    {
      "content": "Post content here",
      "scheduled_time": "2025-01-28T09:00:00Z",
      "platform": "Instagram",
      "hashtags": ["tag1", "tag2"],
      "url": "https://example.com/post"
    }
  ],
  "calendar_name": "My Social Posts",
  "output_filename": "posts.ics"
}
```

**Response:** Downloads `.ics` file

### POST `/api/calendar/export/ical/json`

Export posts to iCal format (JSON response with base64 content).

**Response:**
```json
{
  "success": true,
  "filename": "posts.ics",
  "ical_content": "BEGIN:VCALENDAR...",
  "ical_base64": "QkVHSU46VkNBTEVOREFS...",
  "event_count": 5,
  "calendar_name": "My Social Posts"
}
```

### POST `/api/calendar/google/auth/start`

Start Google Calendar OAuth authentication.

**Response:**
```json
{
  "success": true,
  "authorization_url": "https://accounts.google.com/o/oauth2/auth?..."
}
```

Visit the `authorization_url`, grant permissions, then use the code with `/google/auth/complete`.

### POST `/api/calendar/google/auth/complete`

Complete Google Calendar OAuth authentication.

**Request:**
```json
{
  "authorization_code": "4/0AY0e-g7..."
}
```

**Response:**
```json
{
  "success": true,
  "message": "Authentication successful. Credentials saved."
}
```

### POST `/api/calendar/export/google`

Export posts directly to Google Calendar.

**Request:**
```json
{
  "posts": [
    {
      "content": "Post content",
      "scheduled_time": "2025-01-28T09:00:00Z",
      "platform": "Instagram"
    }
  ],
  "calendar_id": "primary"
}
```

**Response:**
```json
{
  "success": true,
  "events_created": 1,
  "events": [...],
  "message": "Successfully created 1 event(s) in Google Calendar"
}
```

### GET `/api/calendar/google/calendars`

List all available Google Calendars.

**Response:**
```json
{
  "success": true,
  "calendars": [
    {
      "id": "primary",
      "name": "Your Name",
      "description": "",
      "primary": true
    }
  ]
}
```

---

## Post Data Format

Posts can include the following fields:

```python
{
    "title": "Optional title (defaults to first 50 chars of content)",
    "content": "Post content/text (required)",
    "scheduled_time": "2025-01-28T09:00:00Z",  # ISO format datetime
    "platform": "Instagram",  # e.g., Instagram, Twitter, Facebook
    "hashtags": ["tag1", "tag2"],
    "url": "https://example.com/post",
    "location": "Optional location",
    "duration": 1.0,  # Duration in hours (default: 1 hour)
    "metadata": {  # Any additional data
        "post_id": "123",
        "campaign": "Q1 2025"
    }
}
```

**Supported datetime formats:**
- ISO format: `"2025-01-28T09:00:00Z"`
- ISO with timezone: `"2025-01-28T09:00:00+00:00"`
- Simple format: `"2025-01-28 09:00:00"` (assumes UTC)

**Platform examples:**
- Instagram
- Twitter/X
- Facebook
- LinkedIn
- TikTok
- YouTube
- Any custom platform name

---

## Frontend Integration

### JavaScript/TypeScript Example

```typescript
// Export to iCal
async function exportToICal(posts: Post[]) {
  const response = await fetch('/api/calendar/export/ical', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      posts: posts,
      calendar_name: 'Social Media Posts'
    })
  });
  
  // Download file
  const blob = await response.blob();
  const url = window.URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'social_posts.ics';
  a.click();
}

// Export to Google Calendar (after authentication)
async function exportToGoogleCalendar(posts: Post[]) {
  // Check authentication first
  const authStatus = await fetch('/api/calendar/google/auth/status');
  const { authenticated } = await authStatus.json();
  
  if (!authenticated) {
    // Start auth flow
    const authResponse = await fetch('/api/calendar/google/auth/start', {
      method: 'POST'
    });
    const { authorization_url } = await authResponse.json();
    
    // Open auth URL in popup
    window.open(authorization_url, 'Google Auth', 'width=500,height=600');
    
    // After user completes auth, call export
    return;
  }
  
  // Export posts
  const response = await fetch('/api/calendar/export/google', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      posts: posts,
      calendar_id: 'primary'
    })
  });
  
  const result = await response.json();
  console.log(`Created ${result.events_created} events!`);
}
```

---

## Installation

```bash
# Install required packages
pip install -r requirements.txt

# Google Calendar API libraries are optional
# iCal export works without them
```

---

## Troubleshooting

### iCal Export Issues

**Problem:** Events don't appear in calendar after import

**Solutions:**
- Ensure datetime format is correct (ISO format recommended)
- Check timezone (events are stored in UTC)
- Verify the `.ics` file is valid (open in text editor, check format)
- Try importing to a different calendar app first

### Google Calendar API Issues

**Problem:** "Not authenticated" error

**Solution:**
- Run authentication flow again (`/google/auth/start` → `/google/auth/complete`)
- Check that `google_token.json` exists and is valid
- Verify OAuth credentials are correct

**Problem:** "Insufficient permissions" error

**Solution:**
- Delete `google_token.json` and re-authenticate
- Ensure you granted calendar access during OAuth

**Problem:** Events created but not visible

**Solution:**
- Check which calendar ID you're using (`primary` vs specific calendar)
- Verify events in Google Calendar web interface
- Check calendar visibility settings

---

## Best Practices

1. **Use iCal export for one-time exports** - Simple, no auth needed
2. **Use Google API for automation** - Better for recurring exports
3. **Always include `scheduled_time`** - Required for proper scheduling
4. **Use ISO datetime format** - Most reliable across systems
5. **Include platform info** - Helps with organization
6. **Add hashtags** - Useful for filtering/searching
7. **Set appropriate duration** - Default is 1 hour, adjust as needed

---

## Example: Exporting Campaign Posts

```python
from google_calendar_exporter import CalendarExportService
from datetime import datetime, timedelta, timezone

# Campaign posts
campaign_posts = [
    {
        "content": "Week 1: Launch announcement",
        "scheduled_time": (datetime.now(timezone.utc) + timedelta(days=1)).isoformat(),
        "platform": "Instagram",
        "hashtags": ["launch", "newproduct"]
    },
    {
        "content": "Week 2: Feature highlight",
        "scheduled_time": (datetime.now(timezone.utc) + timedelta(days=8)).isoformat(),
        "platform": "Twitter",
        "url": "https://example.com/feature"
    }
]

# Export
service = CalendarExportService()
ical_file = service.export_to_ical(
    campaign_posts,
    calendar_name="Q1 2025 Campaign",
    output_path="campaign.ics"
)

print(f"Exported {len(campaign_posts)} posts to campaign.ics")
```

---

## Alignment with Mission

This service honors:
- **Sacred weight of time** - Respecting scheduled moments
- **Community stewardship** - Making scheduling accessible
- **Energy efficiency** - Streamlined export process
- **We all win** - Works with any calendar system

**Energy + Love = We All Win** 🕊️

---

**Document Version:** 1.0  
**Last Updated:** 2025-01-27
