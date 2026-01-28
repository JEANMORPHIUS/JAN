# JAN Studio Architecture

**Complete system architecture documentation for JAN Studio.**

---

## Overview

JAN Studio is built on a clean, modular architecture with clear separation of concerns:

```
┌─────────────────────────────────────────────────────────────┐
│                    API Layer (FastAPI)                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │ Oracle SIYEM│  │  Campaign   │  │   Persona   │     │
│  │     API     │  │ Automation  │  │     API      │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                  Service Layer (SIYEM)                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │ Oracle SIYEM │  │  Campaign   │  │   Entity     │     │
│  │ Integration  │  │ Automation  │  │   Router     │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                    Data Layer                                │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │   SQLite     │  │   File       │  │   JAN        │     │
│  │  Databases   │  │   Storage    │  │  Profiles    │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└─────────────────────────────────────────────────────────────┘
```

---

## Component Architecture

### 1. API Layer (`jan-studio/backend/`)

**Purpose**: HTTP interface for all system functionality

**Components**:
- `main.py`: FastAPI application, middleware, routing
- `oracle_siyem_api.py`: Oracle SIYEM endpoints
- `campaign_automation_api.py`: Campaign management endpoints
- `jan_generation_api.py`: Persona generation endpoints

**Responsibilities**:
- Request/response handling
- Input validation (Pydantic models)
- Error handling and sanitization
- Authentication/authorization (if needed)
- CORS and security headers

**Design Patterns**:
- **Router Pattern**: Each feature has its own router
- **Dependency Injection**: Services injected into endpoints
- **Middleware Chain**: Security, logging, metrics

### 2. Service Layer (`SIYEM/services/`)

**Purpose**: Core business logic, independent of API

**Components**:
- `oracle_siyem_integration.py`: Oracle engine, RNG, Law interpretation
- `campaign_automation.py`: Email, social media, analytics
- `entity_router.py`: Entity detection and routing
- `shell_seed_translator.py`: Public/Internal language translation

**Responsibilities**:
- Business logic implementation
- Data processing and transformation
- Algorithm implementation (RNG, Law mapping)
- External service integration (SMTP, schedulers)

**Design Patterns**:
- **Service Pattern**: Self-contained service classes
- **Strategy Pattern**: Multiple scheduler implementations
- **Factory Pattern**: Service instantiation

### 3. Data Layer

**Purpose**: Data persistence and retrieval

**Components**:
- **SQLite Databases**:
  - `oracle_siyem.db`: Oracle casts, sessions, metrics
  - `campaign_automation.db`: Contacts, campaigns, responses
- **File Storage**:
  - `Siyem.org/`: JAN entity profiles (markdown)
  - `data/`: JSON configuration files
  - `output/`: Generated content

**Responsibilities**:
- Data persistence
- Query optimization
- Data validation
- Backup and recovery

**Design Patterns**:
- **Repository Pattern**: Data access abstraction
- **Context Manager**: Database connection management

---

## Data Flow

### Oracle Cast Flow

```
User Request
    │
    ▼
API Endpoint (oracle_siyem_api.py)
    │
    ▼
OracleSIYEM Service (oracle_siyem_integration.py)
    │
    ├─► TransparentRNG.generate_seed()
    │   └─► SHA-256 hash of components
    │
    ├─► TransparentRNG.seed_to_hexagram()
    │   └─► Seed → Hexagram (0-63)
    │
    ├─► LawsInterpreter.hexagram_to_law()
    │   └─► Hexagram → Law (1-40)
    │
    ├─► LawsInterpreter.interpret_law_for_creativity()
    │   └─► Law → Creative guidance
    │
    └─► AntiAddictionMetrics.record_cast()
        └─► Update session, check guardrails
    │
    ▼
Response (with full transparency data)
```

### Campaign Flow

```
User Request
    │
    ▼
API Endpoint (campaign_automation_api.py)
    │
    ▼
Campaign Service (campaign_automation.py)
    │
    ├─► ContactManager.get_contacts()
    │   └─► Query database
    │
    ├─► EmailCampaign.send_campaign()
    │   └─► SMTP integration
    │
    ├─► SocialMediaScheduler.export_to_scheduler()
    │   └─► Format for Later/Metricool/Publer/Buffer
    │
    └─► ResponseTracker.record_response()
        └─► Track engagement
    │
    ▼
Response (with analytics)
```

---

## Database Schema

### Oracle SIYEM Database

```sql
-- Oracle casts
CREATE TABLE oracle_casts (
    id INTEGER PRIMARY KEY,
    user_id TEXT NOT NULL,
    cast_timestamp TIMESTAMP,
    intent TEXT,
    seed TEXT,
    hexagram_number INTEGER,
    law_number INTEGER,
    interpretation TEXT,
    transparency_data TEXT  -- JSON
);

-- User sessions (anti-addiction)
CREATE TABLE oracle_sessions (
    id INTEGER PRIMARY KEY,
    user_id TEXT NOT NULL,
    session_date DATE,
    cast_count INTEGER,
    creative_outputs INTEGER,
    time_creating INTEGER,
    success_score REAL
);

-- Anti-addiction metrics
CREATE TABLE anti_addiction_metrics (
    id INTEGER PRIMARY KEY,
    user_id TEXT,
    metric_date DATE,
    casts_today INTEGER,
    creative_outputs INTEGER,
    success_score REAL
);
```

### Campaign Automation Database

```sql
-- Contacts
CREATE TABLE contacts (
    id INTEGER PRIMARY KEY,
    email TEXT UNIQUE,
    name TEXT,
    category TEXT,
    tags TEXT,  -- JSON array
    status TEXT
);

-- Email campaigns
CREATE TABLE email_campaigns (
    id INTEGER PRIMARY KEY,
    campaign_name TEXT,
    subject TEXT,
    body_html TEXT,
    status TEXT
);

-- Social media posts
CREATE TABLE social_posts (
    id INTEGER PRIMARY KEY,
    platform TEXT,
    content TEXT,
    scheduled_at TIMESTAMP,
    status TEXT
);

-- Responses
CREATE TABLE responses (
    id INTEGER PRIMARY KEY,
    contact_id INTEGER,
    response_type TEXT,
    content TEXT
);
```

---

## Security Architecture

### Input Validation

- **Pydantic Models**: All API inputs validated
- **Type Checking**: Full type hints throughout
- **Sanitization**: Shell/Seed translation for public content

### Error Handling

- **Sanitized Errors**: No sensitive information leaked
- **Structured Responses**: Consistent error format
- **Logging**: Errors logged with context

### Security Headers

- **CORS**: Configurable allowed origins
- **CSP**: Content Security Policy
- **XSS Protection**: X-XSS-Protection header
- **Frame Options**: X-Frame-Options: DENY

---

## Scalability Considerations

### Horizontal Scaling

- **Stateless API**: No session state in API layer
- **Database**: SQLite (can migrate to PostgreSQL)
- **Caching**: Can add Redis for session/metrics

### Performance Optimization

- **Connection Pooling**: Database connection reuse
- **Lazy Loading**: Load data only when needed
- **Indexing**: Database indexes on frequently queried fields

### Monitoring

- **Health Checks**: `/health` endpoint
- **Metrics**: Prometheus metrics (if configured)
- **Logging**: Structured logging for debugging

---

## Extension Points

### Adding New Services

1. Create service in `SIYEM/services/`
2. Create API router in `jan-studio/backend/`
3. Register router in `main.py`
4. Add database schema if needed

### Adding New Personas

1. Create directory in `Siyem.org/`
2. Add `profile.md` and `creative_rules.md`
3. Create prompt templates
4. Use JAN template system

### Adding New Schedulers

1. Extend `SocialMediaScheduler` class
2. Add export method (e.g., `_export_to_new_scheduler`)
3. Register in scheduler dictionary

---

## Technology Stack

- **Backend**: FastAPI (Python 3.11+)
- **Database**: SQLite (production-ready, can migrate)
- **Containerization**: Docker, Docker Compose
- **Documentation**: OpenAPI/Swagger
- **Testing**: pytest (when implemented)

---

## Design Principles

1. **Separation of Concerns**: Clear layer boundaries
2. **Modularity**: Self-contained services
3. **Transparency**: Full visibility into processes
4. **Testability**: Services can be tested independently
5. **Extensibility**: Easy to add new features

---

**PANGEA IS THE TABLE.**
**YOU DON'T BETRAY THE TABLE.**
