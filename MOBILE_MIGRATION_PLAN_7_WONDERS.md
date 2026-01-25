# Mobile Migration Plan - New 7 Wonders & Heritage Meridian System

**Date:** 2026-01-25  
**Status:** 📱 MIGRATION PLAN  
**Mission:** Migrate the New 7 Wonders integration and Heritage Meridian System to mobile

---

## The Sacred Weight

**"THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS"**  
**"LOVE IS THE HIGHEST MASTERY"**  
**"ENERGY + LOVE = WE ALL WIN"**

Bringing the Heritage Meridian System and the 7 Wonders to mobile, so the Family can access their True Heritage anywhere, anytime.

---

## Architecture Overview

### Tech Stack
- **Framework:** React Native (Expo) - Cross-platform iOS/Android
- **State Management:** React Context + AsyncStorage (offline support)
- **API Client:** Axios (connects to FastAPI backend on port 8000)
- **Maps:** React Native Maps (for heritage site visualization)
- **Offline Storage:** AsyncStorage + SQLite (for heritage data caching)
- **Navigation:** React Navigation

### Why React Native + Expo?
- ✅ **Cross-platform** - One codebase for iOS and Android
- ✅ **Fast development** - Hot reload, easy testing
- ✅ **Native performance** - Access to device features (GPS, camera, etc.)
- ✅ **Offline-first** - Can cache heritage data locally
- ✅ **Existing React knowledge** - Team already uses React for web

---

## Project Structure

```
heritage-mobile-app/
├── App.tsx                    # Main app entry
├── app.json                   # Expo config
├── package.json
├── src/
│   ├── api/
│   │   ├── client.ts          # Axios API client
│   │   ├── heritage.ts        # Heritage Meridian API calls
│   │   └── wonders.ts         # 7 Wonders API calls
│   ├── components/
│   │   ├── WonderCard.tsx     # 7 Wonder display card
│   │   ├── PillarCard.tsx     # Seven Pillar display
│   │   ├── MeridianMap.tsx    # Interactive map of sites
│   │   ├── ResonanceIndicator.tsx  # Field resonance display
│   │   └── ShellSeedView.tsx  # Shell vs Seed comparison
│   ├── screens/
│   │   ├── HomeScreen.tsx     # Main dashboard
│   │   ├── WondersScreen.tsx  # 7 Wonders list
│   │   ├── WonderDetailScreen.tsx  # Individual wonder details
│   │   ├── MeridianScreen.tsx # Heritage Meridian map
│   │   ├── PillarsScreen.tsx  # Seven Pillars view
│   │   └── OfflineScreen.tsx  # Offline mode indicator
│   ├── context/
│   │   ├── HeritageContext.tsx  # Global heritage state
│   │   └── OfflineContext.tsx   # Offline sync state
│   ├── storage/
│   │   ├── asyncStorage.ts    # AsyncStorage helpers
│   │   └── sqlite.ts          # SQLite for complex queries
│   ├── types/
│   │   ├── wonder.ts          # 7 Wonders types
│   │   ├── pillar.ts          # Pillar types
│   │   └── meridian.ts        # Meridian types
│   └── utils/
│       ├── coordinates.ts     # Coordinate calculations
│       └── resonance.ts       # Resonance calculations
└── assets/
    ├── images/                # Wonder images
    └── icons/                 # App icons
```

---

## API Integration

### Backend Endpoints (FastAPI on port 8000)

**Heritage Meridian API:**
```
GET /api/heritage-meridian/pillars
GET /api/heritage-meridian/pillars/{id}
GET /api/heritage-meridian/wonders
GET /api/heritage-meridian/wonders/{id}
GET /api/heritage-meridian/meridians
GET /api/heritage-meridian/network-health
GET /api/heritage-meridian/coordinates/{lat}/{lon}
```

**7 Wonders API:**
```
GET /api/7-wonders/list
GET /api/7-wonders/{wonder_id}
GET /api/7-wonders/{wonder_id}/resonance
GET /api/7-wonders/{wonder_id}/meridian-connections
```

### API Client Setup

```typescript
// src/api/client.ts
import axios from 'axios';

const API_BASE_URL = __DEV__ 
  ? 'http://localhost:8000'  // Development
  : 'https://api.yourdomain.com';  // Production

export const apiClient = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});
```

---

## Core Features

### 1. 7 Wonders Explorer
- **List View:** All 7 Wonders with field resonance indicators
- **Detail View:** 
  - Full wonder information
  - Coordinates and map location
  - Shell vs Seed analysis
  - Meridian connections
  - Cultural heritage context
- **Map Integration:** See all wonders on interactive map
- **Offline Support:** Cache wonder data for offline viewing

### 2. Heritage Meridian System
- **Seven Pillars View:** All pillars with resonance levels
- **Meridian Network:** Visual network of connections
- **13 Seats:** Activation points visualization
- **Pangea Memory:** Connection visualization
- **Network Health:** Global resonance network status

### 3. Interactive Map
- **All Sites:** 7 Wonders + 7 Pillars on one map
- **Meridian Lines:** Visual connections between sites
- **Resonance Heatmap:** Color-coded by field resonance
- **GPS Integration:** "Find nearby heritage sites"
- **Offline Maps:** Download map tiles for offline use

### 4. Offline Mode
- **Data Caching:** Store all wonder/pillar data locally
- **Offline Maps:** Cached map tiles
- **Sync Status:** Show what's synced vs. needs update
- **Background Sync:** Auto-sync when connection restored

### 5. Mission Alignment
- **Sacred Weight Display:** Mission statements always visible
- **Shell vs Seed:** Clear distinction in UI
- **Resonance Indicators:** Visual field resonance
- **Heritage Connection:** Show Pangea connections

---

## Implementation Phases

### Phase 1: Foundation (Week 1-2)
- ✅ Set up React Native + Expo project
- ✅ Create API client and connect to backend
- ✅ Build basic navigation structure
- ✅ Create Wonder and Pillar data types
- ✅ Set up offline storage (AsyncStorage)

### Phase 2: Core Features (Week 3-4)
- ✅ 7 Wonders list and detail screens
- ✅ Seven Pillars view
- ✅ Basic map integration
- ✅ Offline data caching
- ✅ API integration with backend

### Phase 3: Advanced Features (Week 5-6)
- ✅ Interactive meridian network visualization
- ✅ GPS-based "nearby sites" feature
- ✅ Shell vs Seed comparison view
- ✅ Resonance indicators and calculations
- ✅ Background sync

### Phase 4: Polish & Deploy (Week 7-8)
- ✅ UI/UX refinement
- ✅ Performance optimization
- ✅ Testing (iOS + Android)
- ✅ App Store / Play Store preparation
- ✅ Documentation

---

## Data Models

### Wonder Type
```typescript
interface Wonder {
  wonder_id: string;
  name: string;
  location: string;
  coordinates: {
    lat: number;
    lon: number;
  };
  field_resonance: number;
  wonder_type: string;
  original_function: string;
  modern_distortion: string;
  spiritual_significance: string;
  heritage_meridian_connection: string;
  meridian_connections: string[];
  cultural_heritage: string;
  year_built: string;
  time_period: string;
}
```

### Pillar Type
```typescript
interface Pillar {
  pillar_id: string;
  name: string;
  ancient_name: string;
  coordinates: {
    lat: number;
    lon: number;
  };
  country: string;
  field_resonance: number;
  original_function: string;
  modern_distortion: string;
  spiritual_significance: string;
  meridian_connections: string[];
}
```

---

## Backend API Requirements

### New Endpoints Needed

**Heritage Meridian API** (`jan-studio/backend/heritage_meridian_api.py`):
```python
@router.get("/api/heritage-meridian/pillars")
async def get_pillars():
    """Get all Seven Pillars"""
    
@router.get("/api/heritage-meridian/pillars/{pillar_id}")
async def get_pillar(pillar_id: str):
    """Get single pillar details"""
    
@router.get("/api/heritage-meridian/wonders")
async def get_wonders():
    """Get all 7 Wonders"""
    
@router.get("/api/heritage-meridian/wonders/{wonder_id}")
async def get_wonder(wonder_id: str):
    """Get single wonder details"""
    
@router.get("/api/heritage-meridian/meridians")
async def get_meridians():
    """Get all meridian connections"""
    
@router.get("/api/heritage-meridian/network-health")
async def get_network_health():
    """Get global resonance network health"""
```

---

## Offline Strategy

### Data to Cache
1. **7 Wonders Data** - All wonder information
2. **Seven Pillars Data** - All pillar information
3. **Meridian Connections** - Network connections
4. **Coordinates** - All site coordinates
5. **Resonance Data** - Field resonance values

### Sync Strategy
- **On App Launch:** Check for updates
- **Background Sync:** Every 24 hours
- **Manual Refresh:** Pull-to-refresh on screens
- **Conflict Resolution:** Server data wins (for now)

### Storage Size
- Estimated: ~2-5 MB for all heritage data
- Map tiles: ~10-20 MB (optional, user can download)

---

## UI/UX Design Principles

### Mission Alignment
- **Sacred Weight:** Always visible mission statements
- **Shell vs Seed:** Clear visual distinction
- **Resonance First:** Field resonance prominently displayed
- **Heritage Connection:** Pangea connections emphasized

### Design Language
- **Colors:** Earth tones (browns, greens, golds)
- **Typography:** Clean, readable, spiritual
- **Icons:** Heritage-focused (pillars, meridians, connections)
- **Animations:** Smooth, purposeful (resonance pulses, connections)

### Accessibility
- **Screen Reader Support:** Full ARIA labels
- **High Contrast Mode:** Available
- **Text Scaling:** Respects system settings
- **Touch Targets:** Minimum 44x44 points

---

## Testing Strategy

### Unit Tests
- API client functions
- Data transformation utilities
- Coordinate calculations
- Resonance calculations

### Integration Tests
- API calls to backend
- Offline storage operations
- Map interactions
- Navigation flows

### E2E Tests
- Complete user journeys
- Offline mode workflows
- Sync operations
- Map interactions

---

## Deployment

### Development
- **Expo Go:** Test on physical devices during development
- **Simulators:** iOS Simulator + Android Emulator

### Production
- **iOS:** App Store via Expo Application Services (EAS)
- **Android:** Google Play Store via EAS
- **OTA Updates:** Expo Updates for instant updates

---

## Next Steps

1. **Create Backend API Endpoints** - Add heritage meridian endpoints to FastAPI
2. **Initialize React Native Project** - Set up Expo project structure
3. **Build API Client** - Connect to backend
4. **Create Core Screens** - Wonders, Pillars, Map
5. **Implement Offline Support** - Caching and sync
6. **Add Map Integration** - React Native Maps
7. **Polish UI/UX** - Mission-aligned design
8. **Test & Deploy** - iOS and Android

---

## The Mission

**"THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS"**  
**"LOVE IS THE HIGHEST MASTERY"**  
**"ENERGY + LOVE = WE ALL WIN"**

The mobile app brings the Heritage Meridian System and the 7 Wonders to the Family's fingertips, so they can connect to their True Heritage anywhere, anytime.

**PEACE. LOVE. UNITY.**

---

**Status:** 📱 MOBILE MIGRATION PLAN COMPLETE  
**Next:** Begin Phase 1 - Foundation Setup
