/**
 * COMPLETE SYSTEM ACTIVATION (THE OMEGA KEY) UTILITIES
 * Launch the full 376-Day Stewardship Engine
 */

import {
  SiyemPulseState,
  SyncStatus,
  Engine376State,
  DailyStewardshipModule,
  CommandCenterUIState,
  SystemStatus,
  DashboardComponent,
  GlucoseMetrics,
  LunarPhase,
  CommunityIntegrityMetrics,
  BraidStrengthMetrics,
  CompleteSystemActivationFinalState,
  OMEGA_KEY_CONSTANTS
} from '../types/omegaKey';
import { HealthMetrics, EarthAlignment } from '../types';
import { CommunityNode, LONDON_COMMUNITIES } from '../types/expansionPhase';
import { ProtocolEvent } from '../types/stewardship';

/**
 * Calculate The Siyem Pulse State
 * Activate the `Homeostasis_Sentinel` across all community nodes
 * Sync `biological_ledger` with `ancestral_frequency_api`
 */
export function calculateSiyemPulseState(
  communityNodes: CommunityNode[],
  biologicalLedgerSynced: boolean,
  ancestralFrequencyAPISynced: boolean
): SiyemPulseState {
  const activeCommunityNodes = communityNodes.length > 0 
    ? communityNodes 
    : LONDON_COMMUNITIES;

  const homeostasisSentinelActivated = activeCommunityNodes.length > 0;

  // Calculate sync status
  const syncStatus: SyncStatus = {
    isSynced: biologicalLedgerSynced && ancestralFrequencyAPISynced,
    syncPercentage: ((biologicalLedgerSynced ? 50 : 0) + (ancestralFrequencyAPISynced ? 50 : 0)),
    lastSuccessfulSyncTimestamp: (biologicalLedgerSynced && ancestralFrequencyAPISynced) 
      ? new Date().toISOString() 
      : undefined,
    syncErrorsCount: (biologicalLedgerSynced ? 0 : 1) + (ancestralFrequencyAPISynced ? 0 : 1),
    syncStatusDescription: (biologicalLedgerSynced && ancestralFrequencyAPISynced)
      ? 'Biological ledger and Ancestral Frequency API fully synced'
      : (biologicalLedgerSynced ? 'Biological ledger synced, Ancestral Frequency API pending' : 
         (ancestralFrequencyAPISynced ? 'Ancestral Frequency API synced, Biological ledger pending' : 
         'Sync pending for both systems'))
  };

  const isActive = homeostasisSentinelActivated && syncStatus.isSynced;

  return {
    isActive,
    homeostasisSentinelActivated,
    activeCommunityNodes,
    biologicalLedgerSynced,
    ancestralFrequencyAPISynced,
    syncStatus,
    pulseTimestamp: new Date().toISOString(),
    lastSyncTimestamp: syncStatus.lastSuccessfulSyncTimestamp
  };
}

/**
 * Calculate The 376 Engine State
 * Daily stewardship module with Law 37 progression
 * 
 * `let current_lesson = getDailyStewardshipModule();`
 * IF (StewardshipScore < 1.0): Pause lesson progression
 * NOTE: In the Racon, you don't 'advance' until you've 'finished' (Law 37)
 */
export function calculateEngine376State(
  currentLesson: number,
  stewardshipScore: number,
  lessonsCompleted: number[],
  protocolEvents?: ProtocolEvent[]
): Engine376State {
  const totalLessons = OMEGA_KEY_CONSTANTS.TOTAL_LESSONS;
  const minScoreForProgression = OMEGA_KEY_CONSTANTS.MIN_STEWARDSHIP_SCORE_FOR_PROGRESSION;

  // Check if can advance (stewardship score must be 1.0)
  const canAdvance = stewardshipScore >= minScoreForProgression;

  // Lesson progression paused if stewardship score < 1.0
  const lessonProgressionPaused = !canAdvance;

  let pauseReason: string | undefined;
  if (lessonProgressionPaused) {
    pauseReason = `Stewardship score ${(stewardshipScore * 100).toFixed(1)}% < 100%. Law 37: Finish what you begin before advancing.`;
  }

  // Check Law 37 compliance (all completed lessons must be truly finished)
  const law37Compliance = canAdvance && 
    (protocolEvents?.every(e => e.law37Compliance || e.eventType !== 'completed') ?? true);

  // Get daily stewardship module
  const dailyStewardshipModule = getDailyStewardshipModule(currentLesson);

  // Calculate progress percentage
  const progressPercentage = lessonsCompleted.length > 0
    ? (lessonsCompleted.length / totalLessons) * 100
    : 0;

  const isActive = currentLesson > 0 && currentLesson <= totalLessons;

  return {
    isActive,
    currentLesson,
    dailyStewardshipModule,
    stewardshipScore: Math.round(stewardshipScore * 1000) / 1000,
    canAdvance,
    lessonProgressionPaused,
    pauseReason,
    law37Compliance,
    lessonsCompleted,
    totalLessons,
    progressPercentage: Math.round(progressPercentage * 100) / 100,
    lastLessonUpdateTimestamp: new Date().toISOString()
  };
}

/**
 * Get Daily Stewardship Module
 * `let current_lesson = getDailyStewardshipModule();`
 */
export function getDailyStewardshipModule(lessonNumber: number): DailyStewardshipModule {
  const moduleId = `stewardship_module_lesson_${lessonNumber}`;
  const moduleName = `Stewardship Module ${lessonNumber}: Law ${((lessonNumber - 1) % 40) + 1}`;
  
  // Generate module content (simplified - would come from lesson database)
  const moduleContent = `This is Stewardship Module ${lessonNumber}. Apply Law ${((lessonNumber - 1) % 40) + 1} to your daily stewardship. Finish what you begin (Law 37).`;

  // Generate requirements (simplified)
  const requirements = [
    'Complete daily biological stewardship',
    'Apply current Law to stewardship practice',
    'Maintain word integrity (Law 5)',
    'Finish all initiated protocols (Law 37)'
  ];

  // Generate completion criteria
  const completionCriteria = [
    'Biological data logged accurately',
    'Protocols completed without abandonment',
    'Word integrity maintained (100%)',
    'Law 37 compliance verified'
  ];

  // Check if completed (simplified - would check actual completion)
  const isCompleted = false;

  return {
    id: moduleId,
    lessonNumber,
    moduleName,
    moduleContent,
    requirements,
    completionCriteria,
    isCompleted,
    ...(isCompleted && { completionTimestamp: new Date().toISOString() })
  };
}

/**
 * Calculate Command Center UI State
 * Full dashboard activation: Glucose, Lunar Phase, Community Integrity, and Braid Strength
 * Set `system_status = 'TOTAL_READINESS'`
 */
export function calculateCommandCenterUIState(
  metrics: HealthMetrics[],
  earthAlignment: EarthAlignment,
  communityIntegrityScores: Map<CommunityNode, number>,
  braidStrength: number,
  turkishHonorScore: number,
  greekLogicInquiry: number,
  cypriotSynthesis: number
): CommandCenterUIState {
  // Calculate glucose metrics
  const glucoseMetrics = calculateGlucoseMetrics(metrics);

  // Calculate lunar phase
  const lunarPhase = calculateLunarPhase(earthAlignment);

  // Calculate community integrity
  const communityIntegrity = calculateCommunityIntegrityMetrics(communityIntegrityScores);

  // Calculate braid strength metrics
  const braidStrengthMetrics = calculateBraidStrengthMetrics(
    braidStrength,
    turkishHonorScore,
    greekLogicInquiry,
    cypriotSynthesis
  );

  // Create dashboard components
  const dashboardComponents: DashboardComponent[] = [
    {
      id: 'dashboard_glucose',
      name: 'Glucose Metrics',
      type: 'glucose',
      status: 'active',
      data: glucoseMetrics
    },
    {
      id: 'dashboard_lunar_phase',
      name: 'Lunar Phase',
      type: 'lunar_phase',
      status: 'active',
      data: lunarPhase
    },
    {
      id: 'dashboard_community_integrity',
      name: 'Community Integrity',
      type: 'community_integrity',
      status: 'active',
      data: communityIntegrity
    },
    {
      id: 'dashboard_braid_strength',
      name: 'Braid Strength',
      type: 'braid_strength',
      status: 'active',
      data: braidStrengthMetrics
    }
  ];

  // System status: TOTAL_READINESS
  const systemStatus: SystemStatus = OMEGA_KEY_CONSTANTS.SYSTEM_STATUS_TOTAL_READINESS;

  return {
    isActive: true,
    systemStatus,
    dashboardComponents,
    glucoseMetrics,
    lunarPhase,
    communityIntegrity,
    braidStrength: braidStrengthMetrics,
    lastUpdateTimestamp: new Date().toISOString()
  };
}

/**
 * Calculate Glucose Metrics
 */
function calculateGlucoseMetrics(metrics: HealthMetrics[]): GlucoseMetrics {
  if (metrics.length === 0) {
    return {
      currentGlucose: 0,
      averageGlucose: 0,
      glucoseRange: { min: 0, max: 0 },
      stabilityScore: 0.5,
      glucoseStatus: 'stable'
    };
  }

  const glucoseReadings = metrics
    .filter(m => m.blood_glucose !== undefined)
    .map(m => m.blood_glucose! > 30 ? m.blood_glucose! / 18.0182 : m.blood_glucose!);

  if (glucoseReadings.length === 0) {
    return {
      currentGlucose: 0,
      averageGlucose: 0,
      glucoseRange: { min: 0, max: 0 },
      stabilityScore: 0.5,
      glucoseStatus: 'stable'
    };
  }

  const currentGlucose = glucoseReadings[glucoseReadings.length - 1];
  const averageGlucose = glucoseReadings.reduce((sum, val) => sum + val, 0) / glucoseReadings.length;
  const min = Math.min(...glucoseReadings);
  const max = Math.max(...glucoseReadings);

  // Calculate stability score (lower variance = higher stability)
  const variance = glucoseReadings.reduce((sum, val) => sum + Math.pow(val - averageGlucose, 2), 0) / glucoseReadings.length;
  const stabilityScore = Math.max(0, Math.min(1, 1 - (variance / 10)));

  // Determine glucose status
  let glucoseStatus: 'optimal' | 'stable' | 'warning' | 'critical';
  if (currentGlucose >= 4 && currentGlucose <= 10 && stabilityScore >= 0.8) {
    glucoseStatus = 'optimal';
  } else if (currentGlucose >= 3.5 && currentGlucose <= 15 && stabilityScore >= 0.6) {
    glucoseStatus = 'stable';
  } else if (currentGlucose >= 2.5 && currentGlucose <= 20) {
    glucoseStatus = 'warning';
  } else {
    glucoseStatus = 'critical';
  }

  return {
    currentGlucose: Math.round(currentGlucose * 100) / 100,
    averageGlucose: Math.round(averageGlucose * 100) / 100,
    glucoseRange: {
      min: Math.round(min * 100) / 100,
      max: Math.round(max * 100) / 100
    },
    stabilityScore: Math.round(stabilityScore * 1000) / 1000,
    glucoseStatus
  };
}

/**
 * Calculate Lunar Phase
 */
function calculateLunarPhase(earthAlignment: EarthAlignment): LunarPhase {
  // Calculate next phase change date (simplified - would use actual lunar calculations)
  const nextPhaseChangeDate = new Date();
  nextPhaseChangeDate.setDate(nextPhaseChangeDate.getDate() + (14 - earthAlignment.lunar.daysFromNewMoon));

  return {
    phase: earthAlignment.lunar.phase,
    daysFromNewMoon: earthAlignment.lunar.daysFromNewMoon,
    lunarIntensity: earthAlignment.lunar.lunarIntensity,
    nextPhaseChangeDate: nextPhaseChangeDate.toISOString().split('T')[0]
  };
}

/**
 * Calculate Community Integrity Metrics
 */
function calculateCommunityIntegrityMetrics(
  communityIntegrityScores: Map<CommunityNode, number>
): CommunityIntegrityMetrics {
  const scores = Array.from(communityIntegrityScores.values());
  const overallIntegrity = scores.length > 0
    ? scores.reduce((sum, score) => sum + score, 0) / scores.length
    : 0.5;

  const communitiesAtRisk = Array.from(communityIntegrityScores.entries())
    .filter(([_, score]) => score < 0.6)
    .map(([node, _]) => node);

  // Determine integrity status
  let integrityStatus: 'excellent' | 'good' | 'moderate' | 'poor' | 'critical';
  if (overallIntegrity >= 0.9) {
    integrityStatus = 'excellent';
  } else if (overallIntegrity >= 0.7) {
    integrityStatus = 'good';
  } else if (overallIntegrity >= 0.5) {
    integrityStatus = 'moderate';
  } else if (overallIntegrity >= 0.3) {
    integrityStatus = 'poor';
  } else {
    integrityStatus = 'critical';
  }

  return {
    overallIntegrity: Math.round(overallIntegrity * 1000) / 1000,
    integrityByCommunity: communityIntegrityScores,
    communitiesAtRisk,
    integrityStatus
  };
}

/**
 * Calculate Braid Strength Metrics
 */
function calculateBraidStrengthMetrics(
  braidStrength: number,
  turkishHonorScore: number,
  greekLogicInquiry: number,
  cypriotSynthesis: number
): BraidStrengthMetrics {
  // Determine braid status
  let braidStatus: 'tight' | 'stable' | 'loose' | 'fraying';
  if (braidStrength >= 0.8) {
    braidStatus = 'tight';
  } else if (braidStrength >= 0.6) {
    braidStatus = 'stable';
  } else if (braidStrength >= 0.4) {
    braidStatus = 'loose';
  } else {
    braidStatus = 'fraying';
  }

  return {
    braidStrength: Math.round(braidStrength * 1000) / 1000,
    turkishHonorScore: Math.round(turkishHonorScore * 1000) / 1000,
    greekLogicInquiry: Math.round(greekLogicInquiry * 1000) / 1000,
    cypriotSynthesis: Math.round(cypriotSynthesis * 1000) / 1000,
    braidStatus
  };
}

/**
 * Calculate Complete System Activation Final State
 * The Omega Key: Complete system activation state
 */
export function calculateCompleteSystemActivationFinalState(
  siyemPulse: SiyemPulseState,
  engine376: Engine376State,
  commandCenterUI: CommandCenterUIState
): CompleteSystemActivationFinalState {
  const systemFullyActivated = siyemPulse.isActive &&
    engine376.isActive &&
    commandCenterUI.isActive;

  const allComponentsActive = siyemPulse.homeostasisSentinelActivated &&
    engine376.isActive &&
    commandCenterUI.isActive;

  const omegaKeyActivated = systemFullyActivated &&
    allComponentsActive &&
    commandCenterUI.systemStatus === OMEGA_KEY_CONSTANTS.SYSTEM_STATUS_TOTAL_READINESS;

  return {
    siyemPulse,
    engine376,
    commandCenterUI,
    systemFullyActivated,
    allComponentsActive,
    omegaKeyActivated
  };
}

/**
 * Get The Lord Dictates Constant
 * `const THE_LORD_DICTATES = true;`
 */
export function getTheLordDictates(): boolean {
  return OMEGA_KEY_CONSTANTS.THE_LORD_DICTATES;
}

/**
 * Get We Steward The Rest Constant
 * `const WE_STEWARD_THE_REST = true;`
 */
export function getWeStewardTheRest(): boolean {
  return OMEGA_KEY_CONSTANTS.WE_STEWARD_THE_REST;
}
