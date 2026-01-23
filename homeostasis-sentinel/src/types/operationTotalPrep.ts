/**
 * OPERATION TOTAL_PREP TYPES
 * Stress-test the Stewardship Architecture
 * 
 * 1. Stress_Test_Simulator: Trigger Sovereign_Emergency_Mode
 * 2. The_Ouspensky_Watch: Presence checks with Brotherhood_Alert escalation
 * 3. The_Immutable_Ledger_v2: Triple-redundant data storage
 */

import { HealthMetrics, SystemState } from './index';
import { BiologicalTruthSnapshot } from './integratedStewardship';

/**
 * Red Tape Pressure Level
 */
export type RedTapePressure = 'High' | 'Medium' | 'Low';

/**
 * Emergency Mode State
 */
export type EmergencyModeState = 
  | 'Normal'
  | 'Sovereign_Emergency_Mode'
  | 'Brotherhood_Alert'
  | 'Battle_Ready';

/**
 * Bio Stability Assessment
 * Biological stability score (0-1)
 */
export interface BioStabilityAssessment {
  /** Bio stability score (0-1, higher = more stable) */
  bioStability: number;
  /** Glucose stability component */
  glucoseStability: number;
  /** Vision stability component */
  visionStability: number;
  /** Muscle stability component */
  muscleStability: number;
  /** Breath stability component */
  breathStability: number;
  /** Timestamp of assessment */
  timestamp: string;
  /** Metrics used for assessment */
  metrics: HealthMetrics[];
}

/**
 * Stress Test Result
 * Result of stress test simulation
 */
export interface StressTestResult {
  /** Triggered emergency mode? */
  emergencyModeTriggered: boolean;
  /** Emergency mode state */
  emergencyModeState: EmergencyModeState;
  /** Bio stability assessment */
  bioStability: BioStabilityAssessment;
  /** Red tape pressure */
  redTapePressure: RedTapePressure;
  /** Trigger condition met? */
  triggerConditionMet: boolean;
  /** Action taken */
  action: string;
  /** Timestamp */
  timestamp: string;
}

/**
 * Sovereign Emergency Mode State
 * Cut non-essential Shell comms, focus 100% on Temple Homeostasis
 */
export interface SovereignEmergencyMode {
  /** Emergency mode active? */
  active: boolean;
  /** Shell comms cut? */
  shellCommsCut: boolean;
  /** Focus on Temple Homeostasis */
  templeHomeostasisFocus: boolean;
  /** Non-essential comms disabled */
  nonEssentialCommsDisabled: string[];
  /** Essential comms enabled */
  essentialCommsEnabled: string[];
  /** Activation reason */
  activationReason: string;
  /** Activation timestamp */
  activationTimestamp: string;
}

/**
 * Presence Check State
 * Check if user acknowledges Sentinel within 5 mins during spike
 */
export interface PresenceCheck {
  /** Presence check ID */
  id: string;
  /** Spike detected? */
  spikeDetected: boolean;
  /** Spike details */
  spikeDetails: {
    /** Spike type (glucose, vision, muscle, breath) */
    type: 'glucose' | 'vision' | 'muscle' | 'breath';
    /** Spike value */
    value: number;
    /** Threshold exceeded */
    threshold: number;
    /** Timestamp of spike */
    timestamp: string;
  };
  /** Presence check initiated */
  checkInitiated: string;
  /** Acknowledgment timeout (5 minutes) */
  acknowledgmentTimeout: number; // milliseconds (5 * 60 * 1000)
  /** User acknowledged? */
  userAcknowledged: boolean;
  /** Acknowledgment timestamp */
  acknowledgmentTimestamp?: string;
  /** Timeout reached? */
  timeoutReached: boolean;
  /** Escalated to Brotherhood_Alert? */
  escalatedToBrotherhoodAlert: boolean;
}

/**
 * The Ouspensky Watch State
 * Monitoring system with presence checks
 */
export interface OuspenskyWatch {
  /** Watch active? */
  active: boolean;
  /** Presence checks pending */
  presenceChecksPending: PresenceCheck[];
  /** Presence checks completed */
  presenceChecksCompleted: PresenceCheck[];
  /** Presence checks escalated */
  presenceChecksEscalated: PresenceCheck[];
  /** Acknowledgment timeout (5 minutes in milliseconds) */
  acknowledgmentTimeout: number; // 5 * 60 * 1000 = 300000
  /** Brotherhood_Alert triggered? */
  brotherhoodAlertTriggered: boolean;
  /** Last presence check timestamp */
  lastPresenceCheck: string;
}

/**
 * Brotherhood Alert State
 * Contact the 8 Nodes when presence check times out
 */
export interface BrotherhoodAlert {
  /** Alert ID */
  id: string;
  /** Alert triggered? */
  triggered: boolean;
  /** Trigger reason */
  triggerReason: string;
  /** Trigger timestamp */
  triggerTimestamp: string;
  /** Nodes contacted */
  nodesContacted: BrotherhoodNode[];
  /** Contact status */
  contactStatus: Map<string, 'pending' | 'sent' | 'acknowledged' | 'failed'>;
  /** Alert resolved? */
  resolved: boolean;
  /** Resolution timestamp */
  resolutionTimestamp?: string;
}

/**
 * Brotherhood Node
 * One of the 8 Nodes to contact during Brotherhood_Alert
 */
export interface BrotherhoodNode {
  /** Node ID (1-8) */
  nodeId: number;
  /** Node name */
  nodeName: string;
  /** Contact method */
  contactMethod: string;
  /** Contact status */
  contactStatus: 'pending' | 'sent' | 'acknowledged' | 'failed';
  /** Contact timestamp */
  contactTimestamp?: string;
  /** Response received? */
  responseReceived: boolean;
  /** Response timestamp */
  responseTimestamp?: string;
}

/**
 * Ledger Entry
 * Single entry in the immutable ledger
 */
export interface LedgerEntry {
  /** Entry ID (unique) */
  id: string;
  /** Entry type */
  type: 'metric' | 'truth_set' | 'presence_check' | 'emergency_mode' | 'brotherhood_alert';
  /** Entry data */
  data: any; // Could be HealthMetrics, BiologicalTruthSnapshot, etc.
  /** Entry timestamp */
  timestamp: string;
  /** Entry hash (for verification) */
  hash: string;
  /** Previous entry hash (chain link) */
  previousHash: string;
  /** Immutable: Cannot be modified */
  immutable: true;
}

/**
 * Ledger Storage Location
 * One of the three redundant storage locations
 */
export type LedgerStorageLocation = 'primary' | 'secondary' | 'tertiary';

/**
 * Ledger Redundancy Status
 * Status of triple-redundant storage
 */
export interface LedgerRedundancyStatus {
  /** Primary storage status */
  primary: {
    /** Available? */
    available: boolean;
    /** Entry count */
    entryCount: number;
    /** Last entry timestamp */
    lastEntryTimestamp?: string;
    /** Verification hash */
    verificationHash?: string;
  };
  /** Secondary storage status */
  secondary: {
    /** Available? */
    available: boolean;
    /** Entry count */
    entryCount: number;
    /** Last entry timestamp */
    lastEntryTimestamp?: string;
    /** Verification hash */
    verificationHash?: string;
  };
  /** Tertiary storage status */
  tertiary: {
    /** Available? */
    available: boolean;
    /** Entry count */
    entryCount: number;
    /** Last entry timestamp */
    lastEntryTimestamp?: string;
    /** Verification hash */
    verificationHash?: string;
  };
  /** All storage locations in sync? */
  allInSync: boolean;
  /** Timestamp of last sync check */
  lastSyncCheck: string;
}

/**
 * The Immutable Ledger v2 State
 * Triple-redundant data storage
 */
export interface ImmutableLedgerV2 {
  /** Ledger active? */
  active: boolean;
  /** Entries (primary storage) */
  entries: LedgerEntry[];
  /** Redundancy status */
  redundancyStatus: LedgerRedundancyStatus;
  /** System is battle ready? */
  systemIsBattleReady: boolean;
  /** Law 37 enforced? */
  law37Enforced: boolean;
  /** Last entry ID */
  lastEntryId: string;
  /** Chain head hash */
  chainHeadHash: string;
}

/**
 * Operation Total Prep State
 * Complete stress test system state
 */
export interface OperationTotalPrep {
  /** Operation active? */
  active: boolean;
  /** Stress test simulator state */
  stressTestSimulator: {
    /** Simulator active? */
    active: boolean;
    /** Last test result */
    lastTestResult?: StressTestResult;
    /** Sovereign emergency mode */
    sovereignEmergencyMode: SovereignEmergencyMode;
  };
  /** Ouspensky Watch state */
  ouspenskyWatch: OuspenskyWatch;
  /** Immutable Ledger v2 state */
  immutableLedgerV2: ImmutableLedgerV2;
  /** System is battle ready? */
  systemIsBattleReady: boolean;
  /** Law 37 enforced? */
  law37Enforced: boolean;
  /** Timestamp */
  timestamp: string;
}

/**
 * Constants
 */
export const OPERATION_TOTAL_PREP_CONSTANTS = {
  /** System is battle ready */
  SYSTEM_IS_BATTLE_READY: true,
  /** Law 37 enforced */
  LAW_37_ENFORCED: true,
  /** Bio stability threshold for emergency mode (0.8) */
  BIO_STABILITY_THRESHOLD: 0.8,
  /** Presence check timeout (5 minutes in milliseconds) */
  PRESENCE_CHECK_TIMEOUT: 5 * 60 * 1000, // 300000 ms
  /** Number of Brotherhood Nodes (8) */
  BROTHERHOOD_NODES_COUNT: 8
} as const;
