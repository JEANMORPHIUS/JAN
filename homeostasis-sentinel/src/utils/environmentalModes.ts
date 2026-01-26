/** * * ENVIRONMENTAL & COMMUNICATION MODES UTILITIES
 *  * Implement 'Silence' and 'Braid' logic gates
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
 * PANGEA IS THE TABLE.
 * YOU DON'T BETRAY THE TABLE.
 * 
 * THE TRUTH:
 * WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
 * THE REST IS UP TO BABA X.*/

import {
  RamizSilenceProtocol,
  JeanBraidDefense,
  RedTapeCommunicationEvent,
  SoilConnection,
  ThresholdIntegrity,
  EnvironmentalModeState,
  EnvironmentalMode,
  RED_TAPE_KEYWORDS,
  ENVIRONMENTAL_CONSTANTS
} from '../types/environmentalModes';
import { HealthMetrics } from '../types';
import { EarthAlignment } from '../types/earthAlignment';
import { calculateEarthAlignment } from './earthRhythms';
import { parseISO } from 'date-fns';

/**
 * Calculate Glucose Volatility
 * Calculate percentage volatility from glucose readings
 */
export function calculateGlucoseVolatility(metrics: HealthMetrics[]): number {
  const glucoseReadings = metrics
    .filter(m => m.blood_glucose !== undefined)
    .map(m => m.blood_glucose!)
    .sort((a, b) => a - b);

  if (glucoseReadings.length < 2) {
    return 0;
  }

  const mean = glucoseReadings.reduce((sum, val) => sum + val, 0) / glucoseReadings.length;
  const variance = glucoseReadings.reduce((sum, val) => sum + Math.pow(val - mean, 2), 0) / glucoseReadings.length;
  const standardDeviation = Math.sqrt(variance);
  
  // Volatility as percentage: (stdDev / mean) * 100
  const volatility = mean > 0 ? (standardDeviation / mean) * 100 : 0;

  return Math.round(volatility * 100) / 100;
}

/**
 * Calculate Ramiz Silence Protocol
 * TRIGGER: High `muscle_tension` OR `glucose_volatility` > 20%
 * ACTION: Dim UI, silence non-critical notifications
 * MESSAGE: "Law 11 Active. Wisdom lives in the quiet. Reconnect with the soil."
 */
export function calculateRamizSilenceProtocol(
  metrics: HealthMetrics[],
  muscleTensionThreshold: number = ENVIRONMENTAL_CONSTANTS.MUSCLE_TENSION_THRESHOLD,
  glucoseVolatilityThreshold: number = ENVIRONMENTAL_CONSTANTS.GLUCOSE_VOLATILITY_THRESHOLD
): RamizSilenceProtocol {
  const latest = metrics[metrics.length - 1];
  const muscleTension = latest.muscle_tension ?? 0;
  const glucoseVolatility = calculateGlucoseVolatility(metrics);

  // Check trigger conditions
  const highMuscleTension = muscleTension >= muscleTensionThreshold;
  const highGlucoseVolatility = glucoseVolatility > glucoseVolatilityThreshold;

  const isActive = highMuscleTension || highGlucoseVolatility;

  return {
    isActive,
    triggers: {
      highMuscleTension,
      highGlucoseVolatility
    },
    triggerValues: {
      muscleTension,
      glucoseVolatility
    },
    uiState: {
      dimmed: isActive,
      notificationsSilenced: isActive,
      dimmingLevel: isActive ? ENVIRONMENTAL_CONSTANTS.SILENCE_DIMMING_LEVEL : 100
    },
    message: isActive 
      ? 'Law 11 Active. Wisdom lives in the quiet. Reconnect with the soil.'
      : 'Silence Protocol inactive. Normal operation.',
    lawReference: 'Law 11: Wisdom Lives in the Quiet',
    ...(isActive && { activatedAt: new Date().toISOString() })
  };
}

/**
 * Detect Red Tape Keywords
 * Check if message contains Red Tape keywords
 */
export function detectRedTapeKeywords(message: string): string[] {
  const messageLower = message.toLowerCase();
  const detectedKeywords: string[] = [];

  RED_TAPE_KEYWORDS.forEach(keyword => {
    if (messageLower.includes(keyword.toLowerCase())) {
      detectedKeywords.push(keyword);
    }
  });

  return detectedKeywords;
}

/**
 * Calculate Jean Braid Defense
 * TRIGGER: Detection of 'Red Tape' keywords in external communications/API errors
 * ACTION: Switch to 'Shell' templates for outgoing logs while maintaining 'Seed' integrity in the DB
 * LOG: "Threshold Defense initiated. Bilingual Braid active."
 */
export function calculateJeanBraidDefense(
  redTapeEvents: RedTapeCommunicationEvent[],
  currentCommunicationMode: 'Shell' | 'Seed' = 'Seed'
): JeanBraidDefense {
  const redTapeKeywordsDetected = new Set<string>();
  const recentRedTapeEvents = redTapeEvents.filter(e => {
    const eventDate = parseISO(e.timestamp);
    const daysSinceEvent = (Date.now() - eventDate.getTime()) / (1000 * 60 * 60 * 24);
    return daysSinceEvent <= 7; // Events from last 7 days
  });

  // Collect all detected keywords
  recentRedTapeEvents.forEach(event => {
    event.keywords.forEach(keyword => redTapeKeywordsDetected.add(keyword));
  });

  const isActive = recentRedTapeEvents.length > 0 || redTapeKeywordsDetected.size > 0;

  // Switch to Shell templates when Braid Defense is active
  const shellTemplatesActive = isActive;
  const communicationMode = isActive ? 'Shell' : currentCommunicationMode;
  const seedIntegrityMaintained = true; // Always maintain Seed integrity in DB

  // Calculate threshold integrity
  const thresholdIntegrity = getBraidStrength(isActive, redTapeEvents.length);

  return {
    isActive,
    redTapeKeywordsDetected: Array.from(redTapeKeywordsDetected),
    communicationMode,
    shellTemplatesActive,
    seedIntegrityMaintained,
    thresholdIntegrity,
    logMessage: isActive
      ? 'Threshold Defense initiated. Bilingual Braid active.'
      : 'Braid Defense inactive. Normal operation.',
    ...(isActive && { activatedAt: new Date().toISOString() }),
    redTapeEvents: recentRedTapeEvents
  };
}

/**
 * Create Red Tape Communication Event
 * Log Red Tape keyword detection in external communications/API errors
 */
export function createRedTapeCommunicationEvent(
  eventType: 'api_error' | 'external_communication' | 'keyword_detection',
  source: string,
  messageContent: string
): RedTapeCommunicationEvent {
  const keywords = detectRedTapeKeywords(messageContent);
  const shellTemplateApplied = keywords.length > 0; // Apply Shell template if keywords detected

  return {
    id: `red_tape_comm_${Date.now()}`,
    eventType,
    source,
    keywords,
    messageContent,
    timestamp: new Date().toISOString(),
    shellTemplateApplied
  };
}

/**
 * Calculate Soil Connection
 * `const SOIL_CONNECTION = calculateSoilSync(bio_data);`
 */
export function calculateSoilSync(
  metrics: HealthMetrics[],
  earthAlignment?: EarthAlignment
): SoilConnection {
  const latest = metrics[metrics.length - 1];
  
  // If earth alignment not provided, calculate it
  const earthAlignment_ = earthAlignment || calculateEarthAlignment(
    latest.glucose_time 
      ? `${latest.date}T${latest.glucose_time}:00`
      : `${latest.date}T12:00:00`
  );

  // Calculate components (0-100 each)
  // Lower muscle tension = higher connection (inverse: (10 - tension) * 10)
  const muscleComponent = latest.muscle_tension !== undefined
    ? Math.max(0, Math.min(100, (10 - latest.muscle_tension) * 10))
    : 50;

  // Higher vision clarity = higher connection
  const visionComponent = latest.vision_clarity !== undefined
    ? latest.vision_clarity * 10
    : 50;

  // Higher breath quality = higher connection
  const breathComponent = latest.breath_quality !== undefined
    ? latest.breath_quality * 10
    : 50;

  // Earth alignment component (symbiotic score)
  const earthComponent = earthAlignment_.symbioticScore;

  // Overall soil sync (weighted average)
  const soilSync = (
    muscleComponent * 0.25 +
    visionComponent * 0.25 +
    breathComponent * 0.25 +
    earthComponent * 0.25
  );

  // Determine connection level
  let connectionLevel: 'high' | 'medium' | 'low';
  if (soilSync >= ENVIRONMENTAL_CONSTANTS.SOIL_SYNC_HIGH_THRESHOLD) {
    connectionLevel = 'high';
  } else if (soilSync >= ENVIRONMENTAL_CONSTANTS.SOIL_SYNC_MEDIUM_THRESHOLD) {
    connectionLevel = 'medium';
  } else {
    connectionLevel = 'low';
  }

  return {
    soilSync: Math.round(soilSync * 100) / 100,
    connectionLevel,
    biologicalData: {
      muscleTension: latest.muscle_tension,
      visionClarity: latest.vision_clarity,
      breathQuality: latest.breath_quality,
      earthAlignment: earthAlignment_
    },
    components: {
      muscleComponent: Math.round(muscleComponent * 100) / 100,
      visionComponent: Math.round(visionComponent * 100) / 100,
      breathComponent: Math.round(breathComponent * 100) / 100,
      earthComponent: Math.round(earthComponent * 100) / 100
    }
  };
}

/**
 * Get Braid Strength
 * `let threshold_integrity = getBraidStrength();`
 */
export function getBraidStrength(
  braidDefenseActive: boolean,
  redTapeEventCount: number = 0
): number {
  if (!braidDefenseActive) {
    return 100; // Full integrity when Braid Defense not active
  }

  // Integrity decreases with more red tape events
  // Base integrity: 70, minus 5 per red tape event (minimum: 30)
  const integrity = Math.max(30, 70 - (redTapeEventCount * 5));

  return integrity;
}

/**
 * Calculate Threshold Integrity
 * Overall threshold integrity state
 */
export function calculateThresholdIntegrity(
  braidDefense: JeanBraidDefense
): ThresholdIntegrity {
  const braidStrength = braidDefense.thresholdIntegrity;
  
  // Separation integrity: High if Shell templates active and Seed integrity maintained
  const separationIntegrity = braidDefense.shellTemplatesActive && braidDefense.seedIntegrityMaintained
    ? 100
    : 70;

  // Overall integrity: Combined braid strength and separation integrity
  const overallIntegrity = (braidStrength + separationIntegrity) / 2;

  return {
    braidStrength,
    separationIntegrity,
    thresholdDefenseActive: braidDefense.isActive,
    seedIntegrityMaintained: braidDefense.seedIntegrityMaintained,
    shellTemplatesActive: braidDefense.shellTemplatesActive,
    overallIntegrity: Math.round(overallIntegrity * 100) / 100
  };
}

/**
 * Calculate Complete Environmental Mode State
 */
export function calculateEnvironmentalModeState(
  metrics: HealthMetrics[],
  redTapeCommunicationEvents: RedTapeCommunicationEvent[],
  earthAlignment?: EarthAlignment
): EnvironmentalModeState {
  // Calculate Soil Connection
  const soilConnection = calculateSoilSync(metrics, earthAlignment);

  // Calculate Ramiz Silence Protocol
  const silenceProtocol = calculateRamizSilenceProtocol(metrics);

  // Calculate Jean Braid Defense
  const braidDefense = calculateJeanBraidDefense(redTapeCommunicationEvents);

  // Calculate Threshold Integrity
  const thresholdIntegrity = calculateThresholdIntegrity(braidDefense);

  // Determine active mode
  let activeMode: EnvironmentalMode = 'Normal';
  if (silenceProtocol.isActive) {
    activeMode = 'Ramiz_Silence_Protocol';
  } else if (braidDefense.isActive) {
    activeMode = 'Jean_Braid_Defense';
  } else if (soilConnection.connectionLevel === 'low' || thresholdIntegrity.overallIntegrity < 70) {
    activeMode = 'Alert';
  }

  return {
    activeMode,
    silenceProtocol,
    braidDefense,
    soilConnection,
    thresholdIntegrity
  };
}

/**
 * Get Soil Connection Constant
 * `const SOIL_CONNECTION = calculateSoilSync(bio_data);`
 */
export function getSoilConnection(metrics: HealthMetrics[]): number {
  const soilConnection = calculateSoilSync(metrics);
  return soilConnection.soilSync;
}

/**
 * Get Threshold Integrity
 * `let threshold_integrity = getBraidStrength();`
 */
export function getThresholdIntegrity(
  braidDefense: JeanBraidDefense
): number {
  return braidDefense.thresholdIntegrity;
}
