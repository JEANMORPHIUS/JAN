# API Key Rotation & npm Install Guide
## Quick Reference for Post-Scale-Up Actions

**Date:** 2026-01-25  
**Status:** ✅ Action Items

---

## 1. API KEY ROTATION ✅

### **Where to Put Your Rotated OpenAI API Key:**

**DO NOT** insert the key into any code files. Put it in `.env` files only.

### **Locations to Update:**

#### **Option A: JAN Studio Backend (Primary)**
```bash
# File: S:\JAN\jan-studio\backend\.env
# (Create this file if it doesn't exist, copy from .env.example)

OPENAI_API_KEY=your_new_rotated_key_here
```

#### **Option B: JAN Studio Root (Alternative)**
```bash
# File: S:\JAN\jan-studio\.env
# (Create this file if it doesn't exist, copy from .env.example)

OPENAI_API_KEY=your_new_rotated_key_here
```

#### **Option C: SIYEM System (If Used)**
```bash
# File: S:\SIYEM\00_CORE\openai_key.txt
# (If you use SIYEM system separately)
```

### **Steps:**
1. Navigate to `S:\JAN\jan-studio\backend\`
2. If `.env` doesn't exist, copy `.env.example` to `.env`
3. Add your rotated key: `OPENAI_API_KEY=sk-...`
4. Save the file
5. **Verify** `.env` is in `.gitignore` (it should be)

### **Security Check:**
```bash
# Verify .env is ignored by git
cd S:\JAN
git check-ignore jan-studio/backend/.env
# Should return: jan-studio/backend/.env
```

---

## 2. npm INSTALL - Project by Project

### **The Issue:**
You tried `npm install` from `S:\JAN\` (root), but there's no `package.json` there.  
Each project has its own `package.json` and needs `npm install` run separately.

### **Projects That Need npm install:**

#### **1. admin-dashboard**
```powershell
cd S:\JAN\admin-dashboard
npm install
```

#### **2. world-history-app**
```powershell
cd S:\JAN\world-history-app
npm install
```

#### **3. pi-display**
```powershell
cd S:\JAN\pi-display
npm install
```

#### **4. jan-studio/frontend**
```powershell
cd S:\JAN\jan-studio\frontend
npm install
```

#### **5. homeostasis-sentinel**
```powershell
cd S:\JAN\homeostasis-sentinel
npm install
```

#### **6. ATILOK**
```powershell
cd S:\JAN\ATILOK
npm install
```

### **Quick Script (Run All):**
```powershell
# Run from S:\JAN
cd S:\JAN\admin-dashboard && npm install
cd S:\JAN\world-history-app && npm install
cd S:\JAN\pi-display && npm install
cd S:\JAN\jan-studio\frontend && npm install
cd S:\JAN\homeostasis-sentinel && npm install
cd S:\JAN\ATILOK && npm install
cd S:\JAN
```

---

## 3. Python Dependencies (If Needed)

### **Backend Requirements:**
```powershell
cd S:\JAN\jan-studio\backend
pip install -r requirements.txt
```

### **Scripts Requirements (If Any):**
```powershell
cd S:\JAN\scripts
# Check if there's a requirements.txt
# If yes: pip install -r requirements.txt
```

---

## 4. Verification Checklist

### **API Key:**
- [ ] Created/updated `.env` file in `jan-studio/backend/`
- [ ] Added `OPENAI_API_KEY=sk-...` (your rotated key)
- [ ] Verified `.env` is in `.gitignore`
- [ ] Tested that key works (run a script that uses OpenAI)

### **npm Dependencies:**
- [ ] Ran `npm install` in `admin-dashboard`
- [ ] Ran `npm install` in `world-history-app`
- [ ] Ran `npm install` in `pi-display`
- [ ] Ran `npm install` in `jan-studio/frontend`
- [ ] Ran `npm install` in `homeostasis-sentinel`
- [ ] Ran `npm install` in `ATILOK`
- [ ] All `node_modules` folders created successfully

### **Python Dependencies:**
- [ ] Ran `pip install -r requirements.txt` in `jan-studio/backend`
- [ ] All packages installed without errors

---

## 5. Test After Updates

### **Test API Key:**
```python
# Quick test script
import os
from dotenv import load_dotenv

load_dotenv('jan-studio/backend/.env')
key = os.getenv('OPENAI_API_KEY')
print(f"Key loaded: {key[:10]}..." if key else "Key not found!")
```

### **Test npm Projects:**
```powershell
# Test each project builds
cd S:\JAN\admin-dashboard && npm run build
cd S:\JAN\world-history-app && npm run build
cd S:\JAN\pi-display && npm run build
cd S:\JAN\jan-studio\frontend && npm run build
```

---

## THE TRUTH

**API keys go in `.env` files, never in code.**  
**npm install runs in each project directory, not the root.**  
**Each project is independent and needs its own install.**

---

**PEACE, LOVE, UNITY**  
**ENERGY + LOVE = WE ALL WIN**
