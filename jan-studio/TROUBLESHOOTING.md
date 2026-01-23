# JAN Studio Troubleshooting Guide

**Quick reference for common issues and solutions.**

---

## Table of Contents

1. [Backend Issues](#backend-issues)
2. [Frontend Issues](#frontend-issues)
3. [Docker Issues](#docker-issues)
4. [Database Issues](#database-issues)
5. [Connection Issues](#connection-issues)
6. [Permission Issues](#permission-issues)
7. [Platform-Specific Issues](#platform-specific-issues)
8. [Performance Issues](#performance-issues)

---

## Backend Issues

### Backend Won't Start

#### Error: `ModuleNotFoundError: No module named 'fastapi'`

**Cause:** Python dependencies not installed

**Solution:**
```bash
cd S:/JAN/jan-studio/backend
pip install -r requirements.txt
```

**Alternative:** Use virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

#### Error: `Address already in use` (Port 8000)

**Cause:** Another process is using port 8000

**Find the process:**
```bash
# Windows
netstat -ano | findstr :8000

# Mac/Linux
lsof -i :8000
```

**Solution 1: Kill the process**
```bash
# Windows (replace PID with actual process ID)
taskkill /PID <PID> /F

# Mac/Linux
kill -9 <PID>
```

**Solution 2: Use different port**
```bash
# Edit .env
SERVER_PORT=8001

# Or run directly
uvicorn main:app --host 127.0.0.1 --port 8001
```

---

#### Error: `ModuleNotFoundError: No module named 'jan_studio_api_example'`

**Cause:** Router files still have hyphens instead of underscores

**Check filenames:**
```bash
ls -la backend/
```

**Should see:**
- `jan_studio_api_example.py` (with underscores)
- `jan_generation_api.py` (with underscores)
- `jan_templates_api.py` (with underscores)

**If you see hyphens, rename:**
```bash
cd backend
mv jan-studio-api-example.py jan_studio_api_example.py
mv jan-generation-api.py jan_generation_api.py
mv jan-templates-api.py jan_templates_api.py
```

---

#### Error: `JAN_ROOT directory not found`

**Cause:** JAN directory doesn't exist

**Solution: Run setup script**
```bash
cd S:/JAN/jan-studio/backend
python setup_jan_structure.py
```

**Manual creation:**
```bash
mkdir -p S:/JAN/Siyem.org
mkdir -p S:/JAN/templates
mkdir -p S:/JAN/styles
```

**Set JAN_ROOT in .env:**
```env
JAN_ROOT=S:/JAN
```

---

#### Backend starts but shows router warnings

**Example:**
```
Warning: Could not import jan_studio_router: ...
Warning: Could not import generation_router: ...
```

**Cause:** Router files have import errors or are missing

**Diagnosis:**
```bash
cd backend
python -c "import jan_studio_api_example"
# Check error message
```

**Common causes:**
1. Missing dependencies
2. Syntax errors in router files
3. File naming issues

**Solution:** Check specific error message and fix accordingly

---

## Frontend Issues

### Frontend Won't Start

#### Error: `Port 3000 is already in use`

**Cause:** Another process using port 3000

**Find process:**
```bash
# Windows
netstat -ano | findstr :3000

# Mac/Linux
lsof -i :3000
```

**Solution 1: Kill process**
```bash
# Windows
taskkill /PID <PID> /F

# Mac/Linux
kill -9 <PID>
```

**Solution 2: Use different port**
```bash
npm run dev -- -p 3001
```

---

#### Error: `Module not found` or `Cannot find module`

**Cause:** Node modules not installed or corrupted

**Solution: Reinstall dependencies**
```bash
cd S:/JAN/jan-studio/frontend

# Remove existing modules
rm -rf node_modules package-lock.json

# Reinstall
npm install
```

**If still failing:**
```bash
# Clear npm cache
npm cache clean --force

# Reinstall
npm install
```

---

#### Error: `react-markdown-editor-lite not found`

**Cause:** Missing markdown editor dependency

**Solution:**
```bash
npm install react-markdown-editor-lite react-markdown remark-gfm markdown-it
npm install --save-dev @types/markdown-it
```

---

#### Frontend builds but page is blank

**Cause:** JavaScript errors or API connection issues

**Diagnosis:**
1. Open browser DevTools (F12)
2. Check Console tab for errors
3. Check Network tab for failed requests

**Common issues:**
- Backend not running
- CORS errors
- API URL misconfigured

**Solution: Check backend connection**
```bash
# Is backend running?
curl http://localhost:8000/health

# Check frontend config
cat frontend/.env.local
# Should have: NEXT_PUBLIC_API_URL=http://localhost:8000
```

---

## Docker Issues

### Docker Build Fails

#### Error: `Cannot connect to Docker daemon`

**Cause:** Docker not running

**Solution:**
```bash
# Windows: Start Docker Desktop
# Mac: Start Docker Desktop
# Linux: sudo systemctl start docker
```

---

#### Error: `Context path does not exist`

**Cause:** Running docker-compose from wrong directory

**Solution:**
```bash
# Must run from JAN root (where docker-compose.yml is)
cd S:/JAN
docker-compose build
```

---

#### Build fails with dependency errors

**Cause:** Package installation issues in Docker

**Solution: Rebuild without cache**
```bash
docker-compose build --no-cache
```

**Check Dockerfiles:**
```bash
# Verify requirements.txt exists
cat jan-studio/backend/requirements.txt

# Verify package.json exists
cat jan-studio/frontend/package.json
```

---

### Docker Run Issues

#### Containers start but immediately exit

**Check logs:**
```bash
docker-compose logs backend
docker-compose logs frontend
```

**Common causes:**
1. Missing environment variables
2. Port conflicts
3. Volume mount errors
4. Application errors

---

#### Error: `Cannot create persona` in Docker

**Cause:** Volume mounted as read-only

**Check docker-compose.yml:**
```yaml
volumes:
  - ./jan:/app/jan     # ✅ Correct (read-write)
  - ./jan:/app/jan:ro  # ❌ Wrong (read-only)
```

**Fix:**
```bash
# Edit docker-compose.yml
nano docker-compose.yml

# Remove :ro from jan volume
# Rebuild
docker-compose up -d --build
```

---

#### Containers can't communicate

**Symptom:** Frontend can't reach backend

**Check docker-compose.yml:**
```yaml
environment:
  - NEXT_PUBLIC_API_URL=http://backend:8000  # ✅ Use service name
  # NOT http://localhost:8000 ❌
```

**Verify network:**
```bash
docker-compose exec frontend ping backend
```

---

## Database Issues

### Database Errors

#### Error: `OperationalError: unable to open database file`

**Cause:** Directory not writable or doesn't exist

**Solution:**
```bash
# Check backend directory permissions
ls -la backend/

# Ensure directory is writable
chmod 755 backend/  # Linux/Mac

# On Windows: Right-click → Properties → Security → Edit
```

**Set specific database path:**
```env
# In .env
MARKETPLACE_DB=/path/to/writable/location/marketplace.db
```

---

#### Database corruption

**Symptoms:** SQLite errors, database locked, corruption warnings

**Solution: Reset database**
```bash
cd backend

# Backup existing database
cp marketplace.db marketplace.db.backup

# Delete and reinitialize
rm marketplace.db
python -c "import marketplace_db; print('Database reinitialized')"

# Or restart backend (auto-initializes)
python main.py
```

---

## Connection Issues

### API Connection Failures

#### Error: `Network Error` or `Failed to fetch`

**Diagnosis checklist:**
- [ ] Backend running? `curl http://localhost:8000/health`
- [ ] Frontend running? Browser shows page?
- [ ] Correct ports? Backend:8000, Frontend:3000
- [ ] CORS configured? Check `main.py` CORS settings
- [ ] Firewall blocking? Check firewall rules

**Solution: Verify connection**
```bash
# From frontend, can it reach backend?
curl http://localhost:8000/health

# Expected: {"status":"healthy","service":"JAN Studio API"}
```

**Check browser console:**
1. Open DevTools (F12)
2. Console tab → Look for errors
3. Network tab → Look for failed requests

---

#### CORS Errors

**Symptom:** Browser console shows CORS policy errors

**Check main.py CORS configuration:**
```python
# Should include your frontend URL
allow_origins=[
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
```

**Solution: Add your URL**
```python
allow_origins=[
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:3001",  # If using different port
]
```

**Restart backend after changes**

---

### Slow API Responses

**Symptoms:** Long waits, timeouts, spinning indicators

**Diagnosis:**
```bash
# Check if backend is responsive
time curl http://localhost:8000/api/jan/personas
```

**Common causes:**
1. Large number of personas
2. Slow file system
3. Database not indexed
4. Backend CPU usage high

**Solutions:**
- Limit persona list
- Use pagination
- Optimize database queries
- Check system resources

---

## Permission Issues

### File Permission Errors

#### Error: `Permission denied` when creating personas

**Cause:** No write permissions to JAN directory

**Check permissions:**
```bash
ls -la S:/JAN
```

**Solution: Fix permissions**
```bash
# Linux/Mac
chmod -R 755 S:/JAN

# Windows: Right-click S:/JAN → Properties → Security
# Ensure your user has "Full control"
```

---

#### Error: `Permission denied` for database file

**Cause:** No write permissions to backend directory

**Solution:**
```bash
# Linux/Mac
chmod 755 backend/
chmod 644 backend/marketplace.db

# Windows: Check folder security settings
```

---

## Platform-Specific Issues

### Windows Issues

#### PowerShell execution policy errors

**Error:** `cannot be loaded because running scripts is disabled`

**Solution:**
```powershell
# Run PowerShell as Administrator
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

#### Windows path issues

**Symptom:** Paths with spaces don't work

**Solution: Use quotes**
```bash
cd "S:/Program Files/JAN/jan-studio"
```

**In .env:**
```env
JAN_ROOT="S:/My Documents/JAN"
```

---

#### Windows symlink issues

**Symptom:** Cannot create symlinks

**Solution: Run as Administrator**
```powershell
# Right-click PowerShell → Run as Administrator
New-Item -ItemType SymbolicLink -Path "link" -Target "target"
```

---

### Mac/Linux Issues

#### Python version conflicts

**Symptom:** `python` points to Python 2.x

**Solution: Use python3**
```bash
# Instead of: python main.py
python3 main.py

# Create alias
alias python=python3
```

---

#### Permission denied on execution

**Symptom:** `./script.sh: Permission denied`

**Solution:**
```bash
chmod +x script.sh
./script.sh
```

---

### macOS specific

#### SSL certificate errors

**Symptom:** SSL verification errors with pip

**Solution:**
```bash
# Install certificates
/Applications/Python\ 3.x/Install\ Certificates.command
```

---

## Performance Issues

### Slow Startup

**Causes:**
- Large number of personas
- Slow file system
- Many node_modules

**Solutions:**
1. Use SSD if possible
2. Limit persona scanning
3. Use production mode for frontend

---

### High Memory Usage

**Causes:**
- Development mode
- Many large files
- Memory leaks

**Solutions:**
```bash
# Frontend: Use production build
npm run build
npm start  # Instead of npm run dev

# Backend: Limit workers
uvicorn main:app --workers 1
```

---

### Slow File Operations

**Symptoms:** Slow persona creation/editing

**Causes:**
- Network drive
- Antivirus scanning
- Slow disk

**Solutions:**
1. Use local drive for JAN_ROOT
2. Add exclusions to antivirus
3. Optimize file system

---

## Quick Reference

### Health Checks

```bash
# Backend health
curl http://localhost:8000/health

# Frontend health
curl http://localhost:3000

# Docker health
docker-compose ps
```

### Service Status

```bash
# Check if processes running
# Windows
tasklist | findstr "python\|node"

# Mac/Linux
ps aux | grep "python\|node"
```

### Log Locations

```bash
# Backend logs (console output)
python main.py 2>&1 | tee backend.log

# Frontend logs (console output)
npm run dev 2>&1 | tee frontend.log

# Docker logs
docker-compose logs -f backend
docker-compose logs -f frontend
```

---

## Getting More Help

### Before Asking for Help

1. Check this troubleshooting guide
2. Review INSTALL.md for setup steps
3. Check console/terminal for error messages
4. Check browser console (F12) for frontend issues
5. Verify all prerequisites are installed

### Information to Provide

When reporting issues, include:
1. Operating system and version
2. Python version (`python --version`)
3. Node.js version (`node --version`)
4. Full error message
5. Steps to reproduce
6. What you've already tried

### Useful Commands

```bash
# System information
python --version
node --version
npm --version
docker --version

# Service status
curl http://localhost:8000/health
curl http://localhost:3000

# Process information
# Windows
netstat -ano | findstr "3000\|8000"
tasklist | findstr "python\|node"

# Mac/Linux
lsof -i :3000 -i :8000
ps aux | grep "python\|node"
```

---

## Reset Everything

If all else fails, complete reset:

```bash
# Stop all services
# Ctrl+C in terminals running backend/frontend
# Or: docker-compose down

# Backend reset
cd S:/JAN/jan-studio/backend
rm -rf __pycache__ *.pyc .pytest_cache venv
rm -f marketplace.db

# Frontend reset
cd S:/JAN/jan-studio/frontend
rm -rf node_modules .next package-lock.json

# Reinstall
cd backend
pip install -r requirements.txt

cd ../frontend
npm install

# Restart
# Terminal 1: cd backend && python main.py
# Terminal 2: cd frontend && npm run dev
```

---

**Last Updated:** 2026-01-13
**Version:** 1.0
**Status:** Ready for Week 2 Testing
