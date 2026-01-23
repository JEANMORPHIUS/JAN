# Raspberry Pi Display System
## Kiosk Mode Display for World History

**DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE**  
**Spiritual Alignment Over Mechanical Productivity**

**THE MISSION:**  
**THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS**  
**LOVE IS THE HIGHEST MASTERY**  
**ENERGY + LOVE = WE ALL WIN**  
**PEACE, LOVE, UNITY**

**PANGEA IS THE TABLE.**  
**YOU DON'T BETRAY THE TABLE.**

---

## Overview

The Raspberry Pi Display System is a lightweight React application designed for museum installations, public kiosks, and educational displays. It provides:

- **Auto-rotate slides** - Timeline, map, frequency, featured site
- **Touch interaction** - Swipe, tap, pinch gestures
- **Offline-first** - Cached data for offline operation
- **Low power mode** - Screen dim after 5 minutes

---

## Setup

### Prerequisites

- Raspberry Pi 4
- Node.js 18+
- Display (touchscreen recommended)

### Installation

```bash
# Install dependencies
npm install

# Build for production
npm run build

# Serve (use a simple HTTP server)
npx serve -s dist
```

### Docker Deployment

```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
EXPOSE 3000
CMD ["npx", "serve", "-s", "dist", "-l", "3000"]
```

---

## Features

### Auto-Rotate
- Rotates through slides every 30 seconds
- Manual navigation via touch controls
- Slide indicators

### Touch Interaction
- Swipe left/right to navigate
- Tap to expand details
- Pinch to zoom (future)

### Offline-First
- Caches data locally
- Falls back to cached data if API unavailable
- Auto-updates from central server (nightly)

### Low Power Mode
- Screen dims after 5 minutes of inactivity
- Wakes on touch

---

## Configuration

Set environment variables:
- `VITE_API_URL` - API endpoint (default: http://localhost:8000)

---

**PEACE, LOVE, UNITY**

**ENERGY + LOVE = WE ALL WIN**

**PURPOSE NOT PERFORMANCE**

**AUTHENTIC AND ALIGNED**

**NON-NEGOTIABLE**

---

*Raspberry Pi Display System - World History Kiosk*
