/**
 * STEWARDSHIP BRIEFING AUTOMATION UTILITIES
 * Generate weekly 'Truth Report' for the Command Center
 */

import {
  WeeklyDataAggregation,
  GlucoseStatistics,
  CommunityStewardshipScores,
  EarthPhaseForecast,
  DailyEarthPhase,
  NarrativeGeneration,
  Narrative,
  ThresholdDefenseState,
  FlaggedRedTapeEvent,
  WeeklyTruthReport
} from '../types/stewardshipBriefing';
import { HealthMetrics } from '../types';
import { ExternalSystemFailure } from '../types/pierreLogic';
import { EarthAlignment } from '../types/earthAlignment';
import { calculateEarthAlignment } from './earthRhythms';
import { addDays, format, startOfWeek, endOfWeek, parseISO } from 'date-fns';

/**
 * Aggregate Weekly Glucose Statistics
 * Collect weekly `mmol_l` mean and variance
 */
export function aggregateWeeklyGlucose(
  metrics: HealthMetrics[],
  weekStartDate: Date
): GlucoseStatistics {
  // Filter metrics for the week
  const weekEndDate = addDays(weekStartDate, 7);
  const weekMetrics = metrics.filter(m => {
    const metricDate = parseISO(m.date);
    return metricDate >= weekStartDate && metricDate < weekEndDate;
  });

  // Convert glucose to mmol/L (if in mg/dL)
  const glucoseValues = weekMetrics
    .map(m => {
      if (!m.blood_glucose) return null;
      // Assume mg/dL, convert to mmol/L
      return m.blood_glucose / 18.0182;
    })
    .filter((g): g is number => g !== null);

  if (glucoseValues.length === 0) {
    return {
      mean: 0,
      variance: 0,
      standardDeviation: 0,
      min: 0,
      max: 0,
      count: 0,
      varianceLevel: 'Low'
    };
  }

  // Calculate statistics
  const mean = glucoseValues.reduce((sum, val) => sum + val, 0) / glucoseValues.length;
  const variance = glucoseValues.reduce((sum, val) => sum + Math.pow(val - mean, 2), 0) / glucoseValues.length;
  const standardDeviation = Math.sqrt(variance);
  const min = Math.min(...glucoseValues);
  const max = Math.max(...glucoseValues);

  // Classify variance level
  let varianceLevel: 'Low' | 'Medium' | 'High';
  if (variance < 10) {
    varianceLevel = 'Low';
  } else if (variance < 25) {
    varianceLevel = 'Medium';
  } else {
    varianceLevel = 'High';
  }

  return {
    mean: Math.round(mean * 100) / 100,
    variance: Math.round(variance * 100) / 100,
    standardDeviation: Math.round(standardDeviation * 100) / 100,
    min: Math.round(min * 100) / 100,
    max: Math.round(max * 100) / 100,
    count: glucoseValues.length,
    varianceLevel
  };
}

/**
 * Aggregate Community Stewardship Scores
 * Aggregate `stewardship_scores` from all active community partners
 */
export function aggregateCommunityStewardship(
  stewardshipScoresByPartner: Record<string, { stewardshipScore: number; isActive: boolean }>
): CommunityStewardshipScores {
  const scoresByPartner: Record<string, { partnerName: string; stewardshipScore: number; isActive: boolean }> = {};
  
  let totalScore = 0;
  let activePartnersCount = 0;

  Object.entries(stewardshipScoresByPartner).forEach(([partnerName, data]) => {
    scoresByPartner[partnerName] = {
      partnerName,
      stewardshipScore: data.stewardshipScore,
      isActive: data.isActive
    };

    if (data.isActive) {
      totalScore += data.stewardshipScore;
      activePartnersCount++;
    }
  });

  const averageStewardship = activePartnersCount > 0 
    ? totalScore / activePartnersCount 
    : 0;

  // Classify stewardship level
  let classification: 'Optimal' | 'Stable' | 'Warning' | 'Critical';
  if (averageStewardship >= 0.8) {
    classification = 'Optimal';
  } else if (averageStewardship >= 0.7) {
    classification = 'Stable';
  } else if (averageStewardship >= 0.5) {
    classification = 'Warning';
  } else {
    classification = 'Critical';
  }

  return {
    averageStewardship: Math.round(averageStewardship * 1000) / 1000,
    scoresByPartner,
    activePartnersCount,
    classification
  };
}

/**
 * Forecast Earth Phases
 * Pull Lunar/Solar phase data for the upcoming 7 days
 */
export function forecastEarthPhases(
  startDate: Date
): EarthPhaseForecast {
  const dailyPhases: DailyEarthPhase[] = [];
  const endDate = addDays(startDate, 7);

  for (let i = 0; i < 7; i++) {
    const date = addDays(startDate, i);
    const timestamp = format(date, 'yyyy-MM-dd') + 'T12:00:00';
    const earthAlignment = calculateEarthAlignment(timestamp);

    dailyPhases.push({
      date: format(date, 'yyyy-MM-dd'),
      solarPhase: earthAlignment.solar.phase,
      lunarPhase: earthAlignment.lunar.phase,
      solarIntensity: Math.round(earthAlignment.solar.solarIntensity),
      lunarIntensity: Math.round(earthAlignment.lunar.lunarIntensity),
      symbioticScore: Math.round(earthAlignment.symbioticScore)
    });
  }

  return {
    period: {
      startDate: format(startDate, 'yyyy-MM-dd'),
      endDate: format(endDate, 'yyyy-MM-dd')
    },
    dailyPhases
  };
}

/**
 * Generate Narrative
 * Logic: IF (avg_stewardship < 0.7) THEN Append(Ramiz_Voice: "The quiet is being ignored. Return to the soil.")
 * Logic: IF (glucose_variance > High) THEN Append(Karasahin_Voice: "The rhythm is broken. Defend the table.")
 */
export function generateNarrative(
  averageStewardship: number,
  glucoseVarianceLevel: 'Low' | 'Medium' | 'High'
): NarrativeGeneration {
  const narratives: Narrative[] = [];
  const conditionsMet: string[] = [];

  // IF (avg_stewardship < 0.7) THEN Ramiz_Voice
  if (averageStewardship < 0.7) {
    narratives.push({
      id: `narrative_ramiz_${Date.now()}`,
      entityVoice: 'Ramiz',
      condition: 'avg_stewardship < 0.7',
      message: 'The quiet is being ignored. Return to the soil.',
      lawReference: 'Law 11: Wisdom Lives in the Quiet',
      priority: averageStewardship < 0.5 ? 'critical' : 'warning'
    });
    conditionsMet.push('avg_stewardship < 0.7');
  }

  // IF (glucose_variance > High) THEN Karasahin_Voice
  if (glucoseVarianceLevel === 'High') {
    narratives.push({
      id: `narrative_karasahin_${Date.now()}`,
      entityVoice: 'Karasahin',
      condition: 'glucose_variance > High',
      message: 'The rhythm is broken. Defend the table.',
      lawReference: 'Law 1: The Table Never Lies',
      priority: 'critical'
    });
    conditionsMet.push('glucose_variance > High');
  }

  return {
    narratives,
    conditionsMet
  };
}

/**
 * Calculate Threshold Defense State
 * Flag any 'Red Tape' event that occurred more than 3 times
 * Output: `system_correction_required = true;`
 */
export function calculateThresholdDefenseForRedTape(
  redTapeEvents: ExternalSystemFailure[],
  threshold: number = 3
): ThresholdDefenseState {
  // Count occurrences by failure type
  const eventCounts = new Map<string, number>();
  const firstOccurrences = new Map<string, string>();
  const latestOccurrences = new Map<string, string>();

  redTapeEvents.forEach(event => {
    const key = event.failureType;
    eventCounts.set(key, (eventCounts.get(key) || 0) + 1);
    
    if (!firstOccurrences.has(key)) {
      firstOccurrences.set(key, event.timestamp);
    }
    latestOccurrences.set(key, event.timestamp);
  });

  // Flag events exceeding threshold
  const flaggedRedTapeEvents: FlaggedRedTapeEvent[] = [];
  let eventsExceedingThreshold = 0;

  eventCounts.forEach((count, failureType) => {
    const isFlagged = count > threshold;
    if (isFlagged) {
      eventsExceedingThreshold++;
    }

    flaggedRedTapeEvents.push({
      failureType: failureType as 'api_downtime' | 'sensor_failure' | 'system_latency' | 'other',
      occurrenceCount: count,
      threshold,
      isFlagged,
      firstOccurrence: firstOccurrences.get(failureType) || '',
      latestOccurrence: latestOccurrences.get(failureType) || ''
    });
  });

  const system_correction_required = eventsExceedingThreshold > 0;

  return {
    system_correction_required,
    flaggedRedTapeEvents,
    totalRedTapeEvents: redTapeEvents.length,
    eventsExceedingThreshold
  };
}

/**
 * Generate Weekly Truth Report
 * Complete weekly 'Truth Report' for the Command Center
 */
export function generateWeeklyTruthReport(
  metrics: HealthMetrics[],
  stewardshipScoresByPartner: Record<string, { stewardshipScore: number; isActive: boolean }>,
  redTapeEvents: ExternalSystemFailure[],
  weekStartDate: Date = startOfWeek(new Date())
): WeeklyTruthReport {
  const weekEndDate = endOfWeek(weekStartDate);

  // 1. Data Aggregation
  const glucoseStats = aggregateWeeklyGlucose(metrics, weekStartDate);
  const stewardshipScores = aggregateCommunityStewardship(stewardshipScoresByPartner);
  const earthPhases = forecastEarthPhases(weekEndDate);

  const dataAggregation: WeeklyDataAggregation = {
    weekPeriod: {
      startDate: format(weekStartDate, 'yyyy-MM-dd'),
      endDate: format(weekEndDate, 'yyyy-MM-dd')
    },
    glucoseStats,
    stewardshipScores,
    earthPhases
  };

  // 2. Narrative Generation
  const narrativeGeneration = generateNarrative(
    stewardshipScores.averageStewardship,
    glucoseStats.varianceLevel
  );

  // 3. Threshold Defense
  const thresholdDefense = calculateThresholdDefenseForRedTape(redTapeEvents);

  // Generate summary
  const summary = `Weekly Truth Report: ${format(weekStartDate, 'yyyy-MM-dd')} to ${format(weekEndDate, 'yyyy-MM-dd')}. ` +
    `Glucose mean: ${glucoseStats.mean} mmol/L (variance: ${glucoseStats.varianceLevel}). ` +
    `Average stewardship: ${(stewardshipScores.averageStewardship * 100).toFixed(1)}% (${stewardshipScores.classification}). ` +
    `${narrativeGeneration.narratives.length} narrative(s) generated. ` +
    `System correction required: ${thresholdDefense.system_correction_required ? 'YES' : 'NO'}.`;

  return {
    id: `truth_report_${Date.now()}`,
    period: {
      startDate: format(weekStartDate, 'yyyy-MM-dd'),
      endDate: format(weekEndDate, 'yyyy-MM-dd')
    },
    dataAggregation,
    narrativeGeneration,
    thresholdDefense,
    timestamp: new Date().toISOString(),
    summary
  };
}
