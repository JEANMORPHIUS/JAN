# JAN Ecosystem Mobile App

**Complete mobile app for the entire JAN ecosystem - All channels, entities, projects, and systems**

## Mission

**"THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS"**  
**"LOVE IS THE HIGHEST MASTERY"**  
**"ENERGY + LOVE = WE ALL WIN"**

## Features

### ✅ Heritage & Wonders
- **7 Wonders of the World** explorer with full details
- **Seven Pillars** view with network health
- **Heritage Meridian System** map visualization
- **Shell vs Seed** analysis (modern distortion vs original function)
- **Meridian connections** network display

### ✅ Interactive Map
- All wonders and pillars on one map
- Color-coded markers by field resonance
- Meridian lines visualization
- User location tracking
- Filter controls (All/Wonders/Pillars)
- Map type toggle (Standard/Satellite)

### ✅ GPS Integration
- **Find nearby heritage sites** within configurable radius
- Distance calculation and direction
- Sort by proximity
- Pull-to-refresh support

### ✅ Offline Support
- AsyncStorage caching
- Offline-first loading
- Network detection
- Automatic sync when online
- Manual refresh option

### ✅ Share & Navigation
- Share wonder information
- Get directions to sites (Google Maps)
- Native share functionality

## Setup

```bash
# Install dependencies
npm install

# Start development server
npm start

# Run on iOS
npm run ios

# Run on Android
npm run android
```

## Prerequisites

- Node.js 18+
- Expo CLI: `npm install -g expo-cli`
- iOS Simulator (Mac) or Android Emulator
- FastAPI backend running on port 8000

## Backend Connection

The app connects to the FastAPI backend at:
- **Development:** `http://localhost:8000`
- **Production:** Configure in `src/api/client.ts`

**For physical device testing:**
1. Find your computer's IP address: `ipconfig` (Windows) or `ifconfig` (Mac/Linux)
2. Update `src/api/client.ts`:
   ```typescript
   const API_BASE_URL = 'http://YOUR_IP:8000';
   ```
3. Make sure your phone and computer are on the same WiFi network

## Complete Features

### Entities (11)
- ✅ 5 Creative Personas (Jean, Karasahin, Pierre, Ramiz, Siyem)
- ✅ 4 Business Projects (Edible London, Ilven Seamoss, Edible Cyprus, ATILOK)
- ✅ 2 Governance (Siyem.org, JAN Studio)

### Channels (3)
- ✅ Professional Platform
- ✅ Creator Economy Platform
- ✅ Educational Platform

### Systems (13)
- ✅ World History System
- ✅ Frequential Events System
- ✅ Deep Search (23 domains)
- ✅ Nourishment Hive System
- ✅ Seed to Movement System
- ✅ Spiritual Contracts Registry
- ✅ Historical Aligned Individuals
- ✅ All Industries Frequential Value
- ✅ SIYEM Integration
- ✅ Banking & Hidden Spiritual Alignment
- ✅ Financial Controls System
- ✅ Aligned Investments
- ✅ Free Will System

### Heritage
- ✅ 7 Wonders of the World explorer
- ✅ Seven Pillars view
- ✅ Heritage Meridian System map
- ✅ Interactive meridian network

### Core Features
- ✅ Offline support for all systems
- ✅ GPS-based nearby sites
- ✅ Field resonance indicators
- ✅ Shell vs Seed analysis
- ✅ Unified search across all systems
- ✅ Cross-system integration

## Backend Connection

The app connects to the FastAPI backend at:
- **Development:** `http://localhost:8000`
- **Production:** Configure in `src/api/client.ts`

## Project Structure

See `COMPLETE_MOBILE_MIGRATION_ALL_SYSTEMS.md` for full architecture.
