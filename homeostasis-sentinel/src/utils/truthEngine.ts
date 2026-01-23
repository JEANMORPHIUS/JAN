/**
 * THE TRUTH ENGINE
 * Data Architecture: The Truth Engine
 * 
 * Source: Pull glucose (mmol/L), insulin, and loop data.
 * Earth Alignment: Map all data points against local Solar (Sunrise/Sunset) and Lunar cycles.
 * Original Error Filter: Identify "Red Tape" anomalies—where man-made bureaucracy conflicts with biological reality.
 * 
 * Law 1: The Table Never Lies
 * The database is 'The Table.' It cannot lie.
 * Any belief-based overrides must be flagged as 'Original Error' interference.
 */

import { HealthMetrics } from '../types';
import { 
  EarthAlignment, 
  OriginalErrorFlag, 
  LoopEarthAlignment,
  LoopEvent,
  UrineCharacteristics
} from '../types/earthAlignment';
import {
  BiologicalStewardship,
  BiologicalTruth,
  TempleState,
  ProtocolStewardship
} from '../types/stewardship';
import { calculateEarthAlignment, isLoopAlignedWithEarth, getEarthCycleTime } from './earthRhythms';
import { 
  detectOriginalError, 
  detectBeliefOverride,
  calculateProtocolStewardship,
  ProtocolEvent
} from './raconLaws';
import { parseISO } from 'date-fns';

/**
 * Process Health Metrics with Earth Alignment
 * Map all data points against Earth's rhythms
 */
export function processMetricsWithEarthAlignment(
  metrics: HealthMetrics[]
): (HealthMetrics & { earthAlignment?: EarthAlignment })[] {
  return metrics.map(metric => {
    // Calculate Earth alignment for this metric's timestamp
    const timestamp = metric.glucose_time 
      ? `${metric.date}T${metric.glucose_time}:00`
      : `${metric.date}T12:00:00`;
    
    const earthAlignment = calculateEarthAlignment(timestamp);
    
    return {
      ...metric,
      earth_alignment: earthAlignment
    };
  });
}

/**
 * Process Loop Events with Earth Alignment
 * Map loop frequency against Earth's rhythms
 */
export function processLoopEventsWithEarthAlignment(
  metrics: HealthMetrics[]
): LoopEarthAlignment[] {
  const loopEvents: LoopEarthAlignment[] = [];
  
  for (const metric of metrics) {
    if (metric.loop_frequency !== undefined && metric.loop_frequency > 0) {
      const timestamp = metric.glucose_time 
        ? `${metric.date}T${metric.glucose_time}:00`
        : `${metric.date}T12:00:00`;
      
      const earthAlignment = calculateEarthAlignment(timestamp);
      const symbioticCompliance = isLoopAlignedWithEarth(timestamp);
      
      // Create loop event
      const loopEvent: LoopEvent = {
        timestamp,
        volume: 0, // Would be calculated from loop_frequency
        frequency: metric.loop_frequency,
        urineCharacteristics: {
          color: metric.urine_color ?? 5,
          characteristics: undefined,
          earthCycleTime: getEarthCycleTime(timestamp)
        }
      };
      
      // Check for Original Error: Loop against Earth's rhythm
      const originalErrorFlag = !symbioticCompliance && !earthAlignment.solar.inSolarWindow;
      
      loopEvents.push({
        loopEvent,
        earthAlignment,
        symbioticCompliance,
        originalErrorFlag
      });
    }
  }
  
  return loopEvents;
}

/**
 * Extract Biological Truth from Health Metrics
 * Law 1: The Table Never Lies
 */
export function extractBiologicalTruth(metric: HealthMetrics): BiologicalTruth {
  const timestamp = metric.glucose_time 
    ? `${metric.date}T${metric.glucose_time}:00`
    : `${metric.date}T12:00:00`;
  
  // Detect Original Error interference
  const originalErrorFlags = detectOriginalError([metric]);
  
  return {
    glucose: {
      value: metric.blood_glucose ?? 0,
      unit: 'mg/dL',
      timestamp,
      originalErrorFlag: originalErrorFlags.some(e => e.isError && e.errorType === 'sensor_error')
    },
    visionClarity: {
      value: metric.vision_clarity ?? 0,
      timestamp,
      originalErrorFlag: false // Vision clarity is direct observation, not sensor-dependent
    },
    muscleTension: {
      value: metric.muscle_tension ?? 0,
      timestamp,
      originalErrorFlag: false // Muscle tension is direct observation, not sensor-dependent
    },
    breathQuality: {
      value: metric.breath_quality ?? 10,
      timestamp,
      originalErrorFlag: false // Breath quality is direct observation, not sensor-dependent
    }
  };
}

/**
 * Calculate Biological Stewardship
 * The body as temple - stewarded, not exploited
 */
export function calculateBiologicalStewardship(
  metrics: HealthMetrics[]
): BiologicalStewardship {
  const latestMetric = metrics[metrics.length - 1];
  const timestamp = latestMetric.glucose_time 
    ? `${latestMetric.date}T${latestMetric.glucose_time}:00`
    : `${latestMetric.date}T12:00:00`;
  
  const biologicalTruth = extractBiologicalTruth(latestMetric);
  const earthAlignment = calculateEarthAlignment(timestamp);
  const originalErrors = detectOriginalError(metrics);
  
  // Calculate stewardship level (0-100)
  // Based on: biological truth alignment, Earth alignment, absence of Original Errors
  let stewardshipLevel = 50; // Base score
  
  // Increase for Earth alignment (symbiotic relationship)
  stewardshipLevel += earthAlignment.symbioticScore * 0.3;
  
  // Increase for absence of Original Errors
  const errorPenalty = originalErrors.filter(e => e.isError).length * 10;
  stewardshipLevel = Math.max(0, stewardshipLevel - errorPenalty);
  
  // Adjust for biological truth stability
  if (biologicalTruth.visionClarity.value >= 6 && 
      biologicalTruth.muscleTension.value <= 5 &&
      biologicalTruth.breathQuality.value >= 7) {
    stewardshipLevel += 20;
  }
  
  stewardshipLevel = Math.min(100, stewardshipLevel);
  
  // Determine temple state
  let templeState: TempleState = 'stable';
  if (stewardshipLevel >= 80) {
    templeState = 'optimal';
  } else if (stewardshipLevel >= 60) {
    templeState = 'stable';
  } else if (stewardshipLevel >= 40) {
    templeState = 'attention';
  } else {
    templeState = 'crisis';
  }
  
  return {
    templeState,
    stewardshipLevel: Math.round(stewardshipLevel),
    biologicalTruth,
    originalErrors,
    earthAlignment
  };
}

/**
 * Calculate Integrated Stewardship
 * Mission + Laws + Biology + Earth
 */
export function calculateIntegratedStewardship(
  metrics: HealthMetrics[],
  protocolEvents: ProtocolEvent[] = []
): {
  biological: BiologicalStewardship;
  protocol: ProtocolStewardship;
  earth: LoopEarthAlignment[];
  overallStewardshipScore: number;
} {
  const biological = calculateBiologicalStewardship(metrics);
  const protocol = calculateProtocolStewardship(protocolEvents);
  const earth = processLoopEventsWithEarthAlignment(metrics);
  
  // Calculate overall stewardship score (0-100)
  // Weighted: Biological (40%), Protocol (30%), Earth (30%)
  const biologicalScore = biological.stewardshipLevel * 0.4;
  const protocolScore = protocol.protocolCommitment * 0.3;
  const earthScore = earth.length > 0 
    ? (earth.filter(e => e.symbioticCompliance).length / earth.length) * 100 * 0.3
    : 0;
  
  const overallStewardshipScore = Math.round(biologicalScore + protocolScore + earthScore);
  
  return {
    biological,
    protocol,
    earth,
    overallStewardshipScore: Math.min(100, Math.max(0, overallStewardshipScore))
  };
}

/**
 * Filter Original Error Anomalies
 * Identify "Red Tape" anomalies where man-made bureaucracy conflicts with biological reality
 */
export function filterOriginalErrors(metrics: HealthMetrics[]): {
  cleanMetrics: HealthMetrics[];
  originalErrors: OriginalErrorFlag[];
} {
  const originalErrors = detectOriginalError(metrics);
  const errorIndices = new Set<number>();
  
  // Mark metrics with Original Errors
  originalErrors.forEach(error => {
    if (error.isError) {
      const index = metrics.findIndex(m => 
        m.date === error.timestamp || 
        (error.biologicalTruth.includes(m.date))
      );
      if (index !== -1) {
        errorIndices.add(index);
      }
    }
  });
  
  // Filter out metrics with critical Original Errors (keep flagged but don't use in calculations)
  // For now, keep all metrics but flag them
  const cleanMetrics = metrics.map((metric, index) => ({
    ...metric,
    original_error_flags: errorIndices.has(index) 
      ? originalErrors.filter(e => e.isError && e.timestamp === metric.date)
      : undefined
  }));
  
  return {
    cleanMetrics,
    originalErrors
  };
}

/**
 * Get Symbiotic Compass Data
 * UI element showing loop status in relation to Earth's Circadian rhythm
 */
export function getSymbioticCompassData(
  metrics: HealthMetrics[]
): {
  currentEarthAlignment: EarthAlignment;
  loopAlignment: LoopEarthAlignment[];
  symbioticScore: number;
  inSolarWindow: boolean;
  earthCycleTime: string;
} {
  const latestMetric = metrics[metrics.length - 1];
  const timestamp = latestMetric.glucose_time 
    ? `${latestMetric.date}T${latestMetric.glucose_time}:00`
    : `${latestMetric.date}T12:00:00`;
  
  const currentEarthAlignment = calculateEarthAlignment(timestamp);
  const loopAlignment = processLoopEventsWithEarthAlignment(metrics);
  
  return {
    currentEarthAlignment,
    loopAlignment,
    symbioticScore: currentEarthAlignment.symbioticScore,
    inSolarWindow: currentEarthAlignment.solar.inSolarWindow,
    earthCycleTime: getEarthCycleTime(timestamp)
  };
}
