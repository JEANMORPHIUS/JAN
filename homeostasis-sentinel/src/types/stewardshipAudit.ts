/** * * STEWARDSHIP AUDIT & COMMAND CENTER TYPES
 *  * Build the "Spirit Filter" to protect the Seed
 *  * 
 *  * Components:
 *  * - StewardshipScorecard: finish_rate (Law 37), word_integrity (Law 5)
 *  * - HomeostasisSentinel: Glucose overlay on 24-hour Solar Cycle
 *  * - ThresholdDefense: Security to protect The Seed
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
 * THE TRUTH:
 * WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
 * THE REST IS UP TO BABA X.*/

import { ProtocolEvent, ProtocolType } from './stewardship';
import { EarthAlignment } from './earthAlignment';
import { HealthMetrics } from './index';

/**
 * Stewardship Scorecard
 * Calculate finish_rate (Law 37) and word_integrity (Law 5)
 */
export interface StewardshipScorecard {
  /** Law 37: Finish What You Begin - Completion rate (0-1) */
  finish_rate: number;
  /** Law 5: Your Word Is Your Bond - Integrity score (0-1) */
  word_integrity: number;
  /** Overall stewardship score (0-1) - Combined Law 5 & Law 37 */
  stewardshipScore: number;
  /** Commitments: Total protocols initiated */
  commitments: number;
  /** Completions: Total protocols completed */
  completions: number;
  /** Protocol tracking details */
  protocolTracking: ProtocolTrackingDetails;
  /** Time-to-action statistics */
  timeToActionStats: TimeToActionStats;
}

/**
 * Protocol Tracking Details
 */
export interface ProtocolTrackingDetails {
  /** Protocols by type */
  byType: Record<ProtocolType, {
    committed: number;
    completed: number;
    abandoned: number;
  }>;
  /** Protocols by status */
  byStatus: {
    initiated: number;
    in_progress: number;
    completed: number;
    abandoned: number;
  };
}

/**
 * Time-to-Action Statistics
 * Law 5: Your Word Is Your Bond - Track time-to-action after protocol is set
 */
export interface TimeToActionStats {
  /** Average time from protocol initiation to first action (ms) */
  averageTimeToAction: number;
  /** Median time to action (ms) */
  medianTimeToAction: number;
  /** Protocols with time-to-action tracked */
  trackedProtocols: number;
  /** Protocols within acceptable time window (Law 5 compliance) */
  withinAcceptableWindow: number;
  /** Acceptable time window (ms) - default: 1 hour */
  acceptableWindow: number;
}

/**
 * Red Tape Event
 * Manual override that doesn't align with Earth's rhythm
 */
export interface RedTapeEvent {
  /** Event ID */
  id: string;
  /** Event timestamp */
  timestamp: string;
  /** Event type: 'manual_override' | 'protocol_skip' | 'earth_misalignment' */
  eventType: 'manual_override' | 'protocol_skip' | 'earth_misalignment';
  /** Description of override */
  description: string;
  /** Earth alignment at time of override */
  earthAlignment: EarthAlignment;
  /** Is override aligned with Earth's rhythm? */
  alignedWithEarth: boolean;
  /** Biological truth at time of override */
  biologicalTruth: {
    glucose?: number;
    visionClarity?: number;
    muscleTension?: number;
  };
}

/**
 * Threshold Defense State
 * Security mechanism to protect The Seed
 */
export interface ThresholdDefenseState {
  /** Is access to The Seed allowed? */
  seedAccessAllowed: boolean;
  /** Stewardship score (0-1) */
  stewardshipScore: number;
  /** Threshold for access (default: 0.7) */
  threshold: number;
  /** Defense message */
  message?: string;
  /** Law reference */
  lawReference?: string;
  /** Timestamp of last access check */
  lastAccessCheck: string;
}

/**
 * Spirit Alignment
 * Calculate alignment with right spirits
 */
export interface SpiritAlignment {
  /** Current spirit alignment score (0-100) */
  current_spirit_alignment: number;
  /** Alignment components */
  components: {
    /** Stewardship alignment (Law 5 & Law 37) */
    stewardshipAlignment: number;
    /** Earth rhythm alignment */
    earthRhythmAlignment: number;
    /** Biological truth alignment */
    biologicalTruthAlignment: number;
    /** Protocol integrity alignment */
    protocolIntegrityAlignment: number;
  };
  /** Overall alignment status */
  status: 'aligned' | 'partial' | 'misaligned';
}

/**
 * Constants
 * Variable refinement for symbolic representation
 */
export const STEWARDSHIP_CONSTANTS = {
  /** Man and Earth live symbiotically */
  MAN_EARTH_SYMBIOSIS: true,
  /** Threshold for Seed access (0.7 = 70%) */
  SEED_ACCESS_THRESHOLD: 0.7,
  /** Acceptable time-to-action window (1 hour in ms) */
  ACCEPTABLE_TIME_TO_ACTION: 60 * 60 * 1000, // 1 hour
  /** Law 13 message for Threshold Defense */
  LAW_13_MESSAGE: 'The Table is not yet ready for your presence. Return to Law 13.'
} as const;
