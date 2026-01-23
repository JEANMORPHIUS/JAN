/**
 * INITIALIZE DAY 1 OF 376 TYPES
 * Establish the Baseline for the Sovereign Stewardship
 * 
 * Components:
 * - Reset_Stewardship_Clock: Set current_day = 1, 24-hour First Loop timer
 * - Baseline_Truth_Establishment: Record first glucose_reading as Foundation Value
 * - The Braid_Call: Alert 8 London Nodes
 * - Variables: GO_LIVE, ARCHITECTURE_SHIELD_ACTIVE
 */

import { HealthMetrics } from './index';
import { CommunityNode } from './expansionPhase';

/**
 * Reset Stewardship Clock State
 * Set `current_day = 1`
 * Start 24-hour 'First Loop' timer
 */
export interface ResetStewardshipClockState {
  /** Is clock reset? */
  isReset: boolean;
  /** Current day (1-376) */
  currentDay: number;
  /** Total days (376) */
  totalDays: number;
  /** Day 1 start timestamp */
  day1StartTimestamp: string;
  /** First Loop timer start timestamp */
  firstLoopTimerStartTimestamp: string;
  /** First Loop timer end timestamp (24 hours) */
  firstLoopTimerEndTimestamp: string;
  /** First Loop timer remaining (seconds) */
  firstLoopTimerRemaining: number;
  /** First Loop timer active? */
  firstLoopTimerActive: boolean;
  /** First Loop completed? */
  firstLoopCompleted: boolean;
  /** Clock status */
  clockStatus: 'reset' | 'running' | 'paused' | 'completed';
}

/**
 * Baseline Truth Establishment State
 * Record the first `glucose_reading` as the 'Foundation Value'
 * IF (Manual_Override == TRUE): THEN Flag 'Law 13' (Listen) to remind the user to trust the loop
 */
export interface BaselineTruthEstablishmentState {
  /** Is baseline established? */
  isBaselineEstablished: boolean;
  /** Foundation Value (first glucose reading) */
  foundationValue: FoundationValue;
  /** Manual override detected? */
  manualOverrideDetected: boolean;
  /** Law 13 flagged? */
  law13Flagged: boolean;
  /** Law 13 message */
  law13Message?: string;
  /** Baseline timestamp */
  baselineTimestamp: string;
}

/**
 * Foundation Value
 * The first glucose reading recorded as the Foundation Value
 */
export interface FoundationValue {
  /** Glucose value (mmol/L) */
  glucoseValue: number;
  /** Glucose unit */
  glucoseUnit: 'mmol/L' | 'mg/dL';
  /** Reading timestamp */
  readingTimestamp: string;
  /** Reading source */
  readingSource: 'sensor' | 'manual' | 'hybrid';
  /** Is manual override? */
  isManualOverride: boolean;
  /** Foundation Value immutable */
  immutable: true;
}

/**
 * The Braid Call State
 * Alert the 8 London Nodes: "The Sentinel is Active. Day 1: The Table is Set."
 */
export interface BraidCallState {
  /** Is braid call active? */
  isActive: boolean;
  /** Call message */
  callMessage: string;
  /** Target nodes (8 London Communities) */
  targetNodes: CommunityNode[];
  /** Call status by node */
  callStatusByNode: Map<CommunityNode, 'sent' | 'delivered' | 'acknowledged' | 'failed'>;
  /** Call timestamp */
  callTimestamp: string;
  /** All nodes notified? */
  allNodesNotified: boolean;
  /** Call complete? */
  callComplete: boolean;
}

/**
 * Day 1 Initialization Final State
 * Complete Day 1 initialization state
 */
export interface Day1InitializationFinalState {
  /** Reset Stewardship Clock */
  resetStewardshipClock: ResetStewardshipClockState;
  /** Baseline Truth Establishment */
  baselineTruthEstablishment: BaselineTruthEstablishmentState;
  /** The Braid Call */
  braidCall: BraidCallState;
  /** Day 1 initialized? */
  day1Initialized: boolean;
  /** All components ready? */
  allComponentsReady: boolean;
}

/**
 * Constants
 */
export const DAY_1_INIT_CONSTANTS = {
  /** Current day (1) */
  CURRENT_DAY: 1,
  /** Total days (376) */
  TOTAL_DAYS: 376,
  /** First Loop timer duration (24 hours in seconds) */
  FIRST_LOOP_TIMER_DURATION_SECONDS: 24 * 60 * 60, // 86400 seconds
  /** Go live flag */
  GO_LIVE: true,
  /** Architecture shield active flag */
  ARCHITECTURE_SHIELD_ACTIVE: true
} as const;
