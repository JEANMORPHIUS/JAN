/**
 * FOURTH WAY TYPES
 * Self-Remembering, Observation Gate, Many I's Filter
 * 
 * Based on Gurdjieff/Ouspensky Fourth Way philosophy:
 * - Self-remembering: Am I observing the machine or is the machine observing me?
 * - Many I's: Which 'I' is speaking at the Table right now?
 * - Presence: Response time vs. biological stability
 */

import { HealthMetrics } from './index';

/**
 * Observation Gate
 * Triggers self-remembering prompts at random intervals or when Red Tape is detected
 */
export interface ObservationGate {
  /** Trigger type: random interval or red tape detection */
  triggerType: 'random_interval' | 'red_tape' | 'manual';
  /** Timestamp when gate was triggered */
  timestamp: string;
  /** The prompt dispatched */
  prompt: string; // "Are you observing the machine or is the machine observing you?"
  /** Presence coefficient: response time vs. biological stability (0-1) */
  presenceCoefficient: number;
  /** Response timestamp (if user responded) */
  responseTimestamp?: string;
  /** Response time in milliseconds (from prompt to response) */
  responseTimeMs?: number;
  /** Biological stability at time of prompt (glucose, vision, muscle, breath variance) */
  biologicalStability: number; // 0-1 (higher = more stable)
  /** User's self-observation reflection (if provided) */
  reflection?: string;
}

/**
 * Presence Coefficient
 * Metric tracking self-remembering: response time vs. biological stability
 * - High coefficient = fast response + high stability = present
 * - Low coefficient = slow response + low stability = absent
 */
export interface PresenceCoefficient {
  /** Coefficient value (0-1) */
  value: number;
  /** Response time normalized (0-1, lower is better) */
  responseTimeNormalized: number;
  /** Biological stability at time of observation (0-1, higher is better) */
  biologicalStability: number;
  /** Interpretation: 'present' | 'emerging' | 'absent' */
  interpretation: 'present' | 'emerging' | 'absent';
  /** Guidance based on interpretation */
  guidance: string;
  /** Timestamp */
  timestamp: string;
}

/**
 * Many I's Filter
 * Detects impulsive/inconsistent input and triggers Pierre Voice (Law 5: Your word is your bond)
 */
export interface ManyIsFilter {
  /** Input type that triggered the filter */
  inputType: 'glucose_reading' | 'protocol_entry' | 'community_interaction' | 'other';
  /** Original input */
  input: string;
  /** Timestamp */
  timestamp: string;
  /** Impulsivity score (0-1, higher = more impulsive) */
  impulsivityScore: number;
  /** Inconsistency indicators */
  inconsistencyIndicators: {
    /** Rapid successive entries (within 5 minutes) */
    rapidEntries: boolean;
    /** Large value jumps (e.g., glucose 17.8 → 3.2 in 1 hour) */
    largeJumps: boolean;
    /** Contradictory statements (e.g., "fasting" then "eating") */
    contradictoryStatements: boolean;
    /** Missing context (e.g., reading without time or loop info) */
    missingContext: boolean;
  };
  /** Is filter triggered? (impulsivity > 0.7 or multiple inconsistencies) */
  isTriggered: boolean;
  /** Pierre Voice message (if triggered) */
  pierreVoiceMessage?: string; // "Which 'I' is speaking at the Table right now? Return to the Law 5 Bond."
  /** Law 5 compliance check */
  law5Compliance: {
    /** Is user honoring their word? */
    isCompliant: boolean;
    /** Context for compliance check */
    context: string;
    /** Guidance for return to Law 5 */
    guidance: string;
  };
}

/**
 * Consciousness Level
 * Calculated from biological data and law consistency
 * Measures self-observation and presence
 */
export interface ConsciousnessLevel {
  /** Level value (0-1, higher = more conscious/present) */
  level: number;
  /** Self-observation component (from presence coefficient history) */
  selfObservation: number; // 0-1
  /** Law consistency component (Law 5 and Law 37 adherence) */
  lawConsistency: number; // 0-1
  /** Biological alignment component (Earth rhythm alignment) */
  biologicalAlignment: number; // 0-1
  /** Interpretation: 'awake' | 'emerging' | 'sleeping' | 'mechanical' */
  interpretation: 'awake' | 'emerging' | 'sleeping' | 'mechanical';
  /** Guidance based on level */
  guidance: string;
  /** Timestamp */
  timestamp: string;
  /** Recent presence coefficients (last 7 observations) */
  recentPresenceCoefficients: number[];
  /** Law 5 compliance rate (0-1) */
  law5ComplianceRate: number;
  /** Law 37 compliance rate (0-1) */
  law37ComplianceRate: number;
}

/**
 * Self-Remembering Session
 * A complete self-remembering observation cycle
 */
export interface SelfRememberingSession {
  /** Gate that triggered this session */
  gate: ObservationGate;
  /** Presence coefficient for this session */
  presenceCoefficient: PresenceCoefficient;
  /** Many I's filter result (if triggered) */
  manyIsFilter?: ManyIsFilter;
  /** Consciousness level at time of session */
  consciousnessLevel: ConsciousnessLevel;
  /** Session outcome */
  outcome: {
    /** Did user respond? */
    responded: boolean;
    /** Did user show presence? (presence coefficient > 0.7) */
    showedPresence: boolean;
    /** Did Many I's filter trigger? */
    manyIsTriggered: boolean;
    /** Overall session assessment */
    assessment: 'present' | 'emerging' | 'absent';
  };
}
