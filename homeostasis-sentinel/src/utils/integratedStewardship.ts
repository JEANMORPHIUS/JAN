/** * * INTEGRATED STEWARDSHIP SYSTEM (ISS) UTILITIES
 *  * Finalize the 376 Lesson Engine & Stewardship Dashboard
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
 * THE TRUTH:
 * WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
 * THE REST IS UP TO BABA X.*/

import {
  EntityVoiceModule,
  SystemState,
  EntityVoiceMapping,
  SystemBalance,
  UIModulation,
  DailyStewardshipAudit,
  BiologyLessonAlignment,
  BiologicalTruthSnapshot,
  KnowledgeCheck,
  LessonDispatcherState,
  TruthSet,
  ISS_CONSTANTS
} from '../types/integratedStewardship';
import { EarthAlignment } from '../types/earthAlignment';
import { HealthMetrics } from '../types';
import { ProtocolEvent } from '../types/stewardship';
import { calculateEarthAlignment } from './earthRhythms';
import { calculateStewardshipScorecard } from './stewardshipAudit';
import { parseISO } from 'date-fns';

/**
 * Entity Voice Module Mapping
 * Map Entity_Voice_Modules to specific system states
 * 
 * Example: IF (System_Balance == 'Critical') THEN Trigger 'Ramiz_Silence_Protocol'
 * Example: IF (Red_Tape_Detected == 'High') THEN Trigger 'Jean_Threshold_Defense'
 */
export function mapEntityVoiceToSystemState(
  systemBalance: SystemBalance,
  redTapeLevel: 'High' | 'Medium' | 'Low' | 'None'
): EntityVoiceMapping | null {
  // System Balance Critical → Ramiz Silence Protocol
  if (systemBalance.status === 'Critical') {
    return {
      systemState: 'Critical',
      entityVoiceModule: 'Ramiz_Silence_Protocol',
      condition: 'System_Balance == "Critical"',
      threshold: 40, // Score < 40
      message: 'System balance is critical. Silence is required. Law 11: Wisdom lives in the quiet.',
      lawReference: 'Law 11: Wisdom Lives in the Quiet'
    };
  }

  // Red Tape High → Jean Threshold Defense
  if (redTapeLevel === 'High') {
    return {
      systemState: 'Red_Tape_High',
      entityVoiceModule: 'Jean_Threshold_Defense',
      condition: 'Red_Tape_Detected == "High"',
      threshold: 'High',
      message: 'Red tape interference detected. Threshold defense activated. Protect The Seed.',
      lawReference: 'Law 13: Listen Before You Speak'
    };
  }

  // Red Tape Medium → Pierre Original Error Alert
  if (redTapeLevel === 'Medium') {
    return {
      systemState: 'Red_Tape_Medium',
      entityVoiceModule: 'Pierre_Original_Error_Alert',
      condition: 'Red_Tape_Detected == "Medium"',
      threshold: 'Medium',
      message: 'The Original Error is manifesting. Return to Biological Truth (Law 13).',
      lawReference: 'Law 13: Listen Before You Speak'
    };
  }

  // System Warning → Karasahin System Balance
  if (systemBalance.status === 'Warning') {
    return {
      systemState: 'Warning',
      entityVoiceModule: 'Karasahin_System_Balance',
      condition: 'System_Balance == "Warning"',
      threshold: 60, // Score 40-60
      message: 'System balance warning. Stewardship required. Return to alignment.',
      lawReference: 'Law 37: Finish What You Begin'
    };
  }

  return null;
}

/**
 * Calculate System Balance
 */
export function calculateSystemBalance(
  biologicalScore: number,
  earthRhythmScore: number,
  protocolScore: number,
  stewardshipScore: number
): SystemBalance {
  const biological = biologicalScore;
  const earthRhythm = earthRhythmScore;
  const protocol = protocolScore;
  const stewardship = stewardshipScore;

  const score = (biological + earthRhythm + protocol + stewardship) / 4;

  let status: SystemState;
  if (score >= 80) {
    status = 'Optimal';
  } else if (score >= 60) {
    status = 'Stable';
  } else if (score >= 40) {
    status = 'Warning';
  } else {
    status = 'Critical';
  }

  return {
    status,
    score,
    components: {
      biological,
      earthRhythm,
      protocol,
      stewardship
    }
  };
}

/**
 * Calculate UI Modulation
 * Solar/Lunar APIs modulate UI brightness and Command Tone based on Earth's current movement
 */
export function calculateUIModulation(
  earthAlignment: EarthAlignment
): UIModulation {
  // Brightness: Solar influence (higher during solar peak, lower at night)
  const solarInfluence = earthAlignment.solar.solarIntensity;
  const brightness = Math.round(solarInfluence); // 0-100

  // Command Tone: Lunar + Solar influence (higher during aligned phases)
  const lunarInfluence = earthAlignment.lunar.lunarIntensity;
  const commandTone = Math.round((solarInfluence * 0.6 + lunarInfluence * 0.4)); // 0-100

  // Theme: Based on solar phase
  let theme: 'dawn' | 'day' | 'dusk' | 'night';
  if (earthAlignment.solar.phase === 'sunrise') {
    theme = 'dawn';
  } else if (earthAlignment.solar.phase === 'solar_peak') {
    theme = 'day';
  } else if (earthAlignment.solar.phase === 'sunset') {
    theme = 'dusk';
  } else {
    theme = 'night';
  }

  return {
    brightness,
    commandTone,
    solarInfluence,
    lunarInfluence,
    earthAlignment,
    theme
  };
}

/**
 * Calculate Biology-Lesson Alignment
 * Biology (Data) must match Lesson (Theory)
 */
export function calculateBiologyLessonAlignment(
  biologyData: BiologicalTruthSnapshot,
  lessonTheory: string,
  threshold: number = ISS_CONSTANTS.BIOLOGY_LESSON_ALIGNMENT_THRESHOLD
): BiologyLessonAlignment {
  // Simplified alignment check (in production, would use more sophisticated matching)
  // For now, check if biological data aligns with expected lesson theory patterns
  
  let alignmentScore = 100;
  const mismatches: string[] = [];

  // Example alignment checks (would be expanded based on lesson content)
  // Check if glucose aligns with lesson theory
  if (lessonTheory.includes('glucose') && biologyData.glucose !== undefined) {
    // Theory expectations would be parsed from lesson theory
    // For now, just check if data exists
    if (biologyData.glucose === undefined || biologyData.glucose < 0) {
      alignmentScore -= 20;
      mismatches.push('Glucose data missing or invalid');
    }
  }

  // Check if Earth alignment aligns with lesson theory
  if (lessonTheory.includes('earth') || lessonTheory.includes('solar') || lessonTheory.includes('lunar')) {
    if (biologyData.earthAlignment.symbioticScore < 70) {
      alignmentScore -= 15;
      mismatches.push('Earth alignment not sufficient for lesson');
    }
  }

  // Check if vision clarity aligns with lesson theory
  if (lessonTheory.includes('vision') && biologyData.visionClarity !== undefined) {
    if (biologyData.visionClarity < 4) {
      alignmentScore -= 15;
      mismatches.push('Vision clarity below threshold for lesson');
    }
  }

  const isAligned = alignmentScore >= (threshold * 100);

  return {
    isAligned,
    alignmentScore: Math.max(0, Math.min(100, alignmentScore)),
    biologyData,
    lessonTheory,
    mismatches
  };
}

/**
 * Create Knowledge Check
 * Law 37: Finish what you begin - Each lesson requires Knowledge Check
 */
export function createKnowledgeCheck(
  lessonId: number,
  checkType: 'biology_alignment' | 'earth_alignment' | 'protocol_completion' | 'stewardship_compliance',
  requirement: string,
  solution: string | number,
  biologyData?: BiologicalTruthSnapshot,
  lessonTheory?: string
): KnowledgeCheck {
  const knowledgeCheck: KnowledgeCheck = {
    id: `knowledge_check_${lessonId}_${Date.now()}`,
    lessonId,
    type: checkType,
    requirement,
    solution,
    isPassed: false,
    timestamp: new Date().toISOString()
  };

  // If biology alignment check, calculate alignment
  if (checkType === 'biology_alignment' && biologyData && lessonTheory) {
    knowledgeCheck.biologyLessonAlignment = calculateBiologyLessonAlignment(
      biologyData,
      lessonTheory
    );
    knowledgeCheck.isPassed = knowledgeCheck.biologyLessonAlignment.isAligned;
  }

  return knowledgeCheck;
}

/**
 * Check Knowledge Check Answer
 */
export function checkKnowledgeCheckAnswer(
  knowledgeCheck: KnowledgeCheck,
  userResponse: string | number
): boolean {
  knowledgeCheck.userResponse = userResponse;

  // Compare user response with solution
  if (typeof knowledgeCheck.solution === 'number' && typeof userResponse === 'number') {
    knowledgeCheck.isPassed = Math.abs(knowledgeCheck.solution - userResponse) < 0.01;
  } else {
    knowledgeCheck.isPassed = String(knowledgeCheck.solution).toLowerCase() === String(userResponse).toLowerCase();
  }

  return knowledgeCheck.isPassed;
}

/**
 * Create Daily Stewardship Audit
 * Each day, audit stewardship compliance
 */
export function createDailyStewardshipAudit(
  date: string,
  lessonsCompleted: number,
  knowledgeChecksPassed: number,
  knowledgeChecksTotal: number,
  biologyLessonAlignment: BiologyLessonAlignment,
  stewardshipScore: number
): DailyStewardshipAudit {
  const lessonsTotal = ISS_CONSTANTS.TOTAL_LESSONS;

  // Determine audit status
  let status: 'pending' | 'in_progress' | 'completed' | 'failed';
  if (knowledgeChecksTotal === 0) {
    status = 'pending';
  } else if (knowledgeChecksPassed < knowledgeChecksTotal) {
    status = 'in_progress';
  } else if (biologyLessonAlignment.isAligned && stewardshipScore >= 70) {
    status = 'completed';
  } else {
    status = 'failed';
  }

  return {
    date,
    stewardshipScore,
    lessonsCompleted,
    lessonsTotal,
    knowledgeChecksPassed,
    knowledgeChecksTotal,
    biologyLessonAlignment,
    status
  };
}

/**
 * Check Lesson Progression
 * No progression is allowed until the 'Biology' (Data) matches the 'Lesson' (Theory)
 */
export function checkLessonProgression(
  lessonDispatcherState: LessonDispatcherState,
  biologyData: BiologicalTruthSnapshot,
  lessonTheory: string
): boolean {
  // Calculate Biology-Lesson alignment
  const alignment = calculateBiologyLessonAlignment(biologyData, lessonTheory);

  // Update lesson dispatcher state
  lessonDispatcherState.biologyLessonAlignment = alignment;
  lessonDispatcherState.canProgress = alignment.isAligned;

  return alignment.isAligned;
}

/**
 * Create Truth-Set
 * Immutable Biological Data stored for the Lord's calling
 */
export function createTruthSet(
  biologyData: BiologicalTruthSnapshot,
  earthAlignment: EarthAlignment,
  stewardshipScore: number,
  finishRate: number,
  wordIntegrity: number,
  currentLesson: number,
  lessonsCompleted: number
): TruthSet {
  return {
    id: `truth_set_${Date.now()}`,
    timestamp: new Date().toISOString(),
    biologicalTruth: biologyData,
    earthAlignment,
    stewardshipState: {
      stewardshipScore,
      finishRate,
      wordIntegrity
    },
    lessonState: {
      currentLesson,
      lessonsCompleted
    },
    immutable: true,
    storedForLordsCalling: true
  };
}

/**
 * Get Table Never Lies Constant
 */
export function getTableNeverLies(): boolean {
  return ISS_CONSTANTS.TABLE_NEVER_LIES;
}
