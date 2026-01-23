/**
 * WATER MEMORY UTILITIES
 * Water Holds Memory: Our Vibrations Whilst in It Are Spiritual Battles
 * 
 * Philosophy:
 * - Water holds memory (genetic, vibrational, temporal)
 * - Our vibrations whilst in it are spiritual battles
 * - Everything begins in the mind → Vibrations begin in the mind
 */

import {
  WaterMemory,
  GeneticMemory,
  VibrationalMemory,
  TemporalMemory,
  SpiritualBattle
} from '../types/waterMemory';
import { HealthMetrics } from '../types';

/**
 * Create Genetic Memory
 * Water holds genetic memory (DNA, patterns, truth)
 */
export function createGeneticMemory(
  geneticConditions: string[] = [],
  dnaCarried: boolean = true
): GeneticMemory {
  const geneticTruth = geneticConditions.length > 0
    ? `Urine carries DNA. Genetic conditions (${geneticConditions.join(', ')}) manifest in water. This is genetic truth, not separation.`
    : 'Urine carries DNA. Genetic truth manifests in water. This is genetic truth, not separation.';
  
  return {
    dnaCarried,
    geneticPatterns: geneticConditions,
    geneticTruth
  };
}

/**
 * Create Vibrational Memory
 * Water remembers vibrations (frequency, energy, spiritual battles)
 */
export function createVibrationalMemory(
  frequency: 'purpose' | 'impulsiveness' | 'stillness' | 'noise' = 'purpose',
  energy: 'revelation' | 'reaction' | 'substance' | 'stimulation' = 'revelation',
  spiritualBattle: string = 'Frequency battle: Purpose vs impulsiveness'
): VibrationalMemory {
  return {
    frequency,
    energy,
    spiritualBattle,
    waterRemembers: true // Water always remembers vibrations
  };
}

/**
 * Create Temporal Memory
 * Water remembers when (temporal patterns, history)
 */
export function createTemporalMemory(
  whenVibrationOccurred: string = new Date().toISOString(),
  vibrationHistory: string[] = [],
  waterTransmitsHistory: boolean = true
): TemporalMemory {
  return {
    whenVibrationOccurred,
    vibrationHistory,
    waterTransmitsHistory
  };
}

/**
 * Create Water Memory
 * Complete water memory system
 */
export function createWaterMemory(
  memoryType: 'genetic' | 'vibrational' | 'temporal' = 'vibrational',
  geneticConditions: string[] = [],
  frequency: 'purpose' | 'impulsiveness' | 'stillness' | 'noise' = 'purpose',
  energy: 'revelation' | 'reaction' | 'substance' | 'stimulation' = 'revelation'
): WaterMemory {
  const geneticMemory = createGeneticMemory(geneticConditions);
  const vibrationalMemory = createVibrationalMemory(frequency, energy);
  const temporalMemory = createTemporalMemory();
  
  return {
    memoryType,
    geneticMemory,
    vibrationalMemory,
    temporalMemory,
    timestamp: new Date().toISOString()
  };
}

/**
 * Recognize Spiritual Battle
 * Our vibrations whilst in it are spiritual battles
 */
export function recognizeSpiritualBattle(
  frequency: 'purpose' | 'impulsiveness' | 'stillness' | 'noise',
  energy: 'revelation' | 'reaction' | 'substance' | 'stimulation'
): SpiritualBattle {
  // Determine battle type based on frequency and energy
  let battleType: 'frequency' | 'energy' | 'truth' | 'substance' = 'frequency';
  let battleSides: { light: string; dark: string };
  let battleState: 'active' | 'resolved' | 'ongoing' = 'active';
  
  if (frequency === 'purpose' || frequency === 'stillness') {
    battleType = 'frequency';
    battleSides = {
      light: frequency === 'purpose' ? 'Purpose (mind as source)' : 'Stillness (sacred space)',
      dark: frequency === 'purpose' ? 'Impulsiveness (mind as receiver)' : 'Noise (distraction)'
    };
  } else if (energy === 'revelation' || energy === 'substance') {
    battleType = 'truth';
    battleSides = {
      light: energy === 'revelation' ? 'Revelation (wisdom)' : 'Substance (truth)',
      dark: energy === 'revelation' ? 'Reaction (impulsiveness)' : 'Stimulation (achievement)'
    };
  } else {
    battleType = 'energy';
    battleSides = {
      light: 'Revelation (wisdom)',
      dark: 'Reaction (impulsiveness)'
    };
  }
  
  // Determine outcome based on frequency and energy
  const lightWins = (frequency === 'purpose' || frequency === 'stillness') &&
    (energy === 'revelation' || energy === 'substance');
  const darkWins = (frequency === 'impulsiveness' || frequency === 'noise') &&
    (energy === 'reaction' || energy === 'stimulation');
  
  const outcome: 'light' | 'dark' | 'ongoing' = lightWins
    ? 'light'
    : darkWins
    ? 'dark'
    : 'ongoing';
  
  return {
    battleType,
    battleSides,
    battleState,
    waterRemembers: true, // Water always remembers spiritual battles
    outcome
  };
}

/**
 * Analyze Water Memory from Metrics
 * Extract water memory from health metrics
 */
export function analyzeWaterMemoryFromMetrics(
  metrics: HealthMetrics,
  geneticConditions: string[] = []
): {
  waterMemory: WaterMemory;
  spiritualBattle: SpiritualBattle;
} {
  // Determine frequency from metrics
  let frequency: 'purpose' | 'impulsiveness' | 'stillness' | 'noise' = 'purpose';
  let energy: 'revelation' | 'reaction' | 'substance' | 'stimulation' = 'revelation';
  
  // If glucose is elevated and user reports bitter, it's body speaking truth (purpose, revelation)
  if (metrics.blood_glucose !== undefined && metrics.blood_glucose > 15) {
    frequency = 'purpose'; // Body speaking truth = purpose
    energy = 'revelation'; // Truth = revelation
  }
  
  // If breath quality is low, might indicate reaction/stimulation
  if (metrics.breath_quality !== undefined && metrics.breath_quality < 3) {
    energy = 'reaction'; // Low breath quality = reaction
  }
  
  // Create water memory
  const waterMemory = createWaterMemory('vibrational', geneticConditions, frequency, energy);
  
  // Recognize spiritual battle
  const spiritualBattle = recognizeSpiritualBattle(frequency, energy);
  
  return {
    waterMemory,
    spiritualBattle
  };
}
