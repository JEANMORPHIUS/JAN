# JAN Studio Installation Guide

**Complete step-by-step installation guide for JAN Studio.**

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Quick Install (5 Minutes)](#quick-install-5-minutes)
3. [Detailed Installation](#detailed-installation)
4. [Docker Installation](#docker-installation)
5. [Configuration](#configuration)
6. [Verification](#verification)
7. [Troubleshooting](#troubleshooting)
8. [Next Steps](#next-steps)

---

## Prerequisites

### Required Software

- **Python 3.8+** - Backend server
  ```bash
  python --version  # Should show 3.8 or higher
  ```

- **Node.js 18+** - Frontend application
  ```bash
  node --version  # Should show 18.0 or higher
  ```

- **pip** - Python package manager (usually included with Python)
  ```bash
  pip --version
  ```

- **npm** - Node package manager (included with Node.js)
  ```bash
  npm --version
  ```

### Optional Software

- **Docker & Docker Compose** - For containerized deployment
- **Git** - For version control (if cloning from repository)

### System Requirements

- **OS:** Windows 10/11, macOS 10.15+, Linux (Ubuntu 20.04+)
- **RAM:** 2GB minimum, 4GB recommended
- **Disk:** 500MB for application, additional space for personas
- **Network:** Internet connection for package downloads

---

## Quick Install (5 Minutes)

**For those who want to get started immediately:**

### Step 1: Setup Environment

```bash
# Navigate to jan-studio directory
cd S:/JAN/jan-studio

# Copy environment file
cp .env.example .env

# Edit .env and set JAN_ROOT (optional, defaults work fine)
# nano .env  # or use your preferred editor
```

### Step 2: Setup Backend

```bash
# Navigate to backend
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Initialize JAN directory structure
python setup_jan_structure.py

# Start backend server
python main.py
```

**Expected Output:**
```
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000
```

### Step 3: Setup Frontend (New Terminal)

```bash
# Navigate to frontend
cd S:/JAN/jan-studio/frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

**Expected Output:**
```
ready - started server on 0.0.0.0:3000, url: http://localhost:3000
```

### Step 4: Access JAN Studio

Open your browser to: **http://localhost:3000**

**You should see:** JAN Studio interface with "Create New Persona" button

---

## Detailed Installation

### 1. Clone or Download

If you have the repository:
```bash
git clone <repository-url>
cd jan-studio
```

If you have the files:
```bash
cd S:/JAN/jan-studio
```

### 2. Environment Configuration

```bash
# Copy the example environment file
cp .env.example .env
```

**Edit `.env` file:**

```env
# Set your JAN directory (where personas will be stored)
JAN_ROOT=S:/JAN

# Optional: Add API keys for AI generation (not required for basic use)
GEMINI_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here
```

**Important:** You can use JAN Studio WITHOUT API keys. API keys are only needed for AI content generation features.

### 3. Backend Installation

#### Install Python Dependencies

```bash
cd backend
pip install -r requirements.txt
```

**Expected packages:**
- fastapi
- uvicorn
- pydantic
- python-dotenv
- markdown
- httpx
- requests

**Troubleshooting:**
- If `pip` not found, try `python -m pip install -r requirements.txt`
- If permission errors, add `--user` flag
- Use virtual environment (recommended):
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  pip install -r requirements.txt
  ```

#### Initialize JAN Structure

```bash
python setup_jan_structure.py
```

**This creates:**
```
S:/JAN/
├── Siyem.org/
│   └── example-persona/
│       ├── profile.md
│       ├── creative_rules.md
│       └── prompt_templates/
├── templates/
└── styles/
```

**Expected Output:**
```
Creating JAN structure at: S:/JAN
✅ JAN structure created successfully!
   Location: S:/JAN
   Example persona: S:/JAN/Siyem.org/example-persona
```

#### Start Backend Server

```bash
python main.py
```

**Expected Output:**
```
INFO:     Started server process [12345]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

**Verify Backend:**
```bash
curl http://localhost:8000/health
# Should return: {"status":"healthy","service":"JAN Studio API"}
```

### 4. Frontend Installation

**Open a new terminal** (keep backend running in first terminal)

#### Install Node Dependencies

```bash
cd S:/JAN/jan-studio/frontend
npm install
```

**Expected Output:**
```
added 250+ packages, and audited 251 packages in 30s
```

**If you see warnings about deprecated packages, that's normal and safe to ignore.**

#### Start Frontend Development Server

```bash
npm run dev
```

**Expected Output:**
```
ready - started server on 0.0.0.0:3000, url: http://localhost:3000
info  - Using webpack 5
event - compiled client and server successfully
```

### 5. Access Application

**Open browser:** http://localhost:3000

**You should see:**
- JAN Studio header
- "Create New Persona" button
- Clean, modern UI

**Test the connection:**
1. Click "Create New Persona"
2. Enter name: "test-persona"
3. Click "Create"
4. If successful, you'll see the persona in the list

---

## Docker Installation

### Prerequisites

- Docker installed and running
- Docker Compose installed

### Quick Docker Start

```bash
# Navigate to JAN root (where docker-compose.yml is)
cd S:/JAN

# Create .env file (or copy from jan-studio)
cp jan-studio/.env.example .env

# Edit .env and set JAN_ROOT=/app/jan
nano .env

# Start services
docker-compose up -d

# View logs
docker-compose logs -f
```

**Services:**
- Backend: http://localhost:8000
- Frontend: http://localhost:3000

### Docker Commands

```bash
# Start services
docker-compose up -d

# Stop services
docker-compose down

# Restart services
docker-compose restart

# View logs
docker-compose logs -f

# Rebuild after code changes
docker-compose up -d --build
```

### Docker Troubleshooting

**Port conflicts:**
```bash
# Check what's using ports 3000 and 8000
netstat -an | grep "3000\|8000"

# Change ports in docker-compose.yml if needed
```

**Volume permissions:**
```bash
# On Linux/Mac, ensure directory permissions
chmod -R 755 S:/JAN
```

---

## Configuration

### Environment Variables

**Key variables in `.env`:**

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `JAN_ROOT` | No | `./jan` | Path to JAN directory |
| `SERVER_HOST` | No | `127.0.0.1` | Backend host |
| `SERVER_PORT` | No | `8000` | Backend port |
| `GEMINI_API_KEY` | No | - | Google AI API key |
| `OPENAI_API_KEY` | No | - | OpenAI API key |
| `MARKETPLACE_DB` | No | `./marketplace.db` | Database path |

### JAN_ROOT Configuration

**Option 1: Absolute Path (Recommended)**
```env
JAN_ROOT=S:/JAN
```

**Option 2: Relative Path**
```env
JAN_ROOT=./jan
```

**Option 3: Environment Variable**
```bash
export JAN_ROOT=/path/to/JAN
```

### Port Configuration

**Change ports if defaults are in use:**

```env
# Backend
SERVER_PORT=8001

# Frontend (edit package.json)
"dev": "next dev -p 3001"
```

---

## Verification

### Backend Health Check

```bash
curl http://localhost:8000/health
```

**Expected:**
```json
{
  "status": "healthy",
  "service": "JAN Studio API"
}
```

### API Endpoints Check

```bash
# Get personas list
curl http://localhost:8000/api/jan/personas

# Get API documentation
open http://localhost:8000/docs
```

### Frontend Check

**Open:** http://localhost:3000

**Verify:**
- [ ] Page loads without errors
- [ ] "Create New Persona" button visible
- [ ] No console errors (F12 → Console)

### Full Workflow Test

1. **Create Persona**
   - Click "Create New Persona"
   - Enter name: "test-persona"
   - Click "Create"

2. **Verify Files Created**
   ```bash
   ls -la S:/JAN/Siyem.org/test-persona/
   ```
   Should show:
   - `profile.md`
   - `creative_rules.md`
   - `prompt_templates/`

3. **View in UI**
   - Refresh page
   - See "test-persona" in list
   - Click on it
   - See editor with `profile.md` content

---

## Troubleshooting

### Backend Won't Start

**Error: `ModuleNotFoundError: No module named 'fastapi'`**

**Solution:**
```bash
pip install -r requirements.txt
```

**Error: `Address already in use` (Port 8000)**

**Solution:**
```bash
# Option 1: Kill process using port 8000
netstat -ano | findstr :8000  # Windows
lsof -ti:8000 | xargs kill -9  # Mac/Linux

# Option 2: Change port in .env
SERVER_PORT=8001
```

**Error: `JAN_ROOT directory not found`**

**Solution:**
```bash
# Run setup script
python backend/setup_jan_structure.py

# Or create manually
mkdir -p S:/JAN/Siyem.org
```

### Frontend Won't Start

**Error: `Port 3000 is already in use`**

**Solution:**
```bash
# Option 1: Kill process
netstat -ano | findstr :3000  # Windows
lsof -ti:3000 | xargs kill -9  # Mac/Linux

# Option 2: Use different port
npm run dev -- -p 3001
```

**Error: `Module not found`**

**Solution:**
```bash
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
```

### Connection Issues

**Error: `Network Error` or `Failed to fetch`**

**Check:**
1. Is backend running? → `curl http://localhost:8000/health`
2. Is CORS configured? → Check `main.py` CORS settings
3. Check browser console (F12) for specific errors

**Solution:**
```bash
# Verify both servers are running
ps aux | grep "uvicorn\|next"  # Linux/Mac
tasklist | findstr "python\|node"  # Windows
```

### Permission Issues

**Error: `Permission denied` when creating personas**

**Solution:**
```bash
# Check directory permissions
ls -la S:/JAN

# Fix permissions
chmod -R 755 S:/JAN  # Linux/Mac

# On Windows, check folder properties → Security
```

### Database Issues

**Error: `OperationalError: unable to open database file`**

**Solution:**
```bash
# Check if directory is writable
touch backend/test.db && rm backend/test.db

# Or set specific database path in .env
MARKETPLACE_DB=/path/to/writable/location/marketplace.db
```

---

## Next Steps

### 1. Create Your First Persona

```bash
# Via UI
- Open http://localhost:3000
- Click "Create New Persona"
- Enter name: "my-persona"
- Edit profile.md and creative_rules.md

# Via API
curl -X POST http://localhost:8000/api/jan/personas \
  -H "Content-Type: application/json" \
  -d '{"name":"my-persona"}'
```

### 2. Explore Existing Personas

If you have existing JAN personas:
```bash
# Set JAN_ROOT to your existing JAN directory
JAN_ROOT=S:/JAN

# Restart backend
# Personas will appear in UI automatically
```

### 3. Use Templates

```bash
# Save a persona as template
curl -X POST "http://localhost:8000/api/templates/save-from-persona?persona_name=my-persona&template_name=my-template"

# List templates
curl http://localhost:8000/api/templates/list

# Create persona from template
curl -X POST http://localhost:8000/api/templates/instantiate \
  -H "Content-Type: application/json" \
  -d '{"template_name":"my-template","persona_name":"new-persona"}'
```

### 4. Enable AI Generation (Optional)

To use AI content generation:

1. Get API key from:
   - Google AI (Gemini): https://makersuite.google.com/app/apikey
   - OpenAI: https://platform.openai.com/api-keys
   - Anthropic (Claude): https://console.anthropic.com/

2. Add to `.env`:
   ```env
   GEMINI_API_KEY=your_key_here
   ```

3. Restart backend

4. Use generation endpoint:
   ```bash
   curl -X POST http://localhost:8000/api/jan/generate \
     -H "Content-Type: application/json" \
     -d '{"persona":"my-persona","prompt":"Write a blog post","output_type":"article"}'
   ```

### 5. Explore API Documentation

Open: **http://localhost:8000/docs**

Interactive API documentation with:
- All available endpoints
- Request/response schemas
- Try-it-out functionality

### 6. Production Deployment

For production:
- Use Docker Compose
- Set `SERVER_HOST=0.0.0.0`
- Use absolute paths for `JAN_ROOT`
- Enable authentication
- Use environment-specific `.env` files
- Set up reverse proxy (nginx, traefik)
- Enable HTTPS

---

## Additional Resources

- **Quick Start:** See `QUICKSTART.md` for 5-minute setup
- **Setup Guide:** See `SETUP.md` for detailed configuration
- **API Reference:** http://localhost:8000/docs
- **Troubleshooting:** See `TROUBLESHOOTING.md` (if created)

---

## Support

**Issues:**
- Check [Troubleshooting](#troubleshooting) section above
- Review logs in terminal
- Check browser console (F12)
- Verify all prerequisites are installed

**Common Questions:**
- Do I need API keys? **No, only for AI generation**
- Can I use existing personas? **Yes, set JAN_ROOT**
- Does it work offline? **Yes, except AI generation**

---

**Installation Complete!**

You should now have:
- ✅ Backend running on http://localhost:8000
- ✅ Frontend running on http://localhost:3000
- ✅ JAN directory structure created
- ✅ Example persona available
- ✅ Ready to create and manage personas

**Next:** Visit http://localhost:3000 and create your first persona!

---

**Document Version:** 1.0
**Last Updated:** 2026-01-13
**Status:** Ready for Week 2 Testing
