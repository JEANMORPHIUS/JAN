/**
 * COMPLETE SYSTEM ACTIVATION (THE OMEGA KEY) TYPES
 * Launch the full 376-Day Stewardship Engine
 * 
 * Components:
 * - The_Siyem_Pulse: Homeostasis_Sentinel activation, biological_ledger sync
 * - The 376 Engine: Daily stewardship module, Law 37 progression
 * - Command Center UI: Full dashboard activation
 * - Permanent Directive: THE_LORD_DICTATES, WE_STEWARD_THE_REST
 */

import { HealthMetrics, EarthAlignment } from './index';
import { CommunityNode } from './expansionPhase';
import { ProtocolEvent } from './stewardship';

/**
 * The Siyem Pulse State
 * Activate the `Homeostasis_Sentinel` across all community nodes
 * Sync `biological_ledger` with `ancestral_frequency_api`
 */
export interface SiyemPulseState {
  /** Is pulse active? */
  isActive: boolean;
  /** Homeostasis Sentinel activated across all nodes? */
  homeostasisSentinelActivated: boolean;
  /** Active community nodes */
  activeCommunityNodes: CommunityNode[];
  /** Biological ledger synced? */
  biologicalLedgerSynced: boolean;
  /** Ancestral frequency API synced? */
  ancestralFrequencyAPISynced: boolean;
  /** Sync status */
  syncStatus: SyncStatus;
  /** Pulse timestamp */
  pulseTimestamp: string;
  /** Last sync timestamp */
  lastSyncTimestamp?: string;
}

/**
 * Sync Status
 * Status of synchronization between biological_ledger and ancestral_frequency_api
 */
export interface SyncStatus {
  /** Is synced? */
  isSynced: boolean;
  /** Sync percentage (0-100) */
  syncPercentage: number;
  /** Last successful sync timestamp */
  lastSuccessfulSyncTimestamp?: string;
  /** Sync errors count */
  syncErrorsCount: number;
  /** Sync status description */
  syncStatusDescription: string;
}

/**
 * The 376 Engine State
 * Daily stewardship module with Law 37 progression
 * 
 * `let current_lesson = getDailyStewardshipModule();`
 * IF (StewardshipScore < 1.0): Pause lesson progression
 * NOTE: In the Racon, you don't 'advance' until you've 'finished' (Law 37)
 */
export interface Engine376State {
  /** Is engine active? */
  isActive: boolean;
  /** Current lesson number (1-376) */
  currentLesson: number;
  /** Daily stewardship module */
  dailyStewardshipModule: DailyStewardshipModule;
  /** Stewardship score (0-1) */
  stewardshipScore: number;
  /** Can advance to next lesson? */
  canAdvance: boolean;
  /** Lesson progression paused? */
  lessonProgressionPaused: boolean;
  /** Pause reason */
  pauseReason?: string;
  /** Law 37 compliance: Finish what you begin */
  law37Compliance: boolean;
  /** Lessons completed */
  lessonsCompleted: number[];
  /** Total lessons (376) */
  totalLessons: number;
  /** Progress percentage (0-100) */
  progressPercentage: number;
  /** Last lesson update timestamp */
  lastLessonUpdateTimestamp?: string;
}

/**
 * Daily Stewardship Module
 * Current lesson module for today
 */
export interface DailyStewardshipModule {
  /** Module ID */
  id: string;
  /** Lesson number (1-376) */
  lessonNumber: number;
  /** Module name */
  moduleName: string;
  /** Module content */
  moduleContent: string;
  /** Module requirements */
  requirements: string[];
  /** Completion criteria */
  completionCriteria: string[];
  /** Is completed? */
  isCompleted: boolean;
  /** Completion timestamp */
  completionTimestamp?: string;
}

/**
 * Command Center UI State
 * Full dashboard activation: Glucose, Lunar Phase, Community Integrity, and Braid Strength
 * Set `system_status = 'TOTAL_READINESS'`
 */
export interface CommandCenterUIState {
  /** Is UI active? */
  isActive: boolean;
  /** System status */
  systemStatus: SystemStatus;
  /** Dashboard components */
  dashboardComponents: DashboardComponent[];
  /** Glucose metrics */
  glucoseMetrics: GlucoseMetrics;
  /** Lunar phase */
  lunarPhase: LunarPhase;
  /** Community integrity */
  communityIntegrity: CommunityIntegrityMetrics;
  /** Braid strength */
  braidStrength: BraidStrengthMetrics;
  /** Last update timestamp */
  lastUpdateTimestamp?: string;
}

/**
 * System Status
 */
export type SystemStatus = 'TOTAL_READINESS' | 'READY' | 'PREPARING' | 'INITIALIZING' | 'INACTIVE';

/**
 * Dashboard Component
 */
export interface DashboardComponent {
  /** Component ID */
  id: string;
  /** Component name */
  name: string;
  /** Component type */
  type: 'glucose' | 'lunar_phase' | 'community_integrity' | 'braid_strength' | 'other';
  /** Component status */
  status: 'active' | 'inactive' | 'loading' | 'error';
  /** Component data */
  data: any;
}

/**
 * Glucose Metrics
 */
export interface GlucoseMetrics {
  /** Current glucose (mmol/L) */
  currentGlucose: number;
  /** Average glucose (mmol/L) */
  averageGlucose: number;
  /** Glucose range */
  glucoseRange: {
    min: number;
    max: number;
  };
  /** Glucose stability score (0-1) */
  stabilityScore: number;
  /** Glucose status */
  glucoseStatus: 'optimal' | 'stable' | 'warning' | 'critical';
}

/**
 * Lunar Phase
 */
export interface LunarPhase {
  /** Lunar phase */
  phase: 'new_moon' | 'waxing' | 'full_moon' | 'waning';
  /** Days from new moon */
  daysFromNewMoon: number;
  /** Lunar intensity (0-100) */
  lunarIntensity: number;
  /** Next phase change date */
  nextPhaseChangeDate: string;
}

/**
 * Community Integrity Metrics
 */
export interface CommunityIntegrityMetrics {
  /** Overall integrity score (0-1) */
  overallIntegrity: number;
  /** Integrity by community */
  integrityByCommunity: Map<CommunityNode, number>;
  /** Communities at risk */
  communitiesAtRisk: CommunityNode[];
  /** Integrity status */
  integrityStatus: 'excellent' | 'good' | 'moderate' | 'poor' | 'critical';
}

/**
 * Braid Strength Metrics
 */
export interface BraidStrengthMetrics {
  /** Braid strength (0-1) */
  braidStrength: number;
  /** Turkish honor score (0-1) */
  turkishHonorScore: number;
  /** Greek logic inquiry (0-1) */
  greekLogicInquiry: number;
  /** Cypriot synthesis (0-1) */
  cypriotSynthesis: number;
  /** Braid status */
  braidStatus: 'tight' | 'stable' | 'loose' | 'fraying';
}

/**
 * Complete System Activation Final State
 * The Omega Key: Complete system activation state
 */
export interface CompleteSystemActivationFinalState {
  /** The Siyem Pulse */
  siyemPulse: SiyemPulseState;
  /** The 376 Engine */
  engine376: Engine376State;
  /** Command Center UI */
  commandCenterUI: CommandCenterUIState;
  /** System fully activated? */
  systemFullyActivated: boolean;
  /** All components active? */
  allComponentsActive: boolean;
  /** Omega Key activated? */
  omegaKeyActivated: boolean;
}

/**
 * Constants
 */
export const OMEGA_KEY_CONSTANTS = {
  /** Total lessons (376) */
  TOTAL_LESSONS: 376,
  /** Minimum stewardship score for progression (1.0) */
  MIN_STEWARDSHIP_SCORE_FOR_PROGRESSION: 1.0,
  /** System status: TOTAL_READINESS */
  SYSTEM_STATUS_TOTAL_READINESS: 'TOTAL_READINESS' as SystemStatus,
  /** The Lord dictates flag */
  THE_LORD_DICTATES: true,
  /** We steward the rest flag */
  WE_STEWARD_THE_REST: true
} as const;
