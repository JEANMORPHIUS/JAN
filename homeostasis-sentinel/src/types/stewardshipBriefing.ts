/**
 * STEWARDSHIP BRIEFING AUTOMATION TYPES
 * Generate weekly 'Truth Report' for the Command Center
 * 
 * Features:
 * - Data Aggregation: Weekly glucose, stewardship scores, lunar/solar phases
 * - Narrative Generation: Entity voice modules triggered by conditions
 * - Threshold Defense: Flag red tape events (>3 occurrences)
 */

import { EarthAlignment } from './earthAlignment';
import { ExternalSystemFailure } from './pierreLogic';

/**
 * Weekly Data Aggregation
 */
export interface WeeklyDataAggregation {
  /** Week period (start date - end date) */
  weekPeriod: {
    startDate: string;
    endDate: string;
  };
  /** Weekly glucose statistics */
  glucoseStats: GlucoseStatistics;
  /** Stewardship scores from all active community partners */
  stewardshipScores: CommunityStewardshipScores;
  /** Lunar/Solar phase data for the upcoming 7 days */
  earthPhases: EarthPhaseForecast;
}

/**
 * Glucose Statistics
 */
export interface GlucoseStatistics {
  /** Mean glucose (mmol/L) */
  mean: number;
  /** Variance (mmol/L²) */
  variance: number;
  /** Standard deviation (mmol/L) */
  standardDeviation: number;
  /** Minimum glucose (mmol/L) */
  min: number;
  /** Maximum glucose (mmol/L) */
  max: number;
  /** Data point count */
  count: number;
  /** Variance classification: 'Low' | 'Medium' | 'High' */
  varianceLevel: 'Low' | 'Medium' | 'High';
}

/**
 * Community Stewardship Scores
 */
export interface CommunityStewardshipScores {
  /** Average stewardship score (0-1) */
  averageStewardship: number;
  /** Scores by partner */
  scoresByPartner: Record<string, {
    /** Partner name */
    partnerName: string;
    /** Stewardship score (0-1) */
    stewardshipScore: number;
    /** Active status */
    isActive: boolean;
  }>;
  /** Total active partners */
  activePartnersCount: number;
  /** Classification: 'Optimal' | 'Stable' | 'Warning' | 'Critical' */
  classification: 'Optimal' | 'Stable' | 'Warning' | 'Critical';
}

/**
 * Earth Phase Forecast
 * Lunar/Solar phase data for the upcoming 7 days
 */
export interface EarthPhaseForecast {
  /** Forecast period */
  period: {
    startDate: string;
    endDate: string;
  };
  /** Daily phase data */
  dailyPhases: DailyEarthPhase[];
}

/**
 * Daily Earth Phase
 */
export interface DailyEarthPhase {
  /** Date */
  date: string;
  /** Solar phase */
  solarPhase: 'sunrise' | 'solar_peak' | 'sunset' | 'night';
  /** Lunar phase */
  lunarPhase: 'new_moon' | 'waxing' | 'full_moon' | 'waning';
  /** Solar intensity (0-100) */
  solarIntensity: number;
  /** Lunar intensity (0-100) */
  lunarIntensity: number;
  /** Symbiotic score (0-100) */
  symbioticScore: number;
}

/**
 * Narrative Generation
 * Entity voice modules triggered by conditions
 */
export interface NarrativeGeneration {
  /** Generated narratives */
  narratives: Narrative[];
  /** Trigger conditions met */
  conditionsMet: string[];
}

/**
 * Narrative
 */
export interface Narrative {
  /** Narrative ID */
  id: string;
  /** Entity voice module */
  entityVoice: 'Ramiz' | 'Karasahin' | 'Jean' | 'Pierre';
  /** Trigger condition */
  condition: string;
  /** Narrative message */
  message: string;
  /** Law reference */
  lawReference?: string;
  /** Priority: 'critical' | 'warning' | 'info' */
  priority: 'critical' | 'warning' | 'info';
}

/**
 * Threshold Defense State
 * Flag red tape events that occurred more than 3 times
 */
export interface ThresholdDefenseState {
  /** System correction required? */
  system_correction_required: boolean;
  /** Red tape events flagged */
  flaggedRedTapeEvents: FlaggedRedTapeEvent[];
  /** Total red tape events */
  totalRedTapeEvents: number;
  /** Events exceeding threshold (>3) */
  eventsExceedingThreshold: number;
}

/**
 * Flagged Red Tape Event
 */
export interface FlaggedRedTapeEvent {
  /** Failure type */
  failureType: 'api_downtime' | 'sensor_failure' | 'system_latency' | 'other';
  /** Occurrence count */
  occurrenceCount: number;
  /** Threshold (default: 3) */
  threshold: number;
  /** Is flagged? */
  isFlagged: boolean;
  /** First occurrence timestamp */
  firstOccurrence: string;
  /** Latest occurrence timestamp */
  latestOccurrence: string;
}

/**
 * Weekly Truth Report
 */
export interface WeeklyTruthReport {
  /** Report ID */
  id: string;
  /** Report period */
  period: {
    startDate: string;
    endDate: string;
  };
  /** Data aggregation */
  dataAggregation: WeeklyDataAggregation;
  /** Narrative generation */
  narrativeGeneration: NarrativeGeneration;
  /** Threshold defense state */
  thresholdDefense: ThresholdDefenseState;
  /** Report timestamp */
  timestamp: string;
  /** Report summary */
  summary: string;
}
