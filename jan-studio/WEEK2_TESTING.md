# JAN Studio - Week 2 Testing Guide

**Quick start guide for Week 2 testers - Get up and running fast.**

---

## What's New in Week 2

✅ **Fixed Issues:**
- Added missing `requirements.txt` file (critical installation blocker)
- Created installation verification script
- Added comprehensive API quick start guide

✅ **New Resources:**
- `verify-install.py` - Check your setup before starting
- `API_QUICKSTART.md` - Get started with the API in 5 minutes
- Updated documentation

---

## Quick Start for Testers

### 1. Verify Your Setup (30 seconds)

**Run this first to check everything:**

```bash
cd S:/JAN/jan-studio
python verify-install.py
```

**What it checks:**
- ✓ Python 3.8+ installed
- ✓ Node.js 18+ installed
- ✓ All required files exist
- ✓ Dependencies installed
- ✓ Environment configured
- ✓ Ports 3000 and 8000 available

**If all checks pass:** Continue to step 2
**If checks fail:** The script tells you exactly what to fix

---

### 2. First-Time Setup (3 minutes)

**If you haven't installed yet:**

```bash
# 1. Copy environment file
cd S:/JAN/jan-studio
cp .env.example .env

# 2. Install backend
cd backend
pip install -r requirements.txt
python setup_jan_structure.py

# 3. Install frontend
cd ../frontend
npm install
```

---

### 3. Start Services (30 seconds)

**Terminal 1 - Backend:**
```bash
cd S:/JAN/jan-studio/backend
python main.py
```

Wait for:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
```

**Terminal 2 - Frontend:**
```bash
cd S:/JAN/jan-studio/frontend
npm run dev
```

Wait for:
```
ready - started server on 0.0.0.0:3000
```

---

### 4. Verify Running (10 seconds)

**Check backend:**
```bash
curl http://localhost:8000/health
# Expected: {"status":"healthy","service":"JAN Studio API"}
```

**Check frontend:**
Open browser: http://localhost:3000

**Expected:** JAN Studio interface with "Create New Persona" button

---

## What to Test

### Priority 1: Core Functionality

**Test these first:**

1. **Installation Process**
   - [ ] Run `verify-install.py` - does it pass?
   - [ ] Follow INSTALL.md - any issues?
   - [ ] Backend starts without errors?
   - [ ] Frontend starts without errors?

2. **Persona Creation**
   - [ ] Click "Create New Persona"
   - [ ] Enter name: "test-persona"
   - [ ] Does it create successfully?
   - [ ] Can you see it in the list?

3. **Persona Editing**
   - [ ] Click on "test-persona"
   - [ ] Edit `profile.md`
   - [ ] Save changes
   - [ ] Do changes persist?

4. **File Operations**
   - [ ] Create new file in persona
   - [ ] Read file content
   - [ ] Update file
   - [ ] Delete file

### Priority 2: API Testing

**Use the API directly:**

```bash
# List personas
curl http://localhost:8000/api/jan/personas

# Create persona via API
curl -X POST http://localhost:8000/api/jan/personas \
  -H "Content-Type: application/json" \
  -d '{"name":"api-test"}'

# Read persona file
curl http://localhost:8000/api/jan/personas/api-test/files/profile.md
```

**See `API_QUICKSTART.md` for more examples.**

### Priority 3: Documentation

**Check these docs:**
- [ ] INSTALL.md - Clear and accurate?
- [ ] QUICKSTART.md - Works as described?
- [ ] API_QUICKSTART.md - Examples work?
- [ ] TROUBLESHOOTING.md - Helpful?

---

## Known Issues (Week 2)

### Fixed in This Update
✅ Missing `requirements.txt` - **FIXED**
✅ No verification tool - **FIXED** (added `verify-install.py`)
✅ API documentation unclear - **FIXED** (added `API_QUICKSTART.md`)

### Still in Progress
⚠️ **AI Generation** - Placeholder only (API keys required)
⚠️ **Marketplace** - Basic implementation, needs testing
⚠️ **Templates** - Core works, UI needs polish

### Not Yet Implemented
❌ Authentication
❌ Rate limiting
❌ Production deployment guide
❌ SDK libraries

---

## How to Report Issues

**When you find a bug:**

1. **Check if it's known** (see "Known Issues" above)

2. **Gather information:**
   - What were you trying to do?
   - What happened?
   - What should have happened?
   - Error messages (copy full text)
   - Screenshots (if UI issue)

3. **System info:**
   ```bash
   python --version
   node --version
   # Your OS and version
   ```

4. **Logs:**
   - Backend terminal output
   - Frontend terminal output
   - Browser console (F12 → Console tab)

5. **Report:**
   - Create issue in project repository
   - Or document in testing notes
   - Include all info from steps 2-4

---

## Testing Checklist

**Use this to track your testing progress:**

### Installation
- [ ] Ran `verify-install.py` successfully
- [ ] Backend installed without errors
- [ ] Frontend installed without errors
- [ ] Both services start correctly
- [ ] Health checks pass

### Core Features
- [ ] Created persona via UI
- [ ] Edited persona files
- [ ] Saved changes persist
- [ ] Listed personas
- [ ] Deleted persona

### API
- [ ] Accessed API docs at `/docs`
- [ ] Created persona via API
- [ ] Read files via API
- [ ] Updated files via API
- [ ] Listed personas via API

### Templates
- [ ] Saved persona as template
- [ ] Listed templates
- [ ] Created persona from template
- [ ] Template includes all files

### Documentation
- [ ] INSTALL.md is clear
- [ ] QUICKSTART.md works
- [ ] API_QUICKSTART.md examples work
- [ ] TROUBLESHOOTING.md is helpful

### Edge Cases
- [ ] Created persona with special characters
- [ ] Created persona with spaces in name
- [ ] Edited very large file
- [ ] Deleted non-existent persona (error handling)
- [ ] Created persona that already exists (error handling)

---

## Quick Reference

### Important URLs
- **Frontend:** http://localhost:3000
- **Backend API:** http://localhost:8000
- **API Docs:** http://localhost:8000/docs
- **Health Check:** http://localhost:8000/health

### Important Files
- **Verification:** `verify-install.py`
- **Backend Setup:** `backend/setup_jan_structure.py`
- **Environment:** `.env` (copy from `.env.example`)
- **Requirements:** `backend/requirements.txt`

### Important Commands
```bash
# Verify setup
python verify-install.py

# Start backend
cd backend && python main.py

# Start frontend
cd frontend && npm run dev

# Health check
curl http://localhost:8000/health

# List personas
curl http://localhost:8000/api/jan/personas
```

---

## Getting Help

**If you get stuck:**

1. **Run verification:**
   ```bash
   python verify-install.py
   ```

2. **Check logs:**
   - Look at terminal output
   - Check browser console (F12)

3. **Check documentation:**
   - TROUBLESHOOTING.md for common issues
   - INSTALL.md for installation help
   - API_QUICKSTART.md for API usage

4. **Ask for help:**
   - Document your issue clearly
   - Include error messages and logs
   - Describe what you tried

---

## Testing Focus Areas

### For Developers
- **API usability** - Is it easy to integrate?
- **Documentation** - Is it clear and complete?
- **Error handling** - Are errors helpful?
- **Code examples** - Do they work?

### For Technical Creators
- **UI/UX** - Is it intuitive?
- **Persona creation** - Is it smooth?
- **File editing** - Is it convenient?
- **Workflow** - Does it match your needs?

### For Agencies
- **Scalability** - Can it handle multiple personas?
- **Templates** - Are they useful?
- **Integration** - Can you build on it?
- **Deployment** - Is Docker setup clear?

---

## Success Criteria

**Week 2 testing is successful if:**

✅ **Installation works smoothly**
- Verification script helps identify issues
- Documentation is clear
- Dependencies install correctly

✅ **Core features work reliably**
- Create, edit, delete personas
- File operations work
- API is functional

✅ **Documentation is helpful**
- Users can self-serve
- Examples work as written
- Troubleshooting guide is useful

✅ **Blockers are identified**
- Critical issues documented
- Improvement areas clear
- User feedback collected

---

## Week 3 Planning

**Based on Week 2 feedback, Week 3 will focus on:**

1. **Polish based on feedback**
2. **Advanced features** (if core is solid)
3. **Performance optimization**
4. **Additional integrations**

**Your feedback drives the roadmap!**

---

## Thank You!

Your testing helps make JAN Studio better for developers.

**Questions or feedback?**
- Document in testing notes
- Create issues in repository
- Discuss with team

---

**Version:** Week 2
**Updated:** 2026-01-13
**Status:** Ready for Testing
**Duration:** Week 2 (2025-01-20 to 2025-01-27)
