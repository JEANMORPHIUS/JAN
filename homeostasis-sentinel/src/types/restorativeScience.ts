/**
 * RESTORATIVE SCIENCE TYPES
 * Urine, DNA, Genetic Truth, and the Restoration of the Temple
 * 
 * This is restorative science, not just tracking.
 * Urine carries DNA. Genetic truth manifests. Medications support restoration.
 */

import { EarthAlignment } from './earthAlignment';

/**
 * Genetic Context
 * Urine carries DNA - genetic conditions manifest in urine
 */
export interface GeneticContext {
  /** Genetic conditions (sickle cell, diabetes, etc.) */
  conditions: string[];
  /** How genetics manifest in urine */
  geneticExpression: string;
  /** Urine carries DNA */
  dnaCarried: boolean;
  /** Genetic truth (not separation) */
  geneticTruth: string;
}

/**
 * Medical Context
 * All medications affect urine - medications support restoration
 */
export interface MedicalContext {
  /** Medications (insulin_degludec, insulin_humalog, etc.) */
  medications: string[];
  /** How medications affect urine */
  medicationEffects: string;
  /** How medications support restoration */
  restorativeSupport: string;
  /** Medical truth (not separation) */
  medicalTruth: string;
}

/**
 * Restorative Urine Analysis
 * Urine is biological truth, not waste
 * Taste, color, timing all carry restorative meaning
 */
export interface RestorativeUrineAnalysis {
  /** Taste: Biological communication (not error) */
  taste: 'bitter' | 'sweet' | 'metallic' | 'acetone' | 'fresh';
  /** Color: Genetic/medical truth (1-10: dark/concentrated to clear/dilute) */
  color: number;
  /** Timing: Earth alignment (symbiotic relationship) */
  timing: string;
  /** Frequency: Natural rhythm (not forced) */
  frequency: number;
  
  /** Genetic context: Urine carries DNA */
  geneticContext: GeneticContext;
  /** Medical context: Medications support restoration */
  medicalContext: MedicalContext;
  
  /** Restorative meaning: What this tells us about restoration */
  restorativeMeaning: {
    /** Biological communication (e.g., "Bitter = body speaking truth") */
    biologicalCommunication: string;
    /** Genetic truth (e.g., "Urine reflects genetic conditions") */
    geneticTruth: string;
    /** Medical truth (e.g., "Urine reflects medication effects") */
    medicalTruth: string;
    /** Earth alignment (e.g., "Timing aligns with Earth's rhythm") */
    earthAlignment: string;
  };
  
  /** Earth alignment at time of loop */
  earthAlignment: EarthAlignment;
}

/**
 * Restorative Loop Event
 * Loop is restorative practice, not just tracking
 */
export interface RestorativeLoopEvent {
  /** Loop timestamp */
  timestamp: string;
  /** Urine analysis */
  urineAnalysis: RestorativeUrineAnalysis;
  /** Restorative context */
  restorativeContext: {
    /** What this loop tells us about restoration */
    restorationStory: string;
    /** How this honors genetic truth */
    geneticHonor: string;
    /** How this honors medical truth */
    medicalHonor: string;
    /** How this honors Earth alignment */
    earthHonor: string;
  };
}

/**
 * Restorative Science State
 * Complete restorative science state
 */
export interface RestorativeScienceState {
  /** All restorative loop events */
  loopEvents: RestorativeLoopEvent[];
  /** Genetic conditions context */
  geneticConditions: string[];
  /** Medications context */
  medications: string[];
  /** Restorative science summary */
  restorativeSummary: {
    /** Overall restoration story */
    restorationStory: string;
    /** Genetic truth honored */
    geneticTruthHonored: boolean;
    /** Medical truth honored */
    medicalTruthHonored: boolean;
    /** Earth alignment honored */
    earthAlignmentHonored: boolean;
  };
}
