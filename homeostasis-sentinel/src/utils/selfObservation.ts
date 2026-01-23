/**
 * SELF-OBSERVATION PROTOCOL UTILITIES
 * Bridge Ouspensky's 'Work' with SIYEM Bio-Data
 * 
 * 1. Presence_Audit: Glucose delta monitoring with "Which 'I' is observing?" prompt
 * 2. The_Miraculous_Octave: Map 7 days to musical notes (Do-Re-Mi-Fa-Sol-La-Si)
 * 3. Data Protection: OBSERVER_ACTIVE and MACHINE_AUTO_PILOT constants
 */

import { HealthMetrics } from '../types';
import {
  GlucoseDelta,
  PresenceAudit,
  MiraculousOctave,
  OctaveDay,
  SelfObservationProtocol,
  ObservationRecord,
  MusicalNote,
  SELF_OBSERVATION_CONSTANTS,
  MUSICAL_NOTE_MAPPING,
  NOTE_DESCRIPTIONS,
  NOTE_INTENTS
} from '../types/selfObservation';

/**
 * Calculate Glucose Delta
 * Calculate change in glucose level between two readings
 */
export function calculateGlucoseDelta(
  previousMetric: HealthMetrics,
  currentMetric: HealthMetrics
): GlucoseDelta | null {
  const previousGlucose = previousMetric.glucose;
  const currentGlucose = currentMetric.glucose;

  if (previousGlucose === undefined || currentGlucose === undefined) {
    return null;
  }

  const previousTimestamp = previousMetric.glucose_time || previousMetric.date;
  const currentTimestamp = currentMetric.glucose_time || currentMetric.date;

  // Parse timestamps (simplified - assumes ISO format or HH:MM)
  const previousTime = new Date(previousTimestamp).getTime();
  const currentTime = new Date(currentTimestamp).getTime();
  const timeDifferenceMs = currentTime - previousTime;
  const timeDifferenceMinutes = timeDifferenceMs / (60 * 1000);

  const delta = Math.abs(currentGlucose - previousGlucose);

  return {
    previousGlucose,
    currentGlucose,
    delta,
    previousTimestamp,
    currentTimestamp,
    timeDifferenceMs,
    timeDifferenceMinutes
  };
}

/**
 * Check Presence Audit Trigger
 * Check if glucose delta > 1.0 mmol/L within 15 minutes
 */
export function checkPresenceAuditTrigger(metrics: HealthMetrics[]): PresenceAudit | null {
  if (metrics.length < 2) return null;

  // Sort metrics by timestamp (most recent first)
  const sortedMetrics = [...metrics].sort((a, b) => {
    const timeA = new Date(a.glucose_time || a.date).getTime();
    const timeB = new Date(b.glucose_time || b.date).getTime();
    return timeB - timeA;
  });

  // Check last two metrics
  const currentMetric = sortedMetrics[0];
  const previousMetric = sortedMetrics[1];

  const glucoseDelta = calculateGlucoseDelta(previousMetric, currentMetric);
  if (!glucoseDelta) return null;

  // Check trigger condition: delta > 1.0 mmol/L within 15 minutes
  const triggerConditionMet =
    glucoseDelta.delta > SELF_OBSERVATION_CONSTANTS.GLUCOSE_DELTA_THRESHOLD &&
    glucoseDelta.timeDifferenceMinutes <= SELF_OBSERVATION_CONSTANTS.DELTA_TIME_WINDOW_MINUTES;

  if (!triggerConditionMet) return null;

  // Create Presence Audit
  const auditId = `presence_audit_${Date.now()}`;
  const triggerTimestamp = new Date().toISOString();
  const notification = "The machine is shifting. Which 'I' is observing this? Record the state.";

  return {
    id: auditId,
    triggered: true,
    triggerConditionMet: true,
    glucoseDelta,
    deltaThreshold: SELF_OBSERVATION_CONSTANTS.GLUCOSE_DELTA_THRESHOLD,
    timeWindowMinutes: SELF_OBSERVATION_CONSTANTS.DELTA_TIME_WINDOW_MINUTES,
    triggerTimestamp,
    notification,
    userAcknowledgement: false
  };
}

/**
 * Create Presence Audit
 * Create a new presence audit (manual or triggered)
 */
export function createPresenceAudit(
  glucoseDelta: GlucoseDelta,
  triggered: boolean = true
): PresenceAudit {
  const auditId = `presence_audit_${Date.now()}`;
  const triggerTimestamp = new Date().toISOString();
  const notification = "The machine is shifting. Which 'I' is observing this? Record the state.";

  const triggerConditionMet =
    glucoseDelta.delta > SELF_OBSERVATION_CONSTANTS.GLUCOSE_DELTA_THRESHOLD &&
    glucoseDelta.timeDifferenceMinutes <= SELF_OBSERVATION_CONSTANTS.DELTA_TIME_WINDOW_MINUTES;

  return {
    id: auditId,
    triggered,
    triggerConditionMet,
    glucoseDelta,
    deltaThreshold: SELF_OBSERVATION_CONSTANTS.GLUCOSE_DELTA_THRESHOLD,
    timeWindowMinutes: SELF_OBSERVATION_CONSTANTS.DELTA_TIME_WINDOW_MINUTES,
    triggerTimestamp,
    notification,
    userAcknowledgement: false
  };
}

/**
 * Acknowledge Presence Audit
 * User acknowledges the presence audit
 */
export function acknowledgePresenceAudit(audit: PresenceAudit): PresenceAudit {
  return {
    ...audit,
    userAcknowledgement: true,
    acknowledgementTimestamp: new Date().toISOString()
  };
}

/**
 * Record State for Presence Audit
 * User records their observed state
 */
export function recordStateForPresenceAudit(
  audit: PresenceAudit,
  recordedState: string
): PresenceAudit {
  return {
    ...audit,
    recordedState,
    recordStateTimestamp: new Date().toISOString()
  };
}

/**
 * Create Octave Day
 * Create a single day in the Miraculous Octave
 */
export function createOctaveDay(day: number, date: string): OctaveDay {
  const note = MUSICAL_NOTE_MAPPING[day];
  const noteDescription = NOTE_DESCRIPTIONS[note];
  const noteIntent = NOTE_INTENTS[note];
  const acknowledgementRequired = day === 1; // Day 1 (Do) requires acknowledgement

  return {
    day,
    note,
    noteDescription,
    date,
    acknowledgementRequired,
    acknowledgementReceived: false
  };
}

/**
 * Create The Miraculous Octave
 * Create a 7-day octave starting from a given date
 */
export function createMiraculousOctave(startDate: string): MiraculousOctave {
  const octaveId = `octave_${Date.now()}`;
  const start = new Date(startDate);
  const end = new Date(start);
  end.setDate(end.getDate() + SELF_OBSERVATION_CONSTANTS.OCTAVE_DAYS_COUNT - 1);

  // Create all 7 days
  const days: OctaveDay[] = [];
  for (let day = 1; day <= SELF_OBSERVATION_CONSTANTS.OCTAVE_DAYS_COUNT; day++) {
    const date = new Date(start);
    date.setDate(date.getDate() + day - 1);
    days.push(createOctaveDay(day, date.toISOString().split('T')[0]));
  }

  const currentDay = 1; // Start at Day 1
  const currentNote = MUSICAL_NOTE_MAPPING[currentDay];

  return {
    id: octaveId,
    startDate: start.toISOString().split('T')[0],
    endDate: end.toISOString().split('T')[0],
    currentDay,
    currentNote,
    days,
    userAcknowledgementRequired: SELF_OBSERVATION_CONSTANTS.DAY_1_ACKNOWLEDGEMENT_REQUIRED,
    userAcknowledgementReceived: false
  };
}

/**
 * Get Current Octave Day
 * Get current day in the octave based on date
 */
export function getCurrentOctaveDay(octave: MiraculousOctave, currentDate: string): number {
  const start = new Date(octave.startDate);
  const current = new Date(currentDate);
  const daysDiff = Math.floor((current.getTime() - start.getTime()) / (24 * 60 * 60 * 1000)) + 1;

  if (daysDiff < 1) return 1;
  if (daysDiff > SELF_OBSERVATION_CONSTANTS.OCTAVE_DAYS_COUNT) return SELF_OBSERVATION_CONSTANTS.OCTAVE_DAYS_COUNT;

  return daysDiff;
}

/**
 * Update Current Octave Day
 * Update octave to current day
 */
export function updateCurrentOctaveDay(
  octave: MiraculousOctave,
  currentDate: string
): MiraculousOctave {
  const currentDay = getCurrentOctaveDay(octave, currentDate);
  const currentNote = MUSICAL_NOTE_MAPPING[currentDay];

  return {
    ...octave,
    currentDay,
    currentNote
  };
}

/**
 * Acknowledge Octave Day
 * User acknowledges Day 1 (Do) or any day
 */
export function acknowledgeOctaveDay(
  octave: MiraculousOctave,
  day: number
): MiraculousOctave {
  const updatedDays = octave.days.map(d =>
    d.day === day
      ? {
          ...d,
          acknowledgementReceived: true,
          acknowledgementTimestamp: new Date().toISOString()
        }
      : d
  );

  const day1Acknowledged = updatedDays.find(d => d.day === 1)?.acknowledgementReceived || false;

  return {
    ...octave,
    days: updatedDays,
    userAcknowledgementReceived: day === 1 ? day1Acknowledged : octave.userAcknowledgementReceived,
    acknowledgementTimestamp: day === 1 ? new Date().toISOString() : octave.acknowledgementTimestamp
  };
}

/**
 * Create Observation Record
 * Create a record of an observation
 */
export function createObservationRecord(
  type: ObservationRecord['type'],
  observingI: string,
  recordedState: string,
  presenceAuditId?: string,
  octaveDay?: number,
  octaveNote?: MusicalNote
): ObservationRecord {
  const recordId = `observation_record_${Date.now()}`;
  const timestamp = new Date().toISOString();

  return {
    id: recordId,
    type,
    timestamp,
    observingI,
    recordedState,
    presenceAuditId,
    octaveDay,
    octaveNote
  };
}

/**
 * Create Self-Observation Protocol
 * Initialize complete self-observation system
 */
export function createSelfObservationProtocol(
  startDate?: string
): SelfObservationProtocol {
  const initialOctave = startDate ? createMiraculousOctave(startDate) : null;

  return {
    active: true,
    presenceAudit: null,
    miraculousOctave: initialOctave,
    observerActive: SELF_OBSERVATION_CONSTANTS.OBSERVER_ACTIVE,
    machineAutoPilot: SELF_OBSERVATION_CONSTANTS.MACHINE_AUTO_PILOT,
    lastObservationTimestamp: new Date().toISOString(),
    observationHistory: []
  };
}

/**
 * Add Observation Record
 * Add a new observation record to history
 */
export function addObservationRecord(
  protocol: SelfObservationProtocol,
  record: ObservationRecord
): SelfObservationProtocol {
  return {
    ...protocol,
    observationHistory: [...protocol.observationHistory, record],
    lastObservationTimestamp: record.timestamp
  };
}

/**
 * Constants Export
 */
export const OBSERVER_ACTIVE = SELF_OBSERVATION_CONSTANTS.OBSERVER_ACTIVE;
export const MACHINE_AUTO_PILOT = SELF_OBSERVATION_CONSTANTS.MACHINE_AUTO_PILOT;
