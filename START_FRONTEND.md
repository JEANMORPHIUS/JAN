# START FRONTEND - Quick Guide

**Date:** 2026-01-27  
**Status:** ✅ **FRONTEND STARTUP GUIDE**

---

## THE ISSUE

**You tried:** `NPM RUN DEV`  
**Error:** Unknown command: "RUN"

**The fix:** Use lowercase: `npm run dev`

---

## CORRECT COMMANDS

### **Step 1: Navigate to Frontend**
```powershell
cd S:\JAN\jan-studio\frontend
```

### **Step 2: Install Dependencies (First Time Only)**
```powershell
npm install
```

**Expected:** `added 250+ packages in 45s`

### **Step 3: Start Development Server**
```powershell
npm run dev
```

**Expected Output:**
```
- ready started server on 0.0.0.0:3000
- url: http://localhost:3000
```

---

## QUICK START (All in One)

**If dependencies not installed:**
```powershell
cd S:\JAN\jan-studio\frontend
npm install
npm run dev
```

**If dependencies already installed:**
```powershell
cd S:\JAN\jan-studio\frontend
npm run dev
```

---

## WHAT YOU'LL SEE

**After `npm run dev`:**
- Server starts on `http://localhost:3000`
- Next.js compiles
- Frontend connects to backend (`http://localhost:8000`)

**Open browser:**
- `http://localhost:3000` - Frontend
- `http://localhost:8000` - Backend API
- `http://localhost:8000/docs` - API Documentation

---

## TROUBLESHOOTING

### **Port 3000 Already in Use**
```powershell
npm run dev -- -p 3001
```

### **Module Not Found Errors**
```powershell
npm install
```

### **Backend Not Connected**
- Make sure backend is running: `cd S:\JAN\jan-studio\backend && python main.py`
- Check: `http://localhost:8000/health`

---

## THE TRUTH

**PowerShell is case-sensitive for npm commands:**
- ❌ `NPM RUN DEV` - Doesn't work
- ✅ `npm run dev` - Works

**Always use lowercase for npm commands.**

---

**SPRAGITSO - Our Father's Royal Seal** ✨🙏

**Frontend starting. Backend running. System deploying. Mission serving.**

🌊✨
