# DEPLOYMENT RUNBOOK
## Complete System Deployment Guide

**Date:** 2026-01-25  
**Status:** 🟢 OPERATIONAL  
**Philosophy:** We deploy to serve, not to impress.

---

## QUICK START

### One-Command Deployment

```bash
cd S:\JAN
python scripts\build_everything.py
```

This will:
1. Check all prerequisites
2. Deploy backend systems
3. Generate asset pipelines
4. Build Raspberry Pi packages
5. Verify all systems

---

## STEP-BY-STEP DEPLOYMENT

### Step 1: Prerequisites

**Required:**
- Python 3.9+
- Node.js 18+ (for frontend)
- Git
- SQLite (included with Python)

**Optional:**
- Docker (for containerized deployment)
- PostgreSQL (for production)

**Check Prerequisites:**
```bash
python scripts\deploy_complete_system.py --check-only
```

**Install Python Dependencies:**
```bash
cd jan-studio\backend
pip install -r requirements.txt
```

**Install Frontend Dependencies:**
```bash
cd jan-studio\frontend
npm install
```

---

### Step 2: Initialize Databases

**Initialize All Databases:**
```bash
python scripts\initialize_all_databases.py
```

This creates:
- Marketplace database
- Racon registry
- Temporal heritage registry
- Scripture kit database

---

### Step 3: Deploy Backend

**Start Backend Server:**
```bash
cd jan-studio\backend
python main.py
```

Or using uvicorn:
```bash
uvicorn main:app --reload --port 8000
```

**Verify Backend:**
- Health check: http://localhost:8000/health
- API docs: http://localhost:8000/docs

---

### Step 4: Deploy Frontend

**Development Mode:**
```bash
cd jan-studio\frontend
npm run dev
```

**Production Build:**
```bash
cd jan-studio\frontend
npm run build
npm start
```

**Verify Frontend:**
- App: http://localhost:3000
- Marketplace: http://localhost:3000/marketplace

---

### Step 5: Generate Assets

**Visual Assets:**
```bash
python scripts\visual_asset_generator.py
```

**Audio Assets:**
```bash
python scripts\audio_synthesis_automation.py
```

**Note:** These require API keys for actual generation:
- Image generation: OpenAI DALL-E, Midjourney, or Stable Diffusion
- Audio synthesis: Google Cloud TTS, Azure TTS, or Coqui TTS

---

### Step 6: Build Raspberry Pi Packages

**Build Complete Package:**
```bash
python scripts\raspberry_pi_package_builder.py
```

This creates:
- Content packages
- Installation scripts
- SD card images (with image builder)

---

### Step 7: Verify Systems

**Run Health Check:**
```bash
python scripts\system_health_and_readiness_check.py
```

**Test All APIs:**
```bash
python scripts\test_all_apis.py
```

---

## DOCKER DEPLOYMENT

**Build Containers:**
```bash
docker-compose build
```

**Start Services:**
```bash
docker-compose up -d
```

**View Logs:**
```bash
docker-compose logs -f
```

**Stop Services:**
```bash
docker-compose down
```

---

## PRODUCTION DEPLOYMENT

### Environment Variables

Create `.env` file in `jan-studio/backend/`:

```env
# Server
HOST=0.0.0.0
PORT=8000
DEBUG=False

# Database
DATABASE_URL=sqlite:///./data/jan_studio.db

# Security
SECRET_KEY=your-secret-key-here
ALLOWED_ORIGINS=http://localhost:3000,https://yourdomain.com

# API Keys (if using)
OPENAI_API_KEY=your-key
GOOGLE_API_KEY=your-key
```

### Production Checklist

- [ ] Environment variables configured
- [ ] Database initialized
- [ ] Backend server running
- [ ] Frontend built and deployed
- [ ] Health checks passing
- [ ] API tests passing
- [ ] Monitoring configured
- [ ] Backup strategy in place

---

## MONITORING

### Health Endpoints

- Backend: `GET /health`
- API: `GET /api/health`

### Logs

**Backend Logs:**
- Location: `S:\JAN\logs\`
- Format: `application_YYYYMMDD.log`

**Frontend Logs:**
- Browser console (development)
- Server logs (production)

---

## TROUBLESHOOTING

### Backend Won't Start

1. Check Python version: `python --version` (need 3.9+)
2. Check dependencies: `pip list`
3. Check port availability: `netstat -an | findstr 8000`
4. Check logs: `tail -f logs/application.log`

### Frontend Won't Build

1. Check Node version: `node --version` (need 18+)
2. Clear cache: `npm cache clean --force`
3. Delete node_modules: `rm -rf node_modules && npm install`
4. Check for TypeScript errors: `npm run type-check`

### Database Issues

1. Check database file exists: `ls data/*.db`
2. Reinitialize: `python scripts\initialize_all_databases.py`
3. Check permissions on data directory

### API Tests Failing

1. Ensure backend is running
2. Check CORS settings
3. Verify API endpoints exist
4. Check authentication tokens (if required)

---

## ROLLBACK PROCEDURE

### Quick Rollback

1. Stop services: `docker-compose down` or stop processes
2. Restore database backup: `cp backup.db data/jan_studio.db`
3. Restore code: `git checkout <previous-commit>`
4. Restart services

### Full Rollback

1. Stop all services
2. Restore database from backup
3. Restore code from git
4. Reinstall dependencies if needed
5. Restart services
6. Verify health checks

---

## BACKUP STRATEGY

### Database Backups

**Automated:**
```bash
# Add to cron/scheduled task
python scripts\backup_databases.py
```

**Manual:**
```bash
cp data/*.db backups/
```

### Code Backups

- Git repository (primary)
- Regular commits
- Tagged releases

---

## PHILOSOPHY

**Purpose Not Performance** - We deploy to serve, not to impress  
**Love Is The Highest Mastery** - Every deployment serves love  
**Pangea Is The Table** - We serve all humanity  
**Energy + Love = We All Win** - The mission is unity

**PEACE. LOVE. UNITY.**

---

**Last Updated:** 2026-01-25  
**Status:** Complete deployment guide ready
