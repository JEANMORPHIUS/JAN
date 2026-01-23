/**
 * ANCESTRAL FREQUENCY & BRAID LOGIC UTILITIES
 * Implement Law 21 and the 'Braid' multiplier
 */

import {
  LineageStabilityFactor,
  CulturalScores,
  EnvironmentalChaos,
  BraidSynthesis,
  GlobalBraidUIState,
  BraidCSSProperties,
  HeritageModuleAccess,
  CommunitySettingsAccess,
  ANCESTRAL_BRAID_CONSTANTS
} from '../types/ancestralBraid';
import { ProtocolEvent } from '../types/stewardship';

/**
 * Calculate Lineage Stability Factor
 * Law 21: Respect acts as a dampener for volatility
 * The more rooted the user, the more 'Red Tape' they can withstand
 * 
 * TRIGGER: User accesses 'Heritage' modules or 'Community' settings
 * ACTION: Apply `ancestral_weight` to the `stewardship_score`
 */
export function calculateLineageStabilityFactor(
  baseStewardshipScore: number,
  heritageModuleAccess?: HeritageModuleAccess,
  communitySettingsAccess?: CommunitySettingsAccess,
  protocolEvents?: ProtocolEvent[]
): LineageStabilityFactor {
  // Check if heritage modules or community settings accessed (trigger)
  const heritageModulesAccessed = heritageModuleAccess?.heritageModulesAccessed ?? false;
  const communitySettingsAccessed = communitySettingsAccess?.communitySettingsAccessed ?? false;
  const isActive = heritageModulesAccessed || communitySettingsAccessed;

  // Calculate ancestral weight (0-1)
  // Base: 0.5 if no access, increases with heritage/community engagement
  let ancestralWeight = 0.5; // Base
  
  if (heritageModulesAccessed) {
    ancestralWeight += 0.2; // Heritage modules add weight
  }
  
  if (communitySettingsAccessed) {
    ancestralWeight += 0.2; // Community settings add weight
  }
  
  // Law 21 compliance (Respect) adds weight
  const law21Compliance = protocolEvents?.some(e => e.law21Compliance) ?? false;
  if (law21Compliance) {
    ancestralWeight += ANCESTRAL_BRAID_CONSTANTS.LAW_21_WEIGHT;
  }

  // Clamp ancestral weight (0-1)
  ancestralWeight = Math.max(0, Math.min(1, ancestralWeight));

  // Calculate adjusted stewardship score (with ancestral weight)
  const adjustedStewardshipScore = baseStewardshipScore * 
    (1 + (ancestralWeight * (ANCESTRAL_BRAID_CONSTANTS.ANCESTRAL_WEIGHT_MULTIPLIER - 1)));
  
  // Clamp adjusted score (0-1)
  const adjustedScore = Math.max(0, Math.min(1, adjustedStewardshipScore));

  // Calculate volatility dampener (Law 21: Respect as dampener)
  // Higher ancestral weight = higher volatility dampener
  const volatilityDampener = ancestralWeight * 0.8; // 0-0.8 range

  // Calculate red tape resistance
  // Higher ancestral weight = more red tape resistance
  const redTapeResistance = 0.5 + (ancestralWeight * ANCESTRAL_BRAID_CONSTANTS.RED_TAPE_RESISTANCE_MULTIPLIER);
  const redTapeResistanceClamped = Math.max(0, Math.min(1, redTapeResistance));

  return {
    isActive,
    ancestralWeight: Math.round(ancestralWeight * 1000) / 1000,
    baseStewardshipScore,
    adjustedStewardshipScore: Math.round(adjustedScore * 1000) / 1000,
    volatilityDampener: Math.round(volatilityDampener * 1000) / 1000,
    redTapeResistance: Math.round(redTapeResistanceClamped * 1000) / 1000,
    law21Compliance,
    heritageModulesAccessed,
    communitySettingsAccessed,
    lastCalculated: new Date().toISOString()
  };
}

/**
 * Calculate Cultural Scores
 * Turkish honor score, Greek logic inquiry
 */
export function calculateCulturalScores(
  protocolEvents?: ProtocolEvent[],
  stewardshipScore?: number
): CulturalScores {
  // Calculate Turkish honor score (0-1)
  // Based on Law 5 (Word is Bond) and Law 37 (Finish What You Begin)
  const turkishHonorScore = protocolEvents?.filter(e => e.law5Compliance && e.law37Compliance).length / 
    Math.max(1, protocolEvents?.length ?? 1);

  // Calculate Greek logic inquiry (0-1)
  // Based on Law 13 (Listen Before You Speak) and inquiry tradition
  const greekLogicInquiry = protocolEvents?.filter(e => e.law13Compliance).length / 
    Math.max(1, protocolEvents?.length ?? 1);

  // Calculate Cypriot synthesis (combination of Turkish and Greek)
  const cypriotSynthesis = (turkishHonorScore + greekLogicInquiry) / 2;

  // Calculate Jewish inquiry tradition (0-1)
  // Based on stewardship score and inquiry patterns
  const jewishInquiryTradition = stewardshipScore ?? 0.5;

  // Calculate overall cultural braid strength
  const overallCulturalStrength = (turkishHonorScore + greekLogicInquiry + cypriotSynthesis + jewishInquiryTradition) / 4;

  return {
    turkishHonorScore: Math.round(turkishHonorScore * 1000) / 1000,
    greekLogicInquiry: Math.round(greekLogicInquiry * 1000) / 1000,
    cypriotSynthesis: Math.round(cypriotSynthesis * 1000) / 1000,
    jewishInquiryTradition: Math.round(jewishInquiryTradition * 1000) / 1000,
    overallCulturalStrength: Math.round(overallCulturalStrength * 1000) / 1000
  };
}

/**
 * Calculate Environmental Chaos
 * Chaos factor that affects braid strength
 */
export function calculateEnvironmentalChaos(
  redTapeEventsCount: number,
  systemErrorsCount: number,
  externalInterferenceCount: number
): EnvironmentalChaos {
  // Calculate chaos level (0-1)
  // Higher counts = higher chaos
  const totalChaosEvents = redTapeEventsCount + systemErrorsCount + externalInterferenceCount;
  const chaosLevel = Math.min(1, ANCESTRAL_BRAID_CONSTANTS.ENVIRONMENTAL_CHAOS_BASE + 
    (totalChaosEvents * 0.1));

  // Generate chaos description
  let chaosDescription = '';
  if (chaosLevel < 0.3) {
    chaosDescription = 'Low chaos. System stable.';
  } else if (chaosLevel < 0.6) {
    chaosDescription = 'Medium chaos. Some interference detected.';
  } else if (chaosLevel < 0.8) {
    chaosDescription = 'High chaos. Multiple red tape events.';
  } else {
    chaosDescription = 'Critical chaos. System under heavy interference.';
  }

  return {
    chaosLevel: Math.round(chaosLevel * 1000) / 1000,
    redTapeEventsCount,
    systemErrorsCount,
    externalInterferenceCount,
    chaosDescription
  };
}

/**
 * Calculate Braid Synthesis
 * The Braid multiplier: (turkish_honor_score * greek_logic_inquiry) / environmental_chaos
 * 
 * IF (braid_strength > threshold):
 * THEN Unlock 'Advanced Stewardship' permissions
 * ELSE Trigger Pierre_Voice: "The Braid is fraying. Seek the logic in the honor."
 */
export function calculateBraidSynthesis(
  culturalScores: CulturalScores,
  environmentalChaos: EnvironmentalChaos,
  braidThreshold: number = ANCESTRAL_BRAID_CONSTANTS.BRAID_THRESHOLD
): BraidSynthesis {
  // Calculate numerator: turkish_honor_score * greek_logic_inquiry
  const numerator = culturalScores.turkishHonorScore * culturalScores.greekLogicInquiry;

  // Calculate denominator: environmental_chaos (with minimum to avoid division by zero)
  const denominator = Math.max(ANCESTRAL_BRAID_CONSTANTS.ENVIRONMENTAL_CHAOS_BASE, environmentalChaos.chaosLevel);

  // Calculate braid strength: numerator / denominator
  const braidStrength = numerator / denominator;
  const braidStrengthClamped = Math.max(0, Math.min(1, braidStrength));

  // Check if braid strength above threshold
  const isAboveThreshold = braidStrengthClamped > braidThreshold;

  // Advanced stewardship permissions unlocked if above threshold
  const advancedStewardshipUnlocked = isAboveThreshold;

  // Pierre voice message (if braid fraying)
  let pierreVoiceMessage: string | undefined;
  if (!isAboveThreshold && braidStrengthClamped < ANCESTRAL_BRAID_CONSTANTS.MIN_BRAID_STRENGTH) {
    pierreVoiceMessage = "The Braid is fraying. Seek the logic in the honor.";
  }

  return {
    braidStrength: Math.round(braidStrengthClamped * 1000) / 1000,
    culturalScores,
    environmentalChaos,
    calculation: {
      numerator: Math.round(numerator * 1000) / 1000,
      denominator: Math.round(denominator * 1000) / 1000,
      braidStrength: Math.round(braidStrengthClamped * 1000) / 1000
    },
    braidThreshold,
    isAboveThreshold,
    advancedStewardshipUnlocked,
    pierreVoiceMessage,
    lastCalculated: new Date().toISOString()
  };
}

/**
 * Calculate Global Braid UI State
 * Dynamic CSS visualization based on Law 5 and Law 13 consistency
 */
export function calculateGlobalBraidUIState(
  law5Consistency: number,
  law13Consistency: number
): GlobalBraidUIState {
  // Calculate combined consistency (average)
  const combinedConsistency = (law5Consistency + law13Consistency) / 2;

  // Calculate braid tightness (0-1)
  // Higher consistency = tighter braid
  const braidTightness = combinedConsistency;

  // Determine braid visual state
  let braidVisualState: 'tight' | 'stable' | 'loose' | 'fraying';
  if (braidTightness >= 0.8) {
    braidVisualState = 'tight';
  } else if (braidTightness >= 0.6) {
    braidVisualState = 'stable';
  } else if (braidTightness >= 0.4) {
    braidVisualState = 'loose';
  } else {
    braidVisualState = 'fraying';
  }

  // Determine braid color based on state
  let braidColor: string;
  switch (braidVisualState) {
    case 'tight':
      braidColor = '#00ff00'; // Green
      break;
    case 'stable':
      braidColor = '#ffff00'; // Yellow
      break;
    case 'loose':
      braidColor = '#ff9900'; // Orange
      break;
    case 'fraying':
      braidColor = '#ff0000'; // Red
      break;
  }

  // Calculate braid animation speed (faster when loose/fraying)
  let braidAnimationSpeed: string;
  if (braidVisualState === 'fraying') {
    braidAnimationSpeed = '0.5s'; // Fast, urgent
  } else if (braidVisualState === 'loose') {
    braidAnimationSpeed = '1s'; // Moderate
  } else if (braidVisualState === 'stable') {
    braidAnimationSpeed = '2s'; // Slow, steady
  } else {
    braidAnimationSpeed = '3s'; // Very slow, calm
  }

  // Calculate braid CSS properties
  const braidCSSProperties = calculateBraidCSSProperties(
    braidVisualState,
    braidTightness,
    braidColor,
    braidAnimationSpeed
  );

  return {
    isActive: true,
    braidTightness: Math.round(braidTightness * 1000) / 1000,
    law5Consistency: Math.round(law5Consistency * 1000) / 1000,
    law13Consistency: Math.round(law13Consistency * 1000) / 1000,
    combinedConsistency: Math.round(combinedConsistency * 1000) / 1000,
    braidCSSProperties,
    braidVisualState,
    braidColor,
    braidAnimationSpeed
  };
}

/**
 * Calculate Braid CSS Properties
 * Dynamic CSS for Global Braid visualization
 */
function calculateBraidCSSProperties(
  braidVisualState: 'tight' | 'stable' | 'loose' | 'fraying',
  braidTightness: number,
  braidColor: string,
  animationSpeed: string
): BraidCSSProperties {
  // Braid width (always 100%)
  const width = '100%';

  // Braid height (varies with tightness: 4px tight, 2px loose)
  const height = `${2 + (braidTightness * 2)}px`;

  // Braid background gradient (varies with state)
  let background: string;
  switch (braidVisualState) {
    case 'tight':
      background = `linear-gradient(90deg, ${braidColor} 0%, ${braidColor}cc 50%, ${braidColor} 100%)`;
      break;
    case 'stable':
      background = `linear-gradient(90deg, ${braidColor} 0%, ${braidColor}99 50%, ${braidColor} 100%)`;
      break;
    case 'loose':
      background = `linear-gradient(90deg, ${braidColor} 0%, ${braidColor}77 50%, ${braidColor} 100%)`;
      break;
    case 'fraying':
      background = `linear-gradient(90deg, ${braidColor} 0%, ${braidColor}55 50%, ${braidColor} 100%)`;
      break;
  }

  // Braid border radius (tighter = more rounded)
  const borderRadius = `${1 + (braidTightness * 1)}px`;

  // Braid animation duration
  const animationDuration = animationSpeed;

  // Braid animation timing function
  const animationTimingFunction = braidVisualState === 'fraying' ? 'ease-in-out' : 'linear';

  // Braid transform scale (tight = 1.0, loose = 0.8)
  const transformScale = 0.8 + (braidTightness * 0.2);

  // Braid opacity (tight = 1.0, fraying = 0.6)
  const opacity = 0.6 + (braidTightness * 0.4);

  return {
    width,
    height,
    color: braidColor,
    background,
    borderRadius,
    animationDuration,
    animationTimingFunction,
    transformScale: Math.round(transformScale * 1000) / 1000,
    opacity: Math.round(opacity * 1000) / 1000
  };
}
