/**
 * INITIALIZE DAY 1 OF 376 UTILITIES
 * Establish the Baseline for the Sovereign Stewardship
 */

import {
  ResetStewardshipClockState,
  BaselineTruthEstablishmentState,
  FoundationValue,
  BraidCallState,
  Day1InitializationFinalState,
  DAY_1_INIT_CONSTANTS
} from '../types/day1Init';
import { HealthMetrics } from '../types';
import { CommunityNode, LONDON_COMMUNITIES } from '../types/expansionPhase';
import { addSeconds, format, differenceInSeconds, parseISO } from 'date-fns';

/**
 * Calculate Reset Stewardship Clock State
 * Set `current_day` based on first glucose reading date
 * If firstReadingTimestamp is provided, calculate days since first reading
 * If not provided, assumes startTimestamp is Day 1
 */
export function calculateResetStewardshipClockState(
  startTimestamp: string,
  firstReadingTimestamp?: string
): ResetStewardshipClockState {
  const totalDays = DAY_1_INIT_CONSTANTS.TOTAL_DAYS;
  
  // If first reading timestamp provided, use it as Day 1; otherwise use startTimestamp
  const day1StartTimestamp = firstReadingTimestamp || startTimestamp;
  const day1StartDate = new Date(day1StartTimestamp);
  
  // Calculate current day based on days since Day 1
  const now = new Date();
  const daysSinceDay1 = Math.floor(
    differenceInSeconds(now, day1StartDate) / (24 * 60 * 60)
  );
  const currentDay = Math.max(1, Math.min(daysSinceDay1 + 1, totalDays));

  // First Loop timer: 24 hours from Day 1 start
  const firstLoopTimerStartTimestamp = day1StartTimestamp;
  const firstLoopTimerEndTimestamp = addSeconds(
    day1StartDate,
    DAY_1_INIT_CONSTANTS.FIRST_LOOP_TIMER_DURATION_SECONDS
  ).toISOString();

  // Calculate remaining time (if still on Day 1)
  const now = new Date();
  const endDate = new Date(firstLoopTimerEndTimestamp);
  const remainingSeconds = currentDay === 1 
    ? Math.max(0, differenceInSeconds(endDate, now))
    : 0;
  
  const firstLoopTimerActive = remainingSeconds > 0;
  const firstLoopCompleted = !firstLoopTimerActive;

  // Determine clock status
  let clockStatus: 'reset' | 'running' | 'paused' | 'completed';
  if (firstLoopCompleted) {
    clockStatus = 'completed';
  } else if (firstLoopTimerActive) {
    clockStatus = 'running';
  } else {
    clockStatus = 'reset';
  }

  return {
    isReset: true,
    currentDay,
    totalDays,
    day1StartTimestamp,
    firstLoopTimerStartTimestamp,
    firstLoopTimerEndTimestamp: format(endDate, 'yyyy-MM-dd HH:mm:ss'),
    firstLoopTimerRemaining: remainingSeconds,
    firstLoopTimerActive,
    firstLoopCompleted,
    clockStatus
  };
}

/**
 * Calculate Baseline Truth Establishment State
 * Record the first `glucose_reading` as the 'Foundation Value'
 * IF (Manual_Override == TRUE): THEN Flag 'Law 13' (Listen) to remind the user to trust the loop
 * 
 * Note: The first reading in the metrics array should be the earliest glucose reading
 * This establishes Day 1 as the date of the first reading, not today
 */
export function calculateBaselineTruthEstablishmentState(
  firstGlucoseReading: HealthMetrics
): BaselineTruthEstablishmentState {
  // Extract first glucose reading
  const glucoseValue = firstGlucoseReading.blood_glucose !== undefined
    ? (firstGlucoseReading.blood_glucose > 30 
        ? firstGlucoseReading.blood_glucose / 18.0182 
        : firstGlucoseReading.blood_glucose)
    : 0;

  // Determine reading source (simplified - would check actual source)
  const isManualOverride = firstGlucoseReading.blood_glucose !== undefined && 
    firstGlucoseReading.glucose_time === undefined; // Simplified check

  const readingSource: 'sensor' | 'manual' | 'hybrid' = isManualOverride 
    ? 'manual' 
    : 'sensor';

  // Create Foundation Value
  const foundationValue: FoundationValue = {
    glucoseValue: Math.round(glucoseValue * 100) / 100,
    glucoseUnit: 'mmol/L',
    readingTimestamp: firstGlucoseReading.date + (firstGlucoseReading.glucose_time ? `T${firstGlucoseReading.glucose_time}:00` : 'T12:00:00'),
    readingSource,
    isManualOverride,
    immutable: true
  };

  // Flag Law 13 if manual override detected
  const manualOverrideDetected = isManualOverride;
  const law13Flagged = manualOverrideDetected;

  let law13Message: string | undefined;
  if (law13Flagged) {
    law13Message = "Law 13 Active. Listen. Trust the loop. The sensor is the truth. Manual override detected. Return to biological reality.";
  }

  const isBaselineEstablished = foundationValue.glucoseValue > 0;

  // Use first reading timestamp as baseline (not today)
  const baselineTimestamp = foundationValue.readingTimestamp || new Date().toISOString();

  return {
    isBaselineEstablished,
    foundationValue,
    manualOverrideDetected,
    law13Flagged,
    law13Message,
    baselineTimestamp
  };
}

/**
 * Calculate The Braid Call State
 * Alert the 8 London Nodes: "The Sentinel is Active. Day 1: The Table is Set."
 */
export function calculateBraidCallState(
  targetNodes?: CommunityNode[]
): BraidCallState {
  const nodes = targetNodes || LONDON_COMMUNITIES;
  const callMessage = "The Sentinel is Active. Day 1: The Table is Set.";

  // Initialize call status for all nodes (all start as 'sent')
  const callStatusByNode = new Map<CommunityNode, 'sent' | 'delivered' | 'acknowledged' | 'failed'>();
  nodes.forEach(node => {
    callStatusByNode.set(node, 'sent'); // Simplified - would check actual delivery
  });

  // All nodes notified if all statuses are at least 'sent'
  const allNodesNotified = Array.from(callStatusByNode.values()).every(
    status => status === 'sent' || status === 'delivered' || status === 'acknowledged'
  );

  // Call complete if all nodes acknowledged
  const callComplete = Array.from(callStatusByNode.values()).every(
    status => status === 'acknowledged'
  );

  return {
    isActive: true,
    callMessage,
    targetNodes: nodes,
    callStatusByNode,
    callTimestamp: new Date().toISOString(),
    allNodesNotified,
    callComplete
  };
}

/**
 * Calculate Day 1 Initialization Final State
 * Complete Day 1 initialization state
 */
export function calculateDay1InitializationFinalState(
  resetStewardshipClock: ResetStewardshipClockState,
  baselineTruthEstablishment: BaselineTruthEstablishmentState,
  braidCall: BraidCallState
): Day1InitializationFinalState {
  const day1Initialized = resetStewardshipClock.isReset &&
    baselineTruthEstablishment.isBaselineEstablished &&
    braidCall.isActive;

  const allComponentsReady = resetStewardshipClock.clockStatus === 'running' &&
    baselineTruthEstablishment.isBaselineEstablished &&
    braidCall.allNodesNotified;

  return {
    resetStewardshipClock,
    baselineTruthEstablishment,
    braidCall,
    day1Initialized,
    allComponentsReady
  };
}

/**
 * Get Go Live Constant
 * `const GO_LIVE = true;`
 */
export function getGoLive(): boolean {
  return DAY_1_INIT_CONSTANTS.GO_LIVE;
}

/**
 * Get Architecture Shield Active Constant
 * `const ARCHITECTURE_SHIELD_ACTIVE = true;`
 */
export function getArchitectureShieldActive(): boolean {
  return DAY_1_INIT_CONSTANTS.ARCHITECTURE_SHIELD_ACTIVE;
}
