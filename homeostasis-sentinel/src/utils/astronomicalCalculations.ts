/**
 * ASTRONOMICAL CALCULATIONS
 *
 * Purpose: Calculate actual Earth movements using astronomical data
 * Foundation: "Man and Earth live symbiotically" - honor real Earth cycles
 *
 * Uses SunCalc library for accurate sunrise/sunset calculations based on:
 * - User's geographic location (latitude/longitude)
 * - Current date (seasonal variations)
 * - Astronomical algorithms (not hardcoded times)
 */

import SunCalc from 'suncalc';
import { getHours } from 'date-fns';
import { LocationConfig } from '../config/location';
import { SolarAlignment, SolarPhase } from '../types/earthAlignment';

/**
 * Calculate solar alignment using real astronomical data
 *
 * This replaces hardcoded sunrise/sunset times with actual calculations
 * based on user's location and current date.
 */
export function calculateSolarAlignmentAstronomical(
  date: Date,
  location: LocationConfig
): SolarAlignment & {
  actualSunrise: string;
  actualSunset: string;
  solarWindowStart: number;
  solarWindowEnd: number;
  location: LocationConfig;
} {
  // Get actual astronomical times for this location and date
  const times = SunCalc.getTimes(date, location.latitude, location.longitude);

  const sunrise = times.sunrise;
  const sunset = times.sunset;

  const currentHour = getHours(date);
  const currentMinutes = date.getMinutes();
  const currentTimeDecimal = currentHour + (currentMinutes / 60);

  const sunriseHour = sunrise.getHours();
  const sunriseMinutes = sunrise.getMinutes();
  const sunriseDecimal = sunriseHour + (sunriseMinutes / 60);

  const sunsetHour = sunset.getHours();
  const sunsetMinutes = sunset.getMinutes();
  const sunsetDecimal = sunsetHour + (sunsetMinutes / 60);

  // Determine phase based on actual astronomical times
  let phase: SolarPhase;
  const sunriseStart = sunriseDecimal - 1;
  const sunriseEnd = sunriseDecimal + 1;
  const sunsetStart = sunsetDecimal - 1;
  const sunsetEnd = sunsetDecimal + 1;

  if (currentTimeDecimal >= sunriseStart && currentTimeDecimal < sunriseEnd) {
    phase = 'sunrise';
  } else if (currentTimeDecimal >= sunriseEnd && currentTimeDecimal < sunsetStart) {
    phase = 'solar_peak';
  } else if (currentTimeDecimal >= sunsetStart && currentTimeDecimal < sunsetEnd) {
    phase = 'sunset';
  } else {
    phase = 'night';
  }

  // Calculate optimal solar window
  // Primary window: 3 hours after sunrise to 2 hours before sunset
  // This ensures cortisol has peaked and before melatonin starts rising
  const solarWindowStart = Math.ceil(sunriseDecimal + 3);
  const solarWindowEnd = Math.floor(sunsetDecimal - 2);

  // Adjust for edge cases (very short winter days, very long summer days)
  const adjustedWindowStart = Math.max(8, Math.min(12, solarWindowStart));
  const adjustedWindowEnd = Math.max(16, Math.min(20, solarWindowEnd));

  const inSolarWindow = currentHour >= adjustedWindowStart && currentHour < adjustedWindowEnd;

  // Calculate hours from actual sunrise
  let hoursFromSunrise: number;
  if (currentTimeDecimal >= sunriseDecimal) {
    hoursFromSunrise = currentTimeDecimal - sunriseDecimal;
  } else {
    // Before sunrise (night time)
    hoursFromSunrise = (24 - sunriseDecimal) + currentTimeDecimal;
  }

  // Calculate hours from actual sunset
  let hoursFromSunset: number;
  if (currentTimeDecimal >= sunsetDecimal) {
    hoursFromSunset = currentTimeDecimal - sunsetDecimal;
  } else {
    // Before sunset (day time)
    hoursFromSunset = (24 - sunsetDecimal) + currentTimeDecimal;
  }

  // Calculate solar intensity based on actual sun position (altitude)
  const position = SunCalc.getPosition(date, location.latitude, location.longitude);
  const altitudeDegrees = position.altitude * (180 / Math.PI);

  // Solar intensity based on altitude
  // Sun at zenith (90°) = 100% intensity
  // Sun at horizon (0°) = 0% intensity
  // Sun below horizon (negative) = 0% intensity
  let solarIntensity = Math.max(0, Math.min(100, (altitudeDegrees / 90) * 100));

  // Alternative calculation during solar window: ensure high intensity
  if (inSolarWindow && solarIntensity < 70) {
    // During solar window, intensity should be at least 70%
    // This handles cases where altitude calculation may be lower than expected
    const windowProgress = (currentHour - adjustedWindowStart) / (adjustedWindowEnd - adjustedWindowStart);
    solarIntensity = 70 + (30 * Math.sin(windowProgress * Math.PI));
  }

  return {
    hour: currentHour,
    phase,
    inSolarWindow,
    hoursFromSunrise,
    hoursFromSunset,
    solarIntensity,
    // Additional astronomical data
    actualSunrise: sunrise.toISOString(),
    actualSunset: sunset.toISOString(),
    solarWindowStart: adjustedWindowStart,
    solarWindowEnd: adjustedWindowEnd,
    location
  };
}

/**
 * Get human-readable sunrise time (HH:MM format)
 */
export function formatSunriseTime(date: Date, location: LocationConfig): string {
  const times = SunCalc.getTimes(date, location.latitude, location.longitude);
  const sunrise = times.sunrise;
  return `${sunrise.getHours().toString().padStart(2, '0')}:${sunrise.getMinutes().toString().padStart(2, '0')}`;
}

/**
 * Get human-readable sunset time (HH:MM format)
 */
export function formatSunsetTime(date: Date, location: LocationConfig): string {
  const times = SunCalc.getTimes(date, location.latitude, location.longitude);
  const sunset = times.sunset;
  return `${sunset.getHours().toString().padStart(2, '0')}:${sunset.getMinutes().toString().padStart(2, '0')}`;
}

/**
 * Get human-readable solar window (HH:MM - HH:MM format)
 */
export function formatSolarWindow(date: Date, location: LocationConfig): string {
  const alignment = calculateSolarAlignmentAstronomical(date, location);
  return `${alignment.solarWindowStart.toString().padStart(2, '0')}:00 - ${alignment.solarWindowEnd.toString().padStart(2, '0')}:00`;
}

/**
 * Calculate day length (hours)
 */
export function calculateDayLength(date: Date, location: LocationConfig): number {
  const times = SunCalc.getTimes(date, location.latitude, location.longitude);
  const dayLengthMs = times.sunset.getTime() - times.sunrise.getTime();
  return dayLengthMs / (1000 * 60 * 60); // Convert to hours
}

/**
 * Get seasonal context string
 */
export function getSeasonalContext(date: Date, location: LocationConfig): string {
  const dayLength = calculateDayLength(date, location);

  if (dayLength < 9) {
    return 'Deep Winter (short days, compressed solar window)';
  } else if (dayLength < 11) {
    return 'Winter (shorter days, earlier solar window)';
  } else if (dayLength < 13) {
    return 'Spring/Autumn (balanced days, standard solar window)';
  } else if (dayLength < 15) {
    return 'Summer (longer days, extended solar window)';
  } else {
    return 'Peak Summer (very long days, maximum solar window)';
  }
}

/**
 * Validate if Loop timing aligns with Earth movements
 *
 * Returns true if Loop occurred during solar window
 */
export function validateLoopEarthAlignment(
  loopTimestamp: string,
  location: LocationConfig
): {
  aligned: boolean;
  reason: string;
  recommendation?: string;
} {
  const date = new Date(loopTimestamp);
  const alignment = calculateSolarAlignmentAstronomical(date, location);

  if (alignment.inSolarWindow) {
    return {
      aligned: true,
      reason: `Loop at ${date.getHours()}:${date.getMinutes().toString().padStart(2, '0')} is within solar window (${alignment.solarWindowStart}:00-${alignment.solarWindowEnd}:00)`
    };
  }

  // Not aligned - provide recommendation
  const sunrise = formatSunriseTime(date, location);
  const sunset = formatSunsetTime(date, location);
  const solarWindow = formatSolarWindow(date, location);

  return {
    aligned: false,
    reason: `Loop at ${date.getHours()}:${date.getMinutes().toString().padStart(2, '0')} is outside solar window (${alignment.solarWindowStart}:00-${alignment.solarWindowEnd}:00)`,
    recommendation: `Today's sunrise: ${sunrise}, sunset: ${sunset}. Optimal Loop window: ${solarWindow}`
  };
}
