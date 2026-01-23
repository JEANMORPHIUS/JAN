/**
 * OPERATION TOTAL_PREP UTILITIES
 * Stress-test the Stewardship Architecture
 * 
 * 1. Stress_Test_Simulator: Trigger Sovereign_Emergency_Mode
 * 2. The_Ouspensky_Watch: Presence checks with Brotherhood_Alert escalation
 * 3. The_Immutable_Ledger_v2: Triple-redundant data storage
 */

import { HealthMetrics } from '../types';
import { calculateBiologicalStability, detectRedTape } from './fourthWay';
import {
  BioStabilityAssessment,
  RedTapePressure,
  StressTestResult,
  SovereignEmergencyMode,
  PresenceCheck,
  OuspenskyWatch,
  BrotherhoodAlert,
  BrotherhoodNode,
  LedgerEntry,
  LedgerRedundancyStatus,
  ImmutableLedgerV2,
  OperationTotalPrep,
  EmergencyModeState,
  OPERATION_TOTAL_PREP_CONSTANTS
} from '../types/operationTotalPrep';

/**
 * Calculate Bio Stability Assessment
 * Calculate biological stability from health metrics
 */
export function calculateBioStabilityAssessment(metrics: HealthMetrics[]): BioStabilityAssessment {
  if (metrics.length === 0) {
    return {
      bioStability: 0,
      glucoseStability: 0,
      visionStability: 0,
      muscleStability: 0,
      breathStability: 0,
      timestamp: new Date().toISOString(),
      metrics: []
    };
  }

  // Calculate stability for each component
  const glucoseValues = metrics.filter(m => m.glucose !== undefined).map(m => m.glucose!);
  const visionValues = metrics.filter(m => m.vision_clarity !== undefined).map(m => m.vision_clarity!);
  const muscleValues = metrics.filter(m => m.muscle_tension !== undefined).map(m => m.muscle_tension!);
  const breathValues = metrics.filter(m => m.breath_quality !== undefined).map(m => m.breath_quality!);

  // Stability = 1 - (coefficient of variation)
  const calculateStability = (values: number[]): number => {
    if (values.length === 0) return 0;
    if (values.length === 1) return 1;
    const mean = values.reduce((a, b) => a + b, 0) / values.length;
    const variance = values.reduce((sum, val) => sum + Math.pow(val - mean, 2), 0) / values.length;
    const stdDev = Math.sqrt(variance);
    const coeffOfVariation = mean > 0 ? stdDev / mean : 0;
    return Math.max(0, 1 - coeffOfVariation);
  };

  const glucoseStability = glucoseValues.length > 0 ? calculateStability(glucoseValues) : 0;
  const visionStability = visionValues.length > 0 ? calculateStability(visionValues) : 0;
  const muscleStability = muscleValues.length > 0 ? calculateStability(muscleValues) : 0;
  const breathStability = breathValues.length > 0 ? calculateStability(breathValues) : 0;

  // Overall bio stability (weighted average)
  const componentCount = [glucoseValues, visionValues, muscleValues, breathValues].filter(v => v.length > 0).length;
  const bioStability = componentCount > 0
    ? (glucoseStability + visionStability + muscleStability + breathStability) / componentCount
    : 0;

  return {
    bioStability,
    glucoseStability,
    visionStability,
    muscleStability,
    breathStability,
    timestamp: new Date().toISOString(),
    metrics
  };
}

/**
 * Assess Red Tape Pressure
 * Assess red tape pressure level from metrics
 */
export function assessRedTapePressure(metrics: HealthMetrics[]): RedTapePressure {
  const redTapeDetected = detectRedTape(metrics);
  
  if (redTapeDetected) {
    // Check severity of red tape
    const glucoseValues = metrics.filter(m => m.glucose !== undefined).map(m => m.glucose!);
    if (glucoseValues.length > 1) {
      const mean = glucoseValues.reduce((a, b) => a + b, 0) / glucoseValues.length;
      const variance = glucoseValues.reduce((sum, val) => sum + Math.pow(val - mean, 2), 0) / glucoseValues.length;
      const stdDev = Math.sqrt(variance);
      
      if (stdDev > 5) return 'High';
      if (stdDev > 3) return 'Medium';
    }
    return 'High';
  }
  
  return 'Low';
}

/**
 * Run Stress Test Simulation
 * Check if bio stability < 0.8 AND red tape pressure == High
 * Trigger Sovereign_Emergency_Mode if condition met
 */
export function runStressTestSimulation(metrics: HealthMetrics[]): StressTestResult {
  const bioStability = calculateBioStabilityAssessment(metrics);
  const redTapePressure = assessRedTapePressure(metrics);

  // Trigger condition: Bio_Stability < 0.8 AND Red_Tape_Pressure == High
  const triggerConditionMet = 
    bioStability.bioStability < OPERATION_TOTAL_PREP_CONSTANTS.BIO_STABILITY_THRESHOLD &&
    redTapePressure === 'High';

  const emergencyModeTriggered = triggerConditionMet;
  const emergencyModeState: EmergencyModeState = emergencyModeTriggered 
    ? 'Sovereign_Emergency_Mode'
    : 'Normal';

  const action = emergencyModeTriggered
    ? 'Sovereign_Emergency_Mode triggered. Cut all non-essential Shell comms. Focus 100% on Temple Homeostasis.'
    : 'System stable. No emergency mode required.';

  return {
    emergencyModeTriggered,
    emergencyModeState,
    bioStability,
    redTapePressure,
    triggerConditionMet,
    action,
    timestamp: new Date().toISOString()
  };
}

/**
 * Create Sovereign Emergency Mode
 * Cut all non-essential Shell comms, focus 100% on Temple Homeostasis
 */
export function createSovereignEmergencyMode(
  active: boolean,
  activationReason: string
): SovereignEmergencyMode {
  return {
    active,
    shellCommsCut: active,
    templeHomeostasisFocus: active,
    nonEssentialCommsDisabled: active 
      ? ['external_api', 'social_media', 'analytics', 'marketing', 'promotional']
      : [],
    essentialCommsEnabled: active
      ? ['temple_homeostasis', 'biological_monitoring', 'presence_checks', 'brotherhood_alert']
      : ['all'],
    activationReason,
    activationTimestamp: new Date().toISOString()
  };
}

/**
 * Create Presence Check
 * Check if user acknowledges Sentinel within 5 mins during spike
 */
export function createPresenceCheck(
  spikeType: 'glucose' | 'vision' | 'muscle' | 'breath',
  spikeValue: number,
  threshold: number
): PresenceCheck {
  const checkId = `presence_check_${Date.now()}`;
  const checkInitiated = new Date().toISOString();
  const acknowledgmentTimeout = OPERATION_TOTAL_PREP_CONSTANTS.PRESENCE_CHECK_TIMEOUT;

  return {
    id: checkId,
    spikeDetected: true,
    spikeDetails: {
      type: spikeType,
      value: spikeValue,
      threshold,
      timestamp: checkInitiated
    },
    checkInitiated,
    acknowledgmentTimeout,
    userAcknowledged: false,
    timeoutReached: false,
    escalatedToBrotherhoodAlert: false
  };
}

/**
 * Check Presence Check Timeout
 * Check if 5 minutes have passed without acknowledgment
 */
export function checkPresenceCheckTimeout(presenceCheck: PresenceCheck): boolean {
  if (presenceCheck.userAcknowledged) return false;
  
  const now = Date.now();
  const checkInitiated = new Date(presenceCheck.checkInitiated).getTime();
  const timeoutReached = (now - checkInitiated) >= presenceCheck.acknowledgmentTimeout;
  
  return timeoutReached;
}

/**
 * Acknowledge Presence Check
 * User acknowledges Sentinel within timeout
 */
export function acknowledgePresenceCheck(presenceCheck: PresenceCheck): PresenceCheck {
  return {
    ...presenceCheck,
    userAcknowledged: true,
    acknowledgmentTimestamp: new Date().toISOString(),
    timeoutReached: false,
    escalatedToBrotherhoodAlert: false
  };
}

/**
 * Create Brotherhood Alert
 * Contact the 8 Nodes when presence check times out
 */
export function createBrotherhoodAlert(
  triggerReason: string,
  nodes?: BrotherhoodNode[]
): BrotherhoodAlert {
  const alertId = `brotherhood_alert_${Date.now()}`;
  
  // Default 8 nodes (if not provided, create placeholder)
  const defaultNodes: BrotherhoodNode[] = Array.from({ length: OPERATION_TOTAL_PREP_CONSTANTS.BROTHERHOOD_NODES_COUNT }, (_, i) => ({
    nodeId: i + 1,
    nodeName: `Node ${i + 1}`,
    contactMethod: 'internal_alert',
    contactStatus: 'pending',
    responseReceived: false
  }));

  const nodesToContact = nodes || defaultNodes;
  const contactStatus = new Map<string, 'pending' | 'sent' | 'acknowledged' | 'failed'>();
  nodesToContact.forEach(node => {
    contactStatus.set(node.nodeName, node.contactStatus);
  });

  return {
    id: alertId,
    triggered: true,
    triggerReason,
    triggerTimestamp: new Date().toISOString(),
    nodesContacted: nodesToContact,
    contactStatus,
    resolved: false
  };
}

/**
 * Contact Brotherhood Nodes
 * Send alert to all 8 nodes
 */
export function contactBrotherhoodNodes(alert: BrotherhoodAlert): BrotherhoodAlert {
  const updatedNodes = alert.nodesContacted.map(node => ({
    ...node,
    contactStatus: 'sent' as const,
    contactTimestamp: new Date().toISOString()
  }));

  const updatedContactStatus = new Map(alert.contactStatus);
  updatedNodes.forEach(node => {
    updatedContactStatus.set(node.nodeName, node.contactStatus);
  });

  return {
    ...alert,
    nodesContacted: updatedNodes,
    contactStatus: updatedContactStatus
  };
}

/**
 * Create Ledger Entry
 * Create a new immutable ledger entry
 */
export function createLedgerEntry(
  type: LedgerEntry['type'],
  data: any,
  previousHash: string
): LedgerEntry {
  const entryId = `ledger_entry_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
  const timestamp = new Date().toISOString();
  
  // Create hash from entry data (simplified - would use proper hashing in production)
  const entryString = JSON.stringify({ id: entryId, type, data, timestamp, previousHash });
  const hash = btoa(entryString).substr(0, 64); // Simplified hash

  return {
    id: entryId,
    type,
    data,
    timestamp,
    hash,
    previousHash,
    immutable: true
  };
}

/**
 * Calculate Ledger Hash
 * Calculate hash for ledger verification (simplified)
 */
function calculateLedgerHash(entry: LedgerEntry): string {
  const entryString = JSON.stringify({ id: entry.id, type: entry.type, data: entry.data, timestamp: entry.timestamp, previousHash: entry.previousHash });
  return btoa(entryString).substr(0, 64);
}

/**
 * Verify Ledger Entry
 * Verify ledger entry integrity
 */
export function verifyLedgerEntry(entry: LedgerEntry): boolean {
  const calculatedHash = calculateLedgerHash(entry);
  return calculatedHash === entry.hash && entry.immutable === true;
}

/**
 * Check Ledger Redundancy Status
 * Check if all three storage locations are in sync
 */
export function checkLedgerRedundancyStatus(
  primaryEntries: LedgerEntry[],
  secondaryEntries: LedgerEntry[],
  tertiaryEntries: LedgerEntry[]
): LedgerRedundancyStatus {
  const primaryAvailable = primaryEntries.length > 0;
  const secondaryAvailable = secondaryEntries.length > 0;
  const tertiaryAvailable = tertiaryEntries.length > 0;

  // Calculate verification hashes (simplified - use chain head hash)
  const primaryHash = primaryEntries.length > 0 ? primaryEntries[primaryEntries.length - 1].hash : undefined;
  const secondaryHash = secondaryEntries.length > 0 ? secondaryEntries[secondaryEntries.length - 1].hash : undefined;
  const tertiaryHash = tertiaryEntries.length > 0 ? tertiaryEntries[tertiaryEntries.length - 1].hash : undefined;

  // Check if all hashes match (all in sync)
  const allHashesMatch = primaryHash && secondaryHash && tertiaryHash &&
    primaryHash === secondaryHash && secondaryHash === tertiaryHash;

  const allInSync = primaryAvailable && secondaryAvailable && tertiaryAvailable && allHashesMatch;

  return {
    primary: {
      available: primaryAvailable,
      entryCount: primaryEntries.length,
      lastEntryTimestamp: primaryEntries.length > 0 ? primaryEntries[primaryEntries.length - 1].timestamp : undefined,
      verificationHash: primaryHash
    },
    secondary: {
      available: secondaryAvailable,
      entryCount: secondaryEntries.length,
      lastEntryTimestamp: secondaryEntries.length > 0 ? secondaryEntries[secondaryEntries.length - 1].timestamp : undefined,
      verificationHash: secondaryHash
    },
    tertiary: {
      available: tertiaryAvailable,
      entryCount: tertiaryEntries.length,
      lastEntryTimestamp: tertiaryEntries.length > 0 ? tertiaryEntries[tertiaryEntries.length - 1].timestamp : undefined,
      verificationHash: tertiaryHash
    },
    allInSync,
    lastSyncCheck: new Date().toISOString()
  };
}

/**
 * Store Ledger Entry with Triple Redundancy
 * Store entry in all three storage locations
 */
export function storeLedgerEntryWithTripleRedundancy(
  entry: LedgerEntry,
  primaryStorage: LedgerEntry[],
  secondaryStorage: LedgerEntry[],
  tertiaryStorage: LedgerEntry[]
): {
  primary: LedgerEntry[];
  secondary: LedgerEntry[];
  tertiary: LedgerEntry[];
  success: boolean;
} {
  // Verify entry before storing
  if (!verifyLedgerEntry(entry)) {
    return {
      primary: primaryStorage,
      secondary: secondaryStorage,
      tertiary: tertiaryStorage,
      success: false
    };
  }

  // Store in all three locations
  const updatedPrimary = [...primaryStorage, entry];
  const updatedSecondary = [...secondaryStorage, entry];
  const updatedTertiary = [...tertiaryStorage, entry];

  // Verify all stored
  const primaryStored = updatedPrimary[updatedPrimary.length - 1].id === entry.id;
  const secondaryStored = updatedSecondary[updatedSecondary.length - 1].id === entry.id;
  const tertiaryStored = updatedTertiary[updatedTertiary.length - 1].id === entry.id;

  const success = primaryStored && secondaryStored && tertiaryStored;

  return {
    primary: updatedPrimary,
    secondary: updatedSecondary,
    tertiary: updatedTertiary,
    success
  };
}

/**
 * Create Immutable Ledger v2
 * Initialize triple-redundant ledger
 */
export function createImmutableLedgerV2(): ImmutableLedgerV2 {
  return {
    active: true,
    entries: [],
    redundancyStatus: {
      primary: { available: true, entryCount: 0 },
      secondary: { available: true, entryCount: 0 },
      tertiary: { available: true, entryCount: 0 },
      allInSync: true,
      lastSyncCheck: new Date().toISOString()
    },
    systemIsBattleReady: OPERATION_TOTAL_PREP_CONSTANTS.SYSTEM_IS_BATTLE_READY,
    law37Enforced: OPERATION_TOTAL_PREP_CONSTANTS.LAW_37_ENFORCED,
    lastEntryId: '',
    chainHeadHash: ''
  };
}

/**
 * Create Operation Total Prep State
 * Initialize complete stress test system
 */
export function createOperationTotalPrep(): OperationTotalPrep {
  return {
    active: true,
    stressTestSimulator: {
      active: true,
      sovereignEmergencyMode: createSovereignEmergencyMode(false, 'System initialized')
    },
    ouspenskyWatch: {
      active: true,
      presenceChecksPending: [],
      presenceChecksCompleted: [],
      presenceChecksEscalated: [],
      acknowledgmentTimeout: OPERATION_TOTAL_PREP_CONSTANTS.PRESENCE_CHECK_TIMEOUT,
      brotherhoodAlertTriggered: false,
      lastPresenceCheck: new Date().toISOString()
    },
    immutableLedgerV2: createImmutableLedgerV2(),
    systemIsBattleReady: OPERATION_TOTAL_PREP_CONSTANTS.SYSTEM_IS_BATTLE_READY,
    law37Enforced: OPERATION_TOTAL_PREP_CONSTANTS.LAW_37_ENFORCED,
    timestamp: new Date().toISOString()
  };
}

/**
 * Constants Export
 */
export const SYSTEM_IS_BATTLE_READY = OPERATION_TOTAL_PREP_CONSTANTS.SYSTEM_IS_BATTLE_READY;
export const LAW_37_ENFORCED = OPERATION_TOTAL_PREP_CONSTANTS.LAW_37_ENFORCED;
