# JAN Studio Setup Guide

**Complete setup instructions for JAN Studio.**

---

## Prerequisites

- Node.js 18+ installed
- Python 3.8+ installed
- SIYEM FastAPI server available
- JAN_ROOT environment variable set

---

## Step 1: Frontend Setup

### Install Dependencies

```bash
cd jan-studio/frontend
npm install
```

**Expected Output:**
```
added 200 packages in 30s
```

### Verify Installation

```bash
npm run dev
```

**Expected Output:**
```
- ready started server on 0.0.0.0:3000, url: http://localhost:3000
- info Loaded env from .env.local
```

Open `http://localhost:3000` in your browser. You should see the JAN Studio interface.

---

## Step 2: Backend Setup

### Create Symlink to SIYEM

**Windows (PowerShell as Administrator):**
```powershell
cd S:\JAN\jan-studio
New-Item -ItemType SymbolicLink -Path "backend" -Target "S:\SIYEM\07_AUTOMATION_AI"
```

**Linux/Mac:**
```bash
cd jan-studio
ln -s /path/to/SIYEM/07_AUTOMATION_AI backend
```

### Add API Endpoints to SIYEM

Copy `backend/jan-studio-api-example.py` to your SIYEM server:

```bash
cp backend/jan-studio-api-example.py S:\SIYEM\07_AUTOMATION_AI\api\jan_studio.py
```

### Register Router in SIYEM

Edit `S:\SIYEM\07_AUTOMATION_AI\server.py` (or your main FastAPI file):

```python
from api.jan_studio import router as jan_studio_router

app.include_router(jan_studio_router)
```

### Start SIYEM Server

```bash
cd S:\SIYEM\07_AUTOMATION_AI
uvicorn server:app --reload --port 8000
```

**Expected Output:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete.
```

---

## Step 3: Verify Connection

### Test API Endpoint

```bash
curl http://localhost:8000/api/jan/personas
```

**Expected Output:**
```json
[]
```

Or a list of existing personas.

### Test Frontend

1. Open `http://localhost:3000`
2. You should see "JAN Studio" header
3. Click "+ Create New Persona"
4. Enter a name and create

**If you see errors:**
- Check that SIYEM server is running on port 8000
- Check browser console for errors
- Verify API endpoints are registered

---

## Step 4: First Persona

### Create via UI

1. Click "+ Create New Persona"
2. Enter name: `test-persona`
3. Click "Create"
4. Select the persona from the list
5. You should see the editor with `profile.md` loaded

### Verify Files Created

```bash
ls S:\JAN\Siyem.org\test-persona\
```

**Expected Output:**
```
profile.md
creative_rules.md
prompt_templates/
```

---

## Troubleshooting

### Frontend won't start

**Error:** `Port 3000 is already in use`
- **Solution:** Kill the process using port 3000 or change port in `package.json`

**Error:** `Module not found`
- **Solution:** Run `npm install` again

### Backend connection fails

**Error:** `Network Error` in browser console
- **Solution:** 
  - Check SIYEM server is running
  - Verify `next.config.js` rewrites are correct
  - Check CORS settings in FastAPI

**Error:** `404 Not Found` for API calls
- **Solution:**
  - Verify router is registered in FastAPI
  - Check API endpoint paths match

### Files not saving

**Error:** `Permission denied`
- **Solution:** Check file permissions on JAN directory

**Error:** `Persona not found`
- **Solution:** Verify JAN_ROOT environment variable is set correctly

---

## Development Workflow

### Start Both Servers

**Terminal 1 (Frontend):**
```bash
cd jan-studio/frontend
npm run dev
```

**Terminal 2 (Backend):**
```bash
cd S:\SIYEM\07_AUTOMATION_AI
uvicorn server:app --reload
```

### Make Changes

- Frontend changes hot-reload automatically
- Backend changes require server restart (or use `--reload`)

---

## Next Steps

- Add authentication
- Add file upload/download
- Add validation
- Add persona templates
- Add export/import functionality

---

**Status:** Ready for development  
**Version:** 0.1.0

