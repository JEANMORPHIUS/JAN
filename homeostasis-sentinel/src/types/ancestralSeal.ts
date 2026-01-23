/**
 * WEEK 2 ANCESTRAL SEAL TYPES
 * Finalize Heritage Integration and Rooting Logic
 * 
 * Components:
 * - Ancestral_Validation_Gate: Day 14 trigger, stewardship_score > 0.8, word_bond_consistency == 100%
 * - DATA_STABILITY: Map mmol_l stability against Ancestral Frequency (Lunar/Seasonal averages)
 * - UI Roots Visualization: Command Center to 8 London Community nodes
 */

import { HealthMetrics } from './index';
import { EarthAlignment } from './earthAlignment';
import { ProtocolEvent } from './stewardship';
import { CommunityNode } from './expansionPhase';

/**
 * Ancestral Validation Gate State
 * Day 14 trigger: stewardship_score > 0.8 AND word_bond_consistency == 100%
 */
export interface AncestralValidationGateState {
  /** Is gate active? */
  isActive: boolean;
  /** Current day (1-14) */
  currentDay: number;
  /** Is Day 14 end? */
  isDay14End: boolean;
  /** Week 2 start date */
  week2StartDate: string;
  /** Week 2 end date (Day 14) */
  week2EndDate: string;
  /** Day 14 end timestamp */
  day14EndTimestamp: string;
  /** Stewardship score (0-1) */
  stewardshipScore: number;
  /** Word bond consistency (0-1, as percentage: 0-100%) */
  wordBondConsistency: number;
  /** Word bond consistency percentage (0-100) */
  wordBondConsistencyPercentage: number;
  /** Requirements met? */
  requirementsMet: boolean;
  /** Validation status */
  validationStatus: 'pending' | 'validating' | 'passed' | 'failed';
  /** Week 2 data archived? */
  week2DataArchived: boolean;
  /** Rooted knowledge created? */
  rootedKnowledgeCreated: boolean;
  /** Community expansion unlocked? (Week 3) */
  communityExpansionUnlocked: boolean;
  /** Week 2 complete? */
  week2Complete: boolean;
  /** Validation timestamp */
  validatedAt?: string;
}

/**
 * Rooted Knowledge Archive
 * Week 2 data archived as 'Rooted Knowledge'
 */
export interface RootedKnowledgeArchive {
  /** Archive ID */
  id: string;
  /** Archive timestamp */
  timestamp: string;
  /** Week 2 period */
  week2Period: {
    startDate: string;
    endDate: string;
  };
  /** Week 2 biological data */
  week2BiologicalData: Week2BiologicalData;
  /** Week 2 stewardship data */
  week2StewardshipData: Week2StewardshipData;
  /** Week 2 Earth alignment data */
  week2EarthAlignmentData: EarthAlignment[];
  /** Rooted knowledge status */
  rootedKnowledgeStatus: 'rooted' | 'partial' | 'unrooted';
  /** Archive immutable */
  immutable: true;
}

/**
 * Week 2 Biological Data
 * Archived biological data for Week 2
 */
export interface Week2BiologicalData {
  /** Glucose readings (mmol/L) */
  glucoseReadings: number[];
  /** Glucose statistics */
  glucoseStats: {
    mean: number;
    min: number;
    max: number;
    variance: number;
    stdDev: number;
  };
  /** Vision clarity readings */
  visionReadings: number[];
  /** Muscle tension readings */
  muscleReadings: number[];
  /** Breath quality readings */
  breathReadings: number[];
  /** Data point count */
  dataPointCount: number;
}

/**
 * Week 2 Stewardship Data
 * Archived stewardship data for Week 2
 */
export interface Week2StewardshipData {
  /** Stewardship score (0-1) */
  stewardshipScore: number;
  /** Word bond consistency (0-1) */
  wordBondConsistency: number;
  /** Word bond consistency percentage (0-100) */
  wordBondConsistencyPercentage: number;
  /** Protocol events */
  protocolEvents: ProtocolEvent[];
  /** Protocols completed */
  protocolsCompleted: number;
  /** Protocols abandoned */
  protocolsAbandoned: number;
  /** Law 5 compliance rate (0-1) */
  law5ComplianceRate: number;
  /** Law 37 compliance rate (0-1) */
  law37ComplianceRate: number;
}

/**
 * Data Stability State
 * Map mmol_l stability against Ancestral Frequency (Lunar/Seasonal averages)
 */
export interface DataStabilityState {
  /** Is stability check active? */
  isActive: boolean;
  /** Current mmol_l readings */
  currentGlucoseReadings: number[];
  /** Current glucose statistics */
  currentGlucoseStats: {
    mean: number;
    variance: number;
    stdDev: number;
  };
  /** Ancestral frequency (Lunar/Seasonal averages) */
  ancestralFrequency: AncestralFrequency;
  /** Variance comparison */
  varianceComparison: VarianceComparison;
  /** Variance percentage difference */
  variancePercentage: number;
  /** Variance < 10%? */
  varianceBelow10Percent: boolean;
  /** Homeostatic mastery logged? */
  homeostaticMasteryLogged: boolean;
  /** Stability status */
  stabilityStatus: 'mastery' | 'stable' | 'volatile' | 'unstable';
  /** Last calculated timestamp */
  lastCalculated?: string;
}

/**
 * Ancestral Frequency
 * Lunar/Seasonal averages for glucose stability comparison
 */
export interface AncestralFrequency {
  /** Lunar average glucose (mmol/L) */
  lunarAverageGlucose: number;
  /** Seasonal average glucose (mmol/L) */
  seasonalAverageGlucose: number;
  /** Combined ancestral average (mmol/L) */
  ancestralAverageGlucose: number;
  /** Lunar phase */
  lunarPhase: 'new_moon' | 'waxing' | 'full_moon' | 'waning';
  /** Seasonal phase */
  seasonalPhase: 'winter' | 'spring' | 'summer' | 'autumn';
  /** Ancestral frequency variance (historical) */
  ancestralVariance: number;
}

/**
 * Variance Comparison
 * Compare current variance with ancestral variance
 */
export interface VarianceComparison {
  /** Current variance */
  currentVariance: number;
  /** Ancestral variance */
  ancestralVariance: number;
  /** Variance difference */
  varianceDifference: number;
  /** Variance percentage difference */
  variancePercentageDifference: number;
  /** Is variance within 10% of ancestral? */
  varianceWithin10Percent: boolean;
}

/**
 * UI Roots Visualization State
 * Visualise the 'Roots' extending from the Command Center to the 8 London Community nodes
 */
export interface UIRootsVisualizationState {
  /** Is visualization active? */
  isActive: boolean;
  /** Week 2 complete? */
  week2Complete: boolean;
  /** Command Center coordinates */
  commandCenterCoordinates: {
    latitude: number;
    longitude: number;
  };
  /** Roots (connections to community nodes) */
  roots: Root[];
  /** Roots CSS properties */
  rootsCSSProperties: RootsCSSProperties;
  /** Visualization status */
  visualizationStatus: 'active' | 'inactive' | 'pending';
}

/**
 * Root
 * Connection from Command Center to a Community Node
 */
export interface Root {
  /** Root ID */
  id: string;
  /** Source: Command Center */
  from: 'Command_Center';
  /** Target: Community Node */
  to: CommunityNode;
  /** Root coordinates */
  coordinates: {
    from: { latitude: number; longitude: number };
    to: { latitude: number; longitude: number };
  };
  /** Root strength (0-1) - based on community connection */
  rootStrength: number;
  /** Root thickness (CSS width) */
  rootThickness: string;  // e.g., '2px'
  /** Root color (CSS color) */
  rootColor: string;  // e.g., '#00ff00'
  /** Root opacity (CSS opacity) */
  rootOpacity: number;  // 0-1
  /** Root animation duration (CSS animation-duration) */
  rootAnimationDuration: string;  // e.g., '2s'
}

/**
 * Roots CSS Properties
 * Dynamic CSS for roots visualization
 */
export interface RootsCSSProperties {
  /** Root line width (CSS stroke-width) */
  strokeWidth: string;  // e.g., '2px'
  /** Root line color (CSS stroke) */
  strokeColor: string;  // e.g., '#00ff00'
  /** Root line opacity (CSS stroke-opacity) */
  strokeOpacity: number;  // 0-1
  /** Root animation duration (CSS animation-duration) */
  animationDuration: string;  // e.g., '2s'
  /** Root animation timing function (CSS animation-timing-function) */
  animationTimingFunction: string;  // e.g., 'linear'
  /** Root filter (CSS filter) - glow effect */
  filter: string;  // e.g., 'drop-shadow(0 0 10px rgba(0, 255, 0, 0.8))'
}

/**
 * Constants
 */
export const ANCESTRAL_SEAL_CONSTANTS = {
  /** Week 2 duration (14 days) */
  WEEK_2_DURATION_DAYS: 14,
  /** Day 14 end hour (23) */
  DAY_14_END_HOUR: 23,
  /** Day 14 end minute (59) */
  DAY_14_END_MINUTE: 59,
  /** Minimum stewardship score for validation (0.8) */
  MIN_STEWARDSHIP_SCORE: 0.8,
  /** Required word bond consistency (100%) */
  REQUIRED_WORD_BOND_CONSISTENCY: 1.0,
  /** Variance threshold for homeostatic mastery (10%) */
  VARIANCE_THRESHOLD_PERCENT: 10,
  /** Week 2 complete flag */
  WEEK_2_COMPLETE: true
} as const;

/**
 * London Community Nodes (8)
 */
export const LONDON_COMMUNITY_NODES: CommunityNode[] = [
  'Community_1',
  'Community_2',
  'Community_3',
  'Community_4',
  'Community_5',
  'Community_6',
  'Community_7',
  'Community_8'
] as const;

/**
 * Command Center Coordinates (London Haringey)
 */
export const COMMAND_CENTER_COORDINATES = {
  latitude: 51.5894,
  longitude: -0.1106
} as const;
