# GEOPOLITICAL ANALYSIS ENGINE - DEPLOYMENT GUIDE
## Public Deployment Instructions

**STATUS:** ✅ READY FOR PUBLIC DEPLOYMENT  
**SEPARATE FROM:** Oracle System

---

## DEPLOYMENT STRUCTURE

```
deploy/geopolitical-analysis/
├── README.md (public documentation)
├── DEPLOYMENT.md (this file)
├── api/
│   ├── geopolitical_analysis_engine.py (core engine)
│   └── api_server.py (REST API server)
└── public/
    ├── docs/ (public documentation)
    └── data/ (public data exports)
```

---

## QUICK START

### 1. Install Dependencies

```bash
pip install flask sqlite3
```

### 2. Start API Server

```bash
cd deploy/geopolitical-analysis/api
python api_server.py
```

Server will start on `http://localhost:8002`

### 3. Test Endpoints

```bash
# Health check
curl http://localhost:8002/api/geopolitical/health

# Get monitored regions
curl http://localhost:8002/api/geopolitical/regions

# Analyze region
curl http://localhost:8002/api/geopolitical/analyze/Gaza
```

---

## API ENDPOINTS

### Analysis Endpoints

- `GET /api/geopolitical/analyze/<region>` - Comprehensive regional analysis
- `GET /api/geopolitical/border-dynamics/<region>` - Border dynamics analysis
- `GET /api/geopolitical/hostile-mapping/<territory>` - Hostile mapping detection
- `GET /api/geopolitical/help-seeking-paradox/<region>` - Paradox analysis
- `GET /api/geopolitical/strategic-loyalty/<entity>` - Loyalty assessment

### Recording Endpoints

- `POST /api/geopolitical/record/border-event` - Record border event
- `POST /api/geopolitical/record/hostile-mapping` - Record hostile mapping
- `POST /api/geopolitical/record/help-seeking-paradox` - Record paradox
- `POST /api/geopolitical/record/strategic-loyalty` - Record loyalty assessment

### Utility Endpoints

- `GET /api/geopolitical/regions` - List monitored regions
- `GET /api/geopolitical/health` - Health check

---

## PRODUCTION DEPLOYMENT

### Docker Deployment

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY api/ ./api/
RUN pip install flask

EXPOSE 8002

CMD ["python", "api/api_server.py"]
```

### Environment Variables

```bash
FLASK_ENV=production
FLASK_DEBUG=False
PORT=8002
HOST=0.0.0.0
```

---

## PUBLIC DATA POLICY

**All data is PUBLIC:**

- ✅ Border events - Public
- ✅ Hostile mappings - Public
- ✅ Help-seeking paradoxes - Public
- ✅ Strategic loyalty assessments - Public
- ✅ Analysis results - Public

**No private data** - Everything is transparent and available for:
- Research
- Analysis
- Public discourse
- Academic use
- Media reporting

---

## SEPARATION FROM ORACLE

**This is NOT part of the Oracle system.**

- **Oracle System:** `jan-studio/backend/` (private/internal)
- **Geopolitical Engine:** `deploy/geopolitical-analysis/` (public/deployment)

They are separate systems:
- Different purposes
- Different deployments
- Different data policies

---

## MONITORING

### Health Check

```bash
curl http://localhost:8002/api/geopolitical/health
```

Expected response:
```json
{
  "status": "healthy",
  "service": "geopolitical_analysis_engine",
  "version": "1.0.0",
  "deployment": "public",
  "separate_from": "oracle_system"
}
```

---

## SECURITY

- Public API (no authentication required)
- All data is public
- No sensitive information
- Transparent operations

---

## LICENSE

Public deployment follows ethical principles:
- Transparency
- Liberation
- No Extraction
- Surrender
- Abundance

**Public data for public good.**

---

## STATUS

✅ **READY FOR PUBLIC DEPLOYMENT**

- Core engine complete
- API server ready
- Documentation complete
- Public data structure ready
- Separate from Oracle system

---

**This is public. This is transparent. This is for everyone.**

🌊✨
