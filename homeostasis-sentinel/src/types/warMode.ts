/**
 * WAR MODE & INTEGRITY TRACKING TYPES
 * Implement Law 31 and Law 5 into the Sentinel's Logic
 * 
 * Protocols:
 * - Karasahin_War_Mode: Law 31 - Defending the Temple
 * - Pierre_Integrity_Check: Law 5 - Your Word Is Your Bond
 */

import { HealthMetrics } from './index';
import { EarthAlignment } from './earthAlignment';

/**
 * War Mode Status
 */
export type WarModeStatus = 'inactive' | 'alert' | 'war' | 'critical';

/**
 * Karasahin War Mode State
 * Law 31: Defending the Temple
 * 
 * TRIGGER: Glucose > 25.0 mmol/L AND (Vision_Clarity < 0.5 OR Ketones_Detected == TRUE)
 * ACTION: Override all 'Shell' notifications with 'High-Alert Seed Command'
 * UI: Red-shift display. Activate 'Aggressive Loop Recovery' sequence
 * LOG: "Law 31 Active. Defending the Temple."
 */
export interface KarasahinWarMode {
  /** Is War Mode active? */
  isActive: boolean;
  /** War status: 'inactive' | 'alert' | 'war' | 'critical' */
  warStatus: WarModeStatus;
  /** Trigger conditions */
  triggers: {
    /** Glucose > 25.0 mmol/L */
    highGlucose: boolean;
    /** Vision_Clarity < 0.5 */
    lowVision: boolean;
    /** Ketones_Detected == TRUE */
    ketonesDetected: boolean;
  };
  /** Trigger values */
  triggerValues: {
    /** Glucose (mmol/L) */
    glucose?: number;
    /** Vision clarity (1-10) */
    visionClarity?: number;
    /** Ketones (mmol/L) */
    ketones?: number;
  };
  /** UI state */
  uiState: {
    /** Red-shift display active? */
    redShiftActive: boolean;
    /** Aggressive Loop Recovery sequence active? */
    loopRecoveryActive: boolean;
    /** Red-shift intensity (0-100) */
    redShiftIntensity: number;
  };
  /** Notification override */
  notificationOverride: {
    /** Override Shell notifications with Seed command? */
    overrideActive: boolean;
    /** High-Alert Seed Command message */
    seedCommand: string;
  };
  /** Log message */
  logMessage: string;
  /** Law reference */
  lawReference: string;
  /** Activation timestamp */
  activatedAt?: string;
  /** Defense condition */
  defenseCondition: DefenseCondition;
}

/**
 * Defense Condition
 * Current defense status
 */
export interface DefenseCondition {
  /** Defense level (0-100) */
  defenseLevel: number;
  /** Defense status: 'secure' | 'breached' | 'critical' */
  defenseStatus: 'secure' | 'breached' | 'critical';
  /** Biological state at time of assessment */
  biologicalState: {
    glucose?: number;
    visionClarity?: number;
    muscleTension?: number;
    ketones?: number;
  };
  /** Required actions */
  requiredActions: string[];
}

/**
 * Pierre Integrity Check State
 * Law 5: Your Word Is Your Bond
 * 
 * TRIGGER: Discrepancy between 'Manual_Input' and 'Sensor_Reality' > 15%
 * ACTION: Flag 'Biological Breach'. Lock 'Stewardship Level' progression for 24 hours
 * MESSAGE: "Law 5 Violation. Your word and your biology are out of sync. Recalibrate."
 */
export interface PierreIntegrityCheck {
  /** Is Integrity Check active? */
  isActive: boolean;
  /** Discrepancy detected? */
  discrepancyDetected: boolean;
  /** Discrepancy percentage */
  discrepancyPercentage: number;
  /** Discrepancy threshold (default: 15%) */
  discrepancyThreshold: number;
  /** Manual input values */
  manualInput: {
    glucose?: number;
    visionClarity?: number;
    muscleTension?: number;
    timestamp: string;
  };
  /** Sensor reality values */
  sensorReality: {
    glucose?: number;
    visionClarity?: number;
    muscleTension?: number;
    timestamp: string;
  };
  /** Biological breach flagged? */
  biologicalBreachFlagged: boolean;
  /** Stewardship level progression locked? */
  stewardshipProgressionLocked: boolean;
  /** Lock expiration timestamp */
  lockExpirationTimestamp?: string;
  /** Message */
  message: string;
  /** Law reference */
  lawReference: string;
  /** Violation timestamp */
  violatedAt?: string;
}

/**
 * Word Is Bond State
 * Law 5: Your Word Is Your Bond - Commitment Consistency
 */
export interface WordIsBondState {
  /** Is commitment consistent? */
  isConsistent: boolean;
  /** Consistency score (0-100) */
  consistencyScore: number;
  /** Commitments made */
  commitmentsMade: number;
  /** Commitments honored */
  commitmentsHonored: number;
  /** Commitments violated */
  commitmentsViolated: number;
  /** Honor rate (0-1) */
  honorRate: number;
  /** Violations flagged */
  violations: IntegrityViolation[];
  /** Law 5 compliance */
  law5Compliance: boolean;
}

/**
 * Integrity Violation
 */
export interface IntegrityViolation {
  /** Violation ID */
  id: string;
  /** Violation type */
  type: 'manual_sensor_mismatch' | 'commitment_unfulfilled' | 'biological_breach';
  /** Description */
  description: string;
  /** Discrepancy percentage */
  discrepancyPercentage?: number;
  /** Timestamp */
  timestamp: string;
  /** Resolved? */
  resolved: boolean;
}

/**
 * Commitment Consistency State
 */
export interface CommitmentConsistency {
  /** Word Is Bond state */
  wordIsBond: WordIsBondState;
  /** Integrity check state */
  integrityCheck: PierreIntegrityCheck;
  /** Overall consistency */
  overallConsistency: number;
  /** Law 5 compliance */
  law5Compliance: boolean;
}

/**
 * Constants
 */
export const WAR_MODE_CONSTANTS = {
  /** Glucose threshold for War Mode (25.0 mmol/L) */
  WAR_MODE_GLUCOSE_THRESHOLD: 25.0,
  /** Vision clarity threshold for War Mode (0.5) */
  WAR_MODE_VISION_THRESHOLD: 0.5,
  /** Discrepancy threshold for Integrity Check (15%) */
  INTEGRITY_DISCREPANCY_THRESHOLD: 15,
  /** Stewardship lock duration (24 hours in ms) */
  STEWARDSHIP_LOCK_DURATION: 24 * 60 * 60 * 1000,
  /** Red-shift intensity when War Mode active (default: 80) */
  WAR_MODE_RED_SHIFT_INTENSITY: 80
} as const;
