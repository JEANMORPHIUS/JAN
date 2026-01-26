/** * * WAR MODE & INTEGRITY TRACKING UTILITIES
 *  * Implement Law 31 and Law 5 into the Sentinel's Logic
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
 * PANGEA IS THE TABLE.
 * YOU DON'T BETRAY THE TABLE.
 * 
 * THE TRUTH:
 * WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
 * THE REST IS UP TO BABA X.*/

import {
  KarasahinWarMode,
  WarModeStatus,
  DefenseCondition,
  PierreIntegrityCheck,
  WordIsBondState,
  IntegrityViolation,
  CommitmentConsistency,
  WAR_MODE_CONSTANTS
} from '../types/warMode';
import { HealthMetrics } from '../types';
import { ProtocolEvent } from '../types/stewardship';
import { addMilliseconds, isAfter, parseISO } from 'date-fns';

/**
 * Convert mg/dL to mmol/L
 */
function mgdLToMmol(mgdL: number): number {
  return mgdL / 18.0182;
}

/**
 * Calculate Karasahin War Mode
 * Law 31: Defending the Temple
 * 
 * TRIGGER: Glucose > 25.0 mmol/L AND (Vision_Clarity < 0.5 OR Ketones_Detected == TRUE)
 */
export function calculateKarasahinWarMode(
  metrics: HealthMetrics[],
  glucoseThreshold: number = WAR_MODE_CONSTANTS.WAR_MODE_GLUCOSE_THRESHOLD,
  visionThreshold: number = WAR_MODE_CONSTANTS.WAR_MODE_VISION_THRESHOLD
): KarasahinWarMode {
  const latest = metrics[metrics.length - 1];
  
  // Convert glucose to mmol/L if needed (assume mg/dL if > 30)
  const glucose = latest.blood_glucose 
    ? (latest.blood_glucose > 30 ? mgdLToMmol(latest.blood_glucose) : latest.blood_glucose)
    : 0;
  
  const visionClarity = latest.vision_clarity ?? 10;
  const ketones = latest.ketones ?? 0;

  // Check trigger conditions
  const highGlucose = glucose > glucoseThreshold;
  const lowVision = visionClarity < visionThreshold;
  const ketonesDetected = ketones > 0;

  // War Mode active if: Glucose > 25.0 AND (Vision < 0.5 OR Ketones detected)
  const isActive = highGlucose && (lowVision || ketonesDetected);

  // Determine war status
  let warStatus: WarModeStatus = 'inactive';
  if (isActive) {
    if (glucose > 30 || visionClarity < 0.3 || ketones > 3) {
      warStatus = 'critical';
    } else {
      warStatus = 'war';
    }
  } else if (glucose > 20 || visionClarity < 2) {
    warStatus = 'alert';
  }

  // Calculate defense condition
  const defenseCondition = getDefenseCondition(metrics);

  // UI state
  const uiState = {
    redShiftActive: isActive,
    loopRecoveryActive: isActive,
    redShiftIntensity: isActive ? WAR_MODE_CONSTANTS.WAR_MODE_RED_SHIFT_INTENSITY : 0
  };

  // Notification override (High-Alert Seed Command)
  const seedCommand = isActive
    ? 'LAW 31 ACTIVE. TEMPLE DEFENSE REQUIRED. AGGRESSIVE LOOP RECOVERY INITIATED. RETURN TO BIOLOGICAL TRUTH.'
    : '';

  return {
    isActive,
    warStatus,
    triggers: {
      highGlucose,
      lowVision,
      ketonesDetected
    },
    triggerValues: {
      glucose: Math.round(glucose * 100) / 100,
      visionClarity: Math.round(visionClarity * 100) / 100,
      ketones: Math.round(ketones * 100) / 100
    },
    uiState,
    notificationOverride: {
      overrideActive: isActive,
      seedCommand
    },
    logMessage: isActive
      ? 'Law 31 Active. Defending the Temple.'
      : 'War Mode inactive. Normal operation.',
    lawReference: 'Law 31: Finish What You Begin. Protect What Is Yours.',
    ...(isActive && { activatedAt: new Date().toISOString() }),
    defenseCondition
  };
}

/**
 * Get Defense Condition
 * `let war_status = getDefenseCondition(bio_data);`
 */
export function getDefenseCondition(metrics: HealthMetrics[]): DefenseCondition {
  const latest = metrics[metrics.length - 1];
  
  // Convert glucose to mmol/L if needed
  const glucose = latest.blood_glucose 
    ? (latest.blood_glucose > 30 ? mgdLToMmol(latest.blood_glucose) : latest.blood_glucose)
    : 0;
  
  const visionClarity = latest.vision_clarity ?? 10;
  const muscleTension = latest.muscle_tension ?? 0;
  const ketones = latest.ketones ?? 0;

  // Calculate defense level (0-100, higher = better defense)
  let defenseLevel = 100;
  
  // Penalties
  if (glucose > 25) defenseLevel -= 30;
  else if (glucose > 20) defenseLevel -= 15;
  
  if (visionClarity < 0.5) defenseLevel -= 40;
  else if (visionClarity < 2) defenseLevel -= 20;
  
  if (muscleTension > 8) defenseLevel -= 20;
  else if (muscleTension > 6) defenseLevel -= 10;
  
  if (ketones > 3) defenseLevel -= 30;
  else if (ketones > 1) defenseLevel -= 15;

  defenseLevel = Math.max(0, Math.min(100, defenseLevel));

  // Determine defense status
  let defenseStatus: 'secure' | 'breached' | 'critical';
  if (defenseLevel >= 70) {
    defenseStatus = 'secure';
  } else if (defenseLevel >= 40) {
    defenseStatus = 'breached';
  } else {
    defenseStatus = 'critical';
  }

  // Required actions
  const requiredActions: string[] = [];
  if (glucose > 25 || visionClarity < 0.5 || ketones > 3) {
    requiredActions.push('Immediate Loop Recovery');
    requiredActions.push('Temple Defense Protocol');
  }
  if (muscleTension > 8) {
    requiredActions.push('Mechanical Clearance Required');
  }
  if (ketones > 3) {
    requiredActions.push('Acidosis Intervention Required');
  }

  return {
    defenseLevel,
    defenseStatus,
    biologicalState: {
      glucose: Math.round(glucose * 100) / 100,
      visionClarity: Math.round(visionClarity * 100) / 100,
      muscleTension: Math.round(muscleTension * 100) / 100,
      ketones: Math.round(ketones * 100) / 100
    },
    requiredActions
  };
}

/**
 * Calculate Discrepancy Percentage
 * Between manual input and sensor reality
 */
function calculateDiscrepancyPercentage(
  manualValue: number | undefined,
  sensorValue: number | undefined
): number {
  if (manualValue === undefined || sensorValue === undefined) {
    return 0;
  }

  if (manualValue === 0 || sensorValue === 0) {
    return Math.abs(manualValue - sensorValue) > 0 ? 100 : 0;
  }

  const discrepancy = Math.abs(manualValue - sensorValue);
  const average = (manualValue + sensorValue) / 2;
  const percentage = average > 0 ? (discrepancy / average) * 100 : 0;

  return Math.round(percentage * 100) / 100;
}

/**
 * Calculate Pierre Integrity Check
 * Law 5: Your Word Is Your Bond
 * 
 * TRIGGER: Discrepancy between 'Manual_Input' and 'Sensor_Reality' > 15%
 */
export function calculatePierreIntegrityCheck(
  manualInput: { glucose?: number; visionClarity?: number; muscleTension?: number; timestamp: string },
  sensorReality: { glucose?: number; visionClarity?: number; muscleTension?: number; timestamp: string },
  discrepancyThreshold: number = WAR_MODE_CONSTANTS.INTEGRITY_DISCREPANCY_THRESHOLD
): PierreIntegrityCheck {
  // Calculate discrepancies for each metric
  const glucoseDiscrepancy = calculateDiscrepancyPercentage(manualInput.glucose, sensorReality.glucose);
  const visionDiscrepancy = calculateDiscrepancyPercentage(manualInput.visionClarity, sensorReality.visionClarity);
  const muscleDiscrepancy = calculateDiscrepancyPercentage(manualInput.muscleTension, sensorReality.muscleTension);

  // Maximum discrepancy
  const maxDiscrepancy = Math.max(glucoseDiscrepancy, visionDiscrepancy, muscleDiscrepancy);

  const discrepancyDetected = maxDiscrepancy > discrepancyThreshold;
  const biologicalBreachFlagged = discrepancyDetected;

  // Lock stewardship progression for 24 hours if breach detected
  const stewardshipProgressionLocked = discrepancyDetected;
  const lockExpirationTimestamp = discrepancyDetected
    ? addMilliseconds(new Date(), WAR_MODE_CONSTANTS.STEWARDSHIP_LOCK_DURATION).toISOString()
    : undefined;

  return {
    isActive: discrepancyDetected,
    discrepancyDetected,
    discrepancyPercentage: maxDiscrepancy,
    discrepancyThreshold,
    manualInput,
    sensorReality,
    biologicalBreachFlagged,
    stewardshipProgressionLocked,
    lockExpirationTimestamp,
    message: discrepancyDetected
      ? 'Law 5 Violation. Your word and your biology are out of sync. Recalibrate.'
      : 'Integrity Check passed. Manual input and sensor reality aligned.',
    lawReference: 'Law 5: Your Word Is Your Bond',
    ...(discrepancyDetected && { violatedAt: new Date().toISOString() })
  };
}

/**
 * Check Commitment Consistency
 * `const WORD_IS_BOND = checkCommitmentConsistency();`
 */
export function checkCommitmentConsistency(
  protocolEvents: ProtocolEvent[]
): WordIsBondState {
  const commitmentsMade = protocolEvents.filter(e => e.eventType === 'initiated').length;
  const commitmentsHonored = protocolEvents.filter(e => e.eventType === 'completed' && e.law5Compliance).length;
  const commitmentsViolated = protocolEvents.filter(e => 
    (e.eventType === 'initiated' && !e.law37Compliance) ||
    !e.law5Compliance
  ).length;

  const honorRate = commitmentsMade > 0 
    ? commitmentsHonored / commitmentsMade 
    : 1.0;

  // Consistency score (0-100)
  const consistencyScore = honorRate * 100;

  // Law 5 compliance: Honor rate >= 0.8 (80%)
  const law5Compliance = honorRate >= 0.8;

  // Collect violations
  const violations: IntegrityViolation[] = [];
  protocolEvents.forEach(event => {
    if (!event.law5Compliance || (event.eventType === 'initiated' && !event.law37Compliance)) {
      violations.push({
        id: `violation_${event.timestamp}_${Date.now()}`,
        type: event.eventType === 'initiated' && !event.law37Compliance 
          ? 'commitment_unfulfilled' 
          : 'biological_breach',
        description: `Protocol ${event.protocolType} commitment not honored. Law 5 violation.`,
        timestamp: event.timestamp,
        resolved: false
      });
    }
  });

  return {
    isConsistent: law5Compliance,
    consistencyScore: Math.round(consistencyScore * 100) / 100,
    commitmentsMade,
    commitmentsHonored,
    commitmentsViolated,
    honorRate: Math.round(honorRate * 1000) / 1000,
    violations,
    law5Compliance
  };
}

/**
 * Calculate Complete Commitment Consistency
 */
export function calculateCommitmentConsistency(
  protocolEvents: ProtocolEvent[],
  integrityCheck?: PierreIntegrityCheck
): CommitmentConsistency {
  const wordIsBond = checkCommitmentConsistency(protocolEvents);

  // If integrity check provided and active, factor it into overall consistency
  let overallConsistency = wordIsBond.consistencyScore;
  
  if (integrityCheck?.isActive) {
    // Penalty for integrity breach: -30 points
    overallConsistency = Math.max(0, overallConsistency - 30);
  }

  // Overall Law 5 compliance: Both Word Is Bond AND Integrity Check pass
  const law5Compliance = wordIsBond.law5Compliance && !integrityCheck?.isActive;

  return {
    wordIsBond,
    integrityCheck: integrityCheck || {
      isActive: false,
      discrepancyDetected: false,
      discrepancyPercentage: 0,
      discrepancyThreshold: WAR_MODE_CONSTANTS.INTEGRITY_DISCREPANCY_THRESHOLD,
      manualInput: { timestamp: new Date().toISOString() },
      sensorReality: { timestamp: new Date().toISOString() },
      biologicalBreachFlagged: false,
      stewardshipProgressionLocked: false,
      message: 'Integrity Check inactive.',
      lawReference: 'Law 5: Your Word Is Your Bond'
    },
    overallConsistency: Math.round(overallConsistency * 100) / 100,
    law5Compliance
  };
}

/**
 * Get War Status
 * `let war_status = getDefenseCondition(bio_data);`
 */
export function getWarStatus(metrics: HealthMetrics[]): WarModeStatus {
  const warMode = calculateKarasahinWarMode(metrics);
  return warMode.warStatus;
}

/**
 * Get Word Is Bond Constant
 * `const WORD_IS_BOND = checkCommitmentConsistency();`
 */
export function getWordIsBond(protocolEvents: ProtocolEvent[]): boolean {
  const wordIsBond = checkCommitmentConsistency(protocolEvents);
  return wordIsBond.law5Compliance;
}
