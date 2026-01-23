# Heritage API Documentation

## Base URL
```
http://localhost:8000/api/heritage
```

## Endpoints

### Get Timeline Sites
```http
GET /api/heritage/timeline/{dimension}
```

**Parameters:**
- `dimension` - Timeline dimension (primary, parallel, past_loop, future_loop, regeneration, alternate)
- `period` (optional) - Time period filter

**Example:**
```bash
curl http://localhost:8000/api/heritage/timeline/primary
```

### Get Chronology
```http
GET /api/heritage/chronology?start_year={year}&end_year={year}
```

**Parameters:**
- `start_year` - Start year
- `end_year` - End year
- `timeline` (optional) - Timeline dimension filter

**Example:**
```bash
curl "http://localhost:8000/api/heritage/chronology?start_year=1800&end_year=2000"
```

### Get Temporal Patterns
```http
GET /api/heritage/patterns
```

**Example:**
```bash
curl http://localhost:8000/api/heritage/patterns
```

### Get Site Details
```http
GET /api/heritage/site/{site_id}
```

**Example:**
```bash
curl http://localhost:8000/api/heritage/site/1
```

### Create Site
```http
POST /api/heritage/site
Content-Type: application/json

{
  "site_name": "Example Site",
  "site_type": "Heritage Property",
  "region": "Example Region",
  "country": "Example Country",
  ...
}
```

### Search Sites
```http
GET /api/heritage/search?q={query}
```

**Example:**
```bash
curl "http://localhost:8000/api/heritage/search?q=Cyprus"
```

### Get Statistics
```http
GET /api/heritage/stats
```

**Example:**
```bash
curl http://localhost:8000/api/heritage/stats
```

## Response Formats

All endpoints return JSON with the following structure:

```json
{
  "data": [...],
  "count": 0,
  "timestamp": "2026-01-20T..."
}
```

## Error Handling

Errors are returned with appropriate HTTP status codes:

- `400` - Bad Request (invalid parameters)
- `404` - Not Found (resource not found)
- `500` - Internal Server Error

## PEACE, LOVE, UNITY
## ENERGY + LOVE = WE ALL WIN
