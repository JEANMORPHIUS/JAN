/**
 * STATEMENT OF TRUTH UTILITIES
 * The First Entry - Day 1 (Do) - The Note of Intent
 * 
 * To seal the start of the 376-day count, we need the first "Statement of Truth."
 * This is the foundation - immutable, sacred, and recorded in the Ledger.
 */

import {
  StatementOfTruth,
  TempleState,
  SpiritState,
  FirstEntryCeremony,
  STATEMENT_OF_TRUTH_CONSTANTS
} from '../types/statementOfTruth';
import { createLedgerEntry } from './operationTotalPrep';
import type { LedgerEntry } from '../types/operationTotalPrep';

/**
 * Create Temple State
 * Create the state of the biological temple
 */
export function createTempleState(
  glucose: number,
  glucoseTimestamp: string,
  condition: string,
  metrics?: TempleState['metrics']
): TempleState {
  return {
    glucose,
    glucoseTimestamp,
    metrics,
    condition
  };
}

/**
 * Create Spirit State
 * Create the state of the spirit (how many 'I's are fighting for control)
 */
export function createSpiritState(
  numberOfIs: number,
  activeIs: string[],
  dominantI: string,
  condition: string
): SpiritState {
  return {
    numberOfIs,
    activeIs,
    dominantI,
    condition
  };
}

/**
 * Create Statement of Truth
 * Create the foundational entry that begins the 376-day journey
 */
export function createStatementOfTruth(
  templeState: TempleState,
  spiritState: SpiritState,
  speakingI: string,
  statementText: string,
  octaveDay: number = 1,
  previousHash: string = '0000000000000000000000000000000000000000000000000000000000000000' // Genesis hash
): StatementOfTruth {
  const statementId = `statement_of_truth_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
  const timestamp = new Date().toISOString();

  return {
    id: statementId,
    type: STATEMENT_OF_TRUTH_CONSTANTS.FIRST_ENTRY_TYPE,
    timestamp,
    day1Do: STATEMENT_OF_TRUTH_CONSTANTS.DAY_1_DO,
    templeState,
    spiritState,
    speakingI,
    statementText,
    immutable: STATEMENT_OF_TRUTH_CONSTANTS.STATEMENT_IMMUTABLE,
    sealed: STATEMENT_OF_TRUTH_CONSTANTS.STATEMENT_SEALED,
    octaveDay,
    octaveNote: STATEMENT_OF_TRUTH_CONSTANTS.DAY_1_NOTE
  };
}

/**
 * Create Statement Text
 * Generate the full statement text from temple and spirit states
 */
export function createStatementText(
  templeState: TempleState,
  spiritState: SpiritState,
  speakingI: string
): string {
  return `STATEMENT OF TRUTH - DAY 1 (DO)

The Temple State:
  Glucose: ${templeState.glucose} mmol/L
  Timestamp: ${templeState.glucoseTimestamp}
  Condition: ${templeState.condition}

The Spirit State:
  Number of 'I's: ${spiritState.numberOfIs}
  Active 'I's: ${spiritState.activeIs.join(', ')}
  Dominant 'I': ${spiritState.dominantI}
  Condition: ${spiritState.condition}

Which 'I' is speaking: ${speakingI}

This is the foundation. This is Day 1 (Do). The Note of Intent.
The 376-day journey begins now.
`;
}

/**
 * Create Ledger Entry from Statement of Truth
 * Store Statement of Truth in the Immutable Ledger v2 (triple-redundant)
 */
export function createLedgerEntryFromStatement(
  statement: StatementOfTruth,
  previousHash: string = '0000000000000000000000000000000000000000000000000000000000000000'
): LedgerEntry {
  const ledgerEntry = createLedgerEntry('truth_set', statement, previousHash);
  
  // Link statement to ledger entry
  (statement as StatementOfTruth & { ledgerEntryId: string }).ledgerEntryId = ledgerEntry.id;
  
  return ledgerEntry;
}

/**
 * Create First Entry Ceremony
 * The ceremonial recording of the first Statement of Truth
 */
export function createFirstEntryCeremony(
  templeState: TempleState,
  spiritState: SpiritState,
  speakingI: string,
  location: string = 'London',
  dayOfWeek: string = 'Sunday'
): FirstEntryCeremony {
  const ceremonyId = `first_entry_ceremony_${Date.now()}`;
  const timestamp = new Date().toISOString();
  
  const statementText = createStatementText(templeState, spiritState, speakingI);
  const statement = createStatementOfTruth(templeState, spiritState, speakingI, statementText);
  
  // Create ledger entry (will be stored triple-redundant in actual implementation)
  const ledgerEntry = createLedgerEntryFromStatement(statement);
  statement.ledgerEntryId = ledgerEntry.id;

  return {
    id: ceremonyId,
    timestamp,
    location,
    dayOfWeek,
    statementOfTruth: statement,
    day1Acknowledged: true,
    octaveInitialized: true,
    journeyStarted: true,
    ledgerEntriesCreated: true
  };
}

/**
 * Seal First Entry
 * Final seal on the first Statement of Truth - begins the 376-day journey
 */
export function sealFirstEntry(ceremony: FirstEntryCeremony): FirstEntryCeremony {
  // The ceremony is already sealed by creation
  // This function exists for ceremonial purposes
  return {
    ...ceremony,
    journeyStarted: true
  };
}

/**
 * Validate Statement of Truth
 * Validate that statement meets requirements for Day 1 (Do)
 */
export function validateStatementOfTruth(statement: StatementOfTruth): {
  valid: boolean;
  errors: string[];
} {
  const errors: string[] = [];

  if (!statement.day1Do) {
    errors.push('Statement must be for Day 1 (Do)');
  }

  if (statement.type !== 'first_entry') {
    errors.push('Statement type must be "first_entry"');
  }

  if (!statement.templeState || !statement.templeState.glucose) {
    errors.push('Temple state must include glucose reading');
  }

  if (!statement.spiritState || statement.spiritState.numberOfIs === undefined) {
    errors.push('Spirit state must include number of \'I\'s');
  }

  if (!statement.speakingI || statement.speakingI.trim() === '') {
    errors.push('Which \'I\' is speaking must be specified');
  }

  if (!statement.immutable || !statement.sealed) {
    errors.push('Statement must be immutable and sealed');
  }

  return {
    valid: errors.length === 0,
    errors
  };
}
