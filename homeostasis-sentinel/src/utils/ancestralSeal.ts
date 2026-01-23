/**
 * WEEK 2 ANCESTRAL SEAL UTILITIES
 * Finalize Heritage Integration and Rooting Logic
 */

import {
  AncestralValidationGateState,
  RootedKnowledgeArchive,
  Week2BiologicalData,
  Week2StewardshipData,
  DataStabilityState,
  AncestralFrequency,
  VarianceComparison,
  UIRootsVisualizationState,
  Root,
  RootsCSSProperties,
  ANCESTRAL_SEAL_CONSTANTS,
  LONDON_COMMUNITY_NODES,
  COMMAND_CENTER_COORDINATES
} from '../types/ancestralSeal';
import { HealthMetrics } from '../types';
import { EarthAlignment } from '../types/earthAlignment';
import { ProtocolEvent } from '../types/stewardship';
import { LOCATION_COORDINATES, CommunityNode } from '../types/expansionPhase';
import { parseISO, addDays, format, getHours, getMinutes } from 'date-fns';

/**
 * Calculate Ancestral Validation Gate State
 * Day 14 trigger: stewardship_score > 0.8 AND word_bond_consistency == 100%
 * 
 * TRIGGER: End of Day 14
 * REQUIREMENT: `stewardship_score` > 0.8 AND `word_bond_consistency` == 100%
 * ACTION: Archive Week 2 data as 'Rooted Knowledge'. Unlock 'Community Expansion' (Week 3).
 */
export function calculateAncestralValidationGateState(
  week2StartDate: Date,
  currentTimestamp: string,
  stewardshipScore: number,
  wordBondConsistency: number
): AncestralValidationGateState {
  const week2EndDate = addDays(week2StartDate, ANCESTRAL_SEAL_CONSTANTS.WEEK_2_DURATION_DAYS);
  const day14EndTimestamp = format(week2EndDate, 'yyyy-MM-dd') + 
    `T${ANCESTRAL_SEAL_CONSTANTS.DAY_14_END_HOUR}:${ANCESTRAL_SEAL_CONSTANTS.DAY_14_END_MINUTE}:00`;

  const currentDate = parseISO(currentTimestamp);
  const currentDay = Math.ceil((currentDate.getTime() - week2StartDate.getTime()) / (1000 * 60 * 60 * 24));

  // Check if Day 14 end (23:59)
  const isDay14End = currentDay === ANCESTRAL_SEAL_CONSTANTS.WEEK_2_DURATION_DAYS &&
    getHours(currentDate) === ANCESTRAL_SEAL_CONSTANTS.DAY_14_END_HOUR &&
    getMinutes(currentDate) >= ANCESTRAL_SEAL_CONSTANTS.DAY_14_END_MINUTE;

  const isActive = isDay14End;

  // Word bond consistency as percentage (0-100)
  const wordBondConsistencyPercentage = wordBondConsistency * 100;

  // Check requirements
  const stewardshipScoreMet = stewardshipScore > ANCESTRAL_SEAL_CONSTANTS.MIN_STEWARDSHIP_SCORE;
  const wordBondConsistencyMet = wordBondConsistency >= ANCESTRAL_SEAL_CONSTANTS.REQUIRED_WORD_BOND_CONSISTENCY;
  const requirementsMet = stewardshipScoreMet && wordBondConsistencyMet;

  // Determine validation status
  let validationStatus: 'pending' | 'validating' | 'passed' | 'failed';
  if (!isDay14End) {
    validationStatus = 'pending';
  } else if (isDay14End && requirementsMet) {
    validationStatus = 'passed';
  } else if (isDay14End && !requirementsMet) {
    validationStatus = 'failed';
  } else {
    validationStatus = 'validating';
  }

  // Week 2 complete if validation passed
  const week2Complete = validationStatus === 'passed';
  const week2DataArchived = week2Complete;
  const rootedKnowledgeCreated = week2Complete;
  const communityExpansionUnlocked = week2Complete;

  return {
    isActive,
    currentDay,
    isDay14End,
    week2StartDate: format(week2StartDate, 'yyyy-MM-dd'),
    week2EndDate: format(week2EndDate, 'yyyy-MM-dd'),
    day14EndTimestamp,
    stewardshipScore: Math.round(stewardshipScore * 1000) / 1000,
    wordBondConsistency: Math.round(wordBondConsistency * 1000) / 1000,
    wordBondConsistencyPercentage: Math.round(wordBondConsistencyPercentage * 100) / 100,
    requirementsMet,
    validationStatus,
    week2DataArchived,
    rootedKnowledgeCreated,
    communityExpansionUnlocked,
    week2Complete,
    ...(week2Complete && { validatedAt: new Date().toISOString() })
  };
}

/**
 * Create Rooted Knowledge Archive
 * Archive Week 2 data as 'Rooted Knowledge'
 */
export function createRootedKnowledgeArchive(
  week2StartDate: Date,
  metrics: HealthMetrics[],
  protocolEvents: ProtocolEvent[],
  earthAlignmentData: EarthAlignment[],
  stewardshipScore: number,
  wordBondConsistency: number
): RootedKnowledgeArchive {
  const week2EndDate = addDays(week2StartDate, ANCESTRAL_SEAL_CONSTANTS.WEEK_2_DURATION_DAYS);
  const week2EndTimestamp = format(week2EndDate, 'yyyy-MM-dd') + 
    `T${ANCESTRAL_SEAL_CONSTANTS.DAY_14_END_HOUR}:${ANCESTRAL_SEAL_CONSTANTS.DAY_14_END_MINUTE}:00`;

  // Filter metrics for Week 2
  const week2Metrics = metrics.filter(m => {
    const metricDate = parseISO(m.date);
    return metricDate >= week2StartDate && metricDate <= week2EndDate;
  });

  // Aggregate Week 2 biological data
  const week2BiologicalData = aggregateWeek2BiologicalData(week2Metrics);

  // Aggregate Week 2 stewardship data
  const week2StewardshipData = aggregateWeek2StewardshipData(
    protocolEvents,
    stewardshipScore,
    wordBondConsistency
  );

  // Determine rooted knowledge status
  let rootedKnowledgeStatus: 'rooted' | 'partial' | 'unrooted';
  if (stewardshipScore >= ANCESTRAL_SEAL_CONSTANTS.MIN_STEWARDSHIP_SCORE &&
      wordBondConsistency >= ANCESTRAL_SEAL_CONSTANTS.REQUIRED_WORD_BOND_CONSISTENCY) {
    rootedKnowledgeStatus = 'rooted';
  } else if (stewardshipScore >= 0.6 || wordBondConsistency >= 0.8) {
    rootedKnowledgeStatus = 'partial';
  } else {
    rootedKnowledgeStatus = 'unrooted';
  }

  return {
    id: `rooted_knowledge_week2_${Date.now()}`,
    timestamp: new Date().toISOString(),
    week2Period: {
      startDate: format(week2StartDate, 'yyyy-MM-dd'),
      endDate: format(week2EndDate, 'yyyy-MM-dd')
    },
    week2BiologicalData,
    week2StewardshipData,
    week2EarthAlignmentData: earthAlignmentData,
    rootedKnowledgeStatus,
    immutable: true
  };
}

/**
 * Aggregate Week 2 Biological Data
 */
function aggregateWeek2BiologicalData(metrics: HealthMetrics[]): Week2BiologicalData {
  // Convert glucose to mmol/L if needed
  const glucoseReadings = metrics
    .filter(m => m.blood_glucose !== undefined)
    .map(m => m.blood_glucose! > 30 ? m.blood_glucose! / 18.0182 : m.blood_glucose!);

  const visionReadings = metrics.filter(m => m.vision_clarity !== undefined).map(m => m.vision_clarity!);
  const muscleReadings = metrics.filter(m => m.muscle_tension !== undefined).map(m => m.muscle_tension!);
  const breathReadings = metrics.filter(m => m.breath_quality !== undefined).map(m => m.breath_quality!);

  // Calculate glucose statistics
  const mean = glucoseReadings.length > 0
    ? glucoseReadings.reduce((sum, val) => sum + val, 0) / glucoseReadings.length
    : 0;
  const variance = glucoseReadings.length > 0
    ? glucoseReadings.reduce((sum, val) => sum + Math.pow(val - mean, 2), 0) / glucoseReadings.length
    : 0;
  const stdDev = Math.sqrt(variance);

  return {
    glucoseReadings,
    glucoseStats: {
      mean: Math.round(mean * 100) / 100,
      min: glucoseReadings.length > 0 ? Math.round(Math.min(...glucoseReadings) * 100) / 100 : 0,
      max: glucoseReadings.length > 0 ? Math.round(Math.max(...glucoseReadings) * 100) / 100 : 0,
      variance: Math.round(variance * 1000) / 1000,
      stdDev: Math.round(stdDev * 100) / 100
    },
    visionReadings,
    muscleReadings,
    breathReadings,
    dataPointCount: metrics.length
  };
}

/**
 * Aggregate Week 2 Stewardship Data
 */
function aggregateWeek2StewardshipData(
  protocolEvents: ProtocolEvent[],
  stewardshipScore: number,
  wordBondConsistency: number
): Week2StewardshipData {
  const protocolsCompleted = protocolEvents.filter(e => e.law37Compliance && e.eventType === 'completed').length;
  const protocolsAbandoned = protocolEvents.filter(e => e.eventType === 'abandoned').length;
  const law5ComplianceRate = protocolEvents.length > 0
    ? protocolEvents.filter(e => e.law5Compliance).length / protocolEvents.length
    : 0;
  const law37ComplianceRate = protocolEvents.length > 0
    ? protocolEvents.filter(e => e.law37Compliance).length / protocolEvents.length
    : 0;

  return {
    stewardshipScore,
    wordBondConsistency,
    wordBondConsistencyPercentage: Math.round(wordBondConsistency * 100),
    protocolEvents,
    protocolsCompleted,
    protocolsAbandoned,
    law5ComplianceRate: Math.round(law5ComplianceRate * 1000) / 1000,
    law37ComplianceRate: Math.round(law37ComplianceRate * 1000) / 1000
  };
}

/**
 * Calculate Data Stability State
 * Map mmol_l stability against Ancestral Frequency (Lunar/Seasonal averages)
 * 
 * IF (Variance < 10%): Log as 'Homeostatic Mastery'
 */
export function calculateDataStabilityState(
  currentGlucoseReadings: number[],
  ancestralFrequency: AncestralFrequency
): DataStabilityState {
  // Calculate current glucose statistics
  const mean = currentGlucoseReadings.length > 0
    ? currentGlucoseReadings.reduce((sum, val) => sum + val, 0) / currentGlucoseReadings.length
    : 0;
  const variance = currentGlucoseReadings.length > 0
    ? currentGlucoseReadings.reduce((sum, val) => sum + Math.pow(val - mean, 2), 0) / currentGlucoseReadings.length
    : 0;
  const stdDev = Math.sqrt(variance);

  // Calculate variance comparison
  const varianceComparison = calculateVarianceComparison(variance, ancestralFrequency.ancestralVariance);

  // Calculate variance percentage difference
  const variancePercentage = varianceComparison.variancePercentageDifference;

  // Check if variance < 10%
  const varianceBelow10Percent = variancePercentage < ANCESTRAL_SEAL_CONSTANTS.VARIANCE_THRESHOLD_PERCENT;

  // Determine stability status
  let stabilityStatus: 'mastery' | 'stable' | 'volatile' | 'unstable';
  if (varianceBelow10Percent) {
    stabilityStatus = 'mastery';
  } else if (variancePercentage < 20) {
    stabilityStatus = 'stable';
  } else if (variancePercentage < 40) {
    stabilityStatus = 'volatile';
  } else {
    stabilityStatus = 'unstable';
  }

  // Homeostatic mastery logged if variance < 10%
  const homeostaticMasteryLogged = varianceBelow10Percent;

  return {
    isActive: true,
    currentGlucoseReadings,
    currentGlucoseStats: {
      mean: Math.round(mean * 100) / 100,
      variance: Math.round(variance * 1000) / 1000,
      stdDev: Math.round(stdDev * 100) / 100
    },
    ancestralFrequency,
    varianceComparison,
    variancePercentage: Math.round(variancePercentage * 100) / 100,
    varianceBelow10Percent,
    homeostaticMasteryLogged,
    stabilityStatus,
    lastCalculated: new Date().toISOString()
  };
}

/**
 * Calculate Variance Comparison
 */
function calculateVarianceComparison(
  currentVariance: number,
  ancestralVariance: number
): VarianceComparison {
  const varianceDifference = currentVariance - ancestralVariance;
  const variancePercentageDifference = ancestralVariance > 0
    ? Math.abs((varianceDifference / ancestralVariance) * 100)
    : 0;
  const varianceWithin10Percent = variancePercentageDifference < ANCESTRAL_SEAL_CONSTANTS.VARIANCE_THRESHOLD_PERCENT;

  return {
    currentVariance: Math.round(currentVariance * 1000) / 1000,
    ancestralVariance: Math.round(ancestralVariance * 1000) / 1000,
    varianceDifference: Math.round(varianceDifference * 1000) / 1000,
    variancePercentageDifference: Math.round(variancePercentageDifference * 100) / 100,
    varianceWithin10Percent
  };
}

/**
 * Calculate Ancestral Frequency
 * Lunar/Seasonal averages for glucose stability comparison
 */
export function calculateAncestralFrequency(
  earthAlignment: EarthAlignment,
  historicalGlucoseData: number[]
): AncestralFrequency {
  // Calculate lunar average (simplified - would use historical data by lunar phase)
  const lunarAverageGlucose = historicalGlucoseData.length > 0
    ? historicalGlucoseData.reduce((sum, val) => sum + val, 0) / historicalGlucoseData.length
    : 7.0; // Default

  // Calculate seasonal average (simplified - would use historical data by season)
  const seasonalAverageGlucose = lunarAverageGlucose; // Simplified

  // Combined ancestral average
  const ancestralAverageGlucose = (lunarAverageGlucose + seasonalAverageGlucose) / 2;

  // Calculate ancestral variance (historical variance)
  const ancestralVariance = historicalGlucoseData.length > 0
    ? historicalGlucoseData.reduce((sum, val) => sum + Math.pow(val - ancestralAverageGlucose, 2), 0) / historicalGlucoseData.length
    : 1.0; // Default

  return {
    lunarAverageGlucose: Math.round(lunarAverageGlucose * 100) / 100,
    seasonalAverageGlucose: Math.round(seasonalAverageGlucose * 100) / 100,
    ancestralAverageGlucose: Math.round(ancestralAverageGlucose * 100) / 100,
    lunarPhase: earthAlignment.lunar.phase,
    seasonalPhase: earthAlignment.seasonal.season,
    ancestralVariance: Math.round(ancestralVariance * 1000) / 1000
  };
}

/**
 * Calculate UI Roots Visualization State
 * Visualise the 'Roots' extending from the Command Center to the 8 London Community nodes
 * `const WEEK_2_COMPLETE = true;`
 */
export function calculateUIRootsVisualizationState(
  week2Complete: boolean,
  communityRootStrengths?: Map<CommunityNode, number>
): UIRootsVisualizationState {
  const isActive = week2Complete && ANCESTRAL_SEAL_CONSTANTS.WEEK_2_COMPLETE;

  // Create roots from Command Center to each community node
  const roots: Root[] = LONDON_COMMUNITY_NODES.map((communityNode, index) => {
    // Get community coordinates (simplified - would come from data)
    const communityCoordinates = LOCATION_COORDINATES['London_Haringey']; // Simplified
    
    // Root strength (default 0.7, or from communityRootStrengths)
    const rootStrength = communityRootStrengths?.get(communityNode) ?? 0.7;

    // Root thickness (varies with strength: 1px to 4px)
    const rootThickness = `${1 + (rootStrength * 3)}px`;

    // Root color (varies with strength: green to yellow)
    let rootColor: string;
    if (rootStrength >= 0.8) {
      rootColor = '#00ff00'; // Green
    } else if (rootStrength >= 0.6) {
      rootColor = '#ffff00'; // Yellow
    } else {
      rootColor = '#ff9900'; // Orange
    }

    // Root opacity (varies with strength: 0.5 to 1.0)
    const rootOpacity = 0.5 + (rootStrength * 0.5);

    // Root animation duration (slower = stronger)
    const rootAnimationDuration = rootStrength >= 0.8 ? '3s' : 
      rootStrength >= 0.6 ? '2s' : '1s';

    return {
      id: `root_${communityNode}`,
      from: 'Command_Center',
      to: communityNode,
      coordinates: {
        from: COMMAND_CENTER_COORDINATES,
        to: communityCoordinates
      },
      rootStrength: Math.round(rootStrength * 1000) / 1000,
      rootThickness,
      rootColor,
      rootOpacity: Math.round(rootOpacity * 1000) / 1000,
      rootAnimationDuration
    };
  });

  // Calculate roots CSS properties
  const rootsCSSProperties = calculateRootsCSSProperties(roots);

  // Determine visualization status
  let visualizationStatus: 'active' | 'inactive' | 'pending';
  if (isActive) {
    visualizationStatus = 'active';
  } else if (week2Complete) {
    visualizationStatus = 'pending';
  } else {
    visualizationStatus = 'inactive';
  }

  return {
    isActive,
    week2Complete,
    commandCenterCoordinates: COMMAND_CENTER_COORDINATES,
    roots,
    rootsCSSProperties,
    visualizationStatus
  };
}

/**
 * Calculate Roots CSS Properties
 * Dynamic CSS for roots visualization
 */
function calculateRootsCSSProperties(roots: Root[]): RootsCSSProperties {
  // Average root strength (for overall styling)
  const averageRootStrength = roots.length > 0
    ? roots.reduce((sum, root) => sum + root.rootStrength, 0) / roots.length
    : 0.7;

  // Average root color (simplified - use green if strong)
  const strokeColor = averageRootStrength >= 0.7 ? '#00ff00' : '#ffff00';

  // Average stroke width (from root thicknesses)
  const averageStrokeWidth = roots.length > 0
    ? roots.reduce((sum, root) => {
        const width = parseFloat(root.rootThickness.replace('px', ''));
        return sum + width;
      }, 0) / roots.length
    : 2;
  const strokeWidth = `${averageStrokeWidth}px`;

  // Average root opacity
  const averageOpacity = roots.length > 0
    ? roots.reduce((sum, root) => sum + root.rootOpacity, 0) / roots.length
    : 0.7;

  // Animation duration (average of root animation durations)
  const averageAnimationDuration = averageRootStrength >= 0.8 ? '3s' : 
    averageRootStrength >= 0.6 ? '2s' : '1s';

  // Glow filter (varies with strength)
  const glowIntensity = Math.round(averageOpacity * 255);
  const filter = `drop-shadow(0 0 ${5 + (averageRootStrength * 10)}px rgba(0, ${glowIntensity}, 0, ${averageOpacity.toFixed(2)}))`;

  return {
    strokeWidth,
    strokeColor,
    strokeOpacity: Math.round(averageOpacity * 1000) / 1000,
    animationDuration: averageAnimationDuration,
    animationTimingFunction: 'linear',
    filter
  };
}

/**
 * Get Week 2 Complete Flag
 * `const WEEK_2_COMPLETE = true;`
 */
export function getWeek2Complete(): boolean {
  return ANCESTRAL_SEAL_CONSTANTS.WEEK_2_COMPLETE;
}
