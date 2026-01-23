/**
 * FOURTH WAY UTILITIES
 * Self-Remembering, Observation Gate, Many I's Filter, Consciousness Calculation
 * 
 * Based on Gurdjieff/Ouspensky Fourth Way philosophy:
 * - Self-remembering: Am I observing the machine or is the machine observing me?
 * - Many I's: Which 'I' is speaking at the Table right now?
 * - Presence: Response time vs. biological stability
 */

import {
  ObservationGate,
  PresenceCoefficient,
  ManyIsFilter,
  ConsciousnessLevel,
  SelfRememberingSession
} from '../types/fourthWay';
import { HealthMetrics } from '../types';
import { calculateEarthAlignment } from './earthRhythms';
import { StewardshipScorecard } from '../types/stewardshipAudit';

/**
 * Red Tape Detection
 * Detects system bureaucracy, chaos, or broken system patterns
 */
export function detectRedTape(metrics: HealthMetrics[]): boolean {
  if (metrics.length === 0) return false;
  
  // Red Tape indicators:
  // 1. High variance in readings (system chaos)
  const glucoseReadings = metrics
    .filter(m => m.glucose !== undefined)
    .map(m => m.glucose!);
  
  if (glucoseReadings.length < 2) return false;
  
  const mean = glucoseReadings.reduce((a, b) => a + b, 0) / glucoseReadings.length;
  const variance = glucoseReadings.reduce((sum, val) => sum + Math.pow(val - mean, 2), 0) / glucoseReadings.length;
  const stdDev = Math.sqrt(variance);
  
  // High variance (>5 mmol/L std dev) = red tape (system chaos)
  if (stdDev > 5) return true;
  
  // 2. Missing critical data (broken systems)
  const recentMetrics = metrics.slice(-10);
  const hasMissingCriticalData = recentMetrics.some(m => 
    m.glucose === undefined && m.vision === undefined && m.muscleTension === undefined
  );
  
  if (hasMissingCriticalData) return true;
  
  // 3. Rapid contradictory readings (within 1 hour: 17.8 → 3.2)
  const sortedMetrics = [...metrics].sort((a, b) => 
    new Date(a.timestamp).getTime() - new Date(b.timestamp).getTime()
  );
  
  for (let i = 1; i < sortedMetrics.length; i++) {
    const prev = sortedMetrics[i - 1];
    const curr = sortedMetrics[i];
    const timeDiff = new Date(curr.timestamp).getTime() - new Date(prev.timestamp).getTime();
    const hoursDiff = timeDiff / (1000 * 60 * 60);
    
    if (prev.glucose && curr.glucose && hoursDiff <= 1) {
      const jump = Math.abs(curr.glucose - prev.glucose);
      if (jump > 10) return true; // Large jump in 1 hour = red tape
    }
  }
  
  return false;
}

/**
 * Calculate Biological Stability
 * Measures variance in recent biological metrics (glucose, vision, muscle, breath)
 * Returns 0-1 (higher = more stable)
 */
export function calculateBiologicalStability(metrics: HealthMetrics[]): number {
  if (metrics.length === 0) return 0;
  
  const recentMetrics = metrics.slice(-10); // Last 10 readings
  
  // Calculate stability for each metric type
  const glucoseReadings = recentMetrics
    .filter(m => m.glucose !== undefined)
    .map(m => m.glucose!);
  
  const visionReadings = recentMetrics
    .filter(m => m.vision !== undefined)
    .map(m => m.vision!);
  
  const muscleReadings = recentMetrics
    .filter(m => m.muscleTension !== undefined)
    .map(m => m.muscleTension!);
  
  const breathReadings = recentMetrics
    .filter(m => m.breathQuality !== undefined)
    .map(m => m.breathQuality!);
  
  // Calculate coefficients of variation (std dev / mean) for each metric
  const calculateCoeffVar = (values: number[]): number => {
    if (values.length < 2) return 0;
    const mean = values.reduce((a, b) => a + b, 0) / values.length;
    if (mean === 0) return 1;
    const variance = values.reduce((sum, val) => sum + Math.pow(val - mean, 2), 0) / values.length;
    const stdDev = Math.sqrt(variance);
    return stdDev / mean;
  };
  
  const glucoseCV = calculateCoeffVar(glucoseReadings);
  const visionCV = calculateCoeffVar(visionReadings);
  const muscleCV = calculateCoeffVar(muscleReadings);
  const breathCV = calculateCoeffVar(breathReadings);
  
  // Normalize CV to 0-1 stability score (lower CV = higher stability)
  const normalizeCV = (cv: number): number => {
    // CV of 0 = perfect stability (1.0)
    // CV of 0.5 = moderate stability (0.5)
    // CV of 1.0+ = low stability (0.0)
    return Math.max(0, Math.min(1, 1 - (cv * 2)));
  };
  
  const glucoseStability = normalizeCV(glucoseCV);
  const visionStability = normalizeCV(visionCV);
  const muscleStability = normalizeCV(muscleCV);
  const breathStability = normalizeCV(breathCV);
  
  // Average stability (weighted by available data)
  const weights = [
    glucoseReadings.length > 0 ? 1 : 0,
    visionReadings.length > 0 ? 1 : 0,
    muscleReadings.length > 0 ? 1 : 0,
    breathReadings.length > 0 ? 1 : 0
  ];
  const totalWeight = weights.reduce((a, b) => a + b, 0);
  
  if (totalWeight === 0) return 0;
  
  const weightedSum = 
    glucoseStability * weights[0] +
    visionStability * weights[1] +
    muscleStability * weights[2] +
    breathStability * weights[3];
  
  return weightedSum / totalWeight;
}

/**
 * Create Observation Gate
 * Triggers self-remembering prompt at random interval or when Red Tape is detected
 */
export function createObservationGate(
  metrics: HealthMetrics[],
  triggerType: 'random_interval' | 'red_tape' | 'manual' = 'random_interval'
): ObservationGate {
  const timestamp = new Date().toISOString();
  const biologicalStability = calculateBiologicalStability(metrics);
  
  const prompt = "Are you observing the machine or is the machine observing you?";
  
  // Initial presence coefficient is based on biological stability alone
  // Will be updated when user responds
  const presenceCoefficient = biologicalStability * 0.5; // Initial estimate
  
  return {
    triggerType,
    timestamp,
    prompt,
    presenceCoefficient,
    biologicalStability
  };
}

/**
 * Update Observation Gate with Response
 * Calculates presence coefficient from response time and biological stability
 */
export function updateObservationGateWithResponse(
  gate: ObservationGate,
  responseTimestamp: string,
  reflection?: string
): ObservationGate & { presenceCoefficient: PresenceCoefficient } {
  const responseTimeMs = new Date(responseTimestamp).getTime() - new Date(gate.timestamp).getTime();
  
  // Normalize response time (0-1, lower is better)
  // Fast response (< 30 seconds) = 1.0
  // Medium response (30s - 5min) = 0.5
  // Slow response (> 5min) = 0.0
  const responseTimeNormalized = Math.max(0, Math.min(1, 1 - (responseTimeMs / (5 * 60 * 1000))));
  
  // Presence coefficient = (response time normalized + biological stability) / 2
  const presenceValue = (responseTimeNormalized + gate.biologicalStability) / 2;
  
  let interpretation: 'present' | 'emerging' | 'absent';
  let guidance: string;
  
  if (presenceValue >= 0.7) {
    interpretation = 'present';
    guidance = "You are observing the machine. You are present. Continue self-remembering.";
  } else if (presenceValue >= 0.4) {
    interpretation = 'emerging';
    guidance = "Presence is emerging. Return to self-observation. Are you observing the machine?";
  } else {
    interpretation = 'absent';
    guidance = "The machine is observing you. Return to self-remembering. Law 11: Wisdom lives in the quiet.";
  }
  
  const presenceCoefficient: PresenceCoefficient = {
    value: presenceValue,
    responseTimeNormalized,
    biologicalStability: gate.biologicalStability,
    interpretation,
    guidance,
    timestamp: responseTimestamp
  };
  
  return {
    ...gate,
    responseTimestamp,
    responseTimeMs,
    reflection,
    presenceCoefficient
  };
}

/**
 * Filter Many I's
 * Detects impulsive/inconsistent input and triggers Pierre Voice (Law 5: Your word is your bond)
 */
export function filterManyIs(
  input: string,
  inputType: 'glucose_reading' | 'protocol_entry' | 'community_interaction' | 'other',
  recentInputs: Array<{ input: string; timestamp: string; type: string }>,
  recentMetrics: HealthMetrics[]
): ManyIsFilter {
  const timestamp = new Date().toISOString();
  
  // Check for rapid successive entries (within 5 minutes)
  const recentInputsWithin5Min = recentInputs.filter(ri => {
    const timeDiff = new Date(timestamp).getTime() - new Date(ri.timestamp).getTime();
    return timeDiff <= 5 * 60 * 1000; // 5 minutes
  });
  const rapidEntries = recentInputsWithin5Min.length > 3;
  
  // Check for large value jumps (e.g., glucose 17.8 → 3.2 in 1 hour)
  const sortedMetrics = [...recentMetrics].sort((a, b) =>
    new Date(a.timestamp).getTime() - new Date(b.timestamp).getTime()
  );
  let largeJumps = false;
  if (inputType === 'glucose_reading' && sortedMetrics.length >= 2) {
    const lastMetric = sortedMetrics[sortedMetrics.length - 1];
    const prevMetric = sortedMetrics[sortedMetrics.length - 2];
    if (lastMetric.glucose && prevMetric.glucose) {
      const timeDiff = new Date(lastMetric.timestamp).getTime() - new Date(prevMetric.timestamp).getTime();
      const hoursDiff = timeDiff / (1000 * 60 * 60);
      if (hoursDiff <= 1) {
        const jump = Math.abs(lastMetric.glucose - prevMetric.glucose);
        largeJumps = jump > 10; // >10 mmol/L jump in 1 hour
      }
    }
  }
  
  // Check for contradictory statements (e.g., "fasting" then "eating")
  const lowerInput = input.toLowerCase();
  const hasContradiction = recentInputs.some(ri => {
    const lowerRecent = ri.input.toLowerCase();
    const contradictions = [
      (lowerInput.includes('fasting') && lowerRecent.includes('eating')),
      (lowerInput.includes('eating') && lowerRecent.includes('fasting')),
      (lowerInput.includes('rest') && lowerRecent.includes('working')),
      (lowerInput.includes('working') && lowerRecent.includes('rest'))
    ];
    return contradictions.some(c => c);
  });
  
  // Check for missing context (e.g., reading without time or loop info)
  const missingContext = 
    inputType === 'glucose_reading' &&
    !input.match(/\d{1,2}:\d{2}/) && // No time
    !input.match(/loop|fasting|morning|evening/i); // No context
  
  const inconsistencyIndicators = {
    rapidEntries,
    largeJumps,
    contradictoryStatements: hasContradiction,
    missingContext
  };
  
  // Calculate impulsivity score
  const impulsivityScore = 
    (rapidEntries ? 0.3 : 0) +
    (largeJumps ? 0.3 : 0) +
    (hasContradiction ? 0.2 : 0) +
    (missingContext ? 0.2 : 0);
  
  // Filter is triggered if impulsivity > 0.7 or multiple inconsistencies
  const isTriggered = impulsivityScore > 0.7 || 
    Object.values(inconsistencyIndicators).filter(v => v).length >= 2;
  
  // Pierre Voice message (Law 5: Your word is your bond)
  const pierreVoiceMessage = isTriggered
    ? "Which 'I' is speaking at the Table right now? Return to the Law 5 Bond. Your word is your bond."
    : undefined;
  
  // Law 5 compliance check
  const law5Compliance = {
    isCompliant: !isTriggered,
    context: isTriggered
      ? "Multiple I's detected. Impulsivity or inconsistency suggests mechanical behavior."
      : "Single I speaking. Input is consistent with previous commitments.",
    guidance: isTriggered
      ? "Return to self-remembering. Which I is speaking? Law 5: Your word is your bond."
      : "Your word is being honored. Continue self-observation."
  };
  
  return {
    inputType,
    input,
    timestamp,
    impulsivityScore,
    inconsistencyIndicators,
    isTriggered,
    pierreVoiceMessage,
    law5Compliance
  };
}

/**
 * Calculate Self-Observation (Consciousness Level)
 * Calculates consciousness level from biological data and law consistency
 */
export function calculateSelfObservation(
  bioData: HealthMetrics[],
  lawConsistency: { law5: number; law37: number },
  recentPresenceCoefficients: number[] = []
): ConsciousnessLevel {
  const timestamp = new Date().toISOString();
  
  // Self-observation component (from presence coefficient history)
  const selfObservation = recentPresenceCoefficients.length > 0
    ? recentPresenceCoefficients.reduce((a, b) => a + b, 0) / recentPresenceCoefficients.length
    : 0.5; // Default to 0.5 if no history
  
  // Law consistency component (average of Law 5 and Law 37)
  const lawConsistencyAvg = (lawConsistency.law5 + lawConsistency.law37) / 2;
  
  // Biological alignment component (Earth rhythm alignment)
  const recentMetrics = bioData.slice(-10);
  if (recentMetrics.length === 0) {
    return {
      level: 0,
      selfObservation: 0,
      lawConsistency: 0,
      biologicalAlignment: 0,
      interpretation: 'mechanical',
      guidance: "No biological data available. Begin self-observation. Are you observing the machine?",
      timestamp,
      recentPresenceCoefficients,
      law5ComplianceRate: lawConsistency.law5,
      law37ComplianceRate: lawConsistency.law37
    };
  }
  
  const earthAlignment = calculateEarthAlignment(recentMetrics[recentMetrics.length - 1].timestamp);
  const biologicalAlignment = earthAlignment.symbioticScore / 100; // Convert 0-100 to 0-1
  
  // Consciousness level = weighted average of all three components
  const level = (selfObservation * 0.4 + lawConsistencyAvg * 0.3 + biologicalAlignment * 0.3);
  
  let interpretation: 'awake' | 'emerging' | 'sleeping' | 'mechanical';
  let guidance: string;
  
  if (level >= 0.75) {
    interpretation = 'awake';
    guidance = "You are awake. You are observing the machine. Continue self-remembering. Law 11: Wisdom lives in the quiet.";
  } else if (level >= 0.5) {
    interpretation = 'emerging';
    guidance = "Consciousness is emerging. Return to self-observation. Which I is speaking?";
  } else if (level >= 0.25) {
    interpretation = 'sleeping';
    guidance = "You are sleeping. The machine is observing you. Return to self-remembering. Law 5: Your word is your bond.";
  } else {
    interpretation = 'mechanical';
    guidance = "You are mechanical. Many I's are speaking. Return to the Law 5 Bond. Which I is speaking at the Table?";
  }
  
  return {
    level,
    selfObservation,
    lawConsistency: lawConsistencyAvg,
    biologicalAlignment,
    interpretation,
    guidance,
    timestamp,
    recentPresenceCoefficients: recentPresenceCoefficients.slice(-7), // Last 7
    law5ComplianceRate: lawConsistency.law5,
    law37ComplianceRate: lawConsistency.law37
  };
}

/**
 * Create Self-Remembering Session
 * Complete observation cycle with gate, presence, filter, and consciousness
 */
export function createSelfRememberingSession(
  gate: ObservationGate & { presenceCoefficient?: PresenceCoefficient },
  manyIsFilter?: ManyIsFilter,
  bioData: HealthMetrics[] = [],
  lawConsistency: { law5: number; law37: number } = { law5: 0.5, law37: 0.5 },
  recentPresenceCoefficients: number[] = []
): SelfRememberingSession {
  const consciousnessLevel = calculateSelfObservation(bioData, lawConsistency, recentPresenceCoefficients);
  
  // Include presence coefficient from gate if available
  const presenceCoefficient: PresenceCoefficient = gate.presenceCoefficient || {
    value: gate.biologicalStability * 0.5,
    responseTimeNormalized: 0.5,
    biologicalStability: gate.biologicalStability,
    interpretation: 'emerging',
    guidance: "Presence coefficient pending response. Are you observing the machine?",
    timestamp: gate.timestamp
  };
  
  // Update recent presence coefficients with this one
  const updatedRecentCoefficients = [...recentPresenceCoefficients, presenceCoefficient.value].slice(-7);
  
  // Recalculate consciousness with updated coefficients
  const updatedConsciousnessLevel = calculateSelfObservation(
    bioData,
    lawConsistency,
    updatedRecentCoefficients
  );
  
  const outcome = {
    responded: gate.responseTimestamp !== undefined,
    showedPresence: presenceCoefficient.value >= 0.7,
    manyIsTriggered: manyIsFilter?.isTriggered || false,
    assessment: presenceCoefficient.interpretation
  };
  
  return {
    gate,
    presenceCoefficient,
    manyIsFilter,
    consciousnessLevel: updatedConsciousnessLevel,
    outcome
  };
}
