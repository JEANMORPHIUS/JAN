/**
 * RESTORATIVE SCIENCE UTILITIES
 * Urine, DNA, Genetic Truth, and the Restoration of the Temple
 * 
 * This is restorative science, not just tracking.
 */

import {
  RestorativeUrineAnalysis,
  RestorativeLoopEvent,
  RestorativeScienceState,
  GeneticContext,
  MedicalContext
} from '../types/restorativeScience';
import { HealthMetrics } from '../types';
import { EarthAlignment } from '../types/earthAlignment';
import { calculateEarthAlignment } from './earthRhythms';
import { humanizeMetric } from './humanDignity';

/**
 * Analyze Urine as Restorative Data
 * Urine carries DNA - genetic truth manifests here
 */
export function analyzeRestorativeUrine(
  metrics: HealthMetrics,
  geneticConditions: string[] = [],
  medications: string[] = [],
  earthAlignment?: EarthAlignment
): RestorativeUrineAnalysis {
  const taste = determineTasteFromMetrics(metrics);
  const color = metrics.urine_color ?? 5; // Default to middle
  const timing = metrics.date + (metrics.glucose_time ? `T${metrics.glucose_time}:00` : 'T12:00:00');
  const frequency = metrics.loop_frequency ?? 0;
  
  const earthAlign = earthAlignment || calculateEarthAlignment(timing);
  
  // Genetic context
  const geneticContext: GeneticContext = {
    conditions: geneticConditions,
    geneticExpression: determineGeneticExpression(geneticConditions, taste, color),
    dnaCarried: true, // Urine always carries DNA
    geneticTruth: `Urine carries DNA. Genetic conditions (${geneticConditions.join(', ') || 'none'}) manifest in urine. This is genetic truth, not separation.`
  };
  
  // Medical context
  const medicalContext: MedicalContext = {
    medications,
    medicationEffects: determineMedicationEffects(medications, taste, color),
    restorativeSupport: `Medications (${medications.join(', ') || 'none'}) support body's restoration. This is restorative support, not just treatment.`,
    medicalTruth: `All medications affect urine. This is medical truth, not separation.`
  };
  
  // Restorative meaning
  const biologicalCommunication = determineBiologicalCommunication(taste);
  const geneticTruth = `Urine reflects genetic conditions (${geneticConditions.join(', ') || 'none'}). This is genetic truth, not hidden.`;
  const medicalTruth = `Urine reflects medication effects (${medications.join(', ') || 'none'}). This is medical truth, not hidden.`;
  const earthAlignmentMessage = `Loop timing (${timing}) aligns with Earth's ${earthAlign.solar.phase} phase. This is symbiotic relationship, not separation.`;
  
  return {
    taste,
    color,
    timing,
    frequency,
    geneticContext,
    medicalContext,
    restorativeMeaning: {
      biologicalCommunication,
      geneticTruth,
      medicalTruth,
      earthAlignment: earthAlignmentMessage
    },
    earthAlignment: earthAlign
  };
}

/**
 * Determine Taste from Metrics
 * Taste is biological communication, not error
 */
function determineTasteFromMetrics(metrics: HealthMetrics): RestorativeUrineAnalysis['taste'] {
  // If breath quality indicates ketones, taste might be acetone
  if (metrics.breath_quality !== undefined && metrics.breath_quality < 3) {
    return 'acetone';
  }
  
  // If glucose is elevated and user reports bitter, it's bitter
  if (metrics.blood_glucose !== undefined && metrics.blood_glucose > 15) {
    // User mentioned "bitter" - this is biological communication
    return 'bitter';
  }
  
  // Default based on other indicators
  if (metrics.breath_quality !== undefined && metrics.breath_quality > 7) {
    return 'fresh';
  }
  
  return 'bitter'; // Default to bitter if body is processing
}

/**
 * Determine Genetic Expression
 * How genetics manifest in urine
 */
function determineGeneticExpression(
  conditions: string[],
  taste: RestorativeUrineAnalysis['taste'],
  color: number
): string {
  if (conditions.length === 0) {
    return 'Genetic truth manifests in urine. This is biological truth, not separation.';
  }
  
  const expressions: string[] = [];
  
  if (conditions.includes('sickle_cell')) {
    expressions.push('Sickle cell affects urine composition (hemoglobin, etc.). This is genetic truth, not hidden.');
  }
  
  if (conditions.includes('t1d') || conditions.includes('diabetes')) {
    expressions.push('Diabetes affects urine (glucose, ketones, etc.). This is genetic truth, not hidden.');
  }
  
  // Add more conditions as needed
  
  return expressions.join(' ') || 'Genetic conditions manifest in urine. This is genetic truth, not separation.';
}

/**
 * Determine Medication Effects
 * How medications affect urine
 */
function determineMedicationEffects(
  medications: string[],
  taste: RestorativeUrineAnalysis['taste'],
  color: number
): string {
  if (medications.length === 0) {
    return 'Medications affect urine composition. This is medical truth, not hidden.';
  }
  
  const effects: string[] = [];
  
  if (medications.some(m => m.includes('insulin'))) {
    effects.push('Insulin affects urine (glucose processing, etc.). This is restorative support, not just treatment.');
  }
  
  // Add more medication effects as needed
  
  return effects.join(' ') || 'Medications affect urine. This is medical truth, not hidden.';
}

/**
 * Determine Biological Communication
 * What taste tells us about body's communication
 */
function determineBiologicalCommunication(taste: RestorativeUrineAnalysis['taste']): string {
  switch (taste) {
    case 'bitter':
      return 'Bitter taste = Body speaking truth. Body is processing glucose. This is biological communication, not error.';
    case 'sweet':
      return 'Sweet taste = Metabolic state. This is biological communication, not error.';
    case 'metallic':
      return 'Metallic taste = Ketone production. This is biological communication, not error.';
    case 'acetone':
      return 'Acetone taste = Metabolic state. This is biological communication, not error.';
    case 'fresh':
      return 'Fresh taste = Body in balance. This is biological communication, not error.';
    default:
      return 'Taste = Body speaking truth. This is biological communication, not error.';
  }
}

/**
 * Create Restorative Loop Event
 * Loop is restorative practice, not just tracking
 */
export function createRestorativeLoopEvent(
  metrics: HealthMetrics,
  geneticConditions: string[] = [],
  medications: string[] = [],
  earthAlignment?: EarthAlignment
): RestorativeLoopEvent {
  const urineAnalysis = analyzeRestorativeUrine(metrics, geneticConditions, medications, earthAlignment);
  
  const restorationStory = `The ${urineAnalysis.taste} taste tells the truth. Your body is processing. Genetic conditions (${geneticConditions.join(', ') || 'none'}) manifest in urine. Medications (${medications.join(', ') || 'none'}) support restoration. This is restorative science, not just tracking.`;
  
  const geneticHonor = `Genetic truth (${geneticConditions.join(', ') || 'none'}) is honored, not hidden. Urine carries DNA. This is restoration, not separation.`;
  
  const medicalHonor = `Medical truth (${medications.join(', ') || 'none'}) is honored, not hidden. Medications support restoration. This is restoration, not separation.`;
  
  const earthHonor = `Earth alignment is honored. Loop timing aligns with ${urineAnalysis.earthAlignment.solar.phase} phase. This is symbiotic relationship, not separation.`;
  
  return {
    timestamp: metrics.date + (metrics.glucose_time ? `T${metrics.glucose_time}:00` : 'T12:00:00'),
    urineAnalysis,
    restorativeContext: {
      restorationStory,
      geneticHonor,
      medicalHonor,
      earthHonor
    }
  };
}

/**
 * Calculate Restorative Science State
 * Complete restorative science state
 */
export function calculateRestorativeScienceState(
  metrics: HealthMetrics[],
  geneticConditions: string[] = [],
  medications: string[] = []
): RestorativeScienceState {
  const loopEvents: RestorativeLoopEvent[] = [];
  
  metrics.forEach(metric => {
    if (metric.urine_color !== undefined || metric.breath_quality !== undefined) {
      const event = createRestorativeLoopEvent(metric, geneticConditions, medications);
      loopEvents.push(event);
    }
  });
  
  const restorationStory = `Your body is a temple. Urine carries DNA. Genetic truth (${geneticConditions.join(', ') || 'none'}) manifests. Medications (${medications.join(', ') || 'none'}) support restoration. This is restorative science, not just tracking.`;
  
  return {
    loopEvents,
    geneticConditions,
    medications,
    restorativeSummary: {
      restorationStory,
      geneticTruthHonored: true, // Always honored in restorative science
      medicalTruthHonored: true, // Always honored in restorative science
      earthAlignmentHonored: loopEvents.every(e => e.urineAnalysis.earthAlignment.symbioticScore > 70)
    }
  };
}
