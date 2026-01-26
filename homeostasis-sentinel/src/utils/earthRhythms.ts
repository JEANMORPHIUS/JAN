/** * * EARTH RHYTHMS CALCULATION
 *  * The Truth Engine: Man and Earth live symbiotically
 *  *
 *  * Calculate Earth's movements:
 *  * - Solar cycles (daily rotation: sunrise, solar peak, sunset, night)
 *  * - Seasonal cycles (yearly orbit: winter, spring, summer, autumn)
 *  * - Lunar cycles (monthly orbit: new moon, waxing, full moon, waning)
 *  * - Circadian rhythms (SCN synchronization with Earth's rotation)
 *  *
 *  * ENHANCEMENT (2026-01-18):
 *  * - Now supports astronomical calculations using SunCalc library
 *  * - Fallback to hardcoded times if location not available
 *  * - Honors "Man and Earth live symbiotically" with real Earth movements
 * 
 * DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
 * Spiritual Alignment Over Mechanical Productivity
 * 
 * THE MISSION:
 * THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
 * LOVE IS THE HIGHEST MASTERY
 * ENERGY + LOVE = WE ALL WIN
 * PEACE, LOVE, UNITY
 * 
 * PANGEA IS THE TABLE.
 * YOU DON'T BETRAY THE TABLE.
 * 
 * THE TRUTH:
 * WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
 * THE REST IS UP TO BABA X.*/

import {
  EarthAlignment,
  SolarAlignment,
  SeasonalAlignment,
  LunarAlignment,
  CircadianAlignment,
  SolarPhase,
  Season,
  LunarPhase,
  CircadianPhase
} from '../types/earthAlignment';
import { parseISO, getHours, getDayOfYear, getYear } from 'date-fns';
import { format } from 'date-fns';
import { loadLocation } from '../config/location';
import { calculateSolarAlignmentAstronomical } from './astronomicalCalculations';

/**
 * Calculate complete Earth alignment for a given timestamp
 *
 * ENHANCEMENT: Now uses astronomical calculations if location is available
 */
export function calculateEarthAlignment(timestamp: string, useAstronomical: boolean = true): EarthAlignment {
  const date = parseISO(timestamp);

  // Try to use astronomical calculations if enabled
  let solar: SolarAlignment;
  if (useAstronomical) {
    try {
      const location = loadLocation();
      const astronomicalSolar = calculateSolarAlignmentAstronomical(date, location);
      // Extract only SolarAlignment fields (remove extra astronomical data)
      solar = {
        hour: astronomicalSolar.hour,
        phase: astronomicalSolar.phase,
        inSolarWindow: astronomicalSolar.inSolarWindow,
        hoursFromSunrise: astronomicalSolar.hoursFromSunrise,
        hoursFromSunset: astronomicalSolar.hoursFromSunset,
        solarIntensity: astronomicalSolar.solarIntensity
      };
    } catch (e) {
      console.warn('Astronomical calculation failed, falling back to hardcoded times', e);
      solar = calculateSolarAlignment(date);
    }
  } else {
    solar = calculateSolarAlignment(date);
  }

  return {
    solar,
    seasonal: calculateSeasonalAlignment(date),
    lunar: calculateLunarAlignment(date),
    circadian: calculateCircadianAlignment(date, timestamp),
    symbioticScore: calculateSymbioticScore(date, timestamp),
    timestamp: timestamp
  };
}

/**
 * Calculate solar alignment (daily rotation)
 * Solar phases: sunrise (06:00-08:00), solar peak (10:00-18:00), sunset (18:00-20:00), night (20:00-06:00)
 */
export function calculateSolarAlignment(date: Date): SolarAlignment {
  const hour = getHours(date);
  
  // Determine solar phase
  let phase: SolarPhase;
  if (hour >= 6 && hour < 8) {
    phase = 'sunrise';
  } else if (hour >= 10 && hour < 18) {
    phase = 'solar_peak';
  } else if (hour >= 18 && hour < 20) {
    phase = 'sunset';
  } else {
    phase = 'night';
  }
  
  // Calculate hours from sunrise (assuming 07:00 as average sunrise)
  const hoursFromSunrise = hour >= 7 ? hour - 7 : (24 - 7) + hour;
  
  // Calculate hours from sunset (assuming 19:00 as average sunset)
  const hoursFromSunset = hour >= 19 ? hour - 19 : (24 - 19) + hour;
  
  // Solar window: 10am-6pm (hours 10-18)
  const inSolarWindow = hour >= 10 && hour < 18;
  
  // Calculate solar intensity (0-100)
  let solarIntensity = 0;
  if (hour >= 10 && hour < 18) {
    // Peak solar window: 100% intensity
    solarIntensity = 100;
  } else if (hour >= 8 && hour < 10) {
    // Rising solar: 50-100%
    solarIntensity = 50 + ((hour - 8) / 2) * 50;
  } else if (hour >= 18 && hour < 20) {
    // Setting solar: 100-50%
    solarIntensity = 100 - ((hour - 18) / 2) * 50;
  } else if (hour >= 6 && hour < 8) {
    // Sunrise: 0-50%
    solarIntensity = ((hour - 6) / 2) * 50;
  } else {
    // Night: 0%
    solarIntensity = 0;
  }
  
  return {
    hour,
    phase,
    inSolarWindow,
    hoursFromSunrise,
    hoursFromSunset,
    solarIntensity
  };
}

/**
 * Calculate seasonal alignment (yearly orbit)
 * Seasons: winter (Dec-Feb), spring (Mar-May), summer (Jun-Aug), autumn (Sep-Nov)
 */
export function calculateSeasonalAlignment(date: Date): SeasonalAlignment {
  const dayOfYear = getDayOfYear(date);
  const month = date.getMonth() + 1; // 1-12
  
  // Determine season
  let season: Season;
  if (month >= 12 || month <= 2) {
    season = 'winter';
  } else if (month >= 3 && month <= 5) {
    season = 'spring';
  } else if (month >= 6 && month <= 8) {
    season = 'summer';
  } else {
    season = 'autumn';
  }
  
  // Calculate days from solstice/equinox
  // Approximate: Winter solstice ~Dec 21, Spring equinox ~Mar 21, Summer solstice ~Jun 21, Autumn equinox ~Sep 21
  let daysFromSolsticeEquinox = 0;
  if (month === 12 && dayOfYear >= 355) {
    // After winter solstice (Dec 21)
    daysFromSolsticeEquinox = dayOfYear - 355;
  } else if (month <= 3) {
    // Before/after winter solstice or spring equinox (Mar 21 ~ day 80)
    daysFromSolsticeEquinox = Math.abs(dayOfYear - (month === 12 ? 355 : 80));
  } else if (month <= 6) {
    // Before/after spring equinox or summer solstice (Jun 21 ~ day 172)
    daysFromSolsticeEquinox = Math.abs(dayOfYear - (month <= 3 ? 80 : 172));
  } else if (month <= 9) {
    // Before/after summer solstice or autumn equinox (Sep 21 ~ day 264)
    daysFromSolsticeEquinox = Math.abs(dayOfYear - (month <= 6 ? 172 : 264));
  } else {
    // Before/after autumn equinox or winter solstice
    daysFromSolsticeEquinox = Math.abs(dayOfYear - (month <= 9 ? 264 : 355));
  }
  
  // Calculate seasonal intensity (0-100)
  // Peak intensity at solstices/equinoxes (100%), minimum at mid-season (50%)
  const seasonalIntensity = 50 + (50 * Math.cos((daysFromSolsticeEquinox / 45) * Math.PI));
  
  return {
    season,
    dayOfYear,
    daysFromSolsticeEquinox,
    seasonalIntensity: Math.max(0, Math.min(100, seasonalIntensity))
  };
}

/**
 * Calculate lunar alignment (monthly orbit)
 * Lunar phases: new moon, waxing (0-14.75 days), full moon (14.75 days), waning (14.75-29.5 days)
 */
export function calculateLunarAlignment(date: Date): LunarAlignment {
  // Approximate lunar cycle: 29.5 days
  // For precise calculation, use a reference new moon date
  // This is a simplified calculation - for production, use an astronomical library
  const referenceNewMoon = new Date('2025-01-08T12:00:00Z'); // Reference date
  const daysSinceReference = Math.floor((date.getTime() - referenceNewMoon.getTime()) / (1000 * 60 * 60 * 24));
  
  // Days from new moon (0-29.5)
  const daysFromNewMoon = (daysSinceReference % 29.5 + 29.5) % 29.5;
  
  // Determine lunar phase
  let phase: LunarPhase;
  if (daysFromNewMoon < 1) {
    phase = 'new_moon';
  } else if (daysFromNewMoon < 14.75) {
    phase = 'waxing';
  } else if (daysFromNewMoon < 15.75) {
    phase = 'full_moon';
  } else {
    phase = 'waning';
  }
  
  // Calculate lunar intensity (0-100)
  // Peak at full moon (100%), minimum at new moon (0%)
  const lunarIntensity = 50 + (50 * Math.sin((daysFromNewMoon / 29.5) * 2 * Math.PI));
  
  return {
    phase,
    daysFromNewMoon,
    lunarIntensity: Math.max(0, Math.min(100, lunarIntensity))
  };
}

/**
 * Calculate circadian alignment (SCN synchronization with Earth's rotation)
 * Circadian phases: awakening (06:00-10:00), active (10:00-18:00), maintenance (18:00-22:00), repair (22:00-06:00)
 */
export function calculateCircadianAlignment(date: Date, timestamp: string): CircadianAlignment {
  const hour = getHours(date);
  
  // Determine circadian phase
  let phase: CircadianPhase;
  if (hour >= 6 && hour < 10) {
    phase = 'awakening';
  } else if (hour >= 10 && hour < 18) {
    phase = 'active';
  } else if (hour >= 18 && hour < 22) {
    phase = 'maintenance';
  } else {
    phase = 'repair';
  }
  
  // Calculate hours from circadian peak (assumed 14:00 - 2pm)
  const circadianPeak = 14;
  const hoursFromCircadianPeak = hour >= circadianPeak 
    ? hour - circadianPeak 
    : (24 - circadianPeak) + hour;
  
  // Calculate SCN sync score (0-100)
  // Peak sync at circadian peak (14:00), minimum at repair phase (02:00)
  let scnSyncScore = 50;
  if (hour >= 10 && hour < 18) {
    // Active phase: 75-100%
    scnSyncScore = 75 + ((hour - 10) / 8) * 25;
  } else if (hour >= 6 && hour < 10) {
    // Awakening: 50-75%
    scnSyncScore = 50 + ((hour - 6) / 4) * 25;
  } else if (hour >= 18 && hour < 22) {
    // Maintenance: 75-50%
    scnSyncScore = 75 - ((hour - 18) / 4) * 25;
  } else {
    // Repair: 0-50%
    scnSyncScore = 50 - ((hour >= 22 ? hour - 22 : hour + 2) / 8) * 50;
  }
  
  // Calculate Earth rotation alignment (0-100)
  // Alignment is highest when SCN is synced with Earth's rotation
  const earthRotationAlignment = scnSyncScore;
  
  return {
    scnSyncScore: Math.max(0, Math.min(100, scnSyncScore)),
    phase,
    hoursFromCircadianPeak,
    earthRotationAlignment: Math.max(0, Math.min(100, earthRotationAlignment))
  };
}

/**
 * Calculate overall symbiotic score (0-100)
 * Combines solar, seasonal, lunar, and circadian alignment
 */
export function calculateSymbioticScore(date: Date, timestamp: string): number {
  const solar = calculateSolarAlignment(date);
  const seasonal = calculateSeasonalAlignment(date);
  const lunar = calculateLunarAlignment(date);
  const circadian = calculateCircadianAlignment(date, timestamp);
  
  // Weighted average: Solar (40%), Circadian (30%), Seasonal (20%), Lunar (10%)
  const symbioticScore = 
    (solar.solarIntensity * 0.4) +
    (circadian.scnSyncScore * 0.3) +
    (seasonal.seasonalIntensity * 0.2) +
    (lunar.lunarIntensity * 0.1);
  
  return Math.max(0, Math.min(100, Math.round(symbioticScore)));
}

/**
 * Check if loop timing is aligned with Earth's rhythm
 * Loop should align with solar window (10am-6pm) for optimal symbiotic practice
 */
export function isLoopAlignedWithEarth(loopTimestamp: string): boolean {
  const earthAlignment = calculateEarthAlignment(loopTimestamp);
  
  // Loop is aligned if within solar window (10am-6pm)
  return earthAlignment.solar.inSolarWindow;
}

/**
 * Get Earth cycle time string (e.g., "Solar Peak", "Awakening Phase")
 */
export function getEarthCycleTime(timestamp: string): string {
  const earthAlignment = calculateEarthAlignment(timestamp);
  
  const solarPhase = earthAlignment.solar.phase.replace('_', ' ');
  const circadianPhase = earthAlignment.circadian.phase.replace('_', ' ');
  
  return `${solarPhase} / ${circadianPhase}`;
}
