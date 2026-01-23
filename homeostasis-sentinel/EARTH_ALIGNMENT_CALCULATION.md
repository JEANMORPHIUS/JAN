# Earth Alignment Calculation Methodology

**Purpose:** Document how Homeostasis Sentinel calculates Earth cycles for Loop timing alignment

**Foundation:** "Man and Earth live symbiotically" - Loop timing must align with Earth's movements

---

## Current Implementation Status

### ✅ Implemented (Hardcoded Times)

**Solar Cycles:**
- Sunrise: 06:00-08:00 (hardcoded, assumes 07:00 average)
- Solar Peak: 10:00-18:00 (hardcoded)
- Sunset: 18:00-20:00 (hardcoded, assumes 19:00 average)
- Night: 20:00-06:00 (hardcoded)

**Seasonal Cycles:**
- Winter: December-February
- Spring: March-May
- Summer: June-August
- Autumn: September-November
- Seasonal intensity calculated using day of year

**Lunar Cycles:**
- Simplified calculation using 29.5-day cycle
- Known reference: January 6, 2000 (new moon)
- Phases: New Moon, Waxing, Full Moon, Waning

**Circadian Rhythms:**
- Awakening: 06:00-10:00 (cortisol peak)
- Active: 10:00-18:00 (peak performance)
- Winding Down: 18:00-22:00 (transition)
- Deep Rest: 22:00-06:00 (melatonin peak)

---

## ⚠️ Current Limitation

**Problem:** Solar calculations use hardcoded times that don't account for:
1. Geographic location (latitude/longitude)
2. Seasonal variations (winter vs. summer sunrise/sunset times)
3. Actual astronomical calculations

**Impact:**
- Loop window recommendations may be inaccurate
- Seasonal adjustments documented (Winter: 08:00-16:00, Summer: 06:00-20:00) are NOT automated
- User must manually adjust for location and season

**Risk:** Medium
- System functional but not optimally aligned with actual Earth movements
- User in London (51.5°N) has different sunrise/sunset than Cyprus (35°N)
- December sunrise in London (~08:00) vs. hardcoded 07:00 causes misalignment

---

## 🔧 Recommended Enhancement: Astronomical Calculation

### Implementation Approach

**Option 1: SunCalc Library (Recommended)**
```typescript
import SunCalc from 'suncalc';

interface LocationConfig {
  latitude: number;
  longitude: number;
  timezone: string;
}

// User configuration (can be set in app settings)
const DEFAULT_LOCATION: LocationConfig = {
  latitude: 51.5074,  // London
  longitude: -0.1278,
  timezone: 'Europe/London'
};

export function calculateSolarAlignmentAstronomical(
  date: Date,
  location: LocationConfig = DEFAULT_LOCATION
): SolarAlignment {
  // Get actual sunrise/sunset times for this location and date
  const times = SunCalc.getTimes(date, location.latitude, location.longitude);

  const sunrise = times.sunrise;
  const sunset = times.sunset;
  const solarNoon = times.solarNoon;

  const currentHour = date.getHours();
  const sunriseHour = sunrise.getHours();
  const sunsetHour = sunset.getHours();

  // Determine phase based on actual times
  let phase: SolarPhase;
  if (currentHour >= sunriseHour - 1 && currentHour < sunriseHour + 1) {
    phase = 'sunrise';
  } else if (currentHour >= sunriseHour + 3 && currentHour < sunsetHour - 2) {
    phase = 'solar_peak';
  } else if (currentHour >= sunsetHour - 1 && currentHour < sunsetHour + 1) {
    phase = 'sunset';
  } else {
    phase = 'night';
  }

  // Calculate solar window based on actual sunrise/sunset
  // Primary window: 3 hours after sunrise to 2 hours before sunset
  const solarWindowStart = sunriseHour + 3;
  const solarWindowEnd = sunsetHour - 2;
  const inSolarWindow = currentHour >= solarWindowStart && currentHour < solarWindowEnd;

  // Hours from actual sunrise/sunset
  const hoursFromSunrise = currentHour >= sunriseHour
    ? currentHour - sunriseHour
    : (24 - sunriseHour) + currentHour;

  const hoursFromSunset = currentHour >= sunsetHour
    ? currentHour - sunsetHour
    : (24 - sunsetHour) + currentHour;

  // Calculate solar altitude for intensity
  const position = SunCalc.getPosition(date, location.latitude, location.longitude);
  const altitudeDegrees = position.altitude * (180 / Math.PI);

  // Solar intensity based on altitude (0° = 0%, 90° = 100%)
  const solarIntensity = Math.max(0, Math.min(100, (altitudeDegrees / 90) * 100));

  return {
    hour: currentHour,
    phase,
    inSolarWindow,
    hoursFromSunrise,
    hoursFromSunset,
    solarIntensity,
    // Additional data for user reference
    actualSunrise: sunrise.toISOString(),
    actualSunset: sunset.toISOString(),
    solarWindowStart,
    solarWindowEnd,
    location
  };
}
```

**Installation:**
```bash
cd S:\JAN\homeostasis-sentinel
npm install suncalc
npm install --save-dev @types/suncalc
```

---

### User Configuration

**Add location settings to app:**

```typescript
// src/config/location.ts
export interface LocationConfig {
  name: string;
  latitude: number;
  longitude: number;
  timezone: string;
}

export const PRESET_LOCATIONS: Record<string, LocationConfig> = {
  london: {
    name: 'London, UK',
    latitude: 51.5074,
    longitude: -0.1278,
    timezone: 'Europe/London'
  },
  northCyprus: {
    name: 'North Cyprus',
    latitude: 35.1856,
    longitude: 33.3823,
    timezone: 'Asia/Nicosia'
  },
  cyprus: {
    name: 'Cyprus',
    latitude: 35.1264,
    longitude: 33.4299,
    timezone: 'Asia/Nicosia'
  }
};

export const DEFAULT_LOCATION = PRESET_LOCATIONS.london;
```

**Add settings UI:**
```typescript
// src/components/LocationSettings.tsx
import { useState } from 'react';
import { PRESET_LOCATIONS, DEFAULT_LOCATION, LocationConfig } from '../config/location';

export function LocationSettings({
  onLocationChange
}: {
  onLocationChange: (location: LocationConfig) => void
}) {
  const [location, setLocation] = useState(DEFAULT_LOCATION);

  return (
    <div className="location-settings">
      <h3>Location Settings</h3>
      <p>For accurate sunrise/sunset times</p>

      <select
        value={location.name}
        onChange={(e) => {
          const newLocation = Object.values(PRESET_LOCATIONS)
            .find(loc => loc.name === e.target.value);
          if (newLocation) {
            setLocation(newLocation);
            onLocationChange(newLocation);
          }
        }}
      >
        {Object.values(PRESET_LOCATIONS).map(loc => (
          <option key={loc.name} value={loc.name}>
            {loc.name}
          </option>
        ))}
      </select>

      <div className="location-details">
        <p>Latitude: {location.latitude}</p>
        <p>Longitude: {location.longitude}</p>
        <p>Timezone: {location.timezone}</p>
      </div>
    </div>
  );
}
```

---

## 🎯 Benefits of Astronomical Calculation

1. **Accuracy:** Real sunrise/sunset times for user's location
2. **Seasonal Adjustment:** Automatically adjusts for winter/summer variations
3. **Geographic Accuracy:** London users get London times, Cyprus users get Cyprus times
4. **Solar Intensity:** Based on actual sun altitude, not just time of day
5. **Narrative Alignment:** "Man and Earth live symbiotically" - system truly syncs with Earth

---

## 📋 Implementation Checklist

- [ ] Install `suncalc` library
- [ ] Create `src/config/location.ts` with preset locations
- [ ] Create `src/components/LocationSettings.tsx` for user configuration
- [ ] Update `src/utils/earthRhythms.ts` with astronomical calculations
- [ ] Add location persistence (localStorage)
- [ ] Test accuracy across seasons (winter vs. summer)
- [ ] Test accuracy across locations (London vs. Cyprus)
- [ ] Update UI to show actual sunrise/sunset times
- [ ] Document calculation methodology for users

---

## 🔄 Migration Strategy

**Phase 1: Add alongside existing (feature flag)**
- Keep current hardcoded calculations
- Add new astronomical calculations
- Allow users to toggle between "simple" and "astronomical"

**Phase 2: Make astronomical default**
- Default to astronomical calculations
- Keep simple as fallback if location not set

**Phase 3: Remove simple calculations**
- Once validated, remove hardcoded times
- Require location setting on first use

---

## 📊 Validation

**Test cases:**

1. **London, December 21 (Winter Solstice):**
   - Actual sunrise: ~08:03
   - Actual sunset: ~15:53
   - Expected solar window: ~11:00-14:00

2. **London, June 21 (Summer Solstice):**
   - Actual sunrise: ~04:43
   - Actual sunset: ~21:21
   - Expected solar window: ~07:45-19:20

3. **Cyprus, December 21:**
   - Actual sunrise: ~06:44
   - Actual sunset: ~17:00
   - Expected solar window: ~09:45-15:00

4. **Cyprus, June 21:**
   - Actual sunrise: ~05:36
   - Actual sunset: ~19:58
   - Expected solar window: ~08:35-18:00

**Success Criteria:**
- ✅ Solar window recommendations match actual Earth movements
- ✅ Seasonal variations automatically handled
- ✅ Geographic variations automatically handled
- ✅ User sees actual sunrise/sunset times in UI

---

## 🌍 Symbiotic Truth Honored

**Before Enhancement:** System **claims** to align with Earth but uses approximate times

**After Enhancement:** System **actually** aligns with Earth's movements for user's location and season

**Narrative Integrity:** "Man and Earth live symbiotically" becomes **operational reality**, not aspirational statement

---

**Status:** Enhancement recommended, not critical blocker
**Priority:** Medium (system functional, enhancement improves accuracy)
**Effort:** 4-6 hours implementation + 2 hours testing
**Impact:** High (narrative alignment, user accuracy, seasonal/geographic correctness)

---

**Last Updated:** 2026-01-18
**Maintainer:** Homeostasis Sentinel Development Team
