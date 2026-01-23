/**
 * ENVIRONMENTAL & COMMUNICATION MODES TYPES
 * Implement 'Silence' and 'Braid' logic gates
 * 
 * Modes:
 * - Ramiz_Silence_Protocol: High muscle_tension OR glucose_volatility > 20%
 * - Jean_Braid_Defense: Red Tape keyword detection, Shell/Seed switching
 */

import { HealthMetrics } from './index';
import { EarthAlignment } from './earthAlignment';

/**
 * Environmental Mode Types
 */
export type EnvironmentalMode = 
  | 'Ramiz_Silence_Protocol'
  | 'Jean_Braid_Defense'
  | 'Normal'
  | 'Alert';

/**
 * Ramiz Silence Protocol State
 * TRIGGER: High `muscle_tension` OR `glucose_volatility` > 20%
 */
export interface RamizSilenceProtocol {
  /** Is Silence Protocol active? */
  isActive: boolean;
  /** Trigger conditions */
  triggers: {
    /** High muscle tension (1-10) */
    highMuscleTension: boolean;
    /** Glucose volatility > 20% */
    highGlucoseVolatility: boolean;
  };
  /** Trigger values */
  triggerValues: {
    /** Muscle tension level (1-10) */
    muscleTension?: number;
    /** Glucose volatility percentage */
    glucoseVolatility?: number;
  };
  /** UI state */
  uiState: {
    /** UI dimmed? */
    dimmed: boolean;
    /** Non-critical notifications silenced? */
    notificationsSilenced: boolean;
    /** Dimming level (0-100, 0 = fully dimmed) */
    dimmingLevel: number;
  };
  /** Message */
  message: string;
  /** Law reference */
  lawReference: string;
  /** Activation timestamp */
  activatedAt?: string;
  /** Deactivation timestamp */
  deactivatedAt?: string;
}

/**
 * Jean Braid Defense State
 * TRIGGER: Detection of 'Red Tape' keywords in external communications/API errors
 */
export interface JeanBraidDefense {
  /** Is Braid Defense active? */
  isActive: boolean;
  /** Red Tape keywords detected */
  redTapeKeywordsDetected: string[];
  /** Communication mode: 'Shell' | 'Seed' */
  communicationMode: 'Shell' | 'Seed';
  /** Shell templates active for outgoing logs? */
  shellTemplatesActive: boolean;
  /** Seed integrity maintained in DB? */
  seedIntegrityMaintained: boolean;
  /** Threshold integrity strength */
  thresholdIntegrity: number;
  /** Log message */
  logMessage: string;
  /** Activation timestamp */
  activatedAt?: string;
  /** Red tape events detected */
  redTapeEvents: RedTapeCommunicationEvent[];
}

/**
 * Red Tape Communication Event
 */
export interface RedTapeCommunicationEvent {
  /** Event ID */
  id: string;
  /** Event type: 'api_error' | 'external_communication' | 'keyword_detection' */
  eventType: 'api_error' | 'external_communication' | 'keyword_detection';
  /** Source */
  source: string;
  /** Red tape keywords detected */
  keywords: string[];
  /** Message content */
  messageContent: string;
  /** Timestamp */
  timestamp: string;
  /** Shell template applied? */
  shellTemplateApplied: boolean;
}

/**
 * Soil Connection State
 * Calculate soil sync from biological data
 */
export interface SoilConnection {
  /** Soil sync score (0-100) */
  soilSync: number;
  /** Soil connection level: 'high' | 'medium' | 'low' */
  connectionLevel: 'high' | 'medium' | 'low';
  /** Biological data used for calculation */
  biologicalData: {
    muscleTension?: number;
    visionClarity?: number;
    breathQuality?: number;
    earthAlignment?: EarthAlignment;
  };
  /** Soil sync components */
  components: {
    /** Muscle tension component */
    muscleComponent: number;
    /** Vision clarity component */
    visionComponent: number;
    /** Breath quality component */
    breathComponent: number;
    /** Earth alignment component */
    earthComponent: number;
  };
}

/**
 * Threshold Integrity State
 */
export interface ThresholdIntegrity {
  /** Braid strength (0-100) */
  braidStrength: number;
  /** Shell/Seed separation integrity (0-100) */
  separationIntegrity: number;
  /** Threshold defense active? */
  thresholdDefenseActive: boolean;
  /** Seed integrity maintained? */
  seedIntegrityMaintained: boolean;
  /** Shell templates active? */
  shellTemplatesActive: boolean;
  /** Overall integrity score (0-100) */
  overallIntegrity: number;
}

/**
 * Environmental Mode State
 * Overall state of environmental and communication modes
 */
export interface EnvironmentalModeState {
  /** Current active mode */
  activeMode: EnvironmentalMode;
  /** Ramiz Silence Protocol state */
  silenceProtocol: RamizSilenceProtocol;
  /** Jean Braid Defense state */
  braidDefense: JeanBraidDefense;
  /** Soil connection state */
  soilConnection: SoilConnection;
  /** Threshold integrity state */
  thresholdIntegrity: ThresholdIntegrity;
}

/**
 * Red Tape Keywords
 * Keywords that trigger Jean Braid Defense
 */
export const RED_TAPE_KEYWORDS = [
  'bureaucracy',
  'red tape',
  'delay',
  'error',
  'failure',
  'timeout',
  'unavailable',
  'denied',
  'rejected',
  'invalid',
  'forbidden',
  'unauthorized',
  'broken',
  'failed',
  'system error',
  'api error',
  'network error',
  'connection error'
] as const;

/**
 * Constants
 */
export const ENVIRONMENTAL_CONSTANTS = {
  /** Muscle tension threshold for Silence Protocol (default: 7) */
  MUSCLE_TENSION_THRESHOLD: 7,
  /** Glucose volatility threshold (default: 20%) */
  GLUCOSE_VOLATILITY_THRESHOLD: 20,
  /** UI dimming level when Silence Protocol active (default: 30) */
  SILENCE_DIMMING_LEVEL: 30,
  /** Soil sync threshold for high connection (default: 70) */
  SOIL_SYNC_HIGH_THRESHOLD: 70,
  /** Soil sync threshold for medium connection (default: 50) */
  SOIL_SYNC_MEDIUM_THRESHOLD: 50
} as const;
