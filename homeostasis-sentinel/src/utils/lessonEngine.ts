/** * * LESSON ENGINE
 *  * Transform Lesson 1 into a dynamic, data-driven experience
 *  * 
 *  * Features:
 *  * - Trigger: On 'First Loop' activation, ping Symbiotic Compass
 *  * - Logic: Conditional display based on glucose threshold and sunset timing
 *  * - Compliance: Track 'Finish Rate' (Law 37)
 *  * - Storage: Store result in 'The Table' (Immutable DB)
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

import { HealthMetrics } from '../types';
import { 
  Lesson, 
  LessonState, 
  LessonCompletion, 
  LessonTrigger,
  LessonCondition,
  ConditionLogic,
  TriggerCondition,
  CompletionCriteria,
  TableEntry,
  LessonEngineState
} from '../types/lessonEngine';
import { EarthAlignment } from '../types/earthAlignment';
import { ProtocolEvent, ProtocolType } from '../types/stewardship';
import { calculateEarthAlignment, getEarthCycleTime } from './earthRhythms';
import { completeProtocol, trackProtocolCommitment } from './raconLaws';
import { parseISO, getHours, isAfter, isBefore } from 'date-fns';

/**
 * Lesson 1: First Loop Activation
 * "The Sun is setting. The War (Law 31) begins. Restore the Temple."
 */
export const LESSON_01_FIRST_LOOP: Lesson = {
  id: 'lesson_01_first_loop',
  name: 'First Loop: The War Begins',
  description: 'Dynamic lesson triggered on first loop activation, with conditional display based on glucose threshold and sunset timing.',
  trigger: {
    type: 'combined',
    conditions: [
      { type: 'loop_count', operator: '==', value: 1 }, // First loop
      { type: 'time', operator: '==', value: 'sunset' } // At sunset
    ],
    requiresSymbioticCompass: true
  },
  conditions: [
    {
      id: 'sunset_war',
      logic: {
        all: [
          { condition: { type: 'glucose', operator: '>', value: 180 } }, // Glucose > threshold
          { condition: { type: 'time', operator: '==', value: 'sunset' } } // Time == sunset
        ]
      },
      displayContent: {
        message: 'The Sun is setting. The War (Law 31) begins. Restore the Temple.',
        supportingText: 'High glucose at sunset requires immediate attention. The temple must be restored.',
        raconLawReference: 'Law 31: The War begins. Finish what you begin.',
        earthContext: 'Sunset marks the transition from solar peak to repair phase.',
        action: 'Complete loop alignment. Restore temple homeostasis.'
      }
    },
    {
      id: 'sunset_normal',
      logic: {
        all: [
          { condition: { type: 'glucose', operator: '<=', value: 180 } },
          { condition: { type: 'time', operator: '==', value: 'sunset' } }
        ]
      },
      displayContent: {
        message: 'The Sun is setting. The repair phase begins.',
        supportingText: 'Glucose is within acceptable range. Honor the Earth\'s rhythm.',
        earthContext: 'Sunset marks the transition to repair phase.',
        action: 'Complete loop alignment. Honor the symbiotic relationship.'
      }
    }
  ],
  content: {
    message: 'First Loop activated. Symbiotic Compass engaged.',
    supportingText: 'The loop honors the symbiotic relationship between Man and Earth.',
    earthContext: 'Align with Earth\'s rhythms.'
  },
  completionCriteria: {
    criteria: [
      { type: 'loop_alignment', target: 'complete', weight: 40 },
      { type: 'glucose_target', target: '<180', weight: 30 },
      { type: 'earth_alignment', target: 'synced', weight: 30 }
    ],
    minimumScore: 70
  },
  raconLaw: 'Law 37: Finish What You Begin'
};

/**
 * Check if lesson trigger conditions are met
 */
export function checkLessonTrigger(
  lesson: Lesson,
  metrics: HealthMetrics[],
  earthAlignment: EarthAlignment
): boolean {
  const trigger = lesson.trigger;
  
  if (trigger.type === 'combined') {
    // All trigger conditions must be met
    return trigger.conditions.every(condition => {
      return evaluateTriggerCondition(condition, metrics, earthAlignment);
    });
  }
  
  return false;
}

/**
 * Evaluate a single trigger condition
 */
function evaluateTriggerCondition(
  condition: TriggerCondition,
  metrics: HealthMetrics[],
  earthAlignment: EarthAlignment
): boolean {
  const latest = metrics[metrics.length - 1];
  
  switch (condition.type) {
    case 'loop_count':
      return evaluateComparison(
        latest.loop_frequency ?? 0,
        condition.operator,
        condition.value as number
      );
    
    case 'glucose':
      return evaluateComparison(
        latest.blood_glucose ?? 0,
        condition.operator,
        condition.value as number
      );
    
    case 'time':
      if (condition.value === 'sunset') {
        return earthAlignment.solar.phase === 'sunset';
      }
      if (condition.value === 'sunrise') {
        return earthAlignment.solar.phase === 'sunrise';
      }
      return false;
    
    case 'vision':
      return evaluateComparison(
        latest.vision_clarity ?? 10,
        condition.operator,
        condition.value as number
      );
    
    case 'earth_phase':
      return earthAlignment.solar.phase === condition.value;
    
    default:
      return false;
  }
}

/**
 * Evaluate comparison (>, <, ==, >=, <=)
 */
function evaluateComparison(
  actual: number,
  operator: string,
  target: number
): boolean {
  switch (operator) {
    case '>':
      return actual > target;
    case '<':
      return actual < target;
    case '==':
      return actual === target;
    case '>=':
      return actual >= target;
    case '<=':
      return actual <= target;
    default:
      return false;
  }
}

/**
 * Evaluate lesson conditions and get display content
 */
export function evaluateLessonConditions(
  lesson: Lesson,
  metrics: HealthMetrics[],
  earthAlignment: EarthAlignment
): LessonCondition | null {
  for (const condition of lesson.conditions) {
    if (evaluateConditionLogic(condition.logic, metrics, earthAlignment)) {
      return condition;
    }
  }
  
  // Return default content if no conditions match
  return null;
}

/**
 * Evaluate condition logic (AND/OR combinations)
 */
function evaluateConditionLogic(
  logic: ConditionLogic,
  metrics: HealthMetrics[],
  earthAlignment: EarthAlignment
): boolean {
  if (logic.all) {
    // All conditions must be true
    return logic.all.every(l => evaluateConditionLogic(l, metrics, earthAlignment));
  }
  
  if (logic.any) {
    // Any condition must be true
    return logic.any.some(l => evaluateConditionLogic(l, metrics, earthAlignment));
  }
  
  if (logic.condition) {
    // Single condition
    return evaluateTriggerCondition(logic.condition, metrics, earthAlignment);
  }
  
  return false;
}

/**
 * Trigger lesson on First Loop activation
 * Ping Symbiotic Compass (get Earth alignment)
 */
export function triggerFirstLoopLesson(
  metrics: HealthMetrics[],
  timestamp: string
): LessonState | null {
  const latest = metrics[metrics.length - 1];
  
  // Check if this is the first loop
  if ((latest.loop_frequency ?? 0) !== 1) {
    return null; // Not first loop
  }
  
  // Ping Symbiotic Compass (get Earth alignment)
  const earthAlignment = calculateEarthAlignment(timestamp);
  
  // Check if lesson trigger conditions are met
  const triggerMet = checkLessonTrigger(LESSON_01_FIRST_LOOP, metrics, earthAlignment);
  
  if (!triggerMet) {
    return null; // Trigger conditions not met
  }
  
  // Evaluate conditions and get display content
  const matchedCondition = evaluateLessonConditions(LESSON_01_FIRST_LOOP, metrics, earthAlignment);
  
  // Create lesson state
  const lessonState: LessonState = {
    lessonId: LESSON_01_FIRST_LOOP.id,
    isActive: true,
    wasTriggered: true,
    triggerTimestamp: timestamp,
    conditionsMet: matchedCondition ? [matchedCondition.id] : [],
    displayedContent: matchedCondition?.displayContent || LESSON_01_FIRST_LOOP.content,
    earthAlignment,
    completion: {
      isCompleted: false,
      completionScore: 0,
      finishRate: 0,
      completedRequirements: [],
      failedRequirements: []
    }
  };
  
  return lessonState;
}

/**
 * Calculate lesson completion (Law 37: Finish What You Begin)
 */
export function calculateLessonCompletion(
  lesson: Lesson,
  lessonState: LessonState,
  metrics: HealthMetrics[],
  earthAlignment: EarthAlignment
): LessonCompletion {
  const criteria = lesson.completionCriteria;
  const latest = metrics[metrics.length - 1];
  
  let completionScore = 0;
  const completedRequirements: string[] = [];
  const failedRequirements: string[] = [];
  
  // Evaluate each completion requirement
  for (const requirement of criteria.criteria) {
    let requirementMet = false;
    
    switch (requirement.type) {
      case 'loop_alignment':
        // Loop alignment complete if loop_frequency is tracked
        requirementMet = (latest.loop_frequency ?? 0) >= 1;
        break;
      
      case 'glucose_target':
        if (typeof requirement.target === 'string' && requirement.target.startsWith('<')) {
          const target = parseInt(requirement.target.substring(1));
          requirementMet = (latest.blood_glucose ?? 0) < target;
        }
        break;
      
      case 'earth_alignment':
        // Earth alignment synced if symbiotic score > 70
        requirementMet = earthAlignment.symbioticScore >= 70;
        break;
      
      case 'time_window':
        // Time window met if lesson completed within window
        if (lessonState.completion.completionTimestamp) {
          const completionTime = parseISO(lessonState.completion.completionTimestamp);
          const triggerTime = lessonState.triggerTimestamp ? parseISO(lessonState.triggerTimestamp) : null;
          
          if (triggerTime) {
            const hoursDiff = (completionTime.getTime() - triggerTime.getTime()) / (1000 * 60 * 60);
            requirementMet = hoursDiff <= (requirement.target as number);
          }
        }
        break;
    }
    
    if (requirementMet) {
      completionScore += requirement.weight;
      completedRequirements.push(requirement.type);
    } else {
      failedRequirements.push(requirement.type);
    }
  }
  
  // Calculate finish rate (Law 37 adherence)
  const finishRate = completionScore >= criteria.minimumScore ? 100 : (completionScore / criteria.minimumScore) * 100;
  const isCompleted = completionScore >= criteria.minimumScore;
  
  // Create protocol event (Law 37 tracking)
  let protocolEvent: ProtocolEvent | undefined;
  if (isCompleted) {
    protocolEvent = completeProtocol(
      trackProtocolCommitment('loop_reintegration' as ProtocolType, lessonState.triggerTimestamp || new Date().toISOString(), 90),
      new Date().toISOString()
    );
  }
  
  return {
    isCompleted,
    completionScore,
    finishRate,
    completedRequirements,
    failedRequirements,
    protocolEvent,
    ...(isCompleted && { completionTimestamp: new Date().toISOString() })
  };
}

/**
 * Complete lesson and store in The Table (Immutable DB)
 * Law 1: The Table Never Lies
 * Law 37: Finish What You Begin
 */
export function completeLessonAndStoreInTable(
  lesson: Lesson,
  lessonState: LessonState,
  metrics: HealthMetrics[],
  earthAlignment: EarthAlignment
): TableEntry {
  // Calculate completion
  const completion = calculateLessonCompletion(lesson, lessonState, metrics, earthAlignment);
  
  const latest = metrics[metrics.length - 1];
  
  // Create Table Entry (Immutable)
  const tableEntry: TableEntry = {
    id: `table_${lesson.id}_${Date.now()}`,
    timestamp: new Date().toISOString(),
    lessonId: lesson.id,
    lessonState: {
      ...lessonState,
      completion
    },
    biologicalTruth: {
      glucose: latest.blood_glucose,
      visionClarity: latest.vision_clarity,
      muscleTension: latest.muscle_tension,
      breathQuality: latest.breath_quality
    },
    earthAlignment,
    law37Compliance: completion.isCompleted,
    finishRate: completion.finishRate,
    immutable: true
  };
  
  return tableEntry;
}

/**
 * Get lesson state from The Table
 * Law 1: The Table Never Lies - entries cannot be modified
 */
export function getLessonFromTable(
  lessonId: string,
  theTable: TableEntry[]
): TableEntry[] {
  return theTable.filter(entry => entry.lessonId === lessonId);
}

/**
 * Calculate overall completion rate (Law 37 adherence)
 */
export function calculateOverallCompletionRate(
  theTable: TableEntry[]
): number {
  if (theTable.length === 0) {
    return 0;
  }
  
  const totalFinishRate = theTable.reduce((sum, entry) => sum + entry.finishRate, 0);
  return totalFinishRate / theTable.length;
}
