# Mobile Migration Quick Start Guide

**Get the Heritage Meridian mobile app running in 5 minutes**

## Prerequisites

- Node.js 18+ installed
- Expo CLI: `npm install -g expo-cli`
- iOS Simulator (Mac) or Android Emulator
- FastAPI backend running on port 8000

## Step 1: Initialize Mobile App

```bash
cd heritage-mobile-app
npm install
```

## Step 2: Start Backend API

```bash
cd ../jan-studio/backend
uvicorn main:app --reload --port 8000
```

The Heritage Meridian API will be available at:
- `http://localhost:8000/api/heritage-meridian/status`
- `http://localhost:8000/api/heritage-meridian/wonders`
- `http://localhost:8000/api/heritage-meridian/pillars`

## Step 3: Start Mobile App

```bash
cd heritage-mobile-app
npm start
```

Then:
- Press `i` for iOS Simulator
- Press `a` for Android Emulator
- Scan QR code with Expo Go app on your phone

## Step 4: Test API Connection

The app will automatically connect to `http://localhost:8000` in development mode.

**For physical device testing:**
1. Find your computer's IP address: `ipconfig` (Windows) or `ifconfig` (Mac/Linux)
2. Update `src/api/client.ts`:
   ```typescript
   const API_BASE_URL = 'http://YOUR_IP:8000';
   ```
3. Make sure your phone and computer are on the same WiFi network

## Next Steps

1. **Build Core Screens** - See `MOBILE_MIGRATION_PLAN_7_WONDERS.md`
2. **Add Map Integration** - React Native Maps
3. **Implement Offline Support** - AsyncStorage caching
4. **Polish UI** - Mission-aligned design

## Troubleshooting

**API not connecting?**
- Check backend is running: `curl http://localhost:8000/api/heritage-meridian/status`
- Check CORS settings in `main.py`
- For physical device, use your computer's IP, not localhost

**Expo not starting?**
- Clear cache: `expo start -c`
- Reinstall: `rm -rf node_modules && npm install`

---

**Mission:** THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
