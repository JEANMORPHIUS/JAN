/** * * SELF-OBSERVATION PROTOCOL TYPES
 *  * Bridge Ouspensky's 'Work' with SIYEM Bio-Data
 *  * 
 *  * 1. Presence_Audit: Glucose delta monitoring with "Which 'I' is observing?" prompt
 *  * 2. The_Miraculous_Octave: Map 7 days to musical notes (Do-Re-Mi-Fa-Sol-La-Si)
 *  * 3. Data Protection: OBSERVER_ACTIVE and MACHINE_AUTO_PILOT constants
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

import { HealthMetrics } from './index';

/**
 * Musical Note
 * The seven notes of the octave
 */
export type MusicalNote = 'Do' | 'Re' | 'Mi' | 'Fa' | 'Sol' | 'La' | 'Si';

/**
 * Glucose Delta
 * Change in glucose level over time
 */
export interface GlucoseDelta {
  /** Previous glucose value (mmol/L) */
  previousGlucose: number;
  /** Current glucose value (mmol/L) */
  currentGlucose: number;
  /** Delta value (mmol/L) */
  delta: number;
  /** Previous timestamp */
  previousTimestamp: string;
  /** Current timestamp */
  currentTimestamp: string;
  /** Time difference in milliseconds */
  timeDifferenceMs: number;
  /** Time difference in minutes */
  timeDifferenceMinutes: number;
}

/**
 * Presence Audit State
 * Trigger when glucose delta > 1.0 mmol/L within 15 minutes
 */
export interface PresenceAudit {
  /** Audit ID */
  id: string;
  /** Audit triggered? */
  triggered: boolean;
  /** Trigger condition met? */
  triggerConditionMet: boolean;
  /** Glucose delta */
  glucoseDelta: GlucoseDelta;
  /** Delta threshold (1.0 mmol/L) */
  deltaThreshold: number;
  /** Time window (15 minutes) */
  timeWindowMinutes: number;
  /** Timestamp when audit was triggered */
  triggerTimestamp: string;
  /** The notification dispatched */
  notification: string; // "The machine is shifting. Which 'I' is observing this? Record the state."
  /** User acknowledgement */
  userAcknowledgement: boolean;
  /** Acknowledgement timestamp */
  acknowledgementTimestamp?: string;
  /** User's recorded state */
  recordedState?: string;
  /** Record state timestamp */
  recordStateTimestamp?: string;
}

/**
 * The Miraculous Octave
 * Map 7 days to musical notes (Do-Re-Mi-Fa-Sol-La-Si)
 */
export interface MiraculousOctave {
  /** Octave ID */
  id: string;
  /** Start date of octave */
  startDate: string;
  /** End date of octave (7 days from start) */
  endDate: string;
  /** Current day (1-7) */
  currentDay: number;
  /** Current note */
  currentNote: MusicalNote;
  /** Days mapped to notes */
  days: OctaveDay[];
  /** User acknowledgement required for Day 1 (Do) */
  userAcknowledgementRequired: boolean;
  /** User acknowledgement received? */
  userAcknowledgementReceived: boolean;
  /** Acknowledgement timestamp */
  acknowledgementTimestamp?: string;
}

/**
 * Octave Day
 * Single day in the Miraculous Octave
 */
export interface OctaveDay {
  /** Day number (1-7) */
  day: number;
  /** Musical note */
  note: MusicalNote;
  /** Note description */
  noteDescription: string;
  /** Date */
  date: string;
  /** User acknowledgement required? */
  acknowledgementRequired: boolean;
  /** User acknowledgement received? */
  acknowledgementReceived: boolean;
  /** Acknowledgement timestamp */
  acknowledgementTimestamp?: string;
  /** Note intent/meaning */
  noteIntent: string;
}

/**
 * Self-Observation Protocol State
 * Complete self-observation system state
 */
export interface SelfObservationProtocol {
  /** Protocol active? */
  active: boolean;
  /** Presence audit state */
  presenceAudit: PresenceAudit | null;
  /** The Miraculous Octave state */
  miraculousOctave: MiraculousOctave | null;
  /** Observer active? */
  observerActive: boolean;
  /** Machine auto-pilot? */
  machineAutoPilot: boolean;
  /** Last observation timestamp */
  lastObservationTimestamp: string;
  /** Observation history */
  observationHistory: ObservationRecord[];
}

/**
 * Observation Record
 * Single observation record
 */
export interface ObservationRecord {
  /** Record ID */
  id: string;
  /** Record type */
  type: 'presence_audit' | 'octave_day' | 'manual_observation';
  /** Timestamp */
  timestamp: string;
  /** Which 'I' was observing? */
  observingI: string;
  /** Recorded state */
  recordedState: string;
  /** Presence audit reference (if applicable) */
  presenceAuditId?: string;
  /** Octave day reference (if applicable) */
  octaveDay?: number;
  /** Octave note reference (if applicable) */
  octaveNote?: MusicalNote;
}

/**
 * Constants
 */
export const SELF_OBSERVATION_CONSTANTS = {
  /** Observer active */
  OBSERVER_ACTIVE: true,
  /** Machine auto-pilot */
  MACHINE_AUTO_PILOT: false,
  /** Glucose delta threshold (1.0 mmol/L) */
  GLUCOSE_DELTA_THRESHOLD: 1.0,
  /** Time window for delta check (15 minutes) */
  DELTA_TIME_WINDOW_MINUTES: 15,
  /** Delta time window in milliseconds */
  DELTA_TIME_WINDOW_MS: 15 * 60 * 1000,
  /** Octave days count (7) */
  OCTAVE_DAYS_COUNT: 7,
  /** Day 1 note (Do) */
  DAY_1_NOTE: 'Do' as MusicalNote,
  /** User acknowledgement required for Day 1 */
  DAY_1_ACKNOWLEDGEMENT_REQUIRED: true
} as const;

/**
 * Musical Note Mapping
 * Map day numbers to musical notes
 */
export const MUSICAL_NOTE_MAPPING: Record<number, MusicalNote> = {
  1: 'Do',
  2: 'Re',
  3: 'Mi',
  4: 'Fa',
  5: 'Sol',
  6: 'La',
  7: 'Si'
};

/**
 * Note Descriptions
 * Meaning of each note in the octave
 */
export const NOTE_DESCRIPTIONS: Record<MusicalNote, string> = {
  Do: 'The Note of Intent',
  Re: 'The Note of Response',
  Mi: 'The Note of Movement',
  Fa: 'The Note of Force',
  Sol: 'The Note of Solution',
  La: 'The Note of Labor',
  Si: 'The Note of Synthesis'
};

/**
 * Note Intents
 * Intent/meaning of each note
 */
export const NOTE_INTENTS: Record<MusicalNote, string> = {
  Do: 'Day 1 (Do): The Note of Intent. Set your intention. What do you observe?',
  Re: 'Day 2 (Re): The Note of Response. Observe your response to Day 1.',
  Mi: 'Day 3 (Mi): The Note of Movement. Observe movement in your observation.',
  Fa: 'Day 4 (Fa): The Note of Force. Observe the force that moves you.',
  Sol: 'Day 5 (Sol): The Note of Solution. Observe solutions emerging.',
  La: 'Day 6 (La): The Note of Labor. Observe the work being done.',
  Si: 'Day 7 (Si): The Note of Synthesis. Observe the synthesis of the week.'
};
