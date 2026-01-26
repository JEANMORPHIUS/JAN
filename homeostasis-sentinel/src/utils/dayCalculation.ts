/** * * DAY CALCULATION UTILITIES
 *  * Calculate current day based on first glucose reading date
 *  * 
 *  * Day 1 = Date of first glucose reading (not today)
 *  * Current Day = Days since first reading + 1
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

import { HealthMetrics } from '../types';
import { parseISO, differenceInDays, format } from 'date-fns';

/**
 * Find the earliest glucose reading date from metrics
 * This becomes Day 1 of the 376-day journey
 */
export function findFirstGlucoseReadingDate(
  metrics: HealthMetrics[]
): string | null {
  const glucoseReadings = metrics.filter(m => 
    m.blood_glucose !== undefined && m.date !== undefined
  );

  if (glucoseReadings.length === 0) {
    return null;
  }

  // Sort by date to find earliest
  const sortedReadings = glucoseReadings.sort((a, b) => {
    const dateA = parseISO(a.date);
    const dateB = parseISO(b.date);
    return dateA.getTime() - dateB.getTime();
  });

  const earliestReading = sortedReadings[0];
  const readingTime = earliestReading.glucose_time 
    ? `${earliestReading.date}T${earliestReading.glucose_time}:00`
    : `${earliestReading.date}T12:00:00`;

  return parseISO(readingTime).toISOString();
}

/**
 * Calculate current day based on first reading date
 * Day 1 = Date of first glucose reading
 * Current Day = Days since first reading + 1
 */
export function calculateCurrentDay(
  firstReadingTimestamp: string,
  currentTimestamp: string = new Date().toISOString(),
  totalDays: number = 376
): number {
  const firstDate = parseISO(firstReadingTimestamp);
  const currentDate = parseISO(currentTimestamp);
  
  const daysSinceDay1 = differenceInDays(currentDate, firstDate);
  const currentDay = Math.max(1, Math.min(daysSinceDay1 + 1, totalDays));
  
  return currentDay;
}

/**
 * Calculate Day 1 timestamp from metrics
 * Uses the earliest glucose reading as Day 1
 */
export function calculateDay1FromMetrics(
  metrics: HealthMetrics[]
): {
  day1Timestamp: string;
  currentDay: number;
  firstReading: HealthMetrics | null;
} {
  const firstReadingTimestamp = findFirstGlucoseReadingDate(metrics);
  
  if (!firstReadingTimestamp) {
    // Fallback to today if no readings found
    const today = new Date();
    today.setHours(0, 0, 0, 0);
    return {
      day1Timestamp: today.toISOString(),
      currentDay: 1,
      firstReading: null
    };
  }

  const currentDay = calculateCurrentDay(firstReadingTimestamp);
  
  const firstReading = metrics
    .filter(m => m.blood_glucose !== undefined && m.date !== undefined)
    .sort((a, b) => {
      const dateA = parseISO(a.date);
      const dateB = parseISO(b.date);
      return dateA.getTime() - dateB.getTime();
    })[0] || null;

  return {
    day1Timestamp: firstReadingTimestamp,
    currentDay,
    firstReading
  };
}

/**
 * Get formatted date string for a specific day
 */
export function getDayDate(day1Timestamp: string, day: number): string {
  const day1Date = parseISO(day1Timestamp);
  const targetDate = new Date(day1Date);
  targetDate.setDate(day1Date.getDate() + (day - 1));
  return format(targetDate, 'yyyy-MM-dd');
}
