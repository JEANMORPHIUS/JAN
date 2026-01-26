/** * * STATEMENT OF TRUTH TYPES
 *  * The First Entry - Day 1 (Do) - The Note of Intent
 *  * 
 *  * To seal the start of the 376-day count, we need the first "Statement of Truth."
 *  * This is the foundation - immutable, sacred, and recorded in the Ledger.
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

/**
 * Statement of Truth
 * The foundational entry that begins the 376-day journey
 */
export interface StatementOfTruth {
  /** Statement ID (unique, immutable) */
  id: string;
  /** Statement type */
  type: 'first_entry' | 'octave_day' | 'presence_audit' | 'manual';
  /** Timestamp of statement */
  timestamp: string;
  /** Day 1 (Do) reference */
  day1Do: true;
  /** The Temple State */
  templeState: TempleState;
  /** The Spirit State */
  spiritState: SpiritState;
  /** Which 'I' is speaking? */
  speakingI: string;
  /** Full statement text */
  statementText: string;
  /** Immutable: Cannot be modified */
  immutable: true;
  /** Sealed: This is the foundation */
  sealed: true;
  /** Ledger entry reference (triple-redundant storage) */
  ledgerEntryId?: string;
  /** Octave day reference */
  octaveDay?: number;
  /** Octave note reference */
  octaveNote?: 'Do';
}

/**
 * Temple State
 * The current state of the biological temple
 */
export interface TempleState {
  /** Glucose level (mmol/L) */
  glucose: number; // mmol/L
  /** Timestamp of glucose reading */
  glucoseTimestamp: string;
  /** Additional temple metrics */
  metrics?: {
    vision_clarity?: number;
    muscle_tension?: number;
    breath_quality?: number;
    urine_color?: number;
    ketones?: number;
  };
  /** Temple condition description */
  condition: string; // User's description of temple state
}

/**
 * Spirit State
 * The current state of the spirit (how many 'I's are fighting for control)
 */
export interface SpiritState {
  /** Number of 'I's fighting for control */
  numberOfIs: number;
  /** Description of which 'I's are active */
  activeIs: string[]; // e.g., ["The anxious I", "The disciplined I", "The observing I"]
  /** Which 'I' is dominant right now? */
  dominantI: string;
  /** Spirit condition description */
  condition: string; // User's description of spirit state
}

/**
 * First Entry Ceremony
 * The ceremonial recording of the first Statement of Truth
 */
export interface FirstEntryCeremony {
  /** Ceremony ID */
  id: string;
  /** Ceremony timestamp */
  timestamp: string;
  /** Location */
  location: string; // e.g., "London"
  /** Day of week */
  dayOfWeek: string; // e.g., "Sunday"
  /** The Statement of Truth */
  statementOfTruth: StatementOfTruth;
  /** Day 1 (Do) acknowledged? */
  day1Acknowledged: boolean;
  /** Octave initialized? */
  octaveInitialized: boolean;
  /** 376-day journey started? */
  journeyStarted: boolean;
  /** Ledger entries created (triple-redundant) */
  ledgerEntriesCreated: boolean;
}

/**
 * Constants
 */
export const STATEMENT_OF_TRUTH_CONSTANTS = {
  /** 376-day journey */
  JOURNEY_DAYS: 376,
  /** Day 1 note (Do) */
  DAY_1_NOTE: 'Do' as const,
  /** Statement type for first entry */
  FIRST_ENTRY_TYPE: 'first_entry' as const,
  /** Statement is immutable */
  STATEMENT_IMMUTABLE: true,
  /** Statement is sealed */
  STATEMENT_SEALED: true,
  /** Day 1 (Do) is true */
  DAY_1_DO: true as const
} as const;
