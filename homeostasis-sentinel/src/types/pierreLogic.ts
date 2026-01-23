/**
 * PIERRE'S LOGIC OF THE SEED
 * Implementing Pierre Pressure's "Logic of the Seed" into the UI
 * 
 * Pierre's Voice: Direct, commanding, no-nonsense realism
 * "The Original Error is manifesting. Return to Biological Truth (Law 13)."
 */

import { OriginalErrorFlag } from './earthAlignment';

/**
 * Anomaly Detection State
 * Pierre's Logic: Detect Original Error manifestation
 */
export interface AnomalyDetection {
  /** Is there a sensor error? */
  sensorError: boolean;
  /** System latency (ms) */
  systemLatency: number;
  /** Latency threshold (ms) - default: 1000 */
  latencyThreshold: number;
  /** Is anomaly detected? (sensor error OR latency > threshold) */
  isAnomalyDetected: boolean;
  /** Pierre Voice Module message */
  pierreVoiceMessage?: string;
  /** Original Error flag */
  originalErrorFlag?: OriginalErrorFlag;
  /** Timestamp of anomaly detection */
  timestamp: string;
}

/**
 * Red Tape Counter
 * Track man-made errors (External System Failures)
 */
export interface RedTapeCounter {
  /** Total red tape incidents */
  totalIncidents: number;
  /** Incidents by type */
  incidentsByType: {
    /** API downtime incidents */
    apiDowntime: number;
    /** Sensor failure incidents */
    sensorFailure: number;
    /** System latency incidents */
    systemLatency: number;
    /** Other external system failures */
    other: number;
  };
  /** Latest incident timestamp */
  latestIncidentTimestamp?: string;
  /** Total duration of failures (ms) */
  totalFailureDuration: number;
}

/**
 * Earth Rhythm Success Counter
 * Track data points aligned with Circadian/Lunar cycles
 */
export interface EarthRhythmSuccess {
  /** Total data points */
  totalDataPoints: number;
  /** Data points aligned with Earth rhythms */
  alignedDataPoints: number;
  /** Success rate (0-100) */
  successRate: number;
  /** Alignment breakdown by type */
  alignmentByType: {
    /** Solar-aligned data points */
    solarAligned: number;
    /** Circadian-aligned data points */
    circadianAligned: number;
    /** Lunar-aligned data points */
    lunarAligned: number;
    /** Seasonally-aligned data points */
    seasonallyAligned: number;
  };
}

/**
 * Pierre's Logic Variables
 * Refinement: Variables reflect Pierre's logic
 */
export interface PierreLogicState {
  /** Is this a broken system? (Boolean) */
  is_broken_system: boolean;
  /** Earth rhythm sync score (Float, 0-100) */
  earth_rhythm_sync_score: number;
  /** Red Tape counter */
  redTapeCounter: RedTapeCounter;
  /** Earth Rhythm Success counter */
  earthRhythmSuccess: EarthRhythmSuccess;
  /** Anomaly detection state */
  anomalyDetection: AnomalyDetection;
  /** Pierre Voice Module active? */
  pierreVoiceActive: boolean;
}

/**
 * External System Failure
 * Man-made error logging
 */
export interface ExternalSystemFailure {
  /** Failure type: 'api_downtime' | 'sensor_failure' | 'system_latency' | 'other' */
  failureType: 'api_downtime' | 'sensor_failure' | 'system_latency' | 'other';
  /** Failure description */
  description: string;
  /** Failure timestamp */
  timestamp: string;
  /** Duration (ms) */
  duration?: number;
  /** Is this Original Error? */
  isOriginalError: boolean;
  /** Biological truth at time of failure */
  biologicalTruth?: string;
}
