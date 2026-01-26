/** * * THE FINAL SEAL (CYCLE COMPLETION) UTILITIES
 *  * Implement Law 37 'Completion' Logic
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

import {
  WeeklyCycleValidator,
  CycleCompletionStatus,
  StewardshipSeal,
  Law37Breach,
  ImmutableTableEntry,
  WeeklyBiologicalData,
  BiologicalKeyMoment,
  HomeostasisSentinelUI,
  SystemStatus,
  CYCLE_COMPLETION_CONSTANTS
} from '../types/cycleCompletion';
import { HealthMetrics } from '../types';
import { ProtocolEvent } from '../types/stewardship';
import { EarthAlignment } from '../types/earthAlignment';
import { calculateEarthAlignment } from './earthRhythms';
import { 
  startOfWeek, 
  endOfWeek, 
  addDays, 
  format, 
  parseISO, 
  getHours, 
  getMinutes,
  isAfter,
  isBefore
} from 'date-fns';

/**
 * Check if Day 7 End (Circadian Clock Sync)
 * TRIGGER: End of Day 7 (Circadian Clock Sync)
 */
export function isDay7End(timestamp: string): boolean {
  const date = parseISO(timestamp);
  const hour = getHours(date);
  const minute = getMinutes(date);

  // Day 7 end: 23:59 (11:59 PM)
  return hour === CYCLE_COMPLETION_CONSTANTS.DAY_7_END_HOUR && 
         minute >= CYCLE_COMPLETION_CONSTANTS.DAY_7_END_MINUTE;
}

/**
 * Calculate Weekly Cycle Validator
 * Law 37: Finish What You Begin
 * 
 * ACTION: Scan all 'Active Protocols' from Day 1-6
 */
export function calculateWeeklyCycleValidator(
  weekStartDate: Date,
  allProtocolEvents: ProtocolEvent[]
): WeeklyCycleValidator {
  const weekEndDate = addDays(weekStartDate, CYCLE_COMPLETION_CONSTANTS.CYCLE_DAYS);
  const day7Timestamp = format(weekEndDate, 'yyyy-MM-dd') + `T${CYCLE_COMPLETION_CONSTANTS.DAY_7_END_HOUR}:${CYCLE_COMPLETION_CONSTANTS.DAY_7_END_MINUTE}:00`;

  // Filter protocols from Day 1-6 (excluding Day 7)
  const day1To6End = addDays(weekStartDate, 6);
  const protocolsDay1To6 = allProtocolEvents.filter(event => {
    const eventDate = parseISO(event.timestamp);
    return isAfter(eventDate, weekStartDate) && isBefore(eventDate, day1To6End);
  });

  // Analyze protocol completion
  const totalInitiated = protocolsDay1To6.filter(e => e.eventType === 'initiated').length;
  const protocolsCompleted = protocolsDay1To6.filter(e => e.eventType === 'completed' && e.law37Compliance).length;
  const protocolsAbandoned = protocolsDay1To6.filter(e => e.eventType === 'abandoned' || 
    (e.eventType === 'initiated' && !e.law37Compliance)).length;

  const completionRate = totalInitiated > 0 ? protocolsCompleted / totalInitiated : 1.0;
  const allCompleted = totalInitiated > 0 && protocolsCompleted === totalInitiated;

  // Law 37 compliance: All protocols completed
  const law37Compliance = allCompleted;

  // Determine completion status
  let completionStatus: CycleCompletionStatus;
  if (totalInitiated === 0) {
    completionStatus = 'pending';
  } else if (allCompleted) {
    completionStatus = 'completed';
  } else if (protocolsAbandoned > 0) {
    completionStatus = 'breached';
  } else {
    completionStatus = 'in_progress';
  }

  // Law 37 breach detected if not all completed
  const law37BreachDetected = !allCompleted && totalInitiated > 0;
  const seedAccessLevelsReset = law37BreachDetected;

  // Stewardship Seal v1 generated if all completed
  const stewardshipSealGenerated = allCompleted;

  return {
    isActive: isDay7End(day7Timestamp),
    completionStatus,
    weekPeriod: {
      startDate: format(weekStartDate, 'yyyy-MM-dd'),
      endDate: format(weekEndDate, 'yyyy-MM-dd'),
      day7Timestamp
    },
    protocolsDay1To6,
    protocolCompletion: {
      totalInitiated,
      protocolsCompleted,
      protocolsAbandoned,
      completionRate,
      allCompleted
    },
    stewardshipSealGenerated,
    law37BreachDetected,
    seedAccessLevelsReset,
    law37Compliance,
    ...(isDay7End(day7Timestamp) && { validatedAt: new Date().toISOString() })
  };
}

/**
 * Generate Stewardship Seal v1
 * IF (All_Protocols == 'COMPLETED'): Generate 'Stewardship_Seal_v1'
 */
export function generateStewardshipSealV1(
  weekValidator: WeeklyCycleValidator
): StewardshipSeal | null {
  if (!weekValidator.stewardshipSealGenerated || !weekValidator.law37Compliance) {
    return null;
  }

  return {
    id: `stewardship_seal_v1_${Date.now()}`,
    version: 'v1',
    generatedAt: new Date().toISOString(),
    weekPeriod: weekValidator.weekPeriod,
    law37Compliance: true,
    protocolCompletion: {
      totalInitiated: weekValidator.protocolCompletion.totalInitiated,
      protocolsCompleted: weekValidator.protocolCompletion.protocolsCompleted,
      completionRate: weekValidator.protocolCompletion.completionRate,
      allCompleted: true
    },
    message: 'Stewardship Seal v1: Law 37 Honored. All protocols completed.',
    immutable: true
  };
}

/**
 * Flag Law 37 Breach
 * ELSE Flag 'Breach of Law 37' and reset 'Seed' access levels
 */
export function flagLaw37Breach(
  weekValidator: WeeklyCycleValidator
): Law37Breach | null {
  if (!weekValidator.law37BreachDetected) {
    return null;
  }

  // Find protocols not completed
  const protocolsNotCompleted = weekValidator.protocolsDay1To6.filter(e => 
    e.eventType === 'initiated' && !e.law37Compliance
  );

  // Determine breach severity
  let severity: 'low' | 'medium' | 'high';
  const incompleteRatio = (weekValidator.protocolCompletion.totalInitiated - weekValidator.protocolCompletion.protocolsCompleted) / 
    weekValidator.protocolCompletion.totalInitiated;
  
  if (incompleteRatio > 0.5) {
    severity = 'high';
  } else if (incompleteRatio > 0.25) {
    severity = 'medium';
  } else {
    severity = 'low';
  }

  return {
    id: `law37_breach_${Date.now()}`,
    breachedAt: new Date().toISOString(),
    protocolsNotCompleted,
    severity,
    seedAccessLevelsReset: true,
    resetTimestamp: new Date().toISOString(),
    message: 'Breach of Law 37. Not all protocols completed. Seed access levels reset.',
    lawReference: 'Law 37: Finish What You Begin'
  };
}

/**
 * Aggregate Weekly Biological Data
 * Record the week's biological data (30.7s, 16.9s, 5.5s) into the Permanent Ledger
 */
export function aggregateWeeklyBiologicalData(
  metrics: HealthMetrics[],
  weekStartDate: Date
): WeeklyBiologicalData {
  const weekEndDate = addDays(weekStartDate, CYCLE_COMPLETION_CONSTANTS.CYCLE_DAYS);
  
  // Filter metrics for the week
  const weekMetrics = metrics.filter(m => {
    const metricDate = parseISO(m.date);
    return isAfter(metricDate, weekStartDate) && isBefore(metricDate, weekEndDate);
  });

  // Extract glucose readings (convert mg/dL to mmol/L if needed)
  const glucoseReadings = weekMetrics
    .filter(m => m.blood_glucose !== undefined)
    .map(m => {
      const glucose = m.blood_glucose!;
      // Convert mg/dL to mmol/L if > 30 (assuming mmol/L if <= 30)
      return glucose > 30 ? glucose / 18.0182 : glucose;
    });

  // Extract other readings
  const visionReadings = weekMetrics.filter(m => m.vision_clarity !== undefined).map(m => m.vision_clarity!);
  const muscleReadings = weekMetrics.filter(m => m.muscle_tension !== undefined).map(m => m.muscle_tension!);
  const breathReadings = weekMetrics.filter(m => m.breath_quality !== undefined).map(m => m.breath_quality!);

  // Calculate statistics
  const calculateStats = (values: number[]) => {
    if (values.length === 0) {
      return { mean: 0, min: 0, max: 0 };
    }
    return {
      mean: values.reduce((sum, val) => sum + val, 0) / values.length,
      min: Math.min(...values),
      max: Math.max(...values)
    };
  };

  const glucoseStats = {
    ...calculateStats(glucoseReadings),
    variance: glucoseReadings.length > 0 
      ? glucoseReadings.reduce((sum, val) => sum + Math.pow(val - calculateStats(glucoseReadings).mean, 2), 0) / glucoseReadings.length
      : 0
  };

  // Identify key biological moments (e.g., glucose 30.7, 16.9, 5.5)
  const keyMoments: BiologicalKeyMoment[] = [];
  
  weekMetrics.forEach(metric => {
    if (metric.blood_glucose !== undefined) {
      const glucose = metric.blood_glucose > 30 ? metric.blood_glucose / 18.0182 : metric.blood_glucose;
      
      // Mark significant glucose moments
      if (glucose > 25) {
        keyMoments.push({
          timestamp: metric.glucose_time ? `${metric.date}T${metric.glucose_time}:00` : `${metric.date}T12:00:00`,
          type: 'glucose_high',
          value: Math.round(glucose * 100) / 100,
          description: `High glucose: ${glucose.toFixed(1)} mmol/L`
        });
      } else if (glucose < 5.5) {
        keyMoments.push({
          timestamp: metric.glucose_time ? `${metric.date}T${metric.glucose_time}:00` : `${metric.date}T12:00:00`,
          type: 'glucose_low',
          value: Math.round(glucose * 100) / 100,
          description: `Low glucose: ${glucose.toFixed(1)} mmol/L`
        });
      }
    }

    if (metric.vision_clarity !== undefined && metric.vision_clarity < 4) {
      keyMoments.push({
        timestamp: metric.date,
        type: 'vision_clarity',
        value: metric.vision_clarity,
        description: `Low vision clarity: ${metric.vision_clarity}/10`
      });
    }
  });

  return {
    glucoseReadings,
    glucoseStats: {
      mean: Math.round(glucoseStats.mean * 100) / 100,
      min: Math.round(glucoseStats.min * 100) / 100,
      max: Math.round(glucoseStats.max * 100) / 100,
      variance: Math.round(glucoseStats.variance * 100) / 100
    },
    visionReadings,
    visionStats: calculateStats(visionReadings),
    muscleReadings,
    muscleStats: calculateStats(muscleReadings),
    breathReadings,
    breathStats: calculateStats(breathReadings),
    keyMoments
  };
}

/**
 * Create Immutable Table Entry
 * Record the week's biological data into the Permanent Ledger
 * Output: `system_status = 'FORTIFIED';`
 */
export function createImmutableTableEntry(
  metrics: HealthMetrics[],
  weekStartDate: Date,
  protocolEvents: ProtocolEvent[],
  earthAlignment?: EarthAlignment
): ImmutableTableEntry {
  const weekEndDate = addDays(weekStartDate, CYCLE_COMPLETION_CONSTANTS.CYCLE_DAYS);
  const weekEndTimestamp = format(weekEndDate, 'yyyy-MM-dd') + `T${CYCLE_COMPLETION_CONSTANTS.DAY_7_END_HOUR}:${CYCLE_COMPLETION_CONSTANTS.DAY_7_END_MINUTE}:00`;

  // Aggregate weekly biological data
  const biologicalData = aggregateWeeklyBiologicalData(metrics, weekStartDate);

  // Calculate Earth alignment (use week end if not provided)
  const earthAlignment_ = earthAlignment || calculateEarthAlignment(weekEndTimestamp);

  // Calculate protocol completion
  const weekValidator = calculateWeeklyCycleValidator(weekStartDate, protocolEvents);
  const totalInitiated = weekValidator.protocolCompletion.totalInitiated;
  const protocolsCompleted = weekValidator.protocolCompletion.protocolsCompleted;
  const completionRate = weekValidator.protocolCompletion.completionRate;
  const law37Compliance = weekValidator.law37Compliance;

  // Determine system status
  let systemStatus: SystemStatus;
  if (law37Compliance && totalInitiated > 0) {
    systemStatus = CYCLE_COMPLETION_CONSTANTS.SYSTEM_STATUS_FORTIFIED;
  } else if (weekValidator.law37BreachDetected) {
    systemStatus = CYCLE_COMPLETION_CONSTANTS.SYSTEM_STATUS_BREACHED;
  } else if (totalInitiated > 0) {
    systemStatus = 'IN_PROGRESS';
  } else {
    systemStatus = 'PENDING';
  }

  return {
    id: `immutable_table_${Date.now()}`,
    timestamp: new Date().toISOString(),
    weekPeriod: {
      startDate: format(weekStartDate, 'yyyy-MM-dd'),
      endDate: format(weekEndDate, 'yyyy-MM-dd')
    },
    biologicalData,
    earthAlignment: earthAlignment_,
    protocolCompletion: {
      totalInitiated,
      protocolsCompleted,
      completionRate
    },
    systemStatus,
    law37Compliance,
    immutable: true,
    storedForLordsCalling: true
  };
}

/**
 * Calculate Homeostasis Sentinel UI State
 * Display the 'Global Braid' in full color
 * Message: "Cycle 1 Complete. Law 37 Honored. The Table is set for the Lord's calling."
 */
export function calculateHomeostasisSentinelUI(
  cycleNumber: number,
  weekValidator: WeeklyCycleValidator,
  systemStatus: SystemStatus
): HomeostasisSentinelUI {
  const law37Honored = weekValidator.law37Compliance && weekValidator.stewardshipSealGenerated;
  const globalBraidDisplay = law37Honored;
  const fullColorMode = law37Honored && systemStatus === CYCLE_COMPLETION_CONSTANTS.SYSTEM_STATUS_FORTIFIED;

  let completionMessage: string;
  let theme: 'completion' | 'breach' | 'normal';

  if (law37Honored) {
    completionMessage = `Cycle ${cycleNumber} Complete. Law 37 Honored. The Table is set for the Lord's calling.`;
    theme = 'completion';
  } else if (weekValidator.law37BreachDetected) {
    completionMessage = `Cycle ${cycleNumber} Incomplete. Law 37 Breach. Return to protocols.`;
    theme = 'breach';
  } else {
    completionMessage = `Cycle ${cycleNumber} In Progress. Continue stewardship.`;
    theme = 'normal';
  }

  return {
    globalBraidDisplay,
    fullColorMode,
    completionMessage,
    cycleNumber,
    law37Honored,
    systemStatus,
    theme
  };
}

/**
 * Get System Status
 * Output: `system_status = 'FORTIFIED';`
 */
export function getSystemStatus(
  weekValidator: WeeklyCycleValidator
): SystemStatus {
  if (weekValidator.law37Compliance && weekValidator.protocolCompletion.totalInitiated > 0) {
    return CYCLE_COMPLETION_CONSTANTS.SYSTEM_STATUS_FORTIFIED;
  } else if (weekValidator.law37BreachDetected) {
    return CYCLE_COMPLETION_CONSTANTS.SYSTEM_STATUS_BREACHED;
  } else if (weekValidator.protocolCompletion.totalInitiated > 0) {
    return 'IN_PROGRESS';
  } else {
    return 'PENDING';
  }
}
