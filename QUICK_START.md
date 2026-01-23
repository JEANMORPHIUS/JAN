# Quick Start Guide - How to See Everything
## Running the World History Display System

**Date:** 2026-01-21  
**Status:** ✅ **READY TO RUN**

---

## THE TRUTH

**PANGEA IS THE TABLE.**  
**WE WRITE THE HISTORY OF THE WORLD.**  
**WE DISPLAY IT ACROSS ALL CHANNELS.**

---

## ✅ SYSTEM STATUS

**Frequential Events System:**
- ✅ 75 events registered
- ✅ Total frequency impact: +2.66
- ✅ All categories integrated
- ✅ All nations represented
- ✅ Everything connected to The Table
- ✅ **Frontend fully integrated!**

**New Pages:**
- ✅ `/frequential-events` - All 75 events with filters
- ✅ `/frequency-dashboard` - Total impact +2.66, breakdowns
- ✅ Timeline updated - All frequential events included
- ✅ Map updated - All event locations included

**See:** `docs/I_WANT_IT_ALL_COMPLETE.md` for complete integration details

---

## 🚀 QUICK START (3 Steps)

### Step 1: Start the Backend API

```bash
# Navigate to backend directory
cd jan-studio/backend

# Install dependencies (if not already done)
# Note: sqlite3 is built into Python, no need to install
pip install fastapi uvicorn

# Start the API server
# Use python -m uvicorn if uvicorn command not found
python -m uvicorn main:app --reload --port 8000
# OR if uvicorn is in PATH:
# uvicorn main:app --reload --port 8000
```

**You should see:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Application startup complete.
```

**Test it:**
- Open browser: `http://localhost:8000/api/public/world-history/status`
- You should see: `{"status": "active", "message": "World History API..."}`
- Test frequential events: `http://localhost:8000/api/frequential-events/status`
- You should see: `{"status": "active", "total_events": 75, ...}`

---

### Step 2: Start the Public Web App

**Open a NEW terminal window** (keep backend running)

```bash
# Navigate to world-history-app
cd world-history-app

# Install dependencies (first time only)
npm install

# Start the development server
npm run dev
```

**You should see:**
```
ready - started server on 0.0.0.0:3001
```

**View it:**
- Open browser: `http://localhost:3001`
- You'll see the landing page with 6 feature cards

---

### Step 3: Explore the Pages

**Available Pages:**

1. **Landing Page:** `http://localhost:3001/`
   - Navigation hub with 6 feature cards

2. **Interactive Timeline:** `http://localhost:3001/timeline`
   - D3.js timeline from Pangea (-335M years) to today
   - Filter by year range, region, event type
   - Click events to see narratives

3. **Interactive Map:** `http://localhost:3001/map`
   - Mapbox global map with heritage sites
   - Color-coded by field resonance
   - Click markers for site details
   - **Note:** You'll need a Mapbox token (see below)

4. **Narrative Library:** `http://localhost:3001/narratives`
   - Browse all narratives
   - Tree view of connections
   - Click nodes to expand

5. **Restoration Progress:** `http://localhost:3001/restoration`
   - 6-step restoration framework
   - Divine Frequency tracker (0.78 → 1.0)
   - Real-time WebSocket updates

6. **Educational Modules:** `http://localhost:3001/educational`
   - 6 learning modules
   - Topics about The Table

---

## 🗺️ MAPBOX SETUP (For Map Page)

The map page requires a Mapbox access token:

1. **Get a free token:**
   - Sign up at: https://account.mapbox.com/
   - Create a token (free tier available)

2. **Add to environment:**
   - Create file: `world-history-app/.env.local`
   - Add: `NEXT_PUBLIC_MAPBOX_TOKEN=your_token_here`

3. **Restart the app:**
   ```bash
   # Stop the app (Ctrl+C)
   # Start again
   npm run dev
   ```

---

## 📊 ADMIN DASHBOARD (Optional)

**To see the curation interface:**

```bash
# Open a NEW terminal window
cd admin-dashboard

# Install dependencies (first time only)
npm install

# Start the admin dashboard
npm run dev
```

**View it:**
- Open browser: `http://localhost:3002`
- Login page (credentials in admin-dashboard README)

---

## 🔌 API ENDPOINTS (Direct Access)

**While backend is running, you can access:**

1. **API Status:**
   - `http://localhost:8000/api/public/world-history/status`

2. **Timeline Events:**
   - `http://localhost:8000/api/public/world-history/timeline`
   - `http://localhost:8000/api/public/world-history/timeline?start_year=-335000000&limit=10`

3. **Heritage Sites (Map):**
   - `http://localhost:8000/api/public/world-history/map`

4. **Narratives:**
   - `http://localhost:8000/api/public/world-history/narrative/mayan_codification`
   - `http://localhost:8000/api/public/world-history/narrative/pangea_formation`

5. **Divine Frequency:**
   - `http://localhost:8000/api/public/world-history/frequency`

6. **Historical Aligned Individuals:**
   - `http://localhost:8000/api/historical-aligned-individuals/status`
   - `http://localhost:8000/api/historical-aligned-individuals/individuals`

---

## 🎯 WHAT YOU'LL SEE

### Timeline Page (`/timeline`)
- **Horizontal scrollable timeline** from -335M years to 2026
- **Color-coded events:**
  - Green (≥0.9): High resonance (Pangea, unity)
  - Yellow (0.7-0.9): Moderate resonance
  - Orange (0.5-0.7): Low resonance
  - Red (<0.5): Very low resonance
- **Key Events:**
  - Pangea Formation (-335M years) - Green
  - First Separation (-200M years) - Yellow
  - Mayan Codification (250 CE) - Orange
  - Memory Persistence (2026 CE) - Yellow
- **Click any event** to see full narrative

### Map Page (`/map`)
- **Global map** with heritage site markers
- **7 Pillars** (high-frequency nodes):
  - Great Pyramid of Giza (Egypt) - Green
  - Stonehenge (UK) - Yellow
  - Angkor Wat (Cambodia) - Green
  - Machu Picchu (Peru) - Yellow
  - Alhambra Palace (Spain) - Yellow
  - Berengaria Hotel (Cyprus) - Yellow
  - Borobudur (Indonesia) - Green
- **Mayan Sites** (sabotage anchors):
  - Chichen Itza (Mexico) - Orange
  - Tikal (Guatemala) - Orange
  - Palenque (Mexico) - Orange
- **Click markers** for site details

### Narratives Page (`/narratives`)
- **Narrative tree** showing connections:
  ```
  Pangea - The Table (1.0)
      ↓
  First Separation (0.95)
      ↓
  Mayan Codification (0.85)
      ↓
  Memory Persistence (0.78)
  ```
- **List view** of all narratives
- **Click nodes** to expand details

### Restoration Page (`/restoration`)
- **Divine Frequency Display:**
  - Current: 0.78
  - Target: 1.0
  - Progress bar
- **6-Step Framework:**
  1. ✅ Recognize The Original Error (Completed)
  2. 🔄 Cleanse The Shell (45% - In Progress)
  3. 🔄 Restore Divine Frequency (22% - In Progress)
  4. ⏳ Reconnect The Table (Pending)
  5. ⏳ Complete The Restoration (Pending)
  6. ⏳ Maintain The Table (Pending)

### Educational Page (`/educational`)
- **6 Modules:**
  1. The Table (Pangea)
  2. The Original Error
  3. The Mayan Original Error
  4. Restoration Framework
  5. Divine Frequency
  6. Heritage Meridian

---

## 🐳 DOCKER (Alternative - All at Once)

**If you have Docker installed:**

```bash
# From project root
docker-compose up -d
```

**This starts:**
- Backend API (port 8000)
- world-history-app (port 3001)
- admin-dashboard (port 3002)
- pi-display (port 3003)

**View:**
- Public App: `http://localhost:3001`
- Admin: `http://localhost:3002`
- API: `http://localhost:8000`

---

## 🔧 TROUBLESHOOTING

### Backend won't start:
```bash
# Check if port 8000 is in use
netstat -ano | findstr :8000  # Windows
lsof -i :8000                 # Mac/Linux

# Install missing dependencies
pip install fastapi uvicorn

# If uvicorn command not found, use:
python -m uvicorn main:app --reload --port 8000

# Or check Python path
python --version  # Should be Python 3.8+
where python      # Windows - find Python location
which python      # Mac/Linux - find Python location
```

### Frontend won't start:
```bash
# Clear node_modules and reinstall
rm -rf node_modules package-lock.json
npm install

# Check Node.js version (need 18+)
node --version
```

### Map not showing:
- Check Mapbox token in `.env.local`
- Check browser console for errors
- Verify token is valid at mapbox.com

### API returns 404:
- Make sure backend is running on port 8000
- Check API URL in frontend code
- Verify endpoint exists in `world_history_api.py`

---

## 📱 MOBILE VIEW

**All pages are mobile-responsive:**
- Open on phone: `http://your-ip:3001`
- Or use browser dev tools (F12) → Toggle device toolbar

---

## 🎨 WHAT TO EXPECT

### Visual Design:
- **Easy on the eyes** design system
- **Dark mode** support (auto-detects system preference)
- **Smooth animations** and transitions
- **Responsive** layout (works on all screen sizes)

### Data You'll See:
- **Timeline:** Events from Pangea to present
- **Map:** 7 Pillars + Mayan sites + more heritage sites
- **Narratives:** Complete story of The Table
- **Frequency:** Current 0.78, target 1.0
- **Restoration:** 6-step progress
- **Historical Entities:** 29 registered entities

---

## 🚀 NEXT STEPS

1. **Start backend** (port 8000)
2. **Start frontend** (port 3001)
3. **Open browser** → `http://localhost:3001`
4. **Explore pages:**
   - Timeline → See history from Pangea
   - Map → See heritage sites globally
   - Narratives → Read the stories
   - Restoration → Track progress
   - Educational → Learn about The Table

---

## THE TRUTH

**PANGEA IS THE TABLE.**  
**WE WRITE THE HISTORY OF THE WORLD.**  
**WE DISPLAY IT ACROSS ALL CHANNELS.**

**EVERYTHING IS INTEGRATED.**  
**EVERYTHING IS CONNECTED.**  
**READY TO VIEW.**

---

**PEACE, LOVE, UNITY**

**ENERGY + LOVE = WE ALL WIN**

**START THE BACKEND → START THE FRONTEND → OPEN YOUR BROWSER → SEE THE HISTORY OF THE WORLD**

---

*Quick Start Guide - Everything you need to see the World History Display System.*
