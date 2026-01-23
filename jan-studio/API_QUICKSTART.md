# JAN Studio API Quick Start

**Get started with the JAN Studio API in 5 minutes.**

---

## Quick Reference

**Base URL:** `http://localhost:8000`

**API Docs:** `http://localhost:8000/docs` (Interactive Swagger UI)

---

## Prerequisites

Backend must be running:
```bash
cd S:/JAN/jan-studio/backend
python main.py
```

**Verify:**
```bash
curl http://localhost:8000/health
# Expected: {"status":"healthy","service":"JAN Studio API"}
```

---

## Core Endpoints

### 1. Health Check

**Check if API is running:**

```bash
curl http://localhost:8000/health
```

**Response:**
```json
{
  "status": "healthy",
  "service": "JAN Studio API"
}
```

---

### 2. List Personas

**Get all personas:**

```bash
curl http://localhost:8000/api/jan/personas
```

**Response:**
```json
[
  "example-persona",
  "jk",
  "jean_mahram",
  "pierre_pressure"
]
```

---

### 3. Create Persona

**Create a new persona:**

```bash
curl -X POST http://localhost:8000/api/jan/personas \
  -H "Content-Type: application/json" \
  -d '{"name":"my-persona"}'
```

**Response:**
```json
{
  "success": true,
  "message": "Persona created: my-persona",
  "persona_path": "S:/JAN/Siyem.org/my-persona"
}
```

**Files created:**
- `S:/JAN/Siyem.org/my-persona/profile.md`
- `S:/JAN/Siyem.org/my-persona/creative_rules.md`
- `S:/JAN/Siyem.org/my-persona/prompt_templates/`

---

### 4. Get Persona Files

**List files in a persona:**

```bash
curl http://localhost:8000/api/jan/personas/my-persona/files
```

**Response:**
```json
[
  "profile.md",
  "creative_rules.md",
  "prompt_templates/example_template.md"
]
```

---

### 5. Read File

**Read a persona file:**

```bash
curl http://localhost:8000/api/jan/personas/my-persona/files/profile.md
```

**Response:**
```json
{
  "content": "# My Persona: Entity Profile\n\n## Entity Identity...",
  "path": "profile.md"
}
```

---

### 6. Update File

**Update a persona file:**

```bash
curl -X PUT http://localhost:8000/api/jan/personas/my-persona/files/profile.md \
  -H "Content-Type: application/json" \
  -d '{"content":"# Updated Profile\n\nNew content here..."}'
```

**Response:**
```json
{
  "success": true,
  "message": "File saved: profile.md"
}
```

---

### 7. Delete Persona

**Delete a persona:**

```bash
curl -X DELETE http://localhost:8000/api/jan/personas/my-persona
```

**Response:**
```json
{
  "success": true,
  "message": "Persona deleted: my-persona"
}
```

---

## Template System

### Save Template

**Save a persona as a reusable template:**

```bash
curl -X POST "http://localhost:8000/api/templates/save-from-persona?persona_name=my-persona&template_name=my-template"
```

**Response:**
```json
{
  "success": true,
  "message": "Template saved: my-template",
  "template_path": "S:/JAN/templates/my-template"
}
```

---

### List Templates

**Get all available templates:**

```bash
curl http://localhost:8000/api/templates/list
```

**Response:**
```json
[
  "basic-persona",
  "creative-artist",
  "my-template"
]
```

---

### Create from Template

**Create a new persona from a template:**

```bash
curl -X POST http://localhost:8000/api/templates/instantiate \
  -H "Content-Type: application/json" \
  -d '{
    "template_name": "my-template",
    "persona_name": "new-persona"
  }'
```

**Response:**
```json
{
  "success": true,
  "message": "Persona created from template",
  "persona_name": "new-persona"
}
```

---

## AI Generation (Optional)

**Note:** Requires API keys in `.env` file.

### Generate Content

**Generate content using a persona:**

```bash
curl -X POST http://localhost:8000/api/jan/generate \
  -H "Content-Type: application/json" \
  -d '{
    "persona": "my-persona",
    "prompt": "Write a blog post about AI",
    "output_type": "article",
    "options": {
      "length": "medium",
      "tone": "professional"
    }
  }'
```

**Response:**
```json
{
  "success": true,
  "content": "# AI in Modern World\n\nArtificial Intelligence...",
  "validation": {
    "passed": true,
    "checks": ["tone", "format", "length"]
  },
  "rules_applied": ["voice_guidelines", "content_structure"],
  "timestamp": "2026-01-13T10:30:00Z"
}
```

---

## Python Examples

### Using `requests` library

```python
import requests

BASE_URL = "http://localhost:8000"

# List personas
response = requests.get(f"{BASE_URL}/api/jan/personas")
personas = response.json()
print(f"Found {len(personas)} personas")

# Create persona
response = requests.post(
    f"{BASE_URL}/api/jan/personas",
    json={"name": "test-persona"}
)
result = response.json()
print(f"Created: {result['persona_path']}")

# Read file
response = requests.get(
    f"{BASE_URL}/api/jan/personas/test-persona/files/profile.md"
)
content = response.json()["content"]
print(f"Profile content:\n{content}")

# Update file
response = requests.put(
    f"{BASE_URL}/api/jan/personas/test-persona/files/profile.md",
    json={"content": "# Updated Profile\n\nNew content..."}
)
print(f"Updated: {response.json()['message']}")
```

---

### Using `httpx` (async)

```python
import httpx
import asyncio

async def main():
    async with httpx.AsyncClient() as client:
        # List personas
        response = await client.get("http://localhost:8000/api/jan/personas")
        personas = response.json()
        print(f"Personas: {personas}")

        # Create persona
        response = await client.post(
            "http://localhost:8000/api/jan/personas",
            json={"name": "async-persona"}
        )
        print(f"Created: {response.json()}")

asyncio.run(main())
```

---

## JavaScript/TypeScript Examples

### Using `fetch` API

```javascript
const BASE_URL = 'http://localhost:8000';

// List personas
async function listPersonas() {
  const response = await fetch(`${BASE_URL}/api/jan/personas`);
  const personas = await response.json();
  console.log('Personas:', personas);
  return personas;
}

// Create persona
async function createPersona(name) {
  const response = await fetch(`${BASE_URL}/api/jan/personas`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name })
  });
  const result = await response.json();
  console.log('Created:', result);
  return result;
}

// Read file
async function readFile(persona, file) {
  const response = await fetch(
    `${BASE_URL}/api/jan/personas/${persona}/files/${file}`
  );
  const data = await response.json();
  return data.content;
}

// Usage
listPersonas();
createPersona('my-persona');
```

---

### Using `axios`

```javascript
import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000',
  headers: { 'Content-Type': 'application/json' }
});

// List personas
const personas = await api.get('/api/jan/personas');
console.log(personas.data);

// Create persona
const result = await api.post('/api/jan/personas', {
  name: 'new-persona'
});
console.log(result.data);

// Update file
await api.put('/api/jan/personas/new-persona/files/profile.md', {
  content: '# Updated Profile\n\nContent...'
});
```

---

## Error Handling

### Common Status Codes

| Code | Meaning | Example |
|------|---------|---------|
| 200 | Success | Request completed successfully |
| 201 | Created | New resource created |
| 400 | Bad Request | Invalid input data |
| 404 | Not Found | Persona or file doesn't exist |
| 500 | Server Error | Internal server error |

### Example Error Response

```json
{
  "detail": "Persona not found: invalid-persona"
}
```

### Python Error Handling

```python
import requests

try:
    response = requests.get("http://localhost:8000/api/jan/personas/invalid")
    response.raise_for_status()
    data = response.json()
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
    print(f"Details: {e.response.json()}")
except requests.exceptions.ConnectionError:
    print("Error: Cannot connect to API. Is backend running?")
```

---

## Authentication (Future)

**Current:** No authentication required (local development)

**Planned:**
- API key authentication
- JWT tokens
- OAuth2 support

---

## Rate Limits (Future)

**Current:** No rate limits

**Planned:**
- Development: 100 requests/minute
- Production: Based on plan

---

## API Versioning

**Current:** `/api/jan/*` (v1 implicit)

**Future:** `/api/v1/jan/*`, `/api/v2/jan/*`

**Breaking changes:** Will introduce new version endpoints

---

## Interactive Documentation

**Swagger UI:** http://localhost:8000/docs

**Features:**
- Try all endpoints directly
- See request/response schemas
- View parameter descriptions
- Test with your data

**ReDoc:** http://localhost:8000/redoc (Alternative documentation)

---

## Development Tips

### 1. Test Endpoints Quickly

```bash
# Save common commands as aliases
alias jan-health='curl http://localhost:8000/health'
alias jan-list='curl http://localhost:8000/api/jan/personas'

# Use them
jan-health
jan-list
```

### 2. Watch Logs

```bash
# Backend logs show all requests
cd backend
python main.py
# Watch terminal for request logs
```

### 3. Use Environment Variables

```bash
# Set base URL
export JAN_API_URL="http://localhost:8000"

# Use in scripts
curl $JAN_API_URL/health
```

### 4. JSON Formatting

```bash
# Install jq for pretty JSON
curl http://localhost:8000/api/jan/personas | jq

# Python one-liner
curl -s http://localhost:8000/api/jan/personas | python -m json.tool
```

---

## Troubleshooting

### API Not Responding

**Check backend is running:**
```bash
curl http://localhost:8000/health
```

**If fails:**
1. Start backend: `cd backend && python main.py`
2. Check port 8000 is free: `netstat -an | grep 8000`
3. Check firewall settings

### CORS Errors (Browser)

**Symptom:** Browser console shows CORS errors

**Fix:** Add your frontend URL to CORS in `main.py`:
```python
allow_origins=[
    "http://localhost:3000",
    "http://localhost:5173",
    # Add your URL here
]
```

### 404 Errors

**Persona not found:**
- Check persona exists: `curl http://localhost:8000/api/jan/personas`
- Check name is correct (case-sensitive)
- Check JAN_ROOT is set correctly in `.env`

---

## Next Steps

1. **Explore API:** Open http://localhost:8000/docs
2. **Read Full Docs:** See `API_REFERENCE.md` for complete documentation
3. **Integration:** See `INTEGRATION.md` for workflow examples
4. **SDK:** Check for language-specific SDK libraries (coming soon)

---

## Support

**Issues:**
- Check logs in terminal running backend
- Review API documentation at `/docs`
- See TROUBLESHOOTING.md

**Feature Requests:**
- Submit to project repository
- Describe use case clearly

---

**Version:** 1.0
**Updated:** 2026-01-13
**Status:** Ready for Week 2 Testing
