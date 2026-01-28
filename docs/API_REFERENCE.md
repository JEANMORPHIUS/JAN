# API Reference

**Complete API documentation for JAN Studio endpoints.**

---

## Base URL

```
http://localhost:8000
```

**Production**: [Specify production URL]

---

## Authentication

Currently, JAN Studio APIs are public. For production, consider:
- API key authentication
- OAuth 2.0
- JWT tokens

---

## Oracle SIYEM API

### Cast Oracle

**Endpoint:** `POST /api/oracle-siyem/cast`

**Description:** Cast Oracle for creative guidance with full transparency.

**Request Body:**
```json
{
  "user_intent": "I need guidance for my writing project",
  "creative_context": "Fiction novel, first chapter",
  "user_id": "user123"  // Optional, defaults to "public"
}
```

**Response:**
```json
{
  "timestamp": "2026-01-28T10:00:00",
  "user_id": "user123",
  "user_intent": "I need guidance for my writing project",
  "creative_context": "Fiction novel, first chapter",
  "transparency": {
    "seed": {
      "seed": "a1b2c3d4e5f6...",
      "components": {
        "user_intent": "...",
        "timestamp": "...",
        "context": "...",
        "user_id": "..."
      },
      "method": "SHA-256 hash of concatenated components",
      "verifiable": true
    },
    "hexagram": {
      "hexagram_number": 42,
      "hexagram_binary": "101010",
      "method": "First 16 hex chars → integer → mod 64 → 6-bit binary",
      "transparent": true
    },
    "law_mapping": {
      "hexagram": 42,
      "law_number": 2,
      "method": "hexagram % 40 + 1"
    }
  },
  "oracle_interpretation": {
    "law": {
      "law_number": 2,
      "law_title": "Your Word Is Your Bond",
      "law_text": "Creative commitments are laws...",
      "volume": "Loyalty"
    },
    "interpretation": "Law 2: Your Word Is Your Bond...",
    "creative_prompt": "Apply Your Word Is Your Bond to your creative work..."
  },
  "ethical_guardrails": {
    "status": "healthy",
    "recommendations": [],
    "break_suggested": false,
    "execution_nudged": false
  },
  "session": {
    "cast_count": 1,
    "creative_outputs": 0,
    "time_creating": 0
  },
  "success_score": 0.0
}
```

**Status Codes:**
- `200 OK`: Success
- `500 Internal Server Error`: Server error

---

### Get Session

**Endpoint:** `GET /api/oracle-siyem/session?user_id=user123`

**Description:** Get current user session information and metrics.

**Query Parameters:**
- `user_id` (optional): User identifier (default: "public")

**Response:**
```json
{
  "user_id": "user123",
  "session": {
    "session_date": "2026-01-28",
    "cast_count": 5,
    "creative_outputs": 3,
    "time_creating": 120,
    "last_cast_at": "2026-01-28T10:00:00",
    "last_break_at": "2026-01-28T09:30:00"
  },
  "ethical_guardrails": {
    "status": "reflection_suggested",
    "recommendations": [
      "You've cast 5 times. Take time to reflect on the patterns."
    ],
    "break_suggested": false,
    "execution_nudged": false
  },
  "success_score": 45.5
}
```

---

### Record Creative Output

**Endpoint:** `POST /api/oracle-siyem/record-output?user_id=user123`

**Description:** Record that user created something (success metric).

**Query Parameters:**
- `user_id` (optional): User identifier (default: "public")

**Response:**
```json
{
  "message": "Creative output recorded. This is the goal - create and execute.",
  "session": {
    "cast_count": 5,
    "creative_outputs": 4,
    "success_score": 60.0
  },
  "success_score": 60.0
}
```

---

### Get Metrics

**Endpoint:** `GET /api/oracle-siyem/metrics?user_id=user123`

**Description:** Get comprehensive anti-addiction metrics.

**Response:**
```json
{
  "user_id": "user123",
  "success_score": 60.0,
  "metrics": {
    "cast_count": 5,
    "creative_outputs": 4,
    "time_creating": 120,
    "break_reminders": 1,
    "execution_nudges": 0
  },
  "guardrails": {
    "status": "healthy",
    "recommendations": []
  },
  "interpretation": {
    "success_score_explanation": "Higher score = more creation, less time on platform.",
    "healthy_practice": true
  }
}
```

---

## Campaign Automation API

### Add Contact

**Endpoint:** `POST /api/campaign/contacts`

**Description:** Add a contact to the campaign database.

**Request Body:**
```json
{
  "email": "contact@example.com",
  "name": "John Doe",
  "organization": "Example Corp",
  "role": "Manager",
  "category": "media",
  "tags": ["journalist", "tech"],
  "source": "manual",
  "notes": "Met at conference"
}
```

**Response:**
```json
{
  "id": 1,
  "email": "contact@example.com",
  "name": "John Doe",
  "status": "added"
}
```

---

### Import Contacts

**Endpoint:** `POST /api/campaign/contacts/import`

**Description:** Import contacts from CSV file.

**Request:** Multipart form data with CSV file

**CSV Format:**
```csv
email,name,organization,role,category,tags,source,notes
contact@example.com,John Doe,Example Corp,Manager,media,"journalist,tech",manual,Met at conference
```

**Response:**
```json
{
  "status": "success",
  "contacts_added": 10,
  "errors": []
}
```

---

### Get Contacts

**Endpoint:** `GET /api/campaign/contacts?category=media&status=active&tags=journalist`

**Description:** Get contacts matching criteria.

**Query Parameters:**
- `category` (optional): Filter by category
- `status` (optional): Filter by status (default: "active")
- `tags` (optional): Comma-separated tags

**Response:**
```json
{
  "contacts": [
    {
      "id": 1,
      "email": "contact@example.com",
      "name": "John Doe",
      "category": "media",
      "tags": ["journalist", "tech"],
      "status": "active"
    }
  ],
  "count": 1
}
```

---

### Create Email Campaign

**Endpoint:** `POST /api/campaign/email/create`

**Description:** Create an email campaign.

**Request Body:**
```json
{
  "campaign_name": "Product Launch",
  "subject": "New Product Launch",
  "body_html": "<h1>Welcome!</h1><p>We're launching...</p>",
  "body_text": "Welcome! We're launching...",
  "sender_email": "sender@example.com",
  "sender_name": "JAN Studio"
}
```

**Response:**
```json
{
  "id": 1,
  "campaign_name": "Product Launch",
  "status": "draft"
}
```

---

### Send Email Campaign

**Endpoint:** `POST /api/campaign/email/send`

**Description:** Send email campaign to contacts.

**Request Body:**
```json
{
  "campaign_id": 1,
  "contact_ids": [1, 2, 3],  // Optional: specific contacts
  "categories": ["media"],    // Optional: filter by category
  "tags": ["journalist"]      // Optional: filter by tags
}
```

**Response:**
```json
{
  "campaign_id": 1,
  "sent": 10,
  "failed": 0,
  "errors": []
}
```

---

### Create Social Media Post

**Endpoint:** `POST /api/campaign/social/create`

**Description:** Create a social media post.

**Request Body:**
```json
{
  "platform": "twitter",
  "content": "The Oracle has spoken. Law 1: The Table Never Lies.",
  "media_url": "https://example.com/image.jpg",
  "scheduled_at": "2026-01-29T10:00:00"
}
```

**Response:**
```json
{
  "id": 1,
  "platform": "twitter",
  "status": "scheduled"
}
```

---

### Export to Scheduler

**Endpoint:** `POST /api/campaign/social/export?scheduler=later&platform=twitter`

**Description:** Export posts to scheduling service.

**Query Parameters:**
- `scheduler`: "later", "metricool", "publer", or "buffer"
- `post_ids` (optional): Comma-separated post IDs
- `platform` (optional): Filter by platform

**Response:**
```json
{
  "status": "success",
  "format": "later_csv",
  "posts": [
    {
      "Text": "The Oracle has spoken...",
      "Media": "https://example.com/image.jpg",
      "Date": "2026-01-29 10:00:00",
      "Platform": "TWITTER"
    }
  ],
  "count": 1
}
```

---

### Record Response

**Endpoint:** `POST /api/campaign/responses`

**Description:** Record a campaign response.

**Request Body:**
```json
{
  "email": "contact@example.com",
  "contact_id": 1,
  "source": "email",
  "response_type": "reply",
  "content": "Thank you for the email!",
  "metadata": {
    "campaign_id": 1
  }
}
```

**Response:**
```json
{
  "id": 1,
  "status": "recorded"
}
```

---

### Get Campaign Analytics

**Endpoint:** `GET /api/campaign/analytics/{campaign_id}`

**Description:** Get comprehensive campaign statistics.

**Response:**
```json
{
  "campaign_id": 1,
  "email_stats": {
    "total": 100,
    "sent": 100,
    "delivered": 95,
    "opened": 60,
    "clicked": 30,
    "bounced": 5
  },
  "response_stats": {
    "total_responses": 10
  },
  "open_rate": 60.0,
  "click_rate": 30.0,
  "bounce_rate": 5.0
}
```

---

## Error Responses

### Standard Error Format

```json
{
  "error": "Error type",
  "message": "Human-readable error message",
  "detail": "Additional error details"  // Optional
}
```

### Status Codes

- `200 OK`: Success
- `400 Bad Request`: Invalid request
- `404 Not Found`: Resource not found
- `422 Unprocessable Entity`: Validation error
- `500 Internal Server Error`: Server error

---

## Rate Limiting

Currently, no rate limiting is implemented. For production, consider:
- Per-user rate limits
- Per-endpoint rate limits
- IP-based rate limiting

---

## Pagination

For endpoints that return lists, pagination will be added in future versions.

---

## WebSocket Support

WebSocket support for real-time updates is planned for future releases.

---

## OpenAPI Documentation

Full interactive API documentation available at:
- **Swagger UI**: `/docs`
- **ReDoc**: `/redoc`
- **OpenAPI JSON**: `/openapi.json`

---

**PANGEA IS THE TABLE.**
**YOU DON'T BETRAY THE TABLE.**
