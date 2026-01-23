/**
 * ANCESTRAL FREQUENCY & BRAID LOGIC TYPES
 * Implement Law 21 and the 'Braid' multiplier
 * 
 * Components:
 * - Lineage_Stability_Factor: Ancestral weight applied to stewardship score
 * - Braid_Synthesis: Turkish honor score, Greek logic inquiry, environmental chaos
 * - Global Braid UI: Dynamic CSS visualization based on Law 5 and Law 13 consistency
 */

/**
 * Lineage Stability Factor
 * Law 21: Respect acts as a dampener for volatility
 * The more rooted the user, the more 'Red Tape' they can withstand
 */
export interface LineageStabilityFactor {
  /** Is lineage stability active? */
  isActive: boolean;
  /** Ancestral weight (0-1) */
  ancestralWeight: number;
  /** Base stewardship score */
  baseStewardshipScore: number;
  /** Adjusted stewardship score (with ancestral weight) */
  adjustedStewardshipScore: number;
  /** Volatility dampener (0-1) - higher = more stability */
  volatilityDampener: number;
  /** Red tape resistance threshold (0-1) - higher = can withstand more red tape */
  redTapeResistance: number;
  /** Law 21 compliance (Respect) */
  law21Compliance: boolean;
  /** Heritage modules accessed? */
  heritageModulesAccessed: boolean;
  /** Community settings accessed? */
  communitySettingsAccessed: boolean;
  /** Last calculation timestamp */
  lastCalculated?: string;
}

/**
 * Cultural Scores
 * Turkish honor score, Greek logic inquiry
 */
export interface CulturalScores {
  /** Turkish honor score (0-1) */
  turkishHonorScore: number;
  /** Greek logic inquiry (0-1) */
  greekLogicInquiry: number;
  /** Cypriot synthesis (0-1) - combination of Turkish and Greek */
  cypriotSynthesis: number;
  /** Jewish inquiry tradition (0-1) */
  jewishInquiryTradition: number;
  /** Overall cultural braid strength */
  overallCulturalStrength: number;
}

/**
 * Environmental Chaos
 * Chaos factor that affects braid strength
 */
export interface EnvironmentalChaos {
  /** Chaos level (0-1) - higher = more chaos */
  chaosLevel: number;
  /** Red tape events count */
  redTapeEventsCount: number;
  /** System errors count */
  systemErrorsCount: number;
  /** External interference count */
  externalInterferenceCount: number;
  /** Chaos description */
  chaosDescription: string;
}

/**
 * Braid Synthesis
 * The Braid multiplier: (turkish_honor_score * greek_logic_inquiry) / environmental_chaos
 */
export interface BraidSynthesis {
  /** Braid strength (0-1) */
  braidStrength: number;
  /** Cultural scores */
  culturalScores: CulturalScores;
  /** Environmental chaos */
  environmentalChaos: EnvironmentalChaos;
  /** Braid synthesis calculation */
  calculation: {
    numerator: number;  // turkish_honor_score * greek_logic_inquiry
    denominator: number; // environmental_chaos
    braidStrength: number;
  };
  /** Braid threshold (0-1) */
  braidThreshold: number;
  /** Is braid strength above threshold? */
  isAboveThreshold: boolean;
  /** Advanced stewardship permissions unlocked? */
  advancedStewardshipUnlocked: boolean;
  /** Pierre voice message (if braid fraying) */
  pierreVoiceMessage?: string;
  /** Last calculation timestamp */
  lastCalculated?: string;
}

/**
 * Global Braid UI State
 * Dynamic CSS visualization based on Law 5 and Law 13 consistency
 */
export interface GlobalBraidUIState {
  /** Is braid UI active? */
  isActive: boolean;
  /** Braid tightness (0-1) - higher = tighter braid */
  braidTightness: number;
  /** Law 5 consistency (Word is Bond) (0-1) */
  law5Consistency: number;
  /** Law 13 consistency (Listen Before You Speak) (0-1) */
  law13Consistency: number;
  /** Combined consistency (0-1) */
  combinedConsistency: number;
  /** Braid CSS properties */
  braidCSSProperties: BraidCSSProperties;
  /** Braid visual state */
  braidVisualState: 'tight' | 'stable' | 'loose' | 'fraying';
  /** Braid color (based on state) */
  braidColor: string;
  /** Braid animation speed (CSS animation-duration) */
  braidAnimationSpeed: string;
}

/**
 * Braid CSS Properties
 * Dynamic CSS for Global Braid visualization
 */
export interface BraidCSSProperties {
  /** Braid width (CSS width) */
  width: string;  // e.g., '100%'
  /** Braid height (CSS height) */
  height: string;  // e.g., '4px'
  /** Braid color (CSS color) */
  color: string;  // e.g., '#00ff00'
  /** Braid background gradient (CSS background) */
  background: string;  // e.g., 'linear-gradient(...)'
  /** Braid border radius (CSS border-radius) */
  borderRadius: string;  // e.g., '2px'
  /** Braid animation duration (CSS animation-duration) */
  animationDuration: string;  // e.g., '2s'
  /** Braid animation timing function (CSS animation-timing-function) */
  animationTimingFunction: string;  // e.g., 'ease-in-out'
  /** Braid transform scale (CSS transform scale) */
  transformScale: number;  // e.g., 1.0 (tight) to 0.8 (loose)
  /** Braid opacity (CSS opacity) */
  opacity: number;  // 0-1
}

/**
 * Heritage Module Access
 * Trigger for Lineage Stability Factor
 */
export interface HeritageModuleAccess {
  /** Heritage modules accessed? */
  heritageModulesAccessed: boolean;
  /** Access timestamp */
  accessTimestamp: string;
  /** Modules accessed */
  modulesAccessed: string[];
}

/**
 * Community Settings Access
 * Trigger for Lineage Stability Factor
 */
export interface CommunitySettingsAccess {
  /** Community settings accessed? */
  communitySettingsAccessed: boolean;
  /** Access timestamp */
  accessTimestamp: string;
  /** Settings accessed */
  settingsAccessed: string[];
}

/**
 * Constants
 */
export const ANCESTRAL_BRAID_CONSTANTS = {
  /** Braid threshold for Advanced Stewardship unlock */
  BRAID_THRESHOLD: 0.7,
  /** Minimum braid strength for stability */
  MIN_BRAID_STRENGTH: 0.5,
  /** Law 21 weight (Respect as volatility dampener) */
  LAW_21_WEIGHT: 0.3,
  /** Ancestral weight multiplier (0-1) */
  ANCESTRAL_WEIGHT_MULTIPLIER: 1.2,
  /** Environmental chaos base (minimum chaos level) */
  ENVIRONMENTAL_CHAOS_BASE: 0.1,
  /** Red tape resistance multiplier (per ancestral weight point) */
  RED_TAPE_RESISTANCE_MULTIPLIER: 0.15
} as const;
