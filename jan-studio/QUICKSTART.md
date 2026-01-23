# JAN Studio Quick Start

**Get JAN Studio running in 5 minutes.**

---

## Prerequisites Check

Verify you have the required software:

```bash
python --version  # Should be 3.8+
node --version    # Should be 18+
```

If missing, install from:
- Python: https://python.org
- Node.js: https://nodejs.org

---

## Step 1: Setup Environment (30 seconds)

```bash
# Navigate to jan-studio
cd S:/JAN/jan-studio

# Copy environment template
cp .env.example .env

# Optional: Edit .env to set JAN_ROOT
# Default ./jan works fine for testing
```

**What should I see?**
- `.env` file created
- No errors

---

## Step 2: Install Backend (2 minutes)

```bash
# Navigate to backend
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Initialize JAN directory structure
python setup_jan_structure.py
```

**What should I see?**
```
Successfully installed fastapi-0.104.0 uvicorn-0.24.0 ...
Creating JAN structure at: ./jan
✅ JAN structure created successfully!
```

---

## Step 3: Start Backend (10 seconds)

```bash
# Start backend server
python main.py
```

**What should I see?**
```
INFO:     Started server process [12345]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000
```

**✅ Checkpoint:** Backend is running!

**Verify:**
```bash
# In another terminal
curl http://localhost:8000/health
# Should return: {"status":"healthy","service":"JAN Studio API"}
```

---

## Step 4: Install Frontend (2 minutes)

**Open a NEW terminal** (keep backend running)

```bash
# Navigate to frontend
cd S:/JAN/jan-studio/frontend

# Install Node dependencies
npm install
```

**What should I see?**
```
added 250+ packages in 30s
```

---

## Step 5: Start Frontend (10 seconds)

```bash
# Start development server
npm run dev
```

**What should I see?**
```
ready - started server on 0.0.0.0:3000, url: http://localhost:3000
event - compiled client and server successfully
```

**✅ Checkpoint:** Frontend is running!

---

## Step 6: Access JAN Studio (5 seconds)

**Open your browser:** http://localhost:3000

**What should I see?**
- JAN Studio header
- "Create New Persona" button
- Clean, modern interface
- No error messages

**✅ Checkpoint:** JAN Studio is accessible!

---

## Step 7: Create Your First Persona (30 seconds)

1. Click **"Create New Persona"**
2. Enter name: **test-persona**
3. Click **"Create"**
4. Wait for success message
5. See **test-persona** in the list

**✅ Checkpoint:** Persona created successfully!

---

## Step 8: Verify Files Created

```bash
# Check files were created
ls -la S:/JAN/Siyem.org/test-persona/
```

**What should I see?**
```
profile.md
creative_rules.md
prompt_templates/
```

**✅ Checkpoint:** Files created correctly!

---

## 🎉 Success!

You now have JAN Studio running with:
- ✅ Backend on http://localhost:8000
- ✅ Frontend on http://localhost:3000
- ✅ First persona created
- ✅ Files in correct JAN structure

---

## Next Steps

### 1. Edit Your Persona

1. Click on **test-persona** in the list
2. Edit **profile.md**
3. Save changes
4. See updates reflected

### 2. Explore Templates

```bash
# Save persona as template
curl -X POST "http://localhost:8000/api/templates/save-from-persona?persona_name=test-persona&template_name=my-template"

# List templates
curl http://localhost:8000/api/templates/list
```

### 3. Use API

**Open:** http://localhost:8000/docs

Explore interactive API documentation.

### 4. Create More Personas

Repeat Step 7 with different names to create more personas.

---

## Troubleshooting

### Backend Won't Start

**Problem:** Port 8000 in use

**Solution:**
```bash
# Kill process on port 8000
netstat -ano | findstr :8000  # Windows
lsof -ti:8000 | xargs kill -9 # Mac/Linux
```

**Problem:** Missing dependencies

**Solution:**
```bash
pip install -r requirements.txt
```

---

### Frontend Won't Start

**Problem:** Port 3000 in use

**Solution:**
```bash
# Use different port
npm run dev -- -p 3001
```

**Problem:** Module not found

**Solution:**
```bash
rm -rf node_modules package-lock.json
npm install
```

---

### Can't Create Persona

**Problem:** Network error in browser

**Check:**
```bash
# Is backend running?
curl http://localhost:8000/health
```

**Solution:** Ensure backend is running (Step 3)

---

### For More Help

**See full troubleshooting guide:** [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

**See complete installation:** [INSTALL.md](INSTALL.md)

---

## Docker Quick Start

**Alternative: Use Docker instead**

```bash
# Navigate to JAN root
cd S:/JAN

# Copy environment file
cp jan-studio/.env.example .env

# Start with Docker
docker-compose up -d

# Open browser
# http://localhost:3000
```

**Services:**
- Backend: http://localhost:8000
- Frontend: http://localhost:3000

---

## Summary

**Time:** ~5 minutes
**Steps:** 8 steps
**Result:** Fully functional JAN Studio

**You can now:**
- ✅ Create personas
- ✅ Edit persona files
- ✅ Use templates
- ✅ Access API
- ✅ Manage multiple personas

---

**Ready for more?** See [INSTALL.md](INSTALL.md) for advanced configuration.

**Having issues?** See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for solutions.

**Want to understand?** See [README.md](README.md) for complete documentation.

---

**Version:** 1.0.0 | **Updated:** 2026-01-13 | **Status:** Ready for Testing
