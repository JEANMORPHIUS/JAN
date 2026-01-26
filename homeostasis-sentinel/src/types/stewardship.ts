/** * * STEWARDSHIP TYPES
 *  * The Body as Temple. Earth as System.
 *  * 
 *  * Stewardship-focused naming convention:
 *  * - stewardship_level (not user_compliance)
 *  * - temple_state (not health_status)
 *  * - biological_stewardship (not self_care)
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

import { EarthAlignment, LoopEarthAlignment, OriginalErrorFlag } from './earthAlignment';

/**
 * Biological Stewardship Metrics
 * The body is a temple - stewarded, not exploited
 */
export interface BiologicalStewardship {
  /** Temple state: 'optimal' | 'stable' | 'attention' | 'crisis' */
  templeState: TempleState;
  /** Stewardship level (0-100): How well is the temple being stewarded? */
  stewardshipLevel: number;
  /** Biological truth: Current state of the temple */
  biologicalTruth: BiologicalTruth;
  /** Original Error interference flags */
  originalErrors: OriginalErrorFlag[];
  /** Earth alignment: Symbiotic relationship status */
  earthAlignment: EarthAlignment;
}

export type TempleState = 'optimal' | 'stable' | 'attention' | 'crisis';

export interface BiologicalTruth {
  /** Glucose truth (mmol/L) - The table never lies */
  glucose: {
    value: number;
    unit: 'mmol/L' | 'mg/dL';
    timestamp: string;
    /** Is this reading influenced by Original Error (sensor error, etc)? */
    originalErrorFlag: boolean;
  };
  /** Vision clarity truth (1-10) */
  visionClarity: {
    value: number;
    timestamp: string;
    /** Is this reading influenced by Original Error? */
    originalErrorFlag: boolean;
  };
  /** Muscle tension truth (1-10) */
  muscleTension: {
    value: number;
    timestamp: string;
    /** Is this reading influenced by Original Error? */
    originalErrorFlag: boolean;
  };
  /** Breath quality truth (1-10) */
  breathQuality: {
    value: number;
    timestamp: string;
    /** Is this reading influenced by Original Error? */
    originalErrorFlag: boolean;
  };
}

/**
 * Protocol Stewardship
 * Law 5: Your Word Is Your Bond
 * Law 37: Finish What You Begin
 */
export interface ProtocolStewardship {
  /** Protocol adherence: Commitment to protocol (0-100) */
  protocolCommitment: number;
  /** Active protocols */
  activeProtocols: ActiveProtocol[];
  /** Protocol completion status (Law 37) */
  completionStatus: ProtocolCompletionStatus;
  /** Protocol tracking: All protocol events (Law 5) */
  protocolTracking: ProtocolEvent[];
}

export interface ActiveProtocol {
  /** Protocol name/type */
  protocolType: ProtocolType;
  /** Start time */
  startTime: string;
  /** Expected completion time */
  expectedCompletion: string;
  /** Status: 'initiated' | 'in_progress' | 'completed' | 'abandoned' */
  status: ProtocolStatus;
  /** Commitment level (Law 5: Your Word Is Your Bond) */
  commitmentLevel: number;
}

export type ProtocolType = 
  | 'insulin_bolus'
  | 'loop_reintegration'
  | 'water_flush'
  | 'mechanical_clearance'
  | 'medication_cycle'
  | 'circadian_alignment';

export type ProtocolStatus = 'initiated' | 'in_progress' | 'completed' | 'abandoned';

export interface ProtocolEvent {
  /** Event timestamp */
  timestamp: string;
  /** Protocol type */
  protocolType: ProtocolType;
  /** Event type: 'initiated' | 'progress' | 'completed' | 'abandoned' */
  eventType: ProtocolEventType;
  /** Details of event */
  details: string;
  /** Law 5 compliance: Was commitment honored? */
  law5Compliance: boolean;
  /** Law 37 compliance: Was protocol completed? */
  law37Compliance: boolean;
}

export type ProtocolEventType = 'initiated' | 'progress' | 'completed' | 'abandoned';

export interface ProtocolCompletionStatus {
  /** Total protocols initiated */
  totalInitiated: number;
  /** Protocols completed (Law 37) */
  protocolsCompleted: number;
  /** Protocols abandoned */
  protocolsAbandoned: number;
  /** Completion rate (0-100) */
  completionRate: number;
  /** Law 37 adherence: Finish what you begin */
  law37Adherence: number;
}

/**
 * Integrated Stewardship Architecture
 * Mission + Laws + Biology + Earth
 */
export interface IntegratedStewardship {
  /** Biological stewardship: The body as temple */
  biological: BiologicalStewardship;
  /** Protocol stewardship: Law 5 & Law 37 compliance */
  protocol: ProtocolStewardship;
  /** Earth stewardship: Symbiotic relationship */
  earth: LoopEarthAlignment;
  /** Overall stewardship score (0-100) */
  overallStewardshipScore: number;
  /** Readiness: Ready when people come calling? */
  readiness: ReadinessStatus;
}

export interface ReadinessStatus {
  /** Systems ready? */
  systemsReady: boolean;
  /** Knowledge accessible? */
  knowledgeReady: boolean;
  /** Infrastructure prepared? */
  infrastructureReady: boolean;
  /** Stewardship complete? */
  stewardshipComplete: boolean;
  /** Overall readiness score (0-100) */
  readinessScore: number;
}
