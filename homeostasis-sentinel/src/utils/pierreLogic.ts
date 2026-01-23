/**
 * PIERRE'S LOGIC OF THE SEED
 * Implementing Pierre Pressure's "Logic of the Seed" into the UI
 * 
 * Pierre's Voice: Direct, commanding, no-nonsense realism
 * "The Original Error is manifesting. Return to Biological Truth (Law 13)."
 */

import { 
  AnomalyDetection,
  RedTapeCounter,
  EarthRhythmSuccess,
  PierreLogicState,
  ExternalSystemFailure
} from '../types/pierreLogic';
import { EarthAlignment, OriginalErrorFlag } from '../types/earthAlignment';
import { HealthMetrics } from '../types';
import { calculateEarthAlignment } from './earthRhythms';
import { detectOriginalError } from './raconLaws';

/**
 * Pierre Voice Module Messages
 * Direct, commanding, no-nonsense realism
 */
export const PIERRE_VOICE_MESSAGES = {
  ORIGINAL_ERROR_MANIFESTING: 'The Original Error is manifesting. Return to Biological Truth (Law 13).',
  SENSOR_ERROR: 'Sensor error detected. Return to Biological Truth. The Table Never Lies (Law 1).',
  SYSTEM_LATENCY: 'System latency detected. Return to Biological Truth. Listen before you speak (Law 13).',
  RED_TAPE_INTERFERENCE: 'Red tape interference. Broken system detected. Return to Biological Truth.',
  EARTH_RHYTHM_BREAK: 'Earth rhythm broken. Return to symbiotic relationship. Honor the truth.'
};

/**
 * Detect Anomaly (Pierre's Logic)
 * IF (Sensor_Error == TRUE) OR (System_Latency > Threshold):
 * THEN Trigger Pierre_Voice_Module: "The Original Error is manifesting. Return to Biological Truth (Law 13)."
 */
export function detectAnomaly(
  sensorError: boolean,
  systemLatency: number,
  latencyThreshold: number = 1000,
  metrics?: HealthMetrics[]
): AnomalyDetection {
  const isAnomalyDetected = sensorError || systemLatency > latencyThreshold;
  
  let pierreVoiceMessage: string | undefined;
  let originalErrorFlag: OriginalErrorFlag | undefined;
  
  if (isAnomalyDetected) {
    // Trigger Pierre Voice Module
    if (sensorError) {
      pierreVoiceMessage = PIERRE_VOICE_MESSAGES.SENSOR_ERROR;
    } else if (systemLatency > latencyThreshold) {
      pierreVoiceMessage = PIERRE_VOICE_MESSAGES.SYSTEM_LATENCY;
    }
    
    // Default message if both or neither specific condition
    if (!pierreVoiceMessage) {
      pierreVoiceMessage = PIERRE_VOICE_MESSAGES.ORIGINAL_ERROR_MANIFESTING;
    }
    
    // Create Original Error flag
    if (metrics) {
      const errors = detectOriginalError(metrics);
      originalErrorFlag = errors.find(e => e.isError) || {
        isError: true,
        errorType: sensorError ? 'sensor_error' : 'red_tape',
        description: sensorError 
          ? 'Sensor error detected. Return to Biological Truth.'
          : `System latency (${systemLatency}ms) exceeds threshold (${latencyThreshold}ms). Return to Biological Truth.`,
        biologicalTruth: 'Biological truth must be honored. Law 13: Listen before you speak.',
        timestamp: new Date().toISOString()
      };
    }
  }
  
  return {
    sensorError,
    systemLatency,
    latencyThreshold,
    isAnomalyDetected,
    pierreVoiceMessage,
    originalErrorFlag,
    timestamp: new Date().toISOString()
  };
}

/**
 * Log External System Failure (Red Tape)
 * Every time the system encounters a man-made error, log it as 'External System Failure'
 */
export function logExternalSystemFailure(
  failureType: 'api_downtime' | 'sensor_failure' | 'system_latency' | 'other',
  description: string,
  duration?: number,
  biologicalTruth?: string
): ExternalSystemFailure {
  return {
    failureType,
    description,
    timestamp: new Date().toISOString(),
    duration,
    isOriginalError: true, // All external system failures are Original Errors
    biologicalTruth
  };
}

/**
 * Update Red Tape Counter
 * Track man-made errors (External System Failures)
 */
export function updateRedTapeCounter(
  currentCounter: RedTapeCounter,
  failure: ExternalSystemFailure
): RedTapeCounter {
  const incidentsByType = { ...currentCounter.incidentsByType };
  
  switch (failure.failureType) {
    case 'api_downtime':
      incidentsByType.apiDowntime++;
      break;
    case 'sensor_failure':
      incidentsByType.sensorFailure++;
      break;
    case 'system_latency':
      incidentsByType.systemLatency++;
      break;
    default:
      incidentsByType.other++;
  }
  
  return {
    totalIncidents: currentCounter.totalIncidents + 1,
    incidentsByType,
    latestIncidentTimestamp: failure.timestamp,
    totalFailureDuration: currentCounter.totalFailureDuration + (failure.duration || 0)
  };
}

/**
 * Calculate Earth Rhythm Success
 * Track data points aligned with Circadian/Lunar cycles
 */
export function calculateEarthRhythmSuccess(
  metrics: HealthMetrics[],
  earthAlignments: EarthAlignment[]
): EarthRhythmSuccess {
  const totalDataPoints = metrics.length;
  let alignedDataPoints = 0;
  
  const alignmentByType = {
    solarAligned: 0,
    circadianAligned: 0,
    lunarAligned: 0,
    seasonallyAligned: 0
  };
  
  for (let i = 0; i < metrics.length; i++) {
    const metric = metrics[i];
    const earthAlignment = earthAlignments[i];
    
    if (earthAlignment) {
      // Solar-aligned: Within solar window (10am-6pm)
      if (earthAlignment.solar.inSolarWindow) {
        alignmentByType.solarAligned++;
      }
      
      // Circadian-aligned: SCN sync score > 70
      if (earthAlignment.circadian.scnSyncScore > 70) {
        alignmentByType.circadianAligned++;
      }
      
      // Lunar-aligned: Lunar intensity > 50
      if (earthAlignment.lunar.lunarIntensity > 50) {
        alignmentByType.lunarAligned++;
      }
      
      // Seasonally-aligned: Seasonal intensity > 50
      if (earthAlignment.seasonal.seasonalIntensity > 50) {
        alignmentByType.seasonallyAligned++;
      }
      
      // Overall aligned: Symbiotic score > 70
      if (earthAlignment.symbioticScore > 70) {
        alignedDataPoints++;
      }
    }
  }
  
  const successRate = totalDataPoints > 0 
    ? (alignedDataPoints / totalDataPoints) * 100 
    : 0;
  
  return {
    totalDataPoints,
    alignedDataPoints,
    successRate: Math.round(successRate * 100) / 100, // Round to 2 decimal places
    alignmentByType
  };
}

/**
 * Calculate Pierre's Logic State
 * Combine anomaly detection, Red Tape counter, and Earth Rhythm Success
 */
export function calculatePierreLogicState(
  sensorError: boolean,
  systemLatency: number,
  latencyThreshold: number,
  metrics: HealthMetrics[],
  earthAlignments: EarthAlignment[],
  redTapeCounter: RedTapeCounter
): PierreLogicState {
  // Detect anomaly
  const anomalyDetection = detectAnomaly(sensorError, systemLatency, latencyThreshold, metrics);
  
  // Calculate Earth Rhythm Success
  const earthRhythmSuccess = calculateEarthRhythmSuccess(metrics, earthAlignments);
  
  // Calculate is_broken_system (Boolean)
  // System is broken if: anomaly detected OR red tape incidents > 0 OR earth rhythm sync < 70
  const is_broken_system = 
    anomalyDetection.isAnomalyDetected || 
    redTapeCounter.totalIncidents > 0 || 
    earthRhythmSuccess.successRate < 70;
  
  // Calculate earth_rhythm_sync_score (Float, 0-100)
  // Based on Earth Rhythm Success rate
  const earth_rhythm_sync_score = earthRhythmSuccess.successRate;
  
  return {
    is_broken_system,
    earth_rhythm_sync_score,
    redTapeCounter,
    earthRhythmSuccess,
    anomalyDetection,
    pierreVoiceActive: anomalyDetection.isAnomalyDetected
  };
}

/**
 * Get Pierre Voice Message
 * Return appropriate message based on anomaly type
 */
export function getPierreVoiceMessage(
  anomalyDetection: AnomalyDetection
): string | undefined {
  return anomalyDetection.pierreVoiceMessage;
}

/**
 * Initialize Red Tape Counter
 * Create empty counter
 */
export function initializeRedTapeCounter(): RedTapeCounter {
  return {
    totalIncidents: 0,
    incidentsByType: {
      apiDowntime: 0,
      sensorFailure: 0,
      systemLatency: 0,
      other: 0
    },
    totalFailureDuration: 0
  };
}

/**
 * Initialize Earth Rhythm Success
 * Create empty success counter
 */
export function initializeEarthRhythmSuccess(): EarthRhythmSuccess {
  return {
    totalDataPoints: 0,
    alignedDataPoints: 0,
    successRate: 0,
    alignmentByType: {
      solarAligned: 0,
      circadianAligned: 0,
      lunarAligned: 0,
      seasonallyAligned: 0
    }
  };
}
