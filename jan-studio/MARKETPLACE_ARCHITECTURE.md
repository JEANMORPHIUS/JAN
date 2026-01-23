# Marketplace Architecture

**Complete marketplace infrastructure for sharing JAN personas.**

---

## Database Schema (SQLite)

### Tables

#### 1. `users`
- `id` (INTEGER PRIMARY KEY)
- `username` (TEXT UNIQUE)
- `email` (TEXT UNIQUE)
- `created_at` (TIMESTAMP)

#### 2. `personas`
- `id` (INTEGER PRIMARY KEY)
- `name` (TEXT UNIQUE)
- `author_id` (INTEGER, FK → users.id)
- `description` (TEXT)
- `category` (TEXT)
- `downloads` (INTEGER, DEFAULT 0)
- `rating` (REAL, DEFAULT 0.0)
- `rating_count` (INTEGER, DEFAULT 0)
- `version` (TEXT, DEFAULT '1.0.0')
- `status` (TEXT, DEFAULT 'pending')
- `created_at` (TIMESTAMP)
- `updated_at` (TIMESTAMP)

#### 3. `persona_files`
- `id` (INTEGER PRIMARY KEY)
- `persona_id` (INTEGER, FK → personas.id)
- `file_path` (TEXT)
- `file_content` (TEXT)
- `version` (TEXT, DEFAULT '1.0.0')
- `created_at` (TIMESTAMP)
- UNIQUE(persona_id, file_path, version)

#### 4. `downloads`
- `id` (INTEGER PRIMARY KEY)
- `user_id` (INTEGER, FK → users.id, nullable)
- `persona_id` (INTEGER, FK → personas.id)
- `timestamp` (TIMESTAMP)

#### 5. `ratings`
- `id` (INTEGER PRIMARY KEY)
- `user_id` (INTEGER, FK → users.id, nullable)
- `persona_id` (INTEGER, FK → personas.id)
- `rating` (INTEGER, 1-5)
- `comment` (TEXT, nullable)
- `created_at` (TIMESTAMP)
- UNIQUE(user_id, persona_id)

### Indexes

- `idx_personas_author` on `personas(author_id)`
- `idx_personas_category` on `personas(category)`
- `idx_personas_status` on `personas(status)`
- `idx_downloads_persona` on `downloads(persona_id)`
- `idx_ratings_persona` on `ratings(persona_id)`

---

## API Endpoints

### Backend File: `backend/marketplace_api.py`

#### 1. `GET /api/marketplace/personas`
**Browse personas**

**Query Parameters:**
- `category` (optional) - Filter by category
- `status` (default: "approved") - Filter by status
- `limit` (default: 50, max: 100) - Results per page
- `offset` (default: 0) - Pagination offset
- `sort_by` (default: "downloads") - Sort field

**Response:** `List[PersonaResponse]`

#### 2. `GET /api/marketplace/personas/{persona_id}`
**Get persona details**

**Response:**
```json
{
  "persona": PersonaResponse,
  "files": [...],
  "ratings": [...]
}
```

#### 3. `POST /api/marketplace/personas`
**Submit new persona**

**Request:**
```json
{
  "name": "string",
  "author_username": "string",
  "author_email": "string",
  "description": "string",
  "category": "string (optional)",
  "files": [
    {"path": "profile.md", "content": "..."}
  ]
}
```

**Response:**
```json
{
  "message": "Persona submitted successfully",
  "persona_id": 1,
  "status": "pending"
}
```

#### 4. `POST /api/marketplace/personas/{persona_id}/download`
**Download persona**

**Request:**
```json
{
  "user_id": 1 (optional),
  "username": "string" (optional)
}
```

**Response:**
```json
{
  "message": "Download successful",
  "persona": PersonaResponse,
  "files": [...]
}
```

#### 5. `POST /api/marketplace/personas/{persona_id}/rate`
**Rate persona**

**Request:**
```json
{
  "user_id": 1 (optional),
  "username": "string" (optional),
  "rating": 1-5,
  "comment": "string" (optional)
}
```

**Response:**
```json
{
  "message": "Rating submitted successfully",
  "persona": PersonaResponse
}
```

#### 6. `GET /api/marketplace/categories`
**Get available categories**

**Response:** `List[str]`

---

## Frontend Pages

### 1. `/marketplace` - Browse Grid

**File:** `frontend/src/pages/marketplace/index.tsx`

**Features:**
- Grid layout of persona cards
- Category filter dropdown
- Sort by (downloads, rating, date)
- Search (future)
- "Submit Persona" button
- Persona cards show:
  - Name
  - Author
  - Description (truncated)
  - Rating and download count
  - Category badge
  - Version and date

**Layout:**
```
┌─────────────────────────────────────────┐
│ Header: JAN Marketplace                │
├─────────────────────────────────────────┤
│ Filters: Category | Sort | Submit      │
├─────────────────────────────────────────┤
│ [Card] [Card] [Card]                   │
│ [Card] [Card] [Card]                   │
│ [Card] [Card] [Card]                   │
└─────────────────────────────────────────┘
```

### 2. `/marketplace/{id}` - Detail Page

**File:** `frontend/src/pages/marketplace/[id].tsx`

**Features:**
- Full persona information
- File list with versions
- Ratings and reviews
- Download button
- Rate this persona form
- Stats sidebar:
  - Rating
  - Downloads
  - Category
  - Version
  - Created date

**Layout:**
```
┌─────────────────────────────────────────┐
│ Header: Persona Name | Back            │
├──────────────┬──────────────────────────┤
│ Main Content │ Sidebar                  │
│              │                          │
│ Description  │ Stats                    │
│ Files        │ Download Button          │
│ Ratings      │ Rate Form                │
└──────────────┴──────────────────────────┘
```

### 3. `/marketplace/submit` - Submit Form

**File:** `frontend/src/pages/marketplace/submit.tsx`

**Features:**
- Load from existing persona (pre-fill)
- Persona information form:
  - Name (required)
  - Description (required)
  - Category (optional)
- Author information:
  - Username (required)
  - Email (required)
- Submit button
- Validation

**Layout:**
```
┌─────────────────────────────────────────┐
│ Header: Submit Persona | Back           │
├─────────────────────────────────────────┤
│ Load from Existing Persona              │
├─────────────────────────────────────────┤
│ Persona Information                     │
│ - Name                                  │
│ - Description                           │
│ - Category                              │
├─────────────────────────────────────────┤
│ Author Information                      │
│ - Username                              │
│ - Email                                 │
├─────────────────────────────────────────┤
│ [Submit] [Cancel]                       │
└─────────────────────────────────────────┘
```

---

## Database Operations

### File: `backend/marketplace_db.py`

**Functions:**
- `init_database()` - Initialize schema
- `get_user_by_username()` - Get user
- `create_user()` - Create user
- `get_persona()` - Get persona by ID
- `list_personas()` - List with filters
- `create_persona()` - Create persona
- `get_persona_files()` - Get files
- `record_download()` - Record download
- `add_rating()` - Add/update rating
- `get_ratings()` - Get all ratings

**Context Manager:**
- `get_db()` - Database connection manager

---

## Integration Points

### With Existing JAN Studio

1. **Persona Loading:**
   - Submit form can load from local personas
   - Uses existing `getPersonas()` and `getPersonaFiles()` APIs

2. **File Structure:**
   - Marketplace stores files as JSON
   - Downloads return file structure
   - Compatible with JAN file format

3. **User Management:**
   - Simple username/email system
   - No authentication yet (future)
   - Anonymous downloads/ratings supported

---

## Status Workflow

### Persona Statuses

1. **pending** - Submitted, awaiting review
2. **approved** - Published and available
3. **rejected** - Not approved (future)
4. **archived** - Removed from marketplace (future)

---

## Features

### ✅ Implemented

- Database schema (SQLite)
- API endpoints (FastAPI)
- Browse page (grid layout)
- Detail page (full info)
- Submit page (form)
- Download tracking
- Rating system
- Category filtering
- Sorting options

### 🔄 Future Enhancements

- Authentication system
- Admin review panel
- Search functionality
- User profiles
- Comments/discussions
- Version history
- Fork/clone personas
- Analytics dashboard

---

## Files Created

```
jan-studio/
├── backend/
│   ├── marketplace_db.py      ✅ NEW
│   └── marketplace_api.py     ✅ NEW
├── frontend/src/
│   ├── pages/marketplace/
│   │   ├── index.tsx          ✅ NEW
│   │   ├── [id].tsx           ✅ NEW
│   │   └── submit.tsx         ✅ NEW
│   └── api/
│       └── marketplace.ts     ✅ NEW
└── MARKETPLACE_ARCHITECTURE.md ✅ NEW
```

---

## Setup Instructions

### 1. Initialize Database

```python
from backend.marketplace_db import init_database
init_database()
```

Or it auto-initializes on import.

### 2. Register API Router

In your FastAPI app:

```python
from backend.marketplace_api import router as marketplace_router
app.include_router(marketplace_router)
```

### 3. Frontend Routes

Next.js will automatically handle:
- `/marketplace` → `pages/marketplace/index.tsx`
- `/marketplace/[id]` → `pages/marketplace/[id].tsx`
- `/marketplace/submit` → `pages/marketplace/submit.tsx`

---

## Status

✅ **Database schema complete**  
✅ **API endpoints implemented**  
✅ **Frontend pages built**  
✅ **Integration with JAN Studio**  
⚠️ **No content yet (empty marketplace)**

**Ready for:** Content submission and testing

---

**Last Updated:** 2025-01-27  
**Version:** 0.4.0

